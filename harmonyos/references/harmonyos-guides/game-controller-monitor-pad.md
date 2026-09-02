---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-controller-monitor-pad
title: 监听游戏手柄的轴和按键事件（C/C++）
breadcrumb: 指南 > 应用服务 > Game Controller Kit（游戏控制器服务） > 监听游戏手柄的轴和按键事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:55+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:c0aaf1edcd177398a73774e124110fa19d32e97cc4ae7bdfd9b20b1dc9ef4948
---

**说明** 

须先完成[监听设备上下线](game-controller-monitor-device.md)功能的开发后，才能进行游戏手柄轴事件和按键事件的监听注册。

## 功能介绍

Game Controller Kit提供游戏手柄轴事件和按键事件的监听能力。通过轴事件和按键事件的监听注册，在玩家操作手柄按键和摇杆时可获得对应回调通知。

## 按键

Game Controller Kit支持的手柄键位参考图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/H6HenNiHSKCwxxqxQAwQ1g/zh-cn_image_0000002706834902.png)

## 接口说明

接口详细介绍请参考[GameController](../harmonyos-references/capi-gamecontroller.md)。

| 接口名 | 描述 |
| --- | --- |
| OH\_GamePad\_LeftShoulder\_RegisterButtonInputMonitor | 注册LeftShoulder按键事件的监听。 |
| OH\_GamePad\_RightShoulder\_RegisterButtonInputMonitor | 注册RightShoulder按键事件的监听。 |
| OH\_GamePad\_LeftTrigger\_RegisterButtonInputMonitor | 注册LeftTrigger按键事件的监听。 |
| OH\_GamePad\_RightTrigger\_RegisterButtonInputMonitor | 注册RightTrigger按键事件的监听。 |
| OH\_GamePad\_ButtonMenu\_RegisterButtonInputMonitor | 注册Menu按键事件的监听。 |
| OH\_GamePad\_ButtonHome\_RegisterButtonInputMonitor | 注册Home按键事件的监听。 |
| OH\_GamePad\_ButtonA\_RegisterButtonInputMonitor | 注册A按键事件的监听。 |
| OH\_GamePad\_ButtonB\_RegisterButtonInputMonitor | 注册B按键事件的监听。 |
| OH\_GamePad\_ButtonX\_RegisterButtonInputMonitor | 注册X按键事件的监听。 |
| OH\_GamePad\_ButtonY\_RegisterButtonInputMonitor | 注册Y按键事件的监听。 |
| OH\_GamePad\_ButtonC\_RegisterButtonInputMonitor | 注册C按键事件的监听。 |
| OH\_GamePad\_Dpad\_LeftButton\_RegisterButtonInputMonitor | 注册方向按键的向左按键事件的监听。 |
| OH\_GamePad\_Dpad\_RightButton\_RegisterButtonInputMonitor | 注册方向按键的向右按键事件的监听。 |
| OH\_GamePad\_Dpad\_UpButton\_RegisterButtonInputMonitor | 注册方向按键的向上按键事件的监听。 |
| OH\_GamePad\_Dpad\_DownButton\_RegisterButtonInputMonitor | 注册方向按键的向下按键事件的监听。 |
| OH\_GamePad\_LeftThumbstick\_RegisterButtonInputMonitor | 注册LeftThumbstick按键事件的监听。 |
| OH\_GamePad\_RightThumbstick\_RegisterButtonInputMonitor | 注册RightThumbstick按键事件的监听。 |
| OH\_GamePad\_LeftTrigger\_RegisterAxisInputMonitor | 注册LeftTrigger轴事件的监听。 |
| OH\_GamePad\_RightTrigger\_RegisterAxisInputMonitor | 注册RightTrigger轴事件的监听。 |
| OH\_GamePad\_Dpad\_RegisterAxisInputMonitor | 注册方向按键轴事件的监听。 |
| OH\_GamePad\_LeftThumbstick\_RegisterAxisInputMonitor | 注册LeftThumbstick轴事件的监听。 |
| OH\_GamePad\_RightThumbstick\_RegisterAxisInputMonitor | 注册RightThumbstick轴事件的监听。 |

## 开发步骤

### 链接动态库

