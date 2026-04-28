---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-avscreencapture-oh-audioinfo
title: OH_AudioInfo
breadcrumb: API参考 > 媒体 > Media Kit（媒体服务） > C API > 结构体 > OH_AudioInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:14:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0d39e620c8836fa85fb37522150b571a36fa5c17ad8242f1b90f7c477805803b
---

```
1. typedef struct OH_AudioInfo {...} OH_AudioInfo
```

## 概述

PhonePC/2in1TabletTV

音频信息。

同时采集音频麦克风和音频内录数据时，两路音频的audioSampleRate和audioChannels采样参数需要相同。

**起始版本：** 10

**相关模块：** [AVScreenCapture](capi-avscreencapture.md)

**所在头文件：** [native\_avscreen\_capture\_base.h](capi-native-avscreen-capture-base-h.md)

## 汇总

PhonePC/2in1TabletTV

### 成员变量

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md) micCapInfo | 音频麦克风采样信息。 |
| [OH\_AudioCaptureInfo](capi-avscreencapture-oh-audiocaptureinfo.md) innerCapInfo | 音频内录采样信息。 |
| [OH\_AudioEncInfo](capi-avscreencapture-oh-audioencinfo.md) audioEncInfo | 音频编码信息，原始码流时不需要设置。 |
