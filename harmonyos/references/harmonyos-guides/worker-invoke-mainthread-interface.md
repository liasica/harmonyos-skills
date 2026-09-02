---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-invoke-mainthread-interface
title: Worker同步调用宿主线程的接口
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > Worker同步调用宿主线程的接口
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f839edafff2687ed0741e888de57368d33d6b53c9b12003de0e37630e10eec8
---

如果一个接口已在宿主线程中实现，Worker可以通过以下方式调用该接口。

以下示例展示了Worker同步调用宿主线程接口的方法，创建Worker的方法可参考[创建Worker的注意事项](worker-introduction.md#创建worker的注意事项)。

1. 首先，在宿主线程实现需要调用的接口，并创建Worker对象，在Worker对象上注册需要调用的对象。

   ```typescript
   import { MessageEvents, worker } from '@kit.ArkTS';
      
      class TestObj {
        public getMessage(): string {
          return 'this is a message from TestObj';
        }
      
        public static testObj: TestObj = new TestObj();
      }
      
      @Entry
      @Component
      struct Index {
        @State message: string = 'Hello World';
      
        build() {
          Row() {
            Column() {
              Text(this.message)
                .fontSize(50)
                .fontWeight(FontWeight.Bold)
                .onClick(() => {
                  // 创建Worker对象
                  const workerInstance: worker.ThreadWorker = new worker.ThreadWorker("entry/ets/workers/Worker.ets");
                  // 在Worker上注册需要调用的对象
                  workerInstance.registerGlobalCallObject('testObj', TestObj.testObj);
                  workerInstance.onmessage = (e: MessageEvents): void => {
                    // 接收Worker子线程的结果
                    console.info('mainThread: ' + e.data);
                    // 销毁Worker
                    workerInstance.terminate();
                  }
                  workerInstance.postMessage('start');
                })
            }
            .width('100%')
          }
          .height('100%')
        }
      }
   ```
2. 然后，在Worker中通过[callGlobalCallObjectMethod](../harmonyos-references/js-apis-worker.md#callglobalcallobjectmethod11)接口可以调用宿主线程中的getMessage()方法。

   ```typescript
   import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

   const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   workerPort.onmessage = (e: MessageEvents) => {
     if (e.data === 'start') {
       try {
         // 调用方法
         let res: string = workerPort.callGlobalCallObjectMethod('testObj', 'getMessage', 0) as string;
         if (res === 'this is a message from TestObj') {
           workerPort.postMessage('run function success.');
         }
       } catch (error) {
         // 异常处理
         console.error('worker: error code is ' + error.code + ' error message is ' + error.message);
       }
     }

     // ...
   }
   ```
