---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-controller-monitor-device
title: 监听设备上下线（C/C++）
breadcrumb: 指南 > 应用服务 > Game Controller Kit（游戏控制器服务） > 监听设备上下线（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fa3ba4785d05e9667cdc51c207c072c6fd7f2f0fe26cf2faccb675a17e33fba7
---

## 功能介绍

Game Controller Kit提供设备上下线事件监听和查询在线设备信息的功能。注册监听事件后，设备拔插时可获取实时回调通知，同时支持查询当前所有在线设备的具体信息。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/olsuxmrMTom_nB8T1B5mOA/zh-cn_image_0000002583478883.png?HW-CC-KV=V1&HW-CC-Date=20260427T234859Z&HW-CC-Expire=86400&HW-CC-Sign=AF794618321A234D4F6822443205A413267D231454FC75820EA4073F27129BB0)

1. 玩家启动游戏。
2. 游戏调用OH\_GameDevice\_RegisterDeviceMonitor接口注册设备状态变化事件监听。
3. 玩家插拔设备。
4. 终端系统将设备状态变化通知Game Controller Kit。
5. Game Controller Kit向游戏反馈设备状态变化。
6. 游戏调用OH\_GameDevice\_GetAllDeviceInfos接口向Game Controller Kit查询所有在线的游戏设备信息。
7. Game Controller Kit从终端系统获取所有在线的游戏设备信息。
8. 如果不再需要订阅，游戏可以调用OH\_GameDevice\_UnregisterDeviceMonitor接口取消设备状态变化事件监听。

## 接口说明

接口详细介绍请参考[API参考](../harmonyos-references/capi-game-controller.md)。

