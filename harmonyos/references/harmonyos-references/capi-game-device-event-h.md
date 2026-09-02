---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-event-h
title: game_device_event.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件 > game_device_event.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d11458480919e6d02d7c36fbcc60898e70b71ebf9bbdf2fc03331838d7c31824
---

## 概述

定义游戏设备事件的接口。

**引用文件：** <GameControllerKit/game\_device\_event.h>

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：** [GameController](capi-gamecontroller.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md) | GameDevice\_DeviceInfo | 定义设备信息。 |
| [GameDevice\_DeviceEvent](capi-gamecontroller-gamedevice-deviceevent.md) | GameDevice\_DeviceEvent | 定义设备状态变化事件。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [GameDevice\_StatusChangedType](capi-game-device-event-h.md#gamedevice_statuschangedtype) | GameDevice\_StatusChangedType | 此枚举定义设备的状态变化类型。 |
| [GameDevice\_DeviceType](capi-game-device-event-h.md#gamedevice_devicetype) | GameDevice\_DeviceType | 此枚举定义设备类型。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void(\*GameDevice\_DeviceMonitorCallback)(const struct GameDevice\_DeviceEvent\* deviceEvent)](capi-game-device-event-h.md#gamedevice_devicemonitorcallback) | GameDevice\_DeviceMonitorCallback | 定义[OH\_GameDevice\_RegisterDeviceMonitor](capi-game-device-h.md#oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceEvent\_GetChangedType(const struct GameDevice\_DeviceEvent\* deviceEvent, GameDevice\_StatusChangedType\* statusChangedType)](capi-game-device-event-h.md#oh_gamedevice_deviceevent_getchangedtype) | - | 从设备状态变化事件中获取状态变化类型。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceEvent\_GetDeviceInfo(const struct GameDevice\_DeviceEvent\* deviceEvent, GameDevice\_DeviceInfo\*\* deviceInfo)](capi-game-device-event-h.md#oh_gamedevice_deviceevent_getdeviceinfo) | - | 从设备状态变化事件中获取设备信息。 |
| [GameController\_ErrorCode OH\_GameDevice\_DestroyDeviceInfo(GameDevice\_DeviceInfo\*\* deviceInfo)](capi-game-device-event-h.md#oh_gamedevice_destroydeviceinfo) | - | 销毁设备信息实例。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceInfo\_GetDeviceId(const struct GameDevice\_DeviceInfo\* deviceInfo, char\*\* deviceId)](capi-game-device-event-h.md#oh_gamedevice_deviceinfo_getdeviceid) | - | 从设备信息中获取设备ID。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceInfo\_GetName(const struct GameDevice\_DeviceInfo\* deviceInfo, char\*\* name)](capi-game-device-event-h.md#oh_gamedevice_deviceinfo_getname) | - | 从设备信息中获取设备名称。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceInfo\_GetProduct(const struct GameDevice\_DeviceInfo\* deviceInfo, int32\_t\* product)](capi-game-device-event-h.md#oh_gamedevice_deviceinfo_getproduct) | - | 从设备信息中获取产品信息。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceInfo\_GetVersion(const struct GameDevice\_DeviceInfo\* deviceInfo, int32\_t\* version)](capi-game-device-event-h.md#oh_gamedevice_deviceinfo_getversion) | - | 从设备信息中获取版本信息。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceInfo\_GetPhysicalAddress(const struct GameDevice\_DeviceInfo\* deviceInfo, char\*\* physicalAddress)](capi-game-device-event-h.md#oh_gamedevice_deviceinfo_getphysicaladdress) | - | 从设备信息中获取物理地址。 |
| [GameController\_ErrorCode OH\_GameDevice\_DeviceInfo\_GetDeviceType(const struct GameDevice\_DeviceInfo\* deviceInfo, GameDevice\_DeviceType\* deviceType)](capi-game-device-event-h.md#oh_gamedevice_deviceinfo_getdevicetype) | - | 从设备信息中获取设备类型。 |

## 枚举类型说明

### GameDevice\_StatusChangedType

```c
enum GameDevice_StatusChangedType
```

**描述**

此枚举定义设备的状态变化类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| OFFLINE = 0 | 设备下线。  **起始版本：** 21 |
| ONLINE = 1 | 设备上线。  **起始版本：** 21 |

### GameDevice\_DeviceType

```c
enum GameDevice_DeviceType
```

**描述**

此枚举定义设备类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| UNKNOWN = 0 | 未知。  **起始版本：** 21 |
| GAME\_PAD = 1 | 游戏手柄。  **起始版本：** 21 |

## 函数说明

### GameDevice\_DeviceMonitorCallback()

```c
typedef void(*GameDevice_DeviceMonitorCallback)(const struct GameDevice_DeviceEvent* deviceEvent)
```

**描述**

定义[OH\_GameDevice\_RegisterDeviceMonitor](capi-game-device-h.md#oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct GameDevice\_DeviceEvent\* deviceEvent | 输入参数。设备状态变化事件[GameDevice\_DeviceEvent](capi-gamecontroller-gamedevice-deviceevent.md)。 |

### OH\_GameDevice\_DeviceEvent\_GetChangedType()

```c
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType(const struct GameDevice_DeviceEvent* deviceEvent, GameDevice_StatusChangedType* statusChangedType)
```

**描述**

从设备状态变化事件中获取状态变化类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceEvent](capi-gamecontroller-gamedevice-deviceevent.md)\* deviceEvent | 指针指向[GameDevice\_DeviceEvent](capi-gamecontroller-gamedevice-deviceevent.md)实例，不能为空。 |
| [GameDevice\_StatusChangedType](capi-game-device-event-h.md#gamedevice_statuschangedtype)\* statusChangedType | 输出参数，设备状态变化类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceEvent\_GetDeviceInfo()

```c
GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo(const struct GameDevice_DeviceEvent* deviceEvent, GameDevice_DeviceInfo** deviceInfo)
```

**描述**

从设备状态变化事件中获取设备信息。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceEvent](capi-gamecontroller-gamedevice-deviceevent.md)\* deviceEvent | 指针指向[GameDevice\_DeviceEvent](capi-gamecontroller-gamedevice-deviceevent.md)实例，不能为空。 |
| [GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\*\* deviceInfo | 输出参数，二级指针指向设备信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DestroyDeviceInfo()

```c
GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo(GameDevice_DeviceInfo** deviceInfo)
```

**描述**

销毁设备信息实例。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\*\* deviceInfo | 二级指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceInfo\_GetDeviceId()

```c
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId(const struct GameDevice_DeviceInfo* deviceInfo, char** deviceId)
```

**描述**

从设备信息中获取设备ID。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\* deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |
| char\*\* deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo或deviceId为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceInfo\_GetName()

```c
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName(const struct GameDevice_DeviceInfo* deviceInfo, char** name)
```

**描述**

从设备信息中获取设备名称。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\* deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |
| char\*\* name | 输出参数，二级指针指向设备名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo或name为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceInfo\_GetProduct()

```c
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct(const struct GameDevice_DeviceInfo* deviceInfo, int32_t* product)
```

**描述**

从设备信息中获取产品信息。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\* deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |
| int32\_t\* product | 输出参数，产品信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceInfo\_GetVersion()

```c
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion(const struct GameDevice_DeviceInfo* deviceInfo, int32_t* version)
```

**描述**

从设备信息中获取版本信息。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\* deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |
| int32\_t\* version | 输出参数，版本信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceInfo\_GetPhysicalAddress()

```c
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress(const struct GameDevice_DeviceInfo* deviceInfo, char** physicalAddress)
```

**描述**

从设备信息中获取物理地址。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\* deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |
| char\*\* physicalAddress | 输出参数，二级指针指向物理地址。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo或physicalAddress为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DeviceInfo\_GetDeviceType()

```c
GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType(const struct GameDevice_DeviceInfo* deviceInfo, GameDevice_DeviceType* deviceType)
```

**描述**

从设备信息中获取设备类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\* deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)实例，不能为空。 |
| [GameDevice\_DeviceType](capi-game-device-event-h.md#gamedevice_devicetype)\* deviceType | 输出参数，设备类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceInfo为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |
