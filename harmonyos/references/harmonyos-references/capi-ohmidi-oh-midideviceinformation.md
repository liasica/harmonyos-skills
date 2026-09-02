---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midideviceinformation
title: OH_MIDIDeviceInformation
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDIDeviceInformation
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8c01b2923b83fc8258c811a7a7fbdf38837bad2bda73f78406c5ca1b3e8ea015
---

```c
typedef struct {...} OH_MIDIDeviceInformation
```

## 概述

设备信息结构体，用于存储MIDI设备的详细信息，包括设备唯一标识符、设备类型（如USB、BLE）、支持的MIDI协议、设备名称、厂商ID、产品ID及物理地址等。适用于在MIDI设备枚举、识别和连接管理等场景中，获取并传递设备的完整属性信息。

**起始版本：** 24

**相关模块：** [OHMIDI](capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](capi-native-midi-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t midiDeviceId | MIDI设备的唯一标识符。  **起始版本：** 24 |
| [OH\_MIDIDeviceType](capi-native-midi-base-h.md#oh_mididevicetype) deviceType | 设备类型（USB或BLE）。  **起始版本：** 24 |
| [OH\_MIDIProtocol](capi-native-midi-base-h.md#oh_midiprotocol) nativeProtocol | 设备原生支持的MIDI协议。- OH\_MIDI\_PROTOCOL\_1\_0：设备是传统设备或当前配置为MIDI 1.0。  - OH\_MIDI\_PROTOCOL\_2\_0：设备使用MIDI 2.0协议。  **起始版本：** 24 |
| char deviceName[256] | 设备名称。  **起始版本：** 24 |
| uint64\_t vendorId | 厂商ID。  **起始版本：** 24 |
| uint64\_t productId | 产品ID。  **起始版本：** 24 |
| char deviceAddress[64] | 设备物理地址，采用冒号分隔的十六进制MAC地址格式，例如"00:11:22:33:44:55"，仅BLE设备类型时有效。  **起始版本：** 24 |
