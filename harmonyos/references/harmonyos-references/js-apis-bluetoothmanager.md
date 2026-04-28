---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetoothmanager
title: @ohos.bluetoothManager (蓝牙)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 已停止维护的接口 > @ohos.bluetoothManager (蓝牙)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:12+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5c49a4871ed28a47c9ccd2b94f0b9f47b04593d92adce77e69b7f97cc30359e8
---

蓝牙模块提供了基础的传统蓝牙能力以及BLE的扫描、广播等功能。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API Version 10 开始，该接口不再维护，推荐使用[@ohos.bluetooth.ble](js-apis-bluetooth-ble.md)等相关profile接口。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { bluetoothManager } from '@kit.ConnectivityKit';
```

## bluetoothManager.enableBluetooth(deprecated)

PhonePC/2in1TabletTVWearable

enableBluetooth(): void

开启蓝牙。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[access.enableBluetooth](js-apis-bluetooth-access.md#accessenablebluetooth)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. bluetoothManager.enableBluetooth();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.disableBluetooth(deprecated)

PhonePC/2in1TabletTVWearable

disableBluetooth(): void

关闭蓝牙。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[access.disableBluetooth](js-apis-bluetooth-access.md#accessdisablebluetooth)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. bluetoothManager.disableBluetooth();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ", errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.getLocalName(deprecated)

PhonePC/2in1TabletTVWearable

getLocalName(): string

获取蓝牙本地设备名称。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getLocalName](js-apis-bluetooth-connection.md#connectiongetlocalname)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 蓝牙本地设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let localName: string = bluetoothManager.getLocalName();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.getState(deprecated)

PhonePC/2in1TabletTVWearable

getState(): BluetoothState

获取蓝牙开关状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[access.getState](js-apis-bluetooth-access.md#accessgetstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothState](js-apis-bluetoothmanager.md#bluetoothstatedeprecated) | 表示蓝牙开关状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let state: bluetoothManager.BluetoothState = bluetoothManager.getState();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.getBtConnectionState(deprecated)

PhonePC/2in1TabletTVWearable

getBtConnectionState(): ProfileConnectionState

获取蓝牙本端的Profile连接状态，例如：任意一个支持的Profile连接状态为已连接，则此接口返回状态为已连接。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getProfileConnectionState](js-apis-bluetooth-connection.md#connectiongetprofileconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetoothmanager.md#profileconnectionstatedeprecated) | 表示蓝牙设备的Profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let connectionState: bluetoothManager.ProfileConnectionState = bluetoothManager.getBtConnectionState();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.setLocalName(deprecated)

PhonePC/2in1TabletTVWearable

setLocalName(name: string): void

设置蓝牙本地设备名称。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setLocalName](js-apis-bluetooth-connection.md#connectionsetlocalnamedeprecated)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 要设置的蓝牙名称，最大长度为248字节数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. bluetoothManager.setLocalName('device_name');
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.pairDevice(deprecated)

PhonePC/2in1TabletTVWearable

pairDevice(deviceId: string): void

发起蓝牙配对。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.pairDevice](js-apis-bluetooth-connection.md#connectionpairdevice)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示配对的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. // 实际的地址可由扫描流程获取
4. bluetoothManager.pairDevice("XX:XX:XX:XX:XX:XX");
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

## bluetoothManager.getProfileConnectionState(deprecated)

PhonePC/2in1TabletTVWearable

getProfileConnectionState(profileId: ProfileId): ProfileConnectionState

依据ProfileId获取指定profile的连接状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getProfileConnectionState](js-apis-bluetooth-connection.md#connectiongetprofileconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | ProfileId | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetoothmanager.md#profileconnectionstatedeprecated) | profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let result: bluetoothManager.ProfileConnectionState = bluetoothManager.getProfileConnectionState(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE);
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.getRemoteDeviceName(deprecated)

PhonePC/2in1TabletTVWearable

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getRemoteDeviceName](js-apis-bluetooth-connection.md#connectiongetremotedevicename)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串格式返回设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let remoteDeviceName: string = bluetoothManager.getRemoteDeviceName("XX:XX:XX:XX:XX:XX");
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.getRemoteDeviceClass(deprecated)

PhonePC/2in1TabletTVWearable

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getRemoteDeviceClass](js-apis-bluetooth-connection.md#connectiongetremotedeviceclass)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远程设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClass](js-apis-bluetoothmanager.md#deviceclassdeprecated) | 远程设备的类别。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let remoteDeviceClass: bluetoothManager.DeviceClass  = bluetoothManager.getRemoteDeviceClass("XX:XX:XX:XX:XX:XX");
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.getPairedDevices(deprecated)

PhonePC/2in1TabletTVWearable

getPairedDevices(): Array<string>

获取蓝牙配对列表。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getPairedDevices](js-apis-bluetooth-connection.md#connectiongetpaireddevices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 已配对蓝牙设备的地址列表。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let devices: Array<string> = bluetoothManager.getPairedDevices();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.setBluetoothScanMode(deprecated)

PhonePC/2in1TabletTVWearable

setBluetoothScanMode(mode: ScanMode, duration: number): void

设置蓝牙扫描模式，可以被远端设备发现。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setBluetoothScanMode](js-apis-bluetooth-connection.md#connectionsetbluetoothscanmode)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ScanMode](js-apis-bluetoothmanager.md#scanmodedeprecated) | 是 | 蓝牙扫描模式。 |
| duration | number | 是 | 设备可被发现的持续时间，单位为毫秒；设置为0则持续可发现。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. // 设置为可连接可发现才可被远端设备扫描到，可以连接。
4. bluetoothManager.setBluetoothScanMode(bluetoothManager.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

## bluetoothManager.getBluetoothScanMode(deprecated)

PhonePC/2in1TabletTVWearable

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.getBluetoothScanMode](js-apis-bluetooth-connection.md#connectiongetbluetoothscanmode)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScanMode](js-apis-bluetoothmanager.md#scanmodedeprecated) | 蓝牙扫描模式。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let scanMode: bluetoothManager.ScanMode = bluetoothManager.getBluetoothScanMode();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.startBluetoothDiscovery(deprecated)

PhonePC/2in1TabletTVWearable

startBluetoothDiscovery(): void

开启蓝牙扫描，可以发现远端设备。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.startBluetoothDiscovery](js-apis-bluetooth-connection.md#connectionstartbluetoothdiscovery)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let deviceId: Array<string>;
3. function onReceiveEvent(data: Array<string>) {
4. deviceId = data;
5. }
6. try {
7. bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
8. bluetoothManager.startBluetoothDiscovery();
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

## bluetoothManager.stopBluetoothDiscovery(deprecated)

PhonePC/2in1TabletTVWearable

stopBluetoothDiscovery(): void

关闭蓝牙扫描。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.stopBluetoothDiscovery](js-apis-bluetooth-connection.md#connectionstopbluetoothdiscovery)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. bluetoothManager.stopBluetoothDiscovery();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## bluetoothManager.setDevicePairingConfirmation(deprecated)

PhonePC/2in1TabletTVWearable

setDevicePairingConfirmation(device: string, accept: boolean): void

设置设备配对请求确认。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.setDevicePairingConfirmation](js-apis-bluetooth-connection.md#connectionsetdevicepairingconfirmation)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| accept | boolean | 是 | 接受配对请求设置为true，否则设置为false。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // 订阅“pinRequired”配对请求事件，收到远端配对请求后设置配对确认
3. function onReceivePinRequiredEvent(data: bluetoothManager.PinRequiredParam) { // data为配对请求的入参，配对请求参数
4. console.info('pin required  = '+ JSON.stringify(data));
5. bluetoothManager.setDevicePairingConfirmation(data.deviceId, true);
6. }
7. try {
8. bluetoothManager.on("pinRequired", onReceivePinRequiredEvent);
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

## bluetoothManager.on('bluetoothDeviceFind')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备发现上报事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('bluetoothDeviceFind')](js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: Array<string>) { // data为蓝牙设备地址集合
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
7. } catch (err) {
8. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
9. }
```

