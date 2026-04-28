---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiocapturer-callbacks-struct
title: OH_AudioCapturer_Callbacks_Struct
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioCapturer_Callbacks_Struct
category: harmonyos-references
scraped_at: 2026-04-28T08:11:54+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:23ff170e89be2a8b8776eead0988af46413d553f78c8ec642bc6d5cd0cfa0a8a
---

```
1. typedef struct OH_AudioCapturer_Callbacks_Struct {...} OH_AudioCapturer_Callbacks
```

## 概述

PhonePC/2in1TabletTVWearable

声明输入音频流的回调函数指针。

为了避免不可预期的行为，在设置音频回调函数时，请确保该结构体的每一个成员变量都被自定义的回调方法或空指针初始化。可参考[推荐使用OHAudio开发音频录制功能(C/C++)](../harmonyos-guides/using-ohaudio-for-recording.md)。

**起始版本：** 10

**废弃版本：** 20

**替代接口：**

请分别使用以下回调类型替代：

[OH\_AudioCapturer\_OnReadDataCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onreaddatacallback)、 [OH\_AudioCapturer\_OnDeviceChangeCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_ondevicechangecallback)、 [OH\_AudioCapturer\_OnInterruptCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_oninterruptcallback) 以及 [OH\_AudioCapturer\_OnErrorCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onerrorcallback)。

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audiostream\_base.h](capi-native-audiostream-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*OH\_AudioCapturer\_OnReadData)(OH\_AudioCapturer\* capturer,void\* userData,void\* buffer,int32\_t length)](capi-ohaudio-oh-audiocapturer-callbacks-struct.md#oh_audiocapturer_onreaddata) | 该函数指针将指向用于读取音频数据的回调函数。 |
| [int32\_t (\*OH\_AudioCapturer\_OnStreamEvent)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioStream\_Event event)](capi-ohaudio-oh-audiocapturer-callbacks-struct.md#oh_audiocapturer_onstreamevent) | 该函数指针将指向用于处理音频录制流事件的回调函数。 |
| [int32\_t (\*OH\_AudioCapturer\_OnInterruptEvent)(OH\_AudioCapturer\* capturer,void\* userData,OH\_AudioInterrupt\_ForceType type,OH\_AudioInterrupt\_Hint hint)](capi-ohaudio-oh-audiocapturer-callbacks-struct.md#oh_audiocapturer_oninterruptevent) | 该函数指针将指向用于处理音频录制中断事件的回调函数。 |
| [int32\_t (\*OH\_AudioCapturer\_OnError)(OH\_AudioCapturer\* capturer, void\* userData, OH\_AudioStream\_Result error)](capi-ohaudio-oh-audiocapturer-callbacks-struct.md#oh_audiocapturer_onerror) | 该函数指针将指向用于处理音频录制错误结果的回调函数。 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

说明

以下回调接口的返回值没有枚举定义，当前版本实现并不按返回值区分处理，但为保证后续版本可扩展，默认使用0。

### OH\_AudioCapturer\_OnReadData()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*OH_AudioCapturer_OnReadData)(OH_AudioCapturer* capturer,void* userData,void* buffer,int32_t length)
```

**描述**

该函数指针将指向用于读取音频数据的回调函数。

回调函数仅用来读取音频数据，请勿在回调函数中调用AudioCapturer相关接口。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioCapturer\_OnReadDataCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onreaddatacallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| void\* buffer | 指向录制数据存储区域，用于应用读取录制数据。 |
| int32\_t length | buffer的长度。 |

### OH\_AudioCapturer\_OnStreamEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*OH_AudioCapturer_OnStreamEvent)(OH_AudioCapturer* capturer,void* userData,OH_AudioStream_Event event)
```

**描述**

该函数指针将指向用于处理音频录制流事件的回调函数。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioCapturer\_OnDeviceChangeCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_ondevicechangecallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_Event](capi-native-audiostream-base-h.md#oh_audiostream_event) event | 音频事件。 |

### OH\_AudioCapturer\_OnInterruptEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*OH_AudioCapturer_OnInterruptEvent)(OH_AudioCapturer* capturer,void* userData,OH_AudioInterrupt_ForceType type,OH_AudioInterrupt_Hint hint)
```

**描述**

该函数指针将指向用于处理音频录制中断事件的回调函数。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioCapturer\_OnInterruptCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_oninterruptcallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype) type | 音频中断类型。 |
| [OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint) hint | 音频中断提示类型。 |

### OH\_AudioCapturer\_OnError()

PhonePC/2in1TabletTVWearable

```
1. int32_t (*OH_AudioCapturer_OnError)(OH_AudioCapturer* capturer, void* userData, OH_AudioStream_Result error)
```

**描述**

该函数指针将指向用于处理音频录制错误结果的回调函数。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioCapturer\_OnErrorCallback](capi-native-audiocapturer-h.md#oh_audiocapturer_onerrorcallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioCapturer](capi-ohaudio-oh-audiocapturerstruct.md)\* capturer | 指向[OH\_AudioStreamBuilder\_GenerateCapturer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generatecapturer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) error | 音频录制错误结果，可能为AUDIOSTREAM\_ERROR\_INVALID\_PARAM、AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE或者 AUDIOSTREAM\_ERROR\_SYSTEM。 |
