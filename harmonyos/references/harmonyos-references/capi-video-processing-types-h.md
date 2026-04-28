---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-video-processing-types-h
title: video_processing_types.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > video_processing_types.h
category: harmonyos-references
scraped_at: 2026-04-28T08:13:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6b1c48b89aa38439a014249d2a9e6d4b0211c866844440b2c60247b81f2b3219
---

## 概述

PhonePC/2in1TabletTV

视频处理类型定义。

**引用文件：** <multimedia/video\_processing\_engine/video\_processing\_types.h>

**库：** libvideo\_processing.so

**系统能力：** SystemCapability.Multimedia.VideoProcessingEngine

**起始版本：** 12

**相关模块：** [VideoProcessing](capi-videoprocessing.md)

## 汇总

PhonePC/2in1TabletTV

### 结构体

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [VideoProcessing\_ColorSpaceInfo](api-videoprocessing-videoprocessing-colorspaceinfo.md) | VideoProcessing\_ColorSpaceInfo | 视频颜色空间信息数据结构。 |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md) | OH\_VideoProcessing | 定义视频处理对象。  定义一个OH\_VideoProcessing空指针，调用[OH\_VideoProcessing\_Create](capi-video-processing-h.md#oh_videoprocessing_create)创建视频处理实例，该指针在创建实例之前必须为空。用户可以对不同的处理类型创建不同的视频处理实例。 |
| [NativeWindow](capi-videoprocessing-nativewindow.md) | OHNativeWindow | 定义NativeWindow对象。 |
| [OH\_AVFormat](capi-videoprocessing-oh-avformat.md) | OH\_AVFormat | 定义OH\_AVFormat对象。 |
| [VideoProcessing\_Callback](capi-videoprocessing-videoprocessing-callback.md) | VideoProcessing\_Callback | 视频处理回调对象类型。  定义一个VideoProcessing\_Callback空指针，调用[OH\_VideoProcessingCallback\_Create](capi-video-processing-h.md#oh_videoprocessingcallback_create)来创建一个回调对象。创建之前该指针必须为空。通过调用[OH\_VideoProcessing\_RegisterCallback](capi-video-processing-h.md#oh_videoprocessing_registercallback)来向视频处理实例注册回调对象。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [VideoDetailEnhancer\_QualityLevel](capi-video-processing-types-h.md#videodetailenhancer_qualitylevel) | VideoDetailEnhancer\_QualityLevel | 用于细节增强的质量等级。 |
| [VideoMetadataGeneratorStyleControl](capi-video-processing-types-h.md#videometadatageneratorstylecontrol) | VideoMetadataGeneratorStyleControl | 视频元数据生成的风格模式。参数的具体取值请参考[VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL](capi-video-processing-types-h.md#变量)。 |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) | VideoProcessing\_ErrorCode | 视频处理错误码。 |
| [VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state) | VideoProcessing\_State | 视频处理状态。  视频处理状态通过回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)进行报告。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_VideoProcessingCallback\_OnError)(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_ErrorCode error, void\* userData)](capi-video-processing-types-h.md#oh_videoprocessingcallback_onerror) | OH\_VideoProcessingCallback\_OnError | 视频处理过程中报告错误的回调函数指针。  错误码[VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode)：VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING，不支持的处理，比如不支持输入输出的颜色空间类型转换。  VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE，无效的视频属性，比如视频的颜色空间无效。  VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY，内存不足。  VIDEO\_PROCESSING\_ERROR\_PROCESS\_FAILED，处理过程中出错。 |
| [typedef void (\*OH\_VideoProcessingCallback\_OnState)(OH\_VideoProcessing\* videoProcessor, VideoProcessing\_State state, void\* userData)](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate) | OH\_VideoProcessingCallback\_OnState | 报告视频处理状态的回调函数指针。  [OH\_VideoProcessing\_Start](capi-video-processing-h.md#oh_videoprocessing_start)成功调用之后状态会变为[VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_RUNNING。调用[OH\_VideoProcessing\_Stop](capi-video-processing-h.md#oh_videoprocessing_stop)，所有的缓存buffer处理完成后，状态会变为[VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_STOPPED。 |
| [typedef void (\*OH\_VideoProcessingCallback\_OnNewOutputBuffer)(OH\_VideoProcessing\* videoProcessor, uint32\_t index, void\* userData)](capi-video-processing-types-h.md#oh_videoprocessingcallback_onnewoutputbuffer) | OH\_VideoProcessingCallback\_OnNewOutputBuffer | 报告输出buffer已填充好数据的回调函数指针。  每个新输出buffer填充好数据之后该buffer的索引就会报告给用户。调用[OH\_VideoProcessing\_RenderOutputBuffer](capi-video-processing-h.md#oh_videoprocessing_renderoutputbuffer)根据索引来处理渲染并输出该buffer。如果未注册该函数，则输出buffer填充好数据后不会报告用户，而是直接进行处理渲染并输出。 |

### 变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| const int32\_t VIDEO\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION | 表示创建颜色空间转换视频处理实例。  调用[OH\_VideoProcessing\_Create](capi-video-processing-h.md#oh_videoprocessing_create)创建颜色空间转换视频处理实例，如果不支持该能力返回[VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode).VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  **起始版本：** 12 |
| const int32\_t VIDEO\_PROCESSING\_TYPE\_METADATA\_GENERATION | 表示创建元数据生成视频处理实例。  调用[OH\_VideoProcessing\_Create](capi-video-processing-h.md#oh_videoprocessing_create)创建元数据生成视频处理实例，如果不支持该能力返回[VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode).VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  **起始版本：** 12 |
| const int32\_t VIDEO\_PROCESSING\_TYPE\_DETAIL\_ENHANCER | 表示创建细节增强视频处理实例。  调用[OH\_VideoProcessing\_Create](capi-video-processing-h.md#oh_videoprocessing_create)创建细节增强视频处理实例，如果不支持该能力返回[VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode).VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING。  **起始版本：** 12 |
| const char\* VIDEO\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL | 指定视频细节增强的质量等级，参考[VideoDetailEnhancer\_QualityLevel](capi-video-processing-types-h.md#videodetailenhancer_qualitylevel)查看具体取值。  调用[OH\_VideoProcessing\_SetParameter](capi-video-processing-h.md#oh_videoprocessing_setparameter)设置质量等级。  调用[OH\_VideoProcessing\_GetParameter](capi-video-processing-h.md#oh_videoprocessing_getparameter)获取当前质量等级。  **起始版本：** 12 |
| const char \* VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL | 指定视频元数据生成的风格模式。具体取值请参考[VideoMetadataGeneratorStyleControl](capi-video-processing-types-h.md#videometadatageneratorstylecontrol)。调用[OH\_AVFormat\_SetIntValue](capi-native-avformat-h.md#oh_avformat_setintvalue)设置视频元数据生成的风格模式到AVFormat参数。调用[OH\_VideoProcessing\_SetParameter](capi-video-processing-h.md#oh_videoprocessing_setparameter)设置当前视频元数据生成的风格模式。调用[OH\_VideoProcessing\_GetParameter](capi-video-processing-h.md#oh_videoprocessing_getparameter)获取当前视频元数据生成的风格模式。  **起始版本：** 22 |

## 枚举类型说明

PhonePC/2in1TabletTV

### VideoDetailEnhancer\_QualityLevel

PhonePC/2in1TabletTV

```
1. enum VideoDetailEnhancer_QualityLevel
```

**描述**

用于细节增强的质量等级。参数[VIDEO\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL](capi-video-processing-types-h.md#变量)的具体取值，设置方法详见开发指南。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_NONE | 无细节增强。 |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_LOW | 低质量等级细节增强，速度较快，默认设置。 |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_MEDIUM | 中等质量等级细节增强，速度适中。 |
| VIDEO\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_HIGH | 高质量等级细节增强，速度相对较慢。 |

**参考：**

[OH\_VideoProcessing\_SetParameter](capi-video-processing-h.md#oh_videoprocessing_setparameter)

[OH\_VideoProcessing\_GetParameter](capi-video-processing-h.md#oh_videoprocessing_getparameter)

### VideoMetadataGeneratorStyleControl

PhonePC/2in1TabletTV

```
1. enum VideoMetadataGeneratorStyleControl
```

**描述**

视频元数据生成的风格模式。参数的具体取值请参考[VIDEO\_METADATA\_GENERATOR\_STYLE\_CONTROL](capi-video-processing-types-h.md#变量)。

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_METADATA\_GENERATOR\_CONTRAST\_MODE = 0 | 对比度优先模式。 |
| VIDEO\_METADATA\_GENERATOR\_BRIGHT\_MODE = 1 | 亮度优先模式。 |

**参考：**

[OH\_VideoProcessing\_SetParameter](capi-video-processing-h.md#oh_videoprocessing_setparameter)

[OH\_VideoProcessing\_GetParameter](capi-video-processing-h.md#oh_videoprocessing_getparameter)

[OH\_AVFormat\_SetIntValue](capi-native-avformat-h.md#oh_avformat_setintvalue)

### VideoProcessing\_ErrorCode

PhonePC/2in1TabletTV

```
1. enum VideoProcessing_ErrorCode
```

**描述**

视频处理错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_PROCESSING\_SUCCESS | 处理成功。 |
| VIDEO\_PROCESSING\_ERROR\_INVALID\_PARAMETER = 401 | 输入参数无效。以下情况都会返回该错误码：  1. 无效的输入或输出视频buffer，视频buffer为空。  2. 无效的参数，参数为空。  3. 无效的处理类型。 |
| VIDEO\_PROCESSING\_ERROR\_UNKNOWN = 29210001 | 未知错误，比如GPU计算失败或memcpy失败。 |
| VIDEO\_PROCESSING\_ERROR\_INITIALIZE\_FAILED | 视频处理全局环境初始化失败，比如初始化GPU环境失败。 |
| VIDEO\_PROCESSING\_ERROR\_CREATE\_FAILED | 创建视频处理实例失败，比如实例总数超出上限。 |
| VIDEO\_PROCESSING\_ERROR\_PROCESS\_FAILED | 处理过程失败，比如处理时间超时。 |
| VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING | 不支持的处理类型，可以调用OH\_VideoProcessing\_IsXXXSupported来检查是否支持这种处理。 |
| VIDEO\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED | 不允许的操作，比如不满足调用接口所需的运行状态下调用该接口。 |
| VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY | 内存不足。 |
| VIDEO\_PROCESSING\_ERROR\_INVALID\_INSTANCE | 视频处理实例无效，比如视频处理实例为空实例。 |
| VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE | 输入值无效，以下情况都会造成这种错误：  1. 视频buffer宽高太大或者颜色空间错误。  2. 参数包含无效的值，比如细节增强的质量等级错误。 |

### VideoProcessing\_State

PhonePC/2in1TabletTV

```
1. enum VideoProcessing_State
```

**描述**

视频处理状态。视频处理状态通过回调函数[OH\_VideoProcessingCallback\_OnState](capi-video-processing-types-h.md#oh_videoprocessingcallback_onstate)进行报告。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| VIDEO\_PROCESSING\_STATE\_RUNNING | 视频处理进行中。 |
| VIDEO\_PROCESSING\_STATE\_STOPPED | 视频处理已停止。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_VideoProcessingCallback\_OnError()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_VideoProcessingCallback_OnError)(OH_VideoProcessing* videoProcessor, VideoProcessing_ErrorCode error, void* userData)
```

**描述**

视频处理过程中报告错误的回调函数指针。

错误码[VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode)：

VIDEO\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING，不支持的处理，比如不支持输入输出的颜色空间类型转换。

VIDEO\_PROCESSING\_ERROR\_INVALID\_VALUE，无效的视频属性，比如视频的颜色空间无效。

VIDEO\_PROCESSING\_ERROR\_NO\_MEMORY，内存不足。

VIDEO\_PROCESSING\_ERROR\_PROCESS\_FAILED，处理过程中出错。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 视频处理实例。 |
| [VideoProcessing\_ErrorCode](capi-video-processing-types-h.md#videoprocessing_errorcode) error | 报告给用户的错误码。 |
| void\* userData | 用户的自定义数据。 |

### OH\_VideoProcessingCallback\_OnState()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_VideoProcessingCallback_OnState)(OH_VideoProcessing* videoProcessor, VideoProcessing_State state, void* userData)
```

**描述**

报告视频处理状态的回调函数指针。

[OH\_VideoProcessing\_Start](capi-video-processing-h.md#oh_videoprocessing_start)成功调用之后状态会变为[VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_RUNNING。调用[OH\_VideoProcessing\_Stop](capi-video-processing-h.md#oh_videoprocessing_stop)，所有的缓存buffer处理完成后，状态会变为[VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state).VIDEO\_PROCESSING\_STATE\_STOPPED。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 视频处理实例。 |
| [VideoProcessing\_State](capi-video-processing-types-h.md#videoprocessing_state) state | 视频处理状态。 |
| void\* userData | 用户的自定义数据。 |

### OH\_VideoProcessingCallback\_OnNewOutputBuffer()

PhonePC/2in1TabletTV

```
1. typedef void (*OH_VideoProcessingCallback_OnNewOutputBuffer)(OH_VideoProcessing* videoProcessor, uint32_t index, void* userData)
```

**描述**

报告输出buffer已填充好数据的回调函数指针。

每个新输出buffer填充好数据之后该buffer的索引就会报告给用户。调用[OH\_VideoProcessing\_RenderOutputBuffer](capi-video-processing-h.md#oh_videoprocessing_renderoutputbuffer)根据索引来处理渲染并输出该buffer。如果未注册该函数，则输出buffer填充好数据后不会报告用户，而是直接进行处理渲染并输出。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_VideoProcessing](capi-videoprocessing-oh-videoprocessing.md)\* videoProcessor | 视频处理实例。 |
| uint32\_t index | 新输出buffer的索引。 |
| void\* userData | 用户自定义的数据。 |
