---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-connection
title: @ohos.bluetooth.connection (蓝牙connection模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.connection (蓝牙connection模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0ec0b78ccf26fecfdb7eb809d9d785e2130bfc5f8f347cc28e3b47050a6f3cd5
---

connection模块提供了蓝牙设备的配对、连接及状态查询等能力。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { connection } from '@kit.ConnectivityKit';
```

## ProfileConnectionState

PhonePC/2in1TabletTVWearable

type ProfileConnectionState = constant.ProfileConnectionState

蓝牙设备的Profile协议连接状态。Profile协议包括A2DP（Advanced Audio Distribution Profile）、HFP（Hands-Free Profile）和HID（Human Interface Device）等。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 蓝牙设备的Profile协议连接状态。 |

## ProfileId

PhonePC/2in1TabletTVWearable

type ProfileId = constant.ProfileId

枚举，蓝牙Profile协议。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.ProfileId](js-apis-bluetooth-constant.md#profileid) | 蓝牙Profile协议的枚举。 |

## ProfileUuids12+

PhonePC/2in1TabletTVWearable

type ProfileUuids = constant.ProfileUuids

蓝牙Profile协议的UUID。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.ProfileUuids](js-apis-bluetooth-constant.md#profileuuids12) | 蓝牙Profile协议的UUID。 |

## MajorClass

PhonePC/2in1TabletTVWearable

type MajorClass = constant.MajorClass

蓝牙设备的主要类型。蓝牙标准协议字段。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.MajorClass](js-apis-bluetooth-constant.md#majorclass) | 蓝牙设备的主要类型。 |

## MajorMinorClass

PhonePC/2in1TabletTVWearable

type MajorMinorClass = constant.MajorMinorClass

蓝牙设备的子类型，在[MajorClass](js-apis-bluetooth-constant.md#majorclass)基础上进一步细分的类型。蓝牙标准协议字段。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.MajorMinorClass](js-apis-bluetooth-constant.md#majorminorclass) | 蓝牙设备的子类型。 |

## BluetoothAddress21+

PhonePC/2in1TabletTVWearable

type BluetoothAddress = common.BluetoothAddress

描述蓝牙设备地址信息的参数结构，包括地址与地址类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [common.BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 蓝牙设备的地址信息。 |

## connection.pairDevice

PhonePC/2in1TabletTVWearable

pairDevice(deviceId: string, callback: AsyncCallback<void>): void

主动发起与对端蓝牙设备的配对流程。使用Callback异步回调。

* 若开发者不知道目标设备的[地址类型](js-apis-bluetooth-common.md#bluetoothaddresstype)，建议调用此接口发起配对。
* 蓝牙配对状态通过[on('bondStateChange')](js-apis-bluetooth-connection.md#connectiononbondstatechange)的回调结果获取。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 需要配对的对端蓝牙设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当配对成功，err为undefined，否则为错误对象。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // callback
3. try {
4. connection.pairDevice('11:22:33:44:55:66', (err: BusinessError) => {
5. console.info('pairDevice, device name err:' + JSON.stringify(err));
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.pairDevice

PhonePC/2in1TabletTVWearable

pairDevice(deviceId: string): Promise<void>

主动发起与对端蓝牙设备的配对流程。使用Promise异步回调。

* 若开发者不知道目标设备的[地址类型](js-apis-bluetooth-common.md#bluetoothaddresstype)，建议调用此接口发起配对。
* 蓝牙配对状态通过[on('bondStateChange')](js-apis-bluetooth-connection.md#connectiononbondstatechange)的回调结果获取。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 需要配对的对端蓝牙设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // promise
3. try {
4. connection.pairDevice('11:22:33:44:55:66').then(() => {
5. console.info('pairDevice');
6. }, (error: BusinessError) => {
7. console.error('pairDevice: errCode:' + error.code + ',errMessage' + error.message);
8. })

10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## connection.pairDevice21+

PhonePC/2in1TabletTVWearable

pairDevice(deviceId: BluetoothAddress): Promise<void>

主动发起与对端蓝牙设备的配对流程。使用Promise异步回调。

* 若开发者已知目标设备的MAC地址及[地址类型](js-apis-bluetooth-common.md#bluetoothaddresstype)，建议调用此接口发起配对。
* 蓝牙配对状态通过[on('bondStateChange')](js-apis-bluetooth-connection.md#connectiononbondstatechange)的回调结果获取。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | [BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 是 | 需要配对的对端蓝牙设备地址信息，包括地址与地址类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.ConnectivityKit';
3. // promise
4. try {
5. let btAddr: common.BluetoothAddress = {
6. "address": '11:22:33:44:55:66', // 目标设备的实际MAC地址或虚拟MAC地址
7. "addressType": common.BluetoothAddressType.REAL, // 相应的地址类型
8. }
9. connection.pairDevice(btAddr).then(() => {
10. console.info('pairDevice');
11. }, (error: BusinessError) => {
12. console.error('errCode: ' + error.code + ', errMessage' + error.message);
13. });
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

## connection.getRemoteDeviceName

PhonePC/2in1TabletTVWearable

getRemoteDeviceName(deviceId: string): string

获取对端蓝牙设备的名称。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备名称。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let remoteDeviceName: string = connection.getRemoteDeviceName('XX:XX:XX:XX:XX:XX');
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.getRemoteDeviceName16+

PhonePC/2in1TabletTVWearable

getRemoteDeviceName(deviceId: string, alias?: boolean): string

获取对端蓝牙设备的名称，其中alias为可选参数。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备名称。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 16开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |
| alias | boolean | 否 | 表示是否获取对端蓝牙设备别名。  - 如果携带alias，则根据alias判断是否获取对端蓝牙设备别名：true表示获取对端蓝牙设备别名，false表示获取对端蓝牙设备原始名称。  - 如果未携带alias，则默认值为true，返回对端蓝牙设备别名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 以字符串格式返回设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Failed to obtain the name or alias of the peer Bluetooth device. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let remoteDeviceName: string = connection.getRemoteDeviceName('XX:XX:XX:XX:XX:XX', true);
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.getRemoteDeviceClass

PhonePC/2in1TabletTVWearable

getRemoteDeviceClass(deviceId: string): DeviceClass

获取对端蓝牙设备的类别。

* 从API version 18开始，此接口不再校验ohos.permission.ACCESS\_BLUETOOTH权限。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备类别信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DeviceClass](js-apis-bluetooth-connection.md#deviceclass) | 对端设备的类别。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let remoteDeviceClass: connection.DeviceClass = connection.getRemoteDeviceClass('XX:XX:XX:XX:XX:XX');
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.getRemoteDeviceTransport20+

PhonePC/2in1TabletTVWearable

getRemoteDeviceTransport(deviceId: string): BluetoothTransport

获取对端蓝牙设备的传输类型。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取设备的传输类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BluetoothTransport](js-apis-bluetooth-connection.md#bluetoothtransport) | 对端设备的传输类型。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Get transport failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let transport: connection.BluetoothTransport = connection.getRemoteDeviceTransport('XX:XX:XX:XX:XX:XX');
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.getRemoteProfileUuids12+

PhonePC/2in1TabletTVWearable

getRemoteProfileUuids(deviceId: string, callback: AsyncCallback<Array<ProfileUuids>>): void

获取对端蓝牙设备的Profile协议能力，通过UUID区分。使用Callback异步回调。

* 建议仅对已配对的设备调用该方法。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile协议能力。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| callback | AsyncCallback<Array<[ProfileUuids](js-apis-bluetooth-constant.md#profileuuids12)>> | 是 | 回调函数。当获取UUID成功，err为undefined，获取到的是Profile协议能力集合；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. connection.getRemoteProfileUuids('XX:XX:XX:XX:XX:XX', (err: BusinessError, data: Array<connection.ProfileUuids>) => {
4. console.info('getRemoteProfileUuids, err: ' + JSON.stringify(err) + ', data: ' + JSON.stringify(data));
5. });
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

## connection.getRemoteProfileUuids12+

PhonePC/2in1TabletTVWearable

getRemoteProfileUuids(deviceId: string): Promise<Array<ProfileUuids>>

获取对端蓝牙设备的Profile协议能力，通过UUID区分。使用Promise异步回调。

* 建议仅对已配对的设备调用该方法。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取Profile协议能力。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[ProfileUuids](js-apis-bluetooth-constant.md#profileuuids12)>> | Promise对象，返回支持的Profile协议能力集合。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. connection.getRemoteProfileUuids('XX:XX:XX:XX:XX:XX').then(() => {
4. console.info('getRemoteProfileUuids');
5. }, (err: BusinessError) => {
6. console.error('getRemoteProfileUuids: errCode' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. });
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.getLocalName

PhonePC/2in1TabletTVWearable

getLocalName(): string

获取本机蓝牙设备的名称。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 本机蓝牙设备名称。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let localName: string = connection.getLocalName();
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.getPairedDevices

PhonePC/2in1TabletTVWearable

getPairedDevices(): Array<string>

获取已配对蓝牙设备的地址集合。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 已配对蓝牙设备的地址集合。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 已配对的地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let devices: Array<string> = connection.getPairedDevices();
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.getPairState11+

PhonePC/2in1TabletTVWearable

getPairState(deviceId: string): BondState

获取对端蓝牙设备的配对状态信息。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取配对状态信息。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备的地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BondState](js-apis-bluetooth-connection.md#bondstate) | 表示设备的蓝牙配对状态。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let res: connection.BondState = connection.getPairState("XX:XX:XX:XX:XX:XX");
4. console.info('getPairState: ' + res);
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## connection.getProfileConnectionState

PhonePC/2in1TabletTVWearable

getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState

获取蓝牙Profile协议的连接状态，其中ProfileId为可选参数。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profileId | [ProfileId](js-apis-bluetooth-constant.md#profileid) | 否 | 表示Profile协议的枚举值。如果携带ProfileId，则返回指定Profile协议的连接状态。如果未携带ProfileId，则检查所有支持的Profile连接状态，按如下优先级顺序检查并返回：  - 存在已连接的Profile协议，则返回[STATE\_CONNECTED](js-apis-bluetooth-constant.md#profileconnectionstate)。  - 存在正在连接的Profile协议，则返回[STATE\_CONNECTING](js-apis-bluetooth-constant.md#profileconnectionstate)。  - 存在正在断连的Profile协议，则返回[STATE\_DISCONNECTING](js-apis-bluetooth-constant.md#profileconnectionstate)。  - 以上条件均不满足，则返回[STATE\_DISCONNECTED](js-apis-bluetooth-constant.md#profileconnectionstate)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | Profile协议的连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { constant } from '@kit.ConnectivityKit';
3. try {
4. let result: connection.ProfileConnectionState = connection.getProfileConnectionState(constant.ProfileId.PROFILE_A2DP_SOURCE);
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## connection.setDevicePairingConfirmation

PhonePC/2in1TabletTVWearable

setDevicePairingConfirmation(deviceId: string, accept: boolean): void

收到对端蓝牙设备的配对请求事件后，确认请求结果。

* 对端蓝牙的配对请求通过[on('pinRequired')](js-apis-bluetooth-connection.md#connectiononpinrequired)的回调结果获取。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| accept | boolean | 是 | 是否接受对端设备的配对请求。true表示接受，false表示不接受。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // 订阅“pinRequired”配对请求事件，收到对端配对请求后设置配对确认。
3. function onReceivePinRequiredEvent(data: connection.PinRequiredParam) { // data为配对请求的入参，配对请求参数。
4. console.info('pin required  = '+ JSON.stringify(data));
5. connection.setDevicePairingConfirmation(data.deviceId, true);
6. }
7. try {
8. connection.on('pinRequired', onReceivePinRequiredEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## connection.setDevicePinCode

PhonePC/2in1TabletTVWearable

setDevicePinCode(deviceId: string, code: string, callback: AsyncCallback<void>): void

蓝牙配对时，弹框提示用户输入个人身份识别码（Personal identification number，PIN），调用此接口设置PIN码，完成蓝牙配对。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。 |
| code | string | 是 | 用户输入的PIN码，该字符串的字符个数范围为(0, 16]，例如："12345"。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置PinCode成功，err为undefined，否则为错误对象。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // callback
3. try {
4. connection.setDevicePinCode('11:22:33:44:55:66', '12345', (err: BusinessError) => {
5. console.info('setDevicePinCode,device name err: ' + JSON.stringify(err));
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.setDevicePinCode

PhonePC/2in1TabletTVWearable

setDevicePinCode(deviceId: string, code: string): Promise<void>

蓝牙配对时，弹框提示用户输入PIN码，调用此接口请求用户输入PIN码，完成蓝牙配对。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。 |
| code | string | 是 | 用户输入的PIN码，该字符串的字符个数范围为(0, 16]，例如："12345"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // promise
3. try {
4. connection.setDevicePinCode('11:22:33:44:55:66', '12345').then(() => {
5. console.info('setDevicePinCode');
6. }, (error: BusinessError) => {
7. console.error('setDevicePinCode: errCode:' + error.code + ',errMessage' + error.message);
8. })

10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## connection.setLocalName(deprecated)

PhonePC/2in1TabletTVWearable

setLocalName(name: string): void

设置本机蓝牙设备名称，不能设置为空字符串。如果设为空字符串会失败。

说明

从API version 10开始支持，从API version 12开始废弃，不再提供替代接口。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 需要设置的蓝牙名称，名称长度范围：(0, 248]，单位：Byte。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. connection.setLocalName('device_name');
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.setBluetoothScanMode

PhonePC/2in1TabletTVWearable

setBluetoothScanMode(mode: ScanMode, duration: number): void

设置蓝牙扫描模式，决定本机设备是否可被连接，或者可被发现。搭配[onScanModeChange](js-apis-bluetooth-connection.md#connectiononscanmodechange23)接口使用，可实时监听蓝牙扫描模式变更事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mode | [ScanMode](js-apis-bluetooth-connection.md#scanmode) | 是 | 蓝牙扫描模式。当扫描模式为SCAN\_MODE\_GENERAL\_DISCOVERABLE时，超出duration持续时间(不为0)，扫描模式会重新设置为SCAN\_MODE\_CONNECTABLE。 |
| duration | number | 是 | 设备可被发现的持续时间，单位：ms。设置为0则表示持续可发现。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. // 设置为可连接可发现才可被对端设备扫描到，可以连接。
4. connection.setBluetoothScanMode(connection.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 100);
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## connection.getBluetoothScanMode

PhonePC/2in1TabletTVWearable

getBluetoothScanMode(): ScanMode

获取蓝牙扫描模式。搭配[onScanModeChange](js-apis-bluetooth-connection.md#connectiononscanmodechange23)接口使用，可实时监听蓝牙扫描模式变更事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ScanMode](js-apis-bluetooth-connection.md#scanmode) | 蓝牙扫描模式。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let scanMode: connection.ScanMode = connection.getBluetoothScanMode();
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.startBluetoothDiscovery

PhonePC/2in1TabletTVWearable

startBluetoothDiscovery(): void

开启蓝牙扫描，发现对端蓝牙设备。

* 该接口支持发现传统蓝牙设备和低功耗蓝牙设备，整个蓝牙扫描过程大约持续12s。
* 扫描结果可通过API version 10开始支持的[connection.on('bluetoothDeviceFind')](js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)或者API version 18开始支持的[connection.on('discoveryResult')](js-apis-bluetooth-connection.md#connectionondiscoveryresult18)的回调函数获取到。推荐使用[connection.on('discoveryResult')](js-apis-bluetooth-connection.md#connectionondiscoveryresult18)，该方式可以获取到更多设备信息。
* 若在扫描过程中，请勿重复调用该方法（可使用[connection.isBluetoothDiscovering](js-apis-bluetooth-connection.md#connectionisbluetoothdiscovering11)判断蓝牙当前是否处于扫描过程中）。
* 调用[connection.stopBluetoothDiscovery](js-apis-bluetooth-connection.md#connectionstopbluetoothdiscovery)可以停止该方法开启的扫描流程，扫描停止后，才能开启下一次蓝牙扫描。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: Array<string>) {
3. console.info('data length' + data.length);
4. }
5. try {
6. connection.on('bluetoothDeviceFind', onReceiveEvent);
7. connection.startBluetoothDiscovery();
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.stopBluetoothDiscovery

PhonePC/2in1TabletTVWearable

stopBluetoothDiscovery(): void

关闭蓝牙扫描。

* 关闭的扫描是由[connection.startBluetoothDiscovery](js-apis-bluetooth-connection.md#connectionstartbluetoothdiscovery)触发的。
* 当应用不再需要扫描设备时，需主动调用该方法关闭扫描。
* 若不在扫描过程中，请勿重复调用该方法（可使用[connection.isBluetoothDiscovering](js-apis-bluetooth-connection.md#connectionisbluetoothdiscovering11)判断蓝牙当前是否处于扫描过程中）。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. connection.stopBluetoothDiscovery();
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## connection.isBluetoothDiscovering11+

PhonePC/2in1TabletTVWearable

isBluetoothDiscovering(): boolean

判断本机蓝牙设备是否处于设备扫描状态。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 是否开启蓝牙发现。true表示正在发起设备扫描，false表示未发起设备扫描。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let res: boolean = connection.isBluetoothDiscovering();
4. console.info('isBluetoothDiscovering: ' + res);
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

## connection.setRemoteDeviceName12+

PhonePC/2in1TabletTVWearable

setRemoteDeviceName(deviceId: string, name: string): Promise<void>

设置对端蓝牙设备的名称，不能设置为空字符串。如果设为空字符串会失败。使用Promise异步回调。

* 建议仅对已配对的设备调用该方法。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址进行名称设置。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端设备MAC地址，例如："XX:XX:XX:XX:XX:XX"。 |
| name | string | 是 | 修改对端设备名称，名称长度范围：(0, 64]，单位：Byte。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // promise
3. try {
4. connection.setRemoteDeviceName('11:22:33:44:55:66', 'RemoteDeviceName').then(() => {
5. console.info('setRemoteDeviceName success');
6. }, (error: BusinessError) => {
7. console.error('setRemoteDeviceName: errCode: ' + error.code + ',errMessage' + error.message);
8. })
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

## connection.getRemoteDeviceBatteryInfo12+

PhonePC/2in1TabletTVWearable

getRemoteDeviceBatteryInfo(deviceId: string): Promise<BatteryInfo>

获取对端蓝牙设备的电量信息。使用Promise异步回调。

* 对端蓝牙设备的电量信息变更通过[on('batteryChange')](js-apis-bluetooth-connection.md#connectiononbatterychange12)的回调结果获取。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取电量信息。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示对端蓝牙设备的MAC地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BatteryInfo](js-apis-bluetooth-connection.md#batteryinfo12)> | Promise对象，返回电量信息对象。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // promise
3. try {
4. connection.getRemoteDeviceBatteryInfo('11:22:33:AA:BB:FF').then((data: connection.BatteryInfo) => {
5. console.info('getRemoteDeviceBatteryInfo success, DeviceType:' + JSON.stringify(data));
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.on('batteryChange')12+

PhonePC/2in1TabletTVWearable

on(type: 'batteryChange', callback: Callback<BatteryInfo>): void

订阅对端设备的电量信息变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'batteryChange'，表示对端设备的电量信息变化事件。当该设备通知电量变化时，会触发该事件。 |
| callback | Callback<[BatteryInfo](js-apis-bluetooth-connection.md#batteryinfo12)> | 是 | 指定订阅的回调函数，返回电量信息。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let onReceiveEvent: (data: connection.BatteryInfo) => void = (data: connection.BatteryInfo) => {
3. console.info('BatteryInfo = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('batteryChange', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.off('batteryChange')12+

PhonePC/2in1TabletTVWearable

off(type: 'batteryChange', callback?: Callback<BatteryInfo>): void

取消订阅对端设备的电量信息变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'batteryChange'，表示对端设备的电量信息变化事件。 |
| callback | Callback<[BatteryInfo](js-apis-bluetooth-connection.md#batteryinfo12)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[connection.on('batteryChange')](js-apis-bluetooth-connection.md#connectiononbatterychange12)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let onReceiveEvent: (data: connection.BatteryInfo) => void = (data: connection.BatteryInfo) => {
3. console.info('BatteryInfo = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('batteryChange', onReceiveEvent);
7. connection.off('batteryChange', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.on('bluetoothDeviceFind')

PhonePC/2in1TabletTVWearable

on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void

订阅蓝牙设备扫描结果上报事件。使用Callback异步回调。

* 可扫描到的设备类型包括传统蓝牙设备和低功耗蓝牙设备。
* 该上报方式只支持获取设备地址信息。
* 推荐使用API version 18开始支持的[connection.on('discoveryResult')](js-apis-bluetooth-connection.md#connectionondiscoveryresult18)扫描上报方式，可获取到更多设备信息，包括设备地址、设备信号强度、设备名称和设备类型。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'bluetoothDeviceFind'，表示蓝牙设备扫描结果上报事件。当调用[connection.startBluetoothDiscovery](js-apis-bluetooth-connection.md#connectionstartbluetoothdiscovery)后，开始设备扫描，若扫描到设备，触发该事件。 |
| callback | Callback<Array<string>> | 是 | 指定订阅的回调函数，会携带扫描到的设备地址集合。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 已配对的地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: Array<string>) { // data为蓝牙设备地址集合。
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('bluetoothDeviceFind', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.off('bluetoothDeviceFind')

PhonePC/2in1TabletTVWearable

off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void

取消订阅蓝牙设备扫描结果上报事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'bluetoothDeviceFind'，表示蓝牙设备扫描结果上报事件。 |
| callback | Callback<Array<string>> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[connection.on('bluetoothDeviceFind')](js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: Array<string>) {
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('bluetoothDeviceFind', onReceiveEvent);
7. connection.off('bluetoothDeviceFind', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.on('bondStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'bondStateChange', callback: Callback<BondStateParam>): void

订阅蓝牙配对状态变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'bondStateChange'，表示蓝牙配对状态变化事件。  当调用[connection.pairDevice](js-apis-bluetooth-connection.md#connectionpairdevice)发起主动配对，或者本机设备收到其他设备的配对请求时，触发该事件。 |
| callback | Callback<[BondStateParam](js-apis-bluetooth-connection.md#bondstateparam)> | 是 | 指定订阅的回调函数，会携带配对状态结果。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: connection.BondStateParam) { // data为回调函数入参，表示配对的状态。
3. console.info('pair state = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('bondStateChange', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.off('bondStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void

取消订阅蓝牙配对状态变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'bondStateChange'，表示蓝牙配对状态变化事件。 |
| callback | Callback<[BondStateParam](js-apis-bluetooth-connection.md#bondstateparam)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[connection.on('bondStateChange')](js-apis-bluetooth-connection.md#connectiononbondstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: connection.BondStateParam) {
3. console.info('bond state = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('bondStateChange', onReceiveEvent);
7. connection.off('bondStateChange', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.on('pinRequired')

PhonePC/2in1TabletTVWearable

on(type: 'pinRequired', callback: Callback<PinRequiredParam>): void

订阅配对请求事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pinRequired'，表示配对请求事件。  当调用[connection.pairDevice](js-apis-bluetooth-connection.md#connectionpairdevice)发起主动配对，或者本机设备收到其他设备的配对请求时，触发该事件。 |
| callback | Callback<[PinRequiredParam](js-apis-bluetooth-connection.md#pinrequiredparam)> | 是 | 指定订阅的回调函数，会携带配对请求。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: connection.PinRequiredParam) { // data为配对请求参数。
3. console.info('pin required = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('pinRequired', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.off('pinRequired')

PhonePC/2in1TabletTVWearable

off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void

取消订阅配对请求事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'pinRequired'，表示配对请求事件。 |
| callback | Callback<[PinRequiredParam](js-apis-bluetooth-connection.md#pinrequiredparam)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[connection.on('pinRequired')](js-apis-bluetooth-connection.md#connectiononpinrequired)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: connection.PinRequiredParam) {
3. console.info('pin required = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('pinRequired', onReceiveEvent);
7. connection.off('pinRequired', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.on('discoveryResult')18+

PhonePC/2in1TabletTVWearable

on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void

订阅蓝牙设备扫描结果上报事件。使用Callback异步回调。

* 可扫描到的设备类型包括传统蓝牙设备和低功耗蓝牙设备。
* 该上报方式支持获取设备地址、设备信号强度、设备名称和设备类型。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'discoveryResult'，表示蓝牙设备扫描结果上报事件。当调用[connection.startBluetoothDiscovery](js-apis-bluetooth-connection.md#connectionstartbluetoothdiscovery)后，开始设备扫描，若扫描到设备，触发该事件。 |
| callback | Callback<Array<[DiscoveryResult](js-apis-bluetooth-connection.md#discoveryresult18)>> | 是 | 指定订阅的回调函数，会携带扫描结果的集合。 |

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
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data为蓝牙设备扫描结果集合。
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('discoveryResult', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.off('discoveryResult')18+

PhonePC/2in1TabletTVWearable

off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void

取消订阅蓝牙设备发现上报事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'discoveryResult'，表示蓝牙设备扫描结果上报事件。 |
| callback | Callback<Array<[DiscoveryResult](js-apis-bluetooth-connection.md#discoveryresult18)>> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[connection.on('discoveryResult')](js-apis-bluetooth-connection.md#connectionondiscoveryresult18)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data为蓝牙设备扫描结果集合。
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. connection.on('discoveryResult', onReceiveEvent);
7. connection.off('discoveryResult', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## connection.onScanModeChange23+

PhonePC/2in1TabletTVWearable

onScanModeChange(callback: Callback<ScanMode>): void

订阅蓝牙扫描模式变更事件。使用Callback异步回调。当调用[setBluetoothScanMode](js-apis-bluetooth-connection.md#connectionsetbluetoothscanmode)更改当前蓝牙扫描模式后，如订阅此事件，则会收到携带最新扫描模式的回调函数。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ScanMode](js-apis-bluetooth-connection.md#scanmode)> | 是 | 指定订阅的回调函数，会携带变更后最新的蓝牙扫描模式。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. function ScanModeChangeEvent(scanMode: connection.ScanMode) {
2. console.info(`Scan mode has changed, new mode: ${scanMode}`);
3. }
4. try {
5. connection.onScanModeChange(ScanModeChangeEvent);
6. } catch (err) {
7. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
8. }
```

## connection.offScanModeChange23+

PhonePC/2in1TabletTVWearable

offScanModeChange(callback?: Callback<ScanMode>): void

取消订阅蓝牙扫描模式变更事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[ScanMode](js-apis-bluetooth-connection.md#scanmode)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[connection.onScanModeChange](js-apis-bluetooth-connection.md#connectiononscanmodechange23)中的回调函数一致；若无传参，则取消订阅所有蓝牙扫描模式变更的回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. function ScanModeChangeEvent(scanMode: connection.ScanMode) {
2. console.info(`Scan mode has changed, new mode: ${scanMode}`);
3. }
4. try {
5. connection.offScanModeChange(ScanModeChangeEvent);
6. } catch (err) {
7. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
8. }
```

## connection.getLastConnectionTime15+

PhonePC/2in1TabletTVWearable

getLastConnectionTime(deviceId: string): Promise<number>

获取对端蓝牙设备最近一次连接的时间点。使用Promise异步回调。

* 从API version 21开始，此接口支持使用对端设备的实际MAC地址获取最近一次连接时间。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示远端设备MAC地址。例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回对端蓝牙设备最近一次连接的时间点，格式为秒级的UNIX时间戳。 |

**错误码**：

以下错误码的详细介绍请参见[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // promise
3. try {
4. connection.getLastConnectionTime('11:22:33:44:55:66').then((time: number) => {
5. console.info(`connectionTime: ${time}`);
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## connection.connectAllowedProfiles16+

PhonePC/2in1TabletTVWearable

connectAllowedProfiles(deviceId: string, callback: AsyncCallback<void>): void

连接对端设备支持的profile（只包括A2DP、HFP和HID）。使用Callback异步回调。

* 需先调用[connection.pairDevice](js-apis-bluetooth-connection.md#connectionpairdevice)发起配对，且仅允许在每次发起配对后30s内调用此接口一次。
* 当配对成功后，建议先调用[getRemoteProfileUuids](js-apis-bluetooth-connection.md#connectiongetremoteprofileuuids12)主动查询目标设备支持的profile能力。若存在应用需要的能力，才调用此接口。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址进行profile连接。

**需要权限：**: ohos.permission.ACCESS\_BLUETOOTH

**系统能力：**: SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示需要连接的对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当发起连接成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见 [通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. connection.connectAllowedProfiles('68:13:24:79:4C:8C', (err: BusinessError) => {
4. if (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. return;
7. }
8. console.info('connectAllowedProfiles');
9. });
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## connection.connectAllowedProfiles16+

PhonePC/2in1TabletTVWearable

connectAllowedProfiles(deviceId: string): Promise<void>

连接对端设备支持的profile（只包括A2DP、HFP和HID）。使用Promise异步回调。

* 需先调用[connection.pairDevice](js-apis-bluetooth-connection.md#connectionpairdevice)发起配对，且仅允许在每次发起配对后30s内调用此接口一次。
* 当配对成功后，建议先调用[getRemoteProfileUuids](js-apis-bluetooth-connection.md#connectiongetremoteprofileuuids12)主动查询目标设备支持的profile能力。若存在应用需要的能力，才调用此接口。
* 从API version 21开始，此接口支持使用对端设备的实际MAC地址进行profile连接。

**需要权限：**: ohos.permission.ACCESS\_BLUETOOTH

**系统能力：**: SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 表示需要连接的对端设备地址，例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见 [通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. try {
3. connection.connectAllowedProfiles('68:13:24:79:4C:8C').then(() => {
4. console.info('connectAllowedProfiles');
5. }, (err: BusinessError) => {
6. console.error('connectAllowedProfiles:errCode' + err.code + ', errMessage: ' + err.message);
7. });
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## BondStateParam

PhonePC/2in1TabletTVWearable

描述配对状态结果的参数结构。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 配对中的对端设备地址。 |
| state | [BondState](js-apis-bluetooth-connection.md#bondstate) | 否 | 否 | 配对状态。 |
| cause12+ | [UnbondCause](js-apis-bluetooth-connection.md#unbondcause12) | 否 | 否 | 配对失败的原因。 |

## PinRequiredParam

PhonePC/2in1TabletTVWearable

描述配对请求的参数结构。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 要配对的对端设备地址。 |
| pinCode | string | 否 | 否 | 配对过程中的密钥。 |

## DeviceClass

PhonePC/2in1TabletTVWearable

描述蓝牙设备的类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| majorClass | [MajorClass](js-apis-bluetooth-constant.md#majorclass) | 否 | 否 | 主要类型。是蓝牙标准协议中定义的类型字段。 |
| majorMinorClass | [MajorMinorClass](js-apis-bluetooth-constant.md#majorminorclass) | 否 | 否 | 子类型，是在主要类型上基础上进一步细分的类型。是蓝牙标准协议中定义的类型字段。 |
| classOfDevice | number | 否 | 否 | 设备类型。是蓝牙标准协议中定义的类型字段，包含了[MajorClass](js-apis-bluetooth-constant.md#majorclass)、[MajorMinorClass](js-apis-bluetooth-constant.md#majorminorclass)和支持的主要服务这三种设备信息。 |

## BatteryInfo12+

PhonePC/2in1TabletTVWearable

描述设备的电量信息。

只有支持蓝牙标准协议定义的电量信息AT（Attention）命令（包括：+XEVENT和IPHONEACCEV）的设备才支持上报有效的电量信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| batteryLevel | number | 否 | 否 | 表示设备的电量值。  如果该值为-1，表示没有电量信息。 |
| leftEarBatteryLevel | number | 否 | 否 | 若是蓝牙耳机设备类型，表示左侧耳机的电量值。  如果该值为-1，表示没有电量信息。 |
| leftEarChargeState | [DeviceChargeState](js-apis-bluetooth-connection.md#devicechargestate12) | 否 | 否 | 若是蓝牙耳机设备类型，表示左侧耳机的充电状态。 |
| rightEarBatteryLevel | number | 否 | 否 | 若是蓝牙耳机设备类型，表示右侧耳机的电量值。  如果该值为-1，表示没有电量信息。 |
| rightEarChargeState | [DeviceChargeState](js-apis-bluetooth-connection.md#devicechargestate12) | 否 | 否 | 若是蓝牙耳机设备类型，表示右侧耳机的充电状态。 |
| boxBatteryLevel | number | 否 | 否 | 若是蓝牙耳机设备类型，表示耳机仓的电量值。  如果值该为-1，表示没有电量信息。 |
| boxChargeState | [DeviceChargeState](js-apis-bluetooth-connection.md#devicechargestate12) | 否 | 否 | 若是蓝牙耳机设备类型，表示耳机仓的充电状态。 |

## BluetoothTransport

PhonePC/2in1TabletTVWearable

枚举，表示设备传输类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TRANSPORT\_BR\_EDR | 0 | 传统蓝牙（Basic Rate/Enhanced Data Rate，BR/EDR）设备传输方式。 |
| TRANSPORT\_LE | 1 | 低功耗蓝牙（Bluetooth Low Energy，BLE）设备传输方式。 |
| TRANSPORT\_DUAL20+ | 2 | 同时支持传统蓝牙（BR/EDR）和低功耗蓝牙（BLE）的双模设备传输方式。设备可以根据需要选择使用传统蓝牙（BR/EDR）或低功耗蓝牙（BLE）进行通信。 |
| TRANSPORT\_UNKNOWN20+ | 3 | 未知的设备传输方式。 |

## ScanMode

PhonePC/2in1TabletTVWearable

枚举，表示扫描模式。该模式决定设备是否可被发现或可被连接。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN\_MODE\_NONE | 0 | 不可发现、不可连接模式。 |
| SCAN\_MODE\_CONNECTABLE | 1 | 可连接模式。 |
| SCAN\_MODE\_GENERAL\_DISCOVERABLE | 2 | 通用可发现模式，可被长时间发现。 |
| SCAN\_MODE\_LIMITED\_DISCOVERABLE | 3 | 有限可发现模式，持续一定时间。 |
| SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE | 4 | 可连接及通用可发现模式。 |
| SCAN\_MODE\_CONNECTABLE\_LIMITED\_DISCOVERABLE | 5 | 可连接及有限可发现模式。 |

## BondState

PhonePC/2in1TabletTVWearable

枚举，配对状态。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BOND\_STATE\_INVALID | 0 | 未配对状态。 |
| BOND\_STATE\_BONDING | 1 | 配对中的状态。 |
| BOND\_STATE\_BONDED | 2 | 已配对状态。 |

## UnbondCause12+

PhonePC/2in1TabletTVWearable

枚举，配对失败原因。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| USER\_REMOVED | 0 | 用户主动移除设备。若配对状态[BondState](js-apis-bluetooth-connection.md#bondstate)是已配对，也表示配对成功。 |
| REMOTE\_DEVICE\_DOWN | 1 | 对端设备不在线。例如：对端设备蓝牙是关闭的。 |
| AUTH\_FAILURE | 2 | 鉴权失败。例如：两端设备密钥不匹配。 |
| AUTH\_REJECTED | 3 | 鉴权被拒绝。例如：对端设备拒绝了配对请求。 |
| INTERNAL\_ERROR | 4 | 内部错误。例如：设备不支持配对、配对过程超时等异常。 |

## DeviceChargeState12+

PhonePC/2in1TabletTVWearable

枚举，表示设备当前的充电状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEVICE\_NORMAL\_CHARGE\_NOT\_CHARGED | 0 | 不支持超级快充能力的设备当前处于未充电状态。 |
| DEVICE\_NORMAL\_CHARGE\_IN\_CHARGING | 1 | 不支持超级快充能力的设备当前处于充电状态。 |
| DEVICE\_SUPER\_CHARGE\_NOT\_CHARGED | 2 | 支持超级快充能力的设备当前处于未充电状态。 |
| DEVICE\_SUPER\_CHARGE\_IN\_CHARGING | 3 | 支持超级快充能力的设备当前处于充电状态。 |

## DiscoveryResult18+

PhonePC/2in1TabletTVWearable

扫描到设备后，上报的扫描结果。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 扫描到的设备地址。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 已配对的地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法。 |
| rssi | number | 否 | 否 | 扫描到的设备信号强度，单位：dBm。 |
| deviceName | string | 否 | 否 | 扫描到的设备名称。 |
| deviceClass | [DeviceClass](js-apis-bluetooth-connection.md#deviceclass) | 否 | 否 | 扫描到的设备类型。 |
