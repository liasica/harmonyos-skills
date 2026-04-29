---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-canvasrenderingcontext2d
title: CanvasRenderingContext2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > CanvasRenderingContext2D
category: harmonyos-references
scraped_at: 2026-04-29T13:52:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:203e1bc97842e00a7956ce126ca0ec562ceb71a1d4d8b1cbb4abb5f23315c6ee
---

CanvasRenderingContext2D对象与Canvas组件绑定后，可在Canvas组件上绘制，绘制对象可以是形状、文本、图片等。

说明

* 从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 建议使用时将CanvasRenderingContext2D对象与Canvas组件封装到同一个自定义组件中，保证两者一一对应且生命周期保持一致。
* 本文绘制接口在调用时会存入被关联的Canvas组件的指令队列中。仅当当前帧进入渲染阶段且关联的Canvas组件处于可见状态时，这些指令才会从队列中被提取并执行。因此，在Canvas组件不可见的情况下，应尽量避免频繁调用绘制接口，以防止指令在队列中堆积，从而避免内存占用过大的问题，具体示例请参考[控制在画布组件不可见时不进行绘制](../harmonyos-guides/arkts-drawing-customization-on-canvas.md#控制在画布组件不可见时不进行绘制)。
* [beginPath](ts-canvasrenderingcontext2d.md#beginpath)、[moveTo](ts-canvasrenderingcontext2d.md#moveto)、[lineTo](ts-canvasrenderingcontext2d.md#lineto)、[closePath](ts-canvasrenderingcontext2d.md#closepath)、[bezierCurveTo](ts-canvasrenderingcontext2d.md#beziercurveto)、[quadraticCurveTo](ts-canvasrenderingcontext2d.md#quadraticcurveto)、[arc](ts-canvasrenderingcontext2d.md#arc)、[arcTo](ts-canvasrenderingcontext2d.md#arcto)、[ellipse](ts-canvasrenderingcontext2d.md#ellipse)、[rect](ts-canvasrenderingcontext2d.md#rect)和[roundRect](ts-canvasrenderingcontext2d.md#roundrect20)接口只能对CanvasRenderingContext2D中的路径生效，无法对[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)和[Path2D](ts-components-canvas-path2d.md)对象中设置的路径生效。
* Canvas组件的宽或高超过8000px时使用CPU渲染，会导致性能明显下降。

## 构造函数

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(settings?: RenderingContextSettings)

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settings | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置CanvasRenderingContext2D对象的参数，见[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)。  异常值undefined和null按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造Canvas画布对象，支持配置CanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| settings | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置CanvasRenderingContext2D对象的参数，见[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)。  异常值undefined和null按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 否 | 用来配置CanvasRenderingContext2D对象的单位模式，配置后无法更改。  异常值undefined、NaN和Infinity按默认值处理。  默认值：DEFAULT |

**示例：**

以下示例展示了配置CanvasRenderingContext2D对象的单位模式，默认单位模式为LengthMetricsUnit.DEFAULT，对应默认单位vp，配置后无法动态更改。详细说明见[LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12)。

```
1. // xxx.ets
2. import { LengthMetricsUnit } from '@kit.ArkUI'

4. @Entry
5. @Component
6. struct LengthMetricsUnitDemo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private contextPX: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings, LengthMetricsUnit.PX);
9. private contextVP: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.contextPX)
14. .width('100%')
15. .height(150)
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. this.contextPX.fillRect(10, 10, 100, 100)
19. this.contextPX.clearRect(10, 10, 50, 50)
20. })

22. Canvas(this.contextVP)
23. .width('100%')
24. .height(150)
25. .backgroundColor('#ffff00')
26. .onReady(() => {
27. this.contextVP.fillRect(10, 10, 100, 100)
28. this.contextVP.clearRect(10, 10, 50, 50)
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/BXSqG9M1R92JqsTsTdCOTg/zh-cn_image_0000002589326321.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=88CA1EBD8F6AB5CCD4B476F1A448A546354603D47671EB6A79D46778D975675D)

## 属性

PhonePC/2in1TabletTVWearable

说明

fillStyle、shadowColor与 strokeStyle 中string类型格式为rgb(255, 255, 255)、rgba(255, 255, 255, 1.0)或者#FFFFFF。

### fillStyle

PhonePC/2in1TabletTVWearable

指定绘制的填充色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | number10+ | [CanvasGradient](ts-components-canvas-canvasgradient.md) | [CanvasPattern](ts-components-canvas-canvaspattern.md) | 否 | 否 | - 类型为string时，表示设置填充区域的颜色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中string类型说明。  - 类型为number时，表示设置填充区域的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中number类型说明。  - 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](ts-canvasrenderingcontext2d.md#createlineargradient)方法创建。  - 类型为CanvasPattern时，使用[createPattern](ts-canvasrenderingcontext2d.md#createpattern)方法创建。  默认值：'#000000'（黑色）  异常值设置无效，保持设置前效果。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillStyle = '#0000ff'
16. this.context.fillRect(20, 20, 150, 100)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/wabZ323FRxOGA8yaoaCjSg/zh-cn_image_0000002589246263.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=EE90311D63C83B2837AD6D2006A358A346C902D700D2F9329ADF7EC865FF99F6)

### lineWidth

PhonePC/2in1TabletTVWearable

设置绘制线条的宽度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：1（px）  默认单位：vp  lineWidth取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致lineWidth属性异常，不进行绘制。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineWidthExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.lineWidth = 5
16. this.context.strokeRect(25, 25, 85, 105)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/sca05wxlSDu6o6zFj2dc6A/zh-cn_image_0000002558766456.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=0F0C5816856945F6684370029C6F55DBAD559DF1C35EC3BD4F2D0B36BBC48E3F)

### strokeStyle

PhonePC/2in1TabletTVWearable

设置线条的颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | number10+ | [CanvasGradient](ts-components-canvas-canvasgradient.md) | [CanvasPattern](ts-components-canvas-canvaspattern.md) | 否 | 否 | - 类型为string时，表示设置线条使用的颜色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中string类型说明。  - 类型为number时，表示设置线条使用的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中number类型说明。  - 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](ts-canvasrenderingcontext2d.md#createlineargradient)方法创建。  - 类型为CanvasPattern时，使用[createPattern](ts-canvasrenderingcontext2d.md#createpattern)方法创建。  默认值：'#000000'（黑色）  异常值设置无效，保持设置前效果。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.lineWidth = 10
16. this.context.strokeStyle = '#0000ff'
17. this.context.strokeRect(25, 25, 155, 105)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/zv1RcGUITouIrKNKhTwA5Q/zh-cn_image_0000002558606796.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=D4A7A05F4A4AD45554DA7578764419497D19E27BAFF27917888BAD8432A4BBE8)

### lineCap

PhonePC/2in1TabletTVWearable

指定线端点的样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasLineCap](ts-canvasrenderingcontext2d.md#canvaslinecap类型说明) | 否 | 否 | 默认值：'butt' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineCapExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.lineWidth = 8
16. this.context.beginPath()
17. this.context.lineCap = 'round'
18. this.context.moveTo(30, 50)
19. this.context.lineTo(220, 50)
20. this.context.stroke()
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/mqbW2XtuRBqbwNEjmcluag/zh-cn_image_0000002589326323.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=33F7D801B2C194259D7FDCD1FEE72FBCACDD0E4CC4EFBFE6CA2F48861FE7AE8B)

### lineJoin

PhonePC/2in1TabletTVWearable

指定线段间相交的交点样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasLineJoin](ts-canvasrenderingcontext2d.md#canvaslinejoin类型说明) | 否 | 否 | 可选值为：  - 'round'：在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。  - 'bevel'：在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。  - 'miter'：在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。  默认值：'miter' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineJoinExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.beginPath()
16. this.context.lineWidth = 8
17. this.context.lineJoin = 'miter'
18. this.context.moveTo(30, 30)
19. this.context.lineTo(120, 60)
20. this.context.lineTo(30, 110)
21. this.context.stroke()
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/zgplI2PATR2iX0DdbkZhTQ/zh-cn_image_0000002589246265.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=627407079893F8A5EF6052C845E8D60F70AC794E34E5DA5A3F63AE9E632A20EC)

### miterLimit

PhonePC/2in1TabletTVWearable

设置斜接面限制值，该值指定了线条相交处内角和外角的距离，仅当设置了lineJoin为miter才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：10px  单位：px  miterLimit取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致miterLimit属性异常。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MiterLimit {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.lineWidth = 8
16. this.context.lineJoin = 'miter'
17. this.context.miterLimit = 3
18. this.context.moveTo(30, 30)
19. this.context.lineTo(60, 35)
20. this.context.lineTo(30, 37)
21. this.context.stroke()
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/3eEEi3IqSTSHQtRFYufsIA/zh-cn_image_0000002558766458.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=C31B7C97A39B650550C84BBE59B057396677BEF6DA2E48B94AF1E3BE71C9F149)

### font

PhonePC/2in1TabletTVWearable

设置文本绘制中的字体样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

语法：ctx.font = 'font-style font-weight font-size font-family'

- font-style(可选)，用于指定字体样式，支持如下几种样式：'normal','italic'。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：'normal', 'bold', 'bolder', 'lighter', 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位支持px、vp。使用时需要添加单位。

- font-family(可选)，指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。

从API version 20开始，支持通过该接口设置注册过的自定义字体（DevEco Studio的预览器不支持显示自定义字体）。自定义字体注册有以下两种方式。一种是通过ArkUI的异步接口this.uiContext.getFont().[registerFont](arkts-apis-uicontext-font.md#registerfont)注册，调用后立即绘制可能会导致自定义字体不生效。另一种是直接调用字体引擎的fontCollection.[loadFontSync](js-apis-graphics-text.md#loadfontsync)接口来注册自定义字体到字体引擎。在直接调用字体引擎接口注册自定义字体时，fontCollection的实例需要是text.FontCollection.getGlobalInstance()，因为组件默认会从该实例加载字体。如果使用其他实例，可能会导致自定义字体不生效。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 默认值：'normal normal 14px sans-serif'  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

```
1. // xxx.ets
2. import { text } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct FontDemo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('rgb(213,213,213)')
16. .onReady(() => {
17. // 常规字体样式，常规粗细，字体大小为30px，字体系列为sans-serif
18. this.context.font = 'normal normal 30px sans-serif'
19. this.context.fillText("Hello px", 20, 60)
20. // 斜体样式，加粗，字体大小为30vp，字体系列为monospace
21. this.context.font = 'italic bold 30vp monospace'
22. this.context.fillText("Hello vp", 20, 100)
23. // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Thin_Italic.ttf
24. let fontCollection = text.FontCollection.getGlobalInstance();
25. fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
26. // 加粗，字体大小为30vp，字体系列为HarmonyOS_Sans_Thin_Italic
27. this.context.font = "bold 30vp HarmonyOS_Sans_Thin_Italic"
28. this.context.fillText("Hello customFont", 20, 140)
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/gzTwIpkISM-YE60ouv47Hw/zh-cn_image_0000002558606798.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=0F6894CA4CB9035139634FF1766D2B45A5AF6E2FBCFFC0073DB457115C0A80C8)

### textAlign

PhonePC/2in1TabletTVWearable

设置文本绘制中的文本对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasTextAlign](ts-canvasrenderingcontext2d.md#canvastextalign类型说明) | 否 | 否 | ltr布局模式下'start'和'left'一致，rtl布局模式下'start'和'right'一致。  默认值：'left' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.strokeStyle = 'rgb(39,135,217)'
16. this.context.moveTo(140, 10)
17. this.context.lineTo(140, 160)
18. this.context.stroke()
19. this.context.font = '50px sans-serif'
20. this.context.textAlign = 'start'
21. this.context.fillText('textAlign=start', 140, 60)
22. this.context.textAlign = 'end'
23. this.context.fillText('textAlign=end', 140, 80)
24. this.context.textAlign = 'left'
25. this.context.fillText('textAlign=left', 140, 100)
26. this.context.textAlign = 'center'
27. this.context.fillText('textAlign=center', 140, 120)
28. this.context.textAlign = 'right'
29. this.context.fillText('textAlign=right', 140, 140)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/YouoWXf4SrCGeLArC9bqhA/zh-cn_image_0000002589326325.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=ABE736222FB66A8EA4B61602F2CB2431DF61256E7FFB7B7B2C2B15872AC7206D)

### textBaseline

PhonePC/2in1TabletTVWearable

设置文本绘制中的水平对齐方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasTextBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明) | 否 | 否 | 默认值：'alphabetic' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TextBaseline {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.strokeStyle = 'rgb(0,0,255)'
16. this.context.moveTo(0, 120)
17. this.context.lineTo(400, 120)
18. this.context.stroke()
19. this.context.font = '20px sans-serif'
20. this.context.textBaseline = 'top'
21. this.context.fillText('Top', 10, 120)
22. this.context.textBaseline = 'bottom'
23. this.context.fillText('Bottom', 55, 120)
24. this.context.textBaseline = 'middle'
25. this.context.fillText('Middle', 125, 120)
26. this.context.textBaseline = 'alphabetic'
27. this.context.fillText('Alphabetic', 195, 120)
28. this.context.textBaseline = 'hanging'
29. this.context.fillText('Hanging', 295, 120)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/lGjbZtceSJuGmIrd1o5yPQ/zh-cn_image_0000002589246267.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=18A4F7915C1D223FECACEA1ADEB3EDAD21FA657147C92CF017A3FD966FDE594C)

### globalAlpha

PhonePC/2in1TabletTVWearable

设置透明度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0.  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制。API version 18及以后，设置NaN或Infinity时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认值：1.0 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GlobalAlpha {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillStyle = 'rgb(0,0,255)'
16. this.context.fillRect(0, 0, 50, 50)
17. this.context.globalAlpha = 0.4
18. this.context.fillStyle = 'rgb(0,0,255)'
19. this.context.fillRect(50, 50, 50, 50)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/XTzE7cKwRnekuNpbXh7qdw/zh-cn_image_0000002558766460.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=134E1269758CEDBD53AC37F2FFAE8F7B36223BE16C3B32197B818D0E89CAE6A9)

### lineDashOffset

PhonePC/2in1TabletTVWearable

设置画布的虚线偏移量，精度为float，仅当设置setLineDash时属性才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | API version 18之前，设置NaN或Infinity时，设置了虚线样式的线条绘制出来是实线。API version 18及以后，设置NaN或Infinity时当前接口不生效，设置了虚线样式的线条绘制出来是虚线。  默认值：0.0  默认单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. import { AnimatorResult } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct LineDashOffset {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private animator: AnimatorResult | undefined = undefined;

11. drawAntLine() { // 实现蚂蚁线动画
12. this.animator = this.getUIContext().createAnimator({
13. duration: 2000,
14. easing: 'linear',
15. delay: 0,
16. fill: 'none',
17. direction: 'normal',
18. iterations: -1,
19. begin: 0, // 动画插值起点
20. end: 1 // 动画插值终点
21. });
22. this.animator.onFrame = (value: number) => {
23. this.context.reset();
24. this.context.lineWidth = 2;
25. this.context.setLineDash([10, 5]);
26. this.context.lineDashOffset = 105 * value;
27. this.context.strokeRect(10, 10, 100, 100);
28. };
29. this.animator.play();
30. }

32. aboutToDisappear() {
33. this.animator?.finish();
34. this.animator = undefined;
35. }

37. build() {
38. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
39. Canvas(this.context)
40. .width('100%')
41. .height('100%')
42. .backgroundColor('rgb(213,213,213)')
43. .onReady(() => {
44. this.drawAntLine();
45. })
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/vfV4gAgbR1u4OJfxOpNZfg/zh-cn_image_0000002558606800.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=03D2E8FF1689166D5038B50FE102DE811324DD3FE1EE81005C53BB774BAEAD3F)

### globalCompositeOperation

PhonePC/2in1TabletTVWearable

设置合成操作的方式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 类型字段可选值有'source-over'，'source-atop'，'source-in'，'source-out'，'destination-over'，'destination-atop'，'destination-in'，'destination-out'，'lighter'，'copy'，'xor'。  默认值：'source-over' |

| 名称 | 描述 |
| --- | --- |
| source-over | 在现有绘制内容上显示新绘制内容，属于默认值。 |
| source-atop | 在现有绘制内容顶部显示新绘制内容。 |
| source-in | 在现有绘制内容中显示新绘制内容。 |
| source-out | 在现有绘制内容之外显示新绘制内容。 |
| destination-over | 在新绘制内容上方显示现有绘制内容。 |
| destination-atop | 在新绘制内容顶部显示现有绘制内容。 |
| destination-in | 在新绘制内容中显示现有绘制内容。 |
| destination-out | 在新绘制内容外显示现有绘制内容。 |
| lighter | 显示新绘制内容和现有绘制内容。 |
| copy | 显示新绘制内容而忽略现有绘制内容。 |
| xor | 使用异或操作对新绘制内容与现有绘制内容进行融合。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GlobalCompositeOperation {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private context3: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private context4: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
10. private context5: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
11. private context6: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

13. build() {
14. Column() {
15. Row() {
16. // 1. source-over：新图形覆盖在原有图形上方（默认行为）
17. Canvas(this.context1)
18. .width('45%')
19. .borderWidth(1)
20. .margin(5)
21. .onReady(() => {
22. let ctx1 = this.context1;
23. ctx1.fillStyle = 'rgb(39,135,217)';
24. ctx1.fillRect(25, 25, 75, 75); // 原有图形
25. ctx1.globalCompositeOperation = 'source-over'; // 默认值，可省略
26. ctx1.fillStyle = 'rgb(23,169,141)';
27. ctx1.fillRect(75, 75, 75, 75); // 新图形覆盖
28. })
29. // 2. destination-out：新图形擦除原有图形（橡皮擦核心逻辑）
30. Canvas(this.context2)
31. .width('45%')
32. .borderWidth(1)
33. .margin(5)
34. .onReady(() => {
35. let ctx2 = this.context2;
36. // 先绘制背景
37. ctx2.fillStyle = 'rgb(39,135,217)';
38. ctx2.fillRect(0, 0, ctx2.width, ctx2.height);
39. // 设置合成模式为擦除
40. ctx2.globalCompositeOperation = 'destination-out';
41. // 绘制圆形作为橡皮擦
42. ctx2.beginPath();
43. ctx2.arc(ctx2.width / 2, ctx2.height / 2, 60, 0, Math.PI * 2);
44. ctx2.fill(); // 擦除圆形区域的背景
45. })
46. }
47. .height('30%')

49. Row() {
50. // 3. source-in：仅保留新图形与原有图形重叠的部分（裁剪或蒙版）
51. Canvas(this.context3)
52. .width('45%')
53. .borderWidth(1)
54. .margin(5)
55. .onReady(() => {
56. let ctx3 = this.context3;
57. // 先绘制原有图形（圆形蒙版）
58. ctx3.beginPath();
59. ctx3.arc(ctx3.width / 2, ctx3.height / 2, 80, 0, Math.PI * 2);
60. ctx3.fillStyle = '#fff';
61. ctx3.fill();
62. // 设置合成模式
63. ctx3.globalCompositeOperation = 'source-in';
64. // 绘制新图形（渐变矩形）
65. const gradient = ctx3.createLinearGradient(0, 0, ctx3.width, ctx3.height);
66. gradient.addColorStop(0, 'rgb(23,169,141)');
67. gradient.addColorStop(1, 'rgb(39,135,217)');
68. ctx3.fillStyle = gradient;
69. ctx3.fillRect(0, 0, 200, 200); // 仅圆形区域显示渐变
70. })
71. // 4. lighter：新图形与原有图形叠加（亮度相加，滤色效果）
72. Canvas(this.context4)
73. .width('45%')
74. .borderWidth(1)
75. .margin(5)
76. .onReady(() => {
77. let ctx4 = this.context4;
78. // 原有图形（半透明红色圆）
79. ctx4.beginPath();
80. ctx4.arc(70, 100, 50, 0, Math.PI * 2);
81. ctx4.fillStyle = 'rgba(234, 67, 53, 0.7)';
82. ctx4.fill();
83. // 设置合成模式
84. ctx4.globalCompositeOperation = 'lighter';
85. // 新图形（半透明蓝色圆）
86. ctx4.beginPath();
87. ctx4.arc(110, 100, 50, 0, Math.PI * 2);
88. ctx4.fillStyle = 'rgba(66, 133, 244, 0.7)';
89. ctx4.fill(); // 重叠区域变成紫色（亮度叠加）
90. })
91. }
92. .height('30%')

94. Row() {
95. // 5. destination-atop：保留原有图形与新图形重叠的部分，移除其他区域
96. Canvas(this.context5)
97. .width('45%')
98. .borderWidth(1)
99. .margin(5)
100. .onReady(() => {
101. let ctx5 = this.context5;
102. // 原有图形（绿色矩形）
103. ctx5.fillStyle = 'rgb(23,169,141)';
104. ctx5.fillRect(0, 0, ctx5.width, ctx5.height);
105. // 设置合成模式
106. ctx5.globalCompositeOperation = 'destination-atop';
107. // 新图形（小圆形）
108. ctx5.beginPath();
109. ctx5.arc(ctx5.width / 2, ctx5.height / 2, 60, 0, Math.PI * 2);
110. ctx5.fillStyle = '#000';
111. ctx5.fill(); // 仅矩形与圆形重叠的部分保留
112. })
113. // 6. 文字蒙版（“source-in”的高级用法）
114. Canvas(this.context6)
115. .width('45%')
116. .borderWidth(1)
117. .margin(5)
118. .onReady(() => {
119. let ctx6 = this.context6
120. // 先绘制文字（作为蒙版）
121. ctx6.font = 'bold 40vp';
122. ctx6.textAlign = 'center';
123. ctx6.textBaseline = 'middle';
124. ctx6.fillText('CANVAS', ctx6.width / 2, ctx6.height / 2);
125. // 设置合成模式
126. ctx6.globalCompositeOperation = 'source-in';
127. // 绘制渐变背景（仅文字区域显示）
128. let textGradient = ctx6.createLinearGradient(50, 0, 300, 100);
129. textGradient.addColorStop(0.0, 'rgb(39,135,217)');
130. textGradient.addColorStop(0.5, 'rgb(255,238,240)');
131. textGradient.addColorStop(1.0, 'rgb(23,169,141)');
132. ctx6.fillStyle = textGradient;
133. ctx6.fillRect(0, 0, 200, 200); // 渐变仅填充文字区域
134. })
135. }
136. .height('30%')
137. }
138. .width('100%')
139. .height('100%')
140. }
141. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/dzBXpj5GRSm59Xu9eYJjJA/zh-cn_image_0000002589326327.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=5ADA9C7D1C973D29E3C9CBE1C6B92AF31F5CDB64D7DF38E1288127C563120777)

### shadowBlur

PhonePC/2in1TabletTVWearable

设置绘制阴影时的模糊级别，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 值越大越模糊，精度为float，取值范围≥0。  默认值：0.0  单位：px  shadowBlur取值不支持负数，负数、NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowBlur {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.shadowBlur = 30
16. this.context.shadowColor = 'rgb(0,0,0)'
17. this.context.fillStyle = 'rgb(255,0,0)'
18. this.context.fillRect(20, 20, 100, 80)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/UblOVVBbRzOzyj-0cVWQOg/zh-cn_image_0000002589246269.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=4884FC70E1CE70FA3AD5FD7DDB2420A551BA5F895D53D4B46BD9D0E3417EF483)

### shadowColor

PhonePC/2in1TabletTVWearable

设置绘制阴影时的阴影颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中string类型说明。  默认值：透明黑色 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowColor {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.shadowBlur = 30
16. this.context.shadowColor = 'rgb(0,0,255)'
17. this.context.fillStyle = 'rgb(255,0,0)'
18. this.context.fillRect(30, 30, 100, 100)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/QU9u5z_GRfyDDAu0w7GzWg/zh-cn_image_0000002558766462.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=BAEB9445A7263F8FF1D70BAD5608C028794AEC04303B2F81DBCC3CB64554840C)

### shadowOffsetX

PhonePC/2in1TabletTVWearable

设置绘制阴影时和原有对象的水平偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0  默认单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowOffsetX {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.shadowBlur = 10
16. this.context.shadowOffsetX = 20
17. this.context.shadowColor = 'rgb(0,0,0)'
18. this.context.fillStyle = 'rgb(255,0,0)'
19. this.context.fillRect(20, 20, 100, 80)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/fL2mR_1xSnishWUVvPJK3Q/zh-cn_image_0000002558606802.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=61C4418E6EF7E5A100AB54ABE4236C77BCCFDD478A591A90207AE2B04F8A2916)

### shadowOffsetY

PhonePC/2in1TabletTVWearable

设置绘制阴影时和原有对象的垂直偏移值，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0  默认单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ShadowOffsetY {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.shadowBlur = 10
16. this.context.shadowOffsetY = 20
17. this.context.shadowColor = 'rgb(0,0,0)'
18. this.context.fillStyle = 'rgb(255,0,0)'
19. this.context.fillRect(30, 30, 100, 100)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/xq1638TAQ-ChiC0bV8hEWA/zh-cn_image_0000002589326329.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=94381F5390B7A5284BB442CD910EA2F49CE5720909C938C23159315B9BA283D7)

### imageSmoothingEnabled

PhonePC/2in1TabletTVWearable

用于设置绘制图片时是否进行图像平滑度调整，true为启用，false为不启用，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| boolean | 否 | 否 | 默认值：true |

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageSmoothingEnabled {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/icon.jpg")

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. this.context.imageSmoothingEnabled = false
18. this.context.drawImage(this.img, 0, 0, 400, 200)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ut9oXQcqSmiDISps9dFVSA/zh-cn_image_0000002589246271.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=8B3F13D67DC84C867ABBDE34EAA2875C4C66C95D4E22B35431D5C1A9A31C546B)

### height

PhonePC/2in1TabletTVWearable

组件高度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 是 | 否 | 默认单位：vp |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct HeightExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width(300)
12. .height(300)
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let h = this.context.height
16. this.context.fillRect(0, 0, 300, h / 2)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/0X9sIO-KSuWbyMfFXShU9w/zh-cn_image_0000002558766464.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=FDD0BA2AA52A9B000A6C8DF455C3FF7109D68B0BF0D15BB59C452F94B6CD75EF)

### width

PhonePC/2in1TabletTVWearable

组件宽度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 是 | 否 | 默认单位：vp |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct WidthExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width(300)
12. .height(300)
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let w = this.context.width
16. this.context.fillRect(0, 0, w / 2, 300)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/lJeEB4YrTAyPVHQX56IIkQ/zh-cn_image_0000002558606804.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=E3A5275F6BE55A91A991E94D8741F46892397F59744AB47B6EDB1FAA19887869)

### canvas13+

PhonePC/2in1TabletTVWearable

获取和CanvasRenderingContext2D关联的Canvas组件的FrameNode实例。可用于监听关联的Canvas组件的可见状态。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [FrameNode](js-apis-arkui-framenode.md) | 是 | 否 | 默认值：null |

```
1. import { FrameNode } from '@kit.ArkUI'
2. // xxx.ets
3. @Entry
4. @Component
5. struct CanvasExample {
6. private settings: RenderingContextSettings = new RenderingContextSettings(true)
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
8. private text: string = ''

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. let node: FrameNode = this.context.canvas
18. node?.commonEvent.setOnVisibleAreaApproximateChange(
19. { ratios: [0, 1], expectedUpdateInterval: 10},
20. (isVisible: boolean, currentRatio: number) => {
21. if (!isVisible && currentRatio <= 0.0) {
22. this.text = 'Canvas is completely invisible.'
23. }
24. if (isVisible && currentRatio >= 1.0) {
25. this.text = 'Canvas is fully visible.'
26. }
27. this.context.reset()
28. this.context.font = '30vp sans-serif'
29. this.context.fillText(this.text, 50, 50)
30. }
31. )
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/J8Qi0jmXSVuH5aJ8xLvXxw/zh-cn_image_0000002589326331.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=1800C654E361754CDA882D0E7B7FD54377D2A8912537E330B91123F039B29D31)

### imageSmoothingQuality

PhonePC/2in1TabletTVWearable

imageSmoothingEnabled为true时，用于设置图像平滑度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [ImageSmoothingQuality](ts-canvasrenderingcontext2d.md#imagesmoothingquality类型说明) | 否 | 否 | 默认值："low" |

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageSmoothingQualityDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. let ctx = this.context
18. ctx.imageSmoothingEnabled = true
19. ctx.imageSmoothingQuality = 'high'
20. ctx.drawImage(this.img, 0, 0, 400, 200)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/RixSHzLKTRqY-iVA4hmnLQ/zh-cn_image_0000002589246273.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=E416050B484CC3BC70A517F790E2AD437D8B833A913EFE1D734C21951E561F59)

### direction

PhonePC/2in1TabletTVWearable

用于设置绘制文字时使用的文字方向，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasDirection](ts-canvasrenderingcontext2d.md#canvasdirection类型说明) | 否 | 否 | 默认值："inherit" |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DirectionDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let ctx = this.context
16. ctx.font = '48px serif';
17. ctx.textAlign = 'start'
18. ctx.fillText("Hi ltr!", 200, 50);

20. ctx.direction = "rtl";
21. ctx.fillText("Hi rtl!", 200, 100);
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/UCS2PPmhRSqY1H7DA7R22A/zh-cn_image_0000002558766466.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=564174C9C5A95839C6350F895604A748EDC50EA518BBA1E531A27E681A495E2C)

### filter

PhonePC/2in1TabletTVWearable

用于设置图像的滤镜，可以组合任意数量的滤镜，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 支持的滤镜效果如下：  - 'none': 无滤镜效果。  - 'blur(<length>)'：给图像设置高斯模糊，取值范围≥0，支持单位px、vp、rem，默认值：blur(0px)。  - 'brightness([<number>|<percentage>])'：给图片应用一种线性乘法，使其看起来更亮或更暗，支持数字和百分比参数，取值范围≥0，默认值：brightness(1)。  - 'contrast([<number>|<percentage>])'：调整图像的对比度，支持数字和百分比参数，取值范围≥0，默认值：contrast(1)。  - 'grayscale([<number>|<percentage>])'：将图像转换为灰度图像，支持数字和百分比参数，取值范围[0, 1]，默认值：grayscale(0)。  - 'hue-rotate(<angle>)'：给图像应用色相旋转，取值范围0deg-360deg，默认值：hue-rotate(0deg)。  - 'invert([<number>|<percentage>])'：反转输入图像，支持数字和百分比参数，取值范围[0, 1]，默认值：invert(0)。  - 'opacity([<number>|<percentage>])'：调整图像的透明程度，支持数字和百分比参数，取值范围[0, 1]，默认值：opacity(1)。  - 'saturate([<number>|<percentage>])'：转换图像饱和度，支持数字和百分比参数，取值范围≥0，默认值：saturate(1)。  - 'sepia([<number>|<percentage>])'：将图像转换为深褐色，支持数字和百分比参数，取值范围[0, 1]，默认值：sepia(0)。 |

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FilterDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .onReady(() => {
16. let ctx = this.context
17. let img = this.img

19. ctx.drawImage(img, 0, 0, 100, 100);

21. ctx.filter = 'grayscale(50%)';
22. ctx.drawImage(img, 100, 0, 100, 100);

24. ctx.filter = 'sepia(60%)';
25. ctx.drawImage(img, 200, 0, 100, 100);

27. ctx.filter = 'saturate(30%)';
28. ctx.drawImage(img, 0, 100, 100, 100);

30. ctx.filter = 'hue-rotate(90deg)';
31. ctx.drawImage(img, 100, 100, 100, 100);

33. ctx.filter = 'invert(100%)';
34. ctx.drawImage(img, 200, 100, 100, 100);

36. ctx.filter = 'opacity(25%)';
37. ctx.drawImage(img, 0, 200, 100, 100);

39. ctx.filter = 'brightness(0.4)';
40. ctx.drawImage(img, 100, 200, 100, 100);

42. ctx.filter = 'contrast(200%)';
43. ctx.drawImage(img, 200, 200, 100, 100);

45. ctx.filter = 'blur(5px)';
46. ctx.drawImage(img, 0, 300, 100, 100);

48. // Applying multiple filters
49. ctx.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
50. ctx.drawImage(img, 100, 300, 100, 100);
51. })
52. }
53. .width('100%')
54. .height('100%')
55. }
56. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/fn4N-g2jSx2zK_E4a-9Syw/zh-cn_image_0000002558606806.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=29A5AC8E33E265B8DAB6AD611895A71E327C070A86BFB0B017E424E0C87B921E)

### letterSpacing18+

PhonePC/2in1TabletTVWearable

用于指定绘制文本时字母之间的间距，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | [LengthMetrics](js-apis-arkui-graphics.md#lengthmetrics12) | 否 | 否 | 当使用LengthMetrics时：  字间距按照指定的单位设置；  不支持FP、PERCENT和LPX（按无效值处理）；  支持负数和小数，设为小数时字间距不四舍五入。  当使用string时：  不支持设置百分比（按无效值处理）；  支持负数和小数，设为小数时字间距不四舍五入；  若letterSpacing的赋值未指定单位（例如：letterSpacing='10'），且未指定LengthMetricsUnit时，默认单位设置为vp；  指定LengthMetricsUnit为px时，默认单位设置为px；  当letterSpacing的赋值指定单位时（例如：letterSpacing='10vp'），字间距按照指定的单位设置。  默认值：0（输入无效值时，字间距设为默认值）  注：推荐使用LengthMetrics，性能更好。 |

```
1. // xxx.ets
2. import { LengthMetrics, LengthUnit } from '@kit.ArkUI'

