---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-midi-h
title: native_midi.h
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 头文件 > native_midi.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a369104d30db84059d07576bf1233dd270cb29971343c1836ab683c99887c7ec
---

## 概述

声明MIDI相关的接口。MIDI是一种用于电子乐器、计算机和其他设备之间通信的技术标准。

该文件中的接口用于MIDI设备管理（包括BLE MIDI设备）、MIDI消息发送和接收、设备状态监控等。

使用OHMIDI连接MIDI设备的典型流程如下：

1. **创建客户端**：初始化MIDI客户端上下文，并注册设备热插拔回调及服务异常回调。
2. **发现设备与端口**：获取当前连接的设备列表，并查询设备的端口能力。
3. **打开设备**：建立设备连接会话。
4. **打开端口**：根据端口方向（输入/输出）分别打开端口。
5. **数据交互**：
   * **接收**：通过回调函数接收UMP（Universal MIDI Packet）格式的MIDI数据。
   * **发送**：构建UMP（Universal MIDI Packet）并通过输出端口发送。
6. **释放资源**：使用完毕后关闭端口、设备并销毁客户端。

**引用文件：** <ohmidi/native\_midi.h>

**库：** libohmidi.so

**系统能力：** SystemCapability.Multimedia.Audio.MIDI

**起始版本：** 24

