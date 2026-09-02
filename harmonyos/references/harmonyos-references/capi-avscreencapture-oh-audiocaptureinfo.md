---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo
title: OH_AudioCaptureInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioCaptureInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:979bd65febdfc54b4325f36e0f87bb441ec26073b03944d9586c417b2f26db29
---

```c
typedef struct OH_AudioCaptureInfo {...} OH_AudioCaptureInfo
```

## 概述

音频采样信息。

用于配置屏幕录制中的音频采集参数，包括采样率、声道数和音频源类型。开发者可通过设置audioSampleRate和audioChannels参数来控制录制音频的质量和声道布局，适用于屏幕录制时需要采集系统音频或麦克风音频的场景。

当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t audioSampleRate | 音频采样率，支持列表请查阅Audio Kit的[AudioSamplingRate](arkts-apis-audio-e.md#audiosamplingrate8)。单位为赫兹（Hz）。当audioSampleRate与audioChannels同时为0时，将忽略该类型音频相关参数。 |
| int32\_t audioChannels | 音频声道数，用于配置音频录制的声道数量。具体支持的范围请参考相关音频设备的能力[AudioChannel](arkts-apis-audio-e.md#audiochannel8)。当audioSampleRate与audioChannels同时为0时，将忽略该类型音频相关参数。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) audioSource | 音频源，用于指定录制的音频来源，如系统音频或麦克风录音等。可选值请参考[OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype)。 |