```c
target_link_libraries(entry PUBLIC libohgame_controller.z.so)
```

### 导入模块

```c
#include <GameControllerKit/game_pad.h>
```

### 注册和取消注册轴事件的监听

调用相应接口注册或取消注册轴事件回调，通过回调函数获取轴值。

物理轴及其对应的轴值获取接口如下：

| 物理轴 | 轴值获取接口 |
| --- | --- |
| LeftThumbstick | 通过[OH\_GamePad\_AxisEvent\_GetXAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_getxaxisvalue)获取X轴的轴值。  通过[OH\_GamePad\_AxisEvent\_GetYAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_getyaxisvalue)获取Y轴的轴值。 |
| RightThumbstick | 通过[OH\_GamePad\_AxisEvent\_GetZAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_getzaxisvalue)获取Z轴的轴值。  通过[OH\_GamePad\_AxisEvent\_GetRZAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_getrzaxisvalue)获取RZ轴的轴值。 |
| DPAD | 通过[OH\_GamePad\_AxisEvent\_GetHatXAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_gethatxaxisvalue)获取HatX轴的轴值。  通过[OH\_GamePad\_AxisEvent\_GetHatYAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_gethatyaxisvalue)获取HatY轴的轴值。 |
| LeftTrigger | 通过[OH\_GamePad\_AxisEvent\_GetBrakeAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_getbrakeaxisvalue)获取Brake轴的轴值。 |
| RightTrigger | 通过[OH\_GamePad\_AxisEvent\_GetGasAxisValue](../harmonyos-references/capi-game-pad-event-h.md#oh_gamepad_axisevent_getgasaxisvalue)获取Gas轴的轴值。 |

以LeftThumbstick轴事件为例。

```c
// 注册LeftThumbstick轴事件监听
napi_value GamePad::LeftThumbstick_RegisterAxisInputMonitor(napi_env env, napi_callback_info info) {
    napi_value result;
    GameController_ErrorCode errorCode =
        OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor(GamePad::LeftThumbstick_OnAxisEvent);
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "LeftThumbstick_RegisterAxisInputMonitor Failed, %{public}d", errorCode);
        napi_create_double(env, errorCode, &result);
        return result;
    }
    OH_LOG_INFO(LOG_APP, "LeftThumbstick_RegisterAxisInputMonitor Success");
    napi_create_double(env, 0, &result);
    return result;
}

// 取消注册LeftThumbstick轴事件监听
napi_value GamePad::LeftThumbstick_UnregisterAxisInputMonitor(napi_env env, napi_callback_info info) {
    napi_value result;
    GameController_ErrorCode errorCode = OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor();
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "LeftThumbstick_UnregisterAxisInputMonitor Failed, %{public}d", errorCode);
        napi_create_double(env, errorCode, &result);
        return result;
    }
    OH_LOG_INFO(LOG_APP, "LeftThumbstick_UnregisterAxisInputMonitor Success");
    napi_create_double(env, 0, &result);
    return result;
}

void GamePad::LeftThumbstick_OnAxisEvent(const struct GamePad_AxisEvent *axisEvent) {
    std::string val = "X";
    double xAxisValue;
    OH_GamePad_AxisEvent_GetXAxisValue(axisEvent, &xAxisValue);
    val.append(std::to_string(xAxisValue)).append("_Y");
    double yAxisValue;
    OH_GamePad_AxisEvent_GetYAxisValue(axisEvent, &yAxisValue);
    val.append(std::to_string(yAxisValue));
    OnAxisEvent(axisEvent, "LeftThumbstick_OnAxisEvent", val);
}
```

### 注册按键事件的监听和取消注册

调用相应接口注册或取消注册按键事件回调，从回调函数中获取按键值。

以下是按键名称与对应按键值：

| 按键名称 | 按键值 |
| --- | --- |
| LeftShoulder | 2307 |
| RightShoulder | 2308 |
| LeftTrigger | 2309 |
| RightTrigger | 2310 |
| LeftThumbstick | 2314 |
| RightThumbstick | 2315 |
| ButtonHome | 2311 |
| ButtonMenu | 2312 |
| ButtonA | 2301 |
| ButtonB | 2302 |
| ButtonC | 2303 |
| ButtonX | 2304 |
| ButtonY | 2305 |
| Dpad\_UpButton | 2012 |
| Dpad\_DownButton | 2013 |
| Dpad\_LeftButton | 2014 |
| Dpad\_RightButton | 2015 |

以LeftShoulder按键事件为例。

```c
// 注册LeftShoulder按键事件监听
napi_value GamePad::LeftShoulder_RegisterButtonInputMonitor(napi_env env, napi_callback_info info) {
    napi_value result;
    GameController_ErrorCode errorCode =
        OH_GamePad_LeftShoulder_RegisterButtonInputMonitor(GamePad::LeftShoulder_OnButtonEvent);
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "LeftShoulder_RegisterButtonInputMonitor Failed, %{public}d", errorCode);
        napi_create_double(env, errorCode, &result);
        return result;
    }
    OH_LOG_INFO(LOG_APP, "LeftShoulder_RegisterButtonInputMonitor Success");
    napi_create_double(env, 0, &result);
    return result;
}

// 取消注册LeftShoulder按键事件监听
napi_value GamePad::LeftShoulder_UnregisterButtonInputMonitor(napi_env env, napi_callback_info info) {
    napi_value result;
    GameController_ErrorCode errorCode = OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor();
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "LeftShoulder_UnregisterButtonInputMonitor Failed, %{public}d", errorCode);
        napi_create_double(env, errorCode, &result);
        return result;
    }
    OH_LOG_INFO(LOG_APP, "LeftShoulder_UnregisterButtonInputMonitor Success");
    napi_create_double(env, 0, &result);
    return result;
}

void GamePad::LeftShoulder_OnButtonEvent(const struct GamePad_ButtonEvent *buttonEvent) {
    OnButtonEvent(buttonEvent, "LeftShoulder_OnButtonEvent");
}

void GamePad::OnButtonEvent(const struct GamePad_ButtonEvent *buttonEvent, const std::string &buttonName) {
    std::string temp;
    temp.append("OnButtonEvent:").append(buttonName);
    char *deviceId;
    OH_GamePad_ButtonEvent_GetDeviceId(buttonEvent, &deviceId);
    temp.append(" ,deviceId:").append(deviceId);
    free(deviceId);
    GamePad_Button_ActionType action;
    OH_GamePad_ButtonEvent_GetButtonAction(buttonEvent, &action);
    temp.append(" ,action:").append(std::to_string(action));
    std::int32_t buttonCode;
    OH_GamePad_ButtonEvent_GetButtonCode(buttonEvent, &buttonCode);
    temp.append(" ,code:").append(std::to_string(buttonCode));
    char *buttonCodeName;
    OH_GamePad_ButtonEvent_GetButtonCodeName(buttonEvent, &buttonCodeName);
    temp.append(" ,codeName:").append(buttonCodeName);
    free(buttonCodeName);
    std::int64_t actionTime;
    OH_GamePad_ButtonEvent_GetActionTime(buttonEvent, &actionTime);
    temp.append(" ,actionTime:").append(std::to_string(actionTime));
    std::int32_t count;
    OH_GamePad_PressedButtons_GetCount(buttonEvent, &count);
    temp.append(" ,count:").append(std::to_string(count));
    std::string pressedButtonCodes;
    for (std::int32_t idx = 0; idx < count; idx++) {
        GamePad_PressedButton *pressedButton;
        OH_GamePad_PressedButtons_GetButtonInfo(buttonEvent, idx, &pressedButton);
        int code;
        OH_GamePad_PressedButton_GetButtonCode(pressedButton, &code);
        char *name;
        OH_GamePad_PressedButton_GetButtonCodeName(pressedButton, &name);
        if (idx != 0) {
            pressedButtonCodes = pressedButtonCodes.append(";");
        }
        pressedButtonCodes = pressedButtonCodes.append(std::to_string(code) + "|").append(name);
        free(name);
        OH_GamePad_DestroyPressedButton(&pressedButton);
    }
    temp.append(" ,pressedButtonCodes:").append(pressedButtonCodes);
    OH_LOG_INFO(LOG_APP, "%{public}s", temp.c_str());
    Log::GetInstance()->PrintLog(temp);
}
```
