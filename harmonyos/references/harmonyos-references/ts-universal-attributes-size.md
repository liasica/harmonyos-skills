---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-size
title: 尺寸设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 尺寸设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:15+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:5722bad09ff4b20a8a3b09bdb6de0f49f506666a0492d0c27ed37f0a2ab26028
---

设置组件的宽高、边距。

说明

* 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 如果组件的尺寸通过百分比进行设置， 在计算组件尺寸的百分比大小时，参考最近设置了固定大小的祖先节点的尺寸。
* 从API version 10开始，尺寸设置内部分属性支持使用calc计算特性，具体支持属性请参考对应的属性说明。calc计算特性是一种动态计算长度值的函数，常用于灵活设置布局尺寸（如宽度、高度、边距等）。它允许通过数学表达式组合不同单位和数值，支持通过加减乘除括号运算符组成计算表达式，实现动态响应式设计。注意，在使用calc时，运算符与数值之间需要使用空格隔开。具体使用场景可见[示例1](ts-universal-attributes-size.md#示例1设置组件的宽高和边距)。

## width

PhonePC/2in1TabletTVWearable

width(value: Length): T

设置组件自身的宽度，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会超出父组件的范围。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 要设置的组件宽度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

* 在[TextInput](ts-basic-components-textinput.md)组件中，width设置auto表示自适应文本宽度。
* 在[AlphabetIndexer](ts-container-alphabet-indexer.md)组件中，width设置auto表示自适应宽度最大索引项的宽度。

## height

PhonePC/2in1TabletTVWearable

height(value: Length): T

设置组件自身的高度，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会超出父组件的范围。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 要设置的组件高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

在[Row](ts-container-row.md)、[Column](ts-container-column.md)、[RelativeContainer](ts-container-relativecontainer.md)组件中，width、height设置auto表示自适应子组件。

## width15+

PhonePC/2in1TabletTVWearable

width(widthValue: Length | LayoutPolicy): T

设置组件自身的宽度或水平方向布局策略，缺省时使用元素自身内容需要的宽度。若子组件的宽大于父组件的宽，则会超出父组件的范围。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| widthValue | [Length](ts-types.md#length) | [LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15) | 是 | 要设置的组件宽度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## height15+

PhonePC/2in1TabletTVWearable

height(heightValue: Length | LayoutPolicy): T

设置组件自身的高度或垂直方向布局策略，缺省时使用元素自身内容需要的高度。若子组件的高大于父组件的高，则会超出父组件的范围。

**卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| heightValue | [Length](ts-types.md#length) | [LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15) | 是 | 要设置的组件高度。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## size

PhonePC/2in1TabletTVWearable

size(value: SizeOptions): T

设置组件自身的宽高尺寸。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](ts-types.md#sizeoptions) | 是 | 设置宽高尺寸。  异常值：参数为undefined时，属性设置不生效；其它异常值时，size属性恢复到不配置时的默认行为。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## padding

PhonePC/2in1TabletTVWearable

padding(value: Padding | Length | LocalizedPadding): T

设置组件的内边距属性。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Padding](ts-types.md#padding) | [Length](ts-types.md#length) | [LocalizedPadding](ts-types.md#localizedpadding12)12+ | 是 | 设置组件的内边距。  参数为Length类型时，四个方向内边距同时生效。  默认值：0  单位：vp  padding设置百分比时，上下左右内边距均以父容器的width作为基础值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## margin

PhonePC/2in1TabletTVWearable

margin(value: Margin | Length | LocalizedMargin): T

设置组件的外边距属性。在计算位置时外边距视为组件大小的一部分，从而影响组件位置。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Margin](ts-types.md#margin) | [Length](ts-types.md#length) | [LocalizedMargin](ts-types.md#localizedmargin12)12+ | 是 | 设置组件的外边距。  参数为Length类型时，四个方向外边距同时生效。  默认值：0  单位：vp  margin设置百分比时，上下左右外边距均以父容器的width作为基础值。在[Row](ts-container-row.md)、[Column](ts-container-column.md)、[Flex](ts-container-flex.md)交叉轴上布局时，子组件交叉轴的大小与margin的和为整体。  例如Column容器宽100，其中子组件宽50，margin left为10，right为20，子组件水平方向偏移10。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## safeAreaPadding14+

PhonePC/2in1TabletTVWearable

safeAreaPadding(paddingValue: Padding | LengthMetrics | LocalizedPadding): T

设置安全区边距属性。允许容器向自身添加组件级安全区域，供子组件延伸，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

说明

从API version 18开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 14开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paddingValue | [Padding](ts-types.md#padding) | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | [LocalizedPadding](ts-types.md#localizedpadding12) | 是 | 设置组件的安全区边距。  默认值：0  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

当父辈和祖先容器设置了组件级安全区域时，子组件可以感知并利用该区域，称该区域为累计安全区延伸（accumulatedSafeAreaExpand，下文简称SAE），表示子组件在四个方向上各可延伸的长度。当祖辈与更上一级祖辈的safeAreaPadding相邻接（即未被margin、border、padding分隔）时，SAE将递归地向外累积，直至不存在相邻的更外层safeAreaPadding或递归至页面容器外。系统级避让区域（如状态栏、导航条、挖孔区等，详情参见[安全区域](ts-universal-attributes-expand-safe-area.md)中的说明）可视为页面容器特有的safeAreaPadding，同样参与该延伸范围的计算。

通过与其他属性配合使用，可对上述计算得到的组件级安全区区域加以利用。例如，对子组件设置[ignoreLayoutSafeArea](ts-universal-attributes-expand-safe-area.md#ignorelayoutsafearea20)属性，即可利用SAE延伸组件的布局范围。

## layoutWeight

PhonePC/2in1TabletTVWearable

layoutWeight(value: number | string): T

设置组件的布局权重，使组件在父容器（[Row](ts-container-row.md)/[Column](ts-container-column.md)/[Flex](ts-container-flex.md)）的主轴方向按照权重分配尺寸。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 父容器尺寸确定时，不设置layoutWeight属性或者layoutWeight属性生效值为0的元素优先占位，这些元素占位后在主轴留下的空间称为主轴剩余空间。设置了layoutWeight属性且layoutWeight属性生效值大于0的子元素会从主轴剩余空间中按照各自所设置的权重占比分配尺寸，分配时会忽略元素本身的尺寸设置。  默认值：0  **说明：**  仅在[Row](ts-container-row.md)/[Column](ts-container-column.md)/[Flex](ts-container-flex.md)布局中生效。  可选值为大于等于0的数字，或者可以转换为数字的字符串。  如果容器中有子元素设置了layoutWeight属性，且设置的属性值大于0，则所有子元素不会再基于[flexShrink](ts-universal-attributes-flex-layout.md#flexshrink)和[flexGrow](ts-universal-attributes-flex-layout.md#flexgrow)布局。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## constraintSize

PhonePC/2in1TabletTVWearable

constraintSize(value: ConstraintSizeOptions): T

设置约束尺寸，组件布局时，进行尺寸范围限制。

从API version 10开始，该接口支持calc计算特性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ConstraintSizeOptions](ts-types.md#constraintsizeoptions) | 是 | 设置约束尺寸。constraintSize的优先级高于Width和Height。取值结果参考constraintSize取值对width/height影响。  默认值：  {  minWidth: 0,  maxWidth: Infinity,  minHeight: 0,  maxHeight: Infinity  }  异常值：数值开头的字符串仅解析出数字部分，非数值开头的字符串解析为0；其它异常值时，constraintSize属性恢复到不配置时的默认行为。  单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

**constraintSize(minWidth/maxWidth/minHeight/maxHeight)取值对width/height影响：**

| 缺省值 | 结果 |
| --- | --- |
| \ | width=MAX(minWidth,MIN(maxWidth,width))  height=MAX(minHeight,MIN(maxHeight,height)) |
| maxWidth、maxHeight | width=MAX(minWidth,width)  height=MAX(minHeight,height) |
| minWidth、minHeight | width=MIN(maxWidth,width)  height=MIN(maxHeight,height) |
| width、height | 若minWidth<maxWidth，组件自身布局逻辑生效，width取值范围为[minWidth,maxWidth]；否则，width=MAX(minWidth,maxWidth)。  若minHeight<maxHeight，组件自身布局逻辑生效，height取值范围为[minHeight,maxHeight]；否则，height=MAX(minHeight,maxHeight)。 |
| width与maxWidth、height与maxHeight | width=minWidth  height=minHeight |
| width与minWidth、height与minHeight | 组件自身布局逻辑生效，width取值约束为不大于maxWidth。  组件自身布局逻辑生效，height取值约束为不大于maxHeight。 |
| minWidth与maxWidth、minHeight与maxHeight | width以所设值为基础，根据其他布局属性发生可能的拉伸或者压缩。  height以所设值为基础，根据其他布局属性发生可能的拉伸或者压缩。 |
| width与minWidth与maxWidth | 使用父容器传递的布局限制进行布局。 |
| height与minHeight与maxHeight | 使用父容器传递的布局限制进行布局。 |

## LayoutPolicy15+

PhonePC/2in1TabletTVWearable

用于组件宽度和高度的布局策略。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| matchParent | [LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15) | 是 | 否 | 当前组件自适应父组件布局时，其大小与父组件内容区相等，不包括padding，border和safeAreaPadding。  **卡片能力：** 从API version 15开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| wrapContent20+ | [LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15) | 是 | 否 | 当前组件自适应子组件（内容）时，其大小与子组件（内容）相等，并且其大小受父组件内容区大小约束。  **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| fixAtIdealSize20+ | [LayoutPolicy](ts-universal-attributes-size.md#layoutpolicy15) | 是 | 否 | 当前组件自适应子组件（内容）时，其大小与子组件（内容）相等，并且其大小不受父组件内容区大小约束。  **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

说明

* LayoutPolicy支持设置三种布局策略：matchParent（自适应父组件布局）、wrapContent（根据内容自适应但不超过父组件尺寸的布局）和fixAtIdealSize（根据内容自适应，可能超过父组件尺寸的布局）。具体示例代码参见[设置布局策略](ts-universal-attributes-size.md#示例5设置布局策略)。
* wrapContent和fixAtIdealSize场景，组件无法通过内容确定大小时，如果组件大小有默认值，则按照默认值进行测算；如果没有默认值，则按照宽高(0,0)进行测算。
* 容器设置wrapContent，并且有子组件设置matchParent时（包括仅一边设置matchParent），容器先由确定大小的子组件撑大，设置matchParent的子组件再匹配容器大小；如果没有确定大小的子组件，容器和子组件大小均为0。
* LayoutPolicy优先级低于constraintSize。
* 从API version 15开始，仅Row和Column组件的width和height属性支持设置LayoutPolicy类型参数，其他组件设置LayoutPolicy类型参数后与不设置宽度或高度表现一致；从API version 20开始，所有基础组件均支持设置LayoutPolicy类型参数。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置组件的宽高和边距）

设置组件的宽度、高度、内边距及外边距。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SizeExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('margin and padding:').fontSize(12).fontColor(0xCCCCCC).width('90%')
8. Row() {
9. // 宽度80 ,高度80 ,外边距20(蓝色区域），上下左右的内边距分别为5、15、10、20（白色区域）
10. Row() {
11. Row()
12. .size({ width: '100%', height: '100%' })
13. .backgroundColor(Color.Yellow)
14. }
15. .width(80)
16. .height(80)
17. .padding({
18. top: 5,
19. left: 10,
20. bottom: 15,
21. right: 20
22. })
23. .margin(20)
24. .backgroundColor(Color.White)
25. }.backgroundColor(Color.Blue)

27. Text('constraintSize')
28. .fontSize(12)
29. .fontColor(0xCCCCCC)
30. .width('90%')
31. Text('this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text.this is a Text')
32. .width('90%')
33. .constraintSize({ maxWidth: 200 })

35. Text('layoutWeight')
36. .fontSize(12)
37. .fontColor(0xCCCCCC)
38. .width('90%')
39. // 父容器尺寸确定时，设置了layoutWeight的子元素在主轴布局尺寸按照权重进行分配，忽略本身尺寸设置。
40. Row() {
41. // 权重1，占主轴剩余空间1/3
42. Text('layoutWeight(1)')
43. .size({ width: '30%', height: 110 }).backgroundColor(0xFFEFD5).textAlign(TextAlign.Center)
44. .layoutWeight(1)
45. // 权重2，占主轴剩余空间2/3
46. Text('layoutWeight(2)')
47. .size({ width: '30%', height: 110 }).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
48. .layoutWeight(2)
49. // 未设置layoutWeight属性，组件按照自身尺寸渲染
50. Text('no layoutWeight')
51. .size({ width: '30%', height: 110 }).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
52. }
53. .size({ width: '90%', height: 140 })
54. .backgroundColor(0xAFEEEE)

56. // calc计算特性
57. Text('calc:')
58. .fontSize(12)
59. .fontColor(0xCCCCCC)
60. .width('90%')
61. Column() {
62. Row() {
63. Text('width 50%')
64. .fontSize(14)
65. .borderWidth(1)
66. .textAlign(TextAlign.Center)
67. .size({ width: '50%', height: 50 })
68. Text('width 50vp')
69. .fontSize(14)
70. .borderWidth(1)
71. .textAlign(TextAlign.Center)
72. .size({ width: '50vp', height: 50 })
73. }
74. .width('100%')
75. .justifyContent(FlexAlign.Center)

77. Text('width:calc(50% + 50vp), height:calc(50%)')
78. .fontSize(14)
79. .borderWidth(1)
80. .fontWeight(FontWeight.Bold)
81. .backgroundColor(0xFFFAF0)
82. .textAlign(TextAlign.Center)
83. .size({ width: 'calc(50% + 50vp)', height: 'calc(50%)' })
84. // width和height设置百分比时，以父容器的width和height作为基础值。calc的宽度计算结果与上方的两个text宽度之和相等。
85. }.width('100%').height(100)
86. }
87. .width('100%')
88. .margin({ top: 5 })
89. }
90. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/zdyr7y6pQN6MHVFVmyH6eQ/zh-cn_image_0000002589245819.png?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=F14A629041340D990AF6564A0806F9F8418E9DC563EC420AF11E63DD7B8F2256)

### 示例2（LocalizedPadding和LocalizedMargin类型的使用）

使用LocalizedPadding类型和LocalizedMargin类型定义padding和margin属性。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI'

4. @Entry
5. @Component
6. struct SizeExample {
7. build() {
8. Column({ space: 10 }) {
9. Text('margin and padding:')
10. .fontSize(12)
11. .fontColor(0xCCCCCC)
12. .width('90%')
13. Row() {
14. // 宽度80 ,高度80 ,上下开始结束的外边距40、20、30、10(蓝色区域），上下开始结束的内边距分别为5、15、10、20（白色区域）
15. Row() {
16. Row()
17. .size({ width: '100%', height: '100%' })
18. .backgroundColor(Color.Yellow)
19. }
20. .width(80)
21. .height(80)
22. .padding({
23. top: LengthMetrics.vp(5),
24. bottom: LengthMetrics.vp(15),
25. start: LengthMetrics.vp(10),
26. end: LengthMetrics.vp(20)
27. })
28. .margin({
29. top: LengthMetrics.vp(40),
30. bottom: LengthMetrics.vp(20),
31. start: LengthMetrics.vp(30),
32. end: LengthMetrics.vp(10)
33. })
34. .backgroundColor(Color.White)
35. }
36. .backgroundColor(Color.Blue)
37. }
38. .width('100%')
39. .margin({ top: 5 })
40. }
41. }
```

从左至右显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/BxM_8NhKT6SeZEdZpo4_YQ/zh-cn_image_0000002558766010.png?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=CD6FF98E13BC4A49D39A913236098514B847E70FB645525EAF17A2286DD23820)

从右至左显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/crfQJwW0T8yJ86STuVfMFA/zh-cn_image_0000002558606352.png?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=301AC16EF88CA98722572A76B36B17B48733E4BB350187B764A89DF31D15BCE7)

### 示例3（设置组件级安全区）

对容器设置组件级安全区。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SafeAreaPaddingExample {
7. build() {
8. Column() {
9. Column() {
10. Column()
11. .width('100%')
12. .height('100%')
13. .backgroundColor(Color.Pink)
14. }
15. .width(200)
16. .height(200)
17. .backgroundColor(Color.Yellow)
18. .borderWidth(10)
19. .padding(10)
20. .safeAreaPadding(LengthMetrics.vp(40))
21. }
22. .height('100%')
23. .width('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/vmYfCzzARCOcNz496mG4cQ/zh-cn_image_0000002589325879.png?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=A097FA774F8F30B0D3613B65B22DC6C502ECB3BA62D52D56CDBC0BA0AC80A779)

### 示例4（使用attributeModifier动态设置安全区）

使用attributeModifier对容器设置组件级安全区。

```
1. // xxx.ets
2. class MyModifier implements AttributeModifier<CommonAttribute> {
3. applyNormalAttribute(instance: CommonAttribute): void {
4. instance.safeAreaPadding({
5. left: 10,
6. top: 20,
7. right: 30,
8. bottom: 40
9. })
10. }
11. }

13. @Entry
14. @Component
15. struct SafeAreaPaddingExample {
16. @State modifier: MyModifier = new MyModifier()

18. build() {
19. Column() {
20. Column() {
21. Column()
22. .width('100%')
23. .height('100%')
24. .backgroundColor(Color.Pink)
25. }
26. .width(200)
27. .height(200)
28. .backgroundColor(Color.Yellow)
29. .borderWidth(10)
30. .padding(10)
31. .attributeModifier(this.modifier)
32. }
33. .height('100%')
34. .width('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/-_9fwWkJQRSj1VJdV6ftag/zh-cn_image_0000002589245821.png?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=4472BFFE991052E34ED6AA8F57A07B729CE6EF9A1F0217F78C7F68AE91D2ECED)

### 示例5（设置布局策略）

对容器大小设置布局策略。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LayoutPolicyExample {
5. build() {
6. Column() {
7. Column() {
8. // matchParent生效时，当前组件会与其父组件内容区大小（180vp * 180vp）相等，同时依旧受自身constraintSize（150vp * 150vp）约束，因此当前组件大小为150vp * 150vp
9. Text('matchParent')
10. Flex()
11. .backgroundColor('rgb(0, 74, 175)')
12. .width(LayoutPolicy.matchParent)
13. .height(LayoutPolicy.matchParent)
14. .constraintSize({ maxWidth: 150, maxHeight: 150 })

16. // wrapContent生效时，当前组件会与其子组件大小（300vp * 300vp）相等，但不能超过父组件内容大小（180vp * 180vp）且会受自身constraintSize（250vp * 250vp）约束，因此当前组件大小为180vp * 180vp
17. Text('wrapContent')
18. Row() {
19. Flex()
20. .width(300)
21. .height(300)
22. }
23. .backgroundColor('rgb(39, 135, 217)')
24. .width(LayoutPolicy.wrapContent)
25. .height(LayoutPolicy.wrapContent)
26. .constraintSize({ maxWidth: 250, maxHeight: 250 })

28. // 从API version 20开始，layoutPolicy支持wrapContent和fixAtIdealSize。fixAtIdealSize生效时，当前组件会与其子组件大小（300vp * 300vp）相等，可以超过父组件内容大小（180vp * 180vp）但会受自身constraintSize（250vp * 250vp）约束，因此当前组件大小为250vp * 250vp
29. Text('fixAtIdealSize')

31. Row() {
32. Flex()
33. .width(300)
34. .height(300)
35. }
36. .backgroundColor('rgb(240, 250, 255)')
37. .width(LayoutPolicy.fixAtIdealSize)
38. .height(LayoutPolicy.fixAtIdealSize)
39. .constraintSize({ maxWidth: 250, maxHeight: 250 })
40. }
41. .width(200)
42. .height(200)
43. .padding(10)
44. }
45. .width('100%')
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/xNsDM84QRxiMtENTareFYg/zh-cn_image_0000002558766012.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055114Z&HW-CC-Expire=86400&HW-CC-Sign=87BA1A91C4983A355BB9B036B97339D307B56C4CB3F0478795E6299D8E83C70A)
