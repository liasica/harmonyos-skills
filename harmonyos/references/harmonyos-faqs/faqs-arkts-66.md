---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-66
title: Worker线程内存如何共享
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > Worker线程内存如何共享
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8481b7c60eae0f3bd5a69f0aed8a214ce925380f5f0cdd427f39eeb9aba14bfb
---

Worker底层采用Actor模型，线程间隔离，内存不共享。要实现内存共享，可以传输SharedArrayBuffer对象。

在使用SharedArrayBuffer对象存储数据时，需要通过原子操作确保同步性，即下一个操作必须在上一个操作完成后开始。

参考代码如下：

1.在Index.ets中创建两个ThreadWorker。

```
1. import { worker } from '@kit.ArkTS';

3. @Component
4. export struct ThreadWorkerView {
5. build() {
6. Column() {
7. Button('测试Worker线程内存共享')
8. .width(200)
9. .onClick(() => {
10. let sab = new SharedArrayBuffer(32);
11. let i32a = new Int32Array(sab);
12. i32a[0] = 0;
13. let producer = new worker.ThreadWorker("entry/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerProducer.ets");
14. producer.postMessage(sab);
15. let consumer = new worker.ThreadWorker("entry/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerConsumer.ets");
16. consumer.postMessage(sab);
17. })
18. }
19. }
20. }
```

[ShareWorkerThreadMemory.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ShareWorkerThreadMemory.ets#L21-L40)

2.在build-profile.json5的buildOption中添加字段。

```
1. "buildOption": {
2. "sourceOption": {
3. "workers": [
4. "./src/main/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerProducer.ets",
5. "./src/main/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerConsumer.ets"
6. ]
7. }
8. },
```

[ShareWorkerThreadMemory.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ShareWorkerThreadMemory.json5#L9-L16)

3.编写worker\_producer.ets脚本。

```
1. import { MessageEvents, worker } from '@kit.ArkTS';

3. const workerPort = worker.workerPort;
4. workerPort.onmessage = (e: MessageEvents): void => {
5. let i32a = new Int32Array(e.data);
6. console.info("Worker Producer: received sab");
7. setInterval(() => {
8. let length = i32a.length;
9. for (let i = 1; i < length; i++) {
10. i32a[i] = Math.random() * length;
11. }
12. Atomics.notify(i32a, 0, 1); // notify customer
13. }, 2000);
14. }
```

[Worker\_producer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Worker_producer.ets#L21-L34)

4.编写worker\_consumer.ets脚本。

```
1. import { MessageEvents, worker } from '@kit.ArkTS';

3. const workerPort = worker.workerPort;
4. workerPort.onmessage = (e: MessageEvents): void => {
5. let i32a = new Int32Array(e.data);
6. console.info("Worker Customer: received sab");
7. while (true) {
8. Atomics.wait(i32a, 0, 0);
9. let length = i32a.length;
10. for (let i = length - 1; i > 0; i--) {
11. console.info("arraybuffer " + i + " value is " + i32a[i]);
12. i32a[i] = i;
13. }
14. }
15. }
```

[Worker\_consumer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Worker_consumer.ets#L21-L35)

**参考链接**

[@ohos.worker (启动一个Worker)](../harmonyos-references/js-apis-worker.md)

[多线程并发概述](../harmonyos-guides/multi-thread-concurrency-overview.md)

[Actor模型](../harmonyos-guides/multi-thread-concurrency-overview.md#actor模型)

[内存共享模型](../harmonyos-guides/multi-thread-concurrency-overview.md#内存共享模型)
