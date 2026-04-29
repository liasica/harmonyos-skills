---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-custom-components-new-lifecycle
title: 自定义组件生命周期（推荐）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 自定义组件 > 自定义组件生命周期（推荐）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:02+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f0fc59089e189af35516b989c6e9a1f2e99e472b5c235bcfd5e4c66c18425ce7
---

## 概述

已有的[自定义组件生命周期](arkts-page-custom-components-lifecycle.md)回调函数触发只取决于事件的触发，在某些特定的情况下，会出现自定义组件生命周期回调函数的触发顺序不符合预期。比如：[aboutToDisappear在特定情况下会误调用aboutToAppear、组件未展开被复用时，会误调用aboutToReuse](arkts-custom-components-new-lifecycle.md#生命周期回调函数的区别)。新的自定义组件生命周期回调函数受[状态机](../harmonyos-references/ts-custom-component-new-lifecycle.md#customcomponentlifecyclestate)限制，生命周期回调函数调用时机符合预期。

自定义组件生命周期，即用[@Component](arkts-create-custom-components.md#component)或[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件的生命周期，从API version 23开始，提供以下生命周期装饰器：

* [@ComponentInit](../harmonyos-references/ts-custom-component-new-lifecycle.md#componentinit)：@ComponentInit装饰的函数在自定义组件即将构造完毕时执行。可以在此函数中注册监听和修改变量。
* [@ComponentAppear](../harmonyos-references/ts-custom-component-new-lifecycle.md#componentappear)：组件即将出现时回调该装饰器装饰的函数，具体时机为在创建自定义组件的新实例后，在执行其build函数之前执行。
* [@ComponentBuilt](../harmonyos-references/ts-custom-component-new-lifecycle.md#componentbuilt)：在组件首次渲染触发的build函数执行完成后，回调该装饰器装饰的函数，后续组件重新渲染将不再回调该函数。开发者可以在此阶段实现数据上报等不影响实际UI的功能。
* [@ComponentDisappear](../harmonyos-references/ts-custom-component-new-lifecycle.md#componentdisappear)：该装饰器装饰的函数在自定义组件析构销毁之前执行。不建议在@ComponentDisappear装饰的函数中改变状态变量，特别是@Link变量的修改可能会导致应用程序行为不稳定。
* [@ComponentReuse](../harmonyos-references/ts-custom-component-new-lifecycle.md#componentreuse)：当可复用的自定义组件从缓存中重新添加到节点树时调用该装饰器装饰的函数，以接收组件的构造入参。最后，@ComponentReuse装饰的函数会递归遍历所有子组件，对每个完成复用的组件调用@ComponentReuse装饰的函数。
* [@ComponentRecycle](../harmonyos-references/ts-custom-component-new-lifecycle.md#componentrecycle)：当组件被回收后触发，先执行应用程序中定义的必要回收操作，完成回收后调用该装饰器装饰的函数。最后，@ComponentRecycle装饰的函数会递归遍历所有子组件，对每个完成回收的组件调用@ComponentRecycle装饰的函数。

自定义组件生命周期受状态机限制，流程如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/AR7JvBO9R-K728bVm9Qetw/zh-cn_image_0000002589323913.png?HW-CC-KV=V1&HW-CC-Date=20260429T052701Z&HW-CC-Expire=86400&HW-CC-Sign=6B47440774DBCFD3E34CB15F3167306C0DA1B1E9440B9DD82E0E2341CBCC6200)

### 自定义组件的创建和渲染流程

1. 自定义组件的创建：自定义组件的实例由ArkUI框架创建。
2. 初始化自定义组件的成员变量：通过本地默认值或者构造函数传递参数来初始化自定义组件的成员变量，初始化顺序为成员变量的定义顺序。
3. 在首次渲染的时候，执行build函数渲染系统组件，如果子组件为自定义组件，则创建自定义组件的实例。在首次渲染的过程中，框架会记录状态变量和组件的映射关系，当状态变量改变时，驱动其相关的组件刷新。

### 自定义组件的删除

例如if组件的分支改变或ForEach循环渲染中数组的个数改变，组件将被移除：

1. 在删除组件之前，将调用其@ComponentDisappear装饰的生命周期函数，标记着该节点将要被销毁。ArkUI的节点删除机制是：后端节点直接从组件树上摘下，后端节点被销毁，对前端节点解引用，前端节点已经没有引用时，将被Ark虚拟机垃圾回收。
2. 自定义组件和它的变量将被删除，如果组件有同步的变量（如[@Link](arkts-link.md)、[@Prop](arkts-prop.md)、[@StorageLink](arkts-appstorage.md#storagelink)），将从[同步源](arkts-state-management-glossary.md#数据源同步源data-source)上取消注册。

## 限制条件

* @ComponentInit、@ComponentAppear、@ComponentBuilt、@ComponentDisappear、@ComponentReuse和@ComponentRecycle只能在@Component或者@ComponentV2装饰的struct中使用，否则编译会报错。
* @ComponentInit、@ComponentAppear、@ComponentBuilt、@ComponentDisappear和@ComponentRecycle装饰的函数不能有入参，否则编译会报错。
* 在@Component装饰的struct中，@ComponentReuse装饰的函数可以没有入参或者有一个入参，否则编译会报错。
* 在@ComponentV2装饰的struct中，@ComponentReuse装饰的函数不能有入参，否则编译会报错。
* 新增生命周期装饰器装饰方法时，自定义组件对应事件发生时会回调该方法。新增生命周期装饰器建议单独使用，不与其他状态变量装饰器联合使用。比如生命周期装饰器和[@Computed](arkts-new-computed.md)联合使用时，生命周期装饰器不生效。

  ```
  1. @Computed
  2. @ComponentAppear
  3. get sum() {
  4. return 1 + 2 + 3; // 错误用法，生命周期装饰器装饰get方法不生效
  5. }
  ```
* 当自定义组件没有使用生命周期装饰器，且没有注册监听，使用[getCurrentState](../harmonyos-references/ts-custom-component-new-lifecycle.md#getcurrentstate)查询自定义组件当前生命周期状态时，返回值永远为[CustomComponentLifecycleState.INIT](../harmonyos-references/ts-custom-component-new-lifecycle.md#customcomponentlifecyclestate)。

## 使用场景

### 自定义组件嵌套使用

通过以下示例，来详细说明自定义组件在嵌套使用时，自定义组件生命周期的调用时序：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { ComponentAppear, ComponentBuilt, ComponentDisappear } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State show: boolean = true;
8. @State btnColor: string = '#FF007DFF';
9. build() {
10. Column() {
11. Button('delete Parent And Child')
12. .margin(20)
13. .backgroundColor(this.btnColor)
14. .onClick(() => {
15. this.show = !this.show;
16. })
17. if (this.show) {
18. Parent()
19. }
20. }
21. }
22. }
23. @Component
24. struct Parent {
25. @State showChild: boolean = true;
26. @State btnColor: string = '#FF007DFF';
27. // 组件生命周期ComponentAppear，在Parent创建实例后，执行build函数之前回调myAppear
28. @ComponentAppear
29. myAppear() {
30. hilog.info(0x0000, 'testTag', 'Parent myAppear');
31. }
32. // 组件生命周期ComponentBuilt，在Parent首次渲染触发的build函数执行完成之后回调myBuilt
33. @ComponentBuilt
34. myBuilt() {
35. hilog.info(0x0000, 'testTag', 'Parent myBuilt');
36. }
37. // 组件生命周期ComponentDisappear，在Parent析构销毁之前回调myDisappear
38. @ComponentDisappear
39. myDisappear() {
40. hilog.info(0x0000, 'testTag', 'Parent myDisappear');
41. }

43. build() {
44. Column() {
45. // this.showChild为true，创建Child子组件，执行Child myAppear
46. if (this.showChild) {
47. Child()
48. }
49. Button('delete Child')
50. .margin(20)
51. .backgroundColor(this.btnColor)
52. .onClick(() => {
53. // 更改this.showChild为false，删除Child子组件，执行Child myDisappear
54. // 更改this.showChild为true，添加Child子组件，执行Child myAppear
55. this.showChild = !this.showChild;
56. })
57. }
58. }
59. }

61. @Component
62. struct Child {
63. @State title: string = 'Hello World';
64. @ComponentDisappear
65. myDisappear() {
66. hilog.info(0x0000, 'testTag', 'Child myDisappear');
67. }
68. @ComponentBuilt
69. myBuilt() {
70. hilog.info(0x0000, 'testTag', 'Child myBuilt');
71. }
72. @ComponentAppear
73. myAppear() {
74. hilog.info(0x0000, 'testTag', 'Child myAppear');
75. }

77. build() {
78. Text(this.title)
79. .fontSize(50)
80. .margin(20)
81. .onClick(() => {
82. this.title = 'Hello ArkUI';
83. })
84. }
85. }
```

以上示例中，Index页面包含两个自定义组件，一个是Parent，一个是Child，Parent及其子组件Child分别声明了各自的自定义组件生命周期装饰器装饰的函数（myAppear / myBuilt / myDisappear）。

* 应用冷启动的初始化流程为：Parent myAppear --> Parent build --> Parent myBuilt --> Child myAppear --> Child build --> Child myBuilt。此处体现了自定义组件懒展开特性，即Parent执行完myBuilt之后才会执行Child组件的myAppear。日志输出信息如下：

```
1. Parent myAppear
2. Parent myBuilt
3. Child myAppear
4. Child myBuilt
```

* 点击Button按钮，更改showChild为false，删除Child组件，执行Child myDisappear函数。
* 如果点击Button按钮，更改show为false,或者直接退出应用，则会触发以下生命周期：Parent myDisappear --> Child myDisappear，此处体现了自定义组件删除顺序也是从父到子。日志输出信息如下：

```
1. Parent myDisappear
2. Child myDisappear
```

* 最小化应用或者应用进入后台，当前Index页面未被销毁，所以并不会执行组件的myDisappear。
* 如果showChild的默认值为false，则应用冷启动的初始化流程为：Parent myAppear --> Parent build --> Parent myBuilt。日志输出信息如下：

```
1. Parent myAppear
2. Parent myBuilt
```

* 如果showChild的默认值为false，此时点击Button按钮更改show为false或者直接退出应用，则只执行Parent myDisappear函数。
* 如果showChild的默认值为false，此时点击Button按钮，更改showChild为true，添加Child组件，添加流程为：Child myAppear --> Child build --> Child myBuilt。日志输出信息如下：

```
1. Child myAppear
2. Child myBuilt
```

当showchild为默认值true时，该示例的生命周期流程图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/etbq5S70Qv-HAJOw0QWO-A/zh-cn_image_0000002589243853.png?HW-CC-KV=V1&HW-CC-Date=20260429T052701Z&HW-CC-Expire=86400&HW-CC-Sign=889B484D5BC5C93ACD9A166C6FB866A85D1722BF9F5B7DC1814B9F8D09EC5A03)

### 自定义组件回收复用

通过以下示例，来详细说明自定义组件在使用时，回收复用的生命周期调用时序：

```
1. import { ComponentInit, ComponentAppear, ComponentBuilt, ComponentDisappear, ComponentReuse, ComponentRecycle } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export class Message {
5. value: string | undefined;
6. constructor(value: string) {
7. this.value = value;
8. }
9. }
10. @Entry
11. @Component
12. struct Index {
13. @State switch: boolean = true;

15. build() {
16. Column() {
17. Button('Hello')
18. .fontSize(30)
19. .fontWeight(FontWeight.Bold)
20. .onClick(() => {
21. this.switch = !this.switch;
22. })
23. // 通过改变switch，实现Child的回收和复用
24. // 更改this.switch为false，回收Child子组件，执行Child myRecycle
25. // 更改this.switch为true，复用Child子组件，执行Child myReuse
26. if (this.switch) {
27. // 如果只有一个复用的组件，可以不用设置reuseId。
28. Child({ message: new Message('Child') })
29. .reuseId('Child')
30. }
31. }
32. .height('100%')
33. .width('100%')
34. }
35. }

37. @Reusable
38. @Component
39. struct Child {
40. @State message: Message = new Message('Child');
41. @State label: string = 'HelloWorld';
42. @State switch: boolean = true;
43. @ComponentInit
44. myInit() {
45. hilog.info(0x0000, 'testTag', 'Child myInit');
46. }
47. @ComponentAppear
48. myAppear() {
49. this.label = 'myAppear';
50. hilog.info(0x0000, 'testTag', 'Child myAppear');
51. }
52. @ComponentBuilt
53. myBuilt() {
54. this.label = 'myBuilt';
55. hilog.info(0x0000, 'testTag', 'Child myBuilt');
56. }
57. @ComponentRecycle
58. myRecycle() {
59. this.label = 'myRecycle';
60. hilog.info(0x0000, 'testTag', 'Child myRecycle');
61. }
62. @ComponentDisappear
63. myDisappear() {
64. this.label = 'myDisappear';
65. hilog.info(0x0000, 'testTag', 'Child myDisappear');
66. }
67. @ComponentReuse
68. myReuse(params?: Record<string, Object | undefined | null>) {
69. this.label = 'myReuse';
70. hilog.info(0x0000, 'testTag', 'Child myReuse');
71. }

73. build() {
74. Column() {
75. Text(this.message.value)
76. .fontSize(30)
77. Button('Hello')
78. .fontSize(30)
79. .fontWeight(FontWeight.Bold)
80. .onClick(() => {
81. this.switch = !this.switch;
82. })
83. if (this.switch) {
84. GrandChild({ message: new Message('GrandChild') })
85. .reuseId('GrandChild')
86. }
87. }
88. .borderWidth(1)
89. .height(100)
90. }
91. }

93. @Reusable
94. @Component
95. struct GrandChild {
96. @State message: Message = new Message('GrandChild');
97. @State label: string = 'HelloWorld';
98. @State switch: boolean = true;
99. @ComponentInit
100. myInit() {
101. hilog.info(0x0000, 'testTag', 'GrandChild myInit');
102. }
103. @ComponentAppear
104. myAppear() {
105. this.label = 'myAppear';
106. hilog.info(0x0000, 'testTag', 'GrandChild myAppear');
107. }
108. @ComponentBuilt
109. myBuilt() {
110. this.label = 'myBuilt';
111. hilog.info(0x0000, 'testTag', 'GrandChild myBuilt');
112. }
113. @ComponentRecycle
114. myRecycle() {
115. this.label = 'myRecycle';
116. hilog.info(0x0000, 'testTag', 'GrandChild myRecycle');
117. }
118. @ComponentDisappear
119. myDisappear() {
120. this.label = 'myDisappear';
121. hilog.info(0x0000, 'testTag', 'GrandChild myDisappear');
122. }
123. @ComponentReuse
124. myReuse(params?: Record<string, Object | undefined | null>) {
125. this.label = 'myReuse';
126. hilog.info(0x0000, 'testTag', 'GrandChild myReuse');
127. }

129. build() {
130. Column() {
131. Text(this.message.value)
132. .fontSize(30)
133. }
134. .borderWidth(1)
135. .height(100)
136. }
137. }
```

以上示例中，Index页面包含自定义组件Child，Child组件包含自定义组件GrandChild。Child和GrandChild分别声明了各自的自定义组件生命周期装饰器装饰的函数（myInit / myAppear / myBuilt / myRecycle / myReuse / myDisappear）。

* 应用冷启动的初始化流程为：Child myInit --> Child myAppear --> GrandChild myInit --> Child myBuilt --> GrandChild myAppear --> GrandChild myBuilt。此处体现了自定义组件懒展开特性，即Child执行完myBuilt之后才会执行GrandChild组件的myAppear。日志输出信息如下：

```
1. Child myInit
2. Child myAppear
3. GrandChild myInit
4. Child myBuilt
5. GrandChild myAppear
6. GrandChild myBuilt
```

* 点击Button按钮，更改showChild为false，回收Child组件和GrandChild组件，执行Child和GrandChild的myRecycle函数。

```
1. Child myRecycle
2. GrandChild myRecycle
```

### 自定义组件生命周期的注册监听

[CustomComponentLifecycleObserver](../harmonyos-references/ts-custom-component-new-lifecycle.md#customcomponentlifecycleobserver)用于监听自定义组件的生命周期，开发者可以根据自己的需求重写CustomComponentLifecycleObserver中的回调函数。

```
1. import { ComponentInit, ComponentDisappear, UIUtils, CustomComponentLifecycleObserver, CustomComponentLifecycle } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. export class Message {
5. value: string | undefined;
6. constructor(value: string) {
7. this.value = value;
8. }
9. }

11. @Entry
12. @Component
13. struct Index {
14. @State switch: boolean = true;

16. build() {
17. Column() {
18. Button('Hello')
19. .fontSize(30)
20. .fontWeight(FontWeight.Bold)
21. .onClick(() => {
22. this.switch = !this.switch;
23. })
24. if (this.switch) {
25. // 如果只有一个复用的组件，可以不用设置reuseId。
26. Child({ message: new Message('Child') })
27. .reuseId('Child')
28. }
29. }
30. .height('100%')
31. .width('100%')
32. }
33. }

35. @Reusable
36. @Component
37. struct Child {
38. @State message: Message = new Message('AboutToReuse');
39. @State label: string = 'HelloWorld';
40. @ComponentInit
41. myInit(): void {
42. registerObserver(UIUtils.getLifecycle(this));
43. }
44. @ComponentDisappear
45. myDisappear(): void {
46. unRegisterObserver(UIUtils.getLifecycle(this));
47. }

49. build() {
50. Column() {
51. Text(this.message.value)
52. .fontSize(30)
53. }
54. }
55. }

57. export class MyObserver implements CustomComponentLifecycleObserver {
58. // 重写CustomComponentLifecycleObserver中的生命周期事件，CustomComponentLifecycleObserver无法监听父组件的aboutToInit
59. aboutToAppear() {
60. hilog.info(0x0000, 'testTag', 'MyObserver aboutToAppear');
61. }
62. onDidBuild() {
63. hilog.info(0x0000, 'testTag', 'MyObserver onDidBuild');
64. }
65. aboutToReuse(params?: Record<string, Object | undefined | null>) {
66. // params存在时，为V1的复用；
67. hilog.info(0x0000, 'testTag', 'MyObserver aboutToReuse');
68. }
69. aboutToRecycle() {
70. hilog.info(0x0000, 'testTag', 'MyObserver aboutToRecycle');
71. }
72. // 在父组件的aboutToDelete函数中解除注册监听，则无法监听父组件的aboutToDisappear
73. aboutToDisappear() {
74. hilog.info(0x0000, 'testTag', 'MyObserver aboutToDisappear');
75. }
76. }

78. // 创建Observer对象
79. const observer = new MyObserver();
80. export function registerObserver(lifeCycle: CustomComponentLifecycle) {
81. // 向lifeCycle注册监听
82. lifeCycle.addObserver(observer);
83. }
84. export function unRegisterObserver(lifeCycle: CustomComponentLifecycle) {
85. // 向lifeCycle取消注册监听
86. lifeCycle.removeObserver(observer);
87. }
```

在@ComponentDisappear装饰的函数中解除注册监听，所以监听器无法监听到aboutToDisappear。

按两次Hello按钮，然后关闭程序，此时日志输出信息如下：

```
1. MyObserver aboutToAppear
2. MyObserver onDidBuild
3. MyObserver aboutToRecycle
4. MyObserver aboutToReuse
```

可以在组件的onAppear和onDisAppear中注册和解除监听。在onAppear中注册监听，此时组件已经处于Appeared状态，所以无法监听组件的aboutToAppear。

```
1. Column() {
2. Text('Hello World')
3. }
4. .onAppear(() => {
5. // 在onAppear中注册监听
6. registerObserver(UIUtils.getLifecycle(this));
7. })
8. .onDisAppear(() => {
9. unRegisterObserver(UIUtils.getLifecycle(this));
10. })
```

## 生命周期回调函数的区别

### @ComponentAppear、@ComponentDisappear与aboutToAppear、aboutToDisappear的区别

自定义组件在INIT状态时，即将转化为APPEARED时，先调用aboutToAppear后调用@ComponentAppear装饰的函数。

自定义组件在INIT状态、BUILT状态或RECYCLED状态时，即将转化为DISAPPEARED时，先调用@ComponentDisappear装饰的函数后调用aboutToDisappear。

aboutToAppear是自定义组件build之前执行，aboutToDisappear是自定义组件销毁前执行。但有时自定义组件没有build，就被销毁。为了执行一个完整的生命周期，aboutToDisappear会判断，该组件是否执行了aboutToAppear，如果没有执行便强制触发一次aboutToAppear。@ComponentAppear装饰的函数和@ComponentDisappear装饰的函数受状态机约束，@ComponentDisappear装饰的函数不会误调用@ComponentAppear装饰的函数。例子如下所示：

```
1. // Index.ets
2. import { SwiperExample } from './SwiperPage';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';
8. controller: TabsController = new TabsController();
9. @State show: boolean = false;
10. @State currentTabIndex: number = 0;

12. build() {
13. RelativeContainer() {
14. Text('start')
15. .fontSize(50)
16. .fontColor('#000')
17. .id('text')
18. .alignRules({
19. top: { anchor: '__container__', align: VerticalAlign.Top },
20. middle: { anchor: '__container__', align: HorizontalAlign.Center }
21. })
22. .onClick(() => {
23. // this.show为true，创建SwiperExample；this.show为false，销毁SwiperExample
24. this.show = !this.show;
25. })
26. if (this.show) {
27. SwiperExample()
28. .id('TableExample')
29. .alignRules({
30. bottom: { anchor: '__container__', align: VerticalAlign.Bottom },
31. middle: { anchor: '__container__', align: HorizontalAlign.Center }
32. })
33. .width('100%')
34. .height('auto')
35. }
36. }
37. .height('100%')
38. .width('100%')
39. }
40. }
```

```
1. // SwiperPage.ets
2. import { ComponentAppear, ComponentDisappear } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. export struct SwiperPage {
7. @State name: number = 0;
8. aboutToAppear(): void {
9. hilog.info(0x0000, 'testTag', 'SwiperPage aboutToAppear %{public}d', this.name);
10. }
11. aboutToDisappear(): void {
12. hilog.info(0x0000, 'testTag', 'SwiperPage aboutToDisappear %{public}d', this.name);
13. }
14. @ComponentAppear
15. myAppear(): void {
16. hilog.info(0x0000, 'testTag', 'SwiperPage myAppear %{public}d', this.name);
17. }
18. @ComponentDisappear
19. myDisappear(): void {
20. hilog.info(0x0000, 'testTag', 'SwiperPage myDisappear %{public}d', this.name);
21. }

23. build() {
24. Text(this.name.toString())
25. .width('90%')
26. .height(160)
27. .fontColor(Color.Black)
28. .backgroundColor(0xAFEEEE)
29. .textAlign(TextAlign.Center)
30. .fontSize(30)
31. }
32. }

34. class MyDataSource implements IDataSource {
35. list: number[] = [];
36. constructor(list: number[]) {
37. this.list = list;
38. }
39. totalCount(): number {
40. return this.list.length;
41. }
42. getData(index: number): number {
43. return this.list[index];
44. }
45. registerDataChangeListener(listener: DataChangeListener): void {}
46. unregisterDataChangeListener() {}
47. }

49. @Entry
50. @Component
51. export struct SwiperExample {
52. private swiperController: SwiperController = new SwiperController()
53. private data: MyDataSource = new MyDataSource([])
54. @State selectedTabIndex: number = 0;
55. @ComponentAppear
56. myAppear(): void {
57. // myAppear中为data赋值
58. let list: number[] = [];
59. for (let i = 0; i <= 11; i++) {
60. list.push(i);
61. }
62. this.data = new MyDataSource(list);
63. }

65. build() {
66. Column({ space: 5 }) {
67. Swiper(this.swiperController) {
68. ForEach(this.data.list, (item: number) => {
69. SwiperPage({
70. name: item
71. })
72. })
73. }
74. .index(this.selectedTabIndex)
75. .autoPlay(false)
76. .disableSwipe(true)
77. .indicator(false)
78. .width('100%')
79. .cachedCount(2) // 以当前节点为基础，往前缓存两个节点，往后缓存两个节点
80. .onChange((index) => {
81. this.selectedTabIndex = index;
82. })
83. Row({ space: 12 }) {
84. Button('showNext')
85. .onClick(() => {
86. this.swiperController.showNext();
87. })
88. Button('showPrevious')
89. .onClick(() => {
90. this.swiperController.showPrevious();
91. })
92. }
93. .margin(5)
94. }
95. .width('100%')
96. .margin({ top: 5 })
97. }
98. }
```

启动程序后，先按start按钮，此时只有swipe缓存的五个节点开始执行aboutToAppear和myAppear，非缓存的节点未触发aboutToAppear和myAppear。

日志输出信息如下：

```
1. SwiperPage:aboutToAppear 0
2. SwiperPage:myAppear 0
3. SwiperPage:aboutToAppear 11
4. SwiperPage:myAppear 11
5. SwiperPage:aboutToAppear 1
6. SwiperPage:myAppear 1
7. SwiperPage:aboutToAppear 10
8. SwiperPage:myAppear 10
9. SwiperPage:aboutToAppear 2
10. SwiperPage:myAppear 2
```

此时关闭程序，缓存的五个节点正常触发aboutToDisappear，但是非缓存的节点触发aboutToDisappear前，会强制触发aboutToAppear。无论是否是缓存节点，myDisappear不会误触发myAppear。

```
1. SwiperPage:myDisappear 0
2. SwiperPage:aboutToDisappear 0
3. SwiperPage:myDisappear 1
4. SwiperPage:aboutToDisappear 1
5. SwiperPage:myDisappear 2
6. SwiperPage:aboutToDisappear 2
7. SwiperPage:aboutToAppear 3
8. SwiperPage:myDisappear 3
9. SwiperPage:aboutToDisappear 3
10. SwiperPage:aboutToAppear 4
11. SwiperPage:myDisappear 4
12. SwiperPage:aboutToDisappear 4
13. ...
```

### @ComponentReuse、@ComponentRecycle与aboutToReuse、aboutToRecycle的区别

自定义组件在RECYCLED状态时，即将转化为BUILT时，先调用aboutToReuse后调用@ComponentReuse装饰的函数。

自定义组件在BUILT状态时，即将转化为RECYCLED时，先调用aboutToRecycle后调用@ComponentRecycle装饰的函数。

```
1. import { ComponentAppear, ComponentBuilt, ComponentReuse } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Entry
5. @Component
6. struct ReusableTest {
7. @State flag1: boolean = true;
8. @State flag2: boolean = false;
9. build() {
10. Column() {
11. // 点击Button切换flag1，触发ReusableComp1和ReusableComp2的回收/复用
12. Button('a')
13. .onClick(() => {
14. this.flag1 = !this.flag1;
15. })
16. // 点击Button切换flag2，触发ReusableComp1和ReusableComp3的回收/复用
17. Button('b')
18. .onClick(() => {
19. this.flag2 = !this.flag2;
20. })
21. if (this.flag1) {
22. ReusableComp1({ flag: true })
23. }
24. if (this.flag2) {
25. ReusableComp1({ flag: false })
26. }
27. }
28. }
29. }

31. @Reusable
32. @Component
33. struct ReusableComp1 {
34. @Require @Prop flag: boolean = true;
35. build() {
36. if (this.flag) {
37. ReusableComp2()
38. } else {
39. ReusableComp3()
40. }
41. }
42. }

44. @Reusable
45. @Component
46. struct ReusableComp2 {
47. build() {
48. Text('A')
49. }
50. }

52. @Reusable
53. @Component
54. struct ReusableComp3 {
55. aboutToAppear(): void {
56. hilog.info(0x0000, 'testTag', 'ReusableComp3 aboutToAppear');
57. }
58. aboutToReuse(params: Record<string, Object | undefined | null>): void {
59. hilog.info(0x0000, 'testTag', 'ReusableComp3 aboutToReuse');
60. }
61. @ComponentReuse
62. myReuse(params: Record<string, Object | undefined | null>): void {
63. hilog.info(0x0000, 'testTag', 'ReusableComp3 myReuse');
64. }
65. @ComponentAppear
66. myAppear(): void {
67. hilog.info(0x0000, 'testTag', 'ReusableComp3 myAppear');
68. }
69. @ComponentBuilt
70. myBuilt(): void {
71. hilog.info(0x0000, 'testTag', 'ReusableComp3 myBuilt');
72. }

74. build() {
75. Text('B')
76. }
77. }
```

按下a按钮，此时ReusableComp2进入回收状态，再按下b按钮，此时ReusableComp3第一次被创建，此时日志输出信息如下：

```
1. ReusableComp3 aboutToReuse
2. ReusableComp3 aboutToAppear
3. ReusableComp3 myAppear
4. ReusableComp3 myBuilt
```

ReusableComp3从未创建过，但按下b按钮后，ReusableComp3的aboutToReuse误调用，同时ReusableComp3的aboutToAppear和myBuilt被调用。而myReuse没有被误调用，这是因为myReuse受状态机约束，当组件不是RECYCLED状态时，不会执行myReuse。
