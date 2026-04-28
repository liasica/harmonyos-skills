---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audioencoder-h
title: native_avcodec_audioencoder.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 已停止维护的接口 > 头文件 > native_avcodec_audioencoder.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:13+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f88bb7d8bd2048d6e1bfad04b00192f4333c84dbbb7cc9d49b047fca700511ac
---

## 概述

PhonePC/2in1TabletTVWearable

音频编码Native API的声明。

**引用文件：** <multimedia/player\_framework/native\_avcodec\_audioencoder.h>

**库：** libnative\_media\_aenc.so

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代建议：** 当前模块下的接口均已废弃，开发者可使用[native\_avcodec\_audiocodec.h](capi-native-avcodec-audiocodec-h.md)完成对应功能开发，单个接口的替代关系可查阅具体的接口说明。

**相关模块：** [AudioEncoder](capi-audioencoder.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVCodec \*OH\_AudioEncoder\_CreateByMime(const char \*mime)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_createbymime) | 根据MIME类型创建音频编码器实例，大多数场景下建议使用此方式。(API11废弃) |
| [OH\_AVCodec \*OH\_AudioEncoder\_CreateByName(const char \*name)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_createbyname) | 通过音频编码器名称创建音频编码器实例，使用此接口的前提是知道编码器的确切名称。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Destroy(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_destroy) | 清理编码器内部资源，销毁编码器实例。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_SetCallback(OH\_AVCodec \*codec, OH\_AVCodecAsyncCallback callback, void \*userData)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_setcallback) | 设置异步回调函数，使应用可以响应音频编码器生成的事件。在调用Prepare之前，必须调用此接口。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Configure(OH\_AVCodec \*codec, OH\_AVFormat \*format)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_configure) | 要配置音频编码器，通常需要配置编码后的音轨的描述信息。在调用Prepare之前，必须调用此接口。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Prepare(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_prepare) | 准备编码器的内部资源，在调用此接口之前必须调用Configure接口。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Start(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_start) | 调用此接口启动编码器，在Prepare成功后执行。启动后，编码器将开始上报OH\_AVCodecOnNeedInputData事件。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Stop(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_stop) | 停止编码器。停止后，您可以通过Start重新进入已启动状态。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Flush(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_flush) | 清除编码器中缓存的输入和输出数据。  调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_Reset(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_reset) | 重置编码器。如果要继续编码，需要再次调用Configure接口配置编码器实例。(API11废弃) |
| [OH\_AVFormat \*OH\_AudioEncoder\_GetOutputDescription(OH\_AVCodec \*codec)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_getoutputdescription) | 获取编码器输出数据的描述信息。需要注意的是，返回值所指向的OH\_AVFormat实例的生命周期需要调用者手动释放。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_SetParameter(OH\_AVCodec \*codec, OH\_AVFormat \*format)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_setparameter) | 配置编码器的动态参数。  注意：该接口必须在编码器启动后才能调用。另外，参数配置错误可能会导致编码失败。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_PushInputData(OH\_AVCodec \*codec, uint32\_t index, OH\_AVCodecBufferAttr attr)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_pushinputdata) | 通知音频编码器已完成对index所对应缓冲区进行输入数据的填充。  [OH\_AVCodecOnNeedInputData](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata)回调将报告可用的输入缓冲区和相应的索引值。一旦具有指定索引的缓冲区提交到音频编码器，则无法再次访问此缓冲区，直到再次收到[OH\_AVCodecOnNeedInputData](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata)回调，收到相同索引时此缓冲区才可使用。  此外，对于某些编码器，需要在开始时向编码器输入特定配置参数，以初始化编码器的编码过程。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_FreeOutputData(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_freeoutputdata) | 将处理后的输出缓冲区返回给编码器。(API11废弃) |
| [OH\_AVErrCode OH\_AudioEncoder\_IsValid(OH\_AVCodec \*codec, bool \*isValid)](capi-native-avcodec-audioencoder-h.md#oh_audioencoder_isvalid) | 检查当前编码器实例是否有效，可用于后台故障恢复或应用程序从后台恢复时检测编码器有效状态。(API11废弃) |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioEncoder\_CreateByMime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCodec *OH_AudioEncoder_CreateByMime(const char *mime)
```

**描述**

根据MIME类型创建音频编码器实例，大多数场景下建议使用此方式。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_CreateByMime](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_createbymime)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mime | mime类型描述字符串，请参阅[AVCODEC\_MIMETYPE](capi-native-avcodec-base-h.md#变量)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCodec \*](capi-codecbase-oh-avcodec.md) | 返回指向OH\_AVCodec实例的指针。 |

### OH\_AudioEncoder\_CreateByName()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCodec *OH_AudioEncoder_CreateByName(const char *name)
```

**描述**

通过音频编码器名称创建音频编码器实例，使用此接口的前提是知道编码器的确切名称。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_CreateByName](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_createbyname)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 音频编码器名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCodec \*](capi-codecbase-oh-avcodec.md) | 返回指向OH\_AVCodec实例的指针。 |

