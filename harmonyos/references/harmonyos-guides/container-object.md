---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/container-object
title: 容器类对象
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > 容器类对象
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:56378e129a0eadae93bc03d16ba7ba00d4f5638f82b49e61447235d06df49070
---

容器类对象在跨线程传递时，可通过序列化的机制，确保跨线程间的数据一致，从而实现跨线程数据传递。

目前支持序列化的容器类对象包括[TreeSet](../harmonyos-references/js-apis-treeset.md)，容器类对象中的成员必须是序列化支持的类型，目前序列化支持类型可以参考[线程间通信对象概述](serializable-overview.md)中的相关对象。

说明

* 从HarmonyOS 6.1.0开始，支持使用TreeSet容器类对象实现跨线程数据传递。
* 容器类对象跨线程传递时，只能传递数据，自定义方法会丢失。如果需要自定义方法，则需要使用[@Sendable装饰器](arkts-sendable.md#sendable装饰器)标识为Sendable function后，自定义方法可以跨线程传递。

## 使用示例

```
1. import { taskpool, TreeSet } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Sendable
5. function sendableCompareFunc(firstValue: number, secondValue: number): boolean {
6. return firstValue > secondValue;
7. }

9. @Concurrent
10. function treeSetTestFunc(treeSet: TreeSet<number>) {
11. for (let value of treeSet) {
12. console.info('value:', value);
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. @State message: string = 'Hello World';

21. build() {
22. RelativeContainer() {
23. Text(this.message)
24. .id('HelloWorld')
25. .fontSize(50)
26. .fontWeight(FontWeight.Bold)
27. .alignRules({
28. center: { anchor: '__container__', align: VerticalAlign.Center },
29. middle: { anchor: '__container__', align: HorizontalAlign.Center }
30. })
31. .onClick(() => {
32. // 1. 创建Test实例objA
33. let treeSet: TreeSet<number> = new TreeSet<number>(sendableCompareFunc);

35. treeSet.add(1);
36. treeSet.add(5);
37. treeSet.add(3);
38. treeSet.add(2);
39. // 2. 创建任务task，将treeSet传递给该任务，通过序列化传递给子线程
40. let task = new taskpool.Task(treeSetTestFunc, treeSet);
41. // 3. 执行任务
42. taskpool.execute(task).then(() => {
43. console.info('taskpool: execute task success!');
44. }).catch((e: BusinessError) => {
45. console.error(`taskpool: execute task: Code: ${e.code}, message: ${e.message}`);
46. })
47. this.message = 'success';
48. })
49. }
50. .height('100%')
51. .width('100%')
52. }
53. }
```
