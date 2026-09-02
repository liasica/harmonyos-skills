---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midicallbacks
title: OH_MIDICallbacks
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDICallbacks
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:93906de3e9ac5f1035e8795d48c821f2c6848884f66db3483c305fdccdc5bcfd
---

```c
typedef struct {...} OH_MIDICallbacks
```

## 概述

客户端回调结构体，用于监听MIDI设备的热插拔事件和关键服务错误，包含设备热插拔和错误处理的回调函数指针，适用于需要在应用中实时感知MIDI设备状态变化并处理异常的场景。

**起始版本：** 24

**相关模块：** [OHMIDI](capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](capi-native-midi-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_MIDICallback\_OnDeviceChange](capi-native-midi-base-h.md#oh_midicallback_ondevicechange) onDeviceChange | 处理设备热插拔事件的回调函数指针。  **起始版本：** 24 |
| [OH\_MIDICallback\_OnError](capi-native-midi-base-h.md#oh_midicallback_onerror) onError | 处理服务运行过程中发生的关键错误的回调函数指针。  **起始版本：** 24 |