### OH\_AudioEncoder\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Destroy(OH_AVCodec *codec)
```

**描述**

清理编码器内部资源，销毁编码器实例。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Destroy](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_destroy)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_SetCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_SetCallback(OH_AVCodec *codec, OH_AVCodecAsyncCallback callback, void *userData)
```

**描述**

设置异步回调函数，使应用可以响应音频编码器生成的事件。在调用Prepare之前，必须调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_RegisterCallback](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_registercallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| [OH\_AVCodecAsyncCallback](capi-codecbase-oh-avcodecasynccallback.md) callback | 所有回调函数的集合。 |
| void \*userData | 用户特定数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_Configure()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Configure(OH_AVCodec *codec, OH_AVFormat *format)
```

**描述**

要配置音频编码器，通常需要配置编码后的音轨的描述信息。在调用Prepare之前，必须调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Configure](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_configure)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat的指针，给出要编码的音频轨道的描述。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_Prepare()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Prepare(OH_AVCodec *codec)
```

**描述**

准备编码器的内部资源，在调用此接口之前必须调用Configure接口。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Prepare](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_prepare)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_Start()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Start(OH_AVCodec *codec)
```

**描述**

调用此接口启动编码器，在Prepare成功后执行。启动后，编码器将开始上报OH\_AVCodecOnNeedInputData事件。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Start](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_start)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Stop(OH_AVCodec *codec)
```

**描述**

停止编码器。停止后，您可以通过Start重新进入已启动状态。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Stop](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_stop)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_Flush()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Flush(OH_AVCodec *codec)
```

**描述**

清除编码器中缓存的输入和输出数据。

调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Flush](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_flush)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_Reset()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_Reset(OH_AVCodec *codec)
```

**描述**

重置编码器。如果要继续编码，需要再次调用Configure接口配置编码器实例。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_Reset](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_reset)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_GetOutputDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AudioEncoder_GetOutputDescription(OH_AVCodec *codec)
```

**描述**

获取编码器输出数据的描述信息。需要注意的是，返回值所指向的OH\_AVFormat实例的生命周期需要调用者手动释放。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_GetOutputDescription](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputdescription)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVFormat](capi-core-oh-avformat.md) \* | 返回OH\_AVFormat句柄指针，生命周期将使用下一个GetOutputDescription刷新，或使用OH\_AVCodec销毁。 |

### OH\_AudioEncoder\_SetParameter()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_SetParameter(OH_AVCodec *codec, OH_AVFormat *format)
```

**描述**

配置编码器的动态参数。

注意：该接口必须在编码器启动后才能调用。另外，参数配置错误可能会导致编码失败。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_SetParameter](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_setparameter)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| [OH\_AVFormat](capi-core-oh-avformat.md) \*format | OH\_AVFormat句柄指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_PushInputData()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_PushInputData(OH_AVCodec *codec, uint32_t index, OH_AVCodecBufferAttr attr)
```

**描述**

通知音频编码器已完成对index所对应缓冲区进行输入数据的填充。

[OH\_AVCodecOnNeedInputData](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata)回调将报告可用的输入缓冲区和相应的索引值。一旦具有指定索引的缓冲区提交到音频编码器，则无法再次访问此缓冲区，直到再次收到[OH\_AVCodecOnNeedInputData](capi-native-avcodec-base-h.md#oh_avcodeconneedinputdata)回调，收到相同索引时此缓冲区才可使用。

此外，对于某些编码器，需要在开始时向编码器输入特定配置参数，以初始化编码器的编码过程。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_PushInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_pushinputbuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t index | 输入缓冲区Buffer对应的索引值。 |
| [OH\_AVCodecBufferAttr](capi-core-oh-avcodecbufferattr.md) attr | 描述缓冲区中包含的数据的信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_FreeOutputData()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_FreeOutputData(OH_AVCodec *codec, uint32_t index)
```

**描述**

将处理后的输出缓冲区返回给编码器。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_FreeOutputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_freeoutputbuffer)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t index | 输出缓冲区Buffer对应的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |

### OH\_AudioEncoder\_IsValid()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioEncoder_IsValid(OH_AVCodec *codec, bool *isValid)
```

**描述**

检查当前编码器实例是否有效，可用于后台故障恢复或应用程序从后台恢复时检测编码器有效状态。

**系统能力：** SystemCapability.Multimedia.Media.AudioEncoder

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [OH\_AudioCodec\_IsValid](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_isvalid)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| bool \*isValid | 指向布尔类型的指针，true：编码器实例有效，false：编码器实例无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | 如果执行成功，则返回AV\_ERR\_OK，否则返回特定错误代码。 |
