---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-appfreezewarning-events-ndk
title: 订阅应用冻屏告警事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏告警事件 > 订阅应用冻屏告警事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:39+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:936e0f83c0737d004572f3e5d261f83c8915c5491959a9eb4e31b80f3ec556dc
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

1. 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下。

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
3. 编辑“CMakeLists.txt”文件，添加源文件及动态库。

   ```cmake
   # 新增jsoncpp.cpp（解析订阅事件中的json字符串）源文件
   add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so（日志输出）
   target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
4. 编辑“napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG。

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

     编辑“napi\_init.cpp”文件，定义onReceive类型观察者相关方法：

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
                     strcmp(appEventGroups[i].appEventInfos[j].name, OH_EVENT_APP_FREEZE_WARNING) == 0) {
                     Json::Value params;
                     Json::Reader reader(Json::Features::strictMode());
                     Json::FastWriter writer;
                     if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
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
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s", appRunningUniqueId.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version_code=%{public}d", bundle_version_code);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d", handleSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d", threadSize);
                         OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
                     }
                 }
             }
         }
     }

     static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
         // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
         systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
         // 设置订阅的事件为OH_EVENT_APP_FREEZE_WARNING。
         const char *names[] = {OH_EVENT_APP_FREEZE_WARNING};
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

     编辑“napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

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
                 if (domain ==  DOMAIN_OS && name == OH_EVENT_APP_FREEZE_WARNING) {
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
                     auto handleSize =  eventInfo["event_handler"].size();
                     auto peerBindSize =  eventInfo["peer_binder"].size();
                     auto threadSize =  eventInfo["threads"].size();
                     auto memory =  writer.write(eventInfo["memory"]);
                     auto process_life_time = eventInfo["process_life_time"].asString();
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.app_running_unique_id=%{public}s", appRunningUniqueId.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version_code=%{public}d", bundle_version_code);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d", handleSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d", threadSize);
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
                     OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_life_time=%{public}s", process_life_time.c_str());
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
         // 设置订阅的事件为OH_EVENT_APP_FREEZE_WARNING。
         const char *names[] = {OH_EVENT_APP_FREEZE_WARNING};
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

   编辑“napi\_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：

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

   编辑“index.d.ts”文件，定义ArkTS接口：

   ```ts
   export const registerWatcher: () => void;
   ```
7. 编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   ```ts
   // 导入依赖模块
   import testNapi from 'libentry.so'

   // 在onCreate()函数中新增接口调用
   // 启动时，注册系统事件观察者
   testNapi.registerWatcher();
   ```
8. 编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，新增按钮触发冻屏告警事件。示例代码如下：

   ```ts
     @Entry
     @Component
     struct Index {
       build() {
         RelativeContainer() {
           Column() {
             Button("appFreezeWarning", { stateEffect:true, type: ButtonType.Capsule})
               .width('75%')
               .height(50)
               .margin(15)
               .fontSize(20)
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                // 在按钮点击函数中构造一个appFreezeWarning场景，触发应用冻屏告警事件
                 const t = Date.now();
                 while (Date.now() - t <= 6500) {}
               })
           }.width('100%')
         }
         .height('100%')
         .width('100%')
       }
     }
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
