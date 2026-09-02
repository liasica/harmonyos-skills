---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-postmessageatfront
title: Worker向宿主线程进行消息插队通信
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > Worker向宿主线程进行消息插队通信
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6bef9d96eb86f44e31c8b35f05c555263bd8b41fbde813186d87bdb845fc3e1c
---

## 场景说明

在Worker多线程开发中，Worker线程通过[postMessage](../harmonyos-references/js-apis-worker.md#postmessage9-2)向宿主线程（主线程或其他Worker线程）发送消息时，消息按照发送顺序依次排队处理。当宿主线程繁忙时，消息队列中可能积压大量待处理消息，导致某些需要及时处理的消息（如用户交互响应、关键状态更新等）无法被及时执行。

针对上述场景，从API版本26.0.0开始，ArkTS提供了[postMessageAtFront](../harmonyos-references/js-apis-worker.md#postmessageatfront)接口，允许Worker线程向宿主线程发送插队消息，使消息插入到对应优先级消息队列的头部，从而被提前处理。

## 插队机制

* Worker线程向宿主线程发送消息时，支持插队操作，并支持按优先级[Priority](../harmonyos-references/js-apis-worker.md#priority)发送。
* 可通过将消息插入到对应优先级消息队列的头部，实现插队操作。
* 优先级越高的消息越早被宿主线程处理。处理顺序取决于优先级调度规则：IMMEDIATE > HIGH > LOW > IDLE。

  | 优先级 | 值 | 说明 |
  | --- | --- | --- |
  | IMMEDIATE | 1 | 立即执行优先级，优先于HIGH优先级处理。 |
  | HIGH | 2 | 高优先级，与普通postMessage消息优先级相同。 |
  | LOW | 3 | 低优先级，优先于IDLE优先级处理。 |
  | IDLE | 4 | 后台优先级，仅在没有其他优先级消息时才处理。 |
* 相同优先级的消息，处于消息队列头部的消息会优先被宿主线程处理。

## 使用示例

以下示例通过模拟宿主线程繁忙的场景，演示Worker线程如何通过postMessageAtFront()接口向宿主线程发送插队消息。

1. 在宿主线程创建Worker对象，并发送、接收消息。

   此例中，可通过点击“触发消息发送”按钮，发送消息给Worker线程。

   ```typescript
   import { MessageEvents, worker } from '@kit.ArkTS';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     @State workerObject: worker.ThreadWorker | null = null;
     aboutToAppear(): void {
       this.workerObject = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
       this.workerObject.onmessage = (e: MessageEvents): void => {
         // 模拟耗时操作，每个接收到的消息处理100ms，让消息排队起来
         let start = new Date().getTime();
         while (new Date().getTime() - start < 100) {
           continue;
         }
         let res: string = e.data as string;
         console.info('result is: ' + JSON.stringify(res));
       }
     }
     build() {
       Row() {
         Column({space: 20}) {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
           Button('触发消息发送')
             .fontSize(50)
             .onClick(()=>{
               if (this.workerObject != null) {
                 this.workerObject.postMessage('normal');
               }
             })
           Button('释放worker')
             .fontSize(50)
             .onClick(()=>{
               if (this.workerObject != null) {
                 this.workerObject.terminate();
                 this.workerObject = null;
               }
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
2. 在Worker线程中发送插队消息。

   Worker线程收到宿主线程发送的消息后，发送普通消息和插队消息。

   ```typescript
   import { MessageEvents, ThreadWorkerGlobalScope, worker, Priority } from '@kit.ArkTS';

   const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   workerPort.onmessage = (e: MessageEvents) => {
     // 发送多个消息，让消息排队起来
     for (let i = 0; i < 10; i++) {
       // 使用普通消息发送，按默认顺序排队处理
       workerPort.postMessage('normal message.');
     }
     // HIGH优先级：和普通消息相同优先级，插入到队列头部，让消息提前执行
     workerPort.postMessageAtFront?.('atFront high message', Priority.HIGH);
   }
   ```
