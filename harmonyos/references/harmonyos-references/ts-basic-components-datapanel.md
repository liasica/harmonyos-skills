---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-datapanel
title: DataPanel
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 信息展示 > DataPanel
category: harmonyos-references
scraped_at: 2026-04-29T13:52:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:80a4f97233fe982b1a20bbbfc4a7f135d73498a07f80054ae55e421a0a88c24c
---

数据面板组件，用于将多个数据占比情况使用占比图进行展示。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

DataPanel(options: DataPanelOptions)

创建数据面板组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [DataPanelOptions](ts-basic-components-datapanel.md#datapaneloptions对象说明) | 是 | 数据面板组件参数。 |

## DataPanelOptions对象说明

PhonePC/2in1TabletTVWearable

数据面板选项。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| values | number[] | 否 | 否 | 数据值列表，最多包含9个数据，大于9个数据则取前9个数据。若数据值小于0则置为0。 |
| max | number | 否 | 是 | - max大于0时，表示数据的最大值。  - max小于等于0时，max等于value数组各项的和，按比例显示。  默认值：100 |
| type8+ | [DataPanelType](ts-basic-components-datapanel.md#datapaneltype8枚举说明) | 否 | 是 | 数据面板的类型（不支持动态修改）。  默认值：DataPanelType.Circle |

## DataPanelType8+枚举说明

PhonePC/2in1TabletTVWearable

数据面板的类型。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Line | 0 | 线型数据面板。 |
| Circle | 4 | 环形数据面板。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### closeEffect

PhonePC/2in1TabletTVWearable

closeEffect(value: boolean)

设置是否关闭数据占比图表旋转动效和投影效果。若未设置[trackShadow](ts-basic-components-datapanel.md#trackshadow10)属性，则由该属性控制投影效果的开关，开启投影的效果为投影的默认效果。若设置了trackShadow属性，则由trackShadow属性值控制投影效果的开关。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 关闭数据占比图表旋转动效和投影效果。  默认值：false，false表示开启数据占比图表旋转动效和投影效果，true表示关闭数据占比图表旋转动效和投影效果。 |

### valueColors10+

PhonePC/2in1TabletTVWearable

valueColors(value: Array<ResourceColor | LinearGradient>)

设置各数据段颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10)> | 是 | 各数据段颜色，ResourceColor为纯色，LinearGradient为渐变色。默认渐变色，其九段数据段默认颜色：[{ color: '#F7CE00', offset: 0 }, { color: '#F99B11', offset: 1 }]、[{ color: '#F76223', offset: 0 }, { color: '#F2400A', offset: 1 }]、[{ color: '#F772AC', offset: 0 }, { color: '#E65392', offset: 1 }]、[{ color: '#A575EB', offset: 0 }, { color: '#A12DF7', offset: 1 }]、[{ color: '#7B79F7', offset: 0 }, { color: '#4B48F7', offset: 1 }]、[{ color: '#4B8AF3', offset: 0 }, { color: '#007DFF', offset: 1 }]、[{ color: '#73C1E6', offset: 0 }, { color: '#4FB4E3', offset: 1 }]、[{ color: '#A5D61D', offset: 0 }, { color: '#69D14F', offset: 1 }]、[{ color: '#A2A2B0', offset: 0 }, { color: '#8E8E93', offset: 1 }] |

### trackBackgroundColor10+

PhonePC/2in1TabletTVWearable

trackBackgroundColor(value: ResourceColor)

设置底板颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 底板颜色。  默认值：'#08182431'，格式为十六进制ARGB值，前两位代表透明度。 |

### strokeWidth10+

PhonePC/2in1TabletTVWearable

strokeWidth(value: Length)

设置圆环粗细。数据面板的类型为DataPanelType.Line时该属性不生效。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 圆环粗细。  默认值：24  单位：vp  设置字符串类型参数时，如果不指定单位，默认单位为px，例如'10'，等同于'10px'。  **说明：**  设置小于0的值时，按默认值显示。  请合理设置圆环粗细，当value大于圆环半径时，圆环粗细会自动设置为圆环半径的12%。如果value过大，圆环可能会消失。 |

### trackShadow10+

PhonePC/2in1TabletTVWearable

trackShadow(value: DataPanelShadowOptions)

设置投影样式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DataPanelShadowOptions](ts-basic-components-datapanel.md#datapanelshadowoptions10对象说明) | 是 | 投影样式。  **说明：**  设置为null时，不开启投影。 |

### contentModifier12+

PhonePC/2in1TabletTVWearable

contentModifier(modifier: ContentModifier<DataPanelConfiguration>)

定制DataPanel内容区的方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](ts-universal-attributes-content-modifier.md#contentmodifiert)[<DataPanelConfiguration>](ts-basic-components-datapanel.md#datapanelconfiguration12对象说明) | 是 | 在DataPanel组件上，定制内容区的方法。  modifier：内容修改器，开发者需要自定义class实现ContentModifier接口。 |

## DataPanelShadowOptions10+对象说明

PhonePC/2in1TabletTVWearable

DataPanelShadowOptions继承自[MultiShadowOptions](ts-information-display-common.md#multishadowoptions)，具有MultiShadowOptions的全部属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| colors | Array<[ResourceColor](ts-types.md#resourcecolor) | [LinearGradient](ts-basic-components-datapanel.md#lineargradient10)> | 否 | 是 | 各数据段投影的颜色。  默认值：与valueColors值相同  **说明：**  若设置的投影颜色的个数少于数据段个数时，则显示的投影颜色的个数和设置的投影颜色个数一致。  若设置的投影颜色的个数多于数据段个数时，则显示的投影颜色的个数和数据段个数一致。 |

## LinearGradient10+

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(colorStops: ColorStop[])

线性渐变颜色描述。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorStops | [ColorStop](ts-basic-components-datapanel.md#colorstop10)[] | 是 | 存储渐变颜色和渐变点。 |

## ColorStop10+

PhonePC/2in1TabletTVWearable

颜色断点类型，用于描述渐进色颜色断点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 否 | 渐变色断点处的颜色值。 |
| offset | [Length](ts-types.md#length) | 否 | 否 | 渐变色断点（0~1之间的比例值，若数据值小于0则置为0，若数据值大于1则置为1）。  **说明：**  若传入字符串类型且内容为数字，则转换为对应的数值。  例如'10vp'转换为10，'10%'转换为0.1。 |

## DataPanelConfiguration12+对象说明

PhonePC/2in1TabletTVWearable

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](ts-universal-attributes-content-modifier.md#commonconfigurationt)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| values | number[] | 否 | 否 | 当前DataPanel的数据值。  数组长度范围是[0, 9]。  **说明：**  如果数组长度大于9，则取前9项。 |
| maxValue | number | 否 | 否 | DataPanel显示的最大值。  默认值：100。  **说明：**  如果小于或等于0，maxValue将被设为values数组中所有项的总和，并按比例显示。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置数据面板类型）

该示例通过[DataPanelOptions](ts-basic-components-datapanel.md#datapaneloptions对象说明)的type属性，实现了设置数据面板的类型的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DataPanelExample {
5. public valueArr: number[] = [10, 10, 10, 10, 10, 10, 10, 10, 10]

7. build() {
8. Column({ space: 5 }) {
9. Row() {
10. Stack() {
11. // 单段环形数据面板
12. DataPanel({ values: [30], max: 100, type: DataPanelType.Circle }).width(168).height(168)
13. Column() {
14. Text('30').fontSize(35).fontColor('#182431')
15. Text('1.0.0').fontSize(9.33).lineHeight(12.83).fontWeight(500).opacity(0.6)
16. }

18. Text('%')
19. .fontSize(9.33)
20. .lineHeight(12.83)
21. .fontWeight(500)
22. .opacity(0.6)
23. .position({ x: 104.42, y: 78.17 })
24. }.margin({ right: 44 })

26. // 多段环形数据面板
27. Stack() {
28. DataPanel({ values: [50, 12, 8, 5], max: 100, type: DataPanelType.Circle }).width(168).height(168)
29. Column() {
30. Text('75').fontSize(35).fontColor('#182431')
31. Text('已使用98GB/128GB').fontSize(8.17).lineHeight(11.08).fontWeight(500).opacity(0.6)
32. }

34. Text('%')
35. .fontSize(9.33)
36. .lineHeight(12.83)
37. .fontWeight(500)
38. .opacity(0.6)
39. .position({ x: 104.42, y: 78.17 })
40. }
41. }.margin({ bottom: 59 })

43. // 线形数据面板
44. DataPanel({ values: this.valueArr, max: 100, type: DataPanelType.Line }).width(300).height(20)
45. }.width('100%').margin({ top: 5 })
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/DjinMxuXRlSj5pXaRYQX6A/zh-cn_image_0000002589326295.png?HW-CC-KV=V1&HW-CC-Date=20260429T055217Z&HW-CC-Expire=86400&HW-CC-Sign=AF5FD8C367C9696A6102FE9E2B01E445DF9517023AFCB7DBE2B69909731EBB18)

### 示例2（设置渐变色和阴影）

该示例通过[valueColors](ts-basic-components-datapanel.md#valuecolors10)和[trackShadow](ts-basic-components-datapanel.md#trackshadow10)接口设置[LinearGradient](ts-basic-components-datapanel.md#lineargradient10)颜色，实现了设置渐变色效果和阴影效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LinearGradientDataPanelExample {
5. public values1: number[] = [20, 20, 20, 20]
6. public color1: LinearGradient =
7. new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#FFEF629F', offset: 1 }])
8. public color2: LinearGradient =
9. new LinearGradient([{ color: '#FF67F9D4', offset: 0 }, { color: '#FFFF9554', offset: 1 }])
10. public colorShadow1: LinearGradient =
11. new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#65EF629F', offset: 1 }])
12. public colorShadow2: LinearGradient =
13. new LinearGradient([{ color: '#65e26709', offset: 0 }, { color: '#65efbd08', offset: 1 }])
14. public colorShadow3: LinearGradient =
15. new LinearGradient([{ color: '#6572B513', offset: 0 }, { color: '#6508efa6', offset: 1 }])
16. public colorShadow4: LinearGradient =
17. new LinearGradient([{ color: '#65ed08f5', offset: 0 }, { color: '#65ef0849', offset: 1 }])
18. @State shadowColorArray: Array<LinearGradient | ResourceColor> =
19. [this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4]
20. @State color3: string = '#00FF00'
21. @State color4: string = '#20FF0000'
22. @State colorArray: Array<LinearGradient | ResourceColor> = [this.color1, this.color2, this.color3, this.color4]
23. @State bgColor: string = '#08182431'
24. @State offsetX: number = 15
25. @State offsetY: number = 15
26. @State radius: number = 5

28. build() {
29. Column({ space: 5 }) {
30. Text('LinearGradient')
31. .fontSize(9)
32. .fontColor(0xCCCCCC)
33. .textAlign(TextAlign.Start)
34. .width('100%')
35. .margin({ top: 20, left: 20 })
36. DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })
37. .width(300)
38. .height(300)
39. .valueColors(this.colorArray)
40. .trackShadow({
41. radius: this.radius,
42. colors: this.shadowColorArray,
43. offsetX: this.offsetX,
44. offsetY: this.offsetY
45. })
46. .strokeWidth(30)
47. .trackBackgroundColor(this.bgColor)
48. }.width('100%').margin({ top: 5 })
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/6KRJppE8QXuGFnzvlp6Dtg/zh-cn_image_0000002589246237.png?HW-CC-KV=V1&HW-CC-Date=20260429T055217Z&HW-CC-Expire=86400&HW-CC-Sign=6D98CA1C18AB46618F45E17127DC2B21BB157828B8B50733E0BDBB787D8F5C46)

### 示例3（设置关闭动画和阴影）

该示例通过[closeEffect](ts-basic-components-datapanel.md#closeeffect)接口，实现了关闭数据面板动画和阴影的功能。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LinearGradientDataPanelExample {
5. public values1: number[] = [20, 20, 20, 20]
6. public color1: LinearGradient =
7. new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#FFEF629F', offset: 1 }])
8. public color2: LinearGradient =
9. new LinearGradient([{ color: '#FF67F9D4', offset: 0 }, { color: '#FFFF9554', offset: 1 }])
10. public colorShadow1: LinearGradient =
11. new LinearGradient([{ color: '#65EEC9A3', offset: 0 }, { color: '#65EF629F', offset: 1 }])
12. public colorShadow2: LinearGradient =
13. new LinearGradient([{ color: '#65e26709', offset: 0 }, { color: '#65efbd08', offset: 1 }])
14. public colorShadow3: LinearGradient =
15. new LinearGradient([{ color: '#6572B513', offset: 0 }, { color: '#6508efa6', offset: 1 }])
16. public colorShadow4: LinearGradient =
17. new LinearGradient([{ color: '#65ed08f5', offset: 0 }, { color: '#65ef0849', offset: 1 }])
18. @State shadowColorArray: Array<LinearGradient | ResourceColor> =
19. [this.colorShadow1, this.colorShadow2, this.colorShadow3, this.colorShadow4]
20. @State color3: string = '#00FF00'
21. @State color4: string = '#20FF0000'
22. @State colorArray: Array<LinearGradient | ResourceColor> = [this.color1, this.color2, this.color3, this.color4]
23. @State bgColor: string = '#08182431'
24. @State offsetX: number = 15
25. @State offsetY: number = 15
26. @State radius: number = 5

28. build() {
29. Column({ space: 5 }) {
30. Text('LinearGradient')
31. .fontSize(9)
32. .fontColor(0xCCCCCC)
33. .textAlign(TextAlign.Start)
34. .width('100%')
35. .margin({ top: 20, left: 20 })
36. DataPanel({ values: this.values1, max: 100, type: DataPanelType.Circle })
37. .width(300)
38. .height(300)
39. .valueColors(this.colorArray)
40. .strokeWidth(30)
41. .closeEffect(true)
42. .trackBackgroundColor(this.bgColor)
43. }.width('100%').margin({ top: 5 })
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/ap9Bbj65SJ2-4IATiVeAvA/zh-cn_image_0000002558766430.png?HW-CC-KV=V1&HW-CC-Date=20260429T055217Z&HW-CC-Expire=86400&HW-CC-Sign=6D132729038501DB116A5E4B9B99E6195D068AD0330BB2A06C47DAD896A14EE2)

### 示例4（设置定制内容区）

该示例通过[contentModifier](ts-basic-components-datapanel.md#contentmodifier12)接口，实现了定制数据面板内容区的功能。

```
1. // xxx.ets
2. @Builder
3. function buildDataPanel(config: DataPanelConfiguration) {
4. Column() {
5. Column() {
6. ForEach(config.values, (item: number, index: number) => {
7. ChildItem({ item: item, index: index, max: config.maxValue })
8. }, (item: number, index: number) => item.toString())
9. }.padding(10)

11. Column() {
12. Line().width('100%').backgroundColor('#ff373737').margin({ bottom: 5 })
13. }.padding({ left: 20, right: 20 })

15. Row() {
16. Text('Length=' + config.values.length + '    ').margin({ left: 10 }).align(Alignment.Start)
17. Text('Max=' + config.maxValue).margin({ left: 10 }).align(Alignment.Start)
18. }
19. }
20. }

22. class DataPanelBuilder implements ContentModifier<DataPanelConfiguration> {
23. constructor() {
24. }

26. applyContent(): WrappedBuilder<[DataPanelConfiguration]> {
27. return wrapBuilder(buildDataPanel)
28. }
29. }

31. @Entry
32. @Component
33. struct Index {
34. build() {
35. Column() {
36. Text('Data panel').margin({ top: 12 });
37. Row() {
38. DataPanel({ values: [12.3, 21.1, 13.4, 35.2, 26.0, 32.0], max: 140, type: DataPanelType.Circle })
39. .width(400)
40. .height(260)
41. .constraintSize({ maxWidth: '100%' })
42. .padding({ top: 10 })
43. .contentModifier(new DataPanelBuilder())
44. }.margin(15).backgroundColor('#fff5f5f5')
45. }
46. }
47. }

49. @Component
50. struct ChildItem {
51. @Prop item: number;
52. @Prop index: number;
53. @Prop max: number;
54. public color1: string = '#65ff00dd'
55. public color2: string = '#6500ff99'
56. public color3: string = '#65ffe600'
57. public color4: string = '#6595ff00'
58. public color5: string = '#65000dff'
59. public color6: string = '#650099ff'
60. public colorArray: Array<string> = [this.color1, this.color2, this.color3, this.color4, this.color5, this.color6]

62. build() {
63. RelativeContainer() {
64. Row() {
65. Rect()
66. .height(25)
67. .width(this.item * 600 / this.max)
68. .foregroundColor((this.index < 0 || this.index >= this.colorArray.length) ? this.colorArray[0] :
69. this.colorArray[this.index])
70. .radius(5)
71. .align(Alignment.Start)
72. Text(' ' + this.item)
73. .fontSize(17)
74. }
75. }.height(28)
76. }
77. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Z9F60hztSzuerunUFC61Hw/zh-cn_image_0000002558606770.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055217Z&HW-CC-Expire=86400&HW-CC-Sign=DF04E00B7616943751F5E94AA75A89200545614BEE2A9899FD9C53C7574CFB84)
