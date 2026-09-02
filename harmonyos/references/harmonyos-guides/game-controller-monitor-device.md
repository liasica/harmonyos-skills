---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/game-controller-monitor-device
title: 监听设备上下线（C/C++）
breadcrumb: 指南 > 应用服务 > Game Controller Kit（游戏控制器服务） > 监听设备上下线（C/C++）
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:55+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:49863123ccc6615762448945f3e0da96ff8ed05a0354f69078b79812aacf4cea
---

## 功能介绍

Game Controller Kit提供设备上下线事件监听和查询在线设备信息的功能。注册监听事件后，设备拔插时可获取实时回调通知，同时支持查询当前所有在线设备的具体信息。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Z26Xv29FQ_egBDXhqg14-A/zh-cn_image_0000002736434053.png)

1. 玩家启动游戏。
2. 游戏调用[OH\_GameDevice\_RegisterDeviceMonitor](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_registerdevicemonitor)接口注册设备状态变化事件监听。
3. 玩家插拔设备。
4. 终端系统将设备状态变化通知Game Controller Kit。
5. Game Controller Kit向游戏反馈设备状态变化。
6. 游戏调用[OH\_GameDevice\_GetAllDeviceInfos](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_getalldeviceinfos)接口向Game Controller Kit查询所有在线的游戏设备信息。
7. Game Controller Kit从终端系统获取所有在线的游戏设备信息。
8. 如果不再需要订阅，游戏可以调用[OH\_GameDevice\_UnregisterDeviceMonitor](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_unregisterdevicemonitor)接口取消设备状态变化事件监听。

## 接口说明

接口详细介绍请参考[GameController](../harmonyos-references/capi-gamecontroller.md)。

| 接口名 | 描述 |
| --- | --- |
| GameController\_ErrorCode [OH\_GameDevice\_RegisterDeviceMonitor](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_registerdevicemonitor) (GameDevice\_DeviceMonitorCallback deviceMonitorCallback) | 注册设备状态变化事件的监听回调。 |
| GameController\_ErrorCode [OH\_GameDevice\_UnregisterDeviceMonitor](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_unregisterdevicemonitor) (void) | 取消注册设备状态变化事件的监听回调。 |
| GameController\_ErrorCode [OH\_GameDevice\_GetAllDeviceInfos](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_getalldeviceinfos) (GameDevice\_AllDeviceInfos \*\*allDeviceInfos) | 获取所有在线设备的信息。 |

## 开发步骤

### 链接动态库

```c
target_link_libraries(entry PUBLIC libohgame_controller.z.so)
```

### 导入模块

```c
#include <GameControllerKit/game_device.h>
```

### 注册设备上下线监听

调用[OH\_GameDevice\_RegisterDeviceMonitor](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_registerdevicemonitor)接口注册设备状态变化监听，获取设备上下线的回调通知。

```c
napi_value DeviceApi::RegisterDeviceMonitor(napi_env env, napi_callback_info info) {
    napi_value result;
    GameController_ErrorCode errorCode = OH_GameDevice_RegisterDeviceMonitor(DeviceApi::OnDeviceChanged);
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "RegisterDeviceMonitor Failed, %{public}d", errorCode);
        napi_create_double(env, errorCode, &result);
        return result;
    }
    OH_LOG_INFO(LOG_APP, "RegisterDeviceMonitor Success");
    napi_create_double(env, 0, &result);
    return result;
}

void DeviceApi::OnDeviceChanged(const struct GameDevice_DeviceEvent *deviceEvent) {
    GameDevice_StatusChangedType type;
    OH_GameDevice_DeviceEvent_GetChangedType(deviceEvent, &type);
    GameDevice_DeviceInfo *deviceInfo;
    OH_GameDevice_DeviceEvent_GetDeviceInfo(deviceEvent, &deviceInfo);
    std::string temp = GetDeviceInfoStringForPrint(deviceInfo);
    Log::GetInstance()->PrintLog("OnDeviceChanged type[" + std::to_string(type) + "] DeviceInfo" + temp);
    OH_LOG_INFO(LOG_APP, "OnDeviceChanged type:%{public}d DeviceInfo:%{public}s", type, temp.c_str());
    OH_GameDevice_DestroyDeviceInfo(&deviceInfo);
}
```

