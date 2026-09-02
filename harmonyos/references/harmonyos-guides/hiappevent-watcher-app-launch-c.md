---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-launch-c
title: 订阅启动耗时事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 启动耗时事件 > 订阅启动耗时事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:11+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:cb5a06b3fd4aa493019f838ca0d5cb816cef9dd027d01a2f159b29125a68e50c
---

## 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅启动耗时事件。详细使用说明请参考[HiAppEvent C API文档](../harmonyos-references/capi-hiappevent-h.md)。

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

1. 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README中Amalgamated source的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程，目录结构如下。

   ```text
   entry:
     src:
       main:
         cpp:
           - json:
               - json.h
               - json-forwards.h
           - types:
               libentry:
                 - index.d.ts
           - CMakeLists.txt
           - napi_init.cpp
           - jsoncpp.cpp
         ets:
           - entryability:
               - EntryAbility.ets
           - pages:
               - Index.ets
   ```
3. 在“CMakeLists.txt”文件中，添加源文件和动态库。

   ```text
   # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
4. 在“napi\_init.cpp”文件中，导入依赖文件，并定义LOG\_TAG。

   ```cpp
   #include "napi/native_api.h"
   #include "json/json.h"
   #include "hilog/log.h"
   #include "hiappevent/hiappevent.h"

   #undef LOG_TAG
   #define LOG_TAG "testTag"
   ```
5. 订阅系统事件。

   * onReceive类型观察者，在“napi\_init.cpp”文件中，定义onReceive类型观察者的方法：

   ```cpp
   static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen)
   {
       for (int i = 0; i < groupLen; ++i) {
           for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnReceive");
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
               if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) != 0 || strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_LAUNCH) != 0) {
                   continue;
               }
               Json::Value params;
               Json::Reader reader(Json::Features::strictMode());
               if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", params["time"].asInt64());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", params["bundle_version"].asString().c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", params["bundle_name"].asString().c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", params["process_name"].asString().c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.start_type=%{public}d", params["start_type"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.icon_input_time=%{public}lld", params["icon_input_time"].asInt64());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.animation_finish_time=%{public}d", params["animation_finish_time"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.extend_time=%{public}d", params["extend_time"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.response_latency=%{public}d", params["response_latency"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.laun_to_start_ability_dur=%{public}d", params["laun_to_start_ability_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.startability_processstart_dur=%{public}d", params["startability_processstart_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.processstart_to_appattach_dur=%{public}d", params["processstart_to_appattach_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.appattach_to_appforeground_dur=%{public}d", params["appattach_to_appforeground_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.startability_appforeground_dur=%{public}d", params["startability_appforeground_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.appforegr_abilityonforegr_dur=%{public}d", params["appforegr_abilityonforegr_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.abilityonforeg_startwindow_dur=%{public}d", params["abilityonforeg_startwindow_dur"].asInt());
               }
           }
       }
   }

   // 定义变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *systemEventWatcherR;

   static napi_value RegisterWatcherReceive(napi_env env, napi_callback_info info)
   {
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       systemEventWatcherR = OH_HiAppEvent_CreateWatcher("AppLaunchWatcherR");
       // 设置订阅的事件名称为EVENT_APP_LAUNCH，即启动耗时事件。
       const char *names[] = {EVENT_APP_LAUNCH};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(systemEventWatcherR, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
       OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcherR, OnReceive);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(systemEventWatcherR);
       return {};
   }
   ```

   * onTrigger类型观察者，在“napi\_init.cpp”文件中，定义OnTrigger类型观察者：

   ```cpp
   // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
   static void OnTake(const char *const *events, uint32_t eventLen)
   {
       Json::Reader reader(Json::Features::strictMode());
       Json::FastWriter writer;
       for (int i = 0; i < eventLen; ++i) {
           Json::Value eventInfo;
           if (reader.parse(events[i], eventInfo)) {
               auto domain = eventInfo["domain_"].asString();
               auto name = eventInfo["name_"].asString();
               auto type = eventInfo["type_"].asInt();
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnTrigger");
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
               OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
               if (domain == DOMAIN_OS && name == EVENT_APP_LAUNCH) {
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", eventInfo["time"].asInt64());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", eventInfo["bundle_version"].asString().c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", eventInfo["bundle_name"].asString().c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", eventInfo["process_name"].asString().c_str());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.start_type=%{public}d", eventInfo["start_type"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.icon_input_time=%{public}lld", eventInfo["icon_input_time"].asInt64());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.animation_finish_time=%{public}d", eventInfo["animation_finish_time"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.extend_time=%{public}d", eventInfo["extend_time"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.response_latency=%{public}d", eventInfo["response_latency"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.laun_to_start_ability_dur=%{public}d", eventInfo["laun_to_start_ability_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.startability_processstart_dur=%{public}d", eventInfo["startability_processstart_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.processstart_to_appattach_dur=%{public}d", eventInfo["processstart_to_appattach_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.appattach_to_appforeground_dur=%{public}d", eventInfo["appattach_to_appforeground_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.startability_appforeground_dur=%{public}d", eventInfo["startability_appforeground_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.appforegr_abilityonforegr_dur=%{public}d", eventInfo["appforegr_abilityonforegr_dur"].asInt());
                   OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.abilityonforeg_startwindow_dur=%{public}d", eventInfo["abilityonforeg_startwindow_dur"].asInt());
               }
           }
       }
   }

   // 定义变量，用来缓存创建的观察者的指针。
   static HiAppEvent_Watcher *systemEventWatcherT;

   // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
   static void OnTrigger(int row, int size)
   {
       // 接收回调后，获取指定数量的已接收事件。
       OH_HiAppEvent_TakeWatcherData(systemEventWatcherT, row, OnTake);
   }

   static napi_value RegisterWatcherTrigger(napi_env env, napi_callback_info info)
   {
       // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
       systemEventWatcherT = OH_HiAppEvent_CreateWatcher("AppLaunchWatcherT");
       // 设置订阅的事件为EVENT_APP_LAUNCH。
       const char *names[] = {EVENT_APP_LAUNCH};
       // 开发者订阅感兴趣的事件，此处订阅了系统事件。
       OH_HiAppEvent_SetAppEventFilter(systemEventWatcherT, DOMAIN_OS, 0, names, 1);
       // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
       OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcherT, OnTrigger);
       // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发OnTrigger回调。
       OH_HiAppEvent_SetTriggerCondition(systemEventWatcherT, 1, 0, 0);
       // 使观察者开始监听订阅的事件。
       OH_HiAppEvent_AddWatcher(systemEventWatcherT);
       return {};
   }
   ```
6. 将RegisterWatcher注册为ArkTS接口。

   * 在“napi\_init.cpp”文件中，将RegisterWatcher注册为ArkTS接口：

   ```cpp
   static napi_value Init(napi_env env, napi_value exports)
   {
       napi_property_descriptor desc[] = {
           { "registerWatcherReceive", nullptr, RegisterWatcherReceive, nullptr, nullptr, nullptr, napi_default, nullptr },
           { "registerWatcherTrigger", nullptr, RegisterWatcherTrigger, nullptr, nullptr, nullptr, napi_default, nullptr },
       };
       napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
       return exports;
   }
   ```

   * 在“index.d.ts”文件中，定义ArkTS接口：

   ```ts
   export const registerWatcherReceive: () => void;
   export const registerWatcherTrigger: () => void;
   ```
7. 在“EntryAbility.ets”文件的onCreate()函数中添加接口调用。

   ```ts
   // 导入依赖模块
   import testNapi from 'libentry.so';
   // 在onCreate()函数中新增接口调用
   // 启动时，注册系统事件观察者
   testNapi.registerWatcherReceive();
   testNapi.registerWatcherTrigger();
   ```
8. 点击DevEco Studio界面中的运行按钮，运行应用工程，添加系统事件订阅者，退出应用，再次点击桌面应用图标，触发一次启动耗时事件。
9. 应用工程再次启动可以在Log窗口看到对系统事件数据的处理日志。

   ```text
   HiAppEvent eventInfo.domain=OS
   HiAppEvent eventInfo.name=APP_LAUNCH
   HiAppEvent eventInfo.eventType=4
   HiAppEvent eventInfo.params.time=1780919598366
   HiAppEvent eventInfo.params.bundle_version=1.0.0
   HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
   HiAppEvent eventInfo.params.process_name=com.example.myapplication
   HiAppEvent eventInfo.params.start_type=1
   HiAppEvent eventInfo.params.icon_input_time=1780919593178
   HiAppEvent eventInfo.params.animation_finish_time=568
   HiAppEvent eventInfo.params.extend_time=0
   HiAppEvent eventInfo.params.response_latency=61
   HiAppEvent eventInfo.params.laun_to_start_ability_dur=28
   HiAppEvent eventInfo.params.startability_processstart_dur=0
   HiAppEvent eventInfo.params.processstart_to_appattach_dur=0
   HiAppEvent eventInfo.params.appattach_to_appforeground_dur=0
   HiAppEvent eventInfo.params.startability_appforeground_dur=6
   HiAppEvent eventInfo.params.appforegr_abilityonforegr_dur=2
   HiAppEvent eventInfo.params.abilityonforeg_startwindow_dur=0
   ```
