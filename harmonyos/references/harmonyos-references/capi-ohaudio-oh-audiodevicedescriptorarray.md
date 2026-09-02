---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudio-oh-audiodevicedescriptorarray
title: OH_AudioDeviceDescriptorArray
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_AudioDeviceDescriptorArray
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ad924f9fd69c47aeb0fb6e9b7b18dff5d7dc1b6989591675f7e6f309d048d327
---

```c
typedef struct OH_AudioDeviceDescriptorArray {...} OH_AudioDeviceDescriptorArray
```

## 概述

声明音频设备描述符数组的结构体。

**起始版本：** 12

**相关模块：** [OHAudio](capi-ohaudio.md)

**所在头文件：** [native\_audio\_device\_base.h](capi-native-audio-device-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 音频设备描述符数组元素个数。 |
| [OH\_AudioDeviceDescriptor](capi-ohaudio-oh-audiodevicedescriptor.md)\*\* descriptors | 音频设备描述符数组。 |
