---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-videoencoder-h
title: native_avcodec_videoencoder.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avcodec_videoencoder.h
category: harmonyos-references
scraped_at: 2026-04-29T14:02:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2a018cb104f5a3be985f994cbb99d46be49e7825e8a90dbffd3bbccfa09bf2dc
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于视频编码的接口。

**引用文件：** <multimedia/player\_framework/native\_avcodec\_videoencoder.h>

**库：** libnative\_media\_venc.so

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**相关模块：** [VideoEncoder](capi-videoencoder.md)

**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

接口在每个版本，对每种模式的支持情况说明，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/47Zb1WL5Q4-YBXTyG2I2jg/zh-cn_image_0000002558767380.png?HW-CC-KV=V1&HW-CC-Date=20260429T060243Z&HW-CC-Expire=86400&HW-CC-Sign=2F179A480BA68D789EEE50CFE91C414A938B566D9C95B342275EC4AF7D5960A4)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/2vLyqaXGQPeA61xC4zkhGg/zh-cn_image_0000002589327249.png?HW-CC-KV=V1&HW-CC-Date=20260429T060243Z&HW-CC-Expire=86400&HW-CC-Sign=74095C442A9413E17CFFC3DEF62144B0094218C05A04D4057A46E25E9185F746)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_VideoEncodeBitrateMode](capi-native-avcodec-videoencoder-h.md#oh_videoencodebitratemode) | OH\_VideoEncodeBitrateMode | 视频编码器的码率控制模式。(API14废弃) |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_VideoEncoder\_OnNeedInputParameter)(OH\_AVCodec \*codec, uint32\_t index, OH\_AVFormat \*parameter, void \*userData)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_onneedinputparameter) | OH\_VideoEncoder\_OnNeedInputParameter | 配置随帧参数，当需要设置index对应帧的编码参数时，可以通过该接口设置。只在Surface模式生效。 |
| [OH\_AVCodec \*OH\_VideoEncoder\_CreateByMime(const char \*mime)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_createbymime) | - | 根据MIME类型创建视频编码器实例，推荐使用。 |
| [OH\_AVCodec \*OH\_VideoEncoder\_CreateByName(const char \*name)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_createbyname) | - | 根据视频编码器名称创建视频编码器实例。使用此接口的前提是知道编码器的确切名称，编码器的名称可以通过能力查询获取。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Destroy(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_destroy) | - | 清理编码器内部资源，销毁编码器实例。不能重复销毁。 |
| [OH\_AVErrCode OH\_VideoEncoder\_SetCallback(OH\_AVCodec \*codec, OH\_AVCodecAsyncCallback callback, void \*userData)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_setcallback) | - | 设置OH\_AVCodecCallback回调函数，让应用可以响应视频编码器生成的事件。在调用OH\_VideoEncoder\_Prepare接口之前，必须调用此接口。(API11废弃) |
| [OH\_AVErrCode OH\_VideoEncoder\_RegisterCallback(OH\_AVCodec \*codec, OH\_AVCodecCallback callback, void \*userData)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_registercallback) | - | 注册OH\_AVCodecCallback回调函数，让应用可以响应视频编码器生成的事件。在调用OH\_VideoEncoder\_Prepare接口之前，必须调用此接口。 |
| [OH\_AVErrCode OH\_VideoEncoder\_RegisterParameterCallback(OH\_AVCodec \*codec, OH\_VideoEncoder\_OnNeedInputParameter onInputParameter, void \*userData)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_registerparametercallback) | - | 注册OH\_AVCodecCallback输入参数回调函数，让应用可以响应视频编码器生成的事件。编码Surface模式，需要设置随帧参数时，须使用该接口。  如果使用该接口，必须在[OH\_VideoEncoder\_Configure](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)之前调用该接口。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Configure(OH\_AVCodec \*codec, OH\_AVFormat \*format)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure) | - | 配置视频编码器的编码参数，通常需要配置输入视频帧的描述信息，如帧的宽、高、像素格式等。必须在调用OH\_VideoEncoder\_Prepare接口之前，调用此接口。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Prepare(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_prepare) | - | 准备编码器的内部资源，在OH\_VideoEncoder\_Configure接口后调用。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Start(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_start) | - | 调用[OH\_VideoEncoder\_Prepare](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_prepare)接口成功后调用此接口启动编码器。成功启动后，编码器将开始报告注册的回调事件。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Stop(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_stop) | - | 停止编码器，释放输入输出buffer。停止之后，可以通过调用OH\_VideoEncoder\_Start接口重新进入Running状态。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Flush(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_flush) | - | 清除编码器中缓存的输入和输出数据及参数集如H.264格式的PPS/SPS。  调用此接口后，以前通过异步回调上报的所有缓冲区index都将失效，请确保不要访问这些index对应的缓冲区。该接口不能连续调用。 |
| [OH\_AVErrCode OH\_VideoEncoder\_Reset(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_reset) | - | 重置编码器，编码器回到初始化状态。如果要继续编码，需要再次调用OH\_VideoEncoder\_Configure接口配置编码器实例。 |
| [OH\_AVFormat \*OH\_VideoEncoder\_GetOutputDescription(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputdescription) | - | 获取编码器输出数据的OH\_AVFormat信息。  需要注意的是，返回值指向的OH\_AVFormat实例的生命周期需要开发者通过调用接口[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)释放。 |
| [OH\_AVErrCode OH\_VideoEncoder\_SetParameter(OH\_AVCodec \*codec, OH\_AVFormat \*format)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_setparameter) | - | 在编码器运行时设置编码器参数。  注意，此接口只有在编码器启动后才能调用。同时，不正确的参数设置可能会导致编码失败。 |
| [OH\_AVErrCode OH\_VideoEncoder\_GetSurface(OH\_AVCodec \*codec, OHNativeWindow \*\*window)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getsurface) | - | 从视频编码器获取输入surface，必须在调用OH\_VideoEncoder\_Configure接口之后OH\_VideoEncoder\_Prepare接口之前调用此接口。 |
| [OH\_AVErrCode OH\_VideoEncoder\_FreeOutputData(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputdata) | - | 将处理后的输出缓冲区返回给编码器。(API11废弃) |
| [OH\_AVErrCode OH\_VideoEncoder\_NotifyEndOfStream(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_notifyendofstream) | - | 通知视频编码器输入流已结束。建议使用此接口进行通知。该接口只在Surface模式下使用，Buffer模式通过OH\_AVBuffer携带EOS信息，通知输入流的结束。 |
| [OH\_AVErrCode OH\_VideoEncoder\_PushInputData(OH\_AVCodec \*codec, uint32\_t index, OH\_AVCodecBufferAttr attr)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputdata) | - | 将填入数据的输入缓冲区提交给视频编码器。(API11废弃) |
| [OH\_AVErrCode OH\_VideoEncoder\_PushInputBuffer(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputbuffer) | - | Buffer模式下，将index对应的OH\_AVBuffer送入编码器编码。 |
| [OH\_AVErrCode OH\_VideoEncoder\_PushInputParameter(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputparameter) | - | Surface模式下，将index对应帧的编码参数送入编码器编码。 |
| [OH\_AVErrCode OH\_VideoEncoder\_FreeOutputBuffer(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputbuffer) | - | 将处理后的index对应的OH\_AVBuffer退回给编码器。开发者使用完需要及时调用此接口释放输出缓存区，否则会阻塞编码流程。 |
| [OH\_AVFormat \*OH\_VideoEncoder\_GetInputDescription(OH\_AVCodec \*codec)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputdescription) | - | 编码器接收到的图像的描述信息。调用[OH\_VideoEncoder\_Configure](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)后调用此接口。  需要注意的是，返回指针所指向的OH\_AVFormat实例的生命周期需要由开发者通过调用[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)接口释放。 |
| [OH\_AVErrCode OH\_VideoEncoder\_IsValid(OH\_AVCodec \*codec, bool \*isValid)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_isvalid) | - | 在编码器实例存在的情况下，检查当前编码器服务是否有效。 |
| [OH\_AVErrCode OH\_VideoEncoder\_QueryInputBuffer(struct OH\_AVCodec \*codec, uint32\_t \*index, int64\_t timeoutUs)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryinputbuffer) | - | 查询下一个可用输入缓冲区的索引。  调用此接口后需要接着调用[OH\_VideoEncoder\_GetInputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputbuffer)接口获取缓冲区实例，并通过[OH\_VideoEncoder\_PushInputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputbuffer)接口传递给编码器。  需要注意的是，上述操作仅在同步模式下支持。 |
| [OH\_AVBuffer \*OH\_VideoEncoder\_GetInputBuffer(struct OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputbuffer) | - | 获取可用输入缓冲区的实例。  需要注意的是，此接口仅适用于同步模式。 |
| [OH\_AVErrCode OH\_VideoEncoder\_QueryOutputBuffer(struct OH\_AVCodec \*codec, uint32\_t \*index, int64\_t timeoutUs)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryoutputbuffer) | - | 查询下一个可用输出缓冲区的索引。通过[OH\_VideoEncoder\_GetOutputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputbuffer)接口获取的缓冲区实例可以通过[OH\_VideoEncoder\_FreeOutputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputbuffer)接口将处理后的输出缓冲区返回到编码器。  需要注意的是，上述操作仅在同步模式下支持。 |
| [OH\_AVBuffer \*OH\_VideoEncoder\_GetOutputBuffer(struct OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputbuffer) | - | 获取可用输出缓冲区的实例。  需要注意的是，此接口仅适用于同步模式。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### OH\_VideoEncodeBitrateMode

PhonePC/2in1TabletTVWearable

```
1. enum OH_VideoEncodeBitrateMode
```

**描述**

视频编码器的码率控制模式。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**废弃版本：** 14

**替代接口：** [OH\_BitrateMode](capi-native-avcodec-base-h.md#oh_bitratemode)

| 枚举项 | 描述 |
| --- | --- |
| CBR = 0 | 恒定码率模式。  **替代接口：** [BITRATE\_MODE\_CBR](capi-native-avcodec-base-h.md#oh_bitratemode) |
| VBR = 1 | 可变码率模式。  **替代接口：** [BITRATE\_MODE\_VBR](capi-native-avcodec-base-h.md#oh_bitratemode) |
| CQ = 2 | 恒定QP模式。  **替代接口：** [BITRATE\_MODE\_CQ](capi-native-avcodec-base-h.md#oh_bitratemode) |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_VideoEncoder\_OnNeedInputParameter()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_VideoEncoder_OnNeedInputParameter)(OH_AVCodec *codec, uint32_t index, OH_AVFormat *parameter, void *userData)
```

**描述**

配置随帧参数，当需要设置index对应帧的编码参数时，可以通过该接口设置。只在Surface模式生效。

该接口只能在Surface模式下使用，使用前需要调用OH\_VideoEncoder\_RegisterParameterCallback接口注册。

在Buffer模式下，OH\_AVBuffer可以直接携带帧的编码参数，当前可以支持的随帧参数有帧级QPMin/QPMax，指定LTR设置参考帧。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 对应编码帧的index。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*parameter | 编码参数。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

### OH\_VideoEncoder\_CreateByMime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCodec *OH_VideoEncoder_CreateByMime(const char *mime)
```

**描述**

根据MIME类型创建视频编码器实例，推荐使用。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mime | MIME类型描述字符串，请参阅[AVCODEC\_MIME\_TYPE](capi-native-avcodec-base-h.md#变量)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \* | 成功则返回一个指向视频编码实例的指针。  如果输入为不支持的编码器类型或内存不足时，则返回NULL。 |

### OH\_VideoEncoder\_CreateByName()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCodec *OH_VideoEncoder_CreateByName(const char *name)
```

**描述**

根据视频编码器名称创建视频编码器实例。使用此接口的前提是知道编码器的确切名称，编码器的名称可以通过能力查询获取。

详情请参见：[获取支持的编解码能力](../harmonyos-guides/obtain-supported-codecs.md#创建指定名称的编解码器)。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 视频编码器名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \* | 成功则返回一个指向视频编码实例的指针。  如果输入是不支持编码器名称或者内存资源不足，则返回NULL。 |

### OH\_VideoEncoder\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Destroy(OH_AVCodec *codec)
```

**描述**

清理编码器内部资源，销毁编码器实例。不能重复销毁。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。 |

### OH\_VideoEncoder\_SetCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_SetCallback(OH_AVCodec *codec, OH_AVCodecAsyncCallback callback, void *userData)
```

**描述**

设置OH\_AVCodecCallback回调函数，让应用可以响应视频编码器生成的事件。在调用OH\_VideoEncoder\_Prepare接口之前，必须调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_VideoEncoder\_RegisterCallback](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_registercallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| [OH\_AVCodecAsyncCallback](capi-codecbase-oh-avcodecasynccallback.md) callback | 所有回调函数的集合。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。 |

### OH\_VideoEncoder\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_RegisterCallback(OH_AVCodec *codec, OH_AVCodecCallback callback, void *userData)
```

**描述**

注册OH\_AVCodecCallback回调函数，让应用可以响应视频编码器生成的事件。在调用OH\_VideoEncoder\_Prepare接口之前，必须调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| [OH\_AVCodecCallback](capi-codecbase-oh-avcodeccallback.md) callback | 所有回调函数的集合。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。 |

### OH\_VideoEncoder\_RegisterParameterCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_RegisterParameterCallback(OH_AVCodec *codec, OH_VideoEncoder_OnNeedInputParameter onInputParameter, void *userData)
```

**描述**

注册OH\_AVCodecCallback输入参数回调函数，让应用可以响应视频编码器生成的事件。编码Surface模式，需要设置随帧参数时，须使用该接口。

如果使用该接口，必须在[OH\_VideoEncoder\_Configure](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)之前调用该接口。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| [OH\_VideoEncoder\_OnNeedInputParameter](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_onneedinputparameter) onInputParameter | 输入参数回调指针。 |
| void \*userData | 开发者执行回调所依赖的数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：本接口必须在OH\_VideoEncoder\_Prepare接口前调用，如果在其他状态时调用，则返回此错误码。 |

### OH\_VideoEncoder\_Configure()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Configure(OH_AVCodec *codec, OH_AVFormat *format)
```

**描述**

配置视频编码器的编码参数，通常需要配置输入视频帧的描述信息，如帧的宽、高、像素格式等。必须在调用OH\_VideoEncoder\_Prepare接口之前，调用此接口。

该接口对配置参数进行合法性校验，部分非法参数不会强校验，使用默认值或直接丢弃。部分非法参数会强校验，具体规则如下：

以下参数的配置范围可通过[能力查询](../harmonyos-guides/obtain-supported-codecs.md)获取，OH\_MD\_KEY\_I\_FRAME\_INTERVAL暂不支持能力查询。

设置OH\_MD\_KEY\_VIDEO\_ENCODER\_ENABLE\_TEMPORAL\_SCALABILITY、OH\_MD\_KEY\_VIDEO\_ENCODER\_LTR\_FRAME\_COUNT参数时，如果当前平台不支持这些功能，该接口不会报错，而是继续按照正常编码流程执行。

参数校验：

| Key | 配置正常范围的值 | 配置超出范围的值 | 不配置该参数 |
| --- | --- | --- | --- |
| OH\_MD\_KEY\_WIDTH | AV\_ERR\_OK | AV\_ERR\_INVALID\_VAL | AV\_ERR\_INVALID\_VAL |
| OH\_MD\_KEY\_HEIGHT | AV\_ERR\_OK | AV\_ERR\_INVALID\_VAL | AV\_ERR\_INVALID\_VAL |
| OH\_MD\_KEY\_PIXEL\_FORMAT 请参阅[OH\_AVPixelFormat](capi-native-avformat-h.md#oh_avpixelformat) | AV\_ERR\_OK | AV\_ERR\_UNSUPPORT | AV\_ERR\_OK |
| OH\_MD\_KEY\_FRAME\_RATE | AV\_ERR\_OK | AV\_ERR\_INVALID\_VAL | AV\_ERR\_OK |
| OH\_MD\_KEY\_PROFILE 请参阅[OH\_MD\_KEY\_PROFILE](capi-native-avcodec-base-h.md#变量) | AV\_ERR\_OK | AV\_ERR\_INVALID\_VAL | AV\_ERR\_OK |
| OH\_MD\_KEY\_I\_FRAME\_INTERVAL | AV\_ERR\_OK | \ | AV\_ERR\_OK |

| OH\_MD\_KEY\_  BITRATE | OH\_MD\_KEY\_  QUALITY | OH\_MD\_KEY\_  VIDEO\_ENCODER\_BITRATE\_MODE | 返回值 | 说明 |
| --- | --- | --- | --- | --- |
| \ | \ | \ | AV\_ERR\_OK | 使用编码器默认值 |
| 超出范围 | 超出范围 | 不支持的模式 | AV\_ERR\_INVALID\_VAL | 异常值均报错 |
| 正常值 | 正常值 | \ | AV\_ERR\_INVALID\_VAL | Bitrate 与 Quality 冲突 |
| 正常值 | \ | \ | AV\_ERR\_OK | 使能默认码控模式 |
| 正常值 | \ | BITRATE\_MODE\_VBR、BITRATE\_MODE\_CBR | AV\_ERR\_OK | - |
| 正常值 | \ | BITRATE\_MODE\_CQ | AV\_ERR\_INVALID\_VAL | Bitrate 与 CQ 模式冲突 |
| \ | 正常值 | \ | AV\_ERR\_OK | 使能 CQ 模式 |
| \ | 正常值 | BITRATE\_MODE\_CQ | AV\_ERR\_OK | - |
| \ | 正常值 | BITRATE\_MODE\_VBR、BITRATE\_MODE\_CBR | AV\_ERR\_INVALID\_VAL | Quality 与 VBR、CBR 模式冲突 |
| \ | \ | BITRATE\_MODE\_VBR、BITRATE\_MODE\_CBR | AV\_ERR\_OK | 使用编码器默认码率 |
| \ | \ | BITRATE\_MODE\_CQ | AV\_ERR\_OK | 使用默认quality |

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat的指针，用于给出要编码的视频轨的描述。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：1. 输入的codec指针为非编码器实例，或者为空指针；2. 输入format参数不支持。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：本接口必须在OH\_VideoEncoder\_Prepare接口前调用，如果在其他状态时调用，则返回此错误码。 |

### OH\_VideoEncoder\_Prepare()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Prepare(OH_AVCodec *codec)
```

**描述**

准备编码器的内部资源，在OH\_VideoEncoder\_Configure接口后调用。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_Start()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Start(OH_AVCodec *codec)
```

**描述**

调用[OH\_VideoEncoder\_Prepare](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_prepare)接口成功后调用此接口启动编码器。成功启动后，编码器将开始报告注册的回调事件。

Surface模式下，在surface中有正确的输入后，每完成一帧编码会触发OnNewOutputBuffer。

Buffer模式下，编码器会立即触发输入回调，开发者每完成一次输入，编码器执行编码，每完成一帧编码会触发OnNewOutputBuffer。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Stop(OH_AVCodec *codec)
```

**描述**

停止编码器，释放输入输出buffer。停止之后，可以通过调用OH\_VideoEncoder\_Start接口重新进入Running状态。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_Flush()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Flush(OH_AVCodec *codec)
```

**描述**

清除编码器中缓存的输入和输出数据及参数集如H.264格式的PPS/SPS。

调用此接口后，以前通过异步回调上报的所有缓冲区index都将失效，请确保不要访问这些index对应的缓冲区。该接口不能连续调用。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_Reset()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_Reset(OH_AVCodec *codec)
```

**描述**

重置编码器，编码器回到初始化状态。如果要继续编码，需要再次调用OH\_VideoEncoder\_Configure接口配置编码器实例。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。 |

### OH\_VideoEncoder\_GetOutputDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_VideoEncoder_GetOutputDescription(OH_AVCodec *codec)
```

**描述**

获取编码器输出数据的OH\_AVFormat信息。

需要注意的是，返回值指向的OH\_AVFormat实例的生命周期需要开发者通过调用接口[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)释放。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \* | 返回指向OH\_AVFormat实例的指针。  当输入的codec指针非编码实例，或者为空指针，则返回NULL。 |

### OH\_VideoEncoder\_SetParameter()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_SetParameter(OH_AVCodec *codec, OH_AVFormat *format)
```

**描述**

在编码器运行时设置编码器参数。

注意，此接口只有在编码器启动后才能调用。同时，不正确的参数设置可能会导致编码失败。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：1. 输入的codec指针为非编码器实例，或者为空指针；2. 输入format参数不支持。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_GetSurface()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_GetSurface(OH_AVCodec *codec, OHNativeWindow **window)
```

**描述**

从视频编码器获取输入surface，必须在调用OH\_VideoEncoder\_Configure接口之后OH\_VideoEncoder\_Prepare接口之前调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| [OHNativeWindow](capi-nativewindow-nativewindow.md) \*\*window | 指向OHNativeWindow实例的指针。应用负责管理window的生命周期，结束时调用[OH\_NativeWindow\_DestroyNativeWindow](capi-external-window-h.md#oh_nativewindow_destroynativewindow)释放。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。 |

### OH\_VideoEncoder\_FreeOutputData()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_FreeOutputData(OH_AVCodec *codec, uint32_t index)
```

**描述**

将处理后的输出缓冲区返回给编码器。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_VideoEncoder\_FreeOutputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputbuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输出缓冲区对应的索引值。由[OH\_AVCodecOnNewOutputData](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputdata)给出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_NotifyEndOfStream()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_NotifyEndOfStream(OH_AVCodec *codec)
```

**描述**

通知视频编码器输入流已结束。建议使用此接口进行通知。该接口只在Surface模式下使用，Buffer模式通过OH\_AVBuffer携带EOS信息，通知输入流的结束。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 9

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_PushInputData()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_PushInputData(OH_AVCodec *codec, uint32_t index, OH_AVCodecBufferAttr attr)
```

**描述**

将填入数据的输入缓冲区提交给视频编码器。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_VideoEncoder\_PushInputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputbuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输入缓冲区对应的索引值。由[OH\_AVCodecOnNeedInputData](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata)给出。 |
| [OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) attr | 缓冲区中包含数据的描述信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_PushInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_PushInputBuffer(OH_AVCodec *codec, uint32_t index)
```

**描述**

Buffer模式下，将index对应的OH\_AVBuffer送入编码器编码。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输入缓冲区对应的索引值。由[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)给出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：1. 输入的codec指针为非编码器实例，或者为空指针；2. 输入format参数不支持。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_PushInputParameter()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_PushInputParameter(OH_AVCodec *codec, uint32_t index)
```

**描述**

Surface模式下，将index对应帧的编码参数送入编码器编码。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输入参数缓冲区对应的索引值。由[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)给出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_FreeOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_FreeOutputBuffer(OH_AVCodec *codec, uint32_t index)
```

**描述**

将处理后的index对应的OH\_AVBuffer退回给编码器。开发者使用完需要及时调用此接口释放输出缓存区，否则会阻塞编码流程。

详情请参见：[视频编码](../harmonyos-guides/video-encoding.md) “Surface模式的步骤-13或Buffer模式步骤-11”。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输出缓冲区对应的索引值。由[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)给出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码实例内部异常，如内部出现异常空指针。  AV\_ERR\_INVALID\_VAL：  1. 输入的 codec 指针为非编码器实例，或者为空指针；  2. 输入format参数不支持；  3. index非法或者连续给同一个index，该错误不影响后续编码流程。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_OPERATE\_NOT\_PERMIT：内部执行错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。 |

### OH\_VideoEncoder\_GetInputDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_VideoEncoder_GetInputDescription(OH_AVCodec *codec)
```

**描述**

编码器接收到的图像的描述信息。调用[OH\_VideoEncoder\_Configure](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_configure)后调用此接口。

需要注意的是，返回指针所指向的OH\_AVFormat实例的生命周期需要由开发者通过调用[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)接口释放。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \* | 返回指向OH\_AVFormat实例的指针。  当codec指针非编码实例，或者为空指针，则返回NULL。 |

### OH\_VideoEncoder\_IsValid()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_IsValid(OH_AVCodec *codec, bool *isValid)
```

**描述**

在编码器实例存在的情况下，检查当前编码器服务是否有效。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| bool \*isValid | 输出参数，指向布尔类型的指针。只有当接口返回AV\_ERR\_OK时，该值表示编码器服务的有效性（true为有效，false为无效）。建议开发者将isValid初始化为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。 |

### OH\_VideoEncoder\_QueryInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_QueryInputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs)
```

**描述**

查询下一个可用输入缓冲区的索引。

调用此接口后需要接着调用[OH\_VideoEncoder\_GetInputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getinputbuffer)接口获取缓冲区实例，并通过[OH\_VideoEncoder\_PushInputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_pushinputbuffer)接口传递给编码器。

需要注意的是，上述操作仅在同步模式下支持。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t \*index | 输入buffer对应的索引值。 |
| int64\_t timeoutUs | 超时时长，单位为微秒。负值：无限等待；0：立即退出；正值：等待指定时长后退出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码器实例已经销毁。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。  AV\_ERR\_OPERATE\_NOT\_PERMIT：禁止异步模式下使用。  AV\_ERR\_TRY\_AGAIN\_LATER：查询失败，建议等待短暂间隔后重试。 |

### OH\_VideoEncoder\_GetInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVBuffer *OH_VideoEncoder_GetInputBuffer(struct OH_AVCodec *codec, uint32_t index)
```

**描述**

获取可用输入缓冲区的实例。

需要注意的是，此接口仅适用于同步模式。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输入buffer对应的索引值，可通过[OH\_VideoEncoder\_QueryInputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryinputbuffer) 接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \* | 如果执行成功，则返回一个指向OH\_AVBuffer实例的指针，否则返回NULL。 |

### OH\_VideoEncoder\_QueryOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_VideoEncoder_QueryOutputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs)
```

**描述**

查询下一个可用输出缓冲区的索引。通过[OH\_VideoEncoder\_GetOutputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputbuffer)接口获取的缓冲区实例可以通过[OH\_VideoEncoder\_FreeOutputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_freeoutputbuffer)接口将处理后的输出缓冲区返回到编码器。

需要注意的是，上述操作仅在同步模式下支持。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t \*index | 输出buffer对应的索引值。 |
| int64\_t timeoutUs | 超时时长，单位为微秒。负值：无限等待；0：立即退出；正值：等待指定时长后退出。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_NO\_MEMORY：输入的编码器实例已经销毁。  AV\_ERR\_INVALID\_VAL：输入的codec指针为非编码器实例，或者为空指针。  AV\_ERR\_UNKNOWN：未知错误。  AV\_ERR\_INVALID\_STATE：当前编码器状态不支持调用本接口。  AV\_ERR\_OPERATE\_NOT\_PERMIT：禁止异步模式下使用。  AV\_ERR\_STREAM\_CHANGED：流格式已变更，可以通过调用[OH\_VideoEncoder\_GetOutputDescription](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_getoutputdescription)接口获取新的流信息。  AV\_ERR\_TRY\_AGAIN\_LATER：查询失败，建议等待短暂间隔后重试。 |

### OH\_VideoEncoder\_GetOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVBuffer *OH_VideoEncoder_GetOutputBuffer(struct OH_AVCodec *codec, uint32_t index)
```

**描述**

获取可用输出缓冲区的实例。

需要注意的是，此接口仅适用于同步模式。

**系统能力：** SystemCapability.Multimedia.Media.VideoEncoder

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向视频编码实例的指针。 |
| uint32\_t index | 输出buffer对应的索引值，可通过[OH\_VideoEncoder\_QueryOutputBuffer](capi-native-avcodec-videoencoder-h.md#oh_videoencoder_queryoutputbuffer)接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \* | 如果执行成功，则返回一个指向OH\_AVBuffer实例的指针，否则返回NULL。 |
