---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-lowpower-audio-sink-base-h
title: lowpower_audio_sink_base.h
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 头文件 > lowpower_audio_sink_base.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:35+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dd259d171c6b4226e5b779b5ad7254596f0aa18221294b34284c2ebb3ec9e507
---

## 概述

定义LowPowerAudioSink的结构体和枚举。

**引用文件：** <multimedia/player\_framework/lowpower\_audio\_sink\_base.h>

**库：** liblowpower\_avsink.so

**系统能力：** SystemCapability.Multimedia.Media.LowPowerAVSink

**起始版本：** 20

**相关模块：** [LowPowerAudioSink](capi-lowpoweraudiosink.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md) | OH\_LowPowerAudioSink | LowPowerAudioSink的声明。 |
| [OH\_LowPowerAudioSinkCallback](capi-lowpoweraudiosink-oh-lowpoweraudiosinkcallback.md) | OH\_LowPowerAudioSinkCallback | 包含了LowPowerAudioSink回调函数指针的集合。  应用需注册此实例结构体到[OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)实例中，并对回调上报的信息进行处理，保证LowPowerAudioSink的正常运行。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*OH\_LowPowerAudioSink\_OnError)(OH\_LowPowerAudioSink\* sink, OH\_AVErrCode errCode, const char\* errorMsg, void\* userData)](capi-lowpower-audio-sink-base-h.md#oh_lowpoweraudiosink_onerror) | OH\_LowPowerAudioSink\_OnError | LowPowerAudioSink发生错误时调用该方法。 |
| [typedef void (\*OH\_LowPowerAudioSink\_OnPositionUpdated)(OH\_LowPowerAudioSink\* sink, int64\_t currentPosition, void\* userData)](capi-lowpower-audio-sink-base-h.md#oh_lowpoweraudiosink_onpositionupdated) | OH\_LowPowerAudioSink\_OnPositionUpdated | LowPowerAudioSink进度更新时调用该方法。 |
| [typedef void (\*OH\_LowPowerAudioSink\_OnDataNeeded)(OH\_LowPowerAudioSink\* sink, OH\_AVSamplesBuffer\* samples, void\* userData)](capi-lowpower-audio-sink-base-h.md#oh_lowpoweraudiosink_ondataneeded) | OH\_LowPowerAudioSink\_OnDataNeeded | LowPowerAudioSink需要数据时调用该方法。 |
| [typedef void (\*OH\_LowPowerAudioSink\_OnInterrupted)(OH\_LowPowerAudioSink\* sink, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint, void\* userData)](capi-lowpower-audio-sink-base-h.md#oh_lowpoweraudiosink_oninterrupted) | OH\_LowPowerAudioSink\_OnInterrupted | LowPowerAudioSink焦点打断时调用该方法。 |
| [typedef void (\*OH\_LowPowerAudioSink\_OnDeviceChanged)(OH\_LowPowerAudioSink\* sink, OH\_AudioStream\_DeviceChangeReason reason, void\* userData)](capi-lowpower-audio-sink-base-h.md#oh_lowpoweraudiosink_ondevicechanged) | OH\_LowPowerAudioSink\_OnDeviceChanged | LowPowerAudioSink设备切换时调用该方法。 |
| [typedef void (\*OH\_LowPowerAudioSink\_OnEos)(OH\_LowPowerAudioSink\* sink, void\* userData)](capi-lowpower-audio-sink-base-h.md#oh_lowpoweraudiosink_oneos) | OH\_LowPowerAudioSink\_OnEos | LowPowerAudioSink播放完成时调用该方法。 |

## 函数说明

### OH\_LowPowerAudioSink\_OnError()

```c
typedef void (*OH_LowPowerAudioSink_OnError)(OH_LowPowerAudioSink* sink, OH_AVErrCode errCode, const char* errorMsg, void* userData)
```

**描述**

LowPowerAudioSink发生错误时调用该方法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* sink | 指向OH\_LowPowerAudioSink实例的指针。 |
| [OH\_AVErrCode](capi-native-averrors-h.md#oh_averrcode) errCode | 发生错误时上报的错误码。 |
| const char\* errorMsg | 错误描述信息。 |
| void\* userData | 用户自定义数据。 |

### OH\_LowPowerAudioSink\_OnPositionUpdated()

```c
typedef void (*OH_LowPowerAudioSink_OnPositionUpdated)(OH_LowPowerAudioSink* sink, int64_t currentPosition, void* userData)
```

**描述**

LowPowerAudioSink进度更新时调用该方法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* sink | 指向OH\_LowPowerAudioSink实例的指针。 |
| int64\_t currentPosition | 返回服务当前播放的进度值。单位为毫秒。 |
| void\* userData | 用户自定义数据。 |

### OH\_LowPowerAudioSink\_OnDataNeeded()

```c
typedef void (*OH_LowPowerAudioSink_OnDataNeeded)(OH_LowPowerAudioSink* sink, OH_AVSamplesBuffer* samples, void* userData)
```

**描述**

LowPowerAudioSink需要数据时调用该方法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* sink | 指向OH\_LowPowerAudioSink实例的指针。 |
| [OH\_AVSamplesBuffer](capi-avsinkbase-oh-avsamplesbuffer.md)\* samples | 即将写入的AVSamplesBuffer实例。 |
| void\* userData | 用户自定义数据。 |

### OH\_LowPowerAudioSink\_OnInterrupted()

```c
typedef void (*OH_LowPowerAudioSink_OnInterrupted)(OH_LowPowerAudioSink* sink, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint, void* userData)
```

**描述**

LowPowerAudioSink焦点打断时调用该方法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* sink | 指向OH\_LowPowerAudioSink实例的指针。 |
| [OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype) type | 音频打断类型。 |
| [OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint) hint | 音频打断提示类型。 |
| void\* userData | 用户自定义数据。 |

### OH\_LowPowerAudioSink\_OnDeviceChanged()

```c
typedef void (*OH_LowPowerAudioSink_OnDeviceChanged)(OH_LowPowerAudioSink* sink, OH_AudioStream_DeviceChangeReason reason, void* userData)
```

**描述**

LowPowerAudioSink设备切换时调用该方法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* sink | 指向OH\_LowPowerAudioSink实例的指针。 |
| [OH\_AudioStream\_DeviceChangeReason](capi-native-audiostream-base-h.md#oh_audiostream_devicechangereason) reason | 输出设备发生变化的原因。 |
| void\* userData | 用户自定义数据。 |

### OH\_LowPowerAudioSink\_OnEos()

```c
typedef void (*OH_LowPowerAudioSink_OnEos)(OH_LowPowerAudioSink* sink, void* userData)
```

**描述**

LowPowerAudioSink播放完成时调用该方法。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_LowPowerAudioSink](capi-lowpoweraudiosink-oh-lowpoweraudiosink.md)\* sink | 指向OH\_LowPowerAudioSink实例的指针。 |
| void\* userData | 用户自定义数据。 |
