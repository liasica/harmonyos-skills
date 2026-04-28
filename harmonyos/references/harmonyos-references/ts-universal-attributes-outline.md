---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-outline
title: 外描边设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 外描边设置
category: harmonyos-references
scraped_at: 2026-04-28T08:01:08+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1c09a658153a3914b9c015bfb08bf82c35127973656dcf804fe5c8ba0e84070d
---

设置组件外描边（outline）样式。外描边绘制在组件的外侧，不影响布局，不会占用组件本身大小。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/IbvgKM6qSv-XFr0wvBp2YQ/zh-cn_image_0000002552799872.png?HW-CC-KV=V1&HW-CC-Date=20260428T000106Z&HW-CC-Expire=86400&HW-CC-Sign=5D594E1C17DD2E8801AE16FFD68025850263AE340B6166A46B38881D38702EF7)

说明

从API version 11开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## outline

PhonePC/2in1TabletTVWearable

outline(value: OutlineOptions): T

统一外描边样式设置接口。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [OutlineOptions](ts-types.md#outlineoptions11对象说明) | 是 | 外描边样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outline18+

PhonePC/2in1TabletTVWearable

outline(options: Optional<OutlineOptions>): T

统一外描边样式设置接口。与[outline](ts-universal-attributes-outline.md#outline)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OutlineOptions](ts-types.md#outlineoptions11对象说明)> | 是 | 外描边样式。  当options的值为undefined时，恢复为无外边框效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## OutlineStyle枚举说明

PhonePC/2in1TabletTVWearable

外描边样式。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SOLID | 0 | 显示为一条实线。 |
| DASHED | 1 | 显示为一系列短的方形虚线。 |
| DOTTED | 2 | 显示为一系列圆点，圆点半径为outlineWidth的一半。 |

## outlineStyle

PhonePC/2in1TabletTVWearable

outlineStyle(value: OutlineStyle | EdgeOutlineStyles): T

设置元素的外描边样式。不设置该接口时，默认显示为一条实线。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | [EdgeOutlineStyles](ts-types.md#edgeoutlinestyles11对象说明) | 是 | 设置元素的外描边样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineStyle18+

PhonePC/2in1TabletTVWearable

outlineStyle(style: Optional<OutlineStyle | EdgeOutlineStyles>): T

设置元素的外描边样式。不设置该接口时，默认显示为一条实线。与[outlineStyle](ts-universal-attributes-outline.md#outlinestyle)相比，style参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[OutlineStyle](ts-universal-attributes-outline.md#outlinestyle枚举说明) | [EdgeOutlineStyles](ts-types.md#edgeoutlinestyles11对象说明)> | 是 | 设置元素的外描边样式。  当style的值为undefined时，恢复为无外描边样式的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineWidth

PhonePC/2in1TabletTVWearable

outlineWidth(value: Dimension | EdgeOutlineWidths): T

设置元素的外描边宽度。不设置该接口时，默认无变化。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | [EdgeOutlineWidths](ts-types.md#edgeoutlinewidths11对象说明) | 是 | 设置元素的外描边宽度，不支持百分比。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineWidth18+

PhonePC/2in1TabletTVWearable

outlineWidth(width: Optional<Dimension | EdgeOutlineWidths>): T

设置元素的外描边宽度。不设置该接口时，默认无变化。与[outlineWidth](ts-universal-attributes-outline.md#outlinewidth)相比，width参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Dimension](ts-types.md#dimension10) | [EdgeOutlineWidths](ts-types.md#edgeoutlinewidths11对象说明)> | 是 | 设置元素的外描边宽度，不支持百分比。  当width的值为undefined时，恢复为无外描边宽度的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineColor

PhonePC/2in1TabletTVWearable

outlineColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T

设置元素的外描边颜色。不设置该接口时，默认显示为黑色。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12)12+ | 是 | 设置元素的外描边颜色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineColor18+

PhonePC/2in1TabletTVWearable

outlineColor(color: Optional<ResourceColor | EdgeColors | LocalizedEdgeColors>): T

设置元素的外描边颜色。不设置该接口时，默认显示为黑色。与[outlineColor](ts-universal-attributes-outline.md#outlinecolor)相比，color参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9) | [LocalizedEdgeColors](ts-types.md#localizededgecolors12)> | 是 | 设置元素的外描边颜色。  当color的值为undefined时，恢复为描边颜色为Color.Black的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineRadius

PhonePC/2in1TabletTVWearable

outlineRadius(value: Dimension | OutlineRadiuses): T

设置元素的外描边圆角半径。不设置该接口时，默认无变化。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Dimension](ts-types.md#dimension10) | [OutlineRadiuses](ts-types.md#outlineradiuses11对象说明) | 是 | 设置元素的外描边圆角半径，不支持百分比。  最大生效值：组件width/2 + outlineWidth或组件height/2 + outlineWidth。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## outlineRadius18+

PhonePC/2in1TabletTVWearable

outlineRadius(radius: Optional<Dimension | OutlineRadiuses>): T

设置元素的外描边圆角半径。不设置该接口时，默认无变化。与[outlineRadius](ts-universal-attributes-outline.md#outlineradius)相比，radius参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Dimension](ts-types.md#dimension10) | [OutlineRadiuses](ts-types.md#outlineradiuses11对象说明)> | 是 | 设置元素的外描边圆角半径，不支持百分比。  最大生效值：组件width/2 + outlineWidth或组件height/2 + outlineWidth。  当radius的值为undefined时，恢复为外描边圆角半径为0的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用外描边属性）

该示例主要演示如何通过[outline](ts-universal-attributes-outline.md#outline)来实现组件外描边。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OutlineExample {
5. build() {
6. Column() {
7. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
8. // 线段
9. Text('DASHED')
10. .backgroundColor(Color.Pink)
11. .outlineStyle(OutlineStyle.DASHED).outlineWidth(5).outlineColor(0xAFEEEE).outlineRadius(10)
12. .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
13. // 点线
14. Text('DOTTED')
15. .backgroundColor(Color.Pink)
16. .outline({ width: 5, color: 0x317AF7, radius: 10, style: OutlineStyle.DOTTED })
17. .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
18. }.width('100%').height(150)

20. Text('.outline')
21. .backgroundColor(Color.Pink)
22. .fontSize(50)
23. .width(300)
24. .height(300)
25. .outline({
26. width: { left: 3, right: 6, top: 10, bottom: 15 },
27. color: { left: '#e3bbbb', right: Color.Blue, top: Color.Red, bottom: Color.Green },
28. radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },
29. style: {
30. left: OutlineStyle.DOTTED,
31. right: OutlineStyle.DOTTED,
32. top: OutlineStyle.SOLID,
33. bottom: OutlineStyle.DASHED
34. }
35. }).textAlign(TextAlign.Center)
36. }
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/oLgnxv79TTeTbznV8OfwSg/zh-cn_image_0000002583439567.png?HW-CC-KV=V1&HW-CC-Date=20260428T000106Z&HW-CC-Expire=86400&HW-CC-Sign=78BA3EFC45D2BB64B5C1D94F71A0BCA4EDDE7CD4611B5270B97EB6A4C7AB4BEC)

### 示例2（使用LocalizedEdgeColors类型）

该示例将[outline](ts-universal-attributes-outline.md#outline)属性中的color属性值设置为[LocalizedEdgeColors](ts-types.md#localizededgecolors12)类型。

```
1. // xxx.ets

3. @Entry
4. @Component
5. struct OutlineExample {
6. build() {
7. Column() {
8. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
9. // 线段
10. Text('DASHED')
11. .backgroundColor(Color.Pink)
12. .outlineStyle(OutlineStyle.DASHED).outlineWidth(5).outlineColor(0xAFEEEE).outlineRadius(10)
13. .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
14. // 点线
15. Text('DOTTED')
16. .backgroundColor(Color.Pink)
17. .outline({ width: 5, color: 0x317AF7, radius: 10, style: OutlineStyle.DOTTED })
18. .width(120).height(120).textAlign(TextAlign.Center).fontSize(16)
19. }.width('100%').height(150)

21. Text('.outline')
22. .backgroundColor(Color.Pink)
23. .fontSize(50)
24. .width(300)
25. .height(300)
26. .outline({
27. width: { left: 3, right: 6, top: 10, bottom: 15 },
28. color: { start: '#e3bbbb', end: Color.Blue, top: Color.Red, bottom: Color.Green },
29. radius: { topLeft: 10, topRight: 20, bottomLeft: 40, bottomRight: 80 },
30. style: {
31. left: OutlineStyle.DOTTED,
32. right: OutlineStyle.DOTTED,
33. top: OutlineStyle.SOLID,
34. bottom: OutlineStyle.DASHED
35. }
36. }).textAlign(TextAlign.Center)
37. }
38. }
39. }
```

从左至右显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Xxqxj7e_SVizDJkSYq2rYw/zh-cn_image_0000002552959522.png?HW-CC-KV=V1&HW-CC-Date=20260428T000106Z&HW-CC-Expire=86400&HW-CC-Sign=27091EBBCE9ABF2E8428E47DB5079091D641C439FB7FC4BD884E74D4F340680E)

从右至左显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/BNfmy56NQDelnx5UXm9w1A/zh-cn_image_0000002583479523.png?HW-CC-KV=V1&HW-CC-Date=20260428T000106Z&HW-CC-Expire=86400&HW-CC-Sign=37F4311861360D616C6E95EB5D938FF447791D20307846EDE46E0FB5C7888B87)
