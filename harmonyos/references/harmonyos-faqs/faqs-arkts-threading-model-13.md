---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-13
title: 如何实现Worker并发时序同步
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何实现Worker并发时序同步
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:032369547ac95a63032395108e970864bf68fb3c96ea13ce0498546e3f61113f
---

## 问题现象

通过Worker开启多个子线程并发执行任务，并在子线程中计数，达到阈值触发上传任务。具体操作为：触发事件->存数据库->检查数据库数量->满足上传条件进行上传。

```ts
workerPort.onmessage = async (event: MessageEvents) => {
  let eventData: string = event.data;
  // 1.存储数据
  // 2.检查数据库
  // 3.满足条件，触发上传任务
}
```

## 背景知识

[Worker](../harmonyos-guides/worker-introduction.md)：Worker的主要作用是为应用程序提供一个多线程的运行环境，实现应用程序执行过程与宿主线程分离。通过在后台线程运行脚本处理耗时操作，避免计算密集型或高延迟任务阻塞宿主线程。

## 解决方案

通过主线程统一控制上传触发+原子计数实现时序同步，所有计数操作集中在主线程完成，避免多Worker并发修改共享状态。

完整示例参考如下：

1. 主线程（Index.ets）。

   ```ts
   import { worker, MessageEvents } from '@kit.ArkTS';

   // 原子计数器（主线程维护）
   let uploadCounter = 0;
   const UPLOAD_THRESHOLD = 10;
   const workerInstance = new worker.ThreadWorker('../workers/Worker.ets');

   // 接收Worker存储完成通知
   workerInstance.onmessage = (e: MessageEvents) => {
     if (e.data === 'STORAGE_DONE') {
       uploadCounter++; // 原子递增
       // 主线程判断满足条件后触发上传任务
       if (uploadCounter === UPLOAD_THRESHOLD) {
         triggerUpload();
         uploadCounter = 0; // 重置计数器
       }
     }
   };

   // 触发Worker存储（示例）
   function triggerWorkerStorage(data: number) {
     workerInstance.postMessage(data);
   }

   // 上传执行函数
   function triggerUpload() {
     console.info('执行上传操作');
   }

   @Entry
   @Component
   struct Index {
     private count1: number = 0;
     private count2: number = 0;

     build() {
       Column() {
         Button('触发单次')
           .onClick(() => {
             triggerWorkerStorage(this.count1);
             this.count1 += 1;
           })
         Button('触发多次')
           .onClick(() => {
             for (let index = this.count2; index < this.count2 + 10; index++) {
               triggerWorkerStorage(index);
             }
             this.count2 += 1;
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. Worker线程（Worker.ets）。

   ```ts
   import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

   const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
   // 模拟数据库
   let list: Array<string> = [];

   workerPort.onmessage = (event: MessageEvents) => {
     let eventData: string = event.data;
     storeSQL(eventData);
     try {
       workerPort.postMessage('STORAGE_DONE');
     } catch (error) {
       console.info(`worker postMessage error`);
     }
   };

   // 模拟存数据库
   function storeSQL(data: string) {
     list.push(data);
     console.info(`模拟存储数据库${list.length}`);
   }
   ```