4. @Entry
5. @Component
6. struct letterSpacingDemo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true)
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('rgb(213,213,213)')
16. .onReady(() => {
17. this.context.font = '30vp'
18. this.context.letterSpacing = '10vp'
19. this.context.fillText('hello world', 30, 50)
20. this.context.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
21. this.context.fillText('hello world', 30, 100)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/5O-7TlS2Tyq8AEDpFrE-Nw/zh-cn_image_0000002589326333.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=B4A766DF0A578A181309F0619A5C5175B776E1BE567F11077249BF5C500B583F)

## 方法

PhonePC/2in1TabletTVWearable

以下方法在隐藏页面中调用会产生缓存，应避免在隐藏页面中频繁刷新Canvas。

### fillRect

PhonePC/2in1TabletTVWearable

fillRect(x: number, y: number, w: number, h: number): void

填充一个矩形。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形左上角点的x坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 指定矩形左上角点的y坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.fillRect(30, 30, 100, 100)
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/hOeHYEfjR6ajedo4GTDN6Q/zh-cn_image_0000002589246275.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=0FBAEFBED328630F8ADCE257F4E48FCF30294F95EBFF0F440FA6DEF29A077A97)

### strokeRect

PhonePC/2in1TabletTVWearable

strokeRect(x: number, y: number, w: number, h: number): void

绘制具有边框的矩形，矩形内部不填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.strokeRect(30, 30, 200, 150)
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/Y4O5w1duQlWqIHtFBQJhfw/zh-cn_image_0000002558766468.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=0683CCFA00D991532BC87C010F4E6D32DB0C8D240673D58B94C8B10E571F6DF0)

### clearRect

PhonePC/2in1TabletTVWearable

clearRect(x: number, y: number, w: number, h: number): void

删除指定区域内的绘制内容。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形上的左上角x坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 指定矩形上的左上角y坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClearRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillStyle = 'rgb(0,0,255)'
16. this.context.fillRect(20, 20, 200, 200)
17. this.context.clearRect(30, 30, 150, 100)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/KCP4D45BQkOb-hr4ypzsEA/zh-cn_image_0000002558606808.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=1E7E844BCF8465A5B99A92E369973ACDABECA384C3048F6D22B0440F83D11D4D)

### fillText

PhonePC/2in1TabletTVWearable

fillText(text: string, x: number, y: number, maxWidth?: number): void

绘制填充类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。  异常值undefined或null按无效值处理，不进行绘制。 |
| x | number | 是 | 文本绘制起点的x轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 文本绘制起点的y轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| maxWidth | number | 否 | 指定文本允许的最大宽度。  异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。  默认值：不限制宽度。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.font = '30px sans-serif'
16. this.context.fillText("Hello World!", 20, 100)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/_BXqsh7ESwu9gf29p_mggQ/zh-cn_image_0000002589326335.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=326B9972C6549F20B66A5F1665F2B4EFFEA71A51C8AA06CE69E90945DE4C5C15)

### strokeText

PhonePC/2in1TabletTVWearable

strokeText(text: string, x: number, y: number, maxWidth?: number): void

绘制描边类文本。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要绘制的文本内容。  异常值undefined或null按无效值处理，不进行绘制。 |
| x | number | 是 | 文本绘制起点的x轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| y | number | 是 | 文本绘制起点的y轴坐标。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| maxWidth | number | 否 | 需要绘制的文本的最大宽度。  异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。  默认单位：vp  默认值：不限制宽度。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.font = '50vp sans-serif'
16. this.context.strokeText("Hello World!", 20, 60)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/HB1X28VoRDeWwzN-QSNxqw/zh-cn_image_0000002589246277.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=336A5840554D873749B515562A76D17FAE2E8C43DFC86F281DBE3AF9D7B2CB28)

### measureText

PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。不同设备上获取的宽度值可能不同。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。  传入异常值undefined或null时按"undefined"或"null"计算。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextMetrics](ts-canvasrenderingcontext2d.md#textmetrics) | 文本的尺寸信息。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MeasureText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.font = '50px sans-serif'
16. this.context.fillText("Hello World!", 20, 100)
17. this.context.fillText("width:" + this.context.measureText("Hello World!").width, 20, 200)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/lqqu_Az3RdeYIT_4SkfKEg/zh-cn_image_0000002558766470.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=B6E47835469813C89C34CE7B71674052E9608294939590E80AF5B0A44EDF721E)

### stroke

PhonePC/2in1TabletTVWearable

stroke(): void

根据当前的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Stroke {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.moveTo(125, 25)
16. this.context.lineTo(125, 105)
17. this.context.lineTo(175, 105)
18. this.context.lineTo(175, 25)
19. this.context.strokeStyle = 'rgb(255,0,0)'
20. this.context.stroke()
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/GBFI6oMhSJeyjufJDtmIDw/zh-cn_image_0000002558606810.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=FD3253600E596568DE8DFAE284999ACB347116E1B678BE00C20A4261F26E0CC6)

### stroke

PhonePC/2in1TabletTVWearable

stroke(path: Path2D): void

根据指定的路径，进行边框绘制操作。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path2D](ts-components-canvas-path2d.md) | 是 | 需要绘制的Path2D。  异常值undefined或null按无效值处理，不进行绘制。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Stroke {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. private path2Da: Path2D = new Path2D()

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. this.path2Da.moveTo(25, 25)
17. this.path2Da.lineTo(25, 105)
18. this.path2Da.lineTo(75, 105)
19. this.path2Da.lineTo(75, 25)
20. this.context.strokeStyle = 'rgb(0,0,255)'
21. this.context.stroke(this.path2Da)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/cbrS-p8VSySnBgQG9gZS6w/zh-cn_image_0000002589326337.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=9D93F10B1DB1D035A8F9C6FB91F126348A4F0AD6694E4276DE41957DA271D7A3)

### beginPath

PhonePC/2in1TabletTVWearable

beginPath(): void

创建一个新的绘制路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BeginPath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.lineWidth = 6
16. this.context.strokeStyle = 'rgb(39,135,217)'
17. this.context.moveTo(15, 80)
18. this.context.lineTo(280, 160)
19. this.context.stroke()
20. this.context.beginPath()
21. this.context.lineTo(300, 240)
22. this.context.lineTo(15, 240)
23. this.context.stroke()
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/OmEW90XSS-GdKd9c1NLMNg/zh-cn_image_0000002589246279.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=4EE5E46C7FADB0680A0D7A5FF19ED0597205D65B3EA912126F0F314EF2C90AAE)

### moveTo

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): void

路径从当前点移动到指定点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定位置的y坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

说明

API version 18之前，若未执行moveTo接口或moveTo接口传入无效参数，路径以(0,0)为起点。

API version 18及以后，若未执行moveTo接口或moveTo接口传入无效参数，路径以初次调用的lineTo、arcTo、bezierCurveTo或quadraticCurveTo接口中的起始点为起点。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MoveTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.beginPath()
16. this.context.moveTo(10, 10)
17. this.context.lineTo(280, 160)
18. this.context.stroke()
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/Y31CLlFsSTqxoJgrRTtTJA/zh-cn_image_0000002558766472.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=3E92582F7EBAF0E1E77FBB8FB8E22F1CE5113AE52F14B979EDCC3DC230DC3ED4)

### lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定位置的y坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.beginPath()
16. this.context.moveTo(10, 10)
17. this.context.lineTo(280, 160)
18. this.context.stroke()
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Wi1sWpcGTPWB4jC2Zgcpxw/zh-cn_image_0000002558606812.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=36C5A736D98AB77867CCEF82F76B1863FBB7A9D9486857757CB1402F5138B5D9)

### closePath

PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径，形成一个封闭路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClosePath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.beginPath()
16. this.context.moveTo(30, 30)
17. this.context.lineTo(110, 30)
18. this.context.lineTo(70, 90)
19. this.context.closePath()
20. this.context.stroke()
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/EFkj4vLISgGw7fib1GAHAw/zh-cn_image_0000002589326339.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=C551AA8BD6C0D3ECD9583144646A9A95DDA29AF873FF02A35183955214E6926E)

### createPattern

PhonePC/2in1TabletTVWearable

createPattern(image: ImageBitmap, repetition: string | null): CanvasPattern | null

通过指定图像和重复方式创建图片填充的模板。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](ts-components-canvas-imagebitmap.md) | 是 | 图源对象，具体参考ImageBitmap对象。  异常值undefined或null按无效值处理。 |
| repetition | string | null | 是 | 设置图像重复的方式：  'repeat'：沿x轴和y轴重复绘制图像；  'repeat-x'：沿x轴重复绘制图像；  'repeat-y'：沿y轴重复绘制图像；  'no-repeat'：不重复绘制图像；  'clamp'：在原始边界外绘制时，超出部分使用边缘的颜色绘制；  'mirror'：沿x轴和y轴重复翻转绘制图像。  异常值undefined或null按无效值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasPattern](ts-components-canvas-canvaspattern.md) | null | 通过指定图像和重复方式创建图片填充的模板对象。 |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreatePattern {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/icon.jpg")

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. let pattern = this.context.createPattern(this.img, 'repeat')
18. if (pattern) {
19. this.context.fillStyle = pattern
20. }
21. this.context.fillRect(0, 0, 200, 200)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/yFFX0-FGQReI2rzqCOV1qQ/zh-cn_image_0000002589246281.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=C2D74364E43A566C0D7D241D1813E74E00E4454AADD58B1C12841EB2AA5A0AE1)

### bezierCurveTo

PhonePC/2in1TabletTVWearable

bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void

创建三次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cp1x | number | 是 | 第一个贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp1y | number | 是 | 第一个贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp2x | number | 是 | 第二个贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cp2y | number | 是 | 第二个贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. import { Point } from '@kit.TestKit';

4. @Entry
5. @Component
6. struct BezierCurveTo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private start: Point = { x: 50, y: 50 };
10. private end: Point = { x: 250, y: 100 };
11. private cp1: Point = { x: 200, y: 30 };
12. private cp2: Point = { x: 130, y: 80 };

14. build() {
15. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
16. Canvas(this.context)
17. .width('100%')
18. .height('100%')
19. .backgroundColor('rgb(213,213,213)')
20. .onReady(() => {
21. let ctx = this.context;
22. // 三次贝塞尔曲线
23. ctx.beginPath();
24. ctx.moveTo(this.start.x, this.start.y);
25. ctx.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
26. ctx.stroke();

28. // 起点和终点
29. ctx.fillStyle = 'rgb(39,135,217)';
30. ctx.beginPath();
31. ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
32. ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
33. ctx.fill();

35. // 控制点
36. ctx.fillStyle = 'rgb(23,169,141)';
37. ctx.beginPath();
38. ctx.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
39. ctx.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
40. ctx.fill();
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/ZLSxWtecQDGYMvXCMerLxg/zh-cn_image_0000002558766474.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=B37C2D79A2690AA2F3359BB9A3C9B6DA072487DC7220B769A49E5D3E4A136565)

### quadraticCurveTo

PhonePC/2in1TabletTVWearable

quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void

创建二次贝塞尔曲线的路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cpx | number | 是 | 贝塞尔参数的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| cpy | number | 是 | 贝塞尔参数的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x | number | 是 | 路径结束时的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 路径结束时的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. import { Point } from '@kit.TestKit';

4. @Entry
5. @Component
6. struct QuadraticCurveTo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private start: Point = { x: 50, y: 20 };
10. private end: Point = { x: 50, y: 100 };
11. private cp: Point = { x: 230, y: 30 };

13. build() {
14. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
15. Canvas(this.context)
16. .width('100%')
17. .height('100%')
18. .backgroundColor('rgb(213,213,213)')
19. .onReady(() => {
20. let ctx = this.context;
21. // 二次贝塞尔曲线
22. ctx.beginPath();
23. ctx.moveTo(this.start.x, this.start.y);
24. ctx.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
25. ctx.stroke();

27. // 起始点和结束点
28. ctx.fillStyle = 'rgb(39,135,217)';
29. ctx.beginPath();
30. ctx.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
31. ctx.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
32. ctx.fill();

34. // 控制点
35. ctx.fillStyle = 'rgb(23,169,141)';
36. ctx.beginPath();
37. ctx.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
38. ctx.fill();
39. })
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/ITm3pQGUSEqKitKbTkx_eg/zh-cn_image_0000002558606814.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=660C65CBC69A2E545033CD5E1ECA960DFA98EB539449AE60E1DE651A4F421C97)

### arc

PhonePC/2in1TabletTVWearable

arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

绘制弧线路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 弧线圆心的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 弧线圆心的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radius | number | 是 | 弧线的圆半径。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| startAngle | number | 是 | 弧线的起始弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| endAngle | number | 是 | 弧线的终止弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。  true：逆时针方向绘制圆弧。  false：顺时针方向绘制圆弧。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Arc {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.beginPath()
16. this.context.arc(100, 75, 50, 0, 6.28)
17. this.context.stroke()
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/zjX6ESb1Ss6SnNY9SOgVJA/zh-cn_image_0000002589326341.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=EE2C3DA854FC264A6F93E699494A031A7BD01FFD1D7C4885FA15641BC078D657)

### arcTo

PhonePC/2in1TabletTVWearable

arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void

依据给定的控制点和圆弧半径创建圆弧路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x1 | number | 是 | 第一个控制点的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y1 | number | 是 | 第一个控制点的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| x2 | number | 是 | 第二个控制点的x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y2 | number | 是 | 第二个控制点的y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radius | number | 是 | 圆弧的圆半径值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ArcTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. // 切线
16. this.context.beginPath()
17. this.context.strokeStyle = '#808080'
18. this.context.lineWidth = 1.5;
19. this.context.moveTo(360, 20);
20. this.context.lineTo(360, 170);
21. this.context.lineTo(110, 170);
22. this.context.stroke();

24. // 圆弧
25. this.context.beginPath()
26. this.context.strokeStyle = '#000000'
27. this.context.lineWidth = 3;
28. this.context.moveTo(360, 20)
29. this.context.arcTo(360, 170, 110, 170, 150)
30. this.context.stroke()

32. // 起始点
33. this.context.beginPath();
34. this.context.fillStyle = '#00ff00';
35. this.context.arc(360, 20, 4, 0, 2 * Math.PI);
36. this.context.fill();

38. // 控制点
39. this.context.beginPath();
40. this.context.fillStyle = '#ff0000';
41. this.context.arc(360, 170, 4, 0, 2 * Math.PI);
42. this.context.arc(110, 170, 4, 0, 2 * Math.PI);
43. this.context.fill();
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/faNsBqy-TbGnKqgN6kmW8Q/zh-cn_image_0000002589246283.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=95EF4689984C73B5850C0D009D1221A720FBB1BCB5B036DC3B1FC21E51774548)

此示例中，arcTo()创建的圆弧为黑色，圆弧的两条切线为灰色。控制点为红色，起始点为绿色。

可以想象两条切线：一条切线从起始点到第一个控制点，另一条切线从第一个控制点到第二个控制点。arcTo()在这两条切线间创建一个圆弧，并使圆弧与这两条切线都相切。

### ellipse

PhonePC/2in1TabletTVWearable

ellipse(x: number, y: number, radiusX: number, radiusY: number, rotation: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void

在规定的矩形区域绘制一个椭圆。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 椭圆圆心的x轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 椭圆圆心的y轴坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radiusX | number | 是 | 椭圆x轴的半径长度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| radiusY | number | 是 | 椭圆y轴的半径长度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| rotation | number | 是 | 椭圆的旋转角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位：弧度 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。  true：逆时针方向绘制椭圆。  false：顺时针方向绘制椭圆。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.beginPath()
16. this.context.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
17. this.context.stroke()
18. this.context.beginPath()
19. this.context.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
20. this.context.stroke()
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/22MV2ImkTAOH9dFK6P-uEQ/zh-cn_image_0000002558766476.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=7D3D04FB914EA2CB43833FA5FC880F9904D695673EADDBC558B10C9BD62CE3FF)

### rect

PhonePC/2in1TabletTVWearable

rect(x: number, y: number, w: number, h: number): void

创建矩形路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| h | number | 是 | 指定矩形的高度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
16. this.context.stroke()
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/MIHk_sKvRk2-_bbqzaj_XA/zh-cn_image_0000002558606816.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=16B0F2999714FB858563373CEEF04E75565E46479FB4127176FE69745383DFA0)

