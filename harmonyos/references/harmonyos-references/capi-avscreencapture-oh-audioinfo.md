---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo
title: OH_AudioInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioInfo
category: harmonyos-references
scraped_at: 2026-10-27T07:43:24+08:00
doc_updated_at: 2026-10-26
content_hash: sha256:e2e8018cb3ff387bee74ade77aafe03f9f80281c16914931d6b185c98169b351
---

```c
typedef struct OH_AudioInfo {...} OH_AudioInfo
```

## 概述

音频信息。

OH\_AudioInfo作为OH\_AVScreenCaptureConfig的音频配置成员，包含麦克风采集信息、内录采集信息和音频编码信息三个部分，开发者需根据采集场景选择配置麦克风采集信息或内录采集信息，并在需要编码输出时配置音频编码信息。适用于需要在屏幕录制中采集音频数据的场景。

同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采集参数需要相同，因为两路音频数据将合并为同一音频流输出，采集参数不一致会导致音频同步异常或采集失败。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md) micCapInfo | 音频麦克风采集信息，用于配置麦克风音频采集的采集参数。 |
| [OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md) innerCapInfo | 音频内录采集信息，用于配置内录音频采集的采集参数。 |
| [OH\_AudioEncInfo](capi-avscreencapture-oh-audioencinfo.md) audioEncInfo | 音频编码信息。采集原始码流时不需要设置编码参数。未设置时默认不进行音频编码。 |
