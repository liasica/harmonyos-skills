---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/resident-task-guide
title: 常驻任务开发指导（Worker）
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 常驻任务并发场景 > 常驻任务开发指导（Worker）
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:152de47794eee986e7fa50dcbe9e21694386a06042ae7bcb9101c6c38c4e807b
---

提供使用Worker进行常驻任务的开发指导。Worker将持续执行任务，直到宿主线程发送终止指令。

开发过程和示例如下：

1. DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，单击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建“Worker”为例。

   此外，还支持手动创建Worker文件。具体方式和注意事项请参见[创建Worker的注意事项](worker-introduction.md#创建worker的注意事项)。
2. 首先导入Worker模块，然后在宿主线程中通过调用ThreadWorker的[constructor()](../harmonyos-references/js-apis-worker.md#constructor9)方法创建Worker对象，创建Worker对象的线程为宿主线程。 此处的宿主线程为UI主线程，宿主线程发送'start'以开始执行某个长期运行的任务，并接收子线程返回的相关消息。当不需要执行该任务时，发送'stop'以停止该任务的执行。在此示例中，任务将在10秒后结束。

   ```
   1. import { worker } from '@kit.ArkTS';
   2. import resource from '../util/resource';

   4. const workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');

   6. @Entry
   7. @Component
   8. struct Index {
   9. @State message: string = 'Listener task';

   11. build() {
   12. Column() {
   13. Text(this.message)
   14. .id('HelloWorld')
   15. .fontSize(50)
   16. .fontWeight(FontWeight.Bold)
   17. .onClick(() => {
   18. workerInstance.postMessage({ type: 'End' });
   19. workerInstance.onmessage = (event) => {
   20. console.info(resource.resourceToString($r('app.string.Information')), event.data);
   21. }
   22. // 10秒后停止worker
   23. setTimeout(() => {
   24. workerInstance.postMessage({ type: 'stop' });
   25. }, 10000);
   26. this.message = 'success';
   27. })
   28. }
   29. .height('100%')
   30. .width('100%')
   31. }
   32. }
   ```
3. 在Worker线程中，当接收到宿主线程发送的消息为'start'时，开始执行某个长时间不定期运行的任务，并实时向宿主线程返回消息。当接收到的消息为'stop'时，结束该任务的执行并返回相应的消息给宿主线程。

   ```
   1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   2. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
   3. let isRunning = false;
   4. workerPort.onmessage = (e: MessageEvents) => {
   5. const type = e.data.type as string;
   6. if (type === 'End') {
   7. if (!isRunning) {
   8. isRunning = true;
   9. // 开始常驻任务
   10. performTask();
   11. }
   12. } else if (type === 'stop') {
   13. isRunning = false;
   14. workerPort.close();  // 关闭Worker
   15. }
   16. }
   17. // 模拟常驻任务
   18. function performTask() {
   19. if (isRunning) {
   20. // 模拟某个长期运行的任务
   21. workerPort.postMessage('Worker is performing a task');
   22. // 1秒后再次执行任务
   23. setTimeout(performTask, 1000);
   24. }
   25. workerPort.postMessage('Worker is stop performing a task');
   26. }
   ```
