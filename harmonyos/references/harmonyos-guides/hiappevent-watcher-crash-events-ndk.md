---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events-ndk
title: 订阅崩溃事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 崩溃事件 > 订阅崩溃事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:addab6544105667fcda9c7cb66649cc35771e94024b5094bc3c9d88d1173dbb8
---

## 简介

本文介绍如何使用HiAppEvent提供的C/C++接口订阅应用崩溃事件。详细使用说明请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

说明

使用C/C++接口订阅JsError和NativeCrash崩溃事件。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

**在应用启动后，在执行业务逻辑前添加事件观察者，以确保订阅到崩溃事件。否则，应用可能因崩溃而退出，无法订阅崩溃事件。**

以用户点击按钮触发崩溃事件为例，开发步骤如下：

1. 获取该示例工程依赖的jsoncpp文件，打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，点击“下载当前目录”，下载EventSub工程文件。
2. 新建Native C++工程，并将上述文件导入到新建工程，目录结构如下。

   ```
   1. entry:
   2. libs:    //  放置jsoncpp关联三方库的文件夹
   3. src:
   4. main:
   5. cpp:
   6. - thirdparty:
   7. jsoncpp:    //  放置jsoncpp关联三方库的文件夹
   8. - types:
   9. libentry:
   10. - index.d.ts
   11. - CMakeLists.txt
   12. - napi_init.cpp
   13. ets:
   14. - entryability:
   15. - EntryAbility.ets
   16. - pages:
   17. - Index.ets
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://github.com/open-source-parsers/jsoncpp/archive/refs/tags/1.9.6.tar.gz)。
3. 在"CMakeLists.txt"文件中，添加源文件和动态库。

   ```
   1. add_library(entry SHARED napi_init.cpp)
   2. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   3. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   4. set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   5. set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   6. # 检查是否存在entry/build目录
   7. execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   8. # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   9. execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
   10. WORKING_DIRECTORY ${DEST_DIR})

   12. # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   13. target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   14. target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
