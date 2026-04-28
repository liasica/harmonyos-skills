---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-app-events-ndk
title: 事件订阅（C/C++）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 事件订阅（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3cd616eb990be5da5ecafd995ee91b23049937a9f77ba9adcfa2daa7b63fde46
---

HiAppEvent提供了事件订阅接口，用于订阅并接收应用产生的事件。

## 接口说明

API接口的使用说明，包括参数使用限制和取值范围，请参考[hiappevent.h](../harmonyos-references/capi-hiappevent-h.md)。

**订阅接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher\* watcher) | 添加应用的事件观察者。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher\* watcher) | 移除应用的事件观察者。 |

**打点接口功能介绍**：

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_Write(const char\* domain, const char\* name, enum EventType type, const ParamList list) | 实现对参数为列表类型的应用事件打点。 |

## 事件订阅开发指导

以订阅崩溃事件（系统事件）和按钮点击事件（应用事件）为例，说明开发步骤。

### 步骤一：新建工程及编译配置

1. 将示例工程依赖的jsoncpp库文件复制到新建工程中。

   打开链接[HiAppEvent示例工程EventSub](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/PerformanceAnalysisKit/HiAppEvent/EventSub)，并点击“下载当前目录”，下载EventSub工程文件。

   新建一个Native C++工程。从解压后的EventSub文件夹中拷贝jsoncpp库文件（entry/libs和entry/src/main/cpp/thirdparty整个目录）到新建的工程中，得到的目录结构如下：

   ```
   1. entry
   2. ├── libs        // 自行创建文件夹,放入相关的三方库
   3. └── src
   4. ├── main
   5. │   ├── cpp
   6. │   │   ├── CMakeLists.txt       // 导入so链接
   7. │   │   ├── napi_init.cpp        // 功能函数，观察者定义
   8. │   │   ├── thirdparty    // 自行创建文件夹,放入相关的三方库
   9. │   │   │   └── jsoncpp
   10. │   │   └── types
   11. │   │       └── libentry
   12. │   │           ├── Index.d.ts        // 定义ArkTS接口
   13. │   │           └── oh-package.json5
   14. │   ├── ets
   15. │   │   ├── entryability
   16. │   │   │   └── EntryAbility.ets    // 新增接口调用
   17. │   │   ├── entrybackupability
   18. │   │   │   └── EntryBackupAbility.ets
   19. │   │   └── pages
   20. │   │       └── Index.ets        // 主页
   ```

   该示例工程中jsoncpp库文件对应的源码来自[三方开源库jsoncpp](https://github.com/open-source-parsers/jsoncpp/archive/refs/tags/1.9.6.tar.gz)。
2. 编辑“CMakeLists.txt”文件，添加所需的源文件和动态库。

   ```
   1. set(GZ_FILE "${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/src/jsoncpp-1.9.6.tar.gz")
   2. set(DEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../build")
   3. # 检查是否存在entry/build目录
   4. execute_process(COMMAND ${CMAKE_COMMAND} -E make_directory ${DEST_DIR})
   5. # 解压jsoncpp-1.9.6.tar.gz到entry/build，得到jsoncpp头文件的目录
   6. execute_process(COMMAND tar -xzf ${GZ_FILE} -C ${DEST_DIR}
   7. WORKING_DIRECTORY ${DEST_DIR})

   9. add_library(entry SHARED napi_init.cpp)
   10. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   11. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   12. # 新增三方库依赖libjsoncpp.so(解析订阅事件中的json字符串)
   13. target_link_libraries(entry PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/thirdparty/jsoncpp/${OHOS_ARCH}/lib/libjsoncpp.so)
   14. target_include_directories(entry PRIVATE ${DEST_DIR}/jsoncpp-1.9.6/include/json)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖的文件并定义LOG\_TAG：

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

### 步骤二：订阅事件

1. 订阅事件。分别使用OnReceive类型观察者、OnTrigger类型观察者的订阅方式。

   * 订阅崩溃事件（系统事件），采用OnReceive类型观察者的订阅方式，观察者接收到事件后会立即触发OnReceive()回调。编辑“napi\_init.cpp”文件，定义OnReceive类型观察者相关方法：

   ```
   1. // 定义变量，用来缓存创建的观察者的指针。
   2. static HiAppEvent_Watcher *eventWatcherR1;

   4. static void OnReceive1(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen)
   5. {
   6. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent success to read events with onReceive callback from C API \n");
   7. for (int i = 0; i < groupLen; ++i) {
   8. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
   9. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.domain=%{public}s",
   10. appEventGroups[i].appEventInfos[j].domain);
   11. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.name=%{public}s",
   12. appEventGroups[i].appEventInfos[j].name);
   13. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.eventType=%{public}d",
   14. appEventGroups[i].appEventInfos[j].type);
   15. if (strcmp(appEventGroups[i].appEventInfos[j].domain, DOMAIN_OS) != 0 ||
   16. strcmp(appEventGroups[i].appEventInfos[j].name, EVENT_APP_CRASH) != 0) {
   17. continue;
   18. }
   19. Json::Value params;
   20. Json::Reader reader(Json::Features::strictMode());
   21. Json::FastWriter writer;
   22. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
   23. // 开发者可以获取到崩溃事件发生的时间戳
   24. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.time=%{public}lld",
   25. params["time"].asInt64());
   26. // 开发者可以获取到崩溃应用的包名
   27. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.bundle_name=%{public}s",
   28. params["bundle_name"].asString().c_str());
   29. auto external_log = writer.write(params["external_log"]);
   30. // 开发者可以获取到崩溃事件发生时的故障日志文件
   31. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.external_log=%{public}s",
   32. external_log.c_str());
   33. }
   34. }
   35. }
   36. }
   37. static napi_value RegisterWatcherCrash(napi_env env, napi_callback_info info)
   38. {
   39. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
   40. eventWatcherR1 = OH_HiAppEvent_CreateWatcher("AppCrashWatcher1");
   41. // 设置订阅的事件名称为EVENT_APP_CRASH，即崩溃事件。
   42. const char *names[] = {EVENT_APP_CRASH};
   43. // 开发者订阅感兴趣的事件，此处订阅了系统事件。
   44. OH_HiAppEvent_SetAppEventFilter(eventWatcherR1, DOMAIN_OS, 0, names, 1);
   45. // 开发者设置已实现的回调函数，观察者接收到事件后会立即触发OnReceive1回调。
   46. OH_HiAppEvent_SetWatcherOnReceive(eventWatcherR1, OnReceive1);
   47. // 使观察者开始监听订阅的事件。
   48. OH_HiAppEvent_AddWatcher(eventWatcherR1);
   49. return {};
   50. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L388-L439)

   * 订阅按钮点击事件（应用事件），采用OnTrigger类型观察者的订阅方式。需满足OH\_HiAppEvent\_SetTriggerCondition()设置的条件，才能触发OnTrigger()回调。编辑 “napi\_init.cpp”文件，定义OnTrigger类型观察者相关方法：

   ```
   1. // 定义变量，用来缓存创建的观察者的指针。
   2. static HiAppEvent_Watcher *eventWatcherT1;
   3. // 开发者可以自行实现获取已监听到事件的回调函数，其中events指针指向内容仅在该函数内有效。
   4. static void OnTake1(const char *const *events, uint32_t eventLen)
   5. {
   6. Json::Reader reader(Json::Features::strictMode());
   7. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent success to read events with onTrigger callback from C API \n");
   8. for (int i = 0; i < eventLen; ++i) {
   9. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo=%{public}s", events[i]);
   10. Json::Value eventInfo;
   11. if (reader.parse(events[i], eventInfo)) {
   12. auto domain = eventInfo["domain_"].asString();
   13. auto name = eventInfo["name_"].asString();
   14. auto type = eventInfo["type_"].asInt();
   15. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
   16. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.name=%{public}s", name.c_str());
   17. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.eventType=%{public}d", type);
   18. if (domain == "button" && name == "click") {
   19. auto clickTime = eventInfo["clickTime"].asInt64();
   20. OH_LOG_INFO(LogType::LOG_APP, "AppEvents HiAppEvent eventInfo.params.clickTime=%{public}lld",
   21. clickTime);
   22. }
   23. }
   24. }
   25. }

   27. // 开发者可以自行实现订阅回调函数，以便对获取到的事件打点数据进行自定义处理。
   28. static void OnTrigger1(int row, int size)
   29. {
   30. // 接收回调后，获取指定数量的已接收事件。
   31. OH_HiAppEvent_TakeWatcherData(eventWatcherT1, row, OnTake1);
   32. }

   34. static napi_value RegisterWatcherClick(napi_env env, napi_callback_info info)
   35. {
   36. // 开发者自定义观察者名称，系统根据不同的名称来识别不同的观察者。
   37. eventWatcherT1 = OH_HiAppEvent_CreateWatcher("ButtonClickWatcher1");
   38. // 设置订阅的事件名称为click。
   39. const char *names[] = {"click"};
   40. // 开发者订阅感兴趣的应用事件，此处订阅了button相关事件。
   41. OH_HiAppEvent_SetAppEventFilter(eventWatcherT1, "button", 0, names, 1);
   42. // 开发者设置已实现的回调函数，需OH_HiAppEvent_SetTriggerCondition设置的条件满足方可触发。
   43. OH_HiAppEvent_SetWatcherOnTrigger(eventWatcherT1, OnTrigger1);
   44. // 开发者可以设置订阅触发回调的条件，此处是设置新增事件打点数量为1个时，触发onTrigger回调。
   45. OH_HiAppEvent_SetTriggerCondition(eventWatcherT1, 1, 0, 0);
   46. // 使观察者开始监听订阅的事件。
   47. OH_HiAppEvent_AddWatcher(eventWatcherT1);
   48. return {};
   49. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L440-L490)
2. 编辑“napi\_init.cpp”文件，添加按钮点击事件的打点接口：

   ```
   1. static napi_value WriteAppEvent(napi_env env, napi_callback_info info)
   2. {
   3. auto params = OH_HiAppEvent_CreateParamList();
   4. OH_HiAppEvent_AddInt64Param(params, "clickTime", time(nullptr));
   5. OH_HiAppEvent_Write("button", "click", EventType::BEHAVIOR, params);
   6. OH_HiAppEvent_DestroyParamList(params);
   7. OH_LOG_INFO(LogType::LOG_APP, "writeEvent C++ success");
   8. return {};
   9. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L899-L909)
