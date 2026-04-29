---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-mvvm
title: MVVM模式（V1）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > MVVM模式（V1）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:10+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f514e5db0f93fca7a602c65d352a00ebc283cb2fcf625a246a62f780018cf972
---

当开发者掌握了状态管理的基本概念后，通常会尝试开发自己的应用，在应用开发初期，如果未能精心规划项目结构，随着项目扩展和复杂化，状态变量的增多将导致组件间关系变得错综复杂。此时，开发新功能可能引起连锁反应，维护成本也会增加。为此，本文旨在介绍MVVM模式以及ArkUI的UI开发模式与MVVM的关系，指导开发者如何设计项目结构，以便在产品迭代和升级时能更轻松地开发和维护。

本文档涵盖了大多数状态管理V1装饰器，所以在阅读本文档前，建议开发者对状态管理V1有一定的了解。建议提前阅读：[状态管理概述](arkts-state-management-overview.md)和状态管理V1装饰器相关文档。

## MVVM模式介绍

### 概念

在应用开发中，UI更新需要实时同步数据状态变化，这直接影响应用程序的性能和用户体验。为了解决数据与UI同步的复杂性，ArkUI采用了 Model-View-ViewModel（MVVM）架构模式。MVVM 将应用分为Model、View和ViewModel三个核心部分，实现数据、视图与逻辑的分离。通过这种模式，UI可以自动更新状态变化，从而更高效地管理数据和视图的绑定与更新。

* View：用户界面层。负责用户界面展示并与用户交互，不包含任何业务逻辑。它通过绑定ViewModel层提供的数据实现动态更新。
* Model：数据访问层。以数据为中心，不直接与用户界面交互。负责数据结构定义，数据管理（获取、存储、更新等），以及业务逻辑处理。
* ViewModel：表示逻辑层。作为连接Model和View的桥梁，通常一个View对应一个ViewModel。View和ViewModel有两种通信方式：

  1. 方法调用：View通过事件监听用户行为，在回调里面触发ViewModel层的方法。例如当View监听到用户Button点击行为，调用ViewModel对应的方法，处理用户操作。
  2. 双向绑定：View绑定ViewModel的数据，实现双向同步。

ArkUI的UI开发模式就属于MVVM模式，通过对MVVM概念的基本介绍，开发者大致能猜到状态管理能在MVVM中起什么样的作用，状态管理旨在数据驱动更新，让开发者只用关注页面设计，而不去关注整个UI的刷新逻辑，数据的维护也无需开发者进行感知，由状态变量自动更新完成，而这就是属于ViewModel层所需要支持的内容，因此开发者使用MVVM模式开发自己的应用是最省心省力的。

### ArkUI开发模式图

ArkUI的UI开发模式即是MVVM模式，而状态变量在MVVM模式中扮演着ViewModel的角色，向上刷新UI，向下更新数据，整体框架如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/zEorDJXuT-yJNn2LOf5BmA/zh-cn_image_0000002558604426.png?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=B97C4AD18250068265568FDD0D52036858D55B103BFD9347B4BC668FC92CBA69)

### 分层说明

**View层**

View层通常可以分为下列组件：

* 页面组件：所有应用基本都是按照页面进行分类的，比如登录页，列表页，编辑页，帮助页，版权页等。每个页面对应需要的数据可能是完全不一样的，也可能多个页面需要的数据是同一套。
* 业务组件：本身具备本APP部分业务能力的功能组件，典型的就是这个业务组件可能关联了本项目的ViewModel中的数据，不可以被共享给其他项目使用。
* 通用组件：像系统组件一样，这类组件不会关联本APP中ViewModel的数据，这些组件可实现跨越多个项目进行共享，来完成比较通用的功能。

**Model层**

Model层是应用的原始数据提供者，代表应用的核心业务逻辑和数据。

**ViewModel层**

为View层的组件提供对应数据，按照页面组织，当用户浏览页面时，某些页面可能不会被显示，因此，页面数据最好设计成懒加载（按需加载）的模式。

ViewModel层数据和Model层数据的区别：

Model层数据是按照整个工程、项目来组织数据，构成一套完整的APP业务数据体系。

ViewModel层数据，是提供某个页面上使用的数据，它可能是整个APP的业务数据的一部分。另外ViewModel层还可以附加对应Page的辅助页面显示数据，这部分数据可能与本APP的业务完全无关，仅仅是为页面展示提供便利的辅助数据。

### 架构核心原则

**不可跨层访问**

* View层不可以直接调用Model层的数据，只能通过ViewModel提供的方法进行调用。
* Model层不能直接操作UI，只能通知ViewModel层数据有更新，由ViewModel层更新对应的数据。

