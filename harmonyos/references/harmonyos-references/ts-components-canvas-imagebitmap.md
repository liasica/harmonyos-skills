---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-imagebitmap
title: ImageBitmap
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > ImageBitmap
category: harmonyos-references
scraped_at: 2026-09-02T15:01:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ada417e31438a8dcf3ca36cce641b63362d5c3746bf6045513204c051218e3aa
---

ImageBitmap对象可以存储canvas渲染的像素数据。从API version 11开始，当应用创建[Worker线程](../harmonyos-guides/worker-introduction.md)，支持使用postMessage将ImageBitmap实例传到Worker中进行绘制，并使用onmessage接收Worker线程发送的绘制结果进行显示。

**说明** 

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* ImageBitmap对象仅支持加载静态图片，如需播放动图，建议使用[Image](ts-basic-components-image.md)组件。

## constructor

constructor(src: string)

通过图片数据源创建ImageBitmap对象。

**说明** 

使用完毕后应调用close()方法释放资源，避免图形资源泄漏。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 图片数据源，支持本地图片。  1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。  type为"har"和"shared"类型的Module中推荐使用[ImageSource](../harmonyos-guides/image-decoding.md)图片解码方式将资源图片解码为统一的PixelMap加载使用。  2、支持本地图片类型：bmp、jpg、png、svg和webp类型。  **说明：**  - ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。 |

## constructor

constructor(data: PixelMap)

通过PixelMap创建ImageBitmap对象。

**说明** 

使用完毕后应调用close()方法释放资源，避免图形资源泄漏。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片数据源，通过PixelMap对象设置。适用于需要对图片进行解码、处理后再绘制的场景，可提高图片加载性能。 |

## constructor12+

constructor(src: string, unit: LengthMetricsUnit)

通过图片数据源创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

**说明** 

使用完毕后应调用close()方法释放资源，避免图形资源泄漏。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 图片数据源，支持本地图片。  1、string格式用于加载本地图片，例如ImageBitmap("common/images/example.jpg")，type为"entry"和"feature"类型的Module，其图片加载路径的起点为当前Module的ets文件夹，type为"har"和"shared"类型的Module，其图片加载路径的起点为当前构建的"entry"或"feature"类型Module的ets文件夹。  type为"har"和"shared"类型的Module中推荐使用[ImageSource](../harmonyos-guides/image-decoding.md)图片解码方式将资源图片解码为统一的PixelMap加载使用。  2、支持本地图片类型：bmp、jpg、png、svg和webp类型。  **说明：**  - ArkTS卡片上不支持http://等网络相关路径前缀、datashare://路径前缀以及file://data/storage路径前缀的字符串。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用于配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  默认值：LengthMetricsUnit.DEFAULT。  异常值undefined、NaN和Infinity按默认值处理。 |

## constructor12+

constructor(data: PixelMap, unit: LengthMetricsUnit)

通过PixelMap创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

**说明** 

使用完毕后应调用close()方法释放资源，避免图形资源泄漏。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片数据源，通过PixelMap对象设置。适用于需要对图片进行解码、处理后再绘制的场景，可提高图片加载性能。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用于配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  默认值：LengthMetricsUnit.DEFAULT。  异常值undefined、NaN和Infinity按默认值处理。 |

## constructor

constructor(data: Resource, unit?: LengthMetricsUnit)

通过Resource创建ImageBitmap对象，支持使用unit配置ImageBitmap对象的单位模式。

**说明** 

使用完毕后应调用close()方法释放资源，避免图形资源泄漏。

