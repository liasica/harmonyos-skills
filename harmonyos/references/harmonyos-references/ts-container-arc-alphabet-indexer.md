---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-arc-alphabet-indexer
title: ArcAlphabetIndexer
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > ArcAlphabetIndexer
category: harmonyos-references
scraped_at: 2026-04-29T13:52:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5276e2736579043c6aa81f8b0e3b573fcf644ca83abab577cd0f2d18fb3eb17c
---

弧形索引条是一种弧形的、可按字母顺序排序进行快速定位的组件，可以与容器组件联动，按逻辑结构快速定位至容器显示区域。

说明

* 该组件从API version 18开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件支持在Phone、PC/2in1、Tablet、TV、Wearable设备上使用。API version 22及以前版本，在Phone、PC/2in1、Tablet、TV上使用会编译告警，但可以正常运行。

## 导入模块

PhonePC/2in1TabletTVWearable

说明

* ArcAlphabetIndexerAttribute是用于配置ArcAlphabetIndexer组件属性的关键接口。API version 21及之前版本，导入ArcAlphabetIndexer组件后需要开发者手动导入ArcAlphabetIndexerAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入ArcAlphabetIndexer组件后，会自动导入ArcAlphabetIndexerAttribute，无需开发者手动导入ArcAlphabetIndexerAttribute。
* 如果开发者手动导入ArcAlphabetIndexerAttribute，DevEco Studio会显示置灰，API version 21及之前版本删除会编译报错，API version 22开始，删除对功能无影响。

API version 21及之前版本：

```
1. import { ArcAlphabetIndexer, ArcAlphabetIndexerAttribute } from '@kit.ArkUI';
```

API version 22及之后版本：

```
1. import { ArcAlphabetIndexer } from '@kit.ArkUI';
```

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

ArcAlphabetIndexer(info: ArcAlphabetIndexerInitInfo)

