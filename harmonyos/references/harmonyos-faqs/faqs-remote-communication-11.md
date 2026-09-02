---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-11
title: RCP网络请求在TaskPool子线程中使用异常
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > RCP网络请求在TaskPool子线程中使用异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:aeb3bdf4827d491de0ff244f2c1da74f9609297d912f64815a4ebee514df85ce
---

## 问题现象

RCP网络请求库结合TaskPool使用，无法发请求，日志打印undefined is not callable，关键代码示例：

```ts
@Concurrent
function downloadToFile(savePath: string, session: rcp.Session) {
  session.downloadToFile(downloadUrl, downloadToFile).then((response) => {
    console.info(`Succeeded in getting the response ${response}`);
  }).catch((err: BusinessError) => {
    console.error(`DownloadToFile failed, the error message is ${JSON.stringify(err)}`);
  });
}

@Entry
@Component
struct SendReqInTaskPool {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  savePath = this.context.filesDir;
  session = rcp.createSession();

  build() {
    Column() {
      Button('在taskPool内发rcp请求').onClick(() => {
        taskpool.execute(downloadToFile, this.savePath, this.session);
      });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 背景知识

* [RCP](../harmonyos-references/remote-communication-rcp.md)模块提供HTTP数据请求功能。应用程序可通过HTTP发起数据请求。常见的HTTP方法包括GET、POST、HEAD、PUT、DELETE、PATCH、OPTIONS等。
* TaskPool为应用程序提供多线程环境，降低资源消耗并提高系统性能。无需管理线程生命周期。具体接口信息及使用方法，请参见[TaskPool](../harmonyos-references/js-apis-taskpool.md)。
* ArkTS支持线程间通信的对象有[普通对象](../harmonyos-guides/normal-object.md)、ArrayBuffer对象等，详情可见：[序列化支持类型](../harmonyos-references/js-apis-taskpool.md#序列化支持类型)。

## 问题定位

session实例中包含原型及方法，不属于普通对象。

## 分析结论

rcp.createSession创建的实例对象不支持在taskpool.execute传递。

## 修改建议

将session实例的创建放在@Concurrent装饰的函数内即可，修改之后的代码参考如下：

```ts
import { taskpool } from '@kit.ArkTS';
import { rcp } from '@kit.RemoteCommunicationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

@Concurrent
function downloadToFile(savePath: string) {
  let downloadUrl: string = 'xx.xx.xx'; // 开发者自行配置
  let downloadToFile: rcp.DownloadToFile = {
    kind: 'folder',
    path: savePath // 请根据自身业务选择合适的路径
  } as rcp.DownloadToFile;
  const session = rcp.createSession();
  session.downloadToFile(downloadUrl, downloadToFile).then((response) => {
    console.info(`Succeeded in getting the response ${response}`);
  }).catch((err: BusinessError) => {
    console.error(`DownloadToFile failed, the error message is ${JSON.stringify(err)}`);
  });
}

@Entry
@Component
struct SendReqInTaskPool {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  savePath = this.context.filesDir;

  build() {
    Column() {
      Button('在taskPool内发rcp请求').onClick(() => {
        taskpool.execute(downloadToFile, this.savePath);
      });
    }
    .height('100%')
    .width('100%');
  }
}
```

## 总结

异步处理操作主要有Promise、Work线程、TaskPool任务池三种方式。HarmonyOS应用中每个进程都会有一个主线程，除主线程外，还有一类与主线程并行的独立线程Worker，主要用于执行耗时操作，最多可以创建64个Worker。

* 若调用的API有异步接口，不是特别耗时，不阻塞程序后续执行，可使用Promise进行异步操作。
* 若操作非常耗时，可创建Worker处理耗时操作。
* TaskPool主要是为应用程序提供一个多线程的运行环境，不建议在任务中执行阻塞操作，特别是无限期阻塞操作，长时间的阻塞操作占据工作线程，可能会阻塞其他任务调度，影响应用性能。

根据性能要求进行选择，如果仅使用async\Promise等类似协程的方法，耗时操作还是会阻塞主线程UI更新，因为它们是在同一个线程中执行的，同一个线程中就不存在多任务同时执行这样的情况。async\Promise实际上是单线程任务执行顺序排列，执行到耗时操作时(如文件IO、网络IO等)，在执行完之前是执行不了其它任务，所以会阻塞UI刷新。解决办法是通过TaskPool或者Worker去执行耗时操作，执行完后再把数据返回给UI线程。TaskPool和Worker差异参考：[TaskPool和Worker的对比](../harmonyos-guides/taskpool-vs-worker.md)。应用多线程有数量限制，网络请求这块推荐使用Promise.all来进行处理。
