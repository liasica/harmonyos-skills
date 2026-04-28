---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-rect
title: Rect
category: harmonyos-references
scraped_at: 2026-04-28T08:02:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:09bdd80baa2f04070fa53185c984dd3eb1d2e663b2409662dc07c445396d6b46
---

矩形绘制组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Rect(options?: RectOptions | RoundedRectOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RectOptions](ts-drawing-components-rect.md#rectoptions18对象说明) | [RoundedRectOptions](ts-drawing-components-rect.md#roundedrectoptions18对象说明) | 否 | Rect绘制属性。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## RectOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Rect组件绘制属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度，取值范围≥0。  默认值：0  默认单位：vp  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度，取值范围≥0。  默认值：0  默认单位：vp  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radius7+ | [Length](ts-types.md#length) | Array<any> | 否 | 是 | 圆角半径，支持分别设置四个角的圆角度数，取值范围≥0。  该属性和radiusWidth/radiusHeight属性效果类似，在组合使用时优先于radiusWidth/radiusHeight生效。  默认值：0  默认单位：vp  异常值undefined、null、NaN和Infinity按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## RoundedRectOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Rect绘制属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度，取值范围≥0。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度，取值范围≥0。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radiusWidth7+ | [Length](ts-types.md#length) | 否 | 是 | 圆角宽度，取值范围≥0。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| radiusHeight7+ | [Length](ts-types.md#length) | 否 | 是 | 圆角高度，取值范围≥0。  默认值：0  默认单位：vp  异常值按照默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### radiusWidth

PhonePC/2in1TabletTVWearable

radiusWidth(value: Length)

设置圆角的宽度，仅设置宽时宽高一致，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。 异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 圆角的宽度，取值范围≥0。  默认值：0  默认单位：vp  异常值undefined按照默认值处理。 |

### radiusHeight

PhonePC/2in1TabletTVWearable

radiusHeight(value: Length)

设置圆角的高度，仅设置高时宽高一致，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。 异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | 是 | 圆角的高度，取值范围≥0。  默认值：0  默认单位：vp  异常值undefined按照默认值处理。 |

### radius

PhonePC/2in1TabletTVWearable

radius(value: Length | Array<any>)

设置圆角半径大小，取值范围≥0，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Length](ts-types.md#length) | Array<any> | 是 | 圆角半径大小。  默认值：0  默认单位：vp  异常值undefined和null按照[[0, 0], [0, 0], [0, 0], [0, 0]]处理。 |

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

设置边框间隙，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。取值范围≥0。异常值将按默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 定义Rect轮廓的虚线模式的数组，数组元素交替表示线段长度和间隙长度。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。  **说明：**  空数组：实线  偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->...  奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

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
| value | number | string | [Resource](ts-types.md#resource) | 是 | 边框透明度。  默认值：[stroke](ts-drawing-components-rect.md#stroke)接口设置的透明度。  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

### strokeWidth

PhonePC/2in1TabletTVWearable

strokeWidth(value: Length)

设置边框宽度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。该属性若为string类型，暂不支持百分比，百分比按照1px处理。

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

使用fill、fillOpacity、stroke、radius属性分别绘制矩形的填充颜色、透明度、边框颜色、圆角。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RectExample {
5. build() {
6. Column({ space: 10 }) {
7. Text('normal').fontSize(11).fontColor(0xCCCCCC).width('90%')
8. // 绘制90% * 50的矩形
9. Column({ space: 5 }) {
10. Text('normal').fontSize(9).fontColor(0xCCCCCC).width('90%')
11. // 绘制90% * 50矩形
12. Rect({ width: '90%', height: 50 })
13. .fill(Color.Pink)
14. // 绘制90% * 50的矩形框
15. Rect()
16. .width('90%')
17. .height(50)
18. .fillOpacity(0)
19. .stroke(Color.Red)
20. .strokeWidth(3)

22. Text('with rounded corners').fontSize(11).fontColor(0xCCCCCC).width('90%')
23. // 绘制90% * 80的矩形, 圆角宽高分别为40、20
24. Rect({ width: '90%', height: 80 })
25. .radiusHeight(20)
26. .radiusWidth(40)
27. .fill(Color.Pink)
28. // 绘制90% * 80的矩形, 圆角宽高为20
29. Rect({ width: '90%', height: 80 })
30. .radius(20)
31. .fill(Color.Pink)
32. .stroke(Color.Transparent)
33. }.width('100%').margin({ top: 10 })

35. // 绘制90% * 50矩形, 左上圆角宽高40,右上圆角宽高20,右下圆角宽高40,左下圆角宽高20
36. Rect({ width: '90%', height: 80 })
37. .radius([[40, 40], [20, 20], [40, 40], [20, 20]])
38. .fill(Color.Pink)
39. }.width('100%').margin({ top: 5 })
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/ZGemQuc4QpCqy7Scg2ClqQ/zh-cn_image_0000002583440059.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=F4F223F1D6DE2B79E0A6F787CBE75F7D69D4CB4FA0D47B103FF51D75A6CE4D38)

### 示例2（绘制渐变色矩形）

通过通用属性[linearGradient](ts-universal-attributes-gradient-color.md#lineargradient18)、[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape18)分别绘制渐变色的矩形。

从API version 18开始，新增linearGradient、clipShape通用属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RectExample {
5. build() {
6. Column({ space: 10 }) {
7. Column()
8. .width(100)
9. .height(100)
10. .linearGradient({
11. direction: GradientDirection.Right,
12. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
13. })
14. .clipShape(new Rect({ width: 100, height: 100, radius: 40 }))
15. Rect()
16. .width(100)
17. .height(100)
18. // 设置矩形填充，如果需要显示背景的渐变色，请设置区域透明度.fillOpacity(0.0)
19. .fill(Color.Pink)
20. // 设置倒角为40
21. .radius(40)
22. .stroke(Color.Black)
23. // 设置渐变色，仅100*100的矩形区域生效，渐变色的边界不包含倒角
24. .linearGradient({
25. direction: GradientDirection.Right,
26. colors: [[0xff0000, 0.0], [0x0000ff, 0.3], [0xffff00, 1.0]]
27. })
28. }
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/BtCXHYJiRNKGWBSDlLbBhQ/zh-cn_image_0000002552960014.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=E45E4FE27ED84205BD75FBD778ECF8B40992006F0A6466966199E4529D9881D8)

### 示例3（使用不同参数类型绘制矩形）

width、height、radius、radiusWidth、radiusHeight等属性分别使用不同的长度类型绘制图形。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct RectExample {
5. build() {
6. Column({ space: 10 }) {
7. // 绘制90% * 50矩形，圆角半径为5
8. Rect({ width: '90%', height: '50', radius: '5' }) // 使用string类型
9. .fill(Color.Green)
10. // 绘制200 * 50的矩形框，圆角半径为5
11. Rect({ width: 200, height: 50, radius: 5 }) // 使用number类型
12. .fillOpacity(0)
13. .stroke(Color.Red)
14. .strokeWidth(3)
15. // 绘制200 * 50矩形, 圆角宽80, 圆角高20
16. Rect({
17. width: $r('app.string.RectWidth'), // 使用Resource类型，需用户自定义
18. height: $r('app.string.RectHeight'),
19. radius: $r('app.string.RectRadius')
20. })
21. .radiusWidth($r('app.string.RectRadiusWidth'))
22. .radiusHeight($r('app.string.RectRadiusHeight'))
23. .fill(Color.Green)
24. }.width('100%').margin({ top: 5 })
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/rZO6GNKlT-qVboT3yO8DRw/zh-cn_image_0000002583480015.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=C9CCCDF5819F9E525E6BF52BF56D635D256DE174D7EC1F285AB696D58BF9F94A)

### 示例4（使用attributeModifier动态设置Rect组件的属性）

以下示例展示了如何使用attributeModifier动态设置Rect组件的fill、fillOpacity、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeLineJoin、strokeMiterLimit、strokeOpacity、strokeWidth和antiAlias属性。

```
1. // xxx.ets
2. class MyRectModifier implements AttributeModifier<RectAttribute> {
3. applyNormalAttribute(instance: RectAttribute): void {
4. // 填充颜色#707070，填充透明度0.5，边框颜色#2787D9，边框间隙[20]，向左偏移15，线条两端样式为半圆，拐角样式使用尖角连接路径段，斜接长度与边框宽度比值的极限值为5，边框透明度0.5，边框宽度10，抗锯齿开启
5. instance.fill("#707070")
6. instance.fillOpacity(0.5)
7. instance.stroke("#2787D9")
8. instance.strokeDashArray([20])
9. instance.strokeDashOffset("15")
10. instance.strokeLineCap(LineCapStyle.Round)
11. instance.strokeLineJoin(LineJoinStyle.Miter)
12. instance.strokeMiterLimit(5)
13. instance.strokeOpacity(0.5)
14. instance.strokeWidth(10)
15. instance.antiAlias(true)
16. }
17. }

19. @Entry
20. @Component
21. struct RectModifierDemo {
22. @State modifier: MyRectModifier = new MyRectModifier()

24. build() {
25. Column() {
26. Rect()
27. .width(200)
28. .height(200)
29. .attributeModifier(this.modifier)
30. .offset({ x: 20, y: 20 })
31. }
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/YgkkObkKSIqs_CLsmYvaGA/zh-cn_image_0000002552800366.png?HW-CC-KV=V1&HW-CC-Date=20260428T000211Z&HW-CC-Expire=86400&HW-CC-Sign=A8DD10BD01F6B095856A6DEC46C8DE716E9A85BABA03215F558A6E9F9E8496E1)
