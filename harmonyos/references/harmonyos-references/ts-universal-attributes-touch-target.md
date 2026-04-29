---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-touch-target
title: 触摸热区设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 交互属性 > 触摸交互控制 > 触摸热区设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eac14d73bdc1b5dbdcdfebf2422110cd172acc3a16648160cd4df384a4be44c2
---

设置组件的响应热区。在ArkUI开发框架中，处理触屏事件和鼠标事件时，会在事件触发前进行按压点与组件响应热区的[触摸测试](../harmonyos-guides/arkts-interaction-basic-principles.md#触摸测试)，以收集需响应事件的组件。基于测试结果，框架会分发相应的事件。影响[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[拖拽事件](ts-universal-events-drag-drop.md)、[鼠标事件](ts-universal-mouse-key.md)、[轴事件](ts-universal-events-axis.md)、[悬浮事件](ts-universal-events-hover.md)、[无障碍悬浮事件](ts-universal-accessibility-hover-event.md)和[手势事件](ts-gesture-settings.md)的分发。

说明

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 设置触摸热区属性时，手指需在热区内按下，随后抬起时若满足事件响应条件，事件将被触发。此外，在当前手势结束前，若条件满足，可持续触发的事件也会被激活。

## responseRegion

PhonePC/2in1TabletTVWearable

responseRegion(value: Array<Rectangle> | Rectangle): T

设置一个或多个触摸热区。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明)> | [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 是 | 触摸热区，包括位置和大小。  默认触摸热区为整个组件，默认值：  {  x：0,  y：0,  width：'100%',  height：'100%'  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## mouseResponseRegion10+

PhonePC/2in1TabletTVWearable

mouseResponseRegion(value: Array<Rectangle> | Rectangle): T

设置一个或多个鼠标触摸热区。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<[Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明)> | [Rectangle](ts-universal-attributes-touch-target.md#rectangle对象说明) | 是 | 鼠标触摸热区，包括位置和大小。  默认触摸热区为整个组件，默认值：  {  x：0,  y：0,  width：'100%',  height：'100%'  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## responseRegionList22+

PhonePC/2in1TabletTVWearable

responseRegionList(regions: Array<ResponseRegion>): T

设置组件的触摸热区列表。调用该接口时，[responseRegion](ts-universal-attributes-touch-target.md#responseregion)与[mouseResponseRegion](ts-universal-attributes-touch-target.md#mouseresponseregion10)接口不再生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regions | Array<[ResponseRegion](ts-universal-attributes-touch-target.md#responseregion22对象说明)> | 是 | 组件的触摸热区数组。  每个触摸热区均包括输入工具类型、位置和大小。  默认值：  [{  tool：ResponseRegionSupportedTool.ALL,  x：LengthMetrics.vp(0),  y：LengthMetrics.vp(0),  width：LengthMetrics.percent(1),  height：LengthMetrics.percent(1)  }] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## Rectangle对象说明

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | [Length](ts-types.md#length) | 否 | 是 | 触摸点相对于组件左上角的x轴坐标。  默认值：0vp |
| y | [Length](ts-types.md#length) | 否 | 是 | 触摸点相对于组件左上角的y轴坐标。  默认值：0vp |
| width | [Length](ts-types.md#length) | 否 | 是 | 触摸热区的宽度。  默认值：'100%' |
| height | [Length](ts-types.md#length) | 否 | 是 | 触摸热区的高度。  默认值：'100%' |

说明

* x和y可以设置正负值百分比。当x设置为'100%'时表示热区往右偏移组件本身宽度大小，当x设置为'-100%'时表示热区往左偏移组件本身宽度大小。当y设置为'100%'时表示热区往下偏移组件本身高度大小，当y设置为'-100%'时表示热区往上偏移组件本身高度大小。
* width和height只能设置正值百分比。width：'100%'表示热区宽度设置为该组件本身的宽度。比如组件本身宽度是100vp，那么'100%'表示热区宽度也为100vp。height：'100%'表示热区高度设置为该组件本身的高度。
* 百分比相对于组件自身宽高进行计算。
* 当父组件设置[clip](ts-universal-attributes-sharp-clipping.md#clip12)(true)时，子组件的响应会受到父组件触摸热区的影响，不在父组件触摸热区内的子组件无法响应手势和事件。
* width和height不支持calc()的动态计算。

## ResponseRegion22+对象说明

PhonePC/2in1TabletTVWearable

由输入工具类型、触摸位置和大小组成的触摸热区。

说明

* 当父组件设置[clip](ts-universal-attributes-sharp-clipping.md#clip12)为true时，子组件的响应会受到父组件触摸热区的影响，不在父组件触摸热区内的子组件无法响应手势和事件。
* 如果触摸热区未配置输入工具类型，触摸位置和大小均采用默认值。
* x和y的计算结果为正值时，分别代表向右偏移和向下偏移；当计算结果为负值时，分别代表向左偏移和向上偏移。
* width和height采用string类型时，string需采用小写字符否则不生效，支持calc()的动态计算。指定calc()的入参字符串格式为'宽高缩放比例 ± 宽高增量'，宽高缩放比例为百分比，宽高增量单位为px或vp。例如'calc(80% + 10vp)'中，80%为宽高缩放比例、10vp为宽高增量。width和height采用LengthMetrics类型且单位为percent时，相对于组件自身宽高进行计算，percent(1)代表100%。当计算结果为负值时，采用默认值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tool | [ResponseRegionSupportedTool](ts-appendix-enums.md#responseregionsupportedtool22) | 否 | 是 | 触摸热区适用的输入工具类型。  默认值：ResponseRegionSupportedTool.ALL |
| x | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 触摸点相对于组件左上角的x轴坐标。  默认值：LengthMetrics.vp(0) |
| y | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 是 | 触摸点相对于组件左上角的y轴坐标。  默认值：LengthMetrics.vp(0) |
| width | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | string | 否 | 是 | 触摸热区的宽度。  默认值：LengthMetrics.percent(1) |
| height | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | string | 否 | 是 | 触摸热区的高度。  默认值：LengthMetrics.percent(1) |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（通过responseRegion接口设置触摸热区）

该示例通过responseRegion设置按钮的触摸热区以响应点击事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TouchTargetExample {
5. @State text: string = "";

7. build() {
8. Column({ space: 20 }) {
9. Text("{x:0,y:0,width:'50%',height:'100%'}")
10. // 热区宽度为按钮的一半，点击button1右半部无响应
11. Button("button1")
12. .responseRegion({
13. x: 0,
14. y: 0,
15. width: '50%',
16. height: '100%'
17. })
18. .onClick(() => {
19. this.text = 'button1 clicked'
20. })

22. // 为一个组件添加多个热区
23. Text("[{x:'100%',y:0,width:'50%',height:'100%'}," +
24. "\n{ x: 0, y: 0, width: '50%', height: '100%' }]")
25. Button("button2")
26. .responseRegion([
27. {
28. x: '100%',
29. y: 0,
30. width: '50%',
31. height: '100%'
32. }, // 第一个热区宽度为按钮的一半，且右移一个按钮宽度，点击button2右边按钮宽度一半的区域，点击事件生效
33. {
34. x: 0,
35. y: 0,
36. width: '50%',
37. height: '100%'
38. }// 第二个热区宽度为按钮的一半，点击button2左半部，点击事件生效
39. ])
40. .onClick(() => {
41. this.text = 'button2 clicked'
42. })
43. // 热区大小为整个按钮，且下移一个按钮高度，点击button3下方按钮大小区域，点击事件生效
44. Text("{x:0,y:'100%',width:'100%',height:'100%'}")
45. Button("button3")
46. .responseRegion({
47. x: 0,
48. y: '100%',
49. width: '100%',
50. height: '100%'
51. })
52. .onClick(() => {
53. this.text = 'button3 clicked'
54. })

56. Text(this.text).margin({ top: 50 })
57. }.width('100%').margin({ top: 10 })
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/FinD5ujxReCKu0O7yfvleg/zh-cn_image_0000002558606406.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055124Z&HW-CC-Expire=86400&HW-CC-Sign=FF1D04DBF5DA3CC6AD86F7134639DD1CBE699D4076F233FD8CADD7D9C23339D2)

### 示例2（通过responseRegionList接口设置触摸热区）

该示例通过[responseRegionList](ts-universal-attributes-touch-target.md#responseregionlist22)设置按钮的触摸热区以响应点击事件。

从API version 22开始，新增responseRegionList接口。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct TouchTargetExample {
7. @State text: string = "";

9. build() {
10. Column({ space: 20 }) {
11. Text("left part of button1")
12. // 热区宽度为按钮的一半，点击button1右半部无响应
13. Button("button1")
14. .responseRegionList([{
15. x: LengthMetrics.vp(0),
16. y: LengthMetrics.vp(0),
17. width: LengthMetrics.percent(0.5),
18. height: LengthMetrics.percent(1),
19. }])
20. .onClick(() => {
21. this.text = 'button1 clicked'
22. })

24. // 热区一的大小为整个按钮，且右移一个按钮宽度，点击button2左边按钮大小区域，点击事件生效
25. // 热区二的大小为整个按钮，且下移一个按钮高度，鼠标点击button2下方按钮大小区域，点击事件生效
26. Text("one button size right of button2," + "\n one button size below button2")
27. Button("button2")
28. .responseRegionList([{
29. x: LengthMetrics.percent(1),
30. y: LengthMetrics.vp(0),
31. width: LengthMetrics.percent(1),
32. height: LengthMetrics.percent(1),
33. }, {
34. tool: ResponseRegionSupportedTool.MOUSE,
35. x: LengthMetrics.vp(0),
36. y: LengthMetrics.percent(1),
37. width: 'calc(100% + 0vp)',
38. height: 'calc(100% - 0px)',
39. }])
40. .onClick(() => {
41. this.text = 'button2 clicked'
42. })

44. Text(this.text).margin({ top: 50 })
45. }.width('100%').margin({ top: 10 })
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/MR2H6zRfRnuGP11RV0zbGw/zh-cn_image_0000002589325933.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055124Z&HW-CC-Expire=86400&HW-CC-Sign=1904DD1B508CE242F49D7D20C881D5B9F459C8DB685AA921D27EC1E8134F5DCB)

### 示例3（设置鼠标的触摸热区以响应点击事件）

该示例通过[mouseResponseRegion](ts-universal-attributes-touch-target.md#mouseresponseregion10)设置鼠标的触摸热区以响应点击事件。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MouseResponseRegionExample {
5. @State clickInfo: string = '点击热区触发事件';

7. build() {
8. Column({ space: 30 }) {
9. // 示例1：单个热区（仅按钮左半部分响应鼠标点击）
10. Text('热区：按钮左半区域（点击左半才触发）')
11. .fontSize(14)
12. Button('Button1（左半热区）')
13. .width(200)
14. .height(60)
15. // 鼠标热区：仅按钮左半部分（x/y相对组件自身，宽度50%）
16. .mouseResponseRegion({
17. // 热区相对组件的X坐标（左上角为原点）
18. x: 0,
19. // 热区相对组件的Y坐标
20. y: 0,
21. // 热区宽度（按钮的50%）
22. width: '50%',
23. // 热区高度（按钮的100%）
24. height: '100%'
25. })
26. .onClick(() => {
27. this.clickInfo = 'Button1 左半热区被点击';
28. })
29. // 示例2：多个热区（按钮左半 + 按钮下方区域都响应）
30. Text('热区：按钮左半 + 按钮下方区域（点击两处都触发）')
31. .fontSize(14)
32. Button('Button2（多热区）')
33. .width(200)
34. .height(60)
35. // 鼠标热区：数组形式，包含2个独立热区
36. .mouseResponseRegion([
37. // 热区1：按钮左半部分
38. {
39. x: 0,
40. y: 0,
41. width: '50%',
42. height: '100%'
43. },
44. // 热区2：按钮正下方区域（y=100%表示按钮底部，高度60vp）
45. {
46. x: 0,
47. y: '100%',
48. width: '100%',
49. height: 60
50. }
51. ])
52. .onClick(() => {
53. this.clickInfo = 'Button2 任一热区被点击';
54. })
55. // 示例3：热区在按钮外部（按钮右侧空白处响应）
56. Text('热区：按钮右侧外部（点击按钮右边空白处触发）')
57. .fontSize(14)
58. Button('Button3（右侧外热区）')
59. .width(200)
60. .height(60)
61. // 鼠标热区：按钮右侧外部区域（x=100%表示按钮右边缘）
62. .mouseResponseRegion({
63. // 热区X坐标：按钮右边缘
64. x: '100%',
65. y: 0,
66. // 热区宽度80vp
67. width: 80,
68. height: '100%'
69. })
70. .onClick(() => {
71. this.clickInfo = 'Button3 右侧外热区被点击';
72. })
73. // 显示点击结果
74. Text(this.clickInfo)
75. .fontSize(16)
76. .margin({ top: 20 })
77. }
78. .width('100%')
79. .height('100%')
80. // 整体居中显示
81. .justifyContent(FlexAlign.Center)
82. }
83. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/UTj6KzzKTeCUZPm7X6Xi-w/zh-cn_image_0000002589245875.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055124Z&HW-CC-Expire=86400&HW-CC-Sign=0FDC75C920F7E58D115D4424288BADB1543810F6F86F2B2B410AA638376061A5)
