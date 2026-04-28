---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-controller
title: GameController
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 模块 > GameController
category: harmonyos-references
scraped_at: 2026-04-28T08:16:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b2e02854601141c8cfe13f31268aa87994ece0a48b468a55e17dfeb70e03563
---

## 概述

PhonePC/2in1TabletTV

GameController模块提供游戏控制器功能的API接口。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

## 汇总

PhonePC/2in1TabletTV

### 文件

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [game\_controller\_type.h](capi-game-controller-type.md) | 定义GameController模块的通用枚举类型。 |
| [game\_device.h](capi-game-device.md) | 定义游戏设备的接口。 |
| [game\_device\_event.h](capi-game-device-event.md) | 定义游戏设备事件的接口。 |
| [game\_pad.h](capi-game-pad.md) | 定义游戏手柄的接口。 |
| [game\_pad\_event.h](capi-game-pad-event.md) | 定义游戏手柄事件的接口。 |

### 类型定义

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| typedef enum [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) | 此枚举定义游戏控制器的错误码。 |
| typedef struct [GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos) [GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos) | 定义[OH\_GameDevice\_GetAllDeviceInfos](capi-game-controller.md#oh_gamedevice_getalldeviceinfos)接口的调用结果。 |
| typedef enum [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) | 此枚举定义设备的状态变化类型。 |
| typedef enum [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) | 此枚举定义设备类型。 |
| typedef struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) | 定义设备信息。 |
| typedef struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) | 定义设备状态变化事件。 |
| typedef void(\*[GameDevice\_DeviceMonitorCallback](capi-game-controller.md#gamedevice_devicemonitorcallback)) (const struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) \*deviceEvent) | 定义[OH\_GameDevice\_RegisterDeviceMonitor](capi-game-controller.md#oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。 |
| typedef enum [GamePad\_AxisSourceType](capi-game-controller.md#gamepad_axissourcetype) [GamePad\_AxisSourceType](capi-game-controller.md#gamepad_axissourcetype) | 此枚举定义手柄轴事件来源类型。 |
| typedef enum [GamePad\_Button\_ActionType](capi-game-controller.md#gamepad_button_actiontype) [GamePad\_Button\_ActionType](capi-game-controller.md#gamepad_button_actiontype) | 此枚举定义手柄按键动作类型。 |
| typedef struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) | 定义手柄按键事件。 |
| typedef struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) | 定义手柄轴事件。 |
| typedef struct [GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton) [GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton) | 定义手柄按下的按键。 |
| typedef void(\*[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent) | 定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。 |
| typedef void(\*[GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback)) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent) | 定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。 |

### 枚举

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) {  GAME\_CONTROLLER\_SUCCESS = 0,  GAME\_CONTROLLER\_PARAM\_ERROR = 401,  GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR = 32200001,  GAME\_CONTROLLER\_NO\_MEMORY = 32200002  } | 游戏控制器错误码。 |
| [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) {  OFFLINE = 0,  ONLINE = 1  } | 设备的状态变化类型。 |
| [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) {  UNKNOWN = 0,  GAME\_PAD = 1  } | 设备类型。 |
| [GamePad\_AxisSourceType](capi-game-controller.md#gamepad_axissourcetype) {  DPAD = 0,  LEFT\_THUMBSTICK = 1,  RIGHT\_THUMBSTICK = 2,  LEFT\_TRIGGER = 3,  RIGHT\_TRIGGER = 4  } | 手柄轴事件来源类型。 |
| [GamePad\_Button\_ActionType](capi-game-controller.md#gamepad_button_actiontype) {  DOWN = 0,  UP = 1  } | 手柄按键动作类型。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_GetAllDeviceInfos](capi-game-controller.md#oh_gamedevice_getalldeviceinfos) ([GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos) \*\*allDeviceInfos) | 获取所有在线设备的信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_RegisterDeviceMonitor](capi-game-controller.md#oh_gamedevice_registerdevicemonitor) ([GameDevice\_DeviceMonitorCallback](capi-game-controller.md#gamedevice_devicemonitorcallback) deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_UnregisterDeviceMonitor](capi-game-controller.md#oh_gamedevice_unregisterdevicemonitor) (void) | 取消注册设备状态变化事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DestroyAllDeviceInfos](capi-game-controller.md#oh_gamedevice_destroyalldeviceinfos) ([GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos) \*\*allDeviceInfos) | 当[GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos)实例不再使用，销毁该实例。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_AllDeviceInfos\_GetCount](capi-game-controller.md#oh_gamedevice_alldeviceinfos_getcount) (const struct [GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos) \*allDeviceInfos, int32\_t \*count) | 获取设备数量。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_AllDeviceInfos\_GetDeviceInfo](capi-game-controller.md#oh_gamedevice_alldeviceinfos_getdeviceinfo) (const struct [GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos) \*allDeviceInfos, const int32\_t index, [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*\*deviceInfo) | 从所有设备信息中获取指定序号的设备信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceEvent\_GetChangedType](capi-game-controller.md#oh_gamedevice_deviceevent_getchangedtype) (const struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) \*deviceEvent, [GameDevice\_StatusChangedType](capi-game-controller.md#gamedevice_statuschangedtype) \*statusChangedType) | 从设备状态变化事件中获取状态变化类型。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceEvent\_GetDeviceInfo](capi-game-controller.md#oh_gamedevice_deviceevent_getdeviceinfo) (const struct [GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent) \*deviceEvent, [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*\*deviceInfo) | 从设备状态变化事件中获取设备信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DestroyDeviceInfo](capi-game-controller.md#oh_gamedevice_destroydeviceinfo) ([GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*\*deviceInfo) | 当[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例不再使用，销毁该实例。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetDeviceId](capi-game-controller.md#oh_gamedevice_deviceinfo_getdeviceid) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, char \*\*deviceId) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备ID。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetName](capi-game-controller.md#oh_gamedevice_deviceinfo_getname) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, char \*\*name) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备名称。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetProduct](capi-game-controller.md#oh_gamedevice_deviceinfo_getproduct) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, int32\_t \*product) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取产品信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetVersion](capi-game-controller.md#oh_gamedevice_deviceinfo_getversion) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, int32\_t \*version) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取版本信息。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetPhysicalAddress](capi-game-controller.md#oh_gamedevice_deviceinfo_getphysicaladdress) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, char \*\*physicalAddress) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取物理地址。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GameDevice\_DeviceInfo\_GetDeviceType](capi-game-controller.md#oh_gamedevice_deviceinfo_getdevicetype) (const struct [GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo) \*deviceInfo, [GameDevice\_DeviceType](capi-game-controller.md#gamedevice_devicetype) \*deviceType) | 从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备类型。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftShoulder\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_leftshoulder_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册LeftShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftShoulder\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_leftshoulder_unregisterbuttoninputmonitor) (void) | 取消注册LeftShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightShoulder\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_rightshoulder_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册RightShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightShoulder\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_rightshoulder_unregisterbuttoninputmonitor) (void) | 取消注册RightShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftTrigger\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_lefttrigger_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册LeftTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftTrigger\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_lefttrigger_unregisterbuttoninputmonitor) (void) | 取消注册LeftTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftTrigger\_RegisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_lefttrigger_registeraxisinputmonitor) ([GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback) inputMonitorCallback) | 注册LeftTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftTrigger\_UnregisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_lefttrigger_unregisteraxisinputmonitor) (void) | 取消注册LeftTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightTrigger\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_righttrigger_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册RightTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightTrigger\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_righttrigger_unregisterbuttoninputmonitor) (void) | 取消注册RightTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightTrigger\_RegisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_righttrigger_registeraxisinputmonitor) ([GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback) inputMonitorCallback) | 注册RightTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightTrigger\_UnregisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_righttrigger_unregisteraxisinputmonitor) (void) | 取消注册RightTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonMenu\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonmenu_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册Menu按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonMenu\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonmenu_unregisterbuttoninputmonitor) (void) | 取消注册Menu按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonHome\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonhome_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册Home按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonHome\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonhome_unregisterbuttoninputmonitor) (void) | 取消注册Home按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonA\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttona_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册A按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonA\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttona_unregisterbuttoninputmonitor) (void) | 取消注册A按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonB\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonb_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册B按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonB\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonb_unregisterbuttoninputmonitor) (void) | 取消注册B按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonX\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonx_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册X按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonX\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonx_unregisterbuttoninputmonitor) (void) | 取消注册X按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonY\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttony_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册Y按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonY\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttony_unregisterbuttoninputmonitor) (void) | 取消注册Y按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonC\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonc_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册C按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonC\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_buttonc_unregisterbuttoninputmonitor) (void) | 取消注册C按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_LeftButton\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_leftbutton_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册方向按键的向左按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_LeftButton\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_leftbutton_unregisterbuttoninputmonitor) (void) | 取消注册方向按键的向左按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_RightButton\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_rightbutton_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册方向按键的向右按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_RightButton\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_rightbutton_unregisterbuttoninputmonitor) (void) | 取消注册方向按键的向右按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_UpButton\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_upbutton_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册方向按键的向上按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_UpButton\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_upbutton_unregisterbuttoninputmonitor) (void) | 取消注册方向按键的向上按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_DownButton\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_downbutton_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册方向按键的向下按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_DownButton\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_dpad_downbutton_unregisterbuttoninputmonitor) (void) | 取消注册方向按键的向下按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_RegisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_dpad_registeraxisinputmonitor) ([GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback) inputMonitorCallback) | 注册方向按键轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_Dpad\_UnregisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_dpad_unregisteraxisinputmonitor) (void) | 取消注册方向按键轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftThumbstick\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_leftthumbstick_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册LeftThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftThumbstick\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_leftthumbstick_unregisterbuttoninputmonitor) (void) | 取消注册LeftThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftThumbstick\_RegisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_leftthumbstick_registeraxisinputmonitor) ([GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback) inputMonitorCallback) | 注册LeftThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_LeftThumbstick\_UnregisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_leftthumbstick_unregisteraxisinputmonitor) (void) | 取消注册LeftThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightThumbstick\_RegisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_rightthumbstick_registerbuttoninputmonitor) ([GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback) | 注册RightThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightThumbstick\_UnregisterButtonInputMonitor](capi-game-controller.md#oh_gamepad_rightthumbstick_unregisterbuttoninputmonitor) (void) | 取消注册RightThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightThumbstick\_RegisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_rightthumbstick_registeraxisinputmonitor) ([GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback) inputMonitorCallback) | 注册RightThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_RightThumbstick\_UnregisterAxisInputMonitor](capi-game-controller.md#oh_gamepad_rightthumbstick_unregisteraxisinputmonitor) (void) | 取消注册RightThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetDeviceId](capi-game-controller.md#oh_gamepad_buttonevent_getdeviceid) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, char \*\*deviceId) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取设备ID。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetButtonAction](capi-game-controller.md#oh_gamepad_buttonevent_getbuttonaction) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, [GamePad\_Button\_ActionType](capi-game-controller.md#gamepad_button_actiontype) \*actionType) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键动作类型。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetButtonCode](capi-game-controller.md#oh_gamepad_buttonevent_getbuttoncode) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, int32\_t \*code) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键编码。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetButtonCodeName](capi-game-controller.md#oh_gamepad_buttonevent_getbuttoncodename) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, char \*\*codeName) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键的名称。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButtons\_GetCount](capi-game-controller.md#oh_gamepad_pressedbuttons_getcount) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, int32\_t \*count) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按下的按键数量。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButtons\_GetButtonInfo](capi-game-controller.md#oh_gamepad_pressedbuttons_getbuttoninfo) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, const int32\_t index, [GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton) \*\*pressedButton) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取指定序号的按下的按键。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_DestroyPressedButton](capi-game-controller.md#oh_gamepad_destroypressedbutton) ([GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton) \*\*pressedButton) | 当[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)实例不再使用， 销毁该实例。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButton\_GetButtonCode](capi-game-controller.md#oh_gamepad_pressedbutton_getbuttoncode) (const struct [GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton) \*pressedButton, int32\_t \*code) | 从按下的按键[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)中获取按键编码。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_PressedButton\_GetButtonCodeName](capi-game-controller.md#oh_gamepad_pressedbutton_getbuttoncodename) (const struct [GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton) \*pressedButton, char \*\*codeName) | 从按下的按键[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)中获取按键的名称。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_ButtonEvent\_GetActionTime](capi-game-controller.md#oh_gamepad_buttonevent_getactiontime) (const struct [GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent) \*buttonEvent, int64\_t \*actionTime) | 从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键动作的时间。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetDeviceId](capi-game-controller.md#oh_gamepad_axisevent_getdeviceid) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, char \*\*deviceId) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取设备ID。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetAxisSourceType](capi-game-controller.md#oh_gamepad_axisevent_getaxissourcetype) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, [GamePad\_AxisSourceType](capi-game-controller.md#gamepad_axissourcetype) \*axisSourceType) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取轴事件来源类型。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetXAxisValue](capi-game-controller.md#oh_gamepad_axisevent_getxaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取X轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetYAxisValue](capi-game-controller.md#oh_gamepad_axisevent_getyaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Y轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetZAxisValue](capi-game-controller.md#oh_gamepad_axisevent_getzaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Z轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetRZAxisValue](capi-game-controller.md#oh_gamepad_axisevent_getrzaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取RZ轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetHatXAxisValue](capi-game-controller.md#oh_gamepad_axisevent_gethatxaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取HatX轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetHatYAxisValue](capi-game-controller.md#oh_gamepad_axisevent_gethatyaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取HatY轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetBrakeAxisValue](capi-game-controller.md#oh_gamepad_axisevent_getbrakeaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Brake轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetGasAxisValue](capi-game-controller.md#oh_gamepad_axisevent_getgasaxisvalue) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, double \*axisValue) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Gas轴的轴值。 |
| [GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode) [OH\_GamePad\_AxisEvent\_GetActionTime](capi-game-controller.md#oh_gamepad_axisevent_getactiontime) (const struct [GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent) \*axisEvent, int64\_t \*actionTime) | 从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取动作时间。 |

## 类型定义说明

PhonePC/2in1TabletTV

### GameController\_ErrorCode

PhonePC/2in1TabletTV

```
1. typedef enum GameController_ErrorCode GameController_ErrorCode
```

**描述**

此枚举定义游戏控制器的错误码。

**起始版本：** 21

### GameDevice\_AllDeviceInfos

PhonePC/2in1TabletTV

```
1. typedef struct GameDevice_AllDeviceInfos GameDevice_AllDeviceInfos
```

**描述**

定义[OH\_GameDevice\_GetAllDeviceInfos](capi-game-controller.md#oh_gamedevice_getalldeviceinfos)接口的调用结果。

**起始版本：** 21

### GameDevice\_DeviceEvent

PhonePC/2in1TabletTV

```
1. typedef struct GameDevice_DeviceEvent GameDevice_DeviceEvent
```

**描述**

定义设备状态变化事件。

**起始版本：** 21

### GameDevice\_DeviceInfo

PhonePC/2in1TabletTV

```
1. typedef struct GameDevice_DeviceInfo GameDevice_DeviceInfo
```

**描述**

定义设备信息。

**起始版本：** 21

### GameDevice\_DeviceMonitorCallback

PhonePC/2in1TabletTV

```
1. typedef void(*GameDevice_DeviceMonitorCallback) (const struct GameDevice_DeviceEvent *deviceEvent)
```

**描述**

定义[OH\_GameDevice\_RegisterDeviceMonitor](capi-game-controller.md#oh_gamedevice_registerdevicemonitor)中使用的回调函数。当设备上线或下线时，该回调函数将被调用。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceEvent | 输出参数。设备状态变化事件[GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent)。 |

### GameDevice\_DeviceType

PhonePC/2in1TabletTV

```
1. typedef enum GameDevice_DeviceType GameDevice_DeviceType
```

**描述**

此枚举定义设备类型。

**起始版本：** 21

### GameDevice\_StatusChangedType

PhonePC/2in1TabletTV

```
1. typedef enum GameDevice_StatusChangedType GameDevice_StatusChangedType
```

**描述**

此枚举定义设备的状态变化类型。

**起始版本：** 21

### GamePad\_AxisEvent

PhonePC/2in1TabletTV

```
1. typedef struct GamePad_AxisEvent GamePad_AxisEvent
```

**描述**

定义手柄轴事件。

**起始版本：** 21

### GamePad\_AxisInputMonitorCallback

PhonePC/2in1TabletTV

```
1. typedef void(*GamePad_AxisInputMonitorCallback) (const struct GamePad_AxisEvent *axisEvent)
```

**描述**

定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 输出参数，手柄轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)。 |

### GamePad\_AxisSourceType

PhonePC/2in1TabletTV

```
1. typedef enum GamePad_AxisSourceType GamePad_AxisSourceType
```

**描述**

此枚举定义手柄轴事件来源类型。

**起始版本：** 21

### GamePad\_Button\_ActionType

PhonePC/2in1TabletTV

```
1. typedef enum GamePad_Button_ActionType GamePad_Button_ActionType
```

**描述**

此枚举定义手柄按键动作类型。

**起始版本：** 21

### GamePad\_ButtonEvent

PhonePC/2in1TabletTV

```
1. typedef struct GamePad_ButtonEvent GamePad_ButtonEvent
```

**描述**

定义手柄按键事件。

**起始版本：** 21

### GamePad\_ButtonInputMonitorCallback

PhonePC/2in1TabletTV

```
1. typedef void(*GamePad_ButtonInputMonitorCallback) (const struct GamePad_ButtonEvent *buttonEvent)
```

**描述**

定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 输出参数，手柄按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)。 |

### GamePad\_PressedButton

PhonePC/2in1TabletTV

```
1. typedef struct GamePad_PressedButton GamePad_PressedButton
```

**描述**

定义手柄按下的按键。

**起始版本：** 21

## 枚举类型说明

PhonePC/2in1TabletTV

### GameController\_ErrorCode

PhonePC/2in1TabletTV

```
1. enum GameController_ErrorCode
```

**描述**

此枚举定义游戏控制器的错误码。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| GAME\_CONTROLLER\_SUCCESS | 成功。 |
| GAME\_CONTROLLER\_PARAM\_ERROR | 参数非法。 |
| GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR | 查询多模输入中所有设备信息失败。 |
| GAME\_CONTROLLER\_NO\_MEMORY | 设备内存不足。 |

### GameDevice\_DeviceType

PhonePC/2in1TabletTV

```
1. enum GameDevice_DeviceType
```

**描述**

此枚举定义设备类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| UNKNOWN | 未知。 |
| GAME\_PAD | 游戏手柄。 |

### GameDevice\_StatusChangedType

PhonePC/2in1TabletTV

```
1. enum GameDevice_StatusChangedType
```

**描述**

此枚举定义设备的状态变化类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| OFFLINE | 设备下线。 |
| ONLINE | 设备上线。 |

### GamePad\_AxisSourceType

PhonePC/2in1TabletTV

```
1. enum GamePad_AxisSourceType
```

**描述**

此枚举定义手柄轴事件来源类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| DPAD | 轴事件来源于方向按键DPAD。 |
| LEFT\_THUMBSTICK | 轴事件来源于LeftThumbstick。 |
| RIGHT\_THUMBSTICK | 轴事件来源于RightThumbstick。 |
| LEFT\_TRIGGER | 轴事件来源于LeftTrigger。 |
| RIGHT\_TRIGGER | 轴事件来源于RightTrigger。 |

### GamePad\_Button\_ActionType

PhonePC/2in1TabletTV

```
1. enum GamePad_Button_ActionType
```

**描述**

此枚举定义手柄按键动作类型。

**起始版本：** 21

| 枚举值 | 描述 |
| --- | --- |
| DOWN | 按键按下。 |
| UP | 按键抬起。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_GameDevice\_AllDeviceInfos\_GetCount()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetCount (const struct GameDevice_AllDeviceInfos *allDeviceInfos, int32_t *count)
```

**描述**

获取设备数量。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 指针指向[GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。 |
| count | 输出参数，设备数量。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数allDeviceInfos为null。

### OH\_GameDevice\_AllDeviceInfos\_GetDeviceInfo()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_AllDeviceInfos_GetDeviceInfo (const struct GameDevice_AllDeviceInfos *allDeviceInfos, const int32_t index, GameDevice_DeviceInfo **deviceInfo)
```

**描述**

从所有设备信息中获取指定序号的设备信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 指针指向[GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。 |
| index | 指定查询的设备序号。 |
| deviceInfo | 输出参数，二级指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)设备信息实例。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：allDeviceInfos为null或者index小于0或者index大于等于所有设备数。

### OH\_GameDevice\_DestroyAllDeviceInfos()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DestroyAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos)
```

**描述**

当[GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos)实例不再使用，销毁该实例。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 二级指针指向[GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数allDeviceInfos为null。

### OH\_GameDevice\_DestroyDeviceInfo()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DestroyDeviceInfo (GameDevice_DeviceInfo **deviceInfo)
```

**描述**

当[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例不再使用，销毁该实例。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 二级指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo为null。

### OH\_GameDevice\_DeviceEvent\_GetChangedType()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceEvent_GetChangedType (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_StatusChangedType *statusChangedType)
```

**描述**

从设备状态变化事件[GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent)中获取状态变化类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceEvent | 指针指向[GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent)实例，不能为空，否则将返回错误码。 |
| statusChangedType | 输出参数，设备状态变化类型。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceEvent为null。

### OH\_GameDevice\_DeviceEvent\_GetDeviceInfo()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceEvent_GetDeviceInfo (const struct GameDevice_DeviceEvent *deviceEvent, GameDevice_DeviceInfo **deviceInfo)
```

**描述**

从设备状态变化事件[GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent)中获取设备信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceEvent | 指针指向[GameDevice\_DeviceEvent](capi-game-controller.md#gamedevice_deviceevent)实例，不能为空，否则将返回错误码。 |
| deviceInfo | 输出参数，二级指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)设备信息实例。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceEvent为null。

### OH\_GameDevice\_DeviceInfo\_GetDeviceId()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceId (const struct GameDevice_DeviceInfo *deviceInfo, char **deviceId)
```

**描述**

从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备ID。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |
| deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo或deviceId为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GameDevice\_DeviceInfo\_GetDeviceType()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceInfo_GetDeviceType (const struct GameDevice_DeviceInfo *deviceInfo, GameDevice_DeviceType *deviceType)
```

**描述**

从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |
| deviceType | 输出参数，设备类型。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo为null。

### OH\_GameDevice\_DeviceInfo\_GetName()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceInfo_GetName (const struct GameDevice_DeviceInfo *deviceInfo, char **name)
```

**描述**

从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取设备名称。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |
| name | 输出参数，二级指针指向设备名称。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo或name为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GameDevice\_DeviceInfo\_GetPhysicalAddress()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceInfo_GetPhysicalAddress (const struct GameDevice_DeviceInfo *deviceInfo, char **physicalAddress)
```

**描述**

从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取物理地址。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |
| physicalAddress | 输出参数，二级指针指向物理地址。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo或physicalAddress为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GameDevice\_DeviceInfo\_GetProduct()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceInfo_GetProduct (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *product)
```

**描述**

从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取产品信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |
| product | 输出参数，产品信息。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo为null。

### OH\_GameDevice\_DeviceInfo\_GetVersion()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_DeviceInfo_GetVersion (const struct GameDevice_DeviceInfo *deviceInfo, int32_t *version)
```

**描述**

从设备信息[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)中获取版本信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceInfo | 指针指向[GameDevice\_DeviceInfo](capi-game-controller.md#gamedevice_deviceinfo)实例，不能为空，否则将返回错误码。 |
| version | 输出参数，版本信息。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceInfo为null。

### OH\_GameDevice\_GetAllDeviceInfos()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_GetAllDeviceInfos (GameDevice_AllDeviceInfos **allDeviceInfos)
```

**描述**

获取所有在线设备的信息。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| allDeviceInfos | 输出参数。二级指针指向[GameDevice\_AllDeviceInfos](capi-game-controller.md#gamedevice_alldeviceinfos)实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_MULTIMODAL\_INPUT\_ERROR：查询多模输入中所有设备信息失败。

### OH\_GameDevice\_RegisterDeviceMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_RegisterDeviceMonitor (GameDevice_DeviceMonitorCallback deviceMonitorCallback)
```

**描述**

注册设备状态变化事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| deviceMonitorCallback | 回调函数[GameDevice\_DeviceMonitorCallback](capi-game-controller.md#gamedevice_devicemonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数deviceMonitorCallback为null。

### OH\_GameDevice\_UnregisterDeviceMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GameDevice_UnregisterDeviceMonitor (void)
```

**描述**

取消注册设备状态变化事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_AxisEvent\_GetActionTime()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetActionTime (const struct GamePad_AxisEvent *axisEvent, int64_t *actionTime)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取动作时间。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| actionTime | 输出参数，动作时间。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetAxisSourceType()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetAxisSourceType (const struct GamePad_AxisEvent *axisEvent, GamePad_AxisSourceType *axisSourceType)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取轴事件来源类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisSourceType | 输出参数，轴事件来源类型[GamePad\_AxisSourceType](capi-game-controller.md#gamepad_axissourcetype)。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetBrakeAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetBrakeAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Brake轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetDeviceId()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetDeviceId (const struct GamePad_AxisEvent *axisEvent, char **deviceId)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取设备ID。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent或deviceId为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GamePad\_AxisEvent\_GetGasAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetGasAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Gas轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetHatXAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetHatXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取HatX轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetHatYAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetHatYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取HatY轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetRZAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetRZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取RZ轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetXAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetXAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取X轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetYAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetYAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Y轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_AxisEvent\_GetZAxisValue()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_AxisEvent_GetZAxisValue (const struct GamePad_AxisEvent *axisEvent, double *axisValue)
```

**描述**

从轴事件[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)中获取Z轴的轴值。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| axisEvent | 指针指向[GamePad\_AxisEvent](capi-game-controller.md#gamepad_axisevent)实例，不能为空，否则将返回错误码。 |
| axisValue | 输出参数，轴值。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数axisEvent为null。

### OH\_GamePad\_ButtonA\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonA_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册A按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonA\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonA_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册A按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_ButtonB\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonB_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册B按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonB\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonB_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册B按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_ButtonC\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonC_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册C按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonC\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonC_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册C按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_ButtonEvent\_GetActionTime()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonEvent_GetActionTime (const struct GamePad_ButtonEvent *buttonEvent, int64_t *actionTime)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键动作的时间。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| actionTime | 输出参数，按键动作的时间。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数buttonEvent为null。

### OH\_GamePad\_ButtonEvent\_GetButtonAction()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonAction (const struct GamePad_ButtonEvent *buttonEvent, GamePad_Button_ActionType *actionType)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键动作类型。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| actionType | 输出参数，按键动作类型。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数buttonEvent为null。

### OH\_GamePad\_ButtonEvent\_GetButtonCode()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCode (const struct GamePad_ButtonEvent *buttonEvent, int32_t *code)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键编码。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| code | 输出参数，按键编码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数buttonEvent为null。

### OH\_GamePad\_ButtonEvent\_GetButtonCodeName()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCodeName (const struct GamePad_ButtonEvent *buttonEvent, char **codeName)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按键的名称。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| codeName | 输出参数，二级指针指向按键的名称。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数buttonEvent或codeName为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GamePad\_ButtonEvent\_GetDeviceId()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonEvent_GetDeviceId (const struct GamePad_ButtonEvent *buttonEvent, char **deviceId)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取设备ID。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数buttonEvent或deviceId为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GamePad\_ButtonHome\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonHome_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Home按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonHome\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonHome_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册Home按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_ButtonMenu\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonMenu_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Menu按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonMenu\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册Menu按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_ButtonX\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonX_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册X按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonX\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonX_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册X按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_ButtonY\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonY_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Y按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 输出参数，回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_ButtonY\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_ButtonY_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册Y按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_DestroyPressedButton()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_DestroyPressedButton (GamePad_PressedButton **pressedButton)
```

**描述**

当[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)实例不再使用， 销毁该实例。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| pressedButton | 二级指针指向[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)实例，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数pressedButton为null。

### OH\_GamePad\_Dpad\_DownButton\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向下按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_Dpad\_DownButton\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向下按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_Dpad\_LeftButton\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向左按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_Dpad\_LeftButton\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向左按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_Dpad\_RegisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_Dpad\_RightButton\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向右按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_Dpad\_RightButton\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向右按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_Dpad\_UnregisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册方向按键轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_Dpad\_UpButton\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向上按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_Dpad\_UpButton\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册方向按键的向上按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_LeftShoulder\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftShoulder_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftShoulder按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_LeftShoulder\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册LeftShoulder按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_LeftThumbstick\_RegisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftThumbstick轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_LeftThumbstick\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftThumbstick按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_LeftThumbstick\_UnregisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册LeftThumbstick轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_LeftThumbstick\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册LeftThumbstick按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_LeftTrigger\_RegisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftTrigger轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_LeftTrigger\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftTrigger按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_LeftTrigger\_UnregisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册LeftTrigger轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_LeftTrigger\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册LeftTrigger按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_PressedButton\_GetButtonCode()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCode (const struct GamePad_PressedButton *pressedButton, int32_t *code)
```

**描述**

从按下的按键[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)中获取按键编码。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| pressedButton | 指针指向[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)实例，不能为空，否则将返回错误码。 |
| code | 输出参数，按键编码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数pressedButton为null。

### OH\_GamePad\_PressedButton\_GetButtonCodeName()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCodeName (const struct GamePad_PressedButton *pressedButton, char **codeName)
```

**描述**

从按下的按键[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)中获取按键的名称。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| pressedButton | 指针指向[GamePad\_PressedButton](capi-game-controller.md#gamepad_pressedbutton)实例，不能为空，否则将返回错误码。 |
| codeName | 输出参数，二级指针指向按键的名称。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数pressedButton或codeName为null。
* GAME\_CONTROLLER\_NO\_MEMORY：设备内存不足。

### OH\_GamePad\_PressedButtons\_GetButtonInfo()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_PressedButtons_GetButtonInfo (const struct GamePad_ButtonEvent *buttonEvent, const int32_t index, GamePad_PressedButton **pressedButton)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取指定序号的按下的按键。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| index | 指定按键序号。 |
| pressedButton | 输出参数，二级指针指向按下的键。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：buttonEvent为null或index小于0或index大于等于所有按键数。

### OH\_GamePad\_PressedButtons\_GetCount()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_PressedButtons_GetCount (const struct GamePad_ButtonEvent *buttonEvent, int32_t *count)
```

**描述**

从按键事件[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)中获取按下的按键数量。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-game-controller.md#gamepad_buttonevent)实例，不能为空，否则将返回错误码。 |
| count | 输出参数，按下的按键数量。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数buttonEvent为null。

### OH\_GamePad\_RightShoulder\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightShoulder_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightShoulder按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_RightShoulder\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightShoulder_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册RightShoulder按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_RightThumbstick\_RegisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightThumbstick轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_RightThumbstick\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightThumbstick按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_RightThumbstick\_UnregisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册RightThumbstick轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_RightThumbstick\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册RightThumbstick按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_RightTrigger\_RegisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightTrigger_RegisterAxisInputMonitor (GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightTrigger轴事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-controller.md#gamepad_axisinputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_RightTrigger\_RegisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightTrigger_RegisterButtonInputMonitor (GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightTrigger按键事件的监听回调。

**起始版本：** 21

**参数:**

| 名称 | 描述 |
| --- | --- |
| inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-controller.md#gamepad_buttoninputmonitorcallback)，不能为空，否则将返回错误码。 |

**返回：**

函数的执行结果，错误码[GameController\_ErrorCode](capi-game-controller.md#gamecontroller_errorcode)：

* GAME\_CONTROLLER\_SUCCESS：成功。
* GAME\_CONTROLLER\_PARAM\_ERROR：参数inputMonitorCallback为null。

### OH\_GamePad\_RightTrigger\_UnregisterAxisInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterAxisInputMonitor (void)
```

**描述**

取消注册RightTrigger轴事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。

### OH\_GamePad\_RightTrigger\_UnregisterButtonInputMonitor()

PhonePC/2in1TabletTV

```
1. GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterButtonInputMonitor (void)
```

**描述**

取消注册RightTrigger按键事件的监听回调。

**起始版本：** 21

**返回：**

函数的执行结果，执行成功返回GAME\_CONTROLLER\_SUCCESS。
