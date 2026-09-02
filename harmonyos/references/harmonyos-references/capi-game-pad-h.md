---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad-h
title: game_pad.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件 > game_pad.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:37348c77337feb109630cbfd0a62918ee36ec46f0d953fc5bdc5bf60242ae8f4
---

## 概述

定义游戏手柄的接口。

**引用文件：** <GameControllerKit/game\_pad.h>

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：** [GameController](capi-gamecontroller.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [GameController\_ErrorCode OH\_GamePad\_LeftShoulder\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_leftshoulder_registerbuttoninputmonitor) | 注册LeftShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftShoulder\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_leftshoulder_unregisterbuttoninputmonitor) | 取消注册LeftShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightShoulder\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_rightshoulder_registerbuttoninputmonitor) | 注册RightShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightShoulder\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_rightshoulder_unregisterbuttoninputmonitor) | 取消注册RightShoulder按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftTrigger\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_lefttrigger_registerbuttoninputmonitor) | 注册LeftTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftTrigger\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_lefttrigger_unregisterbuttoninputmonitor) | 取消注册LeftTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftTrigger\_RegisterAxisInputMonitor(GamePad\_AxisInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_lefttrigger_registeraxisinputmonitor) | 注册LeftTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftTrigger\_UnregisterAxisInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_lefttrigger_unregisteraxisinputmonitor) | 取消注册LeftTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightTrigger\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_righttrigger_registerbuttoninputmonitor) | 注册RightTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightTrigger\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_righttrigger_unregisterbuttoninputmonitor) | 取消注册RightTrigger按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightTrigger\_RegisterAxisInputMonitor(GamePad\_AxisInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_righttrigger_registeraxisinputmonitor) | 注册RightTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightTrigger\_UnregisterAxisInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_righttrigger_unregisteraxisinputmonitor) | 取消注册RightTrigger轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonMenu\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttonmenu_registerbuttoninputmonitor) | 注册Menu按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonMenu\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttonmenu_unregisterbuttoninputmonitor) | 取消注册Menu按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonHome\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttonhome_registerbuttoninputmonitor) | 注册Home按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonHome\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttonhome_unregisterbuttoninputmonitor) | 取消注册Home按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonA\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttona_registerbuttoninputmonitor) | 注册A按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonA\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttona_unregisterbuttoninputmonitor) | 取消注册A按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonB\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttonb_registerbuttoninputmonitor) | 注册B按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonB\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttonb_unregisterbuttoninputmonitor) | 取消注册B按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonX\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttonx_registerbuttoninputmonitor) | 注册X按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonX\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttonx_unregisterbuttoninputmonitor) | 取消注册X按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonY\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttony_registerbuttoninputmonitor) | 注册Y按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonY\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttony_unregisterbuttoninputmonitor) | 取消注册Y按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonC\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_buttonc_registerbuttoninputmonitor) | 注册C按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonC\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_buttonc_unregisterbuttoninputmonitor) | 取消注册C按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_LeftButton\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_dpad_leftbutton_registerbuttoninputmonitor) | 注册方向按键的向左按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_LeftButton\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_dpad_leftbutton_unregisterbuttoninputmonitor) | 取消注册方向按键的向左按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_RightButton\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_dpad_rightbutton_registerbuttoninputmonitor) | 注册方向按键的向右按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_RightButton\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_dpad_rightbutton_unregisterbuttoninputmonitor) | 取消注册方向按键的向右按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_UpButton\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_dpad_upbutton_registerbuttoninputmonitor) | 注册方向按键的向上按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_UpButton\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_dpad_upbutton_unregisterbuttoninputmonitor) | 取消注册方向按键的向上按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_DownButton\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_dpad_downbutton_registerbuttoninputmonitor) | 注册方向按键的向下按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_DownButton\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_dpad_downbutton_unregisterbuttoninputmonitor) | 取消注册方向按键的向下按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_RegisterAxisInputMonitor(GamePad\_AxisInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_dpad_registeraxisinputmonitor) | 注册方向按键轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_Dpad\_UnregisterAxisInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_dpad_unregisteraxisinputmonitor) | 取消注册方向按键轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftThumbstick\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_leftthumbstick_registerbuttoninputmonitor) | 注册LeftThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftThumbstick\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_leftthumbstick_unregisterbuttoninputmonitor) | 取消注册LeftThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftThumbstick\_RegisterAxisInputMonitor(GamePad\_AxisInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_leftthumbstick_registeraxisinputmonitor) | 注册LeftThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_LeftThumbstick\_UnregisterAxisInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_leftthumbstick_unregisteraxisinputmonitor) | 取消注册LeftThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightThumbstick\_RegisterButtonInputMonitor(GamePad\_ButtonInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_rightthumbstick_registerbuttoninputmonitor) | 注册RightThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightThumbstick\_UnregisterButtonInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_rightthumbstick_unregisterbuttoninputmonitor) | 取消注册RightThumbstick按键事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightThumbstick\_RegisterAxisInputMonitor(GamePad\_AxisInputMonitorCallback inputMonitorCallback)](capi-game-pad-h.md#oh_gamepad_rightthumbstick_registeraxisinputmonitor) | 注册RightThumbstick轴事件的监听回调。 |
| [GameController\_ErrorCode OH\_GamePad\_RightThumbstick\_UnregisterAxisInputMonitor(void)](capi-game-pad-h.md#oh_gamepad_rightthumbstick_unregisteraxisinputmonitor) | 取消注册RightThumbstick轴事件的监听回调。 |

## 函数说明

### OH\_GamePad\_LeftShoulder\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftShoulder_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftShoulder按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftShoulder\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册LeftShoulder按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightShoulder\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightShoulder_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightShoulder按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightShoulder\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightShoulder_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册RightShoulder按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftTrigger\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftTrigger按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftTrigger\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册LeftTrigger按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftTrigger\_RegisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftTrigger_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftTrigger轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftTrigger\_UnregisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftTrigger_UnregisterAxisInputMonitor(void)
```

**描述**

取消注册LeftTrigger轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightTrigger\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightTrigger_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightTrigger按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightTrigger\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册RightTrigger按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightTrigger\_RegisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightTrigger_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightTrigger轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightTrigger\_UnregisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightTrigger_UnregisterAxisInputMonitor(void)
```

**描述**

取消注册RightTrigger轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonMenu\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonMenu_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Menu按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonMenu\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonMenu_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册Menu按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonHome\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonHome_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Home按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonHome\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonHome_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册Home按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonA\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonA_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册A按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonA\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonA_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册A按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonB\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonB_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册B按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonB\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonB_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册B按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonX\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonX_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册X按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonX\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonX_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册X按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonY\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonY_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册Y按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonY\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonY_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册Y按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonC\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonC_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册C按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonC\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_ButtonC_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册C按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_LeftButton\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_LeftButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向左按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_LeftButton\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_LeftButton_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册方向按键的向左按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_RightButton\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_RightButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向右按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_RightButton\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_RightButton_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册方向按键的向右按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_UpButton\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_UpButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向上按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_UpButton\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_UpButton_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册方向按键的向上按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_DownButton\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_DownButton_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键的向下按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_DownButton\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_DownButton_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册方向按键的向下按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_RegisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册方向按键轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_Dpad\_UnregisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_Dpad_UnregisterAxisInputMonitor(void)
```

**描述**

取消注册方向按键轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftThumbstick\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftThumbstick按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftThumbstick\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册LeftThumbstick按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftThumbstick\_RegisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册LeftThumbstick轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_LeftThumbstick\_UnregisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor(void)
```

**描述**

取消注册LeftThumbstick轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightThumbstick\_RegisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterButtonInputMonitor(GamePad_ButtonInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightThumbstick按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_ButtonInputMonitorCallback](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightThumbstick\_UnregisterButtonInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterButtonInputMonitor(void)
```

**描述**

取消注册RightThumbstick按键事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightThumbstick\_RegisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightThumbstick_RegisterAxisInputMonitor(GamePad_AxisInputMonitorCallback inputMonitorCallback)
```

**描述**

注册RightThumbstick轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback) inputMonitorCallback | 回调函数[GamePad\_AxisInputMonitorCallback](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback)，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数inputMonitorCallback为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_RightThumbstick\_UnregisterAxisInputMonitor()

```c
GameController_ErrorCode OH_GamePad_RightThumbstick_UnregisterAxisInputMonitor(void)
```

**描述**

取消注册RightThumbstick轴事件的监听回调。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |
