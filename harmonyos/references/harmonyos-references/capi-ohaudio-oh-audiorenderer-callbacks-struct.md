---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct
title: OH_AudioRenderer_Callbacks_Struct
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioRenderer_Callbacks_Struct
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d01a97f470ac4e8a7644bd94342a8a2b611520c1e702e0393aab68810e920343
---

```c
typedef struct OH_AudioRenderer_Callbacks_Struct {...} OH_AudioRenderer_Callbacks
```

## 概述

声明输出音频流的回调函数指针。

为了避免不可预期的行为，在设置音频回调函数时，请确保该结构体的每一个成员变量都被自定义的回调函数或空指针初始化。

可参考[推荐使用OHAudio开发音频播放功能(C/C++)](../harmonyos-guides/using-ohaudio-for-playback.md)。

**起始版本：** 10

**废弃版本：** 20

**替代接口：**

请分别使用以下回调类型替代：

[OH\_AudioRenderer\_OnWriteDataCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)、[OH\_AudioRenderer\_OutputDeviceChangeCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_outputdevicechangecallback)、[OH\_AudioRenderer\_OnInterruptCallback](capi-native-audiorenderer-h.md#oh_audiorenderer_oninterruptcallback) 以及 [OH\_AudioRenderer\_OnErrorCallback](capi-native-audiorenderer-h.md#oh_audiorenderer_onerrorcallback)。

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audiostream\_base.h](capi-native-audiostream-base-h.md)

## 汇总

### 成员函数

| 名称 | 描述 |
| --- | --- |
| [int32\_t (\*OH\_AudioRenderer\_OnWriteData)(OH\_AudioRenderer\* renderer, void\* userData, void\* buffer, int32\_t length)](capi-ohaudio-oh-audiorenderer-callbacks-struct.md#oh_audiorenderer_onwritedata) | 该函数指针将指向用于写入音频数据的回调函数。 |
| [int32\_t (\*OH\_AudioRenderer\_OnStreamEvent)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Event event)](capi-ohaudio-oh-audiorenderer-callbacks-struct.md#oh_audiorenderer_onstreamevent) | 该函数指针将指向用于处理音频播放流事件的回调函数。 |
| [int32\_t (\*OH\_AudioRenderer\_OnInterruptEvent)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioInterrupt\_ForceType type, OH\_AudioInterrupt\_Hint hint)](capi-ohaudio-oh-audiorenderer-callbacks-struct.md#oh_audiorenderer_oninterruptevent) | 该函数指针将指向用于处理音频播放中断事件的回调函数。 |
| [int32\_t (\*OH\_AudioRenderer\_OnError)(OH\_AudioRenderer\* renderer, void\* userData, OH\_AudioStream\_Result error)](capi-ohaudio-oh-audiorenderer-callbacks-struct.md#oh_audiorenderer_onerror) | 该函数指针将指向用于处理音频播放错误结果的回调函数。 |

## 成员函数说明

**说明** 

以下回调接口的返回值没有枚举定义，当前版本实现并不按返回值区分处理，但为保证后续版本可扩展，默认使用0。

### OH\_AudioRenderer\_OnWriteData()

```c
int32_t (*OH_AudioRenderer_OnWriteData)(OH_AudioRenderer* renderer, void* userData, void* buffer, int32_t length)
```

**描述**

该函数指针将指向用于写入音频数据的回调函数。

回调函数仅用来写入音频数据，请勿在回调函数中调用AudioRenderer相关接口。

回调函数结束后，音频服务会将buffer数据放入队列中等待播放，因此请勿在回调外再次更改buffer指向的数据，且务必保证往buffer填满length长度的待播放数据，否则会导致音频服务播放杂音。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioRenderer\_OnWriteDataCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_onwritedatacallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| void\* buffer | 指向播放数据存储区域，用于应用填充播放数据。 |
| int32\_t length | buffer的长度，单位为字节（Byte）。 |

### OH\_AudioRenderer\_OnStreamEvent()

```c
int32_t (*OH_AudioRenderer_OnStreamEvent)(OH_AudioRenderer* renderer, void* userData, OH_AudioStream_Event event)
```

**描述**

该函数指针将指向用于处理音频播放流事件的回调函数。

OH\_AudioRenderer\_OnStreamEvent当前无触发场景，为预留接口。从API version 11开始，开发者如果需要监听设备变化，可直接使用[OH\_AudioRenderer\_OutputDeviceChangeCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_outputdevicechangecallback)替代。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioRenderer\_OutputDeviceChangeCallback](capi-native-audiostream-base-h.md#oh_audiorenderer_outputdevicechangecallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_Event](capi-native-audiostream-base-h.md#oh_audiostream_event) event | 音频事件。 |

### OH\_AudioRenderer\_OnInterruptEvent()

```c
int32_t (*OH_AudioRenderer_OnInterruptEvent)(OH_AudioRenderer* renderer, void* userData, OH_AudioInterrupt_ForceType type, OH_AudioInterrupt_Hint hint)
```

**描述**

该函数指针将指向用于处理音频播放中断事件的回调函数。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioRenderer\_OnInterruptCallback](capi-native-audiorenderer-h.md#oh_audiorenderer_oninterruptcallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioInterrupt\_ForceType](capi-native-audiostream-base-h.md#oh_audiointerrupt_forcetype) type | 音频中断类型。 |
| [OH\_AudioInterrupt\_Hint](capi-native-audiostream-base-h.md#oh_audiointerrupt_hint) hint | 音频中断提示类型。 |

### OH\_AudioRenderer\_OnError()

```c
int32_t (*OH_AudioRenderer_OnError)(OH_AudioRenderer* renderer, void* userData, OH_AudioStream_Result error)
```

**描述**

该函数指针将指向用于处理音频播放错误结果的回调函数。

**起始版本：** 10

**废弃版本：** 20

**替代接口：** [OH\_AudioRenderer\_OnErrorCallback](capi-native-audiorenderer-h.md#oh_audiorenderer_onerrorcallback)

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AudioRenderer](capi-ohaudio-oh-audiorendererstruct.md)\* renderer | 指向[OH\_AudioStreamBuilder\_GenerateRenderer](capi-native-audiostreambuilder-h.md#oh_audiostreambuilder_generaterenderer)创建的音频流实例。 |
| void\* userData | 指向应用自定义的数据存储区域。 |
| [OH\_AudioStream\_Result](capi-native-audiostream-base-h.md#oh_audiostream_result) error | 音频播放错误结果，可能为AUDIOSTREAM\_ERROR\_INVALID\_PARAM、AUDIOSTREAM\_ERROR\_ILLEGAL\_STATE或者AUDIOSTREAM\_ERROR\_SYSTEM。 |
