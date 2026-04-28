---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polygon
title: Polygon
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图形绘制 > Polygon
category: harmonyos-references
scraped_at: 2026-04-28T08:02:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:571ab319eea976a12a8a40de4286a37d7310165c286377c63630ec3dbe9bf156
---

多边形绘制组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Polygon(options?: PolygonOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PolygonOptions](ts-drawing-components-polygon.md#polygonoptions18对象说明) | 否 | Polygon绘制区域。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## PolygonOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Polygon组件绘制属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度，取值范围≥0。  默认值：0  默认单位：vp  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度，取值范围≥0。  默认值：0  默认单位：vp  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### points

PhonePC/2in1TabletTVWearable

points(value: Array<any>)

设置多边形的顶点坐标列表，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 多边形的顶点坐标列表。使用时传入一个二维数组，每个子数组表示一个顶点的[x, y]坐标。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。 |

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

设置边框颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。不设置时，默认边框透明度为0，即没有边框。

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

设置边框间隙，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。取值范围≥0。异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 定义Polygon轮廓的虚线模式的数组，数组元素交替表示线段长度和间隙长度。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。  **说明：**  空数组：实线  偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->...  奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

### strokeDashOffset

PhonePC/2in1TabletTVWearable

strokeDashOffset(value: number | string)

设置边框绘制起点的偏移量，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 边框绘制起点的偏移量。  默认值：0  默认单位：vp  异常值undefined和null按照默认值处理，NaN和Infinity会导致strokeDashArray失效。 |

### strokeLineCap

PhonePC/2in1TabletTVWearable

strokeLineCap(value: LineCapStyle)

设置边框端点绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LineCapStyle](ts-appendix-enums.md#linecapstyle) | 是 | 边框端点绘制样式。  默认值：LineCapStyle.Butt  异常值undefined、null、NaN和Infinity按照默认值处理。 |

### strokeLineJoin

PhonePC/2in1TabletTVWearable

strokeLineJoin(value: LineJoinStyle)

设置边框拐角绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [LineJoinStyle](ts-appendix-enums.md#linejoinstyle) | 是 | 边框拐角绘制样式。  默认值：LineJoinStyle.Miter  异常值undefined、null、NaN和Infinity按照默认值处理。 |

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

设置边框透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性的取值范围是[0.0, 1.0]，若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 边框透明度。  默认值：[stroke](ts-drawing-components-polygon.md#stroke)接口设置的透明度。  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

### strokeWidth

PhonePC/2in1TabletTVWearable

strokeWidth(value: Length)

设置边框宽度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性若为string类型, 暂不支持百分比，百分比按照1px处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 边框宽度，取值范围≥0。  默认值：1  默认单位：vp  异常值undefined、null和NaN按照默认值处理，Infinity按0处理。 |

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

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（组件属性绘制）

通过points、fill、fillOpacity、stroke属性分别绘制多边形的经过坐标、填充颜色、透明度、边框颜色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PolygonExample {
5. build() {
6. Column({ space: 10 }) {
7. // 在 100 * 100 的矩形框中绘制一个三角形，起点(0, 0)，经过(50, 100)，终点(100, 0)
8. Polygon({ width: 100, height: 100 })
9. .points([[0, 0], [50, 100], [100, 0]])
10. .fill(Color.Green)
11. // 在 100 * 100 的矩形框中绘制一个四边形，起点(0, 0)，经过(0, 100)和(100, 100)，终点(100, 0)
12. Polygon()
13. .width(100)
14. .height(100)
15. .points([[0, 0], [0, 100], [100, 100], [100, 0]])
16. .fillOpacity(0)
17. .strokeWidth(5)
18. .stroke(Color.Blue)
19. // 在 100 * 100 的矩形框中绘制一个五边形，起点(50, 0)，依次经过(0, 50)、(20, 100)和(80, 100)，终点(100, 50)
20. Polygon()
21. .width(100)
22. .height(100)
23. .points([[50, 0], [0, 50], [20, 100], [80, 100], [100, 50]])
24. .fill(Color.Red)
25. .fillOpacity(0.6)
26. }.width('100%').margin({ top: 10 })
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/K9b3RY-tTSCpe7lw07GSTQ/zh-cn_image_0000002583480011.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=09A350B6FCCF045C9A12B4E13979D779647D5F94832F7380BC4C0AE9A88BDB38)

### 示例2（宽和高使用不同参数类型绘制多边形）

width、height属性分别使用不同的长度类型绘制图形。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PolygonTypeExample {
5. build() {
6. Column({ space: 10 }) {
7. // 在 100 * 100 的矩形框中绘制一个三角形，起点(0, 0)，经过(50, 100)，终点(100, 0)
8. Polygon({ width: '100', height: '100' }) // 使用string类型
9. .points([[0, 0], [50, 100], [100, 0]])
10. // 在 100 * 100 的矩形框中绘制一个四边形，起点(0, 0)，经过(0, 100)和(100, 100)，终点(100, 0)
11. Polygon({ width: 100, height: 100 })// 使用number类型
12. .points([[0, 0], [0, 100], [100, 100], [100, 0]])
13. .fillOpacity(0)
14. .strokeWidth(5)
15. .stroke(Color.Blue)
16. // 在 100 * 100 的矩形框中绘制一个五边形，起点(50, 0)，依次经过(0, 50)、(20, 100)和(80, 100)，终点(100, 50)
17. Polygon({ width: $r('app.string.PolygonWidth'), height: $r('app.string.PolygonHeight') }) // 使用Resource类型，需用户自定义
18. .points([[50, 0], [0, 50], [20, 100], [80, 100], [100, 50]])
19. .fillOpacity(0.6)
20. }.width('100%').margin({ top: 10 })
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/U2f8KxjuSNuI2IlSgKBenQ/zh-cn_image_0000002552800362.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=080EE2CD1B642BFE04845682F80929EA609578FF49D299113FC174321A1DC56A)

### 示例3（使用attributeModifier动态设置Polygon组件的属性）

以下示例展示了如何使用attributeModifier动态设置Polygon组件的points、fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeLineJoin、strokeMiterLimit、strokeOpacity、strokeWidth和antiAlias属性。

```
1. // xxx.ets
2. class MyPolygonModifier implements AttributeModifier<PolygonAttribute> {
3. applyNormalAttribute(instance: PolygonAttribute): void {
4. // 三角形，起点(0, 0)，经过(50, 100)，终点(100, 0)，填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框间隙[20]，向左偏移15，线条两端样式为半圆，拐角样式使用尖角连接路径段，斜接长度与边框宽度比值的极限值为5，边框透明度0.5，边框宽度10，抗锯齿开启
5. instance.points([[0, 0], [50, 100], [100, 0]])
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
22. struct PolygonModifierDemo {
23. @State modifier: MyPolygonModifier = new MyPolygonModifier()

25. build() {
26. Column() {
27. Polygon()
28. .width(100)
29. .height(100)
30. .attributeModifier(this.modifier)
31. .offset({ x: 20, y: 20 })
32. }
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/VTzccUKgRAWiF877TxlkwQ/zh-cn_image_0000002583440057.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=EA74E98D9530D4338D06BE2239DB89AE35CC6ADAEF2626EB7B5395AFAE035885)
