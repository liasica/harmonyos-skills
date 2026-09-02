---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-66
title: Worker线程内存如何共享
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > Worker线程内存如何共享
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4defed13d56f6c493938fcfedf5ae44c9d86b428a3434ed97c37598ecd6695e5
---

Worker底层采用Actor模型，线程间隔离，内存不共享。要实现内存共享，可以传输SharedArrayBuffer对象。

在使用SharedArrayBuffer对象存储数据时，需要通过原子操作确保同步性，即下一个操作必须在上一个操作完成后开始。

参考代码如下：

1.在Index.ets中创建两个ThreadWorker。

```ts
import { worker } from '@kit.ArkTS';

@Component
export struct ThreadWorkerView {
  build() {
    Column() {
      Button('测试Worker线程内存共享')
        .width(200)
        .onClick(() => {
          let sab = new SharedArrayBuffer(32);
          let i32a = new Int32Array(sab);
          i32a[0] = 0;
          let producer = new worker.ThreadWorker("entry/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerProducer.ets");
          producer.postMessage(sab);
          let consumer = new worker.ThreadWorker("entry/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerConsumer.ets");
          consumer.postMessage(sab);
        })
    }
  }
}
```

2.在build-profile.json5的buildOption中添加字段。

```ts
"buildOption": {
  "sourceOption": {
    "workers": [
      "./src/main/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerProducer.ets",
      "./src/main/ets/pages/ThreadWorkerSharedArrayBuffer/WorkerConsumer.ets"
    ]
  }
},
```

3.编写worker\_producer.ets脚本。

Atomics.notify(typedArray, index, count)是静态方法可以唤醒一些在等待队列中休眠的代理。typedArray是基于SharedArrayBuffer的Int32Array，index是typedArray中要唤醒的位置，count是要唤醒的休眠代理的数量。

```ts
import { MessageEvents, worker } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  let i32a = new Int32Array(e.data);
  console.info("Worker Producer: received sab");
  setInterval(() => {
    let length = i32a.length;
    for (let i = 1; i < length; i++) {
      i32a[i] = Math.random() * length;
    }
    Atomics.notify(i32a, 0, 1); // notify customer
  }, 2000);
}
```

4.编写worker\_consumer.ets脚本。

Atomics.wait(typedArray, index, value) 静态方法验证共享内存特定位置是否仍然包含给定值，如果是则休眠，直到被唤醒或超时。typedArray是基于SharedArrayBuffer的Int32Array，index是typedArray中要等待的位置，value是测试期望值。

```ts
import { MessageEvents, worker } from '@kit.ArkTS';

const workerPort = worker.workerPort;
workerPort.onmessage = (e: MessageEvents): void => {
  let i32a = new Int32Array(e.data);
  console.info("Worker Customer: received sab");
  while (true) {
    Atomics.wait(i32a, 0, 0);
    let length = i32a.length;
    for (let i = length - 1; i > 0; i--) {
      console.info("arraybuffer " + i + " value is " + i32a[i]);
      i32a[i] = i;
    }
  }
}
```

**参考链接**

[@ohos.worker (启动一个Worker)](../harmonyos-references/js-apis-worker.md)

[多线程并发概述](../harmonyos-guides/multi-thread-concurrency-overview.md)

[Actor模型](../harmonyos-guides/multi-thread-concurrency-overview.md#actor模型)

[内存共享模型](../harmonyos-guides/multi-thread-concurrency-overview.md#内存共享模型)
