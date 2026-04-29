---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-border
title: 边框设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 布局与边框 > 边框设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e1558bab4ddd05eaeddde904ab90b9f865cd89ed0c55b32698b5b1ff5b74e312
---

设置组件边框样式。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## border

PhonePC/2in1TabletTVWearable

border(value: BorderOptions): T

设置边框样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderOptions](ts-types.md#borderoptions) | 是 | 统一边框样式设置接口。  **说明：**  边框宽度默认值为0，即不显示边框。  从API version 9开始，父节点的border显示在子节点内容之上。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

color、radius缺省时，为了保证[borderColor](ts-universal-attributes-border.md#bordercolor)、[borderRadius](ts-universal-attributes-border.md#borderradius)生效，需要将[borderColor](ts-universal-attributes-border.md#bordercolor)、[borderRadius](ts-universal-attributes-border.md#borderradius)设置在[border](ts-universal-attributes-border.md#border)后。

## borderStyle

PhonePC/2in1TabletTVWearable

borderStyle(value: BorderStyle | EdgeStyles): T

设置元素的边框线条样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BorderStyle](ts-appendix-enums.md#borderstyle) | [EdgeStyles](ts-types.md#edgestyles9)9+ | 是 | 设置元素的边框样式。  默认值：BorderStyle.Solid |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderWidth

PhonePC/2in1TabletTVWearable

borderWidth(value: Length | EdgeWidths | LocalizedEdgeWidths): T

设置边框的宽度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [EdgeWidths](ts-types.md#edgewidths9)9+ | [LocalizedEdgeWidths](ts-types.md#localizededgewidths12)12+ | 是 | 设置元素的边框宽度，不支持百分比。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderColor

PhonePC/2in1TabletTVWearable

borderColor(value: ResourceColor | EdgeColors | LocalizedEdgeColors): T

设置边框的颜色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | [EdgeColors](ts-types.md#edgecolors9)9+ | [LocalizedEdgeColors](ts-types.md#localizededgecolors12)12+ | 是 | 设置元素的边框颜色。  默认值：Color.Black |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderRadius

PhonePC/2in1TabletTVWearable

borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses): T

设置边框的圆角半径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9)9+ | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12)12+ | 是 | 设置元素的边框圆角半径，支持百分比，百分比依据组件宽度。设置圆角后，可搭配[clip](ts-universal-attributes-sharp-clipping.md#clip12)属性进行裁剪，避免子组件超出组件自身。  设置四个不同圆角值，若某个圆角值超过高度或者宽度最小值一半时，按值的比例绘制异形圆角。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## borderRadius22+

PhonePC/2in1TabletTVWearable

borderRadius(value: Length | BorderRadiuses | LocalizedBorderRadiuses, type?: RenderStrategy): T

设置边框的圆角半径和绘制圆角的模式。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | [BorderRadiuses](ts-types.md#borderradiuses9) | [LocalizedBorderRadiuses](ts-types.md#localizedborderradiuses12) | 是 | 设置元素的边框圆角半径，支持百分比，百分比依据组件宽度。设置圆角后，可搭配[clip](ts-universal-attributes-sharp-clipping.md#clip12)属性进行裁剪，避免子组件超出组件自身。 |
| type | [RenderStrategy](ts-appendix-enums.md#renderstrategy22) | 否 | 设置组件绘制圆角的模式。  默认值：RenderStrategy.FAST |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（基本样式用法）

设置边框的宽度、颜色、圆角半径以及点、线样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BorderExample {
5. build() {
6. Column() {
7. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
8. // 线段
9. Text('dashed')
10. .borderStyle(BorderStyle.Dashed)
11. .borderWidth(5)
12. .borderColor(0xAFEEEE)
13. .borderRadius(10)
14. .width(120)
15. .height(120)
16. .textAlign(TextAlign.Center)
17. .fontSize(16)
18. // 点线
19. Text('dotted')
20. .border({
21. width: 5,
22. color: 0x317AF7,
23. radius: 10,
24. style: BorderStyle.Dotted
25. })
26. .width(120)
27. .height(120)
28. .textAlign(TextAlign.Center)
29. .fontSize(16)
30. }.width('100%').height(150)

32. Text('.border')
33. .fontSize(50)
34. .width(300)
35. .height(300)
36. .border({
37. width: {
38. left: 3,
39. right: 6,
40. top: 10,
41. bottom: 15
42. },
43. color: {
44. left: '#e3bbbb',
45. right: Color.Blue,
46. top: Color.Red,
47. bottom: Color.Green
48. },
49. radius: {
50. topLeft: 10,
51. topRight: 20,
52. bottomLeft: 40,
53. bottomRight: 80
54. },
55. style: {
56. left: BorderStyle.Dotted,
57. right: BorderStyle.Dotted,
58. top: BorderStyle.Solid,
59. bottom: BorderStyle.Dashed
60. }
61. })
62. .textAlign(TextAlign.Center)
63. }
64. }
65. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/H6-WeMKGQTm1XNoyvH89XA/zh-cn_image_0000002558766024.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055116Z&HW-CC-Expire=86400&HW-CC-Sign=B290885429C5D303C5E9186F0254172114259B35B69DEE649A5B5837F94E51E9)

### 示例2（边框宽度类型和边框颜色）

border属性的width、radius、color属性值使用LocalizedEdgeWidths类型和LocalizedEdgeColors类型。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct BorderExample {
7. build() {
8. Column() {
9. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
10. // 线段
11. Text('dashed')
12. .borderStyle(BorderStyle.Dashed)
13. .borderWidth(5)
14. .borderColor(0xAFEEEE)
15. .borderRadius(10)
16. .width(120)
17. .height(120)
18. .textAlign(TextAlign.Center)
19. .fontSize(16)
20. // 点线
21. Text('dotted')
22. .border({
23. width: 5,
24. color: 0x317AF7,
25. radius: 10,
26. style: BorderStyle.Dotted
27. })
28. .width(120)
29. .height(120)
30. .textAlign(TextAlign.Center)
31. .fontSize(16)
32. }.width('100%').height(150)

34. Text('.border')
35. .fontSize(50)
36. .width(300)
37. .height(300)
38. .border({
39. width: {
40. start: LengthMetrics.vp(3),
41. end: LengthMetrics.vp(6),
42. top: LengthMetrics.vp(10),
43. bottom: LengthMetrics.vp(15)
44. },
45. color: {
46. start: '#e3bbbb',
47. end: Color.Blue,
48. top: Color.Red,
49. bottom: Color.Green
50. },
51. radius: {
52. topStart: LengthMetrics.vp(10),
53. topEnd: LengthMetrics.vp(20),
54. bottomStart: LengthMetrics.vp(40),
55. bottomEnd: LengthMetrics.vp(80)
56. },
57. style: {
58. left: BorderStyle.Dotted,
59. right: BorderStyle.Dotted,
60. top: BorderStyle.Solid,
61. bottom: BorderStyle.Dashed
62. }
63. })
64. .textAlign(TextAlign.Center)
65. }
66. }
67. }
```

从左至右显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/XK6leMFKT-Sc0WazE-uR3Q/zh-cn_image_0000002558606366.png?HW-CC-KV=V1&HW-CC-Date=20260429T055116Z&HW-CC-Expire=86400&HW-CC-Sign=9B47A1C8266EFC5B9D23013887CAA9B9093873B8CDF9C21F6334232FD7FB9FBD)

从右至左显示语言示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/msrq0SYQRWqGd7-XwbY9lQ/zh-cn_image_0000002589325893.png?HW-CC-KV=V1&HW-CC-Date=20260429T055116Z&HW-CC-Expire=86400&HW-CC-Sign=BEF503BBC504741FFE8EA05CD6D9A84B3782B2BA3E5E767A34BDD3B0FBCFA6BC)

### 示例3（设置离屏圆角）

从API version 22开始，该示例支持设置组件绘制圆角的模式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RenderStrategyExample {
5. build() {
6. NavDestination() {
7. Column({ space: 20 }) {
8. Stack() {
9. Column()
10. .width(320)
11. .height(320)
12. .backgroundColor(Color.Black)

14. Stack() {
15. Stack() {
16. Scroll(new Scroller()) {
17. Image($r('app.media.startIcon'))
18. .width('100%')
19. .height('200%')
20. }

22. Column()
23. .blur(50)
24. .width(300)
25. .height(100)
26. .position({ x: 0, y: 0 })
27. }
28. }
29. .width(300)
30. .height(300)
31. .backgroundColor(Color.Pink)
32. .borderRadius(50, RenderStrategy.FAST)
33. .clip(true)
34. }

36. Stack() {
37. Column()
38. .width(320)
39. .height(320)
40. .backgroundColor(Color.Black)

42. Stack() {
43. Stack() {
44. Scroll(new Scroller()) {
45. Image($r('app.media.startIcon'))
46. .width('100%')
47. .height('200%')
48. }

50. Column()
51. .blur(50)
52. .width(300)
53. .height(100)
54. .position({ x: 0, y: 0 })
55. }
56. }
57. .width(300)
58. .height(300)
59. .backgroundColor(Color.Pink)
60. .borderRadius(50, RenderStrategy.OFFSCREEN)
61. .clip(true)
62. }
63. }
64. }
65. .width('100%')
66. .height('100%')
67. }
68. }
```

设置在线绘制模式（上方）以及离屏绘制模式（下方）的示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/4LLh1eVmQTWFo3BH9GQ11A/zh-cn_image_0000002589245835.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055116Z&HW-CC-Expire=86400&HW-CC-Sign=DB269679F37F7CA9A0E6F813397CE84505A4EAAABB82AF6C080B0396F1197E05)

### 示例4（设置异形圆角）

该示例通过[borderRadius](ts-universal-attributes-border.md#borderradius)设置四个不同圆角值。当其中一个圆角值超过高度或宽度最小值的一半时，按值的比例绘制异形圆角。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BorderExample {
5. build() {
6. Column() {
7. Flex({ justifyContent: FlexAlign.SpaceAround, alignItems: ItemAlign.Center }) {
8. Text('Text')
9. .borderWidth(5)
10. .borderColor(0xAFEEEE)
11. .borderRadius({
12. topLeft: 2000,
13. topRight: 10,
14. bottomLeft: 30,
15. bottomRight: 50
16. })
17. .width(100)
18. .height(100)
19. .textAlign(TextAlign.Center)
20. .fontSize(16)
21. }
22. }
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/jsYyE0UIQSOhR0LNlJBFnA/zh-cn_image_0000002558766026.png?HW-CC-KV=V1&HW-CC-Date=20260429T055116Z&HW-CC-Expire=86400&HW-CC-Sign=BDA21368C291FB28F99D22D5957E006D6760F90AE1D5412C68679951482C99C9)
