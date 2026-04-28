---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-mainthreadjank-events-arkts
title: 订阅主线程超时事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 主线程超时事件 > 订阅主线程超时事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:07+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:19fc6b8470f3423548182928721d79df8bab1eeb06ac969123a45179d13723b7
---

## 简介

本文介绍如何使用HiAppEvent提供的ArkTS接口订阅主线程超时事件。接口的详细使用说明（参数限制、取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

## 接口说明

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

### 添加事件观察者

以主线程超时事件订阅为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   2. import { buffer, util } from '@kit.ArkTS'
   3. import { fileIo as fs } from '@kit.CoreFileKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，可在onCreate、onForeground等生命周期接口中添加系统事件的订阅（结合业务需求，在合适的位置添加订阅方法），示例代码如下：

   ```
   1. hiAppEvent.addWatcher({
   2. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   3. name: "watcher",
   4. // 开发者可以订阅感兴趣的系统事件，此处是订阅了主线程超时事件
   5. appEventFilters: [
   6. {
   7. domain: hiAppEvent.domain.OS,
   8. names: [hiAppEvent.event.MAIN_THREAD_JANK]
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
   22. // 开发者可以获取到主线程超时事件发生的时间戳
   23. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.time=${eventInfo.params['time']}`);
   24. // 开发者可以获取到主线程超时应用的版本信息
   25. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_version=${eventInfo.params['bundle_version']}`);
   26. // 开发者可以获取到主线程超时应用的包名
   27. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.bundle_name=${eventInfo.params['bundle_name']}`);
   28. // 开发者可以获取到主线程超时应用的pid、uid
   29. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.pid=${eventInfo.params['pid']}`);
   30. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.uid=${eventInfo.params['uid']}`);
   31. // 开发者可以获取主线程处理开始和结束时间
   32. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.begin_time=${eventInfo.params['begin_time']}`);
   33. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.end_time=${eventInfo.params['end_time']}`);
   34. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.log_over_limit=${eventInfo.params['log_over_limit']}`);
   35. // 开发者可以获取到主线程超时事件时，任务执行的开始时间（主线程超时采集堆栈参数）
   36. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.app_start_jiffies_time=${JSON.stringify(eventInfo.params['app_start_jiffies_time'])}`);
   37. // 开发者可以获取到生成的主线程超时日志文件中，打印最多次的调用栈（主线程超时采集堆栈参数）
   38. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.heaviest_stack=${eventInfo.params['heaviest_stack']}`);

   40. // 开发者可以获取到主线程超时事件发生时的故障日志文件
   41. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo.params.external_log=${JSON.stringify(eventInfo.params['external_log'])}`);
   42. // 开发者可以通过以下方式移动文件到新的目录
   43. let path: string = String(eventInfo.params['external_log']);
   44. // 自定义的新的存储路径
   45. let targetPath: string = "";
   46. if (path.endsWith(".txt")) {
   47. targetPath= "/data/storage/el2/base/mainThreadJank.txt";
   48. } else if (path.endsWith(".trace")) {
   49. targetPath= "/data/storage/el2/base/mainThreadJank.trace";
   50. }
   51. fs.copyFileSync(path.toString(), targetPath.toString());
   52. }
   53. }
   54. }
   55. });
   ```
3. 该步骤用于模拟主线程超时采样栈事件。

   编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，示例代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. RelativeContainer() {
   6. Column() {
   7. Button("timeOut350", { stateEffect:true, type: ButtonType.Capsule})
   8. .width('75%')
   9. .height(50)
   10. .margin(15)
   11. .fontSize(20)
   12. .fontWeight(FontWeight.Bold)
   13. .onClick(() => {
   14. let t = Date.now();
   15. while (Date.now() - t <= 350) {}
   16. })
   17. }.width('100%')
   18. }
   19. .height('100%')
   20. .width('100%')
   21. }
   22. }
   ```
4. （可选）该步骤用于模拟自定义主线程超时参数，并触发主线程超时事件场景。

   编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，本示例中设置一个customSample的Button控件，在onClick中实现自定义设置采样栈参数代码，示例代码如下：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. // 模拟超时事件函数定义，示例代码：
   5. function wait150ms() {
   6. let t = Date.now();
   7. while (Date.now() - t <= 150){
   8. }
   9. }

   11. function wait500ms() {
   12. let t = Date.now();
   13. while (Date.now() - t <= 500){
   14. }
   15. }

   17. @Entry
   18. @Component
   19. struct Index {
   20. build() {
   21. RelativeContainer() {
   22. Column() {
   23. // 自定义设置采样栈参数按钮
   24. Button("customSample", { stateEffect:true, type: ButtonType.Capsule})
   25. .width('75%')
   26. .height(50)
   27. .margin(15)
   28. .fontSize(20)
   29. .fontWeight(FontWeight.Bold)
   30. .onClick(() => {
   31. // 在按钮点击函数中进行事件打点，以记录按钮点击事件
   32. let params: Record<string, hiAppEvent.ParamType> = {
   33. // 事件类型定义， 0-默认值，1-只采样栈 2-只收集trace
   34. "log_type": "1",
   35. // 超时时间 & 采样间隔
   36. "sample_interval": "100",
   37. // 忽略启动开始时间
   38. "ignore_startup_time": "11",
   39. // 采样次数
   40. "sample_count": "21",
   41. // 事件上报次数定义
   42. "report_times_per_app": "3"
   43. };
   44. hiAppEvent.setEventConfig(hiAppEvent.event.MAIN_THREAD_JANK, params).then(() => {
   45. hilog.info(0x0000, 'testTag', `HiAppEvent success to set event params.`)
   46. }).catch((err: BusinessError) => {
   47. hilog.error(0x0000, 'testTag', `HiAppEvent err.code: ${err.code}, err.message: ${err.message}`)
   48. });
   49. })
   50. // 触发150ms超时事件按钮
   51. Button("timeOut150", { stateEffect:true, type: ButtonType.Capsule})
   52. .width('75%')
   53. .height(50)
   54. .margin(15)
   55. .fontSize(20)
   56. .fontWeight(FontWeight.Bold)
   57. .onClick(() => {
   58. wait150ms();
   59. })
   60. }.width('100%')
   61. }
   62. .height('100%')
   63. .width('100%')
   64. }
   65. }
   ```
5. 该步骤可用于模拟主线程超时采样trace事件。

   编辑工程中的“entry > src > main > ets > pages> Index.ets”文件，添加按钮并在其onClick函数触发主线程超时采集trace功能，具体如下：

   注意

   启动主线程超时检测抓取trace的功能的前提是开发者使用[nolog版本](performance-analysis-kit-terminology.md#nolog版本)并且关闭开发者模式。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. RelativeContainer() {
   6. Column() {
   7. Button("timeOut500", { stateEffect:true, type: ButtonType.Capsule})
   8. .width('75%')
   9. .height(50)
   10. .margin(15)
   11. .fontSize(20)
   12. .fontWeight(FontWeight.Bold)
   13. .onClick(() => {
   14. let t = Date.now();
   15. while (Date.now() - t <= 500) {}
   16. })
   17. }.width('100%')
   18. }
   19. .height('100%')
   20. .width('100%')
   21. }
   22. }
   ```
6. 点击DevEco Studio界面中的运行按钮，运行应用工程。

   注意

   默认情况下，由于应用启动过程本身较为耗时，系统将在**应用启动10s后再进行测试，开始主线程超时事件检测**；

   若开发者使用setEventConfig接口设置自定义设置采样栈参数，系统将**在开发者设定的ignore\_startup\_time时间后，开始主线程超时事件检测**。

   主线程超时触发的条件：在检测任务的间隔内，检测到连续两次超时事件后，才会开启采集堆栈。

   用户可以快速点击2~3次触发超时的按钮（如：timeOut350、timeOut150或timeOut500三种不同卡顿场景的按钮），以触发主线程超时事件。

### 验证观察者是否订阅到主线程超时事件

1. 主线程超时事件上报后，系统会回调应用的onReceive函数，可以在Log窗口看到对系统事件数据的处理日志：

   主线程超时事件采样栈示例：

   ```
   1. HiAppEvent eventInfo.domain=OS
   2. HiAppEvent eventInfo.name=MAIN_THREAD_JANK
   3. HiAppEvent eventInfo.eventType=1
   4. HiAppEvent eventInfo.params.time=1717593620518
   5. HiAppEvent eventInfo.params.bundle_version=1.0.0
   6. HiAppEvent eventInfo.params.bundle_name=com.example.main_thread_jank
   7. HiAppEvent eventInfo.params.pid=40986
   8. HiAppEvent eventInfo.params.uid=20020150
   9. HiAppEvent eventInfo.params.begin_time=1717593620016
   10. HiAppEvent eventInfo.params.end_time=1717593620518
   11. HiAppEvent eventInfo.params.external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_20240613211739_40986.XXX"]
   12. HiAppEvent eventInfo.params.log_over_limit=false
   13. HiAppEvent eventInfo.params.app_start_jiffies_time=XXXX
   14. HiAppEvent eventInfo.params.heaviest_stack=XXXX
   ```

   主线程超时事件采样trace，与采样栈的结果大致相同，不同的地方：

   ```
   1. 栈：
   2. 采样栈增加两个参数：app_start_jiffies_time和heaviest_stack。
   3. external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_yyyyMMDDHHmmss_xxxx.txt"]。xxxx：代表进程pid

   5. trace：
   6. external_log=["/data/storage/el2/log/watchdog/MAIN_THREAD_JANK_unix时间戳_xxxx.trace"]。xxxx：代表进程pid
   ```
