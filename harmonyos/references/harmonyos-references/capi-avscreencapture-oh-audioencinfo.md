---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioencinfo
title: OH_AudioEncInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioEncInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:02:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a4a44f3b9298c0415ef225d09091edc8eb1575e9288130da739c8602e5667a22
---

```c
typedef struct OH_AudioEncInfo {...} OH_AudioEncInfo
```

## 概述

音频编码信息。

用于配置屏幕录制场景下的音频编码参数，包括音频编码比特率和音频编码格式。通过设置这些参数，开发者可以控制音频的质量和文件大小，适用于需要在屏幕录制场景中指定音频编码质量和编码方式的场景。支持的编码格式详见[OH\_AudioCodecFormat](capi-native-avscreen-capture-base-h.md#oh_audiocodecformat)枚举定义。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t audioBitrate | 音频编码比特率，用于设置音频编码的输出比特率。取值范围需参考具体编码格式支持的比特率范围，常见取值有48000、96000和128000。单位为比特每秒（bit/s）。超出编码格式支持范围时可能导致编码失败。 |
| [OH\_AudioCodecFormat](capi-native-avscreen-capture-base-h.md#oh_audiocodecformat) audioCodecformat | 音频编码格式，用于指定屏幕录制时音频数据所采用的编码格式。不同编码格式对应不同的编码算法、压缩效率、兼容性和质量表现，选择合适的编码格式会影响音频文件的大小、播放兼容性和音质。支持的编码格式详见[OH\_AudioCodecFormat](capi-native-avscreen-capture-base-h.md#oh_audiocodecformat)枚举定义。 |
