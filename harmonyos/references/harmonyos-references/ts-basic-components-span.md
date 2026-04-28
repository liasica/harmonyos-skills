---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-span
title: Span
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > Span
category: harmonyos-references
scraped_at: 2026-04-28T08:01:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c4ef6be4924046201cca72010868938a2ec09d42379a9e4cdb7ff1e6f8163861
---

作为[Text](ts-basic-components-text.md)、[ContainerSpan](ts-basic-components-containerspan.md)组件的子组件，用于显示行内文本的组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 10开始支持继承父组件Text的属性，即如果子组件未设置属性且父组件设置属性，则继承父组件设置的属性。支持继承的属性仅包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontFamily、textShadow。

不支持[通用属性](ts-component-general-attributes.md)。若需设置通用属性，应使用[Text](ts-basic-components-text.md)进行设置，或改用[属性字符串](ts-universal-styled-string.md)中的[CustomSpan](ts-universal-styled-string.md#customspan)自行绘制。

[通用事件](ts-component-general-events.md)只支持点击事件[onClick](ts-universal-events-click.md#onclick)和悬浮事件[onHover](ts-universal-events-hover.md#onhover)。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Span(value: string | Resource)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 文本内容。 |

## 属性

PhonePC/2in1TabletTVWearable

属性继承自[BaseSpan](ts-basic-components-span.md#basespan)。

### decoration

PhonePC/2in1TabletTVWearable

decoration(value: DecorationStyleInterface)

设置文本装饰线样式及其颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DecorationStyleInterface12+](ts-universal-styled-string.md#decorationstyleinterface) | 是 | 文本装饰线样式对象。  默认值：  {  type: TextDecorationType.None,  color: Color.Black,  style: TextDecorationStyle.SOLID  }  **说明：**  style参数不支持卡片能力。 |

说明

当文字的下边缘轮廓与装饰线位置相交时，会触发下划线避让规则，下划线将在这些字符处避让文字。常见“gjyqp”等英文字符。

当文本装饰线的颜色设置为Color.Transparent时，装饰线颜色设置为跟随每行第一个字的字体颜色。当文本装饰线的颜色设置为透明色16进制对应值“#00FFFFFF”时，装饰线颜色设置为透明色。

### letterSpacing

PhonePC/2in1TabletTVWearable

letterSpacing(value: number | ResourceStr)

设置文本字符间距。取值小于0，字符聚集重叠，取值大于0且随着数值变大，字符间距越来越大，稀疏分布。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本字符间距。  单位：[fp](ts-pixel-units.md)  从API version 20开始，支持[Resource](ts-types.md#resource)类型。 |

### textCase

PhonePC/2in1TabletTVWearable

textCase(value: TextCase)

设置文本大小写。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [TextCase](ts-appendix-enums.md#textcase) | 是 | 文本大小写。  默认值：TextCase.Normal |

### fontColor

PhonePC/2in1TabletTVWearable

fontColor(value: ResourceColor)

设置字体颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 字体颜色。  默认值：'e6182431'  Wearable设备上默认值为：'#c5ffffff' |

### fontSize

PhonePC/2in1TabletTVWearable

fontSize(value: number | string | Resource)

设置字体大小。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 字体大小。fontSize为number类型时，使用fp单位。字体默认大小16fp。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"，不支持设置百分比字符串。  Wearable设备上默认值为：15fp |

### fontStyle

PhonePC/2in1TabletTVWearable

fontStyle(value: FontStyle)

设置字体样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [FontStyle](ts-appendix-enums.md#fontstyle) | 是 | 字体样式。  默认值：FontStyle.Normal |

### fontWeight

PhonePC/2in1TabletTVWearable

fontWeight(value: number | FontWeight | ResourceStr)

设置文本的字体粗细，设置过大可能会在不同字体下有截断。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [FontWeight](ts-appendix-enums.md#fontweight) | [ResourceStr](ts-types.md#resourcestr) | 是 | 文本的字体粗细，number类型取值[100, 900]，取值间隔为100，默认为400，取值越大，字体越粗。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal  从API version 20开始，支持[Resource](ts-types.md#resource)类型。 |

### fontFamily

PhonePC/2in1TabletTVWearable

fontFamily(value: string | Resource)

设置字体列表。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | 是 | 字体列表。  默认字体'HarmonyOS Sans'。  使用多个字体时，请用逗号','分隔，字体的优先级按顺序生效。例如：'Arial,HarmonyOS Sans'。 |

说明

可以使用[loadFontSync](js-apis-graphics-text.md#loadfontsync)注册自定义字体。

### lineHeight10+

PhonePC/2in1TabletTVWearable

lineHeight(value: Length)

设置文本行高。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 文本行高。  number类型时单位为fp。设置string类型时，支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。 |

### font10+

PhonePC/2in1TabletTVWearable

font(value: Font)

设置文本样式。包括字体大小、字体粗细、字体族和字体风格。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Font](ts-types.md#font) | 是 | 文本样式。 |

### textShadow11+

PhonePC/2in1TabletTVWearable

textShadow(value: ShadowOptions | Array<ShadowOptions>)

设置文字阴影效果。该接口支持以数组形式入参，实现多重文字阴影。不支持fill字段, 不支持智能取色模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | Array<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明)> | 是 | 文字阴影效果。 |

## 事件

PhonePC/2in1TabletTVWearable

通用事件支持[点击事件onClick](ts-universal-events-click.md#onclick)、[悬浮事件onHover](ts-universal-events-hover.md#onhover)。

说明

由于Span组件无尺寸信息，因此点击事件返回的ClickEvent对象的target属性无效。

## BaseSpan

PhonePC/2in1TabletTVWearable

定义BaseSpan基础类，包含Span的通用属性。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

### textBackgroundStyle11+

PhonePC/2in1TabletTVWearable

textBackgroundStyle(style: TextBackgroundStyle): T

设置背景样式。作为[ContainerSpan](ts-basic-components-containerspan.md)的子组件时可以继承它的此属性值，优先使用其自身的此属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [TextBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11对象说明) | 是 | 背景样式。  默认值:  {  color: Color.Transparent,  radius: 0  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前Span的属性。 |

### baselineOffset12+

PhonePC/2in1TabletTVWearable

baselineOffset(value: LengthMetrics): T

设置Span基线的偏移量。此属性与父组件的baselineOffset是共存的。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 是 | 设置Span基线的偏移量，设置该值为百分比时，按默认值显示。  正数内容向上偏移，负数向下偏移。  默认值：0  在ImageSpan中，设置为非0时，[verticalAlign](ts-basic-components-imagespan.md#verticalalign)将固定为ImageSpanAlignment.BASELINE对齐；设置为0时，要使基线对齐策略生效，需同时设置[verticalAlign](ts-basic-components-imagespan.md#verticalalign)为ImageSpanAlignment.BASELINE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前Span的属性。 |

## TextBackgroundStyle11+对象说明

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本背景色。 |
| radius | [Dimension](ts-types.md#dimension10) | [BorderRadiuses](ts-types.md#borderradiuses9) | 否 | 是 | 文本背景圆角。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置文本样式）

该示例展示了设置不同样式的文本效果以及span配置点击事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SpanExample {
5. build() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
7. Text('Basic Usage').fontSize(9).fontColor(0xCCCCCC)
8. Text() {
9. Span('In Line')
10. Span(' Component')
11. Span(' !')
12. }

14. Text() {
15. Span('This is the Span component').fontSize(12).textCase(TextCase.Normal)
16. .decoration({ type: TextDecorationType.None, color: Color.Red })
17. .fontFamily('HarmonyOS Sans')
18. }.margin({ top: 12 })

20. // 文本横线添加
21. Text('Text Decoration').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
22. Text() {
23. Span('I am Underline-WAVY-span')
24. .decoration({ type: TextDecorationType.Underline, color: Color.Red, style: TextDecorationStyle.WAVY })
25. .fontSize(12)
26. }

28. Text() {
29. Span('I am LineThrough-DOTTED-span')
30. .decoration({ type: TextDecorationType.LineThrough, color: Color.Red, style: TextDecorationStyle.DOTTED })
31. .fontSize(12)
32. }

34. Text() {
35. Span('I am Overline-DASHED-span')
36. .decoration({ type: TextDecorationType.Overline, color: Color.Red, style: TextDecorationStyle.DASHED })
37. .fontSize(12)
38. }

40. // 文本字符间距
41. Text('LetterSpacing').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
42. Text() {
43. Span('span letter spacing')
44. .letterSpacing(0)
45. .fontSize(12)
46. }

48. Text() {
49. Span('span letter spacing')
50. .letterSpacing(-2)
51. .fontSize(12)
52. }

54. Text() {
55. Span('span letter spacing')
56. .letterSpacing(3)
57. .fontSize(12)
58. }

60. // 文本大小写展示设置
61. Text('Text Case').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
62. Text() {
63. Span('I am Lower-span').fontSize(12)
64. .textCase(TextCase.LowerCase)
65. .decoration({ type: TextDecorationType.None })
66. }

68. Text() {
69. Span('I am Upper-span').fontSize(12)
70. .textCase(TextCase.UpperCase)
71. .decoration({ type: TextDecorationType.None })
72. }

74. // 文本字体样式设置
75. Text('FontStyle').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
76. Text() {
77. Span('I am FontStyle-Normal').fontSize(12)
78. .fontStyle(FontStyle.Normal)
79. }

81. Text() {
82. Span('I am FontStyle-Italic').fontSize(12)
83. .fontStyle(FontStyle.Italic)
84. }

86. // 文本字体粗细设置
87. Text('FontWeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
88. Text() {
89. Span('I am FontWeight-Lighter').fontSize(12)
90. .fontWeight(FontWeight.Lighter)
91. }

93. Text() {
94. Span('I am FontWeight-Bold').fontSize(12)
95. .fontWeight(FontWeight.Bold)
96. }

98. // 文本行高设置
99. Text('LineHeight').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
100. Text() {
101. Span('I am lineHeight default\n').fontSize(12)
102. .fontWeight(FontWeight.Lighter)
103. Span('I am lineHeight 30').fontSize(12)
104. .lineHeight(30)
105. }
106. .backgroundColor(Color.Gray)

108. // 文本样式设置
109. Text('Font').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
110. Text() {
111. Span('span font 12 Bolder Italic')
112. .font({
113. size: 12,
114. weight: FontWeight.Bolder,
115. style: FontStyle.Italic,
116. family: "HarmonyOS Sans"
117. })
118. }

120. // span点击事件设置
121. Text('span click event').fontSize(9).fontColor(0xCCCCCC).margin({ top: 12 })
122. Text() {
123. Span('Span default ').fontSize(12)
124. Span('Span click')
125. .onClick((event) => {
126. console.info("span onClick")
127. })
128. }
129. }.width('100%').padding({ left: 35, right: 35, top: 35 })
130. }
131. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/qwoYj9QMSW2HNVfHt6tnHg/zh-cn_image_0000002583439855.png?HW-CC-KV=V1&HW-CC-Date=20260428T000147Z&HW-CC-Expire=86400&HW-CC-Sign=18E94F76A17338C4DF568AEBA66D56874DCABC457C2C966DC4D190FA2D573594)

### 示例2（设置文本阴影）

从API version 11开始，该示例通过[textShadow](ts-basic-components-span.md#textshadow11)属性展示了文本设置阴影的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SpanExample {
5. @State textShadows: ShadowOptions | Array<ShadowOptions> = [{
6. radius: 10,
7. color: Color.Red,
8. offsetX: 10,
9. offsetY: 0
10. }, {
11. radius: 10,
12. color: Color.Orange,
13. offsetX: 20,
14. offsetY: 0
15. },
16. {
17. radius: 10,
18. color: Color.Yellow,
19. offsetX: 30,
20. offsetY: 0
21. }, {
22. radius: 10,
23. color: Color.Green,
24. offsetX: 40,
25. offsetY: 0
26. },
27. {
28. radius: 10,
29. color: Color.Blue,
30. offsetX: 100,
31. offsetY: 0
32. }]

34. build() {
35. Column({ space: 8 }) {
36. Text() {
37. Span('123456789').fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
38. }

40. Text() {
41. Span('123456789') // span can inherit text shadow & font size from outer text
42. }.fontSize(50).textShadow(this.textShadows).fontColor(Color.Pink)
43. }
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/uO8cCwNLSOaGD3UlyBLcDQ/zh-cn_image_0000002552959810.png?HW-CC-KV=V1&HW-CC-Date=20260428T000147Z&HW-CC-Expire=86400&HW-CC-Sign=93367FE73F1AE841D7BE0F33AA718EE74BDB3BE4E7C5516525745FEEEFE2D0E7)

### 示例3（设置背景样式）

从API version 11开始，该示例通过[textBackgroundStyle](ts-basic-components-span.md#textbackgroundstyle11)属性展示了文本设置背景样式的效果。

```
1. // xxx.ets
2. @Component
3. @Entry
4. struct SpanExample {
5. build() {
6. Column() {
7. Text() {
8. Span('   Hello World !   ')
9. .fontSize('20fp')
10. .textBackgroundStyle({ color: "#7F007DFF", radius: "5vp" })
11. .fontColor(Color.White)
12. }
13. }.width('100%').margin({ bottom: '5vp' }).alignItems(HorizontalAlign.Center)
14. }
15. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Pywcacy5Q_qkkzk5oFib2A/zh-cn_image_0000002583479811.png?HW-CC-KV=V1&HW-CC-Date=20260428T000147Z&HW-CC-Expire=86400&HW-CC-Sign=63973CC6A7D64F36EB6A1F17BE338B4D6F9E70DDABC13DADE0F7A5142A249205)

### 示例4（设置文本基线偏移量）

从API version 12开始，该示例通过[baselineOffset](ts-basic-components-span.md#baselineoffset12)属性展示了文本设置不同基线偏移量的效果。

```
1. // xxx.ets
2. import { LengthUnit, LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct SpanExample {
7. build() {
8. Row() {
9. Column() {
10. Text() {
11. Span('SpanOne')
12. .fontSize(10)
13. .baselineOffset(new LengthMetrics(20, LengthUnit.VP))
14. Span('SpanTwo')
15. .fontSize(10)
16. .baselineOffset(new LengthMetrics(0, LengthUnit.VP))
17. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
18. ImageSpan($r("app.media.sky"))
19. .width('80px')
20. .baselineOffset(new LengthMetrics(-20, LengthUnit.VP))
21. }
22. .backgroundColor('#7F007DFF')
23. }
24. .width('100%')
25. }
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/hOijLAScRKikKvo9_wU94Q/zh-cn_image_0000002552800162.png?HW-CC-KV=V1&HW-CC-Date=20260428T000147Z&HW-CC-Expire=86400&HW-CC-Sign=FDD04FC812E81344B5E002B13F8CEF4ACCF8CBE047E8EF4EBF176E3248E1EC6E)
