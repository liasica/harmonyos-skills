---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiportinformation
title: OH_MIDIPortInformation
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDIPortInformation
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4924134237dcba2b32cc8176172d355776a5e9effa1e3da056a631e28b48503b
---

```c
typedef struct {...} OH_MIDIPortInformation
```

## 概述

端口信息结构体。用于枚举和标识MIDI设备端口，包含可显示的端口名称、端口索引、所属设备ID及端口方向（输入或输出）等关键信息，便于开发者在MIDI应用中管理和操作各端口。

**起始版本：** 24

**相关模块：** [OHMIDI](capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](capi-native-midi-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t portIndex | 端口在设备中的索引号。  **起始版本：** 24 |
| int64\_t deviceId | 端口所属的MIDI设备ID。  **起始版本：** 24 |
| [OH\_MIDIPortDirection](capi-native-midi-base-h.md#oh_midiportdirection) direction | 端口方向（输入或输出）。  **起始版本：** 24 |
| char name[64] | 端口名称。  **起始版本：** 24 |
