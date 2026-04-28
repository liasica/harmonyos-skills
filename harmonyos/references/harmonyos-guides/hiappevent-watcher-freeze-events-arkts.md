---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-freeze-events-arkts
title: 订阅应用冻屏事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 应用冻屏事件 > 订阅应用冻屏事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:04+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:f6b2ed890912c98fbc8c908a68f2450216be9182c6929258a87251f439ce1ea9
---

## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅应用冻屏事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以订阅应用冻屏事件为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中设置事件的自定义参数，示例代码如下：

   ```
   1. // 开发者完成参数键值对赋值
   2. let params: Record<string, hiAppEvent.ParamType> = {
   3. "test_data": 100,
   4. };
   5. // 开发者可以设置应用冻屏事件的自定义参数
   6. hiAppEvent.setEventParam(params, hiAppEvent.domain.OS, hiAppEvent.event.APP_FREEZE).then(() => {
   7. hilog.info(0x0000, 'testTag', `HiAppEvent success to set event param`);
   8. }).catch((err: BusinessError) => {
   9. hilog.error(0x0000, 'testTag', `HiAppEvent code: ${err.code}, message: ${err.message}`);
   10. });
   ```
3. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下：

   ```
   1. hiAppEvent.addWatcher({
   2. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   3. name: "watcher",
   4. // 开发者可以订阅感兴趣的系统事件，此处是订阅了应用冻屏事件
   5. appEventFilters: [
   6. {
   7. domain: hiAppEvent.domain.OS,
   8. names: [hiAppEvent.event.APP_FREEZE]
   9. }
   10. ],
   11. // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
   12. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
   13. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   14. for (const eventGroup of appEventGroups) {
   15. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   16. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   17. for (const eventInfo of eventGroup.appEventInfos) {
   18. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   19. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.domain=${eventInfo.domain}`);
   20. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.name=${eventInfo.name}`);
   21. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.eventType=${eventInfo.eventType}`);
   22. // 开发者可以获取到应用冻屏事件发生的时间戳
   23. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${eventInfo.params['time']}`);
   24. // 开发者可以获取到应用冻屏事件发生时应用的前后台状态
   25. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.foreground=${eventInfo.params['foreground']}`);
   26. // 开发者可以获取到应用冻屏事件发生时应用的版本信息
   27. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_version=${eventInfo.params['bundle_version']}`);
   28. // 开发者可以获取到应用冻屏事件发生时应用的包名
   29. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_name=${eventInfo.params['bundle_name']}`);
   30. // 开发者可以获取到应用冻屏事件发生时应用的进程名称
   31. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.process_name=${eventInfo.params['process_name']}`);
   32. // 开发者可以获取到应用冻屏事件发生时应用的进程id
   33. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.pid=${eventInfo.params['pid']}`);
   34. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uid=${eventInfo.params['uid']}`);
   35. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uuid=${eventInfo.params['uuid']}`);
   36. // 开发者可以获取到应用冻屏事件发生的异常类型、异常原因
   37. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.exception=${JSON.stringify(eventInfo.params['exception'])}`);
   38. // 开发者可以获取到应用冻屏事件发生时日志信息
   39. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.hilog.size=${eventInfo.params['hilog'].length}`);
   40. // 开发者可以获取到应用冻屏事件发生时主线程未处理消息
   41. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.event_handler.size=${eventInfo.params['event_handler'].length}`);
   42. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.event_handler_size_3s=${eventInfo.params['event_handler_size_3s']}`);
   43. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.event_handler_size_6s=${eventInfo.params['event_handler_size_6s']}`);
   44. // 开发者可以获取到应用冻屏事件发生时同步binder调用信息
   45. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.peer_binder.size=${eventInfo.params['peer_binder'].length}`);
   46. // 开发者可以获取到应用冻屏事件发生时全量线程调用栈
   47. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.threads.size=${eventInfo.params['threads'].length}`);
   48. // 开发者可以获取到应用冻屏事件发生时内存信息
   49. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.memory=${JSON.stringify(eventInfo.params['memory'])}`);
   50. // 开发者可以获取到应用冻屏事件发生时的故障日志文件
   51. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.external_log=${JSON.stringify(eventInfo.params['external_log'])}`);
   52. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.log_over_limit=${eventInfo.params['log_over_limit']}`);
   53. // 开发者可以获取到应用冻屏事件的自定义数据test_data
   54. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.test_data=${eventInfo.params['test_data']}`);
   55. // 开发者可以获取到应用冻屏事件的故障进程存活时间
   56. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.process_life_time=${eventInfo.params['process_life_time']}`);
   57. }
   58. }
   59. }
   60. });
   ```
4. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加按钮并在其onClick函数构造应用无响应场景，以触发应用冻屏事件，示例代码如下：

   ```
   1. Button("appFreeze").onClick(()=>{
   2. // 在按钮点击函数中构造一个freeze场景，触发应用冻屏事件
   3. setTimeout(() => {
   4. let t = Date.now();
   5. while (Date.now() - t <= 15000) {}
   6. }, 5000);
   7. })
   ```
5. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击按钮“appFreeze”，触发一次应用冻屏事件。

### 验证观察者是否订阅到应用冻屏事件

1. 应用无响应退出后，重新进入应用可以在Log窗口看到对系统事件数据的处理日志：

   ```
   1. HiAppEvent onReceive: domain=OS
   2. HiAppEvent eventName=APP_FREEZE
   3. HiAppEvent eventInfo.domain=OS
   4. HiAppEvent eventInfo.name=APP_FREEZE
   5. HiAppEvent eventInfo.eventType=1
   6. HiAppEvent eventInfo.params.time=1711440881768
   7. HiAppEvent eventInfo.params.foreground=true
   8. HiAppEvent eventInfo.params.bundle_version=1.0.0
   9. HiAppEvent eventInfo.params.bundle_name=com.example.myapplication
   10. HiAppEvent eventInfo.params.process_name=com.example.myapplication
   11. HiAppEvent eventInfo.params.pid=3197
   12. HiAppEvent eventInfo.params.uid=20010043
   13. HiAppEvent eventInfo.params.uuid=27fac7098da46efe1cae9904946ec06c5acc91689c365efeefb7a23a0c37df77
   14. HiAppEvent eventInfo.params.exception={"message":"App main thread is not response!","name":"THREAD_BLOCK_6S"}
   15. HiAppEvent eventInfo.params.hilog.size=77
   16. HiAppEvent eventInfo.params.event_handler.size=6
   17. HiAppEvent eventInfo.params.event_handler_size_3s=5
   18. HiAppEvent eventInfo.params.event_handler_size_6s=6
   19. HiAppEvent eventInfo.params.peer_binder.size=0
   20. HiAppEvent eventInfo.params.threads.size=28
   21. HiAppEvent eventInfo.params.memory={"pss":0,"rss":0,"sys_avail_mem":1361464,"sys_free_mem":796232,"sys_total_mem":1992340,"vm_heap_total_size":"9961472","vm_heap_used_size":"7596424","vss":0}
   22. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/hiappevent/APP_FREEZE_1711440899240_3197.log"]
   23. HiAppEvent eventInfo.params.log_over_limit=false
   24. HiAppEvent eventInfo.params.test_data=100
   25. HiAppEvent eventInfo.params.process_life_time=18
   ```
2. 若应用无法启动或长时间未启动，开发者可以参考[使用FaultLogExtensionAbility订阅事件](fault-log-extension-app-events-arkts.md)回调重写的函数，进行延迟上报。

## 从Faultlogger接口迁移应用冻屏事件

[@ohos.faultLogger (故障日志获取)](../harmonyos-references/js-apis-faultlogger.md)接口从API version 18开始废弃使用, 不再维护。后续版本推荐使用[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)订阅应用冻屏事件。该章节指导开发者从Faultlogger接口迁移至hiAppEvent接口，来订阅应用冻屏事件。

在Faultlogger的[FaultType](../harmonyos-references/js-apis-faultlogger.md#faulttype)里定义的APP\_FREEZE即为应用冻屏故障类型。

在hiAppEvent的hiAppEvent.addWatcher接口中设置事件名称为hiAppEvent.event.APP\_FREEZE、事件领域为hiAppEvent.domain.OS，可以订阅应用冻屏事件。

通过[hiAppEvent.AppEventInfo.params](hiappevent-watcher-freeze-events.md#params字段说明)中exception字段的name子字段可以区分具体是哪种应用冻屏事件。

[FaultLogInfo](../harmonyos-references/js-apis-faultlogger.md#faultloginfo)与[hiAppEvent.AppEventInfo.params](hiappevent-watcher-freeze-events.md#params字段说明)的字段对应关系如下：

| Faultlogger.FaultLogInfo | hiAppEvent.AppEventInfo.params | 说明 |
| --- | --- | --- |
| pid | pid | 无。 |
| uid | uid | 无。 |
| type | exception字段中的name子字段 | 类型不同，Faultlogger中是故障类型枚举，hiAppEvent中是字符串类型。 |
| timestamp | time | 无。 |
| module | bundle\_name | 无。 |
| fullLog | external\_log | fullLog为故障日志全文。external\_log为故障日志文件在应用沙箱中的具体路径(/data/storage/el2/log/)，访问该路径的文件，可以得到故障日志全文。 |
| reason | external\_log文件内容中的Reason字段 | 无。 |
| summary | external\_log文件内容中特定段落 | APP\_FREEZE的summary对应external\_log文件中从appfreeze:进程名所在行到DisplayPowerInfo:所在行的这一段内容。 |

[FaultLogger.query(使用callback回调)](../harmonyos-references/js-apis-faultlogger.md#faultloggerquery9)和[FaultLogger.query(使用Promise回调)](../harmonyos-references/js-apis-faultlogger.md#faultloggerquery9-1)都可以使用[hiAppEvent.addWatcher](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#hiappeventaddwatcher)实现相同功能。

查阅[开发步骤](hiappevent-watcher-freeze-events-arkts.md#开发步骤)和[验证观察者是否订阅到应用冻屏事件](hiappevent-watcher-freeze-events-arkts.md#验证观察者是否订阅到应用冻屏事件)，了解使用hiAppEvent订阅应用冻屏事件（ArkTS）的具体步骤。

## 示例代码

* [应用异常处理](https://gitcode.com/HarmonyOS_Samples/exception-handling)
