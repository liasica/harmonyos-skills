---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-background
title: 背景设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 背景设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:284636f40adbc6a542d640834f33d4bcc0b58b2f628b53923697bfec1cad2ebb
---

设置组件的背景样式。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## background10+

PhonePC/2in1TabletTVWearable

background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T

设置组件背景。从API version 20开始，content参数新增了对[ResourceColor](ts-types.md#resourcecolor)类型的支持，并新增了背景向父组件的安全区扩展的能力。

说明

* 不支持[onAppear](ts-universal-events-show-hide.md#onappear)和[onDisAppear](ts-universal-events-show-hide.md#ondisappear)等和节点挂载/卸载相关的事件。
* 从API version 20开始，该接口仅当content的入参类型为ResourceColor时支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [CustomBuilder](ts-types.md#custombuilder8) | [ResourceColor](ts-types.md#resourcecolor) | 是 | 自定义背景。 |
| options | [BackgroundOptions](ts-universal-attributes-background.md#backgroundoptions20对象说明) | 否 | 设置自定义背景选项。  **说明：**  API version 20之前，options:  {  align?: [Alignment](ts-appendix-enums.md#alignment)  } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

* 自定义背景渲染存在一定延迟，不能响应事件。该属性不支持嵌套使用。
* CustomBuilder类型的背景不支持在预览器中预览。
* 从API version 20开始，支持动态更新背景。
* 同时设置background，backgroundColor，backgroundImage时，三者将按以下规则叠加显示：
  + 若background为ResourceColor类型，或设置ignoresLayoutSafeAreaEdges属性，则background位于最底层。
  + 其他情况下，background位于最上层。
* 在background设置content参数为CustomBuilder类型时，background不会跟随CustomBuilder内容更新而变化。

## BackgroundOptions20+对象说明

PhonePC/2in1TabletTVWearable

background配置选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| align10+ | [Alignment](ts-appendix-enums.md#alignment) | 否 | 是 | 自定义背景与组件的对齐方式。该属性仅对CustomBuilder类型的背景生效。如果设置了ignoresLayoutSafeAreaEdges，则背景的布局区域为包含了扩展安全区的范围。  默认值：Alignment.Center  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ignoresLayoutSafeAreaEdges | Array<[LayoutSafeAreaEdge](ts-universal-attributes-expand-safe-area.md#layoutsafeareaedge12)> | 否 | 是 | 配置背景要扩展到的安全区，包括：状态栏，导航栏和[safeAreaPadding](ts-universal-attributes-size.md#safeareapadding14)。  默认值：  - CustomBuilder背景：[]，不扩展。  - ResourceColor背景：[LayoutSafeAreaEdge.ALL]，扩展至所有方向。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

说明

Shape, RowSplit, ColumnSplit, SideBarContainer, Stepper, List, Grid, WaterFlow, Scroll, Refresh, Swiper, Tabs组件的clip属性默认值为true，子组件的背景扩展会被裁剪。

## backgroundColor

PhonePC/2in1TabletTVWearable

backgroundColor(value: ResourceColor): T

设置组件背景色。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 设置组件的背景色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundColor18+

PhonePC/2in1TabletTVWearable

backgroundColor(color: Optional<ResourceColor>): T

设置组件背景色。与[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)相比，color参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<[ResourceColor](ts-types.md#resourcecolor)> | 是 | 设置组件的背景色。  当color的值为undefined时，恢复为默认透明的背景色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

当通过[backgroundBlurStyle](ts-universal-attributes-background.md#backgroundblurstyle9)中的inactiveColor指定背景色时，不建议再通过backgroundColor设置背景色。

## backgroundColor20+

PhonePC/2in1TabletTVWearable

backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T

设置组件背景色。与[backgroundColor](ts-universal-attributes-background.md#backgroundcolor18)相比，color参数新增了对[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)类型的支持。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | Optional<[ResourceColor](ts-types.md#resourcecolor) | [ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)> | 是 | 设置组件的背景色。  当color的值为undefined时，恢复为默认透明的背景色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundImage

PhonePC/2in1TabletTVWearable

backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T

设置组件的背景图片。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | [PixelMap12+](arkts-apis-image-pixelmap.md) | 是 | 图片地址。API version 22及之前版本，支持网络图片资源地址、本地图片资源地址、Base64和PixelMap资源，不支持svg图片、gif和webp等类型的动图。 从API version 23开始，新增支持webp和gif类型的动图，显示动图第一帧，不支持其他类型的动图。 |
| repeat | [ImageRepeat](ts-appendix-enums.md#imagerepeat) | 否 | 设置背景图片的重复样式，默认不重复。当设置的背景图片为透明底色图片，且同时设置了backgroundColor时，二者叠加显示，背景颜色在最底部。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundImage18+

PhonePC/2in1TabletTVWearable

backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T

设置组件的背景图片。与[backgroundImage](ts-universal-attributes-background.md#backgroundimage)相比，增加了设置图片同步或异步加载方式的能力。

说明

该接口不支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | 是 | 图片地址。API version 22及之前版本，支持网络图片资源地址、本地图片资源地址、Base64和PixelMap资源，不支持svg图片、gif和webp等类型的动图。 从API version 23开始，新增支持webp和gif类型的动图，显示动图第一帧，不支持其他类型的动图。 |
| options | [BackgroundImageOptions](ts-universal-attributes-image-effect.md#backgroundimageoptions18) | 否 | 设置背景图选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundImageSize

PhonePC/2in1TabletTVWearable

backgroundImageSize(value: SizeOptions | ImageSize): T

设置组件背景图片的宽度和高度。当未设置backgroundImageSize时，默认组件背景图片宽高效果为[ImageSize.Auto](ts-appendix-enums.md#imagesize)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [SizeOptions](ts-types.md#sizeoptions) | [ImageSize](ts-appendix-enums.md#imagesize) | 是 | 设置背景图像的高度和宽度。默认保持原图的比例不变。  width和height取值范围： [0, +∞)  ImageSize用于控制图片缩放显示模式，如保持比例、填充边界等。  **说明：**  width和height均设置为小于或等于0的值时，按值为0显示。当width和height中只有一个值未设置或者设置为小于等于0的值时，另一个会根据图片原始宽高比进行调整。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundImagePosition

PhonePC/2in1TabletTVWearable

backgroundImagePosition(value: Position | Alignment): T

设置背景图的位置。当未设置backgroundImagePosition时，组件默认背景图位置为当前组件左上角。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Position](ts-types.md#position) | [Alignment](ts-appendix-enums.md#alignment) | 是 | 设置背景图在组件中显示位置，即相对于组件左上角的坐标。  x和y值设置百分比时，偏移量是相对组件自身宽高计算的。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BlurStyle9+

PhonePC/2in1TabletTVWearable

模糊样式类型。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Thin | - | 轻薄材质模糊。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Regular | - | 普通厚度材质模糊。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Thick | - | 厚材质模糊。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BACKGROUND\_THIN10+ | 3 | 近距景深模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BACKGROUND\_REGULAR10+ | 4 | 中距景深模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BACKGROUND\_THICK10+ | 5 | 远距景深模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| BACKGROUND\_ULTRA\_THICK10+ | 6 | 超远距景深模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| NONE10+ | 7 | 关闭模糊。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| COMPONENT\_ULTRA\_THIN11+ | 8 | 组件超轻薄材质模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COMPONENT\_THIN11+ | 9 | 组件轻薄材质模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COMPONENT\_REGULAR11+ | 10 | 组件普通材质模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COMPONENT\_THICK11+ | 11 | 组件厚材质模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| COMPONENT\_ULTRA\_THICK11+ | 12 | 组件超厚材质模糊。  **卡片能力：** 从API version 11开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## SystemAdaptiveOptions19+

PhonePC/2in1TabletTVWearable

系统自适应调节参数，系统会默认开启根据芯片算力进行自适应效果调节的能力。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| disableSystemAdaptation | boolean | 否 | 是 | 系统自适应调节参数，推荐不携带该参数。该参数只影响低算力设备，低算力设备的定义由设备厂商决定。在低芯片算力的设备上，会根据算力和负载等条件，自动决策是否使用低算力的近似效果替代原有效果，比如模糊效果会结合接口中携带的模糊相关参数值及其他低算力处理逻辑，进行自适应效果降级处理。如果想关闭该功能，可以将该标志置为true。  默认值：false |

## backgroundBlurStyle9+

PhonePC/2in1TabletTVWearable

backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [BlurStyle](ts-universal-attributes-background.md#blurstyle9) | 是 | 背景模糊样式。模糊样式中封装了模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度五个参数。 |
| options | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 背景模糊选项。用于配置模糊激活策略和不生效时的背景色。不传入时使用默认激活策略[BlurStyleActivePolicy](ts-universal-attributes-background.md#blurstyleactivepolicy14).ALWAYS\_ACTIVE。  该参数在ArkTS卡片中，暂不支持使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundBlurStyle18+

PhonePC/2in1TabletTVWearable

backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。与[backgroundBlurStyle9+](ts-universal-attributes-background.md#backgroundblurstyle9)相比，style参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<[BlurStyle](ts-universal-attributes-background.md#blurstyle9)> | 是 | 背景模糊样式。模糊样式中封装了模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度五个参数。  当style的值为undefined时，恢复为默认关闭模糊的背景。 |
| options | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 背景模糊选项。用于配置模糊激活策略和不生效时的背景色。不传入时使用默认激活策略[BlurStyleActivePolicy](ts-universal-attributes-background.md#blurstyleactivepolicy14).ALWAYS\_ACTIVE。  该参数在ArkTS卡片中，暂不支持使用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

当通过backgroundBlurStyle中的inactiveColor指定背景色时，不建议再通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)设置背景色。

## backgroundBlurStyle19+

PhonePC/2in1TabletTVWearable

backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T

为当前组件提供一种背景材质模糊能力，通过枚举值的方式封装了不同的模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度。与[backgroundBlurStyle18+](ts-universal-attributes-background.md#backgroundblurstyle18)相比，新增了sysOptions参数，即支持系统自适应调节参数。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | Optional<[BlurStyle](ts-universal-attributes-background.md#blurstyle9)> | 是 | 背景模糊样式。模糊样式中封装了模糊半径、蒙版颜色、蒙版透明度、饱和度、亮度五个参数。  当style的值为undefined时，恢复为默认关闭模糊的背景。 |
| options | [BackgroundBlurStyleOptions](ts-universal-attributes-background.md#backgroundblurstyleoptions10对象说明) | 否 | 背景模糊选项。  该参数在ArkTS卡片中，暂不支持使用。 |
| sysOptions | [SystemAdaptiveOptions](ts-universal-attributes-background.md#systemadaptiveoptions19) | 否 | 系统自适应调节参数。  默认值：{ disableSystemAdaptation: false } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

当通过backgroundBlurStyle中的inactiveColor指定背景色时，不建议再通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor)设置背景色。

## backdropBlur

PhonePC/2in1TabletTVWearable

backdropBlur(value: number, options?: BlurOptions): T

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 为当前组件添加背景模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。  取值范围：[0, +∞)  默认值：0 |
| options11+ | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 灰阶模糊参数。对图像中的黑白色进行色阶调整，使其趋于灰色更为柔和美观，对图像中的彩色调整没有效果。  默认值：grayscale: [0,0] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backdropBlur18+

PhonePC/2in1TabletTVWearable

backdropBlur(radius: Optional<number>, options?: BlurOptions): T

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。与[backdropBlur](ts-universal-attributes-background.md#backdropblur)相比，radius参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | Optional<number> | 是 | 为当前组件添加背景模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。当radius的值为undefined时，恢复为默认无模糊的背景。  取值范围：[0, +∞)  默认值：0 |
| options | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 灰阶模糊参数。对图像中的黑白色进行色阶调整，使其趋于灰色更为柔和美观，对图像中的彩色调整没有效果。  默认值：grayscale: [0,0] |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

blur和backdropBlur是实时模糊接口，会每帧进行实时渲染，性能负载较高。当模糊内容和模糊半径都不需要变化时，建议使用静态模糊接口[blur](js-apis-effectkit.md#blur)。

## backdropBlur19+

PhonePC/2in1TabletTVWearable

backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T

为组件添加背景模糊效果，支持自定义设置模糊半径和灰阶参数。与[backdropBlur18+](ts-universal-attributes-background.md#backdropblur18)相比，新增了sysOptions参数，即支持系统自适应调节参数。

**卡片能力：** 从API version 19开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | Optional<number> | 是 | 为当前组件添加背景模糊效果，入参为模糊半径，模糊半径越大越模糊，为0时不模糊。  当radius的值为undefined时，恢复为默认无模糊的背景。  取值范围：[0, +∞)  默认值：0 |
| options | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 灰阶模糊参数。对图像中的黑白色进行色阶调整，使其趋于灰色更为柔和美观，对图像中的彩色调整没有效果。  默认值：grayscale: [0,0] |
| sysOptions | [SystemAdaptiveOptions](ts-universal-attributes-background.md#systemadaptiveoptions19) | 否 | 系统自适应调节参数。  默认值：{ disableSystemAdaptation: false } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

说明

backgroundBlurStyle、blur和backdropBlur为实时接口，每帧执行实时渲染，性能负载较大。当模糊内容与模糊半径均无需变动时，推荐采用静态模糊接口[blur](js-apis-effectkit.md#blur)。最佳实践请参考[图像模糊动效优化-使用场景](../best-practices/bpta-fuzzy-scene-performance-optimization.md#section4945532519)。

## backgroundEffect11+

PhonePC/2in1TabletTVWearable

backgroundEffect(options: BackgroundEffectOptions): T

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11) | 是 | 设置组件背景属性包括：背景模糊半径、亮度、饱和度和颜色等参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundEffect18+

PhonePC/2in1TabletTVWearable

backgroundEffect(options: Optional<BackgroundEffectOptions>): T

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。与[backgroundEffect11+](ts-universal-attributes-background.md#backgroundeffect11)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional<[BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11)> | 是 | 设置组件背景属性包括：背景模糊半径、亮度、饱和度和颜色等参数。  当options的值为undefined时，恢复为无效果的背景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundEffect19+

PhonePC/2in1TabletTVWearable

backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T

设置组件背景属性，包括背景模糊半径、亮度、饱和度和颜色等参数。与[backgroundEffect18+](ts-universal-attributes-background.md#backgroundeffect18)相比，新增了sysOptions参数，即支持系统自适应调节参数。

说明

backgroundEffect接口为实时接口，每帧对模糊等效果执行实时渲染，性能负载较大。当组件背景模糊效果无需变动时，推荐采用静态模糊接口[blur](js-apis-effectkit.md#blur)实现模糊效果。最佳实践请参考：[图像模糊动效优化-使用场景](../best-practices/bpta-fuzzy-scene-performance-optimization.md#section4945532519)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional<[BackgroundEffectOptions](ts-universal-attributes-background.md#backgroundeffectoptions11)> | 是 | 设置组件背景属性包括：背景模糊半径、亮度、饱和度和颜色等参数。  当options的值为undefined时，恢复为无效果的背景。 |
| sysOptions | [SystemAdaptiveOptions](ts-universal-attributes-background.md#systemadaptiveoptions19) | 否 | 系统自适应调节参数。  默认值：{ disableSystemAdaptation: false } |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BackgroundEffectOptions11+

PhonePC/2in1TabletTVWearable

背景效果参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number | 否 | 否 | 模糊半径，取值范围：[0, +∞)，默认为0。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| saturation | number | 否 | 是 | 饱和度，取值范围：[0, +∞)，默认为1。推荐取值范围：[0, 50]。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| brightness | number | 否 | 是 | 亮度，取值范围：[0, +∞)，默认为1。推荐取值范围：[0, 2]。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| color | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 颜色，默认透明色。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| adaptiveColor | [AdaptiveColor](ts-universal-attributes-foreground-blur-style.md#adaptivecolor枚举说明) | 否 | 是 | 背景模糊效果使用的取色模式，默认为DEFAULT。使用AVERAGE时color必须带有透明度，取色模式才生效。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| blurOptions | [BlurOptions](ts-universal-attributes-foreground-blur-style.md#bluroptions11) | 否 | 是 | 灰阶模糊参数，默认为[0,0]。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| policy14+ | [BlurStyleActivePolicy](ts-universal-attributes-background.md#blurstyleactivepolicy14) | 否 | 是 | 模糊激活策略。  默认值：BlurStyleActivePolicy.ALWAYS\_ACTIVE  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| inactiveColor14+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 模糊不生效时使用的背景色。该参数需配合policy参数使用。当policy使模糊失效时，控件模糊效果会被移除，如果设置了inactiveColor会使用inactiveColor作为控件背景色。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## backgroundImageResizable12+

PhonePC/2in1TabletTVWearable

backgroundImageResizable(value: ResizableOptions): T

设置背景图在拉伸时可调整大小的图像选项。

设置合法的ResizableOptions时，[backgroundImage](ts-universal-attributes-background.md#backgroundimage)属性中的repeat参数设置不生效。

当设置top+bottom大于原图的高或者left+right大于原图的宽时，ResizableOptions属性设置不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResizableOptions](ts-basic-components-image.md#resizableoptions11) | 是 | 图像拉伸时可调整大小的图像选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BackgroundBlurStyleOptions10+对象说明

PhonePC/2in1TabletTVWearable

继承自[BlurStyleOptions](ts-universal-attributes-foreground-blur-style.md#blurstyleoptions)。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| policy14+ | [BlurStyleActivePolicy](ts-universal-attributes-background.md#blurstyleactivepolicy14) | 否 | 是 | 模糊激活策略。  默认值：BlurStyleActivePolicy.ALWAYS\_ACTIVE  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| inactiveColor14+ | [ResourceColor](ts-types.md#resourcecolor) | 否 | 是 | 模糊不生效时使用的背景色。该参数需配合policy参数使用。当policy使模糊失效时，控件模糊效果会被移除，如果设置了inactiveColor会使用inactiveColor作为控件背景色。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |

## BlurStyleActivePolicy14+

PhonePC/2in1TabletTVWearable

定义背景模糊激活策略。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FOLLOWS\_WINDOW\_ACTIVE\_STATE | 0 | 模糊效果跟随窗口焦点状态变化，非焦点不模糊，焦点模糊。 |
| ALWAYS\_ACTIVE | 1 | 一直有模糊效果。 |
| ALWAYS\_INACTIVE | 2 | 一直无模糊效果。 |

## backgroundBrightness12+

PhonePC/2in1TabletTVWearable

backgroundBrightness(params: BackgroundBrightnessOptions): T

设置组件背景提亮效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [BackgroundBrightnessOptions](ts-universal-attributes-background.md#backgroundbrightnessoptions12对象说明) | 是 | 设置组件背景提亮效果，包括：亮度变化速率，提亮程度。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## backgroundBrightness18+

PhonePC/2in1TabletTVWearable

backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T

设置组件背景提亮效果。与[backgroundBrightness12+](ts-universal-attributes-background.md#backgroundbrightness12)相比，options参数新增了对undefined类型的支持。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Optional<[BackgroundBrightnessOptions](ts-universal-attributes-background.md#backgroundbrightnessoptions12对象说明)> | 是 | 设置组件背景提亮效果，包括：亮度变化速率，提亮程度。  当options的值为undefined时，恢复为无提亮效果的背景。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## BackgroundBrightnessOptions12+对象说明

PhonePC/2in1TabletTVWearable

背景亮度选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| rate | number | 否 | 否 | 亮度变化速率。亮度变化速率越大，提亮程度下降速度越快。若rate为0，则lightUpDegree将不生效，即不会产生任何提亮效果。  默认值：0.0  取值范围：(0.0, +∞) |
| lightUpDegree | number | 否 | 否 | 提亮程度。提亮程度越大，亮度提升程度越大。  默认值：0.0  取值范围：[-1.0, 1.0] |

说明

对于组件背景内容，每个像素自身的亮度（灰阶值）的计算公式为：

Y = （0.299R + 0.587G + 0.114B）/ 255.0（R、G、B分别表示像素红色、绿色和蓝色通道的值，Y表示灰阶值），通过上述公式将像素点的灰阶值归一化至0~1的范围。

每个像素的亮度提升计算公式为：ΔY = -rate\*Y + lightUpDegree。例如，当rate=0.5，lightUpDegree=0.5时，对于灰阶值为0.2的像素点，亮度增加值为-0.5\*0.2 + 0.5 = 0.4，对于灰阶值为1的像素点，亮度增加值为-0.5\*1 + 0.5 = 0。

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置背景基础样式）

该示例通过配置backgroundColor、backgroundImage、backgroundImageSize和backgroundImagePosition设置背景的基础样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackgroundExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('background color').fontSize(9).width('90%').fontColor(0xCCCCCC)
8. Row().width('90%').height(50).backgroundColor(0xE5E5E5).border({ width: 1 })

10. Text('background image repeat along X').fontSize(9).width('90%').fontColor(0xCCCCCC)
11. Row()
12. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
13. .backgroundImage($r('app.media.image'), ImageRepeat.X)
14. .backgroundImageSize({ width: '250px', height: '140px' })
15. .width('90%')
16. .height(70)
17. .border({ width: 1 })

19. Text('background image repeat along Y').fontSize(9).width('90%').fontColor(0xCCCCCC)
20. Row()
21. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
22. .backgroundImage($r('app.media.image'), ImageRepeat.Y)
23. .backgroundImageSize({ width: '500px', height: '120px' })
24. .width('90%')
25. .height(100)
26. .border({ width: 1 })

28. Text('background image size').fontSize(9).width('90%').fontColor(0xCCCCCC)
29. Row()
30. .width('90%')
31. .height(150)
32. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
33. .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
34. .backgroundImageSize({ width: 1000, height: 500 })
35. .border({ width: 1 })

37. Text('background fill the box(Cover)').fontSize(9).width('90%').fontColor(0xCCCCCC)
38. // 不保证图片完整的情况下占满盒子
39. Row()
40. .width(200)
41. .height(50)
42. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
43. .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
44. .backgroundImageSize(ImageSize.Cover)
45. .border({ width: 1 })

47. Text('background fill the box(Contain)').fontSize(9).width('90%').fontColor(0xCCCCCC)
48. // 保证图片完整的情况下放到最大
49. Row()
50. .width(200)
51. .height(50)
52. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
53. .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
54. .backgroundImageSize(ImageSize.Contain)
55. .border({ width: 1 })

57. Text('background image position').fontSize(9).width('90%').fontColor(0xCCCCCC)
58. Row()
59. .width(100)
60. .height(50)
61. // $r('app.media.image')需要替换为开发者所需的图像资源文件。
62. .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
63. .backgroundImageSize({ width: 1000, height: 560 })
64. .backgroundImagePosition({ x: -500, y: -300 })
65. .border({ width: 1 })
66. }
67. .width('100%').height('100%').padding({ top: 5 })
68. }
69. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ovZFX15FQSCgSjUmjzRvLA/zh-cn_image_0000002558606340.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=FA2E0D42A2320DCA6246DFF4A8881985EC74D48409634EC3E33889B26E65401B)

### 示例2（设置背景模糊样式）

该示例通过backgroundBlurStyle设置背景模糊样式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackgroundBlurStyleDemo {
5. build() {
6. Column() {
7. Row() {
8. Text("Thin Material")
9. }
10. .width('50%')
11. .height('50%')
12. .backgroundBlurStyle(BlurStyle.Thin,
13. { colorMode: ThemeColorMode.LIGHT, adaptiveColor: AdaptiveColor.DEFAULT, scale: 1.0 })
14. .position({ x: '15%', y: '30%' })
15. }
16. .height('100%')
17. .width('100%')
18. // $r('app.media.bg')需要替换为开发者所需的图像资源文件
19. .backgroundImage($r('app.media.bg'))
20. .backgroundImageSize(ImageSize.Cover)
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/aATJ1dRtSiuUGNscdfEsyA/zh-cn_image_0000002589325867.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=EB9BD4C2D854D2AD20F87EE4FE278205C7112B9D18094132E75167298828C02C)

### 示例3（设置组件背景）

该示例通过background设置组件背景。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackgroundExample {
5. @Builder
6. renderBackground() {
7. Column() {
8. Progress({ value: 50 })
9. }
10. }

12. build() {
13. Column() {
14. Text("content")
15. .width(100)
16. .height(40)
17. .fontColor("#FFF")
18. .position({ x: 50, y: 80 })
19. .textAlign(TextAlign.Center)
20. .backgroundColor(Color.Green)
21. }
22. .width(200).height(200)
23. .background(this.renderBackground)
24. .backgroundColor(Color.Gray)
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/ME4IWHiBSTG3KeQgN922Ig/zh-cn_image_0000002589245809.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=298E5194D9B30913C51BA74537E42A813491A94F6128A78FF8F22229958C13C5)

### 示例4（设置组件背景提亮效果）

该示例通过backgroundBrightness设置组件背景提亮效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackgroundBrightnessDemo {
5. build() {
6. Column() {
7. Row() {
8. Text("BackgroundBrightness")
9. }
10. .width(200)
11. .height(100)
12. .position({ x: 100, y: 100 })
13. .backgroundBlurStyle(BlurStyle.Thin, { colorMode: ThemeColorMode.LIGHT, adaptiveColor: AdaptiveColor.DEFAULT})
14. .backgroundBrightness({rate:0.5,lightUpDegree:0.5}) // 背景提亮效果
15. }
16. .width('100%')
17. .height('100%')
18. // $r('app.media.image')需要替换为开发者所需的图像资源文件
19. .backgroundImage($r('app.media.image'))
20. .backgroundImageSize(ImageSize.Cover)
21. }
22. }
```

效果图如下：

rate和lightUpDegree参数值为0.5,0.5：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/v2EoCuyjTHuydwnS1TLlcQ/zh-cn_image_0000002558766000.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=6CEA9ED3DC740336607AAA71BCC5538C7D868CAC85FD9744B05EF7B3396FCAA3)

修改rate和lightUpDegree参数值为0.5,-0.1：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/cyZ_k8T_SEewDOmN9OY47A/zh-cn_image_0000002558606342.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=933747FC3F529BBB6EEBD55681D64C321D8C723817A61B2A7CD7C1CC900D0402)

去掉backgroundBrightness的设置，效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/grcGxLFDTzu5v4NzEmqwAg/zh-cn_image_0000002589325869.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=F474008F3A8F8AC12DCBAF96FE40B478C4734E513065389ABAD3581D44214EC3)

### 示例5（设置模糊属性）

该示例提供了模糊属性的实现方法。通过blur设置内容模糊，通过backdropBlur设置背景模糊。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BlurEffectsExample {
5. build() {
6. Column({ space: 10 }) {
7. // 对字体进行模糊
8. Text('font').fontSize(15).fontColor(0xCCCCCC).width('90%')
9. Flex({ alignItems: ItemAlign.Center }) {
10. Text('original').margin(10)
11. Text('blur')
12. .blur(5).margin(10)
13. Text('blur')
14. .blur(10, undefined).margin(10) // 内容模糊半径为5，禁用系统自适应优化策略。
15. Text('blur')
16. .blur(15).margin(10)
17. }.width('90%').height(40)
18. .backgroundColor(0xF9CF93)

21. // 对背景进行模糊
22. Text('backdropBlur').fontSize(15).fontColor(0xCCCCCC).width('90%')
23. Text()
24. .width('90%')
25. .height(40)
26. .fontSize(16)
27. .backdropBlur(3)
28. // $r('app.media.image')需要替换为开发者所需的图像资源文件
29. .backgroundImage($r('app.media.image'))
30. .backgroundImageSize({ width: 1200, height: 160 })
31. }.width('100%').margin({ top: 5 })
32. }
33. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Y95oPNxWTwmYKzCbtEInhQ/zh-cn_image_0000002589245811.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=76AF1F7A09890369188C2D9ED0E76DC52F1AFC6F353A2DC5BF5BA9B2B28B3645)

### 示例6（设置文字异形模糊效果）

该示例通过[blendMode](ts-universal-attributes-image-effect.md#blendmode11)和backgroundEffect实现文字异形模糊效果。

如果出现漏线问题，开发者应首先确保两个blendMode所在组件大小严格相同。如果确认相同，可能是组件边界落在浮点数坐标上导致，可尝试设置[pixelRound](ts-universal-attributes-pixelroundforcomponent.md#pixelround)通用属性，使产生的白线、暗线两侧的组件边界对齐到整数像素坐标上。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. @State shColor: Color = Color.White;
6. @State sizeDate: number = 20;
7. @State rVal: number = 255;
8. @State gVal: number = 255;
9. @State bVal: number = 255;
10. @State aVal: number = 0.1;
11. @State rad: number = 40;
12. @State satVal: number = 0.8;
13. @State briVal: number = 1.5;
14. build() {
15. Stack() {
16. // $r('app.media.image')需要替换为开发者所需的图像资源文件
17. Image($r('app.media.image'))
18. Column() {
19. Column({ space: 0 }) {
20. Column() {
21. Text('11')
22. .fontSize(144)
23. .fontWeight(FontWeight.Bold)
24. .fontColor('rgba(255,255,255,1)')
25. .fontFamily('HarmonyOS-Sans-Digit')
26. .maxLines(1)
27. .lineHeight(120 * 1.25)
28. .height(120 * 1.25)
29. .letterSpacing(4 * 1.25)
30. Text('42')
31. .fontSize(144)
32. .fontWeight(FontWeight.Bold)
33. .fontColor('rgba(255,255,255,1)')
34. .fontFamily('HarmonyOS-Sans-Digit')
35. .maxLines(1)
36. .lineHeight(120 * 1.25)
37. .height(120 * 1.25)
38. .letterSpacing(4 * 1.25)
39. .shadow({
40. color: 'rgba(0,0,0,0)',
41. radius: 20,
42. offsetX: 0,
43. offsetY: 0
44. })
45. Row() {
46. Text('10月16日')
47. .fontSize(this.sizeDate)
48. .height(22)
49. .fontWeight('medium')
50. .fontColor('rgba(255,255,255,1)')
51. Text('星期一')
52. .fontSize(this.sizeDate)
53. .height(22)
54. .fontWeight('medium')
55. .fontColor('rgba(255,255,255,1)')
56. }
57. }
58. // blendMode采用离屏渲染，DST_IN模式下仅显示当前组件与下方画布的重叠区域
59. .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)
60. .pixelRound({
61. start: PixelRoundCalcPolicy.FORCE_FLOOR ,
62. top: PixelRoundCalcPolicy.FORCE_FLOOR ,
63. end: PixelRoundCalcPolicy.FORCE_CEIL,
64. bottom: PixelRoundCalcPolicy.FORCE_CEIL
65. })
66. }
67. // blendMode采用离屏渲染，SRC_OVER模式下会将当前组件内容覆盖显示在下方画布之上
68. .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
69. // backgroundEffect配置组件背景的圆角、饱和度、亮度及动态RGBA颜色
70. .backgroundEffect({
71. radius: this.rad,
72. saturation: this.satVal,
73. brightness: this.briVal,
74. color: this.getVolumeDialogWindowColor()
75. })
76. .justifyContent(FlexAlign.Center)
77. .pixelRound({
78. start: PixelRoundCalcPolicy.FORCE_FLOOR ,
79. top: PixelRoundCalcPolicy.FORCE_FLOOR ,
80. end: PixelRoundCalcPolicy.FORCE_CEIL,
81. bottom: PixelRoundCalcPolicy.FORCE_CEIL
82. })
83. }
84. }
85. }
86. getVolumeDialogWindowColor(): ResourceColor | string {
87. return `rgba(${this.rVal.toFixed(0)}, ${this.gVal.toFixed(0)}, ${this.bVal.toFixed(0)}, ${this.aVal.toFixed(0)})`;
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/MswH0M-fRImddQmJDYhmLw/zh-cn_image_0000002558766002.jpeg?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=79849F401526F72A733573D80DF1A05106FA04C28FDD313FD4E3E4E03722E5AF)

### 示例7（模糊效果对比）

该示例对比了[backgroundEffect11+](ts-universal-attributes-background.md#backgroundeffect11)、[backdropBlur](ts-universal-attributes-background.md#backdropblur)和[backgroundBlurStyle9+](ts-universal-attributes-background.md#backgroundblurstyle9)三种不同的模糊效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct BackGroundBlur {
5. private imageSize: number = 150;

7. build() {
8. Column({ space: 5 }) {
9. // backgroundBlurStyle通过枚举值的方式设置模糊参数
10. Stack() {
11. // $r('app.media.test')需要替换为开发者所需的图像资源文件
12. Image($r('app.media.test'))
13. .width(this.imageSize)
14. .height(this.imageSize)
15. Column()
16. .width(this.imageSize)
17. .height(this.imageSize)
18. .backgroundBlurStyle(BlurStyle.Thin)
19. }

21. // backgroundEffect 可以自定义设置 模糊半径，亮度，饱和度等参数
22. Stack() {
23. // $r('app.media.test')需要替换为开发者所需的图像资源文件
24. Image($r('app.media.test'))
25. .width(this.imageSize)
26. .height(this.imageSize)
27. Column()
28. .width(this.imageSize)
29. .height(this.imageSize)
30. .backgroundEffect({ radius: 20, brightness: 0.6, saturation: 15 })
31. }

33. // backdropBlur 只能设置模糊半径和灰阶参数
34. Stack() {
35. // $r('app.media.test')需要替换为开发者所需的图像资源文件
36. Image($r('app.media.test'))
37. .width(this.imageSize)
38. .height(this.imageSize)
39. Column()
40. .width(this.imageSize)
41. .height(this.imageSize)
42. .backdropBlur(20, { grayscale: [30, 50] })
43. }
44. }
45. .width('100%')
46. .padding({ top: 5 })
47. }
48. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/UAsh21itSNa4x7JuNfLdyQ/zh-cn_image_0000002558606344.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=F50379D6F85F08DD748D1A80587695B2BE17E04E5ADAE33CB5D783D10214E793)

### 示例8（设置P3色域背景效果）

从API version 20开始，该示例通过[backgroundColor](ts-universal-attributes-background.md#backgroundcolor20)设置P3色域背景效果。

```
1. // xxx.ets
2. // 设置P3色域时需要在ets/entryability/EntryAbility.ets中，通过setColorSpace接口将当前窗口设置为广色域。
3. import { ColorMetrics } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct P3BackgroundDemo {
8. @State p3Color: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 0.3, 0.8, 1);

10. build() {
11. Column({ space: 5 }) {
12. Text('background color with colorMetrics').fontSize(9).width('90%').fontColor(0xCCCCCC)
13. Row().width('90%').height(50).backgroundColor(this.p3Color)
14. }
15. .width('100%')
16. .height('100%')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/_EJmyN5eSPWRCd2gmWmvFQ/zh-cn_image_0000002589325871.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=2A070111AB4006EAFBBF517BF8CDBA86C58528DD6A8448933596F3B2DA7B3FC2)

### 示例9（设置组件背景扩展）

从API version 20开始，该示例通过[background](ts-universal-attributes-background.md#background10)实现组件背景扩展到父组件的安全区。

```
1. import { LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct BackgroundExtension {
6. @Builder
7. myImages() {
8. Column() {
9. Image($r('app.media.startIcon'))
10. .width('100%')
11. .height('100%')
12. }
13. }

15. build() {
16. Column({space: 10}) {
17. Stack() {
18. // CustomBuilder类型的背景设置了ignoresLayoutSafeAreaEdges属性，背景扩展到父组件安全区
19. Column()
20. .size({ width: '100%', height: '100%' })
21. .border({ width: 1, color: Color.Red })
22. .background(
23. this.myImages(),
24. { align: Alignment.Center , ignoresLayoutSafeAreaEdges: [ LayoutSafeAreaEdge.START, LayoutSafeAreaEdge.TOP ] }
25. )
26. }
27. .size({ width: 300, height: 300 })
28. .backgroundColor('#004aaf')
29. .safeAreaPadding(LengthMetrics.vp(50))

31. Stack() {
32. // ResourceColor类型的背景未设置ignoresLayoutSafeAreaEdges属性，背景默认扩展到父组件安全区
33. Column()
34. .size({ width: '100%', height: '100%' })
35. .border({ width: 1, color: Color.Red })
36. .background('#d5d5d5', { align: Alignment.Center })
37. }
38. .size({ width: 300, height: 300 })
39. .backgroundColor('#707070')
40. .safeAreaPadding(LengthMetrics.vp(50))
41. }
42. .margin(10)
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/DBXDqp_8QFGKBfujvyrkfA/zh-cn_image_0000002589245813.png?HW-CC-KV=V1&HW-CC-Date=20260429T055112Z&HW-CC-Expire=86400&HW-CC-Sign=D544C665127EB689CC4E8A4BAECCF38EBBF200A9563767CFD3C3480DBCAFCBB9)
