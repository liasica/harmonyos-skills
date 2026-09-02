---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-audioformat
title: OH_AudioFormat
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioFormat
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c3596a7bed53a6f0320d07bbbd3f175afd56d048ed5ad6b3c1b64750c0f82c9d
---

```c
typedef struct {...} OH_AudioFormat
```

## 概述

定义音频编创的音频流信息，用于描述基本音频格式。

**起始版本：** 22

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_Audio\_SampleRate](capi-native-audio-suite-base-h.md#oh_audio_samplerate) samplingRate | 音频流采样率。 |
| [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout) channelLayout | 音频流声道布局。  在API版本26.0.0之前，仅支持CH\_LAYOUT\_MONO和CH\_LAYOUT\_STEREO。  在API版本26.0.0及以后，支持CH\_LAYOUT\_MONO、CH\_LAYOUT\_STEREO、CH\_LAYOUT\_STEREO\_DOWNMIX、CH\_LAYOUT\_2POINT1、CH\_LAYOUT\_3POINT0、CH\_LAYOUT\_SURROUND、CH\_LAYOUT\_3POINT1、CH\_LAYOUT\_4POINT0、CH\_LAYOUT\_QUAD\_SIDE、CH\_LAYOUT\_QUAD、CH\_LAYOUT\_2POINT0POINT2、CH\_LAYOUT\_4POINT1、CH\_LAYOUT\_5POINT0、CH\_LAYOUT\_5POINT0\_BACK、CH\_LAYOUT\_2POINT1POINT2、CH\_LAYOUT\_3POINT0POINT2、CH\_LAYOUT\_5POINT1、CH\_LAYOUT\_5POINT1\_BACK、CH\_LAYOUT\_6POINT0、CH\_LAYOUT\_3POINT1POINT2、CH\_LAYOUT\_6POINT0\_FRONT、CH\_LAYOUT\_HEXAGONAL、CH\_LAYOUT\_6POINT1、CH\_LAYOUT\_6POINT1\_BACK、CH\_LAYOUT\_6POINT1\_FRONT、CH\_LAYOUT\_7POINT0、CH\_LAYOUT\_7POINT0\_FRONT、CH\_LAYOUT\_7POINT1、CH\_LAYOUT\_OCTAGONAL、CH\_LAYOUT\_5POINT1POINT2、CH\_LAYOUT\_7POINT1\_WIDE、CH\_LAYOUT\_7POINT1\_WIDE\_BACK、CH\_LAYOUT\_AMB\_ORDER1\_ACN\_N3D、CH\_LAYOUT\_AMB\_ORDER1\_ACN\_SN3D、CH\_LAYOUT\_AMB\_ORDER1\_FUMA、CH\_LAYOUT\_AMB\_ORDER2\_ACN\_N3D、CH\_LAYOUT\_AMB\_ORDER2\_ACN\_SN3D、CH\_LAYOUT\_AMB\_ORDER2\_FUMA、CH\_LAYOUT\_AMB\_ORDER3\_ACN\_N3D、CH\_LAYOUT\_AMB\_ORDER3\_ACN\_SN3D、CH\_LAYOUT\_AMB\_ORDER3\_FUMA。 |
| uint32\_t channelCount | 音频流声道数。  在API版本26.0.0之前，仅支持1声道和2声道。  在API版本26.0.0及以后，支持1至9声道及16声道。 |
| [OH\_Audio\_EncodingType](capi-native-audio-suite-base-h.md#oh_audio_encodingtype) encodingType | 音频流编码类型。 |
| [OH\_Audio\_SampleFormat](capi-native-audio-suite-base-h.md#oh_audio_sampleformat) sampleFormat | 音频流采样格式。 |
