---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-cancel-task
title: 多线程取消TaskPool任务场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 多线程取消TaskPool任务场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:7c28d938f74916b929d55692b6d5173b0f3922943823276194671eb31654e7a6
---

由于任务池[TaskPool](../harmonyos-references/js-apis-taskpool.md)的任务对象[Task](../harmonyos-references/js-apis-taskpool.md#task)不支持跨线程传递，无法在子线程中直接取消任务。从API version 18开始，Task新增了任务ID[属性](../harmonyos-references/js-apis-taskpool.md#属性)，支持通过任务ID在子线程中取消任务。开发者可将已创建任务的任务ID存储在[Sendable对象](arkts-sendable.md)中，需要取消任务时，通过Sendable对象在子线程中取消任务。详情可参考以下示例。

1. 定义一个Sendable类，在类属性中存储任务ID。

   ```typescript
   // sendable.ets
   @Sendable
   export class SendableTest {
     // 存储任务ID
     private taskId: number = 0;

     constructor(id: number) {
       this.taskId = id;
     }

     public getTaskId(): number {
       return this.taskId;
     }
   }
   ```
2. 在UI主线程向TaskPool提交一个延时任务，并在子线程取消该任务。

   ```typescript
   // TaskpoolCancel.ets
   import { taskpool } from '@kit.ArkTS';
   import { SendableTest } from '../utils/Sendable';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { PromptAction } from '@kit.ArkUI';

   @Concurrent
   function cancel(send: SendableTest) {
     // 在子线程中通过任务ID取消任务
     taskpool.cancel(send.getTaskId());
     console.info('cancel task finished');
   }

   @Concurrent
   function delayed() {
     console.info('delayed task finished');
   }

   @Entry
   @Component
   struct TaskpoolCancel {
     @State message: string = 'CancelTaskpool';
     @State returnMessage: string = 'return...';
     @State promptAction: PromptAction = this.getUIContext().getPromptAction();

     build() {
       Row() {
         Column() {
           Button(this.message)
             .fontSize(25)
             .fontWeight(FontWeight.Bold)
             .onClick(async () => {
               let task = new taskpool.Task(delayed);
               taskpool.executeDelayed(2000, task).catch((e: BusinessError) => {
                 console.error(`taskpool execute error, message is: ${e.message}`);
                 // taskpool execute error, message is: taskpool:: task has been canceled.
               });
               let send = new SendableTest(task.taskId);
               taskpool.execute(cancel, send).then(() => {
                 this.returnMessage = 'Taskpool canceled!';
                 this.promptAction.showToast({ message: this.returnMessage });
               });
             })
           // ...
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
