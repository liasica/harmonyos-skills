---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audioaccessorycapabilities
title: OH_AudioAccessoryCapabilities
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioAccessoryCapabilities
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6bbfb88c9f56fee2ad019dc5c71abc6e25dfb0057554787e529ee2ff7d4cc4ed
---

```c
typedef struct OH_AudioAccessoryCapabilities {...} OH_AudioAccessoryCapabilities
```

## 概述

定义音频配件的能力。

调用方需将structSize设置为sizeof(OH\_AudioAccessoryCapabilities)。

**起始版本：** 26.0.0

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audio\_accessory\_common.h](capi-native-audio-accessory-common-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t structSize | 结构体大小，单位为字节（Byte）。  调用方需初始化此字段。 |
| const [OH\_AudioStreamInfo](capi-ohaudio-oh-audiostreaminfo.md) \*streamProperties | 支持的音频流配置数组。  每个条目表示采样率、采样格式和声道数的有效组合。  系统会对此数组进行深拷贝。 |
| uint32\_t streamPropertyCount | 支持的音频流配置数量。 |