| 接口名 | 描述 |
| --- | --- |
| GameController\_ErrorCode OH\_GameDevice\_RegisterDeviceMonitor (GameDevice\_DeviceMonitorCallback deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| GameController\_ErrorCode OH\_GameDevice\_UnregisterDeviceMonitor (void) | 取消注册设备状态变化事件的监听回调。 |
| GameController\_ErrorCode OH\_GameDevice\_GetAllDeviceInfos (GameDevice\_AllDeviceInfos \*\*allDeviceInfos) | 获取所有在线设备的信息。 |

## 开发步骤

### 链接动态库

```
1. target_link_libraries(entry PUBLIC libohgame_controller.z.so)
```

### 导入模块

```
1. #include <GameControllerKit/game_device.h>
```

### 注册设备上下线监听

调用OH\_GameDevice\_RegisterDeviceMonitor接口注册设备状态变化监听，获取设备上下线的回调通知。

```
1. napi_value DeviceApi::RegisterDeviceMonitor(napi_env env, napi_callback_info info) {
2. napi_value result;
3. GameController_ErrorCode errorCode = OH_GameDevice_RegisterDeviceMonitor(DeviceApi::OnDeviceChanged);
4. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
5. OH_LOG_ERROR(LOG_APP, "RegisterDeviceMonitor Failed, %{public}d", errorCode);
6. napi_create_double(env, errorCode, &result);
7. return result;
8. }
9. OH_LOG_INFO(LOG_APP, "RegisterDeviceMonitor Success");
10. napi_create_double(env, 0, &result);
11. return result;
12. }

14. void DeviceApi::OnDeviceChanged(const struct GameDevice_DeviceEvent *deviceEvent) {
15. GameDevice_StatusChangedType type;
16. OH_GameDevice_DeviceEvent_GetChangedType(deviceEvent, &type);
17. GameDevice_DeviceInfo *deviceInfo;
18. OH_GameDevice_DeviceEvent_GetDeviceInfo(deviceEvent, &deviceInfo);
19. std::string temp = GetDeviceInfoStringForPrint(deviceInfo);
20. Log::GetInstance()->PrintLog("OnDeviceChanged type[" + std::to_string(type) + "] DeviceInfo" + temp);
21. OH_LOG_INFO(LOG_APP, "OnDeviceChanged type:%{public}d DeviceInfo:%{public}s", type, temp.c_str());
22. OH_GameDevice_DestroyDeviceInfo(&deviceInfo);
23. }
```

### 取消注册设备上下线监听

如果不再需要订阅，可以调用OH\_GameDevice\_UnregisterDeviceMonitor接口取消设备状态变化事件的监听。

```
1. napi_value DeviceApi::UnregisterDeviceMonitor(napi_env env, napi_callback_info info) {
2. napi_value result;
3. GameController_ErrorCode errorCode = OH_GameDevice_UnregisterDeviceMonitor();
4. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
5. OH_LOG_ERROR(LOG_APP, "UnregisterDeviceMonitor Failed, %{public}d", errorCode);
6. napi_create_double(env, errorCode, &result);
7. return result;
8. }
9. OH_LOG_INFO(LOG_APP, "UnregisterDeviceMonitor Success");
10. napi_create_double(env, 0, &result);
11. return result;
12. }
```

### 查询所有在线设备

调用OH\_GameDevice\_GetAllDeviceInfos接口，查询所有在线游戏设备的信息。

```
1. GameController_ErrorCode DeviceApi::DoQueryAllDeviceInfos() {
2. GameDevice_AllDeviceInfos *gameDevice_AllDeviceInfos;
3. // 查询所有在线设备
4. GameController_ErrorCode errorCode = OH_GameDevice_GetAllDeviceInfos(&gameDevice_AllDeviceInfos);
5. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
6. OH_LOG_ERROR(LOG_APP, "GetAllDeviceInfos Failed, %{public}d", errorCode);
7. return errorCode;
8. }
9. // 依次获取设备信息
10. int count;
11. OH_GameDevice_AllDeviceInfos_GetCount(gameDevice_AllDeviceInfos, &count);
12. Log::GetInstance()->PrintLog("GetAllDeviceInfos Success, the count is " + std::to_string(count));
13. for (int idx = 0; idx < count; idx++) {
14. GameDevice_DeviceInfo *deviceInfo;
15. errorCode = OH_GameDevice_AllDeviceInfos_GetDeviceInfo(gameDevice_AllDeviceInfos, idx, &deviceInfo);
16. if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
17. OH_LOG_ERROR(LOG_APP, "OH_GameDevice_AllDeviceInfos_GetDeviceInfo Failed, %{public}d", errorCode);
18. return errorCode;
19. }
20. std::string temp = GetDeviceInfoStringForPrint(deviceInfo);
21. Log::GetInstance()->PrintLog("AllDeviceInfos[" + std::to_string(idx) + "]" + temp);
22. OH_LOG_INFO(LOG_APP, "AllDeviceInfos[%{public}d] DeviceInfo: %{public}s", idx, temp.c_str());
23. OH_GameDevice_DestroyDeviceInfo(&deviceInfo);
24. }
25. // 销毁指向设备查询结果的指针
26. OH_GameDevice_DestroyAllDeviceInfos(&gameDevice_AllDeviceInfos);
27. OH_LOG_INFO(LOG_APP, "GetAllDeviceInfos Success");
28. return errorCode;
29. }

31. std::string DeviceApi::GetDeviceInfoStringForPrint(GameDevice_DeviceInfo *deviceInfo) {
32. std::string log;
33. char *deviceId = NULL;
34. OH_GameDevice_DeviceInfo_GetDeviceId(deviceInfo, &deviceId);
35. log.append("deviceId:").append(deviceId);
36. free(deviceId);
37. char *name = NULL;
38. OH_GameDevice_DeviceInfo_GetName(deviceInfo, &name);
39. log.append(",name:").append(name);
40. free(name);
41. int product;
42. OH_GameDevice_DeviceInfo_GetProduct(deviceInfo, &product);
43. log.append(",product:").append(std::to_string(product));
44. int version;
45. OH_GameDevice_DeviceInfo_GetVersion(deviceInfo, &version);
46. log.append(",version:").append(std::to_string(version));
47. char *physicalAddress = NULL;
48. OH_GameDevice_DeviceInfo_GetPhysicalAddress(deviceInfo, &physicalAddress);
49. log.append(",physicalAddress:").append(physicalAddress);
50. free(physicalAddress);
51. GameDevice_DeviceType type;
52. OH_GameDevice_DeviceInfo_GetDeviceType(deviceInfo, &type);
53. log.append(",type:").append(std::to_string(type));
54. return log;
55. }
```