**下层不可访问上层数据**

下层数据通过通知模式更新上层数据。在业务逻辑中，下层不可直接获取上层数据。例如，ViewModel层的逻辑处理不应该依赖View层界面上的某个值。

**非父子组件间不可直接访问**

这是针对View层设计的核心原则，一个组件应该具备以下逻辑：

* 禁止直接访问父组件（必须使用事件或是订阅能力）。
* 禁止直接访问兄弟组件。这是因为组件应该仅能访问自己的子节点（通过传参）和父节点（通过事件或通知），以此完成组件之间的解耦。

对于一个组件，这样设计的原因如下：

* 组件自己使用了哪些子组件是明确的，因此可以访问。
* 组件被放置于哪个父节点下是未知的，因此组件想访问父节点，就只能通过通知或者事件能力完成。
* 组件不可能知道自己的兄弟节点是谁，因此组件不可以操作兄弟节点。

## 备忘录开发实战

本节通过备忘录应用的开发，使开发者了解如何使用ArkUI框架设计自己的应用。本节直接进行功能开发，未设计代码架构，即根据需求即时开发，不考虑后续维护，同时，本节还将介绍功能开发所需的装饰器。

### @State状态变量

* [@State](arkts-state.md)装饰器是最常用的装饰器之一，用于定义状态变量。通常，这些状态变量作为父组件的数据源，开发者点击时，触发状态变量的更新，刷新UI。

```
1. @Entry
2. @Component
3. struct StateIndex {
4. @State isFinished: boolean = false;

6. build() {
7. Column() {
8. Row() {
9. // 请将$r('app.string.all_tasks')替换为实际资源文件，在本示例中该资源文件的value值为"全部待办"
10. Text($r('app.string.all_tasks'))
11. .fontSize(30)
12. .fontWeight(FontWeight.Bold)
13. }
14. .width('100%')
15. .margin({ top: 10, bottom: 10 })

17. // 待办事项
18. Row({ space: 15 }) {
19. if (this.isFinished) {
20. // 请将$r('app.media.finished')替换为实际资源文件
21. Image($r('app.media.finished'))
22. .width(28)
23. .height(28)
24. } else {
25. // 请将$r('app.media.unfinished')替换为实际资源文件
26. Image($r('app.media.unfinished'))
27. .width(28)
28. .height(28)
29. }
30. // 请将$r('app.string.all_learn_advanced_math')替换为实际资源文件，在本示例中该资源文件的value值为"学习高数"
31. Text($r('app.string.learn_advanced_math'))
32. .fontSize(24)
33. .decoration({ type: this.isFinished ? TextDecorationType.LineThrough : TextDecorationType.None })
34. }
35. .height('40%')
36. .width('100%')
37. .border({ width: 5 })
38. .padding({ left: 15 })
39. .onClick(() => {
40. this.isFinished = !this.isFinished;
41. })
42. }
43. .height('100%')
44. .width('100%')
45. .margin({ top: 5, bottom: 5 })
46. .backgroundColor('#90f1f3f5')
47. }
48. }
```

[StateIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/pages/StateIndex.ets#L16-L66)

效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/6pQRW6CeSzO7Cd94pxjoTg/zh-cn_image_0000002589323951.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=93ACF1BC3F5286FCC3C8C6A8217DB48735A245C82604E8B58F0E178FD45EEA3A)

### @Prop、@Link的作用

上述示例中，所有代码都写在了@Entry组件中。随着需要渲染的组件越来越多，@Entry组件必然需要进行拆分，为此，拆分出的子组件就需要使用@Prop和@Link装饰器：

* [@Prop](arkts-prop.md)是父子间单向传递，子组件会深拷贝父组件数据，可从父组件更新，也可自己更新数据，但不会同步回父组件。
* [@Link](arkts-link.md)是父子间双向传递，父组件改变，会通知所有的@Link，同时@Link的更新也会通知父组件的数据源进行刷新。

