---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-path
title: Path
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图形绘制 > Path
category: harmonyos-references
scraped_at: 2026-04-29T13:52:39+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:01b749f1b023761a452dcd43c523a972bbe1cddc54e6f9a4de8f1e4176119cd6
---

路径绘制组件，根据绘制路径生成封闭的自定义形状。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Path(options?: PathOptions)

用于描述Path组件绘制属性。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PathOptions](ts-drawing-components-path.md#pathoptions18对象说明) | 否 | Path绘制区域。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## PathOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Path组件绘制属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 路径所在矩形的宽度。  值为异常值或缺省时按照自身内容需要的宽度处理。  默认单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 路径所在矩形的高度。  值为异常值或缺省时按照自身内容需要的高度处理。  默认单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| [commands7+](ts-drawing-components-path.md#commands) | [ResourceStr](ts-types.md#resourcestr) | 否 | 是 | 路径绘制的命令字符串。  值为异常值或缺省时按照自身内容需要的宽高处理。默认值：空字符串  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### commands

PhonePC/2in1TabletTVWearable

commands(value: [ResourceStr](ts-types.md#resourcestr))

设置符合[SVG路径描述规范](ts-drawing-components-path.md#svg路径描述规范)的命令字符串，单位为px。像素单位转换方法请参考[像素单位转换](ts-pixel-units.md)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceStr](ts-types.md#resourcestr) | 是 | 线条绘制的路径。  默认值：空字符串  默认单位：px  异常值undefined和null按照默认值处理。 |

### fill

PhonePC/2in1TabletTVWearable

fill(value: ResourceColor)

设置填充区域的颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。与通用属性foregroundColor同时设置时，后设置的属性生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 填充区域颜色。  默认值：[Color](ts-appendix-enums.md#color).Black  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### fillOpacity

PhonePC/2in1TabletTVWearable

fillOpacity(value: number | string | Resource)

设置填充区域透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 填充区域透明度。  **说明：**  number格式取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0，其余异常值按1.0处理。  string格式支持number格式取值的字符串形式，取值范围与number格式相同。  Resource格式支持系统资源或者应用资源中的字符串，取值范围和number格式相同。  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。  默认值：1.0 |

### stroke

PhonePC/2in1TabletTVWearable

stroke(value: ResourceColor)

设置边框颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框颜色为不透明的黑色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 边框颜色。  默认值：[Color](ts-appendix-enums.md#color).Transparent  异常值undefined和null按照默认值处理，NaN和Infinity按照[Color](ts-appendix-enums.md#color).Black处理。 |

### strokeDashArray

PhonePC/2in1TabletTVWearable

strokeDashArray(value: Array<any>)

设置线条间隙，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。线段相交时可能会出现重叠现象。取值范围≥0，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 定义Path轮廓的虚线模式的数组，数组元素交替表示线段长度和间隙长度。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。  **说明：**  空数组：实线  偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->...  奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

### strokeDashOffset

PhonePC/2in1TabletTVWearable

strokeDashOffset(value: number | string)

设置线条绘制起点的偏移量，设置正值向左边偏移，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 线条绘制起点的偏移量。  默认值：0  默认单位：vp  异常值undefined和null按照默认值处理，NaN和Infinity会导致strokeDashArray失效。 |

### strokeLineCap

PhonePC/2in1TabletTVWearable

strokeLineCap(value: LineCapStyle)

设置线条端点绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LineCapStyle](ts-appendix-enums.md#linecapstyle) | 是 | 线条端点绘制样式。  默认值：LineCapStyle.Butt  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### strokeLineJoin

PhonePC/2in1TabletTVWearable

strokeLineJoin(value: LineJoinStyle)

设置线条拐角绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LineJoinStyle](ts-appendix-enums.md#linejoinstyle) | 是 | 线条拐角绘制样式。  默认值：LineJoinStyle.Miter  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### strokeMiterLimit

PhonePC/2in1TabletTVWearable

strokeMiterLimit(value: number | string)

设置斜接长度与边框宽度比值的极限值，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值需在strokeLineJoin属性取值LineJoinStyle.Miter时生效。

该属性的合法值范围应当大于等于1.0，当取值范围在[0,1)时按1.0处理，其余异常值按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 斜接长度与边框宽度比值的极限值。  默认值：4  异常值undefined、null和NaN按照默认值处理，Infinity会导致stroke失效。 |

### strokeOpacity

PhonePC/2in1TabletTVWearable

strokeOpacity(value: number | string | Resource)

设置线条透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 线条透明度。  默认值：1  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

### strokeWidth

PhonePC/2in1TabletTVWearable

strokeWidth(value: Length)

设置线条宽度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 线条宽度，取值范围≥0。  默认值：1  默认单位：vp  异常值undefined、null和NaN按照默认值处理，Infinity按0处理。 |

### antiAlias

PhonePC/2in1TabletTVWearable

antiAlias(value: boolean)

设置是否开启抗锯齿效果，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启抗锯齿效果。  true：开启抗锯齿；false：关闭抗锯齿。  默认值：true  异常值undefined和null按照false处理。 |

## SVG路径描述规范

PhonePC/2in1TabletTVWearable

SVG路径描述规范支持的命令如下：

| 命令 | 名称 | 参数 | 说明 |
| --- | --- | --- | --- |
| M | moveto | x：起始点的x轴坐标。  y：起始点的y轴坐标。 | 在给定的(x, y)坐标处开始一个新的子路径。例如，M 0 0表示将(0, 0)点作为新子路径的起始点。 |
| L | lineto | x：直线终点的x轴坐标。  y：直线终点的y轴坐标。 | 从当前点到给定的(x, y)坐标画一条线，该坐标成为新的当前点。例如，L 50 50表示绘制当前点到(50, 50)点的直线，并将(50, 50)点作为新子路径的起始点。 |
| H | horizontal lineto | x：水平直线终点的x轴坐标。 | 从当前点绘制一条水平线到给定的x坐标，等效于将y坐标指定为当前点y坐标的L命令。例如，当前点为(100, 100)，H 50 表示绘制当前点到(50, 100)点的直线，并将(50, 100)点作为新子路径的起始点。 |
| V | vertical lineto | y：垂直直线终点的y轴坐标。 | 从当前点绘制一条垂直线到给定的y坐标，等效于将x坐标指定为当前点x坐标的L命令。例如，当前点为(100, 100)，V 50 表示绘制当前点到(100, 50)点的直线，并将(100, 50)点作为新子路径的起始点。 |
| C | curveto | x1：第一个控制点参数的x坐标值。  y1：第一个控制点参数的y坐标值。  x2：第二个控制点参数的x坐标值。  y2：第二个控制点参数的y坐标值。  x：终点参数的x坐标值。  y：终点参数的y坐标值。 | 使用(x1, y1)作为曲线起点的控制点，(x2, y2)作为曲线终点的控制点，从当前点到(x, y)绘制三次贝塞尔曲线。例如，C100 100 250 100 250 200 表示绘制当前点到(250, 200)点的三次贝塞尔曲线，并将(250, 200)点作为新子路径的起始点。 |
| S | smooth curveto | x2：第二个控制点参数的x坐标值。  y2：第二个控制点参数的y坐标值。  x：终点参数的x坐标值。  y：终点参数的y坐标值。 | (x2, y2)作为曲线终点的控制点，绘制从当前点到(x, y)绘制三次贝塞尔曲线。若前一个命令是C或S，则起点控制点是上一个命令的终点控制点相对于起点的映射。例如，C100 100 250 100 250 200 S400 300 400 200第二段贝塞尔曲线的起点控制点为(250, 300)。如果没有前一个命令或者前一个命令不是 C或S，则第一个控制点与当前点重合。 |
| Q | quadratic Bezier curve | x1：第一个控制点参数的x坐标值。  y1：第一个控制点参数的y坐标值。  x：终点参数的x坐标值。  y：终点参数的y坐标值。 | 使用(x1, y1)作为控制点，从当前点到(x, y)绘制二次贝塞尔曲线。例如，Q400 50 600 300 表示绘制当前点到(600, 300)点的二次贝塞尔曲线，并将(600, 300)点作为新子路径的起始点。 |
| T | smooth quadratic Bezier curveto | x：终点参数的x坐标值。  y：终点参数的y坐标值。 | 绘制从当前点到(x, y)绘制二次贝塞尔曲线。若前一个命令是Q或T，则控制点是上一个命令的终点控制点相对于起点的映射。 例如，Q400 50 600 300 T1000 300第二段贝塞尔曲线的控制点为(800, 350)。 如果没有前一个命令或者前一个命令不是Q或T，则第一个控制点与当前点重合。 |
| A | elliptical Arc | rx：椭圆的x轴半径。  ry：椭圆的y轴半径。  x-axis-rotation：椭圆相对于坐标系的旋转角度。  large-arc-flag：标记绘制大弧(1)还是小弧(0)。  sweep-flag：标记向顺时针(1)还是逆时针(0)方向绘制。  x：终点参数的x坐标值。  y：终点参数的y坐标值。 | 从当前点到(x, y)绘制一条椭圆弧。椭圆的大小和方向由两个半径(rx, ry)和x-axis-rotation定义，指示整个椭圆相对于当前坐标系如何旋转（以度为单位）。 large-arc-flag 和 sweep-flag确定弧的绘制方式。 |
| Z | closepath | none | 通过将当前路径连接回当前子路径的初始点来关闭当前子路径。 |

例如：commands('M0 20 L50 50 L50 100 Z')定义了一个三角形，起始于位置(0, 20)，接着绘制点(0, 20)到点(50, 50)的直线，再绘制从点(50, 50)到点(50, 100)的直线，最后绘制从点(50, 100)到(0, 20)的直线关闭路径，形成封闭三角形。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（组件属性绘制）

通过commands、fillOpacity、stroke属性分别绘制路径、透明度、边框颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PathExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('Straight line')
8. .fontSize(11)
9. .fontColor(0xCCCCCC)
10. .width('90%')
11. // 绘制一条长600px，宽3vp的直线
12. Path()
13. .width('600px')
14. .height('10px')
15. .commands('M0 0 L600 0')
16. .stroke(Color.Black)
17. .strokeWidth(3)

19. Text('Straight line graph')
20. .fontSize(11)
21. .fontColor(0xCCCCCC)
22. .width('90%')
23. // 绘制直线图形
24. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
25. Path()
26. .width('210px')
27. .height('310px')
28. .commands('M100 0 L200 240 L0 240 Z')
29. .fillOpacity(0)
30. .stroke(Color.Black)
31. .strokeWidth(3)
32. Path()
33. .width('210px')
34. .height('310px')
35. .commands('M0 0 H200 V200 H0 Z')
36. .fillOpacity(0)
37. .stroke(Color.Black)
38. .strokeWidth(3)
39. Path()
40. .width('210px')
41. .height('310px')
42. .commands('M100 0 L0 100 L50 200 L150 200 L200 100 Z')
43. .fillOpacity(0)
44. .stroke(Color.Black)
45. .strokeWidth(3)
46. }.width('95%')

48. Text('Curve graphics').fontSize(11).fontColor(0xCCCCCC).width('90%')
49. // 绘制弧线图形
50. Flex({ justifyContent: FlexAlign.SpaceBetween }) {
51. Path()
52. .width('250px')
53. .height('310px')
54. .commands("M0 300 S100 0 240 300 Z")
55. .fillOpacity(0)
56. .stroke(Color.Black)
57. .strokeWidth(3)
58. Path()
59. .width('210px')
60. .height('310px')
61. .commands('M0 150 C0 100 140 0 200 150 L100 300 Z')
62. .fillOpacity(0)
63. .stroke(Color.Black)
64. .strokeWidth(3)
65. Path()
66. .width('210px')
67. .height('310px')
68. .commands('M0 100 A30 20 20 0 0 200 100 Z')
69. .fillOpacity(0)
70. .stroke(Color.Black)
71. .strokeWidth(3)
72. }.width('95%')
73. }.width('100%')
74. .margin({ top: 5 })
75. }
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/t2jjPSNBQGe7UdajGPMRlA/zh-cn_image_0000002558766538.png?HW-CC-KV=V1&HW-CC-Date=20260429T055236Z&HW-CC-Expire=86400&HW-CC-Sign=AEF4DD1144CEF878745B6C07E16F4D42612E52A9F6BB1A431BF23863F2A28DE7)

### 示例2（使用不同参数类型绘制路径）

width、height、commands属性分别使用不同的长度类型绘制图形。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PathTypeExample {
5. build() {
6. Column({ space: 10 }) {
7. // 宽、高、命令字符串使用string类型，绘制一条直线。
8. Path({ width: '600px', height: '10px' })
9. .commands('M0 0 L600 0')
10. .fillOpacity(0)
11. .stroke(Color.Black)
12. .strokeWidth(3)
13. // 宽、高使用number类型，绘制一个矩形图形。
14. Path({ width: 200, height: 100 })
15. .commands('M200 0 H400 V200 H200 Z')
16. .fillOpacity(0)
17. .stroke(Color.Black)
18. .strokeWidth(3)
19. // 宽、高、命令字符串使用Resource类型（需用户自定义），绘制一个弧线图形。
20. Path({ width: $r('app.string.PathWidth'), height: $r('app.string.PathHeight') }) // 本示例中PathWidth和PathHeight均定义为"200"。
21. .commands($r('app.string.PathCommands')) // 本示例中PathCommands定义为"M150 300 Q300 0 450 300 Z"。
22. .fillOpacity(0)
23. .stroke(Color.Black)
24. .strokeWidth(3)
25. }.width('100%')
26. .margin({ top: 5 })
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/x-EZff5RTI-v4hVsl8I6EQ/zh-cn_image_0000002558606878.png?HW-CC-KV=V1&HW-CC-Date=20260429T055236Z&HW-CC-Expire=86400&HW-CC-Sign=519DC248BC2666C4B0814FC2F5673DCC0FFDB289CA474E842CA9BD88AF61B28C)

### 示例3（使用attributeModifier动态设置Path组件的属性）

以下示例展示了如何使用attributeModifier动态设置Path组件的commands、fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeLineJoin、strokeMiterLimit、strokeOpacity、strokeWidth和antiAlias属性。

```
1. // xxx.ets
2. class MyPathModifier implements AttributeModifier<PathAttribute> {
3. applyNormalAttribute(instance: PathAttribute): void {
4. // 使用字符串commands绘制一个三角形，填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框间隙[20]，向左偏移15，线条两端样式为半圆，拐角样式使用尖角连接路径段，斜接长度与边框宽度比值的极限值为5，边框透明度0.5，边框宽度10，抗锯齿开启
5. instance.commands('M100 0 L200 240 L0 240 Z')
6. instance.fill("#707070")
7. instance.fillOpacity(0.5)
8. instance.stroke("#2787D9")
9. instance.strokeDashArray([20])
10. instance.strokeDashOffset("15")
11. instance.strokeLineCap(LineCapStyle.Round)
12. instance.strokeLineJoin(LineJoinStyle.Miter)
13. instance.strokeMiterLimit(5)
14. instance.strokeOpacity(0.5)
15. instance.strokeWidth(10)
16. instance.antiAlias(true)
17. }
18. }

20. @Entry
21. @Component
22. struct PathModifierDemo {
23. @State modifier: MyPathModifier = new MyPathModifier()

25. build() {
26. Column() {
27. Path()
28. .attributeModifier(this.modifier)
29. .offset({ x: 20, y: 20 })
30. }
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/oSb7UvfTQneidHhUH0WdKA/zh-cn_image_0000002589326405.png?HW-CC-KV=V1&HW-CC-Date=20260429T055236Z&HW-CC-Expire=86400&HW-CC-Sign=B12ABA5C454514505CB6E759B25F49BC8CE0E6FF65109563EBC20B5F13B36131)
