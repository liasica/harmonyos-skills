---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-apphicollie-events-ndk
title: 订阅任务执行超时事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 任务执行超时事件 > 订阅任务执行超时事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e0f8bf9121cd87078fce4f5f4b684e71511dbd9ae3141b46689e8c8e18517b1d
---

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅任务执行超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以实现对用户点击按钮触发卡顿场景生成的卡顿事件订阅为例，说明开发步骤。

1. 获取该示例工程依赖的jsoncpp文件，打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，点击“下载当前目录”，下载EventSub工程文件。
2. 在DevEco Studio中，新建Native C++工程，从解压后的EventSub工程中拷贝jsoncpp库文件（entry/libs和entry/src/main/cpp/thirdparty文件夹）到新建的工程之中，新工程目录结构如下：

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
3. 编辑工程中的“entry > src > main > cpp > CMakeLists.txt”文件，添加所需源文件及动态库。

   ```cmake
   add_library(entry SHARED napi_init.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so、libhilog_ndk.z.so（日志输出）及libohhicollie.so（hicollie检测）
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libohhicollie.so libhiappevent_ndk.z.so)

   set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   # 检查是否存在entry/build目录
   execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
       WORKING_DIRECTORY ${DEST_DIR})

   # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
4. 编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，导入依赖的头文件，并定义LOG\_TAG。

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
5. 订阅系统事件：

   * onReceive类型观察者

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义onReceive类型观察者相关函数：

   ```
   // 定义一变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *appHicollieWatcherR;
   ```

   ```
   static void OnReceiveAppHicollie(const struct HiAppEvent_AppEventGroup *appEventGroups, int i, int j)
   {
       if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
           strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_HICOLLIE) == 0) {
           Json::Value params;
           Json::Reader reader(Json::Features::strictMode());
           Json::FastWriter writer;
           if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
               auto time = params["time"].asInt64();
               auto foreground = params["foreground"].asBool();
               auto bundleVersion = params["bundle_version"].asString();
               auto processName = params["process_name"].asString();
               auto pid = params["pid"].asInt();
               auto uid = params["uid"].asInt();
               auto uuid = params["uuid"].asString();
               auto exception = writer.write(params["exception"]);
               auto hilogSize = params["hilog"].size();
               auto peerBindSize =  params["peer_binder"].size();
               auto memory =  writer.write(params["memory"]);
               auto externalLog = writer.write(params["external_log"]);
               auto logOverLimit = params["log_over_limit"].asBool();
               auto externalCallbackLog = params["external_callback_log"].asString();
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
                   bundleVersion.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s", uuid.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d", logOverLimit);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_callback_log=%{public}s",
                   externalCallbackLog.c_str());
           }
       }
   }

   static void AppHicollieOnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups,
       uint32_t groupLen)
   {
       for (int i = 0; i < groupLen; ++i) {
           for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s",
                   appEventGroups[i].appEventInfos[j].domain);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s",
                   appEventGroups[i].appEventInfos[j].name);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d",
                   appEventGroups[i].appEventInfos[j].type);
               OnReceiveAppHicollie(appEventGroups, i, j);
           }
       }
   }

   static napi_value RegisterAppHicollieWatcherR(napi_env env, napi_callback_info info)
   {
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       appHicollieWatcherR = OH_HiAppEvent_CreateWatcher("appHicollieWatcherR");
       // 设置订阅的事件为EVENT_APP_HICOLLIE。
       const char *names[] = {EVENT_APP_HICOLLIE};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(appHicollieWatcherR, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，观察者接收到事件后回立即触发OnReceive回调。
       OH_HiAppEvent_SetWatcherOnReceive(appHicollieWatcherR, AppHicollieOnReceive);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(appHicollieWatcherR);
       return {};
   }
   ```

   * onTrigger类型观察者

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义OnTrigger类型观察者相关函数：

   ```
   // 定义一变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *appHicollieWatcherT;
   ```

   ```
   // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
   static void AppHicollieOnTake(const char *const *events, uint32_t eventLen)
   {
       Json::Reader reader(Json::Features::strictMode());
       Json::FastWriter writer;
       for (int i = 0; i < eventLen; ++i) {
           Json::Value eventInfo;
           if (reader.parse(events[i], eventInfo)) {
               auto domain =  eventInfo["domain_"].asString();
               auto name = eventInfo["name_"].asString();
               auto type = eventInfo["type_"].asInt();
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
               if (domain ==  DOMAIN_OS && name == EVENT_APP_HICOLLIE) {
                   auto time = eventInfo["time"].asInt64();
                   auto foreground = eventInfo["foreground"].asBool();
                   auto bundleVersion = eventInfo["bundle_version"].asString();
                   auto processName = eventInfo["process_name"].asString();
                   auto pid = eventInfo["pid"].asInt();
                   auto uid = eventInfo["uid"].asInt();
                   auto uuid = eventInfo["uuid"].asString();
                   auto exception = writer.write(eventInfo["exception"]);
                   auto hilogSize = eventInfo["hilog"].size();
                   auto peerBindSize =  eventInfo["peer_binder"].size();
                   auto memory =  writer.write(eventInfo["memory"]);
                   auto externalLog = writer.write(eventInfo["external_log"]);
                   auto logOverLimit = eventInfo["log_over_limit"].asBool();
                   auto externalCallbackLog = eventInfo["external_callback_log"].asString();
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
                       bundleVersion.c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s",
                       processName.c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s", uuid.c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s",
                       externalLog.c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d", logOverLimit);
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_callback_log=%{public}s",
                       externalCallbackLog.c_str());
               }
           }
       }
   }

   // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
   static void AppHicollieOnTrigger(int row, int size)
   {
       // 接收回调后，获取指定数量的已接收事件。
       OH_HiAppEvent_TakeWatcherData(appHicollieWatcherT, row, AppHicollieOnTake);
   }

   static napi_value RegisterAppHicollieWatcherT(napi_env env, napi_callback_info info)
   {
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       appHicollieWatcherT = OH_HiAppEvent_CreateWatcher("appHicollieWatcherT");
       // 设置订阅的事件为EVENT_APP_HICOLLIE。
       const char *names[] = {EVENT_APP_HICOLLIE};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(appHicollieWatcherT, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
       OH_HiAppEvent_SetWatcherOnTrigger(appHicollieWatcherT, AppHicollieOnTrigger);
       // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
       OH_HiAppEvent_SetTriggerCondition(appHicollieWatcherT, 1, 0, 0);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(appHicollieWatcherT);
       return {};
   }
   ```
6. 新增TestHiCollieTimerNdk函数。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，新增TestHiCollieTimerNdk函数，构造任务执行超时事件：

   ```
   #include <unistd.h>
   #include "hicollie/hicollie.h"
   ```

   ```
   // 定义回调函数
   void CallBack(void*)
   {
       OH_LOG_INFO(LogType::LOG_APP, "HiCollieTimerNdk CallBack");  // 回调函数中打印日志
   }

   static napi_value TestHiCollieTimerNdk(napi_env env, napi_callback_info info)
   {
       int id;
       // 设置HiCollieTimer 参数（Timer任务名，超时时间，回调函数，回调函数参数，超时发生后行为）
       HiCollie_SetTimerParam param = {"testTimer", 1, CallBack, nullptr, HiCollie_Flag::HICOLLIE_FLAG_LOG};
       HiCollie_ErrorCode errorCode = OH_HiCollie_SetTimer(param, &id);  // 注册HiCollieTimer函数执行时长超时检测一次性任务
       if (errorCode == HICOLLIE_SUCCESS) {  // HiCollieTimer任务注册成功
           OH_LOG_INFO(LogType::LOG_APP, "HiCollieTimer taskId: %{public}d", id); // 打印任务id
           sleep(2);  // 模拟执行耗时函数，在这里简单的将线程阻塞2s
           OH_HiCollie_CancelTimer(id);  // 根据id取消已注册任务
       }
       return nullptr;
   }
   ```
7. 将RegisterWatcher及TestHiCollieTimerNdk注册为ArkTS接口。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，在Init函数中的desc[]数组中将TestHiCollieTimerNdk、RegisterAppHicollieWatcherR及RegisterAppHicollieWatcherT方法注册为ArkTS接口。

   ```
   // 将TestHiCollieTimerNdk注册为ArkTS接口
   { "TestHiCollieTimerNdk", nullptr, TestHiCollieTimerNdk, nullptr, nullptr, nullptr, napi_default, nullptr },
   ```

   ```
   { "RegisterAppHicollieWatcherR", nullptr, RegisterAppHicollieWatcherR, nullptr, nullptr, nullptr,
       napi_default, nullptr },
   ```

   ```
   { "RegisterAppHicollieWatcherT", nullptr, RegisterAppHicollieWatcherT, nullptr, nullptr, nullptr,
       napi_default, nullptr },
   ```

   编辑工程中的“entry > src > main > cpp > types > libentry > Index.ets”文件，定义ArkTS接口：

   ```typescript
   export const TestHiCollieTimerNdk: () => void;
   ```

   ```typescript
   export const RegisterAppHicollieWatcherR: () => void;
   ```

   ```typescript
   export const RegisterAppHicollieWatcherT: () => void;
   ```
8. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   ```typescript
   import testNapi from 'libentry.so';
   ```

   ```typescript
   // 在onCreate()函数中新增接口调用，启动时注册系统事件观察者R
   testNapi.RegisterAppHicollieWatcherR();
   ```

   ```typescript
   // 在onCreate()函数中新增接口调用，启动时注册系统事件观察者T
   testNapi.RegisterAppHicollieWatcherT();
   ```
9. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发任务执行超时事件。

   ```typescript
   import testNapi from 'libentry.so';
   ```

   编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，页面新增触发TestHiCollieTimerNdk方法的按钮。

   ```typescript
   // 添加点击事件，触发TestHiCollieTimerNdk方法。
   Button('TestHiCollieTimerNdk')
     .type(ButtonType.Capsule)
     .margin({
       top: 20
     })
     .backgroundColor('#0D9FFB')
     .width('80%')
     .height('5%')
     .onClick(() => {
       testNapi.TestHiCollieTimerNdk();
     })
   ```
10. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“TestHiCollieTimerNdk”，触发任务执行超时事件。

### 验证观察者是否订阅到任务执行超时事件

应用工程崩溃退出后再次运行可以在Log窗口看到对系统事件数据的处理日志。

```text
HiAppEvent eventInfo.domain=OS
HiAppEvent eventInfo.name=APP_HICOLLIE
HiAppEvent eventInfo.eventType=1
HiAppEvent eventInfo.params.time=1740993639620
HiAppEvent eventInfo.params.foreground=1
HiAppEvent eventInfo.params.bundle_version=1.0.0
HiAppEvent eventInfo.params.process_name=com.example.myapplication
HiAppEvent eventInfo.params.pid=26251
HiAppEvent eventInfo.params.uid=20020172
HiAppEvent eventInfo.params.uuid=4e5d7d0e18f5d6d84cf4f0c9e80d66d0b646c1cc2343d3595f07abb0d3547feb
HiAppEvent eventInfo.params.exception={"message":"","name":"APP_HICOLLIE"}
HiAppEvent eventInfo.params.hilog.size=77
HiAppEvent eventInfo.params.peer_binder.size=18
HiAppEvent eventInfo.params.memory={"pss":0,"rss":124668,"sys_avail_mem":2220032,"sys_free_mem":526680,"sys_total_mem":11692576,"vss":4238700}
HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_HICOLLIE_1740993644458_26215.log"]
HiAppEvent eventInfo.params.log_over_limit=0
HiAppEvent eventInfo.params.external_callback_log=THREAD_BLOCK_3S:log3s THREAD_BLOCK_6S:log6s
```

### 移除并销毁事件观察者

1. 移除事件观察者。

   ```
   static napi_value RemoveWatcher(napi_env env, napi_callback_info info)
   {
       // 使观察者停止监听事件
       // ···
       OH_HiAppEvent_RemoveWatcher(appHicollieWatcherR);
       OH_HiAppEvent_RemoveWatcher(appHicollieWatcherT);
       // ···
       return {};
   }
   ```
2. 销毁事件观察者。

   ```
   static napi_value DestroyWatcher(napi_env env, napi_callback_info info)
   {
       // 销毁创建的观察者，并置eventWatcher为nullptr。
       // ···
       OH_HiAppEvent_DestroyWatcher(appHicollieWatcherR);
       OH_HiAppEvent_DestroyWatcher(appHicollieWatcherT);
       appHicollieWatcherR = nullptr;
       appHicollieWatcherT = nullptr;
       // ···
       return {};
   }
   ```
