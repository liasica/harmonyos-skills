---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-shape
title: @ohos.arkui.shape (形状)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.shape (形状)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:32+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:1e72dead0336bce3f2aca259d67f8906e80d498fc01961b0e471ae88d33e90bf
---

在[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape12)和[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)接口中可以传入对应的形状。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { CircleShape, EllipseShape, PathShape, RectShape } from "@kit.ArkUI";
```

## CircleShape

PhonePC/2in1TabletTVWearable

用于clipShape和maskShape接口的圆形形状。

继承自[BaseShape](js-apis-arkui-shape.md#baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ShapeSize)

创建CircleShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShapeSize](js-apis-arkui-shape.md#shapesize) | 否 | 形状的大小。 |

## EllipseShape

PhonePC/2in1TabletTVWearable

用于clipShape和maskShape接口的椭圆形状。

继承自[BaseShape](js-apis-arkui-shape.md#baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: ShapeSize)

创建EllipseShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ShapeSize](js-apis-arkui-shape.md#shapesize) | 否 | 形状的大小。 |

## PathShape

PhonePC/2in1TabletTVWearable

用于clipShape和maskShape接口的路径。

继承自[CommonShapeMethod](js-apis-arkui-shape.md#commonshapemethod)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: PathShapeOptions)

创建PathShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PathShapeOptions](js-apis-arkui-shape.md#pathshapeoptions) | 否 | 路径参数。 |

### commands

PhonePC/2in1TabletTVWearable

commands(commands: string): PathShape

设置路径的绘制指令。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| commands | string | 是 | 路径的绘制指令。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PathShape](js-apis-arkui-shape.md#pathshape) | 返回PathShape对象。 |

## RectShape

PhonePC/2in1TabletTVWearable

用于clipShape和maskShape接口的矩形形状。

继承自[BaseShape](js-apis-arkui-shape.md#baseshape)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(options?: RectShapeOptions | RoundRectShapeOptions)

创建RectShape对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [RectShapeOptions](js-apis-arkui-shape.md#rectshapeoptions) | [RoundRectShapeOptions](js-apis-arkui-shape.md#roundrectshapeoptions) | 否 | 矩形形状参数。 |

### radiusWidth

PhonePC/2in1TabletTVWearable

radiusWidth(rWidth: number | string): RectShape

设置矩形形状圆角半径的宽度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rWidth | number | string | 是 | 矩形形状圆角半径的宽度。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectShape](js-apis-arkui-shape.md#rectshape) | 返回RectShape对象。 |

### radiusHeight

PhonePC/2in1TabletTVWearable

radiusHeight(rHeight: number | string): RectShape

设置矩形形状圆角半径的高度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rHeight | number | string | 是 | 矩形形状圆角半径的高度。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectShape](js-apis-arkui-shape.md#rectshape) | 返回RectShape对象。 |

### radius

PhonePC/2in1TabletTVWearable

radius(radius: number | string | Array<number | string>): RectShape

设置矩形形状的圆角半径。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | string | Array<number | string> | 是 | 矩形形状的圆角半径。仅接受数组的前四个元素，分别为矩形左上，右上，左下，右下的圆角半径。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RectShape](js-apis-arkui-shape.md#rectshape) | 返回RectShape对象。 |

## ShapeSize

PhonePC/2in1TabletTVWearable

形状的尺寸参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width | number | string | 否 | 是 | 形状的宽度。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |
| height | number | string | 否 | 是 | 形状的高度。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |

## PathShapeOptions

PhonePC/2in1TabletTVWearable

PathShape的构造函数参数。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| commands | string | 否 | 是 | 绘制路径的指令。更多说明请参考commands支持的[绘制命令](ts-drawing-components-path.md#commands)。 |

## RectShapeOptions

PhonePC/2in1TabletTVWearable

RectShape 的构造函数参数。

继承自[ShapeSize](js-apis-arkui-shape.md#shapesize)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number | string | Array<number | string> | 否 | 是 | 矩形形状的圆角半径。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |

## RoundRectShapeOptions

PhonePC/2in1TabletTVWearable

RectShape 带有半径的构造函数参数。

继承自[ShapeSize](js-apis-arkui-shape.md#shapesize)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radiusWidth | number | string | 否 | 是 | 矩形形状圆角半径的宽度。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |
| radiusHeight | number | string | 否 | 是 | 矩形形状圆角半径的高度。  类型为number时取值范围是[0, +∞)，string时是[Length](ts-types.md#length)。  单位：vp  取值为异常值时按照0vp处理。 |

## BaseShape

PhonePC/2in1TabletTVWearable

继承自[CommonShapeMethod](js-apis-arkui-shape.md#commonshapemethod)。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### width

PhonePC/2in1TabletTVWearable

width(width: Length): T

设置形状的宽度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Length](ts-types.md#length) | 是 | 形状的宽度。  单位：vp  取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### height

PhonePC/2in1TabletTVWearable

height(height: Length): T

设置形状的高度。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| height | [Length](ts-types.md#length) | 是 | 形状的高度。  单位：vp  取值为异常值时按照0vp处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### size

PhonePC/2in1TabletTVWearable

size(size: SizeOptions): T

设置形状的大小。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [SizeOptions](ts-types.md#sizeoptions) | 是 | 形状的大小。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## CommonShapeMethod

PhonePC/2in1TabletTVWearable

常见的形状方法。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### offset

PhonePC/2in1TabletTVWearable

offset(offset: Position): T

设置相对于组件布局位置的坐标偏移。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | [Position](ts-types.md#position) | 是 | 相对于组件布局位置的坐标偏移。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### fill

PhonePC/2in1TabletTVWearable

fill(color: ResourceColor): T

设置形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 形状的填充区域的透明度，黑色表示完全透明，白色表示完全不透明。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

### position

PhonePC/2in1TabletTVWearable

position(position: Position): T

设置形状的位置。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](ts-types.md#position) | 是 | 设置形状的位置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前对象。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示通过[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape12)和[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)将图片裁剪和遮罩成不同形状。

```
1. import { CircleShape, EllipseShape, PathShape, RectShape } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ShapeExample {
6. build() {
7. Column({ space: 15 }) {
8. Text('CircleShape, position').fontSize(20).width('75%').fontColor('#DCDCDC')
9. // $r('app.media.startIcon')需替换为开发者所需的资源文件
10. Image($r('app.media.startIcon'))
11. .clipShape(new CircleShape({ width: '280px', height: '280px' }).position({ x: '20px', y: '20px' }))
12. .width('500px').height('280px')

14. Text('EllipseShape, offset').fontSize(20).width('75%').fontColor('#DCDCDC')
15. // $r('app.media.startIcon')需替换为开发者所需的资源文件
16. Image($r('app.media.startIcon'))
17. .clipShape(new EllipseShape({ width: '350px', height: '280px' }).offset({ x: '10px', y: '10px' }))
18. .width('500px').height('280px')

20. Text('PathShape, fill').fontSize(20).width('75%').fontColor('#DCDCDC')
21. // $r('app.media.startIcon')需替换为开发者所需的资源文件
22. Image($r('app.media.startIcon'))
23. .maskShape(new PathShape().commands('M100 0 L200 240 L0 240 Z').fill(Color.Red))
24. .width('500px').height('280px')

26. Text('RectShape, width, height, fill').fontSize(20).width('75%').fontColor('#DCDCDC')
27. // $r('app.media.startIcon')需替换为开发者所需的资源文件
28. Image($r('app.media.startIcon'))
29. .maskShape(new RectShape().width('350px').height('280px').fill(Color.Red))
30. .width('500px').height('280px')
31. }
32. .width('100%')
33. .margin({ top: 15 })
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/tSDJAD09Rk-GboCEKPIs5Q/zh-cn_image_0000002558765924.png?HW-CC-KV=V1&HW-CC-Date=20260429T055030Z&HW-CC-Expire=86400&HW-CC-Sign=C3EA2EAE8F9B886F7358620CF5F5878E1F9A198CB627EC6705831CFB5D12D85B)
