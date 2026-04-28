---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-shape
title: Shape
category: harmonyos-references
scraped_at: 2026-04-28T08:02:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:21b5d83451660c74ce7eb3e007a6d9a6b9f8ef0b9eab45f2e4b52c590b68a398
---

绘制组件的父组件，父组件中会描述所有绘制组件均支持的通用属性。

1、绘制组件使用Shape作为父组件，实现类似SVG的效果。

2、绘制组件单独使用，用于在页面上绘制指定的图形。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

PhonePC/2in1TabletTVWearable

包含[Rect](ts-drawing-components-rect.md)、[Path](ts-drawing-components-path.md)、[Circle](ts-drawing-components-circle.md)、[Ellipse](ts-drawing-components-ellipse.md)、[Polyline](ts-drawing-components-polyline.md)、[Polygon](ts-drawing-components-polygon.md)、[Image](ts-basic-components-image.md)、[Text](ts-basic-components-text.md)、[Column](ts-container-column.md)、[Row](ts-container-row.md)和Shape子组件。

## 接口

PhonePC/2in1TabletTVWearable

Shape(value?: PixelMap)

从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持使用PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 绘制目标，可将图形绘制在指定的PixelMap对象中，若未设置，则默认在当前绘制目标中进行绘制。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## ViewportRect18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Viewport的绘制属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x7+ | [Length](ts-types.md#length) | 否 | 是 | 形状视口起始点的水平坐标。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y7+ | [Length](ts-types.md#length) | 否 | 是 | 形状视口起始点的垂直坐标。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 形状视口的宽度，取值范围≥0。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 形状视口的高度，取值范围≥0。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### viewPort

PhonePC/2in1TabletTVWearable

viewPort(value: ViewportRect)

