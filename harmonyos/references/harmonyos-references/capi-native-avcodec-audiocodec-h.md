---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-avcodec-audiocodec-h
title: native_avcodec_audiocodec.h
breadcrumb: API参考 > 媒体 > AVCodec Kit（音视频编解码服务） > C API > 头文件 > native_avcodec_audiocodec.h
category: harmonyos-references
scraped_at: 2026-04-28T08:12:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:487392e4a0224df6a83fd8306aeb9540b5bc94f7a15639ed4cc1adbfe2c9383f
---

## 概述

PhonePC/2in1TabletTVWearable

音频编解码Native API的声明。

**引用文件：** <multimedia/player\_framework/native\_avcodec\_audiocodec.h>

**库：** libnative\_media\_acodec.so

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**相关模块：** [AudioCodec](capi-audiocodec.md)

**相关示例：** [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [MediaKeySession](capi-drm-mediakeysession.md) | MediaKeySession | MediaKeySession字段。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVCodec \*OH\_AudioCodec\_CreateByMime(const char \*mime, bool isEncoder)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_createbymime) | 根据MIME类型创建音频编解码器实例，大多数场景下建议使用此方式。 |
| [OH\_AVCodec \*OH\_AudioCodec\_CreateByName(const char \*name)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_createbyname) | 通过音频编解码器名称创建音频编解码器实例，使用此接口的前提是知道编解码器的确切名称，编解码器的名称可以通过[OH\_AVCapability\_GetName](capi-native-avcapability-h.md#oh_avcapability_getname)获取。 |
| [OH\_AVErrCode OH\_AudioCodec\_Destroy(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_destroy) | 清理编解码器内部资源，销毁编解码器实例。注意不能进行重复销毁，否则将会导致程序崩溃。 |
| [OH\_AVErrCode OH\_AudioCodec\_RegisterCallback(OH\_AVCodec \*codec, OH\_AVCodecCallback callback, void \*userData)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_registercallback) | 设置异步回调函数，使应用可以响应音频编解码器生成的事件。在调用Prepare之前，必须调用此接口。 |
| [OH\_AVErrCode OH\_AudioCodec\_Configure(OH\_AVCodec \*codec, const OH\_AVFormat \*format)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_configure) | 配置音频描述信息。音频编解码器通常会根据音频描述信息进行配置。在调用Prepare之前，必须调用此接口。 |
| [OH\_AVErrCode OH\_AudioCodec\_Prepare(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_prepare) | 准备编解码器的内部资源，在调用此接口之前必须调用Configure接口。 |
| [OH\_AVErrCode OH\_AudioCodec\_Start(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_start) | 调用此接口启动编解码器，在Prepare成功后执行。启动后，编解码器将开始上报OH\_AVCodecOnNeedInputBuffer事件。 |
| [OH\_AVErrCode OH\_AudioCodec\_Stop(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_stop) | 停止编解码器。停止后，可以通过Start重新进入已启动状态（started），但需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。 |
| [OH\_AVErrCode OH\_AudioCodec\_Flush(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_flush) | 清除编解码器中缓存的输入和输出数据。调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。 |
| [OH\_AVErrCode OH\_AudioCodec\_Reset(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_reset) | 重置编解码器。此时会清空已配置的参数和输入输出数据。  如果要继续编解码，需要再次调用Configure接口配置编解码器实例。 |
| [OH\_AVFormat \*OH\_AudioCodec\_GetOutputDescription(OH\_AVCodec \*codec)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputdescription) | 获取编解码器输出数据的OH\_AVFormat信息。  需要注意的是，返回值所指向的OH\_AVFormat实例需要开发者调用[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)接口手动释放。 |
| [OH\_AVErrCode OH\_AudioCodec\_SetParameter(OH\_AVCodec \*codec, const OH\_AVFormat \*format)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_setparameter) | 配置编解码器的动态参数。  注意，该接口必须在编解码器启动后才能调用。另外，参数配置错误可能会导致编解码失败。 |
| [OH\_AVErrCode OH\_AudioCodec\_PushInputBuffer(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_pushinputbuffer) | 通知音频编解码器已完成对index所对应缓冲区进行输入数据的填充。  [OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)回调将报告可用的输入缓冲区和对应的索引值。  一旦具有指定索引的缓冲区被提交给音频编解码器，该缓冲区将无法再次访问，直到再次收到[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)回调，收到相同索引时此缓冲区才可使用。  此外，对于某些编解码器，需要在开始时向编解码器输入编解码特定配置数据(Codec-Specific-Data)，以初始化编解码器的编解码过程。  注意：当返回值为AV\_ERR\_UNKNOWN时此次调用不生效，输入缓冲区仍为未处理状态，需根据返回的特定错误代码处理后输入相同的index重新调用OH\_AudioCodec\_PushInputBuffer。 |
| [OH\_AVErrCode OH\_AudioCodec\_FreeOutputBuffer(OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_freeoutputbuffer) | 将处理后的输出缓冲区返回给编解码器。使用完输出缓冲区后需及时调用此接口进行释放，否则会阻塞编解码流程。 |
| [OH\_AVErrCode OH\_AudioCodec\_IsValid(OH\_AVCodec \*codec, bool \*isValid)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_isvalid) | 检查当前编解码器实例是否有效。  可用于后台故障恢复或应用程序从后台恢复时检测编解码器有效状态。 |
| [OH\_AVErrCode OH\_AudioCodec\_SetDecryptionConfig(OH\_AVCodec \*codec, MediaKeySession \*mediaKeySession, bool secureAudio)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_setdecryptionconfig) | 设置解密信息。 |
| [OH\_AVErrCode OH\_AudioCodec\_QueryInputBuffer(struct OH\_AVCodec \*codec, uint32\_t \*index, int64\_t timeoutUs)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_queryinputbuffer) | 在设置的超时时间内，尝试查询对应音频编解码器可用的输入缓冲区的索引值。  获取到索引值后，使用[OH\_AudioCodec\_GetInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getinputbuffer)接口获取索引值对应的缓冲区。  在缓冲区填充数据后，使用[OH\_AudioCodec\_PushInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_pushinputbuffer)输入对应索引值，将缓冲区数据送到编解码器。  注意：此接口仅可在音频编解码的同步模式中使用。 |
| [OH\_AVBuffer \*OH\_AudioCodec\_GetInputBuffer(struct OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getinputbuffer) | 输入索引值，获取对应音频编解码器中该索引值对应的输入缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。 |
| [OH\_AVErrCode OH\_AudioCodec\_QueryOutputBuffer(struct OH\_AVCodec \*codec, uint32\_t \*index, int64\_t timeoutUs)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_queryoutputbuffer) | 在设置的超时时间内，尝试查询对应音频编解码器可用的输出缓冲区的索引值。获取到索引值后，通过[OH\_AudioCodec\_GetOutputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputbuffer)接口获取的输出缓冲区使用完后，  需要调用[OH\_AudioCodec\_FreeOutputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_freeoutputbuffer)接口进行释放。释放后无法再次使用，长期不释放会阻塞编解码流程。注意：此接口仅可在音频编解码的同步模式中使用。 |
| [OH\_AVBuffer \*OH\_AudioCodec\_GetOutputBuffer(struct OH\_AVCodec \*codec, uint32\_t index)](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputbuffer) | 输入索引值，获取对应音频编解码器中该索引值对应的输出缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioCodec\_CreateByMime()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCodec *OH_AudioCodec_CreateByMime(const char *mime, bool isEncoder)
```

**描述**

根据MIME类型创建音频编解码器实例，大多数场景下建议使用此方式。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*mime | MIME类型描述字符串，请参阅[AVCODEC\_MIMETYPE](capi-native-avcodec-base-h.md#变量)。 |
| bool isEncoder | true表示需要创建编码器，false表示需要创建解码器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \* | 返回OH\_AVCodec实例的指针。 |

### OH\_AudioCodec\_CreateByName()

PhonePC/2in1TabletTVWearable

```
1. OH_AVCodec *OH_AudioCodec_CreateByName(const char *name)
```

**描述**

通过音频编解码器名称创建音频编解码器实例，使用此接口的前提是知道编解码器的确切名称，编解码器的名称可以通过[OH\_AVCapability\_GetName](capi-native-avcapability-h.md#oh_avcapability_getname)获取。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*name | 音频编解码器名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \* | 返回OH\_AVCodec实例的指针。 |

### OH\_AudioCodec\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Destroy(OH_AVCodec *codec)
```

**描述**

清理编解码器内部资源，销毁编解码器实例。注意不能进行重复销毁，否则将会导致程序崩溃。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_NO\_MEMORY：内部资源已经释放。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_RegisterCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_RegisterCallback(OH_AVCodec *codec, OH_AVCodecCallback callback, void *userData)
```

**描述**

设置异步回调函数，使应用可以响应音频编解码器生成的事件。在调用Prepare之前，必须调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| [OH\_AVCodecCallback](capi-codecbase-oh-avcodeccallback.md) callback | 所有回调函数的集合。 |
| void \*userData | 用户特定数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。 |

### OH\_AudioCodec\_Configure()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Configure(OH_AVCodec *codec, const OH_AVFormat *format)
```

**描述**

配置音频描述信息。音频编解码器通常会根据音频描述信息进行配置。在调用Prepare之前，必须调用此接口。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| [const OH\_AVFormat](capi-core-oh-avformat.md) \*format | 指向OH\_AVFormat的指针，给出要编解码的音频轨道的描述。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_Prepare()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Prepare(OH_AVCodec *codec)
```

**描述**

准备编解码器的内部资源，在调用此接口之前必须调用Configure接口。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_Start()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Start(OH_AVCodec *codec)
```

**描述**

调用此接口启动编解码器，在Prepare成功后执行。启动后，编解码器将开始上报OH\_AVCodecOnNeedInputBuffer事件。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Stop(OH_AVCodec *codec)
```

**描述**

停止编解码器。停止后，可以通过Start重新进入已启动状态（started），但需要注意的是，如果编解码器之前已输入数据，则需要重新输入编解码器数据。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_Flush()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Flush(OH_AVCodec *codec)
```

**描述**

清除编解码器中缓存的输入和输出数据。调用此接口后，以前通过异步回调上报的所有缓冲区索引都将失效，请确保不要访问这些索引对应的缓冲区。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_Reset()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_Reset(OH_AVCodec *codec)
```

**描述**

重置编解码器。此时会清空已配置的参数和输入输出数据。

如果要继续编解码，需要再次调用Configure接口配置编解码器实例。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。 |

### OH\_AudioCodec\_GetOutputDescription()

PhonePC/2in1TabletTVWearable

```
1. OH_AVFormat *OH_AudioCodec_GetOutputDescription(OH_AVCodec *codec)
```

**描述**

获取编解码器输出数据的OH\_AVFormat信息。

需要注意的是，返回值所指向的OH\_AVFormat实例需要开发者调用[OH\_AVFormat\_Destroy](capi-native-avformat-h.md#oh_avformat_destroy)接口手动释放。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AVFormat \* | 返回OH\_AVFormat句柄指针，生命周期将使用下一个[OH\_AudioCodec\_GetOutputDescription](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputdescription)刷新，或使用OH\_AVCodec销毁。 |

### OH\_AudioCodec\_SetParameter()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_SetParameter(OH_AVCodec *codec, const OH_AVFormat *format)
```

**描述**

配置编解码器的动态参数。

注意，该接口必须在编解码器启动后才能调用。另外，参数配置错误可能会导致编解码失败。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| const [OH\_AVFormat](capi-core-oh-avformat.md) \*format | OH\_AVFormat句柄指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_PushInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_PushInputBuffer(OH_AVCodec *codec, uint32_t index)
```

**描述**

通知音频编解码器已完成对index所对应缓冲区进行输入数据的填充。

[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)回调将报告可用的输入缓冲区和对应的索引值。

一旦具有指定索引的缓冲区被提交给音频编解码器，该缓冲区将无法再次访问，直到再次收到[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)回调，收到相同索引时此缓冲区才可使用。

此外，对于某些编解码器，需要在开始时向编解码器输入编解码特定配置数据(Codec-Specific-Data)，以初始化编解码器的编解码过程。

注意：当返回值为AV\_ERR\_UNKNOWN时此次调用不生效，输入缓冲区仍为未处理状态，需根据返回的特定错误代码处理后输入相同的index重新调用OH\_AudioCodec\_PushInputBuffer。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t index | 输入回调[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)给出的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入的index已使用或无效，需使用其他[OH\_AVCodecOnNeedInputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconneedinputbuffer)回调返回的index。  AV\_ERR\_INVALID\_STATE：编解码器状态错误，调用OH\_AudioCodec\_PushInputBuffer前需确保按顺序成功调用[OH\_AudioCodec\_Configure](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_configure)、[OH\_AudioCodec\_Prepare](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_prepare)、[OH\_AudioCodec\_Start](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_start)。  AV\_ERR\_UNKNOWN：输入buffer size无效，需确保buffer设置了正确的buffer size和flags。 |

### OH\_AudioCodec\_FreeOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_FreeOutputBuffer(OH_AVCodec *codec, uint32_t index)
```

**描述**

将处理后的输出缓冲区返回给编解码器。使用完输出缓冲区后需及时调用此接口进行释放，否则会阻塞编解码流程。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t index | 输出[OH\_AVCodecOnNewOutputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputbuffer)给出的索引值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数为nullptr或无效。缓冲区索引应该由[OH\_AVCodecOnNewOutputBuffer](capi-native-avcodec-base-h.md#oh_avcodeconnewoutputbuffer)给出。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_OPERATE\_NOT\_PERMIT：不允许操作，这可能是由于状态不正确或不支持的操作。  AV\_ERR\_UNKNOWN：发生内部错误，建议检查日志。 |

### OH\_AudioCodec\_IsValid()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_IsValid(OH_AVCodec *codec, bool *isValid)
```

**描述**

检查当前编解码器实例是否有效。

可用于后台故障恢复或应用程序从后台恢复时检测编解码器有效状态。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| bool \*isValid | 输出参数。指向布尔类型的指针，true：编解码器实例有效，false：编解码器实例无效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：输入参数为nullptr或无效。 |

### OH\_AudioCodec\_SetDecryptionConfig()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_SetDecryptionConfig(OH_AVCodec *codec, MediaKeySession *mediaKeySession,bool secureAudio)
```

**描述**

设置解密信息。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| [MediaKeySession](capi-drm-mediakeysession.md) \*mediaKeySession | 带有解密功能的媒体秘钥会话实例。 |
| bool secureAudio | 是否使用安全解码器。使用安全解码器为true,否则为false。  注意：当前音频解密尚不支持使用安全解码器。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：OH\_AVCodec实例为nullptr或无效，mediaKeySystemInfo实例为nullptr或无效。  AV\_ERR\_INVALID\_STATE：编解码器服务不可用。  AV\_ERR\_NO\_MEMORY：请求内存失败。 |

### OH\_AudioCodec\_QueryInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_QueryInputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs)
```

**描述**

在设置的超时时间内，尝试查询对应音频编解码器可用的输入缓冲区的索引值。

获取到索引值后，使用[OH\_AudioCodec\_GetInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getinputbuffer)接口获取索引值对应的缓冲区。

在缓冲区填充数据后，使用[OH\_AudioCodec\_PushInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_pushinputbuffer)输入对应索引值，将缓冲区数据送到编解码器。

注意：此接口仅可在音频编解码的同步模式中使用。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t \*index | 输出参数，获取到的输入缓冲区的索引值。 |
| int64\_t timeoutUs | 超时时间，单位：微秒。设置为负值时表示无限等待。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：执行失败，输入参数错误。  AV\_ERR\_INVALID\_STATE：执行失败，状态非法，没有启动编解码器等。  AV\_ERR\_OPERATE\_NOT\_PERMIT：执行失败，不允许非同步模式下调用。  AV\_ERR\_TRY\_AGAIN\_LATER：执行失败，超时时间内获取不到可用的缓冲区。 |

### OH\_AudioCodec\_GetInputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVBuffer *OH_AudioCodec_GetInputBuffer(struct OH_AVCodec *codec, uint32_t index)
```

**描述**

输入索引值，获取对应音频编解码器中该索引值对应的输入缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t index | 输入缓冲区的索引值。该索引值通过接口[OH\_AudioCodec\_QueryInputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_queryinputbuffer)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OH\_AVBuffer \* | 如果执行成功，则返回一个指向OH\_AVBuffer实例的指针，否则返回NULL。 |

### OH\_AudioCodec\_QueryOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVErrCode OH_AudioCodec_QueryOutputBuffer(struct OH_AVCodec *codec, uint32_t *index, int64_t timeoutUs)
```

**描述**

在设置的超时时间内，尝试查询对应音频编解码器可用的输出缓冲区的索引值。获取到索引值后，通过[OH\_AudioCodec\_GetOutputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputbuffer)接口获取的输出缓冲区使用完后，

需要调用[OH\_AudioCodec\_FreeOutputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_freeoutputbuffer)接口进行释放。释放后无法再次使用，长期不释放会阻塞编解码流程。注意：此接口仅可在音频编解码的同步模式中使用。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t \*index | 输出参数，获取到的输出缓冲区的索引值。 |
| int64\_t timeoutUs | 超时时间，单位：微秒。设置为负值时表示无限等待。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) | AV\_ERR\_OK：执行成功。  AV\_ERR\_INVALID\_VAL：执行失败，输入参数错误。  AV\_ERR\_INVALID\_STATE：执行失败，状态非法，没有启动编解码器等。  AV\_ERR\_OPERATE\_NOT\_PERMIT：执行失败，不允许非同步模式下调用。  AV\_ERR\_STREAM\_CHANGED：解码输出流格式发生变化, 可以通过调用[OH\_AudioCodec\_GetOutputDescription](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_getoutputdescription)接口获取新的流信息。  AV\_ERR\_TRY\_AGAIN\_LATER：执行失败，超时时间内获取不到可用的缓冲区。 |

### OH\_AudioCodec\_GetOutputBuffer()

PhonePC/2in1TabletTVWearable

```
1. OH_AVBuffer *OH_AudioCodec_GetOutputBuffer(struct OH_AVCodec *codec, uint32_t index)
```

**描述**

输入索引值，获取对应音频编解码器中该索引值对应的输出缓冲区。注意：此接口仅可在音频编解码的同步模式中使用。

**系统能力：** SystemCapability.Multimedia.Media.AudioCodec

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct OH\_AVCodec](capi-codecbase-oh-avcodec.md) \*codec | 指向OH\_AVCodec实例的指针。 |
| uint32\_t index | 输出缓冲区的索引值。该索引值通过接口[OH\_AudioCodec\_QueryOutputBuffer](capi-native-avcodec-audiocodec-h.md#oh_audiocodec_queryoutputbuffer)获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AVBuffer](capi-core-oh-avbuffer.md) \* | 如果执行成功，则返回一个指向OH\_AVBuffer实例的指针，否则返回NULL。 |
