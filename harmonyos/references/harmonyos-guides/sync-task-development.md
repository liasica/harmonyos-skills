---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sync-task-development
title: 同步任务开发指导 (TaskPool和Worker)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 耗时任务并发场景 > 同步任务开发指导 (TaskPool和Worker)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ac1e0c7eaf7cbbe066072bb89484b2fd7286df347325a30138b662aea5dee19e
---

同步任务用于在多个线程间协调执行，确保任务按特定顺序和规则进行（如使用锁防止数据竞争）。

同步任务的实现需要考虑多个线程之间的协作和同步，以确保数据的正确性和程序的正确执行。

当同步任务之间相对独立时，推荐使用TaskPool，例如一系列导入的静态方法或单例实现的方法。如果同步任务之间有关联性，则需要使用Worker。

## 使用TaskPool处理同步任务

以下场景推荐使用TaskPool。

* 调度相互独立的任务。
* 静态方法实现的任务。
* 单例构造的句柄或者类对象跨线程使用。

说明

由于[Actor模型](multi-thread-concurrency-overview.md#actor模型)不同线程间内存隔离的特性，非线程安全的单例无法在不同线程间使用。可通过共享模块导出单例解决此问题。

1. 定义并发函数，实现业务逻辑。
2. 创建任务[Task](../harmonyos-references/js-apis-taskpool.md#task)，通过[execute()](../harmonyos-references/js-apis-taskpool.md#taskpoolexecute-1)接口执行该任务。
3. 对任务返回的结果进行操作。

如下示例中业务使用TaskPool调用相关同步方法的代码，首先定义并发函数taskpoolFunc，需要注意必须使用[@Concurrent装饰器](taskpool-introduction.md#concurrent装饰器)装饰该函数；其次定义函数mainFunc，该函数功能为创建任务，执行任务并处理任务返回的结果。

```
1. import { worker } from '@kit.ArkTS';
2. import { taskpool } from '@kit.ArkTS';

4. // 步骤1: 定义并发函数，实现业务逻辑
5. @Concurrent
6. async function taskpoolFunc(num: number): Promise<number> {
7. // 根据业务逻辑实现相应的功能
8. let tmpNum: number = num + 100;
9. return tmpNum;
10. }

12. async function mainFunc(): Promise<void> {
13. // 步骤2: 创建任务并执行
14. let task1: taskpool.Task = new taskpool.Task(taskpoolFunc, 1);
15. let res1: number = await taskpool.execute(task1) as number;
16. let task2: taskpool.Task = new taskpool.Task(taskpoolFunc, res1);
17. let res2: number = await taskpool.execute(task2) as number;
18. // 步骤3: 对任务返回的结果进行操作
19. console.info('taskpool: task res1 is: ' + res1);
20. console.info('taskpool: task res2 is: ' + res2);
21. }

23. @Entry
24. @Component
25. struct Index {
26. @State message: string = 'Hello World';

28. build() {
29. Row() {
30. Column() {
31. Text(this.message)
32. .fontSize(50)
33. .fontWeight(FontWeight.Bold)
34. .onClick(async () => {
35. mainFunc();
36. let w: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/MyWorker2.ts');
37. w.onmessage = (): void => {
38. // 接收Worker子线程的结果
39. }
40. w.onerror = (): void => {
41. // 接收Worker子线程的错误信息
42. }
43. // 向Worker子线程发送Set消息
44. w.postMessage({ 'type': 0, 'data': 'data' });
45. // 向Worker子线程发送Get消息
46. w.postMessage({ 'type': 1 });
47. // ...
48. // 根据实际业务，选择时机以销毁线程
49. w.terminate();
50. this.message = 'success';
51. })
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

## 使用Worker处理关联的同步任务

当一系列同步任务需要使用同一个句柄调度，或者需要依赖某个类对象调度，且无法在不同任务池之间共享时，需要使用Worker。

1. 在UI主线程中创建Worker对象并接收Worker线程发送的消息。DevEco Studio支持一键生成Worker。在{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可生成Worker的模板文件及配置信息。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State message: string = 'Hello World';

   6. build() {
   7. Row() {
   8. Column() {
   9. Text(this.message)
   10. .fontSize(50)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(async () => {
   13. mainFunc();
   14. let w: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/MyWorker2.ts');
   15. w.onmessage = (): void => {
   16. // 接收Worker子线程的结果
   17. }
   18. w.onerror = (): void => {
   19. // 接收Worker子线程的错误信息
   20. }
   21. // 向Worker子线程发送Set消息
   22. w.postMessage({ 'type': 0, 'data': 'data' });
   23. // 向Worker子线程发送Get消息
   24. w.postMessage({ 'type': 1 });
   25. // ...
   26. // 根据实际业务，选择时机以销毁线程
   27. w.terminate();
   28. this.message = 'success';
   29. })
   30. }
   31. .width('100%')
   32. }
   33. .height('100%')
   34. }
   35. }
   ```
2. 在Worker线程中绑定Worker对象，同时处理同步任务逻辑。

   ```
   1. export default class Handle {
   2. syncGet() {
   3. return;
   4. }

   6. syncSet(num: number) {
   7. return;
   8. }
   9. }
   ```

   ```
   1. import { worker, ThreadWorkerGlobalScope, MessageEvents } from '@kit.ArkTS';
   2. import Handle from './handle'; // 返回句柄

   4. let workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   6. // 无法传输的句柄，所有操作依赖此句柄
   7. let handler: Handle = new Handle()

   9. // Worker线程的onmessage逻辑
   10. workerPort.onmessage = (e: MessageEvents): void => {
   11. switch (e.data.type as number) {
   12. case 0:
   13. handler.syncSet(e.data.data);
   14. workerPort.postMessage('success set');
   15. break;
   16. case 1:
   17. handler.syncGet();
   18. workerPort.postMessage('success get');
   19. break;
   20. default:
   21. break;
   22. }
   23. }
   ```
