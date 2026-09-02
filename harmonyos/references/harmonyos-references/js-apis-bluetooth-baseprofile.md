---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile
title: "@ohos.bluetooth.baseProfile (蓝牙baseProfile模块)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.baseProfile (蓝牙baseProfile模块)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:28e1a3e7e42d550fede11acd186caaa50a2994f1e078d97bfdd15ef4166f36e6
---

本模块提供不同的蓝牙技术协议的基础公共方法，为[A2DP](../harmonyos-guides/terminology.md#a2dp)、[HFP](../harmonyos-guides/terminology.md#hfp)、[PAN](../harmonyos-guides/terminology.md#pan)等蓝牙[Profile](../harmonyos-guides/terminology.md#profile)提供连接状态查询、连接状态订阅与取消订阅等公共能力，适用于需要在应用中统一管理多种蓝牙Profile连接状态的场景。

**说明** 

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { baseProfile } from '@kit.ConnectivityKit';
```

## BaseProfile

基础Profile接口定义，提供订阅和获取连接状态等公共能力。如：[A2dpSourceProfile](js-apis-bluetooth-a2dp.md#a2dpsourceprofile)、[HandsFreeAudioGatewayProfile](js-apis-bluetooth-hfp.md#handsfreeaudiogatewayprofile)等Profile类型都继承于该类。

## ProfileConnectionState

type ProfileConnectionState = constant.ProfileConnectionState

本端和对端蓝牙设备间的Profile连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 类型 | 说明 |
| --- | --- |
| [constant.ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 本端和对端蓝牙设备间的Profile连接状态。 |

## StateChangeParam

本端和对端蓝牙设备间Profile连接状态变化参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | [ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 否 | 否 | Profile连接状态。 |
| cause12+ | [DisconnectCause](js-apis-bluetooth-baseprofile.md#disconnectcause12) | 否 | 否 | Profile断开连接的原因。 |
| role | [PanRole](js-apis-bluetooth-baseprofile.md#panrole) | 否 | 是 | 当前对端设备对应的[PAN](../harmonyos-guides/terminology.md#pan)角色。仅PAN Profile连接状态发生变化时返回该字段，非PAN场景下该字段不存在。  **起始版本**：26.0.0 |

## DisconnectCause12+

枚举，Profile断开连接的原因。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_DISCONNECT | 0 | 用户主动断开连接。 |
| CONNECT\_FROM\_KEYBOARD | 1 | 连接请求需从键盘侧发起。 |
| CONNECT\_FROM\_MOUSE | 2 | 连接请求需从鼠标侧发起。 |
| CONNECT\_FROM\_CAR | 3 | 连接请求需从车机侧发起。 |
| TOO\_MANY\_CONNECTED\_DEVICES | 4 | 当前连接数量超过上限。 |
| CONNECT\_FAIL\_INTERNAL | 5 | 内部错误。 |

## PanRole

枚举，PAN的不同角色。

**起始版本**：26.0.0

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ROLE\_PANNAP | 0 | [NAP](../harmonyos-guides/terminology.md#nap)角色。 |
| ROLE\_PANU | 1 | [PANU](../harmonyos-guides/terminology.md#panu)角色。 |

## BaseProfile.getConnectedDevices

getConnectedDevices(): Array<string>

获取和本端设备间已连接Profile的对端设备列表。例如，在蓝牙音频播放应用中，可通过该方法获取当前已连接的A2DP音频设备列表以进行设备展示或管理。

**需要权限**：

* API版本26.0.0+：ohos.permission.ACCESS\_BLUETOOTH 或 (ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.GET\_BLUETOOTH\_PEERS\_MAC)
* API版本10-24：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回已连接Profile的对端设备列表。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 已配对的地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例**：

```js
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    let retArray = a2dpSrc.getConnectedDevices();
} catch (err) {
    console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
}
```

## BaseProfile.getConnectionState

getConnectionState(deviceId: string): ProfileConnectionState

获取和对端设备间Profile的连接状态。例如，在蓝牙应用中判断设备是否已连接，以决定是否可以发起数据传输或更新设备连接状态显示。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile连接状态。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 返回Profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例**：

```js
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    let ret = a2dpSrc.getConnectionState('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## BaseProfile.on('connectionStateChange')

on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void

订阅Profile的连接状态变化事件。使用Callback异步回调。例如，在蓝牙音频应用中，当耳机连接或断开时实时更新播放界面状态或提示用户。

**需要权限**：

* API版本26.0.0+：ohos.permission.ACCESS\_BLUETOOTH 或 (ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.GET\_BLUETOOTH\_PEERS\_MAC)
* API版本10-24：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示Profile连接状态变化事件。  当Profile连接状态变化时，触发该事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)> | 是 | 指定订阅的回调函数，会携带Profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.  适用版本：10-24 |
| 801 | Capability not supported. |

**示例**：

```js
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

function onReceiveEvent(data: baseProfile.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    a2dpSrc.on('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

## BaseProfile.off('connectionStateChange')

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)>): void

取消订阅Profile的连接状态变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示Profile连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)> | 否 | 指定取消订阅的回调函数。  若传参，则需与[BaseProfile.on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)中的回调函数一致，此时取消订阅该回调函数；若传入的回调与已订阅的回调不一致，则无法取消对应订阅；若无传参，则取消订阅该type对应的所有回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例**：

```js
import { BusinessError } from '@kit.BasicServicesKit';
import { a2dp } from '@kit.ConnectivityKit';

function onReceiveEvent(data: baseProfile.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
try {
    let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
    a2dpSrc.on('connectionStateChange', onReceiveEvent);
    a2dpSrc.off('connectionStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
