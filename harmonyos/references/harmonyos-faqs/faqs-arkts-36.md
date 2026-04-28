---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-36
title: ArkTS中Worker线程、TaskPool线程如何与宿主线程通信
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ArkTS中Worker线程、TaskPool线程如何与宿主线程通信
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:22+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1a6ce37e6e3922bf3c9e114be5603eb181459f1fb871b24bf25f802d735ea51e
---

Worker通过PostMessage向父线程发送任务。TaskPool通过sendData向父线程发送消息，触发任务。

PostMessage接口示例如下：

```
1. import { worker } from '@kit.ArkTS';

3. const workerInstance = new worker.ThreadWorker("entry/ets/workers/worker.ets");
4. let buffer = new ArrayBuffer(8);
5. workerInstance.postMessage(buffer, [buffer]);
```

[CommunicateHostThread.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CommunicateHostThread.ets#L21-L25)

sendData接口示例如下：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function ConcurrentFunc(num: number): number {
5. let res: number = num * 10;
6. taskpool.Task.sendData(res);
7. return num;
8. }
```

[CommunicateHostThread2.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/CommunicateHostThread2.ets#L21-L28)

**参考链接**

[postMessage](../harmonyos-references/js-apis-worker.md#postmessage9)，[sendData](../harmonyos-references/js-apis-taskpool.md#senddata11)