### roundRect20+

PhonePC/2in1TabletTVWearable

roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 指定矩形的左上角x坐标值。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[0, Canvas宽度)。  默认单位：vp |
| y | number | 是 | 指定矩形的左上角y坐标值。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[0, Canvas高度)。  默认单位：vp |
| w | number | 是 | 指定矩形的宽度，设置负值为向左绘制。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[-x, Canvas宽度 - x]。  默认单位：vp |
| h | number | 是 | 指定矩形的高度，设置负值为向上绘制。  null按0处理，undefined按无效值处理，不进行绘制。  如需绘制完整矩形，取值范围：[-y, Canvas高度 - y]。  默认单位：vp |
| radii | number | Array<number> | 否 | 指定用于矩形角的圆弧半径的数字或列表。  参数类型为number时，所有矩形角的圆弧半径按该数字执行。  参数类型为Array<number>时，数目为1-4个按下面执行：  [所有矩形角的圆弧半径]  [左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径]  [左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径]  [左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径]  radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。  默认值：0，null和undefined按默认值处理。  圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。  默认单位：vp |

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](errorcode-canvas.md)。

| 错误码ID | 错误信息 | 可能原因 |
| --- | --- | --- |
| 103701 | Parameter error. | 1. The param radii is a list that has zero or more than four elements; 2. The param radii contains negative value. |

**示例：**

该示例展示了绘制六个圆角矩形：

1. 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
2. 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形并填充；
3. 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形并描边；
4. 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形并描边；
5. 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边；
6. 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形并描边。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct CanvasExample {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#D5D5D5')
16. .onReady(() => {
17. try {
18. this.context.fillStyle = '#707070'
19. this.context.beginPath()
20. // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
21. this.context.roundRect(10, 10, 100, 100, 10)
22. // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
23. this.context.roundRect(120, 10, 100, 100, [10])
24. this.context.fill()
25. this.context.beginPath()
26. // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
27. this.context.roundRect(10, 120, 100, 100, [10, 20])
28. // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
29. this.context.roundRect(120, 120, 100, 100, [10, 20, 30])
30. // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
31. this.context.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
32. // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
33. this.context.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
34. this.context.stroke()
35. } catch (error) {
36. let e: BusinessError = error as BusinessError;
37. console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
38. }
39. })
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/1F5RRrr-RSG8ys7bOyHRbw/zh-cn_image_0000002589326343.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=6A16C94C53D9335B6AE25EB685FD491C523A5BF6856F840C611139F0BFB22273)

### fill

PhonePC/2in1TabletTVWearable

fill(fillRule?: CanvasFillRule): void

对当前路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要填充对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例:**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Fill {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
16. this.context.fill()
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/EmmJuhOAQBCwWeqQIkhEyw/zh-cn_image_0000002589246285.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=91282B5D21D4132618F073CCB403D4DC8D350F427D93C999B0B0C533ADBF6B74)

### fill

PhonePC/2in1TabletTVWearable

fill(path: Path2D, fillRule?: CanvasFillRule): void

对指定路径进行填充。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path2D](ts-components-canvas-path2d.md) | 是 | Path2D填充路径。  异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要填充对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例:**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Fill {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let region = new Path2D()
16. region.moveTo(30, 90)
17. region.lineTo(110, 20)
18. region.lineTo(240, 130)
19. region.lineTo(60, 130)
20. region.lineTo(190, 20)
21. region.lineTo(270, 90)
22. region.closePath()
23. // Fill path
24. this.context.fillStyle = '#00ff00'
25. this.context.fill(region, "evenodd")
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/I4MNFI3OTkqlaD9lOI9t1A/zh-cn_image_0000002558766478.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=153D6AEAF689A982ECEDCF1FD4A29E96CA3B01270436953253B069081FEDCD29)

### clip

PhonePC/2in1TabletTVWearable

clip(fillRule?: CanvasFillRule): void

设置当前路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fillRule | [CanvasFillRule](ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要剪切对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例:**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Clip {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.rect(0, 0, 100, 200)
16. this.context.stroke()
17. this.context.clip()
18. this.context.fillStyle = "rgb(255,0,0)"
19. this.context.fillRect(0, 0, 200, 200)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/6JOn84CzSMqXmVKicfa6zA/zh-cn_image_0000002558606818.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=CD31EE6510E52A0C0A8C02DB8D837EC0D37B3A64F552A439EC5EBD9C7F721E32)

### clip

PhonePC/2in1TabletTVWearable

clip(path: Path2D, fillRule?: CanvasFillRule): void

设置指定路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | [Path2D](ts-components-canvas-path2d.md) | 是 | Path2D剪切路径。  异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要剪切对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例:**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Clip {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let region = new Path2D()
16. region.moveTo(30, 90)
17. region.lineTo(110, 20)
18. region.lineTo(240, 130)
19. region.lineTo(60, 130)
20. region.lineTo(190, 20)
21. region.lineTo(270, 90)
22. region.closePath()
23. this.context.clip(region, "evenodd")
24. this.context.fillStyle = "rgb(0,255,0)"
25. this.context.fillRect(0, 0, this.context.width, this.context.height)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Stutt0SrTHq-sgiphAdlQA/zh-cn_image_0000002589326345.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=46A2B41F04AA9738AB7B948AAD828F33F2B9D6984F35155CD360E098D40975ED)

### reset12+

PhonePC/2in1TabletTVWearable

reset(): void

将CanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Reset {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillStyle = '#0000ff'
16. this.context.fillRect(20, 20, 150, 100)
17. this.context.reset()
18. this.context.fillRect(20, 150, 150, 100)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/Xkf39FNdQeaLXRUQ-JxD9g/zh-cn_image_0000002589246287.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=46F1DE0649D65D79305FAA4468B0C1406B8703B8CF24C536C532B1EBDE05391D)

### saveLayer12+

PhonePC/2in1TabletTVWearable

saveLayer(): void

创建一个图层。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct saveLayer {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() =>{
15. this.context.fillStyle = "#0000ff"
16. this.context.fillRect(50,100,300,100)
17. this.context.fillStyle = "#00ffff"
18. this.context.fillRect(50,150,300,100)
19. this.context.globalCompositeOperation = 'destination-over'
20. this.context.saveLayer()
21. this.context.globalCompositeOperation = 'source-over'
22. this.context.fillStyle = "#ff0000"
23. this.context.fillRect(100,50,100,300)
24. this.context.fillStyle = "#00ff00"
25. this.context.fillRect(150,50,100,300)
26. this.context.restoreLayer()
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/zg5ZWNxdSfqsbSpUc4VvRQ/zh-cn_image_0000002558766480.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=B02DAFFD9923EC5229F146FF4E73F1CDF70DC7B5464CCD2B1BE86C90377E6492)

### restoreLayer12+

PhonePC/2in1TabletTVWearable

restoreLayer(): void

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。restoreLayer示例代码同saveLayer。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### resetTransform

PhonePC/2in1TabletTVWearable

resetTransform(): void

使用单位矩阵重新设置当前矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ResetTransform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.setTransform(1, 0.5, -0.5, 1, 10, 10)
16. this.context.fillStyle = 'rgb(0,0,255)'
17. this.context.fillRect(0, 0, 100, 100)
18. this.context.resetTransform()
19. this.context.fillStyle = 'rgb(255,0,0)'
20. this.context.fillRect(0, 0, 100, 100)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/WZmxC_rOSkSIE9vE_8hW5g/zh-cn_image_0000002558606820.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=600F103BA64BCB7BEDEF2F94CBD396DA86383420733BF665D37B00E0F7AA763A)

### rotate

PhonePC/2in1TabletTVWearable

rotate(angle: number): void

针对当前坐标轴进行顺时针旋转。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | number | 是 | 设置顺时针旋转的弧度值，可以通过 degree \* Math.PI / 180 将角度转换为弧度值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  单位：弧度 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Rotate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.rotate(45 * Math.PI / 180)
16. this.context.fillRect(70, 20, 50, 50)
17. })
18. }
19. .width('100%')
20. .height('100%')
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/_bCVjYJNTRCrZB9cl4iKaw/zh-cn_image_0000002589326347.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=0A4B00E690AD5383F794BFDBCAA68B37066E511CEBA1A111EA14563B22BDCF0E)

### scale

PhonePC/2in1TabletTVWearable

scale(x: number, y: number): void

设置canvas画布的缩放变换属性，后续的绘制操作将按照缩放比例进行缩放。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平方向的缩放值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；不支持设置0和负数，设置0、负数、null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、0、负数、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| y | number | 是 | 设置垂直方向的缩放值，不支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；不支持设置0和负数，设置0、负数、null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、0、负数、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Scale {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.lineWidth = 3
16. this.context.strokeRect(30, 30, 50, 50)
17. this.context.scale(2, 2) // Scale to 200%
18. this.context.strokeRect(30, 30, 50, 50)
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/v-FySRQoQ_yvUYtv6iTnTw/zh-cn_image_0000002589246289.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=635167213F63CF807912F43D7DD30225F5BFEC732DDCB4088165D28946C392F1)

### transform

PhonePC/2in1TabletTVWearable

transform(a: number, b: number, c: number, d: number, e: number, f: number): void

transform方法对应一个变换矩阵，想对一个图形进行变化的时候，只要设置此变换矩阵相应的参数，对图形的各个定点的坐标分别乘以这个矩阵，就能得到新的定点的坐标。矩阵变换效果可叠加。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = a \* x + c \* y + e
* y' = b \* x + d \* y + f

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| a | number | 是 | 变换矩阵中第一行第一列的单元格。scaleX：指定水平缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| b | number | 是 | 变换矩阵第二行第一列的单元格。skewY：指定垂直倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| c | number | 是 | 变换矩阵第一行第二列的单元格。skewX：指定水平倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| d | number | 是 | 变换矩阵第二行第二列的单元格。scaleY：指定垂直缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| e | number | 是 | 变换矩阵第一行第三列的单元格。translateX：指定水平移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |
| f | number | 是 | 变换矩阵第二行第三列的单元格。translateY：指定垂直移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Transform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.fillStyle = 'rgb(112,112,112)'
16. this.context.fillRect(0, 0, 100, 100)
17. this.context.transform(1, 0.5, -0.5, 1, 10, 10)
18. this.context.fillStyle = 'rgb(0,74,175)'
19. this.context.fillRect(0, 0, 100, 100)
20. this.context.transform(1, 0.5, -0.5, 1, 10, 10)
21. this.context.fillStyle = 'rgb(39,135,217)'
22. this.context.fillRect(0, 0, 100, 100)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/KieLKnkuRqG7erCLd5Muew/zh-cn_image_0000002558766482.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=D11204C2A290E923A75A07010B52F5D89A769BAAC46114D0061327BC55448E6C)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(a: number, b: number, c: number, d: number, e: number, f: number): void

setTransform方法使用的参数和transform()方法相同，但setTransform()方法会重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

说明

图形中各个点变换后的坐标可通过下方坐标计算公式计算。

变换后的坐标计算方式（x和y为变换前坐标，x'和y'为变换后坐标）：

