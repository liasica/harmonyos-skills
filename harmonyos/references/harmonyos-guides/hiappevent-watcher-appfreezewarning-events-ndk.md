---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-appfreezewarning-events-ndk
title: 订阅应用冻屏告警事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏告警事件 > 订阅应用冻屏告警事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-11-14T08:47:46+08:00
doc_updated_at: 2026-11-13
content_hash: sha256:231cb9cdec963a0102a24c6b3c44d00fa7e712efdf61458526d0232bb1b00177
---

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅应用冻屏告警事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以订阅应用冻屏告警事件为例，说明开发步骤。

1. 获取该示例工程依赖的jsoncpp文件，打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，点击“下载当前目录”，下载EventSub工程文件。
2. 在DevEco Studio新建Native C++模板工程，并将上述文件导入到新建工程，目录结构如下。

   ```yml
   entry:
     libs:    //  放置jsoncpp关联三方库的文件夹
     src:
       main:
         cpp:
           - thirdparty:
               jsoncpp:    //  放置jsoncpp关联三方库的文件夹
           - types:
               libentry:
                 - index.d.ts
           - CMakeLists.txt
           - napi_init.cpp
         ets:
           - entryability:
               - EntryAbility.ets
           - pages:
               - Index.ets
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://codeload.github.com/open-source-parsers/jsoncpp/tar.gz/refs/tags/1.9.6)。
3. 编辑工程中的“entry > src > main > cpp > CMakeLists.txt”文件，添加源文件及动态库。

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
4. 编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG。

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

   * onReceive类型观察者：

     编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义onReceive类型观察者相关方法：

     ```
     // 定义一个变量，用来缓存创建的观察者的指针。
     static HiAppEvent_Watcher *appFreezeWarningWatcherR;

     // OnReceiveAppFreezeWarning超出50行限制，将日志输出单独抽出
     static void AppFreezeWarningEventOutput(Json::Value params, Json::FastWriter writer)
     {
         auto time = params["time"].asInt64();
         auto foreground = params["foreground"].asBool();
         auto appRunningUniqueId = params["app_running_unique_id"].asString();
         auto bundleVersion = params["bundle_version"].asString();
         auto bundle_version_code = params["bundle_version_code"].asInt();
         auto bundleName = params["bundle_name"].asString();
         auto processName = params["process_name"].asString();
         auto pid = params["pid"].asInt();
         auto uid = params["uid"].asInt();
         auto exception = writer.write(params["exception"]);
         auto hilogSize = params["hilog"].size();
         auto handleSize = params["event_handler"].size();
         auto peerBindSize = params["peer_binder"].size();
         auto threadSize = params["threads"].size();
         auto memory = writer.write(params["memory"]);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s",
             appRunningUniqueId.c_str());
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
             bundleVersion.c_str());
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version_code=%{public}d",
             bundle_version_code);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s",
             bundleName.c_str());
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s",
             processName.c_str());
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s",
             exception.c_str());
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d",
             handleSize);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d",
             peerBindSize);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d",
             threadSize);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s",
             memory.c_str());
     }

     static void HandleAppFreezeWarningEvent(const struct HiAppEvent_AppEventInfo &appEventInfos)
     {
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventInfos.domain);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventInfos.name);
         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventInfos.type);
         if (strcmp(appEventInfos.domain, DOMAIN_OS) == 0 &&
             strcmp(appEventInfos.name, OH_EVENT_APP_FREEZE_WARNING) == 0) {
             Json::Value params;
             Json::Reader reader(Json::Features::strictMode());
             Json::FastWriter writer;
             if (reader.parse(appEventInfos.params, params)) {
                 AppFreezeWarningEventOutput(params, writer);
             }
         }
     }

     static void OnReceiveAppFreezeWarning(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups,
         uint32_t groupLen)
     {
         for (int i = 0; i < groupLen; ++i) {
             for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
                 HandleAppFreezeWarningEvent(appEventGroups[i].appEventInfos[j]);
             }
         }
     }

     static napi_value RegisterAppFreezeWarningReceiveWatcher(napi_env env, napi_callback_info info)
     {
         // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
         appFreezeWarningWatcherR = OH_HiAppEvent_CreateWatcher("onAppFreezeWarningReceiverWatcher");
         // 设置订阅的事件为OH_EVENT_APP_FREEZE_WARNING。
         const char *names[] = {OH_EVENT_APP_FREEZE_WARNING};
         // 开发者订阅感兴趣的事件，此处订阅了系统事件。
         OH_HiAppEvent_SetAppEventFilter(appFreezeWarningWatcherR, DOMAIN_OS, 0, names, 1);
         // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
         OH_HiAppEvent_SetWatcherOnReceive(appFreezeWarningWatcherR, OnReceiveAppFreezeWarning);
         // 使观察者开始监听订阅的事件。
         OH_HiAppEvent_AddWatcher(appFreezeWarningWatcherR);
         return {};
     }
     ```
   * onTrigger类型观察者：

     编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

     ```
     // 定义一个变量，用来缓存创建的观察者的指针。
     static HiAppEvent_Watcher *appFreezeWarningWatcherT;

     // OnTakeAppFreezeWarning超出50行限制，将日志输出单独抽出
     static void OnAppFreezeWarningEventOutPut(std::string domain, std::string name, Json::Value eventInfo,
         Json::FastWriter writer)
     {
         if (domain == DOMAIN_OS && name == OH_EVENT_APP_FREEZE_WARNING) {
             auto time = eventInfo["time"].asInt64();
             auto foreground = eventInfo["foreground"].asBool();
             auto appRunningUniqueId = eventInfo["app_running_unique_id"].asString();
             auto bundleVersion = eventInfo["bundle_version"].asString();
             auto bundle_version_code = eventInfo["bundle_version_code"].asInt();
             auto bundleName = eventInfo["bundle_name"].asString();
             auto processName = eventInfo["process_name"].asString();
             auto pid = eventInfo["pid"].asInt();
             auto uid = eventInfo["uid"].asInt();
             auto exception = writer.write(eventInfo["exception"]);
             auto hilogSize = eventInfo["hilog"].size();
             auto handleSize = eventInfo["event_handler"].size();
             auto peerBindSize = eventInfo["peer_binder"].size();
             auto threadSize = eventInfo["threads"].size();
             auto memory = writer.write(eventInfo["memory"]);
             auto process_life_time = eventInfo["process_life_time"].asString();
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s",
                 appRunningUniqueId.c_str());
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
                 bundleVersion.c_str());
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version_code=%{public}d",
                 bundle_version_code);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s",
                 bundleName.c_str());
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s",
                 processName.c_str());
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s",
                 exception.c_str());
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d",
                 handleSize);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d",
                 peerBindSize);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d",
                 threadSize);
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s",
                 memory.c_str());
             OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_life_time=%{public}s",
                 process_life_time.c_str());
         }
     }

     // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
     static void OnTakeAppFreezeWarning(const char *const *events, uint32_t eventLen)
     {
         Json::Reader reader(Json::Features::strictMode());
         Json::FastWriter writer;
         for (int i = 0; i < eventLen; ++i) {
             Json::Value eventInfo;
             if (reader.parse(events[i], eventInfo)) {
                 auto domain = eventInfo["domain_"].asString();
                 auto name = eventInfo["name_"].asString();
                 auto type = eventInfo["type_"].asInt();
                 OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
                 OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
                 OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
                 // 处理应用冻屏告警事件
                 OnAppFreezeWarningEventOutPut(domain, name, eventInfo, writer);
             }
         }
     }

     // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     static void OnTriggerAppFreezeWarning(int row, int size)
     {
         // 接收回调后，获取指定数量的已接收事件。
         OH_HiAppEvent_TakeWatcherData(appFreezeWarningWatcherT, row, OnTakeAppFreezeWarning);
     }

     static napi_value RegisterAppFreezeWarningTriggerWatcher(napi_env env, napi_callback_info info)
     {
         // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
         appFreezeWarningWatcherT = OH_HiAppEvent_CreateWatcher("onAppFreezeWarningTriggerWatcher");
         // 设置订阅的事件为OH_EVENT_APP_FREEZE_WARNING。
         const char *names[] = {OH_EVENT_APP_FREEZE_WARNING};
         // 开发者订阅感兴趣的事件，此处订阅了系统事件。
         OH_HiAppEvent_SetAppEventFilter(appFreezeWarningWatcherT, DOMAIN_OS, 0, names, 1);
         // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
         OH_HiAppEvent_SetWatcherOnTrigger(appFreezeWarningWatcherT, OnTriggerAppFreezeWarning);
         // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
         OH_HiAppEvent_SetTriggerCondition(appFreezeWarningWatcherT, 1, 0, 0);
         // 使观察者开始监听订阅的事件。
         OH_HiAppEvent_AddWatcher(appFreezeWarningWatcherT);
         return {};
     }
     ```
6. 将RegisterWatcher注册为ArkTS接口。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，将RegisterAppFreezeWarningReceiveWatcher和RegisterAppFreezeWarningTriggerWatcher注册为ArkTS接口：

   ```
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           // ...
           { "registerAppFreezeWarningReceiveWatcher", nullptr, RegisterAppFreezeWarningReceiveWatcher,
               nullptr, nullptr, nullptr, napi_default, nullptr },
           { "registerAppFreezeWarningTriggerWatcher", nullptr, RegisterAppFreezeWarningTriggerWatcher,
               nullptr, nullptr, nullptr, napi_default, nullptr },
           // ...
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   编辑工程中的“entry > src > main > cpp > types > libentry > Index.d.ts”文件，定义ArkTS接口：

   ```typescript
   export const registerAppFreezeWarningReceiveWatcher: () => void;
   export const registerAppFreezeWarningTriggerWatcher: () => void;
   ```
7. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   ```typescript
   // 在onCreate()函数中新增接口调用
   // 启动时，注册系统事件观察者
   testNapi.registerAppFreezeWarningReceiveWatcher();
   testNapi.registerAppFreezeWarningTriggerWatcher();
   ```
8. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发冻屏告警事件。示例代码如下：

   ```typescript
   Button("appFreezeWarning")
     .type(ButtonType.Capsule)
     .margin({
       top: 20
     })
     .backgroundColor('#0D9FFB')
     .width('80%')
     .height('5%')
     .onClick(() => {
       // 在按钮点击函数中构造一个appFreezeWarning场景，触发应用冻屏告警事件
       const t = Date.now();
       while (Date.now() - t <= 6500) {}
     })
   ```
9. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreezeWarning”，触发一次应用冻屏告警事件。

### 验证观察者是否订阅到应用冻屏告警事件

等待约一分钟后，可以在Log窗口看到对系统事件数据的处理日志。

```text
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APPFREEZE_WARNING
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1776946769389
HiAppEvent eventInfo.params.foreground=1
HiAppEvent eventInfo.params.app_running_unique_id=382145346984526931478
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.bundle_version_code=1000000
HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=1587
HiAppEvent eventInfo.params.uid=20010043
HiAppEvent eventInfo.params.exception={""message":"App main thread is not response!Main handler dump start time: 2026-04-23 20:19:28.903","name":"THREAD_BLOCK_3S"}
HiAppEvent eventInfo.params.hilog.size=6
HiAppEvent eventInfo.params.event_handler.size=16
HiAppEvent eventInfo.params.peer_binder.size=0
HiAppEvent eventInfo.params.threads.size=28
HiAppEvent eventInfo.params.memory={"rss":161080,"sys_avail_mem":1361464,"sys_free_mem":796232,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":56960692}
HiAppEvent eventInfo.params.process_life_time=18
```

### 移除并销毁事件观察者

1. 移除事件观察者。

   ```
   static napi_value RemoveAppFreezeWarningWatcher(napi_env env, napi_callback_info info)
   {
       // 使观察者停止监听事件
       OH_HiAppEvent_RemoveWatcher(appFreezeWarningWatcherR);
       OH_HiAppEvent_RemoveWatcher(appFreezeWarningWatcherT);
       return {};
   }
   ```
2. 销毁事件观察者。

   ```
   static napi_value DestroyAppFreezeWarningWatcher(napi_env env, napi_callback_info info)
   {
       // 销毁创建的观察者，并置systemEventWatcher为nullptr。
       OH_HiAppEvent_DestroyWatcher(appFreezeWarningWatcherR);
       OH_HiAppEvent_DestroyWatcher(appFreezeWarningWatcherT);
       appFreezeWarningWatcherR = nullptr;
       appFreezeWarningWatcherT = nullptr;
       return {};
   }
   ```
