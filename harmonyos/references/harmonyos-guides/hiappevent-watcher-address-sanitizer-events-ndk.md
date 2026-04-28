---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-address-sanitizer-events-ndk
title: 订阅地址越界事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 地址越界事件 > 订阅地址越界事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:06+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:5aef14b89723e4084db2b754a9c281bbf4da969df22de05cfc772a748ca01da0
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

**订阅接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对写数组越界场景生成的地址越界事件订阅为例，说明开发步骤。

### 步骤一：新建工程

1. 参考[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)README中**Using JsonCpp in your project**介绍的使用方法获取到jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程内，目录结构如下：

   ```
   1. entry:
   2. src:
   3. main:
   4. cpp:
   5. - json:
   6. - json.h
   7. - json-forwards.h
   8. - types:
   9. libentry:
   10. - index.d.ts
   11. - CMakeLists.txt
   12. - napi_init.cpp
   13. - jsoncpp.cpp
   14. ets:
   15. - entryability:
   16. - EntryAbility.ets
   17. - pages:
   18. - Index.ets
   ```
3. 编辑"CMakeLists.txt"文件，添加源文件及动态库：

   ```
   1. # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   2. add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   3. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
4. 编辑"napi\_init.cpp"文件，导入依赖的文件，并定义LOG\_TAG：

   ```
   1. #include "napi/native_api.h"
   2. #include "json/json.h"
   3. #include "hilog/log.h"
   4. #include "hiappevent/hiappevent.h"

   6. #undef LOG_TAG
   7. #define LOG_TAG "testTag"
   ```

### 步骤二：订阅地址越界事件

1. 订阅系统事件：

   * onReceive类型观察者：

     编辑"napi\_init.cpp"文件，定义onReceive类型观察者相关方法：

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
     11. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_ADDRESS_SANITIZER) == 0) {
     12. Json::Value params;
     13. Json::Reader reader(Json::Features::strictMode());
     14. Json::FastWriter writer;
     15. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     16. auto time = params["time"].asInt64();
     17. auto bundleVersion = params["bundle_version"].asString();
     18. auto bundleName = params["bundle_name"].asString();
     19. auto pid = params["pid"].asInt();
     20. auto uid = params["uid"].asInt();
     21. auto type = params["type"].asString();
     22. std::string logOverLimit = params["log_over_limit"].asBool() ? "true" : "false";
     23. auto externalLog = writer.write(params["external_log"]);
     24. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     25. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     26. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     27. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     29. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.type=%{public}s", type.c_str());
     30. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}s", logOverLimit.c_str());
     32. }
     33. }
     34. }
     35. }
     36. }

     38. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     39. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     40. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
     41. // 设置订阅的事件为EVENT_ADDRESS_SANITIZER。
     42. const char *names[] = {EVENT_ADDRESS_SANITIZER};
     43. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     44. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     45. // 开发者设置已实现的回调函数，观察者接收到事件后回立即触发OnReceive回调。
     46. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
     47. // 使观察者开始监听订阅的事件。
     48. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     49. return {};
     50. }
     ```
   * onTrigger类型观察者：

     编辑"napi\_init.cpp"文件，定义OnTrigger类型观察者相关方法：

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
     17. if (domain ==  DOMAIN_OS && name == EVENT_ADDRESS_SANITIZER) {
     18. auto time = eventInfo["time"].asInt64();
     19. auto bundleVersion = eventInfo["bundle_version"].asString();
     20. auto bundleName = eventInfo["bundle_name"].asString();
     21. auto pid = eventInfo["pid"].asInt();
     22. auto uid = eventInfo["uid"].asInt();
     23. auto asanType = eventInfo["type"].asString();
     24. auto externalLog = writer.write(eventInfo["external_log"]);
     25. std::string logOverLimit = eventInfo["log_over_limit"].asBool() ? "true" : "false";
     26. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     27. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     29. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     30. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.crash_type=%{public}s", asanType.c_str());
     32. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     33. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}s", logOverLimit.c_str());
     34. }
     35. }
     36. }
     37. }

     39. // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     40. static void OnTrigger(int row, int size) {
     41. // 接收回调后，获取指定数量的已接收事件。
     42. OH_HiAppEvent_TakeWatcherData(systemEventWatcher, row, OnTake);
     43. }

     45. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     46. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     47. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
     48. // 设置订阅的事件为EVENT_ADDRESS_SANITIZER。
     49. const char *names[] = {EVENT_ADDRESS_SANITIZER};
     50. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     51. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     52. // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
     53. OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcher, OnTrigger);
     54. // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
     55. OH_HiAppEvent_SetTriggerCondition(systemEventWatcher, 1, 0, 0);
     56. // 使观察者开始监听订阅的事件。
     57. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     58. return {};
     59. }
     ```

### 步骤三：构造地址越界错误

1. 编辑"napi\_init.cpp"文件，定义Test方法, 方法中对一个整数数组进行越界访问：

   ```
   1. static napi_value Test(napi_env env, napi_callback_info info)
   2. {
   3. int a[10];
   4. a[10] = 1;
   5. return {};
   6. }
   ```
2. 将RegisterWatcher和Test注册为ArkTS接口，编辑"napi\_init.cpp"文件，将RegisterWatcher和Test注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. { "registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr },
   5. { "test", nullptr, Test, nullptr, nullptr, nullptr, napi_default, nullptr}
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   ```

   编辑"index.d.ts"文件，定义ArkTS接口：

   ```
   1. export const registerWatcher: () => void;
   2. export const test: () => void;
   ```