### 取消注册设备上下线监听

如果不再需要订阅，可以调用[OH\_GameDevice\_UnregisterDeviceMonitor](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_unregisterdevicemonitor)接口取消设备状态变化事件的监听。

```c
napi_value DeviceApi::UnregisterDeviceMonitor(napi_env env, napi_callback_info info) {
    napi_value result;
    GameController_ErrorCode errorCode = OH_GameDevice_UnregisterDeviceMonitor();
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "UnregisterDeviceMonitor Failed, %{public}d", errorCode);
        napi_create_double(env, errorCode, &result);
        return result;
    }
    OH_LOG_INFO(LOG_APP, "UnregisterDeviceMonitor Success");
    napi_create_double(env, 0, &result);
    return result;
}
```

### 查询所有在线设备

调用[OH\_GameDevice\_GetAllDeviceInfos](../harmonyos-references/capi-game-device-h.md#oh_gamedevice_getalldeviceinfos)接口，查询所有在线游戏设备的信息。

```c
GameController_ErrorCode DeviceApi::DoQueryAllDeviceInfos() {
    GameDevice_AllDeviceInfos *gameDevice_AllDeviceInfos;
    // 查询所有在线设备
    GameController_ErrorCode errorCode = OH_GameDevice_GetAllDeviceInfos(&gameDevice_AllDeviceInfos);
    if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
        OH_LOG_ERROR(LOG_APP, "GetAllDeviceInfos Failed, %{public}d", errorCode);
        return errorCode;
    }
    // 依次获取设备信息
    int count;
    OH_GameDevice_AllDeviceInfos_GetCount(gameDevice_AllDeviceInfos, &count);
    Log::GetInstance()->PrintLog("GetAllDeviceInfos Success, the count is " + std::to_string(count));
    for (int idx = 0; idx < count; idx++) {
        GameDevice_DeviceInfo *deviceInfo;
        errorCode = OH_GameDevice_AllDeviceInfos_GetDeviceInfo(gameDevice_AllDeviceInfos, idx, &deviceInfo);
        if (errorCode != GameController_ErrorCode::GAME_CONTROLLER_SUCCESS) {
            OH_LOG_ERROR(LOG_APP, "OH_GameDevice_AllDeviceInfos_GetDeviceInfo Failed, %{public}d", errorCode);
            return errorCode;
        }
        std::string temp = GetDeviceInfoStringForPrint(deviceInfo);
        Log::GetInstance()->PrintLog("AllDeviceInfos[" + std::to_string(idx) + "]" + temp);
        OH_LOG_INFO(LOG_APP, "AllDeviceInfos[%{public}d] DeviceInfo: %{public}s", idx, temp.c_str());
        OH_GameDevice_DestroyDeviceInfo(&deviceInfo);
    }
    // 销毁指向设备查询结果的指针
    OH_GameDevice_DestroyAllDeviceInfos(&gameDevice_AllDeviceInfos);
    OH_LOG_INFO(LOG_APP, "GetAllDeviceInfos Success");
    return errorCode;
}

std::string DeviceApi::GetDeviceInfoStringForPrint(GameDevice_DeviceInfo *deviceInfo) {
    std::string log;
    char *deviceId = NULL;
    OH_GameDevice_DeviceInfo_GetDeviceId(deviceInfo, &deviceId);
    log.append("deviceId:").append(deviceId);
    free(deviceId);
    char *name = NULL;
    OH_GameDevice_DeviceInfo_GetName(deviceInfo, &name);
    log.append(",name:").append(name);
    free(name);
    int product;
    OH_GameDevice_DeviceInfo_GetProduct(deviceInfo, &product);
    log.append(",product:").append(std::to_string(product));
    int version;
    OH_GameDevice_DeviceInfo_GetVersion(deviceInfo, &version);
    log.append(",version:").append(std::to_string(version));
    char *physicalAddress = NULL;
    OH_GameDevice_DeviceInfo_GetPhysicalAddress(deviceInfo, &physicalAddress);
    log.append(",physicalAddress:").append(physicalAddress);
    free(physicalAddress);
    GameDevice_DeviceType type;
    OH_GameDevice_DeviceInfo_GetDeviceType(deviceInfo, &type);
    log.append(",type:").append(std::to_string(type));
    return log;
}
```
