---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagebitmap
title: ImageBitmap
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > ImageBitmap
category: harmonyos-references
scraped_at: 2026-04-29T13:52:34+08:00
doc_updated_at: 2026-04-10
content_hash: sha256:3c23112d83c76c610ab8c96b8062eea08552a1e628d451100236774c84cc5816
---

ImageBitmap对象可以存储canvas渲染的像素数据。从API version 11开始，当应用创建[Worker线程](../harmonyos-guides/worker-introduction.md)，支持使用postMessage将ImageBitmap实例传到Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。

说明

从 API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## constructor

PhonePC/2in1TabletTVWearable

constructor(src: string)

通过ImageSrc创建ImageBitmap对象。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 图片的数据源支持本地图片。  1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。  type为"har"和"shared"类型的Module中推荐使用[ImageSource](../harmonyos-guides/image-decoding.md)图片解码方式将资源图片解码为统一的PixelMap加载使用。  2、支持本地图片类型：bmp、jpg、png、svg和webp类型。  **说明：**  - ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。 |

## constructor

PhonePC/2in1TabletTVWearable

constructor(data: PixelMap)

通过PixelMap创建ImageBitmap对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片的数据源支持PixelMap对象。 |

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(src: string, unit: LengthMetricsUnit)

通过ImageSrc创建ImageBitmap对象，支持使用unit配置Path2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 图片的数据源支持本地图片。  1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。  type为"har"和"shared"类型的Module中推荐使用[ImageSource](../harmonyos-guides/image-decoding.md)图片解码方式将资源图片解码为统一的PixelMap加载使用。  2、支持本地图片类型：bmp、jpg、png、svg和webp类型。  **说明：**  - ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值undefined、NaN和Infinity按默认值处理。 |

## constructor12+

PhonePC/2in1TabletTVWearable

constructor(data: PixelMap, unit: LengthMetricsUnit)

通过PixelMap创建ImageBitmap对象，支持使用unit配置Path2D对象的单位模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片的数据源支持PixelMap对象。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。 |

## close

PhonePC/2in1TabletTVWearable

close(): void

释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。close示例代码同创建ImageBitmap代码。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | ImageBitmap的像素宽度。  默认单位为vp。 |
| height | number | 是 | 否 | ImageBitmap的像素高度。  默认单位为vp。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（加载图片）

通过ImageBitmap加载本地图片。

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
15. .backgroundColor('#ffff00')
16. .onReady(() => {
17. this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
18. this.img.close()
19. })
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/JrRkbaloT-qH8pg4giViMg/zh-cn_image_0000002589326361.png?HW-CC-KV=V1&HW-CC-Date=20260429T055229Z&HW-CC-Expire=86400&HW-CC-Sign=D5E264E5D1D26DC2B678C07E34973558E8FBBC709240D3952344AE1A2D8565D7)

### 示例2（创建ImageBitmap）

通过PixelMap创建ImageBitmap对象。

说明

DevEco Studio的预览器不支持getPixelMap接口，不支持显示PixelMap绘制的内容。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Demo {
5. private settings: RenderingContextSettings = new RenderingContextSettings(true);
6. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
10. Canvas(this.context)
11. .width('100%')
12. .height('50%')
13. .backgroundColor('#ffff00')
14. .onReady(() => {
15. this.context.fillStyle = "#00ff00"
16. this.context.fillRect(0, 0, 100, 100)
17. let pixel = this.context.getPixelMap(0, 0, 100, 100)
18. let image = new ImageBitmap(pixel)
19. this.context.drawImage(image, 100, 100)
20. })

22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nFydDftySxmPYrWwA7OPdw/zh-cn_image_0000002589246303.png?HW-CC-KV=V1&HW-CC-Date=20260429T055229Z&HW-CC-Expire=86400&HW-CC-Sign=7B948DC6C2FAB65DBEE9660EBA06857DBC3559DB81D1A6C721EBB7C382CD9EA9)

### 示例3（支持并发线程绘制）

通过创建Worker线程，实现并发线程绘制。

说明

DevEco Studio的预览器不支持显示在Worker线程中绘制的内容。

```
1. import { worker } from '@kit.ArkTS';

3. @Entry
4. @Component
5. struct imageBitmapExamplePage {
6. private settings: RenderingContextSettings = new RenderingContextSettings(true);
7. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
8. private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
9. // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
10. private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

12. build() {
13. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
14. Canvas(this.context)
15. .width('100%')
16. .height('100%')
17. .backgroundColor('#ffff00')
18. .onReady(() => {
19. this.myWorker.postMessage({ myImage: this.img });
20. this.myWorker.onmessage = (e): void => {
21. if (e.data.myImage) {
22. let image: ImageBitmap = e.data.myImage
23. this.context.transferFromImageBitmap(image)
24. }
25. }
26. })
27. }
28. .width('100%')
29. .height('100%')
30. }
31. }
```

Worker线程在onmessage中接收到主线程postMessage发送的ImageBitmap，并进行绘制。

```
1. import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
2. import { image } from '@kit.ImageKit';

4. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
5. workerPort.onmessage = (e: MessageEvents) => {
6. if (e.data.myImage) {
7. let img: ImageBitmap = e.data.myImage
8. let offCanvas = new OffscreenCanvas(600, 600)
9. let offContext = offCanvas.getContext("2d")
10. offContext.drawImage(img, 0, 0, 500, 500, 0, 0, 400, 200)
11. let image = offCanvas.transferToImageBitmap()
12. workerPort.postMessage({ myImage: image });
13. }
14. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/tft_9VtZTSO_3weAqdYmdQ/zh-cn_image_0000002589326361.png?HW-CC-KV=V1&HW-CC-Date=20260429T055229Z&HW-CC-Expire=86400&HW-CC-Sign=B1B7D9058D56E26B6087ACB51E25FF16A574BF04425AD7B81CAF1D46527421FB)
