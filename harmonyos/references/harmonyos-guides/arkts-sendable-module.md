---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable-module
title: 共享模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > 共享模块
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:052c51d96582e6ad7740fec22df6944b203ce03e41baa81f29a631f69ba32ce5
---

共享模块是进程内只会加载一次的模块，使用"use shared"这一指令来标记一个模块是否为共享模块。

非共享模块在同一线程内只加载一次，而在不同线程中会多次加载，每个线程都会生成新的模块对象。因此，目前只能使用共享模块实现进程单例。

## 约束限制

* "use shared"需要写在ArkTS文件顶层，即写在import语句之后其他语句之前。

  共享属性不具备传递性。非共享模块A即使引入了共享模块B，也不会因此变成共享模块。
* 共享模块只支持ets文件。
* 共享模块内不允许使用[side-effects-import](arkts-module-side-effects.md)。

  共享模块在同一进程内仅加载一次，可在不同线程间共享。

  共享模块加载时，导入的非共享模块不会立即加载。在共享模块内访问依赖的非共享模块导出变量时，当前线程会懒加载对应的非共享模块。非共享模块在线程间隔离，不同线程访问时会进行一次懒加载。

  由于side-effects-import不涉及导出变量，因此不会被加载，也不受支持。

  ```typescript
  // test.ets
  console.info("This runs immediately when imported");
  ```

  ```typescript
  // sharedModule.ets
  // 不允许使用side-effects-import，编译报错
  import "./test";
  'use shared'
  ```
* 共享模块导出的变量必须是可共享对象。

  共享模块在并发实例间可共享，因此导出的所有对象必须是可共享的。可共享对象参考[Sendable支持的数据类型](arkts-sendable.md#sendable支持的数据类型)。
* 共享模块不支持re-export写法。

  ```typescript
  // test.ets
  export let num = 1;
  export let str = 'aaa';
  ```

  ```typescript
  // share.ets
  // 共享模块
  'use shared'
  export * from './test'; // 编译报错
  export {num, str} from './test'; // 可能导致运行时的未知异常
  ```
* 共享模块可以引用其他共享模块或非共享模块，引用和被引用场景没有限制。
* 仅支持使用静态加载、napi\_load\_module或napi\_load\_module\_with\_info加载共享模块。

  ```typescript
  // test.ets
  import { num } from './A'; // 支持静态加载

  import { worker } from '@kit.ArkTS';
  let wk = new worker.ThreadWorker("./A"); // 不支持其他方式加载共享模块, 将产生运行时报错
  ```

  ```typescript
  // A.ets
  'use shared'
  export let num: number = 10;
  ```

## 使用示例

1. 共享模块导出Sendable对象。

   ```typescript
   // 共享模块
   import { ArkTSUtils } from '@kit.ArkTS';

   // 声明当前模块为共享模块，只能导出Sendable数据
   'use shared'

   // 共享模块，singletonA全局唯一
   @Sendable
   class SingletonA {
     private count_: number = 0;
     public lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();

     public async getCount(): Promise<number> {
       return this.lock_.lockAsync(() => {
         return this.count_;
       })
     }

     public async increaseCount() {
       await this.lock_.lockAsync(() => {
         this.count_++;
       })
     }
   }

   export let singletonA = new SingletonA();
   ```
2. 在多个线程中操作共享模块导出的对象。

   ```typescript
   import { ArkTSUtils, taskpool } from '@kit.ArkTS';
   import { singletonA } from './sharedModule';

   // ...

   @Concurrent
   async function increaseCount() {
     await singletonA.increaseCount();
     console.info(`SharedModule: count is: ${await singletonA.getCount()}`);
   }

   @Concurrent
   async function printCount() {
     console.info(`SharedModule: count is: ${await singletonA.getCount()}`);
   }

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';
     @State mainThreadPrint: string = 'MainThread print count';
     @State taskpoolPrint: string = 'Taskpool print count';
     @State mainThreadIncrease: string = 'MainThread increase count';
     @State taskpoolIncrease: string = 'Taskpool increase count';

     build() {
       Row() {
         Column() {
           Button(this.mainThreadPrint)
             .id('MainThread print count')
             .onClick(async () => {
               await printCount();
               this.mainThreadPrint = 'success';
             })
           Button(this.taskpoolPrint)
             .id('Taskpool print count')
             .onClick(async () => {
               await taskpool.execute(printCount);
               this.taskpoolPrint = 'success';
             })
           Button(this.mainThreadIncrease)
             .id('MainThread increase count')
             .onClick(async () => {
               await increaseCount();
               this.mainThreadIncrease = 'success';
             })
           Button(this.taskpoolIncrease)
             .id('Taskpool increase count')
             .onClick(async () => {
               await taskpool.execute(increaseCount);
               this.taskpoolIncrease = 'success';
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
