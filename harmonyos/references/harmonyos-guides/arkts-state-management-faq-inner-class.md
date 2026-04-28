---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-class
title: 数据对象状态管理常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理常见问题 > 数据对象状态管理常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c343e6b0474594319855ce79ee0dc54c84252cdda47523fbd9f4d75f24897219
---

大型应用中需要封装大量的数据对象，数据对象内部状态变量的使用极大地影响开发者的开发效率，本文将介绍数据对象状态管理的常见问题及解决方案。

在状态管理中，类会被一层“代理”包装。当修改类的成员变量时，代理会拦截该操作并完成两项任务：

* 同步更新数据源：确保原始数据被正确修改；
* 触发UI刷新：通知所有依赖此变量的组件重新渲染。

开发者可以通过[getTarget接口](arkts-new-gettarget.md)获取原始对象，并使用下面的方法可以判断对象是否被状态管理包装。当表达式结果为false时，表示value是状态管理包装过的对象；否则，表示value不是状态管理包装过的对象。

```
1. UIUtils.getTarget(value) === value
```

## 类的构造函数中通过捕获this修改变量无法观察

当在构造函数中初始化修改success的[箭头函数](introduction-to-arkts.md#箭头函数又名lambda函数)时，TestModel实例尚未被代理封装，this指向TestModel实例本身。因此，后续触发query事件时，状态管理无法观测到变化。

当开发者将修改success的箭头函数放在query中时，已完成TestModel对象初始化和代理封装。通过this.viewModel.query()调用query时，query函数中的this指向viewModel代理对象，对代理对象成员属性isSuccess的更改能够被观测到，因此触发query事件可以被状态管理观测到变化。

【反例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State viewModel: TestModel = new TestModel();

8. build() {
9. Row() {
10. Column() {
11. Text(this.viewModel.isSuccess ? 'success' : 'failed')
12. .fontSize(50)
13. .fontWeight(FontWeight.Bold)
14. .onClick(() => {
15. this.viewModel.query();
16. })
17. }.width('100%')
18. }.height('100%')
19. }
20. }

22. export class TestModel {
23. public isSuccess: boolean = false;
24. public model: Model

26. constructor() {
27. this.model = new Model(() => {
28. this.isSuccess = true;
29. hilog.info(0xFF00, 'testTag', '%{public}s', `this.isSuccess: ${this.isSuccess}`);
30. })
31. }

33. query() {
34. this.model.query();
35. }
36. }

38. export class Model {
39. public callback: () => void

41. constructor(cb: () => void) {
42. this.callback = cb;
43. }

45. query() {
46. this.callback();
47. }
48. }
```

[StateProblemThisUnableObserveOpposite.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemThisUnableObserveOpposite.ets#L15-L64)

上述示例代码中，状态变量的修改在构造函数内。界面刚开始时显示“failed”，点击后日志打印“this.isSuccess: true”，表明修改成功，但界面仍然显示“failed”，这说明UI未刷新。

【正例】

```
1. @Entry
2. @Component
3. struct Index {
4. @State viewModel: TestModel = new TestModel();

6. build() {
7. Row() {
8. Column() {
9. Text(this.viewModel.isSuccess ? 'success' : 'failed')
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. .onClick(() => {
13. this.viewModel.query();
14. })
15. }.width('100%')
16. }.height('100%')
17. }
18. }

20. export class TestModel {
21. public isSuccess: boolean = false;
22. public model: Model = new Model(() => {
23. })

25. query() {
26. this.model.callback = () => {
27. this.isSuccess = true;
28. }
29. this.model.query();
30. }
31. }

33. export class Model {
34. public callback: () => void

36. constructor(cb: () => void) {
37. this.callback = cb;
38. }

40. query() {
41. this.callback();
42. }
43. }
```

[StateProblemThisUnableObservePositive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/StateProblemThisUnableObservePositive.ets#L16-L60)

上文示例代码将状态变量的修改放在类的普通方法中，界面开始时显示“failed”，点击后显示“success”。

## 使用箭头函数改变状态变量未生效

在箭头函数中改变状态变量不会触发UI刷新，这是因为箭头函数体内的this对象是定义该函数时所在的作用域指向的对象，而不是调用时所在的作用域指向的对象。所以在该场景下，changeCoverUrl的this指向PlayDetailViewModel，而不是状态变量本身。

【反例】

```
1. export default class PlayDetailViewModel {
2. public coverUrl: string = '#00ff00';
3. public changeCoverUrl = () => {
4. this.coverUrl = '#00F5FF';
5. }
6. }
```

[PlayDetailViewModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/playDetailPageOpposite/PlayDetailViewModel.ets#L17-L24)

```
1. import PlayDetailViewModel from './PlayDetailViewModel';

3. @Entry
4. @Component
5. struct PlayDetailPage {
6. @State vm: PlayDetailViewModel = new PlayDetailViewModel();

8. build() {
9. Stack() {
10. Text(this.vm.coverUrl)
11. .width(100)
12. .height(100)
13. .backgroundColor(this.vm.coverUrl)
14. Row() {
15. Button('Change Color')
16. .onClick(() => {
17. this.vm.changeCoverUrl();
18. })
19. }
20. }
21. .width('100%')
22. .height('100%')
23. .alignContent(Alignment.Top)
24. }
25. }
```

[PlayDetailPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/playDetailPageOpposite/PlayDetailPage.ets#L16-L42)

解决方案：将状态变量的代理对象传入箭头函数，调用代理的属性赋值。

【正例】

```
1. export default class PlayDetailViewModel {
2. public coverUrl: string = '#00ff00';
3. public changeCoverUrl = (model: PlayDetailViewModel) => {
4. model.coverUrl = '#00F5FF';
5. }
6. }
```

[PlayDetailViewModel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/playDetailPagePositive/PlayDetailViewModel.ets#L17-L24)

```
1. import PlayDetailViewModel from './PlayDetailViewModel';

