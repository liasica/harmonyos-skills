---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-input-manager-h
title: oh_input_manager.h
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > C API > 头文件 > oh_input_manager.h
category: harmonyos-references
scraped_at: 2026-04-28T08:10:18+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:728ee5340afe49fc4cb56062e5ed2cc407827ecdee7999d38a18f788aa8690fa
---

## 概述

PhonePC/2in1TabletTVWearable

提供事件注入和关键状态查询等功能。

**引用文件：** <multimodalinput/oh\_input\_manager.h>

**库：** libohinput.so

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**相关模块：** [input](capi-input.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Input\_InterceptorEventCallback](capi-input-input-interceptoreventcallback.md) | Input\_InterceptorEventCallback | 拦截回调事件结构体，拦截鼠标事件、触屏输入事件和轴事件。 |
| [Input\_DeviceListener](capi-input-input-devicelistener.md) | Input\_DeviceListener | 定义一个结构体用于监听设备热插拔。 |
| [OH\_PixelmapNative](capi-input-oh-pixelmapnative.md) | OH\_PixelmapNative | 像素图。 |
| [Input\_KeyState](capi-input-input-keystate.md) | Input\_KeyState | 定义按键信息，用于标识按键行为。例如，“Ctrl”按键信息包含键值和键类型。 |
| [Input\_KeyEvent](capi-input-input-keyevent.md) | Input\_KeyEvent | 按键事件对象。 |
| [Input\_MouseEvent](capi-input-input-mouseevent.md) | Input\_MouseEvent | 鼠标事件对象。 |
| [Input\_TouchEvent](capi-input-input-touchevent.md) | Input\_TouchEvent | 触屏输入事件对象。 |
| [Input\_AxisEvent](capi-input-input-axisevent.md) | Input\_AxisEvent | 轴事件对象。 |
| [Input\_Hotkey](capi-input-input-hotkey.md) | Input\_Hotkey | 定义快捷键结构体。 |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) | Input\_DeviceInfo | 输入设备信息。 |
| [Input\_InterceptorOptions](capi-input-input-interceptoroptions.md) | Input\_InterceptorOptions | 事件拦截选项。 |
| [Input\_CustomCursor](capi-input-input-customcursor.md) | Input\_CustomCursor | 自定义鼠标光标像素图资源。 |
| [Input\_CursorConfig](capi-input-input-cursorconfig.md) | Input\_CursorConfig | 自定义鼠标光标配置。 |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md) | Input\_CursorInfo | 定义鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction) | Input\_KeyStateAction | 按键状态的枚举值。 |
| [Input\_KeyEventAction](capi-oh-input-manager-h.md#input_keyeventaction) | Input\_KeyEventAction | 按键事件类型的枚举值。 |
| [Input\_MouseEventAction](capi-oh-input-manager-h.md#input_mouseeventaction) | Input\_MouseEventAction | 鼠标动作的枚举值。 |
| [InputEvent\_MouseAxis](capi-oh-input-manager-h.md#inputevent_mouseaxis) | InputEvent\_MouseAxis | 鼠标轴事件类型。 |
| [Input\_MouseEventButton](capi-oh-input-manager-h.md#input_mouseeventbutton) | Input\_MouseEventButton | 鼠标按键的枚举值。 |
| [Input\_TouchEventAction](capi-oh-input-manager-h.md#input_toucheventaction) | Input\_TouchEventAction | 触屏动作的枚举值。 |
| [Input\_InjectionStatus](capi-oh-input-manager-h.md#input_injectionstatus) | Input\_InjectionStatus | 注入权限状态枚举值。 |
| [InputEvent\_SourceType](capi-oh-input-manager-h.md#inputevent_sourcetype) | InputEvent\_SourceType | 输入事件源类型。 |
| [Input\_KeyboardType](capi-oh-input-manager-h.md#input_keyboardtype) | Input\_KeyboardType | 输入设备的键盘类型。 |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | Input\_Result | 返回值枚举值。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*Input\_HotkeyCallback)(Input\_Hotkey\* hotkey)](capi-oh-input-manager-h.md#input_hotkeycallback) | Input\_HotkeyCallback | 回调函数，用于回调快捷键事件。 |
| [typedef void (\*Input\_KeyEventCallback)(const Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#input_keyeventcallback) | Input\_KeyEventCallback | 按键事件的回调函数，keyEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_MouseEventCallback)(const Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#input_mouseeventcallback) | Input\_MouseEventCallback | 鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_TouchEventCallback)(const Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#input_toucheventcallback) | Input\_TouchEventCallback | 触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_AxisEventCallback)(const Input\_AxisEvent\* axisEvent)](capi-oh-input-manager-h.md#input_axiseventcallback) | Input\_AxisEventCallback | 轴事件的回调函数，axisEvent的生命周期为回调函数内。 |
| [typedef void (\*Input\_DeviceAddedCallback)(int32\_t deviceId)](capi-oh-input-manager-h.md#input_deviceaddedcallback) | Input\_DeviceAddedCallback | 回调函数，用于回调输入设备的热插事件。 |
| [typedef void (\*Input\_DeviceRemovedCallback)(int32\_t deviceId)](capi-oh-input-manager-h.md#input_deviceremovedcallback) | Input\_DeviceRemovedCallback | 回调函数，用于回调输入设备的热拔事件。 |
| [typedef void (\*Input\_InjectAuthorizeCallback)(Input\_InjectionStatus authorizedStatus)](capi-oh-input-manager-h.md#input_injectauthorizecallback) | Input\_InjectAuthorizeCallback | 回调函数，用于获取注入权限状态。 |
| [Input\_Result OH\_Input\_GetKeyState(struct Input\_KeyState\* keyState)](capi-oh-input-manager-h.md#oh_input_getkeystate) | - | 查询按键状态的枚举对象。 |
| [struct Input\_KeyState\* OH\_Input\_CreateKeyState()](capi-oh-input-manager-h.md#oh_input_createkeystate) | - | 创建按键状态的枚举对象。通过调用[OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate)销毁按键状态的枚举对象。 |
| [void OH\_Input\_DestroyKeyState(struct Input\_KeyState\*\* keyState)](capi-oh-input-manager-h.md#oh_input_destroykeystate) | - | 销毁按键状态的枚举对象。 |
| [void OH\_Input\_SetKeyCode(struct Input\_KeyState\* keyState, int32\_t keyCode)](capi-oh-input-manager-h.md#oh_input_setkeycode) | - | 设置按键状态对象的键值。 |
| [int32\_t OH\_Input\_GetKeyCode(const struct Input\_KeyState\* keyState)](capi-oh-input-manager-h.md#oh_input_getkeycode) | - | 获取按键状态对象的键值。 |
| [void OH\_Input\_SetKeyPressed(struct Input\_KeyState\* keyState, int32\_t keyAction)](capi-oh-input-manager-h.md#oh_input_setkeypressed) | - | 设置按键状态对象的按键是否按下。 |
| [int32\_t OH\_Input\_GetKeyPressed(const struct Input\_KeyState\* keyState)](capi-oh-input-manager-h.md#oh_input_getkeypressed) | - | 获取按键状态对象的按键是否按下。 |
| [void OH\_Input\_SetKeySwitch(struct Input\_KeyState\* keyState, int32\_t keySwitch)](capi-oh-input-manager-h.md#oh_input_setkeyswitch) | - | 设置按键状态对象的按键开关。 |
| [int32\_t OH\_Input\_GetKeySwitch(const struct Input\_KeyState\* keyState)](capi-oh-input-manager-h.md#oh_input_getkeyswitch) | - | 获取按键状态对象的按键开关。 |
| [int32\_t OH\_Input\_InjectKeyEvent(const struct Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#oh_input_injectkeyevent) | - | 注入按键事件。 |
| [struct Input\_KeyEvent\* OH\_Input\_CreateKeyEvent()](capi-oh-input-manager-h.md#oh_input_createkeyevent) | - | 创建按键事件对象。通过调用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)销毁按键事件对象。 |
| [void OH\_Input\_DestroyKeyEvent(struct Input\_KeyEvent\*\* keyEvent)](capi-oh-input-manager-h.md#oh_input_destroykeyevent) | - | 销毁按键事件对象。 |
| [void OH\_Input\_SetKeyEventAction(struct Input\_KeyEvent\* keyEvent, int32\_t action)](capi-oh-input-manager-h.md#oh_input_setkeyeventaction) | - | 设置按键事件类型。 |
| [int32\_t OH\_Input\_GetKeyEventAction(const struct Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#oh_input_getkeyeventaction) | - | 获取按键事件类型。 |
| [void OH\_Input\_SetKeyEventKeyCode(struct Input\_KeyEvent\* keyEvent, int32\_t keyCode)](capi-oh-input-manager-h.md#oh_input_setkeyeventkeycode) | - | 设置按键事件的键值。 |
| [int32\_t OH\_Input\_GetKeyEventKeyCode(const struct Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#oh_input_getkeyeventkeycode) | - | 获取按键事件的键值。 |
| [void OH\_Input\_SetKeyEventActionTime(struct Input\_KeyEvent\* keyEvent, int64\_t actionTime)](capi-oh-input-manager-h.md#oh_input_setkeyeventactiontime) | - | 设置按键事件发生的时间。 |
| [int64\_t OH\_Input\_GetKeyEventActionTime(const struct Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#oh_input_getkeyeventactiontime) | - | 获取按键事件发生的时间。 |
| [void OH\_Input\_SetKeyEventWindowId(struct Input\_KeyEvent\* keyEvent, int32\_t windowId)](capi-oh-input-manager-h.md#oh_input_setkeyeventwindowid) | - | 设置按键事件的窗口ID。 |
| [int32\_t OH\_Input\_GetKeyEventWindowId(const struct Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#oh_input_getkeyeventwindowid) | - | 获取按键事件的窗口ID。 |
| [void OH\_Input\_SetKeyEventDisplayId(struct Input\_KeyEvent\* keyEvent, int32\_t displayId)](capi-oh-input-manager-h.md#oh_input_setkeyeventdisplayid) | - | 设置按键事件的屏幕ID。 |
| [int32\_t OH\_Input\_GetKeyEventDisplayId(const struct Input\_KeyEvent\* keyEvent)](capi-oh-input-manager-h.md#oh_input_getkeyeventdisplayid) | - | 获取按键事件的屏幕ID。 |
| [struct Input\_MouseEvent\* OH\_Input\_CreateMouseEvent()](capi-oh-input-manager-h.md#oh_input_createmouseevent) | - | 创建鼠标事件对象。通过调用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)销毁鼠标事件对象。 |
| [void OH\_Input\_DestroyMouseEvent(struct Input\_MouseEvent\*\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_destroymouseevent) | - | 销毁鼠标事件对象。 |
| [void OH\_Input\_SetMouseEventAction(struct Input\_MouseEvent\* mouseEvent, int32\_t action)](capi-oh-input-manager-h.md#oh_input_setmouseeventaction) | - | 设置鼠标事件的动作。 |
| [int32\_t OH\_Input\_GetMouseEventAction(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventaction) | - | 获取鼠标事件的动作。 |
| [void OH\_Input\_SetMouseEventDisplayX(struct Input\_MouseEvent\* mouseEvent, int32\_t displayX)](capi-oh-input-manager-h.md#oh_input_setmouseeventdisplayx) | - | 设置鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |
| [int32\_t OH\_Input\_GetMouseEventDisplayX(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventdisplayx) | - | 获取鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |
| [void OH\_Input\_SetMouseEventDisplayY(struct Input\_MouseEvent\* mouseEvent, int32\_t displayY)](capi-oh-input-manager-h.md#oh_input_setmouseeventdisplayy) | - | 设置鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |
| [int32\_t OH\_Input\_GetMouseEventDisplayY(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventdisplayy) | - | 获取鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |
| [void OH\_Input\_SetMouseEventButton(struct Input\_MouseEvent\* mouseEvent, int32\_t button)](capi-oh-input-manager-h.md#oh_input_setmouseeventbutton) | - | 设置鼠标事件的按键。 |
| [int32\_t OH\_Input\_GetMouseEventButton(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventbutton) | - | 获取鼠标事件的按键。 |
| [void OH\_Input\_SetMouseEventAxisType(struct Input\_MouseEvent\* mouseEvent, int32\_t axisType)](capi-oh-input-manager-h.md#oh_input_setmouseeventaxistype) | - | 设置鼠标轴事件的类型。 |
| [int32\_t OH\_Input\_GetMouseEventAxisType(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventaxistype) | - | 获取鼠标轴事件的类型。 |
| [void OH\_Input\_SetMouseEventAxisValue(struct Input\_MouseEvent\* mouseEvent, float axisValue)](capi-oh-input-manager-h.md#oh_input_setmouseeventaxisvalue) | - | 设置鼠标轴事件的值。 |
| [float OH\_Input\_GetMouseEventAxisValue(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventaxisvalue) | - | 获取鼠标轴事件的值。 |
| [void OH\_Input\_SetMouseEventActionTime(struct Input\_MouseEvent\* mouseEvent, int64\_t actionTime)](capi-oh-input-manager-h.md#oh_input_setmouseeventactiontime) | - | 设置鼠标事件发生的时间。 |
| [int64\_t OH\_Input\_GetMouseEventActionTime(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventactiontime) | - | 获取鼠标事件发生的时间。 |
| [void OH\_Input\_SetMouseEventWindowId(struct Input\_MouseEvent\* mouseEvent, int32\_t windowId)](capi-oh-input-manager-h.md#oh_input_setmouseeventwindowid) | - | 设置鼠标事件的窗口ID。 |
| [int32\_t OH\_Input\_GetMouseEventWindowId(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventwindowid) | - | 获取鼠标事件的窗口ID。 |
| [void OH\_Input\_SetMouseEventDisplayId(struct Input\_MouseEvent\* mouseEvent, int32\_t displayId)](capi-oh-input-manager-h.md#oh_input_setmouseeventdisplayid) | - | 设置鼠标事件的屏幕ID。 |
| [struct Input\_TouchEvent\* OH\_Input\_CreateTouchEvent()](capi-oh-input-manager-h.md#oh_input_createtouchevent) | - | 创建触屏输入事件对象。通过调用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)销毁触屏输入事件对象。 |
| [void OH\_Input\_DestroyTouchEvent(struct Input\_TouchEvent\*\* touchEvent)](capi-oh-input-manager-h.md#oh_input_destroytouchevent) | - | 销毁触屏输入事件对象。 |
| [void OH\_Input\_SetTouchEventAction(struct Input\_TouchEvent\* touchEvent, int32\_t action)](capi-oh-input-manager-h.md#oh_input_settoucheventaction) | - | 设置触屏输入事件的动作。 |
| [int32\_t OH\_Input\_GetTouchEventAction(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventaction) | - | 获取触屏输入事件的动作。 |
| [void OH\_Input\_SetTouchEventFingerId(struct Input\_TouchEvent\* touchEvent, int32\_t id)](capi-oh-input-manager-h.md#oh_input_settoucheventfingerid) | - | 设置触屏输入事件的手指ID。 |
| [int32\_t OH\_Input\_GetTouchEventFingerId(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventfingerid) | - | 获取触屏输入事件的手指ID。 |
| [void OH\_Input\_SetTouchEventDisplayX(struct Input\_TouchEvent\* touchEvent, int32\_t displayX)](capi-oh-input-manager-h.md#oh_input_settoucheventdisplayx) | - | 设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |
| [int32\_t OH\_Input\_GetTouchEventDisplayX(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventdisplayx) | - | 获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |
| [void OH\_Input\_SetTouchEventDisplayY(struct Input\_TouchEvent\* touchEvent, int32\_t displayY)](capi-oh-input-manager-h.md#oh_input_settoucheventdisplayy) | - | 设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |
| [int32\_t OH\_Input\_GetTouchEventDisplayY(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventdisplayy) | - | 获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |
| [void OH\_Input\_SetTouchEventActionTime(struct Input\_TouchEvent\* touchEvent, int64\_t actionTime)](capi-oh-input-manager-h.md#oh_input_settoucheventactiontime) | - | 设置触屏输入事件发生的时间。 |
| [int64\_t OH\_Input\_GetTouchEventActionTime(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventactiontime) | - | 获取触屏输入事件发生的时间。 |
| [void OH\_Input\_SetTouchEventWindowId(struct Input\_TouchEvent\* touchEvent, int32\_t windowId)](capi-oh-input-manager-h.md#oh_input_settoucheventwindowid) | - | 设置触屏输入事件的窗口ID。 |
| [int32\_t OH\_Input\_GetTouchEventWindowId(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventwindowid) | - | 获取触屏输入事件的窗口ID。 |
| [void OH\_Input\_SetTouchEventDisplayId(struct Input\_TouchEvent\* touchEvent, int32\_t displayId)](capi-oh-input-manager-h.md#oh_input_settoucheventdisplayid) | - | 设置触屏输入事件的屏幕ID。 |
| [int32\_t OH\_Input\_GetTouchEventDisplayId(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventdisplayid) | - | 获取触屏输入事件的屏幕ID。 |
| [void OH\_Input\_CancelInjection()](capi-oh-input-manager-h.md#oh_input_cancelinjection) | - | 取消事件注入并撤销授权。 |
| [Input\_Result OH\_Input\_RequestInjection(Input\_InjectAuthorizeCallback callback)](capi-oh-input-manager-h.md#oh_input_requestinjection) | - | 当前应用申请注入权限，包括申请注入按键事件[OH\_Input\_InjectKeyEvent](capi-oh-input-manager-h.md#oh_input_injectkeyevent)、注入触屏输入事件[OH\_Input\_InjectTouchEvent](capi-oh-input-manager-h.md#oh_input_injecttouchevent)、注入鼠标事件[OH\_Input\_InjectMouseEvent](capi-oh-input-manager-h.md#oh_input_injectmouseevent)等注入操作的权限。 |
| [Input\_Result OH\_Input\_QueryAuthorizedStatus(Input\_InjectionStatus\* status)](capi-oh-input-manager-h.md#oh_input_queryauthorizedstatus) | - | 查询当前应用注入的权限状态。 |
| [Input\_AxisEvent\* OH\_Input\_CreateAxisEvent(void)](capi-oh-input-manager-h.md#oh_input_createaxisevent) | - | 创建轴事件对象。通过调用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)销毁轴事件对象。 |
| [Input\_Result OH\_Input\_DestroyAxisEvent(Input\_AxisEvent\*\* axisEvent)](capi-oh-input-manager-h.md#oh_input_destroyaxisevent) | - | 销毁轴事件对象。 |
| [Input\_Result OH\_Input\_SetAxisEventAction(Input\_AxisEvent\* axisEvent, InputEvent\_AxisAction action)](capi-oh-input-manager-h.md#oh_input_setaxiseventaction) | - | 设置轴事件的动作。 |
| [Input\_Result OH\_Input\_GetAxisEventAction(const Input\_AxisEvent\* axisEvent, InputEvent\_AxisAction \*action)](capi-oh-input-manager-h.md#oh_input_getaxiseventaction) | - | 获取轴事件的动作。 |
| [Input\_Result OH\_Input\_SetAxisEventDisplayX(Input\_AxisEvent\* axisEvent, float displayX)](capi-oh-input-manager-h.md#oh_input_setaxiseventdisplayx) | - | 设置轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |
| [Input\_Result OH\_Input\_GetAxisEventDisplayX(const Input\_AxisEvent\* axisEvent, float\* displayX)](capi-oh-input-manager-h.md#oh_input_getaxiseventdisplayx) | - | 获取轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |
| [Input\_Result OH\_Input\_SetAxisEventDisplayY(Input\_AxisEvent\* axisEvent, float displayY)](capi-oh-input-manager-h.md#oh_input_setaxiseventdisplayy) | - | 设置轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |
| [Input\_Result OH\_Input\_GetAxisEventDisplayY(const Input\_AxisEvent\* axisEvent, float\* displayY)](capi-oh-input-manager-h.md#oh_input_getaxiseventdisplayy) | - | 获取轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |
| [Input\_Result OH\_Input\_SetAxisEventAxisValue(Input\_AxisEvent\* axisEvent,InputEvent\_AxisType axisType, double axisValue)](capi-oh-input-manager-h.md#oh_input_setaxiseventaxisvalue) | - | 设置轴事件指定轴类型的轴值。 |
| [Input\_Result OH\_Input\_GetAxisEventAxisValue(const Input\_AxisEvent\* axisEvent,InputEvent\_AxisType axisType, double\* axisValue)](capi-oh-input-manager-h.md#oh_input_getaxiseventaxisvalue) | - | 获取轴事件指定轴类型的轴值。 |
| [Input\_Result OH\_Input\_SetAxisEventActionTime(Input\_AxisEvent\* axisEvent, int64\_t actionTime)](capi-oh-input-manager-h.md#oh_input_setaxiseventactiontime) | - | 设置轴事件发生的时间。 |
| [Input\_Result OH\_Input\_GetAxisEventActionTime(const Input\_AxisEvent\* axisEvent, int64\_t\* actionTime)](capi-oh-input-manager-h.md#oh_input_getaxiseventactiontime) | - | 获取轴事件发生的时间。 |
| [Input\_Result OH\_Input\_SetAxisEventType(Input\_AxisEvent\* axisEvent, InputEvent\_AxisEventType axisEventType)](capi-oh-input-manager-h.md#oh_input_setaxiseventtype) | - | 设置轴事件类型。 |
| [Input\_Result OH\_Input\_GetAxisEventType(const Input\_AxisEvent\* axisEvent, InputEvent\_AxisEventType\* axisEventType)](capi-oh-input-manager-h.md#oh_input_getaxiseventtype) | - | 获取轴事件类型。 |
| [Input\_Result OH\_Input\_SetAxisEventSourceType(Input\_AxisEvent\* axisEvent, InputEvent\_SourceType sourceType)](capi-oh-input-manager-h.md#oh_input_setaxiseventsourcetype) | - | 设置轴事件源类型。 |
| [Input\_Result OH\_Input\_GetAxisEventSourceType(const Input\_AxisEvent\* axisEvent, InputEvent\_SourceType\* sourceType)](capi-oh-input-manager-h.md#oh_input_getaxiseventsourcetype) | - | 获取轴事件源类型。 |
| [Input\_Result OH\_Input\_SetAxisEventWindowId(Input\_AxisEvent\* axisEvent, int32\_t windowId)](capi-oh-input-manager-h.md#oh_input_setaxiseventwindowid) | - | 设置轴事件的窗口ID。 |
| [Input\_Result OH\_Input\_GetAxisEventWindowId(const Input\_AxisEvent\* axisEvent, int32\_t\* windowId)](capi-oh-input-manager-h.md#oh_input_getaxiseventwindowid) | - | 获取轴事件的窗口ID。 |
| [Input\_Result OH\_Input\_SetAxisEventDisplayId(Input\_AxisEvent\* axisEvent, int32\_t displayId)](capi-oh-input-manager-h.md#oh_input_setaxiseventdisplayid) | - | 设置轴事件的屏幕ID。 |
| [Input\_Result OH\_Input\_GetAxisEventDisplayId(const Input\_AxisEvent\* axisEvent, int32\_t\* displayId)](capi-oh-input-manager-h.md#oh_input_getaxiseventdisplayid) | - | 获取轴事件的屏幕ID。 |
| [Input\_Result OH\_Input\_AddKeyEventMonitor(Input\_KeyEventCallback callback)](capi-oh-input-manager-h.md#oh_input_addkeyeventmonitor) | - | 添加按键事件监听。重复添加只有第一次生效，后续添加请求将被忽略。 |
| [Input\_Result OH\_Input\_AddMouseEventMonitor(Input\_MouseEventCallback callback)](capi-oh-input-manager-h.md#oh_input_addmouseeventmonitor) | - | 添加鼠标事件监听，包含鼠标点击，移动，不包含滚轮事件，滚轮事件归属于轴事件。 |
| [Input\_Result OH\_Input\_AddTouchEventMonitor(Input\_TouchEventCallback callback)](capi-oh-input-manager-h.md#oh_input_addtoucheventmonitor) | - | 添加触屏输入事件监听。 |
| [Input\_Result OH\_Input\_AddAxisEventMonitorForAll(Input\_AxisEventCallback callback)](capi-oh-input-manager-h.md#oh_input_addaxiseventmonitorforall) | - | 添加所有类型轴事件监听，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。 |
| [Input\_Result OH\_Input\_AddAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback)](capi-oh-input-manager-h.md#oh_input_addaxiseventmonitor) | - | 添加指定类型的轴事件监听，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。 |
| [Input\_Result OH\_Input\_RemoveKeyEventMonitor(Input\_KeyEventCallback callback)](capi-oh-input-manager-h.md#oh_input_removekeyeventmonitor) | - | 移除按键事件监听。 |
| [Input\_Result OH\_Input\_RemoveMouseEventMonitor(Input\_MouseEventCallback callback)](capi-oh-input-manager-h.md#oh_input_removemouseeventmonitor) | - | 移除鼠标事件监听。 |
| [Input\_Result OH\_Input\_RemoveTouchEventMonitor(Input\_TouchEventCallback callback)](capi-oh-input-manager-h.md#oh_input_removetoucheventmonitor) | - | 移除触屏输入事件监听。 |
| [Input\_Result OH\_Input\_RemoveAxisEventMonitorForAll(Input\_AxisEventCallback callback)](capi-oh-input-manager-h.md#oh_input_removeaxiseventmonitorforall) | - | 移除所有类型轴事件监听。 |
| [Input\_Result OH\_Input\_RemoveAxisEventMonitor(InputEvent\_AxisEventType axisEventType, Input\_AxisEventCallback callback)](capi-oh-input-manager-h.md#oh_input_removeaxiseventmonitor) | - | 移除指定类型轴事件监听，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。 |
| [Input\_Result OH\_Input\_AddKeyEventInterceptor(Input\_KeyEventCallback callback, Input\_InterceptorOptions \*option)](capi-oh-input-manager-h.md#oh_input_addkeyeventinterceptor) | - | 添加按键事件的拦截，重复添加只有第一次生效，后续添加请求返回错误码[INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result)。仅在应用获焦时拦截按键事件。 |
| [Input\_Result OH\_Input\_AddInputEventInterceptor(Input\_InterceptorEventCallback \*callback,Input\_InterceptorOptions \*option)](capi-oh-input-manager-h.md#oh_input_addinputeventinterceptor) | - | 添加输入事件拦截，包括鼠标、触屏和轴事件。重复添加只有第一次生效，后续添加请求返回错误码[INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result)。仅命中应用窗口时拦截输入事件。 |
| [Input\_Result OH\_Input\_RemoveKeyEventInterceptor(void)](capi-oh-input-manager-h.md#oh_input_removekeyeventinterceptor) | - | 移除按键事件拦截。 |
| [Input\_Result OH\_Input\_RemoveInputEventInterceptor(void)](capi-oh-input-manager-h.md#oh_input_removeinputeventinterceptor) | - | 移除输入事件拦截，包括鼠标、触屏和轴事件。 |
| [Input\_Result OH\_Input\_GetIntervalSinceLastInput(int64\_t \*timeInterval)](capi-oh-input-manager-h.md#oh_input_getintervalsincelastinput) | - | 获取距离上次系统输入事件的时间间隔。 |
| [Input\_Hotkey \*OH\_Input\_CreateHotkey(void)](capi-oh-input-manager-h.md#oh_input_createhotkey) | - | 创建快捷键对象。通过调用[OH\_Input\_DestroyHotkey](capi-oh-input-manager-h.md#oh_input_destroyhotkey)销毁快捷键对象。 |
| [void OH\_Input\_DestroyHotkey(Input\_Hotkey \*\*hotkey)](capi-oh-input-manager-h.md#oh_input_destroyhotkey) | - | 销毁快捷键对象。 |
| [void OH\_Input\_SetPreKeys(Input\_Hotkey \*hotkey, int32\_t \*preKeys, int32\_t size)](capi-oh-input-manager-h.md#oh_input_setprekeys) | - | 设置修饰键。 |
| [Input\_Result OH\_Input\_GetPreKeys(const Input\_Hotkey \*hotkey, int32\_t \*\*preKeys, int32\_t \*preKeyCount)](capi-oh-input-manager-h.md#oh_input_getprekeys) | - | 获取修饰键。 |
| [void OH\_Input\_SetFinalKey(Input\_Hotkey\* hotkey, int32\_t finalKey)](capi-oh-input-manager-h.md#oh_input_setfinalkey) | - | 设置被修饰键。 |
| [Input\_Result OH\_Input\_GetFinalKey(const Input\_Hotkey\* hotkey, int32\_t \*finalKeyCode)](capi-oh-input-manager-h.md#oh_input_getfinalkey) | - | 获取被修饰键。 |
| [Input\_Hotkey \*\*OH\_Input\_CreateAllSystemHotkeys(int32\_t count)](capi-oh-input-manager-h.md#oh_input_createallsystemhotkeys) | - | 创建[Input\_Hotkey](capi-input-input-hotkey.md)类型实例的数组。通过调用[OH\_Input\_DestroyAllSystemHotkeys](capi-oh-input-manager-h.md#oh_input_destroyallsystemhotkeys)销毁[Input\_Hotkey](capi-input-input-hotkey.md)实例数组并回收内存。 |
| [void OH\_Input\_DestroyAllSystemHotkeys(Input\_Hotkey \*\*hotkeys, int32\_t count)](capi-oh-input-manager-h.md#oh_input_destroyallsystemhotkeys) | - | 销毁[Input\_Hotkey](capi-input-input-hotkey.md)实例数组并回收内存。 |
| [Input\_Result OH\_Input\_GetAllSystemHotkeys(Input\_Hotkey \*\*hotkey, int32\_t \*count)](capi-oh-input-manager-h.md#oh_input_getallsystemhotkeys) | - | 获取设置的所有快捷键。 |
| [void OH\_Input\_SetRepeat(Input\_Hotkey\* hotkey, bool isRepeat)](capi-oh-input-manager-h.md#oh_input_setrepeat) | - | 设置是否上报重复key事件。 |
| [Input\_Result OH\_Input\_GetRepeat(const Input\_Hotkey\* hotkey, bool \*isRepeat)](capi-oh-input-manager-h.md#oh_input_getrepeat) | - | 获取是否上报重复key事件。 |
| [Input\_Result OH\_Input\_AddHotkeyMonitor(const Input\_Hotkey\* hotkey, Input\_HotkeyCallback callback)](capi-oh-input-manager-h.md#oh_input_addhotkeymonitor) | - | 订阅快捷键事件。 |
| [Input\_Result OH\_Input\_RemoveHotkeyMonitor(const Input\_Hotkey\* hotkey, Input\_HotkeyCallback callback)](capi-oh-input-manager-h.md#oh_input_removehotkeymonitor) | - | 取消订阅快捷键。 |
| [Input\_Result OH\_Input\_RegisterDeviceListener(Input\_DeviceListener\* listener)](capi-oh-input-manager-h.md#oh_input_registerdevicelistener) | - | 注册设备热插拔的监听器。 |
| [Input\_Result OH\_Input\_UnregisterDeviceListener(Input\_DeviceListener\* listener)](capi-oh-input-manager-h.md#oh_input_unregisterdevicelistener) | - | 取消注册设备热插拔的监听。 |
| [Input\_Result OH\_Input\_UnregisterDeviceListeners()](capi-oh-input-manager-h.md#oh_input_unregisterdevicelisteners) | - | 取消注册所有的设备热插拔的监听。 |
| [Input\_Result OH\_Input\_GetDeviceIds(int32\_t \*deviceIds, int32\_t inSize, int32\_t \*outSize)](capi-oh-input-manager-h.md#oh_input_getdeviceids) | - | 获取所有输入设备的ID列表。 |
| [Input\_Result OH\_Input\_GetDevice(int32\_t deviceId, Input\_DeviceInfo \*\*deviceInfo)](capi-oh-input-manager-h.md#oh_input_getdevice) | - | 获取输入设备信息。 |
| [Input\_DeviceInfo\* OH\_Input\_CreateDeviceInfo(void)](capi-oh-input-manager-h.md#oh_input_createdeviceinfo) | - | 创建输入设备信息的对象。通过调用[OH\_Input\_DestroyDeviceInfo](capi-oh-input-manager-h.md#oh_input_destroydeviceinfo)销毁输入设备信息的对象。 |
| [void OH\_Input\_DestroyDeviceInfo(Input\_DeviceInfo \*\*deviceInfo)](capi-oh-input-manager-h.md#oh_input_destroydeviceinfo) | - | 销毁输入设备信息的对象。 |
| [Input\_Result OH\_Input\_GetKeyboardType(int32\_t deviceId, int32\_t \*keyboardType)](capi-oh-input-manager-h.md#oh_input_getkeyboardtype) | - | 获取输入设备的键盘类型。 |
| [Input\_Result OH\_Input\_GetDeviceId(Input\_DeviceInfo \*deviceInfo, int32\_t \*id)](capi-oh-input-manager-h.md#oh_input_getdeviceid) | - | 获取输入设备的ID。 |
| [Input\_Result OH\_Input\_GetDeviceName(Input\_DeviceInfo \*deviceInfo, char \*\*name)](capi-oh-input-manager-h.md#oh_input_getdevicename) | - | 获取输入设备的名称。 |
| [Input\_Result OH\_Input\_GetCapabilities(Input\_DeviceInfo \*deviceInfo, int32\_t \*capabilities)](capi-oh-input-manager-h.md#oh_input_getcapabilities) | - | 获取有关输入设备能力信息，比如设备是触摸屏、触控板、键盘等。 |
| [Input\_Result OH\_Input\_GetDeviceVersion(Input\_DeviceInfo \*deviceInfo, int32\_t \*version)](capi-oh-input-manager-h.md#oh_input_getdeviceversion) | - | 获取输入设备的版本信息。 |
| [Input\_Result OH\_Input\_GetDeviceProduct(Input\_DeviceInfo \*deviceInfo, int32\_t \*product)](capi-oh-input-manager-h.md#oh_input_getdeviceproduct) | - | 获取输入设备的产品信息。 |
| [Input\_Result OH\_Input\_GetDeviceVendor(Input\_DeviceInfo \*deviceInfo, int32\_t \*vendor)](capi-oh-input-manager-h.md#oh_input_getdevicevendor) | - | 获取输入设备的厂商信息。 |
| [Input\_Result OH\_Input\_GetDeviceAddress(Input\_DeviceInfo \*deviceInfo, char \*\*address)](capi-oh-input-manager-h.md#oh_input_getdeviceaddress) | - | 获取输入设备的物理地址。 |
| [Input\_Result OH\_Input\_GetFunctionKeyState(int32\_t keyCode, int32\_t \*state)](capi-oh-input-manager-h.md#oh_input_getfunctionkeystate) | - | 获取功能键状态。 |
| [int32\_t OH\_Input\_InjectTouchEvent(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_injecttouchevent) | - | 使用以指定屏幕左上角为原点的相对坐标系的坐标注入触屏输入事件。 |
| [int32\_t OH\_Input\_InjectMouseEvent(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_injectmouseevent) | - | 使用以指定屏幕左上角为原点的相对坐标系的坐标注入鼠标事件。 |
| [int32\_t OH\_Input\_GetMouseEventDisplayId(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventdisplayid) | - | 获取鼠标事件的屏幕ID。 |
| [Input\_Result OH\_Input\_QueryMaxTouchPoints(int32\_t \*count)](capi-oh-input-manager-h.md#oh_input_querymaxtouchpoints) | - | 查询设备支持的最大触屏报点数。 |
| [int32\_t OH\_Input\_InjectMouseEventGlobal(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_injectmouseeventglobal) | - | 使用以主屏左上角为原点的全局坐标系的坐标注入鼠标事件。 |
| [void OH\_Input\_SetMouseEventGlobalX(struct Input\_MouseEvent\* mouseEvent, int32\_t globalX)](capi-oh-input-manager-h.md#oh_input_setmouseeventglobalx) | - | 设置鼠标事件以主屏左上角为原点的全局坐标系的X坐标。 |
| [int32\_t OH\_Input\_GetMouseEventGlobalX(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventglobalx) | - | 获取鼠标事件以主屏左上角为原点的全局坐标系的X坐标。 |
| [void OH\_Input\_SetMouseEventGlobalY(struct Input\_MouseEvent\* mouseEvent, int32\_t globalY)](capi-oh-input-manager-h.md#oh_input_setmouseeventglobaly) | - | 设置鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。 |
| [int32\_t OH\_Input\_GetMouseEventGlobalY(const struct Input\_MouseEvent\* mouseEvent)](capi-oh-input-manager-h.md#oh_input_getmouseeventglobaly) | - | 获取鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。 |
| [int32\_t OH\_Input\_InjectTouchEventGlobal(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_injecttoucheventglobal) | - | 使用以主屏左上角为原点的全局坐标系的坐标注入触屏输入事件。 |
| [void OH\_Input\_SetTouchEventGlobalX(struct Input\_TouchEvent\* touchEvent, int32\_t globalX)](capi-oh-input-manager-h.md#oh_input_settoucheventglobalx) | - | 设置触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。 |
| [int32\_t OH\_Input\_GetTouchEventGlobalX(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventglobalx) | - | 获取触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。 |
| [void OH\_Input\_SetTouchEventGlobalY(struct Input\_TouchEvent\* touchEvent, int32\_t globalY)](capi-oh-input-manager-h.md#oh_input_settoucheventglobaly) | - | 设置触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。 |
| [int32\_t OH\_Input\_GetTouchEventGlobalY(const struct Input\_TouchEvent\* touchEvent)](capi-oh-input-manager-h.md#oh_input_gettoucheventglobaly) | - | 获取触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。 |
| [Input\_Result OH\_Input\_SetAxisEventGlobalX(struct Input\_AxisEvent\* axisEvent, int32\_t globalX)](capi-oh-input-manager-h.md#oh_input_setaxiseventglobalx) | - | 设置轴事件以主屏左上角为原点的全局坐标系的X坐标。 |
| [Input\_Result OH\_Input\_GetAxisEventGlobalX(const Input\_AxisEvent\* axisEvent, int32\_t\* globalX)](capi-oh-input-manager-h.md#oh_input_getaxiseventglobalx) | - | 获取轴事件以主屏左上角为原点的全局坐标系的X坐标。 |
| [Input\_Result OH\_Input\_SetAxisEventGlobalY(struct Input\_AxisEvent\* axisEvent, int32\_t globalY)](capi-oh-input-manager-h.md#oh_input_setaxiseventglobaly) | - | 设置轴事件以主屏左上角为原点的全局坐标系的Y坐标。 |
| [Input\_Result OH\_Input\_GetAxisEventGlobalY(const Input\_AxisEvent\* axisEvent, int32\_t\* globalY)](capi-oh-input-manager-h.md#oh_input_getaxiseventglobaly) | - | 获取轴事件以主屏左上角为原点的全局坐标系的Y坐标。 |
| [Input\_Result OH\_Input\_GetPointerLocation(int32\_t \*displayId, double \*displayX, double \*displayY)](capi-oh-input-manager-h.md#oh_input_getpointerlocation) | - | 获取鼠标在屏幕上的坐标点。 |
| [Input\_Result OH\_Input\_GetKeyEventId(const struct Input\_KeyEvent\* keyEvent, int32\_t\* eventId)](capi-oh-input-manager-h.md#oh_input_getkeyeventid) | - | 获取按键事件的ID。 |
| [Input\_Result OH\_Input\_AddKeyEventHook(Input\_KeyEventCallback callback)](capi-oh-input-manager-h.md#oh_input_addkeyeventhook) | - | 添加一个按键事件拦截钩子函数。 |
| [Input\_Result OH\_Input\_RemoveKeyEventHook(Input\_KeyEventCallback callback)](capi-oh-input-manager-h.md#oh_input_removekeyeventhook) | - | 移除按键事件拦截钩子函数。 |
| [Input\_Result OH\_Input\_DispatchToNextHandler(int32\_t eventId)](capi-oh-input-manager-h.md#oh_input_dispatchtonexthandler) | - | 重新分发按键事件。 |
| [Input\_Result OH\_Input\_SetPointerVisible(bool visible)](capi-oh-input-manager-h.md#oh_input_setpointervisible) | - | 设置当前窗口的鼠标光标的显示或隐藏状态。 |
| [Input\_Result OH\_Input\_GetPointerStyle(int32\_t windowId, int32\_t \*pointerStyle)](capi-oh-input-manager-h.md#oh_input_getpointerstyle) | - | 获取指定窗口的鼠标光标样式。 |
| [Input\_Result OH\_Input\_SetPointerStyle(int32\_t windowId, int32\_t pointerStyle)](capi-oh-input-manager-h.md#oh_input_setpointerstyle) | - | 设置指定窗口的鼠标光标样式。 |
| [Input\_CustomCursor\* OH\_Input\_CustomCursor\_Create(OH\_PixelmapNative\* pixelMap, int32\_t anchorX, int32\_t anchorY)](capi-oh-input-manager-h.md#oh_input_customcursor_create) | - | 创建自定义鼠标光标资源对象。通过调用[OH\_Input\_CustomCursor\_Destroy](capi-oh-input-manager-h.md#oh_input_customcursor_destroy)销毁自定义鼠标光标资源对象。 |
| [void OH\_Input\_CustomCursor\_Destroy(Input\_CustomCursor\*\* customCursor)](capi-oh-input-manager-h.md#oh_input_customcursor_destroy) | - | 销毁自定义鼠标光标资源对象。 |
| [Input\_Result OH\_Input\_CustomCursor\_GetPixelMap(Input\_CustomCursor\* customCursor, OH\_PixelmapNative\*\* pixelMap)](capi-oh-input-manager-h.md#oh_input_customcursor_getpixelmap) | - | 获取指定自定义鼠标光标资源的自定义鼠标光标像素图。 |
| [Input\_Result OH\_Input\_CustomCursor\_GetAnchor(Input\_CustomCursor\* customCursor, int32\_t\* anchorX, int32\_t\* anchorY)](capi-oh-input-manager-h.md#oh_input_customcursor_getanchor) | - | 获取指定自定义鼠标光标资源的焦点坐标。 |
| [Input\_CursorConfig\* OH\_Input\_CursorConfig\_Create(bool followSystem)](capi-oh-input-manager-h.md#oh_input_cursorconfig_create) | - | 创建自定义鼠标光标配置对象。通过调用[OH\_Input\_CursorConfig\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorconfig_destroy)销毁自定义鼠标光标配置对象。 |
| [void OH\_Input\_CursorConfig\_Destroy(Input\_CursorConfig\*\* cursorConfig)](capi-oh-input-manager-h.md#oh_input_cursorconfig_destroy) | - | 销毁自定义鼠标光标配置对象。 |
| [Input\_Result OH\_Input\_CursorConfig\_IsFollowSystem(Input\_CursorConfig \*cursorConfig, bool \*followSystem)](capi-oh-input-manager-h.md#oh_input_cursorconfig_isfollowsystem) | - | 查询自定义鼠标光标配置是否跟随系统设置调整光标大小。 |
| [Input\_Result OH\_Input\_SetCustomCursor(int32\_t windowId, Input\_CustomCursor\* customCursor, Input\_CursorConfig\* cursorConfig)](capi-oh-input-manager-h.md#oh_input_setcustomcursor) | - | 设置自定义鼠标光标样式。 |
| [struct Input\_CursorInfo\* OH\_Input\_CursorInfo\_Create()](capi-oh-input-manager-h.md#oh_input_cursorinfo_create) | - | 创建鼠标光标信息对象。通过调用[OH\_Input\_CursorInfo\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy)销毁鼠标光标信息对象。 |
| [void OH\_Input\_CursorInfo\_Destroy(Input\_CursorInfo\*\* cursorInfo)](capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy) | - | 销毁鼠标光标信息对象。 |
| [Input\_Result OH\_Input\_CursorInfo\_IsVisible(Input\_CursorInfo\* cursorInfo, bool\* visible)](capi-oh-input-manager-h.md#oh_input_cursorinfo_isvisible) | - | 获取指定鼠标光标信息对象对应的光标显示状态。 |
| [Input\_Result OH\_Input\_CursorInfo\_GetStyle(Input\_CursorInfo\* cursorInfo, Input\_PointerStyle\* style)](capi-oh-input-manager-h.md#oh_input_cursorinfo_getstyle) | - | 获取指定鼠标光标信息对象对应的光标样式。 |
| [Input\_Result OH\_Input\_CursorInfo\_GetSizeLevel(Input\_CursorInfo\* cursorInfo, int32\_t\* sizeLevel)](capi-oh-input-manager-h.md#oh_input_cursorinfo_getsizelevel) | - | 获取指定鼠标光标信息对象对应的光标大小档位。 |
| [Input\_Result OH\_Input\_CursorInfo\_GetColor(Input\_CursorInfo\* cursorInfo, uint32\_t\* color)](capi-oh-input-manager-h.md#oh_input_cursorinfo_getcolor) | - | 获取指定鼠标光标信息对象对应的光标颜色, 使用32位ARGB整数表示。 |
| [Input\_Result OH\_Input\_GetMouseEventCursorInfo(const struct Input\_MouseEvent\* mouseEvent, Input\_CursorInfo\* cursorInfo)](capi-oh-input-manager-h.md#oh_input_getmouseeventcursorinfo) | - | 获取鼠标事件的鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。 |
| [Input\_Result OH\_Input\_GetCursorInfo(Input\_CursorInfo\* cursorInfo, OH\_PixelmapNative\*\* pixelmap)](capi-oh-input-manager-h.md#oh_input_getcursorinfo) | - | 查询当前鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。如果pixelmap参数非空，且光标样式为[DEVELOPER\_DEFINED\_ICON](capi-oh-pointer-style-h.md#input_pointerstyle)，则会同时返回光标的PixelMap位图对象。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Input\_KeyStateAction

PhonePC/2in1TabletTVWearable

```
1. enum Input_KeyStateAction
```

**描述**

按键状态的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| KEY\_DEFAULT = -1 | 默认状态。 |
| KEY\_PRESSED = 0 | 按键按下。 |
| KEY\_RELEASED = 1 | 按键抬起。 |
| KEY\_SWITCH\_ON = 2 | 按键开关使能。 |
| KEY\_SWITCH\_OFF = 3 | 按键开关去使能。 |

### Input\_KeyEventAction

PhonePC/2in1TabletTVWearable

```
1. enum Input_KeyEventAction
```

**描述**

按键事件类型的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| KEY\_ACTION\_CANCEL = 0 | 按键动作取消。 |
| KEY\_ACTION\_DOWN = 1 | 按键按下。 |
| KEY\_ACTION\_UP = 2 | 按键抬起。 |

### Input\_MouseEventAction

PhonePC/2in1TabletTVWearable

```
1. enum Input_MouseEventAction
```

**描述**

鼠标动作的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| MOUSE\_ACTION\_CANCEL = 0 | 取消鼠标动作。 |
| MOUSE\_ACTION\_MOVE = 1 | 移动鼠标。 |
| MOUSE\_ACTION\_BUTTON\_DOWN = 2 | 按下鼠标。 |
| MOUSE\_ACTION\_BUTTON\_UP = 3 | 抬起鼠标按键。 |
| MOUSE\_ACTION\_AXIS\_BEGIN = 4 | 鼠标轴事件开始。 |
| MOUSE\_ACTION\_AXIS\_UPDATE = 5 | 更新鼠标轴事件。 |
| MOUSE\_ACTION\_AXIS\_END = 6 | 鼠标轴事件结束。 |

### InputEvent\_MouseAxis

PhonePC/2in1TabletTVWearable

```
1. enum InputEvent_MouseAxis
```

**描述**

鼠标轴事件类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| MOUSE\_AXIS\_SCROLL\_VERTICAL = 0 | 垂直滚动轴。 |
| MOUSE\_AXIS\_SCROLL\_HORIZONTAL = 1 | 水平滚动轴。 |

### Input\_MouseEventButton

PhonePC/2in1TabletTVWearable

```
1. enum Input_MouseEventButton
```

**描述**

鼠标按键的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| MOUSE\_BUTTON\_NONE = -1 | 无效按键。 |
| MOUSE\_BUTTON\_LEFT = 0 | 鼠标左键。 |
| MOUSE\_BUTTON\_MIDDLE = 1 | 鼠标中间键。 |
| MOUSE\_BUTTON\_RIGHT = 2 | 鼠标右键。 |
| MOUSE\_BUTTON\_FORWARD = 3 | 鼠标前进键。 |
| MOUSE\_BUTTON\_BACK = 4 | 鼠标返回键。 |

### Input\_TouchEventAction

PhonePC/2in1TabletTVWearable

```
1. enum Input_TouchEventAction
```

**描述**

触屏动作的枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| TOUCH\_ACTION\_CANCEL = 0 | 触屏取消。 |
| TOUCH\_ACTION\_DOWN = 1 | 触屏按下。 |
| TOUCH\_ACTION\_MOVE = 2 | 触屏移动。 |
| TOUCH\_ACTION\_UP = 3 | 触屏抬起。 |

### Input\_InjectionStatus

PhonePC/2in1TabletTVWearable

```
1. enum Input_InjectionStatus
```

**描述**

注入权限状态枚举值。

**起始版本：** 20

| 枚举项 | 描述 |
| --- | --- |
| UNAUTHORIZED = 0 | 未授权。 |
| AUTHORIZING = 1 | 授权中。 |
| AUTHORIZED = 2 | 已授权。 |

### InputEvent\_SourceType

PhonePC/2in1TabletTVWearable

```
1. enum InputEvent_SourceType
```

**描述**

输入事件源类型。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| SOURCE\_TYPE\_MOUSE = 1 | 表示输入源生成鼠标光标移动、按键按下和释放以及滚轮滚动的事件。 |
| SOURCE\_TYPE\_TOUCHSCREEN = 2 | 表示输入源产生触摸屏多点触屏输入事件。 |
| SOURCE\_TYPE\_TOUCHPAD = 3 | 表示输入源产生触控板多点触屏输入事件。 |

### Input\_KeyboardType

PhonePC/2in1TabletTVWearable

```
1. enum Input_KeyboardType
```

**描述**

输入设备的键盘类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| KEYBOARD\_TYPE\_NONE = 0 | 表示无按键设备。 |
| KEYBOARD\_TYPE\_UNKNOWN = 1 | 表示未知按键设备。 |
| KEYBOARD\_TYPE\_ALPHABETIC = 2 | 表示全键盘设备。 |
| KEYBOARD\_TYPE\_DIGITAL = 3 | 表示数字键盘设备。 |
| KEYBOARD\_TYPE\_STYLUS = 4 | 表示手写笔设备。 |
| KEYBOARD\_TYPE\_REMOTE\_CONTROL = 5 | 表示遥控器设备。 |

### Input\_Result

PhonePC/2in1TabletTVWearable

```
1. enum Input_Result
```

**描述**

返回值枚举值。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| INPUT\_SUCCESS = 0 | 操作成功。 |
| INPUT\_PERMISSION\_DENIED = 201 | 权限验证失败。 |
| INPUT\_NOT\_SYSTEM\_APPLICATION = 202 | 非系统应用。 |
| INPUT\_PARAMETER\_ERROR = 401 | 参数检查失败。 |
| INPUT\_DEVICE\_NOT\_SUPPORTED = 801 | 表示不支持该功能。 |
| INPUT\_SERVICE\_EXCEPTION = 3800001 | 服务异常。 |
| INPUT\_REPEAT\_INTERCEPTOR = 4200001 | 应用创建拦截后，再次执行创建拦截的操作。 |
| INPUT\_OCCUPIED\_BY\_SYSTEM = 4200002 | 已经被系统应用占用。  **起始版本：** 14。 |
| INPUT\_OCCUPIED\_BY\_OTHER = 4200003 | 已经被其他应用占用。  **起始版本：** 14。 |
| INPUT\_KEYBOARD\_DEVICE\_NOT\_EXIST = 3900002 | 未连接键盘设备。  **起始版本：** 15。 |
| INPUT\_INJECTION\_AUTHORIZING = 3900005 | 正在授权中。  **起始版本：** 20。 |
| INPUT\_INJECTION\_OPERATION\_FREQUENT = 3900006 | 重复请求。  **起始版本：** 20。 |
| INPUT\_INJECTION\_AUTHORIZED = 3900007 | 当前应用已经授权。  **起始版本：** 20。 |
| INPUT\_INJECTION\_AUTHORIZED\_OTHERS = 3900008 | 其它应用已经授权。  **起始版本：** 20。 |
| INPUT\_APP\_NOT\_FOCUSED = 3900009 | 当前应用不是焦点应用。  **起始版本：** 20。 |
| INPUT\_DEVICE\_NO\_POINTER = 3900010 | 无鼠标类输入外设。  **起始版本：** 20。 |
| INPUT\_INVALID\_WINDOWID = 26500001 | 无效的窗口ID。  **起始版本：** 22。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### Input\_HotkeyCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_HotkeyCallback)(Input_Hotkey* hotkey)
```

**描述**

回调函数，用于回调快捷键事件。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | hotkey 快捷键对象的实例。 |

### Input\_KeyEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_KeyEventCallback)(const Input_KeyEvent* keyEvent)
```

**描述**

按键事件的回调函数，keyEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

### Input\_MouseEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_MouseEventCallback)(const Input_MouseEvent* mouseEvent)
```

**描述**

鼠标事件的回调函数，mouseEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

### Input\_TouchEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_TouchEventCallback)(const Input_TouchEvent* touchEvent)
```

**描述**

触屏输入事件的回调函数，touchEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

### Input\_AxisEventCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_AxisEventCallback)(const Input_AxisEvent* axisEvent)
```

**描述**

轴事件的回调函数，axisEvent的生命周期为回调函数内。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |

### Input\_DeviceAddedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_DeviceAddedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热插事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

### Input\_DeviceRemovedCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_DeviceRemovedCallback)(int32_t deviceId)
```

**描述**

回调函数，用于回调输入设备的热拔事件。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |

### Input\_InjectAuthorizeCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Input_InjectAuthorizeCallback)(Input_InjectionStatus authorizedStatus)
```

**描述**

回调函数，用于获取注入权限状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_InjectionStatus](capi-oh-input-manager-h.md#input_injectionstatus) authorizedStatus | 注入权限状态。 |

### OH\_Input\_GetKeyState()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetKeyState(struct Input_KeyState* keyState)
```

**描述**

查询按键状态的枚举对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 如果操作成功，@return返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；  否则返回[Input\_Result](capi-oh-input-manager-h.md#input_result)中定义的其他错误代码。 |

### OH\_Input\_CreateKeyState()

PhonePC/2in1TabletTVWearable

```
1. struct Input_KeyState* OH_Input_CreateKeyState()
```

**描述**

创建按键状态的枚举对象。通过调用[OH\_Input\_DestroyKeyState](capi-oh-input-manager-h.md#oh_input_destroykeystate)销毁按键状态的枚举对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| struct | 如果操作成功，@return返回一个[Input\_KeyState](capi-input-input-keystate.md)指针对象；否则返回空指针。 |

### OH\_Input\_DestroyKeyState()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyKeyState(struct Input_KeyState** keyState)
```

**描述**

销毁按键状态的枚举对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyState](capi-input-input-keystate.md)\*\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

### OH\_Input\_SetKeyCode()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyCode(struct Input_KeyState* keyState, int32_t keyCode)
```

**描述**

设置按键状态对象的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |
| int32\_t keyCode | 按键键值。 |

### OH\_Input\_GetKeyCode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeyCode(const struct Input_KeyState* keyState)
```

**描述**

获取按键状态对象的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回按键状态对象的键值。相关取值可参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

### OH\_Input\_SetKeyPressed()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyPressed(struct Input_KeyState* keyState, int32_t keyAction)
```

**描述**

设置按键状态对象的按键是否按下。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |
| int32\_t keyAction | 按键是否按下，具体请参考[Input\_KeyEventAction](capi-oh-input-manager-h.md#input_keyeventaction)。 |

### OH\_Input\_GetKeyPressed()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeyPressed(const struct Input_KeyState* keyState)
```

**描述**

获取按键状态对象的按键是否按下。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回按键状态对象的按键按下状态。相关取值可参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

### OH\_Input\_SetKeySwitch()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeySwitch(struct Input_KeyState* keyState, int32_t keySwitch)
```

**描述**

设置按键状态对象的按键开关。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |
| int32\_t keySwitch | 按键开关。 |

### OH\_Input\_GetKeySwitch()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeySwitch(const struct Input_KeyState* keyState)
```

**描述**

获取按键状态对象的按键开关。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyState](capi-input-input-keystate.md)\* keyState | 按键状态的枚举对象，具体请参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回按键状态对象的按键开关。相关取值可参考[Input\_KeyStateAction](capi-oh-input-manager-h.md#input_keystateaction)。 |

### OH\_Input\_InjectKeyEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_InjectKeyEvent(const struct Input_KeyEvent* keyEvent)
```

**描述**

注入按键事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

从API version 20开始，建议先使用[OH\_Input\_RequestInjection](capi-oh-input-manager-h.md#oh_input_requestinjection)请求授权。然后通过[OH\_Input\_QueryAuthorizedStatus](capi-oh-input-manager-h.md#oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](capi-oh-input-manager-h.md#input_injectionstatus)时，再使用该接口。

从API version 22开始，如果注入了修饰键（KEYCODE\_META\_LEFT、KEYCODE\_META\_RIGHT、KEYCODE\_CTRL\_LEFT、KEYCODE\_CTRL\_RIGHT、KEYCODE\_ALT\_LEFT、KEYCODE\_ALT\_RIGHT、KEYCODE\_SHIFT\_LEFT、KEYCODE\_SHIFT\_RIGHT、KEYCODE\_CAPS\_LOCK、KEYCODE\_SCROLL\_LOCK、KEYCODE\_NUM\_LOCK）的按压事件（KEY\_ACTION\_DOWN）时，请及时注入该按键的抬起事件（KEY\_ACTION\_UP），以避免该按键长时间处于按压状态。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。并通过[OH\_Input\_SetKeyEventKeyCode](capi-oh-input-manager-h.md#oh_input_setkeyeventkeycode)、[OH\_Input\_SetKeyEventAction](capi-oh-input-manager-h.md#oh_input_setkeyeventaction)接口可以设置按键事件的键值和按键事件的类型。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | OH\_Input\_InjectKeyEvent 函数返回值。  若注入成功，返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；  若缺少权限，返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若参数错误，返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_CreateKeyEvent()

PhonePC/2in1TabletTVWearable

```
1. struct Input_KeyEvent* OH_Input_CreateKeyEvent()
```

**描述**

创建按键事件对象。通过调用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)销毁按键事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| struct | 如果操作成功返回一个[Input\_KeyEvent](capi-input-input-keyevent.md)指针对象，否则返回空指针。 |

### OH\_Input\_DestroyKeyEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyKeyEvent(struct Input_KeyEvent** keyEvent)
```

**描述**

销毁按键事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyEvent](capi-input-input-keyevent.md)\*\* keyEvent | 按键事件对象。 |

### OH\_Input\_SetKeyEventAction()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyEventAction(struct Input_KeyEvent* keyEvent, int32_t action)
```

**描述**

设置按键事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |
| int32\_t action | 按键事件类型。相关取值可参考[Input\_KeyEventAction](capi-oh-input-manager-h.md#input_keyeventaction)。 |

### OH\_Input\_GetKeyEventAction()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeyEventAction(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回按键事件类型。相关取值可参考[Input\_KeyEventAction](capi-oh-input-manager-h.md#input_keyeventaction)。 |

### OH\_Input\_SetKeyEventKeyCode()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyEventKeyCode(struct Input_KeyEvent* keyEvent, int32_t keyCode)
```

**描述**

设置按键事件的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |
| int32\_t keyCode | 按键的键值。 |

### OH\_Input\_GetKeyEventKeyCode()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeyEventKeyCode(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件的键值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回按键事件的键值。相关取值可参考[Input\_KeyCode](capi-oh-key-code-h.md#input_keycode)。 |

### OH\_Input\_SetKeyEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyEventActionTime(struct Input_KeyEvent* keyEvent, int64_t actionTime)
```

**描述**

设置按键事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |
| int64\_t actionTime | 按键事件发生的时间，表示系统启动运行至今逝去的微秒数。 |

### OH\_Input\_GetKeyEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_Input_GetKeyEventActionTime(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回按键事件发生的时间。 |

### OH\_Input\_SetKeyEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyEventWindowId(struct Input_KeyEvent* keyEvent, int32_t windowId)
```

**描述**

设置按键事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |
| int32\_t windowId | 按键事件对应的窗口ID。 |

### OH\_Input\_GetKeyEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeyEventWindowId(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 按键事件的窗口ID。 |

### OH\_Input\_GetKeyEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetKeyEventDisplayId(const struct Input_KeyEvent* keyEvent)
```

**描述**

获取按键事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 按键事件的屏幕ID。 |

### OH\_Input\_SetKeyEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetKeyEventDisplayId(struct Input_KeyEvent* keyEvent, int32_t displayId)
```

**描述**

设置按键事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |
| int32\_t displayId | 按键事件对应的屏幕ID。 |

### OH\_Input\_CreateMouseEvent()

PhonePC/2in1TabletTVWearable

```
1. struct Input_MouseEvent* OH_Input_CreateMouseEvent()
```

**描述**

创建鼠标事件对象。通过调用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)销毁鼠标事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| struct | 如果操作成功返回一个[Input\_MouseEvent](capi-input-input-mouseevent.md)指针对象，否则返回空指针。 |

### OH\_Input\_DestroyMouseEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyMouseEvent(struct Input_MouseEvent** mouseEvent)
```

**描述**

销毁鼠标事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\*\* mouseEvent | 鼠标事件对象。 |

### OH\_Input\_SetMouseEventAction()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventAction(struct Input_MouseEvent* mouseEvent, int32_t action)
```

**描述**

设置鼠标事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t action | 鼠标的动作。相关取值可参考[Input\_MouseEventAction](capi-oh-input-manager-h.md#input_mouseeventaction)。 |

### OH\_Input\_GetMouseEventAction()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventAction(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标的动作。相关取值可参考[Input\_MouseEventAction](capi-oh-input-manager-h.md#input_mouseeventaction)。 |

### OH\_Input\_SetMouseEventDisplayX()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventDisplayX(struct Input_MouseEvent* mouseEvent, int32_t displayX)
```

**描述**

设置鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t displayX | 鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |

### OH\_Input\_GetMouseEventDisplayX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventDisplayX(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |

### OH\_Input\_SetMouseEventDisplayY()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventDisplayY(struct Input_MouseEvent* mouseEvent, int32_t displayY)
```

**描述**

设置鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t displayY | 鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |

### OH\_Input\_GetMouseEventDisplayY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventDisplayY(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |

### OH\_Input\_SetMouseEventButton()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventButton(struct Input_MouseEvent* mouseEvent, int32_t button)
```

**描述**

设置鼠标事件的按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t button | 鼠标按键。相关取值可参考[Input\_MouseEventButton](capi-oh-input-manager-h.md#input_mouseeventbutton)。 |

### OH\_Input\_GetMouseEventButton()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventButton(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的按键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标按键。相关取值可参考[Input\_MouseEventButton](capi-oh-input-manager-h.md#input_mouseeventbutton)。 |

### OH\_Input\_SetMouseEventAxisType()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventAxisType(struct Input_MouseEvent* mouseEvent, int32_t axisType)
```

**描述**

设置鼠标轴事件的类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t axisType | 鼠标轴类型，比如垂直轴、水平轴。相关取值可参考[InputEvent\_MouseAxis](capi-oh-input-manager-h.md#inputevent_mouseaxis)。 |

### OH\_Input\_GetMouseEventAxisType()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventAxisType(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标轴事件的类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标轴类型。相关取值可参考[InputEvent\_MouseAxis](capi-oh-input-manager-h.md#inputevent_mouseaxis)。 |

### OH\_Input\_SetMouseEventAxisValue()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventAxisValue(struct Input_MouseEvent* mouseEvent, float axisValue)
```

**描述**

设置鼠标轴事件的值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| float axisValue | 轴事件的值，正数向前滚动（例如，1.0表示向前滚动一个单位），负数向后滚动（例如，-1.0表示向后滚动一个单位）,零表示没有滚动。 |

### OH\_Input\_GetMouseEventAxisValue()

PhonePC/2in1TabletTVWearable

```
1. float OH_Input_GetMouseEventAxisValue(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标轴事件的值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| float | 轴事件的值。 |

### OH\_Input\_SetMouseEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventActionTime(struct Input_MouseEvent* mouseEvent, int64_t actionTime)
```

**描述**

设置鼠标事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int64\_t actionTime | 鼠标事件发生的时间，表示系统启动运行至今逝去的微秒数。 |

### OH\_Input\_GetMouseEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_Input_GetMouseEventActionTime(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回鼠标事件发生的时间。 |

### OH\_Input\_SetMouseEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventWindowId(struct Input_MouseEvent* mouseEvent, int32_t windowId)
```

**描述**

设置鼠标事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t windowId | 鼠标事件的窗口ID。 |

### OH\_Input\_GetMouseEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventWindowId(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标事件的窗口ID。 |

### OH\_Input\_SetMouseEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventDisplayId(struct Input_MouseEvent* mouseEvent, int32_t displayId)
```

**描述**

设置鼠标事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t displayId | 鼠标事件的屏幕ID。 |

### OH\_Input\_CreateTouchEvent()

PhonePC/2in1TabletTVWearable

```
1. struct Input_TouchEvent* OH_Input_CreateTouchEvent()
```

**描述**

创建触屏输入事件对象。通过调用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)销毁触屏输入事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| struct | 如果操作成功返回一个[Input\_TouchEvent](capi-input-input-touchevent.md)指针对象，否则返回空指针。 |

### OH\_Input\_DestroyTouchEvent()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyTouchEvent(struct Input_TouchEvent** touchEvent)
```

**描述**

销毁触屏输入事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\*\* touchEvent | 触屏输入事件对象。 |

### OH\_Input\_SetTouchEventAction()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventAction(struct Input_TouchEvent* touchEvent, int32_t action)
```

**描述**

设置触屏输入事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t action | 触屏的动作。相关取值可参考[Input\_TouchEventAction](capi-oh-input-manager-h.md#input_toucheventaction)。 |

### OH\_Input\_GetTouchEventAction()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventAction(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏的动作。相关取值可参考[Input\_TouchEventAction](capi-oh-input-manager-h.md#input_toucheventaction)。 |

### OH\_Input\_SetTouchEventFingerId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventFingerId(struct Input_TouchEvent* touchEvent, int32_t id)
```

**描述**

设置触屏输入事件的手指ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t id | 触屏的手指ID。第一个手指碰到屏幕，ID就是0，第二个手指碰到屏幕，ID就是1，依次累加。 |

### OH\_Input\_GetTouchEventFingerId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventFingerId(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的手指ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏的手指ID。第一个手指碰到屏幕，ID就是0，第二个手指碰到屏幕，ID就是1，依次累加。 |

### OH\_Input\_SetTouchEventDisplayX()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventDisplayX(struct Input_TouchEvent* touchEvent, int32_t displayX)
```

**描述**

设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t displayX | 触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |

### OH\_Input\_GetTouchEventDisplayX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventDisplayX(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏输入事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |

### OH\_Input\_SetTouchEventDisplayY()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventDisplayY(struct Input_TouchEvent* touchEvent, int32_t displayY)
```

**描述**

设置触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t displayY | 触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |

### OH\_Input\_GetTouchEventDisplayY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventDisplayY(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏输入事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |

### OH\_Input\_SetTouchEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventActionTime(struct Input_TouchEvent* touchEvent, int64_t actionTime)
```

**描述**

设置触屏输入事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int64\_t actionTime | 触屏输入事件发生的时间，表示系统启动运行至今逝去的微秒数。 |

### OH\_Input\_GetTouchEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. int64_t OH_Input_GetTouchEventActionTime(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int64\_t | 返回触屏输入事件发生的时间。 |

### OH\_Input\_SetTouchEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventWindowId(struct Input_TouchEvent* touchEvent, int32_t windowId)
```

**描述**

设置触屏输入事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t windowId | 触屏输入事件的窗口ID。 |

### OH\_Input\_GetTouchEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventWindowId(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏输入事件的窗口ID。 |

### OH\_Input\_SetTouchEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventDisplayId(struct Input_TouchEvent* touchEvent, int32_t displayId)
```

**描述**

设置触屏输入事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t displayId | 触屏输入事件的屏幕ID。 |

### OH\_Input\_GetTouchEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventDisplayId(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏输入事件的屏幕ID。 |

### OH\_Input\_CancelInjection()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_CancelInjection()
```

**描述**

取消事件注入并撤销授权。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

### OH\_Input\_RequestInjection()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RequestInjection(Input_InjectAuthorizeCallback callback)
```

**描述**

当前应用申请注入权限，包括申请注入按键事件[OH\_Input\_InjectKeyEvent](capi-oh-input-manager-h.md#oh_input_injectkeyevent)、注入触屏输入事件[OH\_Input\_InjectTouchEvent](capi-oh-input-manager-h.md#oh_input_injecttouchevent)、注入鼠标事件[OH\_Input\_InjectMouseEvent](capi-oh-input-manager-h.md#oh_input_injectmouseevent)等注入操作的权限。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**设备行为差异**：该接口仅在PC/2in1设备上生效，在其他设备上返回801错误码。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_InjectAuthorizeCallback](capi-oh-input-manager-h.md#input_injectauthorizecallback) callback | 授权状态回调，具体请参考[Input\_InjectAuthorizeCallback](capi-oh-input-manager-h.md#input_injectauthorizecallback)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 函数返回值，参见[Input\_Result](capi-oh-input-manager-h.md#input_result)。  INPUT\_SUCCESS = 0 申请授权成功，等待用户授权结果并回调授权状态。  INPUT\_PARAMETER\_ERROR = 401 参数错误，参数callback为空。  INPUT\_DEVICE\_NOT\_SUPPORTED = 801 表示不支持该功能。  INPUT\_SERVICE\_EXCEPTION = 3800001 服务异常。  INPUT\_INJECTION\_AUTHORIZING = 3900005 正在授权中。  INPUT\_INJECTION\_OPERATION\_FREQUENT = 3900006 重复请求（当前应用连续申请授权弹窗成功，间隔时间不超过3秒）。  INPUT\_INJECTION\_AUTHORIZED = 3900007 当前应用已经授权。  INPUT\_INJECTION\_AUTHORIZED\_OTHERS = 3900008 其它应用已经授权。 |

### OH\_Input\_QueryAuthorizedStatus()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_QueryAuthorizedStatus(Input_InjectionStatus* status)
```

**描述**

查询当前应用注入的权限状态。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_InjectionStatus](capi-oh-input-manager-h.md#input_injectionstatus)\* status | 当前应用注入权限状态。参见[Input\_InjectionStatus](capi-oh-input-manager-h.md#input_injectionstatus)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 函数返回值，参见[Input\_Result](capi-oh-input-manager-h.md#input_result)。  INPUT\_SUCCESS = 0 查询成功。  INPUT\_PARAMETER\_ERROR = 401 参数错误，参数status为空。  INPUT\_SERVICE\_EXCEPTION = 3800001 服务异常。 |

### OH\_Input\_CreateAxisEvent()

PhonePC/2in1TabletTVWearable

```
1. Input_AxisEvent* OH_Input_CreateAxisEvent(void)
```

**描述**

创建轴事件对象。通过调用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)销毁轴事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| Input\_AxisEvent\* | 成功返回[Input\_AxisEvent](capi-input-input-axisevent.md)对象实例，失败则返回null。 |

### OH\_Input\_DestroyAxisEvent()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_DestroyAxisEvent(Input_AxisEvent** axisEvent)
```

**描述**

销毁轴事件对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\*\* axisEvent | 轴事件对象实例的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若销毁成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL或者axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventAction()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventAction(Input_AxisEvent* axisEvent, InputEvent_AxisAction action)
```

**描述**

设置轴事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_AxisAction](capi-oh-axis-type-h.md#inputevent_axisaction) action | 轴事件动作，具体请参考[InputEvent\_AxisAction](capi-oh-axis-type-h.md#inputevent_axisaction)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件的动作成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventAction()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventAction(const Input_AxisEvent* axisEvent, InputEvent_AxisAction *action)
```

**描述**

获取轴事件的动作。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_AxisAction](capi-oh-axis-type-h.md#inputevent_axisaction) \*action | action 出参，返回轴事件动作，具体请参考在[InputEvent\_AxisAction](capi-oh-axis-type-h.md#inputevent_axisaction)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件的动作成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者action为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventDisplayX()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventDisplayX(Input_AxisEvent* axisEvent, float displayX)
```

**描述**

设置轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| float displayX | 轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件的X坐标成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventDisplayX()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventDisplayX(const Input_AxisEvent* axisEvent, float* displayX)
```

**描述**

获取轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| float\* displayX | 出参，返回轴事件以指定屏幕左上角为原点的相对坐标系的X坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件的X坐标成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者displayX为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventDisplayY()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventDisplayY(Input_AxisEvent* axisEvent, float displayY)
```

**描述**

设置轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| float displayY | 轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件的Y坐标成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventDisplayY()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventDisplayY(const Input_AxisEvent* axisEvent, float* displayY)
```

**描述**

获取轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| float\* displayY | 出参，返回轴事件以指定屏幕左上角为原点的相对坐标系的Y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件的Y坐标成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者displayY为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventAxisValue()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventAxisValue(Input_AxisEvent* axisEvent,InputEvent_AxisType axisType, double axisValue)
```

**描述**

设置轴事件指定轴类型的轴值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_AxisType](capi-oh-axis-type-h.md#inputevent_axistype) axisType | 轴类型，具体请参考[InputEvent\_AxisType](capi-oh-axis-type-h.md#inputevent_axistype)。 |
| double axisValue | 轴事件的值，正数向前滚动（例如，1.0表示向前滚动一个单位），负数向后滚动（例如，-1.0表示向后滚动一个单位）,零表示没有滚动。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件指定轴类型的轴值成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventAxisValue()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventAxisValue(const Input_AxisEvent* axisEvent,InputEvent_AxisType axisType, double* axisValue)
```

**描述**

获取轴事件指定轴类型的轴值。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_AxisType](capi-oh-axis-type-h.md#inputevent_axistype) axisType | 轴类型，具体请参考[InputEvent\_AxisType](capi-oh-axis-type-h.md#inputevent_axistype)。 |
| double\* axisValue | 出参，返回轴事件的值，正数向前滚动（例如，1.0表示向前滚动一个单位），负数向后滚动（例如，-1.0表示向后滚动一个单位）,零表示没有滚动。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件指定轴类型的轴值成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者axisValue为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventActionTime(Input_AxisEvent* axisEvent, int64_t actionTime)
```

**描述**

设置轴事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int64\_t actionTime | 轴事件发生的时间，表示系统启动运行至今逝去的微秒数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件发生的时间成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventActionTime()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventActionTime(const Input_AxisEvent* axisEvent, int64_t* actionTime)
```

**描述**

获取轴事件发生的时间。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int64\_t\* actionTime | 出参，返回轴事件发生的时间，表示系统启动运行至今逝去的微秒数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件发生的时间成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者actionTime为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventType()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventType(Input_AxisEvent* axisEvent, InputEvent_AxisEventType axisEventType)
```

**描述**

设置轴事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype) axisEventType | 轴事件类型，具体请参考[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件类型成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventType()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventType(const Input_AxisEvent* axisEvent, InputEvent_AxisEventType* axisEventType)
```

**描述**

获取轴事件类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)\* axisEventType | 出参，返回轴事件类型，具体请参考[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件类型成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者axisEventType为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventSourceType()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventSourceType(Input_AxisEvent* axisEvent, InputEvent_SourceType sourceType)
```

**描述**

设置轴事件源类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_SourceType](capi-oh-input-manager-h.md#inputevent_sourcetype) sourceType | 轴事件源类型,具体请参考[InputEvent\_SourceType](capi-oh-input-manager-h.md#inputevent_sourcetype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件源类型成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventSourceType()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventSourceType(const Input_AxisEvent* axisEvent, InputEvent_SourceType* sourceType)
```

**描述**

获取轴事件源类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| [InputEvent\_SourceType](capi-oh-input-manager-h.md#inputevent_sourcetype)\* sourceType | 出参，返回轴事件源类型，具体请参考[InputEvent\_SourceType](capi-oh-input-manager-h.md#inputevent_sourcetype)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件源类型成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者sourceType为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventWindowId(Input_AxisEvent* axisEvent, int32_t windowId)
```

**描述**

设置轴事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t windowId | 轴事件窗口ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件的窗口ID成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventWindowId()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventWindowId(const Input_AxisEvent* axisEvent, int32_t* windowId)
```

**描述**

获取轴事件的窗口ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t\* windowId | 出参，返回轴事件窗口ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件的窗口ID成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者windowId为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetAxisEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventDisplayId(Input_AxisEvent* axisEvent, int32_t displayId)
```

**描述**

设置轴事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t displayId | 轴事件屏幕ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若设置轴事件的屏幕ID成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetAxisEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventDisplayId(const Input_AxisEvent* axisEvent, int32_t* displayId)
```

**描述**

获取轴事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t\* displayId | 出参，返回轴事件屏幕ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若获取轴事件的屏幕ID成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若axisEvent或者displayId为NULL，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddKeyEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddKeyEventMonitor(Input_KeyEventCallback callback)
```

**描述**

添加按键事件监听。重复添加只有第一次生效，后续添加请求将被忽略。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEventCallback](capi-oh-input-manager-h.md#input_keyeventcallback) callback | 回调函数，用于接收按键事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加按键事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddMouseEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddMouseEventMonitor(Input_MouseEventCallback callback)
```

**描述**

添加鼠标事件监听，包含鼠标点击，移动，不包含滚轮事件，滚轮事件归属于轴事件。

该接口处于录屏场景时才允许调用，否则调用该接口不生效。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_MouseEventCallback](capi-oh-input-manager-h.md#input_mouseeventcallback) callback | 回调函数，用于接收鼠标事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加鼠标事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddTouchEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddTouchEventMonitor(Input_TouchEventCallback callback)
```

**描述**

添加触屏输入事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_TouchEventCallback](capi-oh-input-manager-h.md#input_toucheventcallback) callback | 回调函数，用于接收触屏输入事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加触屏输入事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddAxisEventMonitorForAll()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddAxisEventMonitorForAll(Input_AxisEventCallback callback)
```

**描述**

添加所有类型轴事件监听，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEventCallback](capi-oh-input-manager-h.md#input_axiseventcallback) callback | 回调函数，用于接收轴事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加轴事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddAxisEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddAxisEventMonitor(InputEvent_AxisEventType axisEventType, Input_AxisEventCallback callback)
```

**描述**

添加指定类型的轴事件监听，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype) axisEventType | 要监听的轴事件类型，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。 |
| [Input\_AxisEventCallback](capi-oh-input-manager-h.md#input_axiseventcallback) callback | 回调函数，用于接收指定类型的轴事件 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加轴事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveKeyEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveKeyEventMonitor(Input_KeyEventCallback callback)
```

**描述**

移除按键事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEventCallback](capi-oh-input-manager-h.md#input_keyeventcallback) callback | 指定要被移除的用于按键事件监听的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除按键事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空或者没有被添加监听，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveMouseEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveMouseEventMonitor(Input_MouseEventCallback callback)
```

**描述**

移除鼠标事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_MouseEventCallback](capi-oh-input-manager-h.md#input_mouseeventcallback) callback | 指定要被移除的用于鼠标事件监听的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除鼠标事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空或者没有被添加监听，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveTouchEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveTouchEventMonitor(Input_TouchEventCallback callback)
```

**描述**

移除触屏输入事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_TouchEventCallback](capi-oh-input-manager-h.md#input_toucheventcallback) callback | 指定要被移除的用于触屏输入事件监听的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除触屏输入事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空或者没有被添加监听，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveAxisEventMonitorForAll()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveAxisEventMonitorForAll(Input_AxisEventCallback callback)
```

**描述**

移除所有类型轴事件监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_AxisEventCallback](capi-oh-input-manager-h.md#input_axiseventcallback) callback | 指定要被移除的用于所有类型轴事件监听的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除轴事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空或者没有被添加监听，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveAxisEventMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveAxisEventMonitor(InputEvent_AxisEventType axisEventType, Input_AxisEventCallback callback)
```

**描述**

移除指定类型轴事件监听，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INPUT\_MONITORING

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype) axisEventType | 指定要移除监听的轴事件类型，轴事件类型定义在[InputEvent\_AxisEventType](capi-oh-axis-type-h.md#inputevent_axiseventtype)中。 |
| [Input\_AxisEventCallback](capi-oh-input-manager-h.md#input_axiseventcallback) callback | 指定要被移除的用于指定类型轴事件监听的回调函数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除轴事件监听成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空或者没有被添加监听，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddKeyEventInterceptor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddKeyEventInterceptor(Input_KeyEventCallback callback, Input_InterceptorOptions *option)
```

**描述**

添加按键事件的拦截，重复添加只有第一次生效，后续添加请求返回错误码[INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result)。仅在应用获焦时拦截按键事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT\_INPUT\_EVENT

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEventCallback](capi-oh-input-manager-h.md#input_keyeventcallback) callback | 回调函数，用于接收按键事件。 |
| [Input\_InterceptorOptions](capi-input-input-interceptoroptions.md) \*option | option 输入事件拦截的可选项，传null则使用默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加按键事件的拦截成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若重复添加拦截器，则返回[INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result)；  若服务异常；则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddInputEventInterceptor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddInputEventInterceptor(Input_InterceptorEventCallback *callback,Input_InterceptorOptions *option)
```

**描述**

添加输入事件拦截，包括鼠标、触屏和轴事件。重复添加只有第一次生效，后续添加请求返回错误码[INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result)。仅命中应用窗口时拦截输入事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT\_INPUT\_EVENT

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_InterceptorEventCallback](capi-input-input-interceptoreventcallback.md) \*callback | callback 用于回调输入事件的结构体指针，请参考定义[Input\_InterceptorEventCallback](capi-input-input-interceptoreventcallback.md)。 |
| [Input\_InterceptorOptions](capi-input-input-interceptoroptions.md) \*option | option 输入事件拦截的可选项，传null则使用默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若添加输入事件的拦截成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若callback为空，则返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)；若重复添加拦截器，则返回[INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result)；  若服务异常；则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveKeyEventInterceptor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveKeyEventInterceptor(void)
```

**描述**

移除按键事件拦截。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT\_INPUT\_EVENT

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除按键事件拦截成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_RemoveInputEventInterceptor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveInputEventInterceptor(void)
```

**描述**

移除输入事件拦截，包括鼠标、触屏和轴事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**需要权限：** ohos.permission.INTERCEPT\_INPUT\_EVENT

该权限为受限权限，申请方式请参考[申请受限权限](../harmonyos-guides/declare-permissions-in-acl.md)

**起始版本：** 12

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | 若移除输入事件拦截成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若权限校验失败，则返回[INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result)；  若服务异常，则返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_GetIntervalSinceLastInput()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetIntervalSinceLastInput(int64_t *timeInterval)
```

**描述**

获取距离上次系统输入事件的时间间隔。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t \*timeInterval | timeInterval 时间间隔，单位：μs。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetIntervalSinceLastInput 函数返回值。  若获取时间间隔成功，则返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若服务异常，返回[INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result)；若参数错误，返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_CreateHotkey()

PhonePC/2in1TabletTVWearable

```
1. Input_Hotkey *OH_Input_CreateHotkey(void)
```

**描述**

创建快捷键对象。通过调用[OH\_Input\_DestroyHotkey](capi-oh-input-manager-h.md#oh_input_destroyhotkey)销毁快捷键对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md) | 如果操作成功,则返回一个[Input\_Hotkey](capi-input-input-hotkey.md)指针对象。否则, 返回一个空指针， 可能的原因是内存分配失败。 |

### OH\_Input\_DestroyHotkey()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyHotkey(Input_Hotkey **hotkey)
```

**描述**

销毁快捷键对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md) \*\*hotkey | hotkey 快捷键对象的实例。 |

### OH\_Input\_SetPreKeys()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetPreKeys(Input_Hotkey *hotkey, int32_t *preKeys, int32_t size)
```

**描述**

设置修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md) \*hotkey | hotkey 快捷键对象的实例。 |
| int32\_t \*preKeys | preKeys 修饰键列表。 |
| int32\_t size | 修饰键个数， 取值范围1~2个。 |

### OH\_Input\_GetPreKeys()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetPreKeys(const Input_Hotkey *hotkey, int32_t **preKeys, int32_t *preKeyCount)
```

**描述**

获取修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_Hotkey](capi-input-input-hotkey.md) \*hotkey | hotkey 快捷键对象的实例。 |
| int32\_t \*\*preKeys | preKeys 返回修饰键列表。 |
| int32\_t \*preKeyCount | preKeyCount 返回修饰键个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetPreKeys 函数返回值。  若获取成功，返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；若获取失败，返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetFinalKey()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetFinalKey(Input_Hotkey* hotkey, int32_t finalKey)
```

**描述**

设置被修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | 快捷键对象的实例。 |
| int32\_t finalKey | 被修饰键值，被修饰键值只能是1个。 |

### OH\_Input\_GetFinalKey()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetFinalKey(const Input_Hotkey* hotkey, int32_t *finalKeyCode)
```

**描述**

获取被修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | 快捷键对象的实例。 |
| int32\_t \*finalKeyCode | finalKeyCode 返回被修饰键键值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetFinalKey 函数返回值。  若获取成功，返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；  若获取失败，返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_CreateAllSystemHotkeys()

PhonePC/2in1TabletTVWearable

```
1. Input_Hotkey **OH_Input_CreateAllSystemHotkeys(int32_t count)
```

**描述**

创建[Input\_Hotkey](capi-input-input-hotkey.md)类型实例的数组。通过调用[OH\_Input\_DestroyAllSystemHotkeys](capi-oh-input-manager-h.md#oh_input_destroyallsystemhotkeys)销毁[Input\_Hotkey](capi-input-input-hotkey.md)实例数组并回收内存。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**设备行为差异**：该接口在Wearable设备上调用无效果，在其他设备上可正常调用。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t count | 创建[Input\_Hotkey](capi-input-input-hotkey.md)实例的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md) | OH\_Input\_CreateAllSystemHotkeys 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 创建实例数组的双指针成功。 |

### OH\_Input\_DestroyAllSystemHotkeys()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyAllSystemHotkeys(Input_Hotkey **hotkeys, int32_t count)
```

**描述**

销毁[Input\_Hotkey](capi-input-input-hotkey.md)实例数组并回收内存。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md) \*\*hotkeys | hotkeys 指向[Input\_Hotkey](capi-input-input-hotkey.md)实例数组的双指针。 |
| int32\_t count | 销毁[Input\_Hotkey](capi-input-input-hotkey.md)实例的数量。 |

### OH\_Input\_GetAllSystemHotkeys()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAllSystemHotkeys(Input_Hotkey **hotkey, int32_t *count)
```

**描述**

获取设置的所有快捷键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**设备行为差异**：该接口在Wearable设备上调用无效果，在其他设备上可正常调用。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md) \*\*hotkey | hotkey 返回[Input\_Hotkey](capi-input-input-hotkey.md) 类型实例数组。首次调用可传入NULL，可获取数组长度。 |
| int32\_t \*count | count 返回支持快捷键的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetAllSystemHotkeys 函数返回值。  若获取成功，返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；  若获取失败，返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_SetRepeat()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetRepeat(Input_Hotkey* hotkey, bool isRepeat)
```

**描述**

设置是否上报重复key事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | 快捷键对象的实例。 |
| bool isRepeat | 是否上报重复key事件。true表示上报，false表示不上报。 |

### OH\_Input\_GetRepeat()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetRepeat(const Input_Hotkey* hotkey, bool *isRepeat)
```

**描述**

获取是否上报重复key事件。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | 快捷键对象的实例。 |
| bool \*isRepeat | isRepeat 返回Key事件是否重复。true表示重复，false表示不重复。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetRepeat 函数返回值。  若获取成功，返回[INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result)；  若获取失败，返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。 |

### OH\_Input\_AddHotkeyMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddHotkeyMonitor(const Input_Hotkey* hotkey, Input_HotkeyCallback callback)
```

**描述**

订阅快捷键事件。

说明

订阅快捷键事件时，对于preKeys和finalKey有以下约束：

1. preKeys：修饰键（包括 Ctrl、Shift 和 Alt）集合，数量范围[1, 4]，无顺序要求。例如，Ctrl+Shift+Esc中，Ctrl+Shift称为修饰键。
2. finalKey：被修饰键，除修饰键和Meta键以外的按键，详细按键介绍请参见[按键设备的键值](capi-oh-key-code-h.md)。例如，Ctrl+Shift+Esc中，Esc称为被修饰键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**设备行为差异**：该接口在Wearable设备上返回801错误码，在其他设备上可正常调用。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | 指定要订阅的快捷键对象。 |
| [Input\_HotkeyCallback](capi-oh-input-manager-h.md#input_hotkeycallback) callback | 回调函数，用于回调快捷键事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_AddHotkeyMonitor 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示订阅组合按键成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 参数检查失败。  [INPUT\_OCCUPIED\_BY\_SYSTEM](capi-oh-input-manager-h.md#input_result) 该快捷键已被系统占用，可以通过接口[OH\_Input\_GetAllSystemHotkeys](capi-oh-input-manager-h.md#oh_input_getallsystemhotkeys)查询所有的系统快捷键。  [INPUT\_OCCUPIED\_BY\_OTHER](capi-oh-input-manager-h.md#input_result) 已被抢占订阅。  [INPUT\_DEVICE\_NOT\_SUPPORTED](capi-oh-input-manager-h.md#input_result) 表示不支持该功能。 |

### OH\_Input\_RemoveHotkeyMonitor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveHotkeyMonitor(const Input_Hotkey* hotkey, Input_HotkeyCallback callback)
```

**描述**

取消订阅快捷键。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_Hotkey](capi-input-input-hotkey.md)\* hotkey | 指定要取消订阅的快捷键对象。 |
| [Input\_HotkeyCallback](capi-oh-input-manager-h.md#input_hotkeycallback) callback | 回调函数，用于回调快捷键事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_RemoveHotkeyMonitor 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 取消订阅组合按键成功， [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 参数检查失败。 |

### OH\_Input\_RegisterDeviceListener()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RegisterDeviceListener(Input_DeviceListener* listener)
```

**描述**

注册设备热插拔的监听器。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceListener](capi-input-input-devicelistener.md)\* listener | 指向设备热插拔监听器[Input\_DeviceListener](capi-input-input-devicelistener.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_RegisterDeviceListener 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示注册成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示listener 为NULL。 |

### OH\_Input\_UnregisterDeviceListener()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_UnregisterDeviceListener(Input_DeviceListener* listener)
```

**描述**

取消注册设备热插拔的监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceListener](capi-input-input-devicelistener.md)\* listener | 指向设备热插拔监听器[Input\_DeviceListener](capi-input-input-devicelistener.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_UnregisterDeviceListener 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示取消注册成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示listener 为 NULL 或者 listener 未被注册。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示由于服务异常调用失败。 |

### OH\_Input\_UnregisterDeviceListeners()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_UnregisterDeviceListeners()
```

**描述**

取消注册所有的设备热插拔的监听。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_UnregisterDeviceListener 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示调用成功。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示由于服务异常调用失败。 |

### OH\_Input\_GetDeviceIds()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceIds(int32_t *deviceIds, int32_t inSize, int32_t *outSize)
```

**描述**

获取所有输入设备的ID列表。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t \*deviceIds | deviceIds 保存输入设备ID的列表。 |
| int32\_t inSize | 保存输入设备ID列表的大小。 |
| int32\_t \*outSize | outSize 输出输入设备ID列表的长度，值小于等于inSize长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceIds或outSize为空指针或inSize小于0。 |

### OH\_Input\_GetDevice()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDevice(int32_t deviceId, Input_DeviceInfo **deviceInfo)
```

**描述**

获取输入设备信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*\*deviceInfo | deviceInfo 指向输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo为空指针或deviceId无效。  可以通过 [OH\_Input\_GetDeviceIds](capi-oh-input-manager-h.md#oh_input_getdeviceids) 表示接口查询系统支持的设备ID。 |

### OH\_Input\_CreateDeviceInfo()

PhonePC/2in1TabletTVWearable

```
1. Input_DeviceInfo* OH_Input_CreateDeviceInfo(void)
```

**描述**

创建输入设备信息的对象。通过调用[OH\_Input\_DestroyDeviceInfo](capi-oh-input-manager-h.md#oh_input_destroydeviceinfo)销毁输入设备信息的对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| Input\_DeviceInfo\* | 如果操作成功，返回设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)实例的指针。否则返回空指针，可能的原因是分配内存失败。 |

### OH\_Input\_DestroyDeviceInfo()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_DestroyDeviceInfo(Input_DeviceInfo **deviceInfo)
```

**描述**

销毁输入设备信息的对象。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*\*deviceInfo | deviceInfo 设备信息的对象。 |

### OH\_Input\_GetKeyboardType()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetKeyboardType(int32_t deviceId, int32_t *keyboardType)
```

**描述**

获取输入设备的键盘类型。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t deviceId | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| int32\_t \*keyboardType | keyboardType 指向输入设备的键盘指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示设备ID为无效值或者keyboardType是空指针。 |

### OH\_Input\_GetDeviceId()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceId(Input_DeviceInfo *deviceInfo, int32_t *id)
```

**描述**

获取输入设备的ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| int32\_t \*id | id 指向输入设备ID的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者ID是空指针。 |

### OH\_Input\_GetDeviceName()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceName(Input_DeviceInfo *deviceInfo, char **name)
```

**描述**

获取输入设备的名称。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| char \*\*name | name 指向输入设备名称的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者name是空指针。 |

### OH\_Input\_GetCapabilities()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetCapabilities(Input_DeviceInfo *deviceInfo, int32_t *capabilities)
```

**描述**

获取有关输入设备能力信息，比如设备是触摸屏、触控板、键盘等。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| int32\_t \*capabilities | capabilities 指向输入设备能力信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者capabilities是空指针。 |

### OH\_Input\_GetDeviceVersion()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceVersion(Input_DeviceInfo *deviceInfo, int32_t *version)
```

**描述**

获取输入设备的版本信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| int32\_t \*version | version 指向输入设备版本信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者version是空指针。 |

### OH\_Input\_GetDeviceProduct()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceProduct(Input_DeviceInfo *deviceInfo, int32_t *product)
```

**描述**

获取输入设备的产品信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| int32\_t \*product | product 指向输入设备产品信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者product是空指针。 |

### OH\_Input\_GetDeviceVendor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceVendor(Input_DeviceInfo *deviceInfo, int32_t *vendor)
```

**描述**

获取输入设备的厂商信息。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| int32\_t \*vendor | vendor 指向输入设备厂商信息的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者vendor是空指针。 |

### OH\_Input\_GetDeviceAddress()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetDeviceAddress(Input_DeviceInfo *deviceInfo, char **address)
```

**描述**

获取输入设备的物理地址。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_DeviceInfo](capi-input-input-deviceinfo.md) \*deviceInfo | deviceInfo 输入设备信息[Input\_DeviceInfo](capi-input-input-deviceinfo.md)。 |
| char \*\*address | address 指向输入设备物理地址的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示deviceInfo或者address是空指针。 |

### OH\_Input\_GetFunctionKeyState()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetFunctionKeyState(int32_t keyCode, int32_t *state)
```

**描述**

获取功能键状态。

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t keyCode | 功能键值。目前仅支持CapsLock键，键值为1。 |
| int32\_t \*state | state 功能键状态。0表示功能键关闭，1表示功能键打开。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetFunctionKeyState 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示获取状态成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。  [INPUT\_KEYBOARD\_DEVICE\_NOT\_EXIST](capi-oh-input-manager-h.md#input_result) 表示键盘设备不存在。 |

### OH\_Input\_InjectTouchEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_InjectTouchEvent(const struct Input_TouchEvent* touchEvent)
```

**描述**

使用以指定屏幕左上角为原点的相对坐标系的坐标注入触屏输入事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

从API version 20开始，建议先使用[OH\_Input\_RequestInjection](capi-oh-input-manager-h.md#oh_input_requestinjection)请求授权。然后通过[OH\_Input\_QueryAuthorizedStatus](capi-oh-input-manager-h.md#oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](capi-oh-input-manager-h.md#input_injectionstatus)时，再使用该接口。

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备上调用无效果。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | OH\_Input\_InjectTouchEvent 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示注入成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。  [INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result) 表示缺少权限。 |

### OH\_Input\_InjectMouseEvent()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_InjectMouseEvent(const struct Input_MouseEvent* mouseEvent)
```

**描述**

使用以指定屏幕左上角为原点的相对坐标系的坐标注入鼠标事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

从API version 20开始，建议先使用[OH\_Input\_RequestInjection](capi-oh-input-manager-h.md#oh_input_requestinjection)请求授权。然后通过[OH\_Input\_QueryAuthorizedStatus](capi-oh-input-manager-h.md#oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](capi-oh-input-manager-h.md#input_injectionstatus)时，再使用该接口。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | OH\_Input\_InjectTouchEvent 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示注入成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。  [INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result) 表示缺少权限。 |

### OH\_Input\_GetMouseEventDisplayId()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventDisplayId(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件的屏幕ID。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

**起始版本：** 15

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 若获取鼠标事件的屏幕ID成功，则返回鼠标事件的屏幕ID；若mouseEvent为NULL，则返回-1。 |

### OH\_Input\_QueryMaxTouchPoints()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_QueryMaxTouchPoints(int32_t *count)
```

**描述**

查询设备支持的最大触屏报点数。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t \*count | 设备支持的最大触屏报点数，count取值范围为0-10，-1表示未知数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_QueryMaxTouchPoints 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示查询成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。 |

### OH\_Input\_InjectMouseEventGlobal()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_InjectMouseEventGlobal(const struct Input_MouseEvent* mouseEvent)
```

**描述**

使用以主屏左上角为原点的全局坐标系的坐标注入鼠标事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

建议先使用[OH\_Input\_RequestInjection](capi-oh-input-manager-h.md#oh_input_requestinjection)请求授权。然后通过[OH\_Input\_QueryAuthorizedStatus](capi-oh-input-manager-h.md#oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](capi-oh-input-manager-h.md#input_injectionstatus)时，再使用该接口。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | OH\_Input\_InjectMouseEventGlobal 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示注入成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。  [INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result) 表示缺少权限。 |

### OH\_Input\_SetMouseEventGlobalX()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventGlobalX(struct Input_MouseEvent* mouseEvent, int32_t globalX)
```

**描述**

设置鼠标事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t globalX | 鼠标事件以主屏左上角为原点的全局坐标系的X坐标。 |

### OH\_Input\_GetMouseEventGlobalX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventGlobalX(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标事件以主屏左上角为原点的全局坐标系的X坐标。 |

### OH\_Input\_SetMouseEventGlobalY()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetMouseEventGlobalY(struct Input_MouseEvent* mouseEvent, int32_t globalY)
```

**描述**

设置鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |
| int32\_t globalY | 鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。 |

### OH\_Input\_GetMouseEventGlobalY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetMouseEventGlobalY(const struct Input_MouseEvent* mouseEvent)
```

**描述**

获取鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象，通过[OH\_Input\_CreateMouseEvent](capi-oh-input-manager-h.md#oh_input_createmouseevent)接口可以创建鼠标事件对象。  使用完需使用[OH\_Input\_DestroyMouseEvent](capi-oh-input-manager-h.md#oh_input_destroymouseevent)接口销毁鼠标事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 鼠标事件以主屏左上角为原点的全局坐标系的Y坐标。 |

### OH\_Input\_InjectTouchEventGlobal()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_InjectTouchEventGlobal(const struct Input_TouchEvent* touchEvent)
```

**描述**

使用以主屏左上角为原点的全局坐标系的坐标注入触屏输入事件。

如果当前处于用户未授权状态，调用该接口注入事件不生效。

建议先使用[OH\_Input\_RequestInjection](capi-oh-input-manager-h.md#oh_input_requestinjection)请求授权。然后通过[OH\_Input\_QueryAuthorizedStatus](capi-oh-input-manager-h.md#oh_input_queryauthorizedstatus)查询授权状态，当授权状态为[AUTHORIZED](capi-oh-input-manager-h.md#input_injectionstatus)时，再使用该接口。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | OH\_Input\_InjectTouchEventGlobal 函数返回值。  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示注入成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。  [INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result) 表示缺少权限。 |

### OH\_Input\_SetTouchEventGlobalX()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventGlobalX(struct Input_TouchEvent* touchEvent, int32_t globalX)
```

**描述**

设置触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t globalX | 触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。 |

### OH\_Input\_GetTouchEventGlobalX()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventGlobalX(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏输入事件以主屏左上角为原点的全局坐标系的X坐标。 |

### OH\_Input\_SetTouchEventGlobalY()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_SetTouchEventGlobalY(struct Input_TouchEvent* touchEvent, int32_t globalY)
```

**描述**

设置触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |
| int32\_t globalY | 触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。 |

### OH\_Input\_GetTouchEventGlobalY()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Input_GetTouchEventGlobalY(const struct Input_TouchEvent* touchEvent)
```

**描述**

获取触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const struct [Input\_TouchEvent](capi-input-input-touchevent.md)\* touchEvent | 触屏输入事件对象，通过[OH\_Input\_CreateTouchEvent](capi-oh-input-manager-h.md#oh_input_createtouchevent)接口可以创建触屏输入事件对象。  使用完需使用[OH\_Input\_DestroyTouchEvent](capi-oh-input-manager-h.md#oh_input_destroytouchevent)接口销毁触屏输入事件对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 触屏输入事件以主屏左上角为原点的全局坐标系的Y坐标。 |

### OH\_Input\_SetAxisEventGlobalX()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventGlobalX(struct Input_AxisEvent* axisEvent, int32_t globalX)
```

**描述**

设置轴事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t globalX | 轴事件以主屏左上角为原点的全局坐标系的X坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示axisEvent是空指针。 |

### OH\_Input\_GetAxisEventGlobalX()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventGlobalX(const Input_AxisEvent* axisEvent, int32_t* globalX)
```

**描述**

获取轴事件以主屏左上角为原点的全局坐标系的X坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t\* globalX | 轴事件以主屏左上角为原点的全局坐标系的X坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示axisEvent或者globalX是空指针。 |

### OH\_Input\_SetAxisEventGlobalY()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetAxisEventGlobalY(struct Input_AxisEvent* axisEvent, int32_t globalY)
```

**描述**

设置轴事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t globalY | 轴事件以主屏左上角为原点的全局坐标系的Y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示axisEvent是空指针。 |

### OH\_Input\_GetAxisEventGlobalY()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetAxisEventGlobalY(const Input_AxisEvent* axisEvent, int32_t* globalY)
```

**描述**

获取轴事件以主屏左上角为原点的全局坐标系的Y坐标。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_AxisEvent](capi-input-input-axisevent.md)\* axisEvent | 轴事件对象，通过[OH\_Input\_CreateAxisEvent](capi-oh-input-manager-h.md#oh_input_createaxisevent)接口可以创建轴事件对象。  使用完需使用[OH\_Input\_DestroyAxisEvent](capi-oh-input-manager-h.md#oh_input_destroyaxisevent)接口销毁轴事件对象。 |
| int32\_t\* globalY | 轴事件以主屏左上角为原点的全局坐标系的Y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示axisEvent或者globalY是空指针。 |

### OH\_Input\_GetPointerLocation()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetPointerLocation(int32_t *displayId, double *displayX, double *displayY)
```

**描述**

获取当前屏幕上鼠标的坐标点。

**设备行为差异**：该接口在Wearable设备上返回3900010错误码，在其他设备上可正常调用。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t \*displayId | 当前屏幕的屏幕ID。 |
| double \*displayX | 鼠标在当前屏幕的X坐标。 |
| double \*displayY | 鼠标在当前屏幕的Y坐标。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetPointerLocation 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示查询成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数错误。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常。  [INPUT\_APP\_NOT\_FOCUSED](capi-oh-input-manager-h.md#input_result) 表示当前应用不是焦点应用。  [INPUT\_DEVICE\_NO\_POINTER](capi-oh-input-manager-h.md#input_result) 表示无鼠标类输入外设。 |

### OH\_Input\_GetKeyEventId()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetKeyEventId(const struct Input_KeyEvent* keyEvent, int32_t* eventId)
```

**描述**

获取按键事件的ID。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEvent](capi-input-input-keyevent.md)\* keyEvent | 按键事件对象，通过[OH\_Input\_CreateKeyEvent](capi-oh-input-manager-h.md#oh_input_createkeyevent)接口可以创建按键事件对象。  使用完需使用[OH\_Input\_DestroyKeyEvent](capi-oh-input-manager-h.md#oh_input_destroykeyevent)接口销毁按键事件对象。 |
| int32\_t\* eventId | 按键事件的ID。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetKeyEventId 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。 |

### OH\_Input\_AddKeyEventHook()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_AddKeyEventHook(Input_KeyEventCallback callback)
```

**描述**

添加一个按键事件拦截钩子函数。

添加后可以通过[OH\_Input\_RemoveKeyEventHook](capi-oh-input-manager-h.md#oh_input_removekeyeventhook)接口移除。一个进程仅支持设置一个钩子，一个应用支持多个钩子函数，后添加的生效优先级更高。

在使用该接口之前，需要用户在设备的“设置”->“隐私和安全”->“权限管理”中打开“键盘输入辅助”权限。该权限仅PC/2in1、Tablet设备支持。

**需要权限：** ohos.permission.HOOK\_KEY\_EVENT

**设备行为差异**：该接口在Wearable设备上返回801错误码，在其他设备上可正常调用。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEventCallback](capi-oh-input-manager-h.md#input_keyeventcallback) callback | 钩子函数，用于拦截待分发的所有按键事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_AddKeyEventHook 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。  [INPUT\_DEVICE\_NOT\_SUPPORTED](capi-oh-input-manager-h.md#input_result) 表示不支持该功能。  [INPUT\_PERMISSION\_DENIED](capi-oh-input-manager-h.md#input_result) 表示权限验证失败。  [INPUT\_REPEAT\_INTERCEPTOR](capi-oh-input-manager-h.md#input_result) 表示重复设置钩子。一个进程仅支持设置一个钩子。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_RemoveKeyEventHook()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_RemoveKeyEventHook(Input_KeyEventCallback callback)
```

**描述**

移除按键事件拦截钩子函数。

通常与[OH\_Input\_AddKeyEventHook](capi-oh-input-manager-h.md#oh_input_addkeyeventhook)接口配合使用。

**起始版本：** 21

**设备行为差异**：该接口在Wearable设备上返回801错误码，在其他设备上可正常调用。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_KeyEventCallback](capi-oh-input-manager-h.md#input_keyeventcallback) callback | 钩子函数，用于拦截待分发的所有按键事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_RemoveKeyEventHook 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。如果之前没有添加对应钩子，移除时也会返回成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_DispatchToNextHandler()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_DispatchToNextHandler(int32_t eventId)
```

**描述**

重新分发按键事件。

只有被钩子拦截的按键事件才能被重新分发，重新分发的事件必须保持原有优先级顺序。

调用该接口后，按键事件可在3秒内重新分发。如果超过3秒，将返回[INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result)。

重新分发的事件需要保证配对关系。如果重新分发了一个或多个按键按下事件[KEY\_ACTION\_DOWN](capi-oh-input-manager-h.md#input_keyeventaction)，再重新分发按键抬起事件[KEY\_ACTION\_UP](capi-oh-input-manager-h.md#input_keyeventaction)或按键动作取消事件[KEY\_ACTION\_CANCEL](capi-oh-input-manager-h.md#input_keyeventaction)可以成功。

如果仅分发[KEY\_ACTION\_UP](capi-oh-input-manager-h.md#input_keyeventaction)或[KEY\_ACTION\_CANCEL](capi-oh-input-manager-h.md#input_keyeventaction)按键事件，接口可以调用成功，但不会执行实际的分发动作。

如果分发的事件未被钩子拦截，函数调用会成功，但不会执行实际的分发动作。

**设备行为差异**：该接口在Wearable设备上返回801错误码，在其他设备上可正常调用。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t eventId | 按键事件的ID。可以通过[OH\_Input\_GetKeyEventId](capi-oh-input-manager-h.md#oh_input_getkeyeventid)接口获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_DispatchToNextHandler 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。可通过[OH\_Input\_GetKeyEventId](capi-oh-input-manager-h.md#oh_input_getkeyeventid)查看传入的eventId是否准确。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_SetPointerVisible()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetPointerVisible(bool visible)
```

**描述**

设置当前窗口的鼠标光标的显示或隐藏状态。

**设备行为差异**：该接口在Wearable设备上返回801错误码，在其他设备上可正常调用。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool visible | 鼠标光标是否显示。true表示显示，false表示不显示。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_SetPointerVisible 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_DEVICE\_NOT\_SUPPORTED](capi-oh-input-manager-h.md#input_result) 表示设备不支持。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_GetPointerStyle()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetPointerStyle(int32_t windowId, int32_t *pointerStyle)
```

**描述**

获取指定窗口的鼠标光标样式。

**设备行为差异**：该接口在Wearable设备上调用无效果，在其他设备上可正常调用。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。  仅支持传入当前窗口和全局窗口的ID，传入其他ID返回全局窗口的默认光标样式，当前窗口ID可以通过[getWindowProperties](arkts-apis-window-window.md#getwindowproperties9)获取。 |
| int32\_t\* pointerStyle | 鼠标光标样式的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetPointerStyle 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_SetPointerStyle()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetPointerStyle(int32_t windowId, int32_t pointerStyle)
```

**描述**

设置指定窗口的鼠标光标样式。

**设备行为差异**：该接口在Wearable设备上调用无效果，在其他设备上可正常调用。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 窗口ID。取值范围为大于等于0的整数。  仅支持传入当前窗口的光标样式，传入其他窗口ID本接口可以运行成功但设置不生效，当前窗口ID可以通过[getWindowProperties](arkts-apis-window-window.md#getwindowproperties9)获取。 |
| int32\_t pointerStyle | 鼠标光标样式，取值为[Input\_PointerStyle](capi-oh-pointer-style-h.md#input_pointerstyle)的枚举值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_SetPointerStyle 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_CustomCursor\_Create()

PhonePC/2in1TabletTVWearable

```
1. Input_CustomCursor* OH_Input_CustomCursor_Create(OH_PixelmapNative* pixelMap, int32_t anchorX, int32_t anchorY)
```

**描述**

创建自定义鼠标光标资源对象。通过调用[OH\_Input\_CustomCursor\_Destroy](capi-oh-input-manager-h.md#oh_input_customcursor_destroy)销毁自定义鼠标光标资源对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| OH\_PixelmapNative\* pixelMap | [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)自定义鼠标光标像素图。最小限制为资源图本身的最小限制。最大限制为256 x 256px。 |
| int32\_t anchorX | 自定义鼠标光标焦点的水平坐标。该坐标受自定义鼠标光标大小的限制。最小值为0，最大值为资源图的宽度最大值，单位为px。 |
| int32\_t anchorY | 自定义鼠标光标焦点的垂直坐标。该坐标受自定义鼠标光标大小的限制。最小值为0，最大值为资源图的高度最大值，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| Input\_CustomCursor\* | [Input\_CustomCursor](capi-input-input-customcursor.md)对象。操作成功时返回自定义鼠标光标资源对象的指针。异常时返回空指针。 |

### OH\_Input\_CustomCursor\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_CustomCursor_Destroy(Input_CustomCursor** customCursor)
```

**描述**

销毁自定义鼠标光标资源对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| Input\_CustomCursor\*\* customCursor | 自定义鼠标光标资源[Input\_CustomCursor](capi-input-input-customcursor.md)。 |

### OH\_Input\_CustomCursor\_GetPixelMap()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CustomCursor_GetPixelMap(Input_CustomCursor* customCursor, OH_PixelmapNative** pixelMap)
```

**描述**

获取指定自定义鼠标光标资源的自定义鼠标光标像素图。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| Input\_CustomCursor\* customCursor | 自定义鼠标光标资源[Input\_CustomCursor](capi-input-input-customcursor.md)。 |
| OH\_PixelmapNative\*\* pixelMap | [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)自定义鼠标光标像素图。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CustomCursor\_GetPixelMap 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。 |

### OH\_Input\_CustomCursor\_GetAnchor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CustomCursor_GetAnchor(Input_CustomCursor* customCursor, int32_t* anchorX, int32_t* anchorY)
```

**描述**

获取指定自定义鼠标光标资源的焦点坐标。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| Input\_CustomCursor\* customCursor | 自定义鼠标光标资源[Input\_CustomCursor](capi-input-input-customcursor.md)。 |
| int32\_t\* anchorX | 自定义鼠标光标资源的焦点水平坐标，单位为px。 |
| int32\_t\* anchorY | 自定义鼠标光标资源的焦点垂直坐标，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CustomCursor\_GetAnchor 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。 |

### OH\_Input\_CursorConfig\_Create()

PhonePC/2in1TabletTVWearable

```
1. Input_CursorConfig* OH_Input_CursorConfig_Create(bool followSystem)
```

**描述**

创建自定义鼠标光标配置对象。通过调用[OH\_Input\_CursorConfig\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorconfig_destroy)销毁自定义鼠标光标配置对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool followSystem | 是否根据系统设置调整鼠标光标大小。false表示使用自定义鼠标光标样式大小，true表示根据系统设置调整鼠标光标大小，可调整范围为：[光标资源图大小，256×256]，单位为px。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| Input\_CursorConfig\* | 自定义鼠标光标配置[Input\_CursorConfig](capi-input-input-cursorconfig.md)对象。 |

### OH\_Input\_CursorConfig\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_CursorConfig_Destroy(Input_CursorConfig** cursorConfig)
```

**描述**

销毁自定义鼠标光标配置对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| Input\_CursorConfig\*\* cursorConfig | 自定义鼠标光标配置[Input\_CursorConfig](capi-input-input-cursorconfig.md)对象。 |

### OH\_Input\_CursorConfig\_IsFollowSystem()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CursorConfig_IsFollowSystem(Input_CursorConfig *cursorConfig, bool *followSystem)
```

**描述**

查询自定义鼠标光标配置是否跟随系统设置调整光标大小。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| Input\_CursorConfig\* cursorConfig | 自定义鼠标光标配置[Input\_CursorConfig](capi-input-input-cursorconfig.md)。 |
| bool\* followSystem | 是否根据系统设置调整光标大小，取值为true表示根据系统设置调整鼠标光标大小，取值为false表示使用自定义鼠标光标样式大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CursorConfig\_IsFollowSystem 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。 |

### OH\_Input\_SetCustomCursor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_SetCustomCursor(int32_t windowId, Input_CustomCursor* customCursor, Input_CursorConfig* cursorConfig)
```

**描述**

设置自定义鼠标光标样式。

应用窗口布局改变、热区切换、页面跳转、光标移出再回到窗口、光标在窗口不同区域移动，以上场景可能导致光标切换回系统样式，需要开发者重新设置光标样式。

**设备行为差异**：该接口在Wearable设备上返回801错误码，在其他设备上可正常调用。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t windowId | 窗口ID。取值范围为大于等于0的整数，仅支持传入当前窗口的光标样式。 |
| Input\_CustomCursor\* customCursor | 自定义鼠标光标资源[Input\_CustomCursor](capi-input-input-customcursor.md)。 |
| Input\_CursorConfig\* cursorConfig | 自定义鼠标光标配置[Input\_CursorConfig](capi-input-input-cursorconfig.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_SetCustomCursor 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。  [INPUT\_INVALID\_WINDOWID](capi-oh-input-manager-h.md#input_result) 表示窗口ID无效。  [INPUT\_DEVICE\_NOT\_SUPPORTED](capi-oh-input-manager-h.md#input_result) 表示设备不支持。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |

### OH\_Input\_CursorInfo\_Create()

PhonePC/2in1TabletTVWearable

```
1. struct Input_CursorInfo* OH_Input_CursorInfo_Create()
```

**描述**

创建鼠标光标信息对象。通过调用[OH\_Input\_CursorInfo\_Destroy](capi-oh-input-manager-h.md#oh_input_cursorinfo_destroy)销毁鼠标光标信息对象。

**起始版本：** 22

**返回：**

| 类型 | 说明 |
| --- | --- |
| struct Input\_CursorInfo\* | 创建成功返回一个[Input\_CursorInfo](capi-input-input-cursorinfo.md)对象，否则返回空指针，可能原因是内存分配失败。 |

### OH\_Input\_CursorInfo\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Input_CursorInfo_Destroy(Input_CursorInfo** cursorInfo)
```

**描述**

销毁鼠标光标信息对象。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\*\* cursorInfo | 鼠标光标信息对象。 |

### OH\_Input\_CursorInfo\_IsVisible()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CursorInfo_IsVisible(Input_CursorInfo* cursorInfo, bool* visible)
```

**描述**

获取指定鼠标光标信息对象对应的光标显示状态。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\* cursorInfo | 指定鼠标光标信息对象。可以通过[OH\_Input\_GetMouseEventCursorInfo](capi-oh-input-manager-h.md#oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH\_Input\_GetCursorInfo](capi-oh-input-manager-h.md#oh_input_getcursorinfo)接口查询当前的鼠标光标信息。 |
| bool\* visible | 鼠标光标显示或隐藏状态。true代表显示状态，false代表隐藏状态。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CursorInfo\_IsVisible 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。 |

### OH\_Input\_CursorInfo\_GetStyle()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CursorInfo_GetStyle(Input_CursorInfo* cursorInfo, Input_PointerStyle* style)
```

**描述**

获取指定鼠标光标信息对象对应的光标样式。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\* cursorInfo | 指定鼠标光标信息对象。可以通过[OH\_Input\_GetMouseEventCursorInfo](capi-oh-input-manager-h.md#oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH\_Input\_GetCursorInfo](capi-oh-input-manager-h.md#oh_input_getcursorinfo)接口查询当前的鼠标光标信息。 |
| [Input\_PointerStyle](capi-oh-pointer-style-h.md) | 鼠标光标信息的光标样式枚举，具体请参考[Input\_PointerStyle](capi-oh-pointer-style-h.md#input_pointerstyle)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CursorInfo\_GetStyle 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败或者光标不可见。 |

### OH\_Input\_CursorInfo\_GetSizeLevel()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CursorInfo_GetSizeLevel(Input_CursorInfo* cursorInfo, int32_t* sizeLevel)
```

**描述**

获取指定鼠标光标信息对象对应的光标大小档位。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\* cursorInfo | 指定鼠标光标信息对象。可以通过[OH\_Input\_GetMouseEventCursorInfo](capi-oh-input-manager-h.md#oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH\_Input\_GetCursorInfo](capi-oh-input-manager-h.md#oh_input_getcursorinfo)接口查询当前的鼠标光标信息。 |
| int32\_t\* sizeLevel | 鼠标光标信息的光标大小档位。取值范围为整数1~7，数值越大则光标越大。应用自定义光标[DEVELOPER\_DEFINED\_ICON](capi-oh-pointer-style-h.md#input_pointerstyle)请以实际位图大小为准。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CursorInfo\_GetSizeLevel 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败或者光标不可见。 |

### OH\_Input\_CursorInfo\_GetColor()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_CursorInfo_GetColor(Input_CursorInfo* cursorInfo, uint32_t* color)
```

**描述**

获取指定鼠标光标信息对象对应的光标颜色, 使用32位ARGB整数表示。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\* cursorInfo | 指定鼠标光标信息对象。可以通过[OH\_Input\_GetMouseEventCursorInfo](capi-oh-input-manager-h.md#oh_input_getmouseeventcursorinfo)查询指定鼠标事件的鼠标光标信息、或通过[OH\_Input\_GetCursorInfo](capi-oh-input-manager-h.md#oh_input_getcursorinfo)接口查询当前的鼠标光标信息。 |
| uint32\_t\* color | 鼠标光标信息的光标颜色, 使用32位ARGB整数表示。应用自定义光标[DEVELOPER\_DEFINED\_ICON](capi-oh-pointer-style-h.md#input_pointerstyle)请以实际位图颜色为准。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_CursorInfo\_GetColor 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败或者光标不可见。 |

### OH\_Input\_GetMouseEventCursorInfo()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetMouseEventCursorInfo(const struct Input_MouseEvent* mouseEvent, Input_CursorInfo* cursorInfo)
```

**描述**

获取鼠标事件的鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [Input\_MouseEvent](capi-input-input-mouseevent.md)\* mouseEvent | 鼠标事件对象。可以通过[OH\_Input\_AddMouseEventMonitor](capi-oh-input-manager-h.md#oh_input_addmouseeventmonitor)或者[OH\_Input\_AddInputEventInterceptor](capi-oh-input-manager-h.md#oh_input_addinputeventinterceptor)接口的回调函数中获取鼠标事件对象。 |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\* cursorInfo | 鼠标光标信息对象，可以通过[OH\_Input\_CursorInfo\_Create](capi-oh-input-manager-h.md#oh_input_cursorinfo_create)接口创建鼠标光标信息对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetMouseEventCursorInfo 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。 |

### OH\_Input\_GetCursorInfo()

PhonePC/2in1TabletTVWearable

```
1. Input_Result OH_Input_GetCursorInfo(Input_CursorInfo* cursorInfo, OH_PixelmapNative** pixelmap)
```

**描述**

查询当前鼠标光标信息，包括光标显示状态、光标样式、光标大小档位、光标颜色。如果pixelmap参数非空，且光标样式为[DEVELOPER\_DEFINED\_ICON](capi-oh-pointer-style-h.md#input_pointerstyle)，则会同时返回光标的PixelMap位图对象。

**设备行为差异**：该接口在Wearable设备上调用无效果，在其他设备上可正常调用。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Input\_CursorInfo](capi-input-input-cursorinfo.md)\* cursorInfo | 鼠标光标信息对象，可以通过[OH\_Input\_CursorInfo\_Create](capi-oh-input-manager-h.md#oh_input_cursorinfo_create)接口创建鼠标光标信息对象。 |
| [OH\_PixelmapNative](capi-image-nativemodule-oh-pixelmapnative.md)\*\* pixelmap | PixelMap位图对象，如果该参数非空且光标为应用自定义，则会返回光标的PixelMap位图对象，否则不返回PixelMap位图对象。首先通过[OH\_PixelmapInitializationOptions\_Create](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_create)接口创建OH\_PixelmapInitializationOptions对象，然后调用[OH\_PixelmapInitializationOptions\_SetWidth](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setwidth)接口设置大于0的宽度，调用[OH\_PixelmapInitializationOptions\_SetHeight](capi-pixelmap-native-h.md#oh_pixelmapinitializationoptions_setheight)接口设置大于0的高度，最后以该OH\_PixelmapInitializationOptions对象作为入参调用[OH\_PixelmapNative\_CreateEmptyPixelmap](capi-pixelmap-native-h.md#oh_pixelmapnative_createemptypixelmap)接口创建PixelMap位图对象。  使用完需要先调用[OH\_PixelmapNative\_Release](capi-pixelmap-native-h.md#oh_pixelmapnative_release)接口释放PixelMap位图对象，然后调用[OH\_PixelmapNative\_Destroy](capi-pixelmap-native-h.md#oh_pixelmapnative_destroy)接口销毁PixelMap位图对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Input\_Result](capi-oh-input-manager-h.md#input_result) | OH\_Input\_GetCursorInfo 函数返回值：  [INPUT\_SUCCESS](capi-oh-input-manager-h.md#input_result) 表示操作成功。  [INPUT\_PARAMETER\_ERROR](capi-oh-input-manager-h.md#input_result) 表示参数检查失败。  [INPUT\_SERVICE\_EXCEPTION](capi-oh-input-manager-h.md#input_result) 表示服务异常，请重试。 |
