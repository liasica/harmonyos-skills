---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border-image
title: 图片边框设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 图片边框设置
category: harmonyos-references
scraped_at: 2026-04-28T08:01:05+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:6314794a14557d9d94961736d9dbe472f5b9150594df633246db619f8d9a4b90
---

设置组件的图片边框样式。

说明

从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## borderImage

PhonePC/2in1TabletTVWearable

borderImage(value: BorderImageOption): T

设置组件的图片边框。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderImageOption](ts-universal-attributes-border-image.md#borderimageoption对象说明) | 是 | 图片边框或者渐变色边框设置接口。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BorderImageOption对象说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| source | string | [Resource](ts-types.md#resource) | [LinearGradient](ts-universal-attributes-border-image.md#lineargradient) | 否 | 是 | 边框图源或者渐变色设置。参数类型为string类型时，用于设置边框图源，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。  **说明：**  边框图源仅适用于容器组件，如[Row](ts-container-row.md)、[Column](ts-container-column.md)、[Flex](ts-container-flex.md)，在非容器组件上使用会失效。 |
| slice | [Length](ts-types.md#length) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+ | 否 | 是 | 设置边框图片左上角、右上角、左下角以及右下角的切割宽高。  默认值：0  **说明：**  设置负数时取默认值。  参数类型为[Length](ts-types.md#length)时，统一设置四个角的宽高。  参数类型为[EdgeWidths](ts-types.md#edgewidths9)时：  - Top：设置图片上侧被切割的高。  - Bottom：设置图片下侧被切割的高。  - Left：设置图片左侧被切割的宽。  - Right：设置图片右侧被切割的宽。  参数类型为[LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+时：  - Top：设置图片上侧被切割的高。  - Bottom：设置图片下侧被切割的高。  - Start：设置图片左侧被切割的宽。  从右至左显示语言模式下为设置图片右侧被切割的宽。  - End：设置图片右侧被切割的宽。  从右至左显示语言模式下为设置图片左侧被切割的宽。 |
| width | [Length](ts-types.md#length) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+ | 否 | 是 | 设置图片边框宽度。  默认值：0  **说明：**  设置负数时值取1。  参数类型为[Length](ts-types.md#length)时，统一设置四条边框的宽度，设置负数时取默认值。  参数类型为[EdgeWidths](ts-types.md#edgewidths9)时：  - Top：设置图片边框上边框的宽。  - Bottom：设置图片边框下边框的宽。  - Left：设置图片边框左边框的宽。  - Right：设置图片边框右边框宽。  参数类型为[LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+时：  - Top：设置图片边框上边框的宽。  - Bottom：设置图片边框下边框的宽。  - Start：设置图片边框左边框的宽。  从右至左显示语言模式下为设置图片边框右边框宽。  - End：设置图片边框右边框宽。  从右至左显示语言模式下为设置图片边框左边框的宽。 |
| outset | [Length](ts-types.md#length) | [EdgeWidths](ts-types.md#edgewidths9) | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+ | 否 | 是 | 设置边框图片向外延伸距离。  默认值：0  **说明：**  设置负数时取默认值。  参数类型为[Length](ts-types.md#length)时，统一设置四条边框的向外延伸距离。  参数类型为[EdgeWidths](ts-types.md#edgewidths9)时：  - Top：设置边框图片上边框向外延伸的距离。  - Bottom：设置边框图片下边框向外延伸的距离。  - Left：设置边框图片左边框向外延伸的距离。  - Right：设置边框图片右边框向外延伸的距离。  参数类型为[LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+时：  - Top：设置边框图片上边框向外延伸的距离。  - Bottom：设置边框图片下边框向外延伸的距离。  - Start：设置边框图片左边框向外延伸的距离。  从右至左显示语言模式下为设置边框图片右边框向外延伸的距离。  - End：设置边框图片右边框向外延伸的距离。  从右至左显示语言模式下为设置边框图片左边框向外延伸的距离。 |
| repeat | [RepeatMode](ts-universal-attributes-border-image.md#repeatmode) | 否 | 是 | 设置被切割的图片在边框上的重复方式。  默认值：RepeatMode.Stretch |
| fill | boolean | 否 | 是 | 设置边框图片是否中心填充。true表示中心填充，false表示非中心填充。  默认值：false |

## RepeatMode

PhonePC/2in1TabletTVWearable

用于设置被切割的图片在边框上的重复方式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Repeat | 0 | 被切割的图片会重复铺平在图片边框上，超出部分会被剪裁。 |
| Stretch | 1 | 被切割的图片会以拉伸填充的方式铺满图片边框。 |
| Round | 2 | 被切割的图片会以整数次平铺在图片边框上，无法以整数次平铺时会压缩图片。 |
| Space | 3 | 被切割的图片会以整数次平铺在图片边框上，无法以整数次平铺时会以空白填充。 |

## LinearGradient

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| angle | number | string | 否 | 是 | 线性渐变的起始角度。0点方向顺时针旋转为正向角度。  默认值：180  角度为字符串时仅支持类型'deg'，'grad'，'rad'，'turn'。 |
| direction | [GradientDirection](ts-appendix-enums.md#gradientdirection) | 否 | 是 | 线性渐变的方向，设置angle后不生效。  默认值：GradientDirection.Bottom |
| colors | Array<[[ResourceColor](ts-types.md#resourcecolor), number]> | 否 | 否 | 指定渐变色颜色和其对应的百分比位置的数组，设置非法颜色直接跳过。 |
| repeating | boolean | 否 | 是 | 是否允许渐变的颜色重复渲染。  默认值：false  true：允许渐变的颜色重复渲染。  false：不允许渐变的颜色重复渲染。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置渐变色边框）

通过[borderImage](ts-universal-attributes-border-image.md#borderimage)接口为组件设置渐变色边框。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Row() {
7. Column() {
8. Text('This is gradient color.').textAlign(TextAlign.Center).height(50).width(200)
9. .borderImage({
10. source: {
11. angle: 90,
12. direction: GradientDirection.Left,
13. colors: [[0xAEE1E1, 0.0], [0xD3E0DC, 0.3], [0xFCD1D1, 1.0]],
14. repeating: false
15. },
16. slice: { top: 10, bottom: 10, left: 10, right: 10 },
17. width: { top: "10px", bottom: "10px", left: "10px", right: "10px" },
18. repeat: RepeatMode.Stretch,
19. fill: false
20. })
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/9OkXba5OTBymnvUS1QLwsw/zh-cn_image_0000002583479505.png?HW-CC-KV=V1&HW-CC-Date=20260428T000104Z&HW-CC-Expire=86400&HW-CC-Sign=BABF98689B67349397D34BE8F6C2657EAD96007EED7ABA5DEED8CBA85BAE8197)

### 示例2（动态调整属性值）

通过[slider](js-components-basic-slider.md)接口动态调整[borderImage](ts-universal-attributes-border-image.md#borderimage)接口中属性值。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BorderImage {
5. @State WidthValue: number = 0
6. @State SliceValue: number = 0
7. @State OutSetValue: number = 0
8. @State RepeatValue: RepeatMode[] = [RepeatMode.Repeat, RepeatMode.Stretch, RepeatMode.Round, RepeatMode.Space]
9. @State SelectIndex: number = 0
10. @State SelectText: string = 'Repeat'
11. @State FillValue: boolean = false

13. build() {
14. Row() {
15. Column({ space: 20 }) {
16. Row() {
17. Text('This is borderImage.').textAlign(TextAlign.Center).fontSize(50)
18. }
19. .borderImage({
20. source: $r('app.media.icon'),
21. slice: this.SliceValue,
22. width: this.WidthValue,
23. outset: this.OutSetValue,
24. repeat: this.RepeatValue[this.SelectIndex],
25. fill: this.FillValue
26. })

28. Column() {
29. Text(`borderImageSlice = ${this.SliceValue}px`)
30. Slider({
31. value: this.SliceValue,
32. min: 0,
33. max: 100,
34. style: SliderStyle.OutSet
35. })
36. .onChange((value: number, mode: SliderChangeMode) => {
37. this.SliceValue = value
38. })
39. }

41. Column() {
42. Text(`borderImageWidth = ${this.WidthValue}px`)
43. Slider({
44. value: this.WidthValue,
45. min: 0,
46. max: 100,
47. style: SliderStyle.OutSet
48. })
49. .onChange((value: number, mode: SliderChangeMode) => {
50. this.WidthValue = value
51. })
52. }

54. Column() {
55. Text(`borderImageOutSet = ${this.OutSetValue}px`)
56. Slider({
57. value: this.OutSetValue,
58. min: 0,
59. max: 100,
60. style: SliderStyle.OutSet
61. })
62. .onChange((value: number, mode: SliderChangeMode) => {
63. this.OutSetValue = value
64. })
65. }

67. Row() {
68. Text('borderImageRepeat: ')
69. Select([{ value: 'Repeat' }, { value: 'Stretch' }, { value: 'Round' }, { value: 'Space' }])
70. .value(this.SelectText)
71. .selected(this.SelectIndex)
72. .onSelect((index: number, value?: string) => {
73. this.SelectIndex = index
74. this.SelectText = value as string
75. })
76. }

78. Row() {
79. Text(`borderImageFill: ${this.FillValue} `)
80. Toggle({ type: ToggleType.Switch, isOn: this.FillValue })
81. .onChange((isOn: boolean) => {
82. this.FillValue = isOn
83. })
84. }

86. }
87. .width('100%')
88. }
89. .height('100%')
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/-q__joGJQ8mhtIGUvUQjOQ/zh-cn_image_0000002552799856.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000104Z&HW-CC-Expire=86400&HW-CC-Sign=555888D81D6E81F579533E02ACA2A1D7F67BA7B67A1AB3A67AA8D90CEDA16631)

### 示例3（使用LocalizedEdgeWidths类型值）

通过[borderImage](ts-universal-attributes-border-image.md#borderimage)接口中的slice、width和outset属性值使用[LocalizedEdgeWidths](ts-types.md#localizededgewidths12)类型。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI'

4. @Entry
5. @Component
6. struct BorderImage {
7. @State WidthStartValue: number = 0
8. @State WidthEndValue: number = 0
9. @State SliceStartValue: number = 0
10. @State SliceEndValue: number = 0
11. @State OutSetStartValue: number = 0
12. @State OutSetEndValue: number = 0
13. @State RepeatValue: RepeatMode[] = [RepeatMode.Repeat, RepeatMode.Stretch, RepeatMode.Round, RepeatMode.Space]
14. @State SelectIndex: number = 0
15. @State SelectText: string = 'Repeat'
16. @State FillValue: boolean = false

18. build() {
19. Row() {
20. Column({ space: 20 }) {
21. Row() {
22. Text('This is borderImage.').textAlign(TextAlign.Center).fontSize(50)
23. }
24. .borderImage({
25. source: $r('app.media.startIcon'),
26. slice: {
27. top: LengthMetrics.px(10),
28. bottom: LengthMetrics.px(10),
29. start: LengthMetrics.px(this.SliceStartValue),
30. end: LengthMetrics.px(this.SliceEndValue) },
31. width: {
32. top: LengthMetrics.px(10),
33. bottom: LengthMetrics.px(10),
34. start: LengthMetrics.px(this.WidthStartValue),
35. end: LengthMetrics.px(this.WidthEndValue)
36. },
37. outset: {
38. top: LengthMetrics.px(10),
39. bottom: LengthMetrics.px(10),
40. start: LengthMetrics.px(this.OutSetStartValue),
41. end: LengthMetrics.px(this.OutSetEndValue)
42. },
43. repeat: this.RepeatValue[this.SelectIndex],
44. fill: this.FillValue
45. })

47. Column() {
48. Text(`borderImageSliceStart = ${this.SliceStartValue}px`)
49. Slider({
50. value: this.SliceStartValue,
51. min: 0,
52. max: 100,
53. style: SliderStyle.OutSet
54. })
55. .onChange((value: number, mode: SliderChangeMode) => {
56. this.SliceStartValue = value
57. })
58. }

60. Column() {
61. Text(`borderImageEndSliceStart = ${this.SliceEndValue}px`)
62. Slider({
63. value: this.SliceEndValue,
64. min: 0,
65. max: 100,
66. style: SliderStyle.OutSet
67. })
68. .onChange((value: number, mode: SliderChangeMode) => {
69. this.SliceEndValue = value
70. })
71. }

73. Column() {
74. Text(`borderImageWidthStart = ${this.WidthStartValue}px`)
75. Slider({
76. value: this.WidthStartValue,
77. min: 0,
78. max: 100,
79. style: SliderStyle.OutSet
80. })
81. .onChange((value: number, mode: SliderChangeMode) => {
82. this.WidthStartValue = value
83. })
84. }

86. Column() {
87. Text(`borderImageWidthEnd = ${this.WidthEndValue}px`)
88. Slider({
89. value: this.WidthEndValue,
90. min: 0,
91. max: 100,
92. style: SliderStyle.OutSet
93. })
94. .onChange((value: number, mode: SliderChangeMode) => {
95. this.WidthEndValue = value
96. })
97. }

99. Column() {
100. Text(`borderImageOutSetStart = ${this.OutSetStartValue}px`)
101. Slider({
102. value: this.OutSetStartValue,
103. min: 0,
104. max: 100,
105. style: SliderStyle.OutSet
106. })
107. .onChange((value: number, mode: SliderChangeMode) => {
108. this.OutSetStartValue = value
109. })
110. }

112. Column() {
113. Text(`borderImageOutSetEnd = ${this.OutSetEndValue}px`)
114. Slider({
115. value: this.OutSetEndValue,
116. min: 0,
117. max: 100,
118. style: SliderStyle.OutSet
119. })
120. .onChange((value: number, mode: SliderChangeMode) => {
121. this.OutSetEndValue = value
122. })
123. }

125. Row() {
126. Text('borderImageRepeat: ')
127. Select([{ value: 'Repeat' }, { value: 'Stretch' }, { value: 'Round' }, { value: 'Space' }])
128. .value(this.SelectText)
129. .selected(this.SelectIndex)
130. .onSelect((index: number, value?: string) => {
131. this.SelectIndex = index
132. this.SelectText = value as string
133. })
134. }

136. Row() {
137. Text(`borderImageFill: ${this.FillValue} `)
138. Toggle({ type: ToggleType.Switch, isOn: this.FillValue })
139. .onChange((isOn: boolean) => {
140. this.FillValue = isOn
141. })
142. }

144. }
145. .width('100%')
146. }
147. .height('100%')
148. }
149. }
```

显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/lz_alCINSsyl-r7hNZLRQg/zh-cn_image_0000002583439551.png?HW-CC-KV=V1&HW-CC-Date=20260428T000104Z&HW-CC-Expire=86400&HW-CC-Sign=BAA567D1AF0C594461FE717402204FDB099DC567740BE421A7C8EB3A34F64936)
