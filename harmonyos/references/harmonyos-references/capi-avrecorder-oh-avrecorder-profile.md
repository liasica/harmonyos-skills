---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avrecorder-oh-avrecorder-profile
title: OH_AVRecorder_Profile
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AVRecorder_Profile
category: harmonyos-references
scraped_at: 2026-09-02T15:02:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9aec4e8fdb9a9c8b04e6ba53fbcbbdf89f254d7b5bbeb7d6ddfecbd95be36754
---

```c
typedef struct OH_AVRecorder_Profile {/* 成员变量详见汇总部分 */} OH_AVRecorder_Profile;
```

## 概述

定义音视频录制的详细参数。通过配置音频/视频编码格式、比特率、采样率、帧率、分辨率、容器格式、HDR录制、是否启用时域可分层视频编码功能等参数，可以灵活控制录制质量和录制文件大小，适用于需要自定义录制质量、选择录制内容类型（仅音频/仅视频/音视频同时录制）、启用HDR录制或时域可分层视频编码功能的场景。

通过参数设置可以选择仅录制音频或视频，或者同时录制音视频：

1. 当 audioBitrate 或 audioChannels 为 0 时，不录制音频。
2. 当 videoFrameWidth 或 videoFrameHeight 为 0 时，不录制视频。

各参数的范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)。

**起始版本：** 18

**相关模块：** [AVRecorder](capi-avrecorder.md)

**所在头文件：** [avrecorder\_base.h](capi-avrecorder-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t audioBitrate | 音频编码比特率。单位为比特每秒（bit/s）。数值越大音频质量越好，但文件也越大。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，默认值为0，取值为0时不录制音频，超出有效范围时录制失败。 |
| int32\_t audioChannels | 音频声道数。声道数越多音频空间感越强，但文件也越大。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，默认值为0，取值为0时不录制音频，超出有效范围时录制失败。 |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) audioCodec | 音频编码器MIME类型。选择不同的音频编码器将影响录制的音频质量、文件大小和兼容性，各编码器类型详见[OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype)。仅在录制音频时有效。 |
| int32\_t audioSampleRate | 音频采样率。单位为赫兹（Hz）。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，采样率越高音频质量越好，但文件也越大，超出有效范围时录制失败。默认值为0。仅在录制音频时有效。 |
| [OH\_AVRecorder\_ContainerFormatType](capi-avrecorder-base-h.md#oh_avrecorder_containerformattype) fileFormat | 容器格式类型。选择不同的容器格式将决定录制文件的存储格式和支持的音视频编码类型，各格式类型详见[OH\_AVRecorder\_ContainerFormatType](capi-avrecorder-base-h.md#oh_avrecorder_containerformattype)。 |
| int32\_t videoBitrate | 视频编码比特率。单位为比特每秒（bit/s）。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，数值越大视频质量越好，但文件也越大。低比特率适合网络传输或存储受限场景，高比特率适合本地高质量存储场景。超出有效范围时录制失败。默认值为0。仅在录制视频时有效。 |
| [OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype) videoCodec | 视频编码器MIME类型。选择不同的视频编码器将影响录制的视频压缩效率、画质和兼容性，各编码器类型详见[OH\_AVRecorder\_CodecMimeType](capi-avrecorder-base-h.md#oh_avrecorder_codecmimetype)。当isHdr为true时，videoCodec必须为AVRECORDER\_VIDEO\_HEVC。仅在录制视频时有效。 |
| int32\_t videoFrameWidth | 视频帧宽度。单位为像素（px）。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，数值越大视频清晰度越高，但文件也越大。默认值为0，取值为0时不录制视频。超出有效范围时录制失败。 |
| int32\_t videoFrameHeight | 视频帧高度。单位为像素（px）。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，数值越大视频清晰度越高，但文件也越大。默认值为0，取值为0时不录制视频。超出有效范围时录制失败。 |
| int32\_t videoFrameRate | 视频帧率。帧率越高视频越流畅，但文件也越大。单位为帧每秒（fps）。取值范围请参见[AVRecorderProfile](arkts-apis-media-i.md#avrecorderprofile9)，超出有效范围时录制失败。默认值为0。仅在录制视频时有效。 |
| bool isHdr | 是否录制HDR视频。  true表示启用HDR编码，此时videoCodec必须为AVRECORDER\_VIDEO\_HEVC，否则录制会准备失败；false表示不启用HDR编码，对编码格式无要求。  默认值为false。仅在录制视频时有效。 |
| bool enableTemporalScale | 是否启用时域可分层视频编码功能。  true表示编码输出的码流中时域增强层帧可被跳过不编码，适用于需要根据网络带宽或设备性能动态调整编码帧率的场景（如视频直播、视频会议等），false表示编码输出的码流中所有帧均需编码。详情请参考[时域可分层视频编码](../harmonyos-guides/video-encoding-temporal-scalability.md)。  默认值为false。仅在录制视频时有效。 |