3. 编辑“napi\_init.cpp”文件，注册RegisterWatcherCrash()(订阅崩溃事件)、RegisterWatcherClick()（订阅按钮点击事件）、WriteAppEvent()(按钮点击事件打点接口)为ArkTS接口：

   ```
   1. // ...

   3. static napi_value Init(napi_env env, napi_value exports)
   4. {
   5. napi_property_descriptor desc[] = {
   6. // ...
   7. { "registerWatcherCrash", nullptr, RegisterWatcherCrash, nullptr, nullptr, nullptr, napi_default, nullptr },
   8. { "registerWatcherClick", nullptr, RegisterWatcherClick, nullptr, nullptr, nullptr, napi_default, nullptr },
   9. { "writeAppEvent", nullptr, WriteAppEvent, nullptr, nullptr, nullptr, napi_default, nullptr },
   10. // ...
   11. };
   12. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   13. return exports;
   14. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L946-L1298)
4. 编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const registerWatcherCrash: () => void;
   2. export const registerWatcherClick: () => void;
   3. export const writeAppEvent: () => void;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/types/libentry/Index.d.ts#L18-L22)
5. 编辑“EntryAbility.ets”文件，在onCreate()函数中添加接口调用：

   ```
   1. import testNapi from 'libentry.so';
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/entryability/EntryAbility.ets#L27-L29)

   ```
   1. // 在onCreate()函数中添加C API接口调用
   2. // 启动时，注册崩溃事件观察者
   3. testNapi.registerWatcherCrash();
   4. // 启动时，注册按钮点击事件观察者
   5. testNapi.registerWatcherClick();
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/entryability/EntryAbility.ets#L399-L405)

### 步骤三：触发事件

编辑“Index.ets”文件，新增“WatchAppCrash ArkTS&C++”按钮以触发崩溃事件；新增“writeEvent C++”按钮，在按钮点击函数中进行事件打点。示例代码如下：

```
1. import testNapi from 'libentry.so';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/pages/Index.ets#L21-L23)