* x' = a \* x + c \* y + e
* y' = b \* x + d \* y + f

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| a | number | 是 | scaleX：指定水平缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| b | number | 是 | skewY：指定垂直倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| c | number | 是 | skewX：指定水平倾斜值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| d | number | 是 | scaleY：指定垂直缩放值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| e | number | 是 | translateX：指定水平移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |
| f | number | 是 | translateY：指定垂直移动值，支持设置负数。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SetTransform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. this.context.fillStyle = 'rgb(112,112,112)'
16. this.context.fillRect(0, 0, 100, 100)
17. this.context.transform(1, 0.5, -0.5, 1, 10, 10)
18. this.context.fillStyle = 'rgb(23,169,141)'
19. this.context.fillRect(0, 0, 100, 100)
20. this.context.setTransform(1, 0.5, -0.5, 1, 10, 10)
21. this.context.fillStyle = 'rgb(39,135,217)'
22. this.context.fillRect(0, 0, 100, 100)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/ufW0-igoQzCocuIE3ZDt2A/zh-cn_image_0000002558606822.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=64FB988C980CF1DA0922C0E075B59E6175BD2BAE0FBFDD9A6A0A670388F0E9B3)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(transform?: Matrix2D): void

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transform | [Matrix2D](ts-components-canvas-matrix2d.md) | 否 | 变换矩阵。  异常值undefined或null按无效值处理。  默认值：null |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransFormDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Text('context1');
12. Canvas(this.context1)
13. .width('230vp')
14. .height('160vp')
15. .backgroundColor('#ffff00')
16. .onReady(() =>{
17. this.context1.fillRect(100, 20, 50, 50);
18. this.context1.setTransform(1, 0.5, -0.5, 1, 10, 10);
19. this.context1.fillRect(100, 20, 50, 50);
20. })
21. Text('context2');
22. Canvas(this.context2)
23. .width('230vp')
24. .height('160vp')
25. .backgroundColor('#0ffff0')
26. .onReady(() =>{
27. this.context2.fillRect(100, 20, 50, 50);
28. let storedTransform = this.context1.getTransform();
29. this.context2.setTransform(storedTransform);
30. this.context2.fillRect(100, 20, 50, 50);
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Az57Mx1zQwaKddRAz4TEyQ/zh-cn_image_0000002589326349.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=72846B81A5FC064397E529706BE9BFF6F8D0A671E78336897437725461F5371C)

### getTransform

PhonePC/2in1TabletTVWearable

getTransform(): Matrix2D

获取当前被应用到上下文的转换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix2D](ts-components-canvas-matrix2d.md) | 当前被应用到上下文的转换矩阵。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransFormDemo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context1: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Text('context1');
12. Canvas(this.context1)
13. .width('230vp')
14. .height('120vp')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. this.context1.fillRect(50, 50, 50, 50);
18. this.context1.setTransform(1.2, Math.PI / 8, Math.PI / 6, 0.5, 30, -25);
19. this.context1.fillRect(50, 50, 50, 50);
20. })
21. Text('context2');
22. Canvas(this.context2)
23. .width('230vp')
24. .height('120vp')
25. .backgroundColor('#0ffff0')
26. .onReady(() => {
27. this.context2.fillRect(50, 50, 50, 50);
28. let storedTransform = this.context1.getTransform();
29. console.info(`Matrix [scaleX = ${storedTransform.scaleX}, scaleY = ${storedTransform.scaleY}, rotateX = ${storedTransform.rotateX}, rotateY = ${storedTransform.rotateY}, translateX = ${storedTransform.translateX}, translateY = ${storedTransform.translateY}]`)
30. this.context2.setTransform(storedTransform);
31. this.context2.fillRect(50, 50, 50, 50);
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/HqcGzgWXTpesptOb_Fs_mg/zh-cn_image_0000002589246291.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=522DF7720D39CD22E8354F93567A52BC4E79B4190896C0989E41DE143C582B2C)

### translate

PhonePC/2in1TabletTVWearable

translate(x: number, y: number): void

移动当前坐标系的原点。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 设置水平平移量。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |
| y | number | 是 | 设置竖直平移量。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Translate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillRect(10, 10, 50, 50)
16. this.context.translate(70, 70)
17. this.context.fillRect(10, 10, 50, 50)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ZMfxe8RyQHKN9vZePf_Y_A/zh-cn_image_0000002558766484.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=DDCE4B0F66FEB670419449DEDFFDA46CEECC130B624258FD4EF003DA48EAB04D)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

进行图像绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](ts-components-canvas-imagebitmap.md) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#D5D5D5')
16. .onReady(() => {
17. this.context.drawImage(this.img, 0, 0)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/hFAcy3F7TYW8-7d4g8ZKrg/zh-cn_image_0000002558606824.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=4D145FDF3D464F8114B259E456664DD75D4E487D78DAB8B87A7EC6E24A3DA09E)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

将图像拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](ts-components-canvas-imagebitmap.md) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dh | number | 是 | 绘制区域的高度。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#D5D5D5')
16. .onReady(() => {
17. this.context.drawImage(this.img, 0, 0, 300, 300)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/nv_TrEZITDidzjPrn7cYBA/zh-cn_image_0000002589326351.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=1DCCD83402A6830E5B04A6AD5AFF6E8DFA041A80D7774E62883A443A77D07AB9)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](ts-components-canvas-imagebitmap.md) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sw | number | 是 | 裁切源图像时需要裁切的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sh | number | 是 | 裁切源图像时需要裁切的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。当绘制区域的宽度和裁剪图像的宽度不一致时，将图像宽度拉伸或压缩为绘制区域的宽度。  默认单位：vp |
| dh | number | 是 | 绘制区域的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。当绘制区域的高度和裁剪图像的高度不一致时，将图像高度拉伸或压缩为绘制区域的高度。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#D5D5D5')
16. .onReady(() => {
17. this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/a-m88MliSiS1vDoM4OuyCQ/zh-cn_image_0000002589246293.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=80622EE01332DFBA886798B634C1C5F17D2EF60CA3769996A043AD889B8290B9)

### createImageData

PhonePC/2in1TabletTVWearable

createImageData(sw: number, sh: number): ImageData

创建新的、空白的、指定大小的ImageData 对象，请参考[ImageData](ts-components-canvas-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](ts-canvasrenderingcontext2d.md#putimagedata)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sw | number | 是 | ImageData的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sh | number | 是 | ImageData的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](ts-components-canvas-imagedata.md) | 新的ImageData对象。 |

### createImageData

PhonePC/2in1TabletTVWearable

createImageData(imageData: ImageData): ImageData

根据一个现有的ImageData对象重新创建一个宽、高相同的ImageData对象（不会复制图像数据），请参考[ImageData](ts-components-canvas-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同[putImageData](ts-canvasrenderingcontext2d.md#putimagedata)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](ts-components-canvas-imagedata.md) | 是 | 现有的ImageData对象。  异常值undefined和null按width和height为0的ImageData处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](ts-components-canvas-imagedata.md) | 新的ImageData对象。 |

### getPixelMap

PhonePC/2in1TabletTVWearable

getPixelMap(sx: number, sy: number, sw: number, sh: number): PixelMap

以当前canvas指定区域内的像素创建[PixelMap](arkts-apis-image-pixelmap.md)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sh | number | 是 | 需要输出的区域的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PixelMap](arkts-apis-image-pixelmap.md) | 新的PixelMap对象。 |

**示例：**

说明

* DevEco Studio的预览器不支持显示使用setPixelMap绘制的内容。
* 此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GetPixelMap {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg")

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. this.context.drawImage(this.img, 100, 100, 130, 130)
18. let pixelmap = this.context.getPixelMap(150, 150, 130, 130)
19. this.context.setPixelMap(pixelmap)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/DvmnNFy7T8m_fr-tw247Dg/zh-cn_image_0000002558766486.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=D5C99E97792CEB5BEF5B619587094C077DA46320BCB36D34D17F6B6011422D36)

### setPixelMap

PhonePC/2in1TabletTVWearable

setPixelMap(value?: PixelMap): void

将当前传入[PixelMap](arkts-apis-image-pixelmap.md)对象绘制在画布上。setPixelMap示例同getPixelMap。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 包含像素值的PixelMap对象。  异常值undefined和null按无效值处理，不进行绘制。  默认值：null |

### getImageData

PhonePC/2in1TabletTVWearable

getImageData(sx: number, sy: number, sw: number, sh: number): ImageData

以当前canvas指定区域内的像素创建[ImageData](ts-components-canvas-imagedata.md)对象，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 是 | 需要输出的区域的左上角x坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sy | number | 是 | 需要输出的区域的左上角y坐标。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sw | number | 是 | 需要输出的区域的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| sh | number | 是 | 需要输出的区域的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageData](ts-components-canvas-imagedata.md) | 新的ImageData对象。 |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GetImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. // "/common/images/1234.png"需要替换为开发者所需的图像资源文件
8. private img:ImageBitmap = new ImageBitmap("/common/images/1234.png")

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() =>{
17. this.context.drawImage(this.img,0,0,130,130)
18. let imageData = this.context.getImageData(50,50,130,130)
19. this.context.putImageData(imageData,150,150)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/nIC1HjHBT-GlvybS42Vwng/zh-cn_image_0000002558606826.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=D27E19A5F5623C2774EE63DDE9AA7B360D925F6F0A12AE8F4A3902C339B2A27C)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

使用[ImageData](ts-components-canvas-imagedata.md)数据填充新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](ts-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | string10+ | 是 | 填充区域在x轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dy | number | string10+ | 是 | 填充区域在y轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PutImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. let imageDataNum = this.context.createImageData(100, 100)
16. let imageData = this.context.createImageData(imageDataNum)
17. for (let i = 0; i < imageData.data.length; i += 4) {
18. imageData.data[i + 0] = 112
19. imageData.data[i + 1] = 112
20. imageData.data[i + 2] = 112
21. imageData.data[i + 3] = 255
22. }
23. this.context.putImageData(imageData, 10, 10)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/juaonFGhRQ6XrF4Ho0DzVg/zh-cn_image_0000002589326353.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=524E5EE26D4E8DE77E6B9BE70DCD127599741ADDD382A78A08901F19ECE8F1EF)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth: number | string, dirtyHeight: number | string): void

使用[ImageData](ts-components-canvas-imagedata.md)数据裁剪后填充至新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](ts-components-canvas-imagedata.md) | 是 | 包含像素值的ImageData对象。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | string10+ | 是 | 填充区域在x轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dy | number | string10+ | 是 | 填充区域在y轴方向的偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyX | number | string10+ | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的x轴偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyY | number | string10+ | 是 | 源图像数据矩形裁切范围左上角距离源图像左上角的y轴偏移量。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyWidth | number | string10+ | 是 | 源图像数据矩形裁切范围的宽度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |
| dirtyHeight | number | string10+ | 是 | 源图像数据矩形裁切范围的高度。  异常值undefined、null、NaN和Infinity按0处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PutImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. let imageDataNum = this.context.createImageData(100, 100)
16. let imageData = this.context.createImageData(imageDataNum)
17. for (let i = 0; i < imageData.data.length; i += 4) {
18. imageData.data[i + 0] = 112
19. imageData.data[i + 1] = 112
20. imageData.data[i + 2] = 112
21. imageData.data[i + 3] = 255
22. }
23. this.context.putImageData(imageData, 10, 10, 0, 0, 100, 50)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/7P4fc_HnR9SDCEtnHD35Wg/zh-cn_image_0000002589246295.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=7A889A9B0113BC68BFDB1F52B82842F6B592D57CA565FB32E50FBD8EABF22929)

### setLineDash

PhonePC/2in1TabletTVWearable

setLineDash(segments: number[]): void

