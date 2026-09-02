---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-freeze
title: Sendable对象冻结
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > Sendable对象冻结
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:15ce5c0cc2b069fd620f713f17e41e59ec089af23bda6379b9b52cd596a05aed
---

Sendable对象支持冻结操作。冻结后，对象变为只读，不能修改属性。因此，多个并发实例间访问时无需加锁。可以通过调用[Object.freeze](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)接口冻结对象。

**说明** 

不支持在.ets文件中使用Object.freeze接口。

## 使用示例

1. 提供ts文件封装Object.freeze方法。

   ```typescript
   export function freezeObj(obj: any) {
     Object.freeze(obj);
   }
   ```
2. 调用freeze方法冻结对象，然后将其发送到子线程。

   ```typescript
   import { freezeObj } from './helper';
   import { worker } from '@kit.ArkTS';

   @Sendable
   export class GlobalConfig {
     // 一些配置属性与方法
     init() {
       // 初始化相关逻辑
       freezeObj(this); // 初始化完成后冻结当前对象
     }
   }

   @Entry
   @Component
   struct Index {
     @State message: string = 'Sendable freezeObj Test';

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize(50)
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             let gConfig = new GlobalConfig();
             gConfig.init();
             const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: 'Worker1' });
             workerInstance.postMessage(gConfig);
             this.message = 'success';
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
3. 子线程直接操作对象，不加锁。

   ```typescript
   import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   // import { GlobalConfig } from '../pages/Index';
   import { GlobalConfig } from '../managers/SendableFreeze';

   const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
   workerPort.onmessage = (e: MessageEvents) => {
     let gConfig: GlobalConfig = e.data;
     // 使用gConfig对象
   }
   ```
