---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-sendable-module
title: 共享模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > 共享模块
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:54c8667ea42541e75aeb118a42a812359efa222c7fc1849331530ea0c68e11a4
---

共享模块是进程内只会加载一次的模块，使用"use shared"这一指令来标记一个模块是否为共享模块。

非共享模块在同一线程内只加载一次，而在不同线程中会多次加载，每个线程都会生成新的模块对象。因此，目前只能使用共享模块实现进程单例。

## 约束限制

* "use shared"需要与"use strict"一样写在ArkTS文件顶层，写在import语句之后其他语句之前。

  共享属性不具备传递性。非共享模块A即使引入了共享模块B，也不会因此变成共享模块。
* 共享模块只支持ets文件。
* 共享模块内不允许使用side-effects-import。

  共享模块在同一进程内仅加载一次，可在不同线程间共享。

  共享模块加载时，导入的非共享模块不会立即加载。在共享模块内访问依赖的非共享模块导出变量时，当前线程会懒加载对应的非共享模块。非共享模块在线程间隔离，不同线程访问时会进行一次懒加载。

  由于side-effects-import不涉及导出变量，因此不会被加载，也不受支持。

  ```
  1. // test.ets
  2. console.info("This runs immediately when imported");
  ```

  ```
  1. // sharedModule.ets
  2. // 不允许使用side-effects-import，编译报错
  3. import "./test";
  4. "use shared"
  ```
* 共享模块导出的变量必须是可共享对象。

  共享模块在并发实例间可共享，因此导出的所有对象必须是可共享的。可共享对象参考[Sendable支持的数据类型](arkts-sendable.md#sendable支持的数据类型)。
* 共享模块不支持re-export写法。

  ```
  1. // test.ets
  2. export let num = 1;
  3. export let str = 'aaa';
  ```

  ```
  1. // share.ets
  2. // 共享模块
  3. 'use shared'
  4. export * from './test'; // 编译报错
  5. export {num, str} from './test'; // 产生运行时报错
  ```
* 共享模块可以引用其他共享模块或非共享模块，引用和被引用场景没有限制。
* 仅支持使用静态加载、napi\_load\_module或napi\_load\_module\_with\_info加载共享模块。

  ```
  1. // test.ets
  2. import { num } from './A'; // 支持静态加载

  4. import { worker } from '@kit.ArkTS';
  5. let wk = new worker.ThreadWorker("./A"); // 不支持其他方式加载共享模块, 将产生运行时报错
  ```

  ```
  1. // A.ets
  2. 'use shared'
  3. export let num: number = 10;
  ```

## 使用示例

1. 共享模块导出Sendable对象。

   ```
   1. // 共享模块sharedModule.ets
   2. import { ArkTSUtils } from '@kit.ArkTS';

   4. // 声明当前模块为共享模块，只能导出可Sendable数据
   5. "use shared"

   7. // 共享模块，SingletonA全局唯一
   8. @Sendable
   9. class SingletonA {
   10. private count_: number = 0;
   11. lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock()

   13. public async getCount(): Promise<number> {
   14. return this.lock_.lockAsync(() => {
   15. return this.count_;
   16. })
   17. }

   19. public async increaseCount() {
   20. await this.lock_.lockAsync(() => {
   21. this.count_++;
   22. })
   23. }
   24. }

   26. export let singletonA = new SingletonA();
   ```
2. 在多个线程中操作共享模块导出的对象。

   ```
   1. import { taskpool } from '@kit.ArkTS';
   2. import { singletonA } from './sharedModule';

   4. @Concurrent
   5. async function increaseCount() {
   6. await singletonA.increaseCount();
   7. console.info("SharedModule: count is:" + await singletonA.getCount());
   8. }

   10. @Concurrent
   11. async function printCount() {
   12. console.info("SharedModule: count is:" + await singletonA.getCount());
   13. }

   15. @Entry
   16. @Component
   17. struct Index {
   18. @State message: string = 'Hello World';

   20. build() {
   21. Row() {
   22. Column() {
   23. Button("MainThread print count")
   24. .onClick(async () => {
   25. await printCount();
   26. })
   27. Button("Taskpool print count")
   28. .onClick(async () => {
   29. await taskpool.execute(printCount);
   30. })
   31. Button("MainThread increase count")
   32. .onClick(async () => {
   33. await increaseCount();
   34. })
   35. Button("Taskpool increase count")
   36. .onClick(async () => {
   37. await taskpool.execute(increaseCount);
   38. })
   39. }
   40. .width('100%')
   41. }
   42. .height('100%')
   43. }
   44. }
   ```
