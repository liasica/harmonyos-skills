---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth
title: "@ohos.bluetooth (蓝牙)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 已停止维护的接口 > @ohos.bluetooth (蓝牙)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6c16c8018ca9d32d554b61130a764d2c65cb40bf2a8d7385356c7887e944ca8a
---

蓝牙模块提供了基础的传统蓝牙能力以及[BLE](../harmonyos-guides/terminology.md#ble)的扫描、广播等功能。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 9 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble (蓝牙ble模块)](js-apis-bluetooth-ble.md)等相关Profile接口。

## 导入模块

```js
import bluetooth from '@ohos.bluetooth';
```

## bluetooth.enableBluetooth(deprecated)

enableBluetooth(): boolean

开启蓝牙。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.enableBluetooth](js-apis-bluetoothmanager.md#bluetoothmanagerenablebluetoothdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 打开蓝牙，成功返回true，否则返回false。 |

**示例：**

```js
let enable : boolean = bluetooth.enableBluetooth();
```

## bluetooth.disableBluetooth(deprecated)

disableBluetooth(): boolean

关闭蓝牙。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.disableBluetooth](js-apis-bluetoothmanager.md#bluetoothmanagerdisablebluetoothdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 关闭蓝牙，成功返回true，否则返回false。 |

**示例：**

```js
let disable : boolean = bluetooth.disableBluetooth();
```

## bluetooth.getLocalName(deprecated)

getLocalName(): string

获取蓝牙本地设备名称。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getLocalName](js-apis-bluetoothmanager.md#bluetoothmanagergetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 蓝牙本地设备名称。 |

**示例：**

```js
let localName : string = bluetooth.getLocalName();
```

## bluetooth.getState(deprecated)

getState(): BluetoothState

获取蓝牙开关状态。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getState](js-apis-bluetoothmanager.md#bluetoothmanagergetstatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothState](js-apis-bluetooth.md#bluetoothstatedeprecated) | 表示蓝牙开关状态。 |

**示例：**

```js
let state : bluetooth.BluetoothState = bluetooth.getState();
```

## bluetooth.getBtConnectionState(deprecated)

getBtConnectionState(): ProfileConnectionState

获取蓝牙本端的Profile连接状态，例如：任意一个支持的Profile连接状态为已连接，则此接口返回状态为已连接。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getBtConnectionState](js-apis-bluetoothmanager.md#bluetoothmanagergetbtconnectionstatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth.md#profileconnectionstatedeprecated) | 表示蓝牙设备的Profile连接状态。 |

**示例：**

```js
let connectionState : bluetooth.ProfileConnectionState = bluetooth.getBtConnectionState();
```

## bluetooth.setLocalName(deprecated)

setLocalName(name: string): boolean

设置蓝牙本地设备名称。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.setLocalName](js-apis-bluetoothmanager.md#bluetoothmanagersetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要设置的蓝牙名称，最大长度为248字节数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设置蓝牙本地设备名称，成功返回true，否则返回false。 |

**示例：**

```js
let ret : boolean = bluetooth.setLocalName('device_name');
```

## bluetooth.pairDevice(deprecated)

pairDevice(deviceId: string): boolean

发起蓝牙配对。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.pairDevice](js-apis-bluetoothmanager.md#bluetoothmanagerpairdevicedeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 发起蓝牙配对，成功返回true，否则返回false。 |

**示例：**

```js
// 实际的地址可由扫描流程获取
let result : boolean = bluetooth.pairDevice("XX:XX:XX:XX:XX:XX");
```

## bluetooth.getProfileConnState(deprecated)

getProfileConnState(profileId: ProfileId): ProfileConnectionState

依据ProfileId获取指定profile的连接状态。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getProfileConnectionState](js-apis-bluetoothmanager.md#bluetoothmanagergetprofileconnectionstatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | ProfileId | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth.md#profileconnectionstatedeprecated) | profile的连接状态。 |

**示例：**

```js
let result : bluetooth.ProfileConnectionState = bluetooth.getProfileConnState(bluetooth.ProfileId.PROFILE_A2DP_SOURCE);
```

## bluetooth.getRemoteDeviceName(deprecated)

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getRemoteDeviceName](js-apis-bluetoothmanager.md#bluetoothmanagergetremotedevicenamedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串格式返回设备名称。 |

**示例：**

```js
let remoteDeviceName : string = bluetooth.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
```

## bluetooth.getRemoteDeviceClass(deprecated)

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getRemoteDeviceClass](js-apis-bluetoothmanager.md#bluetoothmanagergetremotedeviceclassdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClass](js-apis-bluetooth.md#deviceclassdeprecated) | 远程设备的类别。 |

**示例：**

```js
let remoteDeviceClass : bluetooth.DeviceClass = bluetooth.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
```

## bluetooth.getPairedDevices(deprecated)

getPairedDevices(): Array<string>

获取蓝牙配对列表。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getPairedDevices](js-apis-bluetoothmanager.md#bluetoothmanagergetpaireddevicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 已配对蓝牙设备的地址列表。 |

**示例：**

```js
let devices : Array<string> = bluetooth.getPairedDevices();
```

## bluetooth.setBluetoothScanMode(deprecated)

setBluetoothScanMode(mode: ScanMode, duration: number): boolean

设置蓝牙扫描模式，可以被远端设备发现。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.setBluetoothScanMode](js-apis-bluetoothmanager.md#bluetoothmanagersetbluetoothscanmodedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ScanMode](js-apis-bluetooth.md#scanmodedeprecated) | 是 | 蓝牙扫描模式。 |
| duration | number | 是 | 设备可被发现的持续时间，单位为毫秒；设置为0则持续可发现。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设置蓝牙扫描，成功返回true，否则返回false。 |

**示例：**

```js
// 设置为可连接可发现才可被远端设备扫描到，可以连接。
let result : boolean = bluetooth.setBluetoothScanMode(bluetooth.ScanMode
    .SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
```

## bluetooth.getBluetoothScanMode(deprecated)

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getBluetoothScanMode](js-apis-bluetoothmanager.md#bluetoothmanagergetbluetoothscanmodedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScanMode](js-apis-bluetooth.md#scanmodedeprecated) | 蓝牙扫描模式。 |

**示例：**

```js
let scanMode : bluetooth.ScanMode = bluetooth.getBluetoothScanMode();
```

## bluetooth.startBluetoothDiscovery(deprecated)

startBluetoothDiscovery(): boolean

开启蓝牙扫描，可以发现远端设备。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.startBluetoothDiscovery](js-apis-bluetoothmanager.md#bluetoothmanagerstartbluetoothdiscoverydeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 开启蓝牙扫描，成功返回true，否则返回false。 |

**示例：**

```js
let deviceId : Array<string>;
function onReceiveEvent(data : Array<string>) {
    deviceId = data;
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
let result : boolean = bluetooth.startBluetoothDiscovery();
```

## bluetooth.stopBluetoothDiscovery(deprecated)

stopBluetoothDiscovery(): boolean

关闭蓝牙扫描。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.stopBluetoothDiscovery](js-apis-bluetoothmanager.md#bluetoothmanagerstopbluetoothdiscoverydeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 关闭蓝牙扫描，成功返回true，否则返回false。 |

**示例：**

```js
let result : boolean = bluetooth.stopBluetoothDiscovery();
```

## bluetooth.setDevicePairingConfirmation(deprecated)

setDevicePairingConfirmation(device: string, accept: boolean): boolean

设置设备配对请求确认。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.setDevicePairingConfirmation](js-apis-bluetoothmanager.md#bluetoothmanagersetdevicepairingconfirmationdeprecated)替代。

**需要权限**：ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| accept | boolean | 是 | 接受配对请求设置为true，否则设置为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设置设备配对确认，成功返回true，否则返回false。 |

**示例：**

```js
// 订阅“pinRequired”配对请求事件，收到远端配对请求后设置配对确认
function onReceivePinRequiredEvent(data : bluetooth.PinRequiredParam) { // data为配对请求的入参，配对请求参数
    console.info('pin required  = '+ JSON.stringify(data));
    bluetooth.setDevicePairingConfirmation(data.deviceId, true);
}
bluetooth.on("pinRequired", onReceivePinRequiredEvent);
```

## bluetooth.on('bluetoothDeviceFind')(deprecated)

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备发现上报事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('bluetoothDeviceFind')](js-apis-bluetoothmanager.md#bluetoothmanageronbluetoothdevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<string>) { // data为蓝牙设备地址集合
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
```

## bluetooth.off('bluetoothDeviceFind')(deprecated)

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备发现上报事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('bluetoothDeviceFind')](js-apis-bluetoothmanager.md#bluetoothmanageroffbluetoothdevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 否 | 表示取消订阅蓝牙设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
bluetooth.off('bluetoothDeviceFind', onReceiveEvent);
```

## bluetooth.on('pinRequired')(deprecated)

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅远端蓝牙设备的配对请求事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('pinRequired')](js-apis-bluetoothmanager.md#bluetoothmanageronpinrequireddeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](js-apis-bluetooth.md#pinrequiredparamdeprecated)> | 是 | 表示回调函数的入参，配对请求。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.PinRequiredParam) { // data为配对请求参数
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);
```

## bluetooth.off('pinRequired')(deprecated)

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅远端蓝牙设备的配对请求事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('pinRequired')](js-apis-bluetoothmanager.md#bluetoothmanageroffpinrequireddeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](js-apis-bluetooth.md#pinrequiredparamdeprecated)> | 否 | 表示取消订阅蓝牙配对请求事件上报，入参为配对请求参数。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);
bluetooth.off('pinRequired', onReceiveEvent);
```

## bluetooth.on('bondStateChange')(deprecated)

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态改变事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('bondStateChange')](js-apis-bluetoothmanager.md#bluetoothmanageronbondstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](js-apis-bluetooth.md#bondstateparamdeprecated)> | 是 | 表示回调函数的入参，配对的状态。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BondStateParam) { // data为回调函数入参，表示配对的状态
    console.info('pair state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
```

## bluetooth.off('bondStateChange')(deprecated)

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态改变事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('bondStateChange')](js-apis-bluetoothmanager.md#bluetoothmanageroffbondstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](js-apis-bluetooth.md#bondstateparamdeprecated)> | 否 | 表示取消订阅蓝牙配对状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
bluetooth.off('bondStateChange', onReceiveEvent);
```

## bluetooth.on('stateChange')(deprecated)

on(type: 'stateChange', callback: Callback<BluetoothState>): void

订阅蓝牙连接状态改变事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('stateChange')](js-apis-bluetoothmanager.md#bluetoothmanageronstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](js-apis-bluetooth.md#bluetoothstatedeprecated)> | 是 | 表示回调函数的入参，蓝牙状态。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
```

## bluetooth.off('stateChange')(deprecated)

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

取消订阅蓝牙连接状态改变事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('stateChange')](js-apis-bluetoothmanager.md#bluetoothmanageroffstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](js-apis-bluetooth.md#bluetoothstatedeprecated)> | 否 | 表示取消订阅蓝牙状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
bluetooth.off('stateChange', onReceiveEvent);
```

## bluetooth.sppListen(deprecated)

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

创建一个服务端监听Socket。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppListen](js-apis-bluetoothmanager.md#bluetoothmanagerspplistendeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 服务的名称。 |
| option | [SppOption](js-apis-bluetooth.md#sppoptiondeprecated) | 是 | spp监听配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，服务端Socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}

let sppOption : bluetooth.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
bluetooth.sppListen('server1', sppOption, serverSocket);
```

## bluetooth.sppAccept(deprecated)

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

服务端监听socket等待客户端连接。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppAccept](js-apis-bluetoothmanager.md#bluetoothmanagersppacceptdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverSocket | number | 是 | 服务端socket的id。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}
let clientNumber = -1;
function acceptClientSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth clientSocket Number: ${number}`);
    // 获取的clientNumber用作服务端后续读/写操作socket的id。
    clientNumber = number;
  }
}
bluetooth.sppAccept(serverNumber, acceptClientSocket);
```

## bluetooth.sppConnect(deprecated)

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

客户端向远端设备发起spp连接。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppConnect](js-apis-bluetoothmanager.md#bluetoothmanagersppconnectdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| option | [SppOption](js-apis-bluetooth.md#sppoptiondeprecated) | 是 | spp客户端连接配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let sppOption : bluetooth.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
bluetooth.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
```

## bluetooth.sppCloseServerSocket(deprecated)

sppCloseServerSocket(socket: number): void

