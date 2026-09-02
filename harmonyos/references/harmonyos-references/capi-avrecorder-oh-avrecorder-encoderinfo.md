---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-encoderinfo
title: OH_AVRecorder_EncoderInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_EncoderInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:89d3fbe88774777a2958daa24f67d5673596fd6ce83b06556e7ae659db14b9a4
---

```c
typedef struct OH_AVRecorder_EncoderInfo {...} OH_AVRecorder_EncoderInfo;
```

## 概述

提供AVRecorder编码器能力信息，包括编码器的MIME类型、比特率范围、帧率范围等参数，适用于在录制前查询和选择合适的音频或视频编码器配置的场景，帮助开发者根据编码器能力参数选择最优编码配置。开发者可通过[OH\_AVRecorder\_GetAvailableEncoder](capi-avrecorder-h.md#oh_avrecorder_getavailableencoder)接口获取该结构体对象。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) mimeType | 编码器MIME类型。值与type对应，type为audio时值为音频MIME类型，type为video时值为视频MIME类型。 |
| char\* type | 编码器类型，audio表示音频编码器，video表示视频编码器。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) bitRate | 编码器支持的比特率范围，单位为比特每秒（bit/s）。音频和视频编码器均适用。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) frameRate | 编码器支持的视频帧率范围，单位为帧每秒（fps）。仅适用于视频编码器。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) width | 编码器支持的视频帧宽度范围，单位为像素（px）。仅适用于视频编码器。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) height | 编码器支持的视频帧高度范围，单位为像素（px）。仅适用于视频编码器。 |
| [OH\_AVRecorder\_Range](capi-avrecorder-oh-avrecorder-range.md) channels | 编码器支持的音频声道数的范围，取值由设备编码器能力决定，常见取值为1（单声道）或2（立体声）。仅适用于音频编码器。 |
| int32\_t\* sampleRate | 音频采样率列表，包含所有支持的音频采样率值，取值由设备编码器能力决定，常见取值如8000、16000、44100、48000等，单位为赫兹（Hz）。与sampleRateLen字段配合使用，sampleRateLen表示该列表的长度。仅适用于音频编码器。 |
| int32\_t sampleRateLen | 音频采样率列表长度，取值为大于0的整数，与sampleRate字段配合使用，表示sampleRate数组中元素的个数。仅适用于音频编码器。 |
