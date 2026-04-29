---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-symbolspan
title: SymbolSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > SymbolSpan
category: harmonyos-references
scraped_at: 2026-04-29T13:52:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2f7e1813c43386c1d3845a65b2c63e61c8574bd3ba71db6fda374ae57bd119f0
---

作为Text组件的子组件，用于显示图标小符号的组件。

说明

* 该组件从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 该组件支持继承父组件Text的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的全部属性。
* SymbolSpan拖拽不会置灰显示。

## 子组件

PhonePC/2in1TabletTVWearable

不支持子组件。

## 接口

PhonePC/2in1TabletTVWearable

SymbolSpan(value: Resource)

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Resource](ts-types.md#resource) | 是 | SymbolSpan组件的资源名，如 $r('sys.symbol.ohos\_wifi')。 |

说明

$r('sys.symbol.ohos\_wifi')中引用的资源为系统预置，SymbolSpan仅支持系统预置的symbol资源名，引用非symbol资源将显示异常。

## 属性

PhonePC/2in1TabletTVWearable

不支持[通用属性](ts-component-general-attributes.md)，支持以下属性：

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: Array<ResourceColor>)

设置SymbolSpan组件颜色。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ResourceColor](ts-types.md#resourcecolor)> | 是 | SymbolSpan组件颜色。  默认值：不同渲染策略下默认值不同。 |

### fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: number | string | Resource)

设置SymbolSpan组件大小。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | SymbolSpan组件大小。  默认值：16fp  单位：[fp](ts-pixel-units.md) |

### fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | string)

设置SymbolSpan组件粗细。number类型取值[100,900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如“400”，以及“bold”、“bolder”、“lighter”、“regular” 、“medium”分别对应FontWeight中相应的枚举值。

sys.symbol.ohos\_lungs图标不支持设置fontWeight。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | string | 是 | SymbolSpan组件粗细。  默认值：FontWeight.Normal |

### renderingStrategy

PhonePC/2in1TabletTVWearable

renderingStrategy(value: SymbolRenderingStrategy)

设置SymbolSpan渲染策略。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SymbolRenderingStrategy](ts-basic-components-symbolglyph.md#symbolrenderingstrategy11枚举说明) | 是 | SymbolSpan渲染策略。  默认值：SymbolRenderingStrategy.SINGLE |

不同渲染策略效果可参考以下示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/a4jOKaY_T0qJ_5rYTLfjLw/zh-cn_image_0000002558766338.png?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=738EEAEE92C3669AE99997856AF7583B0857388036F4CEC98596BD5640C74EE6)

### effectStrategy

PhonePC/2in1TabletTVWearable

effectStrategy(value: SymbolEffectStrategy)

设置SymbolSpan动效策略。

说明

从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SymbolEffectStrategy](ts-basic-components-symbolglyph.md#symboleffectstrategy11枚举说明) | 是 | SymbolSpan动效策略。  默认值：SymbolEffectStrategy.NONE |

### attributeModifier12+

PhonePC/2in1TabletTVWearable

attributeModifier(modifier: AttributeModifier<SymbolSpanAttribute>)

设置组件的动态属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifiert)<SymbolSpanAttribute> | 是 | 动态设置组件的属性。 |

## 事件

PhonePC/2in1TabletTVWearable

不支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置渲染和动效策略）

从API version 11开始，该示例通过[renderingStrategy](ts-basic-components-symbolspan.md#renderingstrategy)、[effectStrategy](ts-basic-components-symbolspan.md#effectstrategy)属性展示了不同的渲染和动效策略。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. Row() {
8. Column() {
9. Text("Light")
10. Text() {
11. SymbolSpan($r('sys.symbol.ohos_trash'))
12. .fontWeight(FontWeight.Lighter)
13. .fontSize(96)
14. }
15. }

17. Column() {
18. Text("Normal")
19. Text() {
20. SymbolSpan($r('sys.symbol.ohos_trash'))
21. .fontWeight(FontWeight.Normal)
22. .fontSize(96)
23. }
24. }

26. Column() {
27. Text("Bold")
28. Text() {
29. SymbolSpan($r('sys.symbol.ohos_trash'))
30. .fontWeight(FontWeight.Bold)
31. .fontSize(96)
32. }
33. }
34. }

36. Row() {
37. Column() {
38. Text("单色")
39. Text() {
40. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
41. .fontSize(96)
42. .renderingStrategy(SymbolRenderingStrategy.SINGLE)
43. .fontColor([Color.Black, Color.Green, Color.White])
44. }
45. }

47. Column() {
48. Text("多色")
49. Text() {
50. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
51. .fontSize(96)
52. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_COLOR)
53. .fontColor([Color.Black, Color.Green, Color.White])
54. }
55. }

57. Column() {
58. Text("分层")
59. Text() {
60. SymbolSpan($r('sys.symbol.ohos_folder_badge_plus'))
61. .fontSize(96)
62. .renderingStrategy(SymbolRenderingStrategy.MULTIPLE_OPACITY)
63. .fontColor([Color.Black, Color.Green, Color.White])
64. }
65. }
66. }

68. Row() {
69. Column() {
70. Text("无动效")
71. Text() {
72. SymbolSpan($r('sys.symbol.ohos_wifi'))
73. .fontSize(96)
74. .effectStrategy(SymbolEffectStrategy.NONE)
75. }
76. }

78. Column() {
79. Text("整体缩放动效")
80. Text() {
81. SymbolSpan($r('sys.symbol.ohos_wifi'))
82. .fontSize(96)
83. .effectStrategy(SymbolEffectStrategy.SCALE)
84. }
85. }

87. Column() {
88. Text("层级动效")
89. Text() {
90. SymbolSpan($r('sys.symbol.ohos_wifi'))
91. .fontSize(96)
92. .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
93. }
94. }
95. }
96. }
97. }
98. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/ecKLHiiYQsuqxwtSBi159Q/zh-cn_image_0000002558606680.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=CB15C4F990DA462BAA9EC23AA08D70CDD054575C69788BF5572AE595A0B11173)

### 示例2（设置动态属性）

从API version 12开始，该示例通过[attributeModifier](ts-basic-components-symbolspan.md#attributemodifier12)属性创建指定样式图标。

```
1. import { SymbolSpanModifier } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State modifier: SymbolSpanModifier =
7. new SymbolSpanModifier($r("sys.symbol.ohos_wifi")).fontColor([Color.Blue]).fontSize(100);

9. build() {
10. Row() {
11. Column() {
12. Text() {
13. SymbolSpan(undefined).attributeModifier(this.modifier)
14. }

16. Button('更改SymbolSpanModifier')
17. .onClick(() => {
18. this.modifier = new SymbolSpanModifier($r("sys.symbol.ohos_trash")).fontColor([Color.Red]).fontSize(100);
19. })
20. }
21. .width('100%')
22. }
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/d2QObBM0T1SYQPS88PO2Fg/zh-cn_image_0000002589326207.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055208Z&HW-CC-Expire=86400&HW-CC-Sign=CD01B47F5D88B711FDCC2CBE5980EFD669DD2DC06747631C0918F817F1EFB586)
