---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-thread-concurrency-overview
title: 多线程并发概述
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 多线程并发 > 多线程并发概述
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:29+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:381cca75faf03d09275e34cedfc23db6fd833c834cc78281b8bb8b76430ae50d
---

多线程并发是指在单个程序中同时运行多个线程，通过并行或交替执行任务来提升性能和资源利用率的编程模型。在ArkTS应用开发中，多线程并发适用于多种业务场景，常见的业务场景主要分为以下三类，更详细的使用请参考**应用多线程开发实践案例**。

* 业务逻辑包含大量计算或频繁的I/O读写等需要长时间执行的任务，例如图片和视频的编解码、文件的压缩与解压缩、数据库操作等场景。
* 业务逻辑包括监听和定期采集数据等需要长时间保持运行的任务，例如定期采集传感器数据的场景。
* 业务逻辑跟随主线程的生命周期，或与主线程绑定的任务，例如在游戏中的业务场景。

并发模型用于实现不同应用场景中的并发任务。常见的并发模型有基于内存共享的模型和基于消息通信的模型。

Actor并发模型是基于消息通信的典型并发模型。开发者无需处理锁带来的复杂问题，且具备高并发度，因此应用广泛。

当前ArkTS提供了TaskPool和Worker两种并发能力，两者均基于Actor并发模型实现。

Actor并发模型和内存共享并发模型的具体对比请见[多线程并发模型](multi-thread-concurrency-overview.md#多线程并发模型)。

## 多线程并发模型

内存共享并发模型指多线程同时执行任务，这些线程依赖同一内存资源并且都有权限访问，线程访问内存前需要抢占并锁定内存的使用权，没有抢占到内存的线程需要等待其他线程释放使用权再执行。

Actor并发模型每一个线程都是一个独立Actor，每个Actor有自己独立的内存，Actor之间通过消息传递机制触发对方Actor的行为，不同Actor之间不能直接访问对方的内存空间。

Actor并发模型与内存共享并发模型相比，不同线程间的内存是隔离的，因此不会发生线程竞争同一内存资源的情况。无需处理内存上锁问题，从而提高开发效率。

Actor并发模型中，不同Actor之间不共享内存，需通过消息传递机制传递任务和结果。

本文以经典的生产者消费者问题为例，分析这两种模型在解决问题时的差异。

### 内存共享模型

以下示例伪代码和示意图展示了如何使用内存共享模型解决生产者消费者问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/e_chsR96ScSBvlsQKHkXdA/zh-cn_image_0000002583477529.png?HW-CC-KV=V1&HW-CC-Date=20260427T233828Z&HW-CC-Expire=86400&HW-CC-Sign=D669B1EE69373F3B6E981122BC855677F5D38992D2996E5B15B9378170C99BC5)

为了避免不同生产者或消费者同时访问同一块共享内存容器时产生脏读、脏写现象，同一时间只能有一个生产者或消费者访问该容器。即不同生产者和消费者需争夺使用容器的锁。当一个角色获取锁后，其他角色需等待该角色释放锁，才能重新尝试获取锁以访问该容器。

```
1. // 此段示例为伪代码仅作为逻辑示意，便于开发者理解使用内存共享模型和Actor模型的区别
2. class Queue {
3. // ...
4. push(value: number) {
5. // ...
6. }

8. empty(): boolean {
9. // ...
10. return true;
11. }

13. pop(value: number): number {
14. // ...
15. return value;
16. }
17. // ...
18. }

20. class Mutex {
21. // ...
22. lock(): boolean {
23. // ...
24. return true;
25. }

27. unlock() {
28. // ...
29. }
30. // ...
31. }

33. class BufferQueue {
34. queue: Queue = new Queue();
35. mutex: Mutex = new Mutex();

37. add(value: number) {
38. // 尝试获取锁
39. if (this.mutex.lock()) {
40. this.queue.push(value);
41. this.mutex.unlock();
42. }
43. }

45. take(value: number): number {
46. let res: number = 0;
47. // 尝试获取锁
48. if (this.mutex.lock()) {
49. if (this.queue.empty()) {
50. this.mutex.unlock();
51. res = 1;
52. return res;
53. }
54. let num: number = this.queue.pop(value);
55. this.mutex.unlock();
56. res = num;
57. }
58. return res;
59. }
60. }

62. // 构造一段全局共享的内存
63. let g_bufferQueue = new BufferQueue();

65. class Producer {
66. constructor() {
67. }

69. run() {
70. let value = Math.random();
71. // 跨线程访问bufferQueue对象
72. g_bufferQueue.add(value);
73. }
74. }

76. class ConsumerTest {
77. constructor() {
78. }

80. run() {
81. // 跨线程访问bufferQueue对象
82. let num = 123;
83. let res = g_bufferQueue.take(num);
84. if (res != null) {
85. // 添加消费逻辑
86. }
87. }
88. }

90. function Main(): void {
91. let consumer: ConsumerTest = new ConsumerTest();
92. let producer: Producer = new Producer();
93. let threadNum: number = 10;
94. for (let i = 0; i < threadNum; i++) {
95. // 如下伪代码模拟启动多线程执行生产任务
96. // let thread = new Thread();
97. // thread.run(producer.run());
98. // consumer.run();
99. }
100. }
```

### Actor模型

以下示例简单展示了如何使用基于Actor模型的TaskPool并发能力来解决生产者消费者问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ByTYznSHTLaEtgmWP84Cyg/zh-cn_image_0000002552797880.png?HW-CC-KV=V1&HW-CC-Date=20260427T233828Z&HW-CC-Expire=86400&HW-CC-Sign=90B5020BDB18C95F2FB3DC31B424A460ACF8576A7596247FB8DD01FFF28BC371)

