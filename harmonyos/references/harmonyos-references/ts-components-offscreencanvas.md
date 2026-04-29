---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-offscreencanvas
title: OffscreenCanvas
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > OffscreenCanvas
category: harmonyos-references
scraped_at: 2026-04-29T13:52:35+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:18aac8d32da556cac59c2f4c2f7c0be47fea462b0d0d0e42771a202cb18492af
---

OffscreenCanvas组件用于绘制自定义图形。

使用[Canvas](ts-components-canvas-canvas.md)组件或[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)对象时，渲染、动画和用户交互通常发生在应用程序的主线程上，与画布动画和渲染相关的计算可能会影响应用程序性能。OffscreenCanvas提供了一个可以在屏幕外渲染的画布，这样可以在单独的线程中运行一些任务，从而避免影响应用程序主线程性能。

说明

该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

OffscreenCanvas无法在ServiceExtensionAbility中使用，ServiceExtensionAbility中建议使用[Drawing模块](arkts-apis-graphics-drawing.md)进行离屏绘制。

## 子组件

PhonePC/2in1TabletTVWearable

不支持。

## 构造函数

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number)

构造用于创建离屏画布对象的OffscreenCanvas。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | OffscreenCanvas组件的宽度。  异常值NaN和Infinity按无效值处理。  默认单位为vp。 |
| height | number | 是 | OffscreenCanvas组件的高度。  异常值NaN和Infinity按无效值处理。  默认单位为vp。 |

### constructor12+

PhonePC/2in1TabletTVWearable

constructor(width: number, height: number, unit: LengthMetricsUnit)

构造用于创建离屏画布对象的OffscreenCanvas，支持配置OffscreenCanvas的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | OffscreenCanvas组件的宽度。  异常值NaN和Infinity按无效值处理。  默认单位为vp。 |
| height | number | 是 | OffscreenCanvas组件的高度。  异常值NaN和Infinity按无效值处理。  默认单位为vp。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置OffscreenCanvas对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值NaN和Infinity按默认值处理。  默认值：DEFAULT |

## 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

OffscreenCanvas支持以下属性：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 否 | 否 | OffscreenCanvas组件的宽度。  默认单位为vp。 |
| height | number | 否 | 否 | OffscreenCanvas组件的高度。  默认单位为vp。 |

### width

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasPage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(200, 300);

9. build() {
10. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
11. Column() {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .borderWidth(5)
16. .borderColor('#057D02')
17. .backgroundColor('#FFFFFF')
18. .onReady(() => {
19. let offContext = this.offCanvas.getContext("2d", this.settings)
20. offContext.fillStyle = '#CDCDCD'
21. offContext.fillRect(0, 0, this.offCanvas.width, 150)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.setTransform(1, 0, 0, 1, 50, 200)
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. }.width('100%').height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/PfYyGPe1S6iS8B7p1BDWCw/zh-cn_image_0000002589246307.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=2605B814BF403B84DEB5289757E29758E0FC3FA72DBCF6224597C868DCC10114)

### height

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasPage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(200, 300);

9. build() {
10. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
11. Column() {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .borderWidth(5)
16. .borderColor('#057D02')
17. .backgroundColor('#FFFFFF')
18. .onReady(() => {
19. let offContext = this.offCanvas.getContext("2d", this.settings)
20. offContext.fillStyle = '#CDCDCD'
21. offContext.fillRect(0, 0, 100, this.offCanvas.height)
22. let image = this.offCanvas.transferToImageBitmap()
23. this.context.setTransform(1, 0, 0, 1, 50, 200)
24. this.context.transferFromImageBitmap(image)
25. })
26. }
27. }.width('100%').height('100%')
28. }
29. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/mnT02E0BQIqx0Co8gx2yPg/zh-cn_image_0000002558766500.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=BECE5EBF0F99E8AE8A68FDFAD3250B1C9209E62EDA88C6F0DC2B831999DCBB19)

## 方法

PhonePC/2in1TabletTVWearable

### transferToImageBitmap

PhonePC/2in1TabletTVWearable

transferToImageBitmap(): ImageBitmap

