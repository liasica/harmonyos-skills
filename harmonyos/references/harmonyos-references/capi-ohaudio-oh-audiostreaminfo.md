---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiostreaminfo
title: OH_AudioStreamInfo
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioStreamInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:11:53+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f06121d488d1fdc16224d33678d72041d3c2f417f1758b59dce2d453f053cb60
---

```
1. typedef struct OH_AudioStreamInfo {...} OH_AudioStreamInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义音频流信息，用于描述基本音频格式。

**起始版本：** 19

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audiostream\_base.h](capi-native-audiostream-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t samplingRate | 音频流采样率。 |
| [OH\_AudioChannelLayout](capi-native-audio-channel-layout-h.md#oh_audiochannellayout) channelLayout | 音频流声道布局。 |
| [OH\_AudioStream\_EncodingType](capi-native-audiostream-base-h.md#oh_audiostream_encodingtype) encodingType | 音频流编码类型。 |
| [OH\_AudioStream\_SampleFormat](capi-native-audiostream-base-h.md#oh_audiostream_sampleformat) sampleFormat | 音频流采样格式。 |
