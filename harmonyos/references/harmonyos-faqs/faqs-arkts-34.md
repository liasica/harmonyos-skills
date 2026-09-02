---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-34
title: 在多线程并发场景中，如何实现安全访问同一块共享内存
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 在多线程并发场景中，如何实现安全访问同一块共享内存
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4f35fb913ba19d54a03234508b16e9a43aa44012dc98d34fb9819071aa3eee0d
---

可以使用SharedArrayBuffer对象实现。SharedArrayBuffer对象存储的数据在同时被修改时，必须通过Atomics原子操作确保其同步性，即下一个操作必须在上一个操作完成后才能开始。代码示例：

```ts
// index.ets
import { worker } from '@kit.ArkTS';
let sab = new SharedArrayBuffer(32);
// int32 buffer view for sab
let i32a = new Int32Array(sab);
i32a[0] = 0;
let producer = new worker.ThreadWorker("entry/ets/workers/worker_producer.ets")
producer.postMessage(sab);
let consumer = new worker.ThreadWorker("entry/ets/workers/worker_consumer.ets")
consumer.postMessage(sab);
```

```ts
// worker_producer.ets
import { MessageEvents, worker } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  let sab = e.data as SharedArrayBuffer;
  // view sab buffer in int32 array
  let i32a = new Int32Array(sab);
  console.info("Producer: received sab");
  // Wake up consumers every 2 seconds
  setInterval(() => {
    let length = i32a.length;
    for (let i = 1; i < length; i++) {
      i32a[i] = Math.random() * length;
    }
    Atomics.notify(i32a, 0, 1); // 通知 consumer
  }, 2000);
}
```

```ts
// worker_consumer.ets
import { MessageEvents, worker } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  let sab = e.data as SharedArrayBuffer;
  let i32a = new Int32Array(sab);
  console.info("Consumer: received sab");
  while (true) {
    Atomics.wait(i32a, 0, 0); // This place will be blocked until it wakes up
    let length = i32a.length;
    for (let i = length - 1; i > 0; i--) {
      console.info("arraybuffer " + i + " value is " + i32a[i]);
      i32a[i] = i;
    }
  }
}
```
