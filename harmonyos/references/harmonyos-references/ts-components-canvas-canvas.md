---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-canvas
title: Canvas
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > Canvas
category: harmonyos-references
scraped_at: 2026-04-28T08:02:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fb4480750d509d9b7c4bfe90920c323e6c6ebdc3099325a7984e048a961e2962
---

提供画布组件，用于自定义绘制图形。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 接口

PhonePC/2in1TabletTVWearable

### Canvas23+

PhonePC/2in1TabletTVWearable

Canvas(params: CanvasParams)

使用CanvasParams创建不缓存指令的Canvas组件。创建Canvas组件时，最大面积不超过10000px\*10000px，超过最大面积则无法正常创建。

说明

* 使用本接口创建的Canvas组件将在[onReady23+](ts-components-canvas-canvas.md#onready23)回调的入参中返回一个[DrawingRenderingContext12+](ts-drawingrenderingcontext.md)对象，可用于在该Canvas组件上进行绘制。
* 使用这个接口创建的Canvas组件在组件不可见时将不响应绘制指令。
* 不可见场景主要包括组件所在的页面进入后台、组件滑到窗口外、设置[visibility](ts-universal-attributes-visibility.md#visibility)属性为隐藏等，不包括组件被其他组件或是其他窗口遮挡导致不可见的场景。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [CanvasParams](ts-components-canvas-canvas.md#canvasparams23) | 是 | Canvas组件的构造参数。 |

### Canvas

PhonePC/2in1TabletTVWearable

Canvas(context?: CanvasRenderingContext2D | DrawingRenderingContext)

创建Canvas组件时，最大面积不超过10000px\*10000px，超过最大面积则无法正常创建。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md) | [DrawingRenderingContext12+](ts-drawingrenderingcontext.md) | 否 | CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见[DrawingRenderingContext](ts-drawingrenderingcontext.md)对象。  异常值null和undefined按未设置context处理。 |

### Canvas12+

PhonePC/2in1TabletTVWearable

Canvas(context: CanvasRenderingContext2D | DrawingRenderingContext, imageAIOptions: ImageAIOptions)

创建Canvas组件，支持设置CanvasRenderingContext2D对象或DrawingRenderingContext对象，支持设置AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md) | [DrawingRenderingContext12+](ts-drawingrenderingcontext.md) | 是 | CanvasRenderingContext2D: 不支持多个Canvas共用一个CanvasRenderingContext2D对象，具体描述见[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)对象。DrawingRenderingContext: 不支持多个Canvas共用一个DrawingRenderingContext对象，具体描述见[DrawingRenderingContext](ts-drawingrenderingcontext.md)对象。  异常值null和undefined按未设置context处理。 |
| imageAIOptions | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。  异常值null和undefined按[ImageAIOptions](ts-image-common.md#imageaioptions12)的默认值处理，默认取值为{ type: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT], aiController: new ImageAnalyzerController() }，即开启主体识别和文字识别功能。 |

## CanvasParams23+

PhonePC/2in1TabletTVWearable

定义Canvas的具体配置参数。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 否 | 是 | 用于描述Canvas绘制时所采用的单位模式。  仅可在创建Canvas时设置，后续不可修改。  默认值：LengthMetricsUnit.DEFAULT |
| imageAIOptions | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### enableAnalyzer12+

PhonePC/2in1TabletTVWearable

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

需要搭配[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)中的[StartImageAnalyzer](ts-canvasrenderingcontext2d.md#startimageanalyzer12)和[StopImageAnalyzer](ts-canvasrenderingcontext2d.md#stopimageanalyzer12)一起使用。

不能和[overlay](ts-universal-attributes-overlay.md#overlay)属性同时使用，两者同时设置时overlay中CustomBuilder属性将失效。该特性依赖设备能力。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 组件支持AI分析，需要组件内容支持主体识别、文字识别或对象查找。  设置为true时，组件可进行AI分析，设置为false时，组件不可进行AI分析。  异常值null和undefined按默认值处理。  默认值：false |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持如下事件：

### onReady

PhonePC/2in1TabletTVWearable

onReady(event: VoidCallback)

Canvas组件初始化完成或者发生大小变化时的事件回调，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取，可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时，只触发[onAreaChange](ts-universal-component-area-change-event.md#onareachange)事件，不触发onReady事件。[onAreaChange](ts-universal-component-area-change-event.md#onareachange)事件在onReady事件后触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | Canvas组件初始化完成或者发生大小变化时的事件回调事件。 |

### onReady23+

PhonePC/2in1TabletTVWearable

onReady(event: Callback<DrawingRenderingContext | undefined> | undefined)

Canvas组件初始化完成或者发生大小变化时的事件回调，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

当该事件被触发时画布被清空，该事件之后Canvas组件宽高确定且可获取，可使用Canvas相关API进行绘制。当Canvas组件仅发生位置变化时，只触发[onAreaChange](ts-universal-component-area-change-event.md#onareachange)事件，不触发onReady事件。[onAreaChange](ts-universal-component-area-change-event.md#onareachange)事件在onReady事件后触发。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<[DrawingRenderingContext](ts-drawingrenderingcontext.md) | undefined> | undefined | 是 | Canvas组件初始化完成或者发生大小变化时的回调事件。  关于Callback<DrawingRenderingContext |undefined>类型的入参：  1. 只有使用[CanvasParams](ts-components-canvas-canvas.md#canvasparams23)创建的Canvas组件在该回调中返回DrawingRenderingContext对象，否则返回undefined。  2. 该回调返回的DrawingRenderingContext对象不允许作为参数创建Canvas组件，否则会导致应用崩溃。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（使用CanvasRenderingContext2D中的方法）

该示例实现了如何在Canvas组件使用[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)中的方法进行绘制。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('100%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillRect(0, 30, 100, 100)
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/zjxU2qJCTkmvJUdy9dFSBg/zh-cn_image_0000002583439971.png?HW-CC-KV=V1&HW-CC-Date=20260428T000204Z&HW-CC-Expire=86400&HW-CC-Sign=F2CC9C51302B791010F92373AD05AA26C1B643FBC2986B3DD9C689BA3F212EEE)

### 示例2（使用DrawingRenderingContext中的方法）

该示例实现了如何在Canvas组件使用[DrawingRenderingContext](ts-drawingrenderingcontext.md)中的方法进行绘制。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct CanvasExample {
5. private context: DrawingRenderingContext = new DrawingRenderingContext();

7. build() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
9. Canvas(this.context)
10. .width('100%')
11. .height('100%')
12. .backgroundColor('rgb(213,213,213)')
13. .onReady(() => {
14. this.context.canvas.drawCircle(200, 200, 100)
15. this.context.invalidate()
16. })
17. }
18. .width('100%')
19. .height('100%')
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/zp-8kRB9TyyAtCrB4xiM4A/zh-cn_image_0000002552959926.png?HW-CC-KV=V1&HW-CC-Date=20260428T000204Z&HW-CC-Expire=86400&HW-CC-Sign=DEC7304AD70EFAD824756BD5B6C7B2044F1963D6EE5327D5C88FFA627B286841)

### 示例3（使用attributeModifier动态设置Canvas组件的属性及方法）

该示例展示了如何使用[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置Canvas组件的[enableAnalyzer](ts-components-canvas-canvas.md#enableanalyzer12)属性和[onReady](ts-components-canvas-canvas.md#onready)方法。

说明

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)相关介绍。

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';

4. class MyCanvasModifier implements AttributeModifier<CanvasAttribute> {
5. context: CanvasRenderingContext2D = new CanvasRenderingContext2D()

7. applyNormalAttribute(instance: CanvasAttribute): void {
8. // 从（0，0）绘制一张宽高为200vp的图片
9. instance.onReady(() => {
10. // "common/img.png"需要替换为开发者所需的图像资源文件
11. let image = new ImageBitmap("common/img.png")
12. this.context.drawImage(image, 0, 0, 200, 200)
13. })
14. // 设置开启组件AI分析功能，点击start后，长按触发AI识别功能
15. instance.enableAnalyzer(true)
16. }
17. }

19. @Entry
20. @Component
21. struct attributeDemo {
22. @State modifier: MyCanvasModifier = new MyCanvasModifier()
23. private settings: RenderingContextSettings = new RenderingContextSettings(true)
24. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)
25. private config: ImageAnalyzerConfig = {
26. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
27. }
28. private aiController: ImageAnalyzerController = new ImageAnalyzerController()
29. private options: ImageAIOptions = {
30. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
31. aiController: this.aiController
32. }

34. build() {
35. Row() {
36. Column() {
37. Button('start')
38. .width(100)
39. .height(50)
40. .margin(5)
41. .onClick(() => {
42. this.context.startImageAnalyzer(this.config)
43. .then(() => {
44. console.info("analysis complete")
45. })
46. .catch((error: BusinessError) => {
47. let e: BusinessError = error as BusinessError
48. console.error(`Error code: ${e.code}, message: ${e.message}`)
49. })
50. })
51. Button('stop')
52. .width(100)
53. .height(50)
54. .margin(5)
55. .onClick(() => {
56. this.context.stopImageAnalyzer()
57. })
58. Button('getTypes')
59. .width(100)
60. .height(50)
61. .margin(5)
62. .onClick(() => {
63. this.aiController.getImageAnalyzerSupportTypes()
64. })
65. Canvas(this.context, this.options)
66. .borderWidth(1)
67. .height(200)
68. .width(200)
69. .attributeModifier(this.modifier)
70. .onAppear(() => {
71. this.modifier.context = this.context
72. })
73. }
74. }
75. }
76. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/IWcZVL2oQhK48fYJIV3CYw/zh-cn_image_0000002583479927.png?HW-CC-KV=V1&HW-CC-Date=20260428T000204Z&HW-CC-Expire=86400&HW-CC-Sign=72FD7FADE96A50A66A439BB91CE7C6D61C4143D9283E26A99D38FC89BEADCD0D)

### 示例4（创建不缓存指令Canvas并进行绘制）

该示例介绍了如何使用[CanvasParams](ts-components-canvas-canvas.md#canvasparams23)创建不缓存指令的Canvas组件并进行绘制。

从API version 23开始，新增CanvasParams接口。

```
1. // xxx.ets
2. import { LengthMetricsUnit } from '@kit.ArkUI';
3. import { drawing } from '@kit.ArkGraphics2D';

5. @Entry
6. @Component
7. struct CanvasExample {
8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas({ unit: LengthMetricsUnit.DEFAULT })
11. .onReady((drawingContext?: DrawingRenderingContext) => {
12. if (!drawingContext) {
13. return
14. }
15. // 使用DrawingRenderingContext进行绘制。
16. let brush = new drawing.Brush()
17. brush.setColor({
18. alpha: 255,
19. red: 39,
20. green: 135,
21. blue: 217
22. })
23. drawingContext.canvas.attachBrush(brush)
24. drawingContext.canvas.drawCircle(200, 200, 100)
25. drawingContext.invalidate()

27. // 使用CanvasRenderingContext2D进行绘制。
28. let context2D: CanvasRenderingContext2D =
29. CanvasRenderingContext2D.getContext2DFromDrawingContext(drawingContext, { antialias: true })
30. context2D.fillStyle = 'rgb(39,135,217)'
31. context2D.fillRect(110, 30, 100, 100)
32. })
33. }
34. .width('100%')
35. .height('100%')
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/oKJdafCXSr2IQLyuLa4WuA/zh-cn_image_0000002552800278.png?HW-CC-KV=V1&HW-CC-Date=20260428T000204Z&HW-CC-Expire=86400&HW-CC-Sign=18C6522BB9AA37F4B5DC022B4F65DC548DB036834A3BDECA1C40AB4A983C3C93)
