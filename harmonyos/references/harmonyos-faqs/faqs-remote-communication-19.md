---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-19
title: RCP会话实例如何在子线程使用
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > RCP会话实例如何在子线程使用
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4812aadd9bfdb51a7fe064894a5418e1344787d7a7a7de99cfdd81c1c488f635
---

## 问题现象

网络请求属于耗时的I/O操作，而主线程（也叫UI线程/事件循环线程）的核心职责是处理用户交互、UI渲染等对响应速度要求极高的任务。例如打开电商APP加载首页商品列表、打开新闻APP加载头条内容，这些数据都需要从服务器获取。如果在主线程请求，APP可能会出现“启动白屏”、“卡顿”现象。

## 背景知识

* [Worker运作机制](../harmonyos-guides/worker-introduction.md#worker运作机制)：创建Worker的线程称为宿主线程（不局限于主线程，Worker线程也支持创建Worker子线程）。Worker子线程（或Actor线程、工作线程）是Worker自身运行的线程。每个Worker子线程和宿主线程拥有独立的实例，包含独立执行环境、对象、代码段等。Worker子线程和宿主线程通过消息传递机制通信，利用序列化、引用传递或转移所有权的机制完成命令和数据的交互。
* [TaskPool运作机制](../harmonyos-guides/taskpool-introduction.md#taskpool运作机制)：TaskPool支持在宿主线程提交任务到任务队列，系统选择合适的工作线程执行任务，并将结果返回给宿主线程。通过系统统一线程管理，结合动态调度和负载均衡算法，系统默认启动一个任务工作线程，任务多时会自动扩容。工作线程数量上限由设备的物理核数决定，内部管理具体数量，确保调度和执行效率最优。长时间无任务分发时会缩容，减少工作线程数量。

## 解决方案

开发准备，申请获取网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)。

### 场景一：在Worker中进行实现RCP网络请求

1. 参考[Worker基本用法示例](../harmonyos-guides/worker-introduction.md#worker基本用法示例)，创建Worker。
2. 在index.ets文件中，创建多个Worker任务实例，并注册Worker的回调函数，具体代码如下：

   ```ts
   import { ErrorEvent, MessageEvents, worker } from '@kit.ArkTS';

   @Entry
   @Component
   struct Index {
     @State message: string = '请求结果：';

     build() {
       Column({ space: 20 }) {
         Button('发起多线程请求', { type: ButtonType.Normal })
           .width(200)
           .height(45)
           .backgroundColor('#0a59f7')
           .fontColor(Color.White)
           .borderRadius(32)
           .onClick(() => {
             for (let i: number = 0; i < 6; i++) {
               let fileUrl = `entry/ets/workers/Worker.ets`;
               // 创建Worker对象
               let workerInstance = new worker.ThreadWorker(fileUrl);

               // 注册onmessage回调，捕获宿主线程接收到来自其创建的Worker通过workerPort.postMessage接口发送的消息。该回调在宿主线程执行
               workerInstance.onmessage = (e: MessageEvents) => {
                 let data: string = e.data;
                 this.message += data;
                 this.message += ',';
                 console.info('workerInstance onmessage is: ', data);
               };

               // 注册onAllErrors回调，捕获Worker线程的onmessage回调、timer回调以及文件执行等流程产生的全局异常。该回调在宿主线程执行
               workerInstance.onAllErrors = (err: ErrorEvent) => {
                 console.error('workerInstance onAllErrors message is: ' + err.message);
               };

               // 注册onmessageerror回调，当Worker对象接收到无法序列化的消息时被调用，在宿主线程执行
               workerInstance.onmessageerror = () => {
                 console.error('workerInstance onmessageerror');
               };

               // 注册onexit回调，当Worker销毁时被调用，在宿主线程执行
               workerInstance.onexit = (e: number) => {
                 // Worker正常退出时，code为0；异常退出时，code为1
                 console.info('workerInstance onexit code is: ', e);
               };

               // 发送消息给Worker线程
               workerInstance.postMessage(i.toString());
             }
           });

         Text(`${this.message}`)
           .fontSize(14)
           .margin({ top: 20 });
       }
       .width('100%')
       .height('100%')
       .padding(20)
       .justifyContent(FlexAlign.Center);
     }
   }
   ```
3. 在Worker文件中，新建1024个session，具体代码如下：

   ```ts
   import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   import { rcp } from '@kit.RemoteCommunicationKit';

   const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   /**
    * Defines the event handler to be called when the worker thread receives a message sent by the host thread.
    * The event handler is executed in the worker thread.
    *
    * @param event message data
    */
   workerPort.onmessage = (event: MessageEvents) => {
     let data: string = event.data;
     console.info('workerPort onmessage is: ', data);

     console.info("testGetByTask exec by " + data);
     let sessionMap: Map<number, rcp.Session> = new Map<number, rcp.Session>();
     for (let index = 0; index < 1024; index++) {
       try {
         sessionMap.set(index, rcp.createSession());
       } catch (error) {
         workerPort.postMessage(JSON.stringify(error));
         return;
       }
     }

     // 向宿主线程发送消息
     workerPort.postMessage(sessionMap.size.toString());
   };

   /**
    * Defines the event handler to be called when the worker receives a message that cannot be deserialized.
    * The event handler is executed in the worker thread.
    *
    * @param event message data
    */
   workerPort.onmessageerror = (event: MessageEvents) => {
     console.error('workerPort onmessageerror', event.type);
   };

   /**
    * Defines the event handler to be called when an exception occurs during worker execution.
    * The event handler is executed in the worker thread.
    *
    * @param event error message
    */
   workerPort.onerror = (event: ErrorEvent) => {
     console.error('workerPort onerror err is: ', event.message);
   };
   ```

代码运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/ZlyszmwnShy9tbIf-JAU0Q/zh-cn_image_0000002628612498.png "点击放大")

### 场景二：在TaskPool中进行实现RCP网络请求

详细使用示例代码参考[RCP网络请求在TaskPool子线程中使用异常](faqs-remote-communication-11.md)的修改建议章节。

## 常见FAQ

Q：RCP会话实例在Worker和TaskPool中使用的区别是什么？

A：RCP会话实例是基于线程维度设计的，因此该实例可随Worker子进程的终止自动完成回收；而TaskPool中的任务由系统进行统一的线程池管理，线程可能被不同任务复用，不同子任务创建的RCP会话实例数量可能持续累加，最终超出线程规格限制。

Q：RCP会话实例是否可以在主线程创建后作为入参传递给子线程？

A：不可以。原因在于RCP会话实例不属于[ArkTS支持线程间通信的对象](../harmonyos-guides/serializable-overview.md)。因此需要在主线程中将该会话实例的相关配置信息封装为Sendable类型的对象并传递至子线程，再在子线程内基于该配置重新创建RCP会话实例。