3. 编辑"EntryAbility.ets"文件，在onCreate()函数中新增接口调用：

   ```
   1. // 导入依赖模块
   2. import testNapi from 'libentry.so';

   4. // 在onCreate()函数中新增接口调用
   5. // 启动时，注册系统事件观察者
   6. testNapi.registerWatcher();
   ```
4. 编辑“entry > src > main > ets > pages > Index.ets”文件，新增按钮触发地址越界事件：

   ```
   1. import testNapi from 'libentry.so';

   3. @Entry
   4. @Component
   5. struct Index {
   6. build() {
   7. Row() {
   8. Column() {
   9. Button("address-sanitizer").onClick(() => {
   10. testNapi.test();
   11. })
   12. }
   13. .width('100%')
   14. }
   15. .height('100%')
   16. }
   17. }
   ```
5. 点击DevEco Studio界面中的“entry”，点击“Edit Configurations”，点击“Diagnostics”，勾选“Address Sanitizer”，保存设置。点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“address-sanitizer”，触发一次地址越界事件。应用崩溃后重新进入应用，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=ADDRESS_SANITIZER
   3. HiAppEvent eventInfo.eventType=1
   4. HiAppEvent eventInfo.params.time=1713148093326
   5. HiAppEvent eventInfo.params.bundle_version=1.0.0
   6. HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
   7. HiAppEvent eventInfo.params.pid=3378
   8. HiAppEvent eventInfo.params.uid=20020140
   9. HiAppEvent eventInfo.params.type="stack-buffer-overflow"
   10. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/ADDRESS_SANITIZER_1713148093326_3378.log"]
   11. HiAppEvent eventInfo.params.log_over_limit=false
   ```

### 步骤四：销毁事件观察者

1. 移除事件观察者：

   ```
   1. static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
   2. // 使观察者停止监听事件
   3. OH_HiAppEvent_RemoveWatcher(systemEventWatcher);
   4. return {};
   5. }
   ```
2. 销毁事件观察者：

   ```
   1. static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
   2. // 销毁创建的观察者，并置systemEventWatcher为nullptr。
   3. OH_HiAppEvent_DestroyWatcher(systemEventWatcher);
   4. systemEventWatcher = nullptr;
   5. return {};
   6. }
   ```
