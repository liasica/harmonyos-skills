---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-36
title: ArkTS中Worker线程、Taskpool线程如何与宿主线程通信
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ArkTS中Worker线程、Taskpool线程如何与宿主线程通信
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2cccc3dfe696ead2ec24ac18ed8b4b528eba7b8fa436fa7541853f3611264a4f
---

Worker通过PostMessage向父线程发送任务。TaskPool通过sendData向父线程发送消息，触发任务。

PostMessage接口示例如下：

```ts
import { worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
let buffer = new ArrayBuffer(8);
workerInstance.postMessage(buffer, [buffer]);
```

sendData接口示例如下：

```ts
import { taskpool } from '@kit.ArkTS';

@Concurrent
function ConcurrentFunc(num: number): number {
  let res: number = num * 10;
  taskpool.Task.sendData(res);
  return num;
}
```

**参考链接**

[postMessage](../harmonyos-references/js-apis-worker.md#postmessage9)，[sendData](../harmonyos-references/js-apis-taskpool.md#senddata11)
