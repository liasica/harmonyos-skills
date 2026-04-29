---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-redundancy-refresh-guide
title: 组件冗余刷新解决方案
breadcrumb: 最佳实践 > 声明式语法 > 组件冗余刷新解决方案
category: best-practices
scraped_at: 2026-04-29T14:10:38+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:2851754953c92cfdff6a7baf3d79224e70ed7c3aeff2fe9a74366df4d86f668f
---

## 简介

自定义组件中的变量被状态装饰器（@State，@Prop等）装饰后成为状态变量，而状态变量的改变会引起使用该变量的UI组件渲染刷新。状态变量的不合理使用可能会带来冗余刷新等性能问题。开发者可以使用状态变量组件定位工具（[hidumper](../harmonyos-guides/hidumper.md)）获取状态管理相关信息，例如自定义组件拥有的状态变量、状态变量的同步对象和关联组件等，了解状态变量影响UI的范围，写出高性能应用代码。

下面通过一个点击按钮更改状态变量引起组件刷新的场景示例，结合hidumper工具，介绍状态变量使用范围不当，导致UI冗余刷新的问题定位。

## 示例代码

在以下代码中，创建了自定义组件ComponentA、SpecialImage，每个组件都拥有一些状态变量和UI组件。组件ComponentA中存在Move和Scale两个按钮，在按钮的点击回调中改变状态变量的值刷新相应的组件。

```
1. // constant declaration
2. const animationDuration: number = 500; // Move animation duration
3. const opacityChangeValue: number = 0.1; // The value of each change in opacity
4. const opacityChangeRange: number = 1; // Range of opacity changes
5. const translateYChangeValue: number = 180; // The value of translateY each time it changes
6. const translateYChangeRange: number = 250; // The range in which translateY changes
7. const scaleXChangeValue: number = 0.6; // The value of scaleX for each change
8. const scaleXChangeRange: number = 0.8; // The value of scaleX for each change

10. // Style Attribute Classes
11. class UIStyle {
12. public translateX: number = 0;
13. public translateY: number = 0;
14. public scaleX: number = 0.3;
15. public scaleY: number = 0.3;
16. }

18. @Component
19. struct ComponentA {
20. @Link uiStyle: UIStyle; // Properties of uiStyle used by multiple components

22. build() {
23. Column() {
24. // Components that use state variables
25. SpecialImage({ specialImageUiStyle: this.uiStyle })
26. Column() {
27. // 需要替换为开发者所需的图像资源文件
28. Image($r('app.media.startIcon'))
29. .height('150vp')
30. .width('150vp')
31. .scale({
32. x: this.uiStyle.scaleX,
33. y: this.uiStyle.scaleY
34. })
35. Text('Hello World')
36. .fontWeight(FontWeight.Bold)
37. }
38. .translate({
39. x: this.uiStyle.translateX,
40. y: this.uiStyle.translateY
41. })
42. .width('95%')
43. .height('200vp')
44. .margin({
45. top: '10vp',
46. left: '15vp',
47. right: '15vp'
48. })
49. .borderRadius('16vp')
50. .backgroundColor(Color.White)
51. // Modify the value of a state variable via a button click callback, causing the corresponding component to refresh.
52. Column() {
53. Button('Move')
54. .width('80%')
55. .onClick(() => {
56. this.getUIContext().animateTo({ duration: animationDuration }, () => {
57. this.uiStyle.translateY = (this.uiStyle.translateY + translateYChangeValue) % translateYChangeRange;
58. })
59. })
60. Button('Scale')
61. .width('80%')
62. .onClick(() => {
63. this.uiStyle.scaleX = (this.uiStyle.scaleX + scaleXChangeValue) % scaleXChangeRange;
64. })
65. .margin({
66. top: '10vp',
67. left: '15vp',
68. right: '15vp'
69. })
70. }
71. .height('35%')
72. .justifyContent(FlexAlign.End)
73. .width('100%')
74. }
75. }
76. }

78. @Component
79. struct SpecialImage {
80. @Link specialImageUiStyle: UIStyle;
81. private opacityNum: number = 0.5; // Default transparency

83. private isRenderSpecialImage(): number {
84. // Image transparency increases by 0.1 each time it is rendered, cycling between 0 and 1.
85. this.opacityNum = (this.opacityNum + opacityChangeValue) % opacityChangeRange;
86. return this.opacityNum;
87. }

89. build() {
90. Column() {
91. // 需要替换为开发者所需的图像资源文件
92. Image($r('app.media.startIcon'))
93. .size({ width: 78, height: 78 })
94. .scale({
95. x: this.specialImageUiStyle.scaleX,
96. y: this.specialImageUiStyle.scaleY
97. })
98. .opacity(this.isRenderSpecialImage())
99. Text("SpecialImage")
100. .fontWeight(FontWeight.Bold)
101. }
102. .width('95%')
103. .margin({
104. top: '10vp',
105. left: '15vp',
106. right: '15vp'
107. })
108. .borderRadius('16vp')
109. .height('200vp')
110. .backgroundColor(Color.White)
111. }
112. }

115. @Entry
116. @Component
117. struct DFXStateBeforeOptimization {
118. @State uiStyle: UIStyle = new UIStyle();

120. build() {
121. Column() {
122. ComponentA({
123. uiStyle: this.uiStyle
124. })
125. }
126. .width('100%')
127. .height('100%')
128. .backgroundColor(0xDCDCDC)
129. }
130. }
```

