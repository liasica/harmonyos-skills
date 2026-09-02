---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-device-h
title: game_device.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件 > game_device.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9dd76f9a2cdc5c13eb9ba3b48f8ae8c7f93df9bb7c3c6e01b4855ece210a0b21
---

## 概述

定义游戏设备的接口。

**引用文件：** <GameControllerKit/game\_device.h>

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：** [GameController](capi-gamecontroller.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md) | GameDevice\_AllDeviceInfos | 定义[OH\_GameDevice\_GetAllDeviceInfos](capi-game-device-h.md#oh_gamedevice_getalldeviceinfos)接口的调用结果。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode OH\_GameDevice\_GetAllDeviceInfos(GameDevice\_AllDeviceInfos\*\* allDeviceInfos)](capi-game-device-h.md#oh_gamedevice_getalldeviceinfos) | 获取所有在线设备的信息。 |
| [GameController\_ErrorCode OH\_GameDevice\_RegisterDeviceMonitor(GameDevice\_DeviceMonitorCallback deviceMonitorCallback)](capi-game-device-h.md#oh_gamedevice_registerdevicemonitor) | 注册设备状态变化事件的监听回调。 |
| [GameController\_ErrorCode OH\_GameDevice\_UnregisterDeviceMonitor(void)](capi-game-device-h.md#oh_gamedevice_unregisterdevicemonitor) | 取消注册设备状态变化事件的监听回调。 |
| [GameController\_ErrorCode OH\_GameDevice\_DestroyAllDeviceInfos(GameDevice\_AllDeviceInfos\*\* allDeviceInfos)](capi-game-device-h.md#oh_gamedevice_destroyalldeviceinfos) | 销毁所有设备信息实例。 |
| [GameController\_ErrorCode OH\_GameDevice\_AllDeviceInfos\_GetCount(const struct GameDevice\_AllDeviceInfos\* allDeviceInfos, int32\_t\* count)](capi-game-device-h.md#oh_gamedevice_alldeviceinfos_getcount) | 获取设备数量。 |
| [GameController\_ErrorCode OH\_GameDevice\_AllDeviceInfos\_GetDeviceInfo(const struct GameDevice\_AllDeviceInfos\* allDeviceInfos, const int32\_t index, GameDevice\_DeviceInfo\*\* deviceInfo)](capi-game-device-h.md#oh_gamedevice_alldeviceinfos_getdeviceinfo) | 获取指定索引的设备信息。 |

## 函数说明

### OH\_GameDevice\_GetAllDeviceInfos()

```c
GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos(GameDevice_AllDeviceInfos** allDeviceInfos)
```

**描述**

获取所有在线设备的信息。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)\*\* allDeviceInfos | 输出参数。二级指针指向[GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)实例，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数allDeviceInfos为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果查询多模输入中所有设备信息失败，返回[GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_RegisterDeviceMonitor()

```c
GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor(GameDevice_DeviceMonitorCallback deviceMonitorCallback)
```

**描述**

注册设备状态变化事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GameDevice\_DeviceMonitorCallback](capi-game-device-event-h.md#gamedevice_devicemonitorcallback) deviceMonitorCallback | 回调函数[GameDevice\_DeviceMonitorCallback](capi-game-device-event-h.md#gamedevice_devicemonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数deviceMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_UnregisterDeviceMonitor()

```c
GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor(void)
```

**描述**

取消注册设备状态变化事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_DestroyAllDeviceInfos()

```c
GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos(GameDevice_AllDeviceInfos** allDeviceInfos)
```

**描述**

销毁所有设备信息实例。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)\*\* allDeviceInfos | 二级指针指向[GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)实例，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数allDeviceInfos为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_AllDeviceInfos\_GetCount()

```c
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount(const struct GameDevice_AllDeviceInfos* allDeviceInfos, int32_t* count)
```

**描述**

获取设备数量。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)\* allDeviceInfos | 指针指向[GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)实例，不能为空。 |
| int32\_t\* count | 输出参数，设备数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数allDeviceInfos为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GameDevice\_AllDeviceInfos\_GetDeviceInfo()

```c
GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo(const struct GameDevice_AllDeviceInfos* allDeviceInfos, const int32_t index, GameDevice_DeviceInfo** deviceInfo)
```

**描述**

获取指定索引的设备信息。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)\* allDeviceInfos | 指针指向[GameDevice\_AllDeviceInfos](capi-gamecontroller-gamedevice-alldeviceinfos.md)实例，不能为空。 |
| const int32\_t index | 指定设备索引。 |
| [GameDevice\_DeviceInfo](capi-gamecontroller-gamedevice-deviceinfo.md)\*\* deviceInfo | 输出参数，二级指针指向设备信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数allDeviceInfos为null，或index小于0或大于等于设备总数，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |
