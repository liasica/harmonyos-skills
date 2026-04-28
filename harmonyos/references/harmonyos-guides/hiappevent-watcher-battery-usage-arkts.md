---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-battery-usage-arkts
title: 订阅24h功耗器件分解统计事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 24h功耗器件分解统计事件 > 订阅24h功耗器件分解统计事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1588415799878bea1bda255b0fce4a5beb502310051776dace7b8a028c2cd133
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现对应用内多线程执行耗时操作生成的24h功耗器件分解统计事件订阅为例，说明开发步骤。

1. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，在onCreate函数中添加系统事件的订阅，示例代码如下：

   ```
   1. import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

   3. hiAppEvent.addWatcher({
   4. // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
   5. name: "watcher",
   6. // 开发者可以订阅感兴趣的系统事件，此处是订阅了应用24h功耗器件分解统计事件
   7. appEventFilters: [
   8. {
   9. domain: hiAppEvent.domain.OS,
   10. names: [hiAppEvent.event.BATTERY_USAGE]
   11. }
   12. ],
   13. // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
   14. onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
   15. hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
   16. for (const eventGroup of appEventGroups) {
   17. // 开发者可以根据事件集合中的事件名称区分不同的系统事件
   18. hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
   19. for (const eventInfo of eventGroup.appEventInfos) {
   20. // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
   21. hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo=${JSON.stringify(eventInfo)}`);
   22. }
   23. }
   24. }
   25. });
   ```
2. 工程中构造高耗电测试场景，并进行相关测试，使设备产生实际耗电，演示示例如下：

   注意

   开发者自测试可跳过此步骤，仅需完成应用安装后并断开充电（充电状态下测试会导致无数据上报），使用应用5分钟以上。

   1）工程中添加“entry > src > main > ets > workers> worker.ets”文件，构造一个死循环，接收到主线程的消息后触发CPU高负载事件，完整示例代码如下

   ```
   1. import { worker } from '@kit.ArkTS';

   3. let workerPort = worker.workerPort;
   4. workerPort.onmessage = (message) => {
   5. eatCpu();
   6. }
   7. function eatCpu(): void {
   8. let val:number = 0;
   9. while (true) {
   10. val++;
   11. }
   12. }
   ```

   2）工程中添加“entry > src > main > ets > tester> CpuTester.ets”文件，在CpuTester 类中的start方法中开启多个线程的死循环，以触发多线程的CPU高负载事件，完整示例代码如下：

   ```
   1. import { worker } from '@kit.ArkTS';

   3. export default class CpuTester {
   4. workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker.ets');
   5. start(threadNum: number) {
   6. for (let index = 0; index < threadNum; index++) {
   7. this.workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets');
   8. this.workerInstance.postMessage('msg');
   9. }
   10. }
   11. }
   ```

   3）编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加“CPU加压”按钮并在其onClick函数构造多线程执行死循环，以触发CPU高负载事件，完整示例代码如下：

   ```
   1. import CpuTester from '../tester/CpuTester';

   3. @Entry
   4. @Component
   5. struct Index {
   6. @State message: string = 'Hello World';

   8. @State enable: boolean = true;

   10. @State threadNum: number = 5;

   12. cpuTester: CpuTester = new CpuTester();

   14. build() {
   15. Row() {
   16. Column() {
   17. Text(this.message)
   18. .fontSize(50)
   19. .fontWeight(FontWeight.Bold)
   20. Button('CPU加压')
   21. .fontSize(18)
   22. .margin(12)
   23. .fontWeight(FontWeight.Bold)
   24. .enabled(this.enable)
   25. .onClick(() => {
   26. this.cpuTester.start(this.threadNum);
   27. this.enable = false;
   28. })
   29. }
   30. .width('100%')
   31. }
   32. .height('100%')
   33. }
   34. }
   ```

   4）安装运行测试应用到测试机上，断开USB（2in1设备还需要断开充电线）；

   5）打开测试应用，然后在应用界面中点击“CPU加压”按钮，持续十分钟，测试过程保持屏幕常亮。
3. 测试完成后连接USB，0点后在Log窗口看到对系统事件数据的处理日志（快速触发上报方式：执行命令hdc shell hidumper -s 1213 -a '--test 1'，进入测试模式不进行时间跳变的校验，然后修改设备时间为下午的11点58分）：

   ```
   1. HiAppEvent onReceive: domain=OS
   2. HiAppEvent eventName=BATTERY_USAGE
   3. HiAppEvent eventInfo={"domain":"OS","name":"BATTERY_USAGE","eventType":2,"params":{"audio_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"audio_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"background_usage":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"begin_time":1709654400000,"bundle_name":"com.example.myapplication","bundle_version":"1.0.0","cpu_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"cpu_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125647],"ddr_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"ddr_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,207],"gps_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"gps_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"sensor_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"sensor_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"display_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"display_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8606],"end_time":1709740800000,"foreground_usage":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67766],"gpu_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"gpu_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48],"modem_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"modem_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"others_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"others_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1170],"rom_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"rom_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"time":1709740801326,"wifi_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"wifi_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}}
   ```
