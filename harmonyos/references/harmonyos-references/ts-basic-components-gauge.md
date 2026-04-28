---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-gauge
title: Gauge
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > Gauge
category: harmonyos-references
scraped_at: 2026-04-28T08:02:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c208c46929758911c197888dc729e57c1a766fe85c067c5a4c1caff51cfa7a58
---

数据量规图表组件，用于将数据展示为环形图表。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含单个子组件。

说明

* 支持的子组件类型：系统组件和自定义组件，支持条件渲染控制[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)，不支持循环渲染控制[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)。
* 建议使用文本组件构建当前数值文本和辅助文本。
* 若子组件宽高为百分比形式，则基准范围为以外圆环做为内切圆的矩形。

## 接口

PhonePC/2in1TabletTVWearable

Gauge(options: GaugeOptions)

创建数据量规图表组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GaugeOptions](ts-basic-components-gauge.md#gaugeoptions18对象说明) | 是 | 数据量规图表组件参数。 |

## GaugeOptions18+对象说明

PhonePC/2in1TabletTVWearable

数据量规图表选项。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value8+ | number | 否 | 否 | 量规图的当前数据值，即图中指针指向位置。用于组件创建时量规图初始值的预置。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：**  value不在min和max范围内时使用min作为默认值。 |
| min8+ | number | 否 | 是 | 当前数据段最小值。  默认值：0  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| max8+ | number | 否 | 是 | 当前数据段最大值。  默认值：100  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **说明：**  max小于min时使用默认值0和100。  max和min支持负数。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### value

PhonePC/2in1TabletTVWearable

value(value: number)

设置量规图的数据值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 量规图的数据值，可用于动态修改量规图的数据值。  默认值：0 |

### startAngle

PhonePC/2in1TabletTVWearable

startAngle(angle: number)

设置起始角度位置。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 起始角度位置，时钟0点为0度，顺时针方向为正角度，逆时针方向为负角度，超过360度等价于对360度取余后的角度。  默认值：0  从起始位置到终止位置的绘制只有顺时针方向。 |

### endAngle

PhonePC/2in1TabletTVWearable

endAngle(angle: number)

设置终止角度位置。起始角度和终止角度的差值过小时，会绘制出异常图像，请取合理的起始角度和终止角度。建议使用单色环改变Gauge的value参数实现数据值的调节，可通过定时器setTimeout进行数值的延迟加载。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 终止角度位置，时钟0点为0度，顺时针方向为正角度，逆时针方向为负角度，超过360度等价于对360度取余后的角度。  默认值：360  从起始位置到终止位置的绘制只有顺时针方向。 |

### colors

PhonePC/2in1TabletTVWearable

colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, number]>)

设置量规图的颜色。

从API version 11开始，该接口使用以下规则：

