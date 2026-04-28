---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events-ndk
title: 订阅主线程超时事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 主线程超时事件 > 订阅主线程超时事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:07+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d8c9113744e342a5bd823ab14785fa68249ee9820e9fcb1af6a857d0507b4e94
---

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅主线程超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

1. 获取该示例工程依赖的jsoncpp文件，从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程内，目录结构如下。

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
   5. #include "hiappevent/hiappevent_event.h"
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
     7. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s",
     8. appEventGroups[i].appEventInfos[j].domain);
     9. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s",
     10. appEventGroups[i].appEventInfos[j].name);
     11. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d",
     12. appEventGroups[i].appEventInfos[j].type);
     13. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
     14. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_MAIN_THREAD_JANK) == 0) {
     15. Json::Value params;
     16. Json::Reader reader(Json::Features::strictMode());
     17. Json::FastWriter writer;
     18. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     19. auto time = params["time"].asInt64();
     20. auto pid = params["pid"].asInt();
     21. auto uid = params["uid"].asInt();
     22. auto bundleName = params["bundle_name"].asString();
     23. auto bundleVersion = params["bundle_version"].asString();
     24. auto beginTime = params["begin_time"].asInt64();
     25. auto endTime = params["end_time"].asInt64();
     26. auto externalLog = writer.write(params["external_log"]);
     27. auto logOverLimit = params["logOverLimit"].asBool();
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld", time);
     29. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", pid);
     30. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", uid);
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s",
     32. bundleName.c_str());
     33. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
     34. bundleVersion.c_str());
     35. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.begin_time=%{public}lld", beginTime);
     36. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.end_time=%{public}lld", endTime);
     37. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s", externalLog.c_str());
     38. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d",
     39. logOverLimit);
     40. }
     41. }
     42. }
     43. }
     44. }

     46. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     47. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent RegisterWatcher");
     48. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     49. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
     50. // 设置订阅的事件为EVENT_MAIN_THREAD_JANK。
     51. const char *names[] = {EVENT_MAIN_THREAD_JANK};
     52. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     53. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     54. // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive回调。
     55. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
     56. // 使观察者开始监听订阅的事件。
     57. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     58. return {};
     59. }
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
7. 编辑工程中的“entry > src > main > ets > entryability> EntryAbility.ets”文件，在onCreate()函数中新增接口调用。

   ```
   1. // 导入依赖模块
   2. import testNapi from 'libentry.so';

   4. // 在onCreate()函数中新增接口调用
   5. // 启动时，注册系统事件观察者
   6. testNapi.registerWatcher();
   ```
8. 编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，添加一个Button按钮，并在其onClick函数中模拟触发主线程超时场景，示例代码如下：

   ```
   1. Button("timeOut350")
   2. .fontSize(50)
   3. .fontWeight(FontWeight.Bold)
   4. .onClick(() => {
   5. let t = Date.now();
   6. while (Date.now() - t <= 350) {}
   7. })
   ```
9. 点击DevEco Studio界面中的运行按钮，运行应用工程，可以快速点击2~3次timeOut350按钮，以触发主线程超时事件。

### 验证观察者是否订阅到主线程超时事件

1. 主线程超时事件上报后，可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=MAIN_THREAD_JANK
   3. HiAppEvent eventInfo.eventType=1
   4. HiAppEvent eventInfo.params.time=1717597063727
   5. HiAppEvent eventInfo.params.pid=45572
   6. HiAppEvent eventInfo.params.uid=20020151
   7. HiAppEvent eventInfo.params.bundle_name=com.example.nativemainthread
   8. HiAppEvent eventInfo.params.bundle_version=1.0.0
   9. HiAppEvent eventInfo.params.begin_time=1717597063225
   10. HiAppEvent eventInfo.params.end_time=1717597063727
   11. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_20240613221239_45572.txt"]
   12. HiAppEvent eventInfo.params.log_over_limit=0
   ```

   说明

   主线程超时事件具体规格可参考：[主线程超时事件默认时间规格](apptask-timeout-guidelines.md#检测原理) 和 [主线程超时事件日志规格](apptask-timeout-guidelines.md#日志规格)。

### 移除并销毁事件观察者

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
