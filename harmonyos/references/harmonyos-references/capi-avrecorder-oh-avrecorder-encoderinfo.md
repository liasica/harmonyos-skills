---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-encoderinfo
title: OH_AVRecorder_EncoderInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_EncoderInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:14:00+08:00
doc_updated_at: 2026-04-02
content_hash: sha256:abd33b833a8c91d781ffdda6ec00bd896302db92b24266415f65600a2a031792
---

```
1. typedef struct OH_AVRecorder_EncoderInfo {...} OH_AVRecorder_EncoderInfo
```

## 概述

PhonePC/2in1TabletTVWearable

提供编码器信息。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) mimeType | 编码器MIME类型名称。 |
| char\* type | 编码器类型，audio表示音频编码器，video表示视频编码器。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) bitRate | 比特率，包含该编码器的最大和最小值。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) frameRate | 视频帧率，包含帧率的最大和最小值，仅视频编码器拥有。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) width | 视频帧的宽度，包含宽度的最大和最小值，仅视频编码器拥有。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) height | 视频帧的高度，包含高度的最大和最小值，仅视频编码器拥有。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) channels | 音频采集声道数，包含声道数的最大和最小值，仅音频编码器拥有。 |
| int32\_t\* sampleRate | 音频采样率列表，包含所有可以使用的音频采样率值，仅音频编码器拥有。 |
| int32\_t sampleRateLen | 音频采样率列表长度。 |
