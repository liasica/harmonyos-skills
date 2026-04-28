---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-58
title: TaskPool线程内存如何共享
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > TaskPool线程内存如何共享
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bd381080071ed593a203860310e8236b79b0648a9b7af026e450e3c2698d9450
---

TaskPool 底层采用 Actor 模型，线程间隔离，不共享内存。可以通过传输 SharedArrayBuffer 对象实现内存共享。

需要注意，SharedArrayBuffer对象存储的数据在同时被修改时，必须通过原子操作确保同步，即下一个操作开始前，上一个操作必须已完成。

参考代码如下：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function producer(ArrayBuffer: Int32Array): void {
5. let i32a = ArrayBuffer;
6. console.info("Producer: received sab");
7. setInterval(() => {
8. let length = i32a.length;
9. for (let i = 1; i < length; i++) {
10. i32a[i] = Math.random() * length;
11. }
12. Atomics.notify(i32a, 0, 1); // notify customer
13. }, 2000);
14. }

16. @Concurrent
17. function consumer(ArrayBuffer: Int32Array): void {
18. let i32a = ArrayBuffer;
19. console.info("Customer: received sab");
20. while (true) {
21. Atomics.wait(i32a, 0, 0);
22. let length = i32a.length;
23. for (let i = length - 1; i > 0; i--) {
24. console.info("arraybuffer " + i + " value is " + i32a[i]);
25. i32a[i] = i;
26. }
27. }
28. }

30. function ArrayBufferShared(ArrayBuffer: Int32Array): void {
31. let group: taskpool.TaskGroup = new taskpool.TaskGroup();
32. group.addTask(consumer, ArrayBuffer);
33. group.addTask(producer, ArrayBuffer);
34. taskpool.execute(group, taskpool.Priority.HIGH).then((res: Object) => {
35. // Result array summary processing
36. })
37. }

39. @Component
40. export struct TestArrayBufferSharedView {
41. build() {
42. Row() {
43. Column() {
44. Text('Click')
45. .fontSize(50)
46. .fontWeight(FontWeight.Bold)
47. .onClick(() => {
48. let sab = new SharedArrayBuffer(32);
49. let i32a = new Int32Array(sab);
50. ArrayBufferShared(i32a);
51. })
52. }
53. .width('100%')
54. }
55. .height('100%')
56. }
57. }
```

[ShareTaskPoolThreadMemory.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/ShareTaskPoolThreadMemory.ets#L21-L77)

**参考链接**

[@ohos.taskpool（启动任务池）](../harmonyos-references/js-apis-taskpool.md)

[多线程并发概述](../harmonyos-guides/multi-thread-concurrency-overview.md)
