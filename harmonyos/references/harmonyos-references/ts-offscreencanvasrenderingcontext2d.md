---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d
title: OffscreenCanvasRenderingContext2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > OffscreenCanvasRenderingContext2D
category: harmonyos-references
scraped_at: 2026-04-28T08:02:11+08:00
doc_updated_at: 2026-04-13
content_hash: sha256:3d50ebfac3c9b77552bdc10a48c414f2b647a54ae0bad803c69914bdff8e90bc
---

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓存区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用，ServiceExtensionAbility中建议使用[Drawing模块](arkts-apis-graphics-drawing.md)进行离屏绘制。

[beginPath](ts-offscreencanvasrenderingcontext2d.md#beginpath)、[moveTo](ts-offscreencanvasrenderingcontext2d.md#moveto)、[lineTo](ts-offscreencanvasrenderingcontext2d.md#lineto)、[closePath](ts-offscreencanvasrenderingcontext2d.md#closepath)、[bezierCurveTo](ts-offscreencanvasrenderingcontext2d.md#beziercurveto)、[quadraticCurveTo](ts-offscreencanvasrenderingcontext2d.md#quadraticcurveto)、[arc](ts-offscreencanvasrenderingcontext2d.md#arc)、[arcTo](ts-offscreencanvasrenderingcontext2d.md#arcto)、[ellipse](ts-offscreencanvasrenderingcontext2d.md#ellipse)、[rect](ts-offscreencanvasrenderingcontext2d.md#rect)和[roundRect](ts-offscreencanvasrenderingcontext2d.md#roundrect20)接口只能对OffscreenCanvasRenderingContext2D中的路径生效，无法对[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)和[Path2D](ts-components-canvas-path2d.md)对象中设置的路径生效。

## 构造函数

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, settings?: RenderingContextSettings)

构造离屏Canvas画布对象，支持配置画布宽高和OffscreenCanvasRenderingContext2D对象的参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见RenderingContextSettings接口描述。  异常值undefined按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见RenderingContextSettings接口描述。  异常值undefined按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值undefined、NaN和Infinity按默认值处理。  默认值：DEFAULT |

## 属性

PhonePC/2in1TabletTVWearable

说明

fillStyle、shadowColor与 strokeStyle 中string类型格式为 'rgb(255, 255, 255)'，'rgba(255, 255, 255, 1.0)'，'#FFFFFF'。

### fillStyle

PhonePC/2in1TabletTVWearable

指定绘制的填充色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | number10+ | [CanvasGradient](ts-components-canvas-canvasgradient.md) | [CanvasPattern](ts-components-canvas-canvaspattern.md) | 否 | 否 | - 类型为string时，表示设置填充区域的颜色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中string类型说明。  - 类型为number时，表示设置填充区域的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中number类型说明。  - 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](ts-offscreencanvasrenderingcontext2d.md#createlineargradient)方法创建。  - 类型为CanvasPattern时，使用[createPattern](ts-offscreencanvasrenderingcontext2d.md#createpattern)方法创建。  默认值：'#000000'（黑色）  异常值设置无效。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 使用string设置fillStyle属性
18. offContext.fillStyle = '#0000ff'
19. offContext.fillRect(20, 20, 150, 100)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 使用number设置fillStyle属性
18. offContext.fillStyle = 0x0000FF
19. offContext.fillRect(20, 20, 150, 100)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/RTh39ZtgTiCsVn0AgiFCgQ/zh-cn_image_0000002552959976.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=8E613B179D95A94079D632ABE01079122E5444FE358A5DDE00527AF547EE1F26)

### lineWidth

PhonePC/2in1TabletTVWearable

设置绘制线条的宽度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：1（px）  默认单位：vp  lineWidth取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致和lineWidth属性相关的接口无法绘制。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineWidthExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 设置lineWidth属性
18. offContext.lineWidth = 5
19. offContext.strokeRect(25, 25, 85, 105)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/SgRi_Iw-Sh2SsJXx5P5Nlw/zh-cn_image_0000002583479977.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=33B0FD51740062ABDF6863811FFDEFAEC6609A7EA3F673EF31AF1183927E5F85)

### strokeStyle

PhonePC/2in1TabletTVWearable

设置线条的颜色，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | number10+ | [CanvasGradient](ts-components-canvas-canvasgradient.md) | [CanvasPattern](ts-components-canvas-canvaspattern.md) | 否 | 否 | - 类型为string时，表示设置线条使用的颜色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中string类型说明。  - 类型为number时，表示设置线条使用的颜色，不支持设置全透明色，颜色格式参考[ResourceColor](ts-types.md#resourcecolor)中number类型说明。  - 类型为CanvasGradient时，表示渐变对象，使用[createLinearGradient](ts-offscreencanvasrenderingcontext2d.md#createlineargradient)方法创建。  - 类型为CanvasPattern时，使用[createPattern](ts-offscreencanvasrenderingcontext2d.md#createpattern)方法创建。  默认值：'#000000'（黑色）  异常值设置无效。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 10
18. // 使用string设置strokeStyle属性
19. offContext.strokeStyle = '#0000ff'
20. offContext.strokeRect(25, 25, 155, 105)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeStyleExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 10
18. // 使用number设置strokeStyle属性
19. offContext.strokeStyle = 0x0000ff
20. offContext.strokeRect(25, 25, 155, 105)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/aC1GfBkRTT2BGMdQr_6XUg/zh-cn_image_0000002552800328.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=843CBB1605C43DF47413C431C2DA5D850CB71CAA02BDC60ADA474F5D5DF39EC7)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 8
18. offContext.beginPath()
19. // 设置lineCap属性
20. offContext.lineCap = 'round'
21. offContext.moveTo(30, 50)
22. offContext.lineTo(220, 50)
23. offContext.stroke()
24. let image = this.offCanvas.transferToImageBitmap()
25. this.context.transferFromImageBitmap(image)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/pVLCsO3aRVS4G0rYhXolIQ/zh-cn_image_0000002583440023.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=8EA88219AA4EC98D5426C6A4A528C9326E065B521F19E43374A330984FCE8FE8)

### lineJoin

PhonePC/2in1TabletTVWearable

指定线段间相交的交点样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| [CanvasLineJoin](ts-canvasrenderingcontext2d.md#canvaslinejoin类型说明) | 否 | 否 | 默认值：'miter' |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineJoinExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.lineWidth = 8
19. // 设置lineJoin属性
20. offContext.lineJoin = 'miter'
21. offContext.moveTo(30, 30)
22. offContext.lineTo(120, 60)
23. offContext.lineTo(30, 110)
24. offContext.stroke()
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/W5YZZTKpS82yoEG2NxkSQg/zh-cn_image_0000002552959978.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=C9C782CC62D6A0EF96EEF47DA2486E11EC98798F6805FFDB45451A2FCE4A8C20)

### miterLimit

PhonePC/2in1TabletTVWearable

设置斜接面限制值，该值指定了线条相交处内角和外角的距离，仅当设置了lineJoin为miter才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：10px  单位：px  miterLimit取值不支持0和负数，0、负数和NaN按默认值处理，Infinity会导致和miterLimit属性相关的接口无法绘制。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MiterLimit {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 8
18. offContext.lineJoin = 'miter'
19. // 设置miterLimit属性
20. offContext.miterLimit = 3
21. offContext.moveTo(30, 30)
22. offContext.lineTo(60, 35)
23. offContext.lineTo(30, 37)
24. offContext.stroke()
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/SArEZMCtQDWpQPOuZgzhRg/zh-cn_image_0000002583479979.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=DAB3E34CF1031AA5EBD4B62F7BD8F0920104252630FC78A69617FAB4B6F8D3C7)

### font

PhonePC/2in1TabletTVWearable

设置文本绘制中的字体样式，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

语法：ctx.font = 'font-style font-weight font-size font-family'

- font-style(可选)，用于指定字体样式，支持如下几种样式：'normal','italic'。

- font-weight(可选)，用于指定字体的粗细，支持如下几种类型：'normal', 'bold', 'bolder', 'lighter', 100, 200, 300, 400, 500, 600, 700, 800, 900。

- font-size(可选)，指定字号和行高，单位支持px、vp。使用时需要添加单位。

- font-family(可选)，指定字体系列，支持如下几种类型：'sans-serif', 'serif', 'monospace'。

