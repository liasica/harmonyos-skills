---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-drawing-components-line
title: Line
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图形绘制 > Line
category: harmonyos-references
scraped_at: 2026-04-28T08:02:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c8191fede5b9a4d1a84dc2a504a94cab91502f5c2d0d8a3058b007c958c4bea9
---

直线绘制组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

该组件从API version 20开始支持使用[AttributeUpdater](js-apis-arkui-attributeupdater.md)类的[updateConstructorParams](js-apis-arkui-attributeupdater.md#属性)接口更新构造参数。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

Line(options?: LineOptions)

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [LineOptions](ts-drawing-components-line.md#lineoptions18对象说明) | 否 | Line绘制区域。  异常值undefined和null按照无效值处理，本次设置不生效。 |

## LineOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述Line组件绘制属性。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | [Length](ts-types.md#length) | 否 | 是 | 宽度。  值为异常值或缺省时按照自身内容需要的宽度处理。  默认单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | [Length](ts-types.md#length) | 否 | 是 | 高度。  值为异常值或缺省时按照自身内容需要的高度处理。  默认单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### startPoint

PhonePC/2in1TabletTVWearable

startPoint(value: Array<any>)

设置直线起点坐标点（相对坐标），支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 直线起点坐标点（相对坐标），单位vp。  默认值：[0, 0]  异常值undefined和null按照默认值处理。 |

### endPoint

PhonePC/2in1TabletTVWearable

endPoint(value: Array<any>)

设置直线终点坐标点（相对坐标），支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 直线终点坐标点（相对坐标），单位vp。  默认值：[0, 0]  异常值undefined和null按照默认值处理。 |

### fill

PhonePC/2in1TabletTVWearable

fill(value: ResourceColor)

设置填充区域颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。Line组件无法形成闭合区域，该属性设置无效。

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

设置填充区域透明度，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。Line组件无法形成闭合区域，该属性设置无效。

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

设置边框颜色，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法，不设置时，默认边框透明度为0，即没有边框。

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

设置边框间隙，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。线段相交时可能会出现重叠现象。取值范围≥0，异常值按照默认值处理。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | Array<any> | 是 | 定义Line的虚线模式的数组，数组元素交替表示线段长度和间隙长度。  默认值：[]（空数组）  默认单位：vp  异常值undefined和null按照默认值处理。  **说明：**  空数组：实线  偶数多元素数组：数组元素按顺序循环，如[a, b, c, d]表示线段长度a->间隙长度b->线段长度c->间隙长度d->线段长度a->...  奇数多元素数组：重复一次该数组元素，按偶数多元素数组的规则顺序循环，如[a, b, c]等效于[a, b, c, a, b, c]，表示线段长度a->间隙长度b->线段长度c->间隙长度a->线段长度b->间隙长度c->线段长度a->... |

### strokeDashOffset

PhonePC/2in1TabletTVWearable

strokeDashOffset(value: number | string)

设置边框绘制起点的偏移量，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

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

设置边框拐角绘制样式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。Line组件不支持拐角，该属性设置无效。

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

设置锐角绘制成斜角的极限值，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。Line组件不支持设置锐角图形，该属性设置无效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 锐角绘制成斜角的极限值。  默认值：4  异常值undefined、null和NaN按照默认值处理，Infinity会导致stroke失效。 |

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
| value | number | string | [Resource](ts-types.md#resource) | 是 | 边框透明度。  默认值：[stroke](ts-drawing-components-line.md#stroke)接口设置的透明度。  异常值NaN按0.0处理，undefined、null和Infinity按1.0处理。 |

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

通过startPoint、endPoint、fillOpacity、stroke、strokeDashArray、strokeDashOffset属性分别绘制直线的起始点、结束点、透明度、直线颜色、边框间隙、绘制起点。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineExample {
5. build() {
6. Column({ space: 10 }) {
7. // 线条绘制的起止点坐标均是相对于Line组件本身绘制区域的坐标
8. Line()
9. .width(200)
10. .height(150)
11. .startPoint([0, 0])
12. .endPoint([50, 100])
13. .stroke(Color.Black)
14. .backgroundColor('#F5F5F5')
15. Line()
16. .width(200)
17. .height(150)
18. .startPoint([50, 50])
19. .endPoint([150, 150])
20. .strokeWidth(5)
21. .stroke(Color.Orange)
22. .strokeOpacity(0.5)
23. .backgroundColor('#F5F5F5')
24. // strokeDashOffset用于定义关联虚线strokeDashArray数组渲染时的偏移
25. Line()
26. .width(200)
27. .height(150)
28. .startPoint([0, 0])
29. .endPoint([100, 100])
30. .stroke(Color.Black)
31. .strokeWidth(3)
32. .strokeDashArray([10, 3])
33. .strokeDashOffset(5)
34. .backgroundColor('#F5F5F5')
35. // 当坐标点设置的值超出Line组件的宽高范围时，线条会画出组件绘制区域
36. Line()
37. .width(50)
38. .height(50)
39. .startPoint([0, 0])
40. .endPoint([100, 100])
41. .stroke(Color.Black)
42. .strokeWidth(3)
43. .strokeDashArray([10, 3])
44. .backgroundColor('#F5F5F5')
45. }
46. }
47. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/QhqNykRiSuGRn7SuADJq6w/zh-cn_image_0000002583480007.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=3B919839CA7A2913233F722DDCA058ACADBB442EC09E108A75BE20C504BCA85F)

### 示例2（边框端点绘制）

通过strokeLineCap属性绘制直线的边框端点样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineExample1 {
5. build() {
6. Row({ space: 10 }) {
7. // 当LineCapStyle值为Butt时
8. Line()
9. .width(100)
10. .height(200)
11. .startPoint([50, 50])
12. .endPoint([50, 200])
13. .stroke(Color.Black)
14. .strokeWidth(20)
15. .strokeLineCap(LineCapStyle.Butt)
16. .backgroundColor('#F5F5F5')
17. .margin(10)
18. // 当LineCapStyle值为Round时
19. Line()
20. .width(100)
21. .height(200)
22. .startPoint([50, 50])
23. .endPoint([50, 200])
24. .stroke(Color.Black)
25. .strokeWidth(20)
26. .strokeLineCap(LineCapStyle.Round)
27. .backgroundColor('#F5F5F5')
28. // 当LineCapStyle值为Square时
29. Line()
30. .width(100)
31. .height(200)
32. .startPoint([50, 50])
33. .endPoint([50, 200])
34. .stroke(Color.Black)
35. .strokeWidth(20)
36. .strokeLineCap(LineCapStyle.Square)
37. .backgroundColor('#F5F5F5')
38. }
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/tCLaheNyS0aAKNeaS9B50A/zh-cn_image_0000002552800358.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=D790F2D4C16C519DF12A61DE8931381C355D738650E3CD37361E8A2DB692331B)

### 示例3（边框间隙绘制）

通过strokeDashArray属性绘制直线的边框间隙。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineExample {
5. build() {
6. Column() {
7. Line()
8. .width(300)
9. .height(30)
10. .startPoint([50, 30])
11. .endPoint([300, 30])
12. .stroke(Color.Black)
13. .strokeWidth(10)
14. // 设置strokeDashArray的数组间隔为 50
15. Line()
16. .width(300)
17. .height(30)
18. .startPoint([50, 20])
19. .endPoint([300, 20])
20. .stroke(Color.Black)
21. .strokeWidth(10)
22. .strokeDashArray([50])
23. // 设置strokeDashArray的数组间隔为 50, 10
24. Line()
25. .width(300)
26. .height(30)
27. .startPoint([50, 20])
28. .endPoint([300, 20])
29. .stroke(Color.Black)
30. .strokeWidth(10)
31. .strokeDashArray([50, 10])
32. // 设置strokeDashArray的数组间隔为 50, 10, 20
33. Line()
34. .width(300)
35. .height(30)
36. .startPoint([50, 20])
37. .endPoint([300, 20])
38. .stroke(Color.Black)
39. .strokeWidth(10)
40. .strokeDashArray([50, 10, 20])
41. // 设置strokeDashArray的数组间隔为 50, 10, 20, 30
42. Line()
43. .width(300)
44. .height(30)
45. .startPoint([50, 20])
46. .endPoint([300, 20])
47. .stroke(Color.Black)
48. .strokeWidth(10)
49. .strokeDashArray([50, 10, 20, 30])
50. }
51. }
52. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/7nlTQ0yCQ9upMFhR53sqmw/zh-cn_image_0000002583440053.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=0CA04EC5B8467AC34C5DC3A1B4AFA91B3516E2B94CD83D8252EE0C8884B1A57D)

### 示例4（宽和高使用不同参数类型绘制直线）

width、height属性分别使用不同的长度类型绘制直线。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineTypeExample {
5. build() {
6. Column({ space: 10 }) {
7. // 在200 * 200的区域内绘制一个起始点为（0,0），终点为（150,150），边框宽度为10的直线
8. Line({ width: '200', height: '200' })// 使用string类型
9. .startPoint([0, 0])
10. .endPoint([150, 150])
11. .stroke(Color.Black)
12. .strokeWidth(10)
13. .backgroundColor('#F5F5F5')
14. .margin(10)
15. // 在200 * 200的区域内绘制一个起始点为（0,50），终点为（150,150），边框宽度为10的直线
16. Line({ width: 200, height: 200 })// 使用number类型
17. .startPoint([0, 50])
18. .endPoint([150, 150])
19. .stroke(Color.Black)
20. .strokeWidth(10)
21. .backgroundColor('#F5F5F5')
22. .margin(10)
23. // 在200 * 200的区域内绘制一个起始点为（0,100），终点为（150,150），边框宽度为10的直线
24. Line({ width: $r('app.string.LineWidth'), height: $r('app.string.LineHeight') })// 使用Resource类型，需用户自定义
25. .startPoint([0, 100])
26. .endPoint([150, 150])
27. .stroke(Color.Black)
28. .strokeWidth(10)
29. .backgroundColor('#F5F5F5')
30. .margin(10)
31. }.width('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/dhoInNQ-Q3abZwJvyprzOg/zh-cn_image_0000002552960008.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=9D7C55A91E6FDDB9B352151E62C940308075DA4F10FFDE5C81853A0C96A3620B)

### 示例5（使用attributeModifier动态设置Line组件的属性）

以下示例展示了如何使用attributeModifier动态设置Line组件的startPoint、endPoint、stroke、strokeDashArray、strokeDashOffset、strokeLineCap、strokeOpacity、strokeWidth和antiAlias属性。

```
1. // xxx.ets
2. class MyLineModifier implements AttributeModifier<LineAttribute> {
3. applyNormalAttribute(instance: LineAttribute): void {
4. // 一个起始点为（10, 10），终点为（120, 10）的直线，边框颜色#2787D9，边框间隙[20]，向左偏移15，线条两端样式为半圆，边框透明度0.5，边框宽度10，抗锯齿开启
5. instance.startPoint([10, 10])
6. instance.endPoint([120, 10])
7. instance.stroke("#2787D9")
8. instance.strokeDashArray([20])
9. instance.strokeDashOffset("15")
10. instance.strokeLineCap(LineCapStyle.Round)
11. instance.strokeOpacity(0.5)
12. instance.strokeWidth(10)
13. instance.antiAlias(true)
14. }
15. }

17. @Entry
18. @Component
19. struct LineModifierDemo {
20. @State modifier: MyLineModifier = new MyLineModifier()

22. build() {
23. Column() {
24. Line()
25. .attributeModifier(this.modifier)
26. .offset({ x: 20, y: 20 })
27. }
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/LP-Djz6fSEuLJaO21Q-qUA/zh-cn_image_0000002583480009.png?HW-CC-KV=V1&HW-CC-Date=20260428T000209Z&HW-CC-Expire=86400&HW-CC-Sign=A6CBDBCA005C636392499976A16BA844B62CECA1648F86C9456ECE7E02D0BBD3)
