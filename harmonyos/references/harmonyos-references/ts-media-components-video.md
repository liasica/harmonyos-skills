---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-media-components-video
title: Video
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 图片与视频 > Video
category: harmonyos-references
scraped_at: 2026-04-28T08:01:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:29cd676614877d806ad4ec3d2cf4c0a8a8dce8b60d64b01b35984aec14a2ff5b
---

用于播放视频文件并控制其播放状态的组件。

说明

该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

Video组件只提供简单的视频播放功能，无法支撑复杂的视频播控场景。复杂开发场景推荐使用[AVPlayer](arkts-apis-media-avplayer.md)播控API和[XComponent](ts-basic-components-xcomponent.md)组件开发。

Video组件在使用expandSafeArea扩展安全区域时，组件视频显示内容区域不支持扩展。

## 权限列表

PhonePC/2in1TabletTVWearable

使用网络视频时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 子组件

PhonePC/2in1TabletTVWearable

不支持子组件。

## 接口

PhonePC/2in1TabletTVWearable

### Video

PhonePC/2in1TabletTVWearable

Video(value: VideoOptions)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [VideoOptions](ts-media-components-video.md#videooptions对象说明) | 是 | 视频信息。 |

## VideoOptions对象说明

PhonePC/2in1TabletTVWearable

定义Video的具体配置参数。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| src | string | [Resource](ts-types.md#resource) | 否 | 是 | 视频的数据源，支持本地视频和网络视频。  Resource格式可以跨包/跨模块访问资源文件，常用于访问本地视频。  - 仅支持rawfile文件下的资源，即通过$rawfile引用视频文件。  string格式可用于加载网络视频和本地视频，常用于加载网络视频。  - 支持网络视频地址。  - 支持file://路径前缀的字符串，即[应用沙箱URI](js-apis-file-fileuri.md#constructor10)：file://<bundleName>/<sandboxPath>。用于读取应用沙箱路径内的资源。需要保证目录包路径下的文件有可读权限。  默认值：空字符串  异常值：按默认值处理。  **说明：**  视频支持的格式是：mp4、mkv、TS。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| currentProgressRate | number | string | [PlaybackSpeed8+](ts-media-components-video.md#playbackspeed8枚举说明) | 否 | 是 | 视频播放倍速。  **说明：**  number格式取值仅支持：0.75，1.0，1.25，1.75，2.0。从API version 22开始，新增支持取值0.5，1.5，3，0.25和0.125。  string格式支持number格式取值的字符串形式："0.75"，"1.0"，"1.25"，"1.75"，"2.0"。从API version 22开始，新增支持取值"0.5"，"1.5"，"3"，"0.25"和"0.125"。  除此之外的取值，比如"abc"或"1.5+1.5"会按照异常值处理。  默认值：1.0 | PlaybackSpeed.Speed\_Forward\_1\_00\_X  异常值：按默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| previewUri | string | [PixelMap](arkts-apis-image-pixelmap.md) | [Resource](ts-types.md#resource) | 否 | 是 | 视频未播放时的预览图片路径，默认不显示图片。  string格式可用于加载本地图片和网络图片，  - 支持网络图片地址。  - 支持相对路径引用本地图片，例如：previewUri: “common/test.jpg”。当使用相对路径引用本地图片时，不支持跨包/跨模块调用。  - 支持file://路径前缀的字符串，即[应用沙箱URI](js-apis-file-fileuri.md#constructor10)：file://<bundleName>/<sandboxPath>。用于读取应用沙箱路径内的资源。需要保证目录包路径下的文件有可读权限。  Resource格式可以跨包/跨模块访问资源文件。  - 支持rawfile文件下的资源，即通过$rawfile引用图片。  - 支持通过$r引用系统资源或者应用资源中的图片。  默认值：空字符串  异常值：按默认值处理。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| controller | [VideoController](ts-media-components-video.md#videocontroller) | 否 | 是 | 设置视频控制器，可以控制视频的播放状态。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| imageAIOptions12+ | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 否 | 是 | 设置图像AI分析选项，可配置分析类型或绑定一个分析控制器。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| posterOptions18+ | [PosterOptions](ts-media-components-video.md#posteroptions18对象说明) | 否 | 是 | 设置视频播放的首帧送显选项，可以控制视频是否支持首帧送显。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## PlaybackSpeed8+枚举说明

PhonePC/2in1TabletTVWearable

视频播放倍速选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Speed\_Forward\_0\_75\_X | 0.75 | 0.75倍速播放。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Speed\_Forward\_1\_00\_X | 1 | 1倍速播放。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Speed\_Forward\_1\_25\_X | 1.25 | 1.25倍速播放。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Speed\_Forward\_1\_75\_X | 1.75 | 1.75倍速播放。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| Speed\_Forward\_2\_00\_X | 2 | 2倍速播放。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_0\_50\_X22+ | 0.5 | 0.5倍速播放。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_1\_50\_X22+ | 1.5 | 1.5倍速播放。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_3\_00\_X22+ | 3 | 3倍速播放。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_0\_25\_X22+ | 0.25 | 0.25倍速播放。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| SPEED\_FORWARD\_0\_125\_X22+ | 0.125 | 0.125倍速播放。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### muted

PhonePC/2in1TabletTVWearable

muted(value: boolean)

设置视频是否静音，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 视频是否静音。  true：开启静音；false：关闭静音。  默认值：false |

说明

Video组件在未设置静音的情况下，启播瞬间会抢占音频焦点。若用户想设置静音播放不抢占其他音频焦点，应保证静音设置在开始播放视频之前。

### autoPlay

PhonePC/2in1TabletTVWearable

autoPlay(value: boolean)

设置视频是否自动播放，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否自动播放。  true：开启自动播放；false：关闭自动播放。  默认值：false |

### controls

PhonePC/2in1TabletTVWearable

controls(value: boolean)

设置控制视频播放的控制栏是否显示，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 控制视频播放的控制栏是否显示。  true：控制栏显示；false：控制栏不显示。  默认值：true |

说明

Video组件自带的控制器无法自定义。若有其他需求，可隐藏自带控制器并自定义控制器的样式或功能。参考[视频播放](https://gitcode.com/harmonyos_samples/video-play)。

### objectFit

PhonePC/2in1TabletTVWearable

objectFit(value: ImageFit)

设置视频的填充模式，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](ts-appendix-enums.md#imagefit) | 是 | 视频填充模式。  默认值：Cover  约束：不支持ImageFit类型中的枚举值MATRIX，若设置，则作用效果与Cover一致。  异常值：若设置异常值undefined、null，或不在[ImageFit](ts-appendix-enums.md#imagefit)枚举范围内的值，作用效果均与Cover一致。 |

### loop

PhonePC/2in1TabletTVWearable

loop(value: boolean)

设置是否单个视频循环播放，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否单个视频循环播放。  true：开启循环播放；false：关闭循环播放。  默认值：false |

### enableAnalyzer12+

PhonePC/2in1TabletTVWearable

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

使能后，视频播放暂停时自动进入分析状态，开始分析当前画面帧，视频继续播放后自动退出分析状态。

不能和[overlay](ts-universal-attributes-overlay.md)属性同时使用，两者同时设置时[overlay](ts-universal-attributes-overlay.md)中[CustomBuilder](ts-types.md#custombuilder8)属性将失效。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用AI分析功能。  true：开启AI分析功能；false：关闭AI分析功能。  默认值：false |

说明

当前仅在使用自定义控制栏([controls](ts-media-components-video.md#controls)属性设置为false)时支持该功能。

该特性依赖设备能力。

### analyzerConfig12+

PhonePC/2in1TabletTVWearable

analyzerConfig(config: ImageAnalyzerConfig)

设置AI分析识别类型，包括主体识别、文字识别和对象查找等功能，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](ts-image-common.md#imageanalyzerconfig12) | 是 | 设置AI分析识别类型。 |

### enableShortcutKey15+

PhonePC/2in1TabletTVWearable

enableShortcutKey(enabled: boolean)

设置组件支持快捷键响应，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

目前支持在组件获焦后响应空格键播放/暂停、上下方向键调整视频音量、左右方向键快进/快退。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否启用快捷键响应。  true：开启快捷键响应；false：关闭快捷键响应。  默认值：false |

## 事件

PhonePC/2in1TabletTVWearable

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onStart

PhonePC/2in1TabletTVWearable

onStart(event: VoidCallback)

播放时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 视频播放的回调函数。 |

### onPause

PhonePC/2in1TabletTVWearable

onPause(event: VoidCallback)

暂停时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 视频暂停的回调函数。 |

### onFinish

PhonePC/2in1TabletTVWearable

onFinish(event: VoidCallback)

播放结束时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | 视频播放结束的回调函数。 |

### onError

PhonePC/2in1TabletTVWearable

onError(event: VoidCallback | ErrorCallback)

播放失败时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

说明

从API version 20开始，该接口支持在[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)中调用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | [ErrorCallback](js-apis-base.md#errorcallback)20+ | 是 | 视频播放失败时的回调函数。其中[ErrorCallback](js-apis-base.md#errorcallback)类型入参的回调函数用于接收异常信息，回调返回的错误码详细介绍请参见[Video组件错误码](errorcode-video.md)和[Media错误码](errorcode-media.md)。 |

### onStop12+

PhonePC/2in1TabletTVWearable

onStop(event: Callback<void>)

播放停止时触发该事件(当stop()方法被调用后触发)，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | Callback<void> | 是 | 视频播放停止时的回调函数。 |

### onPrepared

PhonePC/2in1TabletTVWearable

onPrepared(callback: Callback<PreparedInfo>)

视频准备完成时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PreparedInfo](ts-media-components-video.md#preparedinfo18对象说明)> | 是 | 视频准备完成时的回调函数。 |

### onSeeking

PhonePC/2in1TabletTVWearable

onSeeking(callback: Callback<PlaybackInfo>)

操作进度条过程时上报时间信息，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PlaybackInfo](ts-media-components-video.md#playbackinfo18对象说明)> | 是 | 操作进度条过程时的回调函数。 |

### onSeeked

PhonePC/2in1TabletTVWearable

onSeeked(callback: Callback<PlaybackInfo>)

操作进度条完成后，上报播放时间信息，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PlaybackInfo](ts-media-components-video.md#playbackinfo18对象说明)> | 是 | 操作进度条完成后的回调函数。 |

### onUpdate

PhonePC/2in1TabletTVWearable

onUpdate(callback: Callback<PlaybackInfo>)

播放进度变化时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PlaybackInfo](ts-media-components-video.md#playbackinfo18对象说明)> | 是 | 播放进度变化时的回调函数。 |

### onFullscreenChange

PhonePC/2in1TabletTVWearable

onFullscreenChange(callback: Callback<FullscreenInfo>)

在全屏播放与非全屏播放状态之间切换时触发该事件，支持[attributeModifier](ts-universal-attributes-attribute-modifier.md#attributemodifier)动态设置属性方法。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[FullscreenInfo](ts-media-components-video.md#fullscreeninfo18对象说明)> | 是 | 在全屏播放与非全屏播放状态之间切换时的回调函数。 |

## FullscreenInfo18+对象说明

PhonePC/2in1TabletTVWearable

用于描述当前视频是否进入全屏播放状态。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| fullscreen10+ | boolean | 否 | 否 | 当前视频是否进入全屏播放状态。  true：进入全屏播放状态；false：未进入全屏播放状态。  默认值：false  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## PreparedInfo18+对象说明

PhonePC/2in1TabletTVWearable

用于描述当前视频的时长。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration10+ | number | 否 | 否 | 当前视频的时长。  单位：秒  取值范围：[0,+∞)  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## PlaybackInfo18+对象说明

PhonePC/2in1TabletTVWearable

用于描述当前视频播放的进度。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| time10+ | number | 否 | 否 | 当前视频播放的进度。  单位：秒  取值范围：[0,+∞)  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## PosterOptions18+对象说明

PhonePC/2in1TabletTVWearable

用于描述当前视频是否配置首帧送显。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| showFirstFrame | boolean | 否 | 是 | 当前视频是否配置首帧送显，当开启首帧送显时，[VideoOptions对象](ts-media-components-video.md#videooptions对象说明)中的previewUri字段不生效。  true：开启首帧送显；false：关闭首帧送显。  默认值：false  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| contentTransitionEffect21+ | [ContentTransitionEffect](ts-image-common.md#contenttransitioneffect21对象说明) | 否 | 是 | 当前视频的预览图内容变化时的转场动效。配置showFirstFrame为true（即配置开启首帧送显时），或未配置有效的[VideoOptions对象](ts-media-components-video.md#videooptions对象说明)的previewUri时，该字段不生效。  默认值：ContentTransitionEffect.IDENTITY  设置为undefined或null时，取值为ContentTransitionEffect.IDENTITY。  **元服务API：** 从API version 21开始，该接口支持在元服务中使用。 |

## VideoController

PhonePC/2in1TabletTVWearable

一个VideoController对象可以控制一个或多个Video。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### 导入对象

```
1. let controller: VideoController = new VideoController();
```

### constructor

PhonePC/2in1TabletTVWearable

constructor()

VideoController的构造函数。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### start

PhonePC/2in1TabletTVWearable

start()

开始播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### pause

PhonePC/2in1TabletTVWearable

pause()

暂停播放，显示当前帧，再次播放时从当前位置继续播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### stop

PhonePC/2in1TabletTVWearable

stop()

停止播放，显示当前帧，再次播放时从头开始播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### reset12+

PhonePC/2in1TabletTVWearable

reset(): void

Video组件重置AVPlayer。显示当前帧，再次播放时从头开始播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setCurrentTime

PhonePC/2in1TabletTVWearable

setCurrentTime(value: number)

指定视频播放的进度位置。

说明

若用户需要从视频内的某一时间点开始播放，应关闭自动播放，在视频准备完成后先跳转再播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 视频播放进度位置。  取值范围：[0, [duration](ts-media-components-video.md#preparedinfo18对象说明)]  当设置value大于duration时，进度跳转至最后；当设置value小于0时，不会进行进度跳转。  单位：秒  从API version 8开始，支持设置视频的跳转模式，详见[setCurrentTime8+](ts-media-components-video.md#setcurrenttime8)。 |

### requestFullscreen

PhonePC/2in1TabletTVWearable

requestFullscreen(value: boolean)

请求全屏播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean | 是 | 是否全屏（填充满应用窗口）播放。  true：请求全屏播放；false：不请求全屏播放。  默认值：false |

说明

Video组件自带的全屏功能仅将视频内容设为全屏，显示默认控制器，无法显示自定义标题或控制器。如需其他功能，用户需自行实现全屏功能。

### exitFullscreen

PhonePC/2in1TabletTVWearable

exitFullscreen()

退出全屏播放。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setCurrentTime8+

PhonePC/2in1TabletTVWearable

setCurrentTime(value: number, seekMode: SeekMode)

指定视频播放的进度位置，并指定跳转模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 视频播放进度位置。  取值范围：[0, [duration](ts-media-components-video.md#preparedinfo18对象说明)]  当设置value大于duration时，进度跳转至最后；当设置value小于0时，不会进行进度跳转。  单位：秒 |
| seekMode | [SeekMode](ts-media-components-video.md#seekmode8枚举说明) | 是 | 跳转模式。 |

## SeekMode8+枚举说明

PhonePC/2in1TabletTVWearable

视频跳转模式选项。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 说明 |
| --- | --- |
| PreviousKeyframe | 跳转到前一个最近的关键帧。 |
| NextKeyframe | 跳转到后一个最近的关键帧。 |
| ClosestKeyframe | 跳转到最近的关键帧。 |
| Accurate | 精准跳转，不论是否为关键帧。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（视频播放基础用法）

基础用法包括：控制栏、预览图、自动播放、播放速度、响应快捷键（从API version 15开始，支持通过[enableShortcutKey](ts-media-components-video.md#enableshortcutkey15)设置组件开启快捷键响应）、控制器（开始播放、暂停播放、停止播放、重置AVPlayer、跳转等）、首帧送显（从API version 18开始，支持通过[posterOptions](ts-media-components-video.md#posteroptions18对象说明)设置视频播放的首帧送显选项。从API version 21开始，posterOptions支持通过[PosterOptions](ts-media-components-video.md#posteroptions18对象说明)的contentTransitionEffect参数来设置当前视频的预览图内容变化时的转场动效。）以及一些状态回调方法。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct VideoCreateComponent {
5. // $rawfile('video1.mp4')、$r('app.media.poster1')需要分别替换为开发者所需的视频、图片资源文件。
6. @State videoSrc: Resource = $rawfile('video1.mp4');
7. @State previewUri: Resource = $r('app.media.poster1');
8. @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
9. @State isAutoPlay: boolean = false;
10. @State showControls: boolean = true;
11. @State isShortcutKeyEnabled: boolean = false;
12. @State showFirstFrame: boolean = false;
13. controller: VideoController = new VideoController();

15. build() {
16. Column() {
17. Video({
18. src: this.videoSrc,
19. previewUri: this.previewUri, // 设置预览图。
20. currentProgressRate: this.curRate, // 设置播放速度。
21. controller: this.controller,
22. posterOptions: {
23. showFirstFrame: this.showFirstFrame,
24. contentTransitionEffect: ContentTransitionEffect.OPACITY
25. } // 关闭首帧送显, 设置预览图淡入淡出动效。
26. })
27. .width('100%')
28. .height(600)
29. .autoPlay(this.isAutoPlay)
30. .controls(this.showControls)
31. .enableShortcutKey(this.isShortcutKeyEnabled)
32. .onStart(() => {
33. console.info('onStart');
34. })
35. .onPause(() => {
36. console.info('onPause');
37. })
38. .onFinish(() => {
39. console.info('onFinish');
40. })
41. .onError(() => {
42. console.error('onError');
43. })
44. .onStop(() => {
45. console.info('onStop');
46. })
47. .onPrepared((e?: DurationObject) => {
48. if (e != undefined) {
49. console.info(`onPrepared is ${e.duration}`);
50. }
51. })
52. .onSeeking((e?: TimeObject) => {
53. if (e != undefined) {
54. console.info(`onSeeking is ${e.time}`);
55. }
56. })
57. .onSeeked((e?: TimeObject) => {
58. if (e != undefined) {
59. console.info(`onSeeked is ${e.time}`);
60. }
61. })
62. .onUpdate((e?: TimeObject) => {
63. if (e != undefined) {
64. console.info(`onUpdate is ${e.time}`);
65. }
66. })
67. .onFullscreenChange((e?: FullscreenObject) => {
68. if (e != undefined) {
69. console.info(`onFullscreenChange is ${e.fullscreen}`);
70. }
71. })

73. Row() {
74. // $rawfile('video2.mp4')、$r('app.media.poster2')需要分别替换为开发者所需的视频、图片资源文件。
75. Button('src').onClick(() => {
76. this.videoSrc = $rawfile('video2.mp4'); // 切换视频源。
77. }).margin(5)
78. Button('previewUri').onClick(() => {
79. this.previewUri = $r('app.media.poster2'); // 切换视频预览海报。
80. }).margin(5)
81. Button('controls').onClick(() => {
82. this.showControls = !this.showControls; // 切换是否显示视频控制栏。
83. }).margin(5)
84. }

86. Row() {
87. Button('start').onClick(() => {
88. this.controller.start(); // 开始播放。
89. }).margin(2)
90. Button('pause').onClick(() => {
91. this.controller.pause(); // 暂停播放。
92. }).margin(2)
93. Button('stop').onClick(() => {
94. this.controller.stop(); // 结束播放。
95. }).margin(2)
96. Button('reset').onClick(() => {
97. this.controller.reset(); // 重置AVPlayer。
98. }).margin(2)
99. Button('setTime').onClick(() => {
100. this.controller.setCurrentTime(10, SeekMode.Accurate); // 精准跳转到视频的10s位置。
101. }).margin(2)
102. }

104. Row() {
105. Button('rate 0.75').onClick(() => {
106. this.curRate = PlaybackSpeed.Speed_Forward_0_75_X; // 0.75倍速播放。
107. }).margin(5)
108. Button('rate 1').onClick(() => {
109. this.curRate = PlaybackSpeed.Speed_Forward_1_00_X; // 原倍速播放。
110. }).margin(5)
111. Button('rate 2').onClick(() => {
112. this.curRate = PlaybackSpeed.Speed_Forward_2_00_X; // 2倍速播放。
113. }).margin(5)
114. }
115. }
116. }
117. }

119. interface DurationObject {
120. duration: number;
121. }

123. interface TimeObject {
124. time: number;
125. }

127. interface FullscreenObject {
128. fullscreen: boolean;
129. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/FMy3IS-QSGemv3_NzD2tfg/zh-cn_image_0000002583479847.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=69BA3750B24851D90D131CC75B3107E4552EA6ABFE71CEDC882B4D822DC3F6E2)

### 示例2（图像分析功能）

通过enableAnalyzer属性开启图像AI分析。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct ImageAnalyzerExample {
5. // $rawfile('video1.mp4')、$r('app.media.poster1')需要分别替换为开发者所需的视频、图片资源文件
6. @State videoSrc: Resource = $rawfile('video1.mp4');
7. @State previewUri: Resource = $r('app.media.poster1');
8. controller: VideoController = new VideoController();
9. config: ImageAnalyzerConfig = {
10. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
11. }
12. private aiController: ImageAnalyzerController = new ImageAnalyzerController();
13. private options: ImageAIOptions = {
14. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
15. aiController: this.aiController
16. }

18. build() {
19. Column() {
20. Video({
21. src: this.videoSrc,
22. previewUri: this.previewUri,
23. controller: this.controller,
24. imageAIOptions: this.options // 设置图像AI分析选项
25. })
26. .width('100%')
27. .height(600)
28. .controls(false)
29. .enableAnalyzer(true)
30. .analyzerConfig(this.config)
31. .onStart(() => {
32. console.info('onStart');
33. })
34. .onPause(() => {
35. console.info('onPause');
36. })

38. Row() {
39. Button('start').onClick(() => {
40. this.controller.start(); // 开始播放
41. }).margin(5)
42. Button('pause').onClick(() => {
43. this.controller.pause(); // 暂停播放
44. }).margin(5)
45. Button('getTypes').onClick(() => {
46. this.aiController.getImageAnalyzerSupportTypes();
47. }).margin(5)
48. }
49. }
50. }
51. }
```

### 示例3（播放拖入的视频）

以下示例展示了如何使Video组件能够播放拖入的视频。

```
1. // xxx.ets
2. import { unifiedDataChannel, uniformTypeDescriptor } from '@kit.ArkData';

4. @Entry
5. @Component
6. struct Index {
7. // $rawfile('video1.mp4')需要替换为开发者所需的视频资源文件
8. @State videoSrc: Resource | string = $rawfile('video1.mp4');
9. private controller: VideoController = new VideoController();

11. build() {
12. Column() {
13. Video({
14. src: this.videoSrc,
15. controller: this.controller
16. })
17. .width('100%')
18. .height(600)
19. .onPrepared(() => {
20. // 在onPrepared回调中执行controller的start方法，确保视频源更换后直接开始播放。
21. this.controller.start();
22. })
23. .onDrop((e: DragEvent) => {
24. // 外部视频拖入应用Video组件范围，松手后触发通过onDrop注册的回调。
25. // 在DragEvent中会包含拖入的视频源信息，取出后赋值给状态变量videoSrc即可改变Video的视频源。
26. let record = e.getData().getRecords()[0];
27. if (record.getType() == uniformTypeDescriptor.UniformDataType.VIDEO) {
28. let videoInfo = record as unifiedDataChannel.Video;
29. this.videoSrc = videoInfo.videoUri;
30. }
31. })
32. }
33. }
34. }
```

### 示例4（视频填充模式）

通过objectFit属性设置视频填充模式。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct VideoObject {
5. // $rawfile('rabbit.mp4')、$r('app.media.tree')需要分别替换为开发者所需的视频、图片资源文件
6. @State videoSrc: Resource = $rawfile('rabbit.mp4');
7. @State previewUri: Resource = $r('app.media.tree');
8. @State showControls: boolean = true;
9. controller: VideoController = new VideoController();

11. build() {
12. Column() {
13. Text('ImageFit.Contain').fontSize(12)
14. Video({
15. src: this.videoSrc,
16. previewUri: this.previewUri,
17. controller: this.controller
18. })
19. .width(350)
20. .height(230)
21. .controls(this.showControls)
22. .objectFit(ImageFit.Contain) // 设置视频填充模式为ImageFit.Contain
23. .margin(5)

25. Text('ImageFit.Fill').fontSize(12)
26. Video({
27. src: this.videoSrc,
28. previewUri: this.previewUri,
29. controller: this.controller
30. })
31. .width(350)
32. .height(230)
33. .controls(this.showControls)
34. .objectFit(ImageFit.Fill) // 设置视频填充模式为ImageFit.Fill
35. .margin(5)

37. Text('ImageFit.START').fontSize(12)
38. Video({
39. src: this.videoSrc,
40. previewUri: this.previewUri,
41. controller: this.controller
42. })
43. .width(350)
44. .height(230)
45. .controls(this.showControls)
46. .objectFit(ImageFit.START) // 设置视频填充模式为ImageFit.START
47. .margin(5)
48. }.width('100%').alignItems(HorizontalAlign.Center)
49. }
50. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/orGWIXvVQhG4f4wbyD1gZg/zh-cn_image_0000002552800198.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=1602160B4C287C3CA6404ABFD0B0A568AFA70E4C0AC024E1430339172C3039A3)

### 示例5（onError事件上报错误码）

从API version 20开始，支持通过[onError](ts-media-components-video.md#onerror)获取错误信息，该示例以传入不存在的视频资源路径为例。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct VideoErrorComponent {
5. @State videoSrc: string = 'video.mp4'; // 传入不存在的视频资源路径。
6. @State isAutoPlay: boolean = false;
7. @State showControls: boolean = true;
8. @State showFirstFrame: boolean = false;
9. controller: VideoController = new VideoController();
10. @State errorMessage: string = '';

12. build() {
13. Column() {
14. Video({
15. src: this.videoSrc,
16. controller: this.controller,
17. })
18. .width(200)
19. .height(120)
20. .margin(5)
21. .autoPlay(this.isAutoPlay)
22. .controls(this.showControls)
23. .onError((err) => {
24. // 通过onError事件获取错误码，code为错误码，message为错误信息。
25. console.error(`code is ${err.code}, message is ${err.message}`);
26. this.errorMessage = `code is ${err.code}, message is ${err.message}`;
27. })
28. // 传入不存在的视频资源路径，预期："code is 103602, message is Not a valid source"。
29. Text(this.errorMessage)
30. }
31. .width('100%')
32. .height('100%')
33. .backgroundColor('rgb(213,213,213)')
34. }
35. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/bW8Xnd2jR52AUCjxLbGF_g/zh-cn_image_0000002583439893.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=28DEE99018DB3F7C5EE6307D1A05CA0C0252736C38B6D5C5352167CC154319B8)

### 示例6（使用attributeModifier动态设置Video组件的属性及方法）

以下示例展示了如何使用attributeModifier动态设置Video组件的enableAnalyzer、analyzerConfig属性和onStart、onPause、onFinish、onError、onStop、onPrepared、onSeeking、onSeeked、onUpdate、onFullscreenChange方法。

```
1. // xxx.ets
2. class MyVideoModifier implements AttributeModifier<VideoAttribute> {
3. applyNormalAttribute(instance: VideoAttribute): void {
4. // 设置开启组件AI分析功能，长按触发AI识别功能
5. instance.enableAnalyzer(true);
6. let config: ImageAnalyzerConfig = {
7. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
8. }
9. instance.analyzerConfig(config);
10. instance.onStart(() => {
11. console.info('video: onStart');
12. })
13. instance.onPause(() => {
14. console.info('video: onPause');
15. })
16. instance.onFinish(() => {
17. console.info('video: onFinish');
18. })
19. instance.onError((err) => {
20. console.error(`video: onError is code = ${err.code}, message = ${err.message}`);
21. })
22. instance.onStop(() => {
23. console.info('video: onStop');
24. })
25. instance.onPrepared((e?: DurationObject) => {
26. if (e != undefined) {
27. console.info(`video: onPrepared is ${e.duration}`);
28. }
29. })
30. instance.onSeeking((e?: TimeObject) => {
31. if (e != undefined) {
32. console.info(`video: onSeeking is ${e.time}`);
33. }
34. })
35. instance.onSeeked((e?: TimeObject) => {
36. if (e != undefined) {
37. console.info(`video: onSeeked is ${e.time}`);
38. }
39. })
40. instance.onUpdate((e?: TimeObject) => {
41. if (e != undefined) {
42. console.info(`video: onUpdate is ${e.time}`);
43. }
44. })
45. instance.onFullscreenChange((e?: FullscreenObject) => {
46. if (e != undefined) {
47. console.info(`video: onFullscreenChange is ${e.fullscreen}`);
48. }
49. })
50. }
51. }

53. @Entry
54. @Component
55. struct VideoModifierDemo {
56. // $rawfile('video.mp4')需要替换为开发者所需的视频资源文件
57. @State videoSrc: Resource = $rawfile('video.mp4');
58. @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
59. @State isAutoPlay: boolean = false;
60. @State showControls: boolean = false;
61. controller: VideoController = new VideoController();
62. @State modifier: MyVideoModifier = new MyVideoModifier();

64. build() {
65. Column() {
66. Video({
67. src: this.videoSrc,
68. currentProgressRate: this.curRate, // 设置播放速度
69. controller: this.controller
70. })
71. .width(300)
72. .height(180)
73. .autoPlay(this.isAutoPlay)
74. .controls(this.showControls)
75. .attributeModifier(this.modifier)
76. Row() {
77. Button('start').onClick(() => {
78. this.controller.start(); // 开始播放
79. }).margin(2)
80. Button('pause').onClick(() => {
81. this.controller.pause(); // 暂停播放
82. }).margin(2)
83. Button('stop').onClick(() => {
84. this.controller.stop(); // 结束播放
85. }).margin(2)
86. Button('reset').onClick(() => {
87. this.controller.reset(); // 重置AVPlayer
88. }).margin(2)
89. }

91. Row() {
92. Button('Fullscreen').onClick(() => {
93. this.controller.requestFullscreen(true); // 全屏
94. }).margin(2)
95. Button('showControls').onClick(() => {
96. this.showControls = !this.showControls; // 显示控制栏
97. }).margin(2)
98. }
99. }
100. }
101. }

103. interface DurationObject {
104. duration: number;
105. }

107. interface TimeObject {
108. time: number;
109. }

111. interface FullscreenObject {
112. fullscreen: boolean;
113. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/RBwS14-LRlCrt0l7hCxT1w/zh-cn_image_0000002552959848.png?HW-CC-KV=V1&HW-CC-Date=20260428T000154Z&HW-CC-Expire=86400&HW-CC-Sign=F97AEE8F78956D64A69D7C2BF8F5B268997893C276DDBE69E001AEE16AF81961)