4. 在"napi\_init.cpp"文件中，导入依赖文件，并定义LOG\_TAG。

   ```
   1. #include "napi/native_api.h"
   2. // 根据工程中三方库jsoncpp的位置适配引用json.h的路径
   3. #include "../../../build/jsoncpp-1.9.6/include/json/json.h"
   4. #include "hiappevent/hiappevent.h"
   5. #include "hilog/log.h"

   7. #undef LOG_TAG
   8. #define LOG_TAG "testTag"
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L24-L35)
5. 订阅系统事件。

   * onReceive类型观察者

     在"napi\_init.cpp"文件中，定义onReceive类型观察者的方法：

     ```
     1. static void OnReceiveCrashEvent(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups,
     2. uint32_t groupLen)
     3. {
     4. for (int i = 0; i < groupLen; ++i) {
     5. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
     6. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s",
     7. appEventGroups[i].appEventInfos[j].domain);
     8. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s",
     9. appEventGroups[i].appEventInfos[j].name);
     10. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d",
     11. appEventGroups[i].appEventInfos[j].type);
     12. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) != 0 ||
     13. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_CRASH) != 0) {
     14. continue;
     15. }
     16. Json::Value params;
     17. Json::Reader reader(Json::Features::strictMode());
     18. Json::FastWriter writer;
     19. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     20. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld",
     21. params["time"].asInt64());
     22. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.crash_type=%{public}s",
     23. params["crash_type"].asString().c_str());
     24. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d",
     25. params["foreground"].asBool());
     26. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
     27. params["bundle_version"].asString().c_str());
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s",
     29. params["bundle_name"].asString().c_str());
     30. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", params["pid"].asInt());
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", params["uid"].asInt());
     32. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s",
     33. params["uuid"].asString().c_str());
     34. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s",
     35. writer.write(params["exception"]).c_str());
     36. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d",
     37. params["hilog"].size());
     38. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_life_time=%{public}d",
     39. params["process_life_time"].asInt());
     40. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s",
     41. writer.write(params["memory"]).c_str());
     42. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s",
     43. writer.write(params["external_log"]).c_str());
     44. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d",
     45. params["log_over_limit"].asBool());
     46. }
     47. }
     48. }
     49. }

     51. // 定义变量，用来缓存创建的观察者的指针。
     52. static HiAppEvent_Watcher *systemEventWatcherR;

     54. static napi_value RegisterWatcherCrashEvent(napi_env env, napi_callback_info info)
     55. {
     56. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     57. systemEventWatcherR = OH_HiAppEvent_CreateWatcher("AppCrashWatcherR");
     58. // 设置订阅的事件名称为EVENT_APP_CRASH，即崩溃事件。
     59. const char *names[] = {EVENT_APP_CRASH};
     60. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     61. OH_HiAppEvent_SetAppEventFilter(systemEventWatcherR, DOMAIN_OS, 0, names, 1);
     62. // 开发者设置已实现的回调函数，观察者接收到事件后回立即触发OnReceiveCrashEvent回调。
     63. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcherR, OnReceiveCrashEvent);
     64. // 使观察者开始监听订阅的事件。
     65. OH_HiAppEvent_AddWatcher(systemEventWatcherR);
     66. return {};
     67. }
     ```
   * onTrigger类型观察者

     在"napi\_init.cpp"文件中，定义OnTrigger类型观察者：

     ```
     1. // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
     2. static void OnTakeCrash(const char *const *events, uint32_t eventLen)
     3. {
     4. Json::Reader reader(Json::Features::strictMode());
     5. Json::FastWriter writer;
     6. for (int i = 0; i < eventLen; ++i) {
     7. Json::Value eventInfo;
     8. if (reader.parse(events[i], eventInfo)) {
     9. auto domain =  eventInfo["domain_"].asString();
     10. auto name = eventInfo["name_"].asString();
     11. auto type = eventInfo["type_"].asInt();
     12. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.WatcherType=OnTrigger");
     13. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
     14. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
     15. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
     16. if (domain ==  DOMAIN_OS && name == EVENT_APP_CRASH) {
     17. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}lld",
     18. eventInfo["time"].asInt64());
     19. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.crash_type=%{public}s",
     20. eventInfo["crash_type"].asString().c_str());
     21. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.foreground=%{public}d",
     22. eventInfo["foreground"].asBool());
     23. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s",
     24. eventInfo["bundle_version"].asString().c_str());
     25. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s",
     26. eventInfo["bundle_name"].asString().c_str());
     27. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.pid=%{public}d", eventInfo["pid"].asInt());
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uid=%{public}d", eventInfo["uid"].asInt());
     29. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.uuid=%{public}s",
     30. eventInfo["uuid"].asString().c_str());
     31. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.exception=%{public}s",
     32. writer.write(eventInfo["exception"]).c_str());
     33. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.hilog.size=%{public}d",
     34. eventInfo["hilog"].size());
     35. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.process_life_time=%{public}d",
     36. eventInfo["process_life_time"].asInt());
     37. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.memory=%{public}s",
     38. writer.write(eventInfo["memory"]).c_str());
     39. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.external_log=%{public}s",
     40. writer.write(eventInfo["external_log"]).c_str());
     41. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.log_over_limit=%{public}d",
     42. eventInfo["log_over_limit"].asBool());
     43. }
     44. }
     45. }
     46. }

     48. // 定义变量，用来缓存创建的观察者的指针。
     49. static HiAppEvent_Watcher *systemEventWatcherT;

     51. // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     52. static void OnTriggerCrash(int row, int size)
     53. {
     54. // 接收回调后，获取指定数量的已接收事件。
     55. OH_HiAppEvent_TakeWatcherData(systemEventWatcherT, row, OnTakeCrash);
     56. }

     58. static napi_value RegisterWatcherClickCrash(napi_env env, napi_callback_info info)
     59. {
     60. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     61. systemEventWatcherT = OH_HiAppEvent_CreateWatcher("AppCrashWatcherT");
     62. // 设置订阅的事件为EVENT_APP_CRASH。
     63. const char *names[] = {EVENT_APP_CRASH};
     64. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     65. OH_HiAppEvent_SetAppEventFilter(systemEventWatcherT, DOMAIN_OS, 0, names, 1);
     66. // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
     67. OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcherT, OnTriggerCrash);
     68. // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发OnTriggerCrash回调。
     69. OH_HiAppEvent_SetTriggerCondition(systemEventWatcherT, 1, 0, 0);
     70. // 使观察者开始监听订阅的事件。
     71. OH_HiAppEvent_AddWatcher(systemEventWatcherT);
     72. return {};
     73. }
     ```
6. 将RegisterWatcher注册为ArkTS接口。

   在"napi\_init.cpp"文件中，将RegisterWatcher注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. // ···
   5. { "registerWatcherCrashEvent", nullptr, RegisterWatcherCrashEvent, nullptr, nullptr, nullptr, napi_default,
   6. nullptr },
   7. { "registerWatcherClickCrash", nullptr, RegisterWatcherClickCrash, nullptr, nullptr, nullptr, napi_default,
   8. nullptr },
   9. // ···
   10. };
   11. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   12. return exports;
   13. }
   ```

   在"index.d.ts"文件中，定义ArkTS接口：

   ```
   1. export const registerWatcherClickCrash: () => void;
   2. export const registerWatcherCrashEvent: () => void;
   ```
7. 在"EntryAbility.ets"文件的onCreate()函数中添加接口调用。

   ```
   1. // 在onCreate()函数中添加C API接口调用
   2. // 启动时，注册崩溃事件观察者
   3. testNapi.registerWatcherClickCrash();
   4. // 启动时，注册按钮点击事件观察者
   5. testNapi.registerWatcherCrashEvent();
   ```
