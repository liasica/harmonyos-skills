---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad-event-h
title: game_pad_event.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件 > game_pad_event.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e23617c9b5f61982304d67ff36bee31615cca8741a2447bdb6b703c57040367c
---

## 概述

定义游戏手柄事件的接口。

**引用文件：** <GameControllerKit/game\_pad\_event.h>

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：** [GameController](capi-gamecontroller.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md) | GamePad\_ButtonEvent | 定义手柄按键事件。 |
| [GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md) | GamePad\_AxisEvent | 定义手柄轴事件。 |
| [GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md) | GamePad\_PressedButton | 定义手柄按下的按键。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [GamePad\_AxisSourceType](capi-game-pad-event-h.md#gamepad_axissourcetype) | GamePad\_AxisSourceType | 此枚举定义手柄轴事件来源类型。 |
| [GamePad\_Button\_ActionType](capi-game-pad-event-h.md#gamepad_button_actiontype) | GamePad\_Button\_ActionType | 此枚举定义手柄按键动作类型。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void(\*GamePad\_ButtonInputMonitorCallback)(const struct GamePad\_ButtonEvent\* buttonEvent)](capi-game-pad-event-h.md#gamepad_buttoninputmonitorcallback) | GamePad\_ButtonInputMonitorCallback | 定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。 |
| [typedef void(\*GamePad\_AxisInputMonitorCallback)(const struct GamePad\_AxisEvent\* axisEvent)](capi-game-pad-event-h.md#gamepad_axisinputmonitorcallback) | GamePad\_AxisInputMonitorCallback | 定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonEvent\_GetDeviceId(const struct GamePad\_ButtonEvent\* buttonEvent, char\*\* deviceId)](capi-game-pad-event-h.md#oh_gamepad_buttonevent_getdeviceid) | - | 从按键事件中获取设备ID。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonEvent\_GetButtonAction(const struct GamePad\_ButtonEvent\* buttonEvent, GamePad\_Button\_ActionType\* actionType)](capi-game-pad-event-h.md#oh_gamepad_buttonevent_getbuttonaction) | - | 从按键事件中获取按键动作类型。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonEvent\_GetButtonCode(const struct GamePad\_ButtonEvent\* buttonEvent, int32\_t\* code)](capi-game-pad-event-h.md#oh_gamepad_buttonevent_getbuttoncode) | - | 从按键事件中获取按键编码。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonEvent\_GetButtonCodeName(const struct GamePad\_ButtonEvent\* buttonEvent, char\*\* codeName)](capi-game-pad-event-h.md#oh_gamepad_buttonevent_getbuttoncodename) | - | 从按键事件中获取按键名称。 |
| [GameController\_ErrorCode OH\_GamePad\_PressedButtons\_GetCount(const struct GamePad\_ButtonEvent\* buttonEvent, int32\_t\* count)](capi-game-pad-event-h.md#oh_gamepad_pressedbuttons_getcount) | - | 从按键事件中获取按下的按键数量。 |
| [GameController\_ErrorCode OH\_GamePad\_PressedButtons\_GetButtonInfo(const struct GamePad\_ButtonEvent\* buttonEvent, const int32\_t index, GamePad\_PressedButton\*\* pressedButton)](capi-game-pad-event-h.md#oh_gamepad_pressedbuttons_getbuttoninfo) | - | 从按键事件中获取指定索引的按键信息。 |
| [GameController\_ErrorCode OH\_GamePad\_DestroyPressedButton(GamePad\_PressedButton\*\* pressedButton)](capi-game-pad-event-h.md#oh_gamepad_destroypressedbutton) | - | 销毁按下的按键实例。 |
| [GameController\_ErrorCode OH\_GamePad\_PressedButton\_GetButtonCode(const struct GamePad\_PressedButton\* pressedButton, int32\_t\* code)](capi-game-pad-event-h.md#oh_gamepad_pressedbutton_getbuttoncode) | - | 从按下的按键中获取按键编码。 |
| [GameController\_ErrorCode OH\_GamePad\_PressedButton\_GetButtonCodeName(const struct GamePad\_PressedButton\* pressedButton, char\*\* codeName)](capi-game-pad-event-h.md#oh_gamepad_pressedbutton_getbuttoncodename) | - | 从按下的按键中获取按键名称。 |
| [GameController\_ErrorCode OH\_GamePad\_ButtonEvent\_GetActionTime(const struct GamePad\_ButtonEvent\* buttonEvent, int64\_t\* actionTime)](capi-game-pad-event-h.md#oh_gamepad_buttonevent_getactiontime) | - | 从按键事件中获取动作时间。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetDeviceId(const struct GamePad\_AxisEvent\* axisEvent, char\*\* deviceId)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getdeviceid) | - | 从轴事件中获取设备ID。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetAxisSourceType(const struct GamePad\_AxisEvent\* axisEvent, GamePad\_AxisSourceType\* axisSourceType)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getaxissourcetype) | - | 从轴事件中获取轴事件来源类型。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetXAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getxaxisvalue) | - | 从轴事件中获取X轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetYAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getyaxisvalue) | - | 从轴事件中获取Y轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetZAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getzaxisvalue) | - | 从轴事件中获取Z轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetRZAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getrzaxisvalue) | - | 从轴事件中获取RZ轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetHatXAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_gethatxaxisvalue) | - | 从轴事件中获取HatX轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetHatYAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_gethatyaxisvalue) | - | 从轴事件中获取HatY轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetBrakeAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getbrakeaxisvalue) | - | 从轴事件中获取Brake轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetGasAxisValue(const struct GamePad\_AxisEvent\* axisEvent, double\* axisValue)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getgasaxisvalue) | - | 从轴事件中获取Gas轴的值。 |
| [GameController\_ErrorCode OH\_GamePad\_AxisEvent\_GetActionTime(const struct GamePad\_AxisEvent\* axisEvent, int64\_t\* actionTime)](capi-game-pad-event-h.md#oh_gamepad_axisevent_getactiontime) | - | 从轴事件中获取动作时间。 |

## 枚举类型说明

### GamePad\_AxisSourceType

```c
enum GamePad_AxisSourceType
```

**描述**

此枚举定义手柄轴事件来源类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| DPAD = 0 | 轴事件来源于方向按键DPAD。  **起始版本：** 21 |
| LEFT\_THUMBSTICK = 1 | 轴事件来源于LeftThumbstick。  **起始版本：** 21 |
| RIGHT\_THUMBSTICK = 2 | 轴事件来源于RightThumbstick。  **起始版本：** 21 |
| LEFT\_TRIGGER = 3 | 轴事件来源于LeftTrigger。  **起始版本：** 21 |
| RIGHT\_TRIGGER = 4 | 轴事件来源于RightTrigger。  **起始版本：** 21 |

### GamePad\_Button\_ActionType

```c
enum GamePad_Button_ActionType
```

**描述**

此枚举定义手柄按键动作类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

| 枚举项 | 描述 |
| --- | --- |
| DOWN = 0 | 按键按下。  **起始版本：** 21 |
| UP = 1 | 按键抬起。  **起始版本：** 21 |

## 函数说明

### GamePad\_ButtonInputMonitorCallback()

```c
typedef void(*GamePad_ButtonInputMonitorCallback)(const struct GamePad_ButtonEvent* buttonEvent)
```

**描述**

定义在按键事件注册监听接口中使用的回调函数。当玩家按下按键时，该回调函数将被调用。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct GamePad\_ButtonEvent\* buttonEvent | 输入参数，手柄按键事件[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)。 |

### GamePad\_AxisInputMonitorCallback()

```c
typedef void(*GamePad_AxisInputMonitorCallback)(const struct GamePad_AxisEvent* axisEvent)
```

**描述**

定义在轴事件注册监听接口中使用的回调函数。当玩家操作摇杆时，该回调函数将被调用。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct GamePad\_AxisEvent\* axisEvent | 输入参数，手柄轴事件[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)。 |

### OH\_GamePad\_ButtonEvent\_GetDeviceId()

```c
GameController_ErrorCode OH_GamePad_ButtonEvent_GetDeviceId(const struct GamePad_ButtonEvent* buttonEvent, char** deviceId)
```

**描述**

从按键事件中获取设备ID。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| char\*\* deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent或deviceId为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonEvent\_GetButtonAction()

```c
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonAction(const struct GamePad_ButtonEvent* buttonEvent, GamePad_Button_ActionType* actionType)
```

**描述**

从按键事件中获取按键动作类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| [GamePad\_Button\_ActionType](capi-game-pad-event-h.md#gamepad_button_actiontype)\* actionType | 输出参数，按键动作类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonEvent\_GetButtonCode()

```c
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCode(const struct GamePad_ButtonEvent* buttonEvent, int32_t* code)
```

**描述**

从按键事件中获取按键编码。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| int32\_t\* code | 输出参数，按键编码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonEvent\_GetButtonCodeName()

```c
GameController_ErrorCode OH_GamePad_ButtonEvent_GetButtonCodeName(const struct GamePad_ButtonEvent* buttonEvent, char** codeName)
```

**描述**

从按键事件中获取按键名称。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| char\*\* codeName | 输出参数，二级指针指向按键名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent或codeName为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_PressedButtons\_GetCount()

```c
GameController_ErrorCode OH_GamePad_PressedButtons_GetCount(const struct GamePad_ButtonEvent* buttonEvent, int32_t* count)
```

**描述**

从按键事件中获取按下的按键数量。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| int32\_t\* count | 输出参数，按键数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_PressedButtons\_GetButtonInfo()

```c
GameController_ErrorCode OH_GamePad_PressedButtons_GetButtonInfo(const struct GamePad_ButtonEvent* buttonEvent, const int32_t index, GamePad_PressedButton** pressedButton)
```

**描述**

从按键事件中获取指定索引的按键信息。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| const int32\_t index | 指定按键索引。 |
| [GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)\*\* pressedButton | 输出参数，二级指针指向按下的按键。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent为null，或index小于0或大于等于按键总数，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_DestroyPressedButton()

```c
GameController_ErrorCode OH_GamePad_DestroyPressedButton(GamePad_PressedButton** pressedButton)
```

**描述**

销毁按下的按键实例。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)\*\* pressedButton | 二级指针指向[GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)实例，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数pressedButton为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_PressedButton\_GetButtonCode()

```c
GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCode(const struct GamePad_PressedButton* pressedButton, int32_t* code)
```

**描述**

从按下的按键中获取按键编码。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)\* pressedButton | 指针指向[GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)实例，不能为空。 |
| int32\_t\* code | 输出参数，按键编码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数pressedButton为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_PressedButton\_GetButtonCodeName()

```c
GameController_ErrorCode OH_GamePad_PressedButton_GetButtonCodeName(const struct GamePad_PressedButton* pressedButton, char** codeName)
```

**描述**

从按下的按键中获取按键名称。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)\* pressedButton | 指针指向[GamePad\_PressedButton](capi-gamecontroller-gamepad-pressedbutton.md)实例，不能为空。 |
| char\*\* codeName | 输出参数，二级指针指向按键名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数pressedButton或codeName为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_ButtonEvent\_GetActionTime()

```c
GameController_ErrorCode OH_GamePad_ButtonEvent_GetActionTime(const struct GamePad_ButtonEvent* buttonEvent, int64_t* actionTime)
```

**描述**

从按键事件中获取动作时间。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)\* buttonEvent | 指针指向[GamePad\_ButtonEvent](capi-gamecontroller-gamepad-buttonevent.md)实例，不能为空。 |
| int64\_t\* actionTime | 输出参数，动作时间。Unix时间戳，单位：ms。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数buttonEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetDeviceId()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetDeviceId(const struct GamePad_AxisEvent* axisEvent, char** deviceId)
```

**描述**

从轴事件中获取设备ID。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| char\*\* deviceId | 输出参数，二级指针指向设备ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent或deviceId为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果设备内存不足，返回[GAME\_CONTROLLER\_NO\_MEMORY](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetAxisSourceType()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetAxisSourceType(const struct GamePad_AxisEvent* axisEvent, GamePad_AxisSourceType* axisSourceType)
```

**描述**

从轴事件中获取轴事件来源类型。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| [GamePad\_AxisSourceType](capi-game-pad-event-h.md#gamepad_axissourcetype)\* axisSourceType | 输出参数，轴事件来源类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetXAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetXAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取X轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetYAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetYAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取Y轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetZAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetZAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取Z轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetRZAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetRZAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取RZ轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetHatXAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetHatXAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取HatX轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetHatYAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetHatYAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取HatY轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetBrakeAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetBrakeAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取Brake轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetGasAxisValue()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetGasAxisValue(const struct GamePad_AxisEvent* axisEvent, double* axisValue)
```

**描述**

从轴事件中获取Gas轴的值。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| double\* axisValue | 输出参数，轴值。取值范围为[-1.0, 1.0]。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |

### OH\_GamePad\_AxisEvent\_GetActionTime()

```c
GameController_ErrorCode OH_GamePad_AxisEvent_GetActionTime(const struct GamePad_AxisEvent* axisEvent, int64_t* actionTime)
```

**描述**

从轴事件中获取动作时间。

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)\* axisEvent | 指针指向[GamePad\_AxisEvent](capi-gamecontroller-gamepad-axisevent.md)实例，不能为空。 |
| int64\_t\* actionTime | 输出参数，动作时间。Unix时间戳，单位：ms。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [GameController\_ErrorCode](capi-game-controller-type-h.md#gamecontroller_errorcode) | * 如果执行成功，返回[GAME\_CONTROLLER\_SUCCESS](capi-game-controller-type-h.md#gamecontroller_errorcode)。 * 如果参数axisEvent为null，返回[GAME\_CONTROLLER\_PARAM\_ERROR](capi-game-controller-type-h.md#gamecontroller_errorcode)。 |
