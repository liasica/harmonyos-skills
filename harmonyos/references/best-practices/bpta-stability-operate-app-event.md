---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-operate-app-event
title: 应用事件
breadcrumb: 最佳实践 > 稳定性 > 稳定性运维 > 稳定性事件接入 > 应用事件
category: best-practices
scraped_at: 2026-04-28T08:23:07+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:3cb6792ed945e365d1ec825d03f58a7811a5020a7190c4292d614d65c9404cd1
---

## 概述

HiAppEvent是在系统层面为应用开发者提供的一种事件打点机制，支持应用记录在运行过程中发生的故障事件、统计事件、安全事件、行为事件，帮助开发者定位问题、分析应用运行情况，以便进一步统计分析访问数量、日常用户活跃数量、用户操作习惯以及其他影响用户使用产品的关键因素。

本文主要介绍如何使用HiAppEvent订阅和触发应用事件。

## 订阅应用事件（ArkTS）

HiAppEvent提供了事件订阅接口，用于本地获取应用事件。

### 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[应用事件打点](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

**订阅接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用的事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用的事件观察者，以移除对应用事件的订阅。 |

**打点接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| write(info: AppEventInfo, callback: AsyncCallback<void>): void | 应用事件异步打点方法，使用callback方式作为异步回调。 |
| write(info: AppEventInfo): Promise<void> | 应用事件异步打点方法，使用Promise方式作为异步回调。 |

### 开发步骤

