---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audioaccessorynoisereductioncapability
title: OH_AudioAccessoryNoiseReductionCapability
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioAccessoryNoiseReductionCapability
category: harmonyos-references
scraped_at: 2026-11-12T09:56:23+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b7adffb90702a5d924032215caeb67687e0bfb8afc387bc9363089ed58b99bf8
---

```c
typedef struct {...} OH_AudioAccessoryNoiseReductionCapability
```

## 概述

定义音频配件的降噪能力。

**起始版本：** 26.0.0

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audio\_accessory\_common.h](capi-native-audio-accessory-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t structSize | 结构体大小，单位为字节（Byte）。  调用方需初始化此字段。  系统通过此字段校验结构体大小。 |
| const [OH\_AudioNoiseReductionMode](capi-native-audio-common-h.md#oh_audionoisereductionmode) \*supportedModes | 支持的降噪模式数组。 |
| uint32\_t supportedModeCount | 支持的降噪模式数量。 |
| [OH\_AudioNoiseReductionMode](capi-native-audio-common-h.md#oh_audionoisereductionmode) currentMode | 设备当前降噪模式。  表示注册能力时的初始状态。 |
