---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-controller-monitor-pad
title: 监听游戏手柄的轴和按键事件（C/C++）
breadcrumb: 指南 > 应用服务 > Game Controller Kit（游戏控制器服务） > 监听游戏手柄的轴和按键事件（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2def58f3ce4c21d610e84ada1bd0bc18bfecee15da0c59f6442bdb7f7571b6db
---

说明

须先完成[监听设备上下线](game-controller-monitor-device.md)功能的开发后，才能进行游戏手柄轴事件和按键事件的监听注册。

## 功能介绍

Game Controller Kit提供游戏手柄轴事件和按键事件的监听能力。通过轴事件和按键事件的监听注册，在玩家操作手柄按键和摇杆时可获得对应回调通知。

## 按键

Game Controller Kit支持的手柄键位参考图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/EYEIA4EYSRmpuByEYDlQlg/zh-cn_image_0000002552799234.png?HW-CC-KV=V1&HW-CC-Date=20260427T234859Z&HW-CC-Expire=86400&HW-CC-Sign=791C6F72DC62678F52D773257D4A08CA30A2BA66EF8F71AA9B4D06DE42ED69B6)

## 接口说明

接口详细介绍请参考[API参考](../harmonyos-references/capi-game-controller.md)。

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

```
1. target_link_libraries(entry PUBLIC libohgame_controller.z.so)
```

### 导入模块

```
1. #include <GameControllerKit/game_pad.h>
```

### 注册和取消注册轴事件的监听

调用相应接口注册或取消注册轴事件回调，通过回调函数获取轴值。

物理轴及其对应的轴值获取接口如下：

| 物理轴 | 轴值获取接口 |
| --- | --- |
| LeftThumbstick | 通过OH\_GamePad\_AxisEvent\_GetXAxisValue获取X轴的轴值。  通过OH\_GamePad\_AxisEvent\_GetYAxisValue获取Y轴的轴值。 |
| RightThumbstick | 通过OH\_GamePad\_AxisEvent\_GetZAxisValue获取Z轴的轴值。  通过OH\_GamePad\_AxisEvent\_GetRZAxisValue获取RZ轴的轴值。 |
| DPAD | 通过OH\_GamePad\_AxisEvent\_GetHatXAxisValue获取HatX轴的轴值。  通过OH\_GamePad\_AxisEvent\_GetHatYAxisValue获取HatY轴的轴值。 |
| LeftTrigger | 通过OH\_GamePad\_AxisEvent\_GetBrakeAxisValue获取Brake轴的轴值。 |
| RightTrigger | 通过OH\_GamePad\_AxisEvent\_GetGasAxisValue获取Gas轴的轴值。 |

以LeftThumbstick轴事件为例。

```
1. napi_value GamePad::LeftThumbstick_RegisterAxisInputMonitor(napi_env env, napi_callback_info info) {
2. napi_value result;
3. GameController_ErrorCode errorCode =
4. OH_GamePad_LeftThumbstick_RegisterAxisInputMonitor(GamePad::LeftThumbstick_OnAxisEvent);
5. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
6. OH_LOG_ERROR(LOG_APP, "LeftThumbstick_RegisterAxisInputMonitor Failed, %{public}d", errorCode);
7. napi_create_double(env, errorCode, &result);
8. return result;
9. }
10. OH_LOG_INFO(LOG_APP, "LeftThumbstick_RegisterAxisInputMonitor Success");
11. napi_create_double(env, 0, &result);
12. return result;
13. }

15. napi_value GamePad::LeftThumbstick_UnregisterAxisInputMonitor(napi_env env, napi_callback_info info) {
16. napi_value result;
17. GameController_ErrorCode errorCode = OH_GamePad_LeftThumbstick_UnregisterAxisInputMonitor();
18. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
19. OH_LOG_ERROR(LOG_APP, "LeftThumbstick_UnregisterAxisInputMonitor Failed, %{public}d", errorCode);
20. napi_create_double(env, errorCode, &result);
21. return result;
22. }
23. OH_LOG_INFO(LOG_APP, "LeftThumbstick_UnregisterAxisInputMonitor Success");
24. napi_create_double(env, 0, &result);
25. return result;
26. }

28. void GamePad::LeftThumbstick_OnAxisEvent(const struct GamePad_AxisEvent *axisEvent) {
29. std::string val = "X";
30. double xAxisValue;
31. OH_GamePad_AxisEvent_GetXAxisValue(axisEvent, &xAxisValue);
32. val.append(std::to_string(xAxisValue)).append("_Y");
33. double yAxisValue;
34. OH_GamePad_AxisEvent_GetYAxisValue(axisEvent, &yAxisValue);
35. val.append(std::to_string(yAxisValue));
36. OnAxisEvent(axisEvent, "LeftThumbstick_OnAxisEvent", val);
37. }
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

```
1. napi_value GamePad::LeftShoulder_RegisterButtonInputMonitor(napi_env env, napi_callback_info info) {
2. napi_value result;
3. GameController_ErrorCode errorCode =
4. OH_GamePad_LeftShoulder_RegisterButtonInputMonitor(GamePad::LeftShoulder_OnButtonEvent);
5. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
6. OH_LOG_ERROR(LOG_APP, "LeftShoulder_RegisterButtonInputMonitor Failed, %{public}d", errorCode);
7. napi_create_double(env, errorCode, &result);
8. return result;
9. }
10. OH_LOG_INFO(LOG_APP, "LeftShoulder_RegisterButtonInputMonitor Success");
11. napi_create_double(env, 0, &result);
12. return result;
13. }

