---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptorarray
title: OH_AudioDeviceDescriptorArray
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioDeviceDescriptorArray
category: harmonyos-references
scraped_at: 2026-04-28T08:11:52+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5c8f0ffcc9fd02d99e9c8f7b2fce9c7040952f3d1ab3845daf9bbae7038175f8
---

```
1. typedef struct OH_AudioDeviceDescriptorArray {...} OH_AudioDeviceDescriptorArray
```

## 概述

PhonePC/2in1TabletTVWearable

声明音频设备描述符数组。

**起始版本：** 12

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audio\_device\_base.h](capi-native-audio-device-base-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 音频设备描述符数组大小。 |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md)\*\* descriptors | 音频设备描述符数组。 |
