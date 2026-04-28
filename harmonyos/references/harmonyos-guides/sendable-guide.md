---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide
title: Sendable使用场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > Sendable使用场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b1eb0a0e39671072d8e52dc5657e52c188ff5ea2af85d4556f4c2c15567c804
---

Sendable对象在不同并发实例间默认采用引用传递，这种方式比序列化更高效，且不会丢失类成员方法。因此，Sendable能够解决两个关键场景的问题：

* 跨并发实例传输大数据（例如达到100KB以上的数据）。
* 跨并发实例传递带方法的class实例对象。

## 跨并发实例传输大数据场景

由于跨并发实例序列化的开销随数据量线性增长，因此当传输数据量较大时（100KB的数据传输耗时约为1ms），跨并发实例的拷贝开销会影响应用性能。使用引用传递方式传输对象可提升性能。

**示例：**

```
1. // Index.ets
2. import { taskpool } from '@kit.ArkTS';
3. import { testTypeA, testTypeB, Test } from './sendable';
4. import { BusinessError, emitter } from '@kit.BasicServicesKit';

6. // 在并发函数中模拟数据处理
7. @Concurrent
8. async function taskFunc(obj: Test) {
9. console.info("test task res1 is: " + obj.data1.name + " res2 is: " + obj.data2.name);
10. }

12. async function test() {
13. // 使用taskpool传递数据
14. let a: testTypeA = new testTypeA("testTypeA");
15. let b: testTypeB = new testTypeB("testTypeB");
16. let obj: Test = new Test(a, b);
17. let task: taskpool.Task = new taskpool.Task(taskFunc, obj);
18. await taskpool.execute(task);
19. }

21. @Concurrent
22. function SensorListener() {
23. // 监听逻辑
24. // ...
25. }

27. @Entry
28. @Component
29. struct Index {
30. build() {
31. Column() {
32. Text("Listener task")
33. .id('HelloWorld')
34. .fontSize(50)
35. .fontWeight(FontWeight.Bold)
36. .onClick(() => {
37. let sensorTask = new taskpool.LongTask(SensorListener);
38. emitter.on({ eventId: 0 }, (data) => {
39. // Do something here
40. console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}}`);
41. });
42. taskpool.execute(sensorTask).then(() => {
43. console.info("Add listener of ACCELEROMETER success");
44. }).catch((e: BusinessError) => {
45. // Process error
46. })
47. })
48. Text("Data processing task")
49. .id('HelloWorld')
50. .fontSize(50)
51. .fontWeight(FontWeight.Bold)
52. .onClick(() => {
53. test();
54. })
55. }
56. .height('100%')
57. .width('100%')
58. }
59. }
```

```
1. // sendable.ets
2. // 将数据量较大的数据在Sendable class中组装
3. @Sendable
4. export class testTypeA {
5. name: string = "A";
6. constructor(name: string) {
7. this.name = name;
8. }
9. }

11. @Sendable
12. export class testTypeB {
13. name: string = "B";
14. constructor(name: string) {
15. this.name = name;
16. }
17. }

19. @Sendable
20. export class Test {
21. data1: testTypeA;
22. data2: testTypeB;
23. constructor(arg1: testTypeA, arg2: testTypeB) {
24. this.data1 = arg1;
25. this.data2 = arg2;
26. }
27. }
```

## 跨并发实例传递带方法的class实例对象

在序列化传输实例对象时，会丢失方法。因此，若需调用实例方法，应使用引用传递。处理数据时，若需解析数据，可使用[ASON工具](ason-parsing-generation.md)。

**示例：**

```
1. // Index.ets
2. import { taskpool, ArkTSUtils } from '@kit.ArkTS';
3. import { SendableTestClass, ISendable } from './sendable';

5. // 在并发函数中模拟数据处理
6. @Concurrent
7. async function taskFunc(sendableObj: SendableTestClass) {
8. console.info("SendableTestClass: name is: " + sendableObj.printName() + ", age is: " + sendableObj.printAge() + ", sex is: " + sendableObj.printSex());
9. sendableObj.setAge(28);
10. console.info("SendableTestClass: age is: " + sendableObj.printAge());

12. // 解析sendableObj.arr数据生成JSON字符串
13. let str = ArkTSUtils.ASON.stringify(sendableObj.arr);
14. console.info("SendableTestClass: str is: " + str);

16. // 解析该数据并生成ISendable数据
17. let jsonStr = '{"name": "Alexa", "age": 23, "sex": "female"}';
18. let obj = ArkTSUtils.ASON.parse(jsonStr) as ISendable;
19. console.info("SendableTestClass: type is: " + typeof obj);
20. console.info("SendableTestClass: name is: " + (obj as object)?.["name"]); // 输出: 'Alexa'
21. console.info("SendableTestClass: age is: " + (obj as object)?.["age"]); // 输出: 23
22. console.info("SendableTestClass: sex is: " + (obj as object)?.["sex"]); // 输出: 'female'
23. }
24. async function test() {
25. // 使用taskpool传递数据
26. let obj: SendableTestClass = new SendableTestClass();
27. let task: taskpool.Task = new taskpool.Task(taskFunc, obj);
28. await taskpool.execute(task);
29. }

31. @Entry
32. @Component
33. struct Index {
34. @State message: string = 'Hello World';

36. build() {
37. RelativeContainer() {
38. Text(this.message)
39. .id('HelloWorld')
40. .fontSize(50)
41. .fontWeight(FontWeight.Bold)
42. .alignRules({
43. center: { anchor: '__container__', align: VerticalAlign.Center },
44. middle: { anchor: '__container__', align: HorizontalAlign.Center }
45. })
46. .onClick(() => {
47. test();
48. })
49. }
50. .height('100%')
51. .width('100%')
52. }
53. }
```

```
1. // sendable.ets
2. // 定义模拟类SendableTestClass，模仿开发过程中需传递带方法的class
3. import { lang, collections } from '@kit.ArkTS'

5. export type ISendable = lang.ISendable;

7. @Sendable
8. export class SendableTestClass {
9. name: string = 'John';
10. age: number = 20;
11. sex: string = "man";
12. arr: collections.Array<number> = new collections.Array<number>(1, 2, 3);
13. constructor() {
14. }
15. setAge(age: number) : void {
16. this.age = age;
17. }

19. printName(): string {
20. return this.name;
21. }

23. printAge(): number {
24. return this.age;
25. }

27. printSex(): string {
28. return this.sex;
29. }
30. }
```