```
1. @Component
2. struct PropLinkTodoComponent {
3. build() {
4. Row() {
5. // 请将$r('app.string.all_tasks')替换为实际资源文件，在本示例中该资源文件的value值为"全部待办"
6. Text($r('app.string.all_tasks'))
7. .fontSize(30)
8. .fontWeight(FontWeight.Bold)
9. }
10. .width('100%')
11. .margin({ top: 10, bottom: 10 })
12. }
13. }

15. @Component
16. struct PropLinkAllChooseComponent {
17. @Link isFinished: boolean;

19. build() {
20. Row() {
21. // 请将$r('app.string.check_all')替换为实际资源文件，在本示例中该资源文件的value值为"全选"
22. Button($r('app.string.check_all'), { type: ButtonType.Normal })
23. .onClick(() => {
24. this.isFinished = !this.isFinished;
25. })
26. .fontSize(30)
27. .fontWeight(FontWeight.Bold)
28. .backgroundColor('#f7f6cc74')
29. }
30. .padding({ left: 15 })
31. .width('100%')
32. .margin({ top: 10, bottom: 10 })
33. }
34. }

36. @Component
37. struct ThingComponent1 {
38. @Prop isFinished: boolean;

40. build() {
41. // 待办事项1
42. Row({ space: 15 }) {
43. if (this.isFinished) {
44. // 请将$r('app.media.finished')替换为实际资源文件
45. Image($r('app.media.finished'))
46. .width(28)
47. .height(28)
48. } else {
49. // 请将$r('app.media.unfinished')替换为实际资源文件
50. Image($r('app.media.unfinished'))
51. .width(28)
52. .height(28)
53. }
54. // 请将$r('app.string.learn_chinese')替换为实际资源文件，在本示例中该资源文件的value值为"学习语文"
55. Text($r('app.string.learn_chinese'))
56. .fontSize(24)
57. .decoration({ type: this.isFinished ? TextDecorationType.LineThrough : TextDecorationType.None })
58. }
59. .height('40%')
60. .width('100%')
61. .border({ width: 5 })
62. .padding({ left: 15 })
63. .onClick(() => {
64. this.isFinished = !this.isFinished;
65. })
66. }
67. }

69. @Component
70. struct ThingComponent2 {
71. @Prop isFinished: boolean;

73. build() {
74. // 待办事项1
75. Row({ space: 15 }) {
76. if (this.isFinished) {
77. // 请将$r('app.media.finished')替换为实际资源文件
78. Image($r('app.media.finished'))
79. .width(28)
80. .height(28)
81. } else {
82. // 请将$r('app.media.unfinished')替换为实际资源文件
83. Image($r('app.media.unfinished'))
84. .width(28)
85. .height(28)
86. }
87. // 请将$r('app.string.learn_advanced_math')替换为实际资源文件，在本示例中该资源文件的value值为"学习高数"
88. Text($r('app.string.learn_advanced_math'))
89. .fontSize(24)
90. .decoration({ type: this.isFinished ? TextDecorationType.LineThrough : TextDecorationType.None })
91. }
92. .height('40%')
93. .width('100%')
94. .border({ width: 5 })
95. .padding({ left: 15 })
96. .onClick(() => {
97. this.isFinished = !this.isFinished;
98. })
99. }
100. }

102. @Entry
103. @Component
104. struct PropLinkIndex {
105. @State isFinished: boolean = false;

107. build() {
108. Column() {
109. // 全部待办
110. PropLinkTodoComponent()

112. // 全选
113. PropLinkAllChooseComponent({ isFinished: this.isFinished })

115. // 待办事项1
116. ThingComponent1({ isFinished: this.isFinished })

118. // 待办事项2
119. ThingComponent2({ isFinished: this.isFinished })
120. }
121. .height('100%')
122. .width('100%')
123. .margin({ top: 5, bottom: 5 })
124. .backgroundColor('#90f1f3f5')
125. }
126. }
```

[PropLinkIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/pages/PropLinkIndex.ets#L16-L144)

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/dQURmpgPQlCqa7y5l0FebA/zh-cn_image_0000002589243891.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=6BF52CABC0C639B6E82023CBAF2CB9BAD1B61C4FB21264B02643AFD6636B8D00)

### 循环渲染组件

* 上个示例虽然拆分出了子组件，但发现组件1和组件2的代码非常相似，当渲染的组件除了数据外，其他设置都相同时，此时就需要使用[ForEach循环渲染](../harmonyos-references/ts-rendering-control-foreach.md)。
* ForEach使用之后，冗余代码变得更少，并且代码结构更加清晰。

