---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/long-time-task-guide
title: 长时任务开发指导 (TaskPool)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 长时任务并发场景 > 长时任务开发指导 (TaskPool)
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c3131f2df42f15ff6e64be55b70d0f5da50a98532b0a9ac8e26a16c616c5ef7
---

此处提供使用TaskPool进行长时任务的开发指导，以定期采集传感器数据为例。

## 使用TaskPool进行传感器数据监听

1. 导入所需的模块。

   ```typescript
   import { sensor } from '@kit.SensorServiceKit';
   import { taskpool } from '@kit.ArkTS';
   import { BusinessError, emitter } from '@kit.BasicServicesKit';
   ```
2. 定义长时任务，内部监听sensor数据，并通过emitter注册销毁通知。

   ```typescript
   @Concurrent
   async function sensorListener(): Promise<void> {
     sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
       emitter.emit({ eventId: 0 }, { data: data });
     }, { interval: 1000000000 });

     emitter.on({ eventId: 1 }, () => {
       sensor.off(sensor.SensorId.ACCELEROMETER)
       emitter.off(1)
     })
   }
   ```
3. 给应用添加ohos.permission.ACCELEROMETER权限，在module.json5中的"module"字段中添加如下代码示例的"requestPermissions"字段，配置相关权限。

   ```json
   "requestPermissions": [
     {
       "name": "ohos.permission.ACCELEROMETER"
     }
   ]
   ```
4. 宿主线程定义注册及销毁的行为。

   * 注册：发起长时任务，并通过emitter接收监听数据。
   * 销毁：发送取消传感器监听的事件，并结束长时任务。

   ```typescript
   import { sensor } from '@kit.SensorServiceKit';
   import { taskpool } from '@kit.ArkTS';
   import { BusinessError, emitter } from '@kit.BasicServicesKit';

   @Concurrent
   async function sensorListener(): Promise<void> {
     sensor.on(sensor.SensorId.ACCELEROMETER, (data) => {
       emitter.emit({ eventId: 0 }, { data: data });
     }, { interval: 1000000000 });

     emitter.on({ eventId: 1 }, () => {
       sensor.off(sensor.SensorId.ACCELEROMETER)
       emitter.off(1)
     })
   }

   @Entry
   @Component
   struct Index {
     sensorTask?: taskpool.LongTask
     @State addListener: string = 'Add listener';
     @State deleteListener: string = 'Delete listener';

     build() {
       Column() {
         Text(this.addListener)
           .id('Add listener')
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
           .onClick(() => {
             this.sensorTask = new taskpool.LongTask(sensorListener);
             emitter.on({ eventId: 0 }, (data) => {
               // Do something here
               console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}}`);
             });
             taskpool.execute(this.sensorTask).then(() => {
               this.addListener = 'success';
               console.info('Add listener of ACCELEROMETER success');
             }).catch((e: BusinessError) => {
               this.addListener = 'failed';
             })
           })
         Text(this.deleteListener)
           .id('Delete listener')
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
           .onClick(() => {
             emitter.emit({ eventId: 1 });
             emitter.off(0);
             if (this.sensorTask != undefined) {
               taskpool.terminateTask(this.sensorTask);
               this.deleteListener = 'success';
             } else {
               console.error('sensorTask is undefined.');
               this.deleteListener = 'failed';
             }
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