参数类型为[ResourceColor](ts-types.md#resourcecolor)，则圆环类型为单色环。

参数类型为[LinearGradient](ts-basic-components-datapanel.md#lineargradient10)，则圆环类型为渐变环。

参数类型为数组，则圆环类型为分段渐变环，第一个参数为颜色值，若设置为非颜色类型，则置为"0xFFE84026"。第二个参数为颜色所占比重，若设置为负数或是非数值类型，则将比重置为0。

分段渐变环最大显示段数为9段，若多于9段，则多于部分不显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | [ResourceColor11+](ts-types.md#resourcecolor) | [LinearGradient11+](ts-basic-components-datapanel.md#lineargradient10) | Array<[[ResourceColor10+](ts-types.md#resourcecolor) | [LinearGradient11+](ts-basic-components-datapanel.md#lineargradient10) , number]> | 是 | 量规图的颜色，支持分段颜色设置。  API version 9 默认值：Color.Black  API version 11默认值：  若不传颜色，或者数组为空，无法确定圆环类型及颜色，则圆环颜色为"0xFF64BB5C"、"0xFFF7CE00"、"0xFFE84026"的渐变环。  若传入颜色，但颜色值有误，则该颜色为"0xFFE84026"。  若对应颜色的比重为0，则该颜色在圆环中不显示。若所有颜色比重均为0，圆环不显示。 |

### strokeWidth

PhonePC/2in1TabletTVWearable

strokeWidth(length: Length)

设置环形量规图的环形厚度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | [Length](ts-types.md#length) | 是 | 环形量规图的环形厚度。  默认值：4  单位：vp  **说明：**  设置小于等于0的值时，按默认值显示。  环形厚度的最大值为圆环的半径，超过最大值按最大值处理。  不支持百分比。 |

### description11+

PhonePC/2in1TabletTVWearable

description(value: CustomBuilder)

设置说明内容。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](ts-types.md#custombuilder8) | 是 | 说明内容。  **说明：**  @Builder中的内容由开发者自定义，建议使用文本或者图片。  若自定义部分的宽高为百分比形式，则基准范围为圆环直径的44.4%\*25.4%的矩形（图片为28.6%\*28.6%），距离圆环底部0vp，左右居中。  设置null则不显示内容。  不设置则依赖是否设置数据最大最小值。  若设置最大最小值或者只设置其中一个，则显示最大最小值。  若未设置最大最小值，则不显示内容。  最大最小值显示在圆环底部，位置不可移动，若圆环开口角度设置不恰当，存在圆环遮挡文字的情况。 |

### trackShadow11+

PhonePC/2in1TabletTVWearable

trackShadow(value: GaugeShadowOptions)

设置阴影样式。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GaugeShadowOptions](ts-basic-components-gauge.md#gaugeshadowoptions11对象说明) | 是 | 添加阴影效果，可以指定模糊半径、X轴和Y轴的偏移量。  **说明：**  阴影颜色与圆环颜色一致。  设置null为不开启投影。 |

### indicator11+

PhonePC/2in1TabletTVWearable

indicator(value: GaugeIndicatorOptions)

设置指针样式。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GaugeIndicatorOptions](ts-basic-components-gauge.md#gaugeindicatoroptions11对象说明) | 是 | 指针样式。  **说明：**  设置null则不显示指针。 |

### privacySensitive12+

PhonePC/2in1TabletTVWearable

privacySensitive(isPrivacySensitiveMode: Optional<boolean>)

设置隐私敏感。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacySensitiveMode | Optional<boolean> | 是 | 设置隐私敏感。在隐私模式下，Gauge指针指向0位置，最大值最小值文本将被遮罩，量程显示灰色或底色。true表示打开隐私敏感，false表示关闭隐私敏感。  **说明：**  设置null则不敏感。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<GaugeConfiguration>)

定制Gauge内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier<GaugeConfiguration>](ts-basic-components-gauge.md#gaugeconfiguration12对象说明) | 是 | 在Gauge组件上定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## GaugeShadowOptions11+对象说明

PhonePC/2in1TabletTVWearable

GaugeShadowOptions继承自[MultiShadowOptions](ts-information-display-common.md#multishadowoptions)，具有MultiShadowOptions的全部属性。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

## GaugeIndicatorOptions11+对象说明

PhonePC/2in1TabletTVWearable

数据量规图表指针选项。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| icon | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 图标资源路径。  **说明：**  不配置则使用系统默认样式，系统默认样式为三角形指针。  仅支持使用svg格式的图标，若使用其他格式，则使用默认的三角形样式指针。 |
| space | [Dimension](ts-types.md#dimension10) | 否 | 是 | 指针距离圆环外边的间距。(不支持百分比)  默认值：8  单位：vp  **说明：**  对于默认的三角形样式指针，间距为黑色三角形到圆环外边的间距。  若设置值小于0，则使用默认值。  若设置值大于圆环半径，则使用默认值。 |

## GaugeConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | number | 否 | 否 | 当前数据值。 |
| min | number | 否 | 否 | 当前数据段最小值。 |
| max | number | 否 | 否 | 当前数据段最大值。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置多色量规图）

该示例通过[colors](ts-basic-components-gauge.md#colors)接口，实现了多色量规图效果。

```
1. @Entry
2. @Component
3. struct Gauge1 {
4. @Builder
5. descriptionBuilder() {
6. Text('说明文本')
7. .maxFontSize('30sp')
8. .minFontSize('10.0vp')
9. .fontColor('#fffa2a2d')
10. .fontWeight(FontWeight.Medium)
11. .width('100%')
12. .height('100%')
13. .textAlign(TextAlign.Center)
14. }

16. build() {
17. Column() {
18. Gauge({ value: 50, min: 1, max: 100 }) {
19. Column() {
20. Text('50')
21. .fontWeight(FontWeight.Medium)
22. .width('62%')
23. .fontColor('#ff182431')
24. .maxFontSize('60.0vp')
25. .minFontSize('30.0vp')
26. .textAlign(TextAlign.Center)
27. .margin({ top: '35%' })
28. .textOverflow({ overflow: TextOverflow.Ellipsis })
29. .maxLines(1)
30. Text('辅助文本')
31. .maxFontSize('16.0fp')
32. .minFontSize('10.0vp')
33. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
34. .fontWeight(FontWeight.Regular)
35. .width('67.4%')
36. .height('9.5%')
37. .textAlign(TextAlign.Center)
38. }.width('100%').height('100%')
39. }
40. .value(50)
41. .startAngle(210)
42. .endAngle(150)
43. .colors([[new LinearGradient([{ color: '#deb6fb', offset: 0 }, { color: '#ac49f5', offset: 1 }]), 9],
44. [new LinearGradient([{ color: '#bbb7fc', offset: 0 }, { color: '#564af7', offset: 1 }]), 8],
45. [new LinearGradient([{ color: '#f5b5c2', offset: 0 }, { color: '#e64566', offset: 1 }]), 7],
46. [new LinearGradient([{ color: '#f8c5a6', offset: 0 }, { color: '#ed6f21', offset: 1 }]), 6],
47. [new LinearGradient([{ color: '#fceb99', offset: 0 }, { color: '#f7ce00', offset: 1 }]), 5],
48. [new LinearGradient([{ color: '#dbefa5', offset: 0 }, { color: '#a5d61d', offset: 1 }]), 4],
49. [new LinearGradient([{ color: '#c1e4be', offset: 0 }, { color: '#64bb5c', offset: 1 }]), 3],
50. [new LinearGradient([{ color: '#c0ece5', offset: 0 }, { color: '#61cfbe', offset: 1 }]), 2],
51. [new LinearGradient([{ color: '#b5e0f4', offset: 0 }, { color: '#46b1e3', offset: 1 }]), 1]])
52. .width('80%')
53. .height('80%')
54. .strokeWidth(18)
55. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
56. .description(this.descriptionBuilder)
57. .padding(18)
58. }.margin({ top: 40 }).width('100%').height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/D6oP_z7CSE2qv4qgHwFXpA/zh-cn_image_0000002552800256.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=533A9D34A99A9717D029702E71CD0D3534D24A69D46E81B2C5EB0C9324858173)

### 示例2（设置单色量规图）

该示例通过[colors](ts-basic-components-gauge.md#colors)接口，实现了单色量规图效果。

```
1. @Entry
2. @Component
3. struct Gauge2 {
4. @Builder
5. descriptionBuilderImage() {
6. Image($r('sys.media.ohos_ic_public_clock')).width(72).height(72)
7. }

9. build() {
10. Column() {
11. Gauge({ value: 50, min: 1, max: 100 }) {
12. Column() {
13. Text('50')
14. .fontWeight(FontWeight.Medium)
15. .width('62%')
16. .fontColor('#ff182431')
17. .maxFontSize('60.0vp')
18. .minFontSize('30.0vp')
19. .textAlign(TextAlign.Center)
20. .margin({ top: '35%' })
21. .textOverflow({ overflow: TextOverflow.Ellipsis })
22. .maxLines(1)
23. }.width('100%').height('100%')
24. }
25. .startAngle(210)
26. .endAngle(150)
27. .colors('#cca5d61d')
28. .width('80%')
29. .height('80%')
30. .strokeWidth(18)
31. .description(this.descriptionBuilderImage)
32. .padding(18)
33. }.margin({ top: 40 }).width('100%').height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/qarPkyx7TKy5ykx43EoiNg/zh-cn_image_0000002583439951.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=376A7679172C51A7D931031DA8BD51342F9748B70092122996FCFD03D71351E3)

### 示例3（设置定制说明区）

该示例通过[description](ts-basic-components-gauge.md#description11)接口，实现了说明区的设置功能。

```
1. @Entry
2. @Component
3. struct Gauge3 {
4. @Builder
5. descriptionBuilder() {
6. Text('说明文本')
7. .maxFontSize('30sp')
8. .minFontSize('10.0vp')
9. .fontColor('#fffa2a2d')
10. .fontWeight(FontWeight.Medium)
11. .width('100%')
12. .height('100%')
13. .textAlign(TextAlign.Center)
14. }

16. build() {
17. Column() {
18. Column() {
19. Gauge({ value: 50, min: 1, max: 100 }) {
20. Column() {
21. Text('50')
22. .fontWeight(FontWeight.Medium)
23. .width('62%')
24. .fontColor('#ff182431')
25. .maxFontSize('60.0vp')
26. .minFontSize('30.0vp')
27. .textAlign(TextAlign.Center)
28. .margin({ top: '35%' })
29. .textOverflow({ overflow: TextOverflow.Ellipsis })
30. .maxLines(1)
31. }.width('100%').height('100%')
32. }
33. .startAngle(210)
34. .endAngle(150)
35. .colors([[new LinearGradient([{ color: '#deb6fb', offset: 0 }, { color: '#ac49f5', offset: 1 }]), 9],
36. [new LinearGradient([{ color: '#bbb7fc', offset: 0 }, { color: '#564af7', offset: 1 }]), 8],
37. [new LinearGradient([{ color: '#f5b5c2', offset: 0 }, { color: '#e64566', offset: 1 }]), 7],
38. [new LinearGradient([{ color: '#f8c5a6', offset: 0 }, { color: '#ed6f21', offset: 1 }]), 6],
39. [new LinearGradient([{ color: '#fceb99', offset: 0 }, { color: '#f7ce00', offset: 1 }]), 5],
40. [new LinearGradient([{ color: '#dbefa5', offset: 0 }, { color: '#a5d61d', offset: 1 }]), 4],
41. [new LinearGradient([{ color: '#c1e4be', offset: 0 }, { color: '#64bb5c', offset: 1 }]), 3],
42. [new LinearGradient([{ color: '#c0ece5', offset: 0 }, { color: '#61cfbe', offset: 1 }]), 2],
43. [new LinearGradient([{ color: '#b5e0f4', offset: 0 }, { color: '#46b1e3', offset: 1 }]), 1]])
44. .width('80%')
45. .height('80%')
46. .strokeWidth(18)
47. .description(this.descriptionBuilder)
48. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
49. .padding(18)
50. }.margin({ top: 40 }).width('100%').height('100%')
51. }
52. }
53. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/xhG-oNMsQyaG-VQ8i9G5OQ/zh-cn_image_0000002552959906.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=CB7329E6C8367A529B17FB4F8E5D491B99D2FAF3F1F1D4F0E946BCAB792E1D46)

### 示例4（设置辅助区）

该示例通过设置子组件，实现了辅助区的设置功能。

```
1. @Entry
2. @Component
3. struct Gauge4 {
4. build() {
5. Column() {
6. Gauge({ value: 50, min: 1, max: 100 }) {
7. Column() {
8. Text('50')
9. .maxFontSize('72.0vp')
10. .minFontSize('10.0vp')
11. .fontColor('#ff182431')
12. .width('40%')
13. .textAlign(TextAlign.Center)
14. .margin({ top: '35%' })
15. .textOverflow({ overflow: TextOverflow.Ellipsis })
16. .maxLines(1)
17. Text('辅助文本')
18. .maxFontSize('30.0vp')
19. .minFontSize('18.0vp')
20. .fontWeight(FontWeight.Medium)
21. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
22. .width('62%')
23. .height('15.9%')
24. .textAlign(TextAlign.Center)
25. }.width('100%').height('100%')
26. }
27. .startAngle(210)
28. .endAngle(150)
29. .colors([[new LinearGradient([{ color: '#deb6fb', offset: 0 }, { color: '#ac49f5', offset: 1 }]), 9],
30. [new LinearGradient([{ color: '#bbb7fc', offset: 0 }, { color: '#564af7', offset: 1 }]), 8],
31. [new LinearGradient([{ color: '#f5b5c2', offset: 0 }, { color: '#e64566', offset: 1 }]), 7],
32. [new LinearGradient([{ color: '#f8c5a6', offset: 0 }, { color: '#ed6f21', offset: 1 }]), 6],
33. [new LinearGradient([{ color: '#fceb99', offset: 0 }, { color: '#f7ce00', offset: 1 }]), 5],
34. [new LinearGradient([{ color: '#dbefa5', offset: 0 }, { color: '#a5d61d', offset: 1 }]), 4],
35. [new LinearGradient([{ color: '#c1e4be', offset: 0 }, { color: '#64bb5c', offset: 1 }]), 3],
36. [new LinearGradient([{ color: '#c0ece5', offset: 0 }, { color: '#61cfbe', offset: 1 }]), 2],
37. [new LinearGradient([{ color: '#b5e0f4', offset: 0 }, { color: '#46b1e3', offset: 1 }]), 1]])
38. .width('80%')
39. .height('80%')
40. .strokeWidth(18)
41. .description(null)
42. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
43. .padding(18)
44. }.margin({ top: 40 }).width('100%').height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/zPgRGyatTQel4zPCv5lhFA/zh-cn_image_0000002583479907.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=4298E0F02690971FD5EAA1254E64A30D3ECF6A4F0307766F6DBD703BBDCE6364)

### 示例5（设置最大最小值）

该示例通过设置[GaugeOptions](ts-basic-components-gauge.md#gaugeoptions18对象说明)的min、max属性，实现了量规图的最大最小值设置的功能。

```
1. @Entry
2. @Component
3. struct Gauge5 {
4. build() {
5. Column() {
6. Gauge({ value: 50, min: 1, max: 100 }) {
7. Column() {
8. Text('50')
9. .maxFontSize('80sp')
10. .minFontSize('60.0vp')
11. .fontWeight(FontWeight.Medium)
12. .fontColor('#ff182431')
13. .width('40%')
14. .height('30%')
15. .textAlign(TextAlign.Center)
16. .margin({ top: '22.2%' })
17. .textOverflow({ overflow: TextOverflow.Ellipsis })
18. .maxLines(1)
19. }.width('100%').height('100%')
20. }
21. .startAngle(225)
22. .endAngle(135)
23. .colors(new LinearGradient([{ color: '#e84026', offset: 0 },
24. { color: '#f7ce00', offset: 0.6 },
25. { color: '#64bb5c', offset: 1 }]))
26. .width('80%')
27. .height('80%')
28. .strokeWidth(18)
29. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
30. .padding(18)
31. }.margin({ top: 40 }).width('100%').height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/ze6FxbUCQcWtXsD4YSvg7w/zh-cn_image_0000002552800258.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=B4CAA57F65F07E0473BFC87508E7B17BF7495E9576C66AEFD94BE36208EF29ED)

### 示例6（设置指针）

该示例通过[indicator](ts-basic-components-gauge.md#indicator11)接口，实现了设置量规图的指针的功能。

```
1. @Entry
2. @Component
3. struct Gauge6 {
4. build() {
5. Column() {
6. Gauge({ value: 50, min: 1, max: 100 }) {
7. Column() {
8. Text('50')
9. .maxFontSize('60sp')
10. .minFontSize('30.0vp')
11. .fontWeight(FontWeight.Medium)
12. .fontColor('#ff182431')
13. .width('62%')
14. .textAlign(TextAlign.Center)
15. .margin({ top: '35%' })
16. .textOverflow({ overflow: TextOverflow.Ellipsis })
17. .maxLines(1)
18. Text('辅助文本')
19. .maxFontSize('16sp')
20. .minFontSize('10.0vp')
21. .fontColor($r('sys.color.ohos_id_color_text_secondary'))
22. .fontWeight(FontWeight.Regular)
23. .width('67.4%')
24. .height('9.5%')
25. .textAlign(TextAlign.Center)
26. }.width('100%').height('100%')
27. }
28. .startAngle(225)
29. .endAngle(135)
30. .colors(Color.Red)
31. .width('80%')
32. .height('80%')
33. .indicator(null)
34. .strokeWidth(18)
35. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
36. .padding(18)
37. }.margin({ top: 40 }).width('100%').height('100%')
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/kLzjdN9dRIau4TU-iA4eWw/zh-cn_image_0000002583439953.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=801F27D06C3ED5BE6DF826F32247DA2816FB78F14BCBAABEDFF5C560296E2ED5)

### 示例7（设置起止角度）

该示例通过[startAngle](ts-basic-components-gauge.md#startangle)和[endAngle](ts-basic-components-gauge.md#endangle)接口，实现了量规图起止角度设置的功能。

```
1. @Entry
2. @Component
3. struct Gauge7 {
4. build() {
5. Column() {
6. Gauge({ value: 50, min: 1, max: 100 }) {
7. Column() {
8. Text('50')
9. .maxFontSize('60sp')
10. .minFontSize('30.0vp')
11. .fontWeight(FontWeight.Medium)
12. .fontColor('#ff182431')
13. .width('62%')
14. .textAlign(TextAlign.Center)
15. .margin({ top: '35%' })
16. .textOverflow({ overflow: TextOverflow.Ellipsis })
17. .maxLines(1)
18. }.width('100%').height('100%')
19. }
20. .startAngle(225)
21. .endAngle(135)
22. .colors(Color.Red)
23. .width('80%')
24. .height('80%')
25. .indicator(null)
26. .strokeWidth(18)
27. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
28. .padding(18)
29. }.margin({ top: 40 }).width('100%').height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/c4xV6ixFSI2dg5j3ysiRmg/zh-cn_image_0000002552959908.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=217FD723CE52920ED1BCF37288F4F6D673200D5CB0B314C3EC454A48343AB638)

### 示例8（设置定制内容区）

该示例通过[contentModifier](ts-basic-components-gauge.md#contentmodifier12)接口，实现了定制量规图内容区的功能。

```
1. // xxx.ets
2. // 该示例实现了Gauge组件使用Builder定制内容区，使用了环形图表组件，按钮和文本框。点击增加按钮，环形图表指针位置会向右偏移，反之点减少按钮环形图表指针位置会向左偏移。
3. @Builder
4. function buildGauge(config: GaugeConfiguration) {
5. Column({ space: 30 }) {
6. Row() {
7. Text('【ContentModifier】 value：' + JSON.stringify((config.contentModifier as MyGaugeStyle).value) +
8. '  min：' + JSON.stringify((config.contentModifier as MyGaugeStyle).min) +
9. '  max：' + JSON.stringify((config.contentModifier as MyGaugeStyle).max))
10. .fontSize(12)
11. }

13. Text('【Config】value：' + config.value + '  min：' + config.min + '  max：' + config.max).fontSize(12)
14. Gauge({
15. value: config.value,
16. min: config.min,
17. max: config.max
18. }).width('50%')
19. }
20. .width('100%')
21. .padding(20)
22. .margin({ top: 5 })
23. .alignItems(HorizontalAlign.Center)
24. }

26. class MyGaugeStyle implements ContentModifier<GaugeConfiguration> {
27. value: number = 0
28. min: number = 0
29. max: number = 0

31. constructor(value: number, min: number, max: number) {
32. this.value = value
33. this.min = min
34. this.max = max
35. }

37. applyContent(): WrappedBuilder<[GaugeConfiguration]> {
38. return wrapBuilder(buildGauge)
39. }
40. }

42. @Entry
43. @Component
44. struct refreshExample {
45. @State gaugeValue: number = 20
46. @State gaugeMin: number = 0
47. @State gaugeMax: number = 100

49. build() {
50. Column({ space: 20 }) {
51. Gauge({
52. value: this.gaugeValue,
53. min: this.gaugeMin,
54. max: this.gaugeMax
55. })
56. .contentModifier(new MyGaugeStyle(30, 10, 100))

58. Column({ space: 20 }) {
59. Row({ space: 20 }) {
60. Button('增加').onClick(() => {
61. if (this.gaugeValue < this.gaugeMax) {
62. this.gaugeValue += 1
63. }
64. })
65. Button('减少').onClick(() => {
66. if (this.gaugeValue > this.gaugeMin) {
67. this.gaugeValue -= 1
68. }
69. })
70. }
71. }.width('100%')
72. }.width('100%').margin({ top: 5 })
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/voceb-idTfeV914oxw_Hrw/zh-cn_image_0000002583479909.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=F6441F5D2F1C57FF71C84E3F023185CBC06E08FB0512319C47A649A2C42D2C3E)

### 示例9（设置隐私隐藏）

该示例通过[privacySensitive](ts-basic-components-gauge.md#privacysensitive12)接口，实现了隐私隐藏效果，效果展示需要卡片框架支持

```
1. @Entry
2. @Component
3. struct GaugeExample {
4. build() {
5. Scroll() {
6. Column({ space: 15 }) {
7. Row() {
8. Gauge({ value: 60, min: 20, max: 100 })
9. .startAngle(225)
10. .endAngle(135)
11. .colors(Color.Red)
12. .width('80%')
13. .height('80%')
14. .strokeWidth(18)
15. .trackShadow({ radius: 7, offsetX: 7, offsetY: 7 })
16. .padding(18)
17. .privacySensitive(true)
18. }
19. }
20. }
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/BrbK3qMJTe-yuko6A9gu5Q/zh-cn_image_0000002552800260.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=A7635304F72A36A16DCF0AD785851E8923DAE456B574528F2D4F90D17499E3CC)

### 示例10（设置自定义指针）

该示例通过[indicator](ts-basic-components-gauge.md#indicator11)接口，实现了自定义指针功能，开发者导入svg类型的图片以替换默认指针。

```
1. @Entry
2. @Component
3. struct Gauge2 {
4. build() {
5. Column() {
6. Gauge({ value: 50, min: 1, max: 100 })
7. // $r('app.media.indicator')需要替换为开发者所需的图像资源文件。
8. .indicator({ space: 10, icon: $r('app.media.indicator') })
9. .startAngle(210)
10. .endAngle(150)
11. .colors('#cca5d61d')
12. .width('80%')
13. .height('80%')
14. .strokeWidth(18)
15. .padding(18)
16. }.margin({ top: 40 }).width('100%').height('100%')
17. }
18. }
```

```
1. <svg width='200px' height='200px'>
2. <path d='M 10,30 A 20,20 0,0,1 50,30 A 20,20 0,0,1 90,30 Q 90,60 50,90 Q 10,60 10,30 z'
3. stroke='black' stroke-width='3' fill='white'>
4. </path>
5. </svg>
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/fPhyzcaVT5idN_EVNfsghA/zh-cn_image_0000002583439955.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=E5F8628A8135DFAD764B810C67A8003E3604D69ECF081F8A14A6E79D615BCDBA)
