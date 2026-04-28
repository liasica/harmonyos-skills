---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-polyline
title: Polyline
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图形绘制 > Polyline
category: harmonyos-references
scraped_at: 2026-04-28T08:02:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:e4388ff865cb993f29fa0cc1932fe4e8b687a23110ec8e243cf0ae1d705861aa
---

折线绘制组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Polyline(options?: PolylineOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PolylineOptions](ts-drawing-components-polyline.md#polylineoptions18对象说明) | 否 | Polyline绘制区域。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## PolylineOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Polyline组件绘制属性。

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

设置折线经过坐标点列表，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 折线经过坐标点列表。使用时传入一个二维数组，每个子数组表示一个顶点的[x, y]坐标。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。 |

### fill

PhonePC/2in1TabletTVWearable

fill(value: ResourceColor)

设置填充区域的颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。与通用属性foregroundColor同时设置时，后设置的属性生效。

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

设置边框颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即无边框。

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
| value | Array<any> | 是 | 定义Polyline轮廓的虚线模式的数组，数组元素交替表示线段长度和间隙长度。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。  **说明：**  空数组：实线  偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->...  奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

### strokeDashOffset

PhonePC/2in1TabletTVWearable

strokeDashOffset(value: number | string)

设置线条绘制起点的偏移量，设置正值向左边偏移，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

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

设置斜接长度与边框宽度比值的极限值，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。斜接长度表示外边框外边交点到内边交点的距离，边框宽度即strokeWidth属性的值。该属性取值仅在strokeLineJoin属性取值LineJoinStyle.Miter时生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 斜接长度与边框宽度比值的极限值。  默认值：4  该属性的合法值应当大于等于1.0，当取值范围在[0,1)时按1.0处理。  异常值undefined、null和NaN按照默认值处理，Infinity会导致stroke失效。 |

### strokeOpacity

PhonePC/2in1TabletTVWearable

strokeOpacity(value: number | string | Resource)

设置线条透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | [Resource](ts-types.md#resource) | 是 | 线条透明度，取值范围是[0.0, 1.0]。  默认值：[stroke](ts-drawing-components-polyline.md#stroke)接口设置的透明度。  若给定值小于0.0，则取值为0.0；若给定值大于1.0，则取值为1.0。  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

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

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（组件属性绘制）

通过points、fillOpacity、stroke、strokeLineJoin、strokeLineCap属性分别绘制折线的经过坐标、透明度、边框颜色、拐角样式、端点样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PolylineExample {
5. build() {
6. Column({ space: 10 }) {
7. // 在 100 * 100 的矩形框中绘制一段折线，起点(0, 0)，经过(20,60)，到达终点(100, 100)
8. Polyline({ width: 100, height: 100 })
9. .points([[0, 0], [20, 60], [100, 100]])
10. .fillOpacity(0)
11. .stroke(Color.Blue)
12. .strokeWidth(3)
13. // 在 100 * 100 的矩形框中绘制一段折线，起点(20, 0)，经过(0,100)，到达终点(100, 90)
14. Polyline()
15. .width(100)
16. .height(100)
17. .fillOpacity(0)
18. .stroke(Color.Red)
19. .strokeWidth(8)
20. .points([[20, 0], [0, 100], [100, 90]])
21. // 设置折线拐角处为圆弧
22. .strokeLineJoin(LineJoinStyle.Round)
23. // 设置折线两端为半圆
24. .strokeLineCap(LineCapStyle.Round)
25. }.width('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/M1KYhC6uS42iOhIS-4PrBQ/zh-cn_image_0000002552800360.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=72A0883C5C3CE70FBBA61962AA0FC45FD429F9F180327AFCDA524FD9940C5940)

### 示例2（宽和高使用不同参数类型绘制折线）

width、height属性分别使用不同的长度类型绘制图形。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PolylineTypeExample {
5. build() {
6. Column({ space: 10 }) {
7. // 在 100 * 100 的矩形框中绘制一段折线，起点(0, 0)，经过(20,60)，到达终点(100, 100)
8. Polyline({ width: '100', height: '100' }) // 使用string类型
9. .points([[0, 0], [20, 60], [100, 100]])
10. .fillOpacity(0)
11. .stroke(Color.Blue)
12. .strokeWidth(3)
13. Polyline({ width: 100, height: 100 }) // 使用number类型
14. .points([[0, 0], [20, 60], [100, 100]])
15. .fillOpacity(0)
16. .stroke(Color.Blue)
17. .strokeWidth(3)
18. Polyline({ width: $r('app.string.PolylineWidth'), height: $r('app.string.PolylineHeight') }) // 使用Resource类型，需用户自定义
19. .points([[0, 0], [20, 60], [100, 100]])
20. .fillOpacity(0)
21. .stroke(Color.Blue)
22. .strokeWidth(3)
23. }.width('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/Olug72yJSB27AqZjlpOW9Q/zh-cn_image_0000002583440055.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=3B05BF135A498A931687000810383756C7B21763D833538276FF120B78DCBC54)

### 示例3（使用attributeModifier动态设置Polyline组件的属性）

以下示例展示了如何使用attributeModifier动态设置Polyline组件的points、fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeLineJoin、strokeMiterLimit、strokeOpacity、strokeWidth和antiAlias属性。

```
1. // xxx.ets
2. class MyPolylineModifier implements AttributeModifier<PolylineAttribute> {
3. applyNormalAttribute(instance: PolylineAttribute): void {
4. // 折线起点(0, 0)，经过(50, 100)，到达终点(100, 0)，填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框间隙[20]，向左偏移15，线条两端样式为半圆，拐角样式使用尖角连接路径段，斜接长度与边框宽度比值的极限值为5，边框透明度0.5，边框宽度10，抗锯齿开启
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
22. struct PolylineModifierDemo {
23. @State modifier: MyPolylineModifier = new MyPolylineModifier()

25. build() {
26. Column() {
27. Polyline()
28. .width(100)
29. .height(100)
30. .attributeModifier(this.modifier)
31. .offset({ x: 20, y: 20 })
32. }
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/JmQCzy0yTPet0k7K3XZV4w/zh-cn_image_0000002552960010.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=7C5446D3B3C75B0B9D2496BBAA2A4EF61B4DC4EE9E32AD39B5FE72F86A54AE10)
