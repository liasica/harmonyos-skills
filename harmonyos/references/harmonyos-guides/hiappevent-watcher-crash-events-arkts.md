---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-crash-events-arkts
title: 订阅崩溃事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 崩溃事件 > 订阅崩溃事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b4e1eab7a9d689de1a9c5b10c55bd84099af411058421538985993a65215ea12
---

## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅应用崩溃事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

说明

使用ArkTS接口可以订阅JsError和NativeCrash两种崩溃事件。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

**建议在应用启动后、执行业务逻辑前添加事件观察者，以确保能够订阅到崩溃事件。**

以订阅用户点击按钮触发崩溃生成的崩溃事件为例，说明开发步骤。

1. DevEco Studio新建Native C++模板工程，编辑“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块。示例代码如下：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   2. import { deviceInfo } from '@kit.BasicServicesKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中设置事件的[崩溃事件自定义参数](hiappevent-watcher-crash-events.md#崩溃事件自定义参数设置)和[崩溃日志规格自定义参数](hiappevent-watcher-crash-events.md#崩溃日志规格自定义参数设置)，示例代码如下：

   ```
   1. // 构建崩溃事件的自定义参数
   2. let crashParams: Record<string, hiAppEvent.ParamType> = {
   3. "test_data": 100, // test_data为自定义数据，开发者可根据实际需求自定义params参数。
   4. };
   5. // 开发者可以设置崩溃事件的自定义参数
   6. hiAppEvent.setEventParam(crashParams, hiAppEvent.domain.OS, hiAppEvent.event.APP_CRASH).then(() => {
   7. hilog.info(0x0000, 'testTag', `HiAppEvent success to set event param`);
   8. }).catch((err: BusinessError) => {
   9. hilog.error(0x0000, 'testTag', `HiAppEvent code: ${err.code}, message: ${err.message}`);
   10. });

   12. if (deviceInfo.sdkApiVersion >= 20) {  // API Version 20及以后版本，支持设置崩溃日志配置参数
   13. // 构建崩溃日志规格自定义参数
   14. let crashConfigParams: Record<string, hiAppEvent.ParamType> = {
   15. "extend_pc_lr_printing": true, // 使能扩展打印pc和lr寄存器附近的内存值
   16. "log_file_cutoff_sz_bytes": 1024000, // 截断崩溃日志到1000KB
   17. "simplify_vma_printing": true // 使能精简打印maps
   18. };
   19. // 开发者可以设置崩溃日志配置参数
   20. hiAppEvent.setEventConfig(hiAppEvent.event.APP_CRASH, crashConfigParams).then(() => {
   21. hilog.info(0x0000, 'testTag', `HiAppEvent success to set event config.`);
   22. }).catch((err: BusinessError) => {
   23. hilog.error(0x0000, 'testTag', `HiAppEvent code: ${err.code}, message: ${err.message}`);
   24. });
   25. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/entryability/EntryAbility.ets#L100-L106)
3. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在 onCreate 函数中订阅系统事件。示例代码如下：

   ```
   1. // 添加崩溃事件观察者
   2. let watcher: hiAppEvent.Watcher = {
   3. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   4. name: 'crashEventWatcher',
   5. // 开发者可以订阅感兴趣的系统事件，此处是订阅了崩溃事件
   6. appEventFilters: [
   7. {
   8. domain: hiAppEvent.domain.OS,
   9. names: [hiAppEvent.event.APP_CRASH]
   10. }
   11. ],
   12. // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
   13. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
   14. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   15. for (const eventGroup of appEventGroups) {
   16. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   17. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   18. for (const eventInfo of eventGroup.appEventInfos) {
   19. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   20. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
   21. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
   22. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.eventType=${eventInfo.eventType}`);
   23. // 开发者可以获取到崩溃事件发生的时间戳
   24. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${eventInfo.params['time']}`);
   25. // 开发者可以获取到崩溃事件发生的崩溃类型
   26. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.crash_type=${eventInfo.params['crash_type']}`);
   27. // 开发者可以获取到崩溃应用的前后台状态
   28. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.foreground=${eventInfo.params['foreground']}`);
   29. // 开发者可以获取到崩溃应用的版本信息
   30. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_version=${eventInfo.params['bundle_version']}`);
   31. // 开发者可以获取到崩溃应用的包名
   32. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_name=${eventInfo.params['bundle_name']}`);
   33. // 开发者可以获取到崩溃应用的进程id
   34. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.pid=${eventInfo.params['pid']}`);
   35. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uid=${eventInfo.params['uid']}`);
   36. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uuid=${eventInfo.params['uuid']}`);
   37. // 开发者可以获取到崩溃事件发生的异常类型、异常原因和异常调用栈
   38. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.exception=${JSON.stringify(eventInfo.params['exception'])}`);
   39. // 开发者可以获取到崩溃事件发生时日志信息
   40. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.hilog.size=${eventInfo.params['hilog'].length}`);
   41. // 开发者可以获取到崩溃事件的故障进程存活时间
   42. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.process_life_time=${eventInfo.params['process_life_time']}`);
   43. // 开发者可以获取到崩溃事件发生时内存信息
   44. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.memory=${JSON.stringify(eventInfo.params['memory'])}`);
   45. // 开发者可以获取到崩溃事件发生时的崩溃日志文件
   46. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.external_log=${JSON.stringify(eventInfo.params['external_log'])}`);
   47. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.log_over_limit=${eventInfo.params['log_over_limit']}`);
   48. // 开发者可以获取到崩溃事件的自定义数据test_data
   49. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.test_data=${eventInfo.params['test_data']}`);
   50. }
   51. }
   52. }
   53. };
   54. hiAppEvent.addWatcher(watcher);
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/PerformanceAnalysisKit/HiAppEvent/EventSub/entry/src/main/ets/entryability/EntryAbility.ets#L114-L168)
4. 构造崩溃场景

   * 构造NativeCrash类型崩溃

     编辑工程中的“entry > src > main > cpp > napi\_init.cpp”文件，添加TestNullptr方法，并将TestNullptr注册为ArkTS接口，增加如下代码：

     ```
     1. static napi_value TestNullptr(napi_env env, napi_callback_info info)
     2. {
     3. int *p = nullptr;
     4. int a = *p; // 空指针解引用，程序会在此处崩溃
     5. return {};
     6. }
     ```

     ```
     1. static napi_value Init(napi_env env, napi_value exports)
     2. {
     3. napi_property_descriptor desc[] = {
     4. // ···
     5. { "testNullptr", nullptr, TestNullptr, nullptr, nullptr, nullptr, napi_default, nullptr },
     6. // ···
     7. };
     8. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
     9. return exports;
     10. }
     ```

     在"index.d.ts"文件中，定义ArkTS接口：

     ```
     1. export const testNullptr: () => void;
     ```

     编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其onClick函数中构造崩溃场景，以触发崩溃事件。示例代码如下：

     ```
     1. Button('NativeCrash')
     2. .type(ButtonType.Capsule)
     3. .margin({
     4. top: 20
     5. })
     6. .backgroundColor('#0D9FFB')
     7. .width('80%')
     8. .height('5%')
     9. .onClick(() => {
     10. // 在按钮点击函数中构造一个crash场景，触发应用崩溃事件
     11. testNapi.testNullptr();
     12. })
     ```
   * 构造JsError类型崩溃

     编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其onClick函数中构造崩溃场景，以触发崩溃事件。示例代码如下：

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
5. 点击DevEco Studio界面的运行按钮，启动应用工程。在应用界面中点击“NativeCrash”或“JsError”按钮，触发崩溃事件。系统根据崩溃类型生成相应的日志并进行回调。