3. @Entry
4. @Component
5. struct PlayDetailPage {
6. @State vm: PlayDetailViewModel = new PlayDetailViewModel();

8. build() {
9. Stack() {
10. Text(this.vm.coverUrl)
11. .width(100)
12. .height(100)
13. .backgroundColor(this.vm.coverUrl)
14. Row() {
15. Button('Change Color')
16. .onClick(() => {
17. let self = this.vm;
18. this.vm.changeCoverUrl(self);
19. })
20. }
21. }
22. .width('100%')
23. .height('100%')
24. .alignContent(Alignment.Top)
25. }
26. }
```

[PlayDetailPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ParadigmStateManagement/entry/src/main/ets/pages/state/playDetailPagePositive/PlayDetailPage.ets#L16-L43)

## 冗余刷新

### 使用简单属性数组导致冗余刷新

在开发过程中，我们经常会需要设置多个组件的同一种属性，比如Text组件的内容、组件的宽度、高度等样式信息等。将这些属性保存在一个数组中，配合[ForEach](arkts-rendering-control-foreach.md)进行使用是一种简单且方便的方法。但这种使用方式会导致属性元素的冗余刷新，修改数组中一个属性元素，数组中所有元素绑定的组件都会被刷新。

【反例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Entry
7. @Component
8. struct Index {
9. @State items: string[] = [];
10. @State ids: string[] = [];
11. @State age: number[] = [];
12. @State gender: string[] = [];

14. aboutToAppear() {
15. this.items.push('Head');
16. this.items.push('List');
17. for (let i = 0; i < 20; i++) {
18. this.ids.push('id: ' + Math.floor(Math.random() * 1000));
19. this.age.push(Math.floor(Math.random() * 100 % 40));
20. this.gender.push(Math.floor(Math.random() * 100) % 2 == 0 ? 'Male' : 'Female');
21. }
22. }

24. isRenderText(index: number): number {
25. hilog.info(DOMAIN_NUMBER, TAG, `index ${index} is rendered`);
26. return 1;
27. }

29. build() {
30. Row() {
31. Column() {
32. ForEach(this.items, (item: string) => {
33. if (item == 'Head') {
34. Text('Personal Info')
35. .fontSize(40)
36. } else if (item == 'List') {
37. List() {
38. ForEach(this.ids, (id: string, index) => {
39. ListItem() {
40. Row() {
41. Text(id)
42. .fontSize(20)
43. .margin({
44. left: 30,
45. right: 5
46. })
47. Text('age: ' + this.age[index as number])
48. .fontSize(20)
49. .margin({
50. left: 5,
51. right: 5
52. })
53. .position({ x: 100 })
54. .opacity(this.isRenderText(index))
55. .onClick(() => {
56. this.age[index]++;
57. })
58. Text('gender: ' + this.gender[index as number])
59. .margin({
60. left: 5,
61. right: 5
62. })
63. .position({ x: 180 })
64. .fontSize(20)
65. }
66. }
67. .margin({
68. top: 5,
69. bottom: 5
70. })
71. })
72. }
73. }
74. })
75. }
76. }
77. }
78. }
```

[StateArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArray.ets#L15-L94)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/uJ00CpxTQeil3prZ7F1tcA/zh-cn_image_0000002552957636.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=EE325DABADD00D382E5E07EB64EDE0DDF0EFCAAB36D61C3A0D6D459B09571946)

页面内通过ForEach显示了20条信息，当点击某一条信息中age的Text组件时，可以通过日志发现其他的19条信息中age的Text组件也进行了刷新(这体现在日志上，所有的age的Text组件都打出了日志)，但实际上其他19条信息的age的数值并没有改变，也就是说其他19个Text组件并不需要刷新。

这是因为当前状态管理的一个特性。假设存在一个被[@State](arkts-state.md)修饰的number类型的数组Num[]，其中有20个元素，值分别为0到19。这20个元素分别绑定了一个Text组件，当改变其中一个元素，例如第0号元素的值从0改成1，除了0号元素绑定的Text组件会刷新之外，其他的19个Text组件也会刷新，即使1到19号元素的值并没有改变。

这个特性普遍的出现在简单类型数组的场景中，当数组中的元素够多时，会对UI的刷新性能有很大的负面影响。这种“不需要刷新的组件被刷新”的现象即是“冗余刷新”，当“冗余刷新”的节点过多时，UI的刷新效率会大幅度降低，因此需要减少“冗余刷新”，也就是做到**精准控制组件的更新范围**。

为了减少由简单的属性相关的数组引起的“冗余刷新”，需要将属性数组转变为对象数组，配合自定义组件，实现精准控制更新范围。

【正例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class InfoList extends Array<Info> {
8. };

10. @Observed
11. class Info {
12. public ids: number;
13. public age: number;
14. public gender: string;

16. constructor() {
17. this.ids = Math.floor(Math.random() * 1000);
18. this.age = Math.floor(Math.random() * 100 % 40);
19. this.gender = Math.floor(Math.random() * 100) % 2 == 0 ? 'Male' : 'Female';
20. }
21. }

23. @Component
24. struct Information {
25. @ObjectLink info: Info;
26. @State index: number = 0;

28. isRenderText(index: number): number {
29. hilog.info(DOMAIN_NUMBER, TAG, `index ${index} is rendered`);
30. return 1;
31. }

33. build() {
34. Row() {
35. Text('id: ' + this.info.ids)
36. .fontSize(20)
37. .margin({
38. left: 30,
39. right: 5
40. })
41. Text('age: ' + this.info.age)
42. .fontSize(20)
43. .margin({
44. left: 5,
45. right: 5
46. })
47. .position({ x: 100 })
48. .opacity(this.isRenderText(this.index))
49. .onClick(() => {
50. this.info.age++;
51. })
52. Text('gender: ' + this.info.gender)
53. .margin({
54. left: 5,
55. right: 5
56. })
57. .position({ x: 180 })
58. .fontSize(20)
59. }
60. }
61. }

63. @Entry
64. @Component
65. struct Page {
66. @State infoList: InfoList = new InfoList();
67. @State items: string[] = [];

69. aboutToAppear() {
70. this.items.push('Head');
71. this.items.push('List');
72. for (let i = 0; i < 20; i++) {
73. this.infoList.push(new Info()); // 使用对象数组代替了原有的多个属性数组
74. }
75. }

77. build() {
78. Row() {
79. Column() {
80. ForEach(this.items, (item: string) => {
81. if (item == 'Head') {
82. Text('Personal Info')
83. .fontSize(40)
84. } else if (item == 'List') {
85. List() {
86. ForEach(this.infoList, (info: Info, index) => {
87. ListItem() {
88. Information({
89. info: info,
90. index: index
91. })
92. }
93. .margin({
94. top: 5,
95. bottom: 5
96. })
97. })
98. }
99. }
100. })
101. }
102. }
103. }
104. }
```

[StateArrayUpdate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayUpdate.ets#L15-L120)

上述代码的运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/b4tntfvaSXu_qVhA2C7gYQ/zh-cn_image_0000002583477637.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=17CE5CE98A72331F4309C117CEA8D93F01DEF1DC00EDADA11C64F4582EE00440)

修改后的代码使用对象数组代替了原有的多个属性数组，能够避免数组的“冗余刷新”的情况。这是因为对于数组来说，对象内的变化是无法感知的，数组只能观测数组项层级的变化，例如新增数据项，修改数据项（普通数组是直接修改数据项的值，在对象数组的场景下是整个对象被重新赋值，改变某个数据项对象中的属性不会被观测到）、删除数据项等。这意味着当改变对象内的某个属性时，对于数组来说，对象是没有变化的，也就不会去刷新。在当前状态管理的观测能力中，除了数组嵌套对象的场景外，对象嵌套对象的场景也是无法观测到变化的，这一部分内容将在[使用多属性类对象导致冗余刷新](arkts-state-management-faq-inner-class.md#使用多属性类对象导致冗余刷新)中讲到。同时修改代码时使用了自定义组件与ForEach的结合，这一部分内容将在[ForEach和对象数组结合使用导致UI不刷新](arkts-state-management-faq-inner-component.md#foreach和对象数组结合使用导致ui不刷新)讲到。

### 使用多属性类对象导致冗余刷新

说明

从API version 11开始，推荐优先使用[@Track装饰器](arkts-track.md)解决该场景的问题。

在开发过程中，我们有时会定义一个大的对象，其中包含了很多样式相关的属性，并且在父子组件间传递这个对象，将其中的属性绑定在组件上。这种使用方式会导致类属性的冗余刷新，修改一个类属性，类内所有属性绑定的组件都会被刷新。

【反例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class UiStyle {
8. public translateX: number = 0;
9. public translateY: number = 0;
10. public scaleX: number = 0.3;
11. public scaleY: number = 0.3;
12. public width: number = 336;
13. public height: number = 178;
14. public posX: number = 10;
15. public posY: number = 50;
16. public alpha: number = 0.5;
17. public borderRadius: number = 24;
18. public imageWidth: number = 78;
19. public imageHeight: number = 78;
20. public translateImageX: number = 0;
21. public translateImageY: number = 0;
22. public fontSize: number = 20;
23. }

25. @Component
26. struct SpecialImage {
27. @ObjectLink uiStyle: UiStyle;

29. private isRenderSpecialImage(): number { // 显示组件是否渲染的函数
30. hilog.info(DOMAIN_NUMBER, TAG, 'SpecialImage is rendered');
31. return 1;
32. }

34. build() {
35. Image($r('app.media.icon')) // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
36. .width(this.uiStyle.imageWidth)
37. .height(this.uiStyle.imageHeight)
38. .margin({ top: 20 })
39. .translate({
40. x: this.uiStyle.translateImageX,
41. y: this.uiStyle.translateImageY
42. })
43. .opacity(this.isRenderSpecialImage()) // 如果Image重新渲染，该函数将被调用
44. }
45. }

47. @Component
48. struct PageChild {
49. @ObjectLink uiStyle: UiStyle;

51. // 下面的函数用于显示组件是否被渲染
52. private isRenderColumn(): number {
53. hilog.info(DOMAIN_NUMBER, TAG, 'Column is rendered');
54. return 1;
55. }

57. private isRenderStack(): number {
58. hilog.info(DOMAIN_NUMBER, TAG, 'Stack is rendered');
59. return 1;
60. }

62. private isRenderImage(): number {
63. hilog.info(DOMAIN_NUMBER, TAG, 'Image is rendered');
64. return 1;
65. }

67. private isRenderText(): number {
68. hilog.info(DOMAIN_NUMBER, TAG, 'Text is rendered');
69. return 1;
70. }

72. build() {
73. Column() {
74. SpecialImage({
75. uiStyle: this.uiStyle
76. })
77. Stack() {
78. Column() {
79. Image($r('app.media.icon')) // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
80. .opacity(this.uiStyle.alpha)
81. .scale({
82. x: this.uiStyle.scaleX,
83. y: this.uiStyle.scaleY
84. })
85. .padding(this.isRenderImage())
86. .width(300)
87. .height(300)
88. }
89. .width('100%')
90. .position({ y: -80 })

92. Stack() {
93. Text('Hello World')
94. .fontColor('#182431')
95. .fontWeight(FontWeight.Medium)
96. .fontSize(this.uiStyle.fontSize)
97. .opacity(this.isRenderText())
98. .margin({ top: 12 })
99. }
100. .opacity(this.isRenderStack())
101. .position({
102. x: this.uiStyle.posX,
103. y: this.uiStyle.posY
104. })
105. .width('100%')
106. .height('100%')
107. }
108. .margin({ top: 50 })
109. .borderRadius(this.uiStyle.borderRadius)
110. .opacity(this.isRenderStack())
111. .backgroundColor('#FFFFFF')
112. .width(this.uiStyle.width)
113. .height(this.uiStyle.height)
114. .translate({
115. x: this.uiStyle.translateX,
116. y: this.uiStyle.translateY
117. })

119. Column() {
120. Button('Move')
121. .width(312)
122. .fontSize(20)
123. .backgroundColor('#FF007DFF')
124. .margin({ bottom: 10 })
125. .onClick(() => {
126. this.getUIContext().animateTo({
127. duration: 500
128. }, () => {
129. this.uiStyle.translateY = (this.uiStyle.translateY + 180) % 250;
130. });
131. })
132. Button('Scale')
133. .borderRadius(20)
134. .backgroundColor('#FF007DFF')
135. .fontSize(20)
136. .width(312)
137. .onClick(() => {
138. this.uiStyle.scaleX = (this.uiStyle.scaleX + 0.6) % 0.8;
139. })
140. }
141. .position({
142. y: 666
143. })
144. .height('100%')
145. .width('100%')

147. }
148. .opacity(this.isRenderColumn())
149. .width('100%')
150. .height('100%')

152. }
153. }

155. @Entry
156. @Component
157. struct Page {
158. @State uiStyle: UiStyle = new UiStyle();

160. build() {
161. Stack() {
162. PageChild({
163. uiStyle: this.uiStyle
164. })
165. }
166. .backgroundColor('#F1F3F5')
167. }
168. }
```

[StateArrayBig.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayBig.ets#L15-L184)

上述代码的运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/llRGdclPTWOtlm_hiqoN1g/zh-cn_image_0000002552797988.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=9F5BCBEFC8109231003E94810CF44BC7D2834AAB31E70D8C470170746071153A)

优化前点击move按钮的脏节点更新[耗时](ui-inspector-profiler.md#trace调试能力)如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/gnqZNU2rSrSks1yLi1M1jw/zh-cn_image_0000002583437683.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=2591DA4F7F2D7035EC5FCDD151722FA046F0E275DC3785D4F78D7438ECEC7CEF)

在上面的示例中，UiStyle定义了多个属性，并且这些属性分别被多个组件关联。当点击任意一个按钮更改其中的某些属性时，会导致所有这些关联uiStyle的组件进行刷新，虽然它们其实并不需要进行刷新（因为组件的属性都没有改变）。通过定义的一系列isRender函数，可以观察到这些组件的刷新。当点击“move”按钮进行平移动画时，由于translateY的值的多次改变，会导致每一次都存在“冗余刷新”的问题，这对应用的性能有着很大的负面影响。

这是因为当前状态管理的一个刷新机制，假设定义了一个有20个属性的类，创建类的对象实例，将20个属性绑定到组件上，这时修改其中的某个属性，除了这个属性关联的组件会刷新之外，其他的19个属性关联的组件也都会刷新，即使这些属性本身并没有发生变化。

这个机制会导致在使用一个复杂大对象与多个组件关联时，刷新性能的下降。对此，推荐将一个复杂大对象拆分成多个小对象的集合，在保留原有代码结构的基础上，减少“冗余刷新”，实现精准控制组件的更新范围。

【正例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class NeedRenderImage { // 在同一组件中使用的属性可以划分为相同的类
8. public translateImageX: number = 0;
9. public translateImageY: number = 0;
10. public imageWidth: number = 78;
11. public imageHeight: number = 78;
12. }

14. @Observed
15. class NeedRenderScale { // 在一起使用的属性可以划分为相同的类
16. public scaleX: number = 0.3;
17. public scaleY: number = 0.3;
18. }

20. @Observed
21. class NeedRenderAlpha { // 在不同地方使用的属性可以划分为相同的类
22. public alpha: number = 0.5;
23. }

25. @Observed
26. class NeedRenderSize { // 在一起使用的属性可以划分为相同的类
27. public width: number = 336;
28. public height: number = 178;
29. }

31. @Observed
32. class NeedRenderPos { // 在一起使用的属性可以划分为相同的类
33. public posX: number = 10;
34. public posY: number = 50;
35. }

37. @Observed
38. class NeedRenderBorderRadius { // 在不同地方使用的属性可以划分为相同的类
39. public borderRadius: number = 24;
40. }

42. @Observed
43. class NeedRenderFontSize { // 在不同地方使用的属性可以划分为相同的类
44. public fontSize: number = 20;
45. }

47. @Observed
48. class NeedRenderTranslate { // 在一起使用的属性可以划分为相同的类
49. public translateX: number = 0;
50. public translateY: number = 0;
51. }

53. @Observed
54. class UiStyle {
55. // 使用NeedRenderxxx类
56. public needRenderTranslate: NeedRenderTranslate = new NeedRenderTranslate();
57. public needRenderFontSize: NeedRenderFontSize = new NeedRenderFontSize();
58. public needRenderBorderRadius: NeedRenderBorderRadius = new NeedRenderBorderRadius();
59. public needRenderPos: NeedRenderPos = new NeedRenderPos();
60. public needRenderSize: NeedRenderSize = new NeedRenderSize();
61. public needRenderAlpha: NeedRenderAlpha = new NeedRenderAlpha();
62. public needRenderScale: NeedRenderScale = new NeedRenderScale();
63. public needRenderImage: NeedRenderImage = new NeedRenderImage();
64. }

66. @Component
67. struct SpecialImage {
68. @ObjectLink uiStyle: UiStyle;
69. @ObjectLink needRenderImage: NeedRenderImage; // 从其父组件接收新类

71. private isRenderSpecialImage(): number { // 显示组件是否渲染的函数
72. hilog.info(DOMAIN_NUMBER, TAG, 'SpecialImage is rendered');
73. return 1;
74. }

76. build() {
77. Image($r('app.media.icon')) // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
78. .width(this.needRenderImage.imageWidth) // 使用this.needRenderImage.xxx
79. .height(this.needRenderImage.imageHeight)
80. .margin({ top: 20 })
81. .translate({
82. x: this.needRenderImage.translateImageX,
83. y: this.needRenderImage.translateImageY
84. })
85. .opacity(this.isRenderSpecialImage()) // 如果Image重新渲染，该函数将被调用
86. }
87. }

89. @Component
90. struct PageChild {
91. @ObjectLink uiStyle: UiStyle;
92. @ObjectLink needRenderTranslate: NeedRenderTranslate; // 从其父组件接收新定义的NeedRenderxxx类的实例
93. @ObjectLink needRenderFontSize: NeedRenderFontSize;
94. @ObjectLink needRenderBorderRadius: NeedRenderBorderRadius;
95. @ObjectLink needRenderPos: NeedRenderPos;
96. @ObjectLink needRenderSize: NeedRenderSize;
97. @ObjectLink needRenderAlpha: NeedRenderAlpha;
98. @ObjectLink needRenderScale: NeedRenderScale;

100. // 下面的函数用于显示组件是否被渲染
101. private isRenderColumn(): number {
102. hilog.info(DOMAIN_NUMBER, TAG, 'Column is rendered');
103. return 1;
104. }

106. private isRenderStack(): number {
107. hilog.info(DOMAIN_NUMBER, TAG, 'Stack is rendered');
108. return 1;
109. }

111. private isRenderImage(): number {
112. hilog.info(DOMAIN_NUMBER, TAG, 'Image is rendered');
113. return 1;
114. }

116. private isRenderText(): number {
117. hilog.info(DOMAIN_NUMBER, TAG, 'Text is rendered');
118. return 1;
119. }

121. build() {
122. Column() {
123. SpecialImage({
124. uiStyle: this.uiStyle,
125. needRenderImage: this.uiStyle.needRenderImage // 传递给子组件
126. })
127. Stack() {
128. Column() {
129. Image($r('app.media.icon')) // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
130. .opacity(this.needRenderAlpha.alpha)
131. .scale({
132. x: this.needRenderScale.scaleX, // 使用this.needRenderXxx.xxx
133. y: this.needRenderScale.scaleY
134. })
135. .padding(this.isRenderImage())
136. .width(300)
137. .height(300)
138. }
139. .width('100%')
140. .position({ y: -80 })

142. Stack() {
143. Text('Hello World')
144. .fontColor('#182431')
145. .fontWeight(FontWeight.Medium)
146. .fontSize(this.needRenderFontSize.fontSize)
147. .opacity(this.isRenderText())
148. .margin({ top: 12 })
149. }
150. .opacity(this.isRenderStack())
151. .position({
152. x: this.needRenderPos.posX,
153. y: this.needRenderPos.posY
154. })
155. .width('100%')
156. .height('100%')
157. }
158. .margin({ top: 50 })
159. .borderRadius(this.needRenderBorderRadius.borderRadius)
160. .opacity(this.isRenderStack())
161. .backgroundColor('#FFFFFF')
162. .width(this.needRenderSize.width)
163. .height(this.needRenderSize.height)
164. .translate({
165. x: this.needRenderTranslate.translateX,
166. y: this.needRenderTranslate.translateY
167. })

169. Column() {
170. Button('Move')
171. .width(312)
172. .fontSize(20)
173. .backgroundColor('#FF007DFF')
174. .margin({ bottom: 10 })
175. .onClick(() => {
176. this.getUIContext().animateTo({
177. duration: 500
178. }, () => {
179. this.needRenderTranslate.translateY = (this.needRenderTranslate.translateY + 180) % 250;
180. });
181. })
182. Button('Scale')
183. .borderRadius(20)
184. .backgroundColor('#FF007DFF')
185. .fontSize(20)
186. .width(312)
187. .margin({ bottom: 10 })
188. .onClick(() => {
189. this.needRenderScale.scaleX = (this.needRenderScale.scaleX + 0.6) % 0.8;
190. })
191. Button('Change Image')
192. .borderRadius(20)
193. .backgroundColor('#FF007DFF')
194. .fontSize(20)
195. .width(312)
196. .onClick(() => { // 在父组件中，仍使用 this.uiStyle.endRenderXxx.xxx 更改属性
197. this.uiStyle.needRenderImage.imageWidth = (this.uiStyle.needRenderImage.imageWidth + 30) % 160;
198. this.uiStyle.needRenderImage.imageHeight = (this.uiStyle.needRenderImage.imageHeight + 30) % 160;
199. })
200. }
201. .position({
202. y: 616
203. })
204. .height('100%')
205. .width('100%')
206. }
207. .opacity(this.isRenderColumn())
208. .width('100%')
209. .height('100%')
210. }
211. }

213. @Entry
214. @Component
215. struct Page {
216. @State uiStyle: UiStyle = new UiStyle();

218. build() {
219. Stack() {
220. PageChild({
221. uiStyle: this.uiStyle,
222. needRenderTranslate: this.uiStyle.needRenderTranslate, // 传递needRenderxxx类给子组件
223. needRenderFontSize: this.uiStyle.needRenderFontSize,
224. needRenderBorderRadius: this.uiStyle.needRenderBorderRadius,
225. needRenderPos: this.uiStyle.needRenderPos,
226. needRenderSize: this.uiStyle.needRenderSize,
227. needRenderAlpha: this.uiStyle.needRenderAlpha,
228. needRenderScale: this.uiStyle.needRenderScale
229. })
230. }
231. .backgroundColor('#F1F3F5')
232. }
233. }
```

[StateArrayPrecise.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayPrecise.ets#L15-L249)

上述代码的运行效果如下。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/pkv9vixHT8avE4MHUjcWtg/zh-cn_image_0000002552957638.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=BC8A21AFFFA027AE63A8C0BD68B07FCBC7DC573CBF717737ED79B409F66F68F5)

优化后点击move按钮的脏节点更新耗时如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/Ggc-LAs5Q_O4r-R3ymnzhg/zh-cn_image_0000002583477639.png?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=304EDEC6957AC7F883F88ECCD4AFF6EAAF88AD2E5A9664D869B62EF12AA4E506)

修改后的代码将原来的大类中的十五个属性拆成了八个小类，并且在绑定的组件上也做了相应的适配。属性拆分遵循以下几点原则：

* 只作用在同一个组件上的多个属性可以被拆分进同一个新类，即示例中的NeedRenderImage。适用于组件经常被不关联的属性改变而引起刷新的场景，这个时候就要考虑拆分属性，或者重新考虑ViewModel设计是否合理。
* 经常被同时使用的属性可以被拆分进同一个新类，即示例中的NeedRenderScale、NeedRenderTranslate、NeedRenderPos、NeedRenderSize。适用于属性经常成对出现，或者被作用在同一个样式上的情况，例如.translate、.position、.scale等（这些样式通常会接收一个对象作为参数）。
* 可能被用在多个组件上或相对较独立的属性应该被单独拆分进一个新类，即示例中的NeedRenderAlpha，NeedRenderBorderRadius、NeedRenderFontSize。适用于一个属性作用在多个组件上或者与其他属性没有联系的情况，例如.opacity、.borderRadius等（这些样式通常相对独立）。

属性拆分的原理和属性合并类似，都是在嵌套场景下，状态管理无法观测二层以上的属性变化，所以不会因为二层的数据变化导致一层关联的其他属性被刷新，同时利用[@Observed](arkts-observed-and-objectlink.md)和[@ObjectLink](arkts-observed-and-objectlink.md)在父子节点间传递二层的对象，从而在子组件中正常的观测二层的数据变化，实现精准刷新。

[@Track](arkts-track.md)是类属性装饰器。当一个类对象是状态变量时，@Track装饰的属性发生变化，只会触发该属性关联的UI更新，所以使用@Track装饰器则无需做属性拆分，也能达到同样控制组件更新范围的作用。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class UiStyle {
8. @Track public translateX: number = 0;
9. @Track public translateY: number = 0;
10. @Track public scaleX: number = 0.3;
11. @Track public scaleY: number = 0.3;
12. @Track public width: number = 336;
13. @Track public height: number = 178;
14. @Track public posX: number = 10;
15. @Track public posY: number = 50;
16. @Track public alpha: number = 0.5;
17. @Track public borderRadius: number = 24;
18. @Track public imageWidth: number = 78;
19. @Track public imageHeight: number = 78;
20. @Track public translateImageX: number = 0;
21. @Track public translateImageY: number = 0;
22. @Track public fontSize: number = 20;
23. }

25. @Component
26. struct SpecialImage {
27. @ObjectLink uiStyle: UiStyle;

29. private isRenderSpecialImage(): number { // 显示组件是否渲染的函数
30. hilog.info(DOMAIN_NUMBER, TAG, 'SpecialImage is rendered');
31. return 1;
32. }

34. build() {
35. Image($r('app.media.icon')) // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
36. .width(this.uiStyle.imageWidth)
37. .height(this.uiStyle.imageHeight)
38. .margin({ top: 20 })
39. .translate({
40. x: this.uiStyle.translateImageX,
41. y: this.uiStyle.translateImageY
42. })
43. .opacity(this.isRenderSpecialImage()) // 如果Image重新渲染，该函数将被调用
44. }
45. }

47. @Component
48. struct PageChild {
49. @ObjectLink uiStyle: UiStyle;

51. // 下面的函数用于显示组件是否被渲染
52. private isRenderColumn(): number {
53. hilog.info(DOMAIN_NUMBER, TAG, 'Column is rendered');
54. return 1;
55. }

57. private isRenderStack(): number {
58. hilog.info(DOMAIN_NUMBER, TAG, 'Stack is rendered');
59. return 1;
60. }

62. private isRenderImage(): number {
63. hilog.info(DOMAIN_NUMBER, TAG, 'Image is rendered');
64. return 1;
65. }

67. private isRenderText(): number {
68. hilog.info(DOMAIN_NUMBER, TAG, 'Text is rendered');
69. return 1;
70. }

72. build() {
73. Column() {
74. SpecialImage({
75. uiStyle: this.uiStyle
76. })
77. Stack() {
78. Column() {
79. Image($r('app.media.icon')) // 此处'app.media.icon'仅作示例，请开发者自行替换，否则imageSource创建失败会导致后续无法正常执行。
80. .opacity(this.uiStyle.alpha)
81. .scale({
82. x: this.uiStyle.scaleX,
83. y: this.uiStyle.scaleY
84. })
85. .padding(this.isRenderImage())
86. .width(300)
87. .height(300)
88. }
89. .width('100%')
90. .position({ y: -80 })

92. Stack() {
93. Text('Hello World')
94. .fontColor('#182431')
95. .fontWeight(FontWeight.Medium)
96. .fontSize(this.uiStyle.fontSize)
97. .opacity(this.isRenderText())
98. .margin({ top: 12 })
99. }
100. .opacity(this.isRenderStack())
101. .position({
102. x: this.uiStyle.posX,
103. y: this.uiStyle.posY
104. })
105. .width('100%')
106. .height('100%')
107. }
108. .margin({ top: 50 })
109. .borderRadius(this.uiStyle.borderRadius)
110. .opacity(this.isRenderStack())
111. .backgroundColor('#FFFFFF')
112. .width(this.uiStyle.width)
113. .height(this.uiStyle.height)
114. .translate({
115. x: this.uiStyle.translateX,
116. y: this.uiStyle.translateY
117. })

119. Column() {
120. Button('Move')
121. .width(312)
122. .fontSize(20)
123. .backgroundColor('#FF007DFF')
124. .margin({ bottom: 10 })
125. .onClick(() => {
126. this.getUIContext().animateTo({
127. duration: 500
128. }, () => {
129. this.uiStyle.translateY = (this.uiStyle.translateY + 180) % 250;
130. });
131. })
132. Button('Scale')
133. .borderRadius(20)
134. .backgroundColor('#FF007DFF')
135. .fontSize(20)
136. .width(312)
137. .onClick(() => {
138. this.uiStyle.scaleX = (this.uiStyle.scaleX + 0.6) % 0.8;
139. })
140. }
141. .position({
142. y: 666
143. })
144. .height('100%')
145. .width('100%')

147. }
148. .opacity(this.isRenderColumn())
149. .width('100%')
150. .height('100%')

152. }
153. }

155. @Entry
156. @Component
157. struct Page {
158. @State uiStyle: UiStyle = new UiStyle();

160. build() {
161. Stack() {
162. PageChild({
163. uiStyle: this.uiStyle
164. })
165. }
166. .backgroundColor('#F1F3F5')
167. }
168. }
```

[StateArrayTrack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayTrack.ets#L15-L184)

## 数据重置导致UI不刷新

在开发过程中，会有“重置数据”的场景，将一个新创建的对象赋值给原有的状态变量，实现数据的刷新。如果不注意新创建对象的类型，可能会出现UI不刷新的现象。

【反例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class Child {
8. public count: number;

10. constructor(count: number) {
11. this.count = count;
12. }
13. }

15. @Observed
16. class ChildList extends Array<Child> {
17. }

19. @Observed
20. class Ancestor {
21. public childList: ChildList;

23. constructor(childList: ChildList) {
24. this.childList = childList;
25. }

27. public loadData() {
28. let tempList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
29. this.childList = tempList;
30. }

32. public clearData() {
33. this.childList = [];
34. }
35. }

37. @Component
38. struct CompChild {
39. @Link childList: ChildList;
40. @ObjectLink child: Child;

42. build() {
43. Row() {
44. Text(this.child.count + '')
45. .height(70)
46. .fontSize(20)
47. .borderRadius({
48. topLeft: 6,
49. topRight: 6
50. })
51. .margin({ left: 50 })
52. Button('X')
53. .backgroundColor(Color.Red)
54. .onClick(() => {
55. let index = this.childList.findIndex((item) => {
56. return item.count === this.child.count;
57. });
58. if (index !== -1) {
59. this.childList.splice(index, 1);
60. }
61. })
62. .margin({
63. left: 200,
64. right: 30
65. })
66. }
67. .margin({
68. top: 15,
69. left: 15,
70. right: 10,
71. bottom: 15
72. })
73. .borderRadius(6)
74. .backgroundColor(Color.Grey)
75. }
76. }

78. @Component
79. struct CompList {
80. @ObjectLink @Watch('changeChildList') childList: ChildList;

82. changeChildList() {
83. hilog.info(DOMAIN_NUMBER, TAG, 'CompList ChildList change');
84. }

86. isRenderCompChild(index: number): number {
87. hilog.info(DOMAIN_NUMBER, TAG, 'Comp Child is render' + index);
88. return 1;
89. }

91. build() {
92. Column() {
93. List() {
94. ForEach(this.childList, (item: Child, index) => {
95. ListItem() {
96. CompChild({
97. childList: this.childList,
98. child: item
99. })
100. .opacity(this.isRenderCompChild(index))
101. }
102. })
103. }
104. .height('70%')
105. }
106. }
107. }

109. @Component
110. struct CompAncestor {
111. @ObjectLink ancestor: Ancestor;

113. build() {
114. Column() {
115. CompList({ childList: this.ancestor.childList })
116. Row() {
117. Button('Clear')
118. .onClick(() => {
119. this.ancestor.clearData();
120. })
121. .width(100)
122. .margin({ right: 50 })
123. Button('Recover')
124. .onClick(() => {
125. this.ancestor.loadData();
126. })
127. .width(100)
128. }
129. }
130. }
131. }

133. @Entry
134. @Component
135. struct Page {
136. @State childList: ChildList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
137. @State ancestor: Ancestor = new Ancestor(this.childList);

139. build() {
140. Column() {
141. CompAncestor({ ancestor: this.ancestor })
142. }
143. }
144. }
```

[StateArrayObserved.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayObserved.ets#L15-L160)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/172rs0mjS8aGQADkQooiaQ/zh-cn_image_0000002552797990.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=2602B9BF2205D7FD299878234FE298A7D55FE1E3871C67333F7B4FECA9BA1325)

上述代码维护了一个ChildList类型的数据源，点击"X"按钮删除一些数据后再点击Recover进行恢复ChildList，发现再次点击"X"按钮进行删除时，UI并没有刷新，同时也没有打印出“CompList ChildList change”的日志。

代码中对数据源childList重新赋值时，是通过Ancestor对象的方法loadData。

```
1. public loadData() {
2. let tempList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
3. this.childList = tempList;
4. }
```

[StateArrayLoadDate.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayLoadDate.ets#L46-L51)

在loadData方法中，创建了一个临时的Child类型的数组tempList，并且将Ancestor对象的成员变量的childList指向了tempList。但是这里创建的Child[]类型的数组tempList其实并没有能被观测的能力（也就说它的变化无法主动触发UI刷新）。当它被赋值给childList之后，触发了ForEach的刷新，使得界面完成了重建，但是再次点击删除时，由于此时的childList已经指向了新的tempList代表的数组，并且这个数组并没有被观测的能力，是个静态的量，所以它的更改不会被观测到，也就不会引起UI的刷新。实际上这个时候childList里的数据已经减少了，只是UI没有刷新。

有些开发者会注意到，在Page中初始化定义childList的时候，也是以这样一种方法去进行初始化的。

```
1. @State childList: ChildList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
2. @State ancestor: Ancestor = new Ancestor(this.childList);
```

[StateArrayInit.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayInit.ets#L151-L154)

但是由于这里的childList实际上是被@State装饰了，根据当前状态管理的观测能力，尽管右边赋值的是一个Child[]类型的数据，它并没有被@Observed装饰，这里的childList却依然具备了被观测的能力，所以能够正常的触发UI的刷新。当去掉childList的@State的装饰器后，不去重置数据源，也无法通过点击“X”按钮触发刷新。

因此，需要将具有观测能力的类对象绑定组件，来确保当改变这些类对象的内容时，UI能够正常的刷新。

【正例】

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const DOMAIN_NUMBER: number = 0XFF00;
4. const TAG: string = '[Sample_StateManagement]';

6. @Observed
7. class Child {
8. public count: number;

10. constructor(count: number) {
11. this.count = count;
12. }
13. }

15. @Observed
16. class ChildList extends Array<Child> {
17. }

19. @Observed
20. class Ancestor {
21. public childList: ChildList;

23. constructor(childList: ChildList) {
24. this.childList = childList;
25. }

27. public loadData() {
28. let tempList = new ChildList();
29. for (let i = 1; i < 6; i++) {
30. tempList.push(new Child(i));
31. }
32. this.childList = tempList;
33. }

35. public clearData() {
36. this.childList = [];
37. }
38. }

40. @Component
41. struct CompChild {
42. @Link childList: ChildList;
43. @ObjectLink child: Child;

45. build() {
46. Row() {
47. Text(this.child.count + '')
48. .height(70)
49. .fontSize(20)
50. .borderRadius({
51. topLeft: 6,
52. topRight: 6
53. })
54. .margin({ left: 50 })
55. Button('X')
56. .backgroundColor(Color.Red)
57. .onClick(() => {
58. let index = this.childList.findIndex((item) => {
59. return item.count === this.child.count;
60. });
61. if (index !== -1) {
62. this.childList.splice(index, 1);
63. }
64. })
65. .margin({
66. left: 200,
67. right: 30
68. })
69. }
70. .margin({
71. top: 15,
72. left: 15,
73. right: 10,
74. bottom: 15
75. })
76. .borderRadius(6)
77. .backgroundColor(Color.Grey)
78. }
79. }

81. @Component
82. struct CompList {
83. @ObjectLink @Watch('changeChildList') childList: ChildList;

85. changeChildList() {
86. hilog.info(DOMAIN_NUMBER, TAG, 'CompList ChildList change');
87. }

89. isRenderCompChild(index: number): number {
90. hilog.info(DOMAIN_NUMBER, TAG, 'Comp Child is render' + index);
91. return 1;
92. }

94. build() {
95. Column() {
96. List() {
97. ForEach(this.childList, (item: Child, index) => {
98. ListItem() {
99. CompChild({
100. childList: this.childList,
101. child: item
102. })
103. .opacity(this.isRenderCompChild(index))
104. }
105. })
106. }
107. .height('70%')
108. }
109. }
110. }

112. @Component
113. struct CompAncestor {
114. @ObjectLink ancestor: Ancestor;

116. build() {
117. Column() {
118. CompList({ childList: this.ancestor.childList })
119. Row() {
120. Button('Clear')
121. .onClick(() => {
122. this.ancestor.clearData();
123. })
124. .width(100)
125. .margin({ right: 50 })
126. Button('Recover')
127. .onClick(() => {
128. this.ancestor.loadData();
129. })
130. .width(100)
131. }
132. }
133. }
134. }

136. @Entry
137. @Component
138. struct Page {
139. @State childList: ChildList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
140. @State ancestor: Ancestor = new Ancestor(this.childList);

142. build() {
143. Column() {
144. CompAncestor({ ancestor: this.ancestor })
145. }
146. }
147. }
```

[StateArrayNo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayNo.ets#L15-L163)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/r5EqReT-Qb2Qm-aCnsWg5A/zh-cn_image_0000002583437685.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233918Z&HW-CC-Expire=86400&HW-CC-Sign=0581608D3100A182A6E3794929B097ED6AF67A77B3471094C0DC5BC264050B6A)

核心的修改点是将原本Child[]类型的tempList修改为具有被观测能力的ChildList类。

```
1. public loadData() {
2. let tempList = new ChildList();
3. for (let i = 1; i < 6; i++) {
4. tempList.push(new Child(i));
5. }
6. this.childList = tempList;
7. }
```

[StateArrayNo2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayNo2.ets#L39-L47)

ChildList类型在定义的时候使用了@Observed进行装饰，所以用new创建的对象tempList具有被观测的能力，因此在点击“X”按钮删除其中一条内容时，变量childList就能够观测到变化，所以触发了ForEach的刷新，最终UI渲染刷新。