关闭服务端监听Socket，入参socket由sppListen接口返回。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppCloseServerSocket](js-apis-bluetoothmanager.md#bluetoothmanagersppcloseserversocketdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 服务端监听socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let serverNumber = -1;
function serverSocket(code : BusinessError, number : number) {
  console.info(`bluetooth error code: ${code.code}`);
  if (code.code == 0) {
    console.info(`bluetooth serverSocket Number: ${number}`);
    serverNumber = number;
  }
}
bluetooth.sppCloseServerSocket(serverNumber);
```

## bluetooth.sppCloseClientSocket(deprecated)

sppCloseClientSocket(socket: number): void

关闭客户端socket，入参socket由sppAccept或sppConnect接口获取。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppCloseClientSocket](js-apis-bluetoothmanager.md#bluetoothmanagersppcloseclientsocketdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 客户端socket的id。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
bluetooth.sppCloseClientSocket(clientNumber);
```

## bluetooth.sppWrite(deprecated)

sppWrite(clientSocket: number, data: ArrayBuffer): boolean

通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取 。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.sppWrite](js-apis-bluetoothmanager.md#bluetoothmanagersppwritedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端socket的id。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 写数据操作，成功返回true，否则返回false。 |

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
let arrayBuffer = new ArrayBuffer(8);
let data = new Uint8Array(arrayBuffer);
data[0] = 123;
let ret : boolean = bluetooth.sppWrite(clientNumber, arrayBuffer);
if (ret) {
  console.info('spp write successfully');
} else {
  console.error('spp write failed');
}
```

## bluetooth.on('sppRead')(deprecated)

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.on('sppRead')](js-apis-bluetoothmanager.md#bluetoothmanageronsppreaddeprecated)替代。

订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端socket的id。 |
| callback | Callback<ArrayBuffer> | 是 | 表示回调函数的入参，读取到的数据。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
function dataRead(dataBuffer : ArrayBuffer) {
  let data = new Uint8Array(dataBuffer);
}
bluetooth.on('sppRead', clientNumber, dataRead);
```

## bluetooth.off('sppRead')(deprecated)

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

取消订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.off('sppRead')](js-apis-bluetoothmanager.md#bluetoothmanageroffsppreaddeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端Socket的id。 |
| callback | Callback<ArrayBuffer> | 否 | 表示取消订阅spp读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
let clientNumber = -1;
function clientSocket(code : BusinessError, number : number) {
  if (code == null || code.code != 0) {
    return;
  }
  console.info(`bluetooth serverSocket Number: ${number}`);
  // 获取的clientNumber用作客户端后续读/写操作socket的id。
  clientNumber = number;
}
bluetooth.off('sppRead', clientNumber);
```

## bluetooth.getProfile(deprecated)

getProfile(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile

通过ProfileId，获取profile的对象实例。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.getProfileInstance](js-apis-bluetoothmanager.md#bluetoothmanagergetprofileinstancedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | [ProfileId](js-apis-bluetooth.md#profileiddeprecated) | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [A2dpSourceProfile](js-apis-bluetooth.md#a2dpsourceprofile) | [HandsFreeAudioGatewayProfile](js-apis-bluetooth.md#handsfreeaudiogatewayprofile) | 对应的profile的对象实例，当前支持A2dpSourceProfile， HandsFreeAudioGatewayProfile。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
```

## BLE

### createGattServer(deprecated)

createGattServer(): GattServer

创建一个可使用的GattServer实例。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.createGattServer](js-apis-bluetoothmanager.md#creategattserverdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattServer](js-apis-bluetooth.md#gattserver) | server端类，使用server端方法之前需要创建该类的实例进行操作。 |

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
```

### createGattClientDevice(deprecated)

createGattClientDevice(deviceId: string): GattClientDevice

创建一个可使用的GattClientDevice实例。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.createGattClientDevice](js-apis-bluetoothmanager.md#creategattclientdevicedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattClientDevice](js-apis-bluetooth.md#gattclientdevice) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
```

### getConnectedBLEDevices(deprecated)

getConnectedBLEDevices(): Array<string>

获取和当前设备连接的BLE设备。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.getConnectedBLEDevices](js-apis-bluetoothmanager.md#getconnectedbledevicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前设备作为Server端时连接BLE设备地址集合。 |

**示例：**

```js
let result : Array<string> = bluetooth.BLE.getConnectedBLEDevices();
```

### startBLEScan(deprecated)

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

发起BLE扫描流程。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.startBLEScan](js-apis-bluetoothmanager.md#startblescandeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请） 和 ohos.permission.LOCATION

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<[ScanFilter](js-apis-bluetooth.md#scanfilterdeprecated)> | 是 | 表示扫描结果过滤策略集合，如果不使用过滤的方式，该参数设置为null。 |
| options | [ScanOptions](js-apis-bluetooth.md#scanoptionsdeprecated) | 否 | 表示扫描的参数配置，可选参数。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('BLE scan device find result = '+ JSON.stringify(data));
}
bluetooth.BLE.on("BLEDeviceFind", onReceiveEvent);
let scanOptions : bluetooth.ScanOptions = {
    interval: 500,
    dutyMode: bluetooth.ScanDuty.SCAN_MODE_LOW_POWER,
    matchMode: bluetooth.MatchMode.MATCH_MODE_AGGRESSIVE,
}

let scanFilter : bluetooth.ScanFilter = {
    deviceId:"XX:XX:XX:XX:XX:XX",
    name:"test",
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
}
bluetooth.BLE.startBLEScan(
    [scanFilter], scanOptions
);
```

### stopBLEScan(deprecated)

stopBLEScan(): void

停止BLE扫描流程。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.stopBLEScan](js-apis-bluetoothmanager.md#stopblescandeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

无

**示例：**

```js
bluetooth.BLE.stopBLEScan();
```

### on('BLEDeviceFind')(deprecated)

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

订阅BLE设备发现上报事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.on('BLEDeviceFind')](js-apis-bluetoothmanager.md#onbledevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](js-apis-bluetooth.md#scanresultdeprecated)>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
```

### off('BLEDeviceFind')(deprecated)

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

取消订阅BLE设备发现上报事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLE.off('BLEDeviceFind')](js-apis-bluetoothmanager.md#offbledevicefinddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](js-apis-bluetooth.md#scanresultdeprecated)>> | 否 | 表示取消订阅BLE设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
bluetooth.BLE.off('BLEDeviceFind', onReceiveEvent);
```

## BaseProfile

profile基类。

### getConnectionDevices(deprecated)

getConnectionDevices(): Array<string>

获取已连接设备列表。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BaseProfile.getConnectionDevices](js-apis-bluetoothmanager.md#getconnectiondevicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回已连接设备的地址列表。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let retArray : Array<string> = a2dpSrc.getConnectionDevices();
```

### getDeviceState(deprecated)

getDeviceState(device: string): ProfileConnectionState

获取设备profile的连接状态。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BaseProfile.getDeviceState](js-apis-bluetoothmanager.md#getdevicestatedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth.md#profileconnectionstatedeprecated) | 返回profile的连接状态。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : bluetooth.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
```

## A2dpSourceProfile

使用A2dpSourceProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

### connect(deprecated)

connect(device: string): boolean

发起设备的A2dp服务连接请求。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.connect](js-apis-bluetoothmanager.md#connectdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : boolean = a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
```

### disconnect(deprecated)

disconnect(device: string): boolean

断开设备的a2dp服务连接。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.disconnect](js-apis-bluetoothmanager.md#disconnectdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let ret : boolean = a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
```

### on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)>): void

订阅a2dp连接状态变化事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.on('connectionStateChange')](js-apis-bluetoothmanager.md#onconnectionstatechangedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)> | 是 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
```

### off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)>): void

取消订阅a2dp连接状态变化事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.off('connectionStateChange')](js-apis-bluetoothmanager.md#offconnectionstatechangedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)> | 否 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('a2dp state = '+ JSON.stringify(data));
}
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
a2dpSrc.on('connectionStateChange', onReceiveEvent);
a2dpSrc.off('connectionStateChange', onReceiveEvent);
```

### getPlayingState(deprecated)

getPlayingState(device: string): PlayingState

获取设备的播放状态。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.A2dpSourceProfile.getPlayingState](js-apis-bluetoothmanager.md#getplayingstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PlayingState](js-apis-bluetooth.md#playingstatedeprecated) | 远端设备的播放状态。 |

**示例：**

```js
let a2dpSrc : bluetooth.A2dpSourceProfile = bluetooth.getProfile(bluetooth.ProfileId.PROFILE_A2DP_SOURCE) as bluetooth.A2dpSourceProfile;
let state : bluetooth.PlayingState = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
```

## HandsFreeAudioGatewayProfile

使用HandsFreeAudioGatewayProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

### connect(deprecated)

connect(device: string): boolean

连接设备的HFP服务。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.connect](js-apis-bluetoothmanager.md#connectdeprecated-1)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
let ret : boolean = hfpAg.connect('XX:XX:XX:XX:XX:XX');
```

### disconnect(deprecated)

disconnect(device: string): boolean

断开连接设备的HFP服务。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.disconnect](js-apis-bluetoothmanager.md#disconnectdeprecated-1)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 成功返回true，失败返回false。 |

**示例：**

```js
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile = bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
let ret : boolean = hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
```

### on('connectionStateChange')(deprecated)

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)>): void