说明

JsError通过进程内采集故障信息触发回调，速度快，而NativeCrash采取进程外采集故障信息，平均耗时约2秒，具体受业务线程数量和进程间通信影响。开发者可订阅崩溃事件，故障信息采集完成后异步上报，不阻塞当前业务。

### 验证观察者是否订阅到崩溃事件

在应用主动捕获崩溃异常和未主动捕获崩溃异常的场景下，崩溃事件的回调时机不同，需在不同时间验证是否订阅到崩溃事件。

**应用未主动捕获崩溃异常场景**

若应用未主动捕获崩溃异常，系统处理崩溃后应用将退出。**应用下次启动时**，HiAppEvent将崩溃事件上报给已注册的监听，完成回调。

若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](fault-log-extension-app-events-arkts.md)回调重写的函数，进行延迟上报。

**应用主动捕获崩溃异常场景**

若应用主动捕获崩溃异常，崩溃事件将在**应用退出前**回调，例如以下两种情况：

1. 异常处理中未主动退出，应用崩溃后将不会退出。

   采用[errorManager.on](../harmonyos-references/js-apis-app-ability-errormanager.md#errormanageronerror)方法捕获异常会导致JsError类型的崩溃事件在应用退出前回调。若应用主动注册[崩溃信号](cppcrash-guidelines.md#系统处理的崩溃信号)处理函数但未主动退出，会导致NativeCrash类型的崩溃事件在应用退出前回调。
2. 异常处理耗时过长，导致应用退出延迟。

在开发调试阶段，HiAppEvent上报事件完成回调后，可以在DevEco Studio的HiLog窗口查看JsError类型崩溃事件内容。NativeCrash类型崩溃事件内容略有不同，具体参见[崩溃事件字段说明](hiappevent-watcher-crash-events.md#事件字段说明)。JsError类型崩溃事件内容样例如下：

```
1. HiAppEvent onReceive: domain=OS
2. HiAppEvent eventName=APP_CRASH
3. HiAppEvent eventInfo.domain=OS
4. HiAppEvent eventInfo.name=APP_CRASH
5. HiAppEvent eventInfo.eventType=1
6. HiAppEvent eventInfo.params.time=1503045716054
7. HiAppEvent eventInfo.params.crash_type=JsError
8. HiAppEvent eventInfo.params.foreground=true
9. HiAppEvent eventInfo.params.bundle_version=1.0.0
10. HiAppEvent eventInfo.params.bundle_name=com.samples.eventsub
11. HiAppEvent eventInfo.params.pid=2610
12. HiAppEvent eventInfo.params.uid=20010044
13. HiAppEvent eventInfo.params.uuid=7c3b1579c8ca8629af3858f8145254c2867ee402dc16ee18034337aae258620b
14. HiAppEvent eventInfo.params.exception={"message":"Unexpected Text in JSON: Empty Text","name":"SyntaxError","stack":"    at anonymous (entry|entry|1.0.0|src/main/ets/pages/Index.ts:163:22)\n","thread_name":"amples.eventsub"}
15. HiAppEvent eventInfo.params.hilog.size=100
16. HiAppEvent eventInfo.params.process_life_time=25
17. HiAppEvent eventInfo.params.memory={"rss":181964,"sys_avail_mem":1230456,"sys_free_mem":676940,"sys_total_mem":2001932}
18. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_CRASH_1503045716408_2610.log"]
19. HiAppEvent eventInfo.params.log_over_limit=false
20. HiAppEvent eventInfo.params.test_data=100
```

## 从Faultlogger接口迁移崩溃事件

[@ohos.faultLogger (故障日志获取)](../harmonyos-references/js-apis-faultlogger.md)接口从API version 18开始废弃使用, 不再维护。后续版本推荐使用[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)订阅崩溃事件。该章节指导开发者从Faultlogger接口迁移至hiAppEvent接口，来订阅崩溃事件。

在Faultlogger的[FaultType](../harmonyos-references/js-apis-faultlogger.md#faulttype)里定义的CPP\_CRASH和JS\_CRASH都属于崩溃故障类型。

在hiAppEvent的hiAppEvent.addWatcher接口中设置事件名称为hiAppEvent.event.APP\_CRASH、事件领域为hiAppEvent.domain.OS，可以订阅崩溃事件。

通过[hiAppEvent.AppEventInfo.params](hiappevent-watcher-crash-events.md#params字段说明)中的crash\_type字段可以区分具体是哪种崩溃事件。

两者对应关系如下：

| Faultlogger.FaultType | hiAppEvent.AppEventInfo.params.crash\_type |
| --- | --- |
| CPP\_CRASH | NativeCrash |
| JS\_CRASH | JsError |

[FaultLogInfo](../harmonyos-references/js-apis-faultlogger.md#faultloginfo)与[hiAppEvent.AppEventInfo.params](hiappevent-watcher-crash-events.md#params字段说明)的对应关系如下：

| Faultlogger.FaultLogInfo | hiAppEvent.AppEventInfo.params | 说明 |
| --- | --- | --- |
| pid | pid | 无 |
| uid | uid | 无 |
| type | crash\_type | 类型不同，Faultlogger中是故障类型枚举，hiAppEvent中是字符串类型。 |
| timestamp | time | 无 |
| module | bundle\_name | 无 |
| fullLog | external\_log | fullLog为故障日志全文。external\_log为故障日志文件应用沙箱路径，访问该路径的文件，可以得到故障日志全文。 |
| reason | external\_log文件内容中的Reason字段 | 无 |
| summary | external\_log文件内容中的一部分 | CPP\_CRASH的summary对应external\_log文件内容中的Fault thread info字段；JS\_CRASH的summary对应external\_log文件内容中的Error name、Error message、 Stacktrace、HybridStack字段。 |

[FaultLogger.query(使用callback回调)](../harmonyos-references/js-apis-faultlogger.md#faultloggerquery9)和[FaultLogger.query(使用Promise回调)](../harmonyos-references/js-apis-faultlogger.md#faultloggerquery9-1)都可以使用[hiAppEvent.addWatcher](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)实现相同功能。

查阅[开发步骤](hiappevent-watcher-crash-events-arkts.md#开发步骤)和[验证观察者是否订阅到崩溃事件](hiappevent-watcher-crash-events-arkts.md#验证观察者是否订阅到崩溃事件)，了解使用hiAppEvent订阅崩溃事件（ArkTS）的具体步骤。