[segment1.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Redundancy_Refresh_Optimization/entry/src/main/ets/segment/segment1.ets#L2-L132)

运行上述示例并分别点击按钮，可以看到点击Move按钮和Scale按钮时组件SpecialImage都出现了刷新，运行效果图如下。

**图1** 修改代码前点击Scale按钮和Move按钮时运行动图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/rjMbFCdSSpOvYPYBxYcAkA/zh-cn_image_0000002229451917.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061031Z&HW-CC-Expire=86400&HW-CC-Sign=F847E7BC2E9DF251539EEFBD5D4EB9F36EDF6B7BF774AF42FD51C38538E6D096 "点击放大")

点击Move按钮的时候SpecialImage组件却发生了旋转动画，这就造成了冗余刷新。

## 问题定位

下面通过这个示例代码结合hidumper工具来介绍冗余刷新的问题定位。

1. 首先在设备上打开应用，进入ComponentA组件所在的页面。

2. 使用以下命令获取示例应用的窗口Id。当前运行的示例应用包名为performancelibrary，可以在输出结果中找到对应窗口名performancelibrary0的WinId，即为应用的窗口Id。或者当应用正处于前台运行时，Focus window的值就是应用的窗口Id。此处示例应用的窗口Id为11，后面的流程中使用的命令都需要指定窗口Id。

```
1. hdc shell "hidumper -s WindowManagerService -a '-a'"
```

**图2** 命令行获取应用窗口Id运行界面

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/sGIHK-0zTce6UKTuKOcuag/zh-cn_image_0000002194011628.png?HW-CC-KV=V1&HW-CC-Date=20260429T061031Z&HW-CC-Expire=86400&HW-CC-Sign=4F232563A8BB26492EE20E047F5FA3468901605A3ECC0729ADEA4BBA0DF14615 "点击放大")

3. 基于上一步获取的窗口Id 11，使用-viewHierarchy命令携带-r 参数递归打印应用的自定义组件树。

```
1. hdc shell "hidumper -s WindowManagerService -a '-w 11 -jsdump -viewHierarchy -r'"
```

打印应用的自定义组件树结果如下：

```
1. -----------------ViewPUHierarchy-----------------
2. [-viewHierarchy, viewId=4, isRecursive=true]

5. |--DFXStateBeforeOptimization[4]ViewPU {isViewActive: true, isDeleting_: false}
6. |--ComponentA[6]ViewPU {isViewActive: true, isDeleting_: false}
7. |--SpecialImage[8]ViewPU {isViewActive: true, isDeleting_: false}
```

从结果中找到目标组件ComponentA，后面括号中的内容即为组件ComponentA的节点Id 6。

4. 使用命令-stateVariables携带参数-viewId（参数的值为ComponentA的节点Id）获取自定义组件ComponentA中的状态变量信息。

