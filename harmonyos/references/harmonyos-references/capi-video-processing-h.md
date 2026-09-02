---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-h
title: video_processing.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > video_processing.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:738039fff07e0c36e7089c8b45100c8bf5407e3cb785b1d5d644fd91d351e02c
---

## 概述

声明视频处理函数。

提供视频处理能力，包括颜色空间转换、元数据生成和视频缩放。

**引用文件：** <multimedia/video\_processing\_engine/video\_processing.h>

**库：** libvideo\_processing.so

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**起始版本：** 12

**相关模块：** [VideoProcessing](capi-videoprocessing.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_InitializeEnvironment(void)](capi-video-processing-h.md#oh_videoprocessing_initializeenvironment) | 初始化视频处理全局环境。  该函数是可选的。  该函数只在主进程启动时被调用一次，这样可以减少[OH\_VideoProcessing\_Create](capi-video-processing-h.md#oh_videoprocessing_create)的时间。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_DeinitializeEnvironment(void)](capi-video-processing-h.md#oh_videoprocessing_deinitializeenvironment) | 释放视频处理全局环境。  调用前，必须调用[OH\_VideoProcessing\_InitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_initializeenvironment)初始化。  通常在主进程即将退出时调用该函数，以释放通过[OH\_VideoProcessing\_InitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_initializeenvironment)函数初始化的全局环境。  如果仍有视频处理的实例运行中，就不能调用该函数。 |
| [bool OH\_VideoProcessing\_IsColorSpaceConversionSupported(const VideoProcessing\_ColorSpaceInfo\* sourceVideoInfo, const VideoProcessing\_ColorSpaceInfo\* destinationVideoInfo)](capi-video-processing-h.md#oh_videoprocessing_iscolorspaceconversionsupported) | 查询是否支持视频颜色空间转换。 |
| [bool OH\_VideoProcessing\_IsMetadataGenerationSupported(const VideoProcessing\_ColorSpaceInfo\* sourceVideoInfo)](capi-video-processing-h.md#oh_videoprocessing_ismetadatagenerationsupported) | 查询是否支持视频元数据生成。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Create(OH\_VideoProcessing\*\* videoProcessor, int type)](capi-video-processing-h.md#oh_videoprocessing_create) | 创建视频处理实例。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Destroy(OH\_VideoProcessing\* videoProcessor)](capi-video-processing-h.md#oh_videoprocessing_destroy) | 销毁视频处理实例。  销毁之前先停止实例，参阅[OH\_VideoProcessing\_Stop](capi-video-processing-h.md#oh_videoprocessing_stop)。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_RegisterCallback(OH\_VideoProcessing\* videoProcessor,const VideoProcessing\_Callback\* callback, void\* userData)](capi-video-processing-h.md#oh_videoprocessing_registercallback) | 注册回调函数。  在开始视频处理之前注册回调函数，视频处理过程中无法注册回调函数。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_SetSurface(OH\_VideoProcessing\* videoProcessor,const OHNativeWindow\* window)](capi-video-processing-h.md#oh_videoprocessing_setsurface) | 设置视频处理输出surface。  在视频处理启动之前设置输出surface。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_GetSurface(OH\_VideoProcessing\* videoProcessor, OHNativeWindow\*\* window)](capi-video-processing-h.md#oh_videoprocessing_getsurface) | 创建surface。  在视频处理启动之前创建输入surface。调用[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)销毁输入surface。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_SetParameter(OH\_VideoProcessing\* videoProcessor, const OH\_AVFormat\* parameter)](capi-video-processing-h.md#oh_videoprocessing_setparameter) | 设置视频处理输出参数。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_GetParameter(OH\_VideoProcessing\* videoProcessor, OH\_AVFormat\* parameter)](capi-video-processing-h.md#oh_videoprocessing_getparameter) | 获取视频处理参数。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Start(OH\_VideoProcessing\* videoProcessor)](capi-video-processing-h.md#oh_videoprocessing_start) | 启动视频处理。  成功启动后，回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)会报告[VIDEO\_PROCESSING\_STATE\_RUNNING](capi-video-processing-types-h.md#videoprocessing_state)状态。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_Stop(OH\_VideoProcessing\* videoProcessor)](capi-video-processing-h.md#oh_videoprocessing_stop) | 停止视频处理。  成功停止后，回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)会报告[VIDEO\_PROCESSING\_STATE\_STOPPED](capi-video-processing-types-h.md#videoprocessing_state)状态。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessing\_RenderOutputBuffer(OH\_VideoProcessing\* videoProcessor, uint32\_t index)](capi-video-processing-h.md#oh_videoprocessing_renderoutputbuffer) | 渲染处理并输出buffer。  如果设置了回调函数[OH\_VideoProcessingCallback\_OnNewOutputBuffer](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer)，当输出buffer准备好之后会通过回调函数把buffer的索引返回给用户。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_Create(VideoProcessing\_Callback\*\* callback)](capi-video-processing-h.md#oh_videoprocessingcallback_create) | 创建视频处理回调函数对象。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_Destroy(VideoProcessing\_Callback\* callback)](capi-video-processing-h.md#oh_videoprocessingcallback_destroy) | 销毁回调对象。回调对象在注册之后就可以销毁。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnError(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnError onError)](capi-video-processing-h.md#oh_videoprocessingcallback_bindonerror) | 绑定回调函数[OH\_VideoProcessingCallback\_OnError](capi-video-processing-types-h.md#oh_videoprocessingcallback_onerror)到回调对象。绑定完成之后，需要调用 [OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)，将回调对象注册到视频处理实例，才能使其生效。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnState(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnState onState)](capi-video-processing-h.md#oh_videoprocessingcallback_bindonstate) | 绑定回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)到回调对象。绑定完成之后，需要调用 [OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)，将回调对象注册到视频处理实例，才能使其生效。 |
| [VideoProcessing\_ErrorCode OH\_VideoProcessingCallback\_BindOnNewOutputBuffer(VideoProcessing\_Callback\* callback,OH\_VideoProcessingCallback\_OnNewOutputBuffer onNewOutputBuffer)](capi-video-processing-h.md#oh_videoprocessingcallback_bindonnewoutputbuffer) | 绑定回调函数[OH\_VideoProcessingCallback\_OnNewOutputBuffer](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer)到回调对象。绑定完成之后，需要调用 [OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)，将回调对象注册到视频处理实例，才能使其生效。 |

## 函数说明

### OH\_VideoProcessing\_InitializeEnvironment()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_InitializeEnvironment(void)
```

**描述**

初始化视频处理全局环境。

该函数是可选的。

该函数只在主进程启动时被调用一次，用于初始化视频处理全局环境，这样可以减少[OH\_VideoProcessing\_Create](capi-video-processing-h.md#oh_videoprocessing_create)的时间。

调用[OH\_VideoProcessing\_DeinitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_deinitializeenvironment)释放视频处理全局环境。

初始化后，必须释放视频处理全局环境，释放方式及时机详见[OH\_VideoProcessing\_DeinitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_deinitializeenvironment)。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果初始化成功，返回VIDEO\_PROCESSING\_SUCCESS，否则返回VIDEO\_PROCESSING\_ERROR\_INITIALIZE\_FAILED。  如果失败，应用需要检查GPU是否正常工作。 |

### OH\_VideoProcessing\_DeinitializeEnvironment()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_DeinitializeEnvironment(void)
```

**描述**

释放视频处理全局环境。

调用前，必须调用[OH\_VideoProcessing\_InitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_initializeenvironment)初始化。

通常在主进程即将退出时调用该函数来释放通过调用[OH\_VideoProcessing\_InitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_initializeenvironment)函数初始化的全局环境。

如果仍有视频处理的实例运行中，就不能调用该函数。

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果执行成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果还有视频处理的实例没有销毁或者没有调用[OH\_VideoProcessing\_InitializeEnvironment](capi-video-processing-h.md#oh_videoprocessing_initializeenvironment)，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessing\_IsColorSpaceConversionSupported()

```c
bool OH_VideoProcessing_IsColorSpaceConversionSupported(const VideoProcessing_ColorSpaceInfo* sourceVideoInfo,const VideoProcessing_ColorSpaceInfo* destinationVideoInfo)
```

**描述**

查询是否支持视频颜色空间转换。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [VideoProcessing\_ColorSpaceInfo](capi-videoprocessing-videoprocessing-colorspaceinfo.md)\* sourceVideoInfo | 输入视频颜色空间信息。 |
| const [VideoProcessing\_ColorSpaceInfo](capi-videoprocessing-videoprocessing-colorspaceinfo.md)\* destinationVideoInfo | 输出视频颜色空间信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持视频颜色空间转换返回true，否则返回false。 |

### OH\_VideoProcessing\_IsMetadataGenerationSupported()

```c
bool OH_VideoProcessing_IsMetadataGenerationSupported(const VideoProcessing_ColorSpaceInfo* sourceVideoInfo)
```

**描述**

查询是否支持视频元数据生成。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [VideoProcessing\_ColorSpaceInfo](capi-videoprocessing-videoprocessing-colorspaceinfo.md)\* sourceVideoInfo | 输入视频颜色空间信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 如果支持视频元数据生成返回true，否则返回false。 |

### OH\_VideoProcessing\_Create()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_Create(OH_VideoProcessing** videoProcessor, int type)
```

**描述**

创建视频处理实例。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\*\* videoProcessor | 输出参数。指向视频处理对象的指针的指针。输入前\*videoProcessor必须是空指针。 |
| int type | 使用视频处理实例常量来指定处理类型。实例的处理类型不能改变。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果视频处理实例创建成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果处理类型不支持，返回VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING，例如，不支持元数据生成。  如果创建视频处理实例失败，返回VIDEO\_PROCESSING\_ERROR\_CREATE\_FAILED。  如果实例为空或实例的指针非空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果处理类型无效，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_VideoProcessing\_Destroy()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_Destroy(OH_VideoProcessing* videoProcessor)
```

**描述**

销毁视频处理实例。

销毁之前先停止实例，参阅[OH\_VideoProcessing\_Stop](capi-video-processing-h.md#oh_videoprocessing_stop)。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针，建议在实例销毁之后将其设置为空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果实例销毁成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果实例仍在运行，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessing\_RegisterCallback()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_RegisterCallback(OH_VideoProcessing* videoProcessor,const VideoProcessing_Callback* callback, void* userData)
```

**描述**

注册回调函数。

在开始视频处理之前注册回调函数，视频处理过程中无法注册回调函数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |
| const [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md)\* callback | 回调函数指针。 |
| void\* userData | 指向用户特定数据的指针，如this指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果回调函数注册成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果回调函数指针为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  如果实例仍在运行，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessing\_SetSurface()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_SetSurface(OH_VideoProcessing* videoProcessor,const OHNativeWindow* window)
```

**描述**

设置视频处理输出surface。

在视频处理启动之前设置输出surface。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |
| const [OHNativeWindow](capi-videoprocessing-nativewindow.md)\* window | 指向输出surface的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果输出surface设置成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果window为空指针，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_VideoProcessing\_GetSurface()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_GetSurface(OH_VideoProcessing* videoProcessor, OHNativeWindow** window)
```

**描述**

创建surface。

在视频处理启动之前创建输入surface。调用[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)销毁输入surface。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |
| [OHNativeWindow](capi-videoprocessing-nativewindow.md)\*\* window | 指向输入surface的指针。例如，此输入surface指针可以指向视频解码器输出surface。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果执行成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果window为空指针或指向window的指针为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  如果创建surface失败，或者输入surface已经创建，或者视频处理实例还在运行，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessing\_SetParameter()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_SetParameter(OH_VideoProcessing* videoProcessor,const OH_AVFormat* parameter)
```

**描述**

设置视频处理输出参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |
| const [OH\_AVFormat](capi-videoprocessing-oh-avformat.md)\* parameter | 指向视频处理参数实例的指针，用于传入需设置的视频处理参数，例如视频宽度、高度、像素格式及编解码格式等。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果参数设置成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果参数为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  如果参数的某些属性无效，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE，例如，包含不支持的参数值。  如果内存分配失败，返回VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_VideoProcessing\_GetParameter()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_GetParameter(OH_VideoProcessing* videoProcessor, OH_AVFormat* parameter)
```

**描述**

获取视频处理参数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |
| [OH\_AVFormat](capi-videoprocessing-oh-avformat.md)\* parameter | 指向视频处理参数实例的指针，用于获取当前视频处理的参数，比如视频宽度、高度、像素格式、编解码格式等。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果参数获取成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果参数为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_VideoProcessing\_Start()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_Start(OH_VideoProcessing* videoProcessor)
```

**描述**

启动视频处理。

成功启动后，回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)会报告[VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_RUNNING状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果执行成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果没有设置输出surface，或者没有创建输入surface，或者实例已经运行，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessing\_Stop()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_Stop(OH_VideoProcessing* videoProcessor)
```

**描述**

停止视频处理。

成功停止后，回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)会报告[VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_STOPPED状态。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果执行成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果实例已经停止，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessing\_RenderOutputBuffer()

```c
VideoProcessing_ErrorCode OH_VideoProcessing_RenderOutputBuffer(OH_VideoProcessing* videoProcessor, uint32_t index)
```

**描述**

渲染处理并输出buffer。

如果设置了回调函数[OH\_VideoProcessingCallback\_OnNewOutputBuffer](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer)，当输出buffer准备好之后会通过回调函数把buffer的索引返回给用户。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 指向视频处理实例的指针。 |
| uint32\_t index | 输出buffer的索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果执行成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果实例为空或者不是一个视频处理实例，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE。  如果索引值无效，输出VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  如果没有设置回调函数[OH\_VideoProcessingCallback\_OnNewOutputBuffer](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer)或者实例已经停止运行，返回VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED。 |

### OH\_VideoProcessingCallback\_Create()

```c
VideoProcessing_ErrorCode OH_VideoProcessingCallback_Create(VideoProcessing_Callback** callback)
```

**描述**

创建视频处理回调函数对象。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md)\*\* callback | 输出参数。\*callback是指向回调函数对象的指针。在创建回调函数对象之前\*callback必须为空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果回调函数对象创建成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果callback为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。  如果内存不足，返回VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY。 |

### OH\_VideoProcessingCallback\_Destroy()

```c
VideoProcessing_ErrorCode OH_VideoProcessingCallback_Destroy(VideoProcessing_Callback* callback)
```

**描述**

销毁回调对象。回调对象在注册之后就可以销毁。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md)\* callback | 指向回调对象的指针，建议在回调对象销毁之后将其设置为空指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果回调对象销毁成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果callback为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_VideoProcessingCallback\_BindOnError()

```c
VideoProcessing_ErrorCode OH_VideoProcessingCallback_BindOnError(VideoProcessing_Callback* callback,OH_VideoProcessingCallback_OnError onError)
```

**描述**

绑定回调函数[OH\_VideoProcessingCallback\_OnError](capi-video-processing-types-h.md#oh_videoprocessingcallback_onerror)到回调对象。绑定完成之后，需要调用 [OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)，将回调对象注册到视频处理实例，才能使其生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md)\* callback | 指向回调对象的指针。 |
| [OH\_VideoProcessingCallback\_OnError](capi-video-processing-types-h.md#oh_videoprocessingcallback_onerror) onError | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果函数绑定成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果callback为空或者onError为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_VideoProcessingCallback\_BindOnState()

```c
VideoProcessing_ErrorCode OH_VideoProcessingCallback_BindOnState(VideoProcessing_Callback* callback,OH_VideoProcessingCallback_OnState onState)
```

**描述**

绑定回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)到回调对象。绑定完成之后，需要调用 [OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)，将回调对象注册到视频处理实例，才能使其生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md)\* callback | 指向回调对象的指针。 |
| [OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate) onState | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果函数绑定成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果callback为空或者onState为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |

### OH\_VideoProcessingCallback\_BindOnNewOutputBuffer()

```c
VideoProcessing_ErrorCode OH_VideoProcessingCallback_BindOnNewOutputBuffer(VideoProcessing_Callback* callback,OH_VideoProcessingCallback_OnNewOutputBuffer onNewOutputBuffer)
```

**描述**

绑定回调函数[OH\_VideoProcessingCallback\_OnNewOutputBuffer](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer)到回调对象。绑定完成之后，需要调用 [OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)，将回调对象注册到视频处理实例，才能使其生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md)\* callback | 指向回调对象的指针。 |
| [OH\_VideoProcessingCallback\_OnNewOutputBuffer](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer) onNewOutputBuffer | 回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | 如果函数绑定成功，返回VIDEO\_PROCESSING\_SUCCESS。  如果callback为空，返回VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER。 |
