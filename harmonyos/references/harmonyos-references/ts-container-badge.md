---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-badge
title: Badge
category: harmonyos-references
scraped_at: 2026-04-28T08:02:00+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:3389e24e65be945712d86edd4ec66eb2bf426bb552f978740d894285e16d2154
---

信息标记组件，可以附加在单个组件上用于信息提醒的容器组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

说明

* 子组件类型：系统组件和自定义组件，支持渲染控制类型（[if/else](../harmonyos-guides/arkts-rendering-control-ifelse.md)、[ForEach](../harmonyos-guides/arkts-rendering-control-foreach.md)和[LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)）。
* 自定义组件宽高默认为0，需要给其设置宽高，否则标记组件将不显示。
* 当存在多个子组件时，只有最后一个子组件会在界面上显示，但其余子组件的状态更新仍会使Badge及其子组件重新布局渲染。
* 不影响子组件布局，即不会主动规避子组件内容。

## 接口

PhonePC/2in1TabletTVWearable

### Badge

PhonePC/2in1TabletTVWearable

Badge(value: BadgeParamWithNumber)

根据数字创建标记组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BadgeParamWithNumber](ts-container-badge.md#badgeparamwithnumber对象说明) | 是 | 数字标记组件参数。 |

### Badge

PhonePC/2in1TabletTVWearable

Badge(value: BadgeParamWithString)

根据字符串创建标记组件。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

从API version 12开始，该组件显隐时支持scale动效。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BadgeParamWithString](ts-container-badge.md#badgeparamwithstring对象说明) | 是 | 字符串标记组件参数。 |

## BadgeParam对象说明

PhonePC/2in1TabletTVWearable

包含用于创建Badge组件的基础参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| position | [BadgePosition](ts-container-badge.md#badgeposition枚举说明)|[Position10+](ts-types.md#position) | 否 | 是 | 设置提示点显示位置。  默认值：BadgePosition.RightTop  **说明：**  Position作为入参，不支持设置百分比；设置为非法值时，默认(0,0)处理。(0,0)为组件左上角位置。  BadgePosition作为入参时，会跟随[Direction](ts-appendix-enums.md#direction)属性控制镜像显示。 |
| style | [BadgeStyle](ts-container-badge.md#badgestyle对象说明) | 否 | 否 | Badge组件可设置样式，支持设置文本颜色、尺寸、圆点颜色和尺寸。 |

## BadgeParamWithNumber对象说明

PhonePC/2in1TabletTVWearable

BadgeParamWithNumber继承自[BadgeParam](ts-container-badge.md#badgeparam对象说明)，具有BadgeParam的全部属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| count | number | 否 | 否 | 设置提醒消息数。  **说明：**  当该值小于等于0且小于maxCount时不显示信息标记。  取值范围：[-2147483648, 2147483647]。超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。 |
| maxCount | number | 否 | 是 | 最大消息数，超过最大消息时仅显示maxCount+，如maxCount是99时，显示99+。  默认值：99  取值范围：[-2147483648, 2147483647]。超出范围时会加上或减去4294967296，使得值仍在范围内，非整数时会舍去小数部分取整数部分，如5.5取5。 |

## BadgeParamWithString对象说明

PhonePC/2in1TabletTVWearable

BadgeParamWithString继承自[BadgeParam](ts-container-badge.md#badgeparam对象说明)，具有BadgeParam的全部属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 提示内容的文本字符串。  **说明：**  从API version 20开始，支持ResourceStr类型。 |

## BadgePosition枚举说明

PhonePC/2in1TabletTVWearable

提示点显示位置。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RightTop | - | 圆点显示在右上角。 |
| Right | - | 圆点显示在右侧纵向居中。 |
| Left | - | 圆点显示在左侧纵向居中。 |

## BadgeStyle对象说明

PhonePC/2in1TabletTVWearable

Badge的样式。包括文本颜色、尺寸、字重、圆点颜色和尺寸。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 文本颜色。  默认值：Color.White  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 文本大小。string类型仅支持number类型取值的字符串形式，可以附带单位，支持的单位有"px"、"vp"、"fp"、"lpx"，例如"10"、"10fp"，不附带单位时默认单位为"fp"。  默认值：10vp  取值范围：大于0；取值为0时不显示文本，取值小于0时取默认值。  **说明：**  1. 不支持设置百分比，当设置为百分比时，按照默认值处理。  2. 从API version 20开始，支持ResourceStr类型。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| badgeSize | number | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | Badge的大小。string类型支持number类型取值的字符串形式，可以附带单位，例如"16"、"16vp"。  默认值：16  单位：vp  取值范围：大于0；取值为0时不显示Badge，取值小于0时取默认值。  **说明：**  1. 不支持设置百分比，当设置为百分比时，按照默认值处理。  2. 从API version 20开始，支持ResourceStr类型。  3. 当设置了fontSize且badgeSize小于fontSize时，badgeSize将按照fontSize生效。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| badgeColor | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | Badge的颜色。  默认值：Color.Red  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| fontWeight10+ | number |[FontWeight](ts-appendix-enums.md#fontweight) | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 设置文本的字体粗细。number类型取值范围：[100, 900]，取值间隔为100。取值越大，字体越粗。设置number类型在取值范围外时，按默认值400处理。string类型仅支持number类型取值的字符串形式，例如"400"，以及"bold"、"bolder"、"lighter"、"regular"、"medium"，分别对应FontWeight中相应的枚举值。  默认值：FontWeight.Normal  **说明：**  不支持设置百分比，当设置为百分比时，按照默认值处理。从API version 20开始，支持ResourceStr类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| borderColor10+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 底板描边颜色。  默认值：Color.Red  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| borderWidth10+ | [Length](ts-types.md#length) | 否 | 是 | 底板描边粗细。  默认值：1  单位：vp  **说明：**  不支持设置百分比，当设置为百分比时，按照默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| outerBorderColor22+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 底板外描边颜色。  默认值：Color.White  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| outerBorderWidth22+ | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 底板外描边粗细。  默认值：0  单位：vp  不支持设置百分比，当设置为百分比时，按照默认值处理。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| enableAutoAvoidance22+ | boolean | 否 | 是 | 增加角标文本延伸显示时是否避让。  true表示避让，false表示不避让。  默认值：true  **说明：**  1. 避让效果为角标文本向组件内部延伸显示。  2. 当外描边的宽度大于0时，角标的延伸起点为外描边的内侧。  3. 当position设置为具体坐标值时，角标不进行避让处理。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

说明

当borderWidth大于0且borderColor与badgeColor颜色不一致时，先绘制角标，再绘制描边。由于边缘像素经过抗锯齿处理，抗锯齿产生半透明像素，四角会出现 badgeColor 颜色的描边线。如需实现相关场景，建议使用[Text](ts-basic-components-text.md)组件设置[outline](ts-universal-attributes-outline.md)代替Badge组件。

## 属性

PhonePC/2in1TabletTVWearable

支持[通用属性](ts-component-general-attributes.md)。

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置标记组件内容）

该示例通过[BadgeParamWithNumber](ts-container-badge.md#badgeparamwithnumber对象说明)的入参value、[BadgeParamWithString](ts-container-badge.md#badgeparamwithstring对象说明)的入参count，实现了传入空值、字符、数字时标记组件展现不同的效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BadgeExample {
5. @Builder
6. tabBuilder(index: number) {
7. Column() {
8. if (index === 2) {
9. Badge({
10. value: '',
11. style: { badgeSize: 6, badgeColor: '#FA2A2D' }
12. }) {
13. Image('/common/public_icon_off.svg')
14. .width(24)
15. .height(24)
16. }
17. .width(24)
18. .height(24)
19. .margin({ bottom: 4 })
20. } else {
21. Image('/common/public_icon_off.svg')
22. .width(24)
23. .height(24)
24. .margin({ bottom: 4 })
25. }
26. Text('Tab')
27. .fontColor('#182431')
28. .fontSize(10)
29. .fontWeight(500)
30. .lineHeight(14)
31. }.width('100%').height('100%').justifyContent(FlexAlign.Center)
32. }

34. @Builder
35. itemBuilder(value: string) {
36. Row() {
37. Image('common/public_icon.svg').width(32).height(32).opacity(0.6)
38. Text(value)
39. .width(177)
40. .height(21)
41. .margin({ left: 15, right: 76 })
42. .textAlign(TextAlign.Start)
43. .fontColor('#182431')
44. .fontWeight(500)
45. .fontSize(16)
46. .opacity(0.9)
47. Image('common/public_icon_arrow_right.svg').width(12).height(24).opacity(0.6)
48. }.width('100%').padding({ left: 12, right: 12 }).height(56)
49. }

51. build() {
52. Column() {
53. // 红点类型的标记组件
54. Text('dotsBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
55. Tabs() {
56. TabContent()
57. .tabBar(this.tabBuilder(0))
58. TabContent()
59. .tabBar(this.tabBuilder(1))
60. TabContent()
61. .tabBar(this.tabBuilder(2))
62. TabContent()
63. .tabBar(this.tabBuilder(3))
64. }
65. .width(360)
66. .height(56)
67. .backgroundColor('#F1F3F5')

69. // 根据字符创建的标记组件
70. Column() {
71. Text('stringBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
72. List({ space: 12 }) {
73. ListItem() {
74. Text('list1').fontSize(14).fontColor('#182431').margin({ left: 12 })
75. }
76. .width('100%')
77. .height(56)
78. .backgroundColor('#FFFFFF')
79. .borderRadius(24)
80. .align(Alignment.Start)

82. ListItem() {
83. Badge({
84. value: 'New',
85. position: BadgePosition.Right,
86. style: { badgeSize: 16, badgeColor: '#FA2A2D' }
87. }) {
88. Text('list2').width(27).height(19).fontSize(14).fontColor('#182431')
89. }.width(49.5).height(19)
90. .margin({ left: 12 })
91. }
92. .width('100%')
93. .height(56)
94. .backgroundColor('#FFFFFF')
95. .borderRadius(24)
96. .align(Alignment.Start)
97. }.width(336)

99. // 根据数字创建的标记组件
100. Text('numberBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
101. List() {
102. ListItem() {
103. this.itemBuilder('list1')
104. }

106. ListItem() {
107. Row() {
108. Image('common/public_icon.svg').width(32).height(32).opacity(0.6)
109. Badge({
110. count: 1,
111. position: BadgePosition.Right,
112. style: { badgeSize: 16, badgeColor: '#FA2A2D' }
113. }) {
114. Text('list2')
115. .width(177)
116. .height(21)
117. .textAlign(TextAlign.Start)
118. .fontColor('#182431')
119. .fontWeight(500)
120. .fontSize(16)
121. .opacity(0.9)
122. }.width(240).height(21).margin({ left: 15, right: 11 })

124. Image('common/public_icon_arrow_right.svg').width(12).height(24).opacity(0.6)
125. }.width('100%').padding({ left: 12, right: 12 }).height(56)
126. }

128. ListItem() {
129. this.itemBuilder('list3')
130. }

132. ListItem() {
133. this.itemBuilder('list4')
134. }
135. }
136. .width(336)
137. .height(232)
138. .backgroundColor('#FFFFFF')
139. .borderRadius(24)
140. .padding({ top: 4, bottom: 4 })
141. .divider({
142. strokeWidth: 0.5,
143. color: 'rgba(0,0,0,0.1)',
144. startMargin: 60,
145. endMargin: 12
146. })
147. }.width('100%').backgroundColor('#F1F3F5').padding({ bottom: 12 })
148. }.width('100%')
149. }
150. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/KjZX3VACQZ2YthLrG4O6rg/zh-cn_image_0000002552800252.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=F7316BC8DDC7AA1A147C4FDF1704557415DE02471600D34C478946E6B311D0C6)

### 示例2（设置数字控制标记显隐）

该示例通过count属性，实现了设置数字0和1时标记组件的隐藏和显示效果。

```
1. // 该示例实现了Badge组件显隐时缩放
2. @Entry
3. @Component
4. struct Index {
5. @State badgeCount: number = 1;

7. build() {
8. Column({ space: 40 }) {
9. Badge({
10. count: this.badgeCount,
11. style: {},
12. position: BadgePosition.RightTop,
13. }) {
14. Image($r('app.media.startIcon'))
15. .width(50)
16. .height(50)
17. }
18. .width(55)

20. Button('count 0').onClick(() => {
21. this.badgeCount = 0;
22. })
23. Button('count 1').onClick(() => {
24. this.badgeCount = 1;
25. })
26. }
27. .margin({ top: 20 })
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/kVKjFUBjTeWXB3MdPtu5AA/zh-cn_image_0000002583439947.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=E452B0A0305656E4C8F8B218C4585FF920DBBD49AFFA0522122A10F159342AB6)

### 示例3（设置外描边和文本延伸方式）

从API version 22开始，该示例使用outerBorderColor和outerBorderWidth属性设置外描边，通过enableAutoAvoidance属性控制增加角标文本延伸显示时是否避让。

```
1. // 该示例实现了Badge组件自定义外描边和文本延伸方向
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct Index {
7. @State badgeValue: string = '1234';
8. @State textAvoid:boolean[] = [false, true];
9. @State textAvoidIndex: number = 0;
10. @State textAvoidString: string [] = ["false", "true"];
11. build() {
12. Column() {
13. Badge({
14. value: this.badgeValue,
15. style: {
16. badgeSize : 30,
17. fontSize:20,
18. outerBorderColor : Color.Pink,
19. outerBorderWidth : LengthMetrics.vp(5),
20. enableAutoAvoidance : this.textAvoid[this.textAvoidIndex]
21. },
22. position:BadgePosition.RightTop
23. }) {
24. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
25. Image($r("app.media.startIcon"))
26. .width(80)
27. .height(80)
28. }
29. .direction(Direction.Ltr)
30. .margin({ top: 20, bottom: 20 })
31. Button("enableAutoAvoidance ： " + this.textAvoidString[this.textAvoidIndex])
32. .onClick(() => {
33. this.textAvoidIndex = (this.textAvoidIndex + 1) % this.textAvoidString.length;
34. })
35. }
36. .width('100%')
37. .height('80%')
38. .alignItems(HorizontalAlign.Center)
39. .justifyContent(FlexAlign.Center)
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/6iotTpHNSrCWbMWEewLyFg/zh-cn_image_0000002552959902.png?HW-CC-KV=V1&HW-CC-Date=20260428T000159Z&HW-CC-Expire=86400&HW-CC-Sign=F85E86B9DF616A7E9E50DC848862E76A42AC69A2CE3BFC9D466D267CDE30628B)
