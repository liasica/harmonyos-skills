---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiorenderer-h
title: native_audiorenderer.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audiorenderer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4098693c903250d2e28fa156969dc7710e2502492323f917cb7f4455cb741cb6
---

## 概述

PhonePC/2in1TabletTVWearable

声明音频渲染的相关接口。

**引用文件：** <ohaudio/native\_audiorenderer.h>

**库：** libohaudio.so

**系统能力：** SystemCapability.Multimedia.Audio.Core

**起始版本：** 10

**相关模块：** [OHAudio](capi-ohaudio.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer)](capi-native-audiorenderer-h.md#oh_audiorenderer_release) | - | 释放输出音频流。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer)](capi-native-audiorenderer-h.md#oh_audiorenderer_start) | - | 开始输出音频数据。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer)](capi-native-audiorenderer-h.md#oh_audiorenderer_pause) | - | 暂停输出音频流。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer)](capi-native-audiorenderer-h.md#oh_audiorenderer_stop) | - | 停止输出音频流。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer)](capi-native-audiorenderer-h.md#oh_audiorenderer_flush) | - | 清空缓冲区的音频数据。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetCurrentState(OH\_AudioRenderer\* renderer, OH\_AudioStream\_State\* state)](capi-native-audiorenderer-h.md#oh_audiorenderer_getcurrentstate) | - | 查询当前输出音频流状态。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSamplingRate(OH\_AudioRenderer\* renderer, int32\_t\* rate)](capi-native-audiorenderer-h.md#oh_audiorenderer_getsamplingrate) | - | 查询当前输出音频流采样率。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetStreamId(OH\_AudioRenderer\* renderer, uint32\_t\* streamId)](capi-native-audiorenderer-h.md#oh_audiorenderer_getstreamid) | - | 查询当前输出音频流ID。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetChannelCount(OH\_AudioRenderer\* renderer, int32\_t\* channelCount)](capi-native-audiorenderer-h.md#oh_audiorenderer_getchannelcount) | - | 查询当前输出音频流通道数。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSampleFormat(OH\_AudioRenderer\* renderer, OH\_AudioStream\_SampleFormat\* sampleFormat)](capi-native-audiorenderer-h.md#oh_audiorenderer_getsampleformat) | - | 查询当前输出音频流采样格式。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetLatencyMode(OH\_AudioRenderer\* renderer, OH\_AudioStream\_LatencyMode\* latencyMode)](capi-native-audiorenderer-h.md#oh_audiorenderer_getlatencymode) | - | 查询当前输出音频流时延模式。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetRendererInfo(OH\_AudioRenderer\* renderer, OH\_AudioStream\_Usage\* usage)](capi-native-audiorenderer-h.md#oh_audiorenderer_getrendererinfo) | - | 查询当前输出音频流的使用类型。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetEncodingType(OH\_AudioRenderer\* renderer, OH\_AudioStream\_EncodingType\* encodingType)](capi-native-audiorenderer-h.md#oh_audiorenderer_getencodingtype) | - | 查询当前输出音频流编码类型。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetFramesWritten(OH\_AudioRenderer\* renderer, int64\_t\* frames)](capi-native-audiorenderer-h.md#oh_audiorenderer_getframeswritten) | - | 查询自创建流以来已写入的帧数。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetTimestamp(OH\_AudioRenderer\* renderer, clockid\_t clockId, int64\_t\* framePosition, int64\_t\* timestamp)](capi-native-audiorenderer-h.md#oh_audiorenderer_gettimestamp) | - | 获取输出音频流时间戳和位置信息。  该接口可以获取到音频通道实际播放位置（framePosition）以及播放到该位置时候的时间戳（timestamp），时间戳单位为纳秒。  当设备切换或暂停恢复时，由于播放通路本身需要一段时间恢复，调用该接口获取的播放位置和时间戳会短暂地保持在切换或暂停前的状态。  该接口一般用来实现音画同步，频繁调用可能会带来功耗问题，调用时间间隔建议不要小于200ms，可以每分钟调用一次。因此在能保证音画同步效果的情况下，请避免频繁查询时间戳。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetAudioTimestampInfo(OH\_AudioRenderer\* renderer, int64\_t\* framePosition, int64\_t\* timestamp)](capi-native-audiorenderer-h.md#oh_audiorenderer_getaudiotimestampinfo) | - | 获取输出音频流时间戳和位置信息，适配倍速接口。  获取输出音频流时间戳和位置信息，通常用于进行音画同步对齐。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetFrameSizeInCallback(OH\_AudioRenderer\* renderer, int32\_t\* frameSize)](capi-native-audiorenderer-h.md#oh_audiorenderer_getframesizeincallback) | - | 在回调中查询帧大小，它是一个固定的长度，每次回调都要填充流。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSpeed(OH\_AudioRenderer\* renderer, float\* speed)](capi-native-audiorenderer-h.md#oh_audiorenderer_getspeed) | - | 获取音频渲染速率。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetSpeed(OH\_AudioRenderer\* renderer, float speed)](capi-native-audiorenderer-h.md#oh_audiorenderer_setspeed) | - | 设置音频渲染速率。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetMarkPosition(OH\_AudioRenderer\* renderer, uint32\_t samplePos, OH\_AudioRenderer\_OnMarkReachedCallback callback, void\* userData)](capi-native-audiorenderer-h.md#oh_audiorenderer_setmarkposition) | - | 在当前渲染器上设置标记位置。调用此函数将覆盖已设置的标记位置。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_CancelMark(OH\_AudioRenderer\* renderer)](capi-native-audiorenderer-h.md#oh_audiorenderer_cancelmark) | - | 取消由[OH\_AudioRenderer\_SetMarkPosition](capi-native-audiorenderer-h.md#oh_audiorenderer_setmarkposition)设置的标记。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolume(OH\_AudioRenderer\* renderer, float volume)](capi-native-audiorenderer-h.md#oh_audiorenderer_setvolume) | - | 设置当前音频流音量值。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolumeWithRamp(OH\_AudioRenderer\* renderer, float volume, int32\_t durationMs)](capi-native-audiorenderer-h.md#oh_audiorenderer_setvolumewithramp) | - | 在指定时间范围内使用渐变更改音量。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetVolume(OH\_AudioRenderer\* renderer, float\* volume)](capi-native-audiorenderer-h.md#oh_audiorenderer_getvolume) | - | 获取当前音频流音量值。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetUnderflowCount(OH\_AudioRenderer\* renderer, uint32\_t\* count)](capi-native-audiorenderer-h.md#oh_audiorenderer_getunderflowcount) | - | 获取当前播放音频流欠载数。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetChannelLayout(OH\_AudioRenderer\* renderer, OH\_AudioChannelLayout\* channelLayout)](capi-native-audiorenderer-h.md#oh_audiorenderer_getchannellayout) | - | 查询当前音频流声道布局。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetEffectMode(OH\_AudioRenderer\* renderer, OH\_AudioStream\_AudioEffectMode\* effectMode)](capi-native-audiorenderer-h.md#oh_audiorenderer_geteffectmode) | - | 查询当前音频流音效模式。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetEffectMode(OH\_AudioRenderer\* renderer, OH\_AudioStream\_AudioEffectMode effectMode)](capi-native-audiorenderer-h.md#oh_audiorenderer_seteffectmode) | - | 设置当前音频流音效模式。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetRendererPrivacy(OH\_AudioRenderer\* renderer, OH\_AudioStream\_PrivacyType\* privacy)](capi-native-audiorenderer-h.md#oh_audiorenderer_getrendererprivacy) | - | 查询当前播放音频流是否会被其它应用录制。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetSilentModeAndMixWithOthers(OH\_AudioRenderer\* renderer, bool on)](capi-native-audiorenderer-h.md#oh_audiorenderer_setsilentmodeandmixwithothers) | - | 设置静音并发播放模式。  当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其他音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetSilentModeAndMixWithOthers(OH\_AudioRenderer\* renderer, bool\* on)](capi-native-audiorenderer-h.md#oh_audiorenderer_getsilentmodeandmixwithothers) | - | 获取当前音频流是否开启静音并发播放。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetDefaultOutputDevice(OH\_AudioRenderer\* renderer, OH\_AudioDevice\_Type deviceType)](capi-native-audiorenderer-h.md#oh_audiorenderer_setdefaultoutputdevice) | - | 设置默认本机内置发声设备。  本接口仅适用于音频流类型[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage)为语音消息、VoIP语音通话或者VoIP视频通话的场景使用，以及可选的设备类型为听筒、扬声器和系统默认设备。  本接口允许在AudioRenderer创建以后的任何时间被调用，系统会记录应用设置的默认本机内置发声设备。在应用启动播放时，若有外接设备如蓝牙耳机/有线耳机接入，系统优先从外接设备发声；否则系统遵循应用设置的默认本机内置发声设备发声。 |
| [typedef void (\*OH\_AudioRenderer\_OnInterruptCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)](capi-native-audiorenderer-h.md#oh_audiorenderer_oninterruptcallback) | OH\_AudioRenderer\_OnInterruptCallback | 音频流中断事件回调函数。 |
| [typedef void (\*OH\_AudioRenderer\_OnErrorCallback)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Result error)](capi-native-audiorenderer-h.md#oh_audiorenderer_onerrorcallback) | OH\_AudioRenderer\_OnErrorCallback | 音频流错误事件回调函数。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetFastStatus(OH\_AudioRenderer\* renderer, OH\_AudioStream\_FastStatus\* status)](capi-native-audiorenderer-h.md#oh_audiorenderer_getfaststatus) | - | 获取音频播放过程中的运行状态，是否在低时延状态下工作。 |
| [typedef void (\*OH\_AudioRenderer\_OnFastStatusChange)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_FastStatus status)](capi-native-audiorenderer-h.md#oh_audiorenderer_onfaststatuschange) | OH\_AudioRenderer\_OnFastStatusChange | 音频播放过程中低时延状态改变事件的回调函数。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_SetLoudnessGain(OH\_AudioRenderer\* renderer, float loudnessGain)](capi-native-audiorenderer-h.md#oh_audiorenderer_setloudnessgain) | - | 设置音频播放的响度值。默认的响度值是0.0dB。音频流播放类型必须是音乐[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC，  电影或视频[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE，  有声读物（包括听书、相声、评书）、听新闻、播客等[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK。  音频流的时延模式必须是普通时延[OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL。  本接口不支持通过高清通路播放的音频流设置响度。  由于音频框架与硬件之间存在缓冲区，响度调节实际生效存在延迟，时长取决于缓冲区长度。  建议在不同音频开始播放前预先设置响度，以实现最佳均衡效果。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetLoudnessGain(OH\_AudioRenderer\* renderer, float\* loudnessGain)](capi-native-audiorenderer-h.md#oh_audiorenderer_getloudnessgain) | - | 获取音频流的响度值。 |
| [typedef int32\_t (\*OH\_AudioRenderer\_OnWriteDataCallbackAdvanced)(OH\_AudioRenderer\* renderer, void\* userData, void\* audioData, int32\_t audioDataSize)](capi-native-audiorenderer-h.md#oh_audiorenderer_onwritedatacallbackadvanced) | OH\_AudioRenderer\_OnWriteDataCallbackAdvanced | 该函数指针将指向用于写入音频数据的回调函数。不同于OH\_AudioRenderer\_OnWriteDataCallback，此函数允许应用填充[0, audioDataSize]长度的数据。  其中audioDataSize为回调buffer的长度。调用方通过返回值告知系统写入的数据长度。  如果返回0，回调线程将会sleep一段时间。  否则，系统可能会立刻进行下一次回调。 |
| [OH\_AudioStream\_Result OH\_AudioRenderer\_GetLatency(OH\_AudioRenderer\* renderer, OH\_AudioStream\_LatencyType type, int32\_t\* latencyMs)](capi-native-audiorenderer-h.md#oh_audiorenderer_getlatency) | - | 获取当前音频路由的估算时延（单位：毫秒）。无线连接的音频设备，时延估算可能存在误差，结果仅供参考。  由于时延未计入实时缓冲区，建议仅在音频播放开始时获取，避免频繁调用，否则可能因路由切换而阻塞该接口调用。  当音频数据输出到硬件后，建议使用[OH\_AudioRenderer\_GetAudioTimestampInfo](capi-native-audiorenderer-h.md#oh_audiorenderer_getaudiotimestampinfo)进行音视频同步。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioRenderer\_Release()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_Release(OH_AudioRenderer* renderer)
```

**描述**

释放输出音频流。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioRenderer\_Start()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_Start(OH_AudioRenderer* renderer)
```

**描述**

开始输出音频数据。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioRenderer\_Pause()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_Pause(OH_AudioRenderer* renderer)
```

**描述**

暂停输出音频流。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioRenderer\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_Stop(OH_AudioRenderer* renderer)
```

**描述**

停止输出音频流。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioRenderer\_Flush()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_Flush(OH_AudioRenderer* renderer)
```

**描述**

清空缓冲区的音频数据。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioRenderer\_GetCurrentState()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetCurrentState(OH_AudioRenderer* renderer, OH_AudioStream_State* state)
```

**描述**

查询当前输出音频流状态。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_State](capi-native-audiostream-base-h.md#oh_audiostream_state)\* state | 指向一个用来接收音频流状态的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetSamplingRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetSamplingRate(OH_AudioRenderer* renderer, int32_t* rate)
```

**描述**

查询当前输出音频流采样率。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| int32\_t\* rate | 指向一个用来接收音频流采样率的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetStreamId()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetStreamId(OH_AudioRenderer* renderer, uint32_t* streamId)
```

**描述**

查询当前输出音频流ID。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| uint32\_t\* streamId | 指向一个用来接收音频流ID的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetChannelCount()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetChannelCount(OH_AudioRenderer* renderer, int32_t* channelCount)
```

**描述**

查询当前输出音频流通道数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| int32\_t\* channelCount | 指向一个用来接收音频流通道数的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetSampleFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetSampleFormat(OH_AudioRenderer* renderer, OH_AudioStream_SampleFormat* sampleFormat)
```

**描述**

查询当前输出音频流采样格式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_SampleFormat](capi-native-audiostream-base-h.md#oh_audiostream_sampleformat)\* sampleFormat | 指向一个用来接收音频流采样格式的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetLatencyMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetLatencyMode(OH_AudioRenderer* renderer, OH_AudioStream_LatencyMode* latencyMode)
```

**描述**

查询当前输出音频流时延模式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode)\* latencyMode | 指向一个用来接收音频流时延模式的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetRendererInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetRendererInfo(OH_AudioRenderer* renderer, OH_AudioStream_Usage* usage)
```

**描述**

查询当前输出音频流的使用类型。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage)\* usage | 指向一个用来接收输出类型音频流的使用类型的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetEncodingType()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetEncodingType(OH_AudioRenderer* renderer, OH_AudioStream_EncodingType* encodingType)
```

**描述**

查询当前输出音频流编码类型。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype)\* encodingType | 指向一个用来接收音频流编码类型的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetFramesWritten()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetFramesWritten(OH_AudioRenderer* renderer, int64_t* frames)
```

**描述**

查询自创建流以来已写入的帧数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| int64\_t\* frames | 指向将为帧计数设置的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetTimestamp()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetTimestamp(OH_AudioRenderer* renderer, clockid_t clockId, int64_t* framePosition, int64_t* timestamp)
```

**描述**

获取输出音频流时间戳和位置信息。

该接口可以获取到音频通道实际播放位置（framePosition）以及播放到该位置时候的时间戳（timestamp），时间戳单位为纳秒。

当设备切换或暂停恢复时，由于播放通路本身需要一段时间恢复，调用该接口获取的播放位置和时间戳会短暂地保持在切换或暂停前的状态。

该接口一般用来实现音画同步，建议频率不要太频繁，可以每分钟一次，最好不要低于200ms一次。频繁调用可能会带来功耗问题，因此在能保证音画同步效果的情况下，不需要频繁地查询时间戳。

说明

* 当实际播放位置（framePosition）为0时，时间戳（timestamp）是固定值，直到流真正跑起来时才会更新。
* 当调用Flush接口时实际播放位置也会被重置。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| clockid\_t clockId | 时钟标识符，使用CLOCK\_MONOTONIC。 |
| int64\_t\* framePosition | 指向要接收位置的变量的指针。 |
| int64\_t\* timestamp | 指向接收时间戳的变量的指针，单位为纳秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数clockId无效。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioRenderer\_GetAudioTimestampInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetAudioTimestampInfo(OH_AudioRenderer* renderer, int64_t* framePosition, int64_t* timestamp)
```

**描述**

获取输出音频流时间戳和位置信息，适配倍速接口。

获取输出音频流时间戳和位置信息，通常用于进行音画同步对齐。

说明

* 当实际播放位置（framePosition）为0时，时间戳（timestamp）是固定值，直到流真正跑起来时才会更新。
* 当调用Flush接口时实际播放位置也会被重置。
* 当音频流路由（route）变化时，例如设备变化或者输出类型变化时，播放位置也会被重置，但此时时间戳仍会持续增长。推荐当实际播放位置和时间戳的变化稳定后再使用该接口获取的值。该接口适配倍速接口，例如当播放速度设置为2倍时，播放位置的增长速度也会返回为正常的2倍。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| int64\_t\* framePosition | 指向要接收位置的变量的指针。 |
| int64\_t\* timestamp | 指向接收时间戳的变量的指针，单位为纳秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数framePosition或timestamp为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：当前流状态不为合法状态时返回。  AUDIOSTREAM\_ERROR\_SYSTEM：  1. 系统进程崩溃或被阻塞；  2. 内部系统其他错误。 |

### OH\_AudioRenderer\_GetFrameSizeInCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetFrameSizeInCallback(OH_AudioRenderer* renderer, int32_t* frameSize)
```

**描述**

在回调中查询帧大小，它是一个固定的长度，每次回调都要填充流。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| int32\_t\* frameSize | 指向将为帧大小设置的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetSpeed()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetSpeed(OH_AudioRenderer* renderer, float* speed)
```

**描述**

获取音频渲染速率。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float\* speed | 指向接收播放倍速值的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_SetSpeed()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetSpeed(OH_AudioRenderer* renderer, float speed)
```

**描述**

设置音频渲染速率。

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float speed | 设置播放的倍速值（倍速范围：[0.25, 4.0]）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_SetMarkPosition()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetMarkPosition(OH_AudioRenderer* renderer, uint32_t samplePos, OH_AudioRenderer_OnMarkReachedCallback callback, void* userData)
```

**描述**

在当前渲染器上设置标记位置。调用此函数将覆盖已设置的标记位置。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| uint32\_t samplePos | 设置目标标记位置。 |
| [OH\_AudioRenderer\_OnMarkReachedCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_onmarkreachedcallback) callback | 当到达目标标记位置时回调。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数samplePos无效。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。  AUDIOSTREAM\_ERROR\_SYSTEM：出现系统错误。 |

### OH\_AudioRenderer\_CancelMark()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_CancelMark(OH_AudioRenderer* renderer)
```

**描述**

取消由[OH\_AudioRenderer\_SetMarkPosition](capi-native-audiorenderer-h.md#oh_audiorenderer_setmarkposition)设置的标记。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_SetVolume()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetVolume(OH_AudioRenderer* renderer, float volume)
```

**描述**

设置当前音频流音量值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float volume | 设置当前音频流音量，音量值范围[0.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数volume无效。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。  AUDIOSTREAM\_ERROR\_SYSTEM：出现系统错误。 |

### OH\_AudioRenderer\_SetVolumeWithRamp()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetVolumeWithRamp(OH_AudioRenderer* renderer, float volume, int32_t durationMs)
```

**描述**

在指定时间范围内使用渐变更改音量。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float volume | 目标音量值，取值范围[0.0, 1.0]。 |
| int32\_t durationMs | 音量渐变的持续时间，以毫秒为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数volume无效。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。  AUDIOSTREAM\_ERROR\_SYSTEM：出现系统错误。 |

### OH\_AudioRenderer\_GetVolume()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetVolume(OH_AudioRenderer* renderer, float* volume)
```

**描述**

获取当前音频流音量值。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float\* volume | 指向一个获取当前音频流音量值的指针。音量值的范围是[0.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数volume为nullptr。 |

### OH\_AudioRenderer\_GetUnderflowCount()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetUnderflowCount(OH_AudioRenderer* renderer, uint32_t* count)
```

**描述**

获取当前播放音频流欠载数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| uint32\_t\* count | 指向一个用来接收音频流欠载数的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数count为nullptr。 |

### OH\_AudioRenderer\_GetChannelLayout()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetChannelLayout(OH_AudioRenderer* renderer, OH_AudioChannelLayout* channelLayout)
```

**描述**

查询当前音频流声道布局。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout)\* channelLayout | 指向一个用来接收音频流声道布局的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetEffectMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetEffectMode(OH_AudioRenderer* renderer, OH_AudioStream_AudioEffectMode* effectMode)
```

**描述**

查询当前音频流音效模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_AudioEffectMode](capi-native-audiostream-base-h.md#oh_audiostream_audioeffectmode)\* effectMode | 指向一个用来接收音频流音效模式的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_SetEffectMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetEffectMode(OH_AudioRenderer* renderer, OH_AudioStream_AudioEffectMode effectMode)
```

**描述**

设置当前音频流音效模式。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_AudioEffectMode](capi-native-audiostream-base-h.md#oh_audiostream_audioeffectmode) effectMode | 设置当前音频流的目标音效模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetRendererPrivacy()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetRendererPrivacy(OH_AudioRenderer* renderer, OH_AudioStream_PrivacyType* privacy)
```

**描述**

查询当前播放音频流是否会被其它应用录制。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_PrivacyType](capi-native-audiostream-base-h.md#oh_audiostream_privacytype)\* privacy | 用于返回当前流的内录策略。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_SetSilentModeAndMixWithOthers()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetSilentModeAndMixWithOthers(OH_AudioRenderer* renderer, bool on)
```

**描述**

设置静音并发播放模式。

当设置为true，打开静音并发播放模式，系统将让此音频流静音播放，并且不会打断其他音频流。设置为false，将关闭静音并发播放，音频流可根据系统焦点策略抢占焦点。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| bool on | 设置当前音频流的静音并发状态。  true：设置当前播放的音频流静音播放，并且不会打断其它音频流播放。  false：取消当前播放的音频流静音播放，音频流可根据系统焦点策略抢占焦点。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_GetSilentModeAndMixWithOthers()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetSilentModeAndMixWithOthers(OH_AudioRenderer* renderer, bool* on)
```

**描述**

获取当前音频流是否开启静音并发播放。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| bool\* on | 用于返回当前流的静音并发状态。返回true表示打开，返回false表示关闭。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。 |

### OH\_AudioRenderer\_SetDefaultOutputDevice()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetDefaultOutputDevice(OH_AudioRenderer* renderer, OH_AudioDevice_Type deviceType)
```

**描述**

设置默认本机内置发声设备。

本接口仅适用于音频流类型[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage)为语音消息、VoIP语音通话或者VoIP视频通话的场景使用，以及可选的设备类型为听筒、扬声器和系统默认设备。

本接口允许在AudioRenderer创建以后的任何时间被调用，系统会记录应用设置的默认本机内置发声设备。在应用启动播放时，若有外接设备如蓝牙耳机/有线耳机接入，系统优先从外接设备发声；否则系统遵循应用设置的默认本机内置发声设备发声。

**设备行为差异：** 当该接口在无听筒的设备上设置默认发声设备为听筒时，将继续从扬声器发声。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type) deviceType | 指向[OH\_AudioDevice\_Type](capi-native-audio-device-base-h.md#oh_audiodevice_type)用于设置发声设备类型。可设置的设备类型包括:  AUDIO\_DEVICE\_TYPE\_EARPIECE：听筒  AUDIO\_DEVICE\_TYPE\_SPEAKER：扬声器  AUDIO\_DEVICE\_TYPE\_DEFAULT：系统默认设备 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr;  2. 参数deviceType无效。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。  AUDIOSTREAM\_ERROR\_SYSTEM：出现系统错误。 |

### OH\_AudioRenderer\_OnInterruptCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioRenderer_OnInterruptCallback)(OH_AudioRenderer* renderer, void* userData, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)
```

**描述**

音频流中断事件回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype) type | 音频流中断类型。 |
| [OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint) hint | 音频流中断提示类型。 |

### OH\_AudioRenderer\_OnErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioRenderer_OnErrorCallback)(OH_AudioRenderer* renderer, void* userData, OH_AudioStream_Result error)
```

**描述**

音频流错误事件回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) error | 音频流播放错误结果。 |

### OH\_AudioRenderer\_GetFastStatus()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetFastStatus(OH_AudioRenderer* renderer, OH_AudioStream_FastStatus* status)
```

**描述**

获取音频播放过程中的运行状态，是否在低时延状态下工作。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_FastStatus](capi-native-audiostream-base-h.md#oh_audiostream_faststatus)\* status | 指向接收低时延状态的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数renderer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常，仅在释放状态之前可用。 |

### OH\_AudioRenderer\_OnFastStatusChange()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioRenderer_OnFastStatusChange)(OH_AudioRenderer* renderer, void* userData, OH_AudioStream_FastStatus status
2. )
```

**描述**

音频播放过程中低时延状态改变事件的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_FastStatus](capi-native-audiostream-base-h.md#oh_audiostream_faststatus) status | 返回当前低时延状态。 |

### OH\_AudioRenderer\_SetLoudnessGain()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_SetLoudnessGain(OH_AudioRenderer* renderer, float loudnessGain)
```

**描述**

设置音频播放的响度值。默认的响度值是0.0dB。音频流播放类型必须是音乐[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MUSIC，

电影或视频[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_MOVIE，

有声读物（包括听书、相声、评书）、听新闻、播客等[OH\_AudioStream\_Usage](capi-native-audiostream-base-h.md#oh_audiostream_usage).AUDIOSTREAM\_USAGE\_AUDIOBOOK。

音频流的时延模式必须是普通时延[OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode).AUDIOSTREAM\_LATENCY\_MODE\_NORMAL。

本接口不支持通过高清通路播放的音频流设置响度。

由于音频框架与硬件之间存在缓冲区，响度调节实际生效存在延迟，时长取决于缓冲区长度。

建议在不同音频开始播放前预先设置响度，以实现最佳均衡效果。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float loudnessGain | 设置播放的响度值（响度值范围为[-90.0, 24.0]，单位为dB）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr，或音频流不支持设置响度；  2. 参数loudnessGain不在响度值范围内。 |

### OH\_AudioRenderer\_GetLoudnessGain()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetLoudnessGain(OH_AudioRenderer* renderer, float* loudnessGain)
```

**描述**

获取音频流的响度值。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| float\* loudnessGain | 指向接收播放响度值的变量的指针，单位为分贝。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数loudnessGain为nullptr。 |

### OH\_AudioRenderer\_OnWriteDataCallbackAdvanced()

PhonePC/2in1TabletTVWearable

```
1. typedef int32_t (*OH_AudioRenderer_OnWriteDataCallbackAdvanced)(OH_AudioRenderer* renderer, void* userData, void* audioData, int32_t audioDataSize)
```

**描述**

该函数指针将指向用于写入音频数据的回调函数。不同于OH\_AudioRenderer\_OnWriteDataCallback，此函数允许应用填充[0, audioDataSize]长度的数据。

其中audioDataSize为回调buffer的长度。调用方通过返回值告知系统写入的数据长度。

如果返回0，回调线程将会sleep一段时间。

否则，系统可能会立刻进行下一次回调。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向发生回调的实例。 |
| void\* userData | 指向通过回调函数传递的应用数据指针。 |
| void\* audioData | 指向让应用填充音频数据的指针。 |
| int32\_t audioDataSize | 应用应写入音频数据的数据长度，以字节为单位。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 应用实际填充有效音频数据的长度。返回值必须在[0, audioDataSize]范围内。  如果返回值小于0，系统将调整为0。 并且，如果返回值大于audioDataSize，系统将其调整到audioDataSize。  注意返回值必须是单个采样点大小的整数倍。  比如，双声道s16格式的音频数据，必须是4(2 \* 16 / 8)的整数倍。  否则，可能造成播放杂音。 |

### OH\_AudioRenderer\_GetLatency()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioRenderer_GetLatency(OH_AudioRenderer* renderer, OH_AudioStream_LatencyType type, int32_t* latencyMs)
```

**描述**

获取当前音频路由的估算时延（单位：毫秒）。无线连接的音频设备，时延估算可能存在误差，结果仅供参考。

由于时延未计入实时缓冲区，建议仅在音频播放开始时获取，避免频繁调用，否则可能因路由切换而阻塞该接口调用。

当音频数据输出到硬件后，建议使用[OH\_AudioRenderer\_GetAudioTimestampInfo](capi-native-audiorenderer-h.md#oh_audiorenderer_getaudiotimestampinfo)进行音视频同步。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| [OH\_AudioStream\_LatencyType](capi-native-audiostream-base-h.md#oh_audiostream_latencytype) type | 要获取的时延类型。 |
| int32\_t\* latencyMs | 指向用于接收时延（毫秒）变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数renderer为nullptr；  2. 参数latencyMs为nullptr；  3. 参数type无效。  AUDIOSTREAM\_ERROR\_SYSTEM：系统内部错误，例如音频服务异常。 |
