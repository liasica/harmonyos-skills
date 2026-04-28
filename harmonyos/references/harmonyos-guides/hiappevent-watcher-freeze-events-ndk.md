---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-ndk
title: 订阅应用冻屏事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏事件 > 订阅应用冻屏事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:04+08:00
doc_updated_at: 2026-04-09
content_hash: sha256:d345bb604f74652c23ea4d2f7e2cb226f4a243e4a82d481ada5a461a24442a4b
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
2. 新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下。

   ```
   1. entry:
   2. src:
   3. main:
   4. cpp:
   5. json:
   6. - json.h
   7. - json-forwards.h
   8. types:
   9. libentry:
   10. - index.d.ts
   11. - CMakeLists.txt
   12. - jsoncpp.cpp
   13. - napi_init.cpp
   14. ets:
   15. entryability:
   16. - EntryAbility.ets
   17. pages:
   18. - Index.ets
   ```
3. 编辑“CMakeLists.txt”文件，添加源文件及动态库。

   ```
   1. # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   2. add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   3. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
4. 编辑“napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG。

   ```
   1. #include "napi/native_api.h"
   2. #include "json/json.h"
   3. #include "hilog/log.h"
   4. #include "hiappevent/hiappevent.h"

   6. #undef LOG_TAG
   7. #define LOG_TAG "testTag"
   ```
5. 订阅系统事件。

   * onReceive类型观察者

     编辑“napi\_init.cpp”文件，定义onReceive类型观察者相关方法：

     ```
     1. // 定义一个变量，用来缓存创建的观察者的指针。
     2. static HiAppEvent_Watcher *systemEventWatcher;

     4. static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
     5. for (int i = 0; i < groupLen; ++i) {
     6. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
     7. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
     8. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
     9. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
     10. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
     11. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_FREEZE) == 0) {
     12. Json::Value params;
     13. Json::Reader reader(Json::Features::strictMode());
     14. Json::FastWriter writer;
     15. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     16. auto time = params["time"].asInt64();
     17. auto foreground = params["foreground"].asBool();
     18. auto bundleVersion = params["bundle_version"].asString();
     19. auto bundleName = params["bundle_name"].asString();
     20. auto processName = params["process_name"].asString();
     21. auto pid = params["pid"].asInt();
     22. auto uid = params["uid"].asInt();
     23. auto uuid = params["uuid"].asString();
     24. auto exception = writer.write(params["exception"]);
     25. auto hilogSize = params["hilog"].size();
     26. auto handleSize = params["event_handler"].size();
     27. auto handleSize3s = params["event_handler_size_3s"].asString();
     28. auto handleSize6s = params["event_handler_size_6s"].asString();
     29. auto peerBindSize = params["peer_binder"].size();
     30. auto threadSize = params["threads"].size();
     31. auto memory = writer.write(params["memory"]);
     32. auto externalLog = writer.write(params["external_log"]);
     33. auto logOverLimit = params["log_over_limit"].asBool();
     34. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     35. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
     36. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     37. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     38. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
     39. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     40. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     41. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s", uuid.c_str());
     42. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
     43. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
     44. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d", handleSize);
     45. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_3s.size=%{public}s", handleSize3s.c_str());
     46. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_6s.size=%{public}s", handleSize6s.c_str());
     47. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
     48. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d", threadSize);
     49. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
     50. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     51. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d", logOverLimit);
     52. }
     53. }
     54. }
     55. }
     56. }

     58. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     59. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     60. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
     61. // 设置订阅的事件为EVENT_APP_FREEZE。
     62. const char *names[] = {EVENT_APP_FREEZE};
     63. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     64. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     65. // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
     66. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
     67. // 使观察者开始监听订阅的事件。
     68. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     69. return {};
     70. }
     ```
   * onTrigger类型观察者

     编辑“napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

     ```
     1. // 定义一个变量，用来缓存创建的观察者的指针。
     2. static HiAppEvent_Watcher *systemEventWatcher;

     4. // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
     5. static void OnTake(const char *const *events, uint32_t eventLen) {
     6. Json::Reader reader(Json::Features::strictMode());
     7. Json::FastWriter writer;
     8. for (int i = 0; i < eventLen; ++i) {
     9. Json::Value eventInfo;
     10. if (reader.parse(events[i], eventInfo)) {
     11. auto domain =  eventInfo["domain_"].asString();
     12. auto name = eventInfo["name_"].asString();
     13. auto type = eventInfo["type_"].asInt();
     14. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
     15. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
     16. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
     17. if (domain ==  DOMAIN_OS && name == EVENT_APP_FREEZE) {
     18. auto time = eventInfo["time"].asInt64();
     19. auto foreground = eventInfo["foreground"].asBool();
     20. auto bundleVersion = eventInfo["bundle_version"].asString();
     21. auto bundleName = eventInfo["bundle_name"].asString();
     22. auto processName = eventInfo["process_name"].asString();
     23. auto pid = eventInfo["pid"].asInt();
     24. auto uid = eventInfo["uid"].asInt();
     25. auto uuid = eventInfo["uuid"].asString();
     26. auto exception = writer.write(eventInfo["exception"]);
     27. auto hilogSize = eventInfo["hilog"].size();
     28. auto handleSize =  eventInfo["event_handler"].size();
     29. auto handleSize3s =  eventInfo["event_handler_size_3s"].asString();
     30. auto handleSize6s =  eventInfo["event_handler_size_6s"].asString();
     31. auto peerBindSize =  eventInfo["peer_binder"].size();
     32. auto threadSize =  eventInfo["threads"].size();
     33. auto memory =  writer.write(eventInfo["memory"]);
     34. auto externalLog = writer.write(eventInfo["external_log"]);
     35. auto logOverLimit = eventInfo["log_over_limit"].asBool();
     36. auto process_life_time = eventInfo["process_life_time"].asString();
     37. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     38. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d", foreground);
     39. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     40. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     41. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_name=%{public}s", processName.c_str());
     42. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     43. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     44. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s", uuid.c_str());
     45. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s", exception.c_str());
     46. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d", hilogSize);
     47. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler.size=%{public}d", handleSize);
     48. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_3s.size=%{public}s", handleSize3s.c_str());
     49. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.event_handler_6s.size=%{public}s", handleSize6s.c_str());
     50. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.peer_binder.size=%{public}d", peerBindSize);
     51. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.threads.size=%{public}d", threadSize);
     52. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s", memory.c_str());
     53. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     54. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d", logOverLimit);
     55. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_life_time=%{public}s", process_life_time.c_str());
     56. }
     57. }
     58. }
     59. }

     61. // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     62. static void OnTrigger(int row, int size) {
     63. // 接收回调后，获取指定数量的已接收事件。
     64. OH_HiAppEvent_TakeWatcherData(systemEventWatcher, row, OnTake);
     65. }

     67. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     68. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     69. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
     70. // 设置订阅的事件为EVENT_APP_FREEZE。
     71. const char *names[] = {EVENT_APP_FREEZE};
     72. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     73. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     74. // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
     75. OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcher, OnTrigger);
     76. // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
     77. OH_HiAppEvent_SetTriggerCondition(systemEventWatcher, 1, 0, 0);
     78. // 使观察者开始监听订阅的事件。
     79. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     80. return {};
     81. }
     ```
6. 将RegisterWatcher注册为ArkTS接口。

   编辑“napi\_init.cpp”文件，将RegisterWatcher注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. { "registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr }
   5. };
   6. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   7. return exports;
   8. }
   ```

   编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const registerWatcher: () => void;
   ```
7. 编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   ```
   1. // 导入依赖模块
   2. import testNapi from 'libentry.so'

   4. // 在onCreate()函数中新增接口调用
   5. // 启动时，注册系统事件观察者
   6. testNapi.registerWatcher();
   ```
8. 编辑“Index.ets”文件，新增按钮触发卡顿事件。

   ```
   1. Button("appFreeze").onClick(() => {
   2. setTimeout(()=>{
   3. while(true) {}
   4. }, 1000)
   5. })
   ```
9. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreeze”，触发一次应用无响应事件。

### 验证观察者是否订阅到应用无响应事件

1. 应用工程崩溃退出后再次运行可以在Log窗口看到对系统事件数据的处理日志。

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=APP_FREEZE
   3. HiAppEvent eventInfo.eventType=1
   4. HiAppEvent eventInfo.params.time=1502049167732
   5. HiAppEvent eventInfo.params.foreground=1
   6. HiAppEvent eventInfo.params.bundle_version=1.0.0
   7. HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
   8. HiAppEvent eventInfo.params.process_name=com.example.myapplication
   9. HiAppEvent eventInfo.params.pid=1587
   10. HiAppEvent eventInfo.params.uid=20010043
   11. HiAppEvent eventInfo.params.uuid=a78a23b20f3dd9730f18a5cfa2304deac1104ac4086755c4a59cf7c72d414e2e
   12. HiAppEvent eventInfo.params.exception={"message":"App main thread is not response!","name":"THREAD_BLOCK_6S"}
   13. HiAppEvent eventInfo.params.hilog.size=6
   14. HiAppEvent eventInfo.params.event_handler.size=16
   15. HiAppEvent eventInfo.params.event_handler_3s.size=15
   16. HiAppEvent eventInfo.params.event_handler_6s.size=16
   17. HiAppEvent eventInfo.params.peer_binder.size=0
   18. HiAppEvent eventInfo.params.threads.size=28
   19. HiAppEvent eventInfo.params.memory={"pss":0,"rss":0,"sys_avail_mem":1326520,"sys_free_mem":940588,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":0}
   20. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_FREEZE_1502049185239_1587.log"]
   21. HiAppEvent eventInfo.params.log_over_limit=0
   22. HiAppEvent eventInfo.params.process_life_time=18
   ```
2. 若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](fault-log-extension-app-events-arkts.md)回调重写的函数，进行延迟上报。

### 移除并销毁事件观察者

1. 移除事件观察者。

   ```
   1. static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
   2. // 使观察者停止监听事件
   3. OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
   4. return {};
   5. }
   ```
2. 销毁事件观察者。

   ```
   1. static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
   2. // 销毁创建的观察者，并置systemEventWatcher为nullptr。
   3. OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
   4. systemEventWatcher = nullptr;
   5. return {};
   6. }
   ```