设置形状的视口。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ViewportRect](ts-drawing-components-shape.md#viewportrect18对象说明) | 是 | Viewport绘制属性。  默认值：{}  异常值undefined和null按照默认值处理。 |

### fill

PhonePC/2in1TabletTVWearable

fill(value: ResourceColor)

设置填充区域的颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时，后设置的属性生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 填充区域颜色。  默认值：[Color](ts-appendix-enums.md#color).Black  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### fillOpacity

PhonePC/2in1TabletTVWearable

fillOpacity(value: number | string | Resource)

设置填充区域透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 填充区域透明度。  **说明：**  number格式取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。  string格式支持number格式取值的字符串形式，取值范围与number格式相同。  Resource格式支持系统资源或者应用资源中的字符串，取值范围和number格式相同。  默认值：1.0 |

### stroke

PhonePC/2in1TabletTVWearable

stroke(value: ResourceColor)

设置边框颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 边框颜色。  默认值：[Color](ts-appendix-enums.md#color).Transparent  异常值undefined和null按照默认值处理，NaN和Infinity按照[Color](ts-appendix-enums.md#color).Black处理。 |

### strokeDashArray

PhonePC/2in1TabletTVWearable

strokeDashArray(value: Array<any>)

设置边框间隙，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。取值范围为≥0，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 定义Shape轮廓的虚线模式的数组，数组元素交替表示线段长度和间隙长度。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。  **说明：**  空数组：实线  偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->...  奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

### strokeDashOffset

PhonePC/2in1TabletTVWearable

strokeDashOffset(value: Length)

设置边框绘制起点的偏移量，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 边框绘制起点的偏移量。  默认值：0  默认单位：vp  异常值undefined和null按照默认值处理，NaN和Infinity会导致strokeDashArray失效。 |

### strokeLineCap

PhonePC/2in1TabletTVWearable

strokeLineCap(value: LineCapStyle)

设置边框端点绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LineCapStyle](ts-appendix-enums.md#linecapstyle) | 是 | 边框端点绘制样式。  默认值：LineCapStyle.Butt  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### strokeLineJoin

PhonePC/2in1TabletTVWearable

strokeLineJoin(value: LineJoinStyle)

设置边框拐角绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LineJoinStyle](ts-appendix-enums.md#linejoinstyle) | 是 | 边框拐角绘制样式。  默认值：LineJoinStyle.Miter  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### strokeMiterLimit

PhonePC/2in1TabletTVWearable

strokeMiterLimit(value: Length)

设置斜接长度与边框宽度比值的极限值，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。

该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 斜接长度与边框宽度比值的极限值。  默认值：4  异常值undefined、null和NaN按照默认值处理，Infinity会导致stroke失效。 |

### strokeOpacity

PhonePC/2in1TabletTVWearable

strokeOpacity(value: number | string | Resource)

设置边框透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 边框透明度。  默认值：[stroke](ts-drawing-components-shape.md#stroke)接口设置的透明度。  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

### strokeWidth

PhonePC/2in1TabletTVWearable

strokeWidth(value: Length)

设置边框宽度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 边框宽度，取值范围≥0。  默认值：1  默认单位：vp  异常值undefined、null和NaN按照默认值处理，Infinity按0处理。 |

### antiAlias

PhonePC/2in1TabletTVWearable

antiAlias(value: boolean)

设置是否开启抗锯齿效果，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启抗锯齿效果。  true：开启抗锯齿；false：关闭抗锯齿。  默认值：true  异常值undefined和null按照false处理。 |

### mesh8+

PhonePC/2in1TabletTVWearable

mesh(value: Array<any>, column: number, row: number)

设置网格效果。将图像分割为（row + 1）\* (column + 1)的网格，每个网格交点坐标存储在数组中（每两个元素表示一个交点的x、y坐标）。通过数组value中的坐标值，重新定位网格顶点位置，实现图像局部扭曲。支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

说明

mesh只对shape传入pixelMap时生效，且效果作用于传入的pixelMap。与[绘制模块](arkts-apis-graphics-drawing.md)的[drawPixelMapMesh12+](arkts-apis-graphics-drawing-canvas.md#drawpixelmapmesh12)效果一致，建议使用drawPixelMapMesh。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 长度（row + 1）\* （column + 1）\* 2的数组，记录扭曲后的位图各个顶点位置。  设置异常值undefined、null时value按照空数组处理，设置空数组时column和row按0处理，value按空数组处理。 |
| column | number | 是 | mesh矩阵列数。  设置异常值undefined、null、NaN和Infinity时column和row按0处理，value按空数组处理。 |
| row | number | 是 | mesh矩阵行数。  设置异常值undefined、null、NaN和Infinity时column和row按0处理，value按空数组处理。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（组件属性绘制）

通过Shape组件绘制矩形、椭圆和直线路径。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShapeExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('basic').fontSize(11).fontColor(0xCCCCCC).width(320)
8. // 在Shape的(-2, -2)点绘制一个 300 * 50 带边框的矩形,颜色0x317AF7,边框颜色黑色,边框宽度4,边框间隙20,向左偏移10,线条两端样式为半圆,拐角样式圆角,抗锯齿(默认开启)
9. // 在Shape的(-2, 58)点绘制一个 300 * 50 带边框的椭圆,颜色0x317AF7,边框颜色黑色,边框宽度4,边框间隙20,向左偏移10,线条两端样式为半圆,拐角样式圆角,抗锯齿(默认开启)
10. // 在Shape的(-2, 118)点绘制一个 300 * 10 直线路径,颜色0x317AF7,边框颜色黑色,宽度4,间隙20,向左偏移10,线条两端样式为半圆,拐角样式圆角,抗锯齿(默认开启)
11. Shape() {
12. Rect().width(300).height(50)
13. Ellipse().width(300).height(50).offset({ x: 0, y: 60 })
14. Path().width(300).height(10).commands('M0 0 L900 0').offset({ x: 0, y: 120 })
15. }
16. .width(350)
17. .height(140)
18. .viewPort({
19. x: -2,
20. y: -2,
21. width: 304,
22. height: 130
23. })
24. .fill(0x317AF7)
25. .stroke(Color.Black)
26. .strokeWidth(4)
27. .strokeDashArray([20])
28. .strokeDashOffset(10)
29. .strokeLineCap(LineCapStyle.Round)
30. .strokeLineJoin(LineJoinStyle.Round)
31. .antiAlias(true)

33. // 分别在Shape的(0, 0)、(-5, -5)点绘制一个 300 * 50 带边框的矩形,可以看出之所以将视口的起始位置坐标设为负值是因为绘制的起点默认为线宽的中点位置，因此要让边框完全显示则需要让视口偏移半个线宽
34. Shape() {
35. Rect().width(300).height(50)
36. }
37. .width(350)
38. .height(80)
39. .viewPort({
40. x: 0,
41. y: 0,
42. width: 320,
43. height: 70
44. })
45. .fill(0x317AF7)
46. .stroke(Color.Black)
47. .strokeWidth(10)

49. Shape() {
50. Rect().width(300).height(50)
51. }
52. .width(350)
53. .height(80)
54. .viewPort({
55. x: -5,
56. y: -5,
57. width: 320,
58. height: 70
59. })
60. .fill(0x317AF7)
61. .stroke(Color.Black)
62. .strokeWidth(10)

64. Text('path').fontSize(11).fontColor(0xCCCCCC).width(320)
65. // 在Shape的(0, -5)点绘制一条直线路径,颜色0xEE8443,线条宽度10,线条间隙20
66. Shape() {
67. Path().width(300).height(10).commands('M0 0 L900 0')
68. }
69. .width(350)
70. .height(20)
71. .viewPort({
72. x: 0,
73. y: -5,
74. width: 300,
75. height: 20
76. })
77. .stroke(0xEE8443)
78. .strokeWidth(10)
79. .strokeDashArray([20])

81. // 在Shape的(0, -5)点绘制一条直线路径,颜色0xEE8443,线条宽度10,线条间隙20,向左偏移10
82. Shape() {
83. Path().width(300).height(10).commands('M0 0 L900 0')
84. }
85. .width(350)
86. .height(20)
87. .viewPort({
88. x: 0,
89. y: -5,
90. width: 300,
91. height: 20
92. })
93. .stroke(0xEE8443)
94. .strokeWidth(10)
95. .strokeDashArray([20])
96. .strokeDashOffset(10)

98. // 在Shape的(0, -5)点绘制一条直线路径,颜色0xEE8443,线条宽度10,透明度0.5
99. Shape() {
100. Path().width(300).height(10).commands('M0 0 L900 0')
101. }
102. .width(350)
103. .height(20)
104. .viewPort({
105. x: 0,
106. y: -5,
107. width: 300,
108. height: 20
109. })
110. .stroke(0xEE8443)
111. .strokeWidth(10)
112. .strokeOpacity(0.5)

114. // 在Shape的(0, -5)点绘制一条直线路径,颜色0xEE8443,线条宽度10,线条间隙20,线条两端样式为半圆
115. Shape() {
116. Path().width(300).height(10).commands('M0 0 L900 0')
117. }
118. .width(350)
119. .height(20)
120. .viewPort({
121. x: 0,
122. y: -5,
123. width: 300,
124. height: 20
125. })
126. .stroke(0xEE8443)
127. .strokeWidth(10)
128. .strokeDashArray([20])
129. .strokeLineCap(LineCapStyle.Round)

131. // 在Shape的(-20, -5)点绘制一个封闭路径,颜色0x317AF7,线条宽度10,边框颜色0xEE8443,拐角样式锐角（默认值）
132. Shape() {
133. Path().width(200).height(60).commands('M0 0 L400 0 L400 150 Z')
134. }
135. .width(300)
136. .height(200)
137. .viewPort({
138. x: -20,
139. y: -5,
140. width: 310,
141. height: 90
142. })
143. .fill(0x317AF7)
144. .stroke(0xEE8443)
145. .strokeWidth(10)
146. .strokeLineJoin(LineJoinStyle.Miter)
147. .strokeMiterLimit(5)
148. }.width('100%').margin({ top: 15 })
149. }
150. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Rs2RE5W6R1WTma-1eClgcw/zh-cn_image_0000002583440061.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=275B2050464F990546240D4314733D8FB0A98B8DF3D89B6C184BA69F3FE9D2D4)

### 示例2（使用不同参数类型绘制图形）

各属性通过不同的长度类型绘制图形。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShapeTypeExample {
5. build() {
6. Column({ space: 10 }) {
7. // 在Shape的(-2, -2)点绘制一个 300 * 50 带边框的矩形,颜色0x317AF7,边框颜色黑色,边框宽度4,边框间隙20,向左偏移10,线条两端样式为半圆,拐角样式圆角,抗锯齿(默认开启)
8. // 在Shape的(-2, 58)点绘制一个 300 * 50 带边框的椭圆,颜色0x317AF7,边框颜色黑色,边框宽度4,边框间隙20,向左偏移10,线条两端样式为半圆,拐角样式圆角,抗锯齿(默认开启)
9. // 在Shape的(-2, 118)点绘制一个 300 * 10 直线路径,颜色0x317AF7,边框颜色黑色,宽度4,间隙20,向左偏移10,线条两端样式为半圆,拐角样式圆角,抗锯齿(默认开启)
10. Shape() {
11. Rect().width('300').height('50')
12. Ellipse().width(300).height(50).offset({ x: 0, y: 60 })
13. Path().width(300).height(10).commands('M0 0 L900 0').offset({ x: 0, y: 120 })
14. }
15. .width(350)
16. .height(140)
17. .viewPort({
18. x: '-2', // 使用string类型
19. y: '-2',
20. width: $r('app.string.ViewportRectWidth'), // 使用Resource类型，需用户自定义
21. height: $r('app.string.ViewportRectHeight')
22. })
23. .fill(Color.Orange)
24. .stroke(Color.Black)
25. .strokeWidth(4)
26. .strokeDashArray([20])
27. .strokeDashOffset(10) // 使用number类型
28. .strokeLineCap(LineCapStyle.Round)
29. .strokeLineJoin(LineJoinStyle.Round)
30. .strokeMiterLimit(5)
31. .antiAlias(true)
32. }.width('100%').margin({ top: 15 })
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ROzgDYYDRv6sTGKGc5fXsw/zh-cn_image_0000002552960016.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=979568667E8FBC048060958369F045D293D5ADA7B92A82378591850A5B90FC31)

### 示例3（使用attributeModifier动态设置Shape组件的属性）

以下示例展示了如何使用attributeModifier动态设置Shape组件的fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeLineJoin、strokeMiterLimit、strokeOpacity、strokeWidth和antiAlias属性。

```
1. // xxx.ets
2. class MyShapeModifier implements AttributeModifier<ShapeAttribute> {
3. applyNormalAttribute(instance: ShapeAttribute): void {
4. // 填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框间隙[20, 15]，向左偏移15，线条两端样式为半圆，拐角样式使用尖角连接路径段，斜接长度与边框宽度比值的极限值为5，边框透明度0.5，边框宽度10，抗锯齿开启
5. instance.fill("#707070")
6. instance.fillOpacity(0.5)
7. instance.stroke("#2787D9")
8. instance.strokeDashArray([20, 15])
9. instance.strokeDashOffset("15")
10. instance.strokeLineCap(LineCapStyle.Round)
11. instance.strokeLineJoin(LineJoinStyle.Miter)
12. instance.strokeMiterLimit(5)
13. instance.strokeOpacity(0.5)
14. instance.strokeWidth(10)
15. instance.antiAlias(true)
16. }
17. }

19. @Entry
20. @Component
21. struct ShapeModifierDemo {
22. @State modifier: MyShapeModifier = new MyShapeModifier()

24. build() {
25. Column() {
26. Shape() {
27. Rect().width(200).height(50).offset({ x: 20, y: 20 })
28. Ellipse().width(200).height(50).offset({ x: 20, y: 80 })
29. Path().width(200).height(10).commands('M0 0 L900 0').offset({ x: 20, y: 160 })
30. }
31. .width(250).height(200)
32. .attributeModifier(this.modifier)
33. }
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/AK1aZRm8TEuRwFH6rUEhig/zh-cn_image_0000002583480017.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=0479DDB0E3EFDE1B582B4A1F0F7DBB9D6FF39CB6ABEAC3A1F19CB69A7875C463)

### 示例4（使用mesh实现图像局部扭曲）

以下示例展示了如何使用mesh属性设置网格效果，实现图像局部扭曲。

```
1. // xxx.ets
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct Index {
7. private context: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(200, 200)
8. private meshArray: Array<number> = [0, 0, 50, 0, 410, 0, 0, 180, 50, 180, 410, 180, 0, 360, 50, 360, 410, 360]
9. @State pixelMap: image.PixelMap | undefined = undefined

11. aboutToAppear(): void {
12. // "resources/base/media/img.png"需要替换为开发者所需的图像资源文件。
13. let img: ImageBitmap = new ImageBitmap("resources/base/media/img.png")
14. this.context.drawImage(img, 0, 0, 200, 200)
15. this.pixelMap = this.context.getPixelMap(0, 0, 200, 200)
16. }

18. build() {
19. Column() {
20. Shape(this.pixelMap)
21. .backgroundColor(Color.Grey)
22. .width(250)
23. .height(250)
24. .mesh(this.meshArray, 2, 2)

26. Shape(this.pixelMap)
27. .backgroundColor(Color.Grey)
28. .width(250)
29. .height(250)
30. }
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/mVH4GWwISk2joyaqBJE-_Q/zh-cn_image_0000002552800368.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=D464CDF29BA9A4CFA632FC642ECE8DF3589ED2C3F6B3CF598C9EA1A4DB923C20)
