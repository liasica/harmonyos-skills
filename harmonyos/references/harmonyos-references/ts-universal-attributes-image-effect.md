---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect
title: 图像效果
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 图像效果
category: harmonyos-references
scraped_at: 2026-04-28T08:01:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:33db2e7e4ce413b1cca36a0df5947cdde3b576a71d5b061742cfc3a869a65028
---

设置组件的模糊、阴影、球面效果以及设置图片的图像效果。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## blur

PhonePC/2in1TabletTVWearable

blur(value: number, options?: BlurOptions): T

为组件添加内容模糊效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 当前组件添加内容模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。 |
| options11+ | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 灰阶模糊参数。对图像中的黑白色进行色阶调整，使其趋于灰色更为柔和美观，对图像中的彩色调整没有效果。  默认值：grayscale: [0,0] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## blur18+

PhonePC/2in1TabletTVWearable

blur(blurRadius: Optional<number>, options?: BlurOptions): T

为组件添加内容模糊效果。与[blur](ts-universal-attributes-image-effect.md#blur)相比，blurRadius参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 当前组件添加内容模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。  当blurRadius的值为undefined时，维持之前取值。 |
| options | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 灰阶模糊参数。对图像中的黑白色进行色阶调整，使其趋于灰色更为柔和美观，对图像中的彩色调整没有效果。  默认值：grayscale: [0,0] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## blur19+

PhonePC/2in1TabletTVWearable

blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T

为组件添加内容模糊效果。与[blur18+](ts-universal-attributes-image-effect.md#blur18)相比，新增了sysOptions参数，即支持系统自适应调节参数。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 当前组件添加内容模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。  当blurRadius的值为undefined时，维持之前取值。 |
| options | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 灰阶模糊参数。对图像中的黑白色进行色阶调整，使其趋于灰色更为柔和美观，对图像中的彩色调整没有效果。  默认值：grayscale: [0,0] |
| sysOptions | [SystemAdaptiveOptions](ts-universal-attributes-background.md#systemadaptiveoptions19) | 否 | 系统自适应调节参数。  默认值：{ disableSystemAdaptation: false } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## shadow

PhonePC/2in1TabletTVWearable

shadow(value: ShadowOptions | ShadowStyle): T

为组件添加阴影效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用，ArkTS卡片上不支持参数为 [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明)类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明)10+ | 是 | 为当前组件添加阴影效果。  入参类型为ShadowOptions时，可以指定模糊半径、阴影的颜色、X轴和Y轴的偏移量。  入参类型为ShadowStyle时，可指定不同阴影样式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## shadow18+

PhonePC/2in1TabletTVWearable

shadow(options: Optional<ShadowOptions | ShadowStyle>): T

为组件添加阴影效果。与[shadow](ts-universal-attributes-image-effect.md#shadow)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用，ArkTS卡片上不支持参数为[ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明)类型。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[ShadowOptions](ts-universal-attributes-image-effect.md#shadowoptions对象说明) | [ShadowStyle](ts-universal-attributes-image-effect.md#shadowstyle10枚举说明)> | 是 | 为当前组件添加阴影效果。  入参类型为ShadowOptions时，可以指定模糊半径、阴影的颜色、X轴和Y轴的偏移量。  入参类型为ShadowStyle时，可指定不同阴影样式。  当options的值为undefined时，恢复为无样式的阴影效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## grayscale

PhonePC/2in1TabletTVWearable

grayscale(value: number): T

为组件添加灰度效果。上层渲染灰度会覆盖下层子组件渲染。不通过该接口设置时，默认无变化。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 为当前组件添加灰度效果。值定义为灰度转换的比例，入参1.0则完全转为灰度图像，入参0.0则图像无变化，入参在0.0和1.0之间时，效果呈线性变化。  取值范围：[0.0, 1.0]  **说明：**  设置小于0.0的值时，按值为0.0处理，设置大于1.0的值时，按值为1.0处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## grayscale18+

PhonePC/2in1TabletTVWearable

grayscale(grayscale: Optional<number>): T

为组件添加灰度效果。上层渲染灰度会覆盖下层子组件渲染。不通过该接口设置时，默认无变化。与[grayscale](ts-universal-attributes-image-effect.md#grayscale)相比，grayscale参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| grayscale | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 为当前组件添加灰度效果。值定义为灰度转换的比例，入参1.0则完全转为灰度图像，入参0.0则图像无变化，入参在0.0和1.0之间时，效果呈线性变化。  取值范围：[0.0, 1.0]  **说明：**  设置小于0.0的值时，按值为0.0处理，设置大于1.0的值时，按值为1.0处理。  当grayscale的值为undefined时，取默认值0.0。恢复为无灰度效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## brightness

PhonePC/2in1TabletTVWearable

brightness(value: number): T

为组件添加高光效果。不通过该接口设置时，默认无变化。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 为当前组件添加高光效果，入参为高光比例，值为1时没有效果，小于1时亮度变暗，小于或等于0为全黑，大于1时亮度增加，数值越大亮度越大，亮度大于或等于2时会变为全白。  取值范围：[0, +∞)  推荐取值范围：[0, 2]  **说明：**  设置小于0的值时，按值为0处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## brightness18+

PhonePC/2in1TabletTVWearable

brightness(brightness: Optional<number>): T

为组件添加高光效果。不通过该接口设置时，默认无变化。与[brightness](ts-universal-attributes-image-effect.md#brightness)相比，brightness参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 为当前组件添加高光效果，入参为高光比例，值为1时没有效果，小于1时亮度变暗，小于或等于0为全黑，大于1时亮度增加，数值越大亮度越大，亮度大于或等于2时会变为全白。  取值范围：[0, +∞)  推荐取值范围：[0, 2]  **说明：**  设置小于0的值时，按值为0处理。  当brightness的值为undefined时，恢复为亮度为1的高光效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## saturate

PhonePC/2in1TabletTVWearable

saturate(value: number): T

为组件添加饱和度效果。不通过该接口设置时，默认无变化。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 为当前组件添加饱和度效果，饱和度为颜色中的含色成分和消色成分(灰)的比例，入参为1时，显示原图像，大于1时含色成分越大，饱和度越大，小于1时消色成分越大，饱和度越小。  推荐取值范围：[0, 50)  **说明：**  设置小于0的值时，按值为0处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## saturate18+

PhonePC/2in1TabletTVWearable

saturate(saturate: Optional<number>): T

为组件添加饱和度效果。不通过该接口设置时，默认无变化。与[saturate](ts-universal-attributes-image-effect.md#saturate)相比，saturate参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| saturate | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 为当前组件添加饱和度效果，饱和度为颜色中的含色成分和消色成分(灰)的比例，入参为1时，显示原图像，大于1时含色成分越大，饱和度越大，小于1时消色成分越大，饱和度越小。  推荐取值范围：[0, 50)  **说明：**  设置小于0的值时，按值为0处理。  当saturate的值为undefined时。恢复为饱和度为1的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## contrast

PhonePC/2in1TabletTVWearable

contrast(value: number): T

为组件添加对比度效果。不通过该接口设置时，默认无变化。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 为当前组件添加对比度效果，入参为对比度的值。值为1时，显示原图，大于1时，值越大对比度越高，图像越清晰醒目，小于1时，值越小对比度越低，当对比度为0时，图像变为全灰。  推荐取值范围：[0, 10)  **说明：**  设置小于0的值时，按值为0处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## contrast18+

PhonePC/2in1TabletTVWearable

contrast(contrast: Optional<number>): T

为组件添加对比度效果。不通过该接口设置时，默认无变化。与[contrast](ts-universal-attributes-image-effect.md#contrast)相比，contrast参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| contrast | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 为当前组件添加对比度效果，入参为对比度的值。值为1时，显示原图，大于1时，值越大对比度越高，图像越清晰醒目，小于1时，值越小对比度越低，当对比度为0时，图像变为全灰。  推荐取值范围：[0, 10)  **说明：**  设置小于0的值时，按值为0处理。  当contrast的值为undefined时，恢复为对比度为1的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## invert

PhonePC/2in1TabletTVWearable

invert(value: number | InvertOptions): T

反转输入的图像。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [InvertOptions](ts-universal-attributes-image-effect.md#invertoptions11对象说明)11+ | 是 | 反转输入的图像。  入参对象为number时。入参为图像反转的比例，值为1时完全反转，值为0则图像无变化。  取值范围：[0, 1]。  设置小于0的值时，按值为0处理。设置大于1的值时，按值为1处理。  入参对象为 InvertOptions时，对比背景颜色灰度值和阈值区间，背景颜色灰度值小于阈值区间时反色取high值，当背景颜色灰度值大于阈值区间时反色取low值，背景颜色灰度值在阈值区间内取值由high线性渐变到low。  **说明：**  number和InvertOptions两种形式的入参对应不同的反转效果。两种类型的入参切换时，不会清除之前已设置的反转效果，两种反转效果会同时存在，建议始终使用同一种形式的入参。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## invert18+

PhonePC/2in1TabletTVWearable

invert(options: Optional<number | InvertOptions>): T

反转输入的图像。与[invert](ts-universal-attributes-image-effect.md#invert)相比，options参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [InvertOptions](ts-universal-attributes-image-effect.md#invertoptions11对象说明)11+> | 是 | 反转输入的图像。  入参对象为number时。入参为图像反转的比例，值为1时完全反转，值为0则图像无变化。  取值范围：[0, 1]。  设置小于0的值时，按值为0处理。设置大于1的值时，按值为1处理。  入参对象为 InvertOptions时，对比背景颜色灰度值和阈值区间，背景颜色灰度值小于阈值区间时反色取high值，当背景颜色灰度值大于阈值区间时反色取low值，背景颜色灰度值在阈值区间内取值由high线性渐变到low。  当options的值为undefined时，恢复为图像无变化的效果。  **说明：**  number和InvertOptions两种形式的入参对应不同的反转效果。两种类型的入参切换时，不会清除之前已设置的反转效果，两种反转效果会同时存在，建议始终使用同一种形式的入参。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## sepia

PhonePC/2in1TabletTVWearable

sepia(value: number): T

将图像转换为深褐色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将图像转换为深褐色，降低色彩度，产生温暖复古的图像风格。入参为褐色滤镜强度，值为1则完全是深褐色的，值小于等于0则图像无变化，值大于1会进一步放大色彩偏移比例，图像整体会变得更亮且色彩更加偏黄/偏红，但不属于标准sepia效果。  取值范围：[0, +∞)，推荐取值范围：(0, 1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## sepia18+

PhonePC/2in1TabletTVWearable

sepia(sepia: Optional<number>): T

将图像转换为深褐色。与[sepia](ts-universal-attributes-image-effect.md#sepia)相比，sepia参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| sepia | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 将图像转换为深褐色，降低色彩度，产生温暖复古的图像风格。入参为褐色滤镜强度，值为1则完全是深褐色的，值小于等于0则图像无变化，值大于1会进一步放大色彩偏移比例，图像整体会变得更亮且色彩更加偏黄/偏红，但不属于标准sepia效果。  当sepia的值为undefined时，恢复为图像无变化的效果。  取值范围：[0, +∞)，推荐取值范围：(0, 1]。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## hueRotate

PhonePC/2in1TabletTVWearable

hueRotate(value: number | string): T

色相旋转效果。不通过该接口设置时，默认无变化。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | string | 是 | 色相旋转效果，输入参数为旋转角度。  取值范围：(-∞, +∞)  **说明：**  色调旋转360度会显示原始颜色。先将色调旋转180 度，然后再旋转-180度会显示原始颜色。数据类型为number时，值为90和'90deg'效果一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## hueRotate18+

PhonePC/2in1TabletTVWearable

hueRotate(rotation: Optional<number | string>): T

色相旋转效果。不通过该接口设置时，默认无变化。与[hueRotate](ts-universal-attributes-image-effect.md#huerotate)相比，rotation参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | string> | 是 | 色相旋转效果，输入参数为旋转角度。  取值范围：(-∞, +∞)  string需为数值字符串类型。  **说明：**  色调旋转360度会显示原始颜色。先将色调旋转180 度，然后再旋转-180度会显示原始颜色。数据类型为number时，值为90和'90deg'效果一致。  当rotation的值为undefined时，恢复为无色相旋转的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## colorBlend

PhonePC/2in1TabletTVWearable

colorBlend(value: Color | string | Resource): T

为组件添加颜色叠加效果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Color](ts-appendix-enums.md#color) | string | [Resource](ts-types.md#resource) | 是 | 为当前组件添加颜色叠加效果，入参为叠加的颜色字符串。取值可为string类型，如'0x000000'，'rgba(0,0,0,1)'。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## colorBlend18+

PhonePC/2in1TabletTVWearable

colorBlend(color: Optional<Color | string | Resource>): T

为组件添加颜色叠加效果。与[colorBlend](ts-universal-attributes-image-effect.md#colorblend)相比，color参数新增了对undefined类型的支持。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[Color](ts-appendix-enums.md#color) | string | [Resource](ts-types.md#resource)> | 是 | 为当前组件添加颜色叠加效果，入参为叠加的颜色。取值可为string类型，如'0x000000'，'rgba(0,0,0,1)'。  当color的值为undefined时，恢复为无颜色叠加的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## linearGradientBlur12+

PhonePC/2in1TabletTVWearable

linearGradientBlur(value: number, options: LinearGradientBlurOptions): T

为组件添加内容线性渐变模糊效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 为模糊半径，模糊半径越大越模糊，为0时不模糊。  取值范围：[0, 1000] |
| options | [LinearGradientBlurOptions](ts-universal-attributes-image-effect.md#lineargradientbluroptions12) | 是 | 设置线性渐变模糊效果。  线性渐变参数，包含模糊程度和模糊位置数组fractionStops，及渐变模糊方向direction。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## linearGradientBlur18+

PhonePC/2in1TabletTVWearable

linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T

为组件添加内容线性渐变模糊效果。与[linearGradientBlur12+](ts-universal-attributes-image-effect.md#lineargradientblur12)相比，新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 为模糊半径，模糊半径越大越模糊，为0时不模糊。  取值范围：[0, 1000]  当blurRadius的值为undefined时，恢复为渐变模糊为0的效果。 |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[LinearGradientBlurOptions](ts-universal-attributes-image-effect.md#lineargradientbluroptions12)> | 是 | 设置线性渐变模糊效果。  线性渐变参数，包含模糊程度和模糊位置数组fractionStops，及渐变模糊方向direction。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## renderGroup10+

PhonePC/2in1TabletTVWearable

renderGroup(value: boolean): T

设置是否组成节点组。节点组表示当前组件和子组件组成的子树先在离屏画布中渲染，再与父组件融合绘制。设置为节点组后，系统会缓存绘制结果，提升性能。但如果节点组内的组件频繁更新，缓存失效，可能导致性能下降。此外，设置为节点组后，当前组件的不透明度不为1时，绘制效果可能有差异。

不设置该属性时，默认不组成节点组。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前组件和子组件是否组成节点组。  false表示不组成节点组，不进行离屏渲染直接绘制。  true表示当前组件和子组件组成节点组，进行离屏渲染后再与父组件融合绘制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## renderGroup18+

PhonePC/2in1TabletTVWearable

renderGroup(isGroup: Optional<boolean>): T

设置是否组成节点组。节点组表示当前组件和子组件组成的子树先在离屏画布中渲染，再与父组件融合绘制。设置为节点组后，系统会缓存绘制结果，提升性能。但如果节点组内的组件频繁更新，缓存失效，可能导致性能下降。此外，设置为节点组后，当前组件的不透明度不为1时，绘制效果可能有差异。

与[renderGroup10+](ts-universal-attributes-image-effect.md#rendergroup10)相比，isGroup参数新增了对undefined类型的支持。

不设置该属性时，默认不组成节点组。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isGroup | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置当前组件和子组件是否组成节点组。  false表示不组成节点组，不进行离屏渲染直接绘制。  true表示当前组件和子组件组成节点组，进行离屏渲染后再与父组件融合绘制。  当isGroup的值为undefined时，按照不组成节点组处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## blendMode11+

PhonePC/2in1TabletTVWearable

blendMode(value: BlendMode, type?: BlendApplyType): T

将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlendMode](ts-universal-attributes-image-effect.md#blendmode11枚举说明) | 是 | 混合模式。  默认值：BlendMode.NONE  **说明：**  混合模式设置为BlendMode.NONE时，blend效果实际为默认的BlendMode.SRC\_OVER，且BlendApplyType不生效。 |
| type | [BlendApplyType](ts-universal-attributes-image-effect.md#blendapplytype11枚举说明) | 否 | blendMode实现方式是否离屏。  默认值：BlendApplyType.FAST  **说明：**  1. 设置BlendApplyType.FAST时，不离屏。  2. 设置BlendApplyType.OFFSCREEN时，会创建当前组件大小的离屏画布，再将当前组件（含子组件）的内容绘制到离屏画布上，再用指定的混合模式与下方画布已有内容进行混合。使用该实现方式时，将导致[linearGradientBlur12+](ts-universal-attributes-image-effect.md#lineargradientblur12)、[backgroundEffect](ts-universal-attributes-background.md#backgroundeffect11)、[brightness](ts-universal-attributes-image-effect.md#brightness)、[blur](ts-universal-attributes-image-effect.md#blur)等需要截屏的接口无法截取到正确的画面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## blendMode18+

PhonePC/2in1TabletTVWearable

blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T

将当前控件的内容（包含子节点内容）与下方画布（可能为离屏画布）已有内容进行混合。与[blendMode11+](ts-universal-attributes-image-effect.md#blendmode11)相比，mode参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[BlendMode](ts-universal-attributes-image-effect.md#blendmode11枚举说明)> | 是 | 混合模式。  默认值：BlendMode.NONE  当mode的值为undefined时，恢复为内容不进行混合的效果。  **说明：**  混合模式设置为BlendMode.NONE时，blend效果实际为默认的BlendMode.SRC\_OVER，且BlendApplyType不生效。 |
| type | [BlendApplyType](ts-universal-attributes-image-effect.md#blendapplytype11枚举说明) | 否 | blendMode实现方式是否离屏。  默认值：BlendApplyType.FAST  **说明：**  1. 设置BlendApplyType.FAST时，不离屏。  2. 设置BlendApplyType.OFFSCREEN时，会创建当前组件大小的离屏画布，再将当前组件（含子组件）的内容绘制到离屏画布上，再用指定的混合模式与下方画布已有内容进行混合。使用该实现方式时，将导致[linearGradientBlur12+](ts-universal-attributes-image-effect.md#lineargradientblur12)、[backgroundEffect](ts-universal-attributes-background.md#backgroundeffect11)、[brightness](ts-universal-attributes-image-effect.md#brightness)、[blur](ts-universal-attributes-image-effect.md#blur)等需要截屏的接口无法截取到正确的画面。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BlendApplyType11+枚举说明

PhonePC/2in1TabletTVWearable

指示如何将指定的混合模式应用于视图的内容。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FAST | 0 | 在目标图像上按顺序混合视图的内容。 |
| OFFSCREEN | 1 | 将此组件和子组件内容绘制到离屏画布上，然后整体进行混合。 |

## useShadowBatching11+

PhonePC/2in1TabletTVWearable

useShadowBatching(value: boolean): T

控件内部子节点的阴影进行同层绘制，同层元素阴影重叠。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 控件内部子节点的阴影是否进行同层绘制。  默认值：false  true：控件内部子节点的阴影进行同层绘制，子节点的阴影不会产生重叠覆盖效果。  false：控件内部子节点的阴影不进行同层绘制，子节点的阴影重叠区域有覆盖效果。  **说明：**  1. 默认不开启，如果子节点的阴影半径较大，阴影有重叠区域，后绘制的子节点阴影会覆盖在之前绘制的子节点阴影之上。 当开启时，子节点的阴影将同时绘制，不会产生覆盖效果。  2. 不推荐useShadowBatching嵌套使用，如果嵌套使用，只会对当前的子节点生效，无法递推。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## useShadowBatching18+

PhonePC/2in1TabletTVWearable

useShadowBatching(use: Optional<boolean>): T

控件内部子节点的阴影进行同层绘制，同层元素阴影重叠。与[useShadowBatching11+](ts-universal-attributes-image-effect.md#useshadowbatching11)相比，use参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| use | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 控件内部子节点的阴影是否进行同层绘制。  默认值：false  true：控件内部子节点的阴影进行同层绘制，子节点的阴影不会产生重叠覆盖效果。  false：控件内部子节点的阴影不进行同层绘制，子节点的阴影重叠区域有覆盖效果。  **说明：**  1. 默认不开启，如果子节点的阴影半径较大，阴影有重叠区域，后绘制的子节点阴影会覆盖在之前绘制的子节点阴影之上。 当开启时，子节点的阴影将同时绘制，不会产生覆盖效果。  2. 不推荐useShadowBatching嵌套使用，如果嵌套使用，只会对当前的子节点生效，无法递推。  当use的值为undefined时，恢复为不使用元素阴影重叠的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## sphericalEffect12+

PhonePC/2in1TabletTVWearable

sphericalEffect(value: number): T

设置组件的图像球面化程度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置组件的图像球面化程度。  取值范围：[0,1]。  **说明：**  1. 如果value等于0则图像保持原样，如果value等于1则图像为完全球面化效果。在0和1之间，数值越大，则球面化程度越高。  value < 0 或者 value > 1为异常情况，value < 0按0处理，value > 1按1处理。  2. 组件阴影和外描边不支持球面效果。  3. 设置value大于0时，组件冻屏并且把组件内容绘制到透明离屏buffer上，如果要更新组件属性则需要把value设置为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## sphericalEffect18+

PhonePC/2in1TabletTVWearable

sphericalEffect(effect: Optional<number>): T

设置组件的图像球面化程度。与[sphericalEffect12+](ts-universal-attributes-image-effect.md#sphericaleffect12)相比，effect参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| effect | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 设置组件的图像球面化程度。  取值范围：[0,1]。  **说明：**  1. 如果value等于0则图像保持原样，如果value等于1则图像为完全球面化效果。在0和1之间，数值越大，则球面化程度越高。  effect < 0 或者 effect > 1为异常情况，effect < 0按0处理，effect > 1按1处理。  2. 组件阴影和外描边不支持球面效果。  3. 设置effect大于0时，组件冻屏并且把组件内容绘制到透明离屏buffer上，如果要更新组件属性则需要把effect设置为0。  当effect的值为undefined时，恢复为图像球面化程度为0的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## lightUpEffect12+

PhonePC/2in1TabletTVWearable

lightUpEffect(value: number): T

设置组件图像亮起程度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 设置组件图像亮起程度。  取值范围：[0,1]。  如果value等于0则图像为全黑，如果value等于1则图像为全亮效果。0到1之间数值越大，表示图像亮度越高。value < 0 或者 value > 1为异常情况，value < 0按0处理，value > 1按1处理。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## lightUpEffect18+

PhonePC/2in1TabletTVWearable

lightUpEffect(degree: Optional<number>): T

设置组件图像亮起程度。与[lightUpEffect12+](ts-universal-attributes-image-effect.md#lightupeffect12)相比，degree参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| degree | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number> | 是 | 设置组件图像亮起程度。  取值范围：[0,1]。  如果value等于0则图像为全黑，如果value等于1则图像为全亮效果。0到1之间数值越大，表示图像亮度越高。degree < 0 或者 degree > 1为异常情况，degree < 0按0处理，degree > 1按1处理。  当degree的值为undefined时，恢复为亮起为1的效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## pixelStretchEffect12+

PhonePC/2in1TabletTVWearable

pixelStretchEffect(options: PixelStretchEffectOptions): T

设置组件的图像边缘像素扩展距离。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [PixelStretchEffectOptions](ts-universal-attributes-image-effect.md#pixelstretcheffectoptions10) | 是 | 设置组件的图像边缘像素扩展距离。  参数options包括上下左右四个方向的边缘像素扩展距离。  **说明：**  1. 如果距离为正值，表示向外扩展，放大原来图像大小。上下左右四个方向分别用边缘像素填充，填充的距离即为设置的边缘扩展的距离。  2. 如果距离为负值，表示内缩，但是最终图像大小不变。  内缩方式：  图像根据options的设置缩小，缩小大小为四个方向边缘扩展距离的绝对值。  图像用边缘像素扩展到原来大小。  3. 对options的输入约束：  上下左右四个方向的扩展统一为非正值或者非负值。即四个边同时向外扩或者内缩，方向一致。  所有方向的输入均为百分比或者具体值，不支持百分比和具体值混用。  所有异常情况下，显示为{0, 0, 0, 0}效果，即跟原图保持一致。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## pixelStretchEffect18+

PhonePC/2in1TabletTVWearable

pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T

设置组件的图像边缘像素扩展距离。与[pixelStretchEffect12+](ts-universal-attributes-image-effect.md#pixelstretcheffect12)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [Optional](ts-universal-attributes-custom-property.md#optionalt)<[PixelStretchEffectOptions](ts-universal-attributes-image-effect.md#pixelstretcheffectoptions10)> | 是 | 设置组件的图像边缘像素扩展距离。  参数options包括上下左右四个方向的边缘像素扩展距离。  **说明：**  1. 如果距离为正值，表示向外扩展，放大原来图像大小。上下左右四个方向分别用边缘像素填充，填充的距离即为设置的边缘扩展的距离。  2. 如果距离为负值，表示内缩，但是最终图像大小不变。  内缩方式：  图像根据options的设置缩小，缩小大小为四个方向边缘扩展距离的绝对值。  图像用边缘像素扩展到原来大小。  3. 对options的输入约束：  上下左右四个方向的扩展统一为非正值或者非负值。即四个边同时向外扩或者内缩，方向一致。  所有方向的输入均为百分比或者具体值，不支持百分比和具体值混用。  所有异常情况下，显示为{0, 0, 0, 0}效果，即跟原图保持一致。  当options的值为undefined时，恢复为无像素扩展效果。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## PixelStretchEffectOptions10+

PhonePC/2in1TabletTVWearable

像素扩展属性集合，用于描述像素扩展的信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | [Length](ts-types.md#length) | 否 | 是 | 组件图像左边沿像素扩展距离。  默认值：0vp |
| right | [Length](ts-types.md#length) | 否 | 是 | 组件图像右边沿像素扩展距离。  默认值：0vp |
| top | [Length](ts-types.md#length) | 否 | 是 | 组件图像上边沿像素扩展距离。  默认值：0vp |
| bottom | [Length](ts-types.md#length) | 否 | 是 | 组件图像下边沿像素扩展距离。  默认值：0vp |

## systemBarEffect12+

PhonePC/2in1TabletTVWearable

systemBarEffect(): T

根据背景进行智能反色并且带有模糊效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ShadowType10+枚举说明

PhonePC/2in1TabletTVWearable

阴影类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COLOR | 0 | 颜色。 |
| BLUR | 1 | 模糊。 |

## ShadowOptions对象说明

PhonePC/2in1TabletTVWearable

阴影属性集合，用于设置阴影的模糊半径、阴影的颜色、X轴和Y轴的偏移量。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number | [Resource](ts-types.md#resource) | 否 | 否 | 阴影模糊半径。  取值范围：[0, +∞)  单位：px  **说明：**  设置小于0的值时，按值为0处理。  如需使用vp单位的数值可用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)进行转换。  如果radius为Resource类型，则传入的值需为number类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| type10+ | [ShadowType](ts-universal-attributes-image-effect.md#shadowtype10枚举说明) | 否 | 是 | 阴影类型。  默认值：COLOR  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| color | [Color](ts-appendix-enums.md#color) | string | [Resource](ts-types.md#resource)| [ColoringStrategy11+](ts-appendix-enums.md#coloringstrategy10) | 否 | 是 | 阴影的颜色。  默认为黑色。  **说明：**  从API version 11开始，该接口支持使用ColoringStrategy实现智能取色，智能取色功能不支持在ArkTS卡片、[textShadow](ts-basic-components-text.md#textshadow10)中使用。  当前仅支持平均取色和主色取色，智能取色区域为shadow绘制区域。  支持使用'average'字符串触发智能平均取色模式，支持使用'primary'字符串触发智能主色模式。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| offsetX | number | [Resource](ts-types.md#resource) | 否 | 是 | 阴影的X轴偏移量。  默认值：0  单位：px  **说明：**  如需使用vp单位的数值可用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)进行转换。  如果offsetX为Resource类型，则传入的值需为number类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| offsetY | number | [Resource](ts-types.md#resource) | 否 | 是 | 阴影的Y轴偏移量。  默认值：0  单位：px  **说明：**  如需使用vp单位的数值可用[vp2px](arkts-apis-uicontext-uicontext.md#vp2px12)进行转换。  如果offsetY为Resource类型，则传入的值需为number类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| fill11+ | boolean | 否 | 是 | 阴影是否内部填充。true表示阴影在内部填充，false表示阴影在外部填充。  默认值：false。  **说明：**  [textShadow](ts-basic-components-text.md#textshadow10)中该字段不生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ShadowStyle10+枚举说明

PhonePC/2in1TabletTVWearable

组件阴影效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| OUTER\_DEFAULT\_XS | 0 | 超小阴影。 |
| OUTER\_DEFAULT\_SM | 1 | 小阴影。 |
| OUTER\_DEFAULT\_MD | 2 | 中阴影。 |
| OUTER\_DEFAULT\_LG | 3 | 大阴影。 |
| OUTER\_FLOATING\_SM | 4 | 浮动小阴影。 |
| OUTER\_FLOATING\_MD | 5 | 浮动中阴影。 |

## BlendMode11+枚举说明

PhonePC/2in1TabletTVWearable

混合模式。

说明

blendMode枚举中，s表示源像素，d表示目标像素，sa表示源像素透明度，da表示目标像素透明度，r表示混合后像素，ra表示混合后像素透明度。

**卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 将上层图像直接覆盖到下层图像上，不进行任何混合操作。 |
| CLEAR | 1 | 将源像素覆盖的目标像素清除为完全透明。 |
| SRC | 2 | r = s，只显示源像素。 |
| DST | 3 | r = d，只显示目标像素。 |
| SRC\_OVER | 4 | r = s + (1 - sa) \* d，将源像素按照透明度进行混合，覆盖在目标像素上。 |
| DST\_OVER | 5 | r = d + (1 - da) \* s，将目标像素按照透明度进行混合，覆盖在源像素上。 |
| SRC\_IN | 6 | r = s \* da，只显示源像素中与目标像素重叠的部分。 |
| DST\_IN | 7 | r = d \* sa，只显示目标像素中与源像素重叠的部分。 |
| SRC\_OUT | 8 | r = s \* (1 - da)，只显示源像素中与目标像素不重叠的部分。 |
| DST\_OUT | 9 | r = d \* (1 - sa)，只显示目标像素中与源像素不重叠的部分。 |
| SRC\_ATOP | 10 | r = s \* da + d \* (1 - sa)，在源像素和目标像素重叠的地方绘制源像素，在源像素和目标像素不重叠的地方绘制目标像素。 |
| DST\_ATOP | 11 | r = d \* sa + s \* (1 - da)，在源像素和目标像素重叠的地方绘制目标像素，在源像素和目标像素不重叠的地方绘制源像素。 |
| XOR | 12 | r = s \* (1 - da) + d \* (1 - sa)，在源像素和目标像素重叠的地方不显示像素，不重叠的地方显示源像素和目标像素。 |
| PLUS | 13 | r = min(s + d, 1)，将源像素值与目标像素值相加，并将结果作为新的像素值。 |
| MODULATE | 14 | r = s \* d，将源像素与目标像素进行乘法运算，并将结果作为新的像素值。 |
| SCREEN | 15 | r = s + d - s \* d，将两个图像的像素值相加，然后减去它们的乘积来实现混合。 |
| OVERLAY | 16 | 根据目标像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| DARKEN | 17 | rc = s + d - max(s \* da, d \* sa), ra = kSrcOver，当两个颜色重叠时，较暗的颜色会覆盖较亮的颜色。 |
| LIGHTEN | 18 | rc = s + d - min(s \* da, d \* sa), ra = kSrcOver，将源图像和目标图像中的像素进行比较，选取两者中较亮的像素作为最终的混合结果。 |
| COLOR\_DODGE | 19 | 使目标像素变得更亮来反映源像素。 |
| COLOR\_BURN | 20 | 使目标像素变得更暗来反映源像素。 |
| HARD\_LIGHT | 21 | 根据源像素的值来决定目标像素变得更亮或者更暗。根据源像素来决定使用MULTIPLY混合模式还是SCREEN混合模式。 |
| SOFT\_LIGHT | 22 | 根据源像素来决定使用LIGHTEN混合模式还是DARKEN混合模式。 |
| DIFFERENCE | 23 | rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生高对比度的效果。 |
| EXCLUSION | 24 | rc = s + d - 2 \* (s \* d), ra = kSrcOver，对比源像素和目标像素，亮度更高的像素减去亮度更低的像素，产生柔和的效果。 |
| MULTIPLY | 25 | r = s \* (1 - da) + d \* (1 - sa) + s \* d，将源图像与目标图像进行乘法混合，得到一张新的图像。 |
| HUE | 26 | 保留源图像的亮度和饱和度，但会使用目标图像的色调来替换源图像的色调。 |
| SATURATION | 27 | 保留目标像素的亮度和色调，但会使用源像素的饱和度来替换目标像素的饱和度。 |
| COLOR | 28 | 保留源像素的饱和度和色调，但会使用目标像素的亮度来替换源像素的亮度。 |
| LUMINOSITY | 29 | 保留目标像素的色调和饱和度，但会用源像素的亮度替换目标像素的亮度。 |

## LinearGradientBlurOptions12+

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fractionStops | [FractionStop](ts-universal-attributes-image-effect.md#fractionstop12)[] | 否 | 否 | 数组中保存的每一个二元数组（取值0-1，小于0则为0，大于1则为1）表示[模糊程度, 模糊位置]；模糊位置需严格递增，开发者传入的数据不符合规范会记录日志，渐变模糊数组中二元数组个数必须大于等于2，否则渐变模糊不生效。 |
| direction | [GradientDirection](ts-appendix-enums.md#gradientdirection) | 否 | 否 | 渐变模糊方向。  默认值：  GradientDirection.Bottom |

## FractionStop12+

PhonePC/2in1TabletTVWearable

type FractionStop = [ number, number ]

定义模糊段。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ number, number ] | 第一个number表示分数，值1表示不透明，0表示完全透明。  取值范围：[0, 1]  第二个number表示停止位置，值1表示区域结束位置，0表示区域开始位置。  取值范围：[0, 1] |

## InvertOptions11+对象说明

PhonePC/2in1TabletTVWearable

前景智能取反色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| low | number | 否 | 否 | 背景颜色灰度值大于阈值区间时的取值。  取值范围：[0, 1] |
| high | number | 否 | 否 | 背景颜色灰度值小于阈值区间时的取值。  取值范围：[0, 1] |
| threshold | number | 否 | 否 | 灰度阈值。  取值范围：[0, 1] |
| thresholdRange | number | 否 | 否 | 阈值范围。  取值范围：[0, 1]  **说明：**  灰度阈值上下偏移thresholdRange构成阈值区间，背景颜色灰度值在区间内取值由high线性渐变到low。 |

## BackgroundImageOptions18+

PhonePC/2in1TabletTVWearable

定义背景图选项。

说明

背景图片的同步加载可能会带来潜在性能问题，详情可见[Image](ts-basic-components-image.md#image-1)中说明。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| syncLoad | boolean | 否 | 是 | 是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。  默认值：false  false：异步加载图片。  true：同步加载图片。 |
| repeat | [ImageRepeat](ts-appendix-enums.md#imagerepeat) | 否 | 是 | 设置背景图片的重复样式。默认值为ImageRepeat.NoRepeat。 |

## freeze12+

PhonePC/2in1TabletTVWearable

freeze(value: boolean): T

设置当前控件和子控件是否整体离屏渲染绘制后重复绘制缓存，不再进行内部属性更新。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 设置当前控件和子控件是否整体离屏渲染绘制后重复绘制缓存，不再进行内部属性更新。当前控件的不透明度不为1时绘制效果可能有差异。  默认值：false  true时离屏渲染绘制后重复绘制缓存，false时离屏渲染绘制后不重复绘制缓存。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## freeze18+

PhonePC/2in1TabletTVWearable

freeze(freeze: Optional<boolean>): T

设置当前控件和子控件是否整体离屏渲染绘制后重复绘制缓存，不再进行内部属性更新。与[freeze](ts-universal-attributes-image-effect.md#freeze12)相比，freeze参数新增了对undefined类型的支持。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| freeze | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | 设置当前控件和子控件是否整体离屏渲染绘制后重复绘制缓存，不再进行内部属性更新。当前控件的不透明度不为1时绘制效果可能有差异。  默认值：false  true时离屏渲染绘制后重复绘制缓存，false时离屏渲染绘制后不重复绘制缓存。  当freeze的值为undefined时，维持之前取值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置图片不同属性效果）

设置图片的效果，包括阴影，灰度，高光，饱和度，对比度，图像反转，叠色，色相旋转等。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageEffectsExample {
5. build() {
6. Column({ space: 5 }) {
7. // 添加阴影效果，图片效果不变
8. Text('shadow').fontSize(15).fontColor(0xCCCCCC).width('90%')
9. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
10. Image($r('app.media.image'))
11. .width('90%')
12. .height(30)
13. .shadow({
14. radius: 10,
15. color: Color.Green,
16. offsetX: 20,
17. offsetY: 20
18. })

20. // 添加内部阴影效果
21. Text('shadow').fontSize(15).fontColor(0xCCCCCC).width('90%')
22. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
23. Image($r('app.media.image'))
24. .width('90%')
25. .height(30)
26. .shadow({
27. radius: 5,
28. color: Color.Green,
29. offsetX: 20,
30. offsetY: 20,
31. fill: true
32. }).opacity(0.5)

34. // 灰度效果0~1，越接近1，灰度越明显
35. Text('grayscale').fontSize(15).fontColor(0xCCCCCC).width('90%')
36. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
37. Image($r('app.media.image')).width('90%').height(30).grayscale(0.3)
38. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
39. Image($r('app.media.image')).width('90%').height(30).grayscale(0.8)

41. // 高光效果，1为正常图片，<1变暗，>1亮度增大
42. Text('brightness').fontSize(15).fontColor(0xCCCCCC).width('90%')
43. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
44. Image($r('app.media.image')).width('90%').height(30).brightness(1.2)

46. // 饱和度，原图为1
47. Text('saturate').fontSize(15).fontColor(0xCCCCCC).width('90%')
48. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
49. Image($r('app.media.image')).width('90%').height(30).saturate(2.0)
50. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
51. Image($r('app.media.image')).width('90%').height(30).saturate(0.7)

53. // 对比度，1为原图，>1值越大越清晰，<1值越小越模糊
54. Text('contrast').fontSize(15).fontColor(0xCCCCCC).width('90%')
55. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
56. Image($r('app.media.image')).width('90%').height(30).contrast(2.0)
57. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
58. Image($r('app.media.image')).width('90%').height(30).contrast(0.8)

60. // 图像反转比例
61. Text('invert').fontSize(15).fontColor(0xCCCCCC).width('90%')
62. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
63. Image($r('app.media.image')).width('90%').height(30).invert(0.2)
64. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
65. Image($r('app.media.image')).width('90%').height(30).invert(0.8)

67. // 叠色添加
68. Text('colorBlend').fontSize(15).fontColor(0xCCCCCC).width('90%')
69. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
70. Image($r('app.media.image')).width('90%').height(30).colorBlend(Color.Green)
71. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
72. Image($r('app.media.image')).width('90%').height(30).colorBlend(Color.Blue)

74. // 深褐色
75. Text('sepia').fontSize(15).fontColor(0xCCCCCC).width('90%')
76. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
77. Image($r('app.media.image')).width('90%').height(30).sepia(0.8)

79. // 色相旋转
80. Text('hueRotate').fontSize(15).fontColor(0xCCCCCC).width('90%')
81. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
82. Image($r('app.media.image')).width('90%').height(30).hueRotate(90)
83. }.width('100%').margin({ top: 5 })
84. }
85. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/VrZsJzyoTmapC69o2UcpwQ/zh-cn_image_0000002583439555.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=C8BAF3260A848742E72FDB2D6BF39DA76478A100E297BFCFB386A98DC6821655)

### 示例2（设置组件线性渐变模糊效果）

该示例主要演示通过[linearGradientBlur](ts-universal-attributes-image-effect.md#lineargradientblur12)设置组件的内容线性渐变模糊效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageExample1 {
5. // $r('app.media.testlinearGradientBlurOrigin')需要替换为开发者所需的资源文件。
6. private_resource1: Resource = $r('app.media.testlinearGradientBlurOrigin')
7. @State image_src: Resource = this.private_resource1

9. build() {
10. Column() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
12. Row({ space: 5 }) {
13. Image(this.image_src)
14. .blur(0) // 设置图片模糊效果为不模糊
15. .linearGradientBlur(60,
16. { fractionStops: [[0, 0], [0, 0.33], [1, 0.66], [1, 1]], direction: GradientDirection.Bottom })
17. }
18. }
19. }
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/RVOuEb-NSHi4vqBBiwIyqA/zh-cn_image_0000002552959510.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=391E67710046022BBEA19D6EE8EF77AE0E6B8D5FB12BE030EB6BD5CF05AEE958)

### 示例3（设置离屏渲染效果）

该示例主要演示通过[renderGroup](ts-universal-attributes-image-effect.md#rendergroup10)来设置组件是否先整体离屏渲染绘制后，再与父组件融合绘制。

```
1. // xxx.ets
2. @Component
3. struct Component1 {
4. @Prop renderGroupValue: boolean;

6. build() {
7. Row() {
8. Row() {
9. Row()
10. .backgroundColor(Color.Black)
11. .width(100)
12. .height(100)
13. .opacity(1)
14. }
15. .backgroundColor(Color.White)
16. .width(150)
17. .height(150)
18. .justifyContent(FlexAlign.Center)
19. .opacity(0.6)
20. .renderGroup(this.renderGroupValue)
21. }
22. .backgroundColor(Color.Black)
23. .width(200)
24. .height(200)
25. .justifyContent(FlexAlign.Center)
26. .opacity(1)
27. }
28. }

30. @Entry
31. @Component
32. struct RenderGroupExample {
33. build() {
34. Column() {
35. Component1({ renderGroupValue: true })
36. .margin(20)
37. Component1({ renderGroupValue: false })
38. .margin(20)
39. }
40. .width("100%")
41. .height("100%")
42. .alignItems(HorizontalAlign.Center)
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/ewAEjb0QSSagb035u6YrKQ/zh-cn_image_0000002583479511.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=5CD9F9976381496BC743B5F04A71028D61DD915048F735A9ACFC0B5F2E7ADFC4)

### 示例4（当前组件内容与下方画布内容混合）

该示例主要演示通过[blendMode](ts-universal-attributes-image-effect.md#blendmode11)将当前组件内容与下方画布内容混合。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. Text("blendMode")
8. .fontSize(20)
9. .fontWeight(FontWeight.Bold)
10. .fontColor('#ffff0101')
11. Row() {
12. Circle()
13. .width(200)
14. .height(200)
15. .fill(Color.Green)
16. .position({ x: 50, y: 50 })
17. Circle()
18. .width(200)
19. .height(200)
20. .fill(Color.Blue)
21. .position({ x: 150, y: 50 })
22. }
23. .blendMode(BlendMode.OVERLAY, BlendApplyType.OFFSCREEN)
24. .alignItems(VerticalAlign.Center)
25. .height(300)
26. .width('100%')
27. }
28. .height('100%')
29. .width('100%')
30. // $r("app.media.image")需要替换为开发者所需的图像资源文件。
31. .backgroundImage($r('app.media.image'))
32. .backgroundImageSize(ImageSize.Cover)
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/M_slZxt8SUWUVRE8OpEDxw/zh-cn_image_0000002552799862.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=AD8404E3C0E11644810CCE91BF60EDEC5A394674F87434CFF24500B95012ABD5)

### 示例5（前景智能取反色）

该示例主要通过[InvertOptions](ts-universal-attributes-image-effect.md#invertoptions11对象说明)来实现前景智能取反色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Stack() {
7. Column()
8. Stack() {
9. // $r("app.media.r")需要替换为开发者所需的图像资源文件。
10. // 该示例中图片为从左到右，颜色由浅到深。
11. Image($r('app.media.r')).width('100%')
12. Column() {
13. Column().width("100%").height(30).invert({
14. low: 0,
15. high: 1,
16. threshold: 0.5,
17. thresholdRange: 0.2
18. })
19. Column().width("100%").height(30).invert({
20. low: 0.2,
21. high: 0.5,
22. threshold: 0.3,
23. thresholdRange: 0.2
24. })
25. }
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
31. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/-oShg7bNTi-ruKcMWXqjEg/zh-cn_image_0000002583439557.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=6A03992A8195187813DA094FC8854FCD99FFC8AA3DC11A45087524F8B4BE9B8F)

### 示例6（设置同层阴影不重叠效果）

该示例主要通过[useShadowBatching](ts-universal-attributes-image-effect.md#useshadowbatching11)搭配[shadow](ts-universal-attributes-image-effect.md#shadow)实现同层阴影不重叠效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct UseShadowBatchingExample {
5. build() {
6. Column() {
7. Column({ space: 10 }) {
8. Stack() {

10. }
11. .width('90%')
12. .height(50)
13. .margin({ top: 5 })
14. .backgroundColor(0xFFE4C4)
15. .shadow({
16. radius: 120,
17. color: Color.Green,
18. offsetX: 0,
19. offsetY: 0
20. })
21. .align(Alignment.TopStart)
22. .shadow({
23. radius: 120,
24. color: Color.Green,
25. offsetX: 0,
26. offsetY: 0
27. })

29. Stack() {

31. }
32. .width('90%')
33. .height(50)
34. .margin({ top: 5 })
35. .backgroundColor(0xFFE4C4)
36. .align(Alignment.TopStart)
37. .shadow({
38. radius: 120,
39. color: Color.Red,
40. offsetX: 0,
41. offsetY: 0
42. })
43. .width('90%')
44. .backgroundColor(Color.White)

46. Column() {
47. Text()
48. .fontWeight(FontWeight.Bold)
49. .fontSize(20)
50. .fontColor(Color.White)
51. }
52. .justifyContent(FlexAlign.Center)
53. .width(150)
54. .height(150)
55. .borderRadius(10)
56. .backgroundColor(0xf56c6c)
57. .shadow({
58. radius: 300,
59. color: Color.Yellow,
60. offsetX: 0,
61. offsetY: 0
62. })

64. Column() {
65. Text()
66. .fontWeight(FontWeight.Bold)
67. .fontSize(20)
68. .fontColor(Color.White)
69. }
70. .justifyContent(FlexAlign.Center)
71. .width(150)
72. .height(150)
73. .backgroundColor(0x67C23A)
74. .borderRadius(10)
75. .translate({ y: -50 })
76. .shadow({
77. radius: 220,
78. color: Color.Blue,
79. offsetX: 0,
80. offsetY: 0
81. })
82. }
83. .useShadowBatching(true)
84. }
85. .width('100%').margin({ top: 5 })
86. }
87. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/paxGVnhzTSGANanPG-U3tA/zh-cn_image_0000002552959512.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=C1B105B379C8311456A2ACC996B0C79D558433CABEB68DDA47F36238280298E2)

### 示例7（设置组件图像球面效果）

该示例主要演示通过[sphericalEffect](ts-universal-attributes-image-effect.md#sphericaleffect12)设置组件的图像球面效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SphericalEffectExample {
5. build() {
6. Stack() {
7. TextInput({ placeholder: "请输入变化范围百分比（[0%,100%]）" })
8. .width('50%')
9. .height(35)
10. .type(InputType.Number)
11. .enterKeyType(EnterKeyType.Done)
12. .caretColor(Color.Red)
13. .placeholderColor(Color.Blue)
14. .placeholderFont({
15. size: 20,
16. style: FontStyle.Italic,
17. weight: FontWeight.Bold
18. })
19. .sphericalEffect(0.5)
20. }.alignContent(Alignment.Center).width("100%").height("100%")
21. }
22. }
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/vFhLCdCvQjenOcSCRoDoAg/zh-cn_image_0000002583479513.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=017F3B56591E71D20881C4EF035EB7D46FB90C1DB52A818F3584832C4751CC81)

去掉sphericalEffect的设置，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/RBppdEWxTlSESenpg9v4mQ/zh-cn_image_0000002552799864.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=5546CFCC1661DEB20F35773697497A3C99CE6D646F690DDE428EBE457AF0AA20)

### 示例8（设置组件图像渐亮效果）

该示例主要演示通过[lightUpEffect](ts-universal-attributes-image-effect.md#lightupeffect12)设置组件的图像渐亮效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct LightUpExample {
5. build() {
6. Stack() {
7. Text('This is the text content with letterSpacing 0.')
8. .letterSpacing(0)
9. .fontSize(12)
10. .border({ width: 1 })
11. .padding(10)
12. .width('50%')
13. .lightUpEffect(0.6)
14. }.alignContent(Alignment.Center).width("100%").height("100%")
15. }
16. }
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/baxkrrn0SW6HQRKPp_5NHg/zh-cn_image_0000002583439559.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=46E4D6A53D6DB4B60B0AC4136152331EFE85F49B8A9936C035FBCCDD13FC86E2)

修改lightUpEffect参数值为0.2：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/mEzsQafZQxyzNbqulh_87A/zh-cn_image_0000002552959514.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=2C2064AA3717684702AA14CBBEAEE3493B5C83752B00E9A5E6C2C5BFDC3958ED)

去掉lightUpEffect的设置，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/Xt2hppYiQ46Cs30He8-ylA/zh-cn_image_0000002583479515.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=2D7A854812BF2D0FDD5C45CD7F27827AA53B0FF5EC31C1F0864F07A9FFBA6DA0)

### 示例9（设置组件图像边缘像素扩展效果）

该示例主要演示通过[pixelStretchEffect](ts-universal-attributes-image-effect.md#pixelstretcheffect12)设置组件的图像边缘像素扩展效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct PixelStretchExample {
5. build() {
6. Stack() {
7. Text('This is the text content with letterSpacing 0.')
8. .letterSpacing(0)
9. .fontSize(12)
10. .border({ width: 1 })
11. .padding(10)
12. .clip(false)
13. .width('50%')
14. .pixelStretchEffect({
15. top: 10,
16. left: 10,
17. right: 10,
18. bottom: 10
19. })
20. }.alignContent(Alignment.Center).width("100%").height("100%")
21. }
22. }
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/qCv0CRRQR1ekBvHgGtI3Qw/zh-cn_image_0000002552799866.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=6635E56E38B0A5055BF378F93FDBD507348E425D3F1CB1F1D79ABDDD15062A86)

去掉pixelStretchEffect的设置，原图效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/qZ7bSbLXTQiwZ-tD1NAODQ/zh-cn_image_0000002583439561.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=21BCF1B498CCFA9D8061F4C03BF20A903CC9037E4656D3C9418D157B3CC5E500)

### 示例10（系统导航条智能反色）

该示例主要演示通过[systemBarEffect](ts-universal-attributes-image-effect.md#systembareffect12)来实现系统导航条智能反色。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Column() {
7. Stack() {
8. // $r("app.media.testImage")需要替换为开发者所需的图像资源文件。
9. Image($r('app.media.testImage')).width('100%').height('100%')
10. Column()
11. .width(150)
12. .height(10)
13. .systemBarEffect()
14. .border({ radius: 5 })
15. .margin({ bottom: 80 })
16. }.alignContent(Alignment.Center)
17. }
18. }
19. }
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/aReS3bUDTlCGVSIFTtu4sA/zh-cn_image_0000002552959516.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=4423193D0FE49C58365A3A082182854F0E964193EB42386867F724C476B3315D)
