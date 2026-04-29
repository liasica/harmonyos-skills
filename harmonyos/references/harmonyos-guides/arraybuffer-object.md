---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arraybuffer-object
title: ArrayBuffer对象
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > ArrayBuffer对象
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:db07e24677abb17b490c2243a78881f54e2cf79d1315673fc18ee5589217e978
---

ArrayBuffer包含两部分：底层存储数据的Native内存区域，以及封装操作的JS对象壳。JS对象壳分配在虚拟机的本地堆（LocalHeap）中。跨线程传递时，JS对象壳需要序列化和反序列化拷贝传递，而Native内存区域可以通过拷贝或转移的方式传递。

Native内存使用拷贝方式（递归遍历）传输时，传输后两个线程可以独立访问ArrayBuffer。此方式需要重建JS壳和拷贝Native内存，传输效率较低。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/eIsyPmeDRIaEgBQu9HLwiQ/zh-cn_image_0000002558604366.png?HW-CC-KV=V1&HW-CC-Date=20260429T052634Z&HW-CC-Expire=86400&HW-CC-Sign=2B0F816BB1541DB3D6364B3DCF34612F1C6CFE60D20759BF860A24FE7C0098A1)

Native内存使用转移方式传输时，传输后原线程将无法使用此ArrayBuffer对象。跨线程时只需重建JS壳，Native内存无需拷贝，从而提高效率。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/K0k-BYWLQmmBu6Nf8rFvcQ/zh-cn_image_0000002589323891.png?HW-CC-KV=V1&HW-CC-Date=20260429T052634Z&HW-CC-Expire=86400&HW-CC-Sign=4BEE537CA321A3C8E2DF9184AA2E2AD918114678D373AA272B9BE2CC876DE810)

ArrayBuffer可以用来表示图片等资源，在应用开发中，处理图片（如调整亮度、饱和度、大小等）会比较耗时，为了避免长时间阻塞UI主线程，可以将图片传递到子线程中进行处理。采用转移方式传递ArrayBuffer可提高传输性能，但原线程将无法再访问该ArrayBuffer对象。如果两个线程都需要访问该对象，只能采用拷贝方式。反之，建议采用转移方式以提升性能。

以下将通过具体的代码案例分别介绍拷贝和转移两种方式，实现图片跨ArkTS线程传输。

## ArrayBuffer拷贝传输方式

在ArkTS中，TaskPool传递ArrayBuffer数据时，默认采用转移方式。通过调用setTransferList()接口，可以指定部分数据的传递方式为转移方式，其他部分数据可以切换为拷贝方式。

首先，实现一个处理ArrayBuffer的接口，该接口在Task中执行。

然后，通过拷贝方式将ArrayBuffer数据传递到Task中，并进行处理。

最后，UI主线程接收到Task执行完毕后返回的ArrayBuffer数据，进行拼接并展示。

```
1. import { taskpool } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 在Task执行的处理函数，用于处理ArrayBuffer数据
5. @Concurrent
6. function adjustImageValue(arrayBuffer: ArrayBuffer): ArrayBuffer {
7. // 对arrayBuffer进行操作，返回值默认转移
8. return arrayBuffer;
9. }

11. /*
12. * 创建一个Task，用于将ArrayBuffer传入Task执行
13. * isParamsByTransfer用于控制ArrayBuffer是“拷贝”还是“转移”传递
14. */
15. function createImageTask(arrayBuffer: ArrayBuffer, isParamsByTransfer: boolean): taskpool.Task {
16. let task: taskpool.Task = new taskpool.Task(adjustImageValue, arrayBuffer);
17. if (!isParamsByTransfer) {
18. // 传递空数组[]，全部arrayBuffer参数传递均采用拷贝方式
19. task.setTransferList([]);
20. }
21. return task;
22. }

24. @Entry
25. @Component
26. struct Index {
27. @State message: string = 'Hello World';

29. build() {
30. RelativeContainer() {
31. Text(this.message)
32. .id('HelloWorld')
33. .fontSize(50)
34. .fontWeight(FontWeight.Bold)
35. .alignRules({
36. center: { anchor: '__container__', align: VerticalAlign.Center },
37. middle: { anchor: '__container__', align: HorizontalAlign.Center }
38. })
39. .onClick(() => {
40. // 创建待处理的ArrayBuffer，并按taskNum进行切分
41. let taskNum = 4;
42. let arrayBuffer = new ArrayBuffer(1024 * 1024);
43. let taskPoolGroup = new taskpool.TaskGroup();
44. // 创建taskNum个Task
45. for (let i: number = 0; i < taskNum; i++) {
46. let arrayBufferSlice: ArrayBuffer =
47. arrayBuffer.slice(arrayBuffer.byteLength / taskNum * i, arrayBuffer.byteLength / taskNum * (i + 1));
48. // 使用拷贝方式传入ArrayBuffer，所以isParamsByTransfer为false
49. taskPoolGroup.addTask(createImageTask(arrayBufferSlice, false));
50. }
51. // 执行Task，UI主线程接收处理完成后的结果
52. taskpool.execute(taskPoolGroup).then((data) => {
53. // 将各Task返回的ArrayBuffer数据进行拼接
54. }).catch((e: BusinessError) => {
55. console.error(e.message);
56. })
57. // ...
58. })
59. }
60. .height('100%')
61. .width('100%')
62. }
63. }
```

## ArrayBuffer转移传输方式

在TaskPool中，传递ArrayBuffer数据时，默认使用转移方式，原线程将无法再使用已传输给子线程的ArrayBuffer。 在上文示例的基础上去除task.setTransferList接口调用，即在createImageTask的第二个参数传入true，就可以实现转移方式的传输。