15. napi_value GamePad::LeftShoulder_UnregisterButtonInputMonitor(napi_env env, napi_callback_info info) {
16. napi_value result;
17. GameController_ErrorCode errorCode = OH_GamePad_LeftShoulder_UnregisterButtonInputMonitor();
18. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
19. OH_LOG_ERROR(LOG_APP, "LeftShoulder_UnregisterButtonInputMonitor Failed, %{public}d", errorCode);
20. napi_create_double(env, errorCode, &result);
21. return result;
22. }
23. OH_LOG_INFO(LOG_APP, "LeftShoulder_UnregisterButtonInputMonitor Success");
24. napi_create_double(env, 0, &result);
25. return result;
26. }

28. void GamePad::LeftShoulder_OnButtonEvent(const struct GamePad_ButtonEvent *buttonEvent) {
29. OnButtonEvent(buttonEvent, "LeftShoulder_OnButtonEvent");
30. }

32. void GamePad::OnButtonEvent(const struct GamePad_ButtonEvent *buttonEvent, const std::string &buttonName) {
33. std::string temp;
34. temp.append("OnButtonEvent:").append(buttonName);
35. char *deviceId;
36. OH_GamePad_ButtonEvent_GetDeviceId(buttonEvent, &deviceId);
37. temp.append(" ,deviceId:").append(deviceId);
38. free(deviceId);
39. GamePad_Button_ActionType action;
40. OH_GamePad_ButtonEvent_GetButtonAction(buttonEvent, &action);
41. temp.append(" ,action:").append(std::to_string(action));
42. std::int32_t buttonCode;
43. OH_GamePad_ButtonEvent_GetButtonCode(buttonEvent, &buttonCode);
44. temp.append(" ,code:").append(std::to_string(buttonCode));
45. char *buttonCodeName;
46. OH_GamePad_ButtonEvent_GetButtonCodeName(buttonEvent, &buttonCodeName);
47. temp.append(" ,codeName:").append(buttonCodeName);
48. free(buttonCodeName);
49. std::int64_t actionTime;
50. OH_GamePad_ButtonEvent_GetActionTime(buttonEvent, &actionTime);
51. temp.append(" ,actionTime:").append(std::to_string(actionTime));
52. std::int32_t count;
53. OH_GamePad_PressedButtons_GetCount(buttonEvent, &count);
54. temp.append(" ,count:").append(std::to_string(count));
55. std::string pressedButtonCodes;
56. for (std::int32_t idx = 0; idx < count; idx++) {
57. GamePad_PressedButton *pressedButton;
58. OH_GamePad_PressedButtons_GetButtonInfo(buttonEvent, idx, &pressedButton);
59. int code;
60. OH_GamePad_PressedButton_GetButtonCode(pressedButton, &code);
61. char *name;
62. OH_GamePad_PressedButton_GetButtonCodeName(pressedButton, &name);
63. if (idx != 0) {
64. pressedButtonCodes = pressedButtonCodes.append(";");
65. }
66. pressedButtonCodes = pressedButtonCodes.append(std::to_string(code) + "|").append(name);
67. free(name);
68. OH_GamePad_DestroyPressedButton(&pressedButton);
69. }
70. temp.append(" ,pressedButtonCodes:").append(pressedButtonCodes);
71. OH_LOG_INFO(LOG_APP, "%{public}s", temp.c_str());
72. Log::GetInstance()->PrintLog(temp);
73. }
```
