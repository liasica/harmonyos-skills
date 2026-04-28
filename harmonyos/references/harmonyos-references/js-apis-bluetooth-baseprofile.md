---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-baseprofile
title: @ohos.bluetooth.baseProfile (蓝牙baseProfile模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.baseProfile (蓝牙baseProfile模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bf6f36a0e75bc6bf94102b08a4338198a77e8218403edf68153a0551ee8a54ea
---

本模块提供不同的蓝牙技术协议的基础公共方法。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { baseProfile } from '@kit.ConnectivityKit';
```

## BaseProfile

PhonePC/2in1TabletTVWearable

基础Profile接口定义，提供订阅和获取连接状态等公共能力。如：[A2dpSourceProfile](js-apis-bluetooth-a2dp.md#a2dpsourceprofile)、[HandsFreeAudioGatewayProfile](js-apis-bluetooth-hfp.md#handsfreeaudiogatewayprofile)等[Profile](../harmonyos-guides/terminology.md#profile)类型都继承于该类。

## ProfileConnectionState

PhonePC/2in1TabletTVWearable

type ProfileConnectionState = constant.ProfileConnectionState

本端和对端蓝牙设备间的Profile连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 本端和对端蓝牙设备间的Profile连接状态。 |

## StateChangeParam

PhonePC/2in1TabletTVWearable

本端和对端蓝牙设备间Profile连接状态变化参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | [ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 否 | 否 | Profile连接状态。 |
| cause12+ | [DisconnectCause](js-apis-bluetooth-baseprofile.md#disconnectcause12) | 否 | 否 | Profile断开连接的原因。 |

## DisconnectCause12+

PhonePC/2in1TabletTVWearable

枚举，Profile断开连接的原因。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_DISCONNECT | 0 | 用户主动断开连接。 |
| CONNECT\_FROM\_KEYBOARD | 1 | 连接请求需从键盘侧发起。 |
| CONNECT\_FROM\_MOUSE | 2 | 连接请求需从鼠标侧发起。 |
| CONNECT\_FROM\_CAR | 3 | 连接请求需从车机侧发起。 |
| TOO\_MANY\_CONNECTED\_DEVICES | 4 | 当前连接数量超过上限。 |
| CONNECT\_FAIL\_INTERNAL | 5 | 内部错误。 |

## BaseProfile.getConnectedDevices

PhonePC/2in1TabletTVWearable

getConnectedDevices(): Array<string>

获取和本端设备间已连接Profile的对端设备列表。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { a2dp } from '@kit.ConnectivityKit';

4. try {
5. let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
6. let retArray = a2dpSrc.getConnectedDevices();
7. } catch (err) {
8. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
9. }
```

## BaseProfile.getConnectionState

PhonePC/2in1TabletTVWearable

getConnectionState(deviceId: string): ProfileConnectionState

获取和对端设备间Profile的连接状态。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile连接状态。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

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

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { a2dp } from '@kit.ConnectivityKit';

4. try {
5. let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
6. let ret = a2dpSrc.getConnectionState('XX:XX:XX:XX:XX:XX');
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## BaseProfile.on('connectionStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<StateChangeParam>): void

订阅Profile的连接状态变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示Profile连接状态变化事件。  当Profile连接状态变化时，触发该事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)> | 是 | 指定订阅的回调函数，会携带Profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { a2dp } from '@kit.ConnectivityKit';

4. function onReceiveEvent(data: baseProfile.StateChangeParam) {
5. console.info('a2dp state = '+ JSON.stringify(data));
6. }
7. try {
8. let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
9. a2dpSrc.on('connectionStateChange', onReceiveEvent);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## BaseProfile.off('connectionStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)>): void

取消订阅Profile的连接状态变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示Profile连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[BaseProfile.on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { a2dp } from '@kit.ConnectivityKit';

4. function onReceiveEvent(data: baseProfile.StateChangeParam) {
5. console.info('a2dp state = '+ JSON.stringify(data));
6. }
7. try {
8. let a2dpSrc = a2dp.createA2dpSrcProfile(); // 以a2dp举例
9. a2dpSrc.on('connectionStateChange', onReceiveEvent);
10. a2dpSrc.off('connectionStateChange', onReceiveEvent);
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```