## bluetoothManager.off('bluetoothDeviceFind')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备发现上报事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('bluetoothDeviceFind')](js-apis-bluetooth-connection.md#connectionoffbluetoothdevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bluetoothDeviceFind"字符串，表示蓝牙设备发现事件。 |
| callback | Callback<Array<string>> | 否 | 表示取消订阅蓝牙设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: Array<string>) {
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('bluetoothDeviceFind', onReceiveEvent);
7. bluetoothManager.off('bluetoothDeviceFind', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

## bluetoothManager.on('pinRequired')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅远端蓝牙设备的配对请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('pinRequired')](js-apis-bluetooth-connection.md#connectiononpinrequired)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](js-apis-bluetoothmanager.md#pinrequiredparamdeprecated)> | 是 | 表示回调函数的入参，配对请求。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.PinRequiredParam) { // data为配对请求参数
3. console.info('pin required = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('pinRequired', onReceiveEvent);
7. } catch (err) {
8. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
9. }
```

## bluetoothManager.off('pinRequired')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅远端蓝牙设备的配对请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('pinRequired')](js-apis-bluetooth-connection.md#connectionoffpinrequired)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"pinRequired"字符串，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](js-apis-bluetoothmanager.md#pinrequiredparamdeprecated)> | 否 | 表示取消订阅蓝牙配对请求事件上报，入参为配对请求参数。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.PinRequiredParam) {
3. console.info('pin required = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('pinRequired', onReceiveEvent);
7. bluetoothManager.off('pinRequired', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

## bluetoothManager.on('bondStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态改变事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.on('bondStateChange')](js-apis-bluetooth-connection.md#connectiononbondstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](js-apis-bluetoothmanager.md#bondstateparamdeprecated)> | 是 | 表示回调函数的入参，配对的状态。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.BondStateParam) { // data为回调函数入参，表示配对的状态
3. console.info('pair state = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('bondStateChange', onReceiveEvent);
7. } catch (err) {
8. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
9. }
```

## bluetoothManager.off('bondStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态改变事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.off('bondStateChange')](js-apis-bluetooth-connection.md#connectionoffbondstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"bondStateChange"字符串，表示蓝牙配对状态改变事件。 |
| callback | Callback<[BondStateParam](js-apis-bluetoothmanager.md#bondstateparamdeprecated)> | 否 | 表示取消订阅蓝牙配对状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.BondStateParam) {
3. console.info('bond state = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('bondStateChange', onReceiveEvent);
7. bluetoothManager.off('bondStateChange', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

## bluetoothManager.on('stateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'stateChange', callback: Callback<BluetoothState>): void

订阅蓝牙设备开关状态事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[access.on('stateChange')](js-apis-bluetooth-access.md#accessonstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](js-apis-bluetoothmanager.md#bluetoothstatedeprecated)> | 是 | 表示回调函数的入参，蓝牙状态。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.BluetoothState) {
3. console.info('bluetooth state = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('stateChange', onReceiveEvent);
7. } catch (err) {
8. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
9. }
```

## bluetoothManager.off('stateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'stateChange', callback?: Callback<BluetoothState>): void

取消订阅蓝牙设备开关状态事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[access.off('stateChange')](js-apis-bluetooth-access.md#accessoffstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"stateChange"字符串，表示蓝牙状态改变事件。 |
| callback | Callback<[BluetoothState](js-apis-bluetoothmanager.md#bluetoothstatedeprecated)> | 否 | 表示取消订阅蓝牙状态改变事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.BluetoothState) {
3. console.info('bluetooth state = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.on('stateChange', onReceiveEvent);
7. bluetoothManager.off('stateChange', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

## bluetoothManager.sppListen(deprecated)

PhonePC/2in1TabletTVWearable

sppListen(name: string, option: SppOption, callback: AsyncCallback<number>): void

创建一个服务端监听Socket。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppListen](js-apis-bluetooth-socket.md#socketspplisten)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 服务的名称。 |
| option | [SppOption](js-apis-bluetoothmanager.md#sppoptiondeprecated) | 是 | spp监听配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，服务端Socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let serverNumber = -1;
3. function serverSocket(code: BusinessError, number: number) {
4. console.info(`bluetooth error code: ${code.code}`);
5. if (code.code == 0) {
6. console.info(`bluetooth serverSocket Number: ${number}`);
7. serverNumber = number;
8. }
9. }

11. let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
12. try {
13. bluetoothManager.sppListen('server1', sppOption, serverSocket);
14. } catch (err) {
15. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
16. }
```

## bluetoothManager.sppAccept(deprecated)

PhonePC/2in1TabletTVWearable

sppAccept(serverSocket: number, callback: AsyncCallback<number>): void

服务端监听socket等待客户端连接。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppAccept](js-apis-bluetooth-socket.md#socketsppaccept)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverSocket | number | 是 | 服务端socket的id。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let serverNumber = -1;
3. function serverSocket(code: BusinessError, number: number) {
4. console.info(`bluetooth error code: ${code.code}`);
5. if (code.code == 0) {
6. console.info(`bluetooth serverSocket Number: ${number}`);
7. serverNumber = number;
8. }
9. }
10. let clientNumber = -1;
11. function acceptClientSocket(code: BusinessError, number: number) {
12. console.info(`bluetooth error code: ${code.code}`);
13. if (code.code == 0) {
14. console.info(`bluetooth clientSocket Number: ${number}`);
15. // 获取的clientNumber用作服务端后续读/写操作socket的id。
16. clientNumber = number;
17. }
18. }
19. try {
20. bluetoothManager.sppAccept(serverNumber, acceptClientSocket);
21. } catch (err) {
22. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
23. }
```

## bluetoothManager.sppConnect(deprecated)

PhonePC/2in1TabletTVWearable

sppConnect(device: string, option: SppOption, callback: AsyncCallback<number>): void

客户端向远端设备发起spp连接。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppConnect](js-apis-bluetooth-socket.md#socketsppconnect)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| option | [SppOption](js-apis-bluetoothmanager.md#sppoptiondeprecated) | 是 | spp客户端连接配置参数。 |
| callback | AsyncCallback<number> | 是 | 表示回调函数的入参，客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let clientNumber = -1;
4. function clientSocket(code: BusinessError, number: number) {
5. if (code == null || code.code != 0) {
6. return;
7. }
8. console.info(`bluetooth serverSocket Number: ${number}`);
9. // 获取的clientNumber用作客户端后续读/写操作socket的id。
10. clientNumber = number;
11. }
12. let sppOption: bluetoothManager.SppOption = {uuid: '00001810-0000-1000-8000-00805F9B34FB', secure: false, type: 0};
13. try {
14. bluetoothManager.sppConnect('XX:XX:XX:XX:XX:XX', sppOption, clientSocket);
15. } catch (err) {
16. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
17. }
```

## bluetoothManager.sppCloseServerSocket(deprecated)

PhonePC/2in1TabletTVWearable

sppCloseServerSocket(socket: number): void

关闭服务端监听Socket，入参socket由sppListen接口返回。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppCloseServerSocket](js-apis-bluetooth-socket.md#socketsppcloseserversocket)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 服务端监听socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let serverNumber = -1;
3. function serverSocket(code: BusinessError, number: number) {
4. console.info(`bluetooth error code: ${code.code}`);
5. if (code.code == 0) {
6. console.info(`bluetooth serverSocket Number: ${number}`);
7. serverNumber = number;
8. }
9. }
10. try {
11. bluetoothManager.sppCloseServerSocket(serverNumber);
12. } catch (err) {
13. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
14. }
```

## bluetoothManager.sppCloseClientSocket(deprecated)

PhonePC/2in1TabletTVWearable

sppCloseClientSocket(socket: number): void

关闭客户端socket，入参socket由sppAccept或sppConnect接口获取。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppCloseClientSocket](js-apis-bluetooth-socket.md#socketsppcloseclientsocket)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| socket | number | 是 | 客户端socket的id。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let clientNumber = -1;
3. function clientSocket(code: BusinessError, number: number) {
4. if (code == null || code.code != 0) {
5. return;
6. }
7. console.info(`bluetooth serverSocket Number: ${number}`);
8. // 获取的clientNumber用作客户端后续读/写操作socket的id。
9. clientNumber = number;
10. }
11. try {
12. bluetoothManager.sppCloseClientSocket(clientNumber);
13. } catch (err) {
14. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
15. }
```

## bluetoothManager.sppWrite(deprecated)

PhonePC/2in1TabletTVWearable

sppWrite(clientSocket: number, data: ArrayBuffer): void

通过socket向远端发送数据，入参clientSocket由sppAccept或sppConnect接口获取。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.sppWrite](js-apis-bluetooth-socket.md#socketsppwrite)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| clientSocket | number | 是 | 客户端socket的id。 |
| data | ArrayBuffer | 是 | 写入的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let clientNumber = -1;
3. function clientSocket(code: BusinessError, number: number) {
4. if (code == null || code.code != 0) {
5. return;
6. }
7. console.info(`bluetooth serverSocket Number: ${number}`);
8. // 获取的clientNumber用作客户端后续读/写操作socket的id。
9. clientNumber = number;
10. }
11. let arrayBuffer = new ArrayBuffer(8);
12. let data = new Uint8Array(arrayBuffer);
13. data[0] = 123;
14. try {
15. bluetoothManager.sppWrite(clientNumber, arrayBuffer);
16. } catch (err) {
17. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
18. }
```

## bluetoothManager.on('sppRead')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'sppRead', clientSocket: number, callback: Callback<ArrayBuffer>): void

订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.on('sppRead')](js-apis-bluetooth-socket.md#socketonsppread)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端socket的id。 |
| callback | Callback<ArrayBuffer> | 是 | 表示回调函数的入参，读取到的数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2901054 | IO error. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let clientNumber = -1;
3. function clientSocket(code: BusinessError, number: number) {
4. if (code == null || code.code != 0) {
5. return;
6. }
7. console.info(`bluetooth serverSocket Number: ${number}`);
8. // 获取的clientNumber用作客户端后续读/写操作socket的id。
9. clientNumber = number;
10. }
11. function dataRead(dataBuffer: ArrayBuffer) {
12. let data = new Uint8Array(dataBuffer);
13. console.info(`bluetooth data is: ${data[0]}`);
14. }
15. try {
16. bluetoothManager.on('sppRead', clientNumber, dataRead);
17. } catch (err) {
18. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
19. }
```

## bluetoothManager.off('sppRead')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'sppRead', clientSocket: number, callback?: Callback<ArrayBuffer>): void

取消订阅spp读请求事件，入参clientSocket由sppAccept或sppConnect接口获取。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.off('sppRead')](js-apis-bluetooth-socket.md#socketoffsppread)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"sppRead"字符串，表示spp读请求事件。 |
| clientSocket | number | 是 | 客户端Socket的id。 |
| callback | Callback<ArrayBuffer> | 否 | 表示取消订阅spp读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let clientNumber = -1;
3. function clientSocket(code: BusinessError, number: number) {
4. if (code == null || code.code != 0) {
5. return;
6. }
7. console.info(`bluetooth serverSocket Number: ${number}`);
8. // 获取的clientNumber用作客户端后续读/写操作socket的id。
9. clientNumber = number;
10. }
11. try {
12. bluetoothManager.off('sppRead', clientNumber);
13. } catch (err) {
14. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
15. }
```

## bluetoothManager.getProfileInstance(deprecated)

PhonePC/2in1TabletTVWearable

getProfileInstance(profileId: ProfileId): A2dpSourceProfile | HandsFreeAudioGatewayProfile | HidHostProfile | PanProfile

通过ProfileId，获取profile的对象实例，API9新增了HidHostProfile，PanProfile。

说明

从API version 9开始支持，从API version 10开始废弃。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | [ProfileId](js-apis-bluetoothmanager.md#profileiddeprecated) | 是 | 表示profile的枚举值，例如：PROFILE\_A2DP\_SOURCE。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [A2dpSourceProfile](js-apis-bluetoothmanager.md#a2dpsourceprofile) | [HandsFreeAudioGatewayProfile](js-apis-bluetoothmanager.md#handsfreeaudiogatewayprofiledeprecated) | [HidHostProfile](js-apis-bluetoothmanager.md#hidhostprofiledeprecated) | [PanProfile](js-apis-bluetoothmanager.md#panprofile) | 对应的profile的对象实例，当前支持A2dpSourceProfile/HandsFreeAudioGatewayProfile/HidHostProfile/PanProfile。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST);
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

## BLE

PhonePC/2in1TabletTVWearable

BLE模块提供了对蓝牙操作和管理的方法。

### createGattServer(deprecated)

PhonePC/2in1TabletTVWearable

createGattServer(): GattServer

创建一个可使用的GattServer实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.createGattServer](js-apis-bluetooth-ble.md#blecreategattserver)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattServer](js-apis-bluetoothmanager.md#gattserver) | server端类，使用server端方法之前需要创建该类的实例进行操作。 |

**示例：**

```
1. let gattServer: bluetoothManager.GattServer  = bluetoothManager.BLE.createGattServer();
```

### createGattClientDevice(deprecated)

PhonePC/2in1TabletTVWearable

createGattClientDevice(deviceId: string): GattClientDevice

创建一个可使用的GattClientDevice实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.createGattClientDevice](js-apis-bluetooth-ble.md#blecreategattclientdevice)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattClientDevice](js-apis-bluetoothmanager.md#gattclientdevice) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device: bluetoothManager.GattClientDevice = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

### getConnectedBLEDevices(deprecated)

PhonePC/2in1TabletTVWearable

getConnectedBLEDevices(): Array<string>

获取和当前设备连接的BLE设备。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.getConnectedBLEDevices](js-apis-bluetooth-ble.md#blegetconnectedbledevices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回当前设备作为Server端时连接BLE设备地址集合。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let result: Array<string>  = bluetoothManager.BLE.getConnectedBLEDevices();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

### startBLEScan(deprecated)

PhonePC/2in1TabletTVWearable

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

发起BLE扫描流程。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.startBLEScan](js-apis-bluetooth-ble.md#blestartblescan)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<[ScanFilter](js-apis-bluetoothmanager.md#scanfilterdeprecated)> | 是 | 表示扫描结果过滤策略集合，如果不使用过滤的方式，该参数设置为null。 |
| options | [ScanOptions](js-apis-bluetoothmanager.md#scanoptionsdeprecated) | 否 | 表示扫描的参数配置，可选参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
3. console.info('BLE scan device find result = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.BLE.on("BLEDeviceFind", onReceiveEvent);
7. let scanfilter: bluetoothManager.ScanFilter = {
8. deviceId:"XX:XX:XX:XX:XX:XX",
9. name:"test",
10. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
11. };
12. let scanoptions: bluetoothManager.ScanOptions = {
13. interval: 500,
14. dutyMode: bluetoothManager.ScanDuty.SCAN_MODE_LOW_POWER,
15. matchMode: bluetoothManager.MatchMode.MATCH_MODE_AGGRESSIVE,
16. }
17. bluetoothManager.BLE.startBLEScan([scanfilter], scanoptions);
18. } catch (err) {
19. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
20. }
```

### stopBLEScan(deprecated)

PhonePC/2in1TabletTVWearable

stopBLEScan(): void

停止BLE扫描流程。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.stopBLEScan](js-apis-bluetooth-ble.md#blestopblescan)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. bluetoothManager.BLE.stopBLEScan();
4. } catch (err) {
5. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
6. }
```

### on('BLEDeviceFind')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

订阅BLE设备发现上报事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.on('BLEDeviceFind')](js-apis-bluetooth-ble.md#bleonbledevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](js-apis-bluetoothmanager.md#scanresultdeprecated)>> | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
7. } catch (err) {
8. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
9. }
```

### off('BLEDeviceFind')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

取消订阅BLE设备发现上报事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.off('BLEDeviceFind')](js-apis-bluetooth-ble.md#bleoffbledevicefind)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | Callback<Array<[ScanResult](js-apis-bluetoothmanager.md#scanresultdeprecated)>> | 否 | 表示取消订阅BLE设备发现事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: Array<bluetoothManager.ScanResult>) {
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. bluetoothManager.BLE.on('BLEDeviceFind', onReceiveEvent);
7. bluetoothManager.BLE.off('BLEDeviceFind', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

## BaseProfile

PhonePC/2in1TabletTVWearable

profile基类。

### getConnectionDevices(deprecated)

PhonePC/2in1TabletTVWearable

getConnectionDevices(): Array<string>

获取已连接设备列表。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.getConnectedDevices](js-apis-bluetooth-baseprofile.md#baseprofilegetconnecteddevices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回已连接设备的地址列表。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. try {
3. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
4. let retArray: Array<string> = a2dpSrc.getConnectionDevices();
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### getDeviceState(deprecated)

PhonePC/2in1TabletTVWearable

getDeviceState(device: string): ProfileConnectionState

获取设备profile的连接状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.getConnectionState](js-apis-bluetooth-baseprofile.md#baseprofilegetconnectionstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetoothmanager.md#profileconnectionstatedeprecated) | 返回profile的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. try {
3. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
4. let ret: bluetoothManager.ProfileConnectionState = a2dpSrc.getDeviceState('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

## A2dpSourceProfile

PhonePC/2in1TabletTVWearable

使用A2dpSourceProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[a2dp.A2dpSourceProfile](js-apis-bluetooth-a2dp.md#a2dpsourceprofile)替代。

### connect(deprecated)

PhonePC/2in1TabletTVWearable

connect(device: string): void

发起设备的A2dp服务连接请求。

说明

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. try {
3. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
4. a2dpSrc.connect('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### disconnect(deprecated)

PhonePC/2in1TabletTVWearable

disconnect(device: string): void

断开设备的a2dp服务连接。

说明

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. try {
3. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
4. a2dpSrc.disconnect('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

订阅a2dp连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('a2dp state = '+ JSON.stringify(data));
4. }
5. try {
6. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
7. a2dpSrc.on('connectionStateChange', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

### off('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

取消订阅a2dp连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('a2dp state = '+ JSON.stringify(data));
4. }
5. try {
6. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
7. a2dpSrc.on('connectionStateChange', onReceiveEvent);
8. a2dpSrc.off('connectionStateChange', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### getPlayingState(deprecated)

PhonePC/2in1TabletTVWearable

getPlayingState(device: string): PlayingState

获取设备的播放状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[getPlayingState](js-apis-bluetooth-a2dp.md#getplayingstate)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PlayingState](js-apis-bluetoothmanager.md#playingstatedeprecated) | 远端设备的播放状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let a2dpSrc: bluetoothManager.A2dpSourceProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_A2DP_SOURCE) as bluetoothManager.A2dpSourceProfile;
4. let state: bluetoothManager.PlayingState  = a2dpSrc.getPlayingState('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

## HandsFreeAudioGatewayProfile(deprecated)

PhonePC/2in1TabletTVWearable

使用HandsFreeAudioGatewayProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[hfp.HandsFreeAudioGatewayProfile](js-apis-bluetooth-hfp.md#handsfreeaudiogatewayprofile)替代。

### connect(deprecated)

PhonePC/2in1TabletTVWearable

connect(device: string): void

连接设备的HFP服务。

说明

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. try {
3. let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
4. hfpAg.connect('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### disconnect(deprecated)

PhonePC/2in1TabletTVWearable

disconnect(device: string): void

断开连接设备的HFP服务。

说明

从API version 9开始支持，从API version 10开始废弃。替代接口仅向系统应用开放。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| device | string | 是 | 远端设备地址。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. try {
3. let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as bluetoothManager.HandsFreeAudioGatewayProfile;
4. hfpAg.disconnect('XX:XX:XX:XX:XX:XX');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

订阅HFP连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('hfp state = '+ JSON.stringify(data));
4. }
5. try {
6. let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as
7. bluetoothManager.HandsFreeAudioGatewayProfile;
8. hfpAg.on('connectionStateChange', onReceiveEvent);
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

### off('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

取消订阅HFP连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| **示例：** |  |

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('hfp state = '+ JSON.stringify(data));
4. }
5. try {
6. let hfpAg: bluetoothManager.HandsFreeAudioGatewayProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HANDS_FREE_AUDIO_GATEWAY) as
7. bluetoothManager.HandsFreeAudioGatewayProfile;
8. hfpAg.on('connectionStateChange', onReceiveEvent);
9. hfpAg.off('connectionStateChange', onReceiveEvent);
10. } catch (err) {
11. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
12. }
```

## HidHostProfile(deprecated)

PhonePC/2in1TabletTVWearable

使用HidHostProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

### on('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

订阅HidHost连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('hidHost state = '+ JSON.stringify(data));
4. }
5. try {
6. let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
7. hidHost.on('connectionStateChange', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

### off('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

取消订阅HidHost连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('hidHost state = '+ JSON.stringify(data));
4. }
5. try {
6. let hidHost: bluetoothManager.HidHostProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_HID_HOST) as bluetoothManager.HidHostProfile;
7. hidHost.on('connectionStateChange', onReceiveEvent);
8. hidHost.off('connectionStateChange', onReceiveEvent);
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

## PanProfile

PhonePC/2in1TabletTVWearable

使用PanProfile方法之前需要创建该类的实例进行操作，通过getProfile()方法构造此实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[pan.createPanProfile](js-apis-bluetooth-pan.md#pancreatepanprofile)替代。

### on('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

订阅Pan连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.on('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileonconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 是 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('pan state = '+ JSON.stringify(data));
4. }
5. try {
6. let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
7. panProfile.on('connectionStateChange', onReceiveEvent);
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

### off('connectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)>): void

取消订阅Pan连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.off('connectionStateChange')](js-apis-bluetooth-baseprofile.md#baseprofileoffconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[StateChangeParam](js-apis-bluetoothmanager.md#statechangeparamdeprecated)> | 否 | 表示回调函数的入参。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function onReceiveEvent(data: bluetoothManager.StateChangeParam) {
3. console.info('pan state = '+ JSON.stringify(data));
4. }
5. try {
6. let panProfile: bluetoothManager.PanProfile = bluetoothManager.getProfileInstance(bluetoothManager.ProfileId.PROFILE_PAN_NETWORK) as bluetoothManager.PanProfile;
7. panProfile.on('connectionStateChange', onReceiveEvent);
8. panProfile.off('connectionStateChange', onReceiveEvent);
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

## GattServer

PhonePC/2in1TabletTVWearable

server端类，使用server端方法之前需要创建该类的实例进行操作，通过createGattServer()方法构造此实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer](js-apis-bluetooth-ble.md#gattserver)替代。

### startAdvertising(deprecated)

PhonePC/2in1TabletTVWearable

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

开始发送BLE广播。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | [AdvertiseSetting](js-apis-bluetoothmanager.md#advertisesettingdeprecated) | 是 | BLE广播的相关参数。 |
| advData | [AdvertiseData](js-apis-bluetoothmanager.md#advertisedatadeprecated) | 是 | BLE广播包内容。 |
| advResponse | [AdvertiseData](js-apis-bluetoothmanager.md#advertisedatadeprecated) | 否 | BLE回复扫描请求回复响应。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let manufactureValueBuffer = new Uint8Array(4);
3. manufactureValueBuffer[0] = 1;
4. manufactureValueBuffer[1] = 2;
5. manufactureValueBuffer[2] = 3;
6. manufactureValueBuffer[3] = 4;

8. let serviceValueBuffer = new Uint8Array(4);
9. serviceValueBuffer[0] = 4;
10. serviceValueBuffer[1] = 6;
11. serviceValueBuffer[2] = 7;
12. serviceValueBuffer[3] = 8;
13. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
14. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
15. let gattServer = bluetoothManager.BLE.createGattServer();
16. try {
17. let setting: bluetoothManager.AdvertiseSetting = {
18. interval:150,
19. txPower:0,
20. connectable:true,
21. };
22. let manufactureDataUnit: bluetoothManager.ManufactureData = {
23. manufactureId:4567,
24. manufactureValue:manufactureValueBuffer.buffer
25. };
26. let serviceDataUnit: bluetoothManager.ServiceData = {
27. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
28. serviceValue:serviceValueBuffer.buffer
29. };
30. let advData: bluetoothManager.AdvertiseData = {
31. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
32. manufactureData:[manufactureDataUnit],
33. serviceData:[serviceDataUnit],
34. };
35. let advResponse: bluetoothManager.AdvertiseData = {
36. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
37. manufactureData:[manufactureDataUnit],
38. serviceData:[serviceDataUnit],
39. };
40. gattServer.startAdvertising(setting, advData ,advResponse);
41. } catch (err) {
42. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
43. }
```

### stopAdvertising(deprecated)

PhonePC/2in1TabletTVWearable

stopAdvertising(): void

停止发送BLE广播。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let server = bluetoothManager.BLE.createGattServer();
3. try {
4. server.stopAdvertising();
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### addService(deprecated)

PhonePC/2in1TabletTVWearable

addService(service: GattService): void

server端添加服务。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#addService](js-apis-bluetooth-ble.md#addservice)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | [GattService](js-apis-bluetoothmanager.md#gattservicedeprecated) | 是 | 服务端的service数据。BLE广播的相关参数 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // 创建descriptors
3. let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(8);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 11;
7. let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;

12. // 创建characteristics
13. let characteristics: Array<bluetoothManager.BLECharacteristic> = [];
14. let arrayBufferC = new ArrayBuffer(8);
15. let cccV = new Uint8Array(arrayBufferC);
16. cccV[0] = 1;
17. let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
18. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
19. let characteristicN: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
20. characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
21. characteristics[0] = characteristic;

23. // 创建gattService
24. let gattService: bluetoothManager.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

26. let gattServer  = bluetoothManager.BLE.createGattServer();
27. try {
28. gattServer.addService(gattService);
29. } catch (err) {
30. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
31. }
```

### removeService(deprecated)

PhonePC/2in1TabletTVWearable

removeService(serviceUuid: string): void

删除已添加的服务。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#removeService](js-apis-bluetooth-ble.md#removeservice)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | service的UUID，例如“00001810-0000-1000-8000-00805F9B34FB”。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { BusinessError } from '@ohos.base';
2. let server = bluetoothManager.BLE.createGattServer();
3. try {
4. server.removeService('00001810-0000-1000-8000-00805F9B34FB');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### close(deprecated)

PhonePC/2in1TabletTVWearable

close(): void

关闭服务端功能，去注册server在协议栈的注册，调用该接口后[GattServer](js-apis-bluetoothmanager.md#gattserver)实例将不能再使用。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#close](js-apis-bluetooth-ble.md#close)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let server = bluetoothManager.BLE.createGattServer();
3. try {
4. server.close();
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### notifyCharacteristicChanged(deprecated)

PhonePC/2in1TabletTVWearable

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): void

server端特征值发生变化时，主动通知已连接的client设备。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#notifyCharacteristicChanged](js-apis-bluetooth-ble.md#notifycharacteristicchanged)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 接收通知的client端设备地址，例如“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | [NotifyCharacteristic](js-apis-bluetoothmanager.md#notifycharacteristicdeprecated) | 是 | 通知的特征值数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // 创建descriptors
3. let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(8);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 11;
7. let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;
11. let arrayBufferC = new ArrayBuffer(8);
12. let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
13. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
14. let notifyCharacteristic: bluetoothManager.NotifyCharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001821-0000-1000-8000-00805F9B34FB', characteristicValue: characteristic.characteristicValue, confirm: false};
16. let server = bluetoothManager.BLE.createGattServer();
17. try {
18. server.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacteristic);
19. } catch (err) {
20. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
21. }
```

### sendResponse(deprecated)

PhonePC/2in1TabletTVWearable

sendResponse(serverResponse: ServerResponse): void

server端回复client端的读写请求。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#sendResponse](js-apis-bluetooth-ble.md#sendresponse)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverResponse | [ServerResponse](js-apis-bluetoothmanager.md#serverresponsedeprecated) | 是 | server端回复的响应数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. /* send response */
3. let arrayBufferCCC = new ArrayBuffer(8);
4. let cccValue = new Uint8Array(arrayBufferCCC);
5. cccValue[0] = 1;
6. let serverResponse: bluetoothManager.ServerResponse = {
7. deviceId: 'XX:XX:XX:XX:XX:XX',
8. transId: 0,
9. status: 0,
10. offset: 0,
11. value: arrayBufferCCC,
12. };

14. let gattServer = bluetoothManager.BLE.createGattServer();
15. try {
16. gattServer.sendResponse(serverResponse);
17. } catch (err) {
18. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
19. }
```

### on('characteristicRead')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void

server端订阅特征值读请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('characteristicRead')](js-apis-bluetooth-ble.md#oncharacteristicread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadRequest](js-apis-bluetoothmanager.md#characteristicreadrequestdeprecated)> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let arrayBufferCCC = new ArrayBuffer(8);
3. let cccValue = new Uint8Array(arrayBufferCCC);
4. cccValue[0] = 1;
5. function ReadCharacteristicReq(characteristicReadRequest: bluetoothManager.CharacteristicReadRequest) {
6. let deviceId: string = characteristicReadRequest.deviceId;
7. let transId: number = characteristicReadRequest.transId;
8. let offset: number = characteristicReadRequest.offset;
9. let characteristicUuid: string = characteristicReadRequest.characteristicUuid;

11. let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

13. try {
14. gattServer.sendResponse(serverResponse);
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
17. }
18. }

20. let gattServer = bluetoothManager.BLE.createGattServer();
21. gattServer.on("characteristicRead", ReadCharacteristicReq);
```

### off('characteristicRead')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void

server端取消订阅特征值读请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('characteristicRead')](js-apis-bluetooth-ble.md#offcharacteristicread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicRead"字符串，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadRequest](js-apis-bluetoothmanager.md#characteristicreadrequestdeprecated)> | 否 | 表示取消订阅特征值读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let gattServer = bluetoothManager.BLE.createGattServer();
4. gattServer.off("characteristicRead");
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('characteristicWrite')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void

server端订阅特征值写请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('characteristicWrite')](js-apis-bluetooth-ble.md#oncharacteristicwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteRequest](js-apis-bluetoothmanager.md#characteristicwriterequestdeprecated)> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let arrayBufferCCC = new ArrayBuffer(8);
3. let cccValue = new Uint8Array(arrayBufferCCC);
4. function WriteCharacteristicReq(characteristicWriteRequest: bluetoothManager.CharacteristicWriteRequest) {
5. let deviceId: string = characteristicWriteRequest.deviceId;
6. let transId: number = characteristicWriteRequest.transId;
7. let offset: number = characteristicWriteRequest.offset;
8. let isPrep: boolean = characteristicWriteRequest.isPrep;
9. let needRsp: boolean = characteristicWriteRequest.needRsp;
10. let value: Uint8Array =  new Uint8Array(characteristicWriteRequest.value);
11. let characteristicUuid: string = characteristicWriteRequest.characteristicUuid;

13. cccValue[0] = value[0];
14. let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

16. try {
17. gattServer.sendResponse(serverResponse);
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
21. }

23. let gattServer = bluetoothManager.BLE.createGattServer();
24. gattServer.on("characteristicWrite", WriteCharacteristicReq);
```

### off('characteristicWrite')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void

server端取消订阅特征值写请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('characteristicWrite')](js-apis-bluetooth-ble.md#offcharacteristicwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"characteristicWrite"字符串，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteRequest](js-apis-bluetoothmanager.md#characteristicwriterequestdeprecated)> | 否 | 表示取消订阅特征值写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let gattServer = bluetoothManager.BLE.createGattServer();
4. gattServer.off("characteristicWrite");
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('descriptorRead')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void

server端订阅描述符读请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('descriptorRead')](js-apis-bluetooth-ble.md#ondescriptorread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadRequest](js-apis-bluetoothmanager.md#descriptorreadrequestdeprecated)> | 是 | 表示回调函数的入参，client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferDesc = new ArrayBuffer(8);
3. let descValue = new Uint8Array(arrayBufferDesc);
4. descValue[0] = 1;
5. function ReadDescriptorReq(descriptorReadRequest: bluetoothManager.DescriptorReadRequest) {
6. let deviceId: string = descriptorReadRequest.deviceId;
7. let transId: number = descriptorReadRequest.transId;
8. let offset: number = descriptorReadRequest.offset;
9. let descriptorUuid: string = descriptorReadRequest.descriptorUuid;

11. let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

13. try {
14. gattServer.sendResponse(serverResponse);
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. }
18. }

20. let gattServer = bluetoothManager.BLE.createGattServer();
21. gattServer.on("descriptorRead", ReadDescriptorReq);
```

### off('descriptorRead')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void

server端取消订阅描述符读请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('descriptorRead')](js-apis-bluetooth-ble.md#offdescriptorread)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorRead"字符串，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadRequest](js-apis-bluetoothmanager.md#descriptorreadrequestdeprecated)> | 否 | 表示取消订阅描述符读请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let gattServer = bluetoothManager.BLE.createGattServer();
4. gattServer.off("descriptorRead");
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('descriptorWrite')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void

server端订阅描述符写请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('descriptorWrite')](js-apis-bluetooth-ble.md#ondescriptorwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteRequest](js-apis-bluetoothmanager.md#descriptorwriterequestdeprecated)> | 是 | 表示回调函数的入参，client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let arrayBufferDesc = new ArrayBuffer(8);
3. let descValue = new Uint8Array(arrayBufferDesc);
4. function WriteDescriptorReq(descriptorWriteRequest: bluetoothManager.DescriptorWriteRequest) {
5. let deviceId: string = descriptorWriteRequest.deviceId;
6. let transId: number = descriptorWriteRequest.transId;
7. let offset: number = descriptorWriteRequest.offset;
8. let isPrep: boolean = descriptorWriteRequest.isPrep;
9. let needRsp: boolean = descriptorWriteRequest.needRsp;
10. let value: Uint8Array = new Uint8Array(descriptorWriteRequest.value);
11. let descriptorUuid: string = descriptorWriteRequest.descriptorUuid;

13. descValue[0] = value[0];
14. let serverResponse: bluetoothManager.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

16. try {
17. gattServer.sendResponse(serverResponse);
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
21. }

23. let gattServer = bluetoothManager.BLE.createGattServer();
24. gattServer.on("descriptorWrite", WriteDescriptorReq);
```

### off('descriptorWrite')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void

server端取消订阅描述符写请求事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('descriptorWrite')](js-apis-bluetooth-ble.md#offdescriptorwrite)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"descriptorWrite"字符串，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteRequest](js-apis-bluetoothmanager.md#descriptorwriterequestdeprecated)> | 否 | 表示取消订阅描述符写请求事件上报。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let gattServer = bluetoothManager.BLE.createGattServer();
4. gattServer.off("descriptorWrite");
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('connectStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'connectStateChange', callback: Callback<BLEConnectChangedState>): void

server端订阅BLE连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#on('connectionStateChange')](js-apis-bluetooth-ble.md#onconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetoothmanager.md#bleconnectchangedstatedeprecated)> | 是 | 表示回调函数的入参，连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function Connected(BLEConnectChangedState: bluetoothManager.BLEConnectChangedState) {
3. let deviceId: string = BLEConnectChangedState.deviceId;
4. let status: bluetoothManager.ProfileConnectionState  = BLEConnectChangedState.state;
5. }
6. try {
7. let gattServer = bluetoothManager.BLE.createGattServer();
8. gattServer.on("connectStateChange", Connected);
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

### off('connectStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'connectStateChange', callback?: Callback<BLEConnectChangedState>): void

server端取消订阅BLE连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattServer#off('connectionStateChange')](js-apis-bluetooth-ble.md#offconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"connectStateChange"字符串，表示BLE连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetoothmanager.md#bleconnectchangedstatedeprecated)> | 否 | 表示取消订阅BLE连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let gattServer = bluetoothManager.BLE.createGattServer();
4. gattServer.off("connectStateChange");
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

## GattClientDevice

PhonePC/2in1TabletTVWearable

client端类，使用client端方法之前需要创建该类的实例进行操作，通过createGattClientDevice(deviceId: string)方法构造此实例。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice](js-apis-bluetooth-ble.md#gattclientdevice)替代。

### connect(deprecated)

PhonePC/2in1TabletTVWearable

connect(): void

client端发起连接远端蓝牙低功耗设备。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#connect](js-apis-bluetooth-ble.md#connect)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.connect();
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### disconnect(deprecated)

PhonePC/2in1TabletTVWearable

disconnect(): void

client端断开与远端蓝牙低功耗设备的连接。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#disconnect](js-apis-bluetooth-ble.md#disconnect)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.disconnect();
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### close(deprecated)

PhonePC/2in1TabletTVWearable

close(): void

关闭客户端功能，注销client在协议栈的注册，调用该接口后[GattClientDevice](js-apis-bluetoothmanager.md#gattclientdevice)实例将不能再使用。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#close](js-apis-bluetooth-ble.md#close)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.close();
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### getServices(deprecated)

PhonePC/2in1TabletTVWearable

getServices(callback: AsyncCallback<Array<GattService>>): void

client端获取蓝牙低功耗设备的所有服务，即服务发现。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getServices](js-apis-bluetooth-ble.md#getservices)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[GattService](js-apis-bluetoothmanager.md#gattservicedeprecated)>> | 是 | client进行服务发现，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // callback 模式
3. function getServices(code: BusinessError, gattServices: Array<bluetoothManager.GattService>) {
4. if (code.code == 0) {
5. let services: Array<bluetoothManager.GattService> = gattServices;
6. console.info(`bluetooth code is ${code.code}`);
7. console.info(`bluetooth services size is ${services.length}`);

9. for (let i = 0; i < services.length; i++) {
10. console.info(`bluetooth serviceUuid is ${services[i].serviceUuid}`);
11. }
12. }
13. }

15. try {
16. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
17. device.connect();
18. device.getServices(getServices);
19. } catch (err) {
20. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
21. }
```

### getServices(deprecated)

PhonePC/2in1TabletTVWearable

getServices(): Promise<Array<GattService>>

client端获取蓝牙低功耗设备的所有服务，即服务发现。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getServices](js-apis-bluetooth-ble.md#getservices-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GattService](js-apis-bluetoothmanager.md#gattservicedeprecated)>> | client进行服务发现，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // Promise 模式
3. try {
4. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
5. device.connect();
6. device.getServices().then(result => {
7. console.info("getServices successfully:" + JSON.stringify(result));
8. });
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

### readCharacteristicValue(deprecated)

PhonePC/2in1TabletTVWearable

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

client端读取蓝牙低功耗设备特定服务的特征值。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |
| callback | AsyncCallback<[BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated)> | 是 | client读取特征值，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function readCcc(code: BusinessError, BLECharacteristic: bluetoothManager.BLECharacteristic) {
3. if (code.code != 0) {
4. return;
5. }
6. console.info(`bluetooth characteristic uuid: ${BLECharacteristic.characteristicUuid}`);
7. let value = new Uint8Array(BLECharacteristic.characteristicValue);
8. console.info(`value length: ${value.length}`);
9. }

11. let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
12. let bufferDesc = new ArrayBuffer(8);
13. let descV = new Uint8Array(bufferDesc);
14. descV[0] = 11;
15. let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
16. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
17. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
18. descriptors[0] = descriptor;

20. let bufferCCC = new ArrayBuffer(8);
21. let cccV = new Uint8Array(bufferCCC);
22. cccV[0] = 1;
23. let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
24. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
25. characteristicValue: bufferCCC, descriptors:descriptors};

27. try {
28. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
29. device.readCharacteristicValue(characteristic, readCcc);
30. } catch (err) {
31. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
32. }
```

### readCharacteristicValue(deprecated)

PhonePC/2in1TabletTVWearable

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

client端读取蓝牙低功耗设备特定服务的特征值。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated) | 是 | 待读取的特征值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated)> | client读取特征值，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
3. let bufferDesc = new ArrayBuffer(8);
4. let descV = new Uint8Array(bufferDesc);
5. descV[0] = 11;
6. let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
9. descriptors[0] = descriptor;

11. let bufferCCC = new ArrayBuffer(8);
12. let cccV = new Uint8Array(bufferCCC);
13. cccV[0] = 1;
14. let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
16. characteristicValue: bufferCCC, descriptors:descriptors};

18. try {
19. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
20. device.readCharacteristicValue(characteristic);
21. } catch (err) {
22. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
23. }
```

### readDescriptorValue(deprecated)

PhonePC/2in1TabletTVWearable

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

client端读取蓝牙低功耗设备特定的特征包含的描述符。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated) | 是 | 待读取的描述符。 |
| callback | AsyncCallback<[BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated)> | 是 | client读取描述符，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function readDesc(code: BusinessError, BLEDescriptor: bluetoothManager.BLEDescriptor) {
3. if (code.code != 0) {
4. return;
5. }
6. console.info(`bluetooth descriptor uuid: ${BLEDescriptor.descriptorUuid}`);
7. let value = new Uint8Array(BLEDescriptor.descriptorValue);
8. }

10. let bufferDesc = new ArrayBuffer(8);
11. let descV = new Uint8Array(bufferDesc);
12. descV[0] = 11;
13. let descriptor: bluetoothManager.BLEDescriptor = {
14. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
16. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
17. descriptorValue: bufferDesc
18. };
19. try {
20. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
21. device.readDescriptorValue(descriptor, readDesc);
22. } catch (err) {
23. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
24. }
```

### readDescriptorValue(deprecated)

PhonePC/2in1TabletTVWearable

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

client端读取蓝牙低功耗设备特定的特征包含的描述符。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated) | 是 | 待读取的描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated)> | client读取描述符，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901000 | Read forbidden. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let bufferDesc = new ArrayBuffer(8);
3. let descV = new Uint8Array(bufferDesc);
4. descV[0] = 11;
5. let descriptor: bluetoothManager.BLEDescriptor = {
6. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
9. descriptorValue: bufferDesc
10. };
11. try {
12. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
13. device.readDescriptorValue(descriptor);
14. } catch (err) {
15. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
16. }
```

### writeCharacteristicValue(deprecated)

PhonePC/2in1TabletTVWearable

writeCharacteristicValue(characteristic: BLECharacteristic): void

client端向低功耗蓝牙设备写入特定的特征值。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated) | 是 | 蓝牙设备特征对应的二进制值及其它参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
3. let bufferDesc = new ArrayBuffer(8);
4. let descV = new Uint8Array(bufferDesc);
5. descV[0] = 11;
6. let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
9. descriptors[0] = descriptor;

11. let bufferCCC = new ArrayBuffer(8);
12. let cccV = new Uint8Array(bufferCCC);
13. cccV[0] = 1;
14. let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
16. characteristicValue: bufferCCC, descriptors:descriptors};
17. try {
18. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
19. device.writeCharacteristicValue(characteristic);
20. } catch (err) {
21. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
22. }
```

### writeDescriptorValue(deprecated)

PhonePC/2in1TabletTVWearable

writeDescriptorValue(descriptor: BLEDescriptor): void

client端向低功耗蓝牙设备特定的描述符写入二进制数据。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated) | 是 | 蓝牙设备描述符的二进制值及其它参数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2901001 | Write forbidden. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. let bufferDesc = new ArrayBuffer(8);
3. let descV = new Uint8Array(bufferDesc);
4. descV[0] = 22;
5. let descriptor: bluetoothManager.BLEDescriptor = {
6. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB',
9. descriptorValue: bufferDesc
10. };
11. try {
12. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
13. device.writeDescriptorValue(descriptor);
14. } catch (err) {
15. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
16. }
```

### setBLEMtuSize(deprecated)

PhonePC/2in1TabletTVWearable

setBLEMtuSize(mtu: number): void

client协商远端蓝牙低功耗设备的最大传输单元（Maximum Transmission Unit, MTU），调用[connect](js-apis-bluetoothmanager.md#connectdeprecated-1)接口连接成功后才能使用。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#setBLEMtuSize](js-apis-bluetooth-ble.md#setblemtusize)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mtu | number | 是 | 设置范围为22~512字节。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.setBLEMtuSize(128);
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### setNotifyCharacteristicChanged(deprecated)

PhonePC/2in1TabletTVWearable

setNotifyCharacteristicChanged(characteristic: BLECharacteristic, enable: boolean): void

向服务端发送设置通知此特征值请求。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated) | 是 | 蓝牙低功耗特征。 |
| enable | boolean | 是 | 启用接收notify设置为true，否则设置为false。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // 创建descriptors
3. let descriptors: Array<bluetoothManager.BLEDescriptor> = [];
4. let bufferDesc = new ArrayBuffer(8);
5. let descV = new Uint8Array(bufferDesc);
6. descV[0] = 11;
7. let descriptor: bluetoothManager.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002903-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
10. descriptors[0] = descriptor;

12. let bufferCCC = new ArrayBuffer(8);
13. let cccV = new Uint8Array(bufferCCC);
14. cccV[0] = 1;
15. let characteristic: bluetoothManager.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
16. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
17. characteristicValue: bufferCCC, descriptors:descriptors};
18. try {
19. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
20. device.setNotifyCharacteristicChanged(characteristic, false);
21. } catch (err) {
22. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
23. }
```

### on('BLECharacteristicChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

订阅蓝牙低功耗设备的特征值变化事件。需要先调用setNotifyCharacteristicChanged接口才能接收server端的通知。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#on('BLECharacteristicChange')](js-apis-bluetooth-ble.md#onblecharacteristicchange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated)> | 是 | 表示蓝牙低功耗设备的特征值变化事件的回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. function CharacteristicChange(characteristicChangeReq: ble.BLECharacteristic) {
3. let serviceUuid: string = characteristicChangeReq.serviceUuid;
4. let characteristicUuid: string = characteristicChangeReq.characteristicUuid;
5. let value: Uint8Array = new Uint8Array(characteristicChangeReq.characteristicValue);
6. }
7. try {
8. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
9. device.on('BLECharacteristicChange', CharacteristicChange);
10. } catch (err) {
11. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
12. }
```

### off('BLECharacteristicChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

取消订阅蓝牙低功耗设备的特征值变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#off('BLECharacteristicChange')](js-apis-bluetooth-ble.md#offblecharacteristicchange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLECharacteristicChange"字符串，表示特征值变化事件。 |
| callback | Callback<[BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated)> | 否 | 表示取消订阅蓝牙低功耗设备的特征值变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.off('BLECharacteristicChange');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('BLEConnectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectChangedState>): void

client端订阅蓝牙低功耗设备的连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#on('BLEConnectionStateChange')](js-apis-bluetooth-ble.md#onbleconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetoothmanager.md#bleconnectchangedstatedeprecated)> | 是 | 表示连接状态，已连接或断开。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function ConnectStateChanged(state: bluetoothManager.BLEConnectChangedState) {
3. console.info('bluetooth connect state changed');
4. let connectState: bluetoothManager.ProfileConnectionState = state.state;
5. }
6. try {
7. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
8. device.on('BLEConnectionStateChange', ConnectStateChanged);
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

### off('BLEConnectionStateChange')(deprecated)

PhonePC/2in1TabletTVWearable

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectChangedState>): void

取消订阅蓝牙低功耗设备的连接状态变化事件。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#off('BLEConnectionStateChange')](js-apis-bluetooth-ble.md#offbleconnectionstatechange)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 填写"BLEConnectionStateChange"字符串，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectChangedState](js-apis-bluetoothmanager.md#bleconnectchangedstatedeprecated)> | 否 | 表示取消订阅蓝牙低功耗设备的连接状态变化事件。不填该参数则取消订阅该type对应的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. try {
3. let device = bluetoothManager.BLE.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.off('BLEConnectionStateChange');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### getDeviceName(deprecated)

PhonePC/2in1TabletTVWearable

getDeviceName(callback: AsyncCallback<string>): void

client获取远端蓝牙低功耗设备名。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getDeviceName](js-apis-bluetooth-ble.md#getdevicename)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | client获取对端server设备名，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // callback
3. try {
4. let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
5. gattClient.connect();
6. let deviceName = gattClient.getDeviceName((err, data)=> {
7. console.info('device name err ' + JSON.stringify(err));
8. console.info('device name' + JSON.stringify(data));
9. })
10. } catch (err) {
11. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
12. }
```

### getDeviceName(deprecated)

PhonePC/2in1TabletTVWearable

getDeviceName(): Promise<string>

client获取远端蓝牙低功耗设备名。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getDeviceName](js-apis-bluetooth-ble.md#getdevicename-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | client获取对端server设备名，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // promise
3. try {
4. let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
5. gattClient.connect();
6. let deviceName = gattClient.getDeviceName().then((data) => {
7. console.info('device name' + JSON.stringify(data));
8. })
9. } catch (err) {
10. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
11. }
```

### getRssiValue(deprecated)

PhonePC/2in1TabletTVWearable

getRssiValue(callback: AsyncCallback<number>): void

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](js-apis-bluetoothmanager.md#connectdeprecated-1)接口连接成功后才能使用。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getRssiValue](js-apis-bluetooth-ble.md#getrssivalue)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 返回信号强度，单位 dBm，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // callback
3. try {
4. let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
5. gattClient.connect();
6. let rssi = gattClient.getRssiValue((err: BusinessError, data: number)=> {
7. console.info('rssi err ' + JSON.stringify(err));
8. console.info('rssi value' + JSON.stringify(data));
9. })
10. } catch (err) {
11. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
12. }
```

### getRssiValue(deprecated)

PhonePC/2in1TabletTVWearable

getRssiValue(): Promise<number>

client获取远端蓝牙低功耗设备的信号强度 (Received Signal Strength Indication, RSSI)，调用[connect](js-apis-bluetoothmanager.md#connectdeprecated-1)接口连接成功后才能使用。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattClientDevice#getRssiValue](js-apis-bluetooth-ble.md#getrssivalue-1)替代。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 返回信号强度，单位 dBm，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@ohos.base';
2. // promise
3. try {
4. let gattClient = bluetoothManager.BLE.createGattClientDevice("XX:XX:XX:XX:XX:XX");
5. let rssi = gattClient.getRssiValue().then((data: number) => {
6. console.info('rssi' + JSON.stringify(data));
7. })
8. } catch (err) {
9. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
10. }
```

## ScanMode(deprecated)

PhonePC/2in1TabletTVWearable

枚举，扫描模式。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.ScanMode](js-apis-bluetooth-connection.md#scanmode)替代。

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

PhonePC/2in1TabletTVWearable

枚举，配对状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.BondState](js-apis-bluetooth-connection.md#bondstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOND\_STATE\_INVALID | 0 | 无效的配对。 |
| BOND\_STATE\_BONDING | 1 | 正在配对。 |
| BOND\_STATE\_BONDED | 2 | 已配对。 |

## SppOption(deprecated)

PhonePC/2in1TabletTVWearable

描述spp的配置参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.SppOption](js-apis-bluetooth-socket.md#sppoptions)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| uuid | string | 否 | 否 | spp单据的uuid。 |
| secure | boolean | 否 | 否 | 是否是安全通道。 |
| type | [SppType](js-apis-bluetoothmanager.md#spptypedeprecated) | 否 | 否 | Spp链路类型。 |

## SppType(deprecated)

PhonePC/2in1TabletTVWearable

枚举，Spp链路类型。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[socket.SppType](js-apis-bluetooth-socket.md#spptype)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SPP\_RFCOMM | 0 | 表示rfcomm链路类型。 |

## GattService(deprecated)

PhonePC/2in1TabletTVWearable

描述service的接口参数定义。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.GattService](js-apis-bluetooth-ble.md#gattservice)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 否 | 否 | 如果是主服务设置为true，否则设置为false。 |
| characteristics | Array<[BLECharacteristic](js-apis-bluetoothmanager.md#blecharacteristicdeprecated)> | 否 | 否 | 当前服务包含的特征列表。 |
| includeServices | Array<[GattService](js-apis-bluetoothmanager.md#gattservicedeprecated)> | 否 | 是 | 当前服务依赖的其它服务。 |

## BLECharacteristic(deprecated)

PhonePC/2in1TabletTVWearable

描述characteristic的接口参数定义。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| descriptors | Array<[BLEDescriptor](js-apis-bluetoothmanager.md#bledescriptordeprecated)> | 否 | 否 | 特定特征的描述符列表。 |

## BLEDescriptor(deprecated)

PhonePC/2in1TabletTVWearable

描述descriptor的接口参数定义。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| descriptorUuid | string | 否 | 否 | 描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| descriptorValue | ArrayBuffer | 否 | 否 | 描述符对应的二进制值。 |

## NotifyCharacteristic(deprecated)

PhonePC/2in1TabletTVWearable

描述server端特征值变化时发送的特征通知参数定义。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.NotifyCharacteristic](js-apis-bluetooth-ble.md#notifycharacteristic)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征对应的二进制值。 |
| confirm | boolean | 否 | 否 | 如果是notification则对端回复确认设置为true，如果是indication则对端不需要回复确认设置为false。 |

## CharacteristicReadRequest(deprecated)

PhonePC/2in1TabletTVWearable

描述server端订阅后收到的特征值读请求事件参数结构。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.CharacteristicReadRequest](js-apis-bluetooth-ble.md#characteristicreadrequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送特征值读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读特征值数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## CharacteristicWriteRequest(deprecated)

PhonePC/2in1TabletTVWearable

描述server端订阅后收到的特征值写请求事件参数结构。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.CharacteristicWriteRequest](js-apis-bluetooth-ble.md#characteristicwriterequest)替代。

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

## DescriptorReadRequest(deprecated)

PhonePC/2in1TabletTVWearable

描述server端订阅后收到的描述符读请求事件参数结构。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.DescriptorReadRequest](js-apis-bluetooth-ble.md#descriptorreadrequest)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示发送描述符读请求的远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示读请求的传输ID，server端回复响应时需填写相同的传输ID。 |
| offset | number | 否 | 否 | 表示读描述符数据的起始位置。例如：k表示从第k个字节开始读，server端回复响应时需填写相同的offset。 |
| descriptorUuid | string | 否 | 否 | 表示描述符（descriptor）的UUID，例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 特定特征（characteristic）的UUID，例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特定服务（service）的UUID，例如：00001888-0000-1000-8000-00805f9b34fb。 |

## DescriptorWriteRequest(deprecated)

PhonePC/2in1TabletTVWearable

描述server端订阅后收到的描述符写请求事件参数结构。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.DescriptorWriteRequest](js-apis-bluetooth-ble.md#descriptorwriterequest)替代。

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

PhonePC/2in1TabletTVWearable

描述server端回复client端读/写请求的响应参数结构。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ServerResponse](js-apis-bluetooth-ble.md#serverresponse)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 表示请求的传输ID，与订阅的读/写请求事件携带的ID保持一致。 |
| status | number | 否 | 否 | 表示响应的状态，设置为0即可，表示正常。 |
| offset | number | 否 | 否 | 表示请求的读/写起始位置，与订阅的读/写请求事件携带的offset保持一致。 |
| value | ArrayBuffer | 否 | 否 | 表示回复响应的二进制数据。 |

## BLEConnectChangedState(deprecated)

PhonePC/2in1TabletTVWearable

描述Gatt profile连接状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[BLEConnectionChangeState](js-apis-bluetooth-ble.md#bleconnectionchangestate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示远端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| state | [ProfileConnectionState](js-apis-bluetoothmanager.md#profileconnectionstatedeprecated) | 否 | 否 | 表示BLE连接状态的枚举。 |

## ProfileConnectionState(deprecated)

PhonePC/2in1TabletTVWearable

枚举，蓝牙设备的profile连接状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_DISCONNECTED | 0 | 表示profile已断连。 |
| STATE\_CONNECTING | 1 | 表示profile正在连接。 |
| STATE\_CONNECTED | 2 | 表示profile已连接。 |
| STATE\_DISCONNECTING | 3 | 表示profile正在断连。 |

## ScanFilter(deprecated)

PhonePC/2in1TabletTVWearable

扫描过滤参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanFilter](js-apis-bluetooth-ble.md#scanfilter)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 表示过滤的BLE设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| name | string | 否 | 是 | 表示过滤的BLE设备名。 |
| serviceUuid | string | 否 | 是 | 表示过滤包含该UUID服务的设备，例如：00001888-0000-1000-8000-00805f9b34fb。 |
| serviceUuidMask | string | 否 | 是 | 表示过滤包含该UUID服务掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。 |
| serviceSolicitationUuid | string | 否 | 是 | 表示过滤包含该UUID服务请求的设备，例如：00001888-0000-1000-8000-00805F9B34FB。 |
| serviceSolicitationUuidMask | string | 否 | 是 | 表示过滤包含该UUID服务请求掩码的设备，例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。 |
| serviceData | ArrayBuffer | 否 | 是 | 表示过滤包含该服务相关数据的设备，例如：[0x90,0x00,0xF1,0xF2]。 |
| serviceDataMask | ArrayBuffer | 否 | 是 | 表示过滤包含该服务相关数据掩码的设备，例如：[0xFF,0xFF,0xFF,0xFF]。 |
| manufactureId | number | 否 | 是 | 表示过滤包含该制造商ID的设备，例如：0x0006。 |
| manufactureData | ArrayBuffer | 否 | 是 | 表示过滤包含该制造商相关数据的设备，例如：[0x1F,0x2F,0x3F]。 |
| manufactureDataMask | ArrayBuffer | 否 | 是 | 表示过滤包含该制造商相关数据掩码的设备，例如：[0xFF,0xFF,0xFF]。 |

## ScanOptions(deprecated)

PhonePC/2in1TabletTVWearable

扫描的配置参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanOptions](js-apis-bluetooth-ble.md#scanoptions)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 表示扫描结果上报延迟时间，默认值为0。 |
| dutyMode | [ScanDuty](js-apis-bluetoothmanager.md#scandutydeprecated) | 否 | 是 | 表示扫描模式，默认值为SCAN\_MODE\_LOW\_POWER。 |
| matchMode | [MatchMode](js-apis-bluetoothmanager.md#matchmodedeprecated) | 否 | 是 | 表示硬件的过滤匹配模式，默认值为MATCH\_MODE\_AGGRESSIVE。 |

## ScanDuty(deprecated)

PhonePC/2in1TabletTVWearable

枚举，扫描模式。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanDuty](js-apis-bluetooth-ble.md#scanduty)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN\_MODE\_LOW\_POWER | 0 | 表示低功耗模式，默认值。 |
| SCAN\_MODE\_BALANCED | 1 | 表示均衡模式。 |
| SCAN\_MODE\_LOW\_LATENCY | 2 | 表示低延迟模式。 |

## MatchMode(deprecated)

PhonePC/2in1TabletTVWearable

枚举，硬件过滤匹配模式。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.MatchMode](js-apis-bluetooth-ble.md#matchmode)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MATCH\_MODE\_AGGRESSIVE | 1 | 表示硬件上报扫描结果门限较低，比如扫描到的功率较低或者一段时间扫描到的次数较少也触发上报，默认值。 |
| MATCH\_MODE\_STICKY | 2 | 表示硬件上报扫描结果门限较高，更高的功率门限以及扫描到多次才会上报。 |

## ScanResult(deprecated)

PhonePC/2in1TabletTVWearable

扫描结果上报数据。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ScanResult](js-apis-bluetooth-ble.md#scanresult)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示扫描到的设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| rssi | number | 否 | 否 | 表示扫描到的设备的rssi值。 |
| data | ArrayBuffer | 否 | 否 | 表示扫描到的设备发送的广播包。 |

## BluetoothState(deprecated)

PhonePC/2in1TabletTVWearable

枚举，蓝牙开关状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[access.BluetoothState](js-apis-bluetooth-access.md#bluetoothstate)替代。

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

PhonePC/2in1TabletTVWearable

描述蓝牙低功耗设备发送广播的参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.AdvertiseSetting](js-apis-bluetooth-ble.md#advertisesetting)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 表示广播间隔，最小值设置32个slot表示20ms，最大值设置16384个slot，默认值设置为1600个slot表示1s。 |
| txPower | number | 否 | 是 | 表示发送功率，最小值设置-127，最大值设置1，默认值设置-7，单位dbm。 |
| connectable | boolean | 否 | 是 | 表示是否是可连接广播，默认值设置为true。 |

## AdvertiseData(deprecated)

PhonePC/2in1TabletTVWearable

描述BLE广播数据包的内容。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.AdvertiseData](js-apis-bluetooth-ble.md#advertisedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 否 | 表示要广播的服务 UUID 列表。 |
| manufactureData | Array<[ManufactureData](js-apis-bluetoothmanager.md#manufacturedatadeprecated)> | 否 | 否 | 表示要广播的广播的制造商信息列表。 |
| serviceData | Array<[ServiceData](js-apis-bluetoothmanager.md#servicedatadeprecated)> | 否 | 否 | 表示要广播的服务数据列表。 |

## ManufactureData(deprecated)

PhonePC/2in1TabletTVWearable

描述BLE广播数据包的内容。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ManufactureData](js-apis-bluetooth-ble.md#manufacturedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufactureId | number | 否 | 否 | 表示制造商的ID，由蓝牙SIG分配。 |
| manufactureValue | ArrayBuffer | 否 | 否 | 表示制造商发送的制造商数据。 |

## ServiceData(deprecated)

PhonePC/2in1TabletTVWearable

描述广播包中服务数据内容。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[ble.ServiceData](js-apis-bluetooth-ble.md#servicedata)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 表示服务的UUID。 |
| serviceValue | ArrayBuffer | 否 | 否 | 表示服务数据。 |

## PinRequiredParam(deprecated)

PhonePC/2in1TabletTVWearable

描述配对请求参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.PinRequiredParam](js-apis-bluetooth-connection.md#pinrequiredparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| pinCode | string | 否 | 否 | 表示要配对的密钥。 |

## BondStateParam(deprecated)

PhonePC/2in1TabletTVWearable

描述配对状态参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.BondStateParam](js-apis-bluetooth-connection.md#bondstateparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示要配对的设备ID。 |
| state | BondState | 否 | 否 | 表示配对设备的状态。 |

## StateChangeParam(deprecated)

PhonePC/2in1TabletTVWearable

描述profile状态改变参数。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[baseProfile.StateChangeParam](js-apis-bluetooth-baseprofile.md#statechangeparam)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 表示蓝牙设备地址。 |
| state | [ProfileConnectionState](js-apis-bluetoothmanager.md#profileconnectionstatedeprecated) | 否 | 否 | 表示蓝牙设备的profile连接状态。 |

## DeviceClass(deprecated)

PhonePC/2in1TabletTVWearable

描述蓝牙设备的类别。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[connection.DeviceClass](js-apis-bluetooth-connection.md#deviceclass)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| majorClass | [MajorClass](js-apis-bluetoothmanager.md#majorclassdeprecated) | 否 | 否 | 表示蓝牙设备主要类别的枚举。 |
| majorMinorClass | [MajorMinorClass](js-apis-bluetoothmanager.md#majorminorclassdeprecated) | 否 | 否 | 表示主要次要蓝牙设备类别的枚举。 |
| classOfDevice | number | 否 | 否 | 表示设备类别。 |

## MajorClass(deprecated)

PhonePC/2in1TabletTVWearable

枚举，蓝牙设备主要类别。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.MajorClass](js-apis-bluetooth-constant.md#majorclass)替代。

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

PhonePC/2in1TabletTVWearable

枚举，主要次要蓝牙设备类别。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.MajorMinorClass](js-apis-bluetooth-constant.md#majorminorclass)替代。

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
| HEALTH\_STEP\_COUNTER | 0x0920 | 表示阶梯计数器健康设备。 |
| HEALTH\_BODY\_COMPOSITION\_ANALYZER | 0x0924 | 表示身体成分分析仪健康设备。 |
| HEALTH\_PEAK\_FLOW\_MONITOR | 0x0928 | 表示湿度计健康设备。 |
| HEALTH\_MEDICATION\_MONITOR | 0x092C | 表示药物监视仪健康设备。 |
| HEALTH\_KNEE\_PROSTHESIS | 0x0930 | 表示膝盖假肢健康设备。 |
| HEALTH\_ANKLE\_PROSTHESIS | 0x0934 | 表示脚踝假肢健康设备。 |
| HEALTH\_GENERIC\_HEALTH\_MANAGER | 0x0938 | 表示通用健康管理设备。 |
| HEALTH\_PERSONAL\_MOBILITY\_DEVICE | 0x093C | 表示个人移动健康设备。 |

## PlayingState(deprecated)

PhonePC/2in1TabletTVWearable

枚举，蓝牙A2DP 播放状态。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[a2dp.PlayingState](js-apis-bluetooth-a2dp.md#playingstate)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_NOT\_PLAYING | 0x0000 | 表示未播放。 |
| STATE\_PLAYING | 0x0001 | 表示正在播放。 |

## ProfileId(deprecated)

PhonePC/2in1TabletTVWearable

蓝牙profile枚举，API9新增PROFILE\_HID\_HOST，PROFILE\_PAN\_NETWORK。

说明

从API version 9开始支持，从API version 10开始废弃。建议使用[constant.ProfileId](js-apis-bluetooth-constant.md#profileid)替代。

**系统能力**：SystemCapability.Communication.Bluetooth.Core。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PROFILE\_A2DP\_SOURCE | 1 | 表示A2DP profile。 |
| PROFILE\_HANDS\_FREE\_AUDIO\_GATEWAY | 4 | 表示HFP profile。 |
| PROFILE\_HID\_HOST | 6 | 表示HID profile。 |
| PROFILE\_PAN\_NETWORK | 7 | 表示PAN profile。 |
