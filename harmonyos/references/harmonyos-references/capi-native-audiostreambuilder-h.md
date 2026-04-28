---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiostreambuilder-h
title: native_audiostreambuilder.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audiostreambuilder.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74ad29b21eb3f10e175fdefdff09417b8c7ba377225593063004235355ca2784
---

## 概述

PhonePC/2in1TabletTVWearable

声明音频流构造器相关接口。

包含构造和销毁构造器，设置音频流属性，回调等相关接口。

**引用文件：** <ohaudio/native\_audiostreambuilder.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 10

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_Create(OH\_AudioStreamBuilder\*\* builder, OH\_AudioStream\_Type type)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create) | 创建一个输入或者输出类型的音频流构造器。  当构造器不再使用时，需要调用[OH\_AudioStreamBuilder\_Destroy](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_destroy)销毁。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_Destroy(OH\_AudioStreamBuilder\* builder)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_destroy) | 销毁一个音频流构造器。  当构造器不再使用时，需要调用该函数销毁。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetSamplingRate(OH\_AudioStreamBuilder\* builder, int32\_t rate)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setsamplingrate) | 设置音频流的采样率属性。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetChannelCount(OH\_AudioStreamBuilder\* builder, int32\_t channelCount)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setchannelcount) | 设置音频流的通道数属性。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetSampleFormat(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_SampleFormat format)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setsampleformat) | 设置音频流的采样格式属性。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetEncodingType(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_EncodingType encodingType)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setencodingtype) | 设置音频流的编码类型属性。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetLatencyMode(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_LatencyMode latencyMode)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setlatencymode) | 设置音频流的时延模式。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetChannelLayout(OH\_AudioStreamBuilder\* builder, OH\_AudioChannelLayout channelLayout)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setchannellayout) | 设置音频流的声道布局。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInfo(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_Usage usage)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinfo) | 设置输出音频流的工作场景。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetVolumeMode(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_VolumeMode volumeMode)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setvolumemode) | 设置音频流音量模式。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerInfo(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_SourceType sourceType)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerinfo) | 设置输入音频流的工作场景。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_Callbacks callbacks, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback) | 设置输出音频流的回调。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OutputDeviceChangeCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendereroutputdevicechangecallback) | 设置输出音频流设备变更的回调。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererPrivacy(OH\_AudioStreamBuilder\* builder, OH\_AudioStream\_PrivacyType privacy)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererprivacy) | 设置当前播放音频流是否会被其它应用录制。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_Callbacks callbacks, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback) | 设置输入音频流的回调。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_WriteDataWithMetadataCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setwritedatawithmetadatacallback) | 设置同时写入音频数据和元数据的回调。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_GenerateRenderer(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\*\* audioRenderer)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer) | 创建输出音频流实例。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_GenerateCapturer(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\*\* audioCapturer)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer) | 创建输入音频流实例。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetFrameSizeInCallback(OH\_AudioStreamBuilder\* builder, int32\_t frameSize)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setframesizeincallback) | 用于播放时设置每次回调的帧长，帧长至少为音频硬件一次处理的数据大小，并且小于内部缓冲容量的一半。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInterruptMode(OH\_AudioStreamBuilder\* builder, OH\_AudioInterrupt\_Mode mode)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinterruptmode) | 设置流客户端的中断模式。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnWriteDataCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback) | 设置写入音频数据的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)或者本函数，只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnWriteDataCallbackAdvanced callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallbackadvanced) | 设置写入音频数据的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)类似。  如果同时设置该回调和OH\_AudioStreamBuilder\_SetRendererWriteDataCallback，只有最后一次设置的回调生效。  与OH\_AudioStreamBuilder\_SetRendererWriteDataCallback不同，OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced设置的回调函数，允许应用传入可变长度的音频数据，并通知系统写入的数据长度。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererInterruptCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnInterruptCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinterruptcallback) | 设置输出音频流中断事件的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)或者本函数，只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererErrorCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnErrorCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderererrorcallback) | 设置输出音频流错误事件的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerReadDataCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnReadDataCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerreaddatacallback) | 设置输入音频流读取数据的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnDeviceChangeCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerdevicechangecallback) | 设置输入音频流设备变更的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerInterruptCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnInterruptCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerinterruptcallback) | 设置输入音频流中断事件的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerErrorCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnErrorCallback callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturererrorcallback) | 设置输入音频流错误事件的回调函数。  此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted(OH\_AudioStreamBuilder\* builder, bool muteWhenInterrupted)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerwillmutewheninterrupted) | 设置输入音频流是否启用静音打断模式。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetRendererFastStatusChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioRenderer\_OnFastStatusChange callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererfaststatuschangecallback) | 设置音频播放过程中低时延状态改变事件的回调函数。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetCapturerFastStatusChangeCallback(OH\_AudioStreamBuilder\* builder, OH\_AudioCapturer\_OnFastStatusChange callback, void\* userData)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerfaststatuschangecallback) | 设置音频录制过程中低时延状态改变事件的回调函数。 |
| [OH\_AudioStream\_Result OH\_AudioStreamBuilder\_SetPlaybackCaptureMode(OH\_AudioStreamBuilder\* builder, uint32\_t mode)](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setplaybackcapturemode) | 在使用内录（录制设备内部应用的声音）时设置可以录制的音频模式，该模式将决定要录制的音频流类型。此功能仅适用于[AudioStream\_Type\_Capturer](capi-native-audiostream-base-h.md#oh_audiostream_type)类型。该API暂不对外支持。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioStreamBuilder\_Create()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_Create(OH_AudioStreamBuilder** builder, OH_AudioStream_Type type)
```

**描述**

创建一个输入或者输出类型的音频流构造器。

当构造器不再使用时，需要调用[OH\_AudioStreamBuilder\_Destroy](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_destroy)销毁。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\*\* builder | 该引用指向创建的构造器的结果。 |
| [OH\_AudioStream\_Type](capi-native-audiostream-base-h.md#oh_audiostream_type) type | 构造器的流类型。AUDIOSTREAM\_TYPE\_RENDERER或AUDIOSTREAM\_TYPE\_CAPTURER。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。 |

### OH\_AudioStreamBuilder\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_Destroy(OH_AudioStreamBuilder* builder)
```

**描述**

销毁一个音频流构造器。

当构造器不再使用时，需要调用该函数销毁。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioStreamBuilder\_SetSamplingRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetSamplingRate(OH_AudioStreamBuilder* builder, int32_t rate)
```

**描述**

设置音频流的采样率属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| int32\_t rate | 音频流采样率。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. 参数rate无效。 |

### OH\_AudioStreamBuilder\_SetChannelCount()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetChannelCount(OH_AudioStreamBuilder* builder, int32_t channelCount)
```

**描述**

设置音频流的通道数属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| int32\_t channelCount | 音频流通道数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. 参数channelCount无效。 |

### OH\_AudioStreamBuilder\_SetSampleFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetSampleFormat(OH_AudioStreamBuilder* builder,OH_AudioStream_SampleFormat format)
```

**描述**

设置音频流的采样格式属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_SampleFormat](capi-native-audiostream-base-h.md#oh_audiostream_sampleformat) format | 音频流采样格式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AudioStreamBuilder\_SetEncodingType()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetEncodingType(OH_AudioStreamBuilder* builder,OH_AudioStream_EncodingType encodingType)
```

**描述**

设置音频流的编码类型属性。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype) encodingType | 音频流编码类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AudioStreamBuilder\_SetLatencyMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetLatencyMode(OH_AudioStreamBuilder* builder,OH_AudioStream_LatencyMode latencyMode)
```

**描述**

设置音频流的时延模式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode) latencyMode | 音频流时延模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AudioStreamBuilder\_SetChannelLayout()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetChannelLayout(OH_AudioStreamBuilder* builder,OH_AudioChannelLayout channelLayout)
```

