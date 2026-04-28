---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent
title: XComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 渲染绘制 > XComponent
category: harmonyos-references
scraped_at: 2026-04-28T08:02:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a1dc2e45809755e59bb6822e1c0e4df66384be38d8498028d2468277d5807ce0
---

提供用于图形绘制和媒体数据写入的Surface，XComponent负责将其嵌入到视图中，支持应用自定义Surface位置和大小。具体指南请参考[自定义渲染 (XComponent)文档](../harmonyos-guides/napi-xcomponent-guidelines.md)。

说明

该组件从API version 8 开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

无

## 接口

PhonePC/2in1TabletTVWearable

### XComponent19+

PhonePC/2in1TabletTVWearable

XComponent(params: NativeXComponentParameters)

在Native侧获取XComponent节点实例、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [NativeXComponentParameters](ts-basic-components-xcomponent.md#nativexcomponentparameters19) | 是 | 定义XComponent的具体配置参数。 |

### XComponent12+

PhonePC/2in1TabletTVWearable

XComponent(options: XComponentOptions)

创建XComponent组件，支持在ArkTS侧获取SurfaceId、注册XComponent持有的Surface的生命周期回调和触摸、鼠标、按键等组件事件回调，支持AI分析。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [XComponentOptions](ts-basic-components-xcomponent.md#xcomponentoptions12) | 是 | 定义XComponent的具体配置参数。 |

### XComponent10+

PhonePC/2in1TabletTVWearable

XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})

创建XComponent组件，支持Native侧触发XComponent生命周期回调。

