---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audiocaptureinfo
title: OH_AudioCaptureInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioCaptureInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:14:01+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b91a6a0690ec67b4e84850e8c57df7f55d91d3a21cb46e1a9972c806bd47873a
---

```
1. typedef struct OH_AudioCaptureInfo {...} OH_AudioCaptureInfo
```

## 概述

PhonePC/2in1TabletTV

音频采样信息。

当audioSampleRate和audioChannels同时为0时，忽略该类型音频相关参数，不录制该类型音频数据。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| int32\_t audioSampleRate | 音频采样率，支持列表请查阅Audio Kit的[AudioSamplingRate](arkts-apis-audio-e.md#audiosamplingrate8)。 |
| int32\_t audioChannels | 音频声道数。 |
| [OH\_AudioCaptureSourceType](capi-native-avscreen-capture-base-h.md#oh_audiocapturesourcetype) audioSource | 音频源。 |
