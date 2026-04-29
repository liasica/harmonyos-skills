---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-faq-inner-class
title: 数据对象状态管理常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理常见问题 > 数据对象状态管理常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:33+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:f761055968302047f0495a74f6715891125645ef445cfe9fad591e28964df625
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
28. // 此时TestModel实例尚未被代理封装，this指向TestModel实例本身
29. // this.isSuccess的修改无法触发Index中Text的UI刷新
30. this.isSuccess = true;
31. hilog.info(0xFF00, 'testTag', '%{public}s', `this.isSuccess: ${this.isSuccess}`);
32. })
33. }

35. query() {
36. this.model.query();
37. }
38. }

40. export class Model {
41. public callback: () => void

43. constructor(cb: () => void) {
44. this.callback = cb;
45. }

47. query() {
48. this.callback();
49. }
50. }
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

25. // 状态变量的修改放在类的普通方法中
26. query() {
27. this.model.callback = () => {
28. this.isSuccess = true;
29. }
30. this.model.query();
31. }
32. }

34. export class Model {
35. public callback: () => void

37. constructor(cb: () => void) {
38. this.callback = cb;
39. }

41. query() {
42. this.callback();
43. }
44. }
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
25. // 日志打印，观察使用简单属性数组导致冗余刷新
26. hilog.info(DOMAIN_NUMBER, TAG, `index ${index} is rendered`);
27. return 1;
28. }

30. build() {
31. Row() {
32. Column() {
33. ForEach(this.items, (item: string) => {
34. if (item == 'Head') {
35. Text('Personal Info')
36. .fontSize(40)
37. } else if (item == 'List') {
38. List() {
39. ForEach(this.ids, (id: string, index) => {
40. ListItem() {
41. Row() {
42. Text(id)
43. .fontSize(20)
44. .margin({
45. left: 30,
46. right: 5
47. })
48. Text('age: ' + this.age[index as number])
49. .fontSize(20)
50. .margin({
51. left: 5,
52. right: 5
53. })
54. .position({ x: 100 })
55. .opacity(this.isRenderText(index))
56. .onClick(() => {
57. this.age[index]++;
58. })
59. Text('gender: ' + this.gender[index as number])
60. .margin({
61. left: 5,
62. right: 5
63. })
64. .position({ x: 180 })
65. .fontSize(20)
66. }
67. }
68. .margin({
69. top: 5,
70. bottom: 5
71. })
72. })
73. }
74. }
75. })
76. }
77. }
78. }
79. }
```

[StateArray.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArray.ets#L15-L94)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/qVsEzLFhQraZmz0xHMgixg/zh-cn_image_0000002589323995.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=48D182269027FF8782CAD634C6C1B7E67A3D60935513F9F405FD500D06534A5F)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/b1-1y0DjRuOySUwkkYCwyQ/zh-cn_image_0000002589243935.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=AE558D7C6ECA1DDF767F5999B47EDDC6AB94A371748FABDA8BC7D2B4C046E64B)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/h8bXlIVbRBqYXtaSt0Awtg/zh-cn_image_0000002558764128.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=07C17A2F19EB7B7A6A70DE9BD3A8116A4D6684B7FD5C0EFA86A670E09DCB36C2)

优化前点击move按钮的脏节点更新[耗时](ui-inspector-profiler.md#trace调试能力)如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/-Xy8QqbQTKaE0lWsJJyzog/zh-cn_image_0000002558604472.png?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=E9F9669A377C7E0B8E64A85B7C828AEC3BFFAD509D42B98F58F12D8B802E5881)

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

上述代码的运行效果如下。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/PwfECJgTR1-8nVlJ6RoYQQ/zh-cn_image_0000002589323997.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=209302A143F71BEC0E4C93543F1196A6F2071BECFD5FD604947801510DC5288E)

优化后点击move按钮的脏节点更新耗时如下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/blIjGmCSR-Ko80cEyCcpvA/zh-cn_image_0000002589243937.png?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=51A014DE2DB9B42CA9341068651083ACBD1DBFC8F6FB3055E9549F114B317EE6)

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
28. // 这里创建的Child[]类型的数组tempList并没有能被观测的能力
29. let tempList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
30. this.childList = tempList;
31. }

33. public clearData() {
34. this.childList = [];
35. }
36. }

38. @Component
39. struct CompChild {
40. @Link childList: ChildList;
41. @ObjectLink child: Child;

43. build() {
44. Row() {
45. Text(this.child.count + '')
46. .height(70)
47. .fontSize(20)
48. .borderRadius({
49. topLeft: 6,
50. topRight: 6
51. })
52. .margin({ left: 50 })
53. Button('X')
54. .backgroundColor(Color.Red)
55. .onClick(() => {
56. let index = this.childList.findIndex((item) => {
57. return item.count === this.child.count;
58. });
59. if (index !== -1) {
60. this.childList.splice(index, 1);
61. }
62. })
63. .margin({
64. left: 200,
65. right: 30
66. })
67. }
68. .margin({
69. top: 15,
70. left: 15,
71. right: 10,
72. bottom: 15
73. })
74. .borderRadius(6)
75. .backgroundColor(Color.Grey)
76. }
77. }

79. @Component
80. struct CompList {
81. @ObjectLink @Watch('changeChildList') childList: ChildList;

83. changeChildList() {
84. hilog.info(DOMAIN_NUMBER, TAG, 'CompList ChildList change');
85. }

87. isRenderCompChild(index: number): number {
88. hilog.info(DOMAIN_NUMBER, TAG, 'Comp Child is render' + index);
89. return 1;
90. }

92. build() {
93. Column() {
94. List() {
95. ForEach(this.childList, (item: Child, index) => {
96. ListItem() {
97. CompChild({
98. childList: this.childList,
99. child: item
100. })
101. .opacity(this.isRenderCompChild(index))
102. }
103. })
104. }
105. .height('70%')
106. }
107. }
108. }

110. @Component
111. struct CompAncestor {
112. @ObjectLink ancestor: Ancestor;

114. build() {
115. Column() {
116. CompList({ childList: this.ancestor.childList })
117. Row() {
118. // 点击Button对ancestor执行清空数据
119. Button('Clear')
120. .onClick(() => {
121. this.ancestor.clearData();
122. })
123. .width(100)
124. .margin({ right: 50 })
125. Button('Recover')
126. .onClick(() => {
127. this.ancestor.loadData();
128. })
129. .width(100)
130. }
131. }
132. }
133. }

135. @Entry
136. @Component
137. struct Page {
138. @State childList: ChildList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
139. @State ancestor: Ancestor = new Ancestor(this.childList);

141. build() {
142. Column() {
143. CompAncestor({ ancestor: this.ancestor })
144. }
145. }
146. }
```