```
1. @Component
2. struct ForEachTodoComponent {
3. build() {
4. Row() {
5. // 请将$r('app.string.all_tasks')替换为实际资源文件，在本示例中该资源文件的value值为"全部待办"
6. Text($r('app.string.all_tasks'))
7. .fontSize(30)
8. .fontWeight(FontWeight.Bold)
9. }
10. .width('100%')
11. .margin({ top: 10, bottom: 10 })
12. }
13. }

15. @Component
16. struct ForEachAllChooseComponent {
17. @Link isFinished: boolean;

19. build() {
20. Row() {
21. // 请将$r('app.string.check_all')替换为实际资源文件，在本示例中该资源文件的value值为"全选"
22. Button($r('app.string.check_all'), { type: ButtonType.Normal })
23. .onClick(() => {
24. this.isFinished = !this.isFinished;
25. })
26. .fontSize(30)
27. .fontWeight(FontWeight.Bold)
28. .backgroundColor('#f7f6cc74')
29. }
30. .padding({ left: 15 })
31. .width('100%')
32. .margin({ top: 10, bottom: 10 })
33. }
34. }

36. @Component
37. struct ForEachThingComponent {
38. @Prop isFinished: boolean;
39. @Prop thing: string;

41. build() {
42. // 待办事项1
43. Row({ space: 15 }) {
44. if (this.isFinished) {
45. // 请将$r('app.media.finished')替换为实际资源文件
46. Image($r('app.media.finished'))
47. .width(28)
48. .height(28)
49. } else {
50. // 请将$r('app.media.unfinished')替换为实际资源文件
51. Image($r('app.media.unfinished'))
52. .width(28)
53. .height(28)
54. // ...
55. }
56. Text(`${this.thing}`)
57. .fontSize(24)
58. .decoration({ type: this.isFinished ? TextDecorationType.LineThrough : TextDecorationType.None })
59. }
60. .height('8%')
61. .width('90%')
62. .padding({ left: 15 })
63. .opacity(this.isFinished ? 0.3 : 1)
64. .border({ width: 1 })
65. .borderColor(Color.White)
66. .borderRadius(25)
67. .backgroundColor(Color.White)
68. .onClick(() => {
69. this.isFinished = !this.isFinished;
70. })
71. }
72. }

74. @Entry
75. @Component
76. struct ForEachIndex {
77. @State isFinished: boolean = false;
78. @State planList: ResourceStr[] = [
79. // 请将$r('app.string.get_up')替换为实际资源文件，在本示例中该资源文件的value值为"7.30 起床"
80. $r('app.string.get_up'),
81. // 请将$r('app.string.breakfast')替换为实际资源文件，在本示例中该资源文件的value值为"8.30 早餐"
82. $r('app.string.breakfast'),
83. // 请将$r('app.string.lunch')替换为实际资源文件，在本示例中该资源文件的value值为"11.30 中餐"
84. $r('app.string.lunch'),
85. // 请将$r('app.string.dinner')替换为实际资源文件，在本示例中该资源文件的value值为"17.30 晚餐"
86. $r('app.string.dinner'),
87. // 请将$r('app.string.midnight_snack')替换为实际资源文件，在本示例中该资源文件的value值为"21.30 夜宵"
88. $r('app.string.midnight_snack'),
89. // 请将$r('app.string.bathe')替换为实际资源文件，在本示例中该资源文件的value值为"22.30 洗澡"
90. $r('app.string.bathe'),
91. // 请将$r('app.string.sleep')替换为实际资源文件，在本示例中该资源文件的value值为"1.30 睡觉"
92. $r('app.string.sleep')
93. ];
94. context1 = this.getUIContext().getHostContext();

96. aboutToAppear(): void {
97. for (let i = 0; i < this.planList.length; i++) {
98. this.planList[i] = resource.resourceToString(this.planList[i] as Resource);
99. };
100. }

102. build() {
103. Column() {
104. // 全部待办
105. ForEachTodoComponent()

107. // 全选
108. ForEachAllChooseComponent({ isFinished: this.isFinished })

110. List() {
111. ForEach(this.planList, (item: string) => {
112. // 待办事项1
113. ForEachThingComponent({ isFinished: this.isFinished, thing: item })
114. .margin(5)
115. })
116. }
117. }
118. .height('100%')
119. .width('100%')
120. .margin({ top: 5, bottom: 5 })
121. .backgroundColor('#90f1f3f5')
122. }
123. }
```

[ForEachIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/pages/ForEachIndex.ets#L16-L143)

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/UViOtEBkQD2kUByFU26gAQ/zh-cn_image_0000002558764084.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=58C3ECFD13E99AB34BD7DEC8876DBDCE2769CE5F284F90AD197B56A83BD5DB75)

### @Builder方法

* Builder方法用于组件内定义方法，可以使得相同代码可以在组件内进行复用。
* 本示例不仅使用了[@Builder](arkts-builder.md)方法进行去重，还对数据进行了移除，可以看到此时代码更加清晰易读，相对于最开始的代码，@Entry组件基本只用于处理页面构建逻辑，而不处理大量与页面设计无关的内容。

