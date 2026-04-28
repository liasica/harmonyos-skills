---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-audiocapturer-h
title: native_audiocapturer.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_audiocapturer.h
category: harmonyos-references
scraped_at: 2026-04-28T08:11:46+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:48ca676aca44f708812f0d4fc9ea2e7ee0d64a199d86db38693d17ae2877f23d
---

## 概述

PhonePC/2in1TabletTVWearable

声明音频采集的相关接口。

**引用文件：** <ohaudio/native\_audiocapturer.h>

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
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Release(OH\_AudioCapturer\* capturer)](capi-native-audiocapturer-h.md#oh_audiocapturer_release) | - | 释放输入音频流。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Start(OH\_AudioCapturer\* capturer)](capi-native-audiocapturer-h.md#oh_audiocapturer_start) | - | 启动音频采集器，开始获取音频数据。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Pause(OH\_AudioCapturer\* capturer)](capi-native-audiocapturer-h.md#oh_audiocapturer_pause) | - | 暂停输入音频流。在暂停音频，后续需要恢复录音的场景，建议使用pause。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Stop(OH\_AudioCapturer\* capturer)](capi-native-audiocapturer-h.md#oh_audiocapturer_stop) | - | 停止音频采集器，停止输入音频流。如果需要彻底结束录音，建议使用stop。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_Flush(OH\_AudioCapturer\* capturer)](capi-native-audiocapturer-h.md#oh_audiocapturer_flush) | - | 丢弃获取的音频数据。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetCurrentState(OH\_AudioCapturer\* capturer, OH\_AudioStream\_State\* state)](capi-native-audiocapturer-h.md#oh_audiocapturer_getcurrentstate) | - | 查询当前音频流状态。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetLatencyMode(OH\_AudioCapturer\* capturer, OH\_AudioStream\_LatencyMode\* latencyMode)](capi-native-audiocapturer-h.md#oh_audiocapturer_getlatencymode) | - | 查询当前音频流时延模式。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetStreamId(OH\_AudioCapturer\* capturer, uint32\_t\* streamId)](capi-native-audiocapturer-h.md#oh_audiocapturer_getstreamid) | - | 查询当前输入音频流ID。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetSamplingRate(OH\_AudioCapturer\* capturer, int32\_t\* rate)](capi-native-audiocapturer-h.md#oh_audiocapturer_getsamplingrate) | - | 查询当前输入音频流采样率。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetChannelCount(OH\_AudioCapturer\* capturer, int32\_t\* channelCount)](capi-native-audiocapturer-h.md#oh_audiocapturer_getchannelcount) | - | 查询当前音频流通道数。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetSampleFormat(OH\_AudioCapturer\* capturer, OH\_AudioStream\_SampleFormat\* sampleFormat)](capi-native-audiocapturer-h.md#oh_audiocapturer_getsampleformat) | - | 查询当前输入音频流采样格式。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetEncodingType(OH\_AudioCapturer\* capturer, OH\_AudioStream\_EncodingType\* encodingType)](capi-native-audiocapturer-h.md#oh_audiocapturer_getencodingtype) | - | 查询当前音频流编码类型。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetCapturerInfo(OH\_AudioCapturer\* capturer, OH\_AudioStream\_SourceType\* sourceType)](capi-native-audiocapturer-h.md#oh_audiocapturer_getcapturerinfo) | - | 查询当前音频流工作场景类型。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetFrameSizeInCallback(OH\_AudioCapturer\* capturer, int32\_t\* frameSize)](capi-native-audiocapturer-h.md#oh_audiocapturer_getframesizeincallback) | - | 在回调中查询帧大小，它是每次回调返回的缓冲区的固定长度。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetTimestamp(OH\_AudioCapturer\* capturer, clockid\_t clockId,int64\_t\* framePosition, int64\_t\* timestamp)](capi-native-audiocapturer-h.md#oh_audiocapturer_gettimestamp) | - | 获取输入音频流时间戳和当前数据帧位置信息。  该接口可以获取到音频通道实际录制位置（framePosition）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetFramesRead(OH\_AudioCapturer\* capturer, int64\_t\* frames)](capi-native-audiocapturer-h.md#oh_audiocapturer_getframesread) | - | 查询自创建流以来已读取的帧数。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetOverflowCount(OH\_AudioCapturer\* capturer, uint32\_t\* count)](capi-native-audiocapturer-h.md#oh_audiocapturer_getoverflowcount) | - | 查询当前录制音频流过载数。 |
| [typedef void (\*OH\_AudioCapturer\_OnReadDataCallback)(OH\_AudioCapturer\* capturer, void\* userData, void\* audioData, int32\_t audioDataSize)](capi-native-audiocapturer-h.md#oh_audiocapturer_onreaddatacallback) | OH\_AudioCapturer\_OnReadDataCallback | 读取音频数据的回调函数。为了消除麦克风硬件设计带来的上电杂音，通常会对录音启动后的前100ms数据进行静音。 |
| [typedef void (\*OH\_AudioCapturer\_OnDeviceChangeCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioDeviceDescriptorArray\* deviceArray)](capi-native-audiocapturer-h.md#oh_audiocapturer_ondevicechangecallback) | OH\_AudioCapturer\_OnDeviceChangeCallback | 音频录制流的设备变化事件回调函数。 |
| [typedef void (\*OH\_AudioCapturer\_OnInterruptCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)](capi-native-audiocapturer-h.md#oh_audiocapturer_oninterruptcallback) | OH\_AudioCapturer\_OnInterruptCallback | 音频录制流的中断事件回调函数。 |
| [typedef void (\*OH\_AudioCapturer\_OnErrorCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_Result error)](capi-native-audiocapturer-h.md#oh_audiocapturer_onerrorcallback) | OH\_AudioCapturer\_OnErrorCallback | 音频录制流的错误事件回调函数。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_GetFastStatus(OH\_AudioCapturer\* capturer, OH\_AudioStream\_FastStatus\* status)](capi-native-audiocapturer-h.md#oh_audiocapturer_getfaststatus) | - | 获取音频录制过程中的运行状态，是否在低时延状态下工作。 |
| [typedef void (\*OH\_AudioCapturer\_OnFastStatusChange)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_FastStatus status)](capi-native-audiocapturer-h.md#oh_audiocapturer_onfaststatuschange) | OH\_AudioCapturer\_OnFastStatusChange | 音频录制过程中低时延状态改变事件的回调函数。 |
| [typedef void (\*OH\_AudioCapturer\_OnPlaybackCaptureStartCallback)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_PlaybackCaptureStartState state)](capi-native-audiocapturer-h.md#oh_audiocapturer_onplaybackcapturestartcallback) | OH\_AudioCapturer\_OnPlaybackCaptureStartCallback | 音频录制过程中用于内录（录制的是设备内部应用的声音）启动结果的回调函数。该API暂不对外支持。 |
| [OH\_AudioStream\_Result OH\_AudioCapturer\_RequestPlaybackCaptureStart(OH\_AudioCapturer\* capturer, OH\_AudioCapturer\_OnPlaybackCaptureStartCallback callback, void\* userData)](capi-native-audiocapturer-h.md#oh_audiocapturer_requestplaybackcapturestart) | - | 异步请求启动内录流。该函数是非阻塞的，意味着系统在接收到启动请求后，将继续处理用户授权和内录流的启动。  最终结果将通过回调函数返回。该API暂不对外支持。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AudioCapturer\_Release()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_Release(OH_AudioCapturer* capturer)
```

**描述**

释放输入音频流。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_Start()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_Start(OH_AudioCapturer* capturer)
```

**描述**

启动音频采集器，开始获取音频数据。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_Pause()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_Pause(OH_AudioCapturer* capturer)
```

**描述**

暂停输入音频流。在暂停音频，后续需要恢复录音的场景，建议使用pause。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_Stop()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_Stop(OH_AudioCapturer* capturer)
```

**描述**

停止音频采集器，停止输入音频流。如果需要彻底结束录音，建议使用stop。

**需要权限：** ohos.permission.MICROPHONE

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_Flush()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_Flush(OH_AudioCapturer* capturer)
```

**描述**

丢弃获取的音频数据。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_GetCurrentState()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetCurrentState(OH_AudioCapturer* capturer, OH_AudioStream_State* state)
```

**描述**

查询当前音频流状态。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioStream\_State](capi-native-audiostream-base-h.md#oh_audiostream_state)\* state | 指向一个用来接收音频流状态的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetLatencyMode()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetLatencyMode(OH_AudioCapturer* capturer,OH_AudioStream_LatencyMode* latencyMode)
```

**描述**

查询当前音频流时延模式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioStream\_LatencyMode](capi-native-audiostream-base-h.md#oh_audiostream_latencymode)\* latencyMode | 指向一个用来接收音频流时延模式的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetStreamId()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetStreamId(OH_AudioCapturer* capturer, uint32_t* streamId)
```

**描述**

查询当前输入音频流ID。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| uint32\_t\* streamId | 指向一个用来接收音频流ID的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetSamplingRate()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetSamplingRate(OH_AudioCapturer* capturer, int32_t* rate)
```

**描述**

查询当前输入音频流采样率。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| int32\_t\* rate | 指向一个用来接收音频流采样率的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetChannelCount()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetChannelCount(OH_AudioCapturer* capturer, int32_t* channelCount)
```

**描述**

查询当前音频流通道数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| int32\_t\* channelCount | 指向一个用来接收音频流通道数的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetSampleFormat()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetSampleFormat(OH_AudioCapturer* capturer,OH_AudioStream_SampleFormat* sampleFormat)
```

**描述**

查询当前输入音频流采样格式。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioStream\_SampleFormat](capi-native-audiostream-base-h.md#oh_audiostream_sampleformat)\* sampleFormat | 指向一个用来接收音频流采样格式的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetEncodingType()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetEncodingType(OH_AudioCapturer* capturer,OH_AudioStream_EncodingType* encodingType)
```

**描述**

查询当前音频流编码类型。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype)\* encodingType | 指向一个用来接收音频流编码类型的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetCapturerInfo()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetCapturerInfo(OH_AudioCapturer* capturer,OH_AudioStream_SourceType* sourceType)
```

**描述**

查询当前音频流工作场景类型。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioStream\_SourceType](capi-native-audiostream-base-h.md#oh_audiostream_sourcetype)\* sourceType | 指向一个用来接收输入类型音频流的工作场景的变量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetFrameSizeInCallback()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetFrameSizeInCallback(OH_AudioCapturer* capturer,int32_t* frameSize)
```

**描述**

在回调中查询帧大小，它是每次回调返回的缓冲区的固定长度。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| int32\_t\* frameSize | 指向将为帧大小设置的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_GetTimestamp()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetTimestamp(OH_AudioCapturer* capturer, clockid_t clockId,int64_t* framePosition, int64_t* timestamp)
```

**描述**

获取输入音频流时间戳和当前数据帧位置信息。

该接口可以获取到音频通道实际录制位置（framePosition）以及录制到该位置时候的时间戳（timestamp），时间戳单位为纳秒。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| clockid\_t clockId | 时钟标识符，使用CLOCK\_MONOTONIC。 |
| int64\_t\* framePosition | 指向要接收位置的变量的指针。 |
| int64\_t\* timestamp | 指向接收时间戳的变量的指针，单位为纳秒。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：  1. 参数capturer为nullptr；  2. 参数clockId无效。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常。 |

### OH\_AudioCapturer\_GetFramesRead()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetFramesRead(OH_AudioCapturer* capturer, int64_t* frames)
```

**描述**

查询自创建流以来已读取的帧数。

**起始版本：** 10

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| int64\_t\* frames | 指向将为帧计数设置的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_GetOverflowCount()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetOverflowCount(OH_AudioCapturer* capturer, uint32_t* count)
```

**描述**

查询当前录制音频流过载数。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| uint32\_t\* count | 指向一个用来接收音频流过载数的变量的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。 |

### OH\_AudioCapturer\_OnReadDataCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioCapturer_OnReadDataCallback)(OH_AudioCapturer* capturer, void* userData, void* audioData,int32_t audioDataSize)
```

**描述**

读取音频数据的回调函数。为了消除麦克风硬件设计带来的上电杂音，通常会对录音启动后的前100ms数据进行静音。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域，方便应用给自身传递数据。 |
| void\* audioData | 指向录制数据存储区域，用于应用读取录制数据。 |
| int32\_t audioDataSize | 录制数据的长度，单位为字节。 |

### OH\_AudioCapturer\_OnDeviceChangeCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioCapturer_OnDeviceChangeCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioDeviceDescriptorArray* deviceArray)
```

**描述**

音频录制流的设备变化事件回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioDeviceDescriptorArray](capi-ohaudio-oh-audiodevicedescriptorarray.md)\* deviceArray | 音频设备描述符数组。 |

### OH\_AudioCapturer\_OnInterruptCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioCapturer_OnInterruptCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)
```

**描述**

音频录制流的中断事件回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype) type | 音频流中断类型。 |
| [OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint) hint | 音频流中断提示类型。 |

### OH\_AudioCapturer\_OnErrorCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioCapturer_OnErrorCallback)(OH_AudioCapturer* capturer, void* userData,OH_AudioStream_Result error)
```

**描述**

音频录制流的错误事件回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) error | 音频流录制错误结果。 |

### OH\_AudioCapturer\_GetFastStatus()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_GetFastStatus(OH_AudioCapturer* capturer,OH_AudioStream_FastStatus* status)
```

**描述**

获取音频录制过程中的运行状态，是否在低时延状态下工作。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioStream\_FastStatus](capi-native-audiostream-base-h.md#oh_audiostream_faststatus)\* status | 指向接收低时延状态的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：参数capturer为nullptr。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：执行状态异常，仅在释放状态之前可用。 |

### OH\_AudioCapturer\_OnFastStatusChange()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioCapturer_OnFastStatusChange)(OH_AudioCapturer* capturer,void* userData,OH_AudioStream_FastStatus status)
```

**描述**

音频录制过程中低时延状态改变事件的回调函数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_FastStatus](capi-native-audiostream-base-h.md#oh_audiostream_faststatus) status | 返回当前低时延状态。 |

### OH\_AudioCapturer\_OnPlaybackCaptureStartCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*OH_AudioCapturer_OnPlaybackCaptureStartCallback)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_PlaybackCaptureStartState state)
```

**描述**

音频录制过程中用于内录（录制的是设备内部应用的声音）启动结果的回调函数。该API暂不对外支持。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 通过[OH\_AudioCapturer\_RequestPlaybackCaptureStart](capi-native-audiocapturer-h.md#oh_audiocapturer_requestplaybackcapturestart)指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_PlaybackCaptureStartState](capi-native-audiostream-base-h.md#oh_audiostream_playbackcapturestartstate) state | 表示内录请求是否成功的状态。 |

### OH\_AudioCapturer\_RequestPlaybackCaptureStart()

PhonePC/2in1TabletTVWearable

```
1. OH_AudioStream_Result OH_AudioCapturer_RequestPlaybackCaptureStart(OH_AudioCapturer* capturer, OH_AudioCapturer_OnPlaybackCaptureStartCallback callback, void* userData)
```

**描述**

异步请求启动内录流。该函数是非阻塞的，意味着系统在接收到启动请求后，将继续处理用户授权和内录流的启动。

最终结果将通过回调函数返回。该API暂不对外支持。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| [OH\_AudioCapturer\_OnPlaybackCaptureStartCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onplaybackcapturestartcallback) callback | 用于接收启动请求最终结果的回调函数。 |
| void\* userData | 指向应用自定义的数据存储区域, 该结构将传递给回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) | AUDIOSTREAM\_SUCCESS：函数执行成功。  AUDIOSTREAM\_ERROR\_INVALID\_PARAM：capturer或callback是无效的。  AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE：如果流已经在运行中或者已释放则是非法状态。  AUDIOSTREAM\_ERROR\_SYSTEM：系统内部错误，比如音频服务错误。 |