[StateArrayObserved.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayObserved.ets#L15-L160)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/g2Pl2IxeRsmichwqpiGDXQ/zh-cn_image_0000002558764130.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=B0833C8458EE701C680ACFA4A2240764834F3D3BD39A6FB7F23239973C293CCE)

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
28. // 临时的数组tempList修改为具有被观测能力的ChildList类
29. let tempList = new ChildList();
30. for (let i = 1; i < 6; i++) {
31. tempList.push(new Child(i));
32. }
33. this.childList = tempList;
34. }

36. public clearData() {
37. this.childList = [];
38. }
39. }

41. @Component
42. struct CompChild {
43. @Link childList: ChildList;
44. @ObjectLink child: Child;

46. build() {
47. Row() {
48. Text(this.child.count + '')
49. .height(70)
50. .fontSize(20)
51. .borderRadius({
52. topLeft: 6,
53. topRight: 6
54. })
55. .margin({ left: 50 })
56. Button('X')
57. .backgroundColor(Color.Red)
58. .onClick(() => {
59. let index = this.childList.findIndex((item) => {
60. return item.count === this.child.count;
61. });
62. if (index !== -1) {
63. this.childList.splice(index, 1);
64. }
65. })
66. .margin({
67. left: 200,
68. right: 30
69. })
70. }
71. .margin({
72. top: 15,
73. left: 15,
74. right: 10,
75. bottom: 15
76. })
77. .borderRadius(6)
78. .backgroundColor(Color.Grey)
79. }
80. }

82. @Component
83. struct CompList {
84. @ObjectLink @Watch('changeChildList') childList: ChildList;

86. changeChildList() {
87. hilog.info(DOMAIN_NUMBER, TAG, 'CompList ChildList change');
88. }

90. isRenderCompChild(index: number): number {
91. hilog.info(DOMAIN_NUMBER, TAG, 'Comp Child is render' + index);
92. return 1;
93. }

95. build() {
96. Column() {
97. List() {
98. ForEach(this.childList, (item: Child, index) => {
99. ListItem() {
100. CompChild({
101. childList: this.childList,
102. child: item
103. })
104. .opacity(this.isRenderCompChild(index))
105. }
106. })
107. }
108. .height('70%')
109. }
110. }
111. }

113. @Component
114. struct CompAncestor {
115. @ObjectLink ancestor: Ancestor;

117. build() {
118. Column() {
119. CompList({ childList: this.ancestor.childList })
120. Row() {
121. Button('Clear')
122. .onClick(() => {
123. this.ancestor.clearData();
124. })
125. .width(100)
126. .margin({ right: 50 })
127. Button('Recover')
128. .onClick(() => {
129. this.ancestor.loadData();
130. })
131. .width(100)
132. }
133. }
134. }
135. }

137. @Entry
138. @Component
139. struct Page {
140. @State childList: ChildList = [new Child(1), new Child(2), new Child(3), new Child(4), new Child(5)];
141. @State ancestor: Ancestor = new Ancestor(this.childList);

143. build() {
144. Column() {
145. CompAncestor({ ancestor: this.ancestor })
146. }
147. }
148. }
```

[StateArrayNo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/statemanagementproject/entry/src/main/ets/pages/statemanagementguide/StateArrayNo.ets#L15-L163)

上述代码运行效果如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/ATJ3mglyQbOggbEwPa_2CQ/zh-cn_image_0000002558604474.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052731Z&HW-CC-Expire=86400&HW-CC-Sign=4B012B21D3439BF12E404493071C98C2B4590B65AB23756F7A256967BBC2D57E)

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