订阅HFP连接状态变化事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.on('connectionStateChange')](js-apis-bluetoothmanager.md#onconnectionstatechangedeprecated-1)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)> | 是 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
hfpAg.on('connectionStateChange', onReceiveEvent);
```

### off('connectionStateChange')(deprecated)

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)>): void

取消订阅HFP连接状态变化事件。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.HandsFreeAudioGatewayProfile.off('connectionStateChange')](js-apis-bluetoothmanager.md#offconnectionstatechangedeprecated-1)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetooth.md#statechangeparamdeprecated)> | 否 | 表示回调函数的入参。 |

**返回值：**

无

**示例：**

```js
function onReceiveEvent(data : bluetooth.StateChangeParam) {
    console.info('hfp state = '+ JSON.stringify(data));
}
let hfpAg : bluetooth.HandsFreeAudioGatewayProfile= bluetooth.getProfile(bluetooth.ProfileId
    .PROFILE_HANDS_FREE_AUDIO_GATEWAY);
hfpAg.on('connectionStateChange', onReceiveEvent);
hfpAg.off('connectionStateChange', onReceiveEvent);
```

## GattServer

server端类，使用server端方法之前需要创建该类的实例进行操作，通过createGattServer()方法构造此实例。

### startAdvertising(deprecated)

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

开始发送BLE广播。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.startAdvertising](js-apis-bluetoothmanager.md#startadvertisingdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | [AdvertiseSetting](js-apis-bluetooth.md#advertisesettingdeprecated) | 是 | BLE广播的相关参数。 |
| advData | [AdvertiseData](js-apis-bluetooth.md#advertisedatadeprecated) | 是 | BLE广播包内容。 |
| advResponse | [AdvertiseData](js-apis-bluetooth.md#advertisedatadeprecated) | 否 | BLE回复扫描请求回复响应。 |

**返回值：**

无

**示例：**

```js
let manufactureValueBuffer = new Uint8Array(4);
manufactureValueBuffer[0] = 1;
manufactureValueBuffer[1] = 2;
manufactureValueBuffer[2] = 3;
manufactureValueBuffer[3] = 4;

let serviceValueBuffer = new Uint8Array(4);
serviceValueBuffer[0] = 4;
serviceValueBuffer[1] = 6;
serviceValueBuffer[2] = 7;
serviceValueBuffer[3] = 8;
console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let setting : bluetooth.AdvertiseSetting = {
    interval:150,
    txPower:60,
    connectable:true,
}

let manufactureData : bluetooth.ManufactureData = {
    manufactureId:4567,
    manufactureValue:manufactureValueBuffer.buffer
}

let serviceData : bluetooth.ServiceData = {
    serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
    serviceValue:serviceValueBuffer.buffer
}

let advData : bluetooth.AdvertiseData = {
    serviceUuids:["00001889-0000-1000-8000-00805f9b34fb"],
    manufactureData:[manufactureData],
    serviceData:[serviceData],
}

let advResponse : bluetooth.AdvertiseData = {
    serviceUuids:["00001889-0000-1000-8000-00805f9b34fb"],
    manufactureData:[manufactureData],
    serviceData:[serviceData],
}
gattServer.startAdvertising(setting, advData, advResponse);
```

### stopAdvertising(deprecated)

stopAdvertising(): void

停止发送BLE广播。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.stopAdvertising](js-apis-bluetoothmanager.md#stopadvertisingdeprecated)替代。

**需要权限**：ohos.permission.DISCOVER\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

无

**示例：**

```js
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.stopAdvertising();
```

### addService(deprecated)

addService(service: GattService): boolean

server端添加服务。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.addService](js-apis-bluetoothmanager.md#addservicedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | [GattService](js-apis-bluetooth.md#gattservicedeprecated) | 是 | 服务端的service数据。BLE广播的相关参数 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 添加服务操作，成功返回true，否则返回false。 |

**示例：**

```js
// 创建descriptors
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;

// 创建characteristics
let characteristics : Array<bluetooth.BLECharacteristic> = [];
let arrayBufferC = new ArrayBuffer(8);
let cccV = new Uint8Array(arrayBufferC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let characteristicN : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
characteristics[0] = characteristic;

// 创建gattService
let gattService : bluetooth.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.addService(gattService);
if (ret) {
   console.info("add service successfully");
} else {
   console.error("add service failed");
}
```

### removeService(deprecated)

removeService(serviceUuid: string): boolean

删除已添加的服务。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.removeService](js-apis-bluetoothmanager.md#removeservicedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | service的UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 删除服务操作，成功返回true，否则返回false。 |

**示例：**

```js
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.removeService('00001810-0000-1000-8000-00805F9B34FB');
```

### close(deprecated)

close(): void

关闭服务端功能，注销server在协议栈的注册，调用该接口后[GattServer](js-apis-bluetooth.md#gattserver)实例将不能再使用。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.close](js-apis-bluetoothmanager.md#closedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**示例：**

```js
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.close();
```

### notifyCharacteristicChanged(deprecated)

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): boolean

server端特征值发生变化时，主动通知已连接的client设备。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.notifyCharacteristicChanged](js-apis-bluetoothmanager.md#notifycharacteristicchangeddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 接收通知的client端设备地址，例如“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | [NotifyCharacteristic](js-apis-bluetooth.md#notifycharacteristicdeprecated) | 是 | 通知的特征值数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 通知操作，成功返回true，否则返回false。 |

**示例：**

```js
// 创建descriptors
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let notifyCharacteristic : bluetooth.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
let server : bluetooth.GattServer = bluetooth.BLE.createGattServer();
server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
```

### sendResponse(deprecated)

sendResponse(serverResponse: ServerResponse): boolean

server端回复client端的读写请求。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.sendResponse](js-apis-bluetoothmanager.md#sendresponsedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverResponse | [ServerResponse](js-apis-bluetooth.md#serverresponsedeprecated) | 是 | server端回复的响应数据。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 回复响应操作，成功返回true，否则返回false。 |

**示例：**

```js
/* send response */
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
let serverResponse : bluetooth.ServerResponse = {
    "deviceId": "XX:XX:XX:XX:XX:XX",
    "transId": 0,
    "status": 0,
    "offset": 0,
    "value": arrayBufferCCC,
};

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
let ret : boolean = gattServer.sendResponse(serverResponse);
if (ret) {
  console.info('bluetooth sendResponse successfully');
} else {
  console.error('bluetooth sendResponse failed');
}
```

### on('characteristicRead')(deprecated)

on(type: 'characteristicRead', callback: Callback<CharacteristicReadReq>): void

server端订阅特征值读请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('characteristicRead')](js-apis-bluetoothmanager.md#oncharacteristicreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadReq](js-apis-bluetooth.md#characteristicreadreqdeprecated)> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
cccValue[0] = 1;
function ReadCharacteristicReq(CharacteristicReadReq : bluetooth.CharacteristicReadReq) {
  let deviceId : string = CharacteristicReadReq.deviceId;
  let transId : number = CharacteristicReadReq.transId;
  let offset : number = CharacteristicReadReq.offset;
  let characteristicUuid : string = CharacteristicReadReq.characteristicUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicRead", ReadCharacteristicReq);
```

### off('characteristicRead')(deprecated)

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadReq>): void

server端取消订阅特征值读请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('characteristicRead')](js-apis-bluetoothmanager.md#offcharacteristicreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadReq](js-apis-bluetooth.md#characteristicreadreqdeprecated)> | 否 | 表示取消订阅特征值读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicRead");
```

### on('characteristicWrite')(deprecated)

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteReq>): void

server端订阅特征值写请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('characteristicWrite')](js-apis-bluetoothmanager.md#oncharacteristicwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteReq](js-apis-bluetooth.md#characteristicwritereqdeprecated)> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferCCC = new ArrayBuffer(8);
let cccValue = new Uint8Array(arrayBufferCCC);
function WriteCharacteristicReq(CharacteristicWriteReq : bluetooth.CharacteristicWriteReq) {
  let deviceId : string = CharacteristicWriteReq.deviceId;
  let transId : number = CharacteristicWriteReq.transId;
  let offset : number = CharacteristicWriteReq.offset;
  let isPrep : boolean = CharacteristicWriteReq.isPrep;
  let needRsp : boolean = CharacteristicWriteReq.needRsp;
  let value =  new Uint8Array(arrayBufferCCC);
  let characteristicUuid : string = CharacteristicWriteReq.characteristicUuid;

  cccValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferCCC};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("characteristicWrite", WriteCharacteristicReq);
```

### off('characteristicWrite')(deprecated)

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteReq>): void

