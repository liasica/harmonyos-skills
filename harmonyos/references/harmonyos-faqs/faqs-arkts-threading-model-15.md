---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-15
title: 主动取消TaskPool任务的实现
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 主动取消TaskPool任务的实现
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:32+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:77be6af76727b783acec5926cb075d9a7bbc6d3c2662d220c776d4ad01571bcf
---

## 问题现象

在Page页面中使用多个taskpool.execute或taskpool.executePeriodically创建异步任务后，无法主动取消已启动的任务，导致资源浪费或逻辑异常。

## 背景知识

* Taskpool是HarmonyOS系统提供的多线程任务池模块，用于在后台线程执行耗时操作。通过taskpool.execute()可执行一次性任务，taskpool.executePeriodically()可执行周期性任务。
* 从API Version 18起，Task类新增了taskId属性，支持通过任务ID在任意线程中取消任务。而在API Version 18以下，必须持有原始taskpool.Task实例才能调用cancel()方法。

**说明** 

参考文档：[多线程任务取消指南](../harmonyos-guides/multi-thread-cancel-task.md)。

参考文档：[TaskPool API 参考](../harmonyos-references/js-apis-taskpool.md)。

## 解决方案

* **方案一**：API Version 18及以上——使用任务ID取消任务（推荐）。

  步骤说明：

  1. 启动任务时记录任务ID。

     使用taskpool.execute()或taskpool.executePeriodically()启动任务时，会返回一个Task实例，其taskId属性为唯一标识。
  2. 通过taskpool.cancel()方法取消任务。

     在任意线程中调用taskpool.cancel(taskId)，即可取消对应任务。

  **说明** 

  取消后任务不会立即终止。

  取消任务后，任务还会在子线程中继续运行，而且任务存在阻塞的话会一直占用子线程，例如以下示例代码，为了防止while造成死循环而导致子线程占用，需在执行体内部主动检查isCanceled()状态，主动跳出任务，以实现优雅退出，释放子线程资源。

  ```ts
  @Concurrent
  function printArgs(args: number): number {
    while (true) {
      if (taskpool.Task.isCanceled()) {
        hilog.info(0x0000, 'testTag', 'task has been canceled after 2s sleep.');
        return args + 1;
      }
      continue;
    }
  }

  @Concurrent
  function cancelFunction(taskId: number) {
    try {
      taskpool.cancel(taskId);
    } catch (e) {
      hilog.error(0x0000, 'testTag', `taskpool: cancel error code: ${e.code}, info: ${e.message}`);
    }
  }

  function concurrentFuncAfterEighteen() {
    let task = new taskpool.Task(printArgs, 100);
    taskpool.execute(task).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'taskpool catch err: ' + err.message);
    });
    setTimeout(() => {
      hilog.info(0x0000, 'testTag', 'cancel task after Api18');
      let cancelTask = new taskpool.Task(cancelFunction, task.taskId);
      taskpool.execute(cancelTask).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'taskpool catch err: ' + err.message);
      });
    }, 1000);
  }
  ```
* **方案二**：API Version 18以下——使用Task实例引用取消任务。

  步骤说明：

  1. 保存Task实例的引用。

     在启动任务时，必须将返回的Task实例保存在变量中，不能丢弃。
  2. 调用taskpool.cancel()方法取消任务。

     在任意线程中调用taskpool.cancel(task实例)，即可取消对应任务。

  **说明** 

  取消后需在任务体中检查状态。

  与高版本一致，需在任务函数内部定期调用isCanceled()检查是否被取消。

  ```ts
  function concurrentFuncBeforeEighteen() {
    let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
    taskpool.execute(task).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'taskpool catch err: ' + err.message);
    });
    setTimeout(() => {
      try {
        hilog.info(0x0000, 'testTag', 'cancel task before Api18');
        taskpool.cancel(task);
      } catch (e) {
        hilog.error(0x0000, 'testTag', `taskpool: cancel error code: ${e.code}, info: ${e.message}`);
      }
    }, 1000);
  }
  ```

  完整示例参考如下：

  ```ts
  import { hilog } from '@kit.PerformanceAnalysisKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { taskpool } from '@kit.ArkTS';

  @Concurrent
  function printArgs(args: number): number {
    while (true) {
      if (taskpool.Task.isCanceled()) {
        hilog.info(0x0000, 'testTag', 'task has been canceled after 2s sleep.');
        return args + 1;
      }
      continue;
    }
  }

  @Concurrent
  function cancelFunction(taskId: number) {
    try {
      taskpool.cancel(taskId);
    } catch (e) {
      hilog.error(0x0000, 'testTag', `taskpool: cancel error code: ${e.code}, info: ${e.message}`);
    }
  }

  function concurrentFuncAfterEighteen() {
    let task = new taskpool.Task(printArgs, 100);
    taskpool.execute(task).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'taskpool catch err: ' + err.message);
    });
    setTimeout(() => {
      hilog.info(0x0000, 'testTag', 'cancel task after Api18');
      let cancelTask = new taskpool.Task(cancelFunction, task.taskId);
      taskpool.execute(cancelTask).catch((err: BusinessError) => {
        hilog.error(0x0000, 'testTag', 'taskpool catch err: ' + err.message);
      });
    }, 1000);
  }

  function concurrentFuncBeforeEighteen() {
    let task: taskpool.Task = new taskpool.Task(printArgs, 100); // 100: test number
    taskpool.execute(task).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'taskpool catch err: ' + err.message);
    });
    setTimeout(() => {
      try {
        hilog.info(0x0000, 'testTag', 'cancel task before Api18');
        taskpool.cancel(task);
      } catch (e) {
        hilog.error(0x0000, 'testTag', `taskpool: cancel error code: ${e.code}, info: ${e.message}`);
      }
    }, 1000);
  }

  @Entry
  @Component
  struct cancelTaskPool {
    build() {
      Column() {
        Button('AfterApi18')
          .onClick(() => {
            concurrentFuncAfterEighteen();
          }).margin({ bottom: 10 });
        Button('BeforeApi18')
          .onClick(() => {
            concurrentFuncBeforeEighteen();
          }).margin({ bottom: 10 });
      }.width('100%')
      .height('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center);
    }
  }
  ```

## 常见FAQ

Q：为什么取消任务后任务还在执行？

A：cancel()仅设置取消标志，任务需在执行体中主动检查isCanceled()状态并退出。否则任务将继续执行直至完成。

Q：能否在子线程中取消其他线程的任务？

A：可以。从API Version 18起，taskpool.cancelTask(taskId)支持跨线程取消，无需持有Task实例。

Q：任务ID是否全局唯一？

A：是的，taskId在整个应用生命周期内唯一，可用于任务追踪、日志记录或状态管理。
