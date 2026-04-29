---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepper
title: Stepper
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > Stepper
category: harmonyos-references
scraped_at: 2026-04-29T13:53:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c09df7ac7a7c68f80b04f397e76b7f44636e02d118947ba4bdf75ecd90873756
---

步骤导航器组件，适用于引导用户按照步骤完成任务的导航场景。

说明

* 从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](ts-container-swiper.md)替代。详细示例请参考[示例2](ts-basic-components-stepper.md#示例2使用swiper替代stepper)。
* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

仅能包含子组件[StepperItem](ts-basic-components-stepperitem.md)。

## 接口

PhonePC/2in1TabletTVWearable

Stepper(value?: { index?: number })

创建步骤导航器组件。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[index](ts-container-swiper.md#index)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | { index?: number } | 否 | 设置步骤导航器当前显示StepperItem的索引值。  默认值：0  从API version 10开始，该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。 |

## 属性

PhonePC/2in1TabletTVWearable

无

## 事件

PhonePC/2in1TabletTVWearable

### onFinish(deprecated)

PhonePC/2in1TabletTVWearable

onFinish(callback: () => void)

步骤导航器最后一个[StepperItem](ts-basic-components-stepperitem.md)的[nextLabel](ts-basic-components-stepperitem.md#nextlabeldeprecated)被点击时，并且[ItemState](ts-basic-components-stepperitem.md#itemstate枚举说明)属性为Normal时，触发该回调。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](ts-container-swiper.md#onchange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 步骤导航器最后一个StepperItem的nextLabel被点击时，并且ItemState属性为Normal时，触发该回调。 |

### onSkip(deprecated)

PhonePC/2in1TabletTVWearable

onSkip(callback: () => void)

当前显示的[StepperItem](ts-basic-components-stepperitem.md)状态为ItemState.Skip时，[nextLabel](ts-basic-components-stepperitem.md#nextlabeldeprecated)被点击时触发该回调。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](ts-container-swiper.md#onchange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | () => void | 是 | 当前显示的StepperItem状态为ItemState.Skip时，nextLabel被点击时触发该回调。 |

### onChange(deprecated)

PhonePC/2in1TabletTVWearable

onChange(callback: (prevIndex: number, index: number) => void)

点击当前StepperItem的[prevLabel](ts-basic-components-stepperitem.md#prevlabeldeprecated)进行步骤切换时触发该回调；或点击当前StepperItem的[nextLabel](ts-basic-components-stepperitem.md#nextlabeldeprecated)，当前页面不为步骤导航器最后一个StepperItem且[ItemState](ts-basic-components-stepperitem.md#itemstate枚举说明)属性为Normal时，触发该回调。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](ts-container-swiper.md#onchange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| prevIndex | number | 是 | 切换前的步骤页索引值。  取值范围：[0, +∞) |
| index | number | 是 | 切换后的步骤页（前一页或者下一页）索引值。  取值范围：[0, +∞) |

### onNext(deprecated)

PhonePC/2in1TabletTVWearable

onNext(callback: (index: number, pendingIndex: number) => void)

点击StepperItem的[nextLabel](ts-basic-components-stepperitem.md#nextlabeldeprecated)切换下一步骤时，当前页面不为步骤导航器最后一个StepperItem且[ItemState](ts-basic-components-stepperitem.md#itemstate枚举说明)属性为Normal时，触发该回调。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](ts-container-swiper.md#onchange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前步骤页索引值。 |
| pendingIndex | number | 是 | 下一步骤页索引值。 |

### onPrevious(deprecated)

PhonePC/2in1TabletTVWearable

onPrevious(callback: (index: number, pendingIndex: number) => void)

点击StepperItem的[prevLabel](ts-basic-components-stepperitem.md#prevlabeldeprecated)切换上一步骤时触发该回调。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[onChange](ts-container-swiper.md#onchange)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 当前步骤页索引值。 |
| pendingIndex | number | 是 | 上一步骤页索引值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用Stepper）

该示例主要演示如何使用步骤导航器组件。

```
1. // xxx.ets
2. @Styles function itemStyle () {
3. .width(336)
4. .height(621)
5. .margin({ top: 48, left: 12 })
6. .borderRadius(24)
7. .backgroundColor('#FFFFFF')
8. }

10. @Extend(Text) function itemTextStyle () {
11. .fontColor('#182431')
12. .fontSize(36)
13. .fontWeight(500)
14. .opacity(0.4)
15. .margin({ top: 82, bottom: 40 })
16. }

18. @Entry
19. @Component
20. struct StepperExample {
21. @State currentIndex: number = 0;
22. @State firstState: ItemState = ItemState.Normal;
23. @State secondState: ItemState = ItemState.Normal;
24. @State thirdState: ItemState = ItemState.Normal;

26. build() {
27. Stepper({
28. index: this.currentIndex
29. }) {
30. // 第一个步骤页
31. StepperItem() {
32. Column() {
33. Text('Page One')
34. .itemTextStyle()
35. Button('change status:' + this.firstState)
36. .backgroundColor('#007dFF')
37. .onClick(() => {
38. this.firstState = this.firstState === ItemState.Skip ? ItemState.Normal : ItemState.Skip;
39. })
40. }.itemStyle()
41. }
42. .nextLabel('Next')
43. .status(this.firstState)
44. // 第二个步骤页
45. StepperItem() {
46. Column() {
47. Text('Page Two')
48. .itemTextStyle()
49. Button('change status:' + this.secondState)
50. .backgroundColor('#007dFF')
51. .onClick(() => {
52. this.secondState = this.secondState === ItemState.Disabled ? ItemState.Normal : ItemState.Disabled;
53. })
54. }.itemStyle()
55. }
56. .nextLabel('Next')
57. .prevLabel('Previous')
58. .status(this.secondState)
59. // 第三个步骤页
60. StepperItem() {
61. Column() {
62. Text('Page Three')
63. .itemTextStyle()
64. Button('change status:' + this.thirdState)
65. .backgroundColor('#007dFF')
66. .onClick(() => {
67. this.thirdState = this.thirdState === ItemState.Waiting ? ItemState.Normal : ItemState.Waiting;
68. })
69. }.itemStyle()
70. }
71. .status(this.thirdState)
72. // 第四个步骤页
73. StepperItem() {
74. Column() {
75. Text('Page Four')
76. .itemTextStyle()
77. }.itemStyle()
78. }
79. }
80. .backgroundColor('#F1F3F5')
81. .onFinish(() => {
82. // 此处可处理点击最后一页的Finish时的逻辑，例如路由跳转等
83. console.info('onFinish');
84. })
85. .onSkip(() => {
86. // 此处可处理点击跳过时的逻辑，例如动态修改Stepper的index值使其跳转到某一步骤页等
87. console.info('onSkip');
88. })
89. .onChange((prevIndex?: number, index?: number) => {
90. if(index){
91. this.currentIndex = index;
92. }
93. })
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/0boL9XzBTQypcPPuCgNn4g/zh-cn_image_0000002589326561.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055313Z&HW-CC-Expire=86400&HW-CC-Sign=84400C5CD88466EEE345B1A3451D209E7C5A9E844EAF6B4F9B9438F6F02B7BF3)

### 示例2（使用Swiper替代Stepper）

该示例主要演示如何使用Swiper组件实现Stepper组件的功能，示例效果图同示例1。

```
1. @Styles
2. function itemStyle() {
3. .width(336)
4. .height(621)
5. .margin({ top: 48, left: 12 })
6. .borderRadius(24)
7. .backgroundColor('#FFFFFF')
8. }

10. @Extend(Text)
11. function itemTextStyle() {
12. .fontColor('#182431')
13. .fontSize(36)
14. .fontWeight(500)
15. .opacity(0.4)
16. .margin({ top: 82, bottom: 40 })
17. }

19. @Entry
20. @Component
21. struct StepperExample {
22. @State currentIndex: number = 0;
23. @State status: number = 0;
24. @State nextLabel: string = "Next";
25. @State prevLabel: string = "Previous";
26. private swiperController: SwiperController = new SwiperController();

28. build() {
29. Column() {
30. Swiper(this.swiperController) {
31. // 第一个步骤页
32. Column() {
33. Text('Page One')
34. .itemTextStyle()
35. Button('change status:' + this.status)
36. .backgroundColor('#007dFF')
37. .onClick(() => {
38. if (this.status < 3) {
39. this.status += 1
40. } else {
41. this.status = 0
42. }
43. })
44. }.itemStyle()
45. // 第二个步骤页
46. Column() {
47. Text('Page Two')
48. .itemTextStyle()
49. Button('change status:' + this.status)
50. .backgroundColor('#007dFF')
51. .onClick(() => {
52. if (this.status < 3) {
53. this.status += 1
54. } else {
55. this.status = 0
56. }
57. })
58. }.itemStyle()
59. // 第三个步骤页
60. Column() {
61. Text('Page Three')
62. .itemTextStyle()
63. Button('change status:' + this.status)
64. .backgroundColor('#007dFF')
65. .onClick(() => {
66. if (this.status < 3) {
67. this.status += 1
68. } else {
69. this.status = 0
70. }
71. })
72. }.itemStyle()
73. // 第四个步骤页
74. Column() {
75. Text('Page Four')
76. .itemTextStyle()
77. }.itemStyle()
78. }
79. .index(this.currentIndex)
80. .disableSwipe(true)
81. .loop(false)
82. .indicator(false)
83. .backgroundColor('#fff5f2f2')
84. .onChange((index) => {
85. console.info("Changed")
86. this.currentIndex = index
87. this.nextLabel = this.currentIndex == 2 ? "下一步" : "Next"
88. this.prevLabel = this.currentIndex == 2 ? "返回" : "Previous"
89. })
90. // 底部按钮
91. Row() {
92. if (this.currentIndex > 0) {
93. Row() {
94. SymbolGlyph($r("sys.symbol.chevron_left"))
95. .fontSize(20)
96. .margin({ right: 5 })
97. Text(this.prevLabel)
98. // 使用这里的onClick替代原Stepper的onPrevious
99. .onClick(() => {
100. this.swiperController.showPrevious()
101. })
102. }
103. .justifyContent(FlexAlign.Start)
104. .width(100)
105. .height(20)
106. .position({ left: 20 })
107. }
108. Row() {
109. if (this.currentIndex == 3) {
110. Text("开始")
111. // 使用这里的onClick替代原Stepper的onFinish
112. .onClick(() => {
113. console.info("Finish")
114. })
115. } else if (this.status == 0) {
116. Text(this.nextLabel)
117. // 使用这里的onClick替代原Stepper的onNext
118. .onClick(() => {
119. this.swiperController.showNext()
120. })
121. SymbolGlyph($r("sys.symbol.chevron_right"))
122. .fontSize(20)
123. .margin({ left: 5 })
124. } else if (this.status == 1) {
125. Text(this.nextLabel)
126. .fontColor('#ff818181')
127. SymbolGlyph($r("sys.symbol.chevron_right"))
128. .fontSize(20)
129. .fontColor(['#ff818181'])
130. .margin({ left: 5 })
131. } else if (this.status == 2) {
132. LoadingProgress()
133. .width(25)
134. } else if (this.status == 3) {
135. Text("跳过")
136. // 使用这里的onClick替代原Stepper的onSkip
137. .onClick(() => {
138. console.info("Skip")
139. })
140. SymbolGlyph($r("sys.symbol.chevron_right"))
141. .fontSize(20)
142. .margin({ left: 5 })
143. }
144. }
145. .justifyContent(FlexAlign.End)
146. .width(100)
147. .height(20)
148. .position({ right: 20 })
149. }
150. .backgroundColor('#fff5f2f2')
151. .position({ bottom: 30 })
152. .width("100%")
153. }
154. .backgroundColor('#fff5f2f2')
155. .width("100%")
156. .height("100%")
157. }
158. }
```
