---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-introduction
title: TaskPool简介
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 多线程并发 > TaskPool简介
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:662c76a68453587fc69a649f09b96a02ef5eb4b83c8e295de1848b00424a0555
---

TaskPool为应用程序提供多线程环境，降低资源消耗并提高系统性能。无需管理线程生命周期。具体接口信息及使用方法，请参见[TaskPool](../harmonyos-references/js-apis-taskpool.md)。

## TaskPool运作机制

TaskPool运作机制示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/hLHuxzL-SxSiA6A8CVOvgQ/zh-cn_image_0000002558604364.png?HW-CC-KV=V1&HW-CC-Date=20260429T052631Z&HW-CC-Expire=86400&HW-CC-Sign=9D1717231D6120BA455B4B9699FB9B7396E32306D0BD84C53180008A067FC570)

TaskPool支持在宿主线程提交任务到任务队列，系统选择合适的工作线程执行任务，并将结果返回给宿主线程。接口易用，支持任务执行、取消和指定优先级。通过系统统一线程管理，结合动态调度和负载均衡算法，可以节约系统资源。系统默认启动一个任务工作线程，任务多时会自动扩容。工作线程数量上限由设备的物理核数决定，内部管理具体数量，确保调度和执行效率最优。长时间无任务分发时会缩容，减少工作线程数量。具体扩缩容机制请参见[TaskPool扩缩容机制](taskpool-introduction.md#taskpool扩缩容机制)。

## TaskPool注意事项

* 实现任务的函数需要使用[@Concurrent装饰器](taskpool-introduction.md#concurrent装饰器)标注，且仅支持在.ets文件中使用。
* 从API version 11开始，跨并发实例传递带方法的实例对象时，该类必须使用装饰器[@Sendable装饰器](arkts-sendable.md#sendable装饰器)标注，且仅支持在.ets文件中使用。如果不考虑使用@Sendable装饰器标注，可以考虑worker方法，请参考[Worker同步调用宿主线程的接口](worker-invoke-mainthread-interface.md)。
* 任务函数（[LongTask](../harmonyos-references/js-apis-taskpool.md#longtask12)除外）在TaskPool工作线程中的执行时长不能超过3分钟。否则，若因任务逻辑导致阻塞，使任务无法完成，将导致该线程后续无法调度其他任务。当所有线程均被超时占用时，后续提交的任务将无法正常调度执行。需要注意的是，这里的3分钟限制仅统计TaskPool线程的​​同步执行时长​​，不包含异步操作（如Promise或async/await）的等待时长。例如，数据库的插入、删除、更新等操作，如果是异步操作，仅计入CPU实际处理时长（如SQL解析），网络传输或磁盘I/O等待时长不计入；如果是同步操作，整个操作时长（含I/O阻塞时间）均计入限制。开发者可通过[Task](../harmonyos-references/js-apis-taskpool.md#task)的属性ioDuration、cpuDuration获取执行当前任务的异步IO耗时和CPU耗时。
* 实现任务的函数入参需满足序列化支持的类型。详情请参见[线程间通信对象概述](serializable-overview.md)。目前不支持使用[@State装饰器](arkts-state.md)、[@Prop装饰器](arkts-prop.md)、[@Link装饰器](arkts-link.md)等装饰器修饰的复杂类型。
* ArrayBuffer参数在TaskPool中默认转移，需要设置转移列表的话可通过接口[setTransferList()](../harmonyos-references/js-apis-taskpool.md#settransferlist10)设置。如果需要多次调用使用ArrayBuffer作为参数的task，则需要通过接口[setCloneList()](../harmonyos-references/js-apis-taskpool.md#setclonelist11)把ArrayBuffer在线程中的传输行为改成拷贝传递，避免对原有对象产生影响。

除上述注意事项外，使用TaskPool时还需注意[并发注意事项](multi-thread-concurrency-overview.md#并发注意事项)。

```
1. import { taskpool } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Concurrent
5. function printArrayBuffer(buffer: ArrayBuffer) {
6. return buffer;
7. }

9. function testArrayBuffer() {
10. const buffer = new ArrayBuffer(1);
11. const group = new taskpool.TaskGroup();
12. const task = new taskpool.Task(printArrayBuffer, buffer);
13. group.addTask(task);
14. task.setCloneList([buffer]);
15. for (let i = 0; i < 5; i++) {
16. taskpool.execute(group).then(() => {
17. console.info('execute group success');
18. }).catch((e: BusinessError) => {
19. console.error(`execute group error: ${e.message}`);
20. })
21. }
22. }
```

* 由于不同线程中上下文对象不同，TaskPool工作线程只能使用线程安全的模块。例如，不能使用UI相关的非线程安全模块。TaskPool/Worker等工作线程不支持使用操作UI的模块、线程不安全的模块以及其他只支持在主线程中使用的模块。不支持UI模块是因为目前工作线程不支持操作UI，不支持线程不安全的模块是因为多线程使用该模块可能会导致多线程问题，只支持在主线程中使用的模块明确在文档中说明的有[ApplicationContext](../harmonyos-references/js-apis-inner-application-applicationcontext.md)等。线程安全的模块是指多线程同时使用该模块也不会引入多线程问题，如TaskPool/[Worker](worker-introduction.md)/[hilog](hilog.md)等。
* 序列化传输的数据量限制为16MB。
* [Priority](../harmonyos-references/js-apis-taskpool.md#priority)的IDLE优先级是用来标记需要在后台运行的耗时任务（例如数据同步、备份），它的优先级别是最低的。这种优先级的任务只在所有线程都空闲时触发执行，并且同一时间只会有一个IDLE优先级的任务执行。
* Promise不支持跨线程传递。TaskPool返回pending或rejected状态的Promise时会失败，返回fulfilled状态的Promise时TaskPool会解析返回的结果，如果结果可以跨线程传递，则返回成功。
* 不支持在TaskPool工作线程中使用[AppStorage](arkts-appstorage.md)。
* TaskPool支持在宿主线程封装任务并提交给任务队列，理论上支持的任务数量没有上限。然而，任务的执行效率受限于任务的优先级和系统资源。当工作线程达到最大数量时，任务的执行效率可能会下降。
* TaskPool不支持指定任务所运行的线程，任务会被分配到空闲的线程中执行。如果需要指定任务所运行的线程，建议使用[Worker](worker-introduction.md)。

## @Concurrent装饰器

使用[TaskPool](../harmonyos-references/js-apis-taskpool.md)时，执行的并发函数必须用该装饰器修饰，否则无法通过校验。

说明

从API version 9开始，支持使用@Concurrent装饰器声明并校验并发函数。

| @Concurrent并发装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 使用场景 | 仅支持在Stage模型的工程中使用。仅支持在.ets文件中使用。 |
| 装饰的函数类型 | 允许标注为async函数或普通函数。禁止标注为generator、箭头函数、类方法。不支持类成员函数或者匿名函数。 |
| 装饰的函数内的变量类型 | 允许使用局部变量、入参和通过import引入的变量，禁止使用闭包变量。 |
| 装饰的函数内的返回值类型 | 支持的类型请查[线程间通信对象概述](serializable-overview.md)。 |

由于@Concurrent标记的函数不能访问闭包，因此函数内部不能调用当前文件的其他函数，例如：

```
1. function bar() {
2. }

4. @Concurrent
5. function foo() {
6. bar(); // 违反闭包原则，报错
7. }
```

## 装饰器使用示例

### 并发函数一般使用

并发函数为一个计算两数之和的普通函数，taskpool执行该函数并返回结果。

示例：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function add(num1: number, num2: number): number {
5. return num1 + num2;
6. }

8. async function concurrentFunc(): Promise<void> {
9. try {
10. const task: taskpool.Task = new taskpool.Task(add, 1, 2);
11. console.info(`taskpool res is: ${await taskpool.execute(task)}`); // 输出结果：taskpool res is: 3
12. } catch (e) {
13. console.error(`taskpool execute error is: ${e}`);
14. }
15. }

17. @Entry
18. @Component
19. struct Index {
20. @State message: string = 'Hello World';

22. build() {
23. Row() {
24. Column() {
25. Text(this.message)
26. .fontSize(50)
27. .fontWeight(FontWeight.Bold)
28. .onClick(() => {
29. concurrentFunc();
30. this.message = 'success';
31. })
32. }
33. .width('100%')
34. }
35. .height('100%')
36. }
37. }
```

### 并发函数返回Promise

在并发函数中返回Promise时需特别注意。如示例所示，testPromise和testPromise1等函数需处理Promise并返回结果。

示例：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. function testPromise(args1: number, args2: number): Promise<number> {
5. return new Promise<number>((resolve, reject) => {
6. resolve(args1 + args2);
7. });
8. }

10. @Concurrent
11. async function testPromise1(args1: number, args2: number): Promise<number> {
12. return new Promise<number>((resolve, reject) => {
13. resolve(args1 + args2);
14. });
15. }

17. @Concurrent
18. async function testPromise2(args1: number, args2: number): Promise<number> {
19. return await new Promise<number>((resolve, reject) => {
20. resolve(args1 + args2);
21. });
22. }

24. @Concurrent
25. function testPromise3() {
26. return Promise.resolve(1);
27. }

29. @Concurrent
30. async function testPromise4(): Promise<number> {
31. return 1;
32. }

34. @Concurrent
35. async function testPromise5(): Promise<string> {
36. return await new Promise((resolve) => {
37. setTimeout(() => {
38. resolve('Promise setTimeout after resolve');
39. }, 1000)
40. });
41. }

43. async function testConcurrentFunc() {
44. const task1: taskpool.Task = new taskpool.Task(testPromise, 1, 2);
45. const task2: taskpool.Task = new taskpool.Task(testPromise1, 1, 2);
46. const task3: taskpool.Task = new taskpool.Task(testPromise2, 1, 2);
47. const task4: taskpool.Task = new taskpool.Task(testPromise3);
48. const task5: taskpool.Task = new taskpool.Task(testPromise4);
49. const task6: taskpool.Task = new taskpool.Task(testPromise5);

51. taskpool.execute(task1).then((d: object) => {
52. console.info(`task1 res is: ${d}`); // 输出结果：task1 res is: 3
53. }).catch((e: object) => {
54. console.error(`task1 catch e: ${e}`);
55. })
56. taskpool.execute(task2).then((d: object) => {
57. console.info(`task2 res is: ${d}`);
58. }).catch((e: object) => {
59. console.error(`task2 catch e: ${e}`); // 输出结果：task2 catch e: Error: Can't return Promise in pending state
60. })
61. taskpool.execute(task3).then((d: object) => {
62. console.info(`task3 res is: ${d}`); // 输出结果：task3 res is: 3
63. }).catch((e: object) => {
64. console.error(`task3 catch e: ${e}`);
65. })
66. taskpool.execute(task4).then((d: object) => {
67. console.info(`task4 res is: ${d}`); // 输出结果：task4 res is: 1
68. }).catch((e: object) => {
69. console.error(`task4 catch e: ${e}`);
70. })
71. taskpool.execute(task5).then((d: object) => {
72. console.info(`task5 res is: ${d}`); // 输出结果：task5 res is: 1
73. }).catch((e: object) => {
74. console.error(`task5 catch e: ${e}`);
75. })
76. taskpool.execute(task6).then((d: object) => {
77. console.info(`task6 res is: ${d}`); // 输出结果：task6 res is: Promise setTimeout after resolve
78. }).catch((e: object) => {
79. console.error(`task6 catch e: ${e}`);
80. })
81. }

83. @Entry
84. @Component
85. struct Index {
86. @State message: string = 'Hello World';

88. build() {
89. Row() {
90. Column() {
91. Button(this.message)
92. .fontSize(50)
93. .fontWeight(FontWeight.Bold)
94. .onClick(() => {
95. testConcurrentFunc();
96. this.message = 'success';
97. })
98. }
99. .width('100%')
100. }
101. .height('100%')
102. }
103. }
```

### 并发函数中使用自定义类或函数

在并发函数中使用自定义类或函数时，需将其定义在单独的文件中，否则可能被视为闭包。如下示例所示。

示例：

```
1. import { taskpool } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { testAdd, MyTestA, MyTestB } from './Test';

5. function add(arg: number) {
6. return ++arg;
7. }

9. class TestA {
10. constructor(name: string) {
11. this.name = name;
12. }
13. name: string = 'ClassA';
14. }

16. class TestB {
17. static nameStr: string = 'ClassB';
18. }

20. @Concurrent
21. function testFunc() {
22. // case1：在并发函数中直接调用同文件内定义的类或函数

24. // 直接调用同文件定义的函数add()，add飘红报错：
25. // Only imported variables and local variables can be used in @Concurrent decorated functions. <ArkTSCheck>
26. // add(1);
27. // 直接使用同文件定义的TestA构造，TestA飘红报错：
28. // Only imported variables and local variables can be used in @Concurrent decorated functions. <ArkTSCheck>
29. // let a = new TestA('aaa');
30. // 直接访问同文件定义的TestB的成员nameStr，TestB飘红报错：
31. // Only imported variables and local variables can be used in @Concurrent decorated functions. <ArkTSCheck>
32. // console.info(`TestB name is: ${TestB.nameStr}`);

34. // case2：在并发函数中调用定义在Test.ets文件并导入当前文件的类或函数

36. // 输出结果：res1 is: 2
37. console.info(`res1 is: ${testAdd(1)}`);
38. const tmpStr = new MyTestA('TEST A');
39. // 输出结果：res2 is: TEST A
40. console.info(`res2 is: ${tmpStr.name}`);
41. // 输出结果：res3 is: MyTestB
42. console.info(`res3 is: ${MyTestB.nameStr}`);
43. }

46. @Entry
47. @Component
48. struct Index {
49. @State message: string = 'Hello World';

51. build() {
52. RelativeContainer() {
53. Text(this.message)
54. .id('HelloWorld')
55. .fontSize(50)
56. .fontWeight(FontWeight.Bold)
57. .alignRules({
58. center: { anchor: '__container__', align: VerticalAlign.Center },
59. middle: { anchor: '__container__', align: HorizontalAlign.Center }
60. })
61. .onClick(() => {
62. const task = new taskpool.Task(testFunc);
63. taskpool.execute(task).then(() => {
64. console.info('taskpool: execute task success!');
65. }).catch((e:BusinessError) => {
66. console.error(`taskpool: execute: Code: ${e.code}, message: ${e.message}`);
67. })
68. this.message = 'success';
69. })
70. }
71. .height('100%')
72. .width('100%')
73. }
74. }
```

```
1. export function testAdd(arg: number) {
2. return ++arg;
3. }

5. @Sendable
6. export class MyTestA {
7. constructor(name: string) {
8. this.name = name;
9. }
10. name: string = 'MyTestA';
11. }

13. export class MyTestB {
14. static nameStr:string = 'MyTestB';
15. }
```

### 并发异步函数中使用Promise

在并发异步函数中使用Promise时，建议搭配await使用，这样TaskPool可以捕获Promise中的异常。推荐使用示例如下。

示例：

```
1. import { taskpool } from '@kit.ArkTS';

3. @Concurrent
4. async function testPromiseError() {
5. await new Promise<number>((resolve, reject) => {
6. resolve(1);
7. }).then(()=>{
8. throw new Error('testPromise Error');
9. })
10. }

12. @Concurrent
13. async function testPromiseError1() {
14. await new Promise<string>((resolve, reject) => {
15. reject('testPromiseError1 Error msg');
16. })
17. }

19. @Concurrent
20. function testPromiseError2() {
21. return new Promise<string>((resolve, reject) => {
22. reject('testPromiseError2 Error msg');
23. })
24. }

26. async function testConcurrentFunc() {
27. const task1: taskpool.Task = new taskpool.Task(testPromiseError);
28. const task2: taskpool.Task = new taskpool.Task(testPromiseError1);
29. const task3: taskpool.Task = new taskpool.Task(testPromiseError2);

31. taskpool.execute(task1).then((d: object) => {
32. console.info(`task1 res is: ${d}`);
33. }).catch((e: object) => {
34. console.error(`task1 catch e: ${e}`); // task1 catch e: Error: testPromise Error
35. })
36. taskpool.execute(task2).then((d: object) => {
37. console.info(`task2 res is: ${d}`);
38. }).catch((e: object) => {
39. console.error(`task2 catch e: ${e}`); // task2 catch e: testPromiseError1 Error msg
40. })
41. taskpool.execute(task3).then((d: object) => {
42. console.info(`task3 res is: ${d}`);
43. }).catch((e: object) => {
44. console.error(`task3 catch e: ${e}`); // task3 catch e: testPromiseError2 Error msg
45. })
46. }

48. @Entry
49. @Component
50. struct Index {
51. @State message: string = 'Hello World';

53. build() {
54. Row() {
55. Column() {
56. Button(this.message)
57. .fontSize(50)
58. .fontWeight(FontWeight.Bold)
59. .onClick(() => {
60. testConcurrentFunc();
61. // ...
62. })
63. }
64. .width('100%')
65. }
66. .height('100%')
67. }
68. }
```

## TaskPool扩缩容机制

### 扩容机制

一般情况下，向任务队列提交任务时会触发扩容检测。扩容检测首先判断当前空闲工作线程数是否大于任务数。如果大于，说明线程池中有空闲工作线程，无需扩容。否则，通过负载计算确定所需工作线程数并创建。

### 缩容机制

扩容后，TaskPool创建多个工作线程，但当任务数减少后，这些线程就会处于空闲状态，造成资源浪费，因此，TaskPool提供了缩容机制。TaskPool使用定时器，每30秒检测一次当前负载，并尝试释放空闲的工作线程。释放的线程需满足以下条件：

* 该线程空闲时长达到30s。
* 该线程上未执行长时任务（[LongTask](../harmonyos-references/js-apis-taskpool.md#longtask12)）。
* 该线程上没有业务申请且未释放的句柄，例如[Timer(定时器)](../harmonyos-references/js-apis-timer.md)。
* 该线程处于非调试调优阶段。
* 该线程中不存在已创建未销毁的子Worker。
