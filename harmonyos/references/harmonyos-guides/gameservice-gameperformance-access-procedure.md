---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameperformance-access-procedure
title: 开发指导(ArkTS)
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 游戏场景感知（可选） > 开发指导(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:55+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:28c8e99f415f1463ad28d240da527cc9cce8a7be9f9b6f3a050ab454dc824133
---

游戏场景感知包括：

* Game Service Kit通过游戏提供的精细化场景信息、配置信息和网络信息等数据，以及当前负载情况使用不同策略优化系统资源调度。
* Game Service Kit通过感知游戏设备的系统状态信息（包括温度变化趋势数据、GPU性能信息等），并将其反馈给游戏应用，游戏应用可以基于当前设备状态自行调整游戏设置等内容，在系统资源有限的情况下优化玩家的游戏体验。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/N_9u2xgZSN-luE1LNAAxcw/zh-cn_image_0000002736314025.png)

1. 游戏启动后调用[gamePerformance.init](../harmonyos-references/gameservice-gameperformance.md#gameperformanceinit)接口对游戏场景感知进行初始化。
2. 初始化成功后，游戏调用[gamePerformance.on](../harmonyos-references/gameservice-gameperformance.md#gameperformanceondevicestatechanged)接口注册设备状态变化事件监听，订阅设备状态变化通知。
3. 游戏调用[gamePerformance.updateGameInfo](../harmonyos-references/gameservice-gameperformance.md#gameperformanceupdategameinfo)接口向游戏场景感知上报游戏信息（包信息、配置信息、场景信息和网络信息等）。
4. 游戏场景感知广播游戏信息给终端系统。
5. 终端系统根据游戏信息进行系统资源调度。
6. 终端系统会将设备状态变化通知游戏场景感知。
7. 游戏场景感知向游戏客户端反馈设备状态变化。
8. 如不再需要订阅，游戏可调用[gamePerformance.off](../harmonyos-references/gameservice-gameperformance.md#gameperformanceoffdevicestatechanged)接口取消设备状态变化事件监听。
9. 游戏调用[gamePerformance.getDeviceInfoByScope](../harmonyos-references/gameservice-gameperformance.md#gameperformancegetdeviceinfobyscope)接口向游戏场景感知主动查询设备状态信息。

**说明** 

Mali系列GPU不支持采集GPU性能信息，调用订阅和查询设备状态信息接口时无法获取设备GPU性能信息。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-gameperformance.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/gameservice-gameperformance.md#gameperformanceinit)(gamePackageInfo: GamePackageInfo): Promise<void> | 游戏初始化接口，对游戏场景感知进行初始化，通过Promise对象获取返回值。 |
| [on](../harmonyos-references/gameservice-gameperformance.md#gameperformanceondevicestatechanged)(type: 'deviceStateChanged', callback: Callback<DeviceInfo>): void | 订阅设备状态变化接口，主要用于监听deviceStateChanged（设备状态变化）事件。 |
| [on](../harmonyos-references/gameservice-gameperformance.md#gameperformanceondevicestatechanged-1)(type: 'deviceStateChanged', callback: Callback<DeviceInfo>, scope: Array<DeviceInfoType>): void | 按需订阅设备状态变化接口。主要用于监听deviceStateChanged（设备状态变化）事件，支持传入参数指定订阅的设备状态信息类型。 |
| [updateGameInfo](../harmonyos-references/gameservice-gameperformance.md#gameperformanceupdategameinfo)<T extends BaseGameInfo>(gameInfo: T): Promise<void> | 更新游戏信息接口，主要用于上报游戏信息（包信息、配置信息、场景信息和网络信息等），通过Promise对象获取返回值。 |
| [off](../harmonyos-references/gameservice-gameperformance.md#gameperformanceoffdevicestatechanged)(type: 'deviceStateChanged', callback?: Callback<DeviceInfo>): void | 取消订阅设备状态变化接口，主要用于取消监听deviceStateChanged（设备状态变化）事件。 |
| [getDeviceInfoByScope](../harmonyos-references/gameservice-gameperformance.md#gameperformancegetdeviceinfobyscope)(scope: Array<DeviceInfoParameter>): Promise<DeviceInfo> | 查询设备状态信息接口。 |

## 接入步骤

### 导入模块

导入Game Service Kit及公共模块。

```typescript
import { gamePerformance } from '@kit.GameServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
```

### 初始化

导入相关模块后，需先调用[init](../harmonyos-references/gameservice-gameperformance.md#gameperformanceinit)接口对游戏场景感知进行初始化。

**说明** 

init接口是调用其他接口的前提，如果未初始化或初始化失败，将无法调用其他接口。

```typescript
let gamePackageInfo: gamePerformance.GamePackageInfo = {
  messageType: 0,
  bundleName: 'com.example.demo', // 请替换为实际的游戏包名
  appVersion: '1.0'
};
try {
  gamePerformance.init(gamePackageInfo).then(() => {
    // 初始化成功
    hilog.info(0x0001, 'demo', `Succeeded in initializing.`);
  });
} catch (error) {
  // 初始化失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to initialize. Code: ${err.code}, message: ${err.message}`);
}
```

### 订阅设备状态变化

调用[on](../harmonyos-references/gameservice-gameperformance.md#gameperformanceondevicestatechanged)接口可以订阅设备状态变化事件，获取设备状态变化的通知（如设备温控档位）。

```typescript
function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // 设备信息详情
  hilog.info(0x0001, 'demo', `device state changed. tempLevel is ${data.tempLevel}`);
}

// 订阅deviceStateChanged事件
try {
  gamePerformance.on('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // 订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to subscribe. Code: ${err.code}, message: ${err.message}`);
}
```

目前支持订阅GPU和温度变化趋势两种类型的设备状态数据，也可以调用[on](../harmonyos-references/gameservice-gameperformance.md#gameperformanceondevicestatechanged-1)接口按需订阅，如只订阅GPU数据：

```typescript
function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // data中仅含有gpuInfo
  hilog.info(0x0001, 'demo', `device state changed. tempLevel is ${data.tempLevel}`);
}

// 订阅deviceStateChanged事件
try {
  let types:Array<gamePerformance.DeviceInfoType> = [gamePerformance.DeviceInfoType.GPU];
  gamePerformance.on('deviceStateChanged', onDeviceStateChange, types);
} catch (error) {
  // 订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to subscribe. Code: ${err.code}, message: ${err.message}`);
}
```

### 上报游戏信息

初始化成功后，可以通过调用[updateGameInfo](../harmonyos-references/gameservice-gameperformance.md#gameperformanceupdategameinfo)接口上报游戏信息（包信息、配置信息、场景信息和网络信息等）。若需上报自定义数据，可调用[addGameCustomData](../harmonyos-references/gameservice-gameperformance.md#gameperformanceaddgamecustomdata)接口。

```typescript
// 以更新游戏场景信息为例
let gameSceneInfo: gamePerformance.GameSceneInfo = {
  messageType: 2,
  sceneID: 7,
  importanceLevel: 4
};
try {
  gamePerformance.updateGameInfo(gameSceneInfo).then(() => {
    // 更新游戏场景信息成功
    hilog.info(0x0001, 'demo', `Succeeded in updating.`);
  });
} catch (error) {
  // 更新游戏场景信息失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to update. Code: ${err.code}, message: ${err.message}`);
}
```

### 取消订阅设备状态

如不再需要订阅，则可以通过调用[off](../harmonyos-references/gameservice-gameperformance.md#gameperformanceoffdevicestatechanged)接口取消订阅设备状态。

```typescript
function onDeviceStateChange(data:gamePerformance.DeviceInfo) {
  // 设备信息详情
  hilog.info(0x0001, 'demo', `device state changed. tempLevel is ${data.tempLevel}`);
}

// 取消订阅deviceStateChanged事件
try {
  gamePerformance.off('deviceStateChanged', onDeviceStateChange);
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to unsubscribe. Code: ${err.code}, message: ${err.message}`);
}

// 取消deviceStateChanged事件的全部订阅
try {
  gamePerformance.off('deviceStateChanged');
} catch (error) {
  // 取消订阅失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to unsubscribe. Code: ${err.code}, message: ${err.message}`);
}
```

### 查询设备状态信息

除订阅设备状态变化的方式外，也可以通过调用[getDeviceInfoByScope](../harmonyos-references/gameservice-gameperformance.md#gameperformancegetdeviceinfobyscope)接口主动查询设备状态：

```typescript
// 查询设备状态
try {
  let gpuParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.GPU
  };
  let thermalParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.THERMAL
  };
  let gameInfos: Array<gamePerformance.DeviceInfoParameter> = [gpuParam, thermalParam];
  gamePerformance.getDeviceInfoByScope(gameInfos).then((deviceInfo:gamePerformance.DeviceInfo) => {
    hilog.info(0x0001, 'demo', `Succeeded in querying device info. tempLevel is ${deviceInfo.tempLevel}`);
  });
} catch (error) {
  // 查询失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to query. Code: ${err.code}, message: ${err.message}`);
}
```

主动查询接口同样支持按需查询，如只查询温度变化趋势数据：

```typescript
// 只查询设备温度数据
try {
  let thermalParam: gamePerformance.DeviceInfoParameter = {
    deviceInfoType: gamePerformance.DeviceInfoType.THERMAL
  };
  let gameInfos: Array<gamePerformance.DeviceInfoParameter> = [thermalParam];
  gamePerformance.getDeviceInfoByScope(gameInfos).then((deviceInfo:gamePerformance.DeviceInfo) => {
    // 此处的查询结果中将不含有gpuInfo
    hilog.info(0x0001, 'demo', `Succeeded in querying device info. tempLevel is ${deviceInfo.tempLevel}`);
  });
} catch (error) {
  // 查询失败
  let err = error as BusinessError;
  hilog.error(0x0001, 'demo', `Failed to query. Code: ${err.code}, message: ${err.message}`);
}
```

**说明** 

查询温度变化趋势需要历史数据作为计算依据，调用该接口时请保证设备已启动至少一分钟，否则会返回1010300003错误。