该接口从API version 12开始不再演进，推荐使用[XComponent(options: XComponentOptions)](ts-basic-components-xcomponent.md#xcomponent12)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的唯一标识，支持最大的字符串长度128。 |
| type | [XComponentType](ts-appendix-enums.md#xcomponenttype10) | 是 | 用于指定XComponent组件类型。 |
| libraryname | string | 否 | 用Native层编译输出动态库名称（对应的动态库不支持跨模块加载），仅类型为SURFACE或TEXTURE时有效。 |
| controller | [XComponentController](ts-basic-components-xcomponent.md#xcomponentcontroller) | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。 |

### XComponent(deprecated)

PhonePC/2in1TabletTVWearable

XComponent(value: {id: string, type: string, libraryname?: string, controller?: XComponentController})

说明

从API version 8开始支持，从API version 12开始废弃，建议使用[XComponent(value: {id: string, type: XComponentType, libraryname?: string, controller?: XComponentController})](ts-basic-components-xcomponent.md#xcomponent10)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 组件的唯一标识，支持最大的字符串长度128。 |
| type | string | 是 | 用于指定XComponent组件类型，可选值仅有两个为：  -"surface"：用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。  -"component"9+ ：XComponent将变成一个容器组件，并可在其中执行非UI逻辑以动态加载显示内容。  其他值均会被视为"surface"类型 |
| libraryname | string | 否 | 应用Native层编译输出动态库名称（对应的动态库不支持跨模块加载），仅XComponent类型为"surface"时有效。 |
| controller | [XComponentController](ts-basic-components-xcomponent.md#xcomponentcontroller) | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅XComponent类型为"surface"时有效。 |

## XComponentOptions12+

PhonePC/2in1TabletTVWearable

定义XComponent的具体配置参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [XComponentType](ts-appendix-enums.md#xcomponenttype10) | 否 | 否 | 用于指定XComponent组件类型。 |
| controller | [XComponentController](ts-basic-components-xcomponent.md#xcomponentcontroller) | 否 | 否 | 给组件绑定一个控制器，通过控制器调用组件方法，仅类型为SURFACE或TEXTURE时有效。 |
| imageAIOptions | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

## NativeXComponentParameters19+

PhonePC/2in1TabletTVWearable

定义XComponent的具体配置参数。通过这种构造参数创建的XComponent，可以将其对应的[FrameNode](js-apis-arkui-framenode.md)对象传递至Native侧，使用NDK接口进行Surface生命周期的相关设置和[监听组件事件](../harmonyos-guides/ndk-listen-to-component-events.md)。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [XComponentType](ts-appendix-enums.md#xcomponenttype10) | 否 | 否 | 用于指定XComponent组件类型。 |
| imageAIOptions | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 否 | 是 | 给组件设置一个AI分析选项，通过此项可配置分析类型或绑定一个分析控制器。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持通用属性外，还支持以下属性：

说明

不支持foregroundColor、obscured和pixelStretchEffect属性。API version 17及之前，type为SURFACE类型时也不支持动态属性设置、自定义绘制、背景设置(backgroundColor除外)、图像效果(shadow除外)、maskShape和foregroundEffect属性。从API version 18开始，type为SURFACE类型时不支持设置的动态属性包含background、foregroundColor、animation、gesture、priorityGesture、parallelGesture、useEffect、renderGroup、flexGrow、direction、align、useSizeType、clip、geometryTransition、bindPopup、bindMenu、bindContextMenu、bindContentCover、bindSheet、stateStyles、restoreId、onVisibleAreaChange、accessibilityGroup、obscured、reuseId、accessibilityVirtualNode。

对于TEXTURE和SURFACE类型的XComponent组件，当不设置[renderFit](ts-universal-attributes-renderfit.md#renderfit)属性时，取默认值为RenderFit.RESIZE\_FILL。

对于SURFACE类型的XComponent组件，背景色设置为不透明的纯黑色，在API version 18之前，其[renderFit](ts-universal-attributes-renderfit.md#renderfit18)通用属性仅支持设置为RenderFit.RESIZE\_FILL；在API version 18及之后，支持所有的RenderFit枚举值。

对于使用[ArkUI NDK接口](../harmonyos-guides/ndk-access-the-arkts-page.md)创建的XComponent组件，不支持使用属性获取函数[getAttribute](capi-arkui-nativemodule-arkui-nativenodeapi-1.md#getattribute)获取其renderFit属性值。

### enableAnalyzer12+

PhonePC/2in1TabletTVWearable

enableAnalyzer(enable: boolean)

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。

本功能需要搭配XComponentController的[StartImageAnalyzer](ts-basic-components-xcomponent.md#startimageanalyzer12)和[StopImageAnalyzer](ts-basic-components-xcomponent.md#stopimageanalyzer12)一起使用。

不能和[overlay](ts-universal-attributes-overlay.md#overlay)属性同时使用，两者同时设置时overlay中[CustomBuilder](ts-types.md#custombuilder8)属性将失效。该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 是否启用图像分析功能。  true：开启图像分析；false：关闭图像分析。  默认值：false |

说明

仅type为SURFACE和TEXTURE时该功能有效。

### enableSecure13+

PhonePC/2in1TabletTVWearable

enableSecure(isSecure: boolean)

防止组件内自绘制内容被截屏、录屏。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isSecure | boolean | 是 | 是否开启隐私图层模式。  true：开启隐私图层模式；false：关闭隐私图层模式。  默认值：false |

说明

仅type为SURFACE时有效。

不支持[ArkUI NDK接口](../harmonyos-guides/ndk-build-ui-overview.md)创建的XComponent组件。

### hdrBrightness20+

PhonePC/2in1TabletTVWearable

hdrBrightness(brightness: number)

用于调整组件播放HDR视频的亮度。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | number | 是 | 用于调整组件播放HDR视频的亮度; brightness的取值范围为0.0~1.0; 小于0.0的值等价于0.0，大于1.0的值等价于1.0，异常值按1.0处理; 0.0 表示SDR视频的亮度，1.0 表示HDR视频的亮度。  默认值：1.0 |

说明

仅type为SURFACE时有效。

不支持[ArkUI NDK接口](../harmonyos-guides/ndk-build-ui-overview.md)创建的XComponent组件。

## 事件

PhonePC/2in1TabletTVWearable

从API version 12开始，type为SURFACE或TEXTURE时，支持[通用事件](ts-component-general-events.md)。

说明

当配置libraryname参数时，[点击事件](ts-universal-events-click.md)、[触摸事件](ts-universal-events-touch.md)、[挂载卸载事件](ts-universal-events-show-hide.md)、[按键事件](ts-universal-events-key.md)、[焦点事件](ts-universal-focus-event.md)、[鼠标事件](ts-universal-mouse-key.md)仅响应C-API侧事件接口。

仅type为SURFACE或TEXTURE时以下事件有效：

### onLoad

PhonePC/2in1TabletTVWearable

onLoad(callback: OnNativeLoadCallback )

插件加载完成时回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [OnNativeLoadCallback](ts-basic-components-xcomponent.md#onnativeloadcallback18) | 是 | XComponent持有的Surface创建后回调事件。 |

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(event: VoidCallback )

插件卸载完成时回调事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](ts-types.md#voidcallback12) | 是 | XComponent销毁后回调事件。 |

## OnNativeLoadCallback18+

PhonePC/2in1TabletTVWearable

type OnNativeLoadCallback = (event?: object) => void

XComponent持有的Surface创建后回调事件。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | object | 否 | 获取XComponent实例对象的context，context上挂载的方法由开发者在Native层定义。 |

## XComponentController

PhonePC/2in1TabletTVWearable

XComponent组件的控制器，可以将此对象绑定至XComponent组件，然后通过控制器来调用组件方法。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor()

XComponentController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. xcomponentController: XComponentController = new XComponentController();
```

### getXComponentSurfaceId9+

PhonePC/2in1TabletTVWearable

getXComponentSurfaceId(): string

获取XComponent对应Surface的ID，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | XComponent持有Surface的ID。 |

说明

使用自定义组件节点创建XComponent组件时，因为onLoad回调触发时机早于[onSurfaceCreated](ts-basic-components-xcomponent.md#onsurfacecreated12)，所以在onLoad回调中调用[getXComponentSurfaceId](ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)获取surfaceId会失败，建议在[onSurfaceCreated](ts-basic-components-xcomponent.md#onsurfacecreated12)回调中获取。

**示例：**

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. myXComponentController: XComponentController = new XComponentController();

7. build() {
8. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
9. XComponent({
10. type: XComponentType.SURFACE,
11. controller: this.myXComponentController
12. })
13. .onLoad(() => {
14. let surfaceId: string = this.myXComponentController.getXComponentSurfaceId();
15. console.info("XComponent SurfaceId: " + surfaceId);
16. })
17. }
18. }
19. }
```

### setXComponentSurfaceSize(deprecated)

PhonePC/2in1TabletTVWearable

setXComponentSurfaceSize(value: {surfaceWidth: number, surfaceHeight: number}): void

设置XComponent持有Surface的宽度和高度，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

说明

该接口从API version 9开始支持，从API version 12开始废弃，建议使用[setXComponentSurfaceRect](ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceWidth | number | 是 | XComponent持有Surface的宽度。 |
| surfaceHeight | number | 是 | XComponent持有Surface的高度。 |

### getXComponentContext

PhonePC/2in1TabletTVWearable

getXComponentContext(): Object

获取XComponent实例对象的context，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Object | 获取XComponent实例对象的context，context包含的具体接口方法由开发者自定义，context内容与onLoad回调中的第一个参数一致。 |

### setXComponentSurfaceRect12+

PhonePC/2in1TabletTVWearable

setXComponentSurfaceRect(rect: SurfaceRect): void

设置XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rect | [SurfaceRect](ts-basic-components-xcomponent.md#surfacerect12对象说明) | 是 | XComponent持有Surface的显示区域。 |

说明

rect参数中的offsetX/offsetY不设置或传入异常值时，Surface显示区域相对于XComponent左上角x/y轴的偏移效果默认按照居中显示。

rect参数中的surfaceWidth和surfaceHeight存在0、负数或其他异常值时，调用该接口设置显示区域不生效。未调用该接口主动设置Surface显示区域时，surfaceWidth默认与组件宽度一致，surfaceHeight默认与组件高度一致。

该方法优先级高于[border](ts-universal-attributes-border.md#border)、[padding](ts-universal-attributes-size.md#padding)等可以改变内容偏移和大小的属性。

### getXComponentSurfaceRect12+

PhonePC/2in1TabletTVWearable

getXComponentSurfaceRect(): SurfaceRect

获取XComponent持有Surface的显示区域，包括宽高和相对于组件左上角的位置坐标，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SurfaceRect](ts-basic-components-xcomponent.md#surfacerect12对象说明) | 获取XComponent持有Surface的显示区域。 |

### onSurfaceCreated12+

PhonePC/2in1TabletTVWearable

onSurfaceCreated(surfaceId: string): void

当XComponent持有的Surface创建后进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |

说明

仅当XComponent组件未设置libraryname参数时，会进行该回调。

### onSurfaceChanged12+

PhonePC/2in1TabletTVWearable

onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void

当XComponent持有的Surface大小改变后（包括首次创建时的大小改变）进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |
| rect | [SurfaceRect](ts-basic-components-xcomponent.md#surfacerect12对象说明) | 是 | 回调该方法的时候，绑定XComponent持有Surface的显示区域。 |

说明

仅当XComponent组件未设置libraryname参数时，会进行该回调。

### onSurfaceDestroyed12+

PhonePC/2in1TabletTVWearable

onSurfaceDestroyed(surfaceId: string): void

当XComponent持有的Surface销毁后进行该回调，仅XComponent类型为SURFACE("surface")或TEXTURE时有效，具体可以参考指南[创建XComponent和管理Surface生命周期](../harmonyos-guides/napi-xcomponent-guidelines.md#创建xcomponent和管理surface生命周期)章节。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| surfaceId | string | 是 | 回调该方法的时候，绑定XComponent持有Surface的ID。 |

说明

仅当XComponent组件未设置libraryname参数时，会进行该回调。

### startImageAnalyzer12+

PhonePC/2in1TabletTVWearable

startImageAnalyzer(config: ImageAnalyzerConfig): Promise<void>

配置AI分析并启动AI分析功能，使用前需先[启用图像AI分析能力](ts-basic-components-xcomponent.md#enableanalyzer12)。使用Promise异步回调。

该方法调用时，将截取调用时刻的画面帧进行分析，使用时需注意启动分析的时机，避免出现画面和分析内容不一致的情况。

若该方法尚未执行完毕，此时重复调用，则会触发错误回调。

说明

分析类型不支持动态修改。

该特性依赖设备能力，不支持该能力的情况下，将返回错误码。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](ts-image-common.md#imageanalyzerconfig12) | 是 | 执行AI分析所需要的入参，用于配置AI分析功能。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。用于获取AI分析是否成功执行。 |

**错误码：**

以下错误码的详细介绍请参见[图像AI分析错误码](errorcode-image-analyzer.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 110001 | Image analysis feature is unsupported. |
| 110002 | Image analysis is currently being executed. |
| 110003 | Image analysis is stopped. |

### stopImageAnalyzer12+

PhonePC/2in1TabletTVWearable

stopImageAnalyzer(): void

停止AI分析功能，AI分析展示的内容将被销毁。

说明

在startImageAnalyzer方法未返回结果时调用本方法，会触发其错误回调。

该特性依赖设备能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setXComponentSurfaceRotation12+

PhonePC/2in1TabletTVWearable

setXComponentSurfaceRotation(rotationOptions: SurfaceRotationOptions): void

设置XComponent持有Surface在屏幕旋转时是否锁定方向，仅XComponent类型为SURFACE("surface")时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotationOptions | [SurfaceRotationOptions](ts-basic-components-xcomponent.md#surfacerotationoptions12对象说明) | 是 | 设置XComponent持有Surface在屏幕旋转时是否锁定方向。 |

说明

rotationOptions未配置时，默认XComponent持有Surface在屏幕旋转时不锁定方向，跟随屏幕进行旋转。

仅在屏幕旋转过程中生效，旋转完成后不再锁定Surface。

仅在屏幕旋转90°，即发生横竖屏切换时生效。

锁定旋转后的Buffer宽高需要保持不变，否则会有拉伸问题。

### getXComponentSurfaceRotation12+

PhonePC/2in1TabletTVWearable

getXComponentSurfaceRotation(): Required<SurfaceRotationOptions>

获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置，仅XComponent类型为SURFACE("surface")时有效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Required<[SurfaceRotationOptions](ts-basic-components-xcomponent.md#surfacerotationoptions12对象说明)> | 获取XComponent持有Surface在屏幕旋转时是否锁定方向的设置。 |

### lockCanvas20+

PhonePC/2in1TabletTVWearable

lockCanvas(): DrawingCanvas | null

返回可用于向XComponent上绘制内容的画布对象。具体绘制方法请参考[Canvas](arkts-apis-graphics-drawing-canvas.md)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DrawingCanvas](ts-drawingrenderingcontext.md#drawingcanvas12对象说明) | null | 可用于向XComponent区域绘制的画布对象或者空对象null。 |

说明

如果当前XComponent状态无法获取画布对象则将返回null。原因通常为：

1. XComponent持有的Surface未创建完成（可通过设置[onLoad](ts-basic-components-xcomponent.md#onload)/[onSurfaceCreated](ts-basic-components-xcomponent.md#onsurfacecreated12)回调来确定，此回调触发时，Surface已创建完成）。
2. 之前已经调用过lockCanvas来获取过画布对象，且该画布对象未调用[unlockCanvasAndPost](ts-basic-components-xcomponent.md#unlockcanvasandpost20)去释放。

只支持TEXTURE和SURFACE模式。

使用此接口后，同时在NDK侧获取NativeWindow并调用相关接口进行绘制，可能出现缓冲区竞争和上下文冲突而发生绘制画面错误等异常，因此不允许使用。

此接口需要和[unlockCanvasAndPost](ts-basic-components-xcomponent.md#unlockcanvasandpost20)接口配对使用，具体参考[示例3使用画布对象在XComponent上绘制内容](ts-basic-components-xcomponent.md#示例3使用画布对象在xcomponent上绘制内容)。

### unlockCanvasAndPost20+

PhonePC/2in1TabletTVWearable

unlockCanvasAndPost(canvas: DrawingCanvas): void

将画布对象中的内容绘制在XComponent区域，并释放该画布对象。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| canvas | [DrawingCanvas](ts-drawingrenderingcontext.md#drawingcanvas12对象说明) | 是 | 之前调用lockCanvas方法返回的画布对象。 |

说明

1. 画布对象调用unlockCanvasAndPost释放后，不可再使用该画布对象。
2. 只支持TEXTURE和SURFACE模式。
3. 使用此接口后，同时在NDK侧获取NativeWindow并调用相关接口进行绘制，可能出现缓冲区竞争和上下文冲突而发生绘制画面错误等异常，因此不允许使用。
4. 此接口需要和[lockCanvas](ts-basic-components-xcomponent.md#lockcanvas20)接口配对使用，具体参考[示例3使用画布对象在XComponent上绘制内容](ts-basic-components-xcomponent.md#示例3使用画布对象在xcomponent上绘制内容)。

### setXComponentSurfaceConfig22+

PhonePC/2in1TabletTVWearable

setXComponentSurfaceConfig(config: SurfaceConfig): void

设置XComponent创建的Surface的选项，用于设置XComponent持有的Surface在渲染时是否需要被视为不透明。

说明

仅当XComponent组件类型为TEXTURE或SURFACE时，本接口生效。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [SurfaceConfig](ts-basic-components-xcomponent.md#surfaceconfig22对象说明) | 是 | Surface选项。 |

## SurfaceRotationOptions12+对象说明

PhonePC/2in1TabletTVWearable

用于描述XComponent持有Surface在屏幕旋转时是否锁定方向的设置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| lock | boolean | 否 | 是 | Surface在屏幕旋转时是否锁定方向，未设置时默认取值为false，即不锁定方向。  true：锁定方向；false：不锁定方向。 |

## SurfaceRect12+对象说明

PhonePC/2in1TabletTVWearable

用于描述XComponent持有Surface的显示区域。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| offsetX | number | 否 | 是 | Surface显示区域相对于XComponent组件左上角的x轴坐标，单位：px。 |
| offsetY | number | 否 | 是 | Surface显示区域相对于XComponent组件左上角的y轴坐标，单位：px。 |
| surfaceWidth | number | 否 | 否 | Surface显示区域的宽度，单位：px。 |
| surfaceHeight | number | 否 | 否 | Surface显示区域的高度，单位：px。 |

说明

surfaceWidth和surfaceHeight属性在未调用[setXComponentSurfaceRect](ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)也未设置[border](ts-universal-attributes-border.md#border)和[padding](ts-universal-attributes-size.md#padding)等属性时，其取值大小为XComponent组件的大小。

surfaceWidth和surfaceHeight属性的取值都不可超过8192px，否则会导致渲染异常。

沉浸式场景下，默认布局的SurfaceRect不包括安全区，需调用[setXComponentSurfaceRect](ts-basic-components-xcomponent.md#setxcomponentsurfacerect12)接口主动设置Surface显示区域达到沉浸式效果。

## SurfaceConfig22+对象说明

PhonePC/2in1TabletTVWearable

用于描述XComponent持有的Surface在渲染时是否需要被视为不透明。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isOpaque | boolean | 否 | 是 | XComponent持有的Surface在渲染时是否需要被视为不透明，未设置时默认取值为false，即在渲染时会应用Surface中绘制内容像素的透明度。  true表示需要被视为不透明，false表示不需要被视为不透明。  默认值：false |

## 示例

PhonePC/2in1TabletTVWearable

示例效果请以真机运行为准，当前DevEco Studio预览器不支持。

### 示例1（图像AI分析功能）

使用enableAnalyzer属性开启图像AI分析功能。可通过XComponentController控制开始、停止图形AI分析。

说明

本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考[ArkTS XComponent示例](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/ArkTSXComponent)

```
1. // xxx.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import nativeRender from 'libnativerender.so';// 开发者自己实现的so，详见上述说明。

5. class CustomXComponentController extends XComponentController {
6. onSurfaceCreated(surfaceId: string): void {
7. console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
8. nativeRender.SetSurfaceId(BigInt(surfaceId));
9. }

11. onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
12. console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
13. nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
14. }

16. onSurfaceDestroyed(surfaceId: string): void {
17. console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
18. nativeRender.DestroySurface(BigInt(surfaceId));
19. }
20. }

22. @Entry
23. @Component
24. struct XComponentExample {
25. xComponentController: XComponentController = new CustomXComponentController();
26. private config: ImageAnalyzerConfig = {
27. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT]
28. };
29. private aiController: ImageAnalyzerController = new ImageAnalyzerController();
30. private options: ImageAIOptions = {
31. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT],
32. aiController: this.aiController
33. };
34. @State xcWidth: string = "720px";
35. @State xcHeight: string = "720px";
36. @State currentStatus: string = "index";

38. build() {
39. Column({ space: 5 }) {
40. Row() {
41. Text('Native XComponent Sample')
42. .fontSize('24fp')
43. .fontWeight(500)
44. .margin({
45. left: 24,
46. top: 12
47. })
48. }
49. .margin({ top: 24 })
50. .width('100%')
51. .height(56)

53. XComponent({
54. type: XComponentType.SURFACE,
55. controller: this.xComponentController,
56. imageAIOptions: this.options
57. })
58. .width(this.xcWidth)
59. .height(this.xcHeight)
60. .enableAnalyzer(true)
61. .onClick(() => {
62. let surfaceId = this.xComponentController.getXComponentSurfaceId();
63. nativeRender.ChangeColor(BigInt(surfaceId));
64. let hasChangeColor: boolean = false;
65. if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
66. hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
67. }
68. if (hasChangeColor) {
69. this.currentStatus = "change color";
70. }
71. })
72. Text(this.currentStatus)
73. .fontSize('24fp')
74. .fontWeight(500)
75. Column() {
76. Button('start AI analyze')
77. .onClick(() => {
78. this.xComponentController.startImageAnalyzer(this.config)
79. .then(() => {
80. console.info("analysis complete");
81. })
82. .catch((error: BusinessError) => {
83. console.error("error code: " + error.code);
84. })
85. })
86. .margin(2)
87. Button('stop AI analyze')
88. .onClick(() => {
89. this.xComponentController.stopImageAnalyzer();
90. })
91. .margin(2)
92. Button('get analyzer types')
93. .onClick(() => {
94. this.aiController.getImageAnalyzerSupportTypes();
95. })
96. .margin(2)
97. Button('Draw Star')
98. .fontSize('16fp')
99. .fontWeight(500)
100. .margin({ bottom: 24 })
101. .onClick(() => {
102. let surfaceId = this.xComponentController.getXComponentSurfaceId();
103. console.info(`surface rect is ${this.xComponentController.getXComponentSurfaceRect()}`);
104. nativeRender.DrawPattern(BigInt(surfaceId));
105. let hasDraw: boolean = false;
106. if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
107. hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
108. }
109. if (hasDraw) {
110. this.currentStatus = "draw star";
111. }
112. })
113. .margin(2)
114. }.justifyContent(FlexAlign.Center)
115. }
116. .width("100%")
117. }
118. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/dVcrK-coTGGWYum6OHhyXQ/zh-cn_image_0000002583440063.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000212Z&HW-CC-Expire=86400&HW-CC-Sign=DE39470ECBA29E0194BB6228C0814AC8C5B8196637CA33FA8825F8C21F54F4FC)

### 示例2（在surface旋转过程中锁定）

通过setXComponentSurfaceRotation设置surface在屏幕旋转过程中锁定方向，不跟随屏幕进行旋转。

说明

本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考[ArkTS XComponent示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/ArkTSXComponent)。

```
1. // xxx.ets
2. import nativeRender from 'libnativerender.so';

4. class MyXComponentController extends XComponentController {
5. onSurfaceCreated(surfaceId: string): void {
6. console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
7. nativeRender.SetSurfaceId(BigInt(surfaceId));
8. }

10. onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
11. console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
12. nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
13. }

15. onSurfaceDestroyed(surfaceId: string): void {
16. console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
17. nativeRender.DestroySurface(BigInt(surfaceId));
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State isLock: boolean = true;
25. @State xc_width: number = 500;
26. @State xc_height: number = 700;
27. myXComponentController: XComponentController = new MyXComponentController();

29. build() {
30. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
31. XComponent({
32. id: "XComponent",
33. type: XComponentType.SURFACE,
34. controller: this.myXComponentController
35. })
36. .onLoad(() => {
37. let surfaceRotation: SurfaceRotationOptions = { lock: this.isLock };
38. this.myXComponentController.setXComponentSurfaceRotation(surfaceRotation);
39. console.info("Surface getXComponentSurfaceRotation lock = " +
40. this.myXComponentController.getXComponentSurfaceRotation().lock);
41. })
42. .width(this.xc_width)
43. .height(this.xc_height)
44. Button("Draw")
45. .onClick(() => {
46. let surfaceId = this.myXComponentController.getXComponentSurfaceId();
47. nativeRender.DrawPattern(BigInt(surfaceId));
48. })
49. }
50. }
51. }
```

### 示例3（使用画布对象在XComponent上绘制内容）

从API version 20开始，该示例通过调用[lockCanvas](ts-basic-components-xcomponent.md#lockcanvas20)返回画布对象，通过画布对象调用对应的绘制接口，再调用[unlockCanvasAndPost](ts-basic-components-xcomponent.md#unlockcanvasandpost20)在XComponent上绘制内容。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';

4. @Entry
5. @Component
6. struct Index {
7. private xcController: XComponentController = new XComponentController();
8. private mCanvas: DrawingCanvas | null = null;

10. build() {
11. Column() {
12. XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
13. .width("80%")
14. .height("80%")
15. .onLoad(() => {
16. this.mCanvas = this.xcController.lockCanvas();
17. if (this.mCanvas) {
18. this.mCanvas.drawColor(255, 240, 250, 255); // 每次绘制前必须完全重绘整个XComponent区域,可以调用此方法实现
19. const brush = new drawing.Brush(); // 创建画刷对象
20. brush.setColor({ // 设置画刷的颜色
21. alpha: 255,
22. red: 39,
23. green: 135,
24. blue: 217
25. });
26. this.mCanvas.attachBrush(brush); // 绑定画刷到画布上
27. this.mCanvas.drawRect({ // 绘制一个矩形
28. left: 300,
29. right: 800,
30. top: 100,
31. bottom: 800
32. });
33. this.mCanvas.detachBrush(); // 将画刷与画布解绑
34. this.xcController.unlockCanvasAndPost(this.mCanvas);
35. }
36. })
37. }
38. .height('100%')
39. .width('100%')
40. }
41. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/fgXWm2FWT1Sx-5Cew6nOBg/zh-cn_image_0000002552960018.png?HW-CC-KV=V1&HW-CC-Date=20260428T000212Z&HW-CC-Expire=86400&HW-CC-Sign=D9E4444617504BD02879C6FE00E9BAAA54BDFFD99A659E039B82AD617EBC774C)

### 示例4（XComponent实现沉浸式效果）

从API version 20开始，在示例3的基础上，调用setXComponentSurfaceRect接口主动设置Surface显示区域达到沉浸式效果。

```
1. // xxx.ets
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { display } from '@kit.ArkUI'
4. @Entry
5. @Component
6. struct Index {
7. private xcController: XComponentController = new XComponentController();
8. private mCanvas: DrawingCanvas | null = null;
9. @State screenWidth: number = 0;
10. @State screenHeight:number = 0;
11. aboutToAppear() {
12. try {
13. const displayClass = display.getDefaultDisplaySync();
14. this.screenWidth = displayClass.width;
15. this.screenHeight = displayClass.height;
16. } catch (error) {
17. console.error(`失败代码: ${error.code}，信息: ${error.message}`);
18. }
19. }

21. build() {
22. Column() {
23. XComponent({ type: XComponentType.SURFACE, controller: this.xcController })
24. .width("100%")
25. .height("100%")
26. .onLoad(() => {
27. // 请在此处设置Surface大小，过大可能会导致绘制时间长
28. this.xcController.setXComponentSurfaceRect({surfaceWidth: this.screenWidth, surfaceHeight: this.screenHeight, offsetX: 0, offsetY: 0});
29. this.mCanvas = this.xcController.lockCanvas();
30. if (this.mCanvas) {
31. this.mCanvas.drawColor(255, 39, 135, 217); // 每次绘制前必须完全重绘整个XComponent区域，可以调用此方法实现
32. this.xcController.unlockCanvasAndPost(this.mCanvas);
33. }
34. })
35. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
36. }
37. .height('100%')
38. .width('100%')
39. }
40. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/WHwFm5AaQuiozICPm4fP9w/zh-cn_image_0000002583480019.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000212Z&HW-CC-Expire=86400&HW-CC-Sign=BD89F29068D6937EF88669D9A11917D8596657229673FA2097E7E145577240B7)

### 示例5（设置XComponent持有Surface在渲染时是否需要被视为不透明）

从API version 22开始，该示例通过调用[setXComponentSurfaceConfig](ts-basic-components-xcomponent.md#setxcomponentsurfaceconfig22)接口设置XComponent持有的Surface在渲染时是否需要被视为不透明。

说明

本示例画图逻辑具体实现（和nativeRender相关的函数实现）可以参考[ArkTS XComponent示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Native/ArkTSXComponent)。

```
1. // xxx.ets
2. import nativeRender from 'libnativerender.so'; // 开发者自己实现的so，详见上述说明。

4. // 重写XComponentController，设置生命周期回调
5. class MyXComponentController extends XComponentController{
6. onSurfaceCreated(surfaceId: string): void {
7. console.info(`onSurfaceCreated surfaceId: ${surfaceId}`);
8. nativeRender.SetSurfaceId(BigInt(surfaceId));
9. }
10. onSurfaceChanged(surfaceId: string, rect: SurfaceRect): void {
11. console.info(`onSurfaceChanged surfaceId: ${surfaceId}, rect: ${JSON.stringify(rect)}`);
12. // 在onSurfaceChanged中调用ChangeSurface绘制内容
13. nativeRender.ChangeSurface(BigInt(surfaceId), rect.surfaceWidth, rect.surfaceHeight);
14. }
15. onSurfaceDestroyed(surfaceId: string): void {
16. console.info(`onSurfaceDestroyed surfaceId: ${surfaceId}`);
17. nativeRender.DestroySurface(BigInt(surfaceId));
18. }
19. }

21. @Entry
22. @Component
23. struct Index {
24. @State currentStatus: string = "index";
25. xComponentController: XComponentController = new MyXComponentController();

27. aboutToAppear(): void {
28. // 设置XComponent持有的Surface在渲染时被视为不透明
29. this.xComponentController.setXComponentSurfaceConfig({ isOpaque: true });
30. }

32. build() {
33. Column() {
34. Column({ space: 10 }) {
35. XComponent({
36. type: XComponentType.SURFACE,
37. controller: this.xComponentController
38. })
39. .backgroundColor(Color.Transparent)
40. Text(this.currentStatus)
41. .fontSize('24fp')
42. .fontWeight(500)
43. }
44. .onClick(() => {
45. let surfaceId = this.xComponentController.getXComponentSurfaceId();
46. nativeRender.ChangeColor(BigInt(surfaceId));
47. let hasChangeColor: boolean = false;
48. if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
49. hasChangeColor = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasChangeColor;
50. }
51. if (hasChangeColor) {
52. this.currentStatus = "change color";
53. }
54. })
55. .margin({
56. top: 27,
57. left: 12,
58. right: 12
59. })
60. .height('40%')
61. .width('90%')
62. Row() {
63. Button('Draw Star')
64. .fontSize('16fp')
65. .fontWeight(500)
66. .margin({ bottom: 24 })
67. .onClick(() => {
68. let surfaceId = this.xComponentController.getXComponentSurfaceId();
69. nativeRender.DrawPattern(BigInt(surfaceId));
70. let hasDraw: boolean = false;
71. if (nativeRender.GetXComponentStatus(BigInt(surfaceId))) {
72. hasDraw = nativeRender.GetXComponentStatus(BigInt(surfaceId)).hasDraw;
73. }
74. if (hasDraw) {
75. this.currentStatus = "draw star";
76. }
77. })
78. .width('53.6%')
79. .height(40)
80. }
81. .width('100%')
82. .justifyContent(FlexAlign.Center)
83. .alignItems(VerticalAlign.Bottom)
84. .layoutWeight(1)
85. }
86. .width('100%')
87. .height('100%')
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/V7IJJH1vRk-n6BAcfzMGKg/zh-cn_image_0000002552800370.jpeg?HW-CC-KV=V1&HW-CC-Date=20260428T000212Z&HW-CC-Expire=86400&HW-CC-Sign=E8B7B68D46B2C91AC1A37935EC602AABCE68561AE95D236B391178BD30C19EC0)
