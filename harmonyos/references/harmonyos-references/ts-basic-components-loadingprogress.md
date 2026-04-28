---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-loadingprogress
title: LoadingProgress
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > LoadingProgress
category: harmonyos-references
scraped_at: 2026-04-28T08:02:01+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:07fc55da110995958d5d804332a9ccf56e42b0f41057c206f0a77e702defed41
---

用于显示加载动效的组件。

加载动效在组件不可见时停止，组件的可见状态基于[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)处理，可见阈值ratios大于0即视为可见状态。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

LoadingProgress()

创建加载进度组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

说明

组件应设置合理的宽高，当组件宽高设置过大时加载动效可能不符合预期效果。

### color

PhonePC/2in1TabletTVWearable

color(value: ResourceColor)

设置加载进度条前景色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 加载进度条的前景色。  默认值：  API version 10及以下：'#99666666'  API version 11及以上：'#ff666666' |

### enableLoading10+

PhonePC/2in1TabletTVWearable

enableLoading(value: boolean)

设置LoadingProgress动画是否显示。LoadingProgress动画不显示时，该组件依旧占位。通用属性[Visibility](ts-appendix-enums.md#visibility).Hidden隐藏的是包括[border](ts-universal-attributes-border.md#border)、[padding](ts-universal-attributes-size.md#padding)等整个组件范围，而enableLoading=false只隐藏LoadingProgress本身动画内容，不包括border等。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | LoadingProgress动画是否显示。  默认值：true，true表示显示LoadingProgress动画，false表示不显示LoadingProgress动画。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<LoadingProgressConfiguration>)

定制LoadingProgress内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | ContentModifier<[LoadingProgressConfiguration](ts-basic-components-loadingprogress.md#loadingprogressconfiguration12对象说明)> | 是 | 在LoadingProgress组件上，定制内容区的方法。  modifier： 内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## LoadingProgressConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enableLoading | boolean | 否 | 否 | LoadingProgress动画是否显示。  默认值：true，true表示显示LoadingProgress动画，false表示不显示LoadingProgress动画。 |

## LoadingProgressStyle枚举说明

PhonePC/2in1TabletTVWearable

表示LoadingProgress的样式类型，不推荐使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Default | 1 | 默认加载样式。API version 8及以后不支持设置。 |
| Circular | 2 | 环形加载样式。API version 8及以后不支持设置。 |
| Orbital | 3 | 彗星形加载样式。API version 8及以后默认为彗星形样式。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置颜色）

该示例通过[color](ts-basic-components-loadingprogress.md#color)接口，实现了设置加载动效颜色的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LoadingProgressExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('Orbital LoadingProgress ').fontSize(9).fontColor(0xCCCCCC).width('90%')
8. LoadingProgress()
9. .color(Color.Blue)
10. .layoutWeight(1)
11. }.width('100%').margin({ top: 5 })
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/O1e9WdiiTOODHnq2RtHrsA/zh-cn_image_0000002552959910.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=637F07BCAB0269D4E1B4F0A8E3D1C3C3E6188904B9E80A351C39D12B522ABE38)

### 示例2（设置定制内容区）

该示例通过[contentModifier](ts-basic-components-loadingprogress.md#contentmodifier12)接口，实现了定制内容区的功能，并通过[enableLoading](ts-basic-components-loadingprogress.md#enableloading10)接口实现了通过按钮切换是否显示LoadingProgress的效果。

```
1. // xxx.ets
2. import { UIContext } from '@kit.ArkUI';

4. class MyLoadingProgressStyle implements ContentModifier<LoadingProgressConfiguration> {
5. enableLoading: boolean = false;
6. ctx: UIContext | undefined = undefined;

8. constructor(enableLoading: boolean, ctx: UIContext) {
9. this.enableLoading = enableLoading;
10. this.ctx = ctx;
11. }

13. applyContent(): WrappedBuilder<[LoadingProgressConfiguration]> {
14. return wrapBuilder(buildLoadingProgress);
15. }
16. }

18. let arr1: string[] =
19. ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19'];
20. let arr2: string[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

22. @Builder
23. function buildLoadingProgress(config: LoadingProgressConfiguration) {
24. Column({ space: 8 }) {
25. Row() {
26. Column() {
27. Circle({
28. width: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? 100 : 80,
29. height: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? 100 : 80
30. })
31. .fill(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)
32. }.width('50%')

34. Column() {
35. Button('' + ((config.contentModifier as MyLoadingProgressStyle).enableLoading))
36. .onClick((event: ClickEvent) => {
37. let uiContext = (config.contentModifier as MyLoadingProgressStyle).ctx;
38. if (uiContext) {
39. uiContext.getPromptAction().showToast({
40. message: ((config.contentModifier as MyLoadingProgressStyle).enableLoading) + ''
41. });
42. }
43. })
44. .fontColor(Color.White)
45. .backgroundColor(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)
46. }.width('50%')

48. }

50. Row() {
51. Column() {
52. Gauge({
53. value: (config.contentModifier as MyLoadingProgressStyle).enableLoading ? 50 : 30, min: 11, max: 100
54. }) {
55. Column() {
56. Text('60')
57. .maxFontSize('180sp')
58. .minFontSize('160.0vp')
59. .fontWeight(FontWeight.Medium)
60. .fontColor('#ff182431')
61. .width('40%')
62. .height('30%')
63. .textAlign(TextAlign.Center)
64. .margin({ top: '22.2%' })
65. .textOverflow({ overflow: TextOverflow.Ellipsis })
66. .maxLines(1)
67. }.width('100%').height('100%')
68. }
69. .colors(((config.contentModifier as MyLoadingProgressStyle).enableLoading) ? Color.Grey : 0x2577e3)
70. .width(200)
71. .strokeWidth(18)
72. .padding(5)
73. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
74. .height(200)
75. }.width('100%')

77. }

79. Column() {
80. List({ space: 20, initialIndex: 0 }) {
81. ForEach(arr2, (item: string) => {
82. ListItem() {
83. Text((config.contentModifier as MyLoadingProgressStyle).enableLoading ? '' + item : Number(item) * 2 + '')
84. .width('100%')
85. .height('100%')
86. .fontColor((config.contentModifier as MyLoadingProgressStyle).enableLoading ? Color.White : Color.Orange)
87. .fontSize((config.contentModifier as MyLoadingProgressStyle).enableLoading ? 16 : 20)
88. .textAlign(TextAlign.Center)
89. .backgroundColor((config.contentModifier as MyLoadingProgressStyle).enableLoading ? Color.Grey : 0x2577e3)
90. }
91. .height(110)
92. .border({
93. width: 2,
94. color: Color.White
95. })
96. }, (item: string) => item)
97. }
98. .height(200)
99. .width('100%')
100. .friction(0.6)

102. .lanes({
103. minLength: (config.contentModifier as MyLoadingProgressStyle).enableLoading ? 40 : 80,
104. maxLength: (config.contentModifier as MyLoadingProgressStyle).enableLoading ? 40 : 80
105. })
106. .scrollBar(BarState.Off)
107. }

109. }.width('100%').padding(10)
110. }

113. @Entry
114. @Component
115. struct LoadingProgressDemoExample {
116. @State loadingProgressList: (boolean | undefined | null)[] = [undefined, true, null, false];
117. @State widthList: (number | string)[] = ['110%', 220, '40%', 80];
118. @State loadingProgressIndex: number = 0;
119. @State clickFlag: number = 0;
120. scroller: Scroller = new Scroller();

122. build() {
123. Column() {
124. Scroll(this.scroller) {
125. Column({ space: 5 }) {
126. Column() {
127. LoadingProgress()
128. .color('#106836')
129. .size({ width: '100%' })
130. .contentModifier(new MyLoadingProgressStyle(this.loadingProgressList[this.loadingProgressIndex], this.getUIContext()))
131. }.width('100%').backgroundColor(0xdcdcdc)
132. }.width('100%').margin({ top: 5 })
133. }.height('85%')

135. Button('点击切换config.enableloading').onClick(() => {
136. this.clickFlag++;
137. this.loadingProgressIndex = (this.loadingProgressIndex + 1) % this.loadingProgressList.length;
138. console.info('enableLoading:' + this.loadingProgressList[this.loadingProgressIndex]);
139. }).margin(20)
140. }

142. }
143. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/9Pa2JUEoQoS9LDhtAeemEQ/zh-cn_image_0000002583479911.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=92C52C700C7531637B387EBF932DB185F30CBBAC38ADC8A64D301923D67B0A62)