```
1. @Observed
2. class TodoListData {
3. public planList: ResourceStr[] = [
4. // 请将$r('app.string.get_up')替换为实际资源文件，在本示例中该资源文件的value值为"7.30 起床"
5. $r('app.string.get_up'),
6. // 请将$r('app.string.breakfast')替换为实际资源文件，在本示例中该资源文件的value值为"8.30 早餐"
7. $r('app.string.breakfast'),
8. // 请将$r('app.string.lunch')替换为实际资源文件，在本示例中该资源文件的value值为"11.30 中餐"
9. $r('app.string.lunch'),
10. // 请将$r('app.string.dinner')替换为实际资源文件，在本示例中该资源文件的value值为"17.30 晚餐"
11. $r('app.string.dinner'),
12. // 请将$r('app.string.midnight_snack')替换为实际资源文件，在本示例中该资源文件的value值为"21.30 夜宵"
13. $r('app.string.midnight_snack'),
14. // 请将$r('app.string.bathe')替换为实际资源文件，在本示例中该资源文件的value值为"22.30 洗澡"
15. $r('app.string.bathe'),
16. // 请将$r('app.string.sleep')替换为实际资源文件，在本示例中该资源文件的value值为"1.30 睡觉"
17. $r('app.string.sleep')
18. ];
19. }

21. @Component
22. struct StateTodoComponent {
23. build() {
24. Row() {
25. // 请将$r('app.string.all_tasks')替换为实际资源文件，在本示例中该资源文件的value值为"全部待办"
26. Text($r('app.string.all_tasks'))
27. .fontSize(30)
28. .fontWeight(FontWeight.Bold)
29. }
30. .width('100%')
31. .margin({ top: 10, bottom: 10 })
32. }
33. }

35. @Component
36. struct BuilderAllChooseComponent {
37. @Link isFinished: boolean;

39. build() {
40. Row() {
41. // 请将$r('app.string.check_all')替换为实际资源文件，在本示例中该资源文件的value值为"全选"
42. Button($r('app.string.check_all'), { type: ButtonType.Capsule })
43. .onClick(() => {
44. this.isFinished = !this.isFinished;
45. })
46. .fontSize(30)
47. .fontWeight(FontWeight.Bold)
48. .backgroundColor('#f7f6cc74')
49. }
50. .padding({ left: 15 })
51. .width('100%')
52. .margin({ top: 10, bottom: 10 })
53. }
54. }

56. @Component
57. struct BuilderThingComponent {
58. @Prop isFinished: boolean;
59. @Prop thing: string;

61. @Builder
62. displayIcon(icon: Resource) {
63. Image(icon)
64. .width(28)
65. .height(28)
66. .onClick(() => {
67. this.isFinished = !this.isFinished;
68. })
69. // ...
70. }

72. build() {
73. // 待办事项1
74. Row({ space: 15 }) {
75. if (this.isFinished) {
76. // 请将$r('app.media.finished')替换为实际资源文件
77. this.displayIcon($r('app.media.finished'));
78. } else {
79. // 请将$r('app.media.unfinished')替换为实际资源文件
80. this.displayIcon($r('app.media.unfinished'));
81. }
82. Text(`${this.thing}`)
83. .fontSize(24)
84. .decoration({ type: this.isFinished ? TextDecorationType.LineThrough : TextDecorationType.None })
85. .onClick(() => {
86. this.thing += 'lala';
87. })
88. }
89. .height('8%')
90. .width('90%')
91. .padding({ left: 15 })
92. .opacity(this.isFinished ? 0.3 : 1)
93. .border({ width: 1 })
94. .borderColor(Color.White)
95. .borderRadius(25)
96. .backgroundColor(Color.White)
97. }
98. }

100. @Entry
101. @Component
102. struct BuilderIndex {
103. @State isFinished: boolean = false;
104. @State data: TodoListData = new TodoListData(); // View绑定ViewModel的数据

106. aboutToAppear(): void {
107. for (let i = 0; i < this.data.planList.length; i++) {
108. this.data.planList[i] =
109. resource.resourceToString(this.data.planList[i] as Resource);
110. }
111. }

113. build() {
114. Column() {
115. // 全部待办
116. StateTodoComponent()

118. // 全选
119. BuilderAllChooseComponent({ isFinished: this.isFinished })

121. List() {
122. ForEach(this.data.planList, (item: string) => {
123. // 待办事项1
124. BuilderThingComponent({ isFinished: this.isFinished, thing: item })
125. .margin(5)
126. })
127. }
128. }
129. .height('100%')
130. .width('100%')
131. .margin({ top: 5, bottom: 5 })
132. .backgroundColor('#90f1f3f5')
133. }
134. }
```

[BuilderIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/pages/BuilderIndex.ets#L16-L155)

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/SWGOMExzSJabi05yVcNwCQ/zh-cn_image_0000002558604428.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=CEE7FFE8483CF2AB7C14BDA0B49517A6CC804040C71A8CC22ABA384588CB2B34)

