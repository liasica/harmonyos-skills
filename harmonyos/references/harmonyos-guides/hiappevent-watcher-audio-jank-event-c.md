---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-audio-jank-event-c
title: 订阅音频卡顿事件（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 音频卡顿事件 > 订阅音频卡顿事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:153b10ac3c89f25411828a21d9b726e7b20eb14816bbff43579f6f9397845cbd
---

## 接口说明

本文介绍如何使用HiAppEvent提供的C/C++接口订阅音频卡顿事件。详细使用说明请参考[HiAppEvent C API文档](../harmonyos-references/capi-hiappevent-h.md)。

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \*watcher) | 添加应用事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \*watcher) | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

1. 获取示例工程的依赖项jsoncpp。

   参考[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)README中**Amalgamated source**部分，获取jsoncpp.cpp、json.h和json-forwards.h三个文件。
2. 新建Native C++工程，并将上述文件导入到新建工程，目录结构如下。

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
3. 在“CMakeLists.txt”文件中，添加源文件和动态库。

   ```
   1. # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   2. add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   3. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
4. 在“napi\_init.cpp”文件中，导入依赖文件，并定义LOG\_TAG。

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

     在“napi\_init.cpp”文件中，定义onReceive类型观察者的方法：

     ```
     1. //定义变量，用来缓存创建的观察者的指针。
     2. static HiAppEvent_Watcher *systemEventWatcher;

     4. static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
     5. for (int i = 0; i < groupLen; ++i) {
     6. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
     7. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
     8. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
     9. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
     10. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) == 0 &&
     11. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_AUDIO_JANK_FRAME) == 0) {
     12. Json::Value params;
     13. Json::Reader reader(Json::Features::strictMode());
     14. Json::FastWriter writer;
     15. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
     16. auto time = params["time"].asInt64();
     17. auto bundleVersion = params["bundle_version"].asString();
     18. auto bundleName = params["bundle_name"].asString();
     19. auto faultType = params["fault_type"].asString();
     20. auto happenTime = params["happen_time"].asInt64();
     21. auto maxFrameTime = params["max_frame_time"].asInt64();

     23. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}ld", time);
     24. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     25. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     26. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.fault_type=%{public}s", faultType.c_str());
     27. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.happen_time=%{public}ld", happenTime);
     28. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.max_frame_time=%{public}ld", maxFrameTime);
     29. }
     30. }
     31. }
     32. }
     33. }

     35. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     36. // 开发者自定义观察者名称，系统根据观察者名称识别不同的观察者。
     37. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
     38. // 订阅的事件为AUDIO_JANK_FRAME。
     39. const char *names[] = {EVENT_AUDIO_JANK_FRAME};
     40. // 此处开发者订阅了系统事件AUDIO_JANK_FRAME。
     41. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     42. // 开发者通过调用OH_HiAppEvent_SetWatcherOnReceive函数设置已实现的回调函数，观察者接收到事件后会触发OnReceive回调。
     43. OH_HiAppEvent_SetWatcherOnReceive(systemEventWatcher, OnReceive);
     44. // 启动观察者以监听事件。
     45. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     46. return {};
     47. }
     ```
   * onTrigger类型观察者

     在“napi\_init.cpp”文件中，定义OnTrigger类型观察者：

     ```
     1. // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
     2. static void OnTake(const char *const *events, uint32_t eventLen) {
     3. Json::Reader reader(Json::Features::strictMode());
     4. Json::FastWriter writer;
     5. for (int i = 0; i < eventLen; ++i) {
     6. Json::Value eventInfo;
     7. if (reader.parse(events[i], eventInfo)) {
     8. auto domain =  eventInfo["domain_"].asString();
     9. auto name = eventInfo["name_"].asString();
     10. auto type = eventInfo["type_"].asInt();
     11. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
     12. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
     13. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
     14. if (domain ==  DOMAIN_OS && name == EVENT_AUDIO_JANK_FRAME) {
     15. auto time = eventInfo["time"].asInt64();
     16. auto bundleVersion = eventInfo["bundle_version"].asString();
     17. auto bundleName = eventInfo["bundle_name"].asString();
     18. auto faultType = eventInfo["fault_type"].asString();
     19. auto happenTime = eventInfo["happen_time"].asInt64();
     20. auto maxFrameTime = eventInfo["max_frame_time"].asInt64();
     21. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.time=%{public}ld", time);
     22. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_version=%{public}s", bundleVersion.c_str());
     23. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.bundle_name=%{public}s", bundleName.c_str());
     24. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.fault_type=%{public}s", faultType.c_str());
     25. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.happen_time=%{public}ld", happenTime);
     26. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.max_frame_time=%{public}ld", maxFrameTime);
     27. }
     28. }
     29. }
     30. }

     32. // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
     33. static void OnTrigger(int row, int size) {
     34. // 接收回调后，获取指定数量的已接收事件。
     35. OH_HiAppEvent_TakeWatcherData(systemEventWatcher, row, OnTake);
     36. }

     38. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
     39. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
     40. systemEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
     41. // 设置订阅的事件为EVENT_AUDIO_JANK_FRAME。
     42. const char *names[] = {EVENT_AUDIO_JANK_FRAME};

     44. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
     45. OH_HiAppEvent_SetAppEventFilter(systemEventWatcher, DOMAIN_OS, 0, names, 1);
     46. // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
     47. OH_HiAppEvent_SetWatcherOnTrigger(systemEventWatcher, OnTrigger);
     48. // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
     49. OH_HiAppEvent_SetTriggerCondition(systemEventWatcher, 1, 0, 0);
     50. // 使观察者开始监听订阅的事件。
     51. OH_HiAppEvent_AddWatcher(systemEventWatcher);
     52. return {};
     53. }
     ```
6. 将RegisterWatcher注册为ArkTS接口。

   在“napi\_init.cpp”文件中，将RegisterWatcher注册为ArkTS接口：

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

   在“index.d.ts”文件中，定义ArkTS接口：

   ```
   1. export const registerWatcher: () => void;
   ```
7. 在“EntryAbility.ets”文件的onCreate()函数中添加接口调用。

   ```
   1. // 导入依赖模块
   2. import testNapi from 'libentry.so';
   3. // 在onCreate()函数中新增接口调用
   4. // 启动时，注册系统事件观察者
   5. testNapi.registerWatcher();
   ```
8. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个模拟写入音频数据回调函数normalCallback，在该回调中模拟卡顿主动返回INVALID（不送数据）来触发卡顿故障事件。

   ```
   1. let g_invalidCount = 0;
   2. function normalCallback(buffer: ArrayBuffer) {
   3. if (g_invalidCount > 0) {
   4. g_invalidCount--;
   5. return audio.AudioDataCallbackResult.INVALID;
   6. }
   7. //在此添加写数据逻辑
   8. return audio.AudioDataCallbackResult.VALID;
   9. }
   ```
9. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加一个卡顿触发按钮，改变INVALID返回次数，模拟相应音频卡顿。

   ```
   1. Row() {
   2. Button("卡顿").onClick(async () => {
   3. g_invalidCount = 30;
   4. })
   5. }
   ```
10. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，在创建AudioRender实例时，进行耗时操作回调

    ```
    1. audio.createAudioRenderer(audioRendererOptions, (err, renderer) => { // 创建    AudioRenderer实例
    2. if (!err) {
    3. console.info(`${TAG}: creating AudioRenderer success`);
    4. this.renderModel = renderer;
    5. if (this.renderModel !== undefined) {
    6. this.renderModel.on('writeData', normalCallback);
    7. }
    8. } else {
    9. console.info(`${TAG}: creating AudioRenderer failed, error: ${err.message}`);
    10. }
    11. });
    ```
11. AudioRender正常播放时，点击卡顿按钮，即可触发耗时回调，触发音频卡顿事件。
12. 每次音频卡顿触发后，可以在Log窗口看到对系统事件数据的处理日志。

    ```
    1. HiAppEvent eventInfo.domain=OS
    2. HiAppEvent eventInfo.name=AUDIO_JANK_FRAME
    3. HiAppEvent eventInfo.eventType=1
    4. HiAppEvent eventInfo.params.time=1762739184665
    5. HiAppEvent eventInfo.params.bundle_version=1.0.0
    6. HiAppEvent eventInfo.params.bundle_name=com.samples.audio
    7. HiAppEvent eventInfo.params.fault_type=application
    8. HiAppEvent eventInfo.params.happen_time=176273918
    9. HiAppEvent eventInfo.params.max_frame_time=220
    ```