从API version 20开始，支持通过该接口设置注册过的自定义字体（只能在主线程使用，不支持在worker线程中使用；DevEco Studio的预览器不支持显示自定义字体）。自定义字体注册有以下两种方式。一种是通过ArkUI的异步接口this.uiContext.getFont().[registerFont](arkts-apis-uicontext-font.md#registerfont)注册，调用后立即绘制可能会导致自定义字体不生效。另一种是直接调用字体引擎的fontCollection.[loadFontSync](js-apis-graphics-text.md#loadfontsync)接口来注册自定义字体到字体引擎。在直接调用字体引擎接口注册自定义字体时，fontCollection的实例需要是text.FontCollection.getGlobalInstance()，因为组件默认会从该实例加载字体。如果使用其他实例，可能会导致自定义字体不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| string | 否 | 否 | 默认值：'normal normal 14px sans-serif' |

```
1. import { text } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct FontDemo {
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('rgb(213,213,213)')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext("2d", this.settings);
18. // 常规字体样式，常规粗细，字体大小为30px，字体系列为sans-serif
19. offContext.font = 'normal normal 30px sans-serif'
20. offContext.fillText("Hello px", 20, 60)
21. // 斜体样式，加粗，字体大小为30vp，字体系列为monospace
22. offContext.font = 'italic bold 30vp monospace'
23. offContext.fillText("Hello vp", 20, 100)
24. // 加载rawfile目录下的自定义字体文件HarmonyOS_Sans_Thin_Italic.ttf
25. let fontCollection = text.FontCollection.getGlobalInstance();
26. fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
27. // 加粗，字体大小为30vp，字体系列为HarmonyOS_Sans_Thin_Italic
28. offContext.font = "bold 30vp HarmonyOS_Sans_Thin_Italic"
29. offContext.fillText("Hello customFont", 20, 140)
30. let image = this.offCanvas.transferToImageBitmap();
31. this.context.transferFromImageBitmap(image)
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/ZW_AYWHCQCeHhj4Vgz8xDQ/zh-cn_image_0000002552800330.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=E25A4FFD39E4EC4CDEBC20E607948FDF604B80A3F36DA466E06FC13C136FAD92)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.strokeStyle = 'rgb(39,135,217)'
18. offContext.moveTo(140, 10)
19. offContext.lineTo(140, 160)
20. offContext.stroke()

22. offContext.font = '50px sans-serif'

24. // 设置textAlign属性为start
25. offContext.textAlign = 'start'
26. offContext.fillText('textAlign=start', 140, 60)
27. // 设置textAlign属性为end
28. offContext.textAlign = 'end'
29. offContext.fillText('textAlign=end', 140, 80)
30. // 设置textAlign属性为left
31. offContext.textAlign = 'left'
32. offContext.fillText('textAlign=left', 140, 100)
33. // 设置textAlign属性为center
34. offContext.textAlign = 'center'
35. offContext.fillText('textAlign=center', 140, 120)
36. // 设置textAlign属性为right
37. offContext.textAlign = 'right'
38. offContext.fillText('textAlign=right', 140, 140)
39. let image = this.offCanvas.transferToImageBitmap()
40. this.context.transferFromImageBitmap(image)
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/ja6VTKLgS3KjBn4TgsTrGQ/zh-cn_image_0000002583440025.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A3DBB8758FAE6923C4E1D8E4B8F65065BDC7AF7356E2B3275F06259206CBAF22)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.strokeStyle = '#0000ff'
18. offContext.moveTo(0, 120)
19. offContext.lineTo(400, 120)
20. offContext.stroke()

22. offContext.font = '20px sans-serif'

24. // 设置textBaseline属性为top
25. offContext.textBaseline = 'top'
26. offContext.fillText('Top', 10, 120)
27. // 设置textBaseline属性为bottom
28. offContext.textBaseline = 'bottom'
29. offContext.fillText('Bottom', 55, 120)
30. // 设置textBaseline属性为middle
31. offContext.textBaseline = 'middle'
32. offContext.fillText('Middle', 125, 120)
33. // 设置textBaseline属性为alphabetic
34. offContext.textBaseline = 'alphabetic'
35. offContext.fillText('Alphabetic', 195, 120)
36. // 设置textBaseline属性为hanging
37. offContext.textBaseline = 'hanging'
38. offContext.fillText('Hanging', 295, 120)
39. let image = this.offCanvas.transferToImageBitmap()
40. this.context.transferFromImageBitmap(image)
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/f-O2N2CgRGWgh_tQax74yw/zh-cn_image_0000002583439979.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=3B6A843D0EE751C9809437C5BA2B261D099A7C1100D75090F5AD7E308042C871)

### globalAlpha

PhonePC/2in1TabletTVWearable

设置透明度，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 范围为[0.0, 1.0]，0.0为完全透明，1.0为完全不透明。若给定值小于0.0，则取值0.0；若给定值大于1.0，则取值1.0。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制。API version 18及以后，设置NaN或Infinity时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认值：1.0 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct GlobalAlpha {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(0,0,255)'
18. offContext.fillRect(0, 0, 50, 50)
19. // 设置globalAlpha属性
20. offContext.globalAlpha = 0.4
21. offContext.fillStyle = 'rgb(0,0,255)'
22. offContext.fillRect(50, 50, 50, 50)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/CkAALmXySfuMj5KS8fCVdQ/zh-cn_image_0000002552959980.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A88173CB6328BE51FA17E9151D70B2A872AC7515D5C6C88F8E15AD1516E1D74D)

### lineDashOffset

PhonePC/2in1TabletTVWearable

设置画布的虚线偏移量，精度为float，仅当设置setLineDash时属性才生效，此属性为只写属性，可通过赋值语句设置其值，但无法通过读取操作获取其当前值，若尝试读取将返回undefined。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- |
| number | 否 | 否 | 默认值：0.0  单位：vp  异常值NaN和Infinity按默认值处理。 |

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineDashOffset {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.arc(100, 75, 50, 0, 6.28)
18. offContext.setLineDash([10, 20])
19. // 设置lineDashOffset属性
20. offContext.lineDashOffset = 10.0
21. offContext.stroke()
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/hGLje4GyQsaZepsL-0JtZA/zh-cn_image_0000002583479981.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=EF93C70605C64DAA6A48D64B8483DC1E5C51153093BC8F8B2F42D881BF2970D4)

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
23. let offContext = new OffscreenCanvasRenderingContext2D(ctx1.width, ctx1.height, this.settings);
24. offContext.fillStyle = 'rgb(39,135,217)';
25. offContext.fillRect(25, 25, 75, 75); // 原有图形
26. offContext.globalCompositeOperation = 'source-over'; // 默认值，可省略
27. offContext.fillStyle = 'rgb(23,169,141)';
28. offContext.fillRect(75, 75, 75, 75); // 新图形覆盖
29. let image = offContext.transferToImageBitmap();
30. this.context1.transferFromImageBitmap(image);
31. })
32. // 2. destination-out：新图形擦除原有图形（橡皮擦核心逻辑）
33. Canvas(this.context2)
34. .width('45%')
35. .borderWidth(1)
36. .margin(5)
37. .onReady(() => {
38. let ctx2 = this.context2;
39. let offContext = new OffscreenCanvasRenderingContext2D(ctx2.width, ctx2.height, this.settings);
40. // 先绘制背景
41. offContext.fillStyle = 'rgb(39,135,217)';
42. offContext.fillRect(0, 0, ctx2.width, ctx2.height);
43. // 设置合成模式为擦除
44. offContext.globalCompositeOperation = 'destination-out';
45. // 绘制圆形作为橡皮擦
46. offContext.beginPath();
47. offContext.arc(ctx2.width / 2, ctx2.height / 2, 60, 0, Math.PI * 2);
48. offContext.fill(); // 擦除圆形区域的背景
49. let image = offContext.transferToImageBitmap();
50. this.context2.transferFromImageBitmap(image);
51. })
52. }
53. .height('30%')

55. Row() {
56. // 3. source-in：仅保留新图形与原有图形重叠的部分（裁剪或蒙版）
57. Canvas(this.context3)
58. .width('45%')
59. .borderWidth(1)
60. .margin(5)
61. .onReady(() => {
62. let ctx3 = this.context3;
63. let offContext = new OffscreenCanvasRenderingContext2D(ctx3.width, ctx3.height, this.settings);
64. // 先绘制原有图形（圆形蒙版）
65. offContext.beginPath();
66. offContext.arc(ctx3.width / 2, ctx3.height / 2, 80, 0, Math.PI * 2);
67. offContext.fillStyle = '#fff';
68. offContext.fill();
69. // 设置合成模式
70. offContext.globalCompositeOperation = 'source-in';
71. // 绘制新图形（渐变矩形）
72. const gradient = offContext.createLinearGradient(0, 0, ctx3.width, ctx3.height);
73. gradient.addColorStop(0, 'rgb(23,169,141)');
74. gradient.addColorStop(1, 'rgb(39,135,217)');
75. offContext.fillStyle = gradient;
76. offContext.fillRect(0, 0, 200, 200); // 仅圆形区域显示渐变
77. let image = offContext.transferToImageBitmap();
78. this.context3.transferFromImageBitmap(image);
79. })
80. // 4. lighter：新图形与原有图形叠加（亮度相加，滤色效果）
81. Canvas(this.context4)
82. .width('45%')
83. .borderWidth(1)
84. .margin(5)
85. .onReady(() => {
86. let ctx4 = this.context4;
87. let offContext = new OffscreenCanvasRenderingContext2D(ctx4.width, ctx4.height, this.settings);
88. // 原有图形（半透明红色圆）
89. offContext.beginPath();
90. offContext.arc(70, 100, 50, 0, Math.PI * 2);
91. offContext.fillStyle = 'rgba(234, 67, 53, 0.7)';
92. offContext.fill();
93. // 设置合成模式
94. offContext.globalCompositeOperation = 'lighter';
95. // 新图形（半透明蓝色圆）
96. offContext.beginPath();
97. offContext.arc(110, 100, 50, 0, Math.PI * 2);
98. offContext.fillStyle = 'rgba(66, 133, 244, 0.7)';
99. offContext.fill(); // 重叠区域变成紫色（亮度叠加）
100. let image = offContext.transferToImageBitmap();
101. this.context4.transferFromImageBitmap(image);
102. })
103. }
104. .height('30%')

106. Row() {
107. // 5. destination-atop：保留原有图形与新图形重叠的部分，移除其他区域
108. Canvas(this.context5)
109. .width('45%')
110. .borderWidth(1)
111. .margin(5)
112. .onReady(() => {
113. let ctx5 = this.context5;
114. let offContext = new OffscreenCanvasRenderingContext2D(ctx5.width, ctx5.height, this.settings);
115. // 原有图形（绿色矩形）
116. offContext.fillStyle = 'rgb(23,169,141)';
117. offContext.fillRect(0, 0, ctx5.width, ctx5.height);
118. // 设置合成模式
119. offContext.globalCompositeOperation = 'destination-atop';
120. // 新图形（小圆形）
121. offContext.beginPath();
122. offContext.arc(ctx5.width / 2, ctx5.height / 2, 60, 0, Math.PI * 2);
123. offContext.fillStyle = '#000';
124. offContext.fill(); // 仅矩形与圆形重叠的部分保留
125. let image = offContext.transferToImageBitmap();
126. this.context5.transferFromImageBitmap(image);
127. })
128. // 6. 文字蒙版（“source-in”的高级用法）
129. Canvas(this.context6)
130. .width('45%')
131. .borderWidth(1)
132. .margin(5)
133. .onReady(() => {
134. let ctx6 = this.context6;
135. let offContext = new OffscreenCanvasRenderingContext2D(ctx6.width, ctx6.height, this.settings);
136. // 先绘制文字（作为蒙版）
137. offContext.font = 'bold 40vp';
138. offContext.textAlign = 'center';
139. offContext.textBaseline = 'middle';
140. offContext.fillText('CANVAS', ctx6.width / 2, ctx6.height / 2);
141. // 设置合成模式
142. offContext.globalCompositeOperation = 'source-in';
143. // 绘制渐变背景（仅文字区域显示）
144. let textGradient = offContext.createLinearGradient(50, 0, 300, 100);
145. textGradient.addColorStop(0.0, 'rgb(39,135,217)');
146. textGradient.addColorStop(0.5, 'rgb(255,238,240)');
147. textGradient.addColorStop(1.0, 'rgb(23,169,141)');
148. offContext.fillStyle = textGradient;
149. offContext.fillRect(0, 0, 200, 200); // 渐变仅填充文字区域
150. let image = offContext.transferToImageBitmap();
151. this.context6.transferFromImageBitmap(image);
152. })
153. }
154. .height('30%')
155. }
156. .width('100%')
157. .height('100%')
158. }
159. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/SZ7SHlSgRzSyr-Mrerr0mA/zh-cn_image_0000002552800332.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A6B3B243B9FA3936561D3664A884E4C2BDF4E9320F5E7BD603C1CE5A7515E881)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. // 设置shadowBlur属性
18. offContext.shadowBlur = 30
19. offContext.shadowColor = 'rgb(0,0,0)'
20. offContext.fillStyle = 'rgb(39,135,217)'
21. offContext.fillRect(20, 20, 100, 80)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/35C4r_2lTEq1CfJGCa7j3Q/zh-cn_image_0000002583440027.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=7108A9C46A58FBD7DC9A9101364848FA98472C199266C3054A34DD9CF12AC9DF)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.shadowBlur = 30
18. // 设置shadowColor属性
19. offContext.shadowColor = 'rgb(255,192,0)'
20. offContext.fillStyle = 'rgb(39,135,217)'
21. offContext.fillRect(30, 30, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/1lcjuv5WSDiE0Hb9F7-rPQ/zh-cn_image_0000002552959982.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=BA7651B7C8C5A3BDF703F68017173174F1B6066896E905C836893E64D9183993)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.shadowBlur = 10
18. // 设置shadowOffsetX属性
19. offContext.shadowOffsetX = 20
20. offContext.shadowColor = 'rgb(0,0,0)'
21. offContext.fillStyle = 'rgb(255,0,0)'
22. offContext.fillRect(20, 20, 100, 80)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/shmfppxeRiKr-muDhFY8Dg/zh-cn_image_0000002583479983.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=0CCDC0BAFB49F89B84F157A72BB15DD3616497221FBE60F1239614F05EE203D0)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.shadowBlur = 10
18. // 设置shadowOffsetY属性
19. offContext.shadowOffsetY = 20
20. offContext.shadowColor = 'rgb(0,0,0)'
21. offContext.fillStyle = 'rgb(255,0,0)'
22. offContext.fillRect(30, 30, 100, 100)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/_UWmi7E0S-GsF8yQWc42qw/zh-cn_image_0000002552800334.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=CE49400424C8F0724D1E12BF211FED9366F45C68977FFF5530B6A8199A53037E)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/icon.jpg"需要替换为开发者所需的图像资源文件
8. private img:ImageBitmap = new ImageBitmap("common/images/icon.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. // 设置imageSmoothingEnabled属性
20. offContext.imageSmoothingEnabled = false
21. offContext.drawImage(this.img, 0, 0, 400, 200)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/BnbGyw_mQ3emZrb_pCLaLg/zh-cn_image_0000002583440029.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=85142288356B6F01253EE07527F42AA0DEF610ADEA7399C78F8FDF9CA457983C)

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
4. struct ImageSmoothingQualityDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.
7. settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
9. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
10. private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");

12. build() {
13. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,
14. justifyContent: FlexAlign.Center }) {
15. Canvas(this.context)
16. .width('100%')
17. .height('100%')
18. .backgroundColor('#ffff00')
19. .onReady(() => {
20. let offContext = this.offCanvas.getContext("2d", this.settings)
21. let offctx = offContext
22. offctx.imageSmoothingEnabled = true
23. // 设置imageSmoothingQuality属性
24. offctx.imageSmoothingQuality = 'high'
25. offctx.drawImage(this.img, 0, 0, 400, 200)

27. let image = this.offCanvas.transferToImageBitmap()
28. this.context.transferFromImageBitmap(image)
29. })
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/cvFtyJBITZGRw2JSJbnlbw/zh-cn_image_0000002583439985.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=07DE224C8485094EB76D13C230B2BF94722E8CC8B581AEFFF81401AAE8520E35)

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
4. struct DirectionDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.
7. settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center,
12. justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. let offctx = offContext
20. offctx.font = '48px serif';
21. offctx.textAlign = 'start'
22. offctx.fillText("Hi ltr!", 200, 50);

24. // 设置direction属性
25. offctx.direction = "rtl";
26. offctx.fillText("Hi rtl!", 200, 100);

28. let image = offctx.transferToImageBitmap()
29. this.context.transferFromImageBitmap(image)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/0ZTjsj9sQpeFf69RCbNLsw/zh-cn_image_0000002552959940.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=3E9D5FD4EBC59EC921987E9B249F239217BCBA41E19CB4DD1FC810BDE83748B6)

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
4. struct FilterDemoOff {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
9. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext("2d", this.settings)
18. let img = this.img

20. offContext.drawImage(img, 0, 0, 100, 100);

22. offContext.filter = 'grayscale(50%)';
23. offContext.drawImage(img, 100, 0, 100, 100);

25. offContext.filter = 'sepia(60%)';
26. offContext.drawImage(img, 200, 0, 100, 100);

28. offContext.filter = 'saturate(30%)';
29. offContext.drawImage(img, 0, 100, 100, 100);

31. offContext.filter = 'hue-rotate(90deg)';
32. offContext.drawImage(img, 100, 100, 100, 100);

34. offContext.filter = 'invert(100%)';
35. offContext.drawImage(img, 200, 100, 100, 100);

37. offContext.filter = 'opacity(25%)';
38. offContext.drawImage(img, 0, 200, 100, 100);

40. offContext.filter = 'brightness(0.4)';
41. offContext.drawImage(img, 100, 200, 100, 100);

43. offContext.filter = 'contrast(200%)';
44. offContext.drawImage(img, 200, 200, 100, 100);

46. offContext.filter = 'blur(5px)';
47. offContext.drawImage(img, 0, 300, 100, 100);

49. // Applying multiple filters
50. offContext.filter = 'opacity(50%) contrast(200%) grayscale(50%)';
51. offContext.drawImage(img, 100, 300, 100, 100);

53. let image = this.offCanvas.transferToImageBitmap()
54. this.context.transferFromImageBitmap(image)
55. })
56. }
57. .width('100%')
58. .height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/j62qwfHyReG68SF2TvyJvg/zh-cn_image_0000002583479941.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=EEB8FCB90BE6F9A9C62E0FFD9C99971EC177766FBA3A9D59799CCC4C45D234A7)

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
2. import { LengthMetrics, LengthUnit } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct letterSpacingDemo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true);
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('rgb(213,213,213)')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.font = '30vp'
20. // 使用string设置direction属性
21. offContext.letterSpacing = '10vp'
22. offContext.fillText('hello world', 30, 50)
23. // 使用LengthMetrics对象设置direction属性
24. offContext.letterSpacing = new LengthMetrics(10, LengthUnit.VP)
25. offContext.fillText('hello world', 30, 100)
26. let image = this.offCanvas.transferToImageBitmap()
27. this.context.transferFromImageBitmap(image)
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Ij4aRcjaR0q247cIfBOnrQ/zh-cn_image_0000002552800292.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=C7052C32529E583B4BDDB163026FC5015621A1306B05087A55FBD9FCF4EDB392)

## 方法

PhonePC/2in1TabletTVWearable

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillRect(30, 30, 100, 100)
18. let image = this.offCanvas.transferToImageBitmap()
19. this.context.transferFromImageBitmap(image)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/I57V0hF3Sregqbww8Wns_Q/zh-cn_image_0000002583439987.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=8B2EF6655B7C4A782B395E4D0703FD3F90E036FBE38BB4806D4DFE8708C666AF)

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
| width | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| height | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StrokeRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.strokeRect(30, 30, 200, 150)
18. let image = this.offCanvas.transferToImageBitmap()
19. this.context.transferFromImageBitmap(image)
20. })
21. }
22. .width('100%')
23. .height('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/rq13yV-uQNG8J-__NbIdIQ/zh-cn_image_0000002552959942.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=BE798E1626D15C31B2852AA6B520916D903ADF29AB5CC81765805424EB760980)

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
| width | number | 是 | 指定矩形的宽度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |
| height | number | 是 | 指定矩形的高度。  异常值undefined、null、NaN或Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClearRect {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(0,0,255)'
18. offContext.fillRect(20, 20, 200, 200)
19. offContext.clearRect(30, 30, 150, 100)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/3HzNjkq-RxW65MKD3q0P4A/zh-cn_image_0000002583479943.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=4E46D6BF9DD58DCEA1DC128315C293250DBB16599C27F4BCA160C3A631F8C7C3)

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
| maxWidth | number | 否 | 指定文本允许的最大宽度。  异常值null按无效值处理，不进行绘制，undefined、NaN或Infinity按默认值处理。  默认单位：vp  默认值：不限制宽度。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct FillText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '30px sans-serif'
18. offContext.fillText("Hello World!", 20, 100)
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/TMRRt89XSteSVKNl2VX3Fg/zh-cn_image_0000002552800294.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A09998662179B1C8F0D651FDA6AB09B2A03F0D1E62E35FE5D6E0473012EB73E4)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '55px sans-serif'
18. offContext.strokeText("Hello World!", 20, 60)
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/Yxz54tUpSHarpcbaCb03JQ/zh-cn_image_0000002552959984.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=2D729058A462B604E4E990733627C3147C5959CB22B2C3AF4F0E4AB479289CFE)

### measureText

PhonePC/2in1TabletTVWearable

measureText(text: string): TextMetrics

该方法返回一个文本测算的对象，通过该对象可以获取指定文本的宽度值。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 需要进行测量的文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [TextMetrics](ts-canvasrenderingcontext2d.md#textmetrics) | 文本的尺寸信息。  传入异常值undefined或null时按"undefined"或"null"计算。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MeasureText {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.font = '50px sans-serif'
18. offContext.fillText("Hello World!", 20, 100)
19. offContext.fillText("width:" + offContext.measureText("Hello World!").width, 20, 200)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/K9WUmCc3TJSep6TbXu3Oog/zh-cn_image_0000002583479985.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=298EF8D636DF939527887466078F17DBBBD8B5D287E872D4B5C896D81B389CA4)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.moveTo(125, 25)
18. offContext.lineTo(125, 105)
19. offContext.lineTo(175, 105)
20. offContext.lineTo(175, 25)
21. offContext.strokeStyle = 'rgb(255,0,0)'
22. offContext.stroke()
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/oXqH_KgBRPWk6jy4KjR3tA/zh-cn_image_0000002552800336.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=2A2498A0E2AA381BE7FE6AE90CEA6206A1A41827D2E9A1EC8B561339055FD799)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. private path2Da: Path2D = new Path2D();

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. let offContext = this.offCanvas.getContext("2d", this.settings)
18. this.path2Da.moveTo(25, 25)
19. this.path2Da.lineTo(25, 105)
20. this.path2Da.lineTo(75, 105)
21. this.path2Da.lineTo(75, 25)
22. offContext.strokeStyle = 'rgb(0,0,255)'
23. offContext.stroke(this.path2Da)
24. let image = this.offCanvas.transferToImageBitmap()
25. this.context.transferFromImageBitmap(image)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/ELBYMZyeTiSFHAjDXfGaTw/zh-cn_image_0000002583440031.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=688C92DAB65CE7046CA6ED607033C203BE7E0743161776E31CC81B0397BD697E)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.lineWidth = 6
19. offContext.strokeStyle = '#0000ff'
20. offContext.moveTo(15, 80)
21. offContext.lineTo(280, 160)
22. offContext.stroke()
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/xa29iHy_RxezLt9OxquJNQ/zh-cn_image_0000002552959986.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=D8AFD56C5298F4125FEAC19889A617A16F373BC877EF105760559436D411756A)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.moveTo(10, 10)
19. offContext.lineTo(280, 160)
20. offContext.stroke()
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/IpnfxU5FQMqkEZNlVqgJ2g/zh-cn_image_0000002583479987.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A339B5A21B14ABAFF644D18C3421F37717DD42B0CED623B383CCB4EB05D16A10)

### lineTo

PhonePC/2in1TabletTVWearable

lineTo(x: number, y: number): void

从当前点到指定点进行路径连接。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| x | number | 是 | 指定位置的x坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |
| y | number | 是 | 指定位置的y坐标。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LineTo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.moveTo(10, 10)
19. offContext.lineTo(280, 160)
20. offContext.stroke()
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/fwpS4qJwQpqGBbe_NOJ6Qg/zh-cn_image_0000002552800338.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=245FD24612239B7F686C44FABF226F23DBFF5512940B0CF8387FF60E8A6A9962)

### closePath

PhonePC/2in1TabletTVWearable

closePath(): void

结束当前路径形成一个封闭路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ClosePath {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.moveTo(30, 30)
19. offContext.lineTo(110, 30)
20. offContext.lineTo(70, 90)
21. offContext.closePath()
22. offContext.stroke()
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/r5Y8bS7_RT6pI0gvBMcNog/zh-cn_image_0000002583440033.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=FCF7CE8816C15ED3ECBF50A5D0379671191728437E545ABC2F63B60B6898A6B0)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img:ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('rgb(213,213,213)')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. let pattern = offContext.createPattern(this.img, 'repeat')
20. offContext.fillStyle = pattern as CanvasPattern
21. offContext.fillRect(0, 0, 200, 200)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/JRQt7tj6Rsis3s-9_I_20w/zh-cn_image_0000002552959988.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=DC9695C629EDE52792114FDAEAB028BEAAACED08168FA6791BB5FC0E1702CFDC)

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
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
10. private start: Point = { x: 50, y: 50 };
11. private end: Point = { x: 250, y: 100 };
12. private cp1: Point = { x: 200, y: 30 };
13. private cp2: Point = { x: 130, y: 80 };

15. build() {
16. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
17. Canvas(this.context)
18. .width('100%')
19. .height('100%')
20. .backgroundColor('rgb(213,213,213)')
21. .onReady(() => {
22. let offContext = this.offCanvas.getContext("2d", this.settings)
23. // 三次贝塞尔曲线
24. offContext.beginPath();
25. offContext.moveTo(this.start.x, this.start.y);
26. offContext.bezierCurveTo(this.cp1.x, this.cp1.y, this.cp2.x, this.cp2.y, this.end.x, this.end.y);
27. offContext.stroke();

29. // 起点和终点
30. offContext.fillStyle = 'rgb(39,135,217)';
31. offContext.beginPath();
32. offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起点
33. offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 终点
34. offContext.fill();

36. // 控制点
37. offContext.fillStyle = 'rgb(23,169,141)';
38. offContext.beginPath();
39. offContext.arc(this.cp1.x, this.cp1.y, 5, 0, 2 * Math.PI); // 控制点一
40. offContext.arc(this.cp2.x, this.cp2.y, 5, 0, 2 * Math.PI); // 控制点二
41. offContext.fill();
42. let image = this.offCanvas.transferToImageBitmap();
43. this.context.transferFromImageBitmap(image);
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/3Y4Pt-2MQ1GjT-xxuC5D5g/zh-cn_image_0000002583479989.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=F46B5DEA0B07324FAA7E648F21969D53926C227CEDAFBB715DA2312D51ED720F)

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
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
10. private start: Point = { x: 50, y: 20 };
11. private end: Point = { x: 50, y: 100 };
12. private cp: Point = { x: 230, y: 30 };

14. build() {
15. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
16. Canvas(this.context)
17. .width('100%')
18. .height('100%')
19. .backgroundColor('rgb(213,213,213)')
20. .onReady(() => {
21. let offContext = this.offCanvas.getContext("2d", this.settings);
22. // 二次贝塞尔曲线
23. offContext.beginPath();
24. offContext.moveTo(this.start.x, this.start.y);
25. offContext.quadraticCurveTo(this.cp.x, this.cp.y, this.end.x, this.end.y);
26. offContext.stroke();

28. // 起始点和结束点
29. offContext.fillStyle = 'rgb(39,135,217)';
30. offContext.beginPath();
31. offContext.arc(this.start.x, this.start.y, 5, 0, 2 * Math.PI); // 起始点
32. offContext.arc(this.end.x, this.end.y, 5, 0, 2 * Math.PI); // 结束点
33. offContext.fill();

35. // 控制点
36. offContext.fillStyle = 'rgb(23,169,141)';
37. offContext.beginPath();
38. offContext.arc(this.cp.x, this.cp.y, 5, 0, 2 * Math.PI);
39. offContext.fill();

41. let image = this.offCanvas.transferToImageBitmap();
42. this.context.transferFromImageBitmap(image);
43. })
44. }
45. .width('100%')
46. .height('100%')
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/TGSVok3DSLu0E8R-E_jcVA/zh-cn_image_0000002552800340.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=6832DE3786575A40F6807AA7778C4CCFC1492AE5623B78EB2DBB14C13E516308)

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
| startAngle | number | 是 | 弧线的起始弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：弧度 |
| endAngle | number | 是 | 弧线的终止弧度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  默认单位：弧度 |
| counterclockwise | boolean | 否 | 是否逆时针绘制圆弧。  true：逆时针绘制圆弧；false：顺时针绘制圆弧。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Arc {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.beginPath()
18. offContext.arc(100, 75, 50, 0, 6.28)
19. offContext.stroke()
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/eJIXaYs4TRqhJdGiWbdhcw/zh-cn_image_0000002583440035.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=16385D88469D23A4A98CC54047FCEF0ED9EE467A00C976056CAADD8C65BDBA71)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)

18. // 切线
19. offContext.beginPath()
20. offContext.strokeStyle = '#808080'
21. offContext.lineWidth = 1.5;
22. offContext.moveTo(360, 20);
23. offContext.lineTo(360, 170);
24. offContext.lineTo(110, 170);
25. offContext.stroke();

27. // 圆弧
28. offContext.beginPath()
29. offContext.strokeStyle = '#000000'
30. offContext.lineWidth = 3;
31. offContext.moveTo(360, 20)
32. offContext.arcTo(360, 170, 110, 170, 150)
33. offContext.stroke()

35. // 起始点
36. offContext.beginPath();
37. offContext.fillStyle = '#00ff00';
38. offContext.arc(360, 20, 4, 0, 2 * Math.PI);
39. offContext.fill();

41. // 控制点
42. offContext.beginPath();
43. offContext.fillStyle = '#ff0000';
44. offContext.arc(360, 170, 4, 0, 2 * Math.PI);
45. offContext.arc(110, 170, 4, 0, 2 * Math.PI);
46. offContext.fill();

48. let image = this.offCanvas.transferToImageBitmap()
49. this.context.transferFromImageBitmap(image)
50. })
51. }
52. .width('100%')
53. .height('100%')
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/hyiRD0_cRN6kgoLuWqf3CA/zh-cn_image_0000002552959990.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=FC3D2EAE600A8C5116358F757F7F801314CB42770E64F018F5C78D09946BD434)

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
| rotation | number | 是 | 椭圆的旋转角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位为弧度。 |
| startAngle | number | 是 | 椭圆绘制的起始点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位为弧度。 |
| endAngle | number | 是 | 椭圆绘制的结束点角度。  API version 18之前，设置NaN或Infinity时，整条路径不显示；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的路径方法正常绘制。  单位为弧度。 |
| counterclockwise | boolean | 否 | 是否以逆时针方向绘制椭圆。  true：逆时针方向绘制椭圆。  false：顺时针方向绘制椭圆。  默认值：false，设置null或undefined按默认值处理。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. let offContext = this.offCanvas.getContext("2d", this.settings)
16. offContext.beginPath()
17. offContext.ellipse(200, 200, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, false)
18. offContext.stroke()
19. offContext.beginPath()
20. offContext.ellipse(200, 300, 50, 100, Math.PI * 0.25, Math.PI * 0.5, Math.PI * 2, true)
21. offContext.stroke()
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/1ECezGC-TRmYF89LGsPCVg/zh-cn_image_0000002552959950.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=77411D9F398596B18E94DAC57E4052CA70F30B9A69B19B590C9D550B8BDF4E46)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
18. offContext.stroke()
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/jWEWxSYiQbOyuvDrC7srlA/zh-cn_image_0000002583479991.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=96C0F77807F9D9F3D981E81D0C789AE1834D9D2C2D75F5771D7EEC8B5CE76343)

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
| radii | number | Array<number> | 否 | 指定用于矩形角的圆弧半径的数字或列表。  参数类型为number时，所有矩形角的圆弧半径按该数字执行。  参数类型为Array<number>时，数目为1-4个按下面执行：  1. [所有矩形角的圆弧半径]  2. [左上及右下矩形角的圆弧半径, 右上及左下矩形角的圆弧半径]  3. [左上矩形角的圆弧半径, 右上及左下矩形角的圆弧半径, 右下矩形角的圆弧半径]  4. [左上矩形角的圆弧半径, 右上矩形角的圆弧半径, 右下矩形角的圆弧半径, 左下矩形角的圆弧半径]  radii存在负数或列表的数目不在[1,4]内时抛出异常，错误码：103701。  默认值：0，null和undefined按默认值处理。  圆弧半径超过矩形宽高时会等比例缩放到宽高的长度。  默认单位：vp |

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
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. try {
20. offContext.fillStyle = '#707070'
21. offContext.beginPath()
22. // 创建一个(10vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
23. offContext.roundRect(10, 10, 100, 100, 10)
24. // 创建一个(120vp, 10vp)为起点，宽高为100vp，四个矩形角圆弧半径为10vp的圆角矩形
25. offContext.roundRect(120, 10, 100, 100, [10])
26. offContext.fill()
27. offContext.beginPath()
28. // 创建一个(10vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径及右下矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp的圆角矩形
29. offContext.roundRect(10, 120, 100, 100, [10, 20])
30. // 创建一个(120vp, 120vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径及左下矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp的圆角矩形
31. offContext.roundRect(120, 120, 100, 100, [10, 20, 30])
32. // 创建一个(10vp, 230vp)为起点，宽高为100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
33. offContext.roundRect(10, 230, 100, 100, [10, 20, 30, 40])
34. // 创建一个(220vp, 330vp)为起点，宽高为-100vp，左上矩形角圆弧半径为10vp，右上矩形角圆弧半径为20vp，右下矩形角圆弧半径为30vp，左下矩形角圆弧半径为40vp的圆角矩形
35. offContext.roundRect(220, 330, -100, -100, [10, 20, 30, 40])
36. offContext.stroke()
37. } catch (error) {
38. let e: BusinessError = error as BusinessError;
39. console.error(`Failed to create roundRect. Code: ${e.code}, message: ${e.message}`);
40. }
41. // 在离屏画布最近渲染的图像上创建一个ImageBitmap对象
42. let image = this.offCanvas.transferToImageBitmap()
43. // 将创建的ImageBitmap对象显示在Canvas画布上
44. this.context.transferFromImageBitmap(image)
45. })
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/mKxsAtsoQMy1M2PQ1RbqcQ/zh-cn_image_0000002552800302.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=3C35C99532DB4276647D10A57DDB16C5282E5C31B18B431CD543B98A9FCBD83F)

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

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Fill {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = '#000000'
18. offContext.rect(20, 20, 100, 100) // Create a 100*100 rectangle at (20, 20)
19. offContext.fill()
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/zQWGh3X5TOi7yflS36Ruhg/zh-cn_image_0000002552800342.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=4A317247F653981E22CE226368462D6863AFE1B5BA913FE02DC30E3F1F5E972E)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let region = new Path2D()
18. region.moveTo(30, 90)
19. region.lineTo(110, 20)
20. region.lineTo(240, 130)
21. region.lineTo(60, 130)
22. region.lineTo(190, 20)
23. region.lineTo(270, 90)
24. region.closePath()
25. // Fill path
26. offContext.fillStyle = '#00ff00'
27. offContext.fill(region, "evenodd")
28. let image = this.offCanvas.transferToImageBitmap()
29. this.context.transferFromImageBitmap(image)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/JRXV7ySiQPql-TqHY4ot1A/zh-cn_image_0000002583440037.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=316F64BF4F45777384F6DC272A87452C495120BCBCA13F1772138DDAAB8EA676)

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

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Clip {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.rect(0, 0, 100, 200)
18. offContext.stroke()
19. offContext.clip()
20. offContext.fillStyle = "rgb(255,0,0)"
21. offContext.fillRect(0, 0, 200, 200)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/hpHk-P5OTC2jeP_iQ82pSQ/zh-cn_image_0000002583479953.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=AD857A3DB236F6D341C83439D62AE39131E998A031F18C20643CFBE8BDF9293C)

### clip

PhonePC/2in1TabletTVWearable

clip(path: Path2D, fillRule?: CanvasFillRule): void

设置指定路径为剪切路径。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数:**

| 参数名 | 类型 | 必填 | 描述 |
| --- | --- | --- | --- |
| path | [Path2D](ts-components-canvas-path2d.md) | 是 | Path2D剪切路径。  异常值undefined或null按无效值处理。 |
| fillRule | [CanvasFillRule](ts-canvasrenderingcontext2d.md#canvasfillrule类型说明) | 否 | 指定要剪切对象的规则。  可选参数为："nonzero"，"evenodd"。  异常值undefined或null按默认值处理。  默认值："nonzero" |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Clip {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let region = new Path2D()
18. region.moveTo(30, 90)
19. region.lineTo(110, 20)
20. region.lineTo(240, 130)
21. region.lineTo(60, 130)
22. region.lineTo(190, 20)
23. region.lineTo(270, 90)
24. region.closePath()
25. offContext.clip(region,"evenodd")
26. offContext.fillStyle = "rgb(0,255,0)"
27. offContext.fillRect(0, 0, 600, 600)
28. let image = this.offCanvas.transferToImageBitmap()
29. this.context.transferFromImageBitmap(image)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/tv4G5TPtQDGm56spqJUfYw/zh-cn_image_0000002552800304.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=CC4F68C3BE9AC76008CC9C78AB3CD7AF9A1FCCCE2CA5C98A0157460302D2FACC)

### reset12+

PhonePC/2in1TabletTVWearable

reset(): void

将OffscreenCanvasRenderingContext2D重置为其默认状态，清除后台缓冲区、绘制状态栈、绘制路径和样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Reset {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = '#0000ff'
18. offContext.fillRect(20, 20, 150, 100)
19. offContext.reset()
20. offContext.fillRect(20, 150, 150, 100)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/81BwLvLlTU61jzew95OOsQ/zh-cn_image_0000002583439999.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=F3D288BADECBA53918DEB11EA959BA57C2C587E77AFCCC162E341F6974A8E38A)

### saveLayer12+

PhonePC/2in1TabletTVWearable

saveLayer(): void

创建一个图层。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct saveLayer {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = "#0000ff"
18. offContext.fillRect(50, 100, 300, 100)
19. offContext.fillStyle = "#00ffff"
20. offContext.fillRect(50, 150, 300, 100)
21. offContext.globalCompositeOperation = 'destination-over'
22. offContext.saveLayer()
23. offContext.globalCompositeOperation = 'source-over'
24. offContext.fillStyle = "#ff0000"
25. offContext.fillRect(100, 50, 100, 300)
26. offContext.fillStyle = "#00ff00"
27. offContext.fillRect(150, 50, 100, 300)
28. offContext.restoreLayer()
29. let image = this.offCanvas.transferToImageBitmap()
30. this.context.transferFromImageBitmap(image)
31. })
32. }
33. .width('100%')
34. .height('100%')
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/iajWjf8-RNa5ggbh-OCKLQ/zh-cn_image_0000002552959954.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=4C8D44742CC99180C8B95ADD9F4E804CA5E9FC702E15026C0F68F274D489B6F3)

### restoreLayer12+

PhonePC/2in1TabletTVWearable

restoreLayer(): void

恢复图像变换和裁剪状态至saveLayer前的状态，并将图层绘制在canvas上。restoreLayer示例同saveLayer。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
18. offContext.fillStyle = 'rgb(0,0,255)'
19. offContext.fillRect(0, 0, 100, 100)
20. offContext.resetTransform()
21. offContext.fillStyle = 'rgb(255,0,0)'
22. offContext.fillRect(0, 0, 100, 100)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/7Z8CLZ2PTwyjlbKHfprKoA/zh-cn_image_0000002583479955.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=5F4214A0679437AAB5E6D669A675DB2201BFE8CDA7E6DF2CA9E118345A8390FA)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.rotate(45 * Math.PI / 180)
18. offContext.fillRect(70, 20, 50, 50)
19. let image = this.offCanvas.transferToImageBitmap()
20. this.context.transferFromImageBitmap(image)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/V7mMcHTnQdKMuGdLRE8abw/zh-cn_image_0000002552959992.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=F2F246C8111A2E27FCFD9460886613041C36BACBB33D432A0C7A3A17690B8F11)

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
| x | number | 是 | 设置水平方向的缩放值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |
| y | number | 是 | 设置垂直方向的缩放值。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Scale {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.lineWidth = 3
18. offContext.strokeRect(30, 30, 50, 50)
19. offContext.scale(2, 2) // Scale to 200%
20. offContext.strokeRect(30, 30, 50, 50)
21. let image = this.offCanvas.transferToImageBitmap()
22. this.context.transferFromImageBitmap(image)
23. })
24. }
25. .width('100%')
26. .height('100%')
27. }
28. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/cl7PoIPZQZiXca6v0L18Xw/zh-cn_image_0000002583440001.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=5300FFA0B8D09FF16F1C1F3DE8AFB689C3E99BAAC50C9E7E202C2D4D1139E192)

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
4. struct Transform {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(112,112,112)'
18. offContext.fillRect(0, 0, 100, 100)
19. offContext.transform(1, 0.5, -0.5, 1, 10, 10)
20. offContext.fillStyle = 'rgb(0,74,175)'
21. offContext.fillRect(0, 0, 100, 100)
22. offContext.transform(1, 0.5, -0.5, 1, 10, 10)
23. offContext.fillStyle = 'rgb(39,135,217)'
24. offContext.fillRect(0, 0, 100, 100)
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/HClvBiqTQqSXg2SxtEN8EQ/zh-cn_image_0000002552959956.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=C5F37D5E6948B849E68EA18E9D2BB7EA705E2A379E2CAB2EF6D355C70B7EB5DC)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillStyle = 'rgb(255,0,0)'
18. offContext.fillRect(0, 0, 100, 100)
19. offContext.setTransform(1,0.5, -0.5, 1, 10, 10)
20. offContext.fillStyle = 'rgb(0,0,255)'
21. offContext.fillRect(0, 0, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/AHakRMRcSvSFCC6h5VBbTA/zh-cn_image_0000002583479993.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=3CA99B1C523A17238D6DE15595D62462EE694C434CFAB542094DB7F8D18AE2C5)

### setTransform

PhonePC/2in1TabletTVWearable

setTransform(transform?: Matrix2D): void

以Matrix2D对象为模板重置现有的变换矩阵并创建新的变换矩阵。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
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
7. private offcontext1: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);
8. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
9. private offcontext2: OffscreenCanvasRenderingContext2D = new OffscreenCanvasRenderingContext2D(600, 200, this.settings);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Text('context1');
14. Canvas(this.context1)
15. .width('230vp')
16. .height('160vp')
17. .backgroundColor('#ffff00')
18. .onReady(() => {
19. this.offcontext1.fillRect(100, 20, 50, 50);
20. this.offcontext1.setTransform(1, 0.5, -0.5, 1, 10, 10);
21. this.offcontext1.fillRect(100, 20, 50, 50);
22. let image = this.offcontext1.transferToImageBitmap();
23. this.context1.transferFromImageBitmap(image);
24. })
25. Text('context2');
26. Canvas(this.context2)
27. .width('230vp')
28. .height('160vp')
29. .backgroundColor('#0ffff0')
30. .onReady(() => {
31. this.offcontext2.fillRect(100, 20, 50, 50);
32. let storedTransform = this.offcontext1.getTransform();
33. this.offcontext2.setTransform(storedTransform);
34. this.offcontext2.fillRect(100, 20, 50, 50);
35. let image = this.offcontext2.transferToImageBitmap();
36. this.context2.transferFromImageBitmap(image);
37. })
38. }
39. .width('100%')
40. .height('100%')
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/p-vjS1sXSseA_qtnAYcY_A/zh-cn_image_0000002552800344.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=B6616205E2322407E3EA7B97565FA85AF09FCB226587F432E2FE4162C090BBB1)

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
7. private offcontext1: OffscreenCanvasRenderingContext2D =
8. new OffscreenCanvasRenderingContext2D(600, 100, this.settings);
9. private context2: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
10. private offcontext2: OffscreenCanvasRenderingContext2D =
11. new OffscreenCanvasRenderingContext2D(600, 100, this.settings);

13. build() {
14. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
15. Text('context1');
16. Canvas(this.context1)
17. .width('230vp')
18. .height('120vp')
19. .backgroundColor('#ffff00')
20. .onReady(() => {
21. this.offcontext1.fillRect(50, 50, 50, 50);
22. this.offcontext1.setTransform(1.2, Math.PI / 8, Math.PI / 6, 0.5, 30, -25);
23. this.offcontext1.fillRect(50, 50, 50, 50);
24. let image = this.offcontext1.transferToImageBitmap();
25. this.context1.transferFromImageBitmap(image);
26. })
27. Text('context2');
28. Canvas(this.context2)
29. .width('230vp')
30. .height('120vp')
31. .backgroundColor('#0ffff0')
32. .onReady(() => {
33. this.offcontext2.fillRect(50, 50, 50, 50);
34. let storedTransform = this.offcontext1.getTransform();
35. console.info(`Matrix [scaleX = ${storedTransform.scaleX}, scaleY = ${storedTransform.scaleY}, rotateX = ${storedTransform.rotateX}, rotateY = ${storedTransform.rotateY}, translateX = ${storedTransform.translateX}, translateY = ${storedTransform.translateY}]`)
36. this.offcontext2.setTransform(storedTransform);
37. this.offcontext2.fillRect(50, 50, 50, 50);
38. let image = this.offcontext2.transferToImageBitmap();
39. this.context2.transferFromImageBitmap(image);
40. })
41. }
42. .width('100%')
43. .height('100%')
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/ykxJo8uBRz2zuA0tZPGF9Q/zh-cn_image_0000002583440003.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=2AF172CA0AE165A0EA241B72CEA62F5A045FEFD859225CFE8FABC52C5D744D47)

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
| y | number | 是 | 设置垂直平移量。  API version 18之前，设置NaN或Infinity时，在该方法后执行的绘制方法无法绘制；设置null或undefined时，当前接口不生效。API version 18及以后，设置NaN、Infinity、null或undefined时当前接口不生效，其他传入有效参数的绘制方法正常绘制。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Translate {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillRect(10, 10, 50, 50)
18. offContext.translate(70, 70)
19. offContext.fillRect(10, 10, 50, 50)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/wQKtTbxIRLuWt8OsJO21bA/zh-cn_image_0000002583440039.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=29339C6A357B10EB53BD8A77D0F5153A6D0C18B59DCDE5ED8DC688374ED44D1C)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number): void

进行图像绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
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
4. struct DrawImage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/uemS1AONTh-qhgP63jUwVA/zh-cn_image_0000002552959994.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=0CA30949C275BCFF0C879CB7C2E4472CD09AD8C570336148ABBFCDEA8912E1DA)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, dx: number, dy: number, dw: number, dh: number): void

将图像拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](ts-components-canvas-imagebitmap.md) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dh | number | 是 | 绘制区域的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DrawImage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0, 300, 300)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/ohZXx_KtREy4u_K3GnDCGg/zh-cn_image_0000002583479995.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=46BEDD60A96D789ECA6AA03BFC9A52CAD6B7BE12F0B8A3ACC450C44BD5FFF38B)

### drawImage

PhonePC/2in1TabletTVWearable

drawImage(image: ImageBitmap | PixelMap, sx: number, sy: number, sw: number, sh: number, dx: number, dy: number, dw: number, dh: number): void

将图像裁剪后拉伸或压缩绘制。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，卡片中不支持PixelMap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | [ImageBitmap](ts-components-canvas-imagebitmap.md) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片资源，请参考ImageBitmap或PixelMap。  异常值undefined或null按无效值处理，不进行绘制。 |
| sx | number | 是 | 裁切源图像时距离源图像左上角的x坐标值。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sy | number | 是 | 裁切源图像时距离源图像左上角的y坐标值。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sw | number | 是 | 裁切源图像时需要裁切的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| sh | number | 是 | 裁切源图像时需要裁切的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  image类型为ImageBitmap时，默认单位：vp  image类型为PixelMap时，API version 18前，默认单位：px；API version 18及以后，默认单位：vp |
| dx | number | 是 | 绘制区域左上角在x轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dy | number | 是 | 绘制区域左上角在y轴的位置。  异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dw | number | 是 | 绘制区域的宽度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |
| dh | number | 是 | 绘制区域的高度。  负数、异常值undefined或null按0处理，NaN和Infinity按无效值处理，不进行绘制。  默认单位：vp |

**示例：**

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct DrawImage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#D5D5D5')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 300)
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/v8_ctlm-T3q3i5Av6-6t2w/zh-cn_image_0000002552800346.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=0EAF3A6F6B1B5AFE9B999BA137AE1A7583CE3747D6A92A35975577051D3953B5)

### createImageData

PhonePC/2in1TabletTVWearable

createImageData(sw: number, sh: number): ImageData

根据当前ImageData对象重新创建一个宽、高相同的ImageData对象，请参考[ImageData](ts-components-canvas-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

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

createImageData(imageData: ImageData): ImageData

根据已创建的ImageData对象创建新的ImageData对象（不会复制图像数据），请参考[ImageData](ts-components-canvas-imagedata.md)，该接口存在内存拷贝行为，高耗时，应避免频繁使用。createImageData示例同putImageData。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageData | [ImageData](ts-components-canvas-imagedata.md) | 是 | 被复制的ImageData对象。  异常值undefined和null按width和height为0的ImageData处理。 |

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

| 参数 | 类型 | 必填 | 说明 |
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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
8. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");
9. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 100, 100, 130, 130)
20. let pixelmap = offContext.getPixelMap(150, 150, 130, 130)
21. offContext.setPixelMap(pixelmap)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/-iR11k7GSbyZQzQU-02EBg/zh-cn_image_0000002583440041.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=B116A7E94F6C5CD10C9744866DB92C22526462340A0F63582BFCCC519C55E246)

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);
8. // "/common/images/1234.png"需要替换为开发者所需的图像资源文件
9. private img:ImageBitmap = new ImageBitmap("/common/images/1234.png");

11. build() {
12. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
13. Canvas(this.context)
14. .width('100%')
15. .height('100%')
16. .backgroundColor('#ffff00')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.drawImage(this.img, 0, 0, 130, 130)
20. let imageData = offContext.getImageData(50,50,130,130)
21. offContext.putImageData(imageData, 150, 150)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/FuoggdAgSOeMXReGyCZFEg/zh-cn_image_0000002583479961.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=D6E5792DBAA41A48661E4229229CD9FEB9587157960C3C9C35D3AD2FC4AB4DBC)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string): void

使用[ImageData](ts-components-canvas-imagedata.md)数据填充新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let imageDataNum = offContext.createImageData(100, 100)
18. let imageData = offContext.createImageData(imageDataNum)
19. for (let i = 0; i < imageData.data.length; i += 4) {
20. imageData.data[i + 0] = 112
21. imageData.data[i + 1] = 112
22. imageData.data[i + 2] = 112
23. imageData.data[i + 3] = 255
24. }
25. offContext.putImageData(imageData, 10, 10)
26. let image = this.offCanvas.transferToImageBitmap()
27. this.context.transferFromImageBitmap(image)
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/rmE0ZtFmQuuwoBMQE9JvWg/zh-cn_image_0000002552959996.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=7532050668F758B0E420C62F1B16FBCE535AE9B41A20BC8938658803BFAE96B4)

### putImageData

PhonePC/2in1TabletTVWearable

putImageData(imageData: ImageData, dx: number | string, dy: number | string, dirtyX: number | string, dirtyY: number | string, dirtyWidth?: number | string, dirtyHeight: number | string): void

使用[ImageData](ts-components-canvas-imagedata.md)数据裁剪后填充至新的矩形区域。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 描述 |
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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let imageDataNum = offContext.createImageData(100, 100)
18. let imageData = offContext.createImageData(imageDataNum)
19. for (let i = 0; i < imageData.data.length; i += 4) {
20. imageData.data[i + 0] = 112
21. imageData.data[i + 1] = 112
22. imageData.data[i + 2] = 112
23. imageData.data[i + 3] = 255
24. }
25. offContext.putImageData(imageData, 10, 10, 0, 0, 100, 50)
26. let image = this.offCanvas.transferToImageBitmap()
27. this.context.transferFromImageBitmap(image)
28. })
29. }
30. .width('100%')
31. .height('100%')
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/WOyX1ytGTG2eVUAu4O_PIg/zh-cn_image_0000002583479997.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=36E7E9B7F419D13DA2EFF091AB1764FF691150D76E63BBEFAC4123042754687A)

### setLineDash

setLineDash(segments: number[]): void

设置画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#D5D5D5')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.arc(100, 75, 50, 0, 6.28)
18. offContext.setLineDash([10, 20])
19. offContext.stroke()
20. let image = this.offCanvas.transferToImageBitmap()
21. this.context.transferFromImageBitmap(image)
22. })
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/jlWwPemnRNS-HNzMwFnHLQ/zh-cn_image_0000002552800348.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=688505D564DAD78FF9B637D4416CF1A6DD355806D67BCB4CA9EE98590569F0FE)

### getLineDash

getLineDash(): number[]

获得当前画布的虚线样式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number[] | 返回数组，该数组用来描述线段如何交替和间距长度。  异常值undefined或null按无效值处理。  默认单位：vp |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasGetLineDash {
5. @State message: string = 'Hello World';
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

10. build() {
11. Row() {
12. Column() {
13. Text(this.message)
14. .fontSize(50)
15. .fontWeight(FontWeight.Bold)
16. Canvas(this.context)
17. .width('100%')
18. .height('100%')
19. .backgroundColor('#D5D5D5')
20. .onReady(() => {
21. let offContext = this.offCanvas.getContext("2d", this.settings)
22. offContext.arc(100, 75, 50, 0, 6.28)
23. offContext.setLineDash([10, 20])
24. offContext.stroke()
25. let res = offContext.getLineDash()
26. this.message = JSON.stringify(res)
27. let image = this.offCanvas.transferToImageBitmap()
28. this.context.transferFromImageBitmap(image)
29. })
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/9PTo74kISgep7DYVM5nFkg/zh-cn_image_0000002583479963.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A21A735DBE85EB626D29D3287ED1D4572708AE96CCC0C41A5EF158183A2B9838)

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
4. struct ToDataURL {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(100, 100);
8. @State dataURL: string = "";

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width(100)
14. .height(100)
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.fillRect(0, 0, 100, 100)
18. this.dataURL = offContext.toDataURL()
19. })
20. Text(this.dataURL)
21. }
22. .width('100%')
23. .height('100%')
24. .backgroundColor('#ffff00')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/ORSVZKHXS1S_KGA3hMbtqw/zh-cn_image_0000002583440043.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=FF8A4BA8DC0AF9E2B484F4873B7CB761E906469CD5394F8593F73699362B55A9)

### transferToImageBitmap

PhonePC/2in1TabletTVWearable

transferToImageBitmap(): ImageBitmap

在离屏画布最近渲染的图像上创建一个ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageBitmap](ts-components-canvas-imagebitmap.md) | 存储离屏画布上渲染的像素数据。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PutImageData {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let imageData = offContext.createImageData(100, 100)
18. for (let i = 0; i < imageData.data.length; i += 4) {
19. imageData.data[i + 0] = 112
20. imageData.data[i + 1] = 112
21. imageData.data[i + 2] = 112
22. imageData.data[i + 3] = 255
23. }
24. offContext.putImageData(imageData, 10, 10)
25. let image = this.offCanvas.transferToImageBitmap()
26. this.context.transferFromImageBitmap(image)
27. })
28. }
29. .width('100%')
30. .height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/jJ5apDQATzG3VldpkJFQVQ/zh-cn_image_0000002552959998.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=CFF966CF0EDB770837DC1E6ADBC3397E1321588F564A524E1D16CF5C8A44AF25)

### restore

PhonePC/2in1TabletTVWearable

restore(): void

对保存的绘图上下文进行恢复。

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
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.save() // save the default state
18. offContext.fillStyle = "#00ff00"
19. offContext.fillRect(20, 20, 100, 100)
20. offContext.restore() // restore to the default state
21. offContext.fillRect(150, 75, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/ESCDjM8pRRGYxW6EeFX72w/zh-cn_image_0000002552959964.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=D28A450DD938548AEDDE8EC6B0C7EF6A083E20C13E6A08FFD08C9E839B9D53AD)

### save

PhonePC/2in1TabletTVWearable

save(): void

对当前的绘图上下文进行保存。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffff00')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. offContext.save() // save the default state
18. offContext.fillStyle = "#00ff00"
19. offContext.fillRect(20, 20, 100, 100)
20. offContext.restore() // restore to the default state
21. offContext.fillRect(150, 75, 100, 100)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.transferFromImageBitmap(image)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/cUcElE9yQQmDWGZN0kqQRQ/zh-cn_image_0000002552959964.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=C671D94461D15E2329C319CFFD5D28F92C78C6E2843B1AB31CC6D0A877B67D0B)

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
| [CanvasGradient](ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreateLinearGradient {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let grad = offContext.createLinearGradient(50,0, 300,100)
18. grad.addColorStop(0.0, 'rgb(39,135,217)')
19. grad.addColorStop(0.5, 'rgb(255,238,240)')
20. grad.addColorStop(1.0, 'rgb(23,169,141)')
21. offContext.fillStyle = grad
22. offContext.fillRect(0, 0, 400, 400)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/BeeZ5LqwRwSGCSy9veGGmw/zh-cn_image_0000002583439973.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=239116F212294984C0054823915F1187CCE8D44F9BDFA587F668E5A7B1760FDA)

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
| [CanvasGradient](ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CreateRadialGradient {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('rgb(213,213,213)')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let grad = offContext.createRadialGradient(200,200,50, 200,200,200)
18. grad.addColorStop(0.0, 'rgb(39,135,217)')
19. grad.addColorStop(0.5, 'rgb(255,238,240)')
20. grad.addColorStop(1.0, 'rgb(112,112,112)')
21. offContext.fillStyle = grad
22. offContext.fillRect(0, 0, 440, 440)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/GU3RUYXuQM2QwAtoIxSrJw/zh-cn_image_0000002583479965.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=A2E299053372657938F9875D0E3656C537AE473D83D51E4735B4D7EC48CBEFA9)

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
| [CanvasGradient](ts-components-canvas-canvasgradient.md) | 新的CanvasGradient对象，用于在offscreenCanvas上创建渐变效果。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasConicGradientPage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#ffffff')
15. .onReady(() => {
16. let offContext = this.offCanvas.getContext("2d", this.settings)
17. let grad = offContext.createConicGradient(0, 50, 80)
18. grad.addColorStop(0.0, '#ff0000')
19. grad.addColorStop(0.5, '#ffffff')
20. grad.addColorStop(1.0, '#00ff00')
21. offContext.fillStyle = grad
22. offContext.fillRect(0, 30, 100, 100)
23. let image = this.offCanvas.transferToImageBitmap()
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/0qSC2xIlT-mDOhmrX6nsrA/zh-cn_image_0000002552800316.png?HW-CC-KV=V1&HW-CC-Date=20260428T000206Z&HW-CC-Expire=86400&HW-CC-Sign=6C9423A81E5AE8762D00DBF46C36B647F00A280EA26C332169B522939CDE4290)