```
1. Button('WatchAppCrash ArkTS&C++')
2. .type(ButtonType.Capsule)
3. .margin({
4. top: 20
5. })
6. .backgroundColor('#0D9FFB')
7. .width('80%')
8. .height('5%')
9. .onClick(() => {
10. // 在按钮点击函数中构造一个crash场景，触发崩溃事件
11. let result: object = JSON.parse('');
12. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/pages/Index.ets#L35-L48)

```
1. Button('writeEvent C++')
2. .type(ButtonType.Capsule)
3. .margin({
4. top: 20
5. })
6. .backgroundColor('#0D9FFB')
7. .width('80%')
8. .height('5%')
9. .onClick(() => {
10. testNapi.writeAppEvent();
11. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/pages/Index.ets#L158-L170)

## 调测验证

1. 点击DevEco Studio界面中的运行按钮，运行应用工程。在应用界面中点击“WatchAppCrash ArkTS&C++”按钮，触发崩溃事件。应用退出后重新打开应用。
2. 搜索关键字“AppEvents”，在HiLog窗口查看应用处理崩溃事件数据的日志：

   ```
   1. AppEvents HiAppEvent success to read events with onReceive callback from C API
   2. AppEvents HiAppEvent eventInfo.domain=OS
   3. AppEvents HiAppEvent eventInfo.name=APP_CRASH
   4. AppEvents HiAppEvent eventInfo.eventType=1
   5. AppEvents HiAppEvent eventInfo.params.time=1750946685473
   6. AppEvents HiAppEvent eventInfo.params.bundle_name=com.example.cxxxx
   7. AppEvents HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_CRASH_1750946685805_64003.log"]
   ```
3. 点击“writeEvent C++”按钮，触发按钮点击事件。搜索关键字“AppEvents”，在HiLog窗口查看应用处理按钮点击事件数据的日志：

   ```
   1. AppEvents HiAppEvent success to read events with onTrigger callback from C API
   2. AppEvents HiAppEvent eventInfo={"domain_":"button","name_":"click","type_":4,"time_":1750947007108,"tz_":"","pid_":64750,"tid_":64750,"clickTime":1750947007}
   3. AppEvents HiAppEvent eventInfo.domain=button
   4. AppEvents HiAppEvent eventInfo.name=click
   5. AppEvents HiAppEvent eventInfo.eventType=4
   6. AppEvents HiAppEvent eventInfo.params.clickTime=1750947007
   ```
4. 移除应用的事件观察者：

   ```
   1. static napi_value RemoveWatcher(napi_env env, napi_callback_info info)
   2. {
   3. // 使观察者停止监听事件
   4. // ...
   5. OH_HiAppEvent_RemoveWatcher(eventWatcherT1);
   6. OH_HiAppEvent_RemoveWatcher(eventWatcherR1);
   7. // ...
   8. return {};
   9. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L801-L842)
5. 销毁应用的事件观察者：

   ```
   1. static napi_value DestroyWatcher(napi_env env, napi_callback_info info)
   2. {
   3. // 销毁创建的观察者，并置eventWatcher为nullptr。
   4. // ...
   5. OH_HiAppEvent_DestroyWatcher(eventWatcherT1);
   6. OH_HiAppEvent_DestroyWatcher(eventWatcherR1);
   7. eventWatcherT1 = nullptr;
   8. eventWatcherR1 = nullptr;
   9. // ...
   10. return {};
   11. }
   ```

   [napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/cpp/napi_init.cpp#L846-L896)
