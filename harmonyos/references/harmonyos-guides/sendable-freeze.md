---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-freeze
title: Sendable对象冻结
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > Sendable对象冻结
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6d2026c3a384d92e0927f2f93eb62c2bac0e99a745835f86e4ecee6c9c4f94a7
---

Sendable对象支持冻结操作。冻结后，对象变为只读，不能修改属性。因此，多个并发实例间访问时无需加锁。可以通过调用[Object.freeze](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)接口冻结对象。

说明

不支持在.ets文件中使用Object.freeze接口。

## 使用示例

1. 提供ts文件封装Object.freeze方法。

   ```
   1. // helper.ts
   2. export function freezeObj(obj: any) {
   3. Object.freeze(obj);
   4. }
   ```
2. 调用freeze方法冻结对象，然后将其发送到子线程。

   ```
   1. // SendableFreeze.ets
   2. import { freezeObj } from './helper';
   3. import { worker } from '@kit.ArkTS';

   5. @Sendable
   6. export class GlobalConfig {
   7. // 一些配置属性与方法
   8. init() {
   9. // 初始化相关逻辑
   10. freezeObj(this); // 初始化完成后冻结当前对象
   11. }
   12. }

   14. @Entry
   15. @Component
   16. struct Index {
   17. build() {
   18. Column() {
   19. Text("Sendable freezeObj Test")
   20. .id('HelloWorld')
   21. .fontSize(50)
   22. .fontWeight(FontWeight.Bold)
   23. .onClick(() => {
   24. let gConfig = new GlobalConfig();
   25. gConfig.init();
   26. const workerInstance = new worker.ThreadWorker('entry/ets/workers/Worker.ets', { name: "Worker1" });
   27. workerInstance.postMessage(gConfig);
   28. })
   29. }
   30. .height('100%')
   31. .width('100%')
   32. }
   33. }
   ```
3. 子线程直接操作对象，不加锁。

   ```
   1. // Worker.ets
   2. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   3. import { GlobalConfig } from '../pages/Index';

   5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
   6. workerPort.onmessage = (e: MessageEvents) => {
   7. let gConfig: GlobalConfig = e.data;
   8. // 使用gConfig对象
   9. }
   ```