**相关模块：** [OHMIDI](capi-ohmidi.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OH\_MIDIStatusCode OH\_MIDIClient\_Create(OH\_MIDIClient \*\*client, OH\_MIDICallbacks callbacks, void \*userData)](capi-native-midi-h.md#oh_midiclient_create) | 创建MIDI客户端实例。客户端是使用MIDI服务的入口，所有MIDI操作都需要先创建客户端。  MIDI是对低延迟有严格要求的系统服务。为确保实时性能和系统稳定性，服务强制执行以下限制：  1. 系统级限制：全局允许的活动MIDI客户端最大数量为8个。  2. 每应用限制：每个应用UID允许的MIDI客户端最大数量为2个。建议应用在整个生命周期内维护单个MIDI客户端实例，用于管理多个设备/端口。  在不再需要MIDI功能时，使用[OH\_MIDIClient\_Destroy](capi-native-midi-h.md#oh_midiclient_destroy)释放客户端及所有关联资源。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_Destroy(OH\_MIDIClient \*client)](capi-native-midi-h.md#oh_midiclient_destroy) | 销毁MIDI客户端并释放资源。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_GetDeviceCount(const OH\_MIDIClient \*client, size\_t \*count)](capi-native-midi-h.md#oh_midiclient_getdevicecount) | 获取连接的MIDI设备数量。此函数用于确定存储设备信息所需的缓冲区大小。  如果应用未获得蓝牙权限（ohos.permission.ACCESS\_BLUETOOTH），蓝牙MIDI设备将不计入设备数量。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_GetDeviceInfos(const OH\_MIDIClient \*client, OH\_MIDIDeviceInformation \*infos, size\_t capacity, size\_t \*actualDeviceCount)](capi-native-midi-h.md#oh_midiclient_getdeviceinfos) | 获取连接的MIDI设备信息。将设备信息写入infos参数指定的缓冲区。缓冲区大小应基于[OH\_MIDIClient\_GetDeviceCount](capi-native-midi-h.md#oh_midiclient_getdevicecount)返回的数量进行分配。  如果应用未获得蓝牙权限（ohos.permission.ACCESS\_BLUETOOTH），蓝牙MIDI设备将不会包含在返回的设备信息中。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_OpenDevice(OH\_MIDIClient \*client, int64\_t deviceId, OH\_MIDIDevice \*\*device)](capi-native-midi-h.md#oh_midiclient_opendevice) | 打开指定ID的MIDI设备。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_OpenBLEDevice(OH\_MIDIClient \*client, const char \*deviceAddr, OH\_MIDIClient\_OnDeviceOpened callback, void \*userData)](capi-native-midi-h.md#oh_midiclient_openbledevice) | 异步打开蓝牙低功耗（BLE）MIDI设备。此函数为异步操作，调用后立即返回状态码（表示请求是否成功发送），实际连接结果（成功或失败）将在BLE连接过程完成后通过提供的回调异步传递。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_CloseDevice(OH\_MIDIClient \*client, OH\_MIDIDevice \*device)](capi-native-midi-h.md#oh_midiclient_closedevice) | 关闭MIDI设备。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_GetPortCount(const OH\_MIDIClient \*client, int64\_t deviceId, size\_t \*count)](capi-native-midi-h.md#oh_midiclient_getportcount) | 获取指定MIDI设备的端口数量。此函数用于确定存储端口信息所需的缓冲区大小。 |
| [OH\_MIDIStatusCode OH\_MIDIClient\_GetPortInfos(const OH\_MIDIClient \*client, int64\_t deviceId, OH\_MIDIPortInformation \*infos, size\_t capacity, size\_t \*actualPortCount)](capi-native-midi-h.md#oh_midiclient_getportinfos) | 获取指定MIDI设备的端口信息。将端口信息写入由调用者分配的缓冲区。缓冲区大小应基于[OH\_MIDIClient\_GetPortCount](capi-native-midi-h.md#oh_midiclient_getportcount)返回的数量进行分配。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_OpenInputPort(OH\_MIDIDevice \*device, OH\_MIDIPortDescriptor descriptor, OH\_MIDIDevice\_OnReceived callback, void \*userData)](capi-native-midi-h.md#oh_mididevice_openinputport) | 打开MIDI输入端口（接收数据）。注册回调函数以接收MIDI数据流。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_OpenOutputPort(OH\_MIDIDevice \*device, OH\_MIDIPortDescriptor descriptor)](capi-native-midi-h.md#oh_mididevice_openoutputport) | 打开MIDI输出端口（发送数据）。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_CloseInputPort(OH\_MIDIDevice \*device, uint32\_t portIndex)](capi-native-midi-h.md#oh_mididevice_closeinputport) | 关闭MIDI输入端口。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_CloseOutputPort(OH\_MIDIDevice \*device, uint32\_t portIndex)](capi-native-midi-h.md#oh_mididevice_closeoutputport) | 关闭MIDI输出端口。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_Send(OH\_MIDIDevice \*device, uint32\_t portIndex, const OH\_MIDIEvent \*events, uint32\_t eventCount, uint32\_t \*eventsWritten)](capi-native-midi-h.md#oh_mididevice_send) | 批量发送MIDI消息（非阻塞模式，每条消息具有原子性）。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_SendSysEx(OH\_MIDIDevice \*device, uint32\_t portIndex, const uint8\_t \*data, uint32\_t byteSize)](capi-native-midi-h.md#oh_mididevice_sendsysex) | 发送超过标准MIDI消息长度的SysEx（System Exclusive，系统独占消息），自动处理分包和阻塞等待。这是一个实用函数，适用于将SysEx作为原始字节流（MIDI 1.0风格，F0...F7）处理的应用。此函数需要通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的输出端口发送数据。  同时适用于[OH\_MIDI\_PROTOCOL\_1\_0](capi-native-midi-base-h.md#oh_midiprotocol)和[OH\_MIDI\_PROTOCOL\_2\_0](capi-native-midi-base-h.md#oh_midiprotocol)会话。  操作系统MIDI服务会自动将数据转换为设备端口所需的格式。 |
| [OH\_MIDIStatusCode OH\_MIDIDevice\_FlushOutputPort(OH\_MIDIDevice \*device, uint32\_t portIndex)](capi-native-midi-h.md#oh_mididevice_flushoutputport) | 清空输出缓冲区中的待发送消息。立即丢弃指定端口输出缓冲区中等待的所有MIDI事件，包括用于未来时间戳的事件。 |

## 函数说明

### OH\_MIDIClient\_Create()

```c
OH_MIDIStatusCode OH_MIDIClient_Create(OH_MIDIClient **client, OH_MIDICallbacks callbacks, void *userData)
```

**描述**

创建MIDI客户端实例。客户端是使用MIDI服务的入口，所有MIDI操作都需要先创建客户端。

MIDI是对低延迟有严格要求的系统服务。为确保实时性能和系统稳定性，服务强制执行以下限制：

1. 系统级限制：全局允许的活动MIDI客户端最大数量为8个。

2. 每应用限制：每个应用UID允许的MIDI客户端最大数量为2个。建议应用在整个生命周期内维护单个MIDI客户端实例，用于管理多个设备/端口。

在不再需要MIDI功能时，使用[OH\_MIDIClient\_Destroy](capi-native-midi-h.md#oh_midiclient_destroy)释放客户端及所有关联资源。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*\*client | 指向用于接收新客户端句柄的指针。 |
| [OH\_MIDICallbacks](capi-ohmidi-oh-midicallbacks.md) callbacks | 用于系统事件的回调结构体。 |
| void \*userData | 传递给回调函数的用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数client为nullptr。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。  OH\_MIDI\_STATUS\_TOO\_MANY\_CLIENTS：因资源限制MIDI客户端创建失败。当调用应用超出其每UID配额或系统全局客户端数量已达上限时发生。 |

### OH\_MIDIClient\_Destroy()

```c
OH_MIDIStatusCode OH_MIDIClient_Destroy(OH_MIDIClient *client)
```

**描述**

销毁MIDI客户端并释放资源。

**说明** 

在不再需要MIDI功能时（例如应用退出或MIDI模块停用时）调用此函数销毁客户端。销毁客户端时会自动关闭所有通过此客户端打开的设备和端口（安全回收机制），无需手动逐一关闭。建议在销毁前按逆序手动关闭资源以保证代码逻辑清晰（端口->设备->客户端），但这非强制要求。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | 目标客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄为NULL或无效。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIClient\_GetDeviceCount()

```c
OH_MIDIStatusCode OH_MIDIClient_GetDeviceCount(const OH_MIDIClient *client, size_t *count)
```

**描述**

获取连接的MIDI设备数量。此函数用于确定存储设备信息所需的缓冲区大小。

如果应用未获得蓝牙权限（ohos.permission.ACCESS\_BLUETOOTH），蓝牙MIDI设备将不计入设备数量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | MIDI客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| size\_t \*count | 输出参数，用于接收设备数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数count为nullptr。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIClient\_GetDeviceInfos()

```c
OH_MIDIStatusCode OH_MIDIClient_GetDeviceInfos(const OH_MIDIClient *client, OH_MIDIDeviceInformation *infos, size_t capacity, size_t *actualDeviceCount)
```

**描述**

获取连接的MIDI设备信息。将设备信息写入infos参数指定的缓冲区。缓冲区大小应基于[OH\_MIDIClient\_GetDeviceCount](capi-native-midi-h.md#oh_midiclient_getdevicecount)返回的数量进行分配。

如果应用未获得蓝牙权限（ohos.permission.ACCESS\_BLUETOOTH），蓝牙MIDI设备将不会包含在返回的设备信息中。

**说明** 

当实际连接的设备数量大于输入参数'infos'数组的容量时，输出'infos'数组将仅包含部分设备信息，输出'actualDeviceCount'将等于'capacity'，函数返回[OH\_MIDI\_STATUS\_OK](capi-native-midi-base-h.md#oh_midistatuscode)。当实际数量小于或等于'capacity'时，所有可用设备信息将填入'infos'，输出'actualDeviceCount'反映实际设备数量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | MIDI客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| [OH\_MIDIDeviceInformation](capi-ohmidi-oh-midideviceinformation.md) \*infos | 用户分配的缓冲区，用于存储设备信息。 |
| size\_t capacity | 缓冲区可容纳的最大元素数量。 |
| size\_t \*actualDeviceCount | 输出参数，用于接收实际写入的设备数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数infos或actualDeviceCount为nullptr。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIClient\_OpenDevice()

```c
OH_MIDIStatusCode OH_MIDIClient_OpenDevice(OH_MIDIClient *client, int64_t deviceId, OH_MIDIDevice **device)
```

**描述**

打开指定ID的MIDI设备。

**说明** 

使用[OH\_MIDIClient\_CloseDevice](capi-native-midi-h.md#oh_midiclient_closedevice)释放设备资源。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | 目标客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| int64\_t deviceId | 设备的唯一标识符，由[OH\_MIDIClient\_GetDeviceInfos](capi-native-midi-h.md#oh_midiclient_getdeviceinfos)获取。 |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*\*device | 指向用于接收设备句柄的指针，由系统分配。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_DEVICE\_ALREADY\_OPEN：设备已被当前客户端打开。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数device为nullptr，或deviceId不存在。  OH\_MIDI\_STATUS\_TOO\_MANY\_OPEN\_DEVICES：客户端已达到最大打开设备数量限制。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIClient\_OpenBLEDevice()

```c
OH_MIDIStatusCode OH_MIDIClient_OpenBLEDevice(OH_MIDIClient *client, const char *deviceAddr, OH_MIDIClient_OnDeviceOpened callback, void *userData)
```

**描述**

异步打开蓝牙低功耗（BLE）MIDI设备。此函数为异步操作，调用后立即返回状态码（表示请求是否成功发送），实际连接结果（成功或失败）将在BLE连接过程完成后通过提供的回调异步传递。使用[OH\_MIDIClient\_CloseDevice](capi-native-midi-h.md#oh_midiclient_closedevice)释放设备资源。

**说明** 

如果蓝牙权限被拒绝，[OH\_MIDIClient\_OnDeviceOpened](capi-native-midi-base-h.md#oh_midiclient_ondeviceopened)回调将以opened参数为false、device参数为nullptr被调用。应用应检查opened参数后再尝试使用设备句柄。

**需要权限：** ohos.permission.ACCESS\_BLUETOOTH

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | 目标客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| const char \*deviceAddr | BLE设备的MAC地址。  格式："XX:XX:XX:XX:XX:XX"，X为十六进制字符0-9、A-F，例如："AA:BB:CC:DD:EE:FF"。 |
| [OH\_MIDIClient\_OnDeviceOpened](capi-native-midi-base-h.md#oh_midiclient_ondeviceopened) callback | 连接过程完成时要调用的回调函数。 |
| void \*userData | 传递给回调的用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：连接请求已成功分发。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_DEVICE\_ALREADY\_OPEN：设备已被当前客户端打开。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数deviceAddr或callback为nullptr。  OH\_MIDI\_STATUS\_PERMISSION\_DENIED：权限被拒绝。应用未声明或未获得所需权限。  OH\_MIDI\_STATUS\_TOO\_MANY\_OPEN\_DEVICES：客户端已达到最大打开设备数量限制。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIClient\_CloseDevice()

```c
OH_MIDIStatusCode OH_MIDIClient_CloseDevice(OH_MIDIClient *client, OH_MIDIDevice *device)
```

**描述**

关闭MIDI设备。

**说明** 

关闭设备时会同时关闭该设备上所有已打开的端口。该功能与[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)配对使用。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | 目标客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：IPC通信失败。 |

### OH\_MIDIClient\_GetPortCount()

```c
OH_MIDIStatusCode OH_MIDIClient_GetPortCount(const OH_MIDIClient *client, int64_t deviceId, size_t *count)
```

**描述**

获取指定MIDI设备的端口数量。此函数用于确定存储端口信息所需的缓冲区大小。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | MIDI客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| int64\_t deviceId | 目标设备ID，由[OH\_MIDIClient\_GetDeviceInfos](capi-native-midi-h.md#oh_midiclient_getdeviceinfos)获取。 |
| size\_t \*count | 输出参数，用于接收端口数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数count为nullptr，或deviceId无效。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIClient\_GetPortInfos()

```c
OH_MIDIStatusCode OH_MIDIClient_GetPortInfos(const OH_MIDIClient *client, int64_t deviceId, OH_MIDIPortInformation *infos, size_t capacity, size_t *actualPortCount)
```

**描述**

获取指定MIDI设备的端口信息。将端口信息写入由调用者分配的缓冲区。缓冲区大小应基于[OH\_MIDIClient\_GetPortCount](capi-native-midi-h.md#oh_midiclient_getportcount)返回的数量进行分配。

**说明** 

当实际端口数量大于输入参数'infos'数组的容量时，输出'infos'数组将仅包含部分端口信息，输出'actualPortCount'将等于'capacity'，函数返回[OH\_MIDI\_STATUS\_OK](capi-native-midi-base-h.md#oh_midistatuscode)。当实际数量小于或等于'capacity'时，所有可用端口信息将填入'infos'，输出'actualPortCount'反映实际端口数量。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [OH\_MIDIClient](capi-ohmidi-oh-midiclientstruct.md) \*client | MIDI客户端句柄。传入的client指针必须为[OH\_MIDIClient\_Create](capi-native-midi-h.md#oh_midiclient_create)创建的实例。 |
| int64\_t deviceId | 目标设备ID，由[OH\_MIDIClient\_GetDeviceInfos](capi-native-midi-h.md#oh_midiclient_getdeviceinfos)获取。 |
| [OH\_MIDIPortInformation](capi-ohmidi-oh-midiportinformation.md) \*infos | 用户分配的缓冲区，用于存储端口信息。 |
| size\_t capacity | infos缓冲区可容纳的最大元素数量。 |
| size\_t \*actualPortCount | 输出参数，用于接收实际写入的端口数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_CLIENT：客户端句柄无效。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数infos或actualPortCount为nullptr，或deviceId无效。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_OpenInputPort()

```c
OH_MIDIStatusCode OH_MIDIDevice_OpenInputPort(OH_MIDIDevice *device, OH_MIDIPortDescriptor descriptor, OH_MIDIDevice_OnReceived callback, void *userData)
```

**描述**

打开MIDI输入端口（接收数据）。注册回调函数以接收MIDI数据流。

**说明** 

使用[OH\_MIDIDevice\_CloseInputPort](capi-native-midi-h.md#oh_mididevice_closeinputport)关闭输入端口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| [OH\_MIDIPortDescriptor](capi-ohmidi-oh-midiportdescriptor.md) descriptor | 端口索引和协议配置。 |
| [OH\_MIDIDevice\_OnReceived](capi-native-midi-base-h.md#oh_mididevice_onreceived) callback | 有数据可用时调用的回调函数。 |
| void \*userData | 传递给回调的用户自定义数据指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效或不是输入端口。  OH\_MIDI\_STATUS\_PORT\_ALREADY\_OPEN：端口已被此客户端打开。  OH\_MIDI\_STATUS\_TOO\_MANY\_OPEN\_PORTS：已达到最大打开端口数量限制。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数callback为nullptr。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_OpenOutputPort()

```c
OH_MIDIStatusCode OH_MIDIDevice_OpenOutputPort(OH_MIDIDevice *device, OH_MIDIPortDescriptor descriptor)
```

**描述**

打开MIDI输出端口（发送数据）。

**说明** 

使用[OH\_MIDIDevice\_CloseOutputPort](capi-native-midi-h.md#oh_mididevice_closeoutputport)关闭输出端口。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| [OH\_MIDIPortDescriptor](capi-ohmidi-oh-midiportdescriptor.md) descriptor | 端口索引和协议配置。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效或不是输出端口。  OH\_MIDI\_STATUS\_PORT\_ALREADY\_OPEN：端口已被此客户端打开。  OH\_MIDI\_STATUS\_TOO\_MANY\_OPEN\_PORTS：已达到最大打开端口数量限制。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_CloseInputPort()

```c
OH_MIDIStatusCode OH_MIDIDevice_CloseInputPort(OH_MIDIDevice *device, uint32_t portIndex)
```

**描述**

关闭MIDI输入端口。

**说明** 

与[OH\_MIDIDevice\_OpenInputPort](capi-native-midi-h.md#oh_mididevice_openinputport)配对使用。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| uint32\_t portIndex | 要关闭的输入端口索引，须为已通过[OH\_MIDIDevice\_OpenInputPort](capi-native-midi-h.md#oh_mididevice_openinputport)打开的输入端口索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效，或未打开。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_CloseOutputPort()

```c
OH_MIDIStatusCode OH_MIDIDevice_CloseOutputPort(OH_MIDIDevice *device, uint32_t portIndex)
```

**描述**

关闭MIDI输出端口。

**说明** 

与[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)配对使用。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| uint32\_t portIndex | 要关闭的输出端口索引，须为已通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的端口索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效，或不是打开的输出端口。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_Send()

```c
OH_MIDIStatusCode OH_MIDIDevice_Send(OH_MIDIDevice *device, uint32_t portIndex, const OH_MIDIEvent *events, uint32_t eventCount, uint32_t *eventsWritten)
```

**描述**

批量发送MIDI消息（非阻塞模式，每条消息具有原子性）。此函数需要通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的输出端口发送数据，portIndex应为一个已打开的输出端口索引。

**说明** 

将MIDI事件数组写入共享内存缓冲区。

* 单条消息原子性：每条事件作为不可分割的单元处理，不会出现消息被截断的情况。
* 批量操作非原子性：整个数组不一定全部写入成功。如果缓冲区空间不足，已成功写入的事件不会被回滚。函数返回[OH\_MIDI\_STATUS\_WOULD\_BLOCK](capi-native-midi-base-h.md#oh_midistatuscode)，并通过eventsWritten参数返回已成功写入的事件数量，开发者可据此从断点处继续发送剩余事件。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| uint32\_t portIndex | 目标端口索引，须为已通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的输出端口索引。 |
| const [OH\_MIDIEvent](capi-ohmidi-oh-midievent.md) \*events | 指向要发送的事件数组的指针，内存空间需要由开发者分配。 |
| uint32\_t eventCount | 数组中的事件数量。 |
| uint32\_t \*eventsWritten | 输出参数，用于接收成功发送的事件数量。当返回OH\_MIDI\_STATUS\_WOULD\_BLOCK时，可用于从断点处继续发送剩余事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：所有数据均已成功处理并写入。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效，或未打开。  OH\_MIDI\_STATUS\_WOULD\_BLOCK：缓冲区已满（检查eventsWritten）。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数events或eventsWritten为nullptr。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_SendSysEx()

```c
OH_MIDIStatusCode OH_MIDIDevice_SendSysEx(OH_MIDIDevice *device, uint32_t portIndex, const uint8_t *data, uint32_t byteSize)
```

**描述**

发送超过标准MIDI消息长度的SysEx（System Exclusive，系统独占消息），自动处理分包和阻塞等待。这是一个实用函数，适用于将SysEx作为原始字节流（MIDI 1.0风格，F0...F7）处理的应用。此函数需要通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的输出端口发送数据。

同时适用于[OH\_MIDI\_PROTOCOL\_1\_0](capi-native-midi-base-h.md#oh_midiprotocol)和[OH\_MIDI\_PROTOCOL\_2\_0](capi-native-midi-base-h.md#oh_midiprotocol)会话。

操作系统MIDI服务会自动将数据转换为设备端口所需的格式。

**说明** 

此函数为阻塞调用，执行循环写入，当缓冲区填满时将阻塞并重试，直至写入完整。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| uint32\_t portIndex | 目标端口索引，须为已通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的输出端口索引。 |
| const uint8\_t \*data | 指向要发送的字节数据流的指针，内存空间需要由开发者分配。 |
| uint32\_t byteSize | 数据的字节大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：所有数据均已成功处理并写入。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效，或未打开。  OH\_MIDI\_STATUS\_TIMEOUT：操作超时，无法在系统规定的超时时间内完成写入，可使用[OH\_MIDIDevice\_FlushOutputPort](capi-native-midi-h.md#oh_mididevice_flushoutputport)重置输出端口后重试。  OH\_MIDI\_STATUS\_GENERIC\_INVALID\_ARGUMENT：参数data为nullptr，或byteSize为0。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |

### OH\_MIDIDevice\_FlushOutputPort()

```c
OH_MIDIStatusCode OH_MIDIDevice_FlushOutputPort(OH_MIDIDevice *device, uint32_t portIndex)
```

**描述**

清空输出缓冲区中的待发送消息。立即丢弃指定端口输出缓冲区中等待的所有MIDI事件，包括已入队、计划在未来时间戳发送的事件。适用于停止播放、切换音色或设备异常时需要取消尚未发送的MIDI事件的场景。

**说明** 

此操作不发送"All Notes Off"消息，仅清空队列。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_MIDIDevice](capi-ohmidi-oh-mididevicestruct.md) \*device | 目标设备句柄。传入的device指针必须为[OH\_MIDIClient\_OpenDevice](capi-native-midi-h.md#oh_midiclient_opendevice)或[OH\_MIDIClient\_OpenBLEDevice](capi-native-midi-h.md#oh_midiclient_openbledevice)返回的实例。 |
| uint32\_t portIndex | 目标端口索引，须为已通过[OH\_MIDIDevice\_OpenOutputPort](capi-native-midi-h.md#oh_mididevice_openoutputport)打开的输出端口索引。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_MIDIStatusCode](capi-native-midi-base-h.md#oh_midistatuscode) | OH\_MIDI\_STATUS\_OK：操作成功。  OH\_MIDI\_STATUS\_INVALID\_DEVICE\_HANDLE：设备句柄无效。  OH\_MIDI\_STATUS\_INVALID\_PORT：端口索引无效或不是输出端口。  OH\_MIDI\_STATUS\_GENERIC\_IPC\_FAILURE：连接系统服务失败。 |