设置画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| segments | number[] | 是 | 描述线段如何交替和线段间距长度的数组。  异常值undefined或null按无效值处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SetLineDash {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#D5D5D5')
14. .onReady(() =>{
15. this.context.arc(100, 75, 50, 0, 6.28)
16. this.context.setLineDash([10,20])
17. this.context.stroke()
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/FVU8HniKSz6b9Z1NdXV9Nw/zh-cn_image_0000002558766488.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=42C0D33A1089F2DA9523E5D33F9B3C7CBEB1F2AF0053A570A3B28AE4F01D1D83)

### getLineDash

PhonePC/2in1TabletTVWearable

getLineDash(): number[]

获得当前画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回数组，该数组用来描述线段如何交替和间距长度。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasGetLineDash {
5. @State message: string = 'Hello World'
6. private settings: RenderingContextSettings = new RenderingContextSettings(true)
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

9. build() {
10. Row() {
11. Column() {
12. Text(this.message)
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. Canvas(this.context)
16. .width('100%')
17. .height('100%')
18. .backgroundColor('#D5D5D5')
19. .onReady(() => {
20. this.context.arc(100, 75, 50, 0, 6.28)
21. this.context.setLineDash([10, 20])
22. this.context.stroke()
23. let res = this.context.getLineDash()
24. this.message = JSON.stringify(res)
25. })
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/ojsGhveLQ6CzvAVD1lHb7g/zh-cn_image_0000002558606828.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=886936605DB823F2596D76528F229DD6679A6BDA810AC01880685E93C4782E9B)

### transferFromImageBitmap

PhonePC/2in1TabletTVWearable

transferFromImageBitmap(bitmap: ImageBitmap): void

显示给定的ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bitmap | [ImageBitmap](ts-components-canvas-imagebitmap.md) | 是 | 待显示的ImageBitmap对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct TransferFromImageBitmap {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. private offContext: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 600, this.settings)

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() =>{
16. let imageData = this.offContext.createImageData(100, 100)
17. for (let i = 0; i < imageData.data.length; i += 4) {
18. imageData.data[i + 0] = 255
19. imageData.data[i + 1] = 0
20. imageData.data[i + 2] = 60
21. imageData.data[i + 3] = 80
22. }
23. this.offContext.putImageData(imageData, 10, 10)
24. let image = this.offContext.transferToImageBitmap()
25. this.context.transferFromImageBitmap(image)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/SIXotMnjTl697uoBSXEKTA/zh-cn_image_0000002589326355.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=22481B4A941C45A217A52B31D09E7F813F26D3EAB9411CADAEC75A051475FEF4)

### toDataURL

PhonePC/2in1TabletTVWearable

toDataURL(type?: string, quality?: any): string

生成一个包含图片展示的URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 否 | 用于指定图像格式。  可选参数为："image/png"，"image/jpeg"，"image/webp"。  异常值undefined或null按默认值处理。  默认值：image/png |
| quality | any | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量。如果超出取值范围，将会使用默认值0.92。  异常值undefined、null、NaN和Infinity按默认值处理。  默认值：0.92 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
7. @State toDataURL: string = ""

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width(100)
13. .height(100)
14. .onReady(() =>{
15. this.context.fillStyle = "#00ff00"
16. this.context.fillRect(0,0,100,100)
17. this.toDataURL = this.context.toDataURL("image/png", 0.92)
18. })
19. Text(this.toDataURL)
20. }
21. .width('100%')
22. .height('100%')
23. .backgroundColor('#ffff00')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/x01bQ7ijR0KT_4Gdnt1gkg/zh-cn_image_0000002589246297.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=28A695D6709B703895B21FE4E11DA7F87F5DE4A14F6A1EB3E97F434BEFD341DD)

### restore

PhonePC/2in1TabletTVWearable

restore(): void

恢复保存的绘图上下文。

说明

当restore()次数未超出save()次数时，从栈中弹出存储的绘制状态并恢复CanvasRenderingContext2D对象的属性、剪切路径和变换矩阵的值。

当restore()次数超出save()次数时，此方法不做任何改变。

当没有保存状态时，此方法不做任何改变。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() =>{
15. this.context.save() // save the default state
16. this.context.fillStyle = "#00ff00"
17. this.context.fillRect(20, 20, 100, 100)
18. this.context.restore() // restore to the default state
19. this.context.fillRect(150, 75, 100, 100)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/WoXsgdZ7SWmt5oivtWDZ3A/zh-cn_image_0000002558766490.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=91619CB28F39BAA1370EA979C4CC5C786F864BD1A6268A1F7A972BB4C71C510A)

### save

PhonePC/2in1TabletTVWearable

save(): void

将当前状态放入栈中，保存canvas的全部状态，通常在需要保存绘制状态时调用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() =>{
15. this.context.save() // save the default state
16. this.context.fillStyle = "#00ff00"
17. this.context.fillRect(20, 20, 100, 100)
18. this.context.restore() // restore to the default state
19. this.context.fillRect(150, 75, 100, 100)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/JnbLxMRESAGH7iH-SWe5Dw/zh-cn_image_0000002558766490.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=F1534532E27AD04702DA0102238A6516ACCD68B79A6684D0A543BDBEB6975B13)

### createLinearGradient

PhonePC/2in1TabletTVWearable

createLinearGradient(x0: number, y0: number, x1: number, y1: number): CanvasGradient

创建一个线性渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起点的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y0 | number | 是 | 起点的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| x1 | number | 是 | 终点的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y1 | number | 是 | 终点的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasGradient](ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreateLinearGradient {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() =>{
15. let grad = this.context.createLinearGradient(50,0, 300,100)
16. grad.addColorStop(0.0, 'rgb(39,135,217)')
17. grad.addColorStop(0.5, 'rgb(255,238,240)')
18. grad.addColorStop(1.0, 'rgb(23,169,141)')
19. this.context.fillStyle = grad
20. this.context.fillRect(0, 0, 400, 400)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/GjMleju8SSKMXv9dQXGMsw/zh-cn_image_0000002589246261.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=F2013AFB962A95A101619EB2277A4505338AFFD4E34DBDBC59EED925E831C997)

### createRadialGradient

PhonePC/2in1TabletTVWearable

createRadialGradient(x0: number, y0: number, r0: number, x1: number, y1: number, r1: number): CanvasGradient

创建一个径向渐变色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x0 | number | 是 | 起始圆的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y0 | number | 是 | 起始圆的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| r0 | number | 是 | 起始圆的半径。必须是非负且有限的。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| x1 | number | 是 | 终点圆的x轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| y1 | number | 是 | 终点圆的y轴坐标。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |
| r1 | number | 是 | 终点圆的半径。必须为非负且有限的。  异常值undefined和null会导致此接口返回undefined，NaN和Infinity按无效值处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasGradient](ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreateRadialGradient {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('rgb(213,213,213)')
14. .onReady(() => {
15. let grad = this.context.createRadialGradient(200, 200, 50, 200, 200, 200)
16. grad.addColorStop(0.0, 'rgb(39,135,217)')
17. grad.addColorStop(0.5, 'rgb(255,238,240)')
18. grad.addColorStop(1.0, 'rgb(112,112,112)')
19. this.context.fillStyle = grad
20. this.context.fillRect(0, 0, 440, 440)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/hCuDaz_PSYWs40xa5IHn8Q/zh-cn_image_0000002558606830.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=C00A595A6A6AFD5E25719F3187808A7F6CB2793F4B8A7A92516C5B5297E7C8ED)

### createConicGradient10+

PhonePC/2in1TabletTVWearable

createConicGradient(startAngle: number, x: number, y: number): CanvasGradient

创建一个圆锥渐变色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startAngle | number | 是 | 开始渐变的角度。角度测量从中心右侧水平开始，顺时针移动。  异常值undefined和null按0处理，NaN和Infinity按无效值处理。  单位：弧度 |
| x | number | 是 | 圆锥渐变的中心x轴坐标。  异常值undefined和null按0处理，NaN和Infinity按无效值处理。  默认单位：vp |
| y | number | 是 | 圆锥渐变的中心y轴坐标。  异常值undefined和null按0处理，NaN和Infinity按无效值处理。  默认单位：vp |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CanvasGradient](ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在canvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true)
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffffff')
14. .onReady(() => {
15. let grad = this.context.createConicGradient(0, 50, 80)
16. grad.addColorStop(0.0, 'rgb(39,135,217)')
17. grad.addColorStop(0.5, 'rgb(213,213,213)')
18. grad.addColorStop(1.0, 'rgb(23,160,141)')
19. this.context.fillStyle = grad
20. this.context.fillRect(0, 30, 100, 100)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/rV83_yDUQ4aZ3qOvxYgh7g/zh-cn_image_0000002589326357.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=E40122C93936CE2A2B7BF3E895AF49D1FAC6F299F105EEBA1D2B60E6EF0E379D)

### on('onAttach')13+

PhonePC/2in1TabletTVWearable

on(type: 'onAttach', callback: () => void): void

订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅CanvasRenderingContext2D与Canvas组件发生绑定的回调。  异常值undefined或null按无效值处理。 |
| callback | () => void | 是 | 订阅CanvasRenderingContext2D与Canvas组件发生绑定后触发的回调。  异常值undefined或null按无效值处理。 |

说明

CanvasRenderingContext2D对象在同一时间只能与一个Canvas组件绑定。

当CanvasRenderingContext2D对象和Canvas组件发生绑定时，会触发'onAttach'回调，表示可以获取到[canvas](ts-canvasrenderingcontext2d.md#canvas13)。

避免在'onAttach'中执行绘制方法，应保证Canvas组件已经'[onReady](ts-components-canvas-canvas.md#事件)'再进行绘制。

触发'onAttach'回调的一般场景：

1、Canvas组件创建时绑定CanvasRenderingContext2D对象;

2、CanvasRenderingContext2D对象新绑定一个Canvas组件时。

### on('onDetach')13+

PhonePC/2in1TabletTVWearable

on(type: 'onDetach', callback: () => void): void

订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅CanvasRenderingContext2D与Canvas组件解除绑定的回调。  异常值undefined或null按无效值处理。 |
| callback | () => void | 是 | 订阅CanvasRenderingContext2D与Canvas组件解除绑定后触发的回调。  异常值undefined或null按无效值处理。 |

说明

当CanvasRenderingContext2D对象和Canvas组件解除绑定时，会触发'onDetach'回调，表示应停止绘制行为。

触发'onDetach'回调的一般场景：

1、Canvas组件销毁时解除绑定CanvasRenderingContext2D对象;

2、CanvasRenderingContext2D对象新绑定一个Canvas组件，会先解除已有的绑定。

### off('onAttach')13+

PhonePC/2in1TabletTVWearable

off(type: 'onAttach', callback?: () => void): void

取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅CanvasRenderingContext2D与Canvas组件发生绑定的回调。  异常值undefined或null按无效值处理。 |
| callback | () => void | 否 | 为空表示取消所有订阅CanvasRenderingContext2D与Canvas组件发生绑定后触发的回调。  非空则取消订阅发生绑定对应的回调。  异常值undefined或null按无效值处理。 |

### off('onDetach')13+

PhonePC/2in1TabletTVWearable

off(type: 'onDetach', callback?: () => void): void

取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的场景。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 取消订阅CanvasRenderingContext2D与Canvas组件解除绑定的回调。  异常值undefined或null按无效值处理。 |
| callback | () => void | 否 | 为空代表取消所有订阅CanvasRenderingContext2D与Canvas组件解除绑定后触发的回调。  非空代表取消订阅解除绑定对应的回调。  异常值undefined或null按无效值处理。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { FrameNode } from '@kit.ArkUI'

4. // xxx.ets
5. @Entry
6. @Component
7. struct AttachDetachExample {
8. private settings: RenderingContextSettings = new RenderingContextSettings(true)
9. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
10. private scroller: Scroller = new Scroller()
11. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
12. private node: FrameNode | null = null
13. attachCallback = () => {
14. console.info('CanvasRenderingContext2D attached to the canvas frame node.')
15. this.node = this.context.canvas
16. }
17. detachCallback = () => {
18. console.info('CanvasRenderingContext2D detach from the canvas frame node.')
19. this.node = null
20. }

22. aboutToAppear(): void {
23. try {
24. this.context.on('onAttach', this.attachCallback)
25. this.context.on('onDetach', this.detachCallback)
26. } catch (error) {
27. let e: BusinessError = error as BusinessError;
28. console.error(`Error code: ${e.code}, message: ${e.message}`);
29. }
30. }

32. aboutToDisappear(): void {
33. try {
34. this.context.off('onAttach')
35. this.context.off('onDetach')
36. } catch (error) {
37. let e: BusinessError = error as BusinessError;
38. console.error(`Error code: ${e.code}, message: ${e.message}`);
39. }
40. }

42. build() {
43. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
44. Scroll(this.scroller) {
45. Flex({ direction: FlexDirection.Column }) {
46. ForEach(this.arr, (item: number) => {
47. Row() {
48. if (item == 3) {
49. Canvas(this.context)
50. .width('100%')
51. .height(150)
52. .backgroundColor('rgb(213,213,213)')
53. .onReady(() => {
54. this.context.font = '30vp sans-serif'
55. this.node?.commonEvent.setOnVisibleAreaApproximateChange(
56. { ratios: [0, 1], expectedUpdateInterval: 10 },
57. (isVisible: boolean, currentRatio: number) => {
58. if (!isVisible && currentRatio <= 0.0) {
59. console.info('Canvas is completely invisible.')
60. }
61. if (isVisible && currentRatio >= 1.0) {
62. console.info('Canvas is fully visible.')
63. }
64. }
65. )
66. })
67. } else {
68. Text(item.toString())
69. .width('100%')
70. .height(150)
71. .backgroundColor('rgb(39,135,217)')
72. .borderRadius(15)
73. .fontSize(16)
74. .textAlign(TextAlign.Center)
75. .margin({ top: 5 })
76. }
77. }
78. }, (item: number) => item.toString())
79. }
80. }
81. .width('90%')
82. .scrollBar(BarState.Off)
83. .scrollable(ScrollDirection.Vertical)
84. }
85. .width('100%')
86. .height('100%')
87. }
88. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/xy8R1umlQQCIeW0vkKc_oQ/zh-cn_image_0000002589246299.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=DD52ABEF14D40DE5C318A9C691E4E0F07074A752A39D0D0686334CE626DFD4FD)

### startImageAnalyzer12+

PhonePC/2in1TabletTVWearable

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

配置并启动AI分析功能，使用Promise异步回调。使用前需先设置[enableAnalyzer](ts-components-canvas-canvas.md#enableanalyzer12)为true，启用图像AI分析能力。

该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机，避免出现画面和分析内容不一致的情况。

未执行完重复调用该方法会触发错误回调。示例代码同stopImageAnalyzer。

说明

分析类型不支持动态修改。

当检测到画面有变化时，分析结果将自动销毁，可重新调用本接口启动分析。

该特性依赖设备能力，不支持该能力的情况下，将返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](ts-image-common.md#imageanalyzerconfig12) | 是 | 执行AI分析所需要的入参，用于配置AI分析功能。  异常值undefined或null按无效值处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[图像AI分析错误码](errorcode-image-analyzer.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |

### stopImageAnalyzer12+

PhonePC/2in1TabletTVWearable

stopImageAnalyzer(): void

停止AI分析功能，AI分析展示的内容将被销毁。

说明

在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。

该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct ImageAnalyzerExample {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true)
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
9. private config: ImageAnalyzerConfig = {
10. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
11. }
12. // 'common/images/example.png'需要替换为开发者所需的图像资源文件
13. private img = new ImageBitmap('common/images/example.png')
14. private aiController: ImageAnalyzerController = new ImageAnalyzerController()
15. private options: ImageAIOptions = {
16. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
17. aiController: this.aiController
18. }

20. build() {
21. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
22. Button('start')
23. .width(100)
24. .height(50)
25. .margin(5)
26. .onClick(() => {
27. this.context.startImageAnalyzer(this.config)
28. .then(() => {
29. console.info("analysis complete")
30. })
31. .catch((error: BusinessError) => {
32. let e: BusinessError = error as BusinessError
33. console.error(`Error code: ${e.code}, message: ${e.message}`)
34. })
35. })
36. Button('stop')
37. .width(100)
38. .height(50)
39. .margin(5)
40. .onClick(() => {
41. this.context.stopImageAnalyzer()
42. })
43. Button('getTypes')
44. .width(100)
45. .height(50)
46. .margin(5)
47. .onClick(() => {
48. this.aiController.getImageAnalyzerSupportTypes()
49. })
50. Canvas(this.context, this.options)
51. .width(200)
52. .height(200)
53. .enableAnalyzer(true)
54. .onReady(() => {
55. this.context.drawImage(this.img, 0, 0, 200, 200)
56. })
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/3qzMIriFTOWNS2Knf0xtEw/zh-cn_image_0000002558766492.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=EAF5092DE7939D692D8144B2E9415417FB690B9F4A61E5C00A95236E1E155D9B)

### getContext2DFromDrawingContext23+

PhonePC/2in1TabletTVWearable

static getContext2DFromDrawingContext(drawingContext: DrawingRenderingContext, options?: RenderingContextOptions): CanvasRenderingContext2D

从一个DrawingRenderingContext对象中获取一个CanvasRenderingContext2D对象，该CanvasRenderingContext2D对象与入参的DrawingRenderingContext对象绑定了相同的Canvas组件。

说明

* 从该接口获取的CanvasRenderingContext2D对象不允许作为参数创建[Canvas](ts-components-canvas-canvas.md)组件，否则会导致应用崩溃。
* 当入参的DrawingRenderingContext对象未绑定Canvas组件时，将返回错误码。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| drawingContext | [DrawingRenderingContext](ts-drawingrenderingcontext.md) | 是 | 一个DrawingRenderingContext类型的对象。 |
| options | [RenderingContextOptions](ts-canvasrenderingcontext2d.md#renderingcontextoptions23) | 否 | 渲染上下文的配置选项。  默认值：{ antialias: false } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| CanvasRenderingContext2D | 返回一个CanvasRenderingContext2D对象，其与入参的DrawingRenderingContext绑定了相同的Canvas组件。 |

**错误码：**

以下错误码的详细介绍请参见[Canvas组件错误码](errorcode-canvas.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 103702 | The drawingContext is not bound to a canvas component. |

**示例：**

```
1. // xxx.ets
2. import { LengthMetricsUnit } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CanvasExample {
7. build() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
9. Canvas({ unit: LengthMetricsUnit.DEFAULT })
10. .onReady((drawingContext?: DrawingRenderingContext) => {
11. if (!drawingContext) {
12. return
13. }
14. let context2D: CanvasRenderingContext2D =
15. CanvasRenderingContext2D.getContext2DFromDrawingContext(drawingContext, { antialias: true })
16. context2D.fillStyle = 'rgb(39,135,217)'
17. context2D.fillRect(10, 30, 100, 100)
18. })
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/xCHQTEC3QfmMhzPy37fMCA/zh-cn_image_0000002558606832.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=EABA1FA023259CB49D171A89835A3B4855A1E4C2737F050F45CC8D3D76CBE0EC)

## RenderingContextOptions23+

PhonePC/2in1TabletTVWearable

定义渲染上下文的具体配置参数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| antialias | boolean | 否 | 是 | 表明RenderingContext是否需要开启抗锯齿。  取值为undefined时按默认值处理。  true：开启抗锯齿；false：不开启抗锯齿。  默认值：false |

## CanvasDirection类型说明

PhonePC/2in1TabletTVWearable

type CanvasDirection = "inherit" | "ltr" | "rtl"

定义当前文本方向的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| inherit | 继承canvas组件通用属性已设定的文本方向，若canvas组件未设置direction属性，则跟随系统文字方向。 |
| ltr | 从左往右。 |
| rtl | 从右往左。 |

## CanvasFillRule类型说明

PhonePC/2in1TabletTVWearable

type CanvasFillRule = "evenodd" | "nonzero"

定义用于确定点是在路径内还是路径外的填充样式算法的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| evenodd | 奇偶规则。  此规则通过从画布上的某点向任意方向发射一条射线，并统计图形路径与射线的交点数量来判断该点是否在图形内部。如果交点数量是奇数，则该点在图形内部，否则在图形外部。 |
| nonzero | 非零规则。  此规则通过从画布上的某点向任意方向发射一条射线，并检查图形路径与射线的交点来判断该点是否在图形内部。初始计数为0，为路径的每一段线段指定一个方向值，每当路径从左向右穿过射线时加1，从右向左穿过时减1。如果最终的结果是0，则该点在图形外部，否则在图形内部。 |

**示例**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213, 213, 213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '60px sans-serif'
18. offContext.fillStyle = 'rgb(39, 135, 217)';
19. // 非零环绕规则 (nonzero)
20. offContext.beginPath();
21. offContext.arc(100, 100, 60, 0, Math.PI * 2);
22. offContext.arc(100, 100, 20, 0, Math.PI * 2);
23. offContext.fill('nonzero'); // 使用非零环绕规则
24. offContext.fillText('nonzero', 65, 200)
25. // 奇偶环绕规则 (evenodd)
26. offContext.beginPath();
27. offContext.arc(250, 100, 60, 0, Math.PI * 2);
28. offContext.arc(250, 100, 20, 0, Math.PI * 2);
29. offContext.fill('evenodd'); // 使用奇偶环绕规则
30. offContext.fillText('evenodd', 215, 200)
31. let image = this.offCanvas.transferToImageBitmap()
32. this.context.transferFromImageBitmap(image)
33. })
34. }
35. .width('100%')
36. .height('100%')
37. }
38. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/IMT4iQMXS46wCmrUk8qUjA/zh-cn_image_0000002589326359.png?HW-CC-KV=V1&HW-CC-Date=20260429T055223Z&HW-CC-Expire=86400&HW-CC-Sign=5E3EA294FCC37409CEB197A7E974344DD3C7163C9EFDDF5E601EA3E7FA48A7E7)

## CanvasLineCap类型说明

PhonePC/2in1TabletTVWearable

type CanvasLineCap = "butt" | "round" | "square"

定义绘制每条线段端点的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| butt | 线条两端为平行线，不额外扩展。 |
| round | 在线条两端延伸半个圆，直径等于线宽。 |
| square | 在线条两端延伸一个矩形，宽度等于线宽的一半，高度等于线宽。 |

## CanvasLineJoin类型说明

PhonePC/2in1TabletTVWearable

type CanvasLineJoin = "bevel" | "miter" | "round"

定义长度不为0的两个连接部分（线段、圆弧和曲线）的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| bevel | 在线段相连处使用三角形为底填充， 每个部分矩形拐角独立。 |
| miter | 在相连部分的外边缘处进行延伸，使其相交于一点，形成一个菱形区域，该属性可以通过设置miterLimit属性展现效果。 |
| round | 在线段相连处绘制一个扇形，扇形的圆角半径是线段的宽度。 |

## CanvasTextAlign类型说明

PhonePC/2in1TabletTVWearable

type CanvasTextAlign = "center" | "end" | "left" | "right" | "start"

定义文本对齐方式的类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| center | 文本居中对齐。 |
| start | 文本对齐界线开始的地方。 |
| end | 文本对齐界线结束的地方。 |
| left | 文本左对齐。 |
| right | 文本右对齐。 |

## CanvasTextBaseline类型说明

PhonePC/2in1TabletTVWearable

type CanvasTextBaseline = "alphabetic" | "bottom" | "hanging" | "ideographic" | "middle" | "top"

定义文本基线类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| alphabetic | 文本基线是标准的字母基线。 |
| bottom | 文本基线在文本块的底部。 与ideographic基线的区别在于ideographic基线不需要考虑下行字母。 |
| hanging | 文本基线是悬挂基线。 |
| ideographic | 文字基线是表意字基线；如果字符本身超出了alphabetic基线，那么ideographic基线位置在字符本身的底部。 |
| middle | 文本基线在文本块的中间。 |
| top | 文本基线在文本块的顶部。 |

## ImageSmoothingQuality类型说明

PhonePC/2in1TabletTVWearable

type ImageSmoothingQuality = "high" | "low" | "medium"

定义图片平滑度类型。取值类型为下表类型中的并集。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| low | 低画质 |
| medium | 中画质 |
| high | 高画质 |

## TextMetrics

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | 只读属性，文本方块的宽度。 |
| height | number | 是 | 否 | 只读属性，文本方块的高度。 |
| actualBoundingBoxAscent | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到渲染文本的矩形边界顶部的距离。 |
| actualBoundingBoxDescent | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到渲染文本的矩形边界底部的距离。 |
| actualBoundingBoxLeft | number | 是 | 否 | 只读属性，平行于基线，从[CanvasRenderingContext2D.textAlign](ts-canvasrenderingcontext2d.md#canvastextalign类型说明)属性确定的对齐点到文本矩形边界左侧的距离。 |
| actualBoundingBoxRight | number | 是 | 否 | 只读属性，平行于基线，从[CanvasRenderingContext2D.textAlign](ts-canvasrenderingcontext2d.md#canvastextalign类型说明)属性确定的对齐点到文本矩形边界右侧的距离。 |
| alphabeticBaseline | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到线框的 alphabetic 基线的距离。 |
| emHeightAscent | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到线框中 em 方块顶部的距离。 |
| emHeightDescent | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到线框中 em 方块底部的距离。 |
| fontBoundingBoxAscent | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到渲染文本的所有字体的矩形最高边界顶部的距离。 |
| fontBoundingBoxDescent | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到渲染文本的所有字体的矩形边界最底部的距离。 |
| hangingBaseline | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到线框的 hanging 基线的距离。 |
| ideographicBaseline | number | 是 | 否 | 只读属性，从[CanvasRenderingContext2D.textBaseline](ts-canvasrenderingcontext2d.md#canvastextbaseline类型说明)属性标明的水平线到线框的 ideographic 基线的距离。 |

## RenderingContextSettings

PhonePC/2in1TabletTVWearable

用来配置CanvasRenderingContext2D对象的参数，包括是否开启抗锯齿。

说明

RenderingContextSettings的抗锯齿效果对文本绘制无影响。

### constructor

PhonePC/2in1TabletTVWearable

constructor(antialias?: boolean)

构造CanvasRenderingContext2D对象，支持配置开启抗锯齿。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| antialias | boolean | 否 | 表明canvas是否开启抗锯齿。  异常值undefined按默认值处理。  false：表示不开启抗锯齿功能，true：表示开启抗锯齿。  默认值：false |

### 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| antialias | boolean | 否 | 是 | 表明canvas是否开启抗锯齿。  异常值undefined按默认值处理。  false：表示不开启抗锯齿功能，true：表示开启抗锯齿。  默认值：false |
