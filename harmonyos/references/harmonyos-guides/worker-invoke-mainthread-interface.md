---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/worker-invoke-mainthread-interface
title: Worker同步调用宿主线程的接口
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信场景 > Worker同步调用宿主线程的接口
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0195f2adb299d9f86ef1012e05a40f8a3187b942d88e5299776bc0de1300b35e
---

如果一个接口已在宿主线程中实现，Worker可以通过以下方式调用该接口。

以下示例展示了Worker同步调用宿主线程接口的方法，创建worker的方法可参考[创建worker的注意事项](worker-introduction.md#创建worker的注意事项)。

1. 首先，在宿主线程实现需要调用的接口，并创建Worker对象，在Worker对象上注册需要调用的对象。

   ```
   1. import worker from '@ohos.worker';
   2. import { IconItemSource } from './IconItemSource';

   4. // 创建Worker对象
   5. const workerInstance: worker.ThreadWorker = new worker.ThreadWorker('../workers/Worker');

   7. class PicData {
   8. public iconItemSourceList: IconItemSource[] = [];

   10. public setUp(): string {
   11. for (let index = 0; index < 20; index++) {
   12. const numStart: number = index * 6;
   13. // 此处循环使用6张图片资源
   14. this.iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 1}`));
   15. this.iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 2}`));
   16. this.iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 3}`));
   17. this.iconItemSourceList.push(new IconItemSource('$media:startIcon', `item${numStart + 4}`));
   18. this.iconItemSourceList.push(new IconItemSource('$media:background', `item${numStart + 5}`));
   19. this.iconItemSourceList.push(new IconItemSource('$media:foreground', `item${numStart + 6}`));

   21. }
   22. return 'setUpIconItemSourceList success!';
   23. }
   24. }

   26. @Entry
   27. @Component
   28. struct Index {
   29. @State message: string = 'Hello World';

   31. build() {
   32. RelativeContainer() {
   33. Text(this.message)
   34. .id('HelloWorld')
   35. .fontSize(50)
   36. .fontWeight(FontWeight.Bold)
   37. .alignRules({
   38. center: { anchor: '__container__', align: VerticalAlign.Center },
   39. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   40. })
   41. .onClick(() => {
   42. let picData = new PicData();
   43. // 在Worker上注册需要调用的对象
   44. workerInstance.registerGlobalCallObject('picData', picData);
   45. workerInstance.postMessage('run setUp in picData');
   46. this.message = 'success';
   47. })
   48. }
   49. .height('100%')
   50. .width('100%')
   51. }
   52. }
   ```
2. 然后，在Worker中通过callGlobalCallObjectMethod接口可以调用宿主线程中的getMessage()方法。

   ```
   1. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   2. import { CopyEntry } from '../Sendable/CopyEntry';

   4. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   6. try {
   7. // 调用方法无入参
   8. let res: string = workerPort.callGlobalCallObjectMethod('picData', 'setUp', 0) as string;
   9. console.error('worker: ', res);
   10. } catch (error) {
   11. // 异常处理
   12. console.error('worker: error code is ' + error.code + ' error message is ' + error.message);
   13. }
   ```
