---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sharp-clipping
title: 形状裁剪
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 形状裁剪
category: harmonyos-references
scraped_at: 2026-09-02T15:00:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d6edc69011650d60c4005ac8e42aff1293a9076a17adf9234f3a2ca67704a08b
---

用于对组件进行裁剪、遮罩处理。

**说明** 

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## clip12+

clip(value: boolean): T

是否对子组件超出当前组件范围外的区域进行裁剪。设置value为true时，子组件超出当前组件范围外的区域将被裁剪不可见；设置value为false时，不对子组件进行裁剪。未设置时，默认不对子组件超出当前组件范围外的区域进行裁剪。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置子组件是否按照当前组件边缘轮廓进行裁剪。  true表示子组件按照当前组件边缘轮廓进行裁剪，false表示不对子组件进行裁剪。  **说明：** 设置为true后，子组件超出当前组件范围外的区域将不响应绑定的手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## clip18+

clip(clip: Optional<boolean>): T

是否对子组件超出当前组件范围外的区域进行裁剪。未设置时，默认不对子组件超出当前组件范围外的区域进行裁剪。与[clip12+](ts-universal-attributes-sharp-clipping.md#clip12)相比，新增了对undefined类型的支持。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clip | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置子组件是否按照当前组件边缘轮廓进行裁剪。true表示子组件按照当前组件边缘轮廓进行裁剪，false表示不对子组件进行裁剪。  **说明：** 设置为true后，子组件超出当前组件范围外的区域将不响应绑定的手势事件。  当clip的值为undefined时，恢复为不对子组件超出当前组件范围外的区域进行裁剪。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## clip(deprecated)

clip(value: boolean | CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute): T

按指定的形状对当前组件进行裁剪，或设置是否按照当前组件边缘轮廓进行裁剪。

**说明** 

从API version 7开始支持，从API version 12开始废弃，建议使用[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | [CircleAttribute](ts-drawing-components-circle.md) | [EllipseAttribute](ts-drawing-components-ellipse.md) | [PathAttribute](ts-drawing-components-path.md) | [RectAttribute](ts-drawing-components-rect.md) | 是 | 参数为相应类型的组件，按指定的形状对当前组件和子组件进行裁剪；参数为boolean类型时，设置是否按照当前组件边缘轮廓进行裁剪。  默认值：false  true表示按当前组件边缘轮廓进行裁剪，false表示不进行裁剪。  **说明：** 参数为对应类型的组件时，裁剪不会导致被裁剪区域无法响应绑定的手势事件。参数为boolean类型时，裁剪会导致被裁剪区域无法响应绑定的手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## clipShape12+

clipShape(value: CircleShape | EllipseShape | PathShape | RectShape): T

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪，将组件超出形状范围外的区域裁剪掉使其不可见。与[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)不同，clipShape是将组件超出形状范围外的区域裁剪掉（不可见），而maskShape是在组件上叠加指定形状的遮罩覆盖层。

**说明** 

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。

形状中的[fill](js-apis-arkui-shape.md#fill)属性对clipShape接口不生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12) | 是 | 参数为相应类型的组件，按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。  **说明：** 裁剪不会导致被裁剪区域无法响应绑定的手势事件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## clipShape18+

clipShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T

按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。与[clipShape12+](ts-universal-attributes-sharp-clipping.md#clipshape12)相比，新增了对undefined类型的支持。

**说明** 

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。

形状中的[fill](js-apis-arkui-shape.md#fill)属性对clipShape接口不生效。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shape | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12)> | 是 | 参数为相应类型的组件，按指定的形状（形状中可包含位置信息）对当前组件进行裁剪。  **说明：** 裁剪不会导致被裁剪区域无法响应绑定的手势事件。  当shape的值为undefined时，恢复为不添加指定形状的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## CircleShape12+

type CircleShape = import('../api/@ohos.arkui.shape').CircleShape

导入CircleShape类型对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.shape').[CircleShape](js-apis-arkui-shape.md#circleshape) | 圆形形状。 |

## EllipseShape12+

type EllipseShape = import('../api/@ohos.arkui.shape').EllipseShape

导入EllipseShape类型对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.shape').[EllipseShape](js-apis-arkui-shape.md#ellipseshape) | 椭圆形状。 |

## PathShape12+

type PathShape = import('../api/@ohos.arkui.shape').PathShape

导入PathShape类型对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.shape').[PathShape](js-apis-arkui-shape.md#pathshape) | 路径形状。 |

## RectShape12+

type RectShape = import('../api/@ohos.arkui.shape').RectShape

导入RectShape类型对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| import('../api/@ohos.arkui.shape').[RectShape](js-apis-arkui-shape.md#rectshape) | 矩形形状。 |

## mask12+

mask(value: ProgressMask): T

为组件添加可调节进度的遮罩，遮罩覆盖在组件内容上方，通过进度值控制遮罩的显示范围。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ProgressMask](ts-universal-attributes-sharp-clipping.md#progressmask10) | 是 | 在当前组件上加上可动态设置进度、最大值和颜色的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## mask18+

mask(mask: Optional<ProgressMask>): T

为组件添加可调节进度的遮罩，遮罩覆盖在组件内容上方，通过进度值控制遮罩的显示范围。与[mask12+](ts-universal-attributes-sharp-clipping.md#mask12)相比，新增了对undefined类型的支持。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mask | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ProgressMask](ts-universal-attributes-sharp-clipping.md#progressmask10)> | 是 | 在当前组件上加上可动态设置进度和颜色的遮罩。遮罩的最大值(total)在构造ProgressMask对象时设定，不可动态修改。可通过ProgressMask对象的updateProgress()方法更新进度值、updateColor()方法更新颜色、enableBreathingAnimation()方法开关呼吸光晕动画。  当mask的值为undefined时，恢复为无进度遮罩效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## mask(deprecated)

mask(value: CircleAttribute | EllipseAttribute | PathAttribute | RectAttribute | ProgressMask): T

为组件添加指定形状或可调节进度的遮罩。

**说明** 

从API version 7开始支持，从API version 12开始废弃，建议使用[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)替代。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CircleAttribute](ts-drawing-components-circle.md) | [EllipseAttribute](ts-drawing-components-ellipse.md) | [PathAttribute](ts-drawing-components-path.md) | [RectAttribute](ts-drawing-components-rect.md) | [ProgressMask](ts-universal-attributes-sharp-clipping.md#progressmask10)10+ | 是 | 参数为对应形状类型的组件时，在当前组件上加上指定形状的遮罩（圆形、椭圆、路径或矩形）；参数为ProgressMask时，在当前组件上加上可动态设置进度和颜色的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## maskShape12+

maskShape(value: CircleShape | EllipseShape | PathShape | RectShape): T

为组件添加指定形状的遮罩，在组件上叠加指定形状的覆盖层。

**说明** 

* 不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。
* 路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。
* 形状中的fill属性对maskShape接口生效，用于设置遮罩的颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12) | 是 | 在当前组件上加上指定形状的遮罩或可调节进度的遮罩。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## maskShape18+

maskShape(shape: Optional<CircleShape | EllipseShape | PathShape | RectShape>): T

为组件添加指定形状的遮罩，在组件上叠加指定形状的覆盖层。与[maskShape12+](ts-universal-attributes-sharp-clipping.md#maskshape12)相比，新增了对undefined类型的支持。

**说明** 

不同的形状支持的属性范围不同，路径是一种形状，除此之外还有椭圆、矩形等形状。

路径的形状不支持设置宽度和高度。具体形状支持的属性参考具体形状的文档。

形状中的fill属性对maskShape接口生效，用于设置遮罩的颜色。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shape | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[CircleShape](ts-universal-attributes-sharp-clipping.md#circleshape12) | [EllipseShape](ts-universal-attributes-sharp-clipping.md#ellipseshape12) | [PathShape](ts-universal-attributes-sharp-clipping.md#pathshape12) | [RectShape](ts-universal-attributes-sharp-clipping.md#rectshape12)> | 是 | 参数为对应形状类型的组件时，在当前组件上加上指定形状的遮罩（圆形、椭圆、路径或矩形）；参数为ProgressMask时，在当前组件上加上可动态设置进度、最大值和颜色的遮罩。  当shape的值为undefined时，会重置当前值，恢复为无指定形状遮罩效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于链式调用。 |

## ProgressMask10+

ProgressMask用于设置遮罩的进度、最大值和颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor10+

constructor(value: number, total: number, color: ResourceColor)

构造ProgressMask对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 进度遮罩的当前值，与total配合使用确定进度比例，当value等于total时表示进度满。  取值范围：[0.0, +∞)。传入负数时自动修正为0。 |
| total | number | 是 | 进度遮罩的最大值。  取值范围：[0.0, +∞)。传入负数时自动修正为100。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 进度遮罩的颜色。 |

### updateProgress10+

updateProgress(value: number): void

更新进度遮罩的进度值。

**使用说明：**

* 需先通过[mask()](ts-universal-attributes-sharp-clipping.md#mask12)方法将ProgressMask对象应用到组件上，调用此方法后遮罩的进度值会动态更新。
* 若ProgressMask尚未通过mask()方法应用到组件，调用此方法仅更新ProgressMask对象的内部状态，不会产生可见的遮罩效果变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 进度遮罩的当前值。  取值范围：[0.0, +∞)。传入负数时自动修正为0。 |

### updateColor10+

updateColor(value: ResourceColor): void

更新进度遮罩的颜色。

**使用说明：**

* 需先通过[mask()](ts-universal-attributes-sharp-clipping.md#mask12)方法将ProgressMask对象应用到组件上，调用此方法后遮罩颜色会动态更新。
* 若ProgressMask尚未通过mask()方法应用到组件，调用此方法仅更新ProgressMask对象的内部状态，不会产生可见的遮罩效果变化。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 进度遮罩的颜色。 |

### enableBreathingAnimation12+

enableBreathingAnimation(value: boolean): void

进度满时的呼吸光晕动画开关，开启后进度满时遮罩边缘会出现周期性明暗变化的发光效果。未设置时，默认关闭呼吸光晕动画。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否开启进度满时的呼吸光晕动画。  true：开启呼吸光晕动画。  false：关闭呼吸光晕动画。 |

## 示例

### 示例1（使用不同裁剪属性）

该示例通过[clipShape](ts-universal-attributes-sharp-clipping.md#clipshape12)、[clip](ts-universal-attributes-sharp-clipping.md#clip12)、[maskShape](ts-universal-attributes-sharp-clipping.md#maskshape12)实现图片的裁剪和遮罩。

```ts
// xxx.ets
import { CircleShape, RectShape } from '@kit.ArkUI';

@Entry
@Component
struct ClipAndMaskExample {
  build() {
    Column({ space: 15 }) {
      Text('clip').fontSize(12).width('75%').fontColor('#DCDCDC')
      Row() {
        // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
        Image($r('app.media.testImg')).width('500px').height('280px')
      }
      .clip(true) // 如这里不设置clip为true，则Row组件的圆角不会限制其中的Image组件，Image组件的四个角会超出Row
      .borderRadius(20)

      // 用一个280px直径的圆对图片进行裁剪
      // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.testImg'))
        .clipShape(new CircleShape({ width: '280px', height: '280px' }))
        .width('500px').height('280px')

      Text('mask').fontSize(12).width('75%').fontColor('#DCDCDC')
      // 给图片添加了一个500px*280px的方形遮罩
      // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.testImg'))
        .maskShape(new RectShape({ width: '500px', height: '280px' }).fill(Color.Gray))
        .width('500px').height('280px')

      // 给图片添加了一个280px*280px的圆形遮罩
      // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.testImg'))
        .maskShape(new CircleShape({ width: '280px', height: '280px' }).fill(Color.Gray))
        .width('500px').height('280px')
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qo1y0vnVQ7SRCZ6LywvYFQ/zh-cn_image_0000002706675712.png)

### 示例2（实现组件遮罩）

该示例通过[mask](ts-universal-attributes-sharp-clipping.md#mask12)实现图片的遮罩。

```ts
@Entry
@Component
struct ProgressMaskExample {
  @State isRedColor: boolean = true;
  @State value: number = 10.0;
  @State enableBreathingAnimation: boolean = false;
  @State progress: ProgressMask = new ProgressMask(10.0, 100.0, Color.Gray);

  build() {
    Column({ space: 15 }) {
      Text('progress mask').fontSize(12).width('75%').fontColor('#DCDCDC')
      // 给图片添加了一个进度遮罩
      // $r("app.media.testImg")需要替换为开发者所需的图像资源文件。
      Image($r('app.media.testImg'))
        .width('500px').height('280px')
        .mask(this.progress)
        .animation({
          duration: 2000, // 动画时长
          curve: Curve.Linear, // 动画曲线
          delay: 0, // 动画延迟
          iterations: 1, // 播放次数
          playMode: PlayMode.Normal // 动画模式
        }) // 对Image组件的遮罩进度变化进行动画配置

      // 更新进度遮罩的进度值
      Button('updateProgress')
        .onClick((event?: ClickEvent) => {
          this.value += 10;
          this.progress.updateProgress(this.value);
        }).width(200).height(50).margin(20)

      // 更新进度遮罩的颜色
      Button('updateColor')
        .onClick((event?: ClickEvent) => {
          if (this.isRedColor) {
            this.progress.updateColor(0x9fff0000);
          } else {
            this.progress.updateColor(0x9f0000ff);
          }
          this.isRedColor = !this.isRedColor;
        }).width(200).height(50).margin(20)

      // 开关呼吸光晕动画
      Button('enableBreathingAnimation:' + this.enableBreathingAnimation)
        .onClick((event?: ClickEvent) => {
          this.enableBreathingAnimation = !this.enableBreathingAnimation;
          this.progress.enableBreathingAnimation(this.enableBreathingAnimation);
        }).width(200).height(50).margin(20)

      // 恢复进度遮罩
      Button('click reset')
        .onClick((event?: ClickEvent) => {
          this.value = 0;
          this.progress.updateProgress(this.value);
        }).width(200).height(50).margin(20)
    }
    .width('100%')
    .margin({ top: 15 })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/LkLEIIYLR4aN95g3wbbtAg/zh-cn_image_0000002736434799.gif)
