---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-122
title: 如何在TaskPool和Woker获取上下文Context
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何在TaskPool和Woker获取上下文Context
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e5fd23103234a7a31aaa33b49d0647e0365010fc0f272c64505270e9a86c0b5e
---

Worker线程和TaskPool线程中无法直接获取到组件级的Context 。可以通过主线程参数传递应用级Context，通过[getHostContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md#gethostcontext12)接口获取Context上下文。

```ts
import { hilog } from '@kit.PerformanceAnalysisKit';
import { taskpool } from '@kit.ArkTS';

// Support for ordinary functions and passing of reference parameters as input.
@Concurrent
function printArgs(args: string, uiContext: Context | undefined): string {
  hilog.info(0x0000, 'printArgs', `func: ${args}`);
  hilog.info(0x0000, 'printArgs',
    `Obtain the bundle name of the application: ${uiContext?.applicationInfo.name.toString()}`);
  return args;
}

async function taskpoolExecute(uiContext: Context | undefined): Promise<void> {
  try {
    let task: taskpool.Task = new taskpool.Task(printArgs, 'create task, then execute', uiContext!);
    hilog.info(0x0000, 'taskpoolExecute', 'taskpool.execute(task) result: ' + await taskpool.execute(task));
    hilog.info(0x0000, 'taskpoolExecute',
      'taskpool.execute(function) result: ' + await taskpool.execute(printArgs, 'execute task by func', uiContext!));
  } catch (error) {
    hilog.info(0x0000, 'taskpoolExecute', `taskpool: error code: ${error.code}, info: ${error.message}`);
  }
}

@Entry
@Component
struct TaskPoolGetContext {
  @State message: string = 'Hello World';
  // Obtain the context.
  uiContext = this.getUIContext().getHostContext();

  build() {
    Column() {
      Text(this.message)
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .onClick(() => {
          taskpoolExecute(this.uiContext);
        })
    }
    .width('100%')
    .height('100%')
  }
}
```
