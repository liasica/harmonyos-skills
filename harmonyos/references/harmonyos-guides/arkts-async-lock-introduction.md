---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-async-lock-introduction
title: 异步锁
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > 异步锁
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ba8a70fa97fcda408f446ee93a48bb7477bfec1123daa68ae5ccb872d5bafe47
---

为了解决多线程并发实例间的数据竞争问题，ArkTS引入了异步锁能力。异步锁可能会被类对象持有，因此为了更方便地在并发实例间获取同一个异步锁对象，[AsyncLock对象](../harmonyos-references/arkts-apis-arkts-utils-locks.md#asynclock)支持跨线程引用传递。

由于ArkTS语言支持异步操作，阻塞锁容易产生死锁问题，因此在ArkTS中仅支持异步锁（非阻塞式锁）。同时，异步锁还可以用于保证单线程内的异步任务时序一致性，防止因异步任务执行顺序不确定而导致的数据竞争问题。

更多异步锁相关接口，请参见[异步锁ArkTSUtils.locks](../harmonyos-references/arkts-apis-arkts-utils-locks.md)。

说明

使用异步锁的方法需标记为async，调用时需用await修饰，以确保时序正确。

## 使用示例

为了防止[@Sendable共享对象](arkts-sendable.md)在不同线程中修改共享变量导致的竞争问题，可以使用异步锁保护数据。示例如下：

```
1. import { ArkTSUtils, taskpool } from '@kit.ArkTS';

3. @Sendable
4. export class A {
5. private count_: number = 0;
6. lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();

8. public getCount(): Promise<number> {
9. // 对需要保护的数据加异步锁
10. return this.lock_.lockAsync(() => {
11. return this.count_;
12. })
13. }

15. public async increaseCount() {
16. // 对需要保护的数据加异步锁
17. await this.lock_.lockAsync(() => {
18. this.count_++;
19. })
20. }
21. }

23. @Concurrent
24. async function printCount(a: A) {
25. a.increaseCount();
26. console.info("InputModule: count is:" + await a.getCount());
27. }

29. @Entry
30. @Component
31. struct Index {
32. @State message: string = 'Hello World';

34. build() {
35. RelativeContainer() {
36. Text(this.message)
37. .id('HelloWorld')
38. .fontSize(50)
39. .fontWeight(FontWeight.Bold)
40. .alignRules({
41. center: { anchor: '__container__', align: VerticalAlign.Center },
42. middle: { anchor: '__container__', align: HorizontalAlign.Center }
43. })
44. .onClick(async () => {
45. // 创建sendable对象a
46. let a: A = new A();
47. // 将实例a传递给子线程
48. await taskpool.execute(printCount, a);
49. })
50. }
51. .height('100%')
52. .width('100%')
53. }
54. }
```
