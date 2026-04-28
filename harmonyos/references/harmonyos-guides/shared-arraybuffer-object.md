---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/shared-arraybuffer-object
title: SharedArrayBuffer对象
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > SharedArrayBuffer对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e406abadbefb94e7d5b900045b34b9803c00c9cec6e024eae044534af530ab8b
---

SharedArrayBuffer内部包含一块Native内存，其JS对象壳被分配在虚拟机本地堆（LocalHeap）。支持跨并发实例间共享Native内存，但是对共享Native内存的访问及修改需要采用Atomics类，防止数据竞争。SharedArrayBuffer可用于多个并发实例间的状态或数据共享。通信过程如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/x15SIVxuSuWjGqTOOdxmbg/zh-cn_image_0000002583477533.png?HW-CC-KV=V1&HW-CC-Date=20260427T233831Z&HW-CC-Expire=86400&HW-CC-Sign=6E734D8FBE416224DCADB6C967FD6A6ACB63500409AA7C0EC66599700CEF52FD)

## 使用示例

使用TaskPool传递Int32Array对象，实现如下：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function transferAtomics(arg1: Int32Array) {
5. console.info('wait begin::');
6. // 使用Atomics进行操作
7. let res = Atomics.wait(arg1, 0, 0, 3000);
8. return res;
9. }

11. @Entry
12. @Component
13. struct sharedArrayBuffer {
14. @State message: string = 'Hello World';

16. build() {
17. RelativeContainer() {
18. Text(this.message)
19. .id('HelloWorld')
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. .alignRules({
23. center: { anchor: '__container__', align: VerticalAlign.Center },
24. middle: { anchor: '__container__', align: HorizontalAlign.Center }
25. })
26. .onClick(() => {
27. // 定义可共享对象
28. let sab: SharedArrayBuffer = new SharedArrayBuffer(20);
29. let int32 = new Int32Array(sab);
30. let task: taskpool.Task = new taskpool.Task(transferAtomics, int32);
31. taskpool.execute(task).then((res) => {
32. console.info('this res is: ' + res);
33. });
34. setTimeout(() => {
35. Atomics.notify(int32, 0, 1);
36. }, 1000);
37. this.message = 'success';
38. })
39. }
40. .height('100%')
41. .width('100%')
42. }
43. }
```
