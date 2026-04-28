---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-cancel-task
title: 多线程取消TaskPool任务场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 多线程取消TaskPool任务场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:49a9d405a73f4e72083648fb6c834d234e8a98815b1047ce6aad6f3964f109c1
---

由于任务池[TaskPool](../harmonyos-references/js-apis-taskpool.md)的任务对象[Task](../harmonyos-references/js-apis-taskpool.md#task)不支持跨线程传递，无法在子线程中直接取消任务。从 API version 18 开始，Task新增了[任务ID](../harmonyos-references/js-apis-taskpool.md#属性)属性，支持通过任务ID在子线程中取消任务。开发者可将已创建任务的任务ID存储在[Sendable对象](arkts-sendable.md)中，需要取消任务时，通过Sendable对象在子线程中取消任务。详情可参考以下示例。

1. 定义一个Sendable类，在类属性中存储任务ID。

   ```
   1. // sendable.ets
   2. @Sendable
   3. export class SendableTest {
   4. // 存储任务ID
   5. private taskId: number = 0;

   7. constructor(id: number) {
   8. this.taskId = id;
   9. }

   11. public getTaskId(): number {
   12. return this.taskId;
   13. }
   14. }
   ```
2. 在UI主线程向TaskPool提交一个延时任务，并在子线程取消该任务。

   ```
   1. // TaskpoolCancel.ets
   2. import { taskpool } from '@kit.ArkTS';
   3. import { SendableTest } from '../utils/Sendable';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { PromptAction } from '@kit.ArkUI';

   7. @Concurrent
   8. function cancel(send: SendableTest) {
   9. // 在多线程中通过任务ID取消任务
   10. taskpool.cancel(send.getTaskId());
   11. console.info('cancel task finished');
   12. }

   14. @Concurrent
   15. function delayed() {
   16. console.info('delayed task finished');
   17. }

   19. @Entry
   20. @Component
   21. struct TaskpoolCancel {
   22. @State message: string = 'CancelTaskpool';
   23. @State returnMessage: string = 'return...';
   24. @State promptAction: PromptAction = this.getUIContext().getPromptAction();

   26. build() {
   27. Row() {
   28. Column() {
   29. Button(this.message)
   30. .fontSize(25)
   31. .fontWeight(FontWeight.Bold)
   32. .onClick(async () => {
   33. let task = new taskpool.Task(delayed);
   34. taskpool.executeDelayed(2000, task).catch((e: BusinessError) => {
   35. console.error(`taskpool execute error, message is: ${e.message}`);
   36. // taskpool execute error, message is: taskpool:: task has been canceled.
   37. });
   38. let send = new SendableTest(task.taskId);
   39. taskpool.execute(cancel, send);
   40. this.returnMessage = 'Taskpool canceled!';
   41. this.promptAction.showToast({ message: this.returnMessage });
   42. })
   43. // ...
   44. }
   45. .width('100%')
   46. }
   47. .height('100%')
   48. }
   49. }
   ```
