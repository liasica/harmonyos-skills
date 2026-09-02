---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-and-taskpool
title: Worker常驻线程通过TaskPool进行多任务并发处理
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > Worker常驻线程通过TaskPool进行多任务并发处理
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:99edca581f960bf303c5a13cf6d15d101e8ae29a1bec63535ba5bde15c81ab75
---

ArkTS应用开发过程中，可以选择TaskPool或Worker线程进行多任务并发处理，也可以两种并发能力都选择。

本示例将说明在Worker线程中通过TaskPool执行并发任务。

1. 在主线程中创建Worker线程并发送消息。

   ```typescript
   // workerAndTaskpool.ets
   import { MessageEvents, worker } from '@kit.ArkTS';
   import { PromptAction } from '@kit.ArkUI';

   @Entry
   @Component
   struct Index {
     @State message: string = '在主线程中创建Worker线程并发送消息';
     @State returnMessage: string = 'return...';
     @State promptAction: PromptAction = this.getUIContext().getPromptAction();

     build() {
       RelativeContainer() {
         Button(this.message)
           .fontSize(19)
           .id('HelloWorld')
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             // 1. 创建Worker实例
             const myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

             // 2. 注册onmessage回调函数，以处理Worker发送到主线程的消息
             myWorker.onmessage = (e: MessageEvents) => {
               console.info('主线程收到最终结果:', e.data.result);
               this.returnMessage = '主线程收到最终结果:' + e.data.result;
               this.promptAction.showToast({ message: this.returnMessage });
               myWorker.terminate(); // 选择合适的时机销毁Worker
             };

             // 3. 向Worker发送启动指令
             myWorker.postMessage({ type: 'start', data: 10 });
           })
         // ...
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. 在Worker线程中调用TaskPool执行并发任务。

   ```typescript
   // Worker.ets
   import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   import { taskpool } from '@kit.ArkTS';

   const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
   workerPort.onmessage = async (e: MessageEvents) => {
     if (e.data.type === 'start') {
       // 模拟Worker数据处理
       const processedData = heavyComputation(e.data.data);

       // 调用TaskPool执行并发任务
       const task = new taskpool.Task(parallelTask, processedData);
       const result = await taskpool.execute(task);
       console.info('TaskPool线程返回结果: ', result);

       // 将最终结果返回主线程
       workerPort.postMessage({
         status: 'success',
         result: result
       });
     }
   }

   function heavyComputation(base: number): number {
     let sum = 0;
     for (let i = 0; i < base * 10; i++) {
       sum += Math.sqrt(i);
     }
     return sum;
   }

   @Concurrent
   function parallelTask(base: number): number {
     let total = 0;
     for (let i = 0; i < base; i++) {
       total += i % 2 === 0 ? i : -i;
     }
     console.info('TaskPool线程计算结果: ', total);
     return total;
   }
   ```
