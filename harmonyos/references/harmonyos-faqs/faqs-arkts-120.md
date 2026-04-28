---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-120
title: 如何使用TaskPool在子线程调用对象成员函数
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 如何使用TaskPool在子线程调用对象成员函数
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:27+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:7380683f9994ba40c5e2fd478009ed30575e27f1b3510355ef8cb421e645c71d
---

通过将对象Sendable化来使用对象中的方法。具体可参考如下示例代码：

```
1. // TestClass.ets
2. @Sendable
3. export class TestClass {
4. value: number = 888;

6. GetValue(): number {
7. return this.value;
8. }

10. Print(): void {
11. console.info('value:' + this.value);
12. }
13. }
```

[TestClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TestClass.ets#L21-L33)

```
1. // xxx.ets:
2. import { taskpool } from '@kit.ArkTS';
3. import { TestClass } from './TestClass';

5. // Step 1: Define concurrent functions and internally call synchronization methods
6. @Concurrent
7. function func(num: number): number {
8. // Call synchronous wait call implemented in static class objects
9. let testClass = new TestClass();
10. let sum = testClass.GetValue() + num;
11. return sum;
12. }

14. // Step 2: Create a task and execute it
15. function asyncGet(): void {
16. // Create a task and pass it in the function func
17. let task: taskpool.Task = new taskpool.Task(func, 1);
18. // Execute task and operate on the synchronized logic results
19. taskpool.execute(task).then((result: object) => {
20. console.info('testTag result:' + result);
21. });
22. }

24. @Entry
25. @Component
26. struct Index {
27. @State message: string = 'Hello World';

29. build() {
30. Row() {
31. Column() {
32. Text(this.message)
33. .fontSize(50)
34. .fontWeight(FontWeight.Bold)
35. .onClick(() => {
36. // Step 3: Perform concurrent operations
37. asyncGet();
38. })
39. }
40. .width('100%')
41. }
42. .height('100%')
43. }
44. }
```

[EnableSubThreadInTaskPool.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/EnableSubThreadInTaskPool.ets#L21-L65)