Actor模型中，不同角色之间并不共享内存，生产者线程和UI线程都有自己的虚拟机实例，两个虚拟机实例之间拥有独占的内存，相互隔离。生产者生产出结果后，通过序列化通信将结果发送给UI线程。UI线程消费结果后，再发送新的生产任务给生产者线程。

```
1. import { taskpool } from '@kit.ArkTS';
2. import { Main } from './Cale'

4. // 跨线程并发任务
5. @Concurrent
6. async function produce(): Promise<number> {
7. // 添加生产相关逻辑
8. console.info('producing...');
9. return Math.random();
10. }

12. class Consumer {
13. public consume(value: Object) {
14. // 添加消费相关逻辑
15. console.info('consuming value: ' + value);
16. }
17. }

19. @Entry
20. @Component
21. struct Index {
22. @State message: string = 'Hello World';

24. build() {
25. Row() {
26. Column() {
27. Text(this.message)
28. .fontSize(50)
29. .fontWeight(FontWeight.Bold)
30. Button() {
31. Text('Actor start')
32. }.onClick(() => {
33. let produceTask: taskpool.Task = new taskpool.Task(produce);
34. let consumer: Consumer = new Consumer();
35. for (let index: number = 0; index < 10; index++) {
36. // 执行生产异步并发任务
37. taskpool.execute(produceTask).then((res: Object) => {
38. consumer.consume(res);
39. }).catch((e: Error) => {
40. console.error(e.message);
41. })
42. }
43. this.message = 'success';
44. })
45. .id('button')
46. .width('20%')
47. .height('20%')

49. Button() {
50. Text('Actor start2')
51. }.onClick(async () => {
52. let dataArray: number[] = [];
53. let produceTask: taskpool.Task = new taskpool.Task(produce);
54. let consumer: Consumer = new Consumer();
55. for (let index: number = 0; index < 10; index++) {
56. // 执行生产异步并发任务
57. let result = await taskpool.execute(produceTask) as number;
58. dataArray.push(result);
59. }
60. for (let index: number = 0; index < dataArray.length; index++) {
61. consumer.consume(dataArray[index]);
62. }
63. this.message = 'success2';
64. })
65. .id('button2')
66. .width('20%')
67. .height('20%')

69. Button() {
70. Text('cale start')
71. }.onClick(async () => {
72. Main();
73. this.message = 'cale success';
74. })
75. .id('button3')
76. .width('20%')
77. .height('20%')
78. }
79. .width('100%')
80. }
81. .height('100%')
82. }
83. }
```

也可以等待生产者完成所有任务，通过序列化通信将结果发送给UI线程。UI线程接收后，由消费者统一消费结果。

```
1. import { taskpool } from '@kit.ArkTS';

3. // 跨线程并发任务
4. @Concurrent
5. async function produce(): Promise<number> {
6. // 添加生产相关逻辑
7. console.info('producing...');
8. return Math.random();
9. }

11. class Consumer {
12. public consume(value: number) {
13. // 添加消费相关逻辑
14. console.info('consuming value: ' + value);
15. }
16. }

18. @Entry
19. @Component
20. struct Index {
21. @State message: string = 'Hello World'

23. build() {
24. Row() {
25. Column() {
26. Text(this.message)
27. .fontSize(50)
28. .fontWeight(FontWeight.Bold)
29. Button() {
30. Text('start')
31. }.onClick(async () => {
32. let dataArray = new Array<number>();
33. let produceTask: taskpool.Task = new taskpool.Task(produce);
34. let consumer: Consumer = new Consumer();
35. for (let index: number = 0; index < 10; index++) {
36. // 执行生产异步并发任务
37. let result = await taskpool.execute(produceTask) as number;
38. dataArray.push(result);
39. }
40. for (let index: number = 0; index < dataArray.length; index++) {
41. consumer.consume(dataArray[index]);
42. }
43. })
44. .width('20%')
45. .height('20%')
46. }
47. .width('100%')
48. }
49. .height('100%')
50. }
51. }
```

## TaskPool和Worker

ArkTS提供了TaskPool和Worker两种并发能力供开发者选择，各自的运作机制和注意事项请见[TaskPool简介](taskpool-introduction.md)和[Worker简介](worker-introduction.md)，两者之间实现的特点和适用场景也存在差异，请见[TaskPool和Worker的对比](taskpool-vs-worker.md)。

## 并发注意事项

* 避免在并发线程中操作UI

  UI操作必须在主线程中执行。并发线程中操作UI可能导致界面异常或崩溃。
* 数据传递需支持序列化/反序列化

  并发任务间传递数据时，对象必须是可序列化的（如基本类型、普通对象等），不可传递函数、循环引用、特殊对象（如Promise、Error）等。已完成（fulfilled或rejected）状态的 Promise可以被传递，因为其结果是可序列化的。
* 合理控制并发粒度

  频繁创建和销毁并发任务（如Worker、Task）会带来额外性能开销，建议复用或使用任务池机制。
* 注意内存泄漏风险

  避免在并发任务中持有外部对象的强引用，防止内存泄漏。
* 并发任务应具备独立性

  并发任务应尽量不依赖外部状态，减少竞态条件（Race Condition）和同步开销。竞态条件是指多个线程或任务同时访问并修改共享数据，执行结果依赖于任务调度的顺序，可能导致数据不一致或不可预期的行为。
