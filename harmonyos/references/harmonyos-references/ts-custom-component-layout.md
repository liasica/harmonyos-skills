---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-layout
title: 自定义组件的自定义布局
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件的自定义布局
category: harmonyos-references
scraped_at: 2026-04-28T08:02:30+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:be5a95beddf27c651dba13841b6b350d5dbbd0658aba14e7af421050d5e20574
---

自定义组件的自定义布局通过数据计算的方式布局自定义组件内的子组件。

说明

本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

在自定义组件内实现onMeasureSize, onPlaceChildren任一方法即视为实现自定义布局，推荐同时实现两种方法，具体参数说明可见对应接口参数说明。

从API version 20开始，在自定义布局的自定义组件中，子组件若设置了[LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15)对象的fixAtIdealSize属性，表示尺寸将不受父组件约束，完全按照开发者自定义的尺寸范围布局。

自定义布局内不支持使用懒加载(包含[Repeat](../harmonyos-guides/arkts-new-rendering-control-repeat.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md))。

## onMeasureSize10+

PhonePC/2in1TabletTVWearable

onMeasureSize?(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions): SizeResult

ArkUI框架会在自定义组件确定尺寸时，将该自定义组件的节点信息和尺寸范围通过onMeasureSize传递给该开发者。不允许在onMeasureSize函数中改变状态变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selfLayoutInfo | [GeometryInfo](ts-custom-component-layout.md#geometryinfo10) | 是 | 计算自定义组件大小后的自身布局信息。  **说明：**  第一次布局时以自身设置的属性为准。 |
| children | Array<[Measurable](ts-custom-component-layout.md#measurable10)> | 是 | 计算子组件大小后的子组件布局信息。  **说明：**  如果没有设置子组件的布局信息，子组件会维持上一次的布局信息，当子组件从来没有设置过尺寸时，尺寸默认为0。 |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 自定义组件的布局约束信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SizeResult](ts-custom-component-layout.md#sizeresult10) | 组件尺寸信息。 |

## onPlaceChildren10+

PhonePC/2in1TabletTVWearable

onPlaceChildren?(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions): void

ArkUI框架会在自定义组件确定位置时，将该自定义组件的子节点自身的尺寸范围通过onPlaceChildren传递给该自定义组件。不允许在onPlaceChildren函数中改变状态变量。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| selfLayoutInfo | [GeometryInfo](ts-custom-component-layout.md#geometryinfo10) | 是 | 计算自定义组件大小后的自身布局信息。 |
| children | Array<[Layoutable](ts-custom-component-layout.md#layoutable10)> | 是 | 计算子组件大小后的子组件布局信息。 |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 自定义组件的布局约束信息。 |

**示例：**

示例请参考[自定义布局代码示例](ts-custom-component-layout.md#示例)。

## GeometryInfo10+

PhonePC/2in1TabletTVWearable

父组件（自定义组件）布局信息，继承自[SizeResult](ts-custom-component-layout.md#sizeresult10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| borderWidth | [EdgeWidth](ts-types.md#edgewidths9) | 否 | 否 | 父组件（自定义组件）边框宽度。  单位：vp。 |
| margin | [Margin](ts-types.md#margin) | 否 | 否 | 父组件（自定义组件）margin信息。  单位：vp。 |
| padding | [Padding](ts-types.md#padding) | 否 | 否 | 父组件（自定义组件）padding信息。  单位：vp。 |

## Layoutable10+

PhonePC/2in1TabletTVWearable

子组件布局信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| measureResult | [MeasureResult](ts-custom-component-layout.md#measureresult10) | 否 | 否 | 子组件测量后的尺寸信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  单位：vp |
| uniqueId18+ | number | 否 | 是 | 系统为子组件分配的唯一标识UniqueID。  取值范围[0,+∞)。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

### layout10+

PhonePC/2in1TabletTVWearable

layout(position: Position): void

调用此方法对子组件的位置信息进行限制。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](ts-types.md#position) | 是 | 绝对位置。 |

### getMargin12+

PhonePC/2in1TabletTVWearable

getMargin(): DirectionalEdgesT<number>

调用此方法获取子组件的margin信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DirectionalEdgesT<number>](ts-types.md#directionaledgestt12) | 子组件的margin信息。 |

### getPadding12+

PhonePC/2in1TabletTVWearable

getPadding(): DirectionalEdgesT<number>

调用此方法获取子组件的padding信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DirectionalEdgesT<number>](ts-types.md#directionaledgestt12) | 子组件的padding信息。 |

### getBorderWidth12+

PhonePC/2in1TabletTVWearable

getBorderWidth(): DirectionalEdgesT<number>

调用此方法获取子组件的borderWidth信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DirectionalEdgesT<number>](ts-types.md#directionaledgestt12) | 子组件的borderWidth信息。 |

## Measurable10+

PhonePC/2in1TabletTVWearable

子组件位置信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uniqueId18+ | number | 否 | 是 | 系统为子组件分配的唯一标识UniqueID。 |

### measure

PhonePC/2in1TabletTVWearable

measure(constraint: ConstraintSizeOptions) : MeasureResult

调用此方法限制子组件的尺寸范围。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 约束尺寸。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [MeasureResult](ts-custom-component-layout.md#measureresult10) | 测量后的组件布局信息。 |

### getMargin12+

PhonePC/2in1TabletTVWearable

getMargin(): DirectionalEdgesT<number>

获取子组件的margin信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DirectionalEdgesT<number>](ts-types.md#directionaledgestt12) | 子组件的margin信息。 |

### getPadding12+

PhonePC/2in1TabletTVWearable

getPadding(): DirectionalEdgesT<number>

获取子组件的padding信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DirectionalEdgesT<number>](ts-types.md#directionaledgestt12) | 子组件的padding信息。 |

### getBorderWidth12+

PhonePC/2in1TabletTVWearable

getBorderWidth(): DirectionalEdgesT<number>

获取子组件的borderWidth信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DirectionalEdgesT<number>](ts-types.md#directionaledgestt12) | 子组件的borderWidth信息。 |

## MeasureResult10+

PhonePC/2in1TabletTVWearable

测量后的组件布局信息。继承自[SizeResult](ts-custom-component-layout.md#sizeresult10)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## SizeResult10+

PhonePC/2in1TabletTVWearable

组件尺寸信息。

说明

* 自定义布局暂不支持LazyForEach写法。
* 使用builder形式的自定义布局创建，自定义组件的build()方法内只允许存在this.builder()，即示例的推荐用法。
* 父容器（自定义组件）上设置的尺寸信息，除aspectRatio之外，优先级小于onMeasureSize设置的尺寸信息。
* 子组件设置的位置信息，offset、position、markAnchor优先级大于onPlaceChildren设置的位置信息，其他位置设置属性不生效。
* 使用自定义布局方法时，需要同时调用onMeasureSize和onPlaceChildren方法，否则可能出现布局异常。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | 测量后的宽。  单位：vp。 |
| height | number | 否 | 否 | 测量后的高。  单位：vp。 |

## onLayout(deprecated)

PhonePC/2in1TabletTVWearable

onLayout?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void

ArkUI框架会在自定义组件布局时，将该自定义组件的子节点信息和自身的尺寸范围通过onLayout传递给该自定义组件。不允许在onLayout函数中改变状态变量。

说明

从API version 9开始支持，从API version 10开始废弃，推荐使用[onPlaceChildren](ts-custom-component-layout.md#onplacechildren10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| children | Array<[LayoutChild](ts-custom-component-layout.md#layoutchilddeprecated)> | 是 | 子组件布局信息。 |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 父组件constraint信息。 |

## onMeasure(deprecated)

PhonePC/2in1TabletTVWearable

onMeasure?(children: Array<LayoutChild>, constraint: ConstraintSizeOptions): void

ArkUI框架会在自定义组件确定尺寸时，将该自定义组件的子节点信息和自身的尺寸范围通过onMeasure传递给该自定义组件。不允许在onMeasure函数中改变状态变量。

说明

从API version 9开始支持，从API version 10开始废弃，推荐使用[onMeasureSize](ts-custom-component-layout.md#onmeasuresize10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| children | Array<[LayoutChild](ts-custom-component-layout.md#layoutchilddeprecated)> | 是 | 子组件布局信息。 |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 父组件constraint信息。 |

## LayoutChild(deprecated)

PhonePC/2in1TabletTVWearable

子组件布局信息。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[Measurable](ts-custom-component-layout.md#measurable10)或者[Layoutable](ts-custom-component-layout.md#layoutable10)替代。

### 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 子组件名称。 |
| id | string | 否 | 否 | 子组件id。 |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 否 | 否 | 子组件约束尺寸。 |
| borderInfo | [LayoutBorderInfo](ts-custom-component-layout.md#layoutborderinfodeprecated) | 否 | 否 | 子组件border信息。 |
| position | [Position](ts-types.md#position) | 否 | 否 | 子组件位置坐标。 |

### measure(deprecated)

PhonePC/2in1TabletTVWearable

measure(childConstraint: ConstraintSizeOptions)

调用此方法对子组件的尺寸范围进行限制。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[Measurable](ts-custom-component-layout.md#measurable10)或者[Layoutable](ts-custom-component-layout.md#layoutable10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| childConstraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 子组件的尺寸范围的约束信息。 |

### layout(deprecated)

PhonePC/2in1TabletTVWearable

layout(childLayoutInfo: LayoutInfo)

调用此方法对子组件的位置信息进行限制。

说明

从API version 9开始支持，从API version 10开始废弃，建议使用[Measurable](ts-custom-component-layout.md#measurable10)或者[Layoutable](ts-custom-component-layout.md#layoutable10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| childLayoutInfo | [LayoutInfo](ts-custom-component-layout.md#layoutinfodeprecated) | 是 | 子组件layout信息。 |

## LayoutBorderInfo(deprecated)

PhonePC/2in1TabletTVWearable

子组件border信息。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[getBorderWidth](ts-custom-component-layout.md#getborderwidth12)，[getMargin](ts-custom-component-layout.md#getmargin12)和[getPadding](ts-custom-component-layout.md#getpadding12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| borderWidth | [EdgeWidths](ts-types.md#edgewidths9) | 否 | 否 | 边框宽度类型，用于描述组件边框不同方向的宽度。 |
| margin | [Margin](ts-types.md#margin) | 否 | 否 | 外边距类型，用于描述组件不同方向的外边距。 |
| padding | [Padding](ts-types.md#padding) | 否 | 否 | 内边距类型，用于描述组件不同方向的内边距。 |

## LayoutInfo(deprecated)

PhonePC/2in1TabletTVWearable

子组件layout信息。

说明

从API version 9开始支持，从API version 10开始废弃。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [Position](ts-types.md#position) | 否 | 否 | 子组件位置坐标。 |
| constraint | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 否 | 否 | 子组件约束尺寸。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（自定义布局代码示例）

自定义布局代码示例。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. CustomLayout({ builder: ColumnChildren })
8. }
9. }
10. }

12. @Builder
13. function ColumnChildren() {
14. ForEach([1, 2, 3], (index: number) => { // 目前不支持使用lazyForEach语法。
15. Text('S' + index)
16. .fontSize(30)
17. .width(100)
18. .height(100)
19. .borderWidth(2)
20. .offset({ x: 10, y: 20 })
21. })
22. }

24. @Component
25. struct CustomLayout {
26. @Builder
27. doNothingBuilder() {
28. };

30. @BuilderParam builder: () => void = this.doNothingBuilder;
31. @State startSize: number = 100;
32. result: SizeResult = {
33. width: 0,
34. height: 0
35. };

37. onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
38. let startPos = 300;
39. children.forEach((child) => {
40. let pos = startPos - child.measureResult.height;
41. child.layout({ x: pos, y: pos })
42. })
43. }

45. onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
46. let size = 100;
47. children.forEach((child) => {
48. let result: MeasureResult = child.measure({
49. minHeight: size,
50. minWidth: size,
51. maxWidth: size,
52. maxHeight: size
53. })
54. size += result.width / 2;
55. })
56. this.result.width = 100;
57. this.result.height = 400;
58. return this.result;
59. }

61. build() {
62. this.builder()
63. }
64. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/-ERBwH8fR2aYyxi3O1z-og/zh-cn_image_0000002552800442.png?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=194B0626FF642EC7852BB62A7AB59B31C0650416053976EAC4DC1AC450E65665)

### 示例2（判断是否参与布局计算）

通过组件的位置灵活判断是否参与布局计算。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. CustomLayout({ builder: ColumnChildren })
8. }
9. .justifyContent(FlexAlign.Center)
10. .width('100%')
11. .height('100%')
12. }
13. }

15. @Builder
16. function ColumnChildren() {
17. ForEach([1, 2, 3], (item: number, index: number) => { // 目前不支持使用lazyForEach语法。
18. Text('S' + item)
19. .fontSize(20)
20. .width(60 + 10 * index)
21. .height(100)
22. .borderWidth(2)
23. .margin({ left:10 })
24. .padding(10)
25. })
26. }

28. @Component
29. struct CustomLayout {
30. // 只布局一行，如果布局空间不够的子组件不显示的demo。
31. @Builder
32. doNothingBuilder() {
33. };

35. @BuilderParam builder: () => void = this.doNothingBuilder;
36. result: SizeResult = {
37. width: 0,
38. height: 0
39. };
40. overFlowIndex: number = -1;

42. onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
43. let currentX = 0;
44. let infinity = 100000;
45. if (this.overFlowIndex == -1) {
46. this.overFlowIndex = children.length;
47. }
48. for (let index = 0; index < children.length; ++index) {
49. let child = children[index];
50. if (index >= this.overFlowIndex) {
51. // 如果子组件超出父组件范围，将它布局到较偏的位置，达到不显示的目的。
52. child.layout({x: infinity, y: 0});
53. continue;
54. }
55. child.layout({ x: currentX, y: 0 })
56. let margin = child.getMargin();
57. currentX += child.measureResult.width + margin.start + margin.end;
58. }
59. }

61. onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
62. let width = 0;
63. let height = 0;
64. this.overFlowIndex = -1;
65. // 假定该组件的宽度不能超过200vp，也不能超过最大约束。
66. let maxWidth = Math.min(200, constraint.maxWidth as number);
67. for (let index = 0; index < children.length; ++index) {
68. let child = children[index];
69. let childResult: MeasureResult = child.measure({
70. minHeight: constraint.minHeight,
71. minWidth: constraint.minWidth,
72. maxWidth: constraint.maxWidth,
73. maxHeight: constraint.maxHeight
74. })
75. let margin = child.getMargin();
76. let newWidth = width + childResult.width + margin.start + margin.end;
77. if (newWidth > maxWidth) {
78. // 记录不该布局的组件的下标。
79. this.overFlowIndex = index;
80. break;
81. }
82. // 累积父组件的宽度和高度。
83. width = newWidth;
84. height = Math.max(height, childResult.height + margin.top + margin.bottom);
85. }
86. this.result.width = width;
87. this.result.height = height;
88. return this.result;
89. }

91. build() {
92. this.builder()
93. }
94. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/TxJSovitSPGdGseoJ-UENg/zh-cn_image_0000002583440137.png?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=80B1B12FA0A478F01D494D91DC5BDA4593A4F5AA771300E60AA1677D03C50893)

### 示例3（获取子组件FrameNode并设置相关属性）

通过uniqueId获取子组件的[FrameNode](js-apis-arkui-framenode.md)，并调用FrameNode的API接口修改尺寸、背景颜色。

```
1. import { FrameNode, NodeController } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. CustomLayout()
8. }
9. }
10. }

12. class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;
14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext)
16. return this.rootNode
17. }
18. }

20. @Component
21. struct CustomLayout {
22. @Builder
23. childrenBuilder() {
24. ForEach([1, 2, 3], (index: number) => { // 目前不支持使用lazyForEach语法。
25. NodeContainer(new MyNodeController())
26. })
27. };

29. @BuilderParam builder: () => void = this.childrenBuilder;
30. result: SizeResult = {
31. width: 0,
32. height: 0
33. };

35. onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
36. let prev = 0;
37. children.forEach((child) => {
38. let pos = prev + 10;
39. prev = pos + child.measureResult.width
40. child.layout({ x: pos, y: 0 })
41. })
42. }

44. onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
45. let size = 100;
46. children.forEach((child) => {
47. console.info('child uniqueId: ', child.uniqueId)
48. const uiContext = this.getUIContext()
49. if (uiContext) {
50. let node: FrameNode | null = uiContext.getFrameNodeByUniqueId(child.uniqueId) // 获取NodeContainer组件的FrameNode。
51. if (node) {
52. node.getChild(0)!.commonAttribute.width(100)
53. node.getChild(0)!.commonAttribute.height(100)
54. node.getChild(0)!.commonAttribute.backgroundColor(Color.Pink) // 修改FrameNode的尺寸与背景颜色。
55. }
56. }
57. child.measure({ minHeight: size, minWidth: size, maxWidth: size, maxHeight: size })
58. })
59. this.result.width = 320;
60. this.result.height = 100;
61. return this.result;
62. }

64. build() {
65. this.builder()
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/5-mhhfV8ScOdmYVkHdeT8g/zh-cn_image_0000002552960092.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=9F9D3837850076AD918AF7F0F721F69BBA94F24B31F67F11D5E4EB99056EAFC7)

### 示例4（子组件超过父组件大小约束）

在自定义布局的自定义组件中，为子组件设置了[LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15)对象的fixAtIdealSize属性。

```
1. @Entry
2. @Component
3. struct Index {
4. @Builder
5. ColumnChildrenText() {
6. Text('=====Text=====Text=====Text=====Text=====Text=====Text=====Text=====Text' )
7. .fontSize(16).fontColor(Color.Black)
8. .borderWidth(2).backgroundColor('#fff8dc')
9. .width(LayoutPolicy.fixAtIdealSize) // 设置子组件宽度不受到父组件限制。
10. .height(LayoutPolicy.fixAtIdealSize)  // 设置子组件高度不受到父组件限制。
11. }

13. build() {
14. Column() {
15. Column() {
16. CustomLayoutText({ builder: this.ColumnChildrenText })
17. .backgroundColor('#f0ffff').borderRadius(20).margin(10)
18. }
19. .width(300)
20. .height(150)
21. .margin(10)
22. .backgroundColor(Color.Pink)
23. }
24. .width(350)
25. .height(680)
26. .margin(20)
27. .alignItems(HorizontalAlign.Center)
28. }
29. }

31. @Component
32. struct CustomLayoutText {
33. @Builder
34. doSomethingBuilder() {
35. };

37. @BuilderParam
38. builder: () => void = this.doSomethingBuilder;
39. result: SizeResult = {
40. width: 0,
41. height: 0
42. };
43. // 自定义组件进行自定义布局。
44. onPlaceChildren(selfLayoutInfo: GeometryInfo, children: Array<Layoutable>, constraint: ConstraintSizeOptions) {
45. let posY = 20;
46. children.forEach((child) => {
47. let posX = (selfLayoutInfo.width - child.measureResult.width) / 2;
48. child.layout({ x: posX, y: posY })
49. posY += child.measureResult.height + 30;
50. })
51. }

53. onMeasureSize(selfLayoutInfo: GeometryInfo, children: Array<Measurable>, constraint: ConstraintSizeOptions) {
54. children.forEach((child) => {
55. let result: MeasureResult = child.measure({ maxWidth: 335, maxHeight: 50 }) // 设置自定义组件子组件大小的限制。
56. })
57. this.result.width = 200;
58. this.result.height = 130;
59. return this.result;
60. }

62. build() {
63. this.builder()
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/tlzU02b3SEOSD58SVWghZw/zh-cn_image_0000002583480093.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000229Z&HW-CC-Expire=86400&HW-CC-Sign=426F51C319D209937FCF13646B7F226D15F24E71D8B3DF1720457BE45EDC755D)