**描述**

设置音频流的声道布局。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout) channelLayout | 音频流声道布局。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AudioStreamBuilder\_SetRendererInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererInfo(OH_AudioStreamBuilder* builder,OH_AudioStream_Usage usage)
```

**描述**

设置输出音频流的工作场景。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage) usage | 输出音频流属性，使用的工作场景。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. 参数usage无效。 |

### OH\_AudioStreamBuilder\_SetVolumeMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetVolumeMode(OH_AudioStreamBuilder* builder,OH_AudioStream_VolumeMode volumeMode)
```

**描述**

设置音频流音量模式。

**起始版本：** 19

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_VolumeMode](capi-native-audiostream-base-h.md#oh_audiostream_volumemode) volumeMode | 要设置的音频流音量模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. 参数volumeMode无效。 |

### OH\_AudioStreamBuilder\_SetCapturerInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerInfo(OH_AudioStreamBuilder* builder,OH_AudioStream_SourceType sourceType)
```

**描述**

设置输入音频流的工作场景。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype) sourceType | 输入音频流属性，使用的工作场景。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. 参数sourceType无效。 |

### OH\_AudioStreamBuilder\_SetRendererCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_Callbacks callbacks, void* userData)
```

**描述**

设置输出音频流的回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：**

请分别使用以下接口设置回调函数：

[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)、[OH\_AudioStreamBuilder\_SetRendererInterruptCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererinterruptcallback)、[OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendereroutputdevicechangecallback)以及 [OH\_AudioStreamBuilder\_SetRendererErrorCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderererrorcallback)。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_Callbacks](capi-ohaudio-oh-audiorenderer-callbacks-struct.md) callbacks | 将被用来处理输出音频流相关事件的回调函数。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效。 |