### 总结

* 通过逐步优化代码结构，可以看到@Entry组件作为页面的入口，其build函数应该仅考虑将需要的组件组合起来，类似于搭积木。被page调用的子组件则如同积木，等着被需要的page进行调用。状态变量类似于粘合剂，当触发UI刷新事件时，状态变量自动刷新绑定的组件，实现page的按需刷新。
* 虽然现有的架构并未使用到MVVM的设计理念，但MVVM的核心理念已初见端倪。ArkUI的UI开发天然适合MVVM模式。在ArkUI中，page和组件构成View层，page负责组织组件，组件则作为构成元素。当组件需要更新时，通过状态变量驱动组件刷新，从而更新page。ViewModel的数据则来源于Model层。
* 示例中的代码功能较为简单，但随着功能的增加，主页面的代码量也会逐渐增多。当备忘录需要添加更多功能，且其他页面也需要使用到主页面的组件时，可以考虑采用MVVM模式来组织项目结构。

## 通过MVVM开发备忘录实战

上一章节展示了非MVVM模式下的代码组织方式。随着主页面代码的增加，应该采取合理的分层策略，使项目结构清晰，组件之间不互相引用，避免后期维护时牵一发而动全身，增加功能更新的困难。本章将通过对MVVM的核心文件组织模式，向开发者展示如何使用MVVM来重构上一章节的代码。

### MVVM文件结构说明

```
1. ├── src
2. │   ├── ets
3. │   │   ├── pages 存放页面组件。
4. │   │   ├── views 存放业务组件。
5. │   │   ├── shares 存放通用组件。
6. │   │   └── viewmodel 数据服务。
7. │   │   │   ├── LoginViewModel.ets 登录页ViewModel。
8. │   │   │   └── xxxViewModel.ets 其他页ViewModel。
9. │
```

### 分层设计技巧

**Model层**

* model层存放本应用核心数据结构，这层本身和UI开发关系不大，让用户按照自己的业务逻辑进行封装。

**ViewModel层**

注意：

ViewModel层不只是存放数据，它同时需要提供数据的服务及处理。

* ViewModel层是为视图服务的数据层。其设计具有两个特点：
  1. 按照页面组织数据。
  2. 每个页面数据进行懒加载。

**View层**

View层根据需要来组织，但View层需要区分一下三种组件：

* 页面组件：提供整体页面布局，实现多页面之间的跳转，前后台事件处理等页面内容。
* 业务组件：被页面引用，构建出页面。
* 共享组件：与项目无关的多项目共享组件。

共享组件和业务组件的区别：

业务组件包含了ViewModel数据，没有ViewModel，这个组件不能运行。

共享组件：不包含ViewModel层的数据，需要的数据从外部传入。共享组件包含一个自定义组件，只要外部参数（无业务参数）满足，就可以工作。

### 代码示例

按MVVM模式组织结构，重构如下：

```
1. ├── src
2. │   ├── ets
3. │   │   ├── model
4. │   │   │   ├── ThingModel.ets
5. │   │   │   └── TodoListModel.ets
6. │   │   ├── pages
7. │   │   │   ├── Index.ets
8. │   │   ├── views
9. │   │   │   ├── AllChooseComponent.ets
10. │   │   │   ├── ThingComponent.ets
11. │   │   │   ├── TodoComponent.ets
12. │   │   │   └── TodoListComponent.ets
13. │   │   ├── viewmodel
14. │   │   │   ├── ThingViewModel.ets
15. │   │   │   └── TodoListViewModel.ets
16. │   └── resources
17. │   │   ├── rawfile
18. │   │   │   ├── default_tasks.json
19. │
```

文件代码如下：

* ThingModel.ets

```
1. export default class ThingModel {
2. public thingName: string = 'Todo';
3. public isFinish: boolean = false;
4. }
```

[ThingModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/model/ThingModel.ets#L16-L21)

* TodoListModel.ets

```
1. import { common } from '@kit.AbilityKit';
2. import { util } from '@kit.ArkTS';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import ThingModel from './ThingModel';

6. const DOMAIN = 0x0001;
7. const TAG = 'TodoListModel';

9. export default class TodoListModel {
10. public things: Array<ThingModel> = [];

12. constructor(things: Array<ThingModel>) {
13. this.things = things;
14. }

16. async loadTasks(context: common.UIAbilityContext) {
17. try {
18. let getJson = await context.resourceManager.getRawFileContent('default_tasks.json');
19. let textDecoderOptions: util.TextDecoderOptions = { ignoreBOM: true };
20. let textDecoder = util.TextDecoder.create('utf-8', textDecoderOptions);
21. let result = textDecoder.decodeToString(getJson, { stream: false });
22. this.things = JSON.parse(result);
23. } catch (error) {
24. // 任务加载失败，输出error信息，便于排查失败原因
25. hilog.error(DOMAIN, TAG, 'Failed to load tasks. Cause: %{public}s', JSON.stringify(error.message));
26. }
27. }
28. }
```

[TodoListModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/model/TodoListModel.ets#L16-L36)

* Index.ets

```
1. import { common } from '@kit.AbilityKit';
2. // import ViewModel
3. import TodoListViewModel from '../viewmodel/TodoListViewModel';

5. // import View
6. import { TodoComponent } from '../views/TodoComponent';
7. import { AllChooseComponent } from '../views/AllChooseComponent';
8. import { TodoListComponent } from '../views/TodoListComponent';

10. @Entry
11. @Component
12. struct TodoList {
13. @State todoListViewModel: TodoListViewModel = new TodoListViewModel(); // View绑定ViewModel的数据
14. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

16. async aboutToAppear() {
17. await this.todoListViewModel.loadTasks(this.context);
18. }

20. build() {
21. Column() {
22. Row({ space: 40 }) {
23. // 全部待办
24. TodoComponent()
25. // 全选
26. AllChooseComponent({ todoListViewModel: this.todoListViewModel })
27. }

29. Column() {
30. TodoListComponent({ thingViewModelArray: this.todoListViewModel.things })
31. }
32. }
33. .height('100%')
34. .width('100%')
35. .margin({ top: 5, bottom: 5 })
36. .backgroundColor('#90f1f3f5')
37. }
38. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/pages/Index.ets#L16-L55)

* AllChooseComponent.ets

```
1. import TodoListViewModel from '../viewmodel/TodoListViewModel';
2. import { common } from '@kit.AbilityKit';

4. @Component
5. export struct AllChooseComponent {
6. context1 = this.getUIContext().getHostContext() as common.UIAbilityContext;
7. // 请在resources\base\element\string.json文件中配置name为'check_all'，value为非空字符串的资源
8. @State titleName: ResourceStr = this.context1.resourceManager.getStringSync($r('app.string.check_all').id);
9. @Link todoListViewModel: TodoListViewModel;

11. build() {
12. Row() {
13. Button(`${this.titleName}`, { type: ButtonType.Capsule })
14. .onClick(() => {
15. this.todoListViewModel.chooseAll(); // View层点击事件发生时，调用ViewModel层方法chooseAll处理逻辑
16. this.titleName = this.todoListViewModel.isChosen ?
17. // 请在resources\base\element\string.json文件中配置name为'check_all'，value为非空字符串的资源
18. this.context1.resourceManager.getStringSync($r('app.string.check_all').id)
19. // 请在resources\base\element\string.json文件中配置name为'deselect_all'，value为非空字符串的资源
20. : this.context1.resourceManager.getStringSync($r('app.string.deselect_all').id);
21. })
22. .fontSize(30)
23. .fontWeight(FontWeight.Bold)
24. .backgroundColor('#f7f6cc74')
25. }
26. .padding({ left: this.todoListViewModel.isChosen ? 15 : 0 })
27. .width('100%')
28. .margin({ top: 10, bottom: 10 })
29. }
30. }
```

[AllChooseComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/views/AllChooseComponent.ets#L16-L48)

* ThingComponent.ets

```
1. import ThingViewModel from '../viewmodel/ThingViewModel';

3. @Component
4. export struct ThingComponent {
5. @ObjectLink thing: ThingViewModel;

7. @Builder
8. displayIcon(icon: Resource) {
9. Image(icon)
10. .width(28)
11. .height(28)
12. .onClick(() => {
13. this.thing.updateIsFinish(); // View层点击事件发生时，调用ViewModel层方法updateIsFinish处理逻辑
14. })
15. .id(this.thing.thingName)
16. }

18. build() {
19. // 待办事项
20. Row({ space: 15 }) {
21. if (this.thing.isFinish) {
22. // 请将$r('app.media.finished')替换为实际资源文件
23. this.displayIcon($r('app.media.finished'));
24. } else {
25. // 请将$r('app.media.unfinished')替换为实际资源文件
26. this.displayIcon($r('app.media.unfinished'));
27. }

29. Text(`${this.thing.thingName}`)
30. .fontSize(24)
31. .decoration({ type: this.thing.isFinish ? TextDecorationType.LineThrough : TextDecorationType.None })
32. .onClick(() => {
33. this.thing.addSuffixes(); // View层点击事件发生时，调用ViewModel层方法addSuffixes处理逻辑
34. })
35. }
36. .height('8%')
37. .width('90%')
38. .padding({ left: 15 })
39. .opacity(this.thing.isFinish ? 0.3 : 1)
40. .border({ width: 1 })
41. .borderColor(Color.White)
42. .borderRadius(25)
43. .backgroundColor(Color.White)
44. }
45. }
```

[ThingComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/views/ThingComponent.ets#L16-L64)

* TodoComponent.ets

```
1. @Component
2. export struct TodoComponent {
3. build() {
4. Row() {
5. // 请将$r('app.string.all_tasks')替换为实际资源文件，在本示例中该资源文件的value值为"全部待办"
6. Text($r('app.string.all_tasks'))
7. .fontSize(30)
8. .fontWeight(FontWeight.Bold)
9. }
10. .padding({ left: 15 })
11. .width('50%')
12. .margin({ top: 10, bottom: 10 })
13. }
14. }
```

[TodoComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/views/TodoComponent.ets#L16-L31)

* TodoListComponent.ets

```
1. import ThingViewModel from '../viewmodel/ThingViewModel';
2. import { ThingViewModelArray } from '../viewmodel/TodoListViewModel'
3. import { ThingComponent } from './ThingComponent';

5. @Component
6. export struct TodoListComponent {
7. @ObjectLink thingViewModelArray: ThingViewModelArray;

9. build() {
10. Column() {
11. List() {
12. ForEach(this.thingViewModelArray, (item: ThingViewModel) => {
13. // 待办事项
14. ListItem() {
15. ThingComponent({ thing: item })
16. .margin(5)
17. }
18. }, (item: ThingViewModel) => {
19. return item.thingName;
20. })
21. }
22. }
23. }
24. }
```

[TodoListComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/views/TodoListComponent.ets#L16-L41)

* ThingViewModel.ets

```
1. import ThingModel from '../model/ThingModel';

3. @Observed
4. export default class ThingViewModel {
5. @Track public thingName: string = 'Todo';
6. @Track public isFinish: boolean = false;
7. public context: Context = AppStorage.get('context')!;

9. updateTask(thing: ThingModel) {
10. this.thingName = thing.thingName;
11. this.isFinish = thing.isFinish;
12. }

14. updateIsFinish(): void {
15. this.isFinish = !this.isFinish;
16. }

18. addSuffixes(): void {
19. this.thingName += 'lala';
20. }
21. }
```

[ThingViewModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/viewmodel/ThingViewModel.ets#L16-L40)

* TodoListViewModel.ets

```
1. import ThingViewModel from './ThingViewModel';
2. import { common } from '@kit.AbilityKit';
3. import TodoListModel from '../model/TodoListModel';

5. @Observed
6. export class ThingViewModelArray extends Array<ThingViewModel> {
7. }

9. @Observed
10. export default class TodoListViewModel {
11. @Track public isChosen: boolean = true;
12. @Track public things: ThingViewModelArray = new ThingViewModelArray();

14. async loadTasks(context: common.UIAbilityContext) {
15. let todoList = new TodoListModel([]);
16. await todoList.loadTasks(context);
17. for (let thing of todoList.things) {
18. let todoListViewModel = new ThingViewModel();
19. todoListViewModel.updateTask(thing);
20. this.things.push(todoListViewModel);
21. }
22. }

24. chooseAll(): void {
25. // 遍历所有待办事项，设置其完成状态
26. for (let thing of this.things) {
27. thing.isFinish = this.isChosen;
28. }
29. this.isChosen = !this.isChosen;
30. }
31. }
```

[TodoListViewModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArktsMvvmSample/entry/src/main/ets/viewmodel/TodoListViewModel.ets#L16-L47)

* default\_tasks.json

```
1. [
2. {"thingName": "7.30起床", "isFinish": false},
3. {"thingName": "8.30早餐", "isFinish": false},
4. {"thingName": "11.30中餐", "isFinish": false},
5. {"thingName": "17.30晚餐", "isFinish": false},
6. {"thingName": "21.30夜宵", "isFinish": false},
7. {"thingName": "22.30洗澡", "isFinish": false},
8. {"thingName": "1.30睡觉", "isFinish": false}
9. ]
```

MVVM模式拆分后的代码结构更加清晰，模块职责更明确。新页面需要使用事件组件，比如TodoListComponent组件，只需导入组件。

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/chJUKj_-TBOs0rA9K1zcUA/zh-cn_image_0000002589323953.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052708Z&HW-CC-Expire=86400&HW-CC-Sign=0F9D285F1A20D82C2892AA591B8539E5B22C6A3AB31E77CF93A080A4459F89D1)
