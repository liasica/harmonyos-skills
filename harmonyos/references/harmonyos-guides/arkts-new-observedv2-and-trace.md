---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-observedv2-and-trace
title: @ObservedV2装饰器和@Trace装饰器：类属性变化观测
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理数据对象的状态 > @ObservedV2装饰器和@Trace装饰器：类属性变化观测
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6d59372786984872e54f9792b54dd588082390ab348d1e03d923e9e5f9b7667c
---

为了增强状态管理框架对类对象中属性的观测能力，开发者可以使用@ObservedV2装饰器和@Trace装饰器装饰类以及类中的属性。

@ObservedV2和@Trace提供了对嵌套类对象属性变化直接观测的能力，是状态管理V2中相对核心的能力之一。在阅读本文档前，建议提前阅读：[状态管理概述](arkts-state-management-overview.md)来了解状态管理V2整体的能力架构。

说明

@ObservedV2与@Trace装饰器从API version 12开始支持。

从API version 12开始，@ObservedV2与@Trace装饰器支持在ArkTS卡片中使用。

从API version 12开始，@ObservedV2与@Trace装饰器支持在元服务中使用。

## 概述

@ObservedV2装饰器与@Trace装饰器用于装饰类以及类中的属性，使得被装饰的类和属性具有深度观测的能力：

* @ObservedV2装饰器与@Trace装饰器需要配合使用，单独使用@ObservedV2装饰器或@Trace装饰器没有任何作用。
* 被@Trace装饰器装饰的属性property变化时，仅会通知property关联的组件进行刷新。
* 在嵌套类中，嵌套类中的属性property被@Trace装饰且嵌套类被@ObservedV2装饰时，才具有触发UI刷新的能力。
* 在继承类中，父类或子类中的属性property被@Trace装饰且该property所在类被@ObservedV2装饰时，才具有触发UI刷新的能力。
* 未被@Trace装饰的属性用在UI中无法感知到变化，也无法触发UI刷新。
* 使用@ObservedV2与@Trace装饰器的类，需通过new操作符实例化后，才具备被观测变化的能力。

## 状态管理V1版本对嵌套类对象属性变化直接观测的局限性

现有状态管理V1版本无法实现对嵌套类对象属性变化的直接观测。

```
1. @Observed
2. class Father {
3. public son: Son;

5. constructor(name: string, age: number) {
6. this.son = new Son(name, age);
7. }
8. }

10. @Observed
11. class Son {
12. public name: string;
13. public age: number;

15. constructor(name: string, age: number) {
16. this.name = name;
17. this.age = age;
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State father: Father = new Father('John', 8);

26. build() {
27. Row() {
28. Column() {
29. Text(`name: ${this.father.son.name} age: ${this.father.son.age}`)
30. .fontSize(50)
31. .fontWeight(FontWeight.Bold)
32. .onClick(() => {
33. this.father.son.age++;
34. })
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

[Limitations.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/overview/Limitations.ets#L15-L57)

在上述代码中，点击Text组件增加age的值时，不会触发UI刷新。原因在于现有的状态管理框架无法观测到嵌套类中属性age的值变化。V1版本的解决方案是使用[@ObjectLink装饰器](arkts-observed-and-objectlink.md)与自定义组件来实现观测。

```
1. @Observed
2. class Father {
3. public son: Son;

5. constructor(name: string, age: number) {
6. this.son = new Son(name, age);
7. }
8. }

10. @Observed
11. class Son {
12. public name: string;
13. public age: number;

15. constructor(name: string, age: number) {
16. this.name = name;
17. this.age = age;
18. }
19. }