### OH\_AudioStreamBuilder\_SetRendererOutputDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererOutputDeviceChangeCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_OutputDeviceChangeCallback callback, void* userData)
```

**描述**

设置输出音频流设备变更的回调。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_OutputDeviceChangeCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_outputdevicechangecallback) callback | 将被用来处理输出流设备变更相关事件的回调函数。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效。 |

### OH\_AudioStreamBuilder\_SetRendererPrivacy()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererPrivacy(OH_AudioStreamBuilder* builder,OH_AudioStream_PrivacyType privacy)
```

**描述**

设置当前播放音频流是否会被其它应用录制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioStream\_PrivacyType](capi-native-audiostream-base-h.md#oh_audiostream_privacytype) privacy | 标识对应播放音频流是否会被其它应用录制。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效。 |

### OH\_AudioStreamBuilder\_SetCapturerCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerCallback(OH_AudioStreamBuilder* builder,OH_AudioCapturer_Callbacks callbacks, void* userData)
```

**描述**

设置输入音频流的回调。

**起始版本：** 10

**废弃版本：** 20

**替代接口：**

请分别使用以下接口设置回调函数：

[OH\_AudioStreamBuilder\_SetCapturerReadDataCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerreaddatacallback)、[OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerdevicechangecallback)、[OH\_AudioStreamBuilder\_SetCapturerInterruptCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturerinterruptcallback)以及 [OH\_AudioStreamBuilder\_SetCapturerErrorCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturererrorcallback)。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer\_Callbacks](capi-ohaudio-oh-audiocapturer-callbacks-struct.md) callbacks | 将被用来处理输入音频流相关事件的回调函数。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效。 |

### OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetWriteDataWithMetadataCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_WriteDataWithMetadataCallback callback, void* userData)
```

**描述**

设置同时写入音频数据和元数据的回调。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_WriteDataWithMetadataCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_writedatawithmetadatacallback) callback | 将被用来同时写入音频数据和元数据的回调函数。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效。 |

### OH\_AudioStreamBuilder\_GenerateRenderer()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_GenerateRenderer(OH_AudioStreamBuilder* builder,OH_AudioRenderer** audioRenderer)
```

**描述**

创建输出音频流实例。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\*\* audioRenderer | 指向输出音频流实例的指针，将被用来接收函数创建的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效；  3. 创建OHAudioRenderer失败。 |

### OH\_AudioStreamBuilder\_GenerateCapturer()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_GenerateCapturer(OH_AudioStreamBuilder* builder,OH_AudioCapturer** audioCapturer)
```

**描述**

创建输入音频流实例。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\*\* audioCapturer | 指向输入音频流实例的指针，将被用来接收函数创建的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效；  3. 创建OHAudioCapturer失败。 |

### OH\_AudioStreamBuilder\_SetFrameSizeInCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetFrameSizeInCallback(OH_AudioStreamBuilder* builder,int32_t frameSize)
```

**描述**

用于播放时设置每次回调的帧长，帧长至少为音频硬件一次处理的数据大小，并且小于内部缓冲容量的一半。

低时延播放：frameSize可设置为5ms、10ms、15ms、20ms音频数据对应的帧长。

普通通路播放：frameSize可设置为20ms-100ms音频数据对应的帧长。例如，当采样率48000Hz时，20ms音频数据对应的帧长计算方式为：frameSize = 48000 \* 0.02，即960个采样点数。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| int32\_t frameSize | 要设置音频数据的帧长。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数builder为nullptr。 |

### OH\_AudioStreamBuilder\_SetRendererInterruptMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererInterruptMode(OH_AudioStreamBuilder* builder,OH_AudioInterrupt_Mode mode)
```

**描述**

设置流客户端的中断模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioInterrupt\_Mode](capi-native-audiostream-base-h.md#oh_audiointerrupt_mode) mode | 音频中断模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. 参数mode无效；  3. StreamType无效。 |

### OH\_AudioStreamBuilder\_SetRendererWriteDataCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererWriteDataCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_OnWriteDataCallback callback, void* userData)
```

**描述**

设置写入音频数据的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)或者本函数，只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_OnWriteDataCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback) callback | 将被用来写入音频数据的回调函数。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数builder为nullptr；  2. StreamType无效。 |

### OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererWriteDataCallbackAdvanced(OH_AudioStreamBuilder* builder,OH_AudioRenderer_OnWriteDataCallbackAdvanced callback, void* userData)
```

**描述**

设置写入音频数据的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrendererwritedatacallback)类似。

如果同时设置该回调和OH\_AudioStreamBuilder\_SetRendererWriteDataCallback，只有最后一次设置的回调生效。