以实现对用户点击按钮行为的事件打点及订阅为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets” 文件，在onCreate()函数中添加对用户点击按钮事件的订阅，示例代码如下：

   ```
   1. hiAppEvent.addWatcher({
   2. // Developers can customize observer names, and the system will use these names to identify different observers.
   3. name: "watcher1",
   4. appEventFilters: [{ domain: "button" }],
   5. triggerCondition: { row: 1 },
   6. onTrigger: (curRow: number, curSize: number, holder: hiAppEvent.AppEventPackageHolder) => {
   7. if (holder == null) {
   8. hilog.error(0x0000, 'testTag', "HiAppEvent holder is null");
   9. return;
   10. }
   11. hilog.info(0x0000, 'testTag', `HiAppEvent onTrigger: curRow=%{public}d, curSize=%{public}d`, curRow, curSize);
   12. let eventPkg: hiAppEvent.AppEventPackage | null = null;
   13. let maxRetry = 10;
   14. while (maxRetry-- > 0 && (eventPkg = holder.takeNext()) != null){
   15. hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.packageId=%{public}d`, eventPkg.packageId);
   16. hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.row=%{public}d`, eventPkg.row);
   17. hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.size=%{public}d`, eventPkg.size);
   18. for (const eventInfo of eventPkg.data) {
   19. hilog.info(0x0000, 'testTag', `HiAppEvent eventPkg.info=%{public}s`, eventInfo);
   20. }
   21. }
   22. }
   23. });
   ```
3. 编辑工程中的“entry > src > main > ets > pages > Index.ets” 文件，导入依赖模块：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
4. 编辑工程中的“entry > src > main > ets > pages > Index.ets” 文件，添加一个按钮并在其onClick()函数中进行事件打点，以记录按钮点击事件，示例代码如下：

   ```
   1. Button("writeTest").onClick(() => {
   2. let eventParams: Record<string, number> = { 'clickTime': 100 };
   3. let eventInfo: hiAppEvent.AppEventInfo = {
   4. domain: "button",
   5. name: "click",
   6. eventType: hiAppEvent.EventType.BEHAVIOR,
   7. params: eventParams,
   8. };
   9. hiAppEvent.write(eventInfo).then(() => {
   10. hilog.info(0x0000, 'testTag', `HiAppEvent success to write event`)
   11. }).catch((err: BusinessError) => {
   12. hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`)
   13. });
   14. })
   ```
5. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“writeTest”，触发一次按钮点击事件打点。
6. 可以在Log窗口看到按钮点击事件打点成功的日志，以及触发订阅回调后对打点事件数据的处理日志：

   ```
   1. HiAppEvent success to write event
   2. HiAppEvent eventPkg.packageId=0
   3. HiAppEvent eventPkg.row=1
   4. HiAppEvent eventPkg.size=124
   5. HiAppEvent eventPkg.info={"domain_":"button","name_":"click","type_":4,"time_":1670268234523,"tz_":"+0800","pid_":3295,"tid_":3309,"click_time":100}
   ```

## 订阅应用事件（C/C++）

### 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[HiAppEvent](../harmonyos-references/capi-hiappevent.md)。

**订阅接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_AddWatcher(HiAppEvent\_Watcher \* watcher) | 添加应用的事件观察者，以添加对应用事件的订阅。 |
| int OH\_HiAppEvent\_RemoveWatcher(HiAppEvent\_Watcher \* watcher) | 移除应用的事件观察者，以移除对应用事件的订阅。 |

**打点接口功能介绍：**

| 接口名 | 描述 |
| --- | --- |
| int OH\_HiAppEvent\_Write(const char \* domain, const char \* name, enum EventType type, const ParamList list) | 实现对参数为列表类型的应用事件打点。 |

### 开发步骤

以实现对用户点击按钮行为的事件打点及订阅为例，说明开发步骤：

1. 从[三方开源库jsoncpp代码仓](https://github.com/open-source-parsers/jsoncpp)下载源码的压缩包，并按照README的**Amalgamated source**中介绍的操作步骤得到jsoncpp.cpp、json.h和json-forwards.h三个文件。新建Native C++工程，并将jsoncpp导入到新建工程内，目录结构如下：

   ```
   1. entry
   2. └── src
   3. └── main
   4. ├── cpp
   5. │   ├── CMakeLists.txt
   6. │   ├── json
   7. │   │   ├── json-forwards.h
   8. │   │   └── json.h
   9. │   ├── jsoncpp.cpp
   10. │   ├── napi_init.cpp
   11. │   └── types
   12. │       └── libentry
   13. │           ├── Index.d.ts
   14. │           └── oh-package.json5
   15. └── ets
   16. ├── entryability
   17. │   └── EntryAbility.ets
   18. └── pages
   19. └── Index.ets
   ```
2. 编辑“CMakeLists.txt”文件，添加源文件及动态库：

   ```
   1. # 新增jsoncpp.cpp(解析订阅事件中的json字符串)源文件
   2. add_library(entry SHARED napi_init.cpp jsoncpp.cpp)
   3. # 新增动态库依赖libhiappevent_ndk.z.so和libhilog_ndk.z.so(日志输出)
   4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so libhiappevent_ndk.z.so)
   ```
3. 编辑“napi\_init.cpp”文件，导入依赖的文件，并定义LOG\_TAG：

   ```
   1. #include "napi/native_api.h"
   2. #include "json/json.h"
   3. #include "hilog/log.h"
   4. #include "hiappevent/hiappevent.h"

   6. #undef LOG_TAG
   7. #define LOG_TAG "testTag"
   ```
4. 订阅应用事件：
   * OnReceive()类型观察者：编辑“napi\_init.cpp”文件，定义OnReceive()类型观察者相关方法：

   ```
   1. static HiAppEvent_Watcher *appEventWatcher;

   3. static void OnReceive(const char *domain, const struct HiAppEvent_AppEventGroup *appEventGroups, uint32_t groupLen) {
   4. for (int i = 0; i < groupLen; ++i) {
   5. for (int j = 0; j < appEventGroups[i].infoLen; ++j) {
   6. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", appEventGroups[i].appEventInfos[j].domain);
   7. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", appEventGroups[i].appEventInfos[j].name);
   8. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", appEventGroups[i].appEventInfos[j].type);
   9. if (strcmp(appEventGroups[i].appEventInfos[j].domain, "button") == 0 &&
   10. strcmp(appEventGroups[i].appEventInfos[j].name, "click") == 0) {
   11. Json::Value params;
   12. Json::Reader reader(Json::Features::strictMode());
   13. if (reader.parse(appEventGroups[i].appEventInfos[j].params, params)) {
   14. auto time = params["click_time"].asInt64();
   15. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.click_time=%{public}lld", time);
   16. }
   17. }
   18. }
   19. }
   20. }

   22. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
   23. appEventWatcher = OH_HiAppEvent_CreateWatcher("onReceiverWatcher");
   24. const char *names[] = {"click"};
   25. OH_HiAppEvent_SetAppEventFilter(appEventWatcher, "button", 0, names, 1);
   26. OH_HiAppEvent_SetWatcherOnReceive(appEventWatcher, OnReceive);
   27. OH_HiAppEvent_AddWatcher(appEventWatcher);
   28. return {};
   29. }
   ```

   * OnTrigger()类型观察者：编辑“napi\_init.cpp”文件，定义OnTrigger()类型观察者相关方法：

   ```
   1. static HiAppEvent_Watcher *appEventWatcher;

   3. static void OnTake(const char *const *events, uint32_t eventLen) {
   4. Json::Reader reader(Json::Features::strictMode());
   5. for (int i = 0; i < eventLen; ++i) {
   6. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo=%{public}s", events[i]);
   7. Json::Value eventInfo;
   8. if (reader.parse(events[i], eventInfo)) {
   9. auto domain = eventInfo["domain_"].asString();
   10. auto name = eventInfo["name_"].asString();
   11. auto type = eventInfo["type_"].asInt();
   12. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.domain=%{public}s", domain.c_str());
   13. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.name=%{public}s", name.c_str());
   14. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.eventType=%{public}d", type);
   15. if (domain == "button" && name == "click") {
   16. auto clickTime = eventInfo["click_time"].asInt64();
   17. OH_LOG_INFO(LogType::LOG_APP, "HiAppEvent eventInfo.params.click_time=%{public}lld", clickTime);
   18. }
   19. }
   20. }
   21. }

   23. static void OnTrigger(int row, int size) {
   24. OH_HiAppEvent_TakeWatcherData(appEventWatcher, row, OnTake);
   25. }

   27. static napi_value RegisterWatcher(napi_env env, napi_callback_info info) {
   28. appEventWatcher = OH_HiAppEvent_CreateWatcher("onTriggerWatcher");
   29. const char *names[] = {"click"};
   30. OH_HiAppEvent_SetAppEventFilter(appEventWatcher, "button", 0, names, 1);
   31. OH_HiAppEvent_SetWatcherOnTrigger(appEventWatcher, OnTrigger);
   32. OH_HiAppEvent_SetTriggerCondition(appEventWatcher, 1, 0, 0);
   33. OH_HiAppEvent_AddWatcher(appEventWatcher);
   34. return {};
   35. }
   ```
5. 编辑“napi\_init.cpp”文件，添加button事件打点接口：

   ```
   1. static napi_value WriteAppEvent(napi_env env, napi_callback_info info) {
   2. auto params = OH_HiAppEvent_CreateParamList();
   3. OH_HiAppEvent_AddInt64Param(params, "click_time", time(nullptr));
   4. OH_HiAppEvent_Write("button", "click", EventType::BEHAVIOR, params);
   5. OH_HiAppEvent_DestroyParamList(params);
   6. return {};
   7. }
   ```
6. 编辑“napi\_init.cpp”文件，将RegisterWatcher和WriteAppEvent注册为ArkTS接口：

   ```
   1. static napi_value Init(napi_env env, napi_value exports)
   2. {
   3. napi_property_descriptor desc[] = {
   4. {"registerWatcher", nullptr, RegisterWatcher, nullptr, nullptr, nullptr, napi_default, nullptr},
   5. {"writeAppEvent", nullptr, WriteAppEvent, nullptr, nullptr, nullptr, napi_default, nullptr}
   6. };
   7. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
   8. return exports;
   9. }
   ```

   编辑“index.d.ts”文件，定义ArkTS接口：

   ```
   1. export const registerWatcher: () => void;
   2. export const writeAppEvent: () => void;
   ```
7. 编辑“EntryAbility.ets”文件，在onCreate()函数中新增接口调用：

   ```
   1. import testNapi from 'libentry.so'

   3. testNapi.registerWatcher();
   ```
8. 编辑“Index.ets”文件，新增按钮触发打点事件：

   ```
   1. import testNapi from 'libentry.so'

   3. Button("button_click").onClick(() => {
   4. testNapi.writeAppEvent();
   5. })
   ```
9. 可以在Log窗口看到对应用事件数据的处理日志：

   ```
   1. HiAppEvent eventInfo.domain=button
   2. HiAppEvent eventInfo.name=click
   3. HiAppEvent eventInfo.eventType=4
   4. HiAppEvent eventInfo.params.click_time=1502031843
   ```
10. 移除应用事件观察者：

    ```
    1. static napi_value RemoveWatcher(napi_env env, napi_callback_info info) {
    2. OH_HiAppEvent_RemoveWatcher(appEventWatcher);
    3. return {};
    4. }
    ```
11. 销毁应用事件观察者：

    ```
    1. static napi_value DestroyWatcher(napi_env env, napi_callback_info info) {
    2. OH_HiAppEvent_DestroyWatcher(appEventWatcher);
    3. appEventWatcher = nullptr;
    4. return {};
    5. }
    ```
