---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-image
title: Image
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图片与视频 > Image
category: harmonyos-references
scraped_at: 2026-04-28T08:01:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c8de0ad5ed9f31f2aa4925e069e4c80362efe8130047f2d77a572e762a993e04
---

Image为图片组件，常用于在应用中显示图片。Image支持加载[PixelMap](arkts-apis-image-pixelmap.md)、[ResourceStr](ts-types.md#resourcestr)和[DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10)类型的数据源，支持png、jpg、jpeg、bmp、svg、webp、gif、heif和tiff类型的图片格式，不支持apng和svga格式。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 从API version 23开始，图片类型新增支持tiff格式。
* 使用快捷组合键对Image组件复制时，Image组件必须处于获焦状态，如何获焦请参考[设置组件是否可获焦](../harmonyos-guides/arkts-common-events-focus-event.md#设置组件是否可获焦)。Image组件默认不获焦，需将[focusable](ts-universal-attributes-focus.md#focusable)属性设置为true，即可使用Tab键将焦点切换到组件上，再将[focusOnTouch](ts-universal-attributes-focus.md#focusontouch9)属性设置为true，即可实现点击获焦。
* 图片格式支持SVG图源，SVG标签文档请参考[SVG标签说明](ts-basic-svg.md)。
* 动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，通过回调启动动画，当节点不可见时，停止动画。可见性状态的判断是通过[onVisibleAreaChange](ts-universal-component-visible-area-change-event.md#onvisibleareachange)事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。
* 如果图片加载过程中出现白色块，请参考[Image白块问题解决方案](../best-practices/bpta-image-white-lump-solution.md)。如果图片加载时间过长，请参考[预置图片资源加载优化](../best-practices/bpta-texture-compression-improve-performance.md#section91526132216)。

## 需要权限

PhonePC/2in1TabletTVWearable

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

### Image

PhonePC/2in1TabletTVWearable

Image(src: PixelMap | ResourceStr | DrawableDescriptor)

通过图片数据源获取图片，用于后续渲染展示。

Image组件加载图片失败或图片尺寸为0时，图片组件大小自动为0，不跟随父组件的布局约束。

Image组件默认按照居中裁剪，例如组件宽高设置相同，原图长宽不等，此时按照中间区域进行裁剪。

Image加载成功且组件不设置宽高时，其显示大小自适应父组件。

说明

* Image直接传入URL可能会带来的潜在性能问题，例如：(1) 大图加载时无法提前下载，白块显示的时间较长；(2) 小图设置同步加载，在弱网环境下，可能会阻塞UI线程造成冻屏问题；(3) 在快速滑动的瀑布流中，无法提前对即将要显示的图片进行下载，导致滑动白块较多。不同场景下，性能问题会有不同的表现，建议将网络下载部分与Image的显示剥离，可提前下载或者异步下载。如果图片加载过程中出现白色块，请参考[Image白块解决方案](../best-practices/bpta-image-white-lump-solution.md)。如果图片加载时间过长，请参考[预置图片资源加载优化](../best-practices/bpta-texture-compression-improve-performance.md)。
* src由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。
* 当Image组件入参为[PixelMap](arkts-apis-image-pixelmap.md)类型时，只有当PixelMap对象发生变化（即指向一个新的PixelMap实例），Image组件才能感知到数据的变化。仅修改PixelMap对象的内容（如像素值）而不更换对象引用，无法触发数据变化的感知。
* Image组件入参为Base64字符串时，Base64字符串通用格式为data:image/subtype;base64,Base64EncodedData，其中subtype为类型声明，Base64EncodedData为数据对应的base64编码，其他为固定字符串。例如：png图像对应的入参为data:image/png;base64,iVBORw0KGgo...。

  1. image/subType用于声明数据内容的类型。Image组件不会强制校验声明的类型与Base64解码后的实际图片格式是否完全一致。在部分场景下，即使声明的类型与真实格式不一致，图片仍可能正常显示。为避免未来行为变化或未知问题，建议始终保持类型与实际图片格式一致。
  2. Image组件不支持data:image/\*;base64,Base64EncodedData的通配写法，subType必须显式声明具体的图片类型。
  3. Image组件不支持通过Base64字符串形式加载SVG图片。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](ts-image-common.md#pixelmap) | [ResourceStr](ts-types.md#resourcestr)| [DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10) | 是 | 图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。  1. PixelMap格式为像素图，常用于图片编辑的场景。  2. ResourceStr包含Resource和string格式。  string格式可用于加载网络图片和本地图片，常用于加载网络图片。当[使用相对路径引用本地图片](ts-basic-components-image.md#示例25使用相对路径显示图片)时，不支持跨包/跨模块调用该Image组件，建议使用Resource格式来管理需全局使用的图片资源。  从DevEco Studio 6.0.0 Beta2版本开始，新建工程或模块时，默认创建的模块不会对非resource目录下的资源进行打包，需使能相关开关：模块的build-profile.json5中buildOption > resOptions > copyCodeResource > enable 设置为true，详见[resOptions](../harmonyos-guides/ide-hvigor-build-profile.md#table1476161719356)中相关介绍。  - 支持Base64字符串。  - 传入的字符串为https网络图片地址时，建议参考[示例2下载与显示静态网络图片](ts-basic-components-image.md#示例2下载与显示静态网络图片)。  - 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](js-apis-file-fileuri.md#constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](js-apis-file-fileuri.md#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。  Resource格式可以跨包/跨模块访问资源文件，是访问本地图片的推荐方式，具体示例参考[跨HAP/HSP包应用资源](../harmonyos-guides/resource-categories-and-access.md#跨haphsp包应用资源)。  3. 当传入资源id或name为普通图片时，生成DrawableDescriptor对象。传入[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)类型可播放PixelMap数组动画。  **说明：**  - ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。  - ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。 |

### Image12+

PhonePC/2in1TabletTVWearable

Image(src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent)

src新增[ImageContent](ts-basic-components-image.md#imagecontent12)类型，可指定对应的图形内容。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](ts-image-common.md#pixelmap) | [ResourceStr](ts-types.md#resourcestr)| [DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10)| [ImageContent](ts-basic-components-image.md#imagecontent12) | 是 | 图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。  PixelMap、ResourceStr和DrawableDescriptor的使用请参考[Image](ts-basic-components-image.md#image-1)的src参数说明。  传入[ImageContent](ts-basic-components-image.md#imagecontent12)类型，指定图像内容。  **说明：**  - ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。  - ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。 |

### Image12+

PhonePC/2in1TabletTVWearable

Image(src: PixelMap | ResourceStr | DrawableDescriptor, imageAIOptions: ImageAIOptions)

Image新增[imageAIOptions](ts-image-common.md#imageaioptions12)参数，为组件设置AI分析选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](ts-image-common.md#pixelmap) | [ResourceStr](ts-types.md#resourcestr)| [DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10) | 是 | 图片的数据源，支持本地图片和网络图片，引用方式请参考[加载图片资源](../harmonyos-guides/arkts-graphics-display.md#加载图片资源)。  PixelMap、ResourceStr和DrawableDescriptor的使用请参考[Image](ts-basic-components-image.md#image-1)的src参数说明。  **说明：**  - ArkTS卡片上支持gif图片格式动效，但仅在显示时播放一次。  - ArkTS卡片上不支持http://等网络相关路径前缀和file://路径前缀的字符串。 |
| imageAIOptions | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

## 属性

PhonePC/2in1TabletTVWearable

属性的详细使用指导请参考[添加属性](../harmonyos-guides/arkts-graphics-display.md#添加属性)。除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

说明

Image组件不支持设置通用属性[foregroundColor](ts-universal-attributes-foreground-color.md#foregroundcolor)，可以通过Image组件的[fillColor](ts-basic-components-image.md#fillcolor)属性设置填充颜色。

### alt

PhonePC/2in1TabletTVWearable

alt(value: string | Resource | PixelMap)

设置图片加载过程中显示的占位图。

占位图支持使用[objectFit](ts-basic-components-image.md#objectfit)设置填充效果，与图片的填充效果一致。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | [Resource](ts-types.md#resource) | [PixelMap](arkts-apis-image-pixelmap.md)12+ | 是 | 设置图片加载过程中显示的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），支持[PixelMap](arkts-apis-image-pixelmap.md)类型图片，不支持网络图片。  - 支持Base64字符串。  - 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](js-apis-file-fileuri.md#constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](js-apis-file-fileuri.md#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。  默认值：null  由有效值（可正常解析并加载的图片资源）切换为无效值（无法解析或加载的图片路径）时，组件保持显示此前成功加载的图片内容，不进行清除或重置操作。 |

### alt22+

PhonePC/2in1TabletTVWearable

alt(src: ResourceStr | PixelMap | ImageAlt)

设置图片加载过程中和加载失败时的占位图。

说明

通过[ImageAlt](ts-basic-components-image.md#imagealt22)配置占位图时，Image会根据用户配置的加载过程中和加载失败的占位图源生效，未配置时默认不显示。

占位图支持使用[objectFit](ts-basic-components-image.md#objectfit)设置填充效果，与图片的填充效果一致。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md)| [ImageAlt](ts-basic-components-image.md#imagealt22) | 是 | 设置图片加载过程中和加载失败时的占位图，支持本地图片（png、jpg、bmp、svg、gif和heif类型），支持[PixelMap](arkts-apis-image-pixelmap.md)类型图片，不支持网络图片。  - 支持Base64字符串。  - 支持file://路径前缀的字符串，应用沙箱URI：file://<bundleName>/<sandboxPath>。应用沙箱路径URI构造可参考[constructor](js-apis-file-fileuri.md#constructor10)。沙箱路径需要使用[fileUri.getUriFromPath(path)](js-apis-file-fileuri.md#fileurigeturifrompath)方法将路径转换为应用沙箱URI，然后传入显示。同时需要保证目录包路径下的文件有可读权限。 |

### objectFit

PhonePC/2in1TabletTVWearable

objectFit(value: ImageFit)

设置图片的填充效果。未通过该接口设置时，默认为ImageFit.Cover，保持宽高比进行缩小或者放大。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](ts-appendix-enums.md#imagefit) | 是 | 图片的填充效果。 |

### imageMatrix15+

PhonePC/2in1TabletTVWearable

imageMatrix(matrix: ImageMatrix)

设置图片的变换矩阵。通过[ImageMatrix](ts-basic-components-image.md#imagematrix15对象说明)对象使用平移、旋转、缩放等函数，实现宫格缩略图的最佳呈现。SVG类型图源不支持该属性。

设置[resizable](ts-basic-components-image.md#resizable11)、[objectRepeat](ts-basic-components-image.md#objectrepeat)属性时，该属性设置不生效。该属性只针对图源做处理，不会触发Image组件的回调事件。

该属性与[objectFit](ts-basic-components-image.md#objectfit)属性强关联，仅在[objectFit](ts-basic-components-image.md#objectfit)属性设置为ImageFit.MATRIX时生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [ImageMatrix](ts-basic-components-image.md#imagematrix15对象说明) | 是 | 图片的变换矩阵。 |

### objectRepeat

PhonePC/2in1TabletTVWearable

objectRepeat(value: ImageRepeat)

设置图片的重复样式，从中心点向两边重复，剩余空间不足放下一张图片时会截断。SVG类型图源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageRepeat](ts-appendix-enums.md#imagerepeat) | 是 | 图片的重复样式。  默认值：ImageRepeat.NoRepeat |

### interpolation

PhonePC/2in1TabletTVWearable

interpolation(value: ImageInterpolation)

定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageInterpolation](ts-basic-components-image.md#imageinterpolation) | 是 | 图片的插值效果。  默认值：ImageInterpolation.Low  设置undefined时，取值为ImageInterpolation.None。 |

### renderMode

PhonePC/2in1TabletTVWearable

renderMode(value: ImageRenderMode)

设置图片的渲染模式。SVG类型图源不支持该属性。

设置[ColorFilter](ts-basic-components-image.md#colorfilter9)时，该属性设置不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageRenderMode](ts-basic-components-image.md#imagerendermode) | 是 | 图片的渲染模式为原色或黑白。  默认值：ImageRenderMode.Original |

### sourceSize

PhonePC/2in1TabletTVWearable

sourceSize(value: ImageSourceSize)

设置图片解码尺寸。仅在目标尺寸小于图源尺寸时生效。SVG类型图源和PixelMap资源不支持该属性。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageSourceSize](ts-basic-components-image.md#imagesourcesize18对象说明) | 是 | 图片解码尺寸参数，降低图片的分辨率，常用于需要让图片显示尺寸比组件尺寸更小的场景。和[objectFit](ts-basic-components-image.md#objectfit)接口的ImageFit.None配合使用时可在组件内显示小图。 |

### matchTextDirection

PhonePC/2in1TabletTVWearable

matchTextDirection(value: boolean)

设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 图片是否跟随系统语言方向。  默认值：false，false表示图片不跟随系统语言方向，true表示图片跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。 |

### fitOriginalSize

PhonePC/2in1TabletTVWearable

fitOriginalSize(value: boolean)

设置图片的显示尺寸是否跟随图源尺寸。

图片组件已设置width、height属性时，fitOriginalSize属性不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 图片的显示尺寸是否跟随图源尺寸。  默认值：false  **说明：**  当不设置fitOriginalSize或者设置fitOriginalSize为false时，组件显示大小不跟随图源大小。  当设置fitOriginalSize为true时，组件显示大小跟随图源大小。 |

### fillColor

PhonePC/2in1TabletTVWearable

fillColor(value: ResourceColor)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](ts-basic-components-image.md#colorfilter9)。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResourceColor](ts-types.md#resourcecolor) | 是 | 设置填充颜色。  **说明：**  默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。  从API version 21开始，当[supportSvg2](ts-basic-components-image.md#supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。当supportSvg2设置为false时，fillColor生效，替换SVG图片中所有可绘制元素的填充颜色。 |

### fillColor15+

PhonePC/2in1TabletTVWearable

fillColor(color: ResourceColor|ColorContent)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](ts-basic-components-image.md#colorfilter9)。如果想重置填充颜色可以传入[ColorContent](ts-basic-components-image.md#colorcontent15)类型。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor)|[ColorContent](ts-basic-components-image.md#colorcontent15) | 是 | 设置填充颜色。  **说明：**  默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。  从API version 21开始，当[supportSvg2](ts-basic-components-image.md#supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。 |

### fillColor20+

PhonePC/2in1TabletTVWearable

fillColor(color: ResourceColor|ColorContent|ColorMetrics)

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用[colorFilter](ts-basic-components-image.md#colorfilter9)。如果想重置填充颜色可以传入[ColorContent](ts-basic-components-image.md#colorcontent15)类型。支持通过传入[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)类型设置P3色域颜色值，可在支持高色域的设备上获得更丰富的色彩表现。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor)|[ColorContent](ts-basic-components-image.md#colorcontent15)|[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12) | 是 | 设置填充颜色。  **说明：**  默认不对组件进行填充。当传入异常值时，系统将使用默认的主题色：浅色模式下为黑色，深色模式下为白色。  从API version 21开始，当[supportSvg2](ts-basic-components-image.md#supportsvg221)设置为true时，fillColor依赖SVG图源中fill属性的参数配置。当SVG图源中fill属性为'none'时，fillColor不生效。 |

### autoResize

PhonePC/2in1TabletTVWearable

autoResize(value: boolean)

设置图片解码过程中是否对图源自动缩放。降采样解码时图片的部分信息丢失，因此可能会导致图片质量的下降（如：出现锯齿），这时可以选择把autoResize设为false，按原图尺寸解码，提升显示效果，但会增加内存占用。

原图尺寸和显示尺寸不匹配时，图片都会出现些许的失真、模糊。最佳清晰度配置建议：

图片缩小显示时：.autoResize(false) + .interpolation(.Medium)

图片放大显示时：.interpolation(.High)

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)和SVG时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 图片解码过程中是否对图源自动缩放。设置为true时，组件会根据显示区域的尺寸决定用于绘制的图源尺寸，有利于减少内存占用。如原图大小为800x1200，而显示区域大小为200x200，则图片会降采样解码到200x300的尺寸（实际计算过程中会依赖缩放和填充类型的配置，从而得到的计算结果会有差异），从而大幅度节省图片占用的内存。  默认值：false，false表示关闭图源自动缩放，true表示开启图源自动缩放。 |

### syncLoad8+

PhonePC/2in1TabletTVWearable

syncLoad(value: boolean)

设置是否同步加载图片。建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

如果加载图片时出现闪烁，设置syncLoad为true。详情请参见[并发优化](../best-practices/bpta-click-to-click-response-optimization.md#section715115119192)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否同步加载图片，默认是异步加载。同步加载时阻塞UI线程，不会显示占位图。  默认值：false，false表示异步加载图片，true表示同步加载图片。  阻塞主线程超过6s将导致AppFreeze，具体参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。 |

### copyOption9+

PhonePC/2in1TabletTVWearable

copyOption(value: CopyOptions)

设置图片是否可复制。当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、快捷组合键'CTRL+C'等方式进行复制。SVG图片不支持复制。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](ts-appendix-enums.md#copyoptions9) | 是 | 图片是否可复制。  默认值：CopyOptions.None |

### colorFilter9+

PhonePC/2in1TabletTVWearable

colorFilter(value: ColorFilter | DrawingColorFilter)

为图像设置颜色滤镜效果。

设置该属性时，[renderMode](ts-basic-components-image.md#rendermode)属性设置不生效。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ColorFilter](ts-types.md#colorfilter9) | [DrawingColorFilter12+](ts-basic-components-image.md#drawingcolorfilter12) | 是 | 1. 给图像设置颜色滤镜效果，入参为一个的4x5的RGBA转换矩阵。  2. 从API version12开始支持@ohos.graphics.drawing的ColorFilter类型作为入参。  **说明：**  API version 11及之前，SVG类型图源不支持该属性。  从API version 12开始，该接口中的DrawingColorfilter类型支持在元服务中使用。其中，SVG类型的图源只有设置了stroke属性（无论是否有值）才会生效。  从API version 21开始，当[supportSvg2](ts-basic-components-image.md#supportsvg221)属性设置为true时，colorFilter属性对整个SVG图源起作用。 |

颜色滤镜通过一个4x5的矩阵来设置图像的颜色滤镜，矩阵第一行表示R（红色）的向量值，第二行表示G（绿色）的向量值，第三行表示B（蓝色）的向量值，第四行表示A（透明度）的向量值，4行分别代表不同的RGBA的向量值。

当矩阵对角线值为1，其余值为0时，保持图片原有色彩。

**计算规则：**

如果输入的滤镜矩阵如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/vw7CsG1wTqKfhW3rPRGD8Q/zh-cn_image_0000002583439857.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=3C8FEF30098ABDD47F7422961E697F8C2F39540788780168D20C30A4375D09F0)

像素点为[R, G, B, A]，色值的范围[0, 255]

则过滤后的颜色为 [R’, G’, B’, A’]

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/RDhzqRzAQ3iZGXlx07nMaQ/zh-cn_image_0000002552959812.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=63C4628F6D0865B8E85FB802375D6D5DFD2F8424953AA2F54E1CBF75E9E4E528)

该属性的具体使用可以参考[示例9](ts-basic-components-image.md#示例9为图像设置颜色滤镜效果)。

### draggable9+

PhonePC/2in1TabletTVWearable

draggable(value: boolean)

设置组件默认拖拽效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 组件默认拖拽效果，设置为true时，组件可拖拽，绑定的长按手势不生效。  API version 9及之前，默认值为false。API version 10及之后，默认值为true。  若用户需要设置自定义手势，则需要将draggable设置为false。设置为false之后，拖拽类事件不再触发。 |

### enableAnalyzer11+

PhonePC/2in1TabletTVWearable

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。具体使用指导请参考[AI识图](../harmonyos-guides/vision-imageanalyzer.md)。

不能和[overlay](ts-universal-attributes-overlay.md#overlay)属性同时使用，两者同时设置时overlay中[CustomBuilder](ts-types.md#custombuilder8)属性将失效。该特性依赖设备能力。

分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](arkts-apis-image-pixelmap.md)进行分析，目前仅支持[RGBA\_8888](arkts-apis-image-e.md#pixelmapformat7)类型，使用方式见[示例5开启图像AI分析](ts-basic-components-image.md#示例5开启图像ai分析)。

[alt](ts-basic-components-image.md#alt)占位图不支持分析，[objectRepeat](ts-basic-components-image.md#objectrepeat)属性仅在取值为ImageRepeat.NoRepeat时支持分析，隐私遮罩属性[obscured](ts-universal-attributes-obscured.md#obscured)打开时不支持分析。

基于完整原始图像进行分析，设置[clip](ts-universal-attributes-sharp-clipping.md#clip12)、[margin](ts-universal-attributes-size.md#margin)、[borderRadius](ts-universal-attributes-border.md#borderradius)、[position](ts-universal-attributes-location.md#position)和[objectFit](ts-basic-components-image.md#objectfit)属性导致图像显示不完整，或使用[renderMode](ts-basic-components-image.md#rendermode)设置蒙层，仍基于完整原始图像进行分析。 [copyOption](ts-basic-components-image.md#copyoption9)属性不影响AI分析功能。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时设置该属性不生效。

说明

* 需要配置权限：ohos.permission.INTERNET。
* 从API version 12开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | Image组件是否支持AI分析。  设置为true时，Image组件支持AI分析。设置为false时，Image组件不支持AI分析。  默认值：false |

### resizable11+

PhonePC/2in1TabletTVWearable

resizable(value: ResizableOptions)

设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。

设置合法的 [ResizableOptions](ts-basic-components-image.md#resizableoptions11) 时，objectRepeat属性、antialiased属性和orientation属性设置不生效。

当设置 top +bottom 大于原图的高或者 left + right 大于原图的宽时 [ResizableOptions](ts-basic-components-image.md#resizableoptions11) 属性设置不生效。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)和SVG时设置该属性不生效。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResizableOptions](ts-basic-components-image.md#resizableoptions11) | 是 | 图像拉伸时可调整大小的图像选项。 |

### privacySensitive12+

PhonePC/2in1TabletTVWearable

privacySensitive(supported: boolean)

设置是否支持卡片敏感隐私信息。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean | 是 | 是否支持卡片敏感隐私信息。  默认值为false，表示不支持卡片敏感隐私信息，当设置为true时，隐私模式下图片将显示为半透明底板样式。  **说明：**  设置null则不敏感。  进入隐私模式需要卡片框架支持。 |

### dynamicRangeMode12+

PhonePC/2in1TabletTVWearable

dynamicRangeMode(value: DynamicRangeMode)

设置期望展示的图像动态范围。SVG类型图源不支持该属性。

**设备行为差异：** 该接口在手机、PC/2in1和Tablet设备中可正常生效，在其他设备类型中无效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DynamicRangeMode](ts-basic-components-image.md#dynamicrangemode12枚举说明) | 是 | 图像显示的动态范围。  默认值：DynamicRangeMode.STANDARD |

### orientation14+

PhonePC/2in1TabletTVWearable

orientation(orientation: ImageRotateOrientation)

设置图像内容的显示方向。

该属性对[alt](ts-basic-components-image.md#alt)占位图不生效。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 14开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [ImageRotateOrientation](ts-basic-components-image.md#imagerotateorientation14) | 是 | 图像内容的显示方向。  仅支持静态位图的显示。  如果需要显示携带旋转角度信息或翻转信息的图片，建议使用ImageRotateOrientation.AUTO进行设置。  默认值：ImageRotateOrientation.UP  设置为undefined或null时，取值为ImageRotateOrientation.AUTO。 |

### hdrBrightness19+

PhonePC/2in1TabletTVWearable

hdrBrightness(brightness: number)

设置组件在显示HDR图片时的亮度。

SVG类型图源不支持该属性。

该属性与[dynamicRangeMode](ts-basic-components-image.md#dynamicrangemode12)属性同时设置时，[dynamicRangeMode](ts-basic-components-image.md#dynamicrangemode12)属性不生效。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 用于调整组件展示HDR图片的亮度，该接口仅对HDR图源生效。  默认值：1.0  取值范围：[0.0，1.0]，小于0和大于1.0时取1.0。0表示图片按照SDR亮度显示，1.0表示图片按照当前允许的最高HDR亮度显示。 |

### supportSvg221+

PhonePC/2in1TabletTVWearable

supportSvg2(enable: boolean)

开启或关闭[SVG标签解析能力增强功能](ts-image-svg2-capabilities.md)，开启后相关SVG图片显示效果会有变化。

Image组件创建后，不支持动态修改该属性的值。

**卡片能力：** 从API version 21开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 控制是否开启SVG标签解析能力增强功能。  默认值：false  true：支持SVG解析新能力；false：保持原有SVG解析能力。 |

### contentTransition21+

PhonePC/2in1TabletTVWearable

contentTransition(transition: ContentTransitionEffect)

图片内容发生变化时，触发过渡动效。

**元服务API：** 从API version 21开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | [ContentTransitionEffect](ts-image-common.md#contenttransitioneffect21对象说明) | 是 | 过渡动效的类型。  其中取值为ContentTransitionEffect.OPACITY表示淡入淡出效果，取值为ContentTransitionEffect.IDENTITY表示无动画效果。  默认值：ContentTransitionEffect.IDENTITY  设置为undefined或null时，取默认值ContentTransitionEffect.IDENTITY。  **说明**：对动态图片资源不生效。 |

### antialiased23+

PhonePC/2in1TabletTVWearable

antialiased(isAntialiased: Optional<boolean>)

设置位图图片边缘是否开启抗锯齿。未通过该接口设置时，默认不开启抗锯齿。SVG类型图片不支持该属性。

说明

如果图片设置了背景色属性([backgroundColor](ts-universal-attributes-background.md#backgroundcolor))，图片的抗锯齿属性设置为true不会影响背景色的锯齿效果。

和[resizable](ts-basic-components-image.md#resizable11)一起使用时，该属性不生效。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAntialiased | Optional<boolean> | 是 | 设置位图图片边缘是否开启抗锯齿。  true表示开启边缘抗锯齿；false表示不开启边缘抗锯齿。  设置为undefined时，不开启边缘抗锯齿。 |

## ImageContent12+

PhonePC/2in1TabletTVWearable

指定图像内容。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EMPTY | 0 | 空图像。 |

## ImageInterpolation

PhonePC/2in1TabletTVWearable

图片的插值效果。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| None | 0 | 最近邻插值。 |
| Low | 1 | 双线性插值。 |
| Medium | 2 | MipMap插值。 |
| High | 3 | Cubic插值，插值质量最高，可能会影响图片渲染的速度。 |

## ImageRenderMode

PhonePC/2in1TabletTVWearable

图片的渲染模式。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Original | 0 | 原色渲染模式。 |
| Template | 1 | 黑白渲染模式。 |

## ResizableOptions11+

PhonePC/2in1TabletTVWearable

图像拉伸时可调整大小的图像选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slice | [EdgeWidths](ts-types.md#edgewidths9) | 否 | 是 | 边框宽度类型，用于描述组件边框不同方向的宽度。  **说明：**  只有当bottom和right同时大于0时，该属性生效。  当设置了top时，图片顶部拉伸，图片的像素值保持不变。  当设置了right时，图片右部拉伸，图片的像素值保持不变。  当设置了bottom时，图片底部拉伸，图片的像素值保持不变。  当设置了left时，图片左部拉伸，图片的像素值保持不变。  每个方向的宽度默认值为0，传入数字时默认单位为vp。  设置了EdgeWidths后的效果如图1（设置EdgeWidths效果图）所示。 |
| lattice12+ | [DrawingLattice](ts-basic-components-image.md#drawinglattice12) | 否 | 是 | 矩形网格对象。  **说明：**  通过@ohos.graphics.drawing的[createImageLattice](arkts-apis-graphics-drawing-lattice.md#createimagelattice12)接口创建Lattice类型作为入参。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格图像是固定的，不会被拉伸。其他位置的网格图像会根据slice进行拉伸。  该参数对[backgroundImageResizable](ts-universal-attributes-background.md#backgroundimageresizable12)接口不生效。  传入数字时默认单位为px。 |

**图1** 设置EdgeWidths效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/SL0sLXSFQh2tdsFw4S_lRA/zh-cn_image_0000002583439873.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=4680F25A57DA8C2DDD9AF0D37309C0E2FBACDB0C412035595BC16DDE4F78FF82)

## ImageAlt22+

PhonePC/2in1TabletTVWearable

设置图片占位图。

**卡片能力：** 从API version 22开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| placeholder | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 加载过程中的占位图。 |
| error | [ResourceStr](ts-types.md#resourcestr) | [PixelMap](arkts-apis-image-pixelmap.md) | 否 | 是 | 加载失败的占位图。 |

## DynamicRangeMode12+枚举说明

PhonePC/2in1TabletTVWearable

期望展示的图像动态范围。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| HIGH | 0 | 不受限动态范围，最大限度进行图片提亮。 |
| CONSTRAINT | 1 | 受限动态范围，受限进行图片提亮。 |
| STANDARD | 2 | 标准动态范围，不进行图片提亮。 |

## ImageRotateOrientation14+

PhonePC/2in1TabletTVWearable

期望的图像内容显示方向。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| AUTO | 0 | 读取图片携带的EXIF元数据作为显示方向，支持旋转和镜像。  [PixelMap](arkts-apis-image-pixelmap.md)和[DrawableDescriptor](ts-basic-components-image.md#drawabledescriptor10)类型的图片不包含头信息，调用该接口时图片显示效果不变化。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| UP | 1 | 默认按照当前图片的像素数据进行显示，不做任何处理。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| RIGHT | 2 | 将当前图片顺时针旋转90度后显示。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| DOWN | 3 | 将当前图片顺时针旋转180度后显示。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| LEFT | 4 | 将当前图片顺时针旋转270度后显示。  **元服务API：** 从API version 14开始，该接口支持在元服务中使用。 |
| UP\_MIRRORED20+ | 5 | 将当前图片水平翻转后显示。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| RIGHT\_MIRRORED20+ | 6 | 将当前图片水平翻转再顺时针旋转90度后显示。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| DOWN\_MIRRORED20+ | 7 | 将当前图片垂直翻转后显示。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| LEFT\_MIRRORED20+ | 8 | 将当前图片水平翻转再顺时针旋转270度后显示。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ImageSourceSize18+对象说明

PhonePC/2in1TabletTVWearable

图片解码尺寸。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| width7+ | number | 否 | 否 | 图片解码尺寸宽度。  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| height7+ | number | 否 | 否 | 图片解码尺寸高度。  单位：vp  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## DrawableDescriptor10+

PhonePC/2in1TabletTVWearable

type DrawableDescriptor = DrawableDescriptor

作为Image组件的入参对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DrawableDescriptor](js-apis-arkui-drawabledescriptor.md#drawabledescriptor) | 返回一个DrawableDescriptor对象。 |

## DrawingColorFilter12+

PhonePC/2in1TabletTVWearable

type DrawingColorFilter = ColorFilter

颜色滤波器对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [ColorFilter](arkts-apis-graphics-drawing-colorfilter.md) | 返回一个颜色滤波器。 |

## DrawingLattice12+

PhonePC/2in1TabletTVWearable

type DrawingLattice = Lattice

将图片按照矩形网格进行划分。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Lattice](arkts-apis-graphics-drawing-lattice.md) | 返回一个矩阵网格对象。 |

## ImageMatrix15+对象说明

PhonePC/2in1TabletTVWearable

type ImageMatrix = Matrix4Transit

当前的矩阵对象。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [Matrix4Transit](js-apis-matrix4.md#matrix4transit) | 返回当前的矩阵对象。 |

## ColorContent15+

PhonePC/2in1TabletTVWearable

指定颜色填充内容。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| ORIGIN | ColorContent | 是 | 否 | 重置[fillColor](ts-basic-components-image.md#fillcolor)接口，效果上与不设置[fillColor](ts-basic-components-image.md#fillcolor)一致。 |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onComplete

PhonePC/2in1TabletTVWearable

onComplete(callback: (event?: { width: number, height: number, componentWidth: number, componentHeight: number, loadingStatus: number,contentWidth: number, contentHeight: number, contentOffsetX: number, contentOffsetY: number }) => void)

图片数据加载成功和解码成功时均触发该回调，返回成功加载的图片尺寸。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | number | 是 | 图片的宽。  单位：px  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| height | number | 是 | 图片的高。  单位：px  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| componentWidth | number | 是 | 组件的宽。  单位：px  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| componentHeight | number | 是 | 组件的高。  单位：px  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| loadingStatus | number | 是 | 图片加载成功的状态值。  **说明：**  返回的状态值为0时，表示图片数据加载成功。返回的状态值为1时，表示图片解码成功。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。 |
| contentWidth10+ | number | 是 | 图片实际绘制的宽度。  单位：px  **说明：**  仅在loadingStatus返回1时有效。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| contentHeight10+ | number | 是 | 图片实际绘制的高度。  单位：px  **说明：**  仅在loadingStatus返回1时有效。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| contentOffsetX10+ | number | 是 | 实际绘制内容相对于组件自身的x轴偏移。  单位：px  **说明：**  仅在loadingStatus返回1时有效。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |
| contentOffsetY10+ | number | 是 | 实际绘制内容相对于组件自身的y轴偏移。  单位：px  **说明：**  仅在loadingStatus返回1时有效。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。 |

### onError9+

PhonePC/2in1TabletTVWearable

onError(callback: ImageErrorCallback)

图片加载异常时触发该回调。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageErrorCallback](ts-basic-components-image.md#imageerrorcallback9) | 是 | 图片加载异常时触发的回调。  **说明：**  建议开发者使用此回调，可快速确认图片加载失败时的具体原因，参见[ImageError](ts-basic-components-image.md#imageerror9)的错误信息详细介绍。 |

### onFinish

PhonePC/2in1TabletTVWearable

onFinish(event: () => void)

当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。

仅支持SVG格式的图片。当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | () => void | 是 | 当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。 |

## ImageErrorCallback9+

PhonePC/2in1TabletTVWearable

type ImageErrorCallback = (error: ImageError) => void

图片加载异常时触发此回调。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时该事件不触发。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| error | [ImageError](ts-basic-components-image.md#imageerror9) | 是 | 图片加载异常时触发回调的返回对象。 |

## ImageError9+

PhonePC/2in1TabletTVWearable

图片加载异常时触发回调的返回对象。

当组件的参数类型为[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)时该事件不触发。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| componentWidth | number | 否 | 否 | 组件的宽。  单位：px  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| componentHeight | number | 否 | 否 | 组件的高。  单位：px  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| message10+ | string | 否 | 否 | 报错信息。  **卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| error20+ | [BusinessError<void>](ts-basic-components-image.md#businesserror20) | 否 | 是 | 图片加载异常返回的报错信息，其中code为错误码，message为错误信息。报错信息请参考以下错误信息的详细介绍。  默认值：{ code : -1, message : "" }  **卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |
| downloadInfo23+ | [RequestDownloadInfo](ts-basic-components-image.md#requestdownloadinfo23) | 否 | 是 | 网络图片下载的详细信息，包含下载资源、网络、性能等信息。当图片来源为网络图片且下载失败时将携带此字段。  默认值：null  **卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## BusinessError20+

PhonePC/2in1TabletTVWearable

type BusinessError<T = void> = BusinessError<T>

图片加载异常返回的错误信息。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [BusinessError<T>](js-apis-base.md#businesserror) | 图片加载异常返回的错误信息。 |

以下是错误信息的详细介绍：ImageError的error属性为错误信息对象，其中code为错误码，message为错误信息。

| 错误码ID | 错误信息 | 错误信息发生阶段 | 图片加载类型 |
| --- | --- | --- | --- |
| 101000 | unknown source type. | 数据加载 | 未知类型 |
| 102010 | sync http task of uri cancelled. | 数据加载 | 网络文件 |
| 102011 | sync http task of uri failed. | 数据加载 | 网络文件 |
| 102012 | async http task of uri cancelled. | 数据加载 | 网络文件 |
| 102013 | async http task of uri failed. | 数据加载 | 网络文件 |
| 102030 | wrong code format. | 数据加载 | base64字符串文件 |
| 102031 | decode base64 image failed. | 数据加载 | base64字符串文件 |
| 102050 | path is too long. | 数据加载 | 沙箱文件 |
| 102051 | read data failed. | 数据加载 | 沙箱文件 |
| 102070 | get image data by name failed. | 数据加载 | 资源文件 |
| 102071 | get image data by id failed. | 数据加载 | 资源文件 |
| 102072 | uri is invalid. | 数据加载 | 资源文件 |
| 102090 | uri is invalid. | 数据加载 | 包内文件 |
| 102091 | get asset failed. | 数据加载 | 包内文件 |
| 102110 | open file failed. | 数据加载 | 媒体库文件 |
| 102111 | get file stat failed. | 数据加载 | 媒体库文件 |
| 102112 | read file failed. | 数据加载 | 媒体库文件 |
| 102130 | decoded data is empty. | 数据加载 | 媒体库缩略图文件 |
| 102131 | load shared memory image data timeout. | 数据加载 | 共享内存文件 |
| 103100 | make svg dom failed. | 数据加载 | 矢量图文件 |
| 103200 | image data size is invalid. | 数据加载 | 位图文件 |
| 111000 | image source create failed. | 数据解码 | 位图文件 |
| 111001 | pixelmap create failed. | 数据解码 | 位图文件 |

## RequestDownloadInfo23+

PhonePC/2in1TabletTVWearable

type RequestDownloadInfo = DownloadInfo

用于描述网络图片加载失败或异常时的下载信息。该对象包含本次下载任务的资源信息、网络信息以及性能统计信息，可用于定位加载异常的具体原因。

**卡片能力：** 从API version 23开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [DownloadInfo](js-apis-request-cachedownload.md#downloadinfo20) | 网络资源加载异常时返回的下载信息，包含资源信息、网络请求信息与性能统计信息。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（加载基本类型图片）

该示例通过传入[Resource](ts-types.md#resource)资源，加载png、gif、svg和jpg等基本类型的图片。

```
1. @Entry
2. @Component
3. struct ImageExample1 {
4. build() {
5. Column() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
7. Row() {
8. // 加载png格式图片
9. // $r('app.media.ic_camera_master_ai_leaf')需要替换为开发者所需的图像资源文件。
10. Image($r('app.media.ic_camera_master_ai_leaf'))
11. .width(110).height(110).margin(15)
12. .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
13. // 加载gif格式图片
14. // $r('app.media.loading')需要替换为开发者所需的图像资源文件。
15. Image($r('app.media.loading'))
16. .width(110).height(110).margin(15)
17. .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
18. }
19. Row() {
20. // 加载svg格式图片
21. // $r('app.media.ic_camera_master_ai_clouded')需要替换为开发者所需的图像资源文件。
22. Image($r('app.media.ic_camera_master_ai_clouded'))
23. .width(110).height(110).margin(15)
24. .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
25. // 加载jpg格式图片
26. // $r('app.media.ic_public_favor_filled')需要替换为开发者所需的图像资源文件。
27. Image($r('app.media.ic_public_favor_filled'))
28. .width(110).height(110).margin(15)
29. .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
30. }
31. }
32. }.height(320).width(360).padding({ right: 10, top: 10 })
33. }
34. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/K5Ky0NAYT9-pM1YaudsGAQ/zh-cn_image_0000002552959832.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=BE6C6E74E167E27E1F13F3B26E1B6DDAC8253728CA3B5813109A15FDDD6DC202)

### 示例2（下载与显示静态网络图片）

加载网络图片时，默认网络超时是5分钟，建议使用alt配置加载时的占位图。使用[HTTP](../harmonyos-guides/http-request.md)工具包发送网络请求，接着将返回的数据解码为Image组件中的PixelMap，加载gif到PixelMap时，gif显示为静态图。图片开发可参考[Image Kit简介](../harmonyos-guides/image-overview.md)。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

```
1. import { http } from '@kit.NetworkKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { image } from '@kit.ImageKit';

5. @Entry
6. @Component
7. struct ImageExample2 {
8. @State pixelMapImg: PixelMap | undefined = undefined;

10. aboutToAppear() {
11. this.requestImageUrl('https://www.example.com/xxx.png'); // 请填写一个具体的网络图片地址
12. }

14. requestImageUrl(url: string) {
15. http.createHttp().request(url, (error: BusinessError, data: http.HttpResponse) => {
16. if (error) {
17. console.error(`request image failed: url: ${url}, code: ${error.code}, message: ${error.message}`);
18. } else {
19. let imgData: ArrayBuffer = data.result as ArrayBuffer;
20. console.info(`request image success, size: ${imgData.byteLength}`);
21. let imgSource: image.ImageSource = image.createImageSource(imgData);
22. class sizeTmp {
23. height: number = 100;
24. width: number = 100;
25. }
26. let options: Record<string, number | boolean | sizeTmp> = {
27. 'alphaType': 0,
28. 'editable': false,
29. 'pixelFormat': 3,
30. 'scaleMode': 1,
31. 'size': { height: 100, width: 100 }
32. }
33. imgSource.createPixelMap(options).then((pixelMap: PixelMap) => {
34. console.error('image createPixelMap success');
35. this.pixelMapImg = pixelMap;
36. imgSource.release();
37. }).catch(() => {
38. imgSource.release();
39. })
40. }
41. })
42. }

44. build() {
45. Column() {
46. Image(this.pixelMapImg)
47. // $r('app.media.img')需要替换为开发者所需的图像资源文件。
48. .alt($r('app.media.img'))
49. .objectFit(ImageFit.None)
50. .width('100%')
51. .height('100%')
52. }
53. }
54. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/sXx6LYqhTrSxebYY4oWjHg/zh-cn_image_0000002583479833.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=CC567B61C61E0BE3CC41515E5F0C008384E6BFEBD545A4CFFFD69820BEA9AC7E)

### 示例3（下载与显示网络gif图片）

该示例使用[cacheDownload.download](js-apis-request-cachedownload.md#cachedownloaddownload)接口下载网络gif图片。

使用网络图片时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

```
1. import { cacheDownload } from '@kit.BasicServicesKit';

3. @Entry
4. @Component
5. struct Index {
6. @State src: string = 'https://www.example.com/xxx.gif'; // 请填写一个具体的网络图片地址。

8. async aboutToAppear(): Promise<void> {
9. // 提供缓存下载任务的配置选项。
10. let options: cacheDownload.CacheDownloadOptions = {};
11. try {
12. // 进行缓存下载，资源若下载成功会被缓存到应用内存或应用沙箱目录的特定文件中。
13. cacheDownload.download(this.src, options);
14. console.info(`success to download the resource. `);
15. } catch (err) {
16. console.error(`Failed to download the resource: code: ${err.code}, message: ${err.message}`);
17. }
18. }

20. build() {
21. Column() {
22. // 若src指定的是网络图片且已成功下载并缓存，则本次显示无需重复下载。
23. Image(this.src)
24. .width(100)
25. .height(100)
26. .objectFit(ImageFit.Cover)
27. .borderWidth(1)
28. }
29. .height('100%')
30. .width('100%')
31. }
32. }
```

### 示例4（为图片添加事件）

该示例为图片添加[onClick](ts-universal-events-click.md#onclick)和[onFinish](ts-basic-components-image.md#onfinish)事件。

```
1. @Entry
2. @Component
3. struct ImageExample3 {
4. // $r('app.media.earth')需要替换为开发者所需的图像资源文件。
5. private imageOne: Resource = $r('app.media.earth');
6. // $r('app.media.star')需要替换为开发者所需的图像资源文件。
7. private imageTwo: Resource = $r('app.media.star');
8. // $r('app.media.moveStar')需要替换为开发者所需的图像资源文件。
9. private imageThree: Resource = $r('app.media.moveStar');
10. @State src: Resource = this.imageOne;
11. @State src2: Resource = this.imageThree;
12. build(){
13. Column(){
14. // 为图片添加点击事件，点击完成后加载特定图片
15. Image(this.src)
16. .width(100)
17. .height(100)
18. .onClick(() => {
19. this.src = this.imageTwo;
20. })

22. // 当加载图片为SVG格式时
23. Image(this.src2)
24. .width(100)
25. .height(100)
26. .onFinish(() => {
27. // SVG动效播放完成时加载另一张图片
28. this.src2 = this.imageOne;
29. })
30. }.width('100%').height('100%')
31. }
32. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/PRo0F21ORfujapm9pkxP4g/zh-cn_image_0000002552800184.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=3E6F957020498BA67D2713CFA1C0C072F2CA1D95BF07475DD162F403E50F1BF7)

### 示例5（开启图像AI分析）

该示例使用[enableAnalyzer](ts-basic-components-image.md#enableanalyzer11)接口开启图像AI分析。

```
1. import { image } from '@kit.ImageKit'

3. @Entry
4. @Component
5. struct ImageExample4 {
6. @State imagePixelMap: image.PixelMap | undefined = undefined
7. private aiController: ImageAnalyzerController = new ImageAnalyzerController()
8. private options: ImageAIOptions = {
9. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
10. aiController: this.aiController
11. }

13. async aboutToAppear() {
14. this.imagePixelMap = await this.getPixmapFromMedia($r('app.media.img'))
15. }

17. build() {
18. Column() {
19. Image(this.imagePixelMap, this.options)
20. .enableAnalyzer(true)
21. .objectFit(ImageFit.Contain)
22. .width(200)
23. .height(300)
24. .margin({left: 10})
25. Button('getTypes')
26. .onClick(() => {
27. this.aiController.getImageAnalyzerSupportTypes()
28. })
29. }
30. }
31. private async getPixmapFromMedia(resource: Resource) {
32. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent({
33. bundleName: resource.bundleName,
34. moduleName: resource.moduleName,
35. id: resource.id
36. })
37. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength))
38. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
39. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
40. })
41. await imageSource.release()
42. return createPixelMap
43. }
44. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/deAfA-zLTiW4eYWoKTShzw/zh-cn_image_0000002583439879.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=6C802D8E1607E1A1DD49124BF8198B1BA764E0E48C8EF16A26E69D84DA74F661)

### 示例6（通过slice拉伸图片）

该示例通过[resizable](ts-basic-components-image.md#resizable11)属性的slice选项，调整不同方向对图片进行拉伸。

```
1. @Entry
2. @Component
3. struct Index {
4. @State top: number = 10;
5. @State bottom: number = 10;
6. @State left: number = 10;
7. @State right: number = 10;

9. build() {
10. Column({ space: 5 }) {
11. // 原图效果
12. // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
13. Image($r('app.media.landscape'))
14. .width(200).height(200)
15. .border({ width: 2, color: Color.Pink })
16. .objectFit(ImageFit.Contain)

18. // 图像拉伸效果，设置resizable属性，对图片不同方向进行拉伸
19. // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
20. Image($r('app.media.landscape'))
21. .resizable({
22. slice: {
23. // 传入数字时默认为vp单位，但在不同设备上vp单位会被解析成不同大小的px单位，可以根据需要选择传入的单位
24. left: `${this.left}px`,
25. right: `${this.right}px`,
26. top: `${this.top}px`,
27. bottom: `${this.bottom}px`
28. }
29. })
30. .width(200)
31. .height(200)
32. .border({ width: 2, color: Color.Pink })
33. .objectFit(ImageFit.Contain)

35. Row() {
36. Button('add top to ' + this.top).fontSize(10)
37. .onClick(() => {
38. this.top += 10;
39. })
40. Button('add bottom to ' + this.bottom).fontSize(10)
41. .onClick(() => {
42. this.bottom += 10;
43. })
44. }

46. Row() {
47. Button('add left to ' + this.left).fontSize(10)
48. .onClick(() => {
49. this.left += 10;
50. })
51. Button('add right to ' + this.right).fontSize(10)
52. .onClick(() => {
53. this.right += 10;
54. })
55. }

57. }
58. .justifyContent(FlexAlign.Start).width('100%').height('100%')
59. }
60. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/wILaTWLRQkSjVNvbsr5jCQ/zh-cn_image_0000002552959834.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=EC283997CFD96B8DFC4D31087399EEED8E981BD0544225DE2311738056DB154A)

### 示例7（通过lattice拉伸图片）

该示例使用[resizable](ts-basic-components-image.md#resizable11)属性的lattice选项，使用矩形网格对象对图片进行拉伸。

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct drawingLatticeTest {
6. private xDivs: Array<number> = [1, 2, 200];
7. private yDivs: Array<number> = [1, 2, 200];
8. private fXCount: number = 3;
9. private fYCount: number = 3;
10. private drawingLatticeFirst: DrawingLattice =
11. drawing.Lattice.createImageLattice(this.xDivs, this.yDivs, this.fXCount, this.fYCount);

13. build() {
14. Scroll() {
15. Column({ space: 10 }) {
16. Text('Original Image').fontSize(20).fontWeight(700)
17. Column({ space: 10 }) {
18. // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
19. Image($r('app.media.mountain'))
20. .width(260).height(260)
21. }.width('100%')

23. Text('Resize by lattice').fontSize(20).fontWeight(700)
24. Column({ space: 10 }) {
25. // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
26. Image($r('app.media.mountain'))
27. .objectRepeat(ImageRepeat.X)
28. .width(260)
29. .height(260)
30. .resizable({
31. lattice: this.drawingLatticeFirst
32. })
33. }.width('100%')
34. }.width('100%')
35. }
36. }
37. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/zEpbgW6sTW2-1MAQGXtgEw/zh-cn_image_0000002583479835.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=B5317D72BBA96C244F54EDFEBC8C0686EBCE8BC4685E0C36B2C3EB9A23201CE7)

### 示例8（播放PixelMap数组动画）

该示例通过[AnimatedDrawableDescriptor](js-apis-arkui-drawabledescriptor.md#animateddrawabledescriptor12)对象播放PixelMap数组动画。

```
1. import { AnimationOptions, AnimatedDrawableDescriptor } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. @Entry
5. @Component
6. struct ImageExample {
7. pixelMaps: PixelMap[] = [];
8. @State options: AnimationOptions = { iterations: 1 };
9. @State animated: AnimatedDrawableDescriptor | undefined = undefined;

11. async aboutToAppear() {
12. this.pixelMaps = await this.getPixelMaps();
13. this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
14. }

16. build() {
17. Column() {
18. Row() {
19. Image(this.animated)
20. .width('500px').height('500px')
21. .onFinish(() => {
22. console.info('finish');
23. })
24. }.height('50%')

26. Row() {
27. Button('once').width(100).padding(5).onClick(() => {
28. this.options = { iterations: 1 };
29. this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
30. }).margin(5)
31. Button('infinite').width(100).padding(5).onClick(() => {
32. this.options = { iterations: -1 };
33. this.animated = new AnimatedDrawableDescriptor(this.pixelMaps, this.options);
34. }).margin(5)
35. }
36. }.width('50%')
37. }

39. private async getPixmapListFromMedia(resource: Resource) {
40. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
41. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
42. let createPixelMap: image.PixelMap[] = await imageSource.createPixelMapList({
43. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
44. });
45. await imageSource.release();
46. return createPixelMap;
47. }

49. private async getPixmapFromMedia(resource: Resource) {
50. let unit8Array = await this.getUIContext().getHostContext()?.resourceManager?.getMediaContent(resource.id);
51. let imageSource = image.createImageSource(unit8Array?.buffer.slice(0, unit8Array.buffer.byteLength));
52. let createPixelMap: image.PixelMap = await imageSource.createPixelMap({
53. desiredPixelFormat: image.PixelMapFormat.RGBA_8888
54. });
55. await imageSource.release();
56. return createPixelMap;
57. }

59. private async getPixelMaps() {
60. // $r('app.media.mountain')需要替换为开发者所需的图像资源文件。
61. let myPixelMaps: PixelMap[] = await this.getPixmapListFromMedia($r('app.media.mountain')); // 添加图片
62. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
63. myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.sky')));
64. // $r('app.media.clouds')需要替换为开发者所需的图像资源文件。
65. myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.clouds')));
66. // $r('app.media.landscape')需要替换为开发者所需的图像资源文件。
67. myPixelMaps.push(await this.getPixmapFromMedia($r('app.media.landscape')));
68. return myPixelMaps;
69. }
70. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/nnPyx4axQUCtnPFPCqA_kw/zh-cn_image_0000002552800186.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=2C2C6606204B6FAF6790662C8CB0666A8E32462503D60F0498F00A22D26DAA67)

### 示例9（为图像设置颜色滤镜效果）

该示例通过[colorFilter](ts-basic-components-image.md#colorfilter9)属性实现了给图像设置颜色滤镜效果。

```
1. import { drawing, common2D } from '@kit.ArkGraphics2D';

3. @Entry
4. @Component
5. struct ImageExample3 {
6. // 当加载图片为svg格式时
7. // $r('app.media.svg1')需要替换为开发者所需的图像资源文件。
8. private imageOne: Resource = $r('app.media.svg1');
9. // $r('app.media.1')需要替换为开发者所需的图像资源文件。
10. private imageTwo: Resource = $r('app.media.1');
11. @State src: Resource = this.imageOne;
12. @State src2: Resource = this.imageTwo;
13. private colorFilterMatrix: number[] = [1, 0, 0, 0, 0.5,
14. 0, 1, 0, 0, 0,
15. 0, 0, 1, 0, 0,
16. 0, 0, 0, 1, 0];
17. private color: common2D.Color = {
18. alpha: 255,
19. red: 255,
20. green: 0,
21. blue: 0
22. };
23. @State drawingColorFilterFirst: ColorFilter | undefined = undefined;
24. @State drawingColorFilterSecond: ColorFilter | undefined = undefined;
25. @State drawingColorFilterThird: ColorFilter | undefined = undefined;

27. build() {
28. Column() {
29. Image(this.src)
30. .width(100)
31. .height(100)
32. .colorFilter(this.drawingColorFilterFirst)
33. .onClick(()=>{
34. this.drawingColorFilterFirst =
35. drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);
36. })

38. Image(this.src2)
39. .width(100)
40. .height(100)
41. .colorFilter(this.drawingColorFilterSecond)
42. .onClick(()=>{
43. this.drawingColorFilterSecond = new ColorFilter(this.colorFilterMatrix);
44. })

46. // 当加载图片为svg格式时
47. // $r('app.media.svg2')需要替换为开发者所需的图像资源文件。
48. Image($r('app.media.svg2'))
49. .width(110)
50. .height(110)
51. .margin(15)
52. .colorFilter(this.drawingColorFilterThird)
53. .onClick(()=>{
54. this.drawingColorFilterThird =
55. drawing.ColorFilter.createBlendModeColorFilter(this.color, drawing.BlendMode.SRC_IN);
56. })
57. }
58. }
59. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/E_osGIrkSJ-jeMkbIcbrag/zh-cn_image_0000002583439881.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=1BDE0F2508AA5253F7ECF13BA6A5495093F146C058C0B2F122F3274927562566)

### 示例10（为图像设置填充效果）

该示例通过[objectFit](ts-basic-components-image.md#objectfit)属性为图像设置填充效果。

```
1. @Entry
2. @Component
3. struct ImageExample{
4. build() {
5. Column() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
7. Row() {
8. // 加载png格式图片
9. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
10. Image($r('app.media.sky'))
11. .width(110).height(110).margin(15)
12. .overlay('png', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
13. .border({ width: 2, color: Color.Pink })
14. .objectFit(ImageFit.TOP_START)
15. // 加载gif格式图片
16. // $r('app.media.loading')需要替换为开发者所需的图像资源文件。
17. Image($r('app.media.loading'))
18. .width(110).height(110).margin(15)
19. .overlay('gif', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
20. .border({ width: 2, color: Color.Pink })
21. .objectFit(ImageFit.BOTTOM_START)
22. }
23. Row() {
24. // 加载svg格式图片
25. // $r('app.media.svg')需要替换为开发者所需的图像资源文件。
26. Image($r('app.media.svg'))
27. .width(110).height(110).margin(15)
28. .overlay('svg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
29. .border({ width: 2, color: Color.Pink })
30. .objectFit(ImageFit.TOP_END)
31. // 加载jpg格式图片
32. // $r('app.media.jpg')需要替换为开发者所需的图像资源文件。
33. Image($r('app.media.jpg'))
34. .width(110).height(110).margin(15)
35. .overlay('jpg', { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
36. .border({ width: 2, color: Color.Pink })
37. .objectFit(ImageFit.CENTER)
38. }
39. }
40. }.height(320).width(360).padding({ right: 10, top: 10 })
41. }
42. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/gE0CJKZRRpGIkGS9C0HdOw/zh-cn_image_0000002552959836.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=315D86239392DF14133F2490DBE5D4DB3BF0931BA7AD6B98054CA362F5E33EB5)

### 示例11（切换显示不同类型图片）

该示例展示了[ResourceStr](ts-types.md#resourcestr)类型与[ImageContent](ts-basic-components-image.md#imagecontent12)类型作为数据源的显示图片效果。

```
1. @Entry
2. @Component
3. struct ImageContentExample {
4. @State imageSrcIndex: number = 0;
5. // $r('app.media.app_icon')需要替换为开发者所需的图像资源文件。
6. @State imageSrcList: (ResourceStr | ImageContent)[] = [$r('app.media.app_icon'), ImageContent.EMPTY];

8. build() {
9. Column({ space: 10 }) {
10. Image(this.imageSrcList[this.imageSrcIndex])
11. .width(100)
12. .height(100)
13. Button('点击切换Image的src', { type: ButtonType.Capsule, stateEffect: false })
14. .height(50)
15. .onClick(() => {
16. this.imageSrcIndex = (this.imageSrcIndex + 1) % this.imageSrcList.length;
17. })
18. }.width('100%')
19. .padding(20)
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/o1A0e7VmRaChg1xJTITHrA/zh-cn_image_0000002583479837.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=076448A01D84B9F8F362806FFA34AA0ACDDBBA60BFFA08B3DB9546A55CB055F3)

### 示例12（配置隐私隐藏）

该示例通过[privacySensitive](ts-basic-components-image.md#privacysensitive12)属性展示了如何配置隐私隐藏，效果展示需要卡片框架支持。

```
1. @Entry
2. @Component
3. struct ImageExample {
4. build() {
5. Column({ space: 10 }) {
6. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件。
7. Image($r('app.media.startIcon'))
8. .width(50)
9. .height(50)
10. .margin({top :30})
11. .privacySensitive(true)
12. }
13. .alignItems(HorizontalAlign.Center)
14. .width('100%')
15. }
16. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/wJLcUk3oSVyaMniLgVdMtw/zh-cn_image_0000002552800188.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=DA99B033AFEB47BA40FC8D7E1DA34008B6BD1D6B2B81BD0FD253229187734DAB)

### 示例13（为图片设置扫光效果）

该示例通过[linearGradient](ts-basic-components-datapanel.md#lineargradient10)接口和[animateTo()](arkts-apis-uicontext-uicontext.md#animateto)接口实现了给图片设置扫光效果。

```
1. import { curves } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ImageExample11 {
6. private curve = curves.cubicBezierCurve(0.33, 0, 0.67, 1);
7. @State moveImg: string[] = ['imageScanEffect'];
8. @State moveImgVisible: Visibility = Visibility.Visible;
9. @State durationTime: number = 1500;
10. @State iterationsTimes: number = -1;
11. @State private opacityValue: number = 0.5;
12. @State imageWidth: number = 450;
13. @State visible: Visibility = Visibility.Hidden;
14. @State stackBackgroundColor: string = '#E1E4E9';
15. @State linePositionX: number = 0 - this.imageWidth;
16. @State linePositionY: number = 0;
17. @State imgResource: Resource | undefined = undefined;

19. startupAnimate() {
20. this.moveImg.pop();
21. this.moveImg.push('imageScanEffect');
22. setTimeout(() => {
23. // $r('app.media.img')需要替换为开发者所需的图像资源文件。
24. this.imgResource = $r('app.media.img');
25. }, 3000);
26. this.getUIContext()?.animateTo({
27. duration: this.durationTime,
28. curve: this.curve,
29. tempo: 1,
30. iterations: this.iterationsTimes,
31. delay: 0
32. }, () => {
33. this.linePositionX = this.imageWidth;
34. })
35. }

37. build() {
38. Column() {
39. Row() {
40. Stack() {
41. Image(this.imgResource)
42. .width(this.imageWidth)
43. .height(200)
44. .objectFit(ImageFit.Contain)
45. .visibility(this.visible)
46. .onComplete(() => {
47. this.visible = Visibility.Visible;
48. this.moveImg.pop();
49. })
50. .onError(() =>{
51. setTimeout(() => {
52. this.visible = Visibility.Visible;
53. this.moveImg.pop();
54. }, 2600)
55. })
56. ForEach(this.moveImg, (item: string) => {
57. Row()
58. .width(this.imageWidth)
59. .height(200)
60. .visibility(this.moveImgVisible)
61. .position({ x: this.linePositionX, y: this.linePositionY })
62. .linearGradient({
63. direction: GradientDirection.Right,
64. repeating: false,
65. colors: [[0xE1E4E9, 0], [0xFFFFFF, 0.75], [0xE1E4E9, 1]]
66. })
67. .opacity(this.opacityValue)
68. })
69. }
70. .backgroundColor(this.visible ? this.stackBackgroundColor : undefined)
71. .margin({top: 20, left: 20, right: 20})
72. .borderRadius(20)
73. .clip(true)
74. .onAppear(() => {
75. this.startupAnimate();
76. })
77. }
78. }
79. }
80. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/HMff_e69T5Gr09iSb_JOwQ/zh-cn_image_0000002583439883.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=1182BE5399E9E5CCFE5BFC1AAB6E7BAA479D7987EA8E6798ED00612A3A187D6F)

### 示例14（为图片添加变换效果）

该示例通过[imageMatrix](ts-basic-components-image.md#imagematrix15)和[objectFit](ts-basic-components-image.md#objectfit)属性，为图片添加旋转和平移的效果。

从API version 15开始，新增imageMatrix属性。

```
1. import { matrix4 } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Test {
6. private matrix1 = matrix4.identity()
7. .translate({ x: -400, y: -750 })
8. .scale({ x: 0.5, y: 0.5 })
9. .rotate({
10. x: 2,
11. y: 0.5,
12. z: 3,
13. centerX: 10,
14. centerY: 10,
15. angle: -10
16. })

18. build() {
19. Row() {
20. Column({ space: 50 }) {
21. Column({ space: 5 }) {
22. // $r('app.media.example')需要替换为开发者所需的图像资源文件。
23. Image($r('app.media.example'))
24. .border({ width:2, color: Color.Black })
25. .objectFit(ImageFit.Contain)
26. .width(150)
27. .height(150)
28. Text('图片无变换')
29. .fontSize('25px')
30. }
31. Column({ space: 5 }) {
32. // $r('app.media.example')需要替换为开发者所需的图像资源文件。
33. Image($r('app.media.example'))
34. .border({ width:2, color: Color.Black })
35. .objectFit(ImageFit.None)
36. .translate({ x: 10, y: 10 })
37. .scale({ x: 0.5, y: 0.5 })
38. .width(100)
39. .height(100)
40. Text('Image直接变换，默认显示图源左上角。')
41. .fontSize('25px')
42. }
43. Column({ space: 5 }) {
44. // $r('app.media.example')需要替换为开发者所需的图像资源文件。
45. Image($r('app.media.example'))
46. .objectFit(ImageFit.MATRIX)
47. .imageMatrix(this.matrix1)
48. .border({ width:2, color: Color.Black })
49. .width(150)
50. .height(150)
51. Text('通过imageMatrix变换，调整图源位置，实现最佳呈现。')
52. .fontSize('25px')
53. }
54. }
55. .width('100%')
56. }
57. }
58. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/XPrrfjU7SlG_gu2Rec3QIg/zh-cn_image_0000002552959838.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=74E22F3799DF5E6D5E7B7D7BB12C431BE79CC34140443E760BB3D073C473A65D)

### 示例15（通过sourceSize设置图片解码尺寸）

该示例通过[sourceSize](ts-basic-components-image.md#sourcesize)接口自定义图片的解码尺寸。

```
1. @Entry
2. @Component
3. struct Index {
4. @State borderRadiusValue: number = 10;
5. build() {
6. Column() {
7. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.sky'))
9. .sourceSize({width:1393, height:1080})
10. .height(300)
11. .width(300)
12. .objectFit(ImageFit.Contain)
13. .borderWidth(1)
14. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
15. Image($r('app.media.sky'))
16. .sourceSize({width:13, height:10})
17. .height(300)
18. .width(300)
19. .objectFit(ImageFit.Contain)
20. .borderWidth(1)
21. }
22. .height('100%')
23. .width('100%')
24. }
25. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/5fazQgzQQsSzIp-x-pNhew/zh-cn_image_0000002583479839.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=9E277E142BF299407E2559A29A858AD27E1A313A7B4BC92AFFD25EC9F6319C83)

### 示例16（通过renderMode设置图片的渲染模式）

该示例通过[renderMode](ts-basic-components-image.md#rendermode)接口设置图片渲染模式为黑白模式。

```
1. @Entry
2. @Component
3. struct Index {
4. @State borderRadiusValue: number = 10;
5. build() {
6. Column() {
7. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.sky'))
9. .renderMode(ImageRenderMode.Template)
10. .height(300)
11. .width(300)
12. .objectFit(ImageFit.Contain)
13. .borderWidth(1)
14. }
15. .height('100%')
16. .width('100%')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/fl0B4G79S7a5TJMX3xFAuQ/zh-cn_image_0000002552800190.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=A43A7D1C04C777185980122C10153C3AACBB164CFA63F9E87482858C68155C06)

### 示例17（通过objectRepeat设置图片的重复样式）

该示例通过[objectRepeat](ts-basic-components-image.md#objectrepeat)接口在竖直轴上重复绘制图片。

```
1. @Entry
2. @Component
3. struct Index {
4. @State borderRadiusValue: number = 10;
5. build() {
6. Column() {
7. // $r('app.media.sky')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.sky'))
9. .objectRepeat(ImageRepeat.Y)
10. .height('90%')
11. .width('90%')
12. .objectFit(ImageFit.Contain)
13. .borderWidth(1)
14. }
15. .height('100%')
16. .width('100%')
17. }
18. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/bu3llSnNTdOoNUAIlBSKXQ/zh-cn_image_0000002583439885.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=63B86F60EC59A936B00A11A758774E32D0FB4474CDAC0776E14DAC2E71B8CFF7)

### 示例18（设置SVG图片的填充颜色）

该示例通过[fillColor](ts-basic-components-image.md#fillcolor15)属性为SVG图片设置不同颜色的填充效果。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Text('不设置fillColor')
7. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.svgExample'))
9. .height(100)
10. .width(100)
11. .objectFit(ImageFit.Contain)
12. .borderWidth(1)
13. Text('fillColor传入ColorContent.ORIGIN')
14. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
15. Image($r('app.media.svgExample'))
16. .height(100)
17. .width(100)
18. .objectFit(ImageFit.Contain)
19. .borderWidth(1)
20. .fillColor(ColorContent.ORIGIN)
21. Text('fillColor传入Color.Blue')
22. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
23. Image($r('app.media.svgExample'))
24. .height(100)
25. .width(100)
26. .objectFit(ImageFit.Contain)
27. .borderWidth(1)
28. .fillColor(Color.Blue)
29. Text('fillColor传入undefined')
30. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
31. Image($r('app.media.svgExample'))
32. .height(100)
33. .width(100)
34. .objectFit(ImageFit.Contain)
35. .borderWidth(1)
36. .fillColor(undefined)
37. }
38. .height('100%')
39. .width('100%')
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/6tpS9byKRMyX6YK_Gy_7dQ/zh-cn_image_0000002552959840.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=497D2D893AD9475B164453E8A40F581BFB885A1C9464EE219A2EC2CBF961C90E)

### 示例19（设置HDR图源动态提亮）

该示例通过[hdrBrightness](ts-basic-components-image.md#hdrbrightness19)属性调整HDR图源的亮度，将hdrBrightness从0调整到1。

从API version 19开始，新增hdrBrightness属性。

```
1. import { image } from '@kit.ImageKit';

3. const TAG = 'AceImage';

5. @Entry
6. @Component
7. struct Index {
8. // 'img_1'需要替换为开发者所需的图像资源文件。
9. @State imgUrl: string = 'img_1';
10. @State bright: number = 0; // 默认亮度为0
11. aboutToAppear(): void {
12. // 获取资源管理器中的媒体资源
13. let img = this.getUIContext().getHostContext()?.resourceManager.getMediaByNameSync(this.imgUrl);
14. // 创建图片源并获取图片信息
15. if (img && img.buffer) {
16. let imageSource = image.createImageSource(img?.buffer.slice(0));
17. let imageInfo = imageSource.getImageInfoSync();
18. // 检查图片信息是否获取成功
19. if (imageInfo == undefined) {
20. console.error(TAG, 'Failed to obtain the image information.');
21. } else {
22. // 成功获取到图片信息，打印HDR状态
23. console.info(TAG, 'imageInfo.isHdr:' + imageInfo.isHdr);
24. }
25. } else {
26. console.error(TAG, 'Failed to obtain the image buffer.');
27. }
28. }

30. build() {
31. Column() {
32. // $r('app.media.img_1')需要替换为开发者所需的图像资源文件。
33. Image($r('app.media.img_1')).width('50%')
34. .height('auto')
35. .margin({ top: 160 })
36. .hdrBrightness(this.bright) // 设置图片的HDR亮度，值由bright状态控制
37. Button('图片动态提亮 0->1')
38. .onClick(() => {
39. // 动画过渡，切换亮度值
40. this.getUIContext()?.animateTo({}, () => {
41. this.bright = 1.0 - this.bright;
42. });
43. })
44. }
45. .height('100%')
46. .width('100%')
47. }
48. }
```

### 示例20（设置图片是否跟随系统语言方向）

该示例通过[matchTextDirection](ts-basic-components-image.md#matchtextdirection)接口，设置手机语言为维语时图片是否显示镜像翻转显示效果。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
7. Row() {
8. // 图片不跟随系统语言方向
9. // $r('app.media.ocean')需要替换为开发者所需的图像资源文件。
10. Image($r('app.media.ocean'))
11. .width(110).height(110).margin(15)
12. .matchTextDirection(false)
13. }
14. Row() {
15. // 图片跟随系统语言方向
16. // $r('app.media.ocean')需要替换为开发者所需的图像资源文件。
17. Image($r('app.media.ocean'))
18. .width(110).height(110).margin(15)
19. .matchTextDirection(true)
20. }
21. }
22. }.height(320).width(360).padding({ right: 10, top: 10 })
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/mJH8X53yQ_mjUUfl9IzMNw/zh-cn_image_0000002583479841.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=F3565A268D3C247358227B4162F333DD09D40A8F3F04BD1EB8D699F73A56D4AE)

### 示例21（设置图像内容的显示方向）

该示例通过[orientation](ts-basic-components-image.md#orientation14)属性，设置图像内容的显示方向。

```
1. @Entry
2. @Component
3. struct OrientationExample {
4. build() {
5. Column() {
6. Row({ space: 25 }) {
7. Column() {
8. Text('AUTO')
9. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
10. Image($r('app.media.hello'))
11. .width(125).height(125)
12. .orientation(ImageRotateOrientation.AUTO)
13. }

15. Column() {
16. Text('UP')
17. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
18. Image($r('app.media.hello'))
19. .width(125).height(125)
20. .orientation(ImageRotateOrientation.UP)
21. }

23. Column() {
24. Text('RIGHT')
25. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
26. Image($r('app.media.hello'))
27. .width(125).height(125)
28. .orientation(ImageRotateOrientation.RIGHT)
29. }
30. }

32. Row({ space: 25 }) {
33. Column() {
34. Text('DOWN')
35. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
36. Image($r('app.media.hello'))
37. .width(125).height(125)
38. .orientation(ImageRotateOrientation.DOWN)
39. }

41. Column() {
42. Text('LEFT')
43. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
44. Image($r('app.media.hello'))
45. .width(125).height(125)
46. .orientation(ImageRotateOrientation.LEFT)
47. }

49. Column() {
50. Text('UP_MIRRORED')
51. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
52. Image($r('app.media.hello'))
53. .width(125).height(125)
54. .orientation(ImageRotateOrientation.UP_MIRRORED)
55. }
56. }

58. Row({ space: 15 }) {
59. Column() {
60. Text('RIGHT_MIRRORED')
61. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
62. Image($r('app.media.hello'))
63. .width(125).height(125)
64. .orientation(ImageRotateOrientation.RIGHT_MIRRORED)
65. }

67. Column() {
68. Text('DOWN_MIRRORED')
69. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
70. Image($r('app.media.hello'))
71. .width(125).height(125)
72. .orientation(ImageRotateOrientation.DOWN_MIRRORED)
73. }

75. Column() {
76. Text('LEFT_MIRRORED')
77. // $r('app.media.hello')需要替换为开发者所需的图像资源文件。
78. Image($r('app.media.hello'))
79. .width(125).height(125)
80. .orientation(ImageRotateOrientation.LEFT_MIRRORED)
81. }
82. }
83. }
84. }
85. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/KaXM7i91QJy_gKDfxuixjQ/zh-cn_image_0000002552800192.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=DE17EB51A17BBD930C319435283736AD5FFF8D9930243156F2AEFC6BD666D0AC)

### 示例22（获取图片的exif信息并设置图像内容的显示方向）

该示例通过[getImageProperty](arkts-apis-image-imagesource.md#getimageproperty11)接口，获取图片的exif信息，再根据获取到的exif信息，通过[orientation](ts-basic-components-image.md#orientation14)属性设置图像内容显示为正确方向。

```
1. import { image } from '@kit.ImageKit';
2. import { resourceManager } from '@kit.LocalizationKit';

4. @Entry
5. @Component
6. struct Example {
7. @State rotateOrientation: ImageRotateOrientation = ImageRotateOrientation.UP;
8. @State pixelMap: image.PixelMap | undefined = undefined;
9. @State text1: string = 'The exif orientation is ';
10. @State text2: string = 'Set orientation to ';

12. // 根据获取到的EXIF方向信息，转换ImageRotateOrientation，使图片显示为正确的方向。
13. getOrientation(orientation: string): ImageRotateOrientation {
14. if (orientation == 'Top-right') {
15. this.text2 = this.text2 + 'UP_MIRRORED';
16. return ImageRotateOrientation.UP_MIRRORED;
17. } else if (orientation == 'Bottom-right') {
18. this.text2 = this.text2 + 'DOWN';
19. return ImageRotateOrientation.DOWN;
20. } else if (orientation == 'Bottom-left') {
21. this.text2 = this.text2 + 'DOWN_MIRRORED';
22. return ImageRotateOrientation.DOWN_MIRRORED;
23. } else if (orientation == 'Left-top') {
24. this.text2 = this.text2 + 'LEFT_MIRRORED';
25. return ImageRotateOrientation.LEFT_MIRRORED;
26. } else if (orientation == 'Right-top') {
27. this.text2 = this.text2 + 'RIGHT';
28. return ImageRotateOrientation.RIGHT;
29. } else if (orientation == 'Right-bottom') {
30. this.text2 = this.text2 + 'RIGHT_MIRRORED';
31. return ImageRotateOrientation.RIGHT_MIRRORED;
32. } else if (orientation == 'Left-bottom') {
33. this.text2 = this.text2 + 'LEFT';
34. return ImageRotateOrientation.LEFT;
35. } else if (orientation == 'Top-left') {
36. this.text2 = this.text2 + 'UP';
37. return ImageRotateOrientation.UP;
38. } else {
39. this.text2 = this.text2 + 'UP';
40. return ImageRotateOrientation.UP;
41. }
42. }

44. async getFileBuffer(context: Context): Promise<ArrayBuffer | undefined> {
45. try {
46. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
47. // 传入带有EXIF信息的资源文件，获取资源文件内容，返回Uint8Array。
48. // 'hello.jpg'需要替换为开发者所需的图像资源文件。
49. const fileData: Uint8Array = await resourceMgr.getRawFileContent('hello.jpg');
50. console.info('Successfully get RawFileContent');
51. // 转为ArrayBuffer并返回。
52. const buffer: ArrayBuffer = fileData.buffer.slice(0);
53. return buffer;
54. } catch (error) {
55. console.error('Failed to get RawFileContent');
56. return undefined;
57. }
58. }

60. aboutToAppear() {
61. let context = this.getUIContext().getHostContext();
62. if (!context) {
63. return;
64. }
65. this.getFileBuffer(context).then((buf: ArrayBuffer | undefined) => {
66. let imageSource = image.createImageSource(buf);
67. if (!imageSource) {
68. return;
69. }
70. // 从图像源中读取图片的EXIF方向信息。
71. imageSource.getImageProperty(image.PropertyKey.ORIENTATION).then((orientation) => {
72. this.rotateOrientation = this.getOrientation(orientation);
73. this.text1 = this.text1 + orientation;
74. let options: image.DecodingOptions = {
75. 'editable': true,
76. 'desiredPixelFormat': image.PixelMapFormat.RGBA_8888,
77. }
78. imageSource.createPixelMap(options).then((pixelMap: image.PixelMap) => {
79. this.pixelMap = pixelMap;
80. imageSource.release();
81. });
82. }).catch(() => {
83. imageSource.release();
84. });
85. })
86. }

88. build() {
89. Column({ space: 40 }) {
90. Column({ space: 10 }) {
91. Text('before').fontSize(20).fontWeight(700)
92. // 'hello.jpg'需要替换为开发者所需的图像资源文件。
93. Image($rawfile('hello.jpg'))
94. .width(100)
95. .height(100)
96. Text(this.text1)
97. }

99. Column({ space: 10 }) {
100. Text('after').fontSize(20).fontWeight(700)
101. Image(this.pixelMap)
102. .width(100)
103. .height(100)
104. .orientation(this.rotateOrientation)
105. Text(this.text2)
106. }
107. }
108. .height('80%')
109. .width('100%')
110. }
111. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/oyJsJ9b5QrqvmGQa4hGuIQ/zh-cn_image_0000002583439887.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=0A83BFB9DE7284DAC59B6CAB69D1CC50101CB08B6E71577E51CA2001EF3AAC38)

### 示例23（动态切换SVG图片的填充颜色）

通过按钮切换不同色域下的颜色值，动态改变SVG图片的填充颜色效果，以展示[ColorMetrics](js-apis-arkui-graphics.md#colormetrics12)类型的使用方式和显示差异。

```
1. import { ColorMetrics } from '@kit.ArkUI';
2. @Entry
3. @Component
4. struct fillColorMetricsDemo {
5. @State p3Red: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.631, 0.0392, 0.1294);
6. @State sRGBRed: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.631, 0.0392, 0.1294);
7. @State p3Green: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0.09, 0.662 ,0.552);
8. @State sRGBGreen: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0.09, 0.662 ,0.552);
9. @State p3Blue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY_P3, 0, 0.290 ,0.686);
10. @State sRGBBlue: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.SRGB, 0, 0.290 ,0.686);
11. @State colorArray: (Color|undefined|ColorMetrics|ColorContent)[] = [
12. this.p3Red, this.sRGBRed, this.p3Green, this.sRGBGreen, this.p3Blue,
13. this.sRGBBlue, ColorContent.ORIGIN, Color.Gray, undefined
14. ]
15. @State colorArrayStr: string[] = [
16. 'P3 Red', 'SRGB Red', 'P3 Green', 'SRGB Green',
17. 'P3 Blue', 'SRGB Blue', 'ORIGIN', 'Gray', 'undefined'
18. ]
19. @State arrayIdx: number = 0
20. build() {
21. Column() {
22. Text('FillColor is ' + this.colorArrayStr[this.arrayIdx])
23. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
24. Image($r('app.media.svgExample'))
25. .width(110).height(110).margin(15)
26. .fillColor(this.colorArray[this.arrayIdx])
27. Button('ChangeFillColor')
28. .onClick(()=>{
29. this.arrayIdx = (this.arrayIdx + 1) % this.colorArray.length
30. })
31. Blank().height(30).width('100%')
32. Text('FillColor is SRGB Red')
33. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
34. Image($r('app.media.svgExample'))
35. .width(110).height(110).margin(15)
36. .fillColor(this.sRGBRed)
37. Blank().height(30).width('100%')
38. Text('FillColor is SRGB Green')
39. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
40. Image($r('app.media.svgExample'))
41. .width(110).height(110).margin(15)
42. .fillColor(this.sRGBGreen)
43. Blank().height(30).width('100%')
44. Text('FillColor is SRGB Blue')
45. // $r('app.media.svgExample')需要替换为开发者所需的图像资源文件。
46. Image($r('app.media.svgExample'))
47. .width(110).height(110).margin(15)
48. .fillColor(this.sRGBBlue)
49. }
50. }
51. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/lyFy79HDRbiRsgXPpieOQw/zh-cn_image_0000002552959842.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=0C960C48B88FF03CECAF4928D1C5BF7701BC35D493DC863D56B78718F94C30B9)

### 示例24（使用应用沙箱路径显示图片）

在当前应用的haps/entry/files目录下预置一张名为cloud.png的图片，随后使用应用沙箱路径显示该图片。

```
1. import { fileUri } from '@kit.CoreFileKit';

3. @Entry
4. @Component
5. struct Index {
6. private getSandBoxUri(): string {
7. let context = this.getUIContext().getHostContext();
8. if (!context) {
9. return '';
10. }
11. // /data/storage/el2/base/haps/entry/files/cloud.png
12. // 从应用沙箱中的文件路径获取URI
13. // '/cloud.png'需要替换为开发者所需的图像资源文件。
14. return fileUri.getUriFromPath(context.filesDir + '/cloud.png');
15. }

17. build() {
18. Column() {
19. Image(this.getSandBoxUri())
20. .width(150)
21. .height(150)
22. }
23. .height('100%')
24. .width('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/7R1q6I2RTs6zhlo0nF6cHw/zh-cn_image_0000002583479843.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=AF076CBB7A078DE61222DD734F3AB6D9A6ADB26609C2E1E4268C0E6BFB43C278)

### 示例25（使用相对路径显示图片）

在工程pages目录同级位置创建common目录，在common目录下预置一张名为cloud1.png的图片，随后使用相对路径显示该图片。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column({ space: 10 }) {
6. Image('common/cloud1.png')
7. .width(100)
8. .height(100)
9. }
10. .height('100%')
11. .width('100%')
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/y1jKCUPIQuK1fMOTZe-Oow/zh-cn_image_0000002583479843.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=C28612E1E0FFCB6A84746DBD79EA8A2E77A2337A7CAAB667C920C6040255A794)

### 示例26（使用supportSvg2属性时，SVG图片的显示效果）

该示例通过设置[supportSvg2](ts-basic-components-image.md#supportsvg221)属性，使SVG标签解析能力增强功能生效。

从API version 21开始，新增supportSvg2属性。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. Column() {
7. Text('supportSvg2参数设置为true')
8. // $rawfile('image.svg')需要替换为开发者所需的图像资源文件。
9. Image($rawfile('image.svg'))
10. .width(200)
11. .height(200)
12. .border({ width: 2, color: 'red' })
13. .supportSvg2(true)
14. .margin({ bottom: 30 })
15. Text('supportSvg2参数设置为false（默认值）')
16. // $rawfile('image.svg')需要替换为开发者所需的图像资源文件。
17. Image($rawfile('image.svg'))
18. .width(200)
19. .height(200)
20. .border({ width: 2, color: 'red' })
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/j7TmxPXCQ1ap9E4S2vzf8w/zh-cn_image_0000002552800194.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=B068082A5E03415D9F4846920A8EB46B18EED7F69186E37F6E38A8AFB473706F)

### 示例27（使用ContentTransition属性实现图片淡入淡出切换效果）

从API version 21开始，该示例演示了在点击图片切换图源时，通过[contentTransition](ts-basic-components-image.md#contenttransition21)属性实现淡入淡出效果，完成图片的平滑过渡。

```
1. @Entry
2. @Component
3. struct ImageExample {
4. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
5. @State imageResource: Resource = $r('app.media.icon');

7. build() {
8. Row() {
9. Column() {
10. Image(this.imageResource)
11. .width(200)
12. .height(200)
13. // 启用淡入淡出过渡效果。
14. .contentTransition(ContentTransitionEffect.OPACITY)
15. .onClick(() => {
16. // $r('app.media.cloud1')需要替换为开发者所需的图像资源文件。
17. this.imageResource = $r('app.media.cloud1')
18. })
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/UkXzL6dDRaap_sJneH_QrQ/zh-cn_image_0000002583439889.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=14775FEF58B031E78A92CB6EAA67DE3C1A3CA52C8B214BFE751EA40548B6DD0D)

### 示例28（使用alt属性实现设置加载失败中图片和加载失败时图片）

该示例演示了在图片加载过程中和加载失败时，通过设置[alt](ts-basic-components-image.md#alt22)属性实现图片加载过程中和图片加载失败时显示指定图片。

```
1. @Entry
2. @Component
3. struct ImageExample {
4. build() {
5. Column() {
6. Text('同时设置placeholder属性和error属性')
7. // 设置一个错误网址来触发alt的placeholder属性和error属性。
8. Image("https://www.example.com/xxx.png")
9. // $r('app.media.startIcon')和$r('app.media.example')需要替换为开发者所需的图像资源文件。
10. .alt({ placeholder: $r('app.media.startIcon'), error: $r('app.media.example') })
11. .width(100)
12. .height(100)
13. .margin(20)
14. Text('只设置placeholder属性')
15. Image("https://www.example.com/xxx.png")
16. .alt({ placeholder: $r('app.media.startIcon')})
17. .width(100)
18. .height(100)
19. .margin(20)
20. Text('只设置error属性')
21. Image("https://www.example.com/xxx.png")
22. .alt({error: $r('app.media.example')})
23. .width(100)
24. .height(100)
25. .margin(20)
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/sT57akk_Rru0Z5txq7jn_g/zh-cn_image_0000002552959844.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=DAB39F15725E6AD1190E260510DE7E00EA48E5433C41E00AFCF90FAD721F79C5)

### 示例29（使用onError回调监听网络图片加载异常信息）

该示例演示如何通过[onError](ts-basic-components-image.md#onerror9)回调获取网络图片加载异常时的详细下载信息[ImageError](ts-basic-components-image.md#imageerror9)。当图片加载失败时，可通过ImageError中的downloadInfo属性获取网络图片下载的详细信息，包括下载的资源信息、网络请求信息以及性能统计信息，有助于快速定位网络异常或资源错误原因。

从API version 23开始，ImageError新增downloadInfo属性。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. RelativeContainer() {
6. Image('https://www.example.com/xxx.png') // 请填写一个具体的网络图片地址
7. .height(100)
8. .width(100)
9. .onError((e)=>{
10. console.info("DownLoadErrorInfo : " + JSON.stringify(e?.downloadInfo))
11. })
12. }
13. .height('100%')
14. .width('100%')
15. }
16. }
```

### 示例30（设置位图图片边缘抗锯齿）

该示例演示了如何通过设置[antialiased](ts-basic-components-image.md#antialiased23)接口开启位图图片边缘的抗锯齿功能。

从API version 23开始，新增[antialiased](ts-basic-components-image.md#antialiased23)接口。

```
1. @Entry
2. @Component
3. struct ImageExample {
4. // $r('app.media.icon')需要替换为开发者所需的图像资源文件。
5. @State imageResource: Resource = $r('app.media.icon');

7. build() {
8. Row() {
9. Blank()
10. .width(50)

12. Column() {
13. Blank()
14. .height(20)
15. Text('没有设置抗锯齿的有旋转角度的图片')
16. Blank()
17. .height(20)
18. Image(this.imageResource)
19. .width(50)
20. .height(50)
21. .rotate({angle: 1})

23. Blank()
24. .height(20)
25. Text('设置了抗锯齿的有旋转角度的图片')
26. Blank()
27. .height(20)
28. Image(this.imageResource)
29. .width(50)
30. .height(50)
31. .rotate({angle: 1})
32. .antialiased(true)
33. }
34. }
35. }
36. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/c9ko_gySRreyxlppHlmPhw/zh-cn_image_0000002583479845.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=21E686BBDB6CAC0D8A2BEFBCC013607D015F422FA167E26058492019979EEEEE)
