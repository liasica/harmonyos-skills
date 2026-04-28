---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-async-task-guide
title: TaskPool指定任务并发度场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > TaskPool指定任务并发度场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:71451c6c93a9662e01480c5db6a456c852782800546aaf7a7417a2026c0e473f
---

TaskPool支持使用异步队列来控制任务的并发度，能有效避免资源过载，减少任务阻塞，适用于网络请求、视频流处理和数据库操作等场景。

此处提供使用TaskPool创建[异步队列](../harmonyos-references/js-apis-taskpool.md#asyncrunner18)的开发指导，以相机预览流采集数据处理的功能为例。

由于处理过程是一个频繁且耗时的任务，当相机采集速度过快时，将丢弃之前的采集数据，仅保留最新的一帧数据进行处理。

1. 导入需要用到的模块。

   ```
   1. // TaskpoolAsyncLevel.ets
   2. import { taskpool } from '@kit.ArkTS';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { PromptAction } from '@kit.ArkUI';
   ```
2. 定义耗时任务。

   ```
   1. // TaskpoolAsyncLevel.ets
   2. @Concurrent
   3. function collectFrame() {
   4. // 采集数据，并且进行处理
   5. // 模拟处理过程，这里是个耗时任务，持续时间为30秒
   6. let t = new Date().getTime()
   7. while (new Date().getTime() - t < 30000) {
   8. continue;
   9. }
   10. console.info('collectFrame finished');
   11. }
   ```
3. 创建异步队列并执行采集任务。

   ```
   1. // TaskpoolAsyncLevel.ets
   2. @Entry
   3. @Component
   4. struct TaskpoolAsyncLevel {
   5. @State message: string = '触发采集任务';
   6. @State returnMessage: string = 'return...';
   7. @State promptAction: PromptAction = this.getUIContext().getPromptAction();

   9. build() {
   10. Row() {
   11. Column() {
   12. Button(this.message)
   13. .fontSize(50)
   14. .fontWeight(FontWeight.Bold)
   15. .onClick(async () => {
   16. // 创建并发度为5的异步队列，等待队列个数为5，当加入的任务数量超过5时，等待列表中处于队头的任务会被丢弃
   17. let asyncRunner:taskpool.AsyncRunner = new taskpool.AsyncRunner('async', 5, 5);
   18. // 触发采集任务
   19. for (let i = 0; i < 20; i++) {
   20. let task:taskpool.Task = new taskpool.Task(`async${i}`,collectFrame);
   21. asyncRunner.execute(task).then(() => {
   22. console.info('the current task name is ' + task.name);
   23. }).catch((e:BusinessError) => {
   24. console.error('async: error is ' + e);
   25. });
   26. }
   27. console.info('asyncRunner task finished');
   28. this.returnMessage = 'asyncRunner task finished';
   29. this.promptAction.showToast({ message: this.returnMessage });
   30. })
   31. // ...
   32. }
   33. .width('100%')
   34. }
   35. .height('100%')
   36. }
   37. }
   ```
