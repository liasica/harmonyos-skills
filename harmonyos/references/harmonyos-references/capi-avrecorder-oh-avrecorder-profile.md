---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-profile
title: OH_AVRecorder_Profile
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Profile
category: harmonyos-references
scraped_at: 2026-04-28T08:13:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fe0e2a82f5448f47d206b0b33c26ee7847b28702c8b9f1c24554ee1d4016ca44
---

```
1. typedef struct OH_AVRecorder_Profile {...} OH_AVRecorder_Profile
```

## 概述

PhonePC/2in1TabletTVWearable

定义音视频录制的详细参数。

通过参数设置可以选择只录制音频或只录制视频：

1. 当 audioBitrate 或 audioChannels 为 0 时，不录制音频。
2. 当 videoFrameWidth 或 videoFrameHeight 为 0 时，不录制视频。

各参数的范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t audioBitrate | 音频比特率。 |
| int32\_t audioChannels | 音频通道数。 |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) audioCodec | 音频编码格式。 |
| int32\_t audioSampleRate | 音频采样率。 |
| [OH\_AVRecorder\_ContainerFormatType](capi-avrecorder-base-h.md#oh_avrecorder_containerformattype) fileFormat | 输出文件格式。 |
| int32\_t videoBitrate | 视频比特率。 |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) videoCodec | 视频编码格式。 |
| int32\_t videoFrameWidth | 视频宽度。 |
| int32\_t videoFrameHeight | 视频高度。 |
| int32\_t videoFrameRate | 视频帧率。 |
| bool isHdr | 是否录制HDR视频。  true表示录制HDR视频，false表示不录制HDR视频。  默认是false。 |
| bool enableTemporalScale | 是否支持时域分层编码功能。  true表示编码输出的码流中部分帧可以支持跳过不编码，false表示编码输出的码流中所有帧不支持跳过不编码，详情请参考[时域可分层视频编码](../harmonyos-guides/video-encoding-temporal-scalability.md)。  默认是false。 |
