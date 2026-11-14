---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-killed-events-ndk
title: 订阅应用终止事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用终止事件 > 订阅应用终止事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:47+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:c469ce5cc96377acc503f7d1c0cf8ba5d3cfdb702ade0ac30f303749a50800f7
---

## 应用终止事件规格说明

请参考[应用终止事件介绍](hiappevent-watcher-app-killed-events.md)。

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiAppEvent](../harmonyos-references/capi-hiappevent-h.md)。

**订阅接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

1. 获取该示例工程依赖的jsoncpp文件，打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，点击“下载当前目录”，下载EventSub工程文件。
2. 在DevEco Studio新建Native C++模板工程，并将上述文件导入到新建工程，目录结构如下。

   ```yml
   entry:
       libs:    //  放置jsoncpp关联三方库的文件夹
       src:
       main:
           cpp:
           thirdparty:
               jsoncpp:    //  放置jsoncpp关联三方库的文件夹
           types:
               libentry:
               - index.d.ts
           - CMakeLists.txt
           - napi_init.cpp
           ets:
           entryability:
               - EntryAbility.ets
           pages:
               - Index.ets
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://codeload.github.com/open-source-parsers/jsoncpp/tar.gz/refs/tags/1.9.6)。
3. 编辑工程中的“entry > src > main > cpp > CMakeLists.txt”文件，添加源文件和动态库。

   ```text
   set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   # 检查是否存在entry/build目录
   execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
       WORKING_DIRECTORY ${DEST_DIR})

   add_library(entry SHARED napi_init.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
4. 编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，导入依赖文件，并定义LOG\_TAG。

   ```
   #include "napi/native_api.h"
   // 根据工程中三方库jsoncpp的位置适配引用json.h的路径
   #include "../../../build/jsoncpp-1.9.6/include/json/json.h"
   #include "hiappevent/hiappevent.h"
   #include "hiappevent/hiappevent_param.h"
   #include "hilog/log.h"

   #undef LOG_TAG
   #define LOG_TAG "testTag"
   ```
5. 订阅系统事件。

   onReceive类型观察者：

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义onReceive类型观察者相关方法，并且新增Native内存泄漏方法：

   ```
   // 定义一变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *appKillWatcherR;

   static void HandleAppKillEventInfo(const struct HiAppEvent_AppEventInfo &appEventInfos)
   {
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventInfos.domain);
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventInfos.name);
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventInfos.type);
       if (strcmp(appEventInfos.domain, DOMAIN_OS) == 0 &&
           strcmp(appEventInfos.name, EVENT_APP_KILLED) == 0) {
           Json::Value params;
           Json::Reader reader(Json::Features::strictMode());
           Json::FastWriter writer;
           if (reader.parse(appEventInfos.params, params)) {
               auto time = params["time"].asInt64();
               auto reason = params["reason"].asString();
               auto foreground = params["foreground"].asString();
               auto callingPid = params["calling_pid"].asString();
               auto callingProcessName = params["calling_process_name"].asString();
               auto appRunningUniqueId = params["app_running_unique_id"].asString();
               auto bundleVersion = params["bundle_version"].asString();
               auto lastExitDetailInfo = writer.write(params["last_exit_detail_info"]);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.reason=%{public}s", reason.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}s", foreground.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.calling_pid=%{public}s", callingPid.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.calling_process_name=%{public}s",
                   callingProcessName.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s",
                   appRunningUniqueId.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
                   bundleVersion.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.last_exit_detail_info=%{public}s",
                   lastExitDetailInfo.c_str());
           }
       }
   }

   static void OnReceiveAppKillEvent(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups,
       uint32_t groupLen)
   {
       for (int i = 0; i < groupLen; ++i) {
           for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
               HandleAppKillEventInfo(appEventGroups[i].appEventInfos[j]);
           }
       }
   }

   static napi_value RegisterAppKillWatcher(napi_env env, napi_callback_info info)
   {
       OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent RegisterWatcher");
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       appKillWatcherR = OH_HiAppEvent_CreateWatcher("onAppKillReceiverWatcher");
       // 设置订阅的事件为EVENT_APP_KILLED。
       const char *names[] = {EVENT_APP_KILLED};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(appKillWatcherR, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
       OH_HiAppEvent_SetWatcherOnReceive(appKillWatcherR, OnReceiveAppKillEvent);
       // 使观察者开始监听订阅的事件。
       int ret = OH_HiAppEvent_AddWatcher(appKillWatcherR);
       if (ret != 0) {
           OH_LOG_ERROR(LogType::LOG_APP, "HiAppEvent AddWatcher failed, ret=%{public}d", ret);
       }
       return {};
   }
   ```
6. 实现Leak接口（仅用于故障注入及自验证，无需集成到业务逻辑中），编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，新增头文件引用：

   ```
   #include <thread>
   ```

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，新增NativeLeak和Leak方法：

   ```
   static void NativeLeak()
   {
       constexpr int leakSizePerTime = 500000;
       constexpr int sleepTimeMs = 10;
       while (true) {
           char *p = (char *)malloc(leakSizePerTime + 1);
           if (!p) {
               break;
           }
           memset(p, 'a', leakSizePerTime);
           std::this_thread::sleep_for(std::chrono::milliseconds(sleepTimeMs));
       }
   }

   static napi_value Leak(napi_env env, napi_callback_info info)
   {
       std::thread t1(NativeLeak);
       t1.detach();
       return {};
   }
   ```
7. 编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，将RegisterAppKillWatcher和Leak注册为ArkTS接口：

   ```
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           // ...
           { "registerAppKillWatcher", nullptr, RegisterAppKillWatcher, nullptr, nullptr, nullptr,
               napi_default, nullptr },
           { "leak", nullptr, Leak, nullptr, nullptr, nullptr, napi_default, nullptr},
           // ...
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   编辑工程中的“entry > src > main > cpp > types > libentry > Index.d.ts”文件，定义ArkTS接口：

   ```typescript
   export const registerAppKillWatcher: () => void;
   export const leak: () => void;
   ```
8. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate()函数中新增接口调用：

   ```typescript
   // 在onCreate()函数中新增接口调用
   // 启动时，注册系统事件观察者
   testNapi.registerAppKillWatcher();

   // 在按钮操作或者启动时，触发泄漏
   testNapi.leak();
   ```
9. 点击DevEco Studio界面中的运行按钮，运行应用工程，触发泄漏后，等待2-3分钟，应用会退出。
10. 应用被终止后，重新打开应用，会触发终止事件上报，系统会回调应用的onReceive函数，可以在Log窗口看到对系统事件数据的处理日志：

    ```text
      HiAppEvent eventInfo.domain=OS
      HiAppEvent eventInfo.name=APP_KILLED
      HiAppEvent eventInfo.eventType=2
      HiAppEvent eventInfo.params.time=1792739581978
      HiAppEvent eventInfo.params.reason="RssThresholdKiller"
      HiAppEvent eventInfo.params.foreground=true
      HiAppEvent eventInfo.params.calling_pid="43"
      HiAppEvent eventInfo.params.calling_process_name="wk:0/0/1/12"
      HiAppEvent eventInfo.params.app_running_unique_id=8778602711597370439
      HiAppEvent eventInfo.params.bundle_version=1.0.1
      HiAppEvent eventInfo.params.last_exit_detail_info={"exit_msg":"","kill_reason":"RssThresholdKiller","pid":"17248","process_name":"com.example.dfx_test","process_state":"2","pss":"227764","rss":"227764","timestamp":"1792739581947","uid":"20020207"}
    ```

    **说明** 

    根据日志报错内容，可查看具体[应用终止事件介绍](hiappevent-watcher-app-killed-events.md#事件字段说明)。
11. 移除事件观察者：

    ```
    static napi_value RemoveAppKillWatcher(napi_env env, napi_callback_info info)
    {
        // 使观察者停止监听事件
        OH_HiAppEvent_RemoveWatcher(appKillWatcherR);
        return {};
    }
    ```
12. 销毁事件观察者：

    ```
    static napi_value DestroyAppKillWatcher(napi_env env, napi_callback_info info)
    {
        // 销毁创建的观察者，并置appKillWatcherR为nullptr。
        OH_HiAppEvent_DestroyWatcher(appKillWatcherR);
        appKillWatcherR = nullptr;
        return {};
    }
    ```