创建弧形索引条实例，传入弧形索引条配置项参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：** 参数内容为设置弧形索引条索引项字符串数组、初始选中项索引位置。

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| info | [ArcAlphabetIndexerInitInfo](ts-container-arc-alphabet-indexer.md#arcalphabetindexerinitinfo对象说明) | 是 | 定义弧形字母索引条的初始化参数。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

PhonePC/2in1TabletTVWearable

color(color: Optional<ColorMetrics>)

设置普通状态下索引项文字颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 文字颜色。  默认值：0xFFFFFF，显示为白色。 |

### selectedColor

PhonePC/2in1TabletTVWearable

selectedColor(color: Optional<ColorMetrics>)

设置选中项文字颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 选中项文字颜色。  默认值：0xFFFFFF，显示为白色。 |

### popupColor

PhonePC/2in1TabletTVWearable

popupColor(color: Optional<ColorMetrics>)

设置提示弹窗文字颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 提示弹窗文字颜色。  默认值：0xFFFFFF，显示为白色。 |

### selectedBackgroundColor

PhonePC/2in1TabletTVWearable

selectedBackgroundColor(color: Optional<ColorMetrics>)

设置选中项背景颜色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 选中项背景颜色。  默认值：0x1F71FF，显示为深蓝色。 |

### popupBackground

PhonePC/2in1TabletTVWearable

popupBackground(color: Optional<ColorMetrics>)

设置提示弹窗背景色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 提示弹窗背景色。  默认值：0xD8404040，显示为微透明的深灰色。 |

说明

当通过popupBackground设置弹窗气泡的背景颜色后，不建议再通过[popupBackgroundBlurStyle](ts-container-arc-alphabet-indexer.md#popupbackgroundblurstyle)设置背景模糊效果。

### usePopup

PhonePC/2in1TabletTVWearable

usePopup(enabled: Optional<boolean>)

设置是否使用提示弹窗。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否使用提示弹窗。  true表示使用提示弹窗；false表示不使用提示弹窗。  默认值：false |

### selectedFont

PhonePC/2in1TabletTVWearable

selectedFont(font: Optional<Font>)

设置选中项文字尺寸、粗细、字体族、倾斜等样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Font](ts-types.md#font)> | 是 | 选中项文字样式。  默认值：{  size:'13.0fp',  style:FontStyle.Normal,  weight:500,  family:'HarmonyOS Sans'  } |

### popupFont

PhonePC/2in1TabletTVWearable

popupFont(font: Optional<Font>)

设置提示弹窗字体样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Font](ts-types.md#font)> | 是 | 提示弹窗字体样式。  默认值：  {  size:'19.0fp',  style:FontStyle.Normal,  weight:500,  family:'HarmonyOS Sans'  } |

### font

PhonePC/2in1TabletTVWearable

font(font: Optional<Font>)

设置字母索引条默认字体样式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| font | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Font](ts-types.md#font)> | 是 | 字母索引条默认字体样式。  默认值：  {  size:'13.0fp',  style:FontStyle.Normal,  weight:500,  family:'HarmonyOS Sans'  } |

### itemSize

PhonePC/2in1TabletTVWearable

itemSize(size: Optional<LengthMetrics>)

设置字母索引条字母区域大小。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12)> | 是 | 字母索引条字母区域大小，字母区域为圆形，即圆形直径。不支持设置为百分比。  默认值：24.0  单位：vp |

### selected

PhonePC/2in1TabletTVWearable

selected(index: Optional<number>)

设置选中项索引值。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | Optional<number> | 是 | 选中项索引值。  默认值：0  该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。 |

### autoCollapse

PhonePC/2in1TabletTVWearable

autoCollapse(enable: Optional<boolean>)

设置是否使用自适应折叠模式。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 是否使用自适应折叠模式。  默认值：true  true：使用自适应折叠模式。  false：不使用自适应折叠模式。 |

### popupBackgroundBlurStyle

PhonePC/2in1TabletTVWearable

popupBackgroundBlurStyle(style: Optional<BlurStyle>)

设置提示弹窗的背景模糊材质。未通过该接口设置时，默认为关闭模糊，对应取值为BlurStyle中的NONE。

说明

当通过popupBackgroundBlurStyle设置弹窗气泡的背景模糊材质时，不建议再通过[popupBackground](ts-container-arc-alphabet-indexer.md#popupbackground)设置背景色。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[BlurStyle](ts-universal-attributes-background.md#blurstyle9)> | 是 | 设置提示弹窗的背景模糊材质。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onSelect

PhonePC/2in1TabletTVWearable

onSelect(handler: Optional<OnSelectCallback>)

索引条选中回调，返回值为当前选中索引。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| handler | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OnSelectCallback](ts-container-arc-alphabet-indexer.md#onselectcallback)> | 是 | 回调函数类型。 |

## ArcAlphabetIndexerInitInfo对象说明

PhonePC/2in1TabletTVWearable

定义弧形字母索引条的初始化参数。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| arrayValue | string[] | 否 | 否 | 字母索引字符串数组，不可设置为空。 |
| selected | number | 否 | 否 | 初始选中项索引值，若超出索引值范围，则取默认值0。  该参数支持[!!](../harmonyos-guides/arkts-new-binding.md)双向绑定变量。 |

## OnSelectCallback

PhonePC/2in1TabletTVWearable

type OnSelectCallback = (index: number) => void

定义[onSelect](ts-container-arc-alphabet-indexer.md#onselect)中使用的回调类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 选中项序号。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例实现了弧形索引条和弧形列表联动控制和定位。

```
1. // xxx.ets
2. import {
3. LengthMetrics,
4. ColorMetrics,
5. ArcList,
6. ArcListItem,
7. ArcListAttribute,
8. ArcListItemAttribute,
9. ArcAlphabetIndexer,
10. ArcAlphabetIndexerAttribute
11. } from '@kit.ArkUI';
12. // 从API version 22开始，无需手动导入ArcListAttribute、ArcListItemAttribute、ArcAlphabetIndexerAttribute。具体请参考ArcList、ArcListItem、ArcAlphabetIndexer的导入模块说明。

14. @Entry
15. @Component
16. struct ArcListAndIndexer {
17. private fullValue: string[] = [
18. '#', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
19. 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
20. ];
21. private arrName : string[] = [
22. '1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',
23. '21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38',
24. '39','40', '41','42',
25. ];

27. private scrollerForList: Scroller = new Scroller();
28. @State indexerIndex: number = 0;

30. private watchSize: string = '466px'; // 手表默认宽高：233*233
31. private itemSize: number = 24;  // 索引项默认大小：24

33. build() {
34. Column() {
35. Row() {
36. Stack() {
37. ArcList({ scroller : this.scrollerForList, initialIndex: 0 }) {
38. ForEach(this.arrName, (itemName: string, index: number) => {
39. ArcListItem() {
40. Text(itemName)
41. .width('90%')
42. .height('92px')
43. .fontSize(16)
44. .textAlign(TextAlign.Center)
45. .backgroundColor(index % 2 == 0 ? 0xAFEEEE : 0x00FFFF)
46. .borderRadius(23)
47. }
48. })
49. }
50. .scrollBar(BarState.Off)
51. .onScrollIndex((firstIndex: number, lastIndex: number, centerIndex: number) => {
52. this.indexerIndex = centerIndex;
53. })
54. .borderWidth(1)
55. .width(this.watchSize)
56. .height(this.watchSize)
57. .borderRadius(this.watchSize)
58. .space(LengthMetrics.px(4))

60. ArcAlphabetIndexer({ arrayValue: this.fullValue, selected: 0 })
61. .autoCollapse(true)
62. .width(this.watchSize)
63. .height(this.watchSize)
64. .usePopup(false)
65. .selected(this.indexerIndex)
66. .onSelect((index: number) => {
67. this.indexerIndex = index;
68. this.scrollerForList.scrollToIndex(this.indexerIndex);
69. })
70. .borderWidth(1)
71. .hitTestBehavior(HitTestMode.Transparent)
72. .selectedColor(ColorMetrics.resourceColor(0xFFFFFF))
73. .selectedBackgroundColor(ColorMetrics.resourceColor(0x1F71FF))
74. .color(ColorMetrics.resourceColor(0xFFFFFF))
75. .popupColor(ColorMetrics.resourceColor(0xFFFFFF))
76. .popupBackground(ColorMetrics.resourceColor(0xD8404040))
77. .itemSize(LengthMetrics.px(this.itemSize))
78. .selectedFont({
79. size:'11.0fp',
80. style:FontStyle.Normal,
81. weight:500,
82. family:'HarmonyOS Sans'
83. })
84. .font({
85. size:'11.0fp',
86. style:FontStyle.Normal,
87. weight:500,
88. family:'HarmonyOS Sans'
89. })

91. }.width('100%').height('100%')
92. }.width('100%').height('100%')
93. }
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/JsV_dfnwT7KAfXVcd4yVeg/zh-cn_image_0000002558606766.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055216Z&HW-CC-Expire=86400&HW-CC-Sign=431A94877777E56822CF1413035795F43181214C12797E87C00363BD2A3ED37B)
