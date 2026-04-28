---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-game-pad
title: game_pad.h
breadcrumb: API参考 > 应用服务 > Game Controller Kit（游戏控制器服务） > C API > 头文件和结构体 > 头文件 > game_pad.h
category: harmonyos-references
scraped_at: 2026-04-28T08:16:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:60057a4b7215181086e56ebbc8ebeddae9c31ba4a3c398b137e185396a4a9847
---

## 概述

PhonePC/2in1TabletTV

定义游戏手柄的接口。

**库：** libohgame\_controller.z.so

**系统能力：** SystemCapability.Game.GameController

**起始版本：** 21

**相关模块：**[GameController](capi-game-controller.md)

## 汇总

PhonePC/2in1TabletTV

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
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
