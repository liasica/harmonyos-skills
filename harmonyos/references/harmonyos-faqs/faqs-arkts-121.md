---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-121
title: 如何在Worker中开启多级子线程
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何在Worker中开启多级子线程
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3b330f77b5e4779939729ed3d031b5baa4d55c924cfb63c6da30e2b44c1c6f8
---

在Worker中开启多级子线程，具体可参考如下示例代码：

```ts
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

const workerInstance = new worker.ThreadWorker('entry/ets/pages/Worker.ets');

// The main thread passes information to the worker thread
workerInstance.postMessage('123');

// The main thread receives worker thread information
workerInstance.onmessage = (e: MessageEvents): void => {
  // Data: Information sent by the Worker thread
  let data: string = e.data;
  console.info(`main thread onmessage, data:${data}`);
  const workerInstance1 = new worker.ThreadWorker('entry/ets/pages/Work.ets');
  workerInstance1.postMessage('123');
  workerInstance1.onmessage = (e: MessageEvents): void => {
    // data：Information sent by worker threads
    let data1: string = e.data;
    console.info(`main thread onmessage1, data:${data1}`);
    // Destroy Worker object
    workerInstance1.terminate();
  }
  // After calling terminate, execute onexit
  workerInstance1.onexit = (code) => {
    console.info(`main thread terminate, code:${code}`);
  }
  // Destroy Worker object
  workerInstance.terminate();

}
// After calling terminate, execute onexit
workerInstance.onexit = (code) => {
  console.info(`main thread terminate, code:${code}`);
}

workerInstance.onerror = (err: ErrorEvent) => {
  console.error('main error message ' + err.message);
}
```

```ts
// Work.ets & Worker.ets
import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

// Create an object in the worker thread that communicates with the main thread
const workerPort = worker.workerPort;

// The worker thread receives information from the main thread
workerPort.onmessage = (e: MessageEvents): void => {
  // Data: Information sent by the main thread
  let data: string = e.data;
  console.info(`Work.ets onmessage: data ${data}`);

  // Worker thread sends information to main thread
  workerPort.postMessage('123');
}

// Callback for worker thread error
workerPort.onerror = (err: ErrorEvent) => {
  console.info('Worker.ets onerror' + err.message);
}
```

```ts
"buildOption": {
  "sourceOption": {
    "workers": [
      "./src/main/ets/pages/Worker.ets",
      "./src/main/ets/pages/Work.ets"
    ]
  }
},
```

**参考链接**

[@ohos.worker (启动一个Worker)](../harmonyos-references/js-apis-worker.md)
