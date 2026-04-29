---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-observed-and-objectlink
title: @Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V1） > 管理组件拥有的状态 > @Observed装饰器和@ObjectLink装饰器：嵌套类对象属性变化
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:14+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:da3e4a33e6dc0218e4523d863f6f4a7b902e8745966b04ccb2b1aadf3a025285
---

上文所述的装饰器（包括[@State](arkts-state.md)、[@Prop](arkts-prop.md)、[@Link](arkts-link.md)、[@Provide和@Consume](arkts-provide-and-consume.md)装饰器）仅能观察到第一层的变化，但是在实际应用开发中，应用会根据开发需要，封装自己的数据模型。对于多层嵌套的情况，比如二维数组、对象数组、嵌套类场景，无法观察到第二层的属性变化。因此，为了实现对嵌套数据结构中深层属性变化的观察，引入了@Observed和@ObjectLink装饰器。

@Observed/@ObjectLink适用于观察嵌套对象（对象的属性是对象）属性的变化，需要开发者对装饰器的基本观察能力有一定的了解，再来对比阅读该文档。建议提前阅读：[@State](arkts-state.md)的基本用法。最佳实践请参考[状态管理最佳实践](../best-practices/bpta-status-management.md)。常见问题请参考[状态管理常见问题](arkts-state-management-faq.md)。

说明

从API version 9开始，这两个装饰器支持在ArkTS卡片中使用。

从API version 11开始，这两个装饰器支持在元服务中使用。

## 概述

@ObjectLink和@Observed类装饰器配合使用，可实现嵌套对象或数组的双向数据同步，使用方式如下：

