---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-offscreencanvasrenderingcontext2d
title: OffscreenCanvasRenderingContext2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > OffscreenCanvasRenderingContext2D
category: harmonyos-references
scraped_at: 2026-09-05T06:17:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6b912499d3312fb4d516b2ad164e4561b98505e7ce0327c4343f17d22660713d
---

使用OffscreenCanvasRenderingContext2D在Canvas上进行离屏绘制，绘制对象可以是形状、文本、图片等。离屏绘制是指将需要绘制的内容先绘制在缓冲区，然后将其转换成图片，一次性绘制到Canvas上。离屏绘制使用CPU进行绘制，绘制速度较慢，对绘制速度有要求的场景应避免使用离屏绘制。

**说明** 

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* OffscreenCanvasRenderingContext2D无法在ServiceExtensionAbility中使用，ServiceExtensionAbility中建议使用[绘制模块](arkts-apis-graphics-drawing.md)进行离屏绘制。
* [beginPath](ts-components-canvas-common-method.md#beginpath)、[moveTo](ts-components-canvas-common-method.md#moveto)、[lineTo](ts-components-canvas-common-method.md#lineto)、[closePath](ts-components-canvas-common-method.md#closepath)、[bezierCurveTo](ts-components-canvas-common-method.md#beziercurveto)、[quadraticCurveTo](ts-components-canvas-common-method.md#quadraticcurveto)、[arc](ts-components-canvas-common-method.md#arc)、[arcTo](ts-components-canvas-common-method.md#arcto)、[ellipse](ts-components-canvas-common-method.md#ellipse)、[rect](ts-components-canvas-common-method.md#rect)和[roundRect](ts-components-canvas-common-method.md#roundrect20)接口只能对OffscreenCanvasRenderingContext2D中的路径生效，无法对[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)和[Path2D](ts-components-canvas-path2d.md)对象中设置的路径生效。
* 支持使用[画布绘制通用方法](ts-components-canvas-common-method.md)和设置[画布绘制通用属性](ts-components-canvas-common-property.md)。

## constructor

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
| settings | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，当需要开启抗锯齿等高级配置时传入此参数，见RenderingContextSettings接口描述。  异常值undefined按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |

## constructor12+

constructor(width: number, height: number, settings?: RenderingContextSettings, unit?: LengthMetricsUnit)

构造离屏Canvas画布对象，支持配置画布宽高、OffscreenCanvasRenderingContext2D对象的参数和单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 离屏画布的宽度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| height | number | 是 | 离屏画布的高度，默认单位：vp  异常值NaN和Infinity按无效值处理。 |
| settings | [RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的参数，当需要开启抗锯齿等高级配置时传入此参数，见RenderingContextSettings接口描述。  异常值undefined按[RenderingContextSettings](ts-canvasrenderingcontext2d.md#renderingcontextsettings)的默认值处理。  默认值：null |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 否 | 用来配置OffscreenCanvasRenderingContext2D对象的单位模式，DEFAULT（默认vp单位，适合大多数场景）、PX（px像素单位，适合需要精确像素控制的场景）。配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  异常值undefined、NaN和Infinity按默认值处理。  默认值：DEFAULT |

## toDataURL

toDataURL(type?: string, quality?: any): string

生成一个包含图片展示的Data URL，该接口存在内存拷贝行为，高耗时，应避免频繁使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 否 | 用于指定图像格式。  可选参数为："image/png"，"image/jpeg"，"image/webp"。  异常值undefined或null按默认值处理。  默认值：image/png |
| quality | any | 否 | 在指定图片格式为image/jpeg或image/webp的情况下，可以从0到1的区间内选择图片的质量，取值范围[0, 1]。如果超出取值范围，将会使用默认值0.92。  异常值undefined、null、NaN和Infinity按默认值处理。  默认值：0.92 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 图像的URL地址。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct ToDataURL {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(100, 100);
  @State dataURL: string = "";

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width(100)
        .height(100)
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          offContext.fillRect(0, 0, 100, 100)
          this.dataURL = offContext.toDataURL()
        })
      Text(this.dataURL)
    }
    .width('100%')
    .height('100%')
    .backgroundColor('#ffff00')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/W9ty5SAbQHSCckflNq7LUg/zh-cn_image_0000002742125279.png)

## transferToImageBitmap

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

```ts
// xxx.ets
@Entry
@Component
struct PutImageData {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private offCanvas: OffscreenCanvas = new OffscreenCanvas(600, 600);

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .backgroundColor('rgb(213,213,213)')
        .onReady(() => {
          let offContext = this.offCanvas.getContext("2d", this.settings)
          let imageData = offContext.createImageData(100, 100)
          for (let i = 0; i < imageData.data.length; i += 4) {
            imageData.data[i + 0] = 112
            imageData.data[i + 1] = 112
            imageData.data[i + 2] = 112
            imageData.data[i + 3] = 255
          }
          offContext.putImageData(imageData, 10, 10)
          let image = this.offCanvas.transferToImageBitmap()
          this.context.transferFromImageBitmap(image)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/XX4JCFI_Tp27O2TenQKdng/zh-cn_image_0000002712246372.png)