```
1. hdc shell "hidumper -s WindowManagerService -a '-w 11 -jsdump -stateVariables -viewId=6'"
```

打印组件ComponentA的状态变量信息如下：

```
1. --------------ViewPUState Variables--------------
2. [-stateVariables, viewId=6, isRecursive=false]

4. |--ComponentA[6]
5. @Link 'uiStyle'[-1]
6. |--Owned by @Component 'ComponentA'[6]
7. |--Sync peers: {
8. @Link 'specialImageUiStyle'[-2] <@Component 'SpecialImage'[8]>
9. }
10. dependencies: variable assignment affects elmtIds: Column[9], Image[10]
11. |--Dependent elements: Column[9], Image[10]; @Component 'SpecialImage'[8], Image[18]
```

结果显示ComponentA拥有@Link类型的状态变量uiStyle。每条状态变量的详细信息都包含状态变量的所属组件、同步对象和关联组件。

5. 以状态变量uiStyle为例。

① Sync peers表示uiStyle在自定义组件SpecialImage中存在@Link类型的状态变量specialImageUiStyle订阅数据变化。

② Dependent elements表示当前状态变量和其同步对象的关联组件SpecialImage。

所以当uiStyle变化时，影响的组件范围为自定义组件SpecialImage以及系统组件Column[9]和Image[10]。

示例中组件SpecialImage仅使用了uiStyle传递到specialImageUiStyle中的属性scaleX、scaleY。但点击Move按钮修改uiStyle中的属性translateY时，引起的uiStyle变化也会导致组件SpecialImage的刷新。所以，可以将uiStyle中的属性scaleX、scaleY提取到状态变量scaleStyle中，属性translateX和translateY提取到状态变量translateStyle中，仅传递scaleStyle给组件SpecialImage，避免不必要的刷新。

由于提取后存在Class的嵌套，因此需要使用@Observed/@ObjectLink装饰器装饰相应的Class和状态变量。修改后的部分代码如下：

