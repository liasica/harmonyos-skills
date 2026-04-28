---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-34
title: 在多线程并发场景中，如何实现安全访问同一块共享内存
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 在多线程并发场景中，如何实现安全访问同一块共享内存
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:09795cad9b76d5c26c5f26e9e8ebe5adee4d688134d4de3098e163effd7d03a8
---

可以使用SharedArrayBuffer对象实现。SharedArrayBuffer对象存储的数据在同时被修改时，必须通过Atomics原子操作确保其同步性，即下一个操作必须在上一个操作完成后才能开始。代码示例：

```
1. // index.ets
2. import { worker } from '@kit.ArkTS';
3. let sab = new SharedArrayBuffer(32);
4. // int32 buffer view for sab
5. let i32a = new Int32Array(sab);
6. i32a[0] = 0;
7. let producer = new worker.ThreadWorker("entry/ets/workers/worker_producer.ets")
8. producer.postMessage(sab);
9. let consumer = new worker.ThreadWorker("entry/ets/workers/worker_consumer.ets")
10. consumer.postMessage(sab);
```

[SecureAccessShared.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SecureSharedMemoryBlock/SecureAccessShared.ets#L21-L30)

```
1. // worker_producer.ets
2. import { MessageEvents, worker } from '@kit.ArkTS';

4. const workerPort = worker.workerPort;
5. workerPort.onmessage = (e: MessageEvents): void => {
6. let sab = e.data as SharedArrayBuffer;
7. // view sab buffer in int32 array
8. let i32a = new Int32Array(sab);
9. console.info("Producer: received sab");
10. // Wake up consumers every 2 seconds
11. setInterval(() => {
12. let length = i32a.length;
13. for (let i = 1; i < length; i++) {
14. i32a[i] = Math.random() * length;
15. }
16. Atomics.notify(i32a, 0, 1); // 通知 consumer
17. }, 2000);
18. }
```

[Worker\_producer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SecureSharedMemoryBlock/Worker_producer.ets#L21-L38)

```
1. // worker_consumer.ets
2. import { MessageEvents, worker } from '@kit.ArkTS';

4. const workerPort = worker.workerPort;
5. workerPort.onmessage = (e: MessageEvents) => {
6. let sab = e.data as SharedArrayBuffer;
7. let i32a = new Int32Array(sab);
8. console.info("Consumer: received sab");
9. while (true) {
10. Atomics.wait(i32a, 0, 0); // This place will be blocked until it wakes up
11. let length = i32a.length;
12. for (let i = length - 1; i > 0; i--) {
13. console.info("arraybuffer " + i + " value is " + i32a[i]);
14. i32a[i] = i;
15. }
16. }
17. }
```

[Worker\_consumer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/SecureSharedMemoryBlock/Worker_consumer.ets#L21-L37)
