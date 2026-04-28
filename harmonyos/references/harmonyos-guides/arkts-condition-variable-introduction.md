---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-condition-variable-introduction
title: 异步等待
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > 异步等待
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e0edea3140ac7f6c05f12c5c47f3e6cebca3f7593241d420a8be317589fbf17d
---

ArkTS引入了异步任务的等待和唤醒能力，以解决多线程任务时序控制问题。异步任务通过[ConditionVariable](../harmonyos-references/arkts-apis-arkts-utils-locks.md#conditionvariable18)对象实现等待和唤醒机制，该对象支持跨线程引用传递。

ArkTS语言支持异步操作，现已增加异步任务的等待和唤醒功能。当异步任务收到唤醒通知或等待超时后，将继续执行。

说明

使用异步方法需标记为async，调用时需用await修饰，确保时序正确。

## 使用示例

[Sendable](arkts-sendable.md)共享对象在不同线程控制异步任务等待和唤醒的示例如下：

```
1. import { ArkTSUtils, taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function notifyAll(conditionVariable: ArkTSUtils.locks.ConditionVariable) {
5. console.info(`TaskPool Thread notifyAll`);
6. conditionVariable.notifyAll();
7. }

9. @Concurrent
10. function notifyOne(conditionVariable: ArkTSUtils.locks.ConditionVariable) {
11. console.info(`TaskPool Thread notifyOne`);
12. conditionVariable.notifyOne();
13. }

15. @Concurrent
16. async function wait(conditionVariable: ArkTSUtils.locks.ConditionVariable) {
17. await conditionVariable.wait();
18. console.info(`TaskPool Thread Wait: success`);
19. }

21. @Concurrent
22. async function waitFor(conditionVariable: ArkTSUtils.locks.ConditionVariable) {
23. await conditionVariable.waitFor(3000);
24. console.info(`TaskPool Thread WaitFor: success`);
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State message: string | ResourceStr = $r('app.string.AsyncButton');

32. build() {
33. Row() {
34. Column() {
35. Button(this.message)
36. .fontSize(25)
37. .fontWeight(FontWeight.Bold)
38. .onClick(async () => {
39. // 创建conditionVariable对象。
40. const conditionVariable: ArkTSUtils.locks.ConditionVariable = new ArkTSUtils.locks.ConditionVariable();
41. // 将实例conditionVariable传递给wait线程。
42. await taskpool.execute(wait, conditionVariable);
43. // 将实例conditionVariable传递给notifyAll线程，唤醒wait线程，日志输出"TaskPool Thread Wait: success"。
44. await taskpool.execute(notifyAll, conditionVariable);
45. // 将实例conditionVariable传递给waitFor线程。
46. await taskpool.execute(waitFor, conditionVariable);
47. // 将实例conditionVariable传递给notifyOne线程，唤醒waitFor线程，日志输出"TaskPool Thread WaitFor: success"。
48. await taskpool.execute(notifyOne, conditionVariable);

50. // 创建有name的conditionVariable对象。
51. const conditionVariableRequest: ArkTSUtils.locks.ConditionVariable =
52. ArkTSUtils.locks.ConditionVariable.request('Request1');
53. // 将实例conditionVariableRequest传递给wait线程。
54. await taskpool.execute(wait, conditionVariableRequest);
55. // 将实例conditionVariableRequest传递给notifyAll线程，唤醒wait线程，日志输出"TaskPool Thread Wait: success"。
56. await taskpool.execute(notifyAll, conditionVariableRequest);
57. // 将实例conditionVariableRequest传递给waitFor线程。
58. await taskpool.execute(waitFor, conditionVariableRequest);
59. // 将实例conditionVariableRequest传递给notifyOne线程，唤醒waitFor线程，日志输出"TaskPool Thread WaitFor: success"。
60. await taskpool.execute(notifyOne, conditionVariableRequest);
61. })
62. }
63. .width('100%')
64. }
65. .height('100%')
66. }
67. }
```
