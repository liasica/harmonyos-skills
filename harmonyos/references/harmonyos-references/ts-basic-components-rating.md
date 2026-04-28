---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating
title: Rating
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 按钮与选择 > Rating
category: harmonyos-references
scraped_at: 2026-04-28T08:01:45+08:00
doc_updated_at: 2026-04-08
content_hash: sha256:fce2088465e276161aff4cf50fb12b5c307983a09d22831d63a95f2557bd8c26
---

提供在给定范围内选择评分的组件。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 当Rating的父节点有指定宽高时，需为Rating组件指定宽高，或为父节点设置值为true的[clip](ts-universal-attributes-sharp-clipping.md#clip18)属性。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Rating(options?: RatingOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RatingOptions](ts-basic-components-rating.md#ratingoptions18对象说明) | 否 | 设置评分组件。  未设置时，则按照RatingOptions中各参数的默认值配置。 |

## 属性

PhonePC/2in1TabletTVWearable

### stars

PhonePC/2in1TabletTVWearable

stars(value: number)

设置评分总数。设置为小于等于0的值时，按默认值显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置评分总数。  默认值：5 |

### stars18+

PhonePC/2in1TabletTVWearable

stars(starCount: Optional<number>)

设置评分总数。设置为小于等于0的值时，按默认值显示。与[stars](ts-basic-components-rating.md#stars)相比，starCount参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| starCount | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 设置评分总数。  当starCount的值为undefined时，默认值：5 |

### stepSize

PhonePC/2in1TabletTVWearable

stepSize(value: number)

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 操作评级的步长。  默认值：0.5  取值范围：[0.1, stars] |

### stepSize18+

PhonePC/2in1TabletTVWearable

stepSize(size: Optional<number>)

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。与[stepSize](ts-basic-components-rating.md#stepsize)相比，size参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 操作评级的步长。  当size的值为undefined时，默认值：0.5  取值范围：[0.1, stars] |

### starStyle

PhonePC/2in1TabletTVWearable

starStyle(options: StarStyleOptions)

设置评分的样式。该属性所支持的图片类型能力参考[Image](ts-basic-components-image.md)组件。

支持加载本地图片和网络图片，暂不支持PixelMap类型。

默认图片加载方式为异步，暂不支持同步加载。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [StarStyleOptions](ts-basic-components-rating.md#starstyleoptions18对象说明) | 是 | 评分的样式。  **说明：**  当backgroundUri、foregroundUri或secondaryUri设置的图片路径错误时，图片将保持上次的图片显示结果。如果首次设置错误，则不显示图片。  当backgroundUri或foregroundUri设置为undefined或空字符串时，Rating组件将加载系统默认星型图源。  当secondaryUri未设置或设置为undefined或空字符串时，将优先使用backgroundUri，效果等同于仅设置foregroundUri和backgroundUri。 |

### starStyle18+

PhonePC/2in1TabletTVWearable

starStyle(options: Optional<StarStyleOptions>)

设置评分的样式。该属性所支持的图片类型能力参考[Image](ts-basic-components-image.md)组件。

支持加载本地图片和网络图片，暂不支持PixelMap类型。

默认图片加载方式为异步，暂不支持同步加载。

与[starStyle](ts-basic-components-rating.md#starstyle)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[StarStyleOptions](ts-basic-components-rating.md#starstyleoptions18对象说明)> | 是 | 评分的样式。  **说明：**  当backgroundUri、foregroundUri或secondaryUri设置的图片路径错误时，图片将保持上次的图片显示结果。如果首次设置错误，则不显示图片。  当backgroundUri或foregroundUri设置为undefined或空字符串时，Rating组件将加载系统默认星型图源。  当secondaryUri未设置或设置为undefined或空字符串时，将优先使用backgroundUri，效果等同于仅设置foregroundUri和backgroundUri。 |

说明

当Rating组件的宽高为[width, height]时，单个图片的绘制区域为[width / stars, height]。

为确保绘制区域为方形，建议自定义宽高时采用[height \* stars, height]，即width = height \* stars的方式。

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<RatingConfiguration>)

定制Rating内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier<RatingConfiguration>](ts-basic-components-rating.md#ratingconfiguration12对象说明) | 是 | 在Rating组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

### contentModifier18+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: Optional<ContentModifier<RatingConfiguration>>)

定制Rating内容区的方法。与[contentModifier](ts-basic-components-rating.md#contentmodifier12)相比，modifier参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ContentModifier<RatingConfiguration>](ts-basic-components-rating.md#ratingconfiguration12对象说明)> | 是 | 在Rating组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。  当modifier的值为undefined时，不使用内容修改器。 |

## 事件

PhonePC/2in1TabletTVWearable

### onChange

PhonePC/2in1TabletTVWearable

onChange(callback:(value: number) => void)

当评分条的评星变化时触发该回调。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 评分条的评分。 |

### onChange18+

PhonePC/2in1TabletTVWearable

onChange(callback:Optional<OnRatingChangeCallback>)

当评分条的评星变化时触发该回调。与[onChange](ts-basic-components-rating.md#onchange)相比，callback参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnRatingChangeCallback](ts-basic-components-rating.md#onratingchangecallback18)> | 是 | 操作评分条的评星变化时触发该回调。  当callback的值为undefined时，不使用回调函数。 |

## OnRatingChangeCallback18+

PhonePC/2in1TabletTVWearable

type OnRatingChangeCallback = (rating: number) => void

操作评分条的评星变化时触发该回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rating | number | 是 | 评分条的评分。 |

## 键盘走焦规格

PhonePC/2in1TabletTVWearable

| 按键 | 功能描述 |
| --- | --- |
| Tab | 组件间切换焦点。 |
| 左右方向键 | 评分预览增加/减少（步长为step），不改变实际分值。 |
| Home | 移动到第一个星星， 不改变实际分值。 |
| End | 移动到最后一个星星， 不改变实际分值。 |
| Space/Enter | 根据当前评分提交评分结果。 |

## RatingConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rating | number | 否 | 否 | 设置并接收评分值。  默认值：0  取值范围： [0, stars]  小于0取0，大于[stars](ts-basic-components-rating.md#stars)取最大值stars。  该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  该参数支持[!!](../harmonyos-guides/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。 |
| indicator | boolean | 否 | 否 | 评分条是否作为指示器使用。当值为true时，表示作为指示器；当值为false时，表示不作为指示器。  默认值：false |
| stars | number | 否 | 否 | 评分条的星级总数。  默认值：5 |
| stepSize | number | 否 | 否 | 评分条的评分步长。  默认值：0.5 |
| triggerChange | Callback<number> | 否 | 否 | 触发评分数量变化。 |

## RatingOptions18+对象说明

PhonePC/2in1TabletTVWearable

评分组件的信息。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rating7+ | number | 否 | 否 | 设置并接收评分值。  默认值：0  取值范围： [0, stars]  小于0取0，大于[stars](ts-basic-components-rating.md#stars)取最大值stars。  该参数支持[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定变量。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| indicator7+ | boolean | 否 | 是 | 设置评分组件作为指示器使用，值为true时，不可改变评分。  默认值：false，可进行评分  **说明：**  indicator=true时，默认组件高度height=12.0vp，组件width=height \* stars。  indicator=false时，默认组件高度height=28.0vp，组件width=height \* stars。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## StarStyleOptions18+对象说明

PhonePC/2in1TabletTVWearable

评分组件选中、未选中以及部分选中的星级样式。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| backgroundUri7+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 未选中的星级的图片链接，可由用户自定义或使用系统默认图片。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，该接口支持设置Resource资源。参考[示例3（通过Resource资源设置评分的样式）](ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)代码。 |
| foregroundUri7+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 选中的星级的图片路径，可由用户自定义或使用系统默认图片。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，该接口支持设置Resource资源。参考[示例3（通过Resource资源设置评分的样式）](ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)代码。 |
| secondaryUri7+ | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 部分选中的星级的图片路径，可由用户自定义或使用系统默认图片。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  从API version 20开始，该接口支持设置Resource资源。参考[示例3（通过Resource资源设置评分的样式）](ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)代码。 |

说明

string格式可用于加载网络图片和本地图片。当使用相对路径引用本地图片时，例如Image("common/test.jpg")，其中common目录与pages同级，同时支持Base64字符串。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置默认评分样式）

以下示例展示了如何创建默认星型评分样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RatingExample {
5. @State rating: number = 3.5;

7. build() {
8. Column() {
9. Column() {
10. Rating({ rating: this.rating, indicator: false })
11. .stars(5)
12. .stepSize(0.5)
13. .margin({ top: 24 })
14. .onChange((value: number) => {
15. this.rating = value;
16. })
17. Text('current score is ' + this.rating)
18. .fontSize(16)
19. .fontColor('rgba(24,36,49,0.60)')
20. .margin({ top: 16 })
21. }.width(360).height(113).backgroundColor('#FFFFFF').margin({ top: 68 })

23. Row() {
24. Image('common/testImage.jpg')
25. .width(40)
26. .height(40)
27. .borderRadius(20)
28. .margin({ left: 24 })
29. Column() {
30. Text('Yue')
31. .fontSize(16)
32. .fontColor('#182431')
33. .fontWeight(500)
34. Row() {
35. Rating({ rating: 3.5, indicator: false }).margin({ top: 1, right: 8 })
36. Text('2021/06/02')
37. .fontSize(10)
38. .fontColor('#182431')
39. }
40. }.margin({ left: 12 }).alignItems(HorizontalAlign.Start)

42. Text('1st Floor')
43. .fontSize(10)
44. .fontColor('#182431')
45. .position({ x: 295, y: 8 })
46. }.width(360).height(56).backgroundColor('#FFFFFF').margin({ top: 64 })
47. }.width('100%').height('100%').backgroundColor('#F1F3F5')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/lOuU39mcT2KB40NnBtkF-A/zh-cn_image_0000002583479721.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000143Z&HW-CC-Expire=86400&HW-CC-Sign=7E6B3291D296AA551D8C4AFE87EFC2A5F0F4FE7911BA508C9B85B9F641DDD8C3)

### 示例2（自定义评分条）

以下示例实现了自定义评分条的功能，其中每个圆圈表示0.5分。当ratingIndicator为true时，评分条作为指示器使用，不可改变评分；当为false时，可进行评分。ratingStars用于设置评分总数，ratingStepsize用于设置评分步长。

```
1. // xxx.ets
2. class MyRatingStyle implements ContentModifier<RatingConfiguration> {
3. name: string = "";
4. style: number = 0;

6. constructor(value1: string, value2: number) {
7. this.name = value1;
8. this.style = value2;
9. }

11. applyContent(): WrappedBuilder<[RatingConfiguration]> {
12. return wrapBuilder(buildRating);
13. }
14. }

16. @Builder
17. function buildRating(config: RatingConfiguration) {
18. Column() {
19. Row() {
20. Circle({ width: 25, height: 25 })
21. .fill(config.rating >= 0.4 ? Color.Black : Color.Red)
22. .onClick((event: ClickEvent) => {
23. if (!config.indicator) {
24. if (config.stepSize === 0.5) {
25. config.triggerChange(0.5);
26. return
27. }
28. if (config.stepSize === 1.0) {
29. config.triggerChange(1);
30. return
31. }
32. }
33. }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)
34. Circle({ width: 25, height: 25 })
35. .fill(config.rating >= 0.9 ? Color.Black : Color.Red)
36. .onClick((event: ClickEvent) => {
37. if (!config.indicator) {
38. config.triggerChange(1);
39. }
40. }).visibility(config.stars >= 1 ? Visibility.Visible : Visibility.Hidden)
41. Circle({ width: 25, height: 25 })
42. .fill(config.rating >= 1.4 ? Color.Black : Color.Red)
43. .onClick((event: ClickEvent) => {
44. if (!config.indicator) {
45. if (config.stepSize === 0.5) {
46. config.triggerChange(1.5);
47. return
48. }
49. if (config.stepSize === 1.0) {
50. config.triggerChange(2);
51. return
52. }
53. }
54. }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
55. Circle({ width: 25, height: 25 })
56. .fill(config.rating >= 1.9 ? Color.Black : Color.Red)
57. .onClick((event: ClickEvent) => {
58. if (!config.indicator) {
59. config.triggerChange(2);
60. }
61. }).visibility(config.stars >= 2 ? Visibility.Visible : Visibility.Hidden)
62. Circle({ width: 25, height: 25 })
63. .fill(config.rating >= 2.4 ? Color.Black : Color.Red)
64. .onClick((event: ClickEvent) => {
65. if (!config.indicator) {
66. if (config.stepSize === 0.5) {
67. config.triggerChange(2.5);
68. return
69. }
70. if (config.stepSize === 1.0) {
71. config.triggerChange(3);
72. return
73. }
74. }
75. }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
76. Circle({ width: 25, height: 25 })
77. .fill(config.rating >= 2.9 ? Color.Black : Color.Red)
78. .onClick((event: ClickEvent) => {
79. if (!config.indicator) {
80. config.triggerChange(3);
81. }
82. }).visibility(config.stars >= 3 ? Visibility.Visible : Visibility.Hidden)
83. Circle({ width: 25, height: 25 })
84. .fill(config.rating >= 3.4 ? Color.Black : Color.Red)
85. .onClick((event: ClickEvent) => {
86. if (!config.indicator) {
87. if (config.stepSize === 0.5) {
88. config.triggerChange(3.5);
89. return
90. }
91. if (config.stepSize === 1.0) {
92. config.triggerChange(4);
93. return
94. }
95. }
96. }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
97. Circle({ width: 25, height: 25 })
98. .fill(config.rating >= 3.9 ? Color.Black : Color.Red)
99. .onClick((event: ClickEvent) => {
100. if (!config.indicator) {
101. config.triggerChange(4);
102. }
103. }).visibility(config.stars >= 4 ? Visibility.Visible : Visibility.Hidden)
104. Circle({ width: 25, height: 25 })
105. .fill(config.rating >= 4.4 ? Color.Black : Color.Red)
106. .onClick((event: ClickEvent) => {
107. if (!config.indicator) {
108. if (config.stepSize === 0.5) {
109. config.triggerChange(4.5);
110. return
111. }
112. if (config.stepSize === 1.0) {
113. config.triggerChange(5);
114. return
115. }
116. }
117. }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden).margin({ left: 10 })
118. Circle({ width: 25, height: 25 })
119. .fill(config.rating >= 4.9 ? Color.Black : Color.Red)
120. .onClick((event: ClickEvent) => {
121. if (!config.indicator) {
122. config.triggerChange(5);
123. }
124. }).visibility(config.stars >= 5 ? Visibility.Visible : Visibility.Hidden)
125. }

127. Text("分值：" + config.rating)
128. }
129. }

131. @Entry
132. @Component
133. struct ratingExample {
134. @State rating: number = 0;
135. @State ratingIndicator: boolean = true;
136. @State ratingStars: number = 0;
137. @State ratingStepSize: number = 0.5;
138. @State ratingEnabled: boolean = true;

140. build() {
141. Row() {
142. Column() {
143. Rating({
144. rating: 0,
145. indicator: this.ratingIndicator
146. })
147. .stepSize(this.ratingStepSize)
148. .stars(this.ratingStars)
149. .backgroundColor(Color.Transparent)
150. .width('100%')
151. .height(50)
152. .onChange((value: number) => {
153. console.info('Rating change is' + value);
154. this.rating = value;
155. })
156. .contentModifier(new MyRatingStyle("hello", 3))
157. Button(this.ratingIndicator ? "ratingIndicator : true" : "ratingIndicator : false")
158. .onClick((event) => {
159. if (this.ratingIndicator) {
160. this.ratingIndicator = false;
161. } else {
162. this.ratingIndicator = true;
163. }
164. }).margin({ top: 5 })

166. Button(this.ratingStars < 5 ? "ratingStars + 1, ratingStars =" + this.ratingStars : "ratingStars最大值为5")
167. .onClick((event) => {
168. if (this.ratingStars < 5) {
169. this.ratingStars += 1;
170. }
171. }).margin({ top: 5 })

173. Button(this.ratingStars > 0 ? "ratingStars - 1, ratingStars =" + this.ratingStars :
174. "ratingStars小于等于0时默认等于5")
175. .onClick((event) => {
176. if (this.ratingStars > 0) {
177. this.ratingStars -= 1;
178. }
179. }).margin({ top: 5 })

181. Button(this.ratingStepSize == 0.5 ? "ratingStepSize : 0.5" : "ratingStepSize : 1")
182. .onClick((event) => {
183. if (this.ratingStepSize == 0.5) {
184. this.ratingStepSize = 1;
185. } else {
186. this.ratingStepSize = 0.5;
187. }
188. }).margin({ top: 5 })
189. }
190. .width('100%')
191. .height('100%')
192. .justifyContent(FlexAlign.Center)
193. }
194. .height('100%')
195. }
196. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/aZ-PJ9AsTIGfiJUIaD9Rog/zh-cn_image_0000002552800072.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000143Z&HW-CC-Expire=86400&HW-CC-Sign=55D0567B164F5081C7427E59EA7B9A0D2FFFEECB8581942589BDB1EA443E176E)

### 示例3（通过Resource资源设置评分的样式）

该示例通过Resource资源配置starStyle，实现自定义星级图片链接，API version 20之后推荐使用该方法设置样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RatingExample {
5. @State rating: number = 3.5;

7. build() {
8. Column() {
9. Rating({ rating: this.rating, indicator: false })
10. .stars(5)
11. .stepSize(0.5)
12. .starStyle({
13. // $r('app.media.xxx')需要替换为开发者所需的图像资源文件。
14. backgroundUri: $r('app.media.imag1'),
15. foregroundUri: $r('app.media.imag2'),
16. secondaryUri: $r('app.media.imag3')
17. })
18. .margin({ top: 24 })
19. .onChange((value: number) => {
20. this.rating = value;
21. })
22. Text('current score is ' + this.rating)
23. .fontSize(16)
24. .fontColor('rgba(24,36,49,0.60)')
25. .margin({ top: 16 })
26. }.width('100%').height('100%').backgroundColor('#F1F3F5')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/TCUVwgkfRn6Vs13qQlZ9bg/zh-cn_image_0000002583439767.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000143Z&HW-CC-Expire=86400&HW-CC-Sign=E77D3801B3EF24C765661AC39BB188E279F80F213966F083CE6795E4CB6E2FAB)

### 示例4（设置评分的样式）

以下示例展示了如何通过配置starStyle实现自定义星级的图片链接。

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2开始，新建工程或者模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOptions > resOptions > copyCodeResource > enable设置为true，详见[resOptions](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)中相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RatingExample {
5. @State rating: number = 3.5;

7. build() {
8. Column() {
9. Rating({ rating: this.rating, indicator: false })
10. .stars(5)
11. .stepSize(0.5)
12. .starStyle({
13. backgroundUri: '/common/image1.png', // common目录与pages同级
14. foregroundUri: '/common/image2.png',
15. secondaryUri: '/common/image3.png'
16. })
17. .margin({ top: 24 })
18. .onChange((value: number) => {
19. this.rating = value;
20. })
21. Text('current score is ' + this.rating)
22. .fontSize(16)
23. .fontColor('rgba(24,36,49,0.60)')
24. .margin({ top: 16 })
25. }.width('100%').height('100%').backgroundColor('#F1F3F5')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/6LKxQqCxTX6KYqFFDlQNYw/zh-cn_image_0000002583439767.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000143Z&HW-CC-Expire=86400&HW-CC-Sign=672EA588F24E91D23F89A6865A5B92EBD961B82ED3A673391F38F8A57908BA28)