8. 在"Index.ets"文件中，新增按钮触发崩溃事件。

   ```
   1. Button('JsError')
   2. .type(ButtonType.Capsule)
   3. .margin({
   4. top: 20
   5. })
   6. .backgroundColor('#0D9FFB')
   7. .width('80%')
   8. .height('5%')
   9. .onClick(() => {
   10. // 在按钮点击函数中构造一个crash场景，触发应用崩溃事件
   11. JSON.parse('');
   12. })
   ```
9. 点击运行按钮，启动应用工程。在应用界面中点击“JsError”按钮，触发崩溃事件。系统生成相应的崩溃日志并进行回调。

说明

JsError通过进程内采集故障信息触发回调，速度快。NativeCrash采取进程外采集故障信息，平均耗时约2秒，具体受业务线程数量和进程间通信影响。订阅崩溃事件后，故障信息采集完成会异步上报，不阻塞当前业务。

### 验证观察者是否订阅到崩溃事件

在应用未主动捕获崩溃异常和主动捕获崩溃异常的两种场景中，崩溃事件的回调时机不同。开发者需要在每种情况下验证是否订阅到崩溃事件。

**应用未主动捕获崩溃异常场景**

若应用未主动捕获崩溃异常，则系统处理崩溃后应用将退出。**应用下次启动时**，HiAppEvent将崩溃事件上报给已注册的监听，完成回调。

从API version 21开始，若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](fault-log-extension-app-events-arkts.md)回调重写的函数，进行延迟上报。

**应用主动捕获崩溃异常场景**

若应用主动捕获崩溃异常，HiAppEvent事件将在**应用退出前**触发回调，例如：

1. 异常处理中未主动退出的应用崩溃后不会退出。

   采用[errorManager.on](../harmonyos-references/js-apis-app-ability-errormanager.md#errormanageronerror)方法捕获异常会导致JsError类型的崩溃事件在应用退出前触发回调。若应用注册[崩溃信号](cppcrash-guidelines.md#系统处理的崩溃信号)处理函数但未主动退出，会导致NativeCrash类型的崩溃事件在应用退出前触发回调。
2. 异常处理耗时过长，会导致应用退出延迟。

在开发调试阶段，HiAppEvent上报事件完成回调后，可在DevEco Studio的HiLog窗口查看订阅的崩溃事件内容。

```
1. HiAppEvent eventInfo.domain=OS
2. HiAppEvent eventInfo.name=APP_CRASH
3. HiAppEvent eventInfo.eventType=1
4. HiAppEvent eventInfo.params.time=1503045716054
5. HiAppEvent eventInfo.params.crash_type=JsError
6. HiAppEvent eventInfo.params.foreground=1
7. HiAppEvent eventInfo.params.bundle_version=1.0.0
8. HiAppEvent eventInfo.params.bundle_name=com.samples.eventsub
9. HiAppEvent eventInfo.params.pid=2610
10. HiAppEvent eventInfo.params.uid=20010044
11. HiAppEvent eventInfo.params.uuid=7c3b1579c8ca8629af3858f8145254c2867ee402dc16ee18034337aae258620b
12. HiAppEvent eventInfo.params.exception={"message":"Unexpected Text in JSON: Empty Text","name":"SyntaxError","stack":"    at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:163:22)\n","thread_name":"amples.eventsub"}
13. HiAppEvent eventInfo.params.hilog.size=100
14. HiAppEvent eventInfo.params.process_life_time=25
15. HiAppEvent eventInfo.params.memory={"rss":181964,"sys_avail_mem":1230456,"sys_free_mem":676940,"sys_total_mem":2001932}
16. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_CRASH_1503045716408_2610.log"]
17. HiAppEvent eventInfo.params.log_over_limit=0
```

### 移除并销毁事件观察者

1. 移除事件观察者。

   ```
   1. static napi_value RemoveWatcherCrash(napi_env env, napi_callback_info info)
   2. {
   3. // 使观察者停止监听crash事件
   4. OH_HiAppEvent_RemoveWatcher(systemEventWatcherR);
   5. OH_HiAppEvent_RemoveWatcher(systemEventWatcherT);
   6. return {};
   7. }
   ```
2. 销毁事件观察者。

   ```
   1. static napi_value DestroyWatcherCrash(napi_env env, napi_callback_info info)
   2. {
   3. // 销毁创建的观察者，并置eventWatcher为nullptr。
   4. OH_HiAppEvent_DestroyWatcher(systemEventWatcherR);
   5. OH_HiAppEvent_DestroyWatcher(systemEventWatcherT);
   6. systemEventWatcherR = nullptr;
   7. systemEventWatcherT = nullptr;
   8. return {};
   9. }
   ```