从OffscreenCanvas组件中最近渲染的图像创建一个ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ImageBitmap](ts-components-canvas-imagebitmap.md) | 创建的ImageBitmap对象。 |

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OffscreenCanvasPage {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
7. private offCanvas: OffscreenCanvas = new OffscreenCanvas(400, 600);

9. build() {
10. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .borderWidth(5)
15. .borderColor('rgb(39,135,217)')
16. .backgroundColor('#FFFFFF')
17. .onReady(() => {
18. let offContext = this.offCanvas.getContext("2d", this.settings)
19. offContext.fillStyle = '#CDCDCD'
20. offContext.fillRect(0, 0, 400, 600)
21. offContext.fillStyle = '#000000'
22. offContext.font = '40px serif bold'
23. offContext.fillText("Offscreen : Hello World!", 20, 60)
24. let image = this.offCanvas.transferToImageBitmap()
25. this.context.transferFromImageBitmap(image)
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Ty0_CH2QTy2DS5-kGhEJMw/zh-cn_image_0000002558606840.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=A77B0C502530A401C6E5C17326932842FAB23E86E0E5604000946EBA40B9E5E5)

### getContext10+

PhonePC/2in1TabletTVWearable

getContext(contextType: "2d", options?: RenderingContextSettings): OffscreenCanvasRenderingContext2D

返回OffscreenCanvas组件的绘图上下文。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contextType | string | 是 | OffscreenCanvas组件绘图上下文的类型，当前仅支持"2d"类型。  "2d"：创建一个表示二维渲染上下文的OffscreenCanvasRenderingContext2D对象。  异常值undefined和null按无效值处理，当前接口返回undefined。 |
| options | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，见[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)。  异常值undefined和null按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md) | OffscreenCanvas组件的绘图上下文。如果getContext方法的入参contextType为"2d"以外类型（包括null或者undefined），返回undefined，使用前应判断返回值是否为undefined。 |

**示例：**

```
1. @Entry
2. @Component
3. struct OffscreenCanvasExamplePage {
4. private settings: RenderingContextSettings = new RenderingContextSettings(true);
5. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
6. private offscreenCanvas: OffscreenCanvas = new OffscreenCanvas(600, 800);

8. build() {
9. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
10. Column() {
11. Canvas(this.context)
12. .width('100%')
13. .height('100%')
14. .backgroundColor('#FFFFFF')
15. .onReady(() => {
16. let offContext = this.offscreenCanvas.getContext("2d", this.settings)
17. offContext.font = '70px sans-serif'
18. offContext.fillText("Offscreen : Hello World!", 20, 60)
19. offContext.fillStyle = "#0000ff"
20. offContext.fillRect(230, 350, 50, 50)
21. offContext.fillStyle = "#EE0077"
22. offContext.translate(70, 70)
23. offContext.fillRect(230, 350, 50, 50)
24. offContext.fillStyle = "#77EE0077"
25. offContext.translate(-70, -70)
26. offContext.fillStyle = "#00ffff"
27. offContext.rotate(45 * Math.PI / 180);
28. offContext.fillRect(180, 120, 50, 50);
29. offContext.rotate(-45 * Math.PI / 180);
30. offContext.beginPath()
31. offContext.moveTo(10, 150)
32. offContext.bezierCurveTo(20, 100, 200, 100, 200, 20)
33. offContext.stroke()
34. offContext.fillStyle = '#FF00FF'
35. offContext.fillRect(100, 100, 60, 60)
36. let imageData = this.offscreenCanvas.transferToImageBitmap()
37. this.context.transferFromImageBitmap(imageData)
38. })
39. }.width('100%').height('100%')
40. }
41. .width('100%')
42. .height('100%')
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/70LH6usYQn6HZgRRk-hdNQ/zh-cn_image_0000002589326367.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=928923482BAB3A16C71330BC51E22F366D005B86B75DD4CA8E6F47A567ABD56A)

## OffscreenCanvas支持并发线程绘制

PhonePC/2in1TabletTVWearable

从API version 11开始，当应用创建[Worker线程](../harmonyos-guides/worker-introduction.md)，支持使用postMessage将OffscreenCanvas实例传到Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。

说明

OffscreenCanvas对象使用getContext获取绘图上下文后，不允许通过postMessage传该对象给其他线程，否则抛出异常。

已经通过postMessage传OffscreenCanvas对象到某一线程，声明该对象的线程不允许该对象使用getContext和transferToImageBitmap方法，否则抛出异常。

已经通过postMessage传OffscreenCanvas对象到某一线程，不允许再将该对象通过postMessage传给其他线程，否则抛出异常。

DevEco Studio的预览器不支持显示在Worker线程中绘制的内容。

**示例：**

```
1. import { worker } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';
4. import { resourceManager } from '@kit.LocalizationKit';
5. import { common } from '@kit.AbilityKit';

7. @Entry
8. @Component
9. struct OffscreenCanvasExamplePage {
10. private settings: RenderingContextSettings = new RenderingContextSettings(true);
11. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
12. private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
13. private imgPixelMap: image.PixelMap | undefined = undefined

15. aboutToAppear(): void {
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
17. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
18. try {
19. this.imgPixelMap = resourceMgr.getDrawableDescriptor($r("app.media.startIcon").id).getPixelMap();
20. } catch (error) {
21. console.error(`resourceMgr getDrawableDescriptor error, error code: ${(error as BusinessError).code}`);
22. }
23. }

25. build() {
26. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Start }) {
27. Column() {
28. Canvas(this.context)
29. .width('100%')
30. .height('100%')
31. .borderWidth(5)
32. .borderColor('#057D02')
33. .backgroundColor('#FFFFFF')
34. .onReady(() => {
35. let offCanvas = new OffscreenCanvas(600, 800)
36. // worker线程中绘制图像
37. this.myWorker.postMessage({ myOffCanvas: offCanvas, imgPixelMap: this.imgPixelMap });
38. this.myWorker.onmessage = (e): void => {
39. if (e.data.myImage) {
40. let image: ImageBitmap = e.data.myImage
41. this.context.transferFromImageBitmap(image)
42. }
43. }
44. })
45. }
46. .width('100%')
47. .height('100%')
48. }
49. .width('100%')
50. .height('100%')
51. }
52. }
```

Worker线程在onmessage中接收到主线程postMessage发送的OffscreenCanvas，并进行绘制。

```
1. // entry/src/main/ets/workers/Worker.ets
2. import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
3. import { image } from '@kit.ImageKit';

5. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

7. workerPort.onmessage = (e: MessageEvents) => {
8. if (e.data.myOffCanvas) {
9. let offCanvas: OffscreenCanvas = e.data.myOffCanvas
10. let offContext = offCanvas.getContext("2d")
11. offContext.fillStyle = '#CDCDCD'
12. offContext.fillRect(0, 0, 200, 150)

14. let imgPixelMap: image.PixelMap = e.data.imgPixelMap
15. let imgBitmap: ImageBitmap = new ImageBitmap(imgPixelMap)
16. offContext.drawImage(imgBitmap, 0, 200)

18. let path2d = new Path2D("M250 150 L150 350 L350 350 Z")
19. offContext.stroke(path2d)

21. let matrix: Matrix2D = new Matrix2D()
22. matrix.scaleX = 1
23. matrix.scaleY = 1
24. matrix.rotateX = -0.5
25. matrix.rotateY = 0.5
26. matrix.translateX = 10
27. matrix.translateY = 10
28. offContext.setTransform(matrix)
29. offContext.fillStyle = "#707070"
30. offContext.fillRect(20, 20, 100, 100)

32. let image = offCanvas.transferToImageBitmap()
33. workerPort.postMessage({ myImage: image });
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/yi_cbUI8S6-TlufDoDb_SQ/zh-cn_image_0000002589246309.png?HW-CC-KV=V1&HW-CC-Date=20260429T055230Z&HW-CC-Expire=86400&HW-CC-Sign=7F571CAF2BA5CE812D53DC12E8A6C5FB49CA4778945A612DA6FC44A25D58A525)
