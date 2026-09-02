---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohmidi-oh-midiportdescriptor
title: OH_MIDIPortDescriptor
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_MIDIPortDescriptor
category: harmonyos-references
scraped_at: 2026-09-02T15:02:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b2437952875cf1ef29c88a538899435910b8997f70a6ec055b030df520e9ced9
---

```c
typedef struct {...} OH_MIDIPortDescriptor
```

## 概述

端口描述符结构体，用于打开端口时指定端口索引和MIDI协议版本（MIDI 1.0或MIDI 2.0），由系统自动完成应用与硬件之间的协议适配与数据转换，适用于需要在不同MIDI协议版本间进行兼容通信的场景。

**起始版本：** 24

**相关模块：** [OHMIDI](capi-ohmidi.md)

**所在头文件：** [native\_midi\_base.h](capi-native-midi-base-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t portIndex | 要打开的端口索引号。取值范围为0到设备实际端口数减1，具体有效索引需通过设备枚举接口获取。  **起始版本：** 24 |
| [OH\_MIDIProtocol](capi-native-midi-base-h.md#oh_midiprotocol) protocol | 指定要使用的MIDI协议版本（MIDI 1.0或MIDI 2.0）。服务会根据此字段在应用和硬件之间转换数据。应用只需声明期望的协议版本，以下是协议版本与硬件不匹配时的系统处理行为：  1. 在MIDI 2.0设备上请求OH\_MIDI\_PROTOCOL\_1\_0：（无损兼容）  应用发送UMP Type 2（MIDI 1.0通道声音）消息，服务直接转发给设备，无数据损失。  2. 在MIDI 1.0设备上请求OH\_MIDI\_PROTOCOL\_2\_0：（有损转换）  应用发送UMP Type 4（MIDI 2.0通道声音）消息，服务将Type 4降级转换为Type 2（例如：截断力度值，丢弃逐音符数据），会丢失数据精度，MIDI 2.0新增且在MIDI 1.0中无法表达的消息（如Per-Note控制器消息）可能被丢弃。  **起始版本：** 24 |