21. @Component
22. struct Child {
23. @ObjectLink son: Son;

25. build() {
26. Row() {
27. Column() {
28. Text(`name: ${this.son.name} age: ${this.son.age}`)
29. .fontSize(50)
30. .fontWeight(FontWeight.Bold)
31. .onClick(() => {
32. this.son.age++;
33. })
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }

41. @Entry
42. @Component
43. struct Index {
44. @State father: Father = new Father('John', 8);

46. build() {
47. Column() {
48. Child({ son: this.father.son })
49. }
50. }
51. }
```

[RealizeObservation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/overview/RealizeObservation.ets#L15-L68)

通过这种方式虽然能够实现对嵌套类中属性变化的观测，但是当嵌套层级较深时，代码将会变得十分复杂，易用性差。因此推出类装饰器@ObservedV2与成员变量装饰器@Trace，增强对嵌套类中属性变化的观测能力。

## 装饰器说明

| @ObservedV2类装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 类装饰器 | 装饰class。需要放在class的定义前，使用new创建类对象。 |

| @Trace成员变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 可装饰的变量 | class中成员属性。属性的类型可以为number、string、boolean、class、[Array](arkts-new-observedv2-and-trace.md#trace装饰基础类型的数组)、[Date](arkts-new-observedv2-and-trace.md#trace装饰date类型)、[Map](arkts-new-observedv2-and-trace.md#trace装饰map类型)、[Set](arkts-new-observedv2-and-trace.md#trace装饰set类型)等类型。@Trace不支持观察Function类型的数据，修改@Trace装饰的Function类型的数据，UI不会刷新。 |

## 观察变化

使用@ObservedV2装饰的类中被@Trace装饰的属性具有被观测变化的能力，当该属性值变化时，会触发该属性绑定的UI组件刷新。

* 在嵌套类中使用@Trace装饰的属性具有被观测变化的能力。

```
1. @ObservedV2
2. class Son {
3. @Trace public age: number = 100;
4. }

6. class Father {
7. public son: Son = new Son();
8. }

10. @Entry
11. @ComponentV2
12. struct Index {
13. father: Father = new Father();

15. build() {
16. Column() {
17. // 当点击改变age时，Text组件会刷新
18. Text(`${this.father.son.age}`)
19. .onClick(() => {
20. this.father.son.age++;
21. })
22. }
23. }
24. }
```

[ObserveChanges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/overview/ObserveChanges.ets#L15-L41)

* 在继承类中使用@Trace装饰的属性具有被观测变化的能力。

```
1. @ObservedV2
2. class Father {
3. @Trace public name: string = 'Tom';
4. }

6. class Son extends Father {
7. }

9. @Entry
10. @ComponentV2
11. struct Index {
12. son: Son = new Son();

14. build() {
15. Column() {
16. // 当点击改变name时，Text组件会刷新
17. Text(`${this.son.name}`)
18. .onClick(() => {
19. this.son.name = 'Jack';
20. })
21. }
22. }
23. }
```

[InheritedChanges.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/overview/InheritedChanges.ets#L15-L40)

* 类中使用@Trace装饰的静态属性具有被观测变化的能力。

```
1. @ObservedV2
2. class Manager {
3. @Trace public static count: number = 1;
4. }

6. @Entry
7. @ComponentV2
8. struct Index {
9. build() {
10. Column() {
11. // 当点击改变count时，Text组件会刷新
12. Text(`${Manager.count}`)
13. .onClick(() => {
14. Manager.count++;
15. })
16. }
17. }
18. }
```

[StaticAttribute.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/overview/StaticAttribute.ets#L15-L35)

* @Trace装饰内置类型时，可以观测各自API导致的变化：

  | 类型 | 可观测变化的API |
  | --- | --- |
  | Array | push、pop、shift、unshift、splice、copyWithin、fill、reverse、sort |
  | Date | setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds |
  | Map | set, clear, delete |
  | Set | add, clear, delete |

## 使用限制

@ObservedV2与@Trace装饰器存在以下使用限制：

* 非@Trace装饰的成员属性用在UI上无法触发UI刷新。

```
1. @ObservedV2
2. class Person {
3. public id: number = 0;
4. @Trace public age: number = 8;
5. }

7. @Entry
8. @ComponentV2
9. struct Index {
10. person: Person = new Person();

12. build() {
13. Column() {
14. // age被@Trace装饰，用在UI中可以触发UI刷新
15. Text(`${this.person.age}`)
16. .onClick(() => {
17. this.person.age++; // 点击会触发UI刷新
18. })
19. // id未被@Trace装饰，用在UI中不会触发UI刷新
20. Text(`${this.person.id}`) // 当id变化时不会刷新
21. .onClick(() => {
22. this.person.id++; // 点击不会触发UI刷新
23. })
24. }
25. }
26. }
```

[UiRefreshCannotTriggered.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagerestrictions/UiRefreshCannotTriggered.ets#L15-L43)

* @ObservedV2仅能装饰class，无法装饰自定义组件。

```
1. @ObservedV2 // 错误用法，编译时报错
2. struct Index {
3. build() {
4. }
5. }
```

* @Trace不能用在没有被@ObservedV2装饰的class上。

```
1. class User {
2. id: number = 0;
3. @Trace name: string = 'Tom'; // 错误用法，编译时报错
4. }
```

* @Trace是class中属性的装饰器，不能用在struct中。

```
1. @ComponentV2
2. struct Comp {
3. @Trace message: string = 'Hello World'; // 错误用法，编译时报错

5. build() {
6. }
7. }
```

* @ObservedV2、@Trace不能与[@Observed](arkts-observed-and-objectlink.md)、[@Track](arkts-track.md)混合使用。

```
1. @Observed
2. class User {
3. @Trace name: string = 'Tom'; // 错误用法，编译时报错
4. }

6. @ObservedV2
7. class Person {
8. @Track name: string = 'Jack'; // 错误用法，编译时报错
9. }
```

* 使用@ObservedV2与@Trace装饰的类不能和[@State](arkts-state.md)等V1的装饰器混合使用，编译时报错。

```
1. // 以@State装饰器为例
2. @ObservedV2
3. class Job {
4. @Trace public jobName: string = 'Teacher';
5. }

7. @ObservedV2
8. class Info {
9. @Trace public name: string = 'Tom';
10. @Trace public age: number = 25;
11. public job: Job = new Job();
12. }

14. @Entry
15. @ComponentV2
16. struct Index {
17. // @State info: Info = new Info(); 无法混用，编译时报错
18. @Local info: Info = new Info();

20. build() {
21. Column() {
22. Text(`name: ${this.info.name}`)
23. Text(`age: ${this.info.age}`)
24. Text(`jobName: ${this.info.job.jobName}`)
25. Button('change age')
26. .onClick(() => {
27. this.info.age++;
28. })
29. Button('Change job')
30. .onClick(() => {
31. this.info.job.jobName = 'Doctor';
32. })
33. }
34. }
35. }
```

[UseMixture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagerestrictions/UseMixture.ets#L15-L52)

* 继承自@ObservedV2的类无法和@State等V1的装饰器混用，运行时报错。

```
1. // 以@State装饰器为例
2. @ObservedV2
3. class Job {
4. @Trace public jobName: string = 'Teacher';
5. }

7. @ObservedV2
8. class Info {
9. @Trace public name: string = 'Tom';
10. @Trace public age: number = 25;
11. public job: Job = new Job();
12. }

14. class Message extends Info {
15. constructor() {
16. super();
17. }
18. }

20. @Entry
21. @Component
22. struct Index {
23. // @State message: Message = new Message();  无法混用，运行时报错
24. message: Message = new Message();

26. build() {
27. Column() {
28. Text(`name: ${this.message.name}`)
29. Text(`age: ${this.message.age}`)
30. Text(`jobName: ${this.message.job.jobName}`)
31. Button('change age')
32. .onClick(() => {
33. this.message.age++;
34. })
35. Button('Change job')
36. .onClick(() => {
37. this.message.job.jobName = 'Doctor';
38. })
39. }
40. }
41. }
```

[InheritanceMixture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagerestrictions/InheritanceMixture.ets#L15-L58)

* 使用@ObservedV2与@Trace装饰器的类，需通过new操作符实例化后，才具备被观测变化的能力。
* @ObservedV2的类实例无法直接使用JSON.parse反序列化获得（直接使用JSON.parse反序列化获得的对象无法观察属性变化），可搭配三方库[class-transformer](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/class-transformer)实现反序列化后可观察，示例请参考[@ObservedV2装饰对象的序列化与反序列化](arkts-new-observedv2-and-trace.md#observedv2装饰对象的序列化与反序列化)。

## 使用场景

### 嵌套类场景

在下面的嵌套类场景中，Pencil类是Son类中最里层的类，Pencil类被@ObservedV2装饰且属性length被@Trace装饰，此时length的变化能够被观测到。

@Trace装饰器与现有状态管理框架的[@Track](arkts-track.md)与[@State](arkts-state.md)装饰器的能力不同，@Track使class具有属性级更新的能力，但并不具备深度观测的能力；而@State只能观测到对象本身以及第一层的变化，对于多层嵌套场景只能通过封装自定义组件，搭配[@Observed](arkts-observed-and-objectlink.md)和[@ObjectLink](arkts-observed-and-objectlink.md)来实现观测。

* 点击Button('change length')，length是被@Trace装饰的属性，它的变化可以触发关联的UI组件，即UINode (1)的刷新，并输出"id: 1 renderTimes: x"的日志，其中x根据点击次数依次增长。
* 自定义组件Page中的son是常规变量，因此点击Button('assign Son')并不会观测到变化。
* 当点击Button('assign Son')后，再点击Button('change length')并不会引起UI刷新。因为此时son的地址改变，其关联的UI组件并没有关联到最新的son。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'ArktsObservedV2AndTrace';

6. @ObservedV2
7. class Pencil {
8. @Trace public length: number = 21; // 当length变化时，会刷新关联的组件
9. }

11. class Bag {
12. public width: number = 50;
13. public height: number = 60;
14. public pencil: Pencil = new Pencil();
15. }

17. class Son {
18. public age: number = 5;
19. public school: string = 'some';
20. public bag: Bag = new Bag();
21. }

23. @Entry
24. @ComponentV2
25. struct Page {
26. son: Son = new Son();
27. renderTimes: number = 0;

29. isRender(id: number): number {
30. hilog.info(DOMAIN, TAG, `id: ${id} renderTimes: ${this.renderTimes}`);
31. this.renderTimes++;
32. return 40;
33. }

35. build() {
36. Column() {
37. Text('pencil length' + this.son.bag.pencil.length)
38. .fontSize(this.isRender(1)) // UINode (1)
39. Button('change length')
40. .onClick(() => {
41. // 点击更改length值，UINode（1）会刷新
42. this.son.bag.pencil.length += 100;
43. })
44. Button('assign Son')
45. .onClick(() => {
46. // 由于变量son非状态变量，因此无法刷新UINode（1）
47. this.son = new Son();
48. })
49. }
50. }
51. }
```

[NestedClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/NestedClass.ets#L15-L68)

### 继承类场景

@Trace支持在类的继承场景中使用，无论是在基类还是继承类中，只有被@Trace装饰的属性才具有被观测变化的能力。

以下例子中，声明class GrandFather、Father、Uncle、Son、Cousin，继承关系如下图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/GNTL-254SsGt7ZajP5Xk0w/zh-cn_image_0000002583437663.png?HW-CC-KV=V1&HW-CC-Date=20260427T233907Z&HW-CC-Expire=86400&HW-CC-Sign=FD067A4BE8FF84BA4DE60CCED5A1C1790A452D94B354B8FF47146E28512AA910)

创建类Son和类Cousin的实例，点击Button('change Son age')和Button('change Cousin age')可以触发UI的刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'ArktsObservedV2AndTrace';

6. @ObservedV2
7. class GrandFather {
8. @Trace public age: number = 0;

10. constructor(age: number) {
11. this.age = age;
12. }
13. }

15. class Father extends GrandFather {
16. constructor(father: number) {
17. super(father);
18. }
19. }

21. class Uncle extends GrandFather {
22. constructor(uncle: number) {
23. super(uncle);
24. }
25. }

27. class Son extends Father {
28. constructor(son: number) {
29. super(son);
30. }
31. }

33. class Cousin extends Uncle {
34. constructor(cousin: number) {
35. super(cousin);
36. }
37. }

39. @Entry
40. @ComponentV2
41. struct Index {
42. son: Son = new Son(0);
43. cousin: Cousin = new Cousin(0);
44. renderTimes: number = 0;

46. isRender(id: number): number {
47. hilog.info(DOMAIN, TAG, `id: ${id} renderTimes: ${this.renderTimes}`);
48. this.renderTimes++;
49. return 40;
50. }

52. build() {
53. Row() {
54. Column() {
55. Text(`Son ${this.son.age}`)
56. .fontSize(this.isRender(1))
57. .fontWeight(FontWeight.Bold)
58. Text(`Cousin ${this.cousin.age}`)
59. .fontSize(this.isRender(2))
60. .fontWeight(FontWeight.Bold)
61. Button('change Son age')
62. .onClick(() => {
63. this.son.age++;
64. })
65. Button('change Cousin age')
66. .onClick(() => {
67. this.cousin.age++;
68. })
69. }
70. .width('100%')
71. }
72. .height('100%')
73. }
74. }
```

[InheritanceClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/InheritanceClass.ets#L15-L91)

### @Trace装饰基础类型的数组

@Trace装饰数组时，使用支持的API能够观测到变化。支持的API见[观察变化](arkts-new-observedv2-and-trace.md#观察变化)。

在下面的示例中@ObservedV2装饰的Arr类中的属性numberArr是@Trace装饰的数组，当使用数组API操作numberArr时，可以观测到对应的变化。注意使用数组长度进行判断以防越界访问。

```
1. let nextId: number = 0;

3. @ObservedV2
4. class Arr {
5. public id: number = 0;
6. @Trace public numberArr: number[] = [];

8. constructor() {
9. this.id = nextId++;
10. this.numberArr = [0, 1, 2];
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct Index {
17. arr: Arr = new Arr();

19. build() {
20. Column() {
21. Text(`length: ${this.arr.numberArr.length}`)
22. .fontSize(40)
23. Divider()
24. if (this.arr.numberArr.length >= 3) {
25. Text(`${this.arr.numberArr[0]}`)
26. .fontSize(40)
27. .onClick(() => {
28. this.arr.numberArr[0]++;
29. })
30. Text(`${this.arr.numberArr[1]}`)
31. .fontSize(40)
32. .onClick(() => {
33. this.arr.numberArr[1]++;
34. })
35. Text(`${this.arr.numberArr[2]}`)
36. .fontSize(40)
37. .onClick(() => {
38. this.arr.numberArr[2]++;
39. })
40. }

42. Divider()

44. ForEach(this.arr.numberArr, (item: number, index: number) => {
45. Text(`${index} ${item}`)
46. .fontSize(40)
47. })

49. Button('push')
50. .onClick(() => {
51. this.arr.numberArr.push(50);
52. })

54. Button('pop')
55. .onClick(() => {
56. this.arr.numberArr.pop();
57. })

59. Button('shift')
60. .onClick(() => {
61. this.arr.numberArr.shift();
62. })

64. Button('splice')
65. .onClick(() => {
66. this.arr.numberArr.splice(1, 0, 60);
67. })

70. Button('unshift')
71. .onClick(() => {
72. this.arr.numberArr.unshift(100);
73. })

75. Button('copywithin')
76. .onClick(() => {
77. this.arr.numberArr.copyWithin(0, 1, 2);
78. })

80. Button('fill')
81. .onClick(() => {
82. this.arr.numberArr.fill(0, 2, 4);
83. })

85. Button('reverse')
86. .onClick(() => {
87. this.arr.numberArr.reverse();
88. })

90. Button('sort')
91. .onClick(() => {
92. this.arr.numberArr.sort();
93. })
94. }
95. }
96. }
```

[DecorationFoundation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/DecorationFoundation.ets#L15-L113)

### @Trace装饰对象数组

* @Trace装饰对象数组personList以及Person类中的age属性，因此当personList、age改变时均可以观测到变化。
* 点击Text组件更改age时，Text组件会刷新。

```
1. let nextId: number = 0;

3. @ObservedV2
4. class Person {
5. @Trace public age: number = 0;

7. constructor(age: number) {
8. this.age = age;
9. }
10. }

12. @ObservedV2
13. class Info {
14. public id: number = 0;
15. @Trace public personList: Person[] = [];

17. constructor() {
18. this.id = nextId++;
19. this.personList = [new Person(0), new Person(1), new Person(2)];
20. }
21. }

23. @Entry
24. @ComponentV2
25. struct Index {
26. info: Info = new Info();

28. build() {
29. Column() {
30. Text(`length: ${this.info.personList.length}`)
31. .fontSize(40)
32. Divider()
33. if (this.info.personList.length >= 3) {
34. Text(`${this.info.personList[0].age}`)
35. .fontSize(40)
36. .onClick(() => {
37. this.info.personList[0].age++;
38. })

40. Text(`${this.info.personList[1].age}`)
41. .fontSize(40)
42. .onClick(() => {
43. this.info.personList[1].age++;
44. })

46. Text(`${this.info.personList[2].age}`)
47. .fontSize(40)
48. .onClick(() => {
49. this.info.personList[2].age++;
50. })
51. }

53. Divider()

55. ForEach(this.info.personList, (item: Person, index: number) => {
56. Text(`${index} ${item.age}`)
57. .fontSize(40)
58. })
59. }
60. }
61. }
```

[DecorativeObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/DecorativeObject.ets#L15-L78)

### @Trace装饰Map类型

* 被@Trace装饰的Map类型属性可以观测到调用API带来的变化，包括 set、clear、delete。
* 因为Info类被@ObservedV2装饰且属性memberMap被@Trace装饰，点击Button('init map')对memberMap赋值也可以观测到变化。

```
1. @ObservedV2
2. class Info {
3. @Trace public memberMap: Map<number, string> = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
4. }

6. @Entry
7. @ComponentV2
8. struct MapSample {
9. info: Info = new Info();

11. build() {
12. Row() {
13. Column() {
14. ForEach(Array.from(this.info.memberMap.entries()), (item: [number, string]) => {
15. Text(`${item[0]}`)
16. .fontSize(30)
17. Text(`${item[1]}`)
18. .fontSize(30)
19. Divider()
20. })
21. Button('init map')
22. .onClick(() => {
23. this.info.memberMap = new Map([[0, 'a'], [1, 'b'], [3, 'c']]);
24. })
25. Button('set new one')
26. .onClick(() => {
27. this.info.memberMap.set(4, 'd');
28. })
29. Button('clear')
30. .onClick(() => {
31. this.info.memberMap.clear();
32. })
33. Button('set the key: 0')
34. .onClick(() => {
35. this.info.memberMap.set(0, 'aa');
36. })
37. Button('delete the first one')
38. .onClick(() => {
39. this.info.memberMap.delete(0);
40. })
41. }
42. .width('100%')
43. }
44. .height('100%')
45. }
46. }
```

[DecorationMap.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/DecorationMap.ets#L15-L63)

### @Trace装饰Set类型

* 被@Trace装饰的Set类型属性可以观测到调用API带来的变化，包括 add、clear和delete。
* 因为Info类被@ObservedV2装饰且属性memberSet被@Trace装饰，点击Button('init set')对memberSet赋值也可以观测到变化。

```
1. @ObservedV2
2. class Info {
3. @Trace public memberSet: Set<number> = new Set([0, 1, 2, 3, 4]);
4. }

6. @Entry
7. @ComponentV2
8. struct SetSample {
9. info: Info = new Info();

11. build() {
12. Row() {
13. Column() {
14. ForEach(Array.from(this.info.memberSet.entries()), (item: [number, number]) => {
15. Text(`${item[0]}`)
16. .fontSize(30)
17. Divider()
18. })
19. Button('init set')
20. .onClick(() => {
21. this.info.memberSet = new Set([0, 1, 2, 3, 4]);
22. })
23. Button('set new one')
24. .onClick(() => {
25. this.info.memberSet.add(5);
26. })
27. Button('clear')
28. .onClick(() => {
29. this.info.memberSet.clear();
30. })
31. Button('delete the first one')
32. .onClick(() => {
33. this.info.memberSet.delete(0);
34. })
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

[DecorationSet.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/DecorationSet.ets#L15-L57)

### @Trace装饰Date类型

* @Trace装饰的Date类型属性可以观测调用API带来的变化，包括 setFullYear、setMonth、setDate、setHours、setMinutes、setSeconds、setMilliseconds、setTime、setUTCFullYear、setUTCMonth、setUTCDate、setUTCHours、setUTCMinutes、setUTCSeconds、setUTCMilliseconds。
* 因为Info类被@ObservedV2装饰且属性selectedDate被@Trace装饰，点击Button('set selectedDate to 2023-07-08')对selectedDate赋值也可以观测到变化。

```
1. @ObservedV2
2. class Info {
3. @Trace public selectedDate: Date = new Date('2021-08-08');
4. }

6. @Entry
7. @ComponentV2
8. struct DateSample {
9. info: Info = new Info();

11. build() {
12. Column() {
13. Button('set selectedDate to 2023-07-08')
14. .margin(10)
15. .onClick(() => {
16. this.info.selectedDate = new Date('2023-07-08');
17. })
18. Button('increase the year by 1')
19. .margin(10)
20. .onClick(() => {
21. this.info.selectedDate.setFullYear(this.info.selectedDate.getFullYear() + 1);
22. })
23. Button('increase the month by 1')
24. .margin(10)
25. .onClick(() => {
26. this.info.selectedDate.setMonth(this.info.selectedDate.getMonth() + 1);
27. })
28. Button('increase the day by 1')
29. .margin(10)
30. .onClick(() => {
31. this.info.selectedDate.setDate(this.info.selectedDate.getDate() + 1);
32. })
33. DatePicker({
34. start: new Date('1970-1-1'),
35. end: new Date('2100-1-1'),
36. selected: this.info.selectedDate
37. })
38. }.width('100%')
39. }
40. }
```

[DecorateDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/usagescenarios/DecorateDate.ets#L15-L57)

## 常见问题

### @ObservedV2装饰对象的序列化与反序列化

@ObservedV2装饰的对象序列化后会为@Trace装饰的属性添加\_\_ob\_前缀。

```
1. @ObservedV2
2. class Info {
3. @Trace name: string = 'Tom';
4. @Trace age: number = 24;
5. }

7. let realInfo: Info = new Info();
8. let jsonResult: string = JSON.stringify(realInfo); // '{"__ob_name":"Tom","__ob_age":24}'
```

将@ObservedV2装饰的对象通过JSON.stringify序列化后，再通过JSON.parse反序列化，将失去观察能力。

```
1. @ObservedV2
2. class Info {
3. @Trace name: string = 'Tom';
4. @Trace age: number = 24;
5. }

7. let realInfo: Info = new Info();
8. let jsonResult: string = JSON.stringify(realInfo); // '{"__ob_name":"Tom","__ob_age":24}'
9. let parseInfo: Info = JSON.parse(jsonResult);

11. // 与直接通过new操作符创建的对象不同，JSON.parse获得的对象实际并不是Info的实例，所以无属性观察能力
12. let isInfoByNew: boolean = realInfo instanceof Info; // true
13. let isInfoByParse: boolean = parseInfo instanceof Info; // false
```

可以配合三方库[class-transformer](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/class-transformer)实现反序列化后可观察。

class-transformer可以通过如下命令安装。

```
1. ohpm install class-transformer
```

```
1. import { plainToInstance } from 'class-transformer'; // 导入三方库
2. @ObservedV2
3. class Info {
4. @Trace name: string = 'Tom';
5. @Trace age: number = 24;
6. }
7. let realInfo: Info = new Info();
8. let jsonResult: string = JSON.stringify(realInfo); // '{"__ob_name":"Tom","__ob_age":24}'
9. let parseInfo: Info = JSON.parse(jsonResult);

11. let transformedInfo: Info = plainToInstance(Info, parseInfo);
12. let isInfoByTransformed: boolean = transformedInfo instanceof Info; // true
```

若为多层对象嵌套场景，需要进行额外处理，包括：

* 去除序列化结果中的\_\_ob\_前缀，否则内层对象无法被正确转换。
* 使用class-transformer库中提供的@Type装饰器（为与状态管理V2的[@Type装饰器](arkts-new-type.md)区分，示例中重命名为TypeFromLibrary）标记里层对象的类型。

使用三方库的@Type装饰器需要安装[reflect-metadata](https://gitcode.com/openharmony-tpc/openharmony_tpc_samples/tree/master/reflect-metadata)。

reflect-metadata可以通过如下命令安装。

```
1. ohpm install reflect-metadata@0.2.1
```

```
1. import { plainToInstance, Type as TypeFromLibrary} from 'class-transformer'; // 导入三方库
2. import 'reflect-metadata'; // 三方库的@Type装饰器需要使用
3. @ObservedV2
4. class Info {
5. @Trace name: string = 'Tom';
6. @Trace age: number = 24;
7. }
8. @ObservedV2
9. class InfoWrapper {
10. // 使用三方库的@Type装饰器（重命名为TypeFromLibrary）标记内层属性的类型
11. @TypeFromLibrary(() => Info)
12. @Trace info: Info = new Info();
13. }
14. let realWrapper: InfoWrapper = new InfoWrapper();
15. let infoWrapperJson: string = JSON.stringify(realWrapper); // '{"__ob_info":{"__ob_name":"Tom","__ob_age":24}}'
16. // 去除属性key的'__ob_'前缀，此处仅做演示，开发者需根据实际类型定义情况完成去除key中的'__ob_'前缀
17. let jsonHandled = infoWrapperJson.replaceAll('__ob_', ''); // '{"info":{"name":"Tom","age":24}}'
18. let wrapperHandled = plainToInstance(InfoWrapper, JSON.parse(jsonHandled));

20. let isWrapper: boolean = wrapperHandled instanceof InfoWrapper; // true
21. let isInfo: boolean = (wrapperHandled.info) instanceof Info; // true
```

在UI中使用的完整示例如下。

```
1. import { plainToInstance, Type as TypeFromLibrary } from 'class-transformer'; // 导入三方库
2. import 'reflect-metadata'; // 三方库的@Type装饰器需要使用

4. // 模拟json键值对对象
5. let testJSON: Record<string, ESObject> = {
6. 'id': 1,
7. 'info': {
8. 'name': 'Tom',
9. 'age': 24
10. },
11. 'friends': [
12. {
13. 'name': 'John',
14. 'age': 23
15. },
16. {
17. 'name': 'Mary',
18. 'age': 24
19. }
20. ]
21. }

23. @ObservedV2
24. class Info {
25. @Trace public name?: string;
26. @Trace public age?: number;
27. }

29. @ObservedV2
30. class Person {
31. public id?: number;
32. // 使用三方库的@Type装饰器（重命名为TypeFromLibrary）标记内层属性的类型
33. @TypeFromLibrary(() => Info)
34. @Trace public info?: Info;
35. // 使用三方库的@Type装饰器（重命名为TypeFromLibrary）标记内层属性的类型
36. @TypeFromLibrary(() => Info)
37. @Trace public friends?: Info[];
38. }

40. @Entry
41. @ComponentV2
42. struct SerializationAndDeserialization {
43. @Local person: Person | undefined = undefined;
44. aboutToAppear(): void {
45. this.person = plainToInstance(Person, testJSON); // 直接将对象通过plainToInstance转为Person实例
46. }

48. build() {
49. Column() {
50. Text(`name: ${this.person?.info?.name}, age: ${this.person?.info?.age}`)
51. .onClick(() => {
52. if (this.person?.info?.age) {
53. this.person!.info!.age++; // 修改可观察
54. }
55. })
56. ForEach(this.person?.friends, (item: Info) => {
57. Text(`friend name: ${item.name}, age: ${item.age}`)
58. .onClick(() => {
59. if (item.age) {
60. item.age++; // 修改可观察
61. }
62. })
63. })

65. Button('Refresh Info')
66. .onClick(() => {
67. let json: string =
68. `{
69. "id":12,
70. "__ob_info":
71. {
72. "__ob_name":"Jimmy",
73. "__ob_age":35
74. },
75. "__ob_friends":[
76. {
77. "__ob_name":"Bob",
78. "__ob_age":30
79. },
80. {
81. "__ob_name":"Kevin",
82. "__ob_age":33
83. }
84. ]
85. }`;
86. // 去除'__ob_'前缀后通过JSON.parse与plainToInstance将json字符串转化成Person对象
87. this.person = plainToInstance(Person, JSON.parse(json.replaceAll('__ob_', '')));
88. })
89. }
90. }
91. }
```

[SerializationAndDeserialization.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/faqs/SerializationAndDeserialization.ets#L15-L107)

### router传递的@ObservedV2类型显示异常

用router传递的@ObservedV2类，由于经过序列化生成的属性名称与类中的原始属性名称不一致，不能直接通过as类型转换成@ObservedV2的实例，需要反序列化重新生成@ObservedV2实例。反序列化相关内容请参考[@ObservedV2装饰对象的序列化与反序列化](arkts-new-observedv2-and-trace.md#observedv2装饰对象的序列化与反序列化)。

【反例】

```
1. // 文件pages/faqs/RouterIndex.ets内容

3. @ObservedV2
4. export class RouterModel {
5. @Trace id: number = -1;
6. @Trace info: string = 'default';
7. }

9. @Entry
10. @ComponentV2
11. struct RouterIndex {
12. @Local paramsInfo: RouterModel = new RouterModel();
13. onJumpClick(): void {
14. this.paramsInfo.id = 0;
15. this.paramsInfo.info = 'RouterModel';
16. this.getUIContext().getRouter().pushUrl({
17. url: 'pages/faqs/ChildPage',
18. params: this.paramsInfo // 传递@ObservedV2实例到子页面
19. }, (err) => {
20. if (err) {
21. console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
22. return;
23. }
24. console.info('Invoke pushUrl succeeded.');
25. })
26. }

28. build() {
29. Column() {
30. Text('Parent page')
31. Button('Jump')
32. .onClick(() => {
33. this.onJumpClick();
34. })
35. }
36. }
37. }
```

```
1. // 文件pages/faqs/ChildPage.ets内容

3. import { RouterModel } from './RouterIndex';

5. @Entry
6. @ComponentV2
7. struct Detail {
8. @Local params?: RouterModel
9. aboutToAppear(): void {
10. // 错误使用方式！@ObservedV2类型通过router传递无法直接类型转换
11. this.params = this.getUIContext().getRouter().getParams() as RouterModel;
12. }
13. build() {
14. Column() {
15. Text(`Detail Page: ${this.params?.id} ${this.params?.info}`) // 由于传递数据失败，这里会显示undefined
16. }
17. }
18. }
```

【正例】

```
1. @ObservedV2
2. export class RouterModel {
3. @Trace public id: number = -1;
4. @Trace public info: string = 'default';
5. }

7. @Entry
8. @ComponentV2
9. struct RouterIndex {
10. @Local paramsInfo: RouterModel = new RouterModel();
11. onJumpClick(): void {
12. this.paramsInfo.id = 0;
13. this.paramsInfo.info = 'RouterModel';
14. this.getUIContext().getRouter().pushUrl({
15. url: 'pages/faqs/ChildPage',
16. params: this.paramsInfo // 传递@ObservedV2实例到子页面
17. }, (err) => {
18. if (err) {
19. console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
20. return;
21. }
22. console.info('Invoke pushUrl succeeded.');
23. })
24. }

26. build() {
27. Column() {
28. Text('Parent page')
29. Button('Jump')
30. .onClick(() => {
31. this.onJumpClick();
32. })
33. }
34. }
35. }
```

[RouterIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/faqs/RouterIndex.ets#L15-L51)

```
1. import { RouterModel } from './RouterIndex';
2. import { plainToInstance } from 'class-transformer'; // 导入三方库

4. @Entry
5. @ComponentV2
6. struct Detail {
7. @Local params?: RouterModel
8. aboutToAppear(): void {
9. this.params =
10. plainToInstance(RouterModel, JSON.parse(JSON.stringify(this.getUIContext().getRouter().getParams())));
11. }
12. build() {
13. Column() {
14. Text(`Detail Page: ${this.params?.id} ${this.params?.info}`)
15. }
16. }
17. }
```

[ChildPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedv2andtrace/entry/src/main/ets/pages/faqs/ChildPage.ets#L15-L33)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/MoQqnb7tTQeJj0JOuyCxeA/zh-cn_image_0000002552957618.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233907Z&HW-CC-Expire=86400&HW-CC-Sign=47EF7F11CDD66F3F7B0E8254229D46E442C7071E294F69AD706DCA9A8B5A88E2)