**起始版本：** 26.0.0

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API版本26.0.0开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [Resource](ts-types.md#resource) | 是 | 图片数据源，通过Resource资源引用方式设置。适用于引用应用资源目录下的图片资源，如$r('app.media.example')，可避免硬编码路径。  支持图片类型：bmp、jpg、png、svg和webp类型。 |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 否 | 用来配置ImageBitmap对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  默认值：LengthMetricsUnit.DEFAULT。  异常值undefined、NaN和Infinity按默认值处理。 |

## close

close(): void

释放ImageBitmap对象相关联的所有图形资源，并将ImageBitmap对象的宽高置为0。

**说明** 

* 必须与[constructor()](ts-components-canvas-imagebitmap.md#constructor)方法配对使用，创建ImageBitmap对象后，应在使用完毕时调用close()释放资源。未调用close()可能导致图形资源泄漏，影响应用性能。
* 建议在Canvas绘制完成后调用，如在[onReady](ts-components-canvas-canvas.md#onready)回调的最后调用close()。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | 是 | 否 | ImageBitmap的宽度。  单位：vp。 |
| height | number | 是 | 否 | ImageBitmap的高度。  单位：vp。 |

## 示例

### 示例1（加载图片）

通过ImageBitmap加载本地图片。

**说明** 

此示例的资源不在src > main > resource目录下，从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resources目录下的资源进行打包，需启用相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable设置为true，详见resOptions中[copyCodeResource](../harmonyos-guides/ide-hvigor-build-profile.md#section754823013348)相关介绍。

```ts
// xxx.ets
@Entry
@Component
struct ImageExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap('common/images/example.jpg');

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/58HMur7eTjSNzpXanCMKcA/zh-cn_image_0000002736435265.png)

### 示例2（创建ImageBitmap）

通过PixelMap创建ImageBitmap对象。

**说明** 

DevEco Studio的预览器不支持getPixelMap接口，不支持显示PixelMap绘制的内容。

```ts
// xxx.ets
@Entry
@Component
struct Demo {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('50%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillStyle = '#00ff00'
          this.context.fillRect(0, 0, 100, 100)
          let pixel = this.context.getPixelMap(0, 0, 100, 100)
          let image = new ImageBitmap(pixel)
          this.context.drawImage(image, 100, 100)
        })

    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/SqWicCDmTq2SgsgdgQbeNA/zh-cn_image_0000002706836118.png)

### 示例3（支持并发线程绘制）

通过创建Worker线程，实现并发线程绘制。

**说明** 

DevEco Studio的预览器不支持显示在Worker线程中绘制的内容。

```ts
import { worker } from '@kit.ArkTS';

@Entry
@Component
struct imageBitmapExamplePage {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private myWorker = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
  // "common/images/example.jpg"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap("common/images/example.jpg");

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.myWorker.postMessage({ myImage: this.img });
          this.myWorker.onmessage = (e): void => {
            if (e.data.myImage) {
              let image: ImageBitmap = e.data.myImage
              this.context.transferFromImageBitmap(image)
            }
          }
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

Worker线程在onmessage中接收到主线程postMessage发送的ImageBitmap，并进行绘制。

```ts
import { MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;
workerPort.onmessage = (e: MessageEvents) => {
  if (e.data.myImage) {
    let img: ImageBitmap = e.data.myImage
    let offCanvas = new OffscreenCanvas(600, 600)
    let offContext = offCanvas.getContext('2d')
    offContext.drawImage(img, 0, 0, 500, 500, 0, 0, 400, 200)
    let image = offCanvas.transferToImageBitmap()
    workerPort.postMessage({ myImage: image });
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/B27YxBQzRDC9FV7ucyNrBA/zh-cn_image_0000002736435265.png)

### 示例4（加载Resource图片）

通过constructor接口创建Resource类型的ImageBitmap对象，用于Canvas绘制。

从API版本26.0.0开始，新增[constructor](ts-components-canvas-imagebitmap.md#constructor-2)接口。

```ts
// xxx.ets
@Entry
@Component
struct ImageBitmapResourceExample {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // "app.media.example"需要替换为开发者所需的图像资源文件
  private img: ImageBitmap = new ImageBitmap($r("app.media.example"));

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.drawImage(this.img, 0, 0, 500, 500, 0, 0, 400, 200)
          this.img.close()
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ZHBBDiseQr2_CiDOGKqOYQ/zh-cn_image_0000002736315223.png)
