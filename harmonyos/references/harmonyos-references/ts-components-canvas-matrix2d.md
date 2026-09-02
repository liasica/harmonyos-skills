---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-canvas-matrix2d
title: Matrix2D
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 画布绘制 > Matrix2D
category: harmonyos-references
scraped_at: 2026-09-02T15:01:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:073ed67881b7c8af04133947c878c054389a9f32d5249bb2beaf49e698f06cfe
---

用于[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)、[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)、[CanvasPattern](ts-components-canvas-canvaspattern.md)和[Path2D](ts-components-canvas-path2d.md)图形变换的矩阵对象，可以对矩阵进行缩放、旋转和平移等变换。

Matrix2D的使用场景包括：

1. [CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)和[OffscreenCanvasRenderingContext2D](ts-offscreencanvasrenderingcontext2d.md)中调用[getTransform](ts-components-canvas-common-method.md#gettransform)接口获取画布的图形变换矩阵Matrix2D对象，调用[setTransform](ts-components-canvas-common-method.md#settransform-1)接口对后续绘制内容进行Matrix2D对象对应的图形变换。
2. [CanvasPattern](ts-components-canvas-canvaspattern.md)中调用[setTransform](ts-components-canvas-canvaspattern.md#settransform)接口对[CanvasPattern](ts-components-canvas-canvaspattern.md)对象进行Matrix2D对象对应的图形变换。
3. [Path2D](ts-components-canvas-path2d.md)中调用[addPath](ts-components-canvas-path2d.md#addpath)接口对[Path2D](ts-components-canvas-path2d.md)对象进行Matrix2D对象对应的图形变换。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## constructor10+

constructor()

构造二维变换矩阵对象，默认值是属性全为0的矩阵。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor12+

constructor(unit: LengthMetricsUnit)

构造二维变换矩阵对象，默认值是属性全为0的矩阵，支持配置Matrix2D对象的单位模式。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 用来配置Matrix2D对象的单位模式，配置后无法动态更改，配置方法同[CanvasRenderingContext2D](ts-canvasrenderingcontext2d.md)。  默认值：DEFAULT  异常值NaN和Infinity按默认值处理。 |

## 属性

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| scaleX | number | 否 | 是 | 水平缩放系数，取值范围无限制。值大于1时放大，小于1时缩小，负值时水平翻转。  默认值：1  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| scaleY | number | 否 | 是 | 垂直缩放系数，取值范围无限制。值大于1时放大，小于1时缩小，负值时垂直翻转。  默认值：1  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| rotateX | number | 否 | 是 | 水平倾斜系数，取值范围无限制。  默认值：0  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| rotateY | number | 否 | 是 | 垂直倾斜系数，取值范围无限制。  默认值：0  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。 |
| translateX | number | 否 | 是 | 水平平移距离，取值范围无限制。  默认值：0  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。  默认单位：vp |
| translateY | number | 否 | 是 | 垂直平移距离，取值范围无限制。  默认值：0  异常值undefined按无效值处理，NaN和Infinity会导致Matrix2D异常，设置后绘制内容不显示。  默认单位：vp |

**说明** 

可使用[px2vp](arkts-apis-uicontext-uicontext.md#px2vp12)接口进行单位转换。

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Parameter {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 20, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/SyUy3kWmTByG3LUUn30mew/zh-cn_image_0000002736435267.png)

## identity

identity(): Matrix2D

创建单位矩阵。常用于重置变换矩阵，清除之前的所有变换操作，使后续绘制内容不受之前的变换影响。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 单位矩阵，可用于初始化或重置图形变换状态。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Identity {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 20, 50, 50)
          this.matrix = this.matrix.identity()
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 100, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/5vy4eFZAQ1abBRwz69ptyw/zh-cn_image_0000002706836120.png)

## invert

invert(): Matrix2D

获取当前矩阵的逆矩阵。常用于撤销之前的变换操作，或计算反向变换，实现坐标系的反向映射。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 逆矩阵结果，可用于反向变换或撤销之前的变换操作。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Invert {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(100, 110, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.invert()
          this.context.setTransform(this.matrix)
          this.context.fillRect(100, 110, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/Rm0rxIoQSNyfZfveR04m9A/zh-cn_image_0000002736315225.png)

## multiply(deprecated)

multiply(other?: Matrix2D): Matrix2D

当前矩阵与目标矩阵相乘。此接口为空接口，无实际效果。

该接口从API version 10开始废弃，且无实际绘制效果，故不提供示例。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| other | Matrix2D | 否 | 目标矩阵。  异常值undefined和null按无效值处理。  默认值：null |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 此接口为空实现，返回值无实际意义。 |

## rotate(deprecated)

rotate(rx?: number, ry?: number): Matrix2D

对当前矩阵进行旋转运算。此接口为空接口，无实际效果。

**说明** 

从API version 8开始支持，从API version 10开始废弃。建议使用[rotate](ts-components-canvas-matrix2d.md#rotate10)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。该接口为空接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。  默认单位：vp  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：0 |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。  默认单位：vp  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象，可用于对图形进行旋转变换。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(50, 110, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.rotate(5, 5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(50, 110, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/9F9IpeiDQ3CuLKNZCE_U-w/zh-cn_image_0000002706676182.png)

## rotate10+

rotate(degree: number, rx?: number, ry?: number): Matrix2D

以旋转点为中心，对当前矩阵进行左乘旋转运算。常用于图形旋转动画或图片旋转处理等场景。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | number | 是 | 旋转角度（弧度值），取值范围无限制。顺时针方向为正值，可以通过角度 \* Math.PI / 180将角度转换为弧度值传入该接口。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：弧度 |
| rx | number | 否 | 旋转点的水平方向坐标，取值范围无限制。  默认单位：vp  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：0 |
| ry | number | 否 | 旋转点的垂直方向坐标，取值范围无限制。  默认单位：vp  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 旋转后结果矩阵对象，可用于对图形进行旋转变换。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Rotate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(60, 80, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.rotate(-60 * Math.PI / 180, 5, 5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(60, 80, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/agd-TfjZTHuUj9I9zK_BRQ/zh-cn_image_0000002736435269.png)

## translate

translate(tx?: number, ty?: number): Matrix2D

对当前矩阵进行左乘平移运算。常用于调整图形位置、实现位移动画或偏移画布坐标系等场景。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tx | number | 否 | 水平方向平移距离，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：vp  默认值：0 |
| ty | number | 否 | 垂直方向平移距离，取值范围无限制。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认单位：vp  默认值：0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 平移后结果矩阵对象，可用于对图形进行平移变换。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Translate {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(40, 20, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = 0
          this.matrix.rotateY = 0
          this.matrix.translateX = 0
          this.matrix.translateY = 0
          this.matrix.translate(100, 100)
          this.context.setTransform(this.matrix)
          this.context.fillRect(40, 20, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/WHAfv6afQ0KLCr4S1OUmuQ/zh-cn_image_0000002706836122.png)

## scale

scale(sx?: number, sy?: number): Matrix2D

对当前矩阵进行左乘缩放运算。常用于图形放大缩小或翻转等场景。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sx | number | 否 | 水平缩放比例系数，取值范围无限制。值大于1时放大，小于1时缩小，负值时水平翻转。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：1.0 |
| sy | number | 否 | 垂直缩放比例系数，取值范围无限制。值大于1时放大，小于1时缩小，负值时垂直翻转。  异常值undefined和null按无效值处理，NaN和Infinity会导致Matrix2D异常。  默认值：1.0 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix2D | 缩放结果矩阵对象，可用于对图形进行缩放变换。 |

**示例：**

```ts
// xxx.ets
@Entry
@Component
struct Scale {
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  private matrix: Matrix2D = new Matrix2D();

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Canvas(this.context)
        .width('240vp')
        .height('180vp')
        .backgroundColor('#ffff00')
        .onReady(() => {
          this.context.fillRect(120, 70, 50, 50)
          this.matrix.scaleX = 1
          this.matrix.scaleY = 1
          this.matrix.rotateX = -0.5
          this.matrix.rotateY = 0.5
          this.matrix.translateX = 10
          this.matrix.translateY = 10
          this.matrix.scale(0.5, 0.5)
          this.context.setTransform(this.matrix)
          this.context.fillRect(120, 70, 50, 50)
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/QPfRh5M2Re28BYow4HbC6Q/zh-cn_image_0000002736315227.png)
