---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-mixusage-before-api-version
title: 状态管理V1和V2混用指导（API version 19前）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1和V2混用场景 > 状态管理V1和V2混用指导（API version 19前）
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ad868b9489f05c82862691d0ed3b755b3bd76dbaede8e56a4feef99ffcfa8596
---

## 概述

说明

本文档中使用“->”表示变量的传递，比如“V1->V2”，表示V1状态变量向V2状态变量传递。

在API version 19之前，混用场景有相对严格的校验，状态管理V1与V2的混用规则如下：

**1. V1->V2规则总结**

* V1的自定义组件中不可以使用V2的装饰器，否则编译报错。
* 当组件间不传递变量时，V1的自定义组件中可以使用V2的自定义组件，包括导入第三方的@ComponentV2装饰的自定义组件。
* 组件间存在变量传递时，V1的变量传递给V2的自定义组件，有以下限制：

  + V1中未被装饰器装饰的变量（后称普通变量）：V2只能使用@Param接收。
  + V1中被装饰器装饰的变量（后称状态变量）：V2只能通过@Param装饰器接收，且仅限于boolean、number、enum、string、undefined、null这些简单类型数据。

**2. V2->V1规则总结**

* V2的自定义组件中不可以使用V1的装饰器，否则编译报错。
* 组件间不存在变量传递时，V2自定义组件可以使用V1的自定义组件，包括导入第三方的@Component装饰的自定义组件。
* 组件间存在变量传递时，V2的变量传递给V1的自定义组件，有以下限制：

  + V2普通变量（未使用状态变量装饰器）传递给V1自定义组件：

    如果V1使用状态变量接收该数据，只能使用[@State](arkts-state.md)、[@Prop](arkts-prop.md)、[@Provide](arkts-provide-and-consume.md)这三种V1的状态变量装饰器。
  + V2状态变量（使用状态变量装饰器）传递给V1自定义组件：

    如果V1使用状态变量装饰器（同样仅限@State、@Prop、@Provide支持）装饰接收的数据，不支持内置类型数据：Array、Set、Map、Date。需要注意V2状态变量支持Function类型，但是V1的状态变量装饰器均不支持Function类型，传递Function类型会导致运行时校验报错。以@State为例，详情见[@State限制条件](arkts-state.md#限制条件)。
  + V1中[@Link](arkts-link.md)遵循其原本初始化规则，只能被V1状态变量初始化，详情见[@Link初始化规则示意图](arkts-link.md#变量的传递访问规则说明)。

## 限制条件

* V1和V2的装饰器不允许混用。

  V1的组件内装饰器不支持在V2的自定义组件中使用，V2的组件内装饰器也不支持在V1的自定义组件中使用，编译会报错。
* V1装饰器不能和[@ObservedV2](arkts-new-observedv2-and-trace.md)一起使用，否则编译报错。
* V2装饰器不能和[@Observed](arkts-observed-and-objectlink.md)一起使用，否则编译报错。
* V1->V2传递状态变量只支持简单类型，不允许传复杂类型的状态变量。比如传递@Observed装饰的class、装饰器修饰的built-in类型（Array、Map、Set、Date），编译报错。
* V2->V1可以传简单类型状态变量和普通class。如果传递@ObservedV2装饰的class、装饰器修饰的built-in类型（Array、Map、Set、Date），编译报错。
* V1中@ObjectLink只接受@Observed装饰的class初始化。
* V1中[@Link](arkts-link.md)遵循其原本初始化规则，只能被V1状态变量初始化，详情见[@Link初始化规则示意图](arkts-link.md#变量的传递访问规则说明)。
* 多个装饰器不允许装饰同一个变量（@Watch、@Once、@Require除外）。

  ```
  1. @State @Prop message: string = "";  // 多个V1的装饰器不可以修饰同一个变量，编译器报错
  ```

  ```
  1. @Local @Param message: string = 'Hello World'; // 多个V2的装饰器不允许修饰同一个变量，编译器报错
  ```

  除了@Watch、@Once、@Require这些能力扩展装饰器可以与其他装饰器配合使用外，其他装饰器不允许装饰同一个变量。

## V1中使用V2的自定义组件

### 不传递变量

在V1中使用V2的自定义组件时，如果不存在变量传递，则不会产生影响。以下示例代码中，ChildSix是不接受参数的V2自定义组件，IndexSix可直接使用ChildSix。

```
1. @ComponentV2
2. struct ChildSix {
3. @Local message: string = 'hello';

5. build() {
6. Column() {
7. Text(this.message)
8. .fontSize(50)
9. .fontWeight(FontWeight.Bold)
10. .onClick(() => {
11. this.message = 'world';
12. })
13. }
14. }
15. }

17. @Entry
18. @Component
19. struct IndexSix {
20. @State message: string = 'Hello World';

22. build() {
23. Column() {
24. Text(this.message)
25. .fontSize(50)
26. .fontWeight(FontWeight.Bold)
27. .onClick(() => {
28. this.message = 'world hello';
29. })
30. Divider()
31. .color(Color.Blue)
32. // 可以只是使用无参数的V2组件
33. ChildSix()
34. }
35. .height('100%')
36. .width('100%')
37. }
38. }
```

[V2InV1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsMixingUse/entry/src/main/ets/pages/MixingUseofCustomComponents/V2InV1.ets#L16-L54)

### 传递未被装饰的变量

当变量未被装饰器装饰时，不具备被观测的能力。将该变量传递给V2时，需注意V2组件对数据输入有严格的管理，必须通过[@Param](arkts-new-param.md)装饰器接收。V2中接收数据的观测能力为@Param能力，对于接收的Class，需要通过@ObservedV2和@Trace才能观察变化。

以下代码示例中，定义了ChildTwo为V2组件，组件接受message、undefinedVal、info等参数。ChildTwo中用@Param接收的简单类型message和undefinedVal，能观测到变化；Class类型变量info未被@ObservedV2和@Trace修饰，无法观测到类属性变化。

```
1. class InfoTwo {
2. public myId: number;
3. public name: string;

5. constructor(myId?: number, name?: string) {
6. this.myId = myId || 0;
7. this.name = name || 'aaa';
8. }
9. }

11. @ComponentV2
12. struct ChildTwo {
13. // V2对数据输入有严格的管理，从父组件传入数据时，必须使用@Param装饰器进行数据接收
14. @Param @Once message: string = 'hello'; // 可以观测到变化，同步回父组件依赖@Event，使用了@Once可以修改@Param装饰的变量
15. @Param @Once undefinedVal: string | undefined = undefined; // 使用了@Once可以修改@Param装饰的变量
16. @Param info: InfoTwo = new InfoTwo(); // 观测不到类属性变化
17. @Require @Param set: Set<number>;

19. build() {
20. Column() {
21. Text(`child message:${this.message}`) // 显示message变量
22. .fontSize(30)
23. .fontWeight(FontWeight.Bold)
24. .onClick(() => {
25. this.message = 'world'; // 刷新当前组件
26. })

28. Divider()
29. .color(Color.Blue)
30. Text(`undefinedVal:${this.undefinedVal}`) // 显示undefinedVal变量
31. .fontSize(30)
32. .fontWeight(FontWeight.Bold)
33. .onClick(() => {
34. this.undefinedVal = 'change to define'; // 刷新当前组件
35. })
36. Divider()
37. .color(Color.Blue)
38. Text(`info id:${this.info.myId}`) // 显示info.myId变量
39. .fontSize(30)
40. .fontWeight(FontWeight.Bold)
41. .onClick(() => {
42. this.info.myId++; // 不刷新
43. })
44. Divider()
45. .color(Color.Blue)
46. ForEach(Array.from(this.set.values()), (item: number) => { // 显示set变量
47. Text(`${item}`)
48. .fontSize(30)
49. })
50. }
51. .margin(5)
52. }
53. }

55. @Entry
56. @Component
57. struct IndexTwo {
58. message: string = 'Hello World'; // 简单数据
59. undefinedVal: undefined = undefined; // 简单类型，undefined
60. info: InfoTwo = new InfoTwo(); // Class类型
61. set: Set<number> = new Set([10, 20]); // 内置类型

63. build() {
64. Column() {
65. Text(`message:${this.message}`)
66. .fontSize(30)
67. .fontWeight(FontWeight.Bold)
68. .onClick(() => {
69. this.message = 'world hello';
70. })
71. Divider()
72. .color(Color.Blue)
73. ChildTwo({
74. message: this.message,
75. undefinedVal: this.undefinedVal,
76. info: this.info,
77. set: this.set
78. })
79. }
80. .height('100%')
81. .width('100%')
82. }
83. }
```

[V1CommonVariablesToV2CustomComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsMixingUse/entry/src/main/ets/pages/MixingUseofCustomComponents/V1CommonVariablesToV2CustomComponent.ets#L16-L100)

### 传递简单类型状态变量

在V1中使用V2组件时，V1组件中的装饰器仅支持修饰简单类型数据，包括：boolean、number、string、null、undefined。V2组件使用@Param接收参数。

若在V1中使用V2组件时，传递了使用@State装饰的Class类型或内置类型（Array、Map、Set、Date），会造成编译报错。以下示例代码中，info和set变量需删除@State装饰器。@Prop、@Link、@ObjectLink、@Provide、@Consume、@StorageProp、@StorageLink、@LocalStorageProp、@LocalStorageLink的行为和@State保持一致。

```
1. class InfoFour {
2. public myId: number;
3. public name: string;

5. constructor(myId?: number, name?: string) {
6. this.myId = myId || 0;
7. this.name = name || 'aaa';
8. }
9. }

11. @ComponentV2
12. struct ChildFour {
13. // V2对数据输入有严格的管理，从父组件传入数据时，必须使用@Param装饰器进行数据接收
14. @Param @Once message: string = 'hello';
15. @Param @Once undefinedVal: string | undefined = undefined; // 使用了@Once可以修改@Param装饰的变量
16. @Param info: InfoFour = new InfoFour();
17. @Require @Param set: Set<number>;

19. build() {
20. Column() {
21. Text(`child message:${this.message}`) // 显示message变量
22. .fontSize(30)
23. .fontWeight(FontWeight.Bold)
24. .onClick(() => {
25. this.message = 'world';
26. })
27. Divider()
28. .color(Color.Blue)
29. Text(`undefinedVal:${this.undefinedVal}`) // 显示undefinedVal变量
30. .fontSize(30)
31. .fontWeight(FontWeight.Bold)
32. .onClick(() => {
33. this.undefinedVal = 'change to define';
34. })
35. Divider()
36. .color(Color.Blue)
37. Text(`info id:${this.info.myId}`) // 显示info.myId变量
38. .fontSize(30)
39. .fontWeight(FontWeight.Bold)
40. .onClick(() => {
41. this.info.myId++;
42. })
43. Divider()
44. .color(Color.Blue)
45. ForEach(Array.from(this.set.values()), (item: number) => { // 显示set变量
46. Text(`${item}`)
47. .fontSize(30)
48. })
49. }
50. .margin(5)
51. }
52. }

54. @Entry
55. @Component
56. struct IndexFour {
57. @State message: string = 'Hello World'; // 简单类型数据，支持
58. @State undefinedVal: undefined = undefined; // 简单类型数据，undefined，支持
59. @State info: InfoFour = new InfoFour(); // Class类型，不支持传递，编译器报错；消除编译错误请去掉@State
60. @State set: Set<number> = new Set([10, 20]); // 内置类型，不支持传递，编译器报错；消除编译错误请去掉@State

62. build() {
63. Column() {
64. Text(`message:${this.message}`)
65. .fontSize(30)
66. .fontWeight(FontWeight.Bold)
67. .onClick(() => {
68. this.message = 'world hello';
69. })
70. Divider()
71. .color(Color.Blue)
72. ChildFour({
73. message: this.message,
74. undefinedVal: this.undefinedVal,
75. info: this.info,
76. set: this.set
77. })
78. }
79. .height('100%')
80. .width('100%')
81. }
82. }
```

[V1StateVariablesToV2CustomComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsMixingUse/entry/src/main/ets/pages/MixingUseofCustomComponents/V1StateVariablesToV2CustomComponent.ets#L16-L98)

### 传递class类型状态变量

由于在V1中使用V2组件传递参数，V1的装饰器仅支持修饰简单类型数据，不支持class类型。以下给出class类型数据传递的场景的迁移方案。

**@Observed装饰的class**

V2装饰器不能和@Observed一起使用，V1传递@Observed装饰的class类给V2自定义组件时，不直接用@Param接收数据，如下图所示先定义V1BridgeComponent组件作为桥接层。在桥接层监听V1组件的数据，同步到V2定义的单例数据。V1组件直接使用V1BridgeComponent，在V1BridgeComponent中引入V2自定义组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/6YgFmXEgToCiXXHlConnBg/zh-cn_image_0000002552957632.png?HW-CC-KV=V1&HW-CC-Date=20260427T233916Z&HW-CC-Expire=86400&HW-CC-Sign=C2CC98955012786C31E8B877313AA10C46B6A7E79AA6B72BDF693ADB275C06FD)

具体实现可参考以下示例代码：

1. 用@ObservedV2装饰class单例ViewModelV2，V2组件V2Comp直接使用单例ViewModelV2实例化进行UI渲染。
2. V1组件V1Comp和V2组件V2Comp之间新增@Component修饰的桥接组件V1BridgeComponent，用@Watch监听，将V1中@Observed修饰的class数据赋值给V2中@ObservedV2修饰的class数据。
3. V1组件V1Comp中直接引入桥接组件V1BridgeComponent，桥接组件V1BridgeComponent引入V2组件V2Comp。

```
1. @Observed
2. class ViewModelV1 {
3. @Track public fontSize: number;

5. constructor(fontSize: number) {
6. this.fontSize = fontSize;
7. }

9. updateFontSize(fontSize: number) {
10. this.fontSize = fontSize;
11. }
12. }

14. // 存量的V1组件
15. @Entry
16. @Component
17. struct V1Comp {
18. build() {
19. Column() {
20. // ------------ V1桥接组件 ------------
21. V1BridgeComponent()

23. // ....

25. }
26. }
27. }

29. // V1桥接组件
30. @Component
31. struct V1BridgeComponent {
32. @State @Watch('onDirectionChange') viewModel: ViewModelV1 = new ViewModelV1(20);

34. onDirectionChange() {
35. // 将V1的数据转成V2的数据
36. ViewModelV2.instance().fontSize = this.viewModel.fontSize;
37. }

39. build() {
40. Column() {
41. Text(`V1组件原始数据fontSize-${this.viewModel.fontSize}`)
42. .fontSize(this.viewModel.fontSize)

44. Button('V1组件修改字体大小').onClick(() => {
45. this.viewModel.updateFontSize(10); // V1 V2组件刷新
46. })

48. // ------------ V2业务组件 ------------
49. V2Comp()
50. }
51. }
52. }

54. @ObservedV2
55. class ViewModelV2 {
56. // 单例实例
57. private static singleton_: ViewModelV2;
58. @Trace public fontSize: number = 40;

60. // 私有构造函数（禁止外部new）
61. private constructor() {
62. }

64. static instance(): ViewModelV2 {
65. if (!ViewModelV2.singleton_) {
66. ViewModelV2.singleton_ = new ViewModelV2();
67. }
68. return ViewModelV2.singleton_;
69. }
70. }

72. // 新增V2业务组件
73. @ComponentV2
74. struct V2Comp {
75. // 获取V2单例实例（组件内可直接访问）
76. private v2Model = ViewModelV2.instance();

78. build() {
79. Column() {
80. Text(`V2组件fontSize-${this.v2Model.fontSize}`)
81. .fontSize(this.v2Model.fontSize)

83. Button('V2组件修改字体大小')
84. .onClick(() => {
85. this.v2Model.fontSize = 60; // V2组件刷新
86. })
87. }
88. }
89. }
```

**@ObservedV2装饰的class**

@ObservedV2+@Trace的观测能力在V1和V2版本中均受支持，但在V1中不支持将V1装饰器与@ObservedV2装饰的实例对象共同使用。以下示例代码中，若info对象被@State修饰，则会导致编译错误，需移除V1的装饰器。

```
1. @ObservedV2
2. class InfoTen {
3. @Trace public myId: number;
4. public name: string;

6. constructor(myId?: number, name?: string) {
7. this.myId = myId || 0;
8. this.name = name || 'aaa';
9. }
10. }

12. @ComponentV2
13. struct ChildTen {
14. // V2对数据输入有严格的管理，从父组件传入数据时，必须使用@Param装饰器进行数据接收
15. @Param info: InfoTen = new InfoTen();

17. build() {
18. Column() {
19. Text(`Child-V2 info id:${this.info.myId}`)
20. .fontSize(30)
21. .fontWeight(FontWeight.Bold)
22. .onClick(() => {
23. this.info.myId++; // 刷新
24. })
25. }
26. }
27. }

29. @Entry
30. @Component
31. struct IndexTen {
32. // @State info: InfoTen = new InfoTen(); // 错误写法。Class类型，不支持传递，编译器报错；消除编译错误请去掉@State
33. info: InfoTen = new InfoTen(); // 正确写法

35. build() {
36. Column() {
37. Text(`Parent-V1 info id:${this.info.myId}`)
38. .fontSize(30)
39. .fontWeight(FontWeight.Bold)
40. .onClick(() => {
41. this.info.myId++; // 刷新
42. })

44. ChildTen({
45. info: this.info,
46. })
47. }
48. .height('100%')
49. .width('100%')
50. }
51. }
```

### 传递嵌套对象

V1装饰器的观测能力是对数据本身做代理，因此当数据存在嵌套时，V1只能通过@Observed+@ObjectLink的方式拆分子组件，观测深层次数据。但V2无法接收@Observed装饰的对象，@ObjectLink也无法在V2中使用。@Observed并没有@ObservedV2+@Trace那样强大的深层次观测能力，这里不再对@Observed的深层次嵌套进行讨论，只讨论@ObservedV2在V1的使用场景。

**@Observed装饰的class嵌套@ObservedV2装饰的class**

@ObservedV2和@Observed嵌套使用时，类对象能否被V1的装饰器装饰取决于最外层class使用的装饰器。如果最外层是@Observed修饰的类，可以和V2装饰器一起使用，比如@State。@State仅能观察第一层的变化，如果要深度观察，需要传递给@ObjectLink。

以下示例代码中：

* 最外层MessageInfoNested1类被@Observed修饰，在V1组件IndexOne中可以被@State修饰。数据源@State的第二层的改变（info和messageId属性），虽不能触发本层的刷新，但会被@ObjectLink和@Param观察到，并触发它们关联组件的刷新。
* messageInfo属性传递给V1组件，V1组件ChildOne要用@ObjectLink接收，而传递给V2组件GrandSon1的info属性的class类用@ObservedV2修饰。
* @Track防止MessageInfo1类中的info因messageId改变而连带刷新，开发者去掉@Track可观测到，当messageId改变时，info的连带刷新，但这并非@ObjectLink的观测能力。

```
1. @ObservedV2
2. class InfoOne {
3. @Trace public myId: number;
4. public name: string;

6. constructor(myId?: number, name?: string) {
7. this.myId = myId || 0;
8. this.name = name || 'aaa';
9. }
10. }

12. @Observed
13. class MessageInfo1 { // 一层嵌套
14. @Track public info: InfoOne; // 防止messageId改变导致info的连带刷新
15. @Track public messageId: number; // 防止messageId改变导致info的连带刷新

17. constructor(info?: InfoOne, messageId?: number) {
18. this.info = info || new InfoOne();
19. this.messageId = messageId || 0;
20. }
21. }

23. @Observed
24. class MessageInfoNested1 { // 二层嵌套
25. public messageInfo: MessageInfo1;

27. constructor(messageInfo?: MessageInfo1) {
28. this.messageInfo = messageInfo || new MessageInfo1();
29. }
30. }

32. @ComponentV2
33. struct GrandSon1 {
34. @Param info: InfoOne = new InfoOne();

36. build() {
37. Column() {
38. Text(`ObjectLink info info.myId:${this.info.myId}`) // myId属性被@Trace装饰，可以观测变化
39. .fontSize(30)
40. .onClick(() => {
41. this.info.myId++; // 当前组件和父组件ChildOne都刷新
42. })
43. }
44. }
45. }

47. @Component
48. struct ChildOne {
49. @ObjectLink messageInfo: MessageInfo1;

51. build() {
52. Column() {
53. Text(`ObjectLink MessageInfo messageId:${this.messageInfo.messageId}`) // 经过@ObjectLink拆解之后，可以观测一层类属性变化
54. .fontSize(30)
55. .onClick(() => {
56. this.messageInfo.messageId++; // 当前组件UI刷新
57. })
58. Divider()
59. .color(Color.Blue)
60. Text(`ObjectLink MessageInfo info.myId:${this.messageInfo.info.myId}`) // myId属性被@Trace装饰，可以观测变化
61. .fontSize(30)
62. .onClick(() => {
63. this.messageInfo.info.myId++; // 当前组件和GrandSon1子组件的UI都刷新
64. })
65. GrandSon1({ info: this.messageInfo.info }); // 继续拆解一层子组件
66. }
67. }
68. }

70. @Entry
71. @Component
72. struct IndexOne {
73. @State messageInfoNested: MessageInfoNested1 = new MessageInfoNested1(); // 三层嵌套的数据，如何观测内部。

75. build() {
76. Column() {
77. // 观察messageInfoNested，@State只有一层观测能力，无法观察到变化
78. Text(`messageInfoNested messageId:${this.messageInfoNested.messageInfo.messageId}`)
79. .fontSize(30)
80. .onClick(() => {
81. this.messageInfoNested.messageInfo.messageId++; // 当前组件不刷新，子组件ChildOne的UI刷新
82. })
83. Divider()
84. .color(Color.Blue)
85. // 通过@ObjectLink嵌套观察 messageInfoId
86. ChildOne({ messageInfo: this.messageInfoNested.messageInfo }) // 经过拆分后，使用@ObjectLink拆分可以观察到深一层的变化
87. Divider()
88. .color(Color.Blue)
89. }
90. .height('100%')
91. .width('100%')
92. .margin(10)
93. }
94. }
```

**@ObservedV2+@Trace观察class嵌套类**

@ObservedV2+@Trace将观测能力实现在类属性上，所以当类属性被@Trace标记时，无论嵌套多少层，均能观测到变化。以下示例代码中，MessageInfoNested对象及其属性均被@ObservedV2修饰，在V1组件Index中使用时，不能和V1装饰器一起使用。将messageInfo属性从V1组件传递给V2组件，V2组件Child通过@Param接收，且修改能被观测。

```
1. @ObservedV2
2. class Info {
3. @Trace public myId: number;
4. public name: string;

6. constructor(myId?: number, name?: string) {
7. this.myId = myId || 0;
8. this.name = name || 'aaa';
9. }
10. }

12. @ObservedV2
13. class MessageInfo { // 一层嵌套
14. @Trace public info: Info; // 防止messageId改变导致info的连带刷新
15. @Trace public messageId: number; // 防止info改变导致messageId的连带刷新

17. constructor(info?: Info, messageId?: number) {
18. this.info = info || new Info(); // 使用传入的info或创建一个新的Info
19. this.messageId = messageId || 0;
20. }
21. }

23. @ObservedV2
24. class MessageInfoNested { // 二层嵌套，MessageInfoNested如果是被@ObservedV2装饰，则不可以被V1的状态变量更新相关的装饰器装饰，如@State
25. public messageInfo: MessageInfo;

27. constructor(messageInfo?: MessageInfo) {
28. this.messageInfo = messageInfo || new MessageInfo();
29. }
30. }

32. @ComponentV2
33. struct Child {
34. @Param messageInfo: MessageInfo =  new MessageInfo();

36. build() {
37. Column() {
38. Text(`Child MessageInfo messageId:${this.messageInfo.messageId}`)
39. .fontSize(30)
40. .onClick(() => {
41. this.messageInfo.messageId++; // 刷新
42. })
43. }
44. }
45. }

47. @Entry
48. @Component
49. struct Index {
50. messageInfoNested: MessageInfoNested = new MessageInfoNested(); // 三层嵌套的数据，如何观测内部。

52. build() {
53. Column() {
54. Text(`messageInfoNested messageId:${this.messageInfoNested.messageInfo.messageId}`)
55. .fontSize(30)
56. .onClick(() => {
57. this.messageInfoNested.messageInfo.messageId++;
58. })
59. Divider()
60. .color(Color.Blue)
61. Text(`messageInfoNested name:${this.messageInfoNested.messageInfo.info.name}`) // 未被@Trace修饰，无法观测
62. .fontSize(30)
63. .onClick(() => {
64. this.messageInfoNested.messageInfo.info.name += 'a';
65. })
66. Divider()
67. .color(Color.Blue)
68. Text(`messageInfoNested myId:${this.messageInfoNested.messageInfo.info.myId}`) // 被@Trace修饰，无论嵌套多少层都能观测
69. .fontSize(30)
70. .onClick(() => {
71. this.messageInfoNested.messageInfo.info.myId++;
72. })
73. Divider()
74. .color(Color.Blue)
75. // 通过@ObservedV2和@Trace观察messageInfo
76. Child({messageInfo: this.messageInfoNested.messageInfo})
77. }
78. .height('100%')
79. .width('100%')
80. .margin(10)
81. }
82. }
```

## V2组件使用V1组件

V2的状态变量传递给V1的自定义组件，存在以下限制：

* V1可以不使用装饰器接收数据。V1自定义组件中，不使用装饰器接收的变量被视为普通变量。
* V1使用装饰器接收数据时，仅可通过@State、@Prop、@Provide接收。
* V1使用装饰器接收数据时，不支持内置类型的数据，否则编译报错。

### 传递简单类型状态变量

V2向V1自定义组件传递简单类型状态变量时，V1仅能通过@State、@Prop、@Provide装饰器接收数据。以下示例代码中，ThirdPartyComp组件模拟第三方库，接收来自V2组件的布尔值。

```
1. // 模拟三方库导入的V1组件
2. @Component
3. struct ThirdPartyComp {
4. // V1从V2接收的状态变量，仅可使用@State、@Prop、@Provide接收
5. @State prop: boolean = true; // 可以观测到变化

7. build() {
8. Column() {
9. Text(`ThirdPartyComp：${this.prop}`)
10. }
11. }
12. }

14. @Entry
15. @ComponentV2
16. struct V2Comp2 {
17. @Local param: boolean = false;

19. build() {
20. Column() {
21. Text(`V2Comp2：${this.param}`)

23. // V2组件向V1的三方库传递简单状态变量
24. ThirdPartyComp({ prop: this.param })
25. }
26. }
27. }
```

### 传递class类型

**定义普通class**

V2向V1自定义组件传递数据时，支持普通class类。在以下示例代码中，InfoFive类未被@ObservedV2修饰，传递给V1组件ChildFive时，可以使用@State接收。修改V1组件中的info变量，依赖@State的观测能力刷新UI。

```
1. class InfoFive {
2. public myId: number;
3. public name: string;

5. constructor(myId?: number, name?: string) {
6. this.myId = myId || 0;
7. this.name = name || 'aaa';
8. }
9. }

11. @Component
12. struct ChildFive {
13. // V1从V2接收的状态变量，仅可使用@State、@Prop、@Provide接收
14. @State info: InfoFive = new InfoFive(); // 可以观测一层类属性变化

16. build() {
17. Column() {
18. Text(`info id:${this.info.myId}`)
19. .fontSize(30)
20. .fontWeight(FontWeight.Bold)
21. .onClick(() => {
22. this.info.myId++; // 当前组件UI刷新
23. })
24. }
25. }
26. }

28. @Entry
29. @ComponentV2
30. struct IndexFive {
31. @Provider() info: InfoFive = new InfoFive(); // Class类型，支持传递

33. build() {
34. Column() {
35. ChildFive({
36. info: this.info,
37. })
38. }
39. .height('100%')
40. .width('100%')
41. }
42. }
```

[V2CommonVariablesToV1CustomComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/CustomComponentsMixingUse/entry/src/main/ets/pages/MixingUseofCustomComponents/V2CommonVariablesToV1CustomComponent.ets#L16-L98)

**定义@ObserveV2修饰的class**

V1装饰器不能和@ObservedV2一起使用。在以下示例代码中，InfoNine类被@observedV2装饰，V1组件接收变量时，info变量不能被V1装饰器修饰，但通过修改可以刷新UI，依赖的是@ObservedV2+@Trace的观测能力。

```
1. @ObservedV2
2. class InfoNine {
3. @Trace public myId: number;
4. public name: string;

6. constructor(myId?: number, name?: string) {
7. this.myId = myId || 0;
8. this.name = name || 'aaa';
9. }
10. }

12. @Component
13. struct ChildNine {
14. info: InfoNine = new InfoNine(); // V1装饰器不能和@ObservedV2一起使用

16. build() {
17. Column() {
18. Text(`info id:${this.info.myId}`) // 显示info.myId变量
19. .fontSize(30)
20. .fontWeight(FontWeight.Bold)
21. .onClick(() => {
22. this.info.myId++; // 当前组件UI刷新,依赖@ObservedV2+@Trace的能力
23. })
24. }
25. }
26. }

28. @Entry
29. @ComponentV2
30. struct IndexNine {
31. @Provider() info: InfoNine = new InfoNine();

33. build() {
34. Column() {
35. ChildNine({
36. info: this.info,
37. })
38. }
39. .height('100%')
40. .width('100%')
41. }
42. }
```

### 传递普通内置类型

V2->V1传递内置类型，V2定义内置类型的装饰器和V1接收内置类型的装饰器是互斥的。

* V1使用装饰器接收数据时，内置类型不支持在V2中用装饰器修饰。
* V1可以不使用装饰器接收数据，接收过来的变量在V1定义组件内也会是普通变量，在V2中可以用装饰器修饰。

在以下示例代码中，V2向V1自定义组件传递set变量，V1组件使用@Provide接收。因此，在V2组件IndexEight中定义set变量时，为避免编译错误，set变量不能用@Local修饰。

```
1. @Component
2. struct ChildEight {
3. // V1从V2接收的状态变量，仅可使用@State、@Prop、@Provide接收
4. @Provide set: Set<number> = new Set();

6. build() {
7. Column() {
8. ForEach(Array.from(this.set.values()), (item: number) => { // 显示set变量
9. Text(`${item}`)
10. .fontSize(30)
11. })
12. }
13. }
14. }

16. @Entry
17. @ComponentV2
18. struct IndexEight {
19. // @Local set: Set<number> = new Set([10, 20]); // 错误写法。内置类型状态变量，不支持传递；消除编译错误请去掉@Local
20. set: Set<number> = new Set([10, 20]); // 正确写法。

22. build() {
23. Column() {
24. ChildEight({
25. set: this.set
26. })
27. }
28. .height('100%')
29. .width('100%')
30. }
31. }
```

## 混用场景总结

对V1和V2混用场景进行梳理后，可以总结出：

* 当V1中混用V2自定义组件时（即V1的组件或者类数据向V2传递），大部分V1的能力在V2都是被禁止的。
* 当V2中混用V1自定义组件时（即V2的组件或者类数据向V1传递），做了部分功能开放。例如：@ObservedV2和@Trace，这也是对V1嵌套类数据的观测能提供的最大的帮助。

所以在代码开发过程中，不建议开发者混用V1和V2版本。然而，在代码迁移方面，V1的开发者可以逐步将代码迁移到V2，以稳步替换V1的功能代码。同时，不建议在V2的代码架构中混用V1的代码。