```
1. // constant declaration
2. const animationDuration: number = 500; // Move animation duration
3. const opacityChangeValue: number = 0.1; // The value of each change in opacity
4. const opacityChangeRange: number = 1; // Range of opacity changes
5. const translateYChangeValue: number = 180; // The value of translateY each time it changes
6. const translateYChangeRange: number = 250; // The range in which translateY changes
7. const scaleXChangeValue: number = 0.6; // The value of scaleX for each change
8. const scaleXChangeRange: number = 0.8; // The value of scaleX for each change

10. // Style property class, nested ScaleStyle, TranslateStyle
11. @Observed
12. class UIStyle {
13. translateStyle: TranslateStyle = new TranslateStyle();
14. scaleStyle: ScaleStyle = new ScaleStyle();
15. }

17. // Zoom Property Class
18. @Observed
19. class ScaleStyle {
20. public scaleX: number = 0.3;
21. public scaleY: number = 0.3;
22. }

24. // Displacement Attribute Class
25. @Observed
26. class TranslateStyle {
27. public translateX: number = 0;
28. public translateY: number = 0;
29. }

31. @Component
32. struct ComponentA {
33. @ObjectLink scaleStyle: ScaleStyle;
34. @ObjectLink translateStyle: TranslateStyle;

36. build() {
37. Column() {
38. SpecialImage({
39. specialImageScaleStyle: this.scaleStyle
40. })
41. // Other UI components
42. Column() {
43. // 需要替换为开发者所需的图像资源文件
44. Image($r('app.media.startIcon'))
45. .height('150vp')
46. .width('150vp')
47. .scale({
48. x: this.scaleStyle.scaleX,
49. y: this.scaleStyle.scaleY
50. })
51. Text('Hello World')
52. .fontWeight(FontWeight.Bold)
53. }

55. .translate({
56. x: this.translateStyle.translateX,
57. y: this.translateStyle.translateY
58. })
59. .width('95%')
60. .height('200vp')
61. .margin({
62. top: '10vp',
63. left: '15vp',
64. right: '15vp'
65. })
66. .borderRadius('16vp')
67. .backgroundColor(Color.White)
68. // Modify the value of a state variable via a button click callback, causing the corresponding component to refresh.
69. Column() {
70. Button('Move')
71. .width('80%')
72. .onClick(() => {
73. this.getUIContext().animateTo({ duration: animationDuration }, () => {
74. this.translateStyle.translateY =
75. (this.translateStyle.translateY + translateYChangeValue) % translateYChangeRange;
76. })
77. })
78. Button('Scale')
79. .width('80%')
80. .onClick(() => {
81. this.scaleStyle.scaleX = (this.scaleStyle.scaleX + scaleXChangeValue) % scaleXChangeRange;
82. })
83. .margin({
84. top: '10vp',
85. left: '15vp',
86. right: '15vp'
87. })
88. }
89. .height('35%')
90. .justifyContent(FlexAlign.End)
91. .width('100%')
92. }
93. }
94. }

96. @Component
97. struct SpecialImage {
98. @Link specialImageScaleStyle: ScaleStyle;
99. private opacityNum: number = 0.5; // Default transparency

101. // isRenderSpecialImage function
102. private isRenderSpecialImage(): number {
103. // Image transparency increases by 0.1 each time it is rendered, cycling between 0 and 1.
104. this.opacityNum = (this.opacityNum + opacityChangeValue) % opacityChangeRange;
105. return this.opacityNum;
106. }

108. build() {
109. Column() {
110. // 需要替换为开发者所需的图像资源文件
111. Image($r('app.media.startIcon'))
112. .size({ width: 78, height: 78 })
113. .scale({
114. x: this.specialImageScaleStyle.scaleX,
115. y: this.specialImageScaleStyle.scaleY
116. })
117. .opacity(this.isRenderSpecialImage())
118. Text("SpecialImage")
119. .fontWeight(FontWeight.Bold)
120. }
121. .width('95%')
122. .margin({
123. top: '10vp',
124. left: '15vp',
125. right: '15vp'
126. })
127. .borderRadius('16vp')
128. .height('200vp')
129. .backgroundColor(Color.White)
130. }
131. }

133. @Entry
134. @Component
135. struct DFXStateAfterOptimization {
136. @State uiStyle: UIStyle = new UIStyle();

138. build() {
139. Stack() {
140. ComponentA({
141. scaleStyle: this.uiStyle.scaleStyle,
142. translateStyle: this.uiStyle.translateStyle,
143. })
144. }
145. .width('100%')
146. .height('100%')
147. .backgroundColor(0xDCDCDC)
148. }
149. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Redundancy_Refresh_Optimization/entry/src/main/ets/segment/segment2.ets#L2-L151)

修改后的示例运行效果图如下，只有点击Scale按钮时SpecialImage产生刷新现象，点击Move按钮时SpecialImage不会刷新。

**图3** 修改代码后点击Scale按钮和Move按钮时运行动图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/HE23RMWnSHmF-8jrpQLTAA/zh-cn_image_0000002193852044.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061031Z&HW-CC-Expire=86400&HW-CC-Sign=FB71D91C64AFA1389C59C2A474E22F44B1EAC9A6F45D8ECB5C1ED4D39F58E23E "点击放大")

可以使用上文步骤再次获取ComponentA组件的状态变量信息如下，可以看到ComponentA中状态变量scaleStyle影响组件SpecialImage[8]和Image[18]，状态变量translateStyle影响组件Column[9]，translateStyle的变化不会再导致SpecialImage的刷新。

```
1. --------------ViewPUState Variables--------------
2. [-stateVariables, viewId=6, isRecursive=false]

4. |--ComponentA[6]
5. @ObjectLink 'scaleStyle'[-1]
6. |--Owned by @Component 'ComponentA'[6]
7. |--Sync peers: {
8. @Link 'specialImageScaleStyle'[-3] <@Component 'SpecialImage'[8]>
9. }
10. dependencies: variable assignment affects elmtIds: Image[10]
11. |--Dependent elements: Image[10]; @Component 'SpecialImage'[8], Image[18]
12. @ObjectLink 'translateStyle'[-2]
13. |--Owned by @Component 'ComponentA'[6]
14. |--Sync peers: none
15. dependencies: variable assignment affects elmtIds: Column[9]
16. |--Dependent elements: Column[9]
```
