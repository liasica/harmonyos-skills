---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-103
title: ArkTS实现多Worker实例
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ArkTS实现多Worker实例
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:26+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:2c3d4031b877e1ae704a6bfecc57557dc253d489ee265218a2b3f1ada42a7dd1
---

实现多Worker并进行消息传递，使用registerGlobalCallObject方法传递对象及调用函数，获取缓冲区。注意：callGlobalCallObjectMethod方法在主线程中运行。

1. 在MultipleWorkerInstances.ets文件中调用自定义函数。

   ```
   1. import { testMultyWorker } from './TestWorker'; // Import Method

   3. @Entry
   4. @Component
   5. struct Index {
   6. build() {
   7. Row() {
   8. Column() {
   9. Button('test workers')
   10. .onClick(() => {
   11. testMultyWorker(); // Testing multiple workers
   12. })
   13. }.width('100%')
   14. }.height('100%')
   15. }
   16. }
   ```

   [MultipleWorkerInstances.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/MultipleWorkerInstances.ets#L21-L36)
2. 在TestWorker.ets文件中实现worker的管理调度。

   ```
   1. import { MessageEvents, worker } from '@kit.ArkTS';

   3. const mainThreadTag: string = 'mainthread';

   5. // Initialize 2 workers, if closed or terminated, it cannot be used
   6. let worker1: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker1.ets', { name: 'worker1' });
   7. let worker2: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/worker2.ets', { name: 'worker2' });

   9. // Custom Single Example
   10. class TestObj {
   11. private message: string = 'this is a message from TestObj';

   13. public getMessage(): string {
   14. console.log(mainThreadTag, 'worker call obj func: getMessage()');
   15. return this.message;
   16. }

   18. public getMessageWithInput(str: string): string {
   19. return this.message + 'with input:' + str;
   20. }

   22. public setSharedArrayBuffer() {
   23. let num = new Int16Array(this.sharedBuffer);
   24. num[0] = 20;
   25. }

   27. public getSharedArrayBuffer(): SharedArrayBuffer {
   28. return this.sharedBuffer;
   29. }

   31. static registerObj: TestObj = new TestObj();
   32. private sharedBuffer: SharedArrayBuffer = new SharedArrayBuffer(1024);
   33. }

   35. // Worker's onMessage monitoring
   36. function onMessage(e: MessageEvents): void {
   37. switch (e.data.type as number) {
   38. case 0:
   39. console.log(mainThreadTag, 'received message type: 0, value is: %{public}s, next to post msg to worker2',
   40. e.data.value);
   41. worker2.postMessage('This is msg from mainthread switch');
   42. break;
   43. case 1:
   44. console.log(mainThreadTag, 'received message value %{public}d, next to post msg to worker1',
   45. e.data.value as number);
   46. worker1.postMessage({ 'type': 0 });
   47. break;
   48. default:
   49. console.log(mainThreadTag, 'invalid type, next to return');
   50. // Add a timer to reflect worker operation
   51. setTimeout(() => {
   52. console.log(mainThreadTag, 'invalid type, next to return');
   53. }, 5000);
   54. break;
   55. }
   56. }

   58. // Export function
   59. export function testMultyWorker() {
   60. TestObj.registerObj.setSharedArrayBuffer();
   61. // Register registrant Obj on ThreadWorker instance
   62. worker2.registerGlobalCallObject('myObj', TestObj.registerObj);
   63. worker1.registerGlobalCallObject('myObj', TestObj.registerObj);

   65. console.log(mainThreadTag, 'this is a msg to start worker');
   66. worker1.postMessage('this is a msg to start worker1');

   68. worker1.onmessage = onMessage;
   69. worker2.onmessage = onMessage;

   71. console.log(mainThreadTag, 'end');
   72. worker1.onexit = () => {
   73. console.log('main thread terminate worker1');
   74. }
   75. worker2.onexit = () => {
   76. console.log('main thread terminate worker2');
   77. }
   78. }
   ```

   [TestWorker.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TestWorker.ets#L21-L98)
3. Worker代码如下：

   Worker1.ets：

   ```
   1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker, process } from '@kit.ArkTS';

   3. const worker1: string = 'worker1';
   4. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   6. workerPort.onmessage = (e: MessageEvents) => {
   7. console.log(worker1,'enter worker1, process uid:%{public}d, pid:%{public}d, tid:%{public}d',
   8. process.uid,process.pid,process.tid);

   10. if (e.data.type === 0) {
   11. workerPort.postMessage({ 'type': 2 });
   12. console.log(worker1,'begin to end worker1');
   13. // workerPort.close()  // Do not allow reuse after closing, otherwise it may cause a crash
   14. return;
   15. }

   17. try {
   18. let str1: string = workerPort.callGlobalCallObjectMethod('myObj','getMessage',0) as string;
   19. console.log(worker1,'call shared class to get func: getMessage(), return is: %{public}s',str1);
   20. } catch (e) {
   21. console.log(worker1,'call shared class getMessage get this %{public}s ,errcode %{public}d',e.message,e.code);
   22. }

   24. try {
   25. let res: SharedArrayBuffer =
   26. workerPort.callGlobalCallObjectMethod('myObj','getSharedArrayBuffer',0) as SharedArrayBuffer;
   27. let typedArr = new Int16Array(res);
   28. console.log(worker1,'call shared class func: getSharedArrayBuffer(), return is: %{public}d',typedArr[0]);
   29. typedArr[0] = 25;
   30. console.log(worker1,'work1 change the value to： %{public}d',typedArr[0]);
   31. } catch (e) {
   32. console.log(worker1,'call shared class getSharedArrayBuffer get this %{public}s',e.message);
   33. }

   35. workerPort.postMessage({ 'type': 0,'value': 'this is a msg from worker1 to main' });

   38. workerPort.onmessageerror = (e: MessageEvents) => {
   39. console.log(worker1,'received a message error');
   40. }

   42. workerPort.onerror = (e: ErrorEvent) => {
   43. console.log(worker1,'worker1 error');
   44. }
   45. }
   ```

   [Worker1.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Worker1.ets#L21-L65)

   Worker2.ets：

   ```
   1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker, process } from '@kit.ArkTS';

   3. const worker2: string = 'worker2';
   4. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   6. workerPort.onmessage = (e: MessageEvents) => {
   7. console.log(worker2, 'enter worker2, process update %{public}d,%{public}d,%{public}d', process.uid, process.pid,
   8. process.tid);
   9. let str: string = workerPort.callGlobalCallObjectMethod('myObj', 'getMessage', 0) as string;
   10. console.log(worker2, 'call shared class func get value: %{public}s', str);

   12. let res: SharedArrayBuffer =
   13. workerPort.callGlobalCallObjectMethod('myObj', 'getSharedArrayBuffer', 0) as SharedArrayBuffer;
   14. let typedArr = new Int16Array(res);
   15. console.log(worker2, 'call shared class func get value: %{public}d', typedArr[0]);
   16. workerPort.postMessage({ 'type': 1, 'value': typedArr[0] });
   17. }

   19. workerPort.onmessageerror = (e: MessageEvents) => {
   20. console.log(worker2, 'received a message error');
   21. }

   23. workerPort.onerror = (e: ErrorEvent) => {
   24. console.log(worker2, 'worker2 error');
   25. }
   ```

   [Worker2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Worker2.ets#L21-L45)