* 将数组项或类属性声明为@Observed装饰的类型，示例请参考[嵌套对象](arkts-observed-and-objectlink.md#嵌套对象)。
* 在子组件中使用@ObjectLink装饰的状态变量，用于接收父组件@Observed装饰的类实例，从而建立双向数据绑定。
* API version 19之前，@ObjectLink只能接收@Observed装饰的类实例；API version 19及以后，@ObjectLink也可以接收复杂类型，无@Observed装饰的限制。但需注意，如需观察嵌套类型场景，需要其接收@Observed装饰的类实例或[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)的返回值。示例请参考[二维数组](arkts-observed-and-objectlink.md#二维数组)。

开发者如需实现单向数据同步，需要搭配@Prop使用，示例请参考[@Prop与@ObjectLink的差异](arkts-observed-and-objectlink.md#prop与objectlink的差异)。

## 装饰器说明

| @Observed类装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 类装饰器 | 装饰class。需要放在class的定义前，使用new创建类对象。 |

| @ObjectLink变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 允许装饰的变量类型 | 支持继承Date、[Array](arkts-observed-and-objectlink.md#二维数组)的class实例。  API version 11及以后支持继承[Map](arkts-observed-and-objectlink.md#继承map类)、[Set](arkts-observed-and-objectlink.md#继承set类)的class实例以及@Observed装饰类和undefined或null组成的联合类型，比如ClassA | ClassB、 ClassA | undefined 或者 ClassA | null, 示例请参考[@ObjectLink支持联合类型](arkts-observed-and-objectlink.md#objectlink支持联合类型)。  API version 19之前，必须为被@Observed装饰的class实例。  API version 19及以后，@ObjectLink可以被复杂类型初始化，即class、object或built-in类型。但当观察嵌套类型时，仍需其接收@Observed装饰的类实例或makeV1Observed的返回值。  **说明：**  @ObjectLink不支持简单类型，如果开发者需要使用简单类型，可以使用[@Prop](arkts-prop.md)。 |
| 被装饰变量的初始值 | 禁止本地初始化。 |

@ObjectLink的属性可以被改变，但不允许整体赋值，即@ObjectLink装饰的变量是只读的。

```
1. // 允许@ObjectLink装饰的数据属性赋值
2. this.objLink.a= ...
3. // 不允许@ObjectLink装饰的数据自身赋值
4. this.objLink= ...
```

说明

@ObjectLink装饰的变量不能被赋值，如果要使用赋值操作，请使用[@Prop](arkts-prop.md)。

* @Prop装饰的变量和数据源的关系是单向同步，@Prop装饰的变量在本地拷贝了数据源，所以它允许本地更改，如果父组件中的数据源有更新，@Prop装饰的变量在本地的修改将被覆盖。
* @ObjectLink装饰的变量和数据源的关系是双向同步，@ObjectLink装饰的变量相当于指向数据源的指针。禁止对@ObjectLink装饰的变量赋值，如果发生@ObjectLink装饰的变量的赋值，则同步链将被打断。

## 变量的传递/访问规则说明

| @ObjectLink传递/访问 | 说明 |
| --- | --- |
| 从父组件初始化 | 必须指定。  必须使用复杂类型初始化@ObjectLink装饰的变量，如果需要观察变化需要满足以下场景：  - API version 19之前，类型必须为被@Observed装饰的class实例。  - API version 19及以后，@ObjectLink可以被复杂类型初始化，即class、object或built-in类型。但当观察嵌套类型时，仍需其接收@Observed装饰的类实例或makeV1Observed的返回值。  - 同步源的class或者数组必须是[@State](arkts-state.md)，[@Link](arkts-link.md)，[@Provide](arkts-provide-and-consume.md)，[@Consume](arkts-provide-and-consume.md)或者@ObjectLink装饰的数据。  同步源是数组项的示例请参考[对象数组](arkts-observed-and-objectlink.md#对象数组)。初始化的class的示例请参考[嵌套对象](arkts-observed-and-objectlink.md#嵌套对象)。 |
| 与源对象同步 | 双向。 |
| 可以初始化子组件 | 允许，可用于初始化常规变量、@State、@Link、@Prop、@Provide |

**图1** 初始化规则图示

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/jb_mThRvQpqS9K8F_hvgtw/zh-cn_image_0000002589323963.png?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=DD421B9A3CD2E0402BE6DF6494E0BA5E4713E460DC6A03EC7FC48E5241381B55)

## 观察变化和行为表现

### 观察变化

API version 19之前，如果需要观察嵌套场景的变化，如嵌套类，二维数组，对象数组等，那么内层的数据类型也需要被@Observed装饰。API version 19及以后，也可以通过使用[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)来使内层数据可观察。内层数据需要传递给@ObjectLink，使其在UI上可观察。示例请参考[嵌套对象](arkts-observed-and-objectlink.md#嵌套对象)。

@ObjectLink接收对象时，如果对象被@State或其他状态变量装饰器装饰，则可以观察第一层变化。示例请参考[对象类型](arkts-observed-and-objectlink.md#对象类型)。

@ObjectLink接收嵌套对象时，内层对象需要为被@Observed装饰的class类型。从API version 19开始，内层对象也支持被[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)处理的返回值。示例请参考[嵌套对象](arkts-observed-and-objectlink.md#嵌套对象)。

@ObjectLink推荐设计单独的自定义组件来渲染每一个数组或对象。此时，对象数组或嵌套对象需要两个自定义组件，一个自定义组件呈现外部数组/对象，另一个自定义组件呈现嵌套在数组/对象内的类对象。可以观察到：

* 其属性的数值的变化，其中属性是指Object.keys(observedObject)返回的所有属性，示例请参考[嵌套对象](arkts-observed-and-objectlink.md#嵌套对象)。
* 如果数据源是数组，则可以观察到数组项的替换，如果数据源是class，可观察到class的属性的变化，示例请参考[对象数组](arkts-observed-and-objectlink.md#对象数组)。

@ObjectLink装饰继承于Date的class时，可以观察到Date整体的赋值，同时可通过调用Date的接口setFullYear, setMonth, setDate, setHours, setMinutes, setSeconds, setMilliseconds, setTime, setUTCFullYear, setUTCMonth, setUTCDate, setUTCHours, setUTCMinutes, setUTCSeconds, setUTCMilliseconds 更新Date的属性。

```
1. @Observed
2. class DateClass extends Date {
3. constructor(args: number | string) {
4. super(args);
5. }
6. }

8. @Observed
9. class NewDate {
10. public data: DateClass;

12. constructor(data: DateClass) {
13. this.data = data;
14. }
15. }

17. @Component
18. struct Child {
19. label: string = 'date';
20. @ObjectLink data: DateClass;

22. build() {
23. Column() {
24. // data被@Observed和@ObjectLink装饰，可以被观察到Date整体的赋值以及调用Date接口带来的变化
25. Button('child increase the day by 1')
26. .onClick(() => {
27. this.data.setDate(this.data.getDate() + 1);
28. })
29. DatePicker({
30. start: new Date('1970-1-1'),
31. end: new Date('2100-1-1'),
32. selected: this.data
33. })
34. }
35. }
36. }

38. @Entry
39. @Component
40. struct Parent {
41. @State newData: NewDate = new NewDate(new DateClass('2023-1-1'));

43. build() {
44. Column() {
45. Child({ label: 'date', data: this.newData.data })

47. Button('parent update the new date')
48. .onClick(() => {
49. this.newData.data = new DateClass('2023-07-07');
50. })
51. Button(`ViewB: this.newData = new NewDate(new DateClass('2023-08-20'))`)
52. .onClick(() => {
53. this.newData = new NewDate(new DateClass('2023-08-20'));
54. })
55. }
56. }
57. }
```

[ObservationChangeInheritance.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/overview/ObservationChangeInheritance.ets#L15-L72)

@ObjectLink装饰继承于Map的class时，可以观察到Map整体的赋值，同时可通过调用Map的接口set, clear, delete 更新Map的值。示例请参考[继承Map类](arkts-observed-and-objectlink.md#继承map类)。

@ObjectLink装饰继承于Set的class时，可以观察到Set整体的赋值，同时可通过调用Set的接口add, clear, delete 更新Set的值。示例请参考[继承Set类](arkts-observed-and-objectlink.md#继承set类)。

### 框架行为

1. 初始渲染：

   a. @Observed装饰的class的实例会被代理对象包装，代理了class上的属性的setter和getter方法。

   b. 子组件中@ObjectLink装饰的变量从父组件初始化，接收被@Observed装饰的class的实例，@ObjectLink的包装类会将自己注册给@Observed class。这里的注册行为指的是，@ObjectLink包装类会向@Observed实例提供自身的引用，让@Observed实例将其添加到依赖列表中，以便属性变化时能通知到它。
2. 属性更新：当@Observed装饰的class属性改变时，会执行代理的setter和getter，然后遍历依赖它的@ObjectLink包装类，通知数据更新。

## 限制条件

1. 使用@Observed装饰class会改变class原始的原型链，@Observed和其他类装饰器装饰同一个class可能会带来问题。
2. @ObjectLink装饰器不建议在[@Entry](arkts-create-custom-components.md#entry)装饰的自定义组件中使用，编译时会产生告警。
3. @ObjectLink装饰的类型必须是复杂类型，否则会有编译时报错。
4. API version 19前，@ObjectLink装饰的变量类型必须是显式地由@Observed装饰的类。如果未指定类型，或不是@Observed装饰的class，编译时报错。

   API version 19及以后，@ObjectLink也可以被[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)的返回值初始化，若@ObjectLink接收未使用@Observed装饰的class或makeV1Observed返回值进行初始化，则会有运行时告警日志。

   ```
   1. class Test {
   2. msg: number;

   4. constructor(msg: number) {
   5. this.msg = msg;
   6. }
   7. }
   8. // 错误写法，count未指定类型，编译报错
   9. @ObjectLink count;
   10. // 错误写法，Test未被@Observed装饰，编译报错
   11. @ObjectLink test: Test;
   ```

   ```
   1. @Observed
   2. class Info {
   3. public count: number;

   5. constructor(count: number) {
   6. this.count = count;
   7. }
   8. }
   9. // ...
   10. // 正确写法
   11. @ObjectLink count: Info;
   ```
5. @ObjectLink装饰的变量不能本地初始化，仅能通过构造参数从父组件传入初始值，否则编译时会报错。

   ```
   1. // 错误写法，编译报错
   2. @ObjectLink count: CountInfo = new CountInfo(10);
   ```

   ```
   1. @Observed
   2. class CountInfo {
   3. public count: number;

   5. constructor(count: number) {
   6. this.count = count;
   7. }
   8. }
   9. // ...
   10. // 正确写法
   11. @ObjectLink count: CountInfo;
   ```
6. @ObjectLink装饰的变量是只读的，不能被赋值，否则会有运行时报错提示Cannot set property when setter is undefined。如果需要对@ObjectLink装饰的变量进行整体替换，可以在父组件对其进行整体替换。

   【反例】

   ```
   1. @Observed
   2. class Info {
   3. count: number;

   5. constructor(count: number) {
   6. this.count = count;
   7. }
   8. }

   10. @Component
   11. struct Child {
   12. @ObjectLink num: Info;

   14. build() {
   15. Column() {
   16. Text(`num的值: ${this.num.count}`)
   17. .onClick(() => {
   18. // 错误写法，@ObjectLink装饰的变量不能被赋值，运行时报错
   19. this.num = new Info(10);
   20. })
   21. }
   22. }
   23. }

   25. @Entry
   26. @Component
   27. struct Parent {
   28. @State num: Info = new Info(10);

   30. build() {
   31. Column() {
   32. Text(`count的值: ${this.num.count}`)
   33. Child({num: this.num})
   34. }
   35. }
   36. }
   ```

   【正例】

   ```
   1. @Observed
   2. class Info {
   3. public count: number;

   5. constructor(count: number) {
   6. this.count = count;
   7. }
   8. }

   10. @Component
   11. struct Child {
   12. @ObjectLink num: Info;

   14. build() {
   15. Column() {
   16. Text(`num value: ${this.num.count}`)
   17. .onClick(() => {
   18. // 正确写法，可以更改@ObjectLink装饰变量的成员属性
   19. this.num.count = 20;
   20. })
   21. }
   22. }
   23. }

   25. @Entry
   26. @Component
   27. struct Parent {
   28. @State num: Info = new Info(10);

   30. build() {
   31. Column() {
   32. Text(`count value: ${this.num.count}`)
   33. Button('click')
   34. .onClick(() => {
   35. // 可以在父组件做整体替换
   36. this.num = new Info(30);
   37. })
   38. Child({ num: this.num })
   39. }
   40. }
   41. }
   ```

   [ReadOnlyVariable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/restrictiveconditions/ReadOnlyVariable.ets#L15-L58)

## 使用场景

### 对象类型

该场景包含built-in类型（Array、Map、Set和Date）和普通class。从API version 19开始，@ObjectLink接收@State传递built-in类型和普通class对象，可以观察其API调用和第一层变化，无需额外添加@Observed装饰。因为@State等状态变量装饰器，会给对象（外层对象）添加一层“代理”包装，其功能等同于添加@Observed装饰。

```
1. class Book {
2. public name: string;

4. constructor(name: string) {
5. this.name = name;
6. }
7. }

9. @Component
10. struct BookCard {
11. @ObjectLink book: Book;

13. build() {
14. Column() {
15. Text(`BookCard: ${this.book.name}`) // 可以观察到name的变化
16. .width(320)
17. .margin(10)
18. .textAlign(TextAlign.Center)

20. Button('change book.name')
21. .width(320)
22. .margin(10)
23. .onClick(() => {
24. this.book.name = 'C++';
25. })
26. }
27. }
28. }

30. @Entry
31. @Component
32. struct Index {
33. @State book: Book = new Book('JS');

35. build() {
36. Column() {
37. BookCard({ book: this.book })
38. }
39. }
40. }
```

### 嵌套对象

```
1. @Observed
2. class Book {
3. public name: string;

5. constructor(name: string) {
6. this.name = name;
7. }
8. }

10. @Observed
11. class Bag {
12. public book: Book;

14. constructor(book: Book) {
15. this.book = book;
16. }
17. }

19. @Component
20. struct BookCard {
21. @ObjectLink book: Book;

23. build() {
24. Column() {
25. Text(`BookCard: ${this.book.name}`) // 可以观察到name的变化
26. .width(320)
27. .margin(10)
28. .textAlign(TextAlign.Center)

30. Button('change book.name')
31. .width(320)
32. .margin(10)
33. .onClick(() => {
34. this.book.name = 'C++';
35. })
36. }
37. }
38. }

40. @Entry
41. @Component
42. struct Index {
43. @State bag: Bag = new Bag(new Book('JS'));

45. build() {
46. Column() {
47. Text(`Index: ${this.bag.book.name}`) // 无法观察到name的变化
48. .width(320)
49. .margin(10)
50. .textAlign(TextAlign.Center)

52. Button('change bag.book.name')
53. .width(320)
54. .margin(10)
55. .onClick(() => {
56. this.bag.book.name = 'TS';
57. })

59. BookCard({ book: this.bag.book })
60. }
61. }
62. }
```

[NestedObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/NestedObject.ets#L15-L79)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/5-vIhCk8T5CQW7kwzvJRLA/zh-cn_image_0000002589243903.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=91DDDDBEC5E50C6EE5365C6CA44E49F3E3289CE28E2630F862EEE8BB0D2F6216)

上述示例中：

* 对于Index组件内状态变量@State bag: Bag，bag.book是第一层，bag.book.name是第二层。因此，当点击change bag.book.name直接修改this.bag.book.name时，Index中的Text('Index: ${this.bag.book.name}')不会刷新，因为@State只能观察到第一层属性变化，不能直接观察嵌套对象内部属性name的变化。
* 对于BookCard组件内状态变量@ObjectLink book: Book，Book被@Observed装饰，且book被@ObjectLink接收。book.name变化可以被@ObjectLink观察，因此无论是在父组件Index中点击change bag.book.name，还是在子组件BookCard中点击change book.name，BookCard中的Text('BookCard: ${this.book.name}')都会刷新。
* @State负责感知外层对象Bag的第一层变化，@Observed + @ObjectLink负责感知内层对象Book的属性变化。

### 对象数组

对象数组是一种常用的数据结构。以下示例展示了对象数组的用法。

说明

NextID是用来在[ForEach循环渲染](arkts-rendering-control-foreach.md)过程中，为每个数组元素生成一个唯一且持久的键值，标识对应的组件。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'ArkTSObservedAndObjectlink';
5. let nextID: number = 1;

7. @Observed
8. class Info {
9. public id: number;
10. public info: number;

12. constructor(info: number) {
13. this.id = nextID++;
14. this.info = info;
15. }
16. }

18. @Component
19. struct Child {
20. // 子组件Child的@ObjectLink的类型是Info
21. @ObjectLink info: Info;
22. label: string = 'ViewChild';

24. build() {
25. Row() {
26. Button(`ViewChild [${this.label}] this.info.info = ${this.info ? this.info.info : 'undefined'}`)
27. .width(320)
28. .margin(10)
29. .onClick(() => {
30. this.info.info += 1;
31. })
32. }
33. }
34. }

36. @Entry
37. @Component
38. struct Parent {
39. // Parent中有@State装饰的Info[]
40. @State arrA: Info[] = [new Info(0), new Info(0)];

42. build() {
43. Column() {
44. ForEach(this.arrA,
45. (item: Info) => {
46. Child({ label: `#${item.id}`, info: item })
47. },
48. (item: Info): string => item.id.toString()
49. )
50. // 使用@State装饰的数组的数组项初始化@ObjectLink，其中数组项是被@Observed装饰的Info的实例
51. Child({ label: 'ViewChild this.arrA[first]', info: this.arrA[0] })
52. Child({ label: 'ViewChild this.arrA[last]', info: this.arrA[this.arrA.length-1] })

54. Button('ViewParent: reset array')
55. .width(320)
56. .margin(10)
57. .onClick(() => {
58. this.arrA = [new Info(0), new Info(0)];
59. })
60. Button('ViewParent: push')
61. .width(320)
62. .margin(10)
63. .onClick(() => {
64. this.arrA.push(new Info(0));
65. })
66. Button('ViewParent: shift')
67. .width(320)
68. .margin(10)
69. .onClick(() => {
70. if (this.arrA.length > 0) {
71. this.arrA.shift();
72. } else {
73. hilog.info(DOMAIN, TAG, 'length <= 0');
74. }
75. })
76. Button('ViewParent: item property in middle')
77. .width(320)
78. .margin(10)
79. .onClick(() => {
80. this.arrA[Math.floor(this.arrA.length / 2)].info = 10;
81. })
82. Button('ViewParent: item property in middle')
83. .width(320)
84. .margin(10)
85. .onClick(() => {
86. this.arrA[Math.floor(this.arrA.length / 2)] = new Info(11);
87. })
88. }
89. }
90. }
```

[ObjectArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/ObjectArray.ets#L15-L107)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/TA8aTVCxSUejNzMUPwTi0Q/zh-cn_image_0000002558764096.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=9BBCC1E972329FE082D48A117C8444DEC2364D050B0A725D9229793A9ED15A1B)

* this.arrA[Math.floor(this.arrA.length/2)] = new Info(..) ：该状态变量的改变触发2次更新：

  1. ForEach：数组项的赋值导致ForEach的[itemGenerator](../harmonyos-references/ts-rendering-control-foreach.md)被修改，因此数组项被识别为有更改，ForEach的item builder将执行，创建新的Child组件实例。
  2. Child({ label: 'ViewChild this.arrA[last]', info: this.arrA[this.arrA.length-1] })：上述更改改变了数组中第二个元素，所以绑定this.arrA[1]的Child将被更新。
* this.arrA.push(new Info(0)) ： 将触发2次不同效果的更新：

  1. ForEach：新添加的Info对象对于ForEach是未知的[itemGenerator](../harmonyos-references/ts-rendering-control-foreach.md)，ForEach的item builder将执行，创建新的Child组件实例。
  2. Child({ label: 'ViewChild this.arrA[last]', info: this.arrA[this.arrA.length-1] })：数组的最后一项有更改，因此引起第二个Child的实例的更改。对于Child({ label: 'ViewChild this.arrA[first]', info: this.arrA[0] })，数组的更改并没有触发一个数组项更改的改变，所以第一个Child不会刷新。
* this.arrA[Math.floor(this.arrA.length/2)].info：@State无法观察到第二层的变化，但是Info被@Observed装饰，Info的属性的变化将被@ObjectLink观察到。

### 二维数组

使用@Observed观察二维数组的变化。可以声明一个被@Observed装饰的继承Array的子类。

```
1. @Observed
2. class ObservedArray<T> extends Array<T> {
3. }
```

声明一个继承自Array的类ObservedArray<T>，并使用new操作符创建ObservedArray<string>的实例，该实例可以观察到属性变化。

在下面的示例中，展示了如何利用@Observed观察二维数组的变化。

```
1. @Observed
2. class ObservedArray<T> extends Array<T> {
3. }

5. @Component
6. struct Item {
7. @ObjectLink itemArr: ObservedArray<string>;

9. build() {
10. Row() {
11. ForEach(this.itemArr, (item: string, index: number) => {
12. Text(`${index}: ${item}`)
13. .width(100)
14. .height(100)
15. }, (item: string) => item)
16. }
17. }
18. }

20. @Entry
21. @Component
22. struct IndexPage {
23. // new操作符创建的ObservedArray<string>的实例可以观察到属性变化
24. @State arr: Array<ObservedArray<string>> = [
25. new ObservedArray<string>('apple'),
26. new ObservedArray<string>('banana'),
27. new ObservedArray<string>('orange')
28. ];

30. build() {
31. Column() {
32. ForEach(this.arr, (itemArr: ObservedArray<string>) => {
33. Item({ itemArr: itemArr })
34. })

36. Divider()

38. Button('push two-dimensional array item')
39. .margin(10)
40. .onClick(() => {
41. this.arr[0].push('strawberry');
42. })

44. Button('push array item')
45. .margin(10)
46. .onClick(() => {
47. this.arr.push(new ObservedArray<string>('pear'));
48. })

50. Button('change two-dimensional array first item')
51. .margin(10)
52. .onClick(() => {
53. this.arr[0][0] = 'APPLE';
54. })

56. Button('change array first item')
57. .margin(10)
58. .onClick(() => {
59. this.arr[0] = new ObservedArray<string>('watermelon');
60. })
61. }
62. }
63. }
```

[TwoDimensionalArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/TwoDimensionalArray.ets#L16-L80)

API version 19及以后，@ObjectLink也可以被[makeV1Observed](../harmonyos-references/js-apis-statemanagement.md#makev1observed19)的返回值初始化。所以开发者如果不想额外声明继承Array的类，也可以使用makeV1Observed来达到同样的效果。

完整例子如下。

```
1. import { UIUtils } from '@kit.ArkUI';

3. @Component
4. struct Item {
5. @ObjectLink itemArr: Array<string>;

7. build() {
8. Row() {
9. ForEach(this.itemArr, (item: string, index: number) => {
10. Text(`${index}: ${item}`)
11. .width(100)
12. .height(100)
13. }, (item: string) => item)
14. }
15. }
16. }

18. @Entry
19. @Component
20. struct IndexPage {
21. // 利用makeV1Observed观察二维数组的变化
22. @State arr: Array<Array<string>> =
23. [UIUtils.makeV1Observed(['apple']), UIUtils.makeV1Observed(['banana']), UIUtils.makeV1Observed(['orange'])];

25. build() {
26. Column() {
27. ForEach(this.arr, (itemArr: Array<string>) => {
28. Item({ itemArr: itemArr })
29. })

31. Divider()

33. Button('push two-dimensional array item')
34. .margin(10)
35. .onClick(() => {
36. this.arr[0].push('strawberry');
37. })

39. Button('push array item')
40. .margin(10)
41. .onClick(() => {
42. this.arr.push(UIUtils.makeV1Observed(['pear']));
43. })

45. Button('change two-dimensional array first item')
46. .margin(10)
47. .onClick(() => {
48. this.arr[0][0] = 'APPLE';
49. })

51. Button('change array first item')
52. .margin(10)
53. .onClick(() => {
54. this.arr[0] = UIUtils.makeV1Observed(['watermelon']);
55. })
56. }
57. }
58. }
```

[CompleteExampleTwoDimensionalArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/CompleteExampleTwoDimensionalArray.ets#L15-L73)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/aCKIneXRQoSmdimR06PCeg/zh-cn_image_0000002558604440.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=00674AF346B5AFE35673FF6D3341C16145AE7DC5DA6BB525D4EFBD7B4493856B)

### 继承Map类

说明

从API version 11开始，@ObjectLink支持@Observed装饰Map类型和继承Map类的类型。

在下面的示例中，myMap类型为MyMap<number, string>，点击Button改变myMap的属性，视图会随之刷新。

```
1. @Observed
2. class Info {
3. public info: MyMap<number, string>;

5. constructor(info: MyMap<number, string>) {
6. this.info = info;
7. }
8. }

10. @Observed
11. export class MyMap<K, V> extends Map<K, V> {
12. public name: string;

14. constructor(name?: string, args?: [K, V][]) {
15. super(args);
16. this.name = name ? name : 'My Map';
17. }

19. getName() {
20. return this.name;
21. }
22. }

24. @Entry
25. @Component
26. struct MapSampleNested {
27. @State message: Info = new Info(new MyMap('myMap', [[0, 'a'], [1, 'b'], [3, 'c']]));

29. build() {
30. Row() {
31. Column() {
32. MapSampleNestedChild({ myMap: this.message.info })
33. }
34. .width('100%')
35. }
36. .height('100%')
37. }
38. }

40. @Component
41. struct MapSampleNestedChild {
42. @ObjectLink myMap: MyMap<number, string>;

44. build() {
45. Row() {
46. Column() {
47. ForEach(Array.from(this.myMap.entries()), (item: [number, string]) => {
48. Text(`${item[0]}`).fontSize(30)
49. Text(`${item[1]}`).fontSize(30)
50. Divider().strokeWidth(5)
51. })

53. // myMap被@Observed和@ObjectLink装饰，可以被观察到Map整体的赋值以及调用Map接口带来的变化
54. Button('set new one')
55. .width(200)
56. .margin(10)
57. .onClick(() => {
58. this.myMap.set(4, 'd');
59. })
60. Button('clear')
61. .width(200)
62. .margin(10)
63. .onClick(() => {
64. this.myMap.clear();
65. })
66. Button('replace the first one')
67. .width(200)
68. .margin(10)
69. .onClick(() => {
70. this.myMap.set(0, 'aa');
71. })
72. Button('delete the first one')
73. .width(200)
74. .margin(10)
75. .onClick(() => {
76. this.myMap.delete(0);
77. })
78. }
79. .width('100%')
80. }
81. .height('100%')
82. }
83. }
```

[InheritFromMapClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/InheritFromMapClass.ets#L15-L99)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/7ZzNl04DQP6Ddv_ttQFCIw/zh-cn_image_0000002589323965.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=A5287C03E36D37D747DC80AF778C6247A1D5C240A04C55500E0AD4DBC6DDCC36)

### 继承Set类

说明

从API version 11开始，@ObjectLink支持@Observed装饰Set类型和继承Set类的类型。

在下面的示例中，mySet类型为MySet<number>，点击Button改变mySet的属性，视图会随之刷新。

```
1. @Observed
2. class Info {
3. public info: MySet<number>;

5. constructor(info: MySet<number>) {
6. this.info = info;
7. }
8. }

10. @Observed
11. export class MySet<T> extends Set<T> {
12. public name: string;

14. constructor(name?: string, args?: T[]) {
15. super(args);
16. this.name = name ? name : 'My Set';
17. }

19. getName() {
20. return this.name;
21. }
22. }

24. @Entry
25. @Component
26. struct SetSampleNested {
27. @State message: Info = new Info(new MySet('Set', [0, 1, 2, 3, 4]));

29. build() {
30. Row() {
31. Column() {
32. SetSampleNestedChild({ mySet: this.message.info })
33. }
34. .width('100%')
35. }
36. .height('100%')
37. }
38. }

40. @Component
41. struct SetSampleNestedChild {
42. @ObjectLink mySet: MySet<number>;

44. build() {
45. Row() {
46. Column() {
47. ForEach(Array.from(this.mySet.entries()), (item: [number, number]) => {
48. Text(`${item}`).fontSize(30)
49. Divider()
50. })
51. // mySet被@Observed和@ObjectLink装饰，可以被观察到Set整体的赋值以及调用Set接口带来的变化
52. Button('set new one')
53. .width(200)
54. .margin(10)
55. .onClick(() => {
56. this.mySet.add(5);
57. })
58. Button('clear')
59. .width(200)
60. .margin(10)
61. .onClick(() => {
62. this.mySet.clear();
63. })
64. Button('delete the first one')
65. .width(200)
66. .margin(10)
67. .onClick(() => {
68. this.mySet.delete(0);
69. })
70. }
71. .width('100%')
72. }
73. .height('100%')
74. }
75. }
```

[InheritFromSetClass.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/InheritFromSetClass.ets#L15-L91)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/qShI7X5qRRGNkPMQDFTE7w/zh-cn_image_0000002589243905.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=30326E951397455A66F049290D1D98A41F6C9DFE9E9EC5E98504BBBD240D44B3)

### ObjectLink支持联合类型

@ObjectLink支持@Observed装饰类和undefined或null组成的联合类型，在下面的示例中，count类型为Source | Data | undefined，点击父组件Parent中的Button改变count的属性或者类型，Child组件中对应的Text组件刷新。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'ArkTSObservedAndObjectlink';

6. @Observed
7. class Source {
8. public source: number;

10. constructor(source: number) {
11. this.source = source;
12. }
13. }

15. @Observed
16. class Data {
17. public data: number;

19. constructor(data: number) {
20. this.data = data;
21. }
22. }

24. @Entry
25. @Component
26. struct Parent {
27. @State count: Source | Data | undefined = new Source(10);

29. build() {
30. Column() {
31. Child({ count: this.count })

33. Button('change count property')
34. .margin(10)
35. .onClick(() => {
36. // 判断count的类型，做属性的更新
37. if (this.count instanceof Source) {
38. this.count.source += 1;
39. } else if (this.count instanceof Data) {
40. this.count.data += 1;
41. } else {
42. hilog.info(DOMAIN, TAG, `count is undefined, cannot change property`);
43. }
44. })

46. Button('change count to Source')
47. .margin(10)
48. .onClick(() => {
49. // 赋值为Source的实例
50. this.count = new Source(100);
51. })

53. Button('change count to Data')
54. .margin(10)
55. .onClick(() => {
56. // 赋值为Data的实例
57. this.count = new Data(100);
58. })

60. Button('change count to undefined')
61. .margin(10)
62. .onClick(() => {
63. // 赋值为undefined
64. this.count = undefined;
65. })
66. }.width('100%')
67. }
68. }

70. @Component
71. struct Child {
72. @ObjectLink count: Source | Data | undefined;

74. build() {
75. Column() {
76. Text(`count is instanceof ${this.count instanceof Source ? 'Source' :
77. this.count instanceof Data ? 'Data' : 'undefined'}`)
78. .fontSize(30)
79. .margin(10)

81. Text(`count's property is  ${this.count instanceof Source ? this.count.source : this.count?.data}`).fontSize(15)

83. }.width('100%')
84. }
85. }
```

[ObjectLinkSupportsUnionTypes.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/objectLinkusagescenarios/ObjectLinkSupportsUnionTypes.ets#L15-L102)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/50cWy7oWTzqJeVeHgiqwFA/zh-cn_image_0000002558764098.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=CE554D18B19646A6B1198A675A153D612C6BC5F80F6277F2AA75870A9E3B1FCC)

## 常见问题

### 基础嵌套对象属性更改失效

在应用开发中，有很多嵌套对象场景，例如，开发者更新了某个属性，但UI没有进行对应的更新。

每个装饰器都有观察能力，但并非所有的改变都可以被观察到，只有可以被观察到的变化才会触发UI更新。@Observed装饰器可以观察到嵌套对象的属性变化，其他装饰器仅能观察到第一层的变化。

【反例】

下面的例子中，一些UI组件并不会更新。

```
1. class Parent {
2. parentId: number;

4. constructor(parentId: number) {
5. this.parentId = parentId;
6. }

8. getParentId(): number {
9. return this.parentId;
10. }

12. setParentId(parentId: number): void {
13. this.parentId = parentId;
14. }
15. }

17. class Child {
18. childId: number;

20. constructor(childId: number) {
21. this.childId = childId;
22. }

24. getChildId(): number {
25. return this.childId;
26. }

28. setChildId(childId: number): void {
29. this.childId = childId;
30. }
31. }

33. class Cousin extends Parent {
34. cousinId: number = 47;
35. child: Child;

37. constructor(parentId: number, cousinId: number, childId: number) {
38. super(parentId);
39. this.cousinId = cousinId;
40. this.child = new Child(childId);
41. }

43. getCousinId(): number {
44. return this.cousinId;
45. }

47. setCousinId(cousinId: number): void {
48. this.cousinId = cousinId;
49. }

51. getChild(): number {
52. return this.child.getChildId();
53. }

55. setChild(childId: number): void {
56. this.child.setChildId(childId);
57. }
58. }

60. @Entry
61. @Component
62. struct MyView {
63. @State cousin: Cousin = new Cousin(10, 20, 30);

65. build() {
66. Column({ space: 10 }) {
67. Text(`parentId: ${this.cousin.parentId}`)
68. Button('Change Parent.parent')
69. .onClick(() => {
70. this.cousin.parentId += 1;
71. })

73. Text(`cousinId: ${this.cousin.cousinId}`)
74. Button('Change Cousin.cousinId')
75. .onClick(() => {
76. this.cousin.cousinId += 1;
77. })

79. Text(`childId: ${this.cousin.child.childId}`)
80. Button('Change Cousin.Child.childId')
81. .onClick(() => {
82. // 点击时上面的Text组件不会刷新
83. this.cousin.child.childId += 1;
84. })
85. }
86. }
87. }
```

* 最后一个Text组件Text('child: ${this.cousin.child.childId}')，当点击该组件时UI不会刷新。 因为，@State cousin : Cousin 只能观察到this.cousin属性的变化，比如this.cousin.parentId, this.cousin.cousinId 和this.cousin.child的变化，但是无法观察嵌套在属性中的属性，即this.cousin.child.childId（属性childId是内嵌在cousin中的对象Child的属性）。
* 为了观察到嵌套于内部的Child的属性，需要做如下改变：

  + 构造一个子组件，用于单独渲染Child的实例。 该子组件可以使用@ObjectLink child : Child或@Prop child : Child。通常会使用@ObjectLink，除非子组件需要对其Child对象进行本地修改。
  + 嵌套的Child必须用@Observed装饰。当在Cousin中创建Child对象时（本示例中的Cousin(10, 20, 30）)，它将被包装在ES6代理中，当Child属性更改时（this.cousin.child.childId += 1），该代码将修改通知到@ObjectLink变量。

【正例】

以下示例使用@Observed/@ObjectLink来观察嵌套对象的属性更改。

```
1. class Parent {
2. public parentId: number;

4. constructor(parentId: number) {
5. this.parentId = parentId;
6. }

8. getParentId(): number {
9. return this.parentId;
10. }

12. setParentId(parentId: number): void {
13. this.parentId = parentId;
14. }
15. }

17. @Observed
18. class Child {
19. public childId: number;

21. constructor(childId: number) {
22. this.childId = childId;
23. }

25. getChildId(): number {
26. return this.childId;
27. }

29. setChildId(childId: number): void {
30. this.childId = childId;
31. }
32. }

34. class Cousin extends Parent {
35. public cousinId: number = 47;
36. public child: Child;

38. constructor(parentId: number, cousinId: number, childId: number) {
39. super(parentId);
40. this.cousinId = cousinId;
41. this.child = new Child(childId);
42. }

44. getCousinId(): number {
45. return this.cousinId;
46. }

48. setCousinId(cousinId: number): void {
49. this.cousinId = cousinId;
50. }

52. getChild(): number {
53. return this.child.getChildId();
54. }

56. setChild(childId: number): void {
57. this.child.setChildId(childId);
58. }
59. }

61. @Component
62. struct ViewChild {
63. @ObjectLink child: Child;

65. build() {
66. Column({ space: 10 }) {
67. Text(`childId: ${this.child.getChildId()}`)
68. Button('Change childId')
69. .onClick(() => {
70. this.child.setChildId(this.child.getChildId() + 1);
71. })
72. }
73. }
74. }

76. @Entry
77. @Component
78. struct MyView {
79. @State cousin: Cousin = new Cousin(10, 20, 30);

81. build() {
82. Column({ space: 10 }) {
83. Text(`parentId: ${this.cousin.parentId}`)
84. Button('Change Parent.parentId')
85. .onClick(() => {
86. this.cousin.parentId += 1;
87. })

89. Text(`cousinId: ${this.cousin.cousinId}`)
90. Button('Change Cousin.cousinId')
91. .onClick(() => {
92. this.cousin.cousinId += 1;
93. })

95. ViewChild({ child: this.cousin.child }) // Text(`childId: ${this.cousin.child.childId}`)的替代写法
96. Button('Change Cousin.Child.childId')
97. .onClick(() => {
98. this.cousin.child.childId += 1;
99. })
100. }
101. }
102. }
```

[BasicNesting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/BasicNesting.ets#L15-L118)

### 复杂嵌套对象属性更改失效

【反例】

以下示例创建了一个带有@ObjectLink装饰变量的子组件，用于渲染一个含有嵌套属性的ParentCounter，用@Observed装饰嵌套在ParentCounter中的SubCounter。

```
1. let nextId = 1;
2. @Observed
3. class SubCounter {
4. counter: number;
5. constructor(c: number) {
6. this.counter = c;
7. }
8. }
9. @Observed
10. class ParentCounter {
11. id: number;
12. counter: number;
13. subCounter: SubCounter;
14. incrCounter() {
15. this.counter++;
16. }
17. incrSubCounter(c: number) {
18. this.subCounter.counter += c;
19. }
20. setSubCounter(c: number): void {
21. this.subCounter.counter = c;
22. }
23. constructor(c: number) {
24. this.id = nextId++;
25. this.counter = c;
26. this.subCounter = new SubCounter(c);
27. }
28. }
29. @Component
30. struct CounterComp {
31. @ObjectLink value: ParentCounter;
32. build() {
33. Column({ space: 10 }) {
34. Text(`${this.value.counter}`)
35. .fontSize(25)
36. .onClick(() => {
37. this.value.incrCounter();
38. })
39. Text(`${this.value.subCounter.counter}`)
40. .onClick(() => {
41. this.value.incrSubCounter(1);
42. })
43. Divider().height(2)
44. }
45. }
46. }
47. @Entry
48. @Component
49. struct ParentComp {
50. @State counter: ParentCounter[] = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
51. build() {
52. Row() {
53. Column() {
54. CounterComp({ value: this.counter[0] })
55. CounterComp({ value: this.counter[1] })
56. CounterComp({ value: this.counter[2] })
57. Divider().height(5)
58. ForEach(this.counter,
59. (item: ParentCounter) => {
60. CounterComp({ value: item })
61. },
62. (item: ParentCounter) => item.id.toString()
63. )
64. Divider().height(5)
65. // 第一个点击事件
66. Text('Parent: incr counter[0].counter')
67. .fontSize(20).height(50)
68. .onClick(() => {
69. this.counter[0].incrCounter();
70. // 每次触发时自增10
71. this.counter[0].incrSubCounter(10);
72. })
73. // 第二个点击事件
74. Text('Parent: set.counter to 10')
75. .fontSize(20).height(50)
76. .onClick(() => {
77. // 无法将value设置为10，UI不会刷新
78. this.counter[0].setSubCounter(10);
79. })
80. Text('Parent: reset entire counter')
81. .fontSize(20).height(50)
82. .onClick(() => {
83. this.counter = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
84. })
85. }
86. }
87. }
88. }
```

对于Text('Parent: incr counter[0].counter')的onClick事件，this.counter[0].incrSubCounter(10)调用incrSubCounter方法使SubCounter的counter值增加10，UI同步刷新。

然而，在Text('Parent: set.counter to 10')的onClick中调用this.counter[0].setSubCounter(10)时，SubCounter的counter值无法重置为10。

incrSubCounter和setSubCounter都是同一个SubCounter的函数。在第一个点击处理时调用incrSubCounter可以正确更新UI，而第二个点击处理调用setSubCounter时却没有更新UI。实际上incrSubCounter和setSubCounter两个函数都不能触发Text('${this.value.subCounter.counter}')的更新，因为@ObjectLink value : ParentCounter仅能观察其代理ParentCounter的属性，对于this.value.subCounter.counter是SubCounter的属性，无法观察到嵌套类的属性。

另外，第一个click事件调用this.counter[0].incrCounter()将CounterComp自定义组件中的@ObjectLink value: ParentCounter标记为已更改，会触发Text('${this.value.subCounter.counter}')的更新。如果在第一个点击事件中删除this.counter[0].incrCounter()，则无法更新UI。

【正例】

对于上述问题，为了直接观察SubCounter中的属性，以便this.counter[0].setSubCounter(10)操作有效，可以利用下面的方法：

```
1. let nextId = 1;

3. @Observed
4. class SubCounter {
5. public counter: number;

7. constructor(c: number) {
8. this.counter = c;
9. }
10. }

12. @Observed
13. class ParentCounter {
14. public id: number;
15. public counter: number;
16. public subCounter: SubCounter;

18. incrCounter() {
19. this.counter++;
20. }

22. incrSubCounter(c: number) {
23. this.subCounter.counter += c;
24. }

26. setSubCounter(c: number): void {
27. this.subCounter.counter = c;
28. }

30. constructor(c: number) {
31. this.id = nextId++;
32. this.counter = c;
33. this.subCounter = new SubCounter(c);
34. }
35. }

38. @Entry
39. @Component
40. struct ParentComp {
41. @State counter: ParentCounter[] = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
42. build() {
43. Row() {
44. CounterComp({ value: this.counter[0] }) // ParentComp组件传递 ParentCounter 给 CounterComp 组件
45. }
46. }
47. }

49. @Component
50. struct CounterComp {
51. @ObjectLink value: ParentCounter; // @ObjectLink 接收 ParentCounter
52. build() {
53. // CounterChild 是 CounterComp 的子组件，CounterComp 传递 this.value.subCounter 给 CounterChild 组件
54. CounterChild({ subValue: this.value.subCounter })
55. }
56. }

58. @Component
59. struct CounterChild {
60. @ObjectLink subValue: SubCounter; // @ObjectLink 接收 SubCounter
61. build() {
62. Text(`${this.subValue.counter}`)
63. .onClick(() => {
64. this.subValue.counter += 1;
65. })
66. }
67. }
```

[ComplexMethodsNesting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/ComplexMethodsNesting.ets#L15-L83)

该方法使得@ObjectLink分别代理了ParentCounter和SubCounter的属性，这样对于这两个类的属性的变化都可以观察到，即都会对UI视图进行刷新。即使删除了上面所说的this.counter[0].incrCounter()，UI也会进行正确的刷新。

该方法可用于实现“两个层级”的观察，即外部对象和内部嵌套对象的观察。但是该方法只能用于@ObjectLink装饰器，无法作用于@Prop（@Prop通过深拷贝传入对象）。详情参考[@Prop与@ObjectLink的差异](arkts-observed-and-objectlink.md#prop与objectlink的差异)。

```
1. let nextId = 1;

3. @Observed
4. class SubCounter {
5. public counter: number;

7. constructor(c: number) {
8. this.counter = c;
9. }
10. }

12. @Observed
13. class ParentCounter {
14. public id: number;
15. public counter: number;
16. public subCounter: SubCounter;

18. incrCounter() {
19. this.counter++;
20. }

22. incrSubCounter(c: number) {
23. this.subCounter.counter += c;
24. }

26. setSubCounter(c: number): void {
27. this.subCounter.counter = c;
28. }

30. constructor(c: number) {
31. this.id = nextId++;
32. this.counter = c;
33. this.subCounter = new SubCounter(c);
34. }
35. }

37. @Component
38. struct CounterComp {
39. @ObjectLink value: ParentCounter;

41. build() {
42. Column({ space: 10 }) {
43. Text(`${this.value.counter}`)
44. .fontSize(25)
45. .onClick(() => {
46. this.value.incrCounter();
47. })
48. CounterChild({ subValue: this.value.subCounter })
49. Divider().height(2)
50. }
51. }
52. }

54. @Component
55. struct CounterChild {
56. @ObjectLink subValue: SubCounter;

58. build() {
59. Text(`${this.subValue.counter}`)
60. .onClick(() => {
61. this.subValue.counter += 1;
62. })
63. }
64. }

66. @Entry
67. @Component
68. struct ParentComp {
69. // @ObjectLink分别代理了ParentCounter和SubCounter的属性，这两个类的属性的变化都可以观察到
70. @State counter: ParentCounter[] = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];

72. build() {
73. Row() {
74. Column() {
75. CounterComp({ value: this.counter[0] })
76. CounterComp({ value: this.counter[1] })
77. CounterComp({ value: this.counter[2] })
78. Divider().height(5)
79. ForEach(this.counter,
80. (item: ParentCounter) => {
81. CounterComp({ value: item })
82. },
83. (item: ParentCounter) => item.id.toString()
84. )
85. Divider().height(5)
86. Text('Parent: reset entire counter')
87. .fontSize(20).height(50)
88. .onClick(() => {
89. this.counter = [new ParentCounter(1), new ParentCounter(2), new ParentCounter(3)];
90. })
91. Text('Parent: incr counter[0].counter')
92. .fontSize(20).height(50)
93. .onClick(() => {
94. this.counter[0].incrCounter();
95. this.counter[0].incrSubCounter(10);
96. })
97. Text('Parent: set.counter to 10')
98. .fontSize(20).height(50)
99. .onClick(() => {
100. this.counter[0].setSubCounter(10);
101. })
102. }
103. }
104. }
105. }
```

[ComplexNestingComplete.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/ComplexNestingComplete.ets#L15-L121)

### @Prop与@ObjectLink的差异

@Prop和@ObjectLink都可以接收@Observed装饰的类对象实例。@Prop对对象进行深拷贝，修改深拷贝后的对象不会影响原对象及其关联的组件。@ObjectLink获取对象的引用，修改引用对象会影响原对象及其关联的组件。

下面的例子中，UserChild组件同时使用@Prop与@ObjectLink接收了来自父组件的@Observed装饰的类对象实例作为数据源。对该数据源对象的修改将同时影响@Prop与@ObjectLink装饰的变量。依次点击change @ObjectLink value按钮和change @Prop value按钮可以观察到：

1. 修改@ObjectLink装饰的对象内容将影响数据源对象，并重新同步给@Prop，因此两个Text组件都将刷新。
2. 修改@Prop装饰的对象内容仅影响使用该对象的Text2组件，不会影响数据源对象。

```
1. let nextId = 0;

3. @Observed
4. class User {
5. public id: number;

7. constructor() {
8. this.id = nextId++;
9. }
10. }

12. @Entry
13. @Component
14. struct Index {
15. @State users: User[] = [new User(), new User(), new User()];

17. build() {
18. Column() {
19. UserChild({ firstUserByObjectLink: this.users[0], firstUserByProp: this.users[0] })
20. }
21. }
22. }

24. @Component
25. struct UserChild {
26. @ObjectLink firstUserByObjectLink: User;
27. @Prop firstUserByProp: User;

29. build() {
30. Column() {
31. // 比较结果为false说明@Prop经过深拷贝后得到的对象与原对象已不是同一个对象
32. Text(`firstUserByObjectLink equals firstUserByProp? : ${this.firstUserByObjectLink === this.firstUserByProp}`)
33. Text(`UserChild firstUserByObjectLink.id: ${this.firstUserByObjectLink.id}`) // Text1
34. Text(`UserChild firstUserByProp.id: ${this.firstUserByProp.id}`) // Text2
35. Button('change @ObjectLink value')
36. .onClick(() => {
37. this.firstUserByObjectLink.id++;
38. })
39. Button('change @Prop value')
40. .onClick(() => {
41. this.firstUserByProp.id++;
42. })
43. }
44. }
45. }
```

[DifferencesPropObjectLink.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/DifferencesPropObjectLink.ets#L15-L61)

上面的示例关系如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/b2u59-lMQDWcYkikHlMkTw/zh-cn_image_0000002558604442.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=C424A039F55D7838ACFABD0D2F9D7EA2BD678D55E95DF590FB231E242FFCA9AA)

### 在@Observed装饰类的构造函数中延时更改成员变量

在状态管理中，使用@Observed装饰类后，会给该类使用一层“代理”进行包装。当在组件中改变该类的成员变量时，会被该代理进行拦截，在更改数据源中值的同时，也会将变化通知给绑定的组件，从而实现观测变化与触发刷新。

当开发者在类的构造函数中对成员变量进行赋值或者修改时，此修改不会经过代理（因为是直接对数据源中的值进行修改），也就无法被观测到。所以，如果开发者在类的构造函数中使用定时器修改类中的成员变量，即使该修改成功执行了，也不会触发UI的刷新。

【反例】

```
1. @Observed
2. class RenderClass {
3. waitToRender: boolean = false;

5. constructor() {
6. setTimeout(() => {
7. this.waitToRender = true;
8. console.info('更改waitToRender的值为：' + this.waitToRender);
9. }, 1000)
10. }
11. }

13. @Entry
14. @Component
15. struct Index {
16. @State @Watch('renderClassChange') renderClass: RenderClass = new RenderClass();
17. @State textColor: Color = Color.Black;

19. renderClassChange() {
20. console.info('renderClass的值被更改为：' + this.renderClass.waitToRender);
21. }

23. build() {
24. Row() {
25. Column() {
26. Text('renderClass的值为：' + this.renderClass.waitToRender)
27. .fontSize(20)
28. .fontColor(this.textColor)
29. Button('Show')
30. .onClick(() => {
31. // 使用其他状态变量强行刷新UI的做法并不推荐，此处仅用来检测waitToRender的值是否更新
32. this.textColor = Color.Red;
33. })
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```

上文的示例代码中在RenderClass的构造函数中使用定时器在1秒后修改了waitToRender的值，但是不会触发UI的刷新。此时，点击按钮强行刷新Text组件，可以看到waitToRender的值已经被修改成了true。

【正例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'ArkTSObservedAndObjectlink';

6. @Observed
7. class RenderClass {
8. public waitToRender: boolean = false;

10. constructor() {
11. }
12. }

14. @Entry
15. @Component
16. struct DelayedChangeIndex {
17. @State @Watch('renderClassChange') renderClass: RenderClass = new RenderClass();

19. renderClassChange() {
20. hilog.info(DOMAIN, TAG, `The value of renderClass is changed to: ${this.renderClass.waitToRender}`);
21. }

23. onPageShow() {
24. setTimeout(() => {
25. this.renderClass.waitToRender = true;
26. }, 1000);
27. }

29. build() {
30. Row() {
31. Column() {
32. Text(`The value of renderClass is: ${this.renderClass.waitToRender}`)
33. .fontSize(20)
34. }
35. .width('100%')
36. }
37. .height('100%')
38. }
39. }
```

[DelayedChange.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/DelayedChange.ets#L15-L55)

上文的示例代码将定时器修改移入到组件内，此时界面显示时会先显示“The value of renderClass is：false”。待定时器触发时，renderClass的值改变，触发[@Watch](arkts-watch.md)回调，此时界面刷新显示“The value of renderClass is：true”，日志输出“The value of renderClass is changed to：true”。

因此，更推荐开发者在组件中对@Observed装饰的类成员变量进行修改，以实现刷新。

### @ObjectLink数据源更新时机

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN = 0x0001;
4. const TAG = 'ArkTSObservedAndObjectlink';

6. @Observed
7. class Person {
8. public name: string = '';
9. public age: number = 0;

11. constructor(name: string, age: number) {
12. this.name = name;
13. this.age = age;
14. }
15. }

17. @Observed
18. class Info {
19. public person: Person;

21. constructor(person: Person) {
22. this.person = person;
23. }
24. }

26. @Entry
27. @Component
28. struct Parent {
29. @State @Watch('onChange01') info: Info =
30. new Info(
31. new Person('Bob', 10)
32. );

34. onChange01() {
35. hilog.info(DOMAIN, TAG, `:::onChange01: + ${this.info.person.name}`); // 2
36. }

38. build() {
39. Column() {
40. Text(this.info.person.name).height(40)
41. Child({
42. per: this.info.person, clickEvent: () => {
43. hilog.info(DOMAIN, TAG, `:::clickEvent before ${this.info.person.name}`); // 1
44. this.info.person = new Person('Jack', 12);
45. hilog.info(DOMAIN, TAG, `:::clickEvent after ${this.info.person.name}`); // 3
46. }
47. })
48. }
49. }
50. }

52. @Component
53. struct Child {
54. @ObjectLink @Watch('onChange02') per: Person;
55. clickEvent?: () => void;

57. onChange02() {
58. hilog.info(DOMAIN, TAG, `:::onChange02:${this.per.name}`); // 5
59. }

61. build() {
62. Column() {
63. Button(this.per.name)
64. .height(40)
65. .onClick(() => {
66. this.onClickType();
67. })
68. }
69. }

71. private onClickType() {
72. if (this.clickEvent) {
73. this.clickEvent();
74. }
75. hilog.info(DOMAIN, TAG, `:::--------this.per.name in Child is still: ${this.per.name}`); // 4
76. };
77. }
```

[ObjectLinkDataSourceUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/ObjectLinkDataSourceUpdate.ets#L15-L93)

@ObjectLink的数据源更新依赖其父组件，当父组件中数据源改变引起父组件刷新时，会重新设置子组件@ObjectLink的数据源。这个过程不是在父组件数据源变化后立刻发生的，而是在父组件实际刷新时才会进行。上述示例中，Parent包含Child，Parent传递箭头函数给Child，在点击时，日志打印顺序是1-2-3-4-5，打印到日志4时，点击事件流程结束，此时仅仅是将子组件Child标记为需要父组件更新的节点，因此日志4打印的this.per.name的值仍为Bob，等到父组件真正更新时，才会更新Child的数据源。

当@ObjectLink @Watch('onChange02') per: Person的@Watch函数执行时，说明@ObjectLink的数据源已被父组件更新，此时日志5打印的值为更新后的Jack。

日志的含义为：

* 日志1：对Parent @State @Watch('onChange01') info: Info = new Info(new Person('Bob', 10)) 赋值前。
* 日志2：对Parent @State @Watch('onChange01') info: Info = new Info(new Person('Bob', 10)) 赋值，执行其@Watch函数，同步执行。
* 日志3：对Parent @State @Watch('onChange01') info: Info = new Info(new Person('Bob', 10)) 赋值完成。
* 日志4：onClickType方法内clickEvent执行完，此时只是将子组件Child标记为需要父组件更新的节点，未将最新的值更新给Child @ObjectLink @Watch('onChange02') per: Person，所以日志4打印的this.per.name的值仍然是Bob。
* 日志5：下一次vsync信号触发Child更新，@ObjectLink @Watch('onChange02') per: Person被更新，触发其@Watch方法，此时@ObjectLink @Watch('onChange02') per: Person为新值Jack。

@Prop父子同步原理与@ObjectLink一致。

当clickEvent中更改this.info.person.name时，修改会立刻生效，此时日志4打印的值是Jack。

```
1. Child({
2. per: this.info.person, clickEvent: () => {
3. hilog.info(DOMAIN, TAG, `:::clickEvent before ${this.info.person.name}`); // 1
4. this.info.person.name = 'Jack';
5. hilog.info(DOMAIN, TAG, `:::clickEvent after ${this.info.person.name}`); // 3
6. }
7. })
```

[ClickEventJack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/arktsobservedandobjectlink/entry/src/main/ets/pages/ObservedAndObjectLinkFAQs/ClickEventJack.ets#L52-L60)

此时Parent中Text组件不会刷新，因为this.info.person.name属于两层嵌套。

### @Observed装饰的类，在构造函数中使用this赋值属性，不触发UI更新

@Observed类的构造函数中对成员变量进行赋值或者修改时，此修改不会经过代理，无法被观测到。

【反例】

```
1. @Observed
2. class DataDownloader {
3. state: number;
4. constructor() {
5. this.state = 0;
6. setInterval(() => {
7. // 从构造函数修改成员变量，不触发UI更新
8. this.state += 1;
9. }, 2000);
10. }
11. }

13. @Entry
14. @Component
15. struct Index {
16. @State dataDownloader: DataDownloader = new DataDownloader();
17. build() {
18. Column() {
19. Text(`Download state is ${this.dataDownloader.state}`)
20. }
21. }
22. }
```

【正例】

```
1. @Observed
2. class DataDownloader {
3. public state: number;

5. constructor() {
6. this.state = 0;
7. }

9. startIntervalUpdate() {
10. setInterval(() => {
11. this.state += 1;
12. }, 2000);
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. @State dataDownloader: DataDownloader = new DataDownloader();

21. aboutToAppear() {
22. this.dataDownloader.startIntervalUpdate(); // @Observed装饰的类构建后再修改属性可以触发更新UI
23. }

25. build() {
26. Column() {
27. Text(`Download state is ${this.dataDownloader.state}`)
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/D6wKNCppT6qrm9g-_CvDQA/zh-cn_image_0000002589323967.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=F508B919397CFB704EC356FCEF0B9F319219297D7B2D9C877F1F66F7D1FF5B97)

### LazyForEach和@ObjectLink一起使用时，替换数组数据后UI不刷新

@Observed装饰的类的数组，用[LazyForEach](arkts-rendering-control-lazyforeach.md)展开显示的时候，可能会出现替换数组数据后，修改数组数据不刷新UI的问题。改变数组数据后，需要调用onDataChange通知LazyForEach组件重新绑定状态变量，否则就会出现上述问题。

【反例】

```
1. // LazyForEach遍历数据基类
2. class BasicDataSource implements IDataSource {
3. private listeners: DataChangeListener[] = [];
4. private originDataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.originDataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.originDataArray[index];
12. }

14. registerDataChangeListener(listener: DataChangeListener): void {
15. if (this.listeners.indexOf(listener) < 0) {
16. console.info('add listener');
17. this.listeners.push(listener);
18. }
19. }

21. unregisterDataChangeListener(listener: DataChangeListener): void {
22. const pos = this.listeners.indexOf(listener);
23. if (pos >= 0) {
24. console.info('remove listener');
25. this.listeners.splice(pos, 1);
26. }
27. }

29. notifyDataAdd(index: number): void {
30. this.listeners.forEach(listener => {
31. listener.onDataAdd(index);
32. });
33. }
34. }

36. // LazyForEach遍历数据类型
37. class MyDataSource extends BasicDataSource {
38. public dataArray: StringData[] = [];

40. public totalCount(): number {
41. return this.dataArray.length;
42. }

44. public getData(index: number): StringData {
45. return this.dataArray[index];
46. }

48. public pushData(data: StringData): void {
49. this.dataArray.push(data);
50. this.notifyDataAdd(this.dataArray.length - 1);
51. }
52. }

54. @Observed
55. class StringData {
56. message: string;

58. constructor(message: string) {
59. this.message = message;
60. }
61. }

63. @Entry
64. @Component
65. struct MyComponent {
66. private data: MyDataSource = new MyDataSource();
67. helloCount: number = 4;

69. aboutToAppear() {
70. for (let i = 0; i <= 3; i++) {
71. this.data.pushData(new StringData(`Hello ${i}`));
72. }
73. }

75. build() {
76. Column() {
77. List({ space: 3 }) {
78. // 使用LazyForEach懒加载遍历数据
79. LazyForEach(this.data, (item: StringData, index: number) => {
80. ListItem() {
81. ChildComponent({ data: item })
82. }
83. }, (item: StringData, index: number) => index.toString() + item.message)
84. }.cachedCount(3)
85. Button('替换第一个元素')
86. .onClick(() => {
87. // 替换数组元素不刷新UI，此时新替换的值还未绑定到LazyForEach组件上。
88. this.data.dataArray[0] = new StringData('Hello ' + this.helloCount++)
89. })
90. Button('修改第一个元素的数据')
91. .onClick(() => {
92. // 替换数组元素后修改元素值也不会刷新UI。
93. this.data.dataArray[0].message += '1';
94. })
95. }
96. }
97. }

99. // 使用@Reusable实现组件复用
100. @Reusable
101. @Component
102. struct ChildComponent {
103. // 使用@ObjectLink接收@Observed装饰的类的数据
104. @ObjectLink data: StringData;

106. aboutToAppear(): void {
107. console.info(`aboutToAppear: ${this.data.message}`);
108. }

110. aboutToRecycle(): void {
111. console.info(`aboutToRecycle: ${this.data.message}`);
112. }

114. // 对复用的组件进行数据更新
115. aboutToReuse(params: Record<string, ESObject>): void {
116. this.data.message = (params.data as StringData).message;
117. console.info(`aboutToReuse: ${this.data.message}`);
118. }

120. build() {
121. Row() {
122. Text(this.data.message)
123. .fontSize(50)
124. .onAppear(() => {
125. console.info(`appear: ${this.data.message}`);
126. })
127. }.margin({ left: 10, right: 10 })
128. }
129. }
```

【正例】

```
1. // LazyForEach遍历数据基类
2. class BasicDataSource implements IDataSource {
3. private listeners: DataChangeListener[] = [];
4. private originDataArray: StringData[] = [];

6. public totalCount(): number {
7. return this.originDataArray.length;
8. }

10. public getData(index: number): StringData {
11. return this.originDataArray[index];
12. }

14. registerDataChangeListener(listener: DataChangeListener): void {
15. if (this.listeners.indexOf(listener) < 0) {
16. console.info('add listener');
17. this.listeners.push(listener);
18. }
19. }

21. unregisterDataChangeListener(listener: DataChangeListener): void {
22. const pos = this.listeners.indexOf(listener);
23. if (pos >= 0) {
24. console.info('remove listener');
25. this.listeners.splice(pos, 1);
26. }
27. }

29. notifyDataAdd(index: number): void {
30. this.listeners.forEach(listener => {
31. listener.onDataAdd(index);
32. });
33. }

35. // 通知LazyForEach处理数据替换
36. notifyDataChanged(index: number): void {
37. this.listeners.forEach(listener => {
38. listener.onDataChange(index);
39. })
40. }
41. }

43. // LazyForEach遍历数据类型
44. class MyDataSource extends BasicDataSource {
45. public dataArray: StringData[] = [];

47. public totalCount(): number {
48. return this.dataArray.length;
49. }

51. public getData(index: number): StringData {
52. return this.dataArray[index];
53. }

55. public pushData(data: StringData): void {
56. this.dataArray.push(data);
57. this.notifyDataAdd(this.dataArray.length - 1);
58. }
59. }

61. @Observed
62. class StringData {
63. public message: string;

65. constructor(message: string) {
66. this.message = message;
67. }
68. }

70. @Entry
71. @Component
72. struct MyComponent {
73. private data: MyDataSource = new MyDataSource();
74. helloCount: number = 4;

76. aboutToAppear() {
77. for (let i = 0; i <= 2; i++) {
78. this.data.pushData(new StringData(`Hello ${i}`));
79. }
80. }

82. build() {
83. Column({ space: 3 }) {
84. List({ space: 3 }) {
85. // 使用LazyForEach懒加载遍历数据
86. LazyForEach(this.data, (item: StringData, index: number) => {
87. ListItem() {
88. ChildComponent({ data: item })
89. }.width('100%')
90. // LazyForEach的key从index和message构建，每次替换元素时，需要修改key才能触发UI刷新。
91. }, (item: StringData, index: number) => index.toString() + item.message)
92. }.cachedCount(3)
93. Button('替换第一个元素')
94. .onClick(() => {
95. this.data.dataArray[0] = new StringData('Hello ' + this.helloCount++);
96. // 替换元素后通知LazyForEach，可以刷新UI。
97. this.data.notifyDataChanged(0);
98. })
99. Button('修改第一个元素的数据')
100. .onClick(() => {
101. // 替换元素后由于重新建立绑定，后续修改元素值也能刷新UI。
102. this.data.dataArray[0].message += '1';
103. })
104. }
105. .width('100%')
106. .alignItems(HorizontalAlign.Center)
107. }
108. }

110. // 使用Reusable使能组件复用
111. @Reusable
112. @Component
113. struct ChildComponent {
114. // 使用@ObjectLink接受@Observed类数据
115. @ObjectLink data: StringData;

117. aboutToAppear(): void {
118. console.info(`aboutToAppear: ${this.data.message}`);
119. }

121. aboutToRecycle(): void {
122. console.info(`aboutToRecycle: ${this.data.message}`);
123. }

125. // 对复用的组件进行数据更新
126. aboutToReuse(params: Record<string, ESObject>): void {
127. this.data.message = (params.data as StringData).message;
128. console.info(`aboutToReuse: ${this.data.message}`);
129. }

131. build() {
132. Row() {
133. Text(this.data.message)
134. .fontSize(50)
135. .onAppear(() => {
136. console.info(`appear: ${this.data.message}`);
137. })
138. }.margin({ left: 10, right: 10 })
139. }
140. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/fOC1X8uNTyeLsL_NkcoA3g/zh-cn_image_0000002589243907.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052712Z&HW-CC-Expire=86400&HW-CC-Sign=BA19A854B0A68EC6197FB2C7AF5710BEC493FE69CB11C4F9CB70A4734B063028)
