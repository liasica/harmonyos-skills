---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hiappevent-watcher-cpu-usage-high-arkts
title: 订阅CPU高负载事件（ArkTS）
breadcrumb: 指南 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > 事件订阅 > 使用HiAppEvent订阅事件 > 系统事件 > CPU高负载事件 > 订阅CPU高负载事件（ArkTS）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:40+08:00
doc_updated_at: 2026-05-14
content_hash: sha256:1820b612af1e6f6d33f0b4650876d214b5d60c100cba034996182c0607445d96
---

## 接口说明

API接口的具体使用说明（参数使用限制、具体取值范围等）请参考[@ohos.hiviewdfx.hiAppEvent (应用事件打点)ArkTS API文档](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md)。

| 接口名 | 描述 |
| --- | --- |
| addWatcher(watcher: Watcher): AppEventPackageHolder | 添加应用事件观察者，以添加对应用事件的订阅。 |
| removeWatcher(watcher: Watcher): void | 移除应用事件观察者，以移除对应用事件的订阅。 |

## 开发步骤

以实现应用内多线程执行死循环生成的CPU高负载事件订阅为例，说明开发步骤。

1. 新建一个ArkTS应用工程，编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，导入依赖模块，示例代码如下：

   ```ts
   import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，可以在例如onCreate函数中添加系统事件的订阅，示例代码如下：

   ```ts
   hiAppEvent.addWatcher({
      // 开发者可以自定义观察者名称，系统会使用名称来标识不同的观察者
      name: "watcher",
      // 开发者可以订阅感兴趣的系统事件，此处是订阅了崩溃事件
      appEventFilters: [
        {
          domain: hiAppEvent.domain.OS,
          names: [hiAppEvent.event.CPU_USAGE_HIGH]
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
3. （可选）以下示例用于模拟自定义CPU高负载事件的配置策略

   编辑工程中的“entry > src > main > ets > entryability > EntryAbility.ets”文件，自定义CPU高负载事件的配置策略，用法详见[CpuUsageHighPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#cpuusagehighpolicy22)章节，示例代码如下：

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   let policy: hiAppEvent.EventPolicy = {
     "cpuUsageHighPolicy":{
       "foregroundLoadThreshold" : 10,  // 设置应用前台CPU负载异常阈值为10%
       "backgroundLoadThreshold" : 5,   // 设置应用前台CPU负载异常阈值为5%
       "threadLoadThreshold" : 50,      // 设置应用线程CPU负载异常阈值为50%
       "perfLogCaptureCount" : 3,       // 设置采样栈每日采集次数上限为3次
       "threadLoadInterval" : 30,       // 设置应用线程负载异常检测周期为30秒
     }
   };
   hiAppEvent.configEventPolicy(policy).then(() => {
     hilog.info(0x0000, 'hiAppEvent', `Successfully set cpu usage high event policy.`);
   }).catch((err: BusinessError) => {
     hilog.error(0x0000, 'hiAppEvent', `Failed to set cpu usage high event policy. Code: ${err?.code}, message: ${err?.message}`);
   });
   ```

   **说明** 

   抓取采样栈有内存开销，影响功耗性能，只建议开发者在本地调试时使用自定义参数功能。

   此外，Debug版本应用，采样栈每日采集次数阈值范围为：[-1, 100]； Release版本应用，采样栈每日采集次数阈值范围为阈值范围：[0, 20]，详见[CpuUsageHighPolicy](../harmonyos-references/js-apis-hiviewdfx-hiappevent.md#cpuusagehighpolicy22)。
4. 工程中添加“entry > src > main > ets > workers> worker.ets”文件，构造一个死循环，接收到主线程的消息后触发CPU高负载事件，完整示例代码如下：

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
5. 工程中添加“entry > src > main > ets > tester> CpuTester.ets”文件，在CpuTester 类中的start方法中开启多个线程的死循环，以触发多线程的CPU高负载事件，完整示例代码如下：

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
6. 编辑工程中的“entry > src > main > ets > pages > Index.ets”文件，添加“CPU加压”按钮并在其onClick函数构造多线程执行死循环，以触发CPU高负载事件，完整示例代码如下：

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
7. 点击DevEco Studio界面中的运行按钮，运行应用工程，然后在应用界面中点击“CPU加压”按钮，触发CPU高负载事件。应用保持在前台且屏幕处于亮屏状态，五到十分钟之后可以在Log窗口看到对系统事件数据的处理日志：

   **说明** 

   默认状态下，CPU高负载事件[抓取次数存在限制](power-detection.md#约束和限制)。

   开发者如果未抓取到CPU高负载事件external\_log日志，可以尝试重启测试设备重新抓取或自定义相关配置策略。

   ```text
   HiAppEvent eventInfo={"domain":"OS","eventType":1,"name":"CPU_USAGE_HIGH","params":{"begin_time":1723725541352,"bundle_name":"com.xpower.test","bundle_version":"1.0.0","end_time":1723725843413,"external_log":["/data/storage/el2/log/hiappevent/CPU_USAGE_HIGH_1723725950017_0.log","/data/storage/el2/log/hiappevent/CPU_USAGE_HIGH_1723725950197_0.log"],"fault_type":1,"foreground":false,"log_over_limit":false,"threads":[{"name":"com.xpower.test","tid":60677,"usage":0.070805000000000007},{"name":"WorkerThread","tid":60856,"usage":7.4353600000000002},{"name":"WorkerThread","tid":60855,"usage":7.4645099999999998},{"name":"WorkerThread","tid":60854,"usage":7.4120400000000002},{"name":"WorkerThread","tid":60853,"usage":7.4770099999999999}],"time":1723725949836,"usage":25}}
   ```
