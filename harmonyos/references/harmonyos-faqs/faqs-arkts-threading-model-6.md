---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-6
title: 如何在多线程中传递Context上下文对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何在多线程中传递Context上下文对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-07-02
content_hash: sha256:95bd21e14b94e9fb6963cfec29406f487e9216010fea76f799f9f1c02177e23a
---

## 问题现象

在使用TaskPool/Worker执行任务时，如何获取应用主进程的Context上下文对象呢?

## 背景知识

* [Context是应用中对象的上下文](../harmonyos-guides/application-context-stage.md)，其提供了应用的一些基础信息，例如resourceManager（资源管理）、applicationInfo（当前应用信息）、dir（应用文件路径）、area（文件分区）等，以及应用的一些基本方法，例如getApplicationContext()等。
* [Transferable对象](../harmonyos-guides/transferabled-object.md)，也称为NativeBinding对象，是指绑定C++对象的JS对象，主体功能由C++提供，其JS对象壳被分配在虚拟机本地堆（LocalHeap）。跨线程传输时复用同一个C++对象，相比于JS对象的拷贝模式，传输效率高。因此，可共享或转移的NativeBinding对象也被称为Transferable对象。
* [workerPort.postMessage](../harmonyos-references/js-apis-worker.md#postmessage9-2)和[postMessageWithSharedSendable](../harmonyos-references/js-apis-worker.md#postmessagewithsharedsendable12-1)都是宿主线程向Worker发送消息的方式，但postMessage只支持[序列化类型](../harmonyos-references/js-apis-worker.md#序列化支持类型)，postMessageWithSharedSendable支持[序列化类型](../harmonyos-references/js-apis-worker.md#序列化支持类型)和[Sendable支持的数据类型](../harmonyos-guides/arkts-sendable.md#sendable支持的数据类型)。
* [SendableContext](../harmonyos-references/js-apis-inner-application-sendablecontext.md)符合Sendable协议，可以与Context对象相互转换，用于ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）的数据传递。

## 解决方案

**一般常见多线程Context传递使用场景中，仅限于对Context中的资源进行读取，如果存在读写，可能存在并发安全问题，需要用到异步锁保证并发安全，不在本文中讨论。**

**一、多线程中传递Context上下文对象有以下常见场景：**

* 子线程读写主线程数据库，需要用到主线程Context对象，创建数据库对象，进行增删改查等操作。
* 子线程需要访问主线程中的资源文件，需要用到主线程Context对象，访问资源文件，处理相关业务。

**二、多线程中传递Context上下文对象有以下方案：**

* 方案一：利用[TaskPool](../harmonyos-guides/taskpool-introduction.md)/[Worker](../harmonyos-guides/worker-introduction.md#worker基本用法示例)序列化接口直接传递Context对象。

  背景知识中提到Context对象是共享模式NativeBinding对象，可以在多线程间共享传递，但是由于JS对象被分配在虚拟机本地堆，所以传递过程还是会存在一定内存开销。
  + Worker传递Context对象：
    1. 主线程中通过postMessage发送Context对象。

       ```ts
       import { worker } from '@kit.ArkTS';
       import { common } from '@kit.AbilityKit';

       @Entry
       @Component
       struct Index {

         build() {
           RelativeContainer() {
             Text('向Worker线程传递上下文对象')
               .fontSize(20)
               .fontWeight(FontWeight.Medium)
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
               .onClick(() => {
                 let workerInstance: worker.ThreadWorker = new worker.ThreadWorker('../workers/Worker.ets');
                 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 try {
                   workerInstance.postMessage(context);
                 } catch (error) {
                   console.error(JSON.stringify(error));
                 }
               })
           }
           .height('100%')
           .width('100%')
         }
       }
       ```
    2. Worker中获取Context对象操作资源文件。

       ```ts
       import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
       import { BusinessError } from '@kit.BasicServicesKit';

       const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

       workerPort.onmessage = (event: MessageEvents) => {
         const contextWorker = event.data as Context;
         try {
           contextWorker.resourceManager.getStringValue($r('app.string.module_desc').id,
             (error: BusinessError, value: string) => {
               if (error != null) {
                 console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
               } else {
                 console.info(`worker msg： ${value}`);
               }
             });
         } catch (error) {
           console.info(JSON.stringify(error));
         }
       };
       ```
  + TaskPool传递Context对象：
    1. 先在主线程中获取对应的Context对象，通过TaskPool序列化接口execute传递。

       ```ts
       @Entry
       @Component
       struct TaskPoolDemo {

         build() {
           RelativeContainer() {
             Text('TaskPool传递Context对象')
               .fontSize(20)
               .fontWeight(FontWeight.Medium)
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
               .onClick(() => {
                 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 taskpool.execute(getStringFromUIThread, context).catch((error: BusinessError) => {
                   console.error(`taskpool execute failed, error code: ${error.code}, message: ${error.message}.`);
                 });
               })
           }
           .height('100%')
           .width('100%')
         }
       }
       ```
    2. 然后在子线程中使用Context对象。

       ```ts
       @Concurrent
       async function getStringFromUIThread(context: Context) {
         try {
           context.resourceManager.getStringValue($r('app.string.module_desc').id, (error: BusinessError, value: string) => {
             if (error != null) {
               console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
             } else {
               console.info(`worker msg： ${value}`);
             }
           });
         } catch (error) {
           console.error(JSON.stringify(error));
         }
       }
       ```
* 方案二：[利用SendableContext传递](../harmonyos-references/js-apis-app-ability-sendablecontextmanager.md)。

  因为SendableContext是遵循@Sendable协议，在底层是进行引用传递，但是如果子线程较多，会存在多份引用，难以维护、管理。
  + Worker传递SendableContext对象：
    1. 主线程传递将Context对象转成SendableContext，通过postMessageWithSharedSendable发送给子线程。

       ```ts
       import { common, sendableContextManager } from '@kit.AbilityKit';
       import { worker } from '@kit.ArkTS';

       @Sendable
       class SendableObject {
         constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
           this.sendableContext = sendableContext;
           this.contextName = contextName;
         }

         sendableContext: sendableContextManager.SendableContext;
         contextName: string;
       }

       @Entry
       @Component
       struct SharedContextWorkerDemo {

         build() {
           RelativeContainer() {
             Text('利用SendableContext传递')
               .fontSize(20)
               .fontWeight(FontWeight.Medium)
               .alignRules({
                 center: { anchor: '__container__', align: VerticalAlign.Center },
                 middle: { anchor: '__container__', align: HorizontalAlign.Center }
               })
               .onClick(() => {
                 let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
                 let workerInstance: worker.ThreadWorker = new worker.ThreadWorker('../workers/TestWorker.ets');
                 let sendableContext: sendableContextManager.SendableContext =
                   sendableContextManager.convertFromContext(context);
                 let object: SendableObject = new SendableObject(sendableContext, 'UIAbilityContext');
                 try {
                   workerInstance.postMessageWithSharedSendable(object);
                 } catch (error) {
                   JSON.stringify(error);
                 }
               })
           }
           .height('100%')
           .width('100%')
         }
       }
       ```
    2. Worker线程接收SendableContext对象并转回Context对象。

       ```ts
       import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
       import { common, sendableContextManager } from '@kit.AbilityKit';
       import { BusinessError } from '@kit.BasicServicesKit';

       @Sendable
       class SendableObject {
         constructor(sendableContext: sendableContextManager.SendableContext, contextName: string) {
           this.sendableContext = sendableContext;
           this.contextName = contextName;
         }

         sendableContext: sendableContextManager.SendableContext;
         contextName: string;
       }

       const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

       workerPort.onmessage = (e: MessageEvents) => {
         let object: SendableObject = e.data;
         let sendableContext: sendableContextManager.SendableContext = object.sendableContext;
         if (object.contextName == 'UIAbilityContext') {
           try {
             let context: common.UIAbilityContext = sendableContextManager.convertToUIAbilityContext(sendableContext);
             context.resourceManager.getStringValue($r('app.string.module_desc').id,
               (error: BusinessError, value: string) => {
                 if (error != null) {
                   console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
                 } else {
                   console.info(`worker msg： ${value}`);
                 }
               });
           } catch (error) {
             console.error(JSON.stringify(error));
           }
         }
       };
       ```
  + TaskPool传递SendableContext对象：

    可以将Context对象直接转成SendableContext对象传给执行函数，在执行函数中再转成Context。

    ```ts
    import { common, sendableContextManager } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { taskpool } from '@kit.ArkTS';

    @Concurrent
    async function getCacheDir(sendableContext: sendableContextManager.SendableContext) {
      const contextTask: common.UIAbilityContext = sendableContextManager.convertToUIAbilityContext(sendableContext);
      // 直接使用getContext方法时，主线程调用获取Context对象并可正常打印。子线程调用时无法获取Context对象
      try {
        contextTask.resourceManager.getStringValue($r('app.string.module_desc').id,
          (error: BusinessError, value: string) => {
            if (error != null) {
              console.error(`callback getStringValue failed, error code: ${error.code}, message: ${error.message}.`);
            } else {
              console.info(`worker msg： ${value}`);
            }
          });
      } catch (error) {
        console.error(JSON.stringify(error));
      }
    }

    @Entry
    @Component
    struct SharedContextTaskPoolDemo {

      build() {
        RelativeContainer() {
          Text('TaskPool传递SendableContext对象')
            .fontSize(20)
            .fontWeight(FontWeight.Medium)
            .alignRules({
              center: { anchor: '__container__', align: VerticalAlign.Center },
              middle: { anchor: '__container__', align: HorizontalAlign.Center }
            })
            .onClick(() => {
              let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
              let sendableContext = sendableContextManager.convertFromContext(context);
              taskpool.execute(getCacheDir, sendableContext).catch((error: BusinessError) => {
                console.error(`taskpool execute failed, error code: ${error.code}, message: ${error.message}.`);
              });
            })
        }
        .height('100%')
        .width('100%')
      }
    }
    ```

* 方案三：使用[共享模块](../harmonyos-guides/arkts-sendable-module.md)，实现一个单例类。在模块方法中将实例化的Context并转换为[SendableContext](../harmonyos-references/js-apis-app-ability-sendablecontextmanager.md#sendablecontextmanagerconvertfromcontext)，最后导出Sendable对象，在子线程中使用。

  该方案既保证了Context可以引用传递，减少内存开销，又避免了Context对象在多个线程间进行引用。
  1. 实现共享模块的单例Context类。

     ```ts
     import { sendableContextManager } from '@kit.AbilityKit';

     // 声明当前模块为共享模块，只能导出可Sendable数据
     'use shared'

     // 共享模块，SingletonA全局唯一
     @Sendable
     class SingletonShareContext {
       private sendableContext: sendableContextManager.SendableContext | undefined;

       init(context: Context) {
         if (!this.sendableContext) {
           this.sendableContext = sendableContextManager.convertFromContext(context);
         }
       }

       // 返回sendableContext对象
       public getContext() {
         if (this.sendableContext === undefined) {
           console.error('sendableContext未初始化');
         }
         return this.sendableContext;
       }
     }

     export const singletonShareContext = new SingletonShareContext();
     ```
  2. 在多线程业务代码中引用单例类，进行Context对象的使用。

     ```ts
     import { taskpool } from '@kit.ArkTS';
     import { common, sendableContextManager } from '@kit.AbilityKit';
     import { singletonShareContext } from './SingletonShareContext';
     import { BusinessError } from '@kit.BasicServicesKit';

     @Concurrent
     async function printContext() {
       // 将SendableContext对象转换为Context
       let context: common.Context = sendableContextManager.convertToUIAbilityContext(singletonShareContext.getContext()!);
       // 主线程和子线程调用时均可正常打印
       console.info('sendableContextManager:' + context.cacheDir);
     }

     @Entry
     @Component
     struct SingletonSharedDemo {

       aboutToAppear(): void {
         singletonShareContext.init(this.getUIContext().getHostContext()!);
       }

       build() {
         Row() {
           Column({ space: 10 }) {
             Button('MainThread print')
               .onClick(async () => {
                 console.info('MainThread print');
                 printContext();
               })
             Button('TaskPool print')
               .onClick(() => {
                 console.info('Taskpool print');
                 taskpool.execute(printContext).catch((error: BusinessError) => {
                   console.error(JSON.stringify(error));
                 });
               })
           }
           .width('100%')
         }
         .height('100%')
       }
     }
     ```

## 常见FAQ

Q：为什么通过postMessage将SendableContext传递到Worker会报错？

A：postMessage只支持序列化对象。SendableContext对象是Sendable支持的数据类型，需要通过postMessageWithSharedSendable进行发送。

Q：postMessageWithSharedSendable和postMessage区别？

A：postMessage：宿主线程通过转移对象所有权或者拷贝数据的方式向Worker线程发送消息。

postMessageWithSharedSendable：宿主线程向Worker线程发送消息，消息中的Sendable对象通过引用传递，非Sendable对象通过序列化传递。

## 总结

|  | 方案一 | 方案二 | 方案三 |
| --- | --- | --- | --- |
| 优点 | 简单易用、接口简单 | 通过引用传递，减少了程序开销 | 减少了程序开销，同时也避免引用次数过多，便于管理 |
| 缺点 | 直接拷贝传递Context对象存在一定程序开销 | 但是如果线程过多，线程间引用较多，难以维护 | 实现稍复杂，不适合用于Context传递较少的场景 |
| 适用场景 | 子线程读取rawfile目录的资源文件 | 子线程读取rawfile目录的资源文件 | 子线程频繁读取主线程创建的数据库 |

对于Context传递不频繁的场景，优先选择方案二；对于Context传递频繁的场景，优先选择方案三。
