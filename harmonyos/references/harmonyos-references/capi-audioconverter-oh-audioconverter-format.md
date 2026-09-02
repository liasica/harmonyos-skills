---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-audioconverter-oh-audioconverter-format
title: OH_AudioConverter_Format
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioConverter_Format
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:45b511c25c6c5aca932351f1f136e5c945160d9afb64e558f99e6a8cd4304494
---

```c
typedef struct OH_AudioConverter_Format {...} OH_AudioConverter_Format
```

## 概述

定义音频转换器格式数据结构，用于描述基本音频格式。

**起始版本：** 26.0.0

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_converter.h](capi-native-audio-converter-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_Audio\_EncodingType](capi-native-audio-suite-base-h.md#oh_audio_encodingtype) encodingType | 音频编码格式类型。  **起始版本：** 26.0.0 |
| [OH\_Audio\_SampleRate](capi-native-audio-suite-base-h.md#oh_audio_samplerate) samplingRate | 音频采样率。  **起始版本：** 26.0.0 |
| [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout) channelLayout | 音频声道布局。  **起始版本：** 26.0.0 |
| [OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat) sampleFormat | 音频采样格式。  **起始版本：** 26.0.0 |
