---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cpu-intensive-task-development
title: CPU密集型任务开发指导 (TaskPool和Worker)
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 耗时任务并发场景 > CPU密集型任务开发指导 (TaskPool和Worker)
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:37+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4937985915f2624f44389656b4e242506c55edd21beca1993f05cf9d4b9753bd
---

CPU密集型任务是指需要占用系统资源进行大量计算的任务，这类任务需要长时间运行，会阻塞线程中其他事件的处理，因此不适合在UI主线程中执行。例如图像处理、视频编码、数据分析等。

基于多线程并发机制处理CPU密集型任务可以提高CPU利用率，提升应用程序响应速度。

当任务不需要长时间（3分钟）占用后台线程，而是一个个独立的任务时，推荐使用TaskPool，反之推荐使用Worker。

接下来将分别以图像直方图处理和后台长时间模型预测任务为例进行说明。

## 使用TaskPool进行图像直方图处理

1. 实现图像处理的业务逻辑。
2. 对数据进行分段，并通过任务组发起关联任务调度。

   创建[TaskGroup](../harmonyos-references/js-apis-taskpool.md#taskgroup10)，通过[addTask()](../harmonyos-references/js-apis-taskpool.md#addtask10)添加对应的任务，然后通过[execute()](../harmonyos-references/js-apis-taskpool.md#taskpoolexecute10)执行任务组，并指定为[高优先级](../harmonyos-references/js-apis-taskpool.md#priority)。在当前任务组所有任务结束后，会将直方图处理结果同时返回。
3. 汇总处理结果数组。

```
1. import { taskpool } from '@kit.ArkTS';
2. // ...

4. @Concurrent
5. function imageProcessing(dataSlice: ArrayBuffer): ArrayBuffer {
6. // 步骤1: 具体的图像处理操作及其他耗时操作
7. return dataSlice;
8. }

10. function histogramStatistic(pixelBuffer: ArrayBuffer): void {
11. // 步骤2: 分成三段并发调度
12. let number: number = pixelBuffer.byteLength / 3;
13. let buffer1: ArrayBuffer = pixelBuffer.slice(0, number);
14. let buffer2: ArrayBuffer = pixelBuffer.slice(number, number * 2);
15. let buffer3: ArrayBuffer = pixelBuffer.slice(number * 2);

17. let group: taskpool.TaskGroup = new taskpool.TaskGroup();
18. group.addTask(imageProcessing, buffer1);
19. group.addTask(imageProcessing, buffer2);
20. group.addTask(imageProcessing, buffer3);

22. taskpool.execute(group, taskpool.Priority.HIGH).then((ret: Object) => {
23. // 步骤3: 结果数组汇总处理
24. })
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State message: string = 'Hello World'

32. build() {
33. Row() {
34. Column() {
35. Text(this.message)
36. .fontSize(50)
37. .fontWeight(FontWeight.Bold)
38. .onClick(() => {
39. let buffer: ArrayBuffer = new ArrayBuffer(24);
40. histogramStatistic(buffer);
41. this.message = 'success';
42. // 销毁Worker线程
43. workerInstance.terminate();
44. })
45. }
46. .width('100%')
47. }
48. .height('100%')
49. }
50. }
```

## 使用Worker进行长时间数据分析

本文通过某地区提供的房价数据训练一个简易的房价预测模型，该模型支持通过输入房屋面积和房间数量去预测该区域的房价，模型需要长时间运行，房价预测需要使用前面的模型运行结果，因此需要使用Worker。

1. DevEco Studio提供了Worker创建的模板，创建一个Worker线程，例如命名为“MyWorker”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/dt3qFNVBQoi2ELWiQpZ5lA/zh-cn_image_0000002552797886.png?HW-CC-KV=V1&HW-CC-Date=20260427T233835Z&HW-CC-Expire=86400&HW-CC-Sign=EEC4B85EE7DB87BBD3DEBD53FF9AFF5C0203F232C0C33418ACD4AF7CDC3E335E)
2. 在宿主线程中首先调用ThreadWorker的[constructor()](../harmonyos-references/js-apis-worker.md#constructor9)方法创建Worker对象；然后通过注册[onmessage()](../harmonyos-references/js-apis-worker.md#属性-1)回调接收Worker线程发送过来的消息；最后通过调用[postMessage()](../harmonyos-references/js-apis-worker.md#postmessage9)方法向Worker线程发送消息。

   例如，向Worker线程发送训练和预测的消息，并接收Worker线程发送回来的消息。

   ```
   1. import { worker } from '@kit.ArkTS';

   3. const workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/MyWorker1.ts');

   5. let done = false;

   7. // 接收Worker子线程的结果
   8. workerInstance.onmessage = (() => {
   9. console.info('MyWorker.ts onmessage');
   10. if (!done) {
   11. workerInstance.postMessage({ 'type': 1, 'value': 0 });
   12. done = true;
   13. }
   14. })

   16. workerInstance.onerror = (() => {
   17. // 接收Worker子线程的错误信息
   18. })

   20. // 向Worker子线程发送训练消息
   21. workerInstance.postMessage({ 'type': 0 });
   ```
3. 在MyWorker.ets文件中绑定Worker对象，当前线程即为Worker线程。在Worker线程中通过注册[onmessage()](../harmonyos-references/js-apis-worker.md#属性-2)回调接收宿主线程发送的消息，并通过调用[postMessage()](../harmonyos-references/js-apis-worker.md#postmessage9-2)方法向宿主线程发送消息。

   例如，在Worker线程中定义预测模型及其训练过程，并与宿主线程进行信息交互。

   ```
   1. import { worker, ThreadWorkerGlobalScope, MessageEvents, ErrorEvent } from '@kit.ArkTS';

   3. let workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   5. // 定义训练模型及结果
   6. let result: Array<number>;

   8. // 定义预测函数
   9. function predict(x: number): number {
   10. return result[x];
   11. }

   13. // 定义优化器训练过程
   14. function optimize(): void {
   15. result = [0];
   16. }

   18. // Worker线程的onmessage逻辑
   19. workerPort.onmessage = (e: MessageEvents): void => {
   20. // 根据传输的数据的type选择进行操作
   21. switch (e.data.type as number) {
   22. case 0:
   23. // 进行训练
   24. optimize();
   25. // 训练之后发送宿主线程训练成功的消息
   26. workerPort.postMessage({ type: 'message', value: 'train success.' });
   27. break;
   28. case 1:
   29. // 执行预测
   30. const output: number = predict(e.data.value as number);
   31. // 发送宿主线程预测的结果
   32. workerPort.postMessage({ type: 'predict', value: output });
   33. break;
   34. default:
   35. workerPort.postMessage({ type: 'message', value: 'send message is invalid' });
   36. break;
   37. }
   38. // 销毁线程
   39. // workerPort.close();
   40. }
   ```
4. 在Worker线程中完成任务后，可以执行销毁操作。销毁方式有两种：一是在宿主线程中销毁Worker线程；二是在Worker线程中主动销毁。

   在宿主线程中通过调用[onexit()](../harmonyos-references/js-apis-worker.md#属性-1)回调定义Worker线程销毁后的处理逻辑。

   ```
   1. // Worker线程销毁后，执行onexit回调方法
   2. workerInstance.onexit = (): void => {
   3. console.info('main thread terminate');
   4. }
   ```

   ```
   1. // Worker线程销毁后，执行onexit回调方法
   2. workerInstance.onexit = (): void => {
   3. console.info('main thread terminate');
   4. }
   ```

   方式一：在宿主线程中通过调用[terminate()](../harmonyos-references/js-apis-worker.md#terminate9)方法销毁Worker线程，并终止Worker接收消息。

   ```
   1. // Index.ets
   2. // 销毁Worker线程
   3. workerInstance.terminate();
   ```

   方式二：在Worker线程中通过调用[close()](../harmonyos-references/js-apis-worker.md#close9)方法主动销毁Worker线程，并终止Worker接收消息。

   ```
   1. // MyWorker.ets
   2. // 销毁线程
   3. workerPort.close();
   ```
