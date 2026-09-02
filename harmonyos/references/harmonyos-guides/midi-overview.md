---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/midi-overview
title: OH_MIDI概述(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > MIDI设备通信 > OH_MIDI概述(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:43+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:fc7d5f55d514774806b30098ca4bdc9128b4658a17cb052cce92c8df70da895c
---

## MIDI简介

乐器数字接口（Musical Instrument Digital Interface）是一种用于电子乐器、计算机和其他设备之间进行通信的国际标准协议。同时定义了音符、控制信号等音乐数据的传输方式，广泛应用于音乐制作、舞台演出和游戏开发等领域。

从API version 24开始，Audio Kit支持MIDI（Musical Instrument Digital Interface）功能，应用可通过OH\_MIDI API与外接MIDI设备（如USB MIDI键盘、蓝牙MIDI设备）进行数据交互。由于OH\_MIDI采用UMP（Universal MIDI Packet）作为统一的数据交互格式，所以开发者无需关心底层协议差异，只需要以现代化的方式构建音乐创作、乐器控制和MIDI数据处理等应用。

### MIDI协议版本

* MIDI 1.0：1983年发布的经典协议，使用7位（bit）分辨率（取值范围为[0, 127]），单向通信，广泛兼容现有设备。
* MIDI 2.0：2020年发布的新一代协议，支持32位高分辨率、双向通信、自动配置（MIDI-CI）等特性。

OH\_MIDI支持连接标准MIDI 1.0设备，并通过系统服务层自动将传统的MIDI 1.0字节流转换为32位UMP格式，从而简化应用开发。同时，该架构设计在数据格式上兼容MIDI 2.0标准，为未来系统内核支持高分辨率MIDI设备提供了必要的技术基础。

### UMP数据格式说明

通用MIDI数据包（Universal MIDI Packet）是MIDI 2.0标准中定义的统一数据包格式，采用32位对齐结构，可同时承载MIDI 1.0和MIDI 2.0协议消息。

协议与数据格式的关系（可以类比为"信封"和"信的内容语言"）：

* UMP：统一的32位对齐容器（信封格式）。
* MIDI 1.0/2.0 协议：传统/现代语义（信的内容语言）。

无论选择哪种协议，数据封装格式（UMP）都是统一的。

OH\_MIDI包含客户端、设备、端口和事件四个核心概念。使用OH\_MIDI开发MIDI应用的基本流程为：创建客户端 → 枚举/打开设备 → 打开端口 → 收发MIDI消息 → 关闭端口/设备/客户端。完整的开发步骤和示例代码请参考[使用OH\_MIDI进行MIDI开发(C/C++)](using-ohmidi.md)。

核心概念之间的关系：

* **客户端（Client）**：应用与MIDI服务交互的入口。创建客户端后，可注册热插拔和错误回调、枚举已连接的设备、打开设备句柄。
* **设备（Device）**：通过客户端打开的MIDI接口设备，包括USB MIDI设备和BLE MIDI设备。每个设备可打开多个端口。
* **端口（Port）**：设备上的数据传输端点，分为输入端口（接收MIDI数据）和输出端口（发送MIDI数据）。
* **事件（Event）**：端口收发数据的基本单元，采用UMP格式，包含时间戳（timestamp）、数据长度（length）和数据指针（data）。

## OH\_MIDI客户端（Client）

客户端是应用使用MIDI服务的入口点，所有MIDI操作都需要先创建客户端。同时，客户端负责管理与MIDI服务的连接、提供设备枚举、设备打开和端口管理等核心功能。

通过[OH\_MIDIClient\_Create](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_create)接口创建客户端后，应用可以获取当前连接的所有MIDI设备列表，并通过注册的回调监听设备的热插拔事件（[OH\_MIDICallback\_OnDeviceChange](../harmonyos-references/capi-native-midi-base-h.md#oh_midicallback_ondevicechange)）和系统级错误（[OH\_MIDICallback\_OnError](../harmonyos-references/capi-native-midi-base-h.md#oh_midicallback_onerror)）。

关闭客户端时，系统会自动关闭该客户端名下打开的所有设备和端口（自动资源回收机制）。建议应用按相反顺序（端口→设备→客户端）主动释放资源，以保证代码逻辑清晰。

## OH\_MIDI设备（Device）

MIDI设备是指物理或虚拟的MIDI接口设备，包括USB MIDI键盘、蓝牙MIDI控制器等。设备连接后，MIDI服务会为其分配标识符（[OH\_MIDIDeviceInformation](../harmonyos-references/capi-ohmidi-oh-midideviceinformation.md)中的midiDeviceId），用于在当前会话中区分和管理不同设备。

设备信息包含设备类型（USB或蓝牙）、原生协议能力、设备名称、厂商ID、产品ID和设备地址等属性。

**连接方式：** USB设备通过[OH\_MIDIClient\_OpenDevice](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_opendevice)接口同步打开，蓝牙低功耗（Bluetooth Low Energy）MIDI设备则需要通过[OH\_MIDIClient\_OpenBLEDevice](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_openbledevice)接口异步连接。

**原生协议能力：** 指示设备当前的通讯协议模式。在当前版本中，当设备支持多种协议时，系统会优先以MIDI 1.0模式与设备通讯，并在MIDI服务层将数据封装为MIDI 2.0 UMP格式提供给应用。

## OH\_MIDI端口（Port）

MIDI端口是设备上的数据传输端点，分为输入端口和输出端口。

* 输入端口（Input Port）：用于从设备接收MIDI数据。通过[OH\_MIDIDevice\_OpenInputPort](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_openinputport)接口打开并注册[OH\_MIDIDevice\_OnReceived](../harmonyos-references/capi-native-midi-base-h.md#oh_mididevice_onreceived)回调，实现批量消息接收。

  数据流向说明：MIDI设备向应用发送数据，应用通过回调接收。
* 输出端口（Output Port）：用于向设备发送MIDI数据。通过[OH\_MIDIDevice\_OpenOutputPort](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_openoutputport)接口打开输出端口后，使用[OH\_MIDIDevice\_Send](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_send)接口发送UMP格式消息。

  数据流向说明：应用调用[OH\_MIDIDevice\_Send](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_send)接口向MIDI设备发送数据。

```text
[应用] <--接收-- [输入端口] <-- [设备]
[应用] --发送--> [输出端口] --> [设备]
```

每个设备可以有多个输入和输出端口。当每个端口打开时，可以通过[OH\_MIDIPortDescriptor](../harmonyos-references/capi-ohmidi-oh-midiportdescriptor.md)结构配置期望的协议行为。

* 数据转换：无论底层设备是MIDI 1.0还是2.0，应用层均统一收发UMP数据包。
* 协议降级：如果应用请求发送MIDI 2.0高精度消息（UMP Type 4），但底层设备仅支持MIDI 1.0，MIDI服务层会自动将其降级转换为MIDI 1.0消息发送。
* 自动转换说明：系统服务层会在接收方向自动将底层协议数据转换为UMP格式供应用处理。但在发送方向上，应用需要按照UMP规范自行构造[OH\_MIDIEvent](../harmonyos-references/capi-ohmidi-oh-midievent.md)数据。

## OH\_MIDI事件（Event）

MIDI事件是MIDI数据传输的基本单元。OH\_MIDI强制使用UMP（Universal MIDI Packet）格式，统一承载MIDI 1.0和MIDI 2.0数据。

每个事件包含三个核心字段：

* 时间戳（timestamp）：纳秒级精度。取值范围为[0, 2^63-1]纳秒。0表示立即发送。
* 数据长度（length）：表示data数组中32位字（Word）的数量。取值范围为[1, 128]。
* UMP数据指针（data）：指向4字节对齐的uint32\_t数组。

### 完整消息类型参考

UMP格式通过消息类型（Message Type）区分不同消息。MT是UMP数据包的最高4位，决定了消息的功能范围、数据包大小和状态字段大小。

| MT值 | 名称 | 大小（bit） | 说明 |
| --- | --- | --- | --- |
| 0x0 | Utility Messages | 32 | 实用消息，如[JR](midi-overview.md#术语表)时间戳。 |
| 0x1 | System Real Time and System Common Messages | 32 | 系统实时消息和系统公共消息（不含System Exclusive）。 |
| 0x2 | MIDI 1.0 Channel Voice Messages | 32 | MIDI 1.0通道声音消息，兼容现有设备。 |
| 0x3 | Data Messages | 64 | 数据消息，如[SysEx](midi-overview.md#术语表)（包含System Exclusive）。 |
| 0x4 | MIDI 2.0 Channel Voice Messages | 64 | MIDI 2.0高分辨率[Channel Voice](midi-overview.md#术语表)消息。 |
| 0x5 | Data Messages | 128 | 数据消息。 |
| 0x6 | Reserved | 32 | 保留供未来使用。 |
| 0x7 | Reserved | 32 | 保留供未来使用。 |
| 0x8 | Reserved | 64 | 保留供未来使用。 |
| 0x9 | Reserved | 64 | 保留供未来使用。 |
| 0xA | Reserved | 64 | 保留供未来使用。 |
| 0xB | Reserved | 96 | 保留供未来使用。 |
| 0xC | Reserved | 96 | 保留供未来使用。 |
| 0xD | Flex Data Messages | 128 | [Flex Data](midi-overview.md#术语表)灵活数据消息，如文本、歌词。 |
| 0xE | Reserved | 128 | 保留供未来使用。 |
| 0xF | UMP Stream Messages | 128 | UMP流消息，如端点发现、功能块配置。 |

**注意** 

* 大多数应用场景下，开发者只需使用MT 0x2（MIDI 1.0通道声音）和MT 0x4（MIDI 2.0通道声音）即可完成MIDI音符的发送与接收。
* 接收回调中的events数组及其包含的data指针仅在回调执行期间有效。应用如需保留MIDI数据供后续处理，必须在回调返回前将数据深拷贝到应用自己的内存中，以避免访问过期指针导致的未定义行为。

## 术语表

| 术语 | 全称 | 说明 |
| --- | --- | --- |
| UMP | Universal MIDI Packet | 通用MIDI数据包，32位对齐的统一容器格式。 |
| MT | Message Type | 消息类型，UMP数据包最高4位，决定消息功能和大小。 |
| SysEx | System Exclusive | 系统独占消息，用于厂商自定义数据传输。 |
| JR | Jitter Reduction | 抖动消除，网络/蓝牙传输时的时间戳同步机制。 |
| Channel Voice | 通道声音消息 | 控制音符、力度、控制器等的核心消息类型。 |
| Flex Data | 灵活数据 | MIDI 2.0新增，支持文本、歌词等128位长消息。 |
| MIDI-CI | MIDI Capability Inquiry | MIDI能力查询，MIDI 2.0的设备自动配置协议。 |

## 约束与限制

* 同时打开的设备数量限制：单个客户端最多可同时打开16个MIDI设备。超过限制时，[OH\_MIDIClient\_OpenDevice](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_opendevice)接口将返回OH\_MIDI\_STATUS\_TOO\_MANY\_OPEN\_DEVICES错误。
* 每个设备的端口数量限制：每个MIDI设备最多可有64个端口（输入+输出总计）。单个客户端最多可同时打开64个端口。超过限制时，[OH\_MIDIDevice\_OpenInputPort](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_openinputport)或[OH\_MIDIDevice\_OpenOutputPort](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_openoutputport)接口将返回OH\_MIDI\_STATUS\_TOO\_MANY\_OPEN\_PORTS错误。
* 缓冲区大小限制：共享内存缓冲区大小为4KB。发送大量MIDI消息时，如果缓冲区填满，[OH\_MIDIDevice\_Send](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_send)接口将返回OH\_MIDI\_STATUS\_WOULD\_BLOCK。建议应用批量发送消息，并在收到此错误后延迟10ms再重试。
* 线程模型和回调执行环境：所有回调（[OH\_MIDIDevice\_OnReceived](../harmonyos-references/capi-native-midi-base-h.md#oh_mididevice_onreceived)、[OH\_MIDICallback\_OnDeviceChange](../harmonyos-references/capi-native-midi-base-h.md#oh_midicallback_ondevicechange)、[OH\_MIDICallback\_OnError](../harmonyos-references/capi-native-midi-base-h.md#oh_midicallback_onerror)）在高优先级系统线程上执行。回调中应避免执行阻塞操作、大量计算或I/O操作，以免影响MIDI系统的实时性能。
* 内存安全：[OH\_MIDIDevice\_OnReceived](../harmonyos-references/capi-native-midi-base-h.md#oh_mididevice_onreceived)回调中的events数组及其包含的数据指针仅在回调期间有效。如需保留数据，必须在回调返回前复制。访问过期指针会导致未定义行为（崩溃、内存损坏）。
* 资源管理顺序：关闭客户端时会自动关闭所有设备和端口。建议应用按相反顺序关闭资源，以保证代码逻辑清晰。

  + 第一步：关闭所有端口（[OH\_MIDIDevice\_CloseInputPort](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_closeinputport)/[OH\_MIDIDevice\_CloseOutputPort](../harmonyos-references/capi-native-midi-h.md#oh_mididevice_closeoutputport)）。
  + 第二步：关闭所有设备（[OH\_MIDIClient\_CloseDevice](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_closedevice)）。
  + 第三步：销毁客户端（[OH\_MIDIClient\_Destroy](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_destroy)）。

  此顺序为推荐做法，用于保证代码逻辑清晰，但系统提供自动资源回收机制确保资源正确释放。
* 设备类型特性差异：

  + USB MIDI设备：通过USB连接，支持低延迟传输，设备枚举通过系统USB驱动完成。
  + 蓝牙MIDI设备：通过蓝牙BLE连接，需要ohos.permission.ACCESS\_BLUETOOTH权限，使用[OH\_MIDIClient\_OpenBLEDevice](../harmonyos-references/capi-native-midi-h.md#oh_midiclient_openbledevice)接口异步打开。

## 相关参考

* [使用OH\_MIDI进行MIDI开发(C/C++)](using-ohmidi.md)
* + [OHMIDI](../harmonyos-references/capi-ohmidi.md)API参考
* MIDI状态码枚举：[OH\_MIDIStatusCode](../harmonyos-references/capi-native-midi-base-h.md#oh_midistatuscode)