server端取消订阅特征值写请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('characteristicWrite')](js-apis-bluetoothmanager.md#offcharacteristicwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteReq](js-apis-bluetooth.md#characteristicwritereqdeprecated)> | 否 | 表示取消订阅特征值写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("characteristicWrite");
```

### on('descriptorRead')(deprecated)

on(type: 'descriptorRead', callback: Callback<DescriptorReadReq>): void

server端订阅描述符读请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('descriptorRead')](js-apis-bluetoothmanager.md#ondescriptorreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadReq](js-apis-bluetooth.md#descriptorreadreqdeprecated)> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
descValue[0] = 1;
function ReadDescriptorReq(DescriptorReadReq : bluetooth.DescriptorReadReq) {
  let deviceId : string = DescriptorReadReq.deviceId;
  let transId : number = DescriptorReadReq.transId;
  let offset : number = DescriptorReadReq.offset;
  let descriptorUuid : string = DescriptorReadReq.descriptorUuid;

  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0,
  offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorRead", ReadDescriptorReq);
```

### off('descriptorRead')(deprecated)

off(type: 'descriptorRead', callback?: Callback<DescriptorReadReq>): void

server端取消订阅描述符读请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('descriptorRead')](js-apis-bluetoothmanager.md#offdescriptorreaddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadReq](js-apis-bluetooth.md#descriptorreadreqdeprecated)> | 否 | 表示取消订阅描述符读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorRead");
```

### on('descriptorWrite')(deprecated)

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteReq>): void

server端订阅描述符写请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('descriptorWrite')](js-apis-bluetoothmanager.md#ondescriptorwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteReq](js-apis-bluetooth.md#descriptorwritereqdeprecated)> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**返回值：**

无

**示例：**

```js
let arrayBufferDesc = new ArrayBuffer(8);
let descValue = new Uint8Array(arrayBufferDesc);
function WriteDescriptorReq(DescriptorWriteReq : bluetooth.DescriptorWriteReq) {
  let deviceId : string = DescriptorWriteReq.deviceId;
  let transId : number = DescriptorWriteReq.transId;
  let offset : number = DescriptorWriteReq.offset;
  let isPrep : boolean = DescriptorWriteReq.isPrep;
  let needRsp : boolean = DescriptorWriteReq.needRsp;
  let value = new Uint8Array(arrayBufferDesc);
  let descriptorUuid : string = DescriptorWriteReq.descriptorUuid;

  descValue.set(new Uint8Array(value));
  let serverResponse : bluetooth.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

  let ret : boolean = gattServer.sendResponse(serverResponse);
  if (ret) {
    console.info('bluetooth sendResponse successfully');
  } else {
    console.error('bluetooth sendResponse failed');
  }
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("descriptorWrite", WriteDescriptorReq);
```

### off('descriptorWrite')(deprecated)

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteReq>): void

server端取消订阅描述符写请求事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('descriptorWrite')](js-apis-bluetoothmanager.md#offdescriptorwritedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteReq](js-apis-bluetooth.md#descriptorwritereqdeprecated)> | 否 | 表示取消订阅描述符写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("descriptorWrite");
```

### on('connectStateChange')(deprecated)

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

server端订阅BLE连接状态变化事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.on('connectStateChange')](js-apis-bluetoothmanager.md#onconnectstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetooth.md#bleconnectchangedstatedeprecated)> | 是 | 表示回调函数的入参，连接状态。 |

**返回值：**

无

**示例：**

```js
function Connected(BLEConnectChangedState : bluetooth.BLEConnectChangedState) {
  let deviceId : string = BLEConnectChangedState.deviceId;
  let status : bluetooth.ProfileConnectionState = BLEConnectChangedState.state;
}

let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.on("connectStateChange", Connected);
```

### off('connectStateChange')(deprecated)

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

server端取消订阅BLE连接状态变化事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattServer.off('connectStateChange')](js-apis-bluetoothmanager.md#offconnectstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetooth.md#bleconnectchangedstatedeprecated)> | 否 | 表示取消订阅BLE连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let gattServer : bluetooth.GattServer = bluetooth.BLE.createGattServer();
gattServer.off("connectStateChange");
```

## GattClientDevice

client端类，使用client端方法之前需要创建该类的实例进行操作，通过createGattClientDevice(deviceId: string)方法构造此实例。

### connect(deprecated)

connect(): boolean

client端发起连接远端蓝牙低功耗设备。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.connect](js-apis-bluetoothmanager.md#connectdeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 连接操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.connect();
```

### disconnect(deprecated)

disconnect(): boolean

client端断开与远端蓝牙低功耗设备的连接。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.disconnect](js-apis-bluetoothmanager.md#disconnectdeprecated-2)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 断开连接操作，成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.disconnect();
```

### close(deprecated)

close(): boolean

关闭客户端功能，注销client在协议栈的注册，调用该接口后[GattClientDevice](js-apis-bluetooth.md#gattclientdevice)实例将不能再使用。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.close](js-apis-bluetoothmanager.md#closedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 关闭操作，成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let ret : boolean = device.close();
```

### getServices(deprecated)

getServices(callback: AsyncCallback<Array<GattService>>): void

client端获取蓝牙低功耗设备的所有服务，即服务发现 。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getServices](js-apis-bluetoothmanager.md#getservicesdeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[GattService](js-apis-bluetooth.md#gattservicedeprecated)>> | 是 | client进行服务发现，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
// callback 模式
function getServices(code : BusinessError, gattServices : Array<bluetooth.GattService>) {
  if (code.code == 0) {
      console.info(`bluetooth code is ${code.code}`);
      console.info(`bluetooth services size is ${gattServices.length}`);

      for (let i = 0; i < gattServices.length; i++) {
        console.info(`bluetooth serviceUuid is ${gattServices[i].serviceUuid}`);
      }
  }
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.connect();
device.getServices(getServices);
```

### getServices(deprecated)

getServices(): Promise<Array<GattService>>

client端获取蓝牙低功耗设备的所有服务，即服务发现。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getServices](js-apis-bluetoothmanager.md#getservicesdeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GattService](js-apis-bluetooth.md#gattservicedeprecated)>> | client进行服务发现，通过promise形式获取。 |

**示例：**

```js
// Promise 模式
let device : bluetooth.GattClientDevice= bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.connect();
device.getServices().then((result : Array<bluetooth.GattService>) => {
    console.info("getServices successfully:" + JSON.stringify(result));
});
```

### readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

client端读取蓝牙低功耗设备特定服务的特征值。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readCharacteristicValue](js-apis-bluetoothmanager.md#readcharacteristicvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |
| callback | AsyncCallback<[BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated)> | 是 | client读取特征值，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function readCcc(code : BusinessError, BLECharacteristic : bluetooth.BLECharacteristic) {
  if (code.code != 0) {
      return;
  }
  console.info(`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}`);
  let value = new Uint8Array(BLECharacteristic.characteristicValue);
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let bufferDesc : ArrayBuffer = new ArrayBuffer(8);
let descV : Uint8Array = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
characteristicValue: bufferCCC, descriptors:descriptors};

device.readCharacteristicValue(characteristic, readCcc);
```

### readCharacteristicValue(deprecated)

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

client端读取蓝牙低功耗设备特定服务的特征值。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readCharacteristicValue](js-apis-bluetoothmanager.md#readcharacteristicvaluedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated)> | client读取特征值，通过promise形式获取。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
characteristicValue: bufferCCC, descriptors:descriptors};

device.readCharacteristicValue(characteristic);
```

### readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

client端读取蓝牙低功耗设备特定的特征包含的描述符。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readDescriptorValue](js-apis-bluetoothmanager.md#readdescriptorvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth.md#bledescriptordeprecated) | 是 | 待读取的描述符。 |
| callback | AsyncCallback<[BLEDescriptor](js-apis-bluetooth.md#bledescriptordeprecated)> | 是 | client读取描述符，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@kit.BasicServicesKit';
function readDesc(code : BusinessError, BLEDescriptor : bluetooth.BLEDescriptor) {
  if (code.code != 0) {
      return;
  }
  console.info(`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}`);
  let value = new Uint8Array(BLEDescriptor.descriptorValue);
}

let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
device.readDescriptorValue(descriptor, readDesc);
```

### readDescriptorValue(deprecated)

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

client端读取蓝牙低功耗设备特定的特征包含的描述符。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.readDescriptorValue](js-apis-bluetoothmanager.md#readdescriptorvaluedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth.md#bledescriptordeprecated) | 是 | 待读取的描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BLEDescriptor](js-apis-bluetooth.md#bledescriptordeprecated)> | client读取描述符，通过promise形式获取。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
device.readDescriptorValue(descriptor);
```

### writeCharacteristicValue(deprecated)

writeCharacteristicValue(characteristic: BLECharacteristic): boolean

client端向低功耗蓝牙设备写入特定的特征值。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.writeCharacteristicValue](js-apis-bluetoothmanager.md#writecharacteristicvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated) | 是 | 蓝牙设备特征对应的二进制值及其它参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 写特征值操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
descriptors[0] = descriptor;

let bufferCCC = new ArrayBuffer(8);
let cccV = new Uint8Array(bufferCCC);
cccV[0] = 1;
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  characteristicValue: bufferCCC, descriptors:descriptors};
let retWriteCcc : boolean = device.writeCharacteristicValue(characteristic);
if (retWriteCcc) {
  console.info('write characteristic successfully');
} else {
  console.error('write characteristic failed');
}
```

### writeDescriptorValue(deprecated)

writeDescriptorValue(descriptor: BLEDescriptor): boolean

client端向低功耗蓝牙设备特定的描述符写入二进制数据。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.writeDescriptorValue](js-apis-bluetoothmanager.md#writedescriptorvaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth.md#bledescriptordeprecated) | 是 | 蓝牙设备描述符的二进制值及其它参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 写描述符操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
let bufferDesc = new ArrayBuffer(8);
let descV = new Uint8Array(bufferDesc);
descV[0] = 22;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
let retWriteDesc : boolean = device.writeDescriptorValue(descriptor);
if (retWriteDesc) {
  console.info('bluetooth write descriptor successfully');
} else {
  console.error('bluetooth write descriptor failed');
}
```

### setBLEMtuSize(deprecated)

setBLEMtuSize(mtu: number): boolean

client协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU），调用[connect](js-apis-bluetooth.md#connectdeprecated)接口连接成功后才能使用。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.setBLEMtuSize](js-apis-bluetoothmanager.md#setblemtusizedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mtu | number | 是 | 设置范围为22~512字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | MTU协商操作成功返回true，操作失败返回false。 |

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.setBLEMtuSize(128);
```

### setNotifyCharacteristicChanged(deprecated)

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): boolean

