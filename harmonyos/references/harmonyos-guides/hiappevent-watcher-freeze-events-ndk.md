---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-ndk
title: 订阅应用冻屏事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏事件 > 订阅应用冻屏事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:237042057be30f748ee7345598d7feed27e80b75d54d905f895e3db1d1af8c44
---

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅应用冻屏事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以订阅应用冻屏事件为例，说明开发步骤。

1. 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 在DevEco Studio中，新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下。

   ```yml
   entry:
     src:
       main:
         cpp:
           json:
             - json.h
             - json-forwards.h
           types:
             libentry:
               - index.d.ts
           - CMakeLists.txt
           - jsoncpp.cpp
           - napi_init.cpp
         ets:
           entryability:
             - EntryAbility.ets
           pages:
             - Index.ets
   ```
3. 编辑工程中的“entry > src > main > cpp > CMakeLists.txt”文件，添加源文件及动态库。

   ```cmake
   # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
4. 编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG。

   ```
   #include "napi/native_api.h"
   #include "json/json.h"
   #include "hilog/log.h"
   #include "hiappevent/hiappevent.h"

   #undef LOG_TAG
   #define LOG_TAG "testTag"
   ```
5. 订阅系统事件。

   * onReceive类型观察者

     编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义onReceive类型观察者相关方法：

     ```
     // 定义一个变量，用来缓存创建的观察者的指针。
     static HiAppEvent_Watcher *systemEventWatcher;

     static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
         for (int i = 0; i < groupLen; ++i) {
             for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
                 OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
                 OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
                 OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
                 if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
                     strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_FREEZE) == 0) {
                     Json::Value params;
                     Json::Reader reader(Json::Features::strictMode());
                     Json::FastWriter writer;
                     if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
                         auto time = params["time"].asInt64();
                         auto foreground = params["foreground"].asBool();
                         auto appRunningUniqueId = params["app_running_unique_id"].asString();
                         auto bundleVersion = params["bundle_version"].asString();
                         auto bundleName = params["bundle_name"].asString();
                         auto processName = params["process_name"].asString();
                         auto pid = params["pid"].asInt();
                         auto uid = params["uid"].asInt();
                         auto uuid = params["uuid"].asString();
                         auto exception = writer.write(params["exception"]);
                         auto hilogSize = params["hilog"].size();
                         auto handleSize = params["event_handler"].size();
                         auto handleSize3s = params["event_handler_size_3s"].asString();
                         auto handleSize6s = params["event_handler_size_6s"].asString();
                         auto peerBindSize = params["peer_binder"].size();
                         auto threadSize = params["threads"].size();
                         auto memory = writer.write(params["memory"]);
                         auto externalLog = writer.write(params["external_log"]);
                         auto logOverLimit = params["log_over_limit"].asBool();
                         auto externalCallbackLog = params["external_callback_log"].asString();
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s", appRunningUniqueId.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s", uuid.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d", handleSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_3s.size=%{public}s", handleSize3s.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_6s.size=%{public}s", handleSize6s.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d", threadSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d", logOverLimit);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_callback_log=%{public}s", externalCallbackLog.c_str());
                     }
                 }
             }
         }
     }

     static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
         // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
         systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
         // 设置订阅的事件为EVENT_APP_FREEZE。
         const char *names[] = {EVENT_APP_FREEZE};
         // 开发者订阅感兴趣的事件，此处订阅了系统事件。
         OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
         // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
         OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
         // 使观察者开始监听订阅的事件。
         OH_HiAppEvent_AddWatcher(systemEventWatcher);
         return {};
     }
     ```
   * onTrigger类型观察者

     编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

     ```
     // 定义一个变量，用来缓存创建的观察者的指针。
     static HiAppEvent_Watcher *systemEventWatcher;

     // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
     static void OnTake(const char *const *events, uint32_t eventLen) {
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
                 if (domain ==  DOMAIN_OS && name == EVENT_APP_FREEZE) {
                     auto time = eventInfo["time"].asInt64();
                     auto foreground = eventInfo["foreground"].asBool();
                     auto appRunningUniqueId = eventInfo["app_running_unique_id"].asString();
                     auto bundleVersion = eventInfo["bundle_version"].asString();
                     auto bundleName = eventInfo["bundle_name"].asString();
                     auto processName = eventInfo["process_name"].asString();
                     auto pid = eventInfo["pid"].asInt();
                     auto uid = eventInfo["uid"].asInt();
                     auto uuid = eventInfo["uuid"].asString();
                     auto exception = writer.write(eventInfo["exception"]);
                     auto hilogSize = eventInfo["hilog"].size();
                     auto handleSize =  eventInfo["event_handler"].size();
                     auto handleSize3s =  eventInfo["event_handler_size_3s"].asString();
                     auto handleSize6s =  eventInfo["event_handler_size_6s"].asString();
                     auto peerBindSize =  eventInfo["peer_binder"].size();
                     auto threadSize =  eventInfo["threads"].size();
                     auto memory =  writer.write(eventInfo["memory"]);
                     auto externalLog = writer.write(eventInfo["external_log"]);
                     auto logOverLimit = eventInfo["log_over_limit"].asBool();
                     auto process_life_time = eventInfo["process_life_time"].asString();
                     auto externalCallbackLog = params["external_callback_log"].asString();
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s", appRunningUniqueId.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s", uuid.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d", handleSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_3s.size=%{public}s", handleSize3s.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_6s.size=%{public}s", handleSize6s.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d", threadSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d", logOverLimit);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_life_time=%{public}s", process_life_time.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_callback_log=%{public}s", externalCallbackLog.c_str());
                 }
             }
         }
     }

     // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     static void OnTrigger(int row, int size) {
         // 接收回调后，获取指定数量的已接收事件。
         OH_HiAppEvent_TakeWatcherData(systemEventWatcher, row, OnTake);
     }

     static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
         // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
         systemEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
         // 设置订阅的事件为EVENT_APP_FREEZE。
         const char *names[] = {EVENT_APP_FREEZE};
         // 开发者订阅感兴趣的事件，此处订阅了系统事件。
         OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
         // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
         OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcher, OnTrigger);
         // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
         OH_HiAppEvent_SetTriggerCondition(systemEventWatcher, 1, 0, 0);
         // 使观察者开始监听订阅的事件。
         OH_HiAppEvent_AddWatcher(systemEventWatcher);
         return {};
     }
     ```
6. 将RegisterWatcher注册为ArkTS接口。

   编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：

   ```
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr }
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   编辑工程中的“entry > src > main > cpp > types > libentry > Index.ets”文件，定义ArkTS接口：

   ```typescript
   export const registerWatcher: () => void;
   ```
7. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   ```typescript
   // 导入依赖模块
   import testNapi from 'libentry.so'

   // 在onCreate()函数中新增接口调用
   // 启动时，注册系统事件观察者
   testNapi.registerWatcher();
   ```
8. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发卡顿事件。

   ```typescript
   Button("appFreeze").onClick(() => {
     setTimeout(()=>{
        // 构造场景故障
        let date = Date.now();
        while (Date.now() - date < 15000) {
        };
     }, 1000)
   })
   ```
9. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreeze”，触发一次应用冻屏事件。

### 验证观察者是否订阅到应用冻屏事件

1. 应用工程崩溃退出后再次运行可以在Log窗口看到对系统事件数据的处理日志。

   ```text
   HiAppEvent eventInfo.domain=OS
   HiAppEvent eventInfo.name=APP_FREEZE
   HiAppEvent eventInfo.eventType=1
   HiAppEvent eventInfo.params.time=1502049167732
   HiAppEvent eventInfo.params.foreground=1
   HiAppEvent eventInfo.params.app_running_unique_id=382145346984526931478
   HiAppEvent eventInfo.params.bundle_version=1.0.0
   HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
   HiAppEvent eventInfo.params.process_name=com.example.myapplication
   HiAppEvent eventInfo.params.pid=1587
   HiAppEvent eventInfo.params.uid=20010043
   HiAppEvent eventInfo.params.uuid=a78a23b20f3dd9730f18a5cfa2304deac1104ac4086755c4a59cf7c72d414e2e
   HiAppEvent eventInfo.params.exception={"message":"App main thread is not response!","name":"THREAD_BLOCK_6S"}
   HiAppEvent eventInfo.params.hilog.size=6
   HiAppEvent eventInfo.params.event_handler.size=16
   HiAppEvent eventInfo.params.event_handler_3s.size=15
   HiAppEvent eventInfo.params.event_handler_6s.size=16
   HiAppEvent eventInfo.params.peer_binder.size=0
   HiAppEvent eventInfo.params.threads.size=28
   HiAppEvent eventInfo.params.memory={"pss":0,"rss":0,"sys_avail_mem":1326520,"sys_free_mem":940588,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":0}
   HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_FREEZE_1502049185239_1587.log"]
   HiAppEvent eventInfo.params.log_over_limit=0
   HiAppEvent eventInfo.params.process_life_time=18
   HiAppEvent eventInfo.params.external_callback_log=THREAD_BLOCK_3S:log3s THREAD_BLOCK_6S:log6s
   ```
2. 若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](fault-log-extension-app-events-arkts.md)回调重写的函数，进行延迟上报。

### 移除并销毁事件观察者

1. 移除事件观察者。

   ```
   static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
       // 使观察者停止监听事件
       OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
       return {};
   }
   ```
2. 销毁事件观察者。

   ```
   static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
       // 销毁创建的观察者，并置systemEventWatcher为nullptr。
       OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
       systemEventWatcher = nullptr;
       return {};
   }
   ```