与OH\_AudioStreamBuilder\_SetRendererWriteDataCallback不同，OH\_AudioStreamBuilder\_SetRendererWriteDataCallbackAdvanced设置的回调函数，允许应用传入可变长度的音频数据，并通知系统写入的数据长度。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_OnWriteDataCallbackAdvanced](capi-native-audiorenderer-h.md#oh_audiorenderer_onwritedatacallbackadvanced) callback | 将被用来写入音频数据的回调函数。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数非法，比如builder为空指针，等等。 |

### OH\_AudioStreamBuilder\_SetRendererInterruptCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererInterruptCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_OnInterruptCallback callback, void* userData)
```

**描述**

设置输出音频流中断事件的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)或者本函数，只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_OnInterruptCallback](capi-native-audiorenderer-h.md#oh_audiorenderer_oninterruptcallback) callback | 用于接收中断事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetRendererErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererErrorCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_OnErrorCallback callback, void* userData)
```

**描述**

设置输出音频流错误事件的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetRendererCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setrenderercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_OnErrorCallback](capi-native-audiorenderer-h.md#oh_audiorenderer_onerrorcallback) callback | 用于接收错误事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetCapturerReadDataCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerReadDataCallback(OH_AudioStreamBuilder* builder,OH_AudioCapturer_OnReadDataCallback callback, void* userData)
```

**描述**

设置输入音频流读取数据的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer\_OnReadDataCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onreaddatacallback) callback | 用于接收读取数据事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetCapturerDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerDeviceChangeCallback(OH_AudioStreamBuilder* builder,OH_AudioCapturer_OnDeviceChangeCallback callback, void* userData)
```

**描述**

设置输入音频流设备变更的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer\_OnDeviceChangeCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_ondevicechangecallback) callback | 用于接收设备变更事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetCapturerInterruptCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerInterruptCallback(OH_AudioStreamBuilder* builder,OH_AudioCapturer_OnInterruptCallback callback, void* userData)
```

**描述**

设置输入音频流中断事件的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer\_OnInterruptCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_oninterruptcallback) callback | 用于接收中断事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetCapturerErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerErrorCallback(OH_AudioStreamBuilder* builder,OH_AudioCapturer_OnErrorCallback callback, void* userData)
```

**描述**

设置输入音频流错误事件的回调函数。

此函数与[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)类似。如果同时使用[OH\_AudioStreamBuilder\_SetCapturerCallback](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_setcapturercallback)或者本函数，那么只有最后一次设置的回调才生效，其它回调不会生效。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer\_OnErrorCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onerrorcallback) callback | 用于接收错误事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerWillMuteWhenInterrupted(OH_AudioStreamBuilder* builder,bool muteWhenInterrupted)
```

**描述**

设置输入音频流是否启用静音打断模式。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| bool muteWhenInterrupted | 设置当前录制音频流是否启用静音打断模式。true表示启用；false表示不启用，保持为默认打断模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetRendererFastStatusChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetRendererFastStatusChangeCallback(OH_AudioStreamBuilder* builder,OH_AudioRenderer_OnFastStatusChange callback, void* userData)
```

**描述**

设置音频播放过程中低时延状态改变事件的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioRenderer\_OnFastStatusChange](capi-native-audiorenderer-h.md#oh_audiorenderer_onfaststatuschange) callback | 用于接收播放低时延状态改变事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetCapturerFastStatusChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetCapturerFastStatusChangeCallback(OH_AudioStreamBuilder* builder,OH_AudioCapturer_OnFastStatusChange callback, void* userData)
```

**描述**

设置音频录制过程中低时延状态改变事件的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| [OH\_AudioCapturer\_OnFastStatusChange](capi-native-audiocapturer-h.md#oh_audiocapturer_onfaststatuschange) callback | 用于接收录制低时延状态改变事件的回调函数。 |
| void\* userData | 指向应用程序数据结构的指针，该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效，比如，builder为空指针。 |

### OH\_AudioStreamBuilder\_SetPlaybackCaptureMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioStreamBuilder_SetPlaybackCaptureMode(OH_AudioStreamBuilder* builder, uint32_t mode)
```

**描述**

在使用内录（录制设备内部应用的声音）时设置可以录制的音频模式，该模式将决定要录制的音频流类型。此功能仅适用于[AudioStream\_Type\_Capturer](capi-native-audiostream-base-h.md#oh_audiostream_type)类型。该API暂不对外支持。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioStreamBuilder](capi-ohaudio-oh-audiostreambuilderstruct.md)\* builder | 指向[OH\_AudioStreamBuilder\_Create](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_create)创建的构造器实例。 |
| uint32\_t mode | 要设置的内录模式，可为[OH\_AudioStream\_PlaybackCaptureMode](capi-native-audiostream-base-h.md#oh_audiostream_playbackcapturemode)中多个值的组合。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数无效。例如，builder或mode为空指针。 |
