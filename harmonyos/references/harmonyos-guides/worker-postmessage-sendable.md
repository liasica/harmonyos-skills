---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-postmessage-sendable
title: 多级Worker间高性能消息通信
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > 多级Worker间高性能消息通信
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:89d3fb53c16cc15688364a0a9302e24a19f33ed596e7550a194635b03be76ae0
---

多级[Worker](worker-introduction.md)（即通过父Worker创建子Worker的机制形成层级线程关系）间通信是一种常见的需求，由于Worker线程生命周期由用户自行管理，因此需要注意多级Worker生命周期的正确管理，建议开发者确保销毁父Worker前先销毁所有子Worker。

本文介绍如何在多级Worker间实现高性能消息通信。高性能消息通信的关键在于[Sendable对象](arkts-sendable.md)，结合[postMessageWithSharedSendable接口](../harmonyos-references/js-apis-worker.md#postmessagewithsharedsendable12)，可以实现线程间高性能的对象传递。例如，在数据克隆场景中，假设有一个父Worker和两个子Worker。父Worker负责创建子Worker，并向子Worker发送数据克隆任务。子Worker接收任务并执行数据克隆操作，完成后将克隆结果返回给父Worker。

1. 在ets文件夹下新建文件夹Sendable，并准备一个Sendable类CopyEntry，封装克隆任务数据。

   ```
   1. // CopyEntry.ets
   2. @Sendable
   3. export class CopyEntry {
   4. // 克隆类型
   5. type: string;
   6. // 文件路径
   7. filePath: string;
   8. constructor(type: string, filePath: string) {
   9. this.type = type;
   10. this.filePath = filePath;
   11. }
   12. }
   ```
2. 创建两个Worker文件，DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，单击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息。本文以创建“ParentWorker”（父Worker）和“ChildWorker”（子Worker）为例。父Worker负责分发克隆任务，并在所有子Worker任务完成后，依次关闭子Worker，最后关闭自身。子Worker负责接收任务，执行数据克隆操作，并在任务完成后通知父Worker。

   ```
   1. // ParentWorker.ets
   2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker, collections, ArkTSUtils } from '@kit.ArkTS'
   3. import { CopyEntry } from '../Sendable/CopyEntry'

   5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   7. // 计算worker1的任务数量
   8. let count1 = 0;
   9. // 计算worker2的任务数量
   10. let count2 = 0;
   11. // 计算总任务数量
   12. let sum = 0;
   13. // 异步锁
   14. const asyncLock = new ArkTSUtils.locks.AsyncLock();
   15. // 创建子Worker
   16. const copyWorker1 = new worker.ThreadWorker('entry/ets/workers/ChildWorker.ets');
   17. const copyWorker2 = new worker.ThreadWorker('entry/ets/workers/ChildWorker.ets');

   19. workerPort.onmessage = (e : MessageEvents) => {
   20. let array = e.data as collections.Array<CopyEntry>;
   21. sum = array.length;
   22. for (let i = 0; i < array.length; i++) {
   23. let entry = array[i];
   24. if (entry.type === 'copy1') {
   25. count1++;
   26. // 如果是copy1类型，则将数据传递给 copyWorker1
   27. copyWorker1.postMessageWithSharedSendable(entry);
   28. } else if (entry.type === 'copy2') {
   29. count2++;
   30. // 如果是copy2类型，则将数据传递给 copyWorker2
   31. copyWorker2.postMessageWithSharedSendable(entry);
   32. }
   33. }
   34. }

   36. copyWorker1.onmessage = async (e : MessageEvents) => {
   37. console.info('copyWorker1 onmessage:' + e.data);
   38. await asyncLock.lockAsync(() => {
   39. count1--;
   40. if (count1 == 0) {
   41. // 如果copyWorker1的任务全部完成，则关闭copyWorker1
   42. console.info('copyWorker1 close');
   43. copyWorker1.terminate();
   44. }
   45. sum--;
   46. if (sum == 0) {
   47. // 如果所有任务全部完成，则关闭父Worker
   48. workerPort.close();
   49. }
   50. })
   51. }

   53. copyWorker2.onmessage = async (e : MessageEvents) => {
   54. console.info('copyWorker2 onmessage:' + e.data);
   55. await asyncLock.lockAsync(() => {
   56. count2--;
   57. sum--;
   58. if (count2 == 0) {
   59. // 如果copyWorker2的任务全部完成，则关闭copyWorker2
   60. console.info('copyWorker2 close')
   61. copyWorker2.terminate();
   62. }
   63. if (sum == 0) {
   64. // 如果所有任务全部完成，则关闭父Worker
   65. workerPort.close();
   66. }
   67. })
   68. }

   70. workerPort.onmessageerror = (e : MessageEvents) => {
   71. console.error('onmessageerror:' + e.data);
   72. }

   74. workerPort.onerror = (e : ErrorEvent) => {
   75. console.error('onerror:' + e.message);
   76. }
   ```

   ```
   1. // ChildWorker.ets
   2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker} from '@kit.ArkTS'
   3. import { CopyEntry } from '../Sendable/CopyEntry'

   5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   7. workerPort.onmessage = (e : MessageEvents) => {
   8. let data = e.data as CopyEntry;
   9. // 中间copy操作省略
   10. console.info(data.filePath);
   11. workerPort.postMessageWithSharedSendable('done');
   12. }

   14. workerPort.onmessageerror = (e : MessageEvents) => {
   15. console.error('onmessageerror:' + e.data);
   16. }

   18. workerPort.onerror = (e : ErrorEvent) => {
   19. console.error('onerror:' + e.message);
   20. }
   ```
3. 在UI主线程页面，创建父Worker并准备克隆任务所需的数据，准备完成后将数据发送给父Worker。

   ```
   1. // Index.ets
   2. import { worker, collections } from '@kit.ArkTS';
   3. import { CopyEntry } from '../Sendable/CopyEntry'

   5. function promiseCase() {
   6. let p: Promise<void> = new Promise<void>((resolve: Function, reject: Function) => {
   7. setTimeout(() => {
   8. resolve();
   9. }, 100);
   10. });
   11. return p;
   12. }

   14. async function postMessageTest() {
   15. let ss = new worker.ThreadWorker('entry/ets/workers/ParentWorker.ets');
   16. let isTerminate = false;
   17. ss.onexit = () => {
   18. isTerminate = true;
   19. }
   20. let array = new collections.Array<CopyEntry>();
   21. // 准备数据
   22. for (let i = 0; i < 4; i++) {
   23. if (i % 2 == 0) {
   24. array.push(new CopyEntry('copy1', 'file://copy1.txt'));
   25. } else {
   26. array.push(new CopyEntry('copy2', 'file://copy2.txt'));
   27. }
   28. }
   29. // 给Worker线程发送消息
   30. ss.postMessageWithSharedSendable(array);
   31. while (!isTerminate) {
   32. await promiseCase();
   33. }
   34. console.info('Worker线程已退出');
   35. }

   37. @Entry
   38. @Component
   39. struct Index {
   40. @State message: string = 'Hello World';
   41. build() {
   42. Row() {
   43. Column() {
   44. Text(this.message)
   45. .fontSize(50)
   46. .fontWeight(FontWeight.Bold)
   47. .onClick(() => {
   48. postMessageTest();
   49. // ...
   50. })
   51. }
   52. .width('100%')
   53. }
   54. .height('100%')
   55. }
   56. }
   ```
