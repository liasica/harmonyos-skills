---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-46
title: 如何将类Java语言的线程模型（内存共享）的实现方式转换成在ArkTS的线程模型下（内存隔离）的实现方式
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将类Java语言的线程模型（内存共享）的实现方式转换成在ArkTS的线程模型下（内存隔离）的实现方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:1a44868e1cfc508f853a3c9865d923c1b2b64781754f0293cf2f7e6f3e7bc9da
---

可以利用TaskPool接口转换，具体分为以下四个场景：

* 场景一：主线程将独立任务放到子线程执行。代码示例：

  共享内存写法：

  ```ts
  class Task {
    static run(args) {
      // Do some independent tasks
    }
  }
  let thread = new Thread(() => {
    let result = Task.run(args)
    // deal with result
  })
  ```

  ArkTS写法：

  ```ts
  import { taskpool } from '@kit.ArkTS';

  @Concurrent
  function run(args: number) {
    // Do some independent tasks
  }
  let task: taskpool.Task = new taskpool.Task(run, 100); // 100: test number
  taskpool.execute(task).then((res) => {
    // Return result
  });
  ```
* 场景二：主线程在子线程使用类对象实例。代码示例：

  共享内存写法：

  ```ts
  class Material {
    action(args) {
      // Do some independent tasks
    }
  }
  let material = new Material()
  let thread = new Thread(() => {
    let result = material.action(args)
    // deal with result
  })
  ```

  ArkTS写法：

  ```ts
  import { taskpool } from '@kit.ArkTS';

  @Concurrent
  function runner(material: Material): void {
    return material.action(100); // 100: test number
  }
  @Sendable
  class Material {
    action(args: number) {
      // Do some independent tasks
    }
  }
  let material = new Material()
  taskpool.execute(runner, material).then((ret) => {
    // Return result
  })
  ```
* 场景三：子线程更新主线程状态。代码示例：

  共享内存写法：

  ```ts
  class Task {
      run(args) {
          // deal with result
          runOnUiThread(() => {
              UpdateUI(result)
          })
      }
  }
  let task = new Task()
  let thread = new Thread(() => {
      let result = task.run(args)
      // Processing results
  })
  ```

  ArkTS写法：

  ```ts
  import taskpool from '@ohos.taskpool'

  // let result: Object[] | undefined = undefined

  @Concurrent
  function runner(task:Task) {
    task.run()
  }
  @Sendable
  class Task {
    run(args?: Object[] | undefined) {
      // Do some independent tasks
      taskpool.Task.sendData(JsResult)
    }
  }
  let task = new Task()
  let run = new taskpool.Task(runner, task)
  run.onReceiveData((result?: Function | undefined) => {
    UpdateUI(result)
  })
  taskpool.execute(run).then((ret) => {
    // Return result
  })
  ```
* 场景四：子线程同步调用主线程接口。代码示例：

  ```ts
  class SdkU3d {
      static getInst() {
          return SdkMgr.getInst();
      }
      getPropStr(str: string) {
          return xx;
      }
  }
  let thread = new Thread(() => {
      // In the game thread
      let sdk = SdkU3d.getInst()
      let ret = sdk.getPropStr("xx")
  })
  ```

  ArkTS写法：

  ```ts
  import { MessageEvents, taskpool, worker } from '@kit.ArkTS';
  class SdkU3d {
    static getInst(): Object {
      return SdkMgr.getInst();
    }
    getPropStr(str: string) { }
  }
  let workerInstance = new worker.ThreadWorker("xx/worker.ts");
  workerInstance.registerGlobalCallObject("instance_xx", SdkU3d.getInst());
  workerInstance.postMessage("start");
  // In the game worker thread
  const mainPort = worker.workerPort;
  mainPort.onmessage = (e: MessageEvents): void => {
    let ret = mainPort.callGlobalCallObjectMethod("instance_xx", "getPropStr", 100); // 100: test number
  }
  ```

**参考链接**

[并发概述](../harmonyos-guides/concurrency-overview.md)
