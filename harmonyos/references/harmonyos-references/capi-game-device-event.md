---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-event
title: game_device_event.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件和结构体 > 头文件 > game_device_event.h
category: harmonyos-references
scraped_at: 2026-04-28T08:16:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7edfb02227cc5d58564cb0989a880df99f18aedfdf6b071e0b07bbf8a79c526c
---

## 概述

PhonePC/2in1TabletTV

定义游戏设备事件的接口。

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](capi-game-controller.md)

## 汇总

PhonePC/2in1TabletTV

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef enum [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) | 此枚举定义设备的状态变化类型。 |
| typedef enum [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) | 此枚举定义设备类型。 |
| typedef struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) | 定义设备信息。 |
| typedef struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) | 定义设备状态变化事件。 |
| typedef void(\*[GameDevice\_DeviceMonitorCallback](capi-game-controller.md#gamedevice_devicemonitorcallback)) (const struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) \*deviceEvent) | 定义[OH\_GameDevice\_RegisterDeviceMonitor](capi-game-controller.md#oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) {  OFFLINE = 0,  ONLINE = 1  } | 设备的状态变化类型。 |
| [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) {  UNKNOWN = 0,  GAME\_PAD = 1  } | 设备类型。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceEvent\_GetChangedType](capi-game-controller.md#oh_gamedevice_deviceevent_getchangedtype) (const struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) \*deviceEvent, [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) \*statusChangedType) | 从设备状态变化事件中获取状态变化类型。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceEvent\_GetDeviceInfo](capi-game-controller.md#oh_gamedevice_deviceevent_getdeviceinfo) (const struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) \*deviceEvent, [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*\*deviceInfo) | 从设备状态变化事件中获取设备信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DestroyDeviceInfo](capi-game-controller.md#oh_gamedevice_destroydeviceinfo) ([GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*\*deviceInfo) | 当[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例不再使用，销毁该实例。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetDeviceId](capi-game-controller.md#oh_gamedevice_deviceinfo_getdeviceid) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, char \*\*deviceId) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备ID。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetName](capi-game-controller.md#oh_gamedevice_deviceinfo_getname) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, char \*\*name) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备名称。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetProduct](capi-game-controller.md#oh_gamedevice_deviceinfo_getproduct) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, int32\_t \*product) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取产品信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetVersion](capi-game-controller.md#oh_gamedevice_deviceinfo_getversion) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, int32\_t \*version) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取版本信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetPhysicalAddress](capi-game-controller.md#oh_gamedevice_deviceinfo_getphysicaladdress) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, char \*\*physicalAddress) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取物理地址。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetDeviceType](capi-game-controller.md#oh_gamedevice_deviceinfo_getdevicetype) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) \*deviceType) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备类型。 |