向服务端发送设置通知此特征值请求。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.setNotifyCharacteristicChanged](js-apis-bluetoothmanager.md#setnotifycharacteristicchangeddeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated) | 是 | 蓝牙低功耗特征。 |
| enable | boolean | 是 | 启用接收notify设置为true，否则设置为false。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 设置操作成功返回true，操作失败返回false。 |

**示例：**

```js
// 创建descriptors
let descriptors : Array<bluetooth.BLEDescriptor> = [];
let arrayBuffer = new ArrayBuffer(8);
let descV = new Uint8Array(arrayBuffer);
descV[0] = 11;
let descriptor : bluetooth.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
  descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
descriptors[0] = descriptor;
let arrayBufferC = new ArrayBuffer(8);
let characteristic : bluetooth.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
  characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.setNotifyCharacteristicChanged(characteristic, false);
```

### on('BLECharacteristicChange')(deprecated)

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

订阅蓝牙低功耗设备的特征值变化事件。需要先调用setNotifyCharacteristicChanged接口才能接收server端的通知。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.on('BLECharacteristicChange')](js-apis-bluetoothmanager.md#onblecharacteristicchangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated)> | 是 | 表示蓝牙低功耗设备的特征值变化事件的回调函数。 |

**返回值：**

无

**示例：**

```js
function CharacteristicChange(CharacteristicChangeReq : bluetooth.BLECharacteristic) {
  let serviceUuid : string = CharacteristicChangeReq.serviceUuid;
  let characteristicUuid : string = CharacteristicChangeReq.characteristicUuid;
  let value = new Uint8Array(CharacteristicChangeReq.characteristicValue);
}
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.on('BLECharacteristicChange', CharacteristicChange);
```

### off('BLECharacteristicChange')(deprecated)

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

取消订阅蓝牙低功耗设备的特征值变化事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.off('BLECharacteristicChange')](js-apis-bluetoothmanager.md#offblecharacteristicchangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated)> | 否 | 表示取消订阅蓝牙低功耗设备的特征值变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.off('BLECharacteristicChange');
```

### on('BLEConnectionStateChange')(deprecated)

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

client端订阅蓝牙低功耗设备的连接状态变化事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.on('BLEConnectionStateChange')](js-apis-bluetoothmanager.md#onbleconnectionstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetooth.md#bleconnectchangedstatedeprecated)> | 是 | 表示连接状态，已连接或断开。 |

**返回值：**

无

**示例：**

```js
function ConnectStateChanged(state : bluetooth.BLEConnectChangedState) {
  console.info('bluetooth connect state changed');
  let connectState : bluetooth.ProfileConnectionState = state.state;
}
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.on('BLEConnectionStateChange', ConnectStateChanged);
```

### off('BLEConnectionStateChange')(deprecated)

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

取消订阅蓝牙低功耗设备的连接状态变化事件。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.off('BLEConnectionStateChange')](js-apis-bluetoothmanager.md#offbleconnectionstatechangedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetooth.md#bleconnectchangedstatedeprecated)> | 否 | 表示取消订阅蓝牙低功耗设备的连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**返回值：**

无

**示例：**

```js
let device : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
device.off('BLEConnectionStateChange');
```

### getDeviceName(deprecated)

getDeviceName(callback: AsyncCallback<string>): void

client获取远端蓝牙低功耗设备名。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getDeviceName](js-apis-bluetoothmanager.md#getdevicenamedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | client获取对端server设备名，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@ohos.base';
// callback
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let deviceName : void = gattClient.getDeviceName((err : BusinessError, data : string)=> {
    console.info('device name err ' + JSON.stringify(err));
    console.info('device name' + JSON.stringify(data));
})
```

### getDeviceName(deprecated)

getDeviceName(): Promise<string>

client获取远端蓝牙低功耗设备名。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getDeviceName](js-apis-bluetoothmanager.md#getdevicenamedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | client获取对端server设备名，通过promise形式获取。 |

**示例：**

```js
// promise
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClient.getDeviceName().then((data) => {
    console.info('device name' + JSON.stringify(data));
})
```

### getRssiValue(deprecated)

getRssiValue(callback: AsyncCallback<number>): void

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](js-apis-bluetooth.md#connectdeprecated)接口连接成功后才能使用。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getRssiValue](js-apis-bluetoothmanager.md#getrssivaluedeprecated)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 返回信号强度，单位 dBm，通过注册回调函数获取。 |

**返回值：**

无

**示例：**

```js
import { BusinessError } from '@ohos.base';
// callback
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
let ret : boolean = gattClient.connect();
gattClient.getRssiValue((err : BusinessError, data : number)=> {
    console.info('rssi err ' + JSON.stringify(err));
    console.info('rssi value' + JSON.stringify(data));
})
```

### getRssiValue(deprecated)

getRssiValue(): Promise<number>

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](js-apis-bluetooth.md#connectdeprecated)接口连接成功后才能使用。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattClientDevice.getRssiValue](js-apis-bluetoothmanager.md#getrssivaluedeprecated-1)替代。

**需要权限**：ohos.permission.USE\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回信号强度，单位 dBm，通过promise形式获取。 |

**示例：**

```js
// promise
let gattClient : bluetooth.GattClientDevice = bluetooth.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
gattClient.getRssiValue().then((data : number) => {
    console.info('rssi' + JSON.stringify(data));
})
```

## ScanMode(deprecated)

枚举，扫描模式。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanMode](js-apis-bluetoothmanager.md#scanmodedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN\_MODE\_NONE | 0 | 没有扫描模式。 |
| SCAN\_MODE\_CONNECTABLE | 1 | 可连接扫描模式。 |
| SCAN\_MODE\_GENERAL\_DISCOVERABLE | 2 | general发现模式。 |
| SCAN\_MODE\_LIMITED\_DISCOVERABLE | 3 | limited发现模式。 |
| SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE | 4 | 可连接general发现模式。 |
| SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE | 5 | 可连接limited发现模式。 |

## BondState(deprecated)

枚举，配对状态。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BondState](js-apis-bluetoothmanager.md#bondstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOND\_STATE\_INVALID | 0 | 无效的配对。 |
| BOND\_STATE\_BONDING | 1 | 正在配对。 |
| BOND\_STATE\_BONDED | 2 | 已配对。 |

## SppOption(deprecated)

描述spp的配置参数。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.SppOption](js-apis-bluetoothmanager.md#sppoptiondeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uuid | string | 否 | 否 | 套接字链路类型的服务UUID。 |
| secure | boolean | 否 | 否 | 是否是安全通道。 |
| type | [SppType](js-apis-bluetooth.md#spptypedeprecated) | 否 | 否 | Spp链路类型。 |

## SppType(deprecated)

枚举，Spp链路类型。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.SppType](js-apis-bluetoothmanager.md#spptypedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPP\_RFCOMM | 0 | 表示rfcomm链路类型。 |

## GattService(deprecated)

描述service的接口参数定义。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.GattService](js-apis-bluetoothmanager.md#gattservicedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 否 | 否 | 如果是主服务设置为true，否则设置为false。 |
| characteristics | Array<[BLECharacteristic](js-apis-bluetooth.md#blecharacteristicdeprecated)> | 否 | 否 | 当前服务包含的特征列表。 |
| includeServices | Array<[GattService](js-apis-bluetooth.md#gattservicedeprecated)> | 否 | 是 | 当前服务依赖的其它服务。 |

## BLECharacteristic(deprecated)

描述characteristic的接口参数定义 。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| descriptors | Array<[BLEDescriptor](js-apis-bluetooth.md#bledescriptordeprecated)> | 否 | 否 | 特定特征的描述符列表。 |

## BLEDescriptor(deprecated)

描述descriptor的接口参数定义 。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| descriptorUuid | string | 否 | 否 | 描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| descriptorValue | ArrayBuffer | 否 | 否 | 描述符对应的二进制值。 |

## NotifyCharacteristic(deprecated)

描述server端特征值变化时发送的特征通知参数定义。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.NotifyCharacteristic](js-apis-bluetoothmanager.md#notifycharacteristicdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| confirm | boolean | 否 | 否 | 如果是notification则对端回复确认设置为true，如果是indication则对端不需要回复确认设置为false。 |

## CharacteristicReadReq(deprecated)

描述server端订阅后收到的特征值读请求事件参数结构。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.CharacteristicReadRequest](js-apis-bluetoothmanager.md#characteristicreadrequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送特征值读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读特征值数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## CharacteristicWriteReq(deprecated)

描述server端订阅后收到的特征值写请求事件参数结构。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.CharacteristicWriteRequest](js-apis-bluetoothmanager.md#characteristicwriterequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送特征值写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示写特征值数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。 |
| isPrep | boolean | 否 | 否 | 表示写请求是否立即执行。true表示立即执行。 |
| needRsp | boolean | 否 | 否 | 表示是否要给client端回复响应。true表示需要回复。 |
| value | ArrayBuffer | 否 | 否 | 表示写入的描述符二进制数据。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## DescriptorReadReq(deprecated)

描述server端订阅后收到的描述符读请求事件参数结构。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.DescriptorReadRequest](js-apis-bluetoothmanager.md#descriptorreadrequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## DescriptorWriteReq(deprecated)

描述server端订阅后收到的描述符写请求事件参数结构。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.DescriptorWriteRequest](js-apis-bluetoothmanager.md#descriptorwriterequestdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送描述符写请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示写请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示写描述符数据的起始位置。例如：k表示从第k个字节开始写，server端回复响应时需填写相同的offset。 |
| isPrep | boolean | 否 | 否 | 表示写请求是否立即执行。 |
| needRsp | boolean | 否 | 否 | 表示是否要给client端回复响应。 |
| value | ArrayBuffer | 否 | 否 | 表示写入的描述符二进制数据。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## ServerResponse(deprecated)

描述server端回复client端读/写请求的响应参数结构。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ServerResponse](js-apis-bluetoothmanager.md#serverresponsedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。 |
| status | number | 否 | 否 | 表示响应的状态，设置为0即可，表示正常。 |
| offset | number | 否 | 否 | 表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。 |
| value | ArrayBuffer | 否 | 否 | 表示回复响应的二进制数据。 |

## BLEConnectChangedState(deprecated)

描述Gatt profile连接状态 。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BLEConnectChangedState](js-apis-bluetoothmanager.md#bleconnectchangedstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | [ProfileConnectionState](js-apis-bluetooth.md#profileconnectionstatedeprecated) | 否 | 否 | 表示BLE连接状态的枚举。 |

## ProfileConnectionState(deprecated)

枚举，蓝牙设备的profile连接状态。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ProfileConnectionState](js-apis-bluetoothmanager.md#profileconnectionstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_DISCONNECTED | 0 | 表示profile已断连。 |
| STATE\_CONNECTING | 1 | 表示profile正在连接。 |
| STATE\_CONNECTED | 2 | 表示profile已连接。 |
| STATE\_DISCONNECTING | 3 | 表示profile正在断连。 |

## ScanFilter(deprecated)

扫描过滤参数。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanFilter](js-apis-bluetoothmanager.md#scanfilterdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 表示过滤的BLE设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| name | string | 否 | 是 | 表示过滤的BLE设备名。 |
| serviceUuid | string | 否 | 是 | 表示过滤包含该UUID服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## ScanOptions(deprecated)

扫描的配置参数。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanOptions](js-apis-bluetoothmanager.md#scanoptionsdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 表示扫描结果上报延迟时间，默认值为0。 |
| dutyMode | [ScanDuty](js-apis-bluetooth.md#scandutydeprecated) | 否 | 是 | 表示扫描模式，默认值为SCAN\_MODE\_LOW\_POWER。 |
| matchMode | [MatchMode](js-apis-bluetooth.md#matchmodedeprecated) | 否 | 是 | 表示硬件的过滤匹配模式，默认值为MATCH\_MODE\_AGGRESSIVE。 |

## ScanDuty(deprecated)

枚举，扫描模式。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanDuty](js-apis-bluetoothmanager.md#scandutydeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN\_MODE\_LOW\_POWER | 0 | 表示低功耗模式，默认值。 |
| SCAN\_MODE\_BALANCED | 1 | 表示均衡模式。 |
| SCAN\_MODE\_LOW\_LATENCY | 2 | 表示低延迟模式。 |

## MatchMode(deprecated)

枚举，硬件过滤匹配模式。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.MatchMode](js-apis-bluetoothmanager.md#matchmodedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MATCH\_MODE\_AGGRESSIVE | 1 | 表示硬件上报扫描结果门限较低，比如扫描到的功率较低或者一段时间扫描到的次数较少也触发上报，默认值。 |
| MATCH\_MODE\_STICKY | 2 | 表示硬件上报扫描结果门限较高，更高的功率门限以及扫描到多次才会上报。 |

## ScanResult(deprecated)

扫描结果上报数据。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ScanResult](js-apis-bluetoothmanager.md#scanresultdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值。 |
| data | ArrayBuffer | 否 | 否 | 表示扫描到的设备发送的广播包。 |

## BluetoothState(deprecated)

枚举，蓝牙开关状态。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BluetoothState](js-apis-bluetoothmanager.md#bluetoothstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_OFF | 0 | 表示蓝牙已关闭。 |
| STATE\_TURNING\_ON | 1 | 表示蓝牙正在打开。 |
| STATE\_ON | 2 | 表示蓝牙已打开。 |
| STATE\_TURNING\_OFF | 3 | 表示蓝牙正在关闭。 |
| STATE\_BLE\_TURNING\_ON | 4 | 表示蓝牙正在打开LE-only模式。 |
| STATE\_BLE\_ON | 5 | 表示蓝牙正处于LE-only模式。 |
| STATE\_BLE\_TURNING\_OFF | 6 | 表示蓝牙正在关闭LE-only模式。 |

## AdvertiseSetting(deprecated)

描述蓝牙低功耗设备发送广播的参数。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.AdvertiseSetting](js-apis-bluetoothmanager.md#advertisesettingdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 表示广播间隔，最小值设置32个slot表示20ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。 |
| txPower | number | 否 | 是 | 表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dBm。 |
| connectable | boolean | 否 | 是 | 表示是否是可连接广播，默认值设置为true。 |

## AdvertiseData(deprecated)

描述BLE广播数据包的内容。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.AdvertiseData](js-apis-bluetoothmanager.md#advertisedatadeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 否 | 表示要广播的服务 UUID 列表。 |
| manufactureData | Array<[ManufactureData](js-apis-bluetooth.md#manufacturedatadeprecated)> | 否 | 否 | 表示要广播的广播的制造商信息列表。 |
| serviceData | Array<[ServiceData](js-apis-bluetooth.md#servicedatadeprecated)> | 否 | 否 | 表示要广播的服务数据列表。 |

## ManufactureData(deprecated)

描述BLE广播数据包的内容。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ManufactureData](js-apis-bluetoothmanager.md#manufacturedatadeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufactureId | number | 否 | 否 | 表示制造商的ID，由蓝牙SIG分配。 |
| manufactureValue | ArrayBuffer | 否 | 否 | 表示制造商发送的制造商数据。 |

## ServiceData(deprecated)

描述广播包中服务数据内容。

**说明** 

从API version 7开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ServiceData](js-apis-bluetoothmanager.md#servicedatadeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。 |
| serviceValue | ArrayBuffer | 否 | 否 | 表示服务数据。 |

## PinRequiredParam(deprecated)

描述配对请求参数。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.PinRequiredParam](js-apis-bluetoothmanager.md#pinrequiredparamdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| pinCode | string | 否 | 否 | 表示要配对的密钥。 |

## BondStateParam(deprecated)

描述配对状态参数。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.BondStateParam](js-apis-bluetoothmanager.md#bondstateparamdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| state | BondState | 否 | 否 | 表示配对设备的状态。 |

## StateChangeParam(deprecated)

描述profile状态改变参数。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示蓝牙设备地址。 |
| state | [ProfileConnectionState](js-apis-bluetooth.md#profileconnectionstatedeprecated) | 否 | 否 | 表示蓝牙设备的profile连接状态。 |

## DeviceClass(deprecated)

描述蓝牙设备的类别。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.DeviceClass](js-apis-bluetoothmanager.md#deviceclassdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| majorClass | [MajorClass](js-apis-bluetooth.md#majorclassdeprecated) | 否 | 否 | 表示蓝牙设备主要类别的枚举。 |
| majorMinorClass | [MajorMinorClass](js-apis-bluetooth.md#majorminorclassdeprecated) | 否 | 否 | 表示主要次要蓝牙设备类别的枚举。 |
| classOfDevice | number | 否 | 否 | 表示设备类别。 |

## MajorClass(deprecated)

枚举，蓝牙设备主要类别。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.MajorClass](js-apis-bluetoothmanager.md#majorclassdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MAJOR\_MISC | 0x0000 | 表示杂项设备。 |
| MAJOR\_COMPUTER | 0x0100 | 表示计算机设备。 |
| MAJOR\_PHONE | 0x0200 | 表示手机设备。 |
| MAJOR\_NETWORKING | 0x0300 | 表示网络设备。 |
| MAJOR\_AUDIO\_VIDEO | 0x0400 | 表示音频和视频设备。 |
| MAJOR\_PERIPHERAL | 0x0500 | 表示外围设备。 |
| MAJOR\_IMAGING | 0x0600 | 表示成像设备。 |
| MAJOR\_WEARABLE | 0x0700 | 表示可穿戴设备。 |
| MAJOR\_TOY | 0x0800 | 表示玩具设备。 |
| MAJOR\_HEALTH | 0x0900 | 表示健康设备。 |
| MAJOR\_UNCATEGORIZED | 0x1F00 | 表示未分类设备。 |

## MajorMinorClass(deprecated)

枚举，主要次要蓝牙设备类别。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.MajorMinorClass](js-apis-bluetoothmanager.md#majorminorclassdeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPUTER\_UNCATEGORIZED | 0x0100 | 表示未分类计算机设备。 |
| COMPUTER\_DESKTOP | 0x0104 | 表示台式计算机设备。 |
| COMPUTER\_SERVER | 0x0108 | 表示服务器设备。 |
| COMPUTER\_LAPTOP | 0x010C | 表示便携式计算机设备。 |
| COMPUTER\_HANDHELD\_PC\_PDA | 0x0110 | 表示手持式计算机设备。 |
| COMPUTER\_PALM\_SIZE\_PC\_PDA | 0x0114 | 表示掌上电脑设备。 |
| COMPUTER\_WEARABLE | 0x0118 | 表示可穿戴计算机设备。 |
| COMPUTER\_TABLET | 0x011C | 表示平板电脑设备。 |
| PHONE\_UNCATEGORIZED | 0x0200 | 表示未分类手机设备。 |
| PHONE\_CELLULAR | 0x0204 | 表示便携式手机设备。 |
| PHONE\_CORDLESS | 0x0208 | 表示无线电话设备。 |
| PHONE\_SMART | 0x020C | 表示智能手机设备。 |
| PHONE\_MODEM\_OR\_GATEWAY | 0x0210 | 表示调制解调器或网关手机设备。 |
| PHONE\_ISDN | 0x0214 | 表示ISDN手机设备。 |
| NETWORK\_FULLY\_AVAILABLE | 0x0300 | 表示网络完全可用设备。 |
| NETWORK\_1\_TO\_17\_UTILIZED | 0x0320 | 表示使用网络1到17设备。 |
| NETWORK\_17\_TO\_33\_UTILIZED | 0x0340 | 表示使用网络17到33设备。 |
| NETWORK\_33\_TO\_50\_UTILIZED | 0x0360 | 表示使用网络33到50设备。 |
| NETWORK\_60\_TO\_67\_UTILIZED | 0x0380 | 表示使用网络60到67设备。 |
| NETWORK\_67\_TO\_83\_UTILIZED | 0x03A0 | 表示使用网络67到83设备。 |
| NETWORK\_83\_TO\_99\_UTILIZED | 0x03C0 | 表示使用网络83到99设备。 |
| NETWORK\_NO\_SERVICE | 0x03E0 | 表示网络无服务设备。 |
| AUDIO\_VIDEO\_UNCATEGORIZED | 0x0400 | 表示未分类音频视频设备。 |
| AUDIO\_VIDEO\_WEARABLE\_HEADSET | 0x0404 | 表示可穿戴式音频视频设备。 |
| AUDIO\_VIDEO\_HANDSFREE | 0x0408 | 表示免提音频视频设备。 |
| AUDIO\_VIDEO\_MICROPHONE | 0x0410 | 表示麦克风音频视频设备。 |
| AUDIO\_VIDEO\_LOUDSPEAKER | 0x0414 | 表示扬声器音频视频设备。 |
| AUDIO\_VIDEO\_HEADPHONES | 0x0418 | 表示头戴式音频视频设备。 |
| AUDIO\_VIDEO\_PORTABLE\_AUDIO | 0x041C | 表示便携式音频视频设备。 |
| AUDIO\_VIDEO\_CAR\_AUDIO | 0x0420 | 表示汽车音频视频设备。 |
| AUDIO\_VIDEO\_SET\_TOP\_BOX | 0x0424 | 表示机顶盒音频视频设备。 |
| AUDIO\_VIDEO\_HIFI\_AUDIO | 0x0428 | 表示高保真音响设备。 |
| AUDIO\_VIDEO\_VCR | 0x042C | 表示录像机音频视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_CAMERA | 0x0430 | 表示照相机音频视频设备。 |
| AUDIO\_VIDEO\_CAMCORDER | 0x0434 | 表示摄像机音频视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_MONITOR | 0x0438 | 表示监视器音频视频设备。 |
| AUDIO\_VIDEO\_VIDEO\_DISPLAY\_AND\_LOUDSPEAKER | 0x043C | 表示视频显示器和扬声器设备。 |
| AUDIO\_VIDEO\_VIDEO\_CONFERENCING | 0x0440 | 表示音频视频会议设备。 |
| AUDIO\_VIDEO\_VIDEO\_GAMING\_TOY | 0x0448 | 表示游戏玩具音频视频设备。 |
| PERIPHERAL\_NON\_KEYBOARD\_NON\_POINTING | 0x0500 | 表示非键盘非指向外围设备。 |
| PERIPHERAL\_KEYBOARD | 0x0540 | 表示外设键盘设备。 |
| PERIPHERAL\_POINTING\_DEVICE | 0x0580 | 表示定点装置外围设备。 |
| PERIPHERAL\_KEYBOARD\_POINTING | 0x05C0 | 表示键盘指向外围设备。 |
| PERIPHERAL\_UNCATEGORIZED | 0x0500 | 表示未分类外围设备。 |
| PERIPHERAL\_JOYSTICK | 0x0504 | 表示周边操纵杆设备。 |
| PERIPHERAL\_GAMEPAD | 0x0508 | 表示周边游戏板设备。 |
| PERIPHERAL\_REMOTE\_CONTROL | 0x05C0 | 表示远程控制外围设备。 |
| PERIPHERAL\_SENSING\_DEVICE | 0x0510 | 表示外围传感设备设备。 |
| PERIPHERAL\_DIGITIZER\_TABLET | 0x0514 | 表示外围数字化仪平板电脑设备。 |
| PERIPHERAL\_CARD\_READER | 0x0518 | 表示外围读卡器设备。 |
| PERIPHERAL\_DIGITAL\_PEN | 0x051C | 表示外设数码笔设备。 |
| PERIPHERAL\_SCANNER\_RFID | 0x0520 | 表示射频识别扫描仪外围设备。 |
| PERIPHERAL\_GESTURAL\_INPUT | 0x0522 | 表示手势输入外围设备。 |
| IMAGING\_UNCATEGORIZED | 0x0600 | 表示未分类的图像设备。 |
| IMAGING\_DISPLAY | 0x0610 | 表示图像显示设备。 |
| IMAGING\_CAMERA | 0x0620 | 表示成像照相机设备。 |
| IMAGING\_SCANNER | 0x0640 | 表示成像扫描仪设备。 |
| IMAGING\_PRINTER | 0x0680 | 表示成像打印机设备。 |
| WEARABLE\_UNCATEGORIZED | 0x0700 | 表示未分类的可穿戴设备。 |
| WEARABLE\_WRIST\_WATCH | 0x0704 | 表示可穿戴腕表设备。 |
| WEARABLE\_PAGER | 0x0708 | 表示可穿戴寻呼机设备。 |
| WEARABLE\_JACKET | 0x070C | 表示夹克可穿戴设备。 |
| WEARABLE\_HELMET | 0x0710 | 表示可穿戴头盔设备。 |
| WEARABLE\_GLASSES | 0x0714 | 表示可穿戴眼镜设备。 |
| TOY\_UNCATEGORIZED | 0x0800 | 表示未分类的玩具设备。 |
| TOY\_ROBOT | 0x0804 | 表示玩具机器人设备。 |
| TOY\_VEHICLE | 0x0808 | 表示玩具车设备。 |
| TOY\_DOLL\_ACTION\_FIGURE | 0x080C | 表示人形娃娃玩具设备。 |
| TOY\_CONTROLLER | 0x0810 | 表示玩具控制器设备。 |
| TOY\_GAME | 0x0814 | 表示玩具游戏设备。 |
| HEALTH\_UNCATEGORIZED | 0x0900 | 表示未分类健康设备。 |
| HEALTH\_BLOOD\_PRESSURE | 0x0904 | 表示血压健康设备。 |
| HEALTH\_THERMOMETER | 0x0908 | 表示温度计健康设备。 |
| HEALTH\_WEIGHING | 0x090C | 表示体重健康设备。 |
| HEALTH\_GLUCOSE | 0x0910 | 表示葡萄糖健康设备。 |
| HEALTH\_PULSE\_OXIMETER | 0x0914 | 表示脉搏血氧仪健康设备。 |
| HEALTH\_PULSE\_RATE | 0x0918 | 表示脉搏率健康设备。 |
| HEALTH\_DATA\_DISPLAY | 0x091C | 表示数据显示健康设备。 |
| HEALTH\_STEP\_COUNTER | 0x0920 | 表示计步器健康设备。 |
| HEALTH\_BODY\_COMPOSITION\_ANALYZER | 0x0924 | 表示身体成分分析仪健康设备。 |
| HEALTH\_PEAK\_FLOW\_MOITOR | 0x0928 | 表示峰值流量监控仪健康设备。 |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | 表示药物监视仪健康设备。 |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | 表示膝盖假肢健康设备。 |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | 表示脚踝假肢健康设备。 |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | 表示通用健康管理设备。 |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | 表示个人移动健康设备。 |

## PlayingState(deprecated)

枚举，蓝牙A2DP 播放状态。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.PlayingState](js-apis-bluetoothmanager.md#playingstatedeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_NOT\_PLAYING | 0 | 表示未播放。 |
| STATE\_PLAYING | 1 | 表示正在播放。 |

## ProfileId(deprecated)

蓝牙profile枚举，API9新增PROFILE\_HID\_HOST，PROFILE\_PAN\_NETWORK。

**说明** 

从API version 8开始支持，从API version 9开始废弃。建议使用[bluetoothManager.ProfileId](js-apis-bluetoothmanager.md#profileiddeprecated)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROFILE\_A2DP\_SOURCE | 1 | 表示A2DP profile。 |
| PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY | 4 | 表示HFP profile。 |
