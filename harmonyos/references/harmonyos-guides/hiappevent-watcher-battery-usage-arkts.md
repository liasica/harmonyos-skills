---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-battery-usage-arkts
title: 订阅24h功耗器件分解统计事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > 24h功耗器件分解统计事件 > 订阅24h功耗器件分解统计事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:071250381e27e2d910fe95b1ac6c6e9e0db9c90efa321d6eb358f53375120d4d
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

   ```ts
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';

   hiAppEvent.addWatcher({
      // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
      name: "watcher",
      // 开发者可以订阅感兴趣的系统事件，此处是订阅了应用24h功耗器件分解统计事件
      appEventFilters: [
        {
          domain: hiAppEvent.domain.OS,
          names: [hiAppEvent.event.BATTERY_USAGE]
        }
      ],
      // 开发者可以自行实现订阅实时回调函数，以便对订阅获取到的事件数据进行自定义处理
      onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
        hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
        for (const eventGroup of appEventGroups) {
          // 开发者可以根据事件集合中的事件名称区分不同的系统事件
          hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
          for (const eventInfo of eventGroup.appEventInfos) {
            // 开发者可以对事件集合中的事件数据进行自定义处理，此处是将事件数据打印在日志中
            hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo=${JSON.stringify(eventInfo)}`);
          }
        }
      }
    });
   ```
2. 工程中构造高耗电测试场景，并进行相关测试，使设备产生实际耗电，演示示例如下：

   **注意** 

   开发者自测试可跳过此步骤，仅需完成应用安装后并断开充电（充电状态下测试会导致无数据上报），使用应用5分钟以上。

   1）工程中添加“entry > src > main > ets > workers> worker.ets”文件，构造一个死循环，接收到主线程的消息后触发CPU高负载事件，完整示例代码如下

   ```ts
   import { worker } from '@kit.ArkTS';

   let workerPort = worker.workerPort;
   workerPort.onmessage = (message) => {
     eatCpu();
   }
   function eatCpu(): void {
     let val:number = 0;
     while (true) {
       val++;
     }
   }
   ```

   2）工程中添加“entry > src > main > ets > tester> CpuTester.ets”文件，在CpuTester 类中的start方法中开启多个线程的死循环，以触发多线程的CPU高负载事件，完整示例代码如下：

   ```ts
   import { worker } from '@kit.ArkTS';

   export default class CpuTester {
     workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker.ets');
     start(threadNum: number) {
       for (let index = 0; index < threadNum; index++) {
         this.workerInstance = new worker.ThreadWorker('entry/ets/workers/worker.ets');
         this.workerInstance.postMessage('msg');
       }
     }
   }
   ```

   3）编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加“CPU加压”按钮并在其onClick函数构造多线程执行死循环，以触发CPU高负载事件，完整示例代码如下：

   ```ts
   import CpuTester from '../tester/CpuTester';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     @State enable: boolean = true;

     @State threadNum: number = 5;

     cpuTester: CpuTester = new CpuTester();

   build() {
     Row() {
       Column() {
         Text(this.message)
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
         Button('CPU加压')
           .fontSize(18)
           .margin(12)
           .fontWeight(FontWeight.Bold)
           .enabled(this.enable)
           .onClick(() => {
             this.cpuTester.start(this.threadNum);
             this.enable = false;
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```

   4）安装运行测试应用到测试机上，断开USB（2in1设备还需要断开充电线）；

   5）打开测试应用，然后在应用界面中点击“CPU加压”按钮，持续十分钟，测试过程保持屏幕常亮。
3. 测试完成后连接USB，0点后在Log窗口看到对系统事件数据的处理日志（快速触发上报方式：执行命令hdc shell hidumper -s 1213 -a '--test 1'，进入测试模式不进行时间跳变的校验，然后修改设备时间为下午的11点58分）：

   ```text
   HiAppEvent onReceive: domain=OS
   HiAppEvent eventName=BATTERY_USAGE
   HiAppEvent eventInfo={"domain":"OS","name":"BATTERY_USAGE","eventType":2,"params":{"audio_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"audio_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"background_usage":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"begin_time":1709654400000,"bundle_name":"com.example.myapplication","bundle_version":"1.0.0","cpu_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"cpu_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125647],"ddr_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"ddr_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,207],"gps_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"gps_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"sensor_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"sensor_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"display_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"display_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8606],"end_time":1709740800000,"foreground_usage":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67766],"gpu_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"gpu_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48],"modem_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"modem_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"others_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"others_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1170],"rom_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"rom_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"time":1709740801326,"wifi_background_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],"wifi_foreground_energy":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}}
   ```
