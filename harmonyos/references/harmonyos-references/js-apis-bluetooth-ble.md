---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bluetooth-ble
title: @ohos.bluetooth.ble (蓝牙ble模块)
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.bluetooth.ble (蓝牙ble模块)
category: harmonyos-references
scraped_at: 2026-04-28T08:07:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:badf44480e6e7d473fc3c30c7c44b2673e9c7003c92a1b02f40d72e7050ca634
---

本模块提供了基于低功耗蓝牙（Bluetooth Low Energy，[BLE](../harmonyos-guides/terminology.md#ble)）技术的蓝牙能力，支持发起BLE扫描、发送BLE广播报文、以及基于通用属性协议（Generic Attribute Profile，[GATT](../harmonyos-guides/terminology.md#gatt)）的连接和传输数据。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 接口中涉及的[UUID](../harmonyos-guides/terminology.md#uuid)服务，可以通过工具函数[util.generateRandomUUID](js-apis-util.md#utilgeneraterandomuuid9)生成。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { ble } from '@kit.ConnectivityKit';
```

## ProfileConnectionState

PhonePC/2in1TabletTVWearable

type ProfileConnectionState = constant.ProfileConnectionState

蓝牙设备的Profile协议连接状态。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [constant.ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 蓝牙设备的profile连接状态。 |

## BluetoothAddress23+

PhonePC/2in1TabletTVWearable

type BluetoothAddress = common.BluetoothAddress

描述蓝牙设备地址信息的参数结构，包括地址与地址类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 类型 | 说明 |
| --- | --- |
| [common.BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 蓝牙设备的地址信息。 |

## ble.createGattServer

PhonePC/2in1TabletTVWearable

createGattServer(): GattServer

创建[GattServer](js-apis-bluetooth-ble.md#gattserver)实例，表示GATT连接中的server端。

* 通过该实例可以操作server端的行为，如添加服务[addService](js-apis-bluetooth-ble.md#addservice)、通知特征值变化[notifyCharacteristicChanged](js-apis-bluetooth-ble.md#notifycharacteristicchanged)等。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattServer](js-apis-bluetooth-ble.md#gattserver) | 返回一个Gatt服务的实例。 |

**示例：**

```
1. let gattServer: ble.GattServer = ble.createGattServer();
2. console.info('gatt success');
```

## ble.createGattClientDevice

PhonePC/2in1TabletTVWearable

createGattClientDevice(deviceId: string): GattClientDevice

创建[GattClientDevice](js-apis-bluetooth-ble.md#gattclientdevice)实例，表示GATT连接中的client端。

* 通过该实例可以操作client端行为，如调用[connect](js-apis-bluetooth-ble.md#connect)向对端设备发起连接，调用[getServices](js-apis-bluetooth-ble.md#getservices)获取对端设备支持的所有服务能力。
* 创建该实例所需要的设备地址表示server端设备。可以通过[ble.startBLEScan](js-apis-bluetooth-ble.md#blestartblescan)或[BleScanner](js-apis-bluetooth-ble.md#blescanner15)的[startScan](js-apis-bluetooth-ble.md#startscan15)接口获取server端设备地址，且需保证server端设备的BLE广播是可连接的。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 对端设备地址， 例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattClientDevice](js-apis-bluetooth-ble.md#gattclientdevice) | client端类，使用client端方法之前需要创建该类的实例进行操作。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. try {
2. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
3. } catch (err) {
4. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
5. }
```

## ble.getConnectedBLEDevices

PhonePC/2in1TabletTVWearable

getConnectedBLEDevices(): Array<string>

获取和本机设备已连接GATT的BLE设备集合。

* 建议给server端使用，client端使用返回的设备地址集合为空。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回和本机设备已建立GATT连接的BLE设备地址集合。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 若和该设备地址配对成功后，该地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. try {
2. let result: Array<string> = ble.getConnectedBLEDevices();
3. } catch (err) {
4. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
5. }
```

## ble.getConnectedBLEDevices21+

PhonePC/2in1TabletTVWearable

getConnectedBLEDevices(profile: BleProfile): Array<string>

根据指定的本机设备Profile协议类型，获取和本机设备已连接GATT的BLE设备集合。

* 若指定本机设备作为client端，则返回与本机设备连接的所有server端设备地址集合。
* 若指定本机设备作为server端，则返回与本机设备连接的所有client端设备地址集合。
* 若指定本机设备同时作为client端和server端，则返回与本机设备连接的所有client端和server端设备地址集合。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| profile | [BleProfile](js-apis-bluetooth-ble.md#bleprofile21) | 是 | 当前设备的Profile协议类型，表明该设备在GATT链路中的通信角色。  - GATT\_CLIENT表示指定本机设备为client端角色，与其建立GATT连接的所有对端设备为server端角色。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 返回和本机设备已建立GATT连接的BLE设备地址集合。  基于信息安全考虑，此处获取的设备地址为虚拟MAC地址。  - 若和该设备地址配对成功后，该地址不会变更。  - 取消配对该设备或蓝牙关闭后，若重新获取，该虚拟地址会变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. try {
2. let result: Array<string> = ble.getConnectedBLEDevices(ble.BleProfile.GATT_CLIENT);
3. } catch (err) {
4. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
5. }
```

## ble.startBLEScan

PhonePC/2in1TabletTVWearable

startBLEScan(filters: Array<ScanFilter>, options?: ScanOptions): void

发起BLE扫描流程。

* 扫描结果会通过[ble.on('BLEDeviceFind')](js-apis-bluetooth-ble.md#bleonbledevicefind)的回调函数获取到。只能扫描BLE设备，调用[ble.stopBLEScan](js-apis-bluetooth-ble.md#blestopblescan)可以停止该方法开启的扫描流程。
* 该接口只支持单路扫描，即应用同时只能调用一次，下一次调用前，需要先调用[ble.stopBLEScan](js-apis-bluetooth-ble.md#blestopblescan)停止上一次的扫描流程。
* 若需要使用多路扫描，可使用[BleScanner](js-apis-bluetooth-ble.md#blescanner15)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<[ScanFilter](js-apis-bluetooth-ble.md#scanfilter)> | 是 | 表示扫描结果过滤策略集合，符合过滤条件的设备发现会保留。  -若该参数设置为null，将扫描所有可发现的周边BLE设备，但是不建议使用此方式，可能扫描到非预期设备，并增加功耗。 |
| options | [ScanOptions](js-apis-bluetooth-ble.md#scanoptions) | 否 | 表示扫描的参数配置。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { common } from '@kit.ConnectivityKit';
2. function onReceiveEvent(data: Array<ble.ScanResult>) {
3. console.info('BLE scan device find result = '+ JSON.stringify(data));
4. }
5. try {
6. ble.on("BLEDeviceFind", onReceiveEvent);
7. let addressInfo : common.BluetoothAddress = {
8. address:"XX:XX:XX:XX:XX:XX",
9. addressType:common.BluetoothAddressType.REAL,
10. rawAddressType:common.BluetoothRawAddressType.PUBLIC
11. }
12. let scanFilter: ble.ScanFilter = {
13. deviceId:"XX:XX:XX:XX:XX:XX",
14. address:addressInfo, // 使用address时不需要重复设置deviceId
15. name:"test",
16. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
17. };
18. let scanOptions: ble.ScanOptions = {
19. interval: 500,
20. dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
21. matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
22. }
23. ble.startBLEScan([scanFilter],scanOptions);
24. } catch (err) {
25. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
26. }
```

## ble.stopBLEScan

PhonePC/2in1TabletTVWearable

stopBLEScan(): void

停止BLE扫描流程。

* 停止的BLE扫描由[ble.startBLEScan](js-apis-bluetooth-ble.md#blestartblescan)触发。
* 当应用不再需要扫描BLE设备时，需主动调用该方法停止扫描。
* 调用此接口后将不再收到扫描结果上报，重新开启BLE扫描即可再次扫到BLE设备。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. try {
2. ble.stopBLEScan();
3. } catch (err) {
4. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
5. }
```

## ble.startAdvertising

PhonePC/2in1TabletTVWearable

startAdvertising(setting: AdvertiseSetting, advData: AdvertiseData, advResponse?: AdvertiseData): void

开始发送BLE广播报文。

* 当应用不再需要发送BLE广播报文时，需主动调用[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising)停止发送。
* 同步接口，不要和API version 11的[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising11)搭配使用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH 或 (ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME)

* 当应用使用[AdvertiseData](js-apis-bluetooth-ble.md#advertisedata)中的advertiseName字段时，需要申请[ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_bluetooth_advertiser_name)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| setting | [AdvertiseSetting](js-apis-bluetooth-ble.md#advertisesetting) | 是 | BLE广播的相关参数。 |
| advData | [AdvertiseData](js-apis-bluetooth-ble.md#advertisedata) | 是 | BLE广播报文内容。 |
| advResponse | [AdvertiseData](js-apis-bluetooth-ble.md#advertisedata) | 否 | BLE扫描回复广播报文。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900010 | The number of advertising resources reaches the upper limit. |
| 2900099 | Operation failed. |
| 2902054 | The length of the advertising data exceeds the upper limit. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit],
32. advertiseName:"testName" // 需申请ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME权限
33. };
34. let advResponse: ble.AdvertiseData = {
35. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
36. manufactureData:[manufactureDataUnit],
37. serviceData:[serviceDataUnit],
38. advertiseName:"testName" // 需申请ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME权限
39. };
40. ble.startAdvertising(setting, advData ,advResponse);
41. } catch (err) {
42. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
43. }
```

## ble.stopAdvertising

PhonePC/2in1TabletTVWearable

stopAdvertising(): void

停止发送BLE广播报文。

* 停止的BLE广播是由[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising)触发的。
* 不可以和API version 11的[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)搭配使用。
* 当应用不再需要发送BLE广播报文时，需主动调用该方法停止发送。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. try {
2. ble.stopAdvertising();
3. } catch (err) {
4. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
5. }
```

## ble.startAdvertising11+

PhonePC/2in1TabletTVWearable

startAdvertising(advertisingParams: AdvertisingParams, callback: AsyncCallback<number>): void

首次启动发送BLE广播报文。使用Callback异步回调。

* 启动成功后，蓝牙子系统会分配相关资源，并使用Callback异步返回该广播的标识。
* 若携带了发送广播持续时间，则一定时间后，广播会停止发送，但分配的广播资源还存在，可以通过[ble.enableAdvertising](js-apis-bluetooth-ble.md#bleenableadvertising11)重新启动发送该广播。
* 从API version 15开始，应用可多次调用，支持发起多路广播，每一路广播通过不同的ID标识管理。
* 当应用不再需要该广播时，需调用API version 11开始支持的[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising11)完全停止该广播，不要与API version 10开始支持的[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising)混用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH 或 (ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME)

* 当使用[AdvertiseData](js-apis-bluetooth-ble.md#advertisedata)中的advertiseName字段时，需要同步申请[ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_bluetooth_advertiser_name)。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingParams | [AdvertisingParams](js-apis-bluetooth-ble.md#advertisingparams11) | 是 | 启动BLE广播的相关参数。 |
| callback | AsyncCallback<number> | 是 | 广播ID标识，通过注册回调函数获取。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900010 | The number of advertising resources reaches the upper limit. |
| 2900099 | Operation failed. |
| 2902054 | The length of the advertising data exceeds the upper limit. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true,
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit],
32. advertiseName:"testName" // 需申请ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME权限
33. };
34. let advResponse: ble.AdvertiseData = {
35. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
36. manufactureData:[manufactureDataUnit],
37. serviceData:[serviceDataUnit],
38. advertiseName:"testName" // 需申请ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME权限
39. };
40. let advertisingParams: ble.AdvertisingParams = {
41. advertisingSettings: setting,
42. advertisingData: advData,
43. advertisingResponse: advResponse,
44. duration: 0
45. }
46. let advHandle = 0xFF;
47. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
48. if (err) {
49. return;
50. } else {
51. advHandle = outAdvHandle;
52. console.info("advHandle: " + advHandle);
53. }
54. });
55. } catch (err) {
56. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
57. }
```

## ble.startAdvertising11+

PhonePC/2in1TabletTVWearable

startAdvertising(advertisingParams: AdvertisingParams): Promise<number>

首次启动发送BLE广播报文。使用Promise异步回调。

* 启动成功后，蓝牙子系统会分配相关资源，并使用Promise异步返回该广播的标识。
* 若携带了发送广播持续时间，则一定时间后，广播会停止发送，但分配的广播资源还存在，可以通过[ble.enableAdvertising](js-apis-bluetooth-ble.md#bleenableadvertising11)重新启动发送该广播。
* 从API version 15开始，应用可多次调用，支持发起多路广播，每一路广播通过不同的ID标识管理。
* 当应用不再需要该广播时，需调用API version 11开始支持的[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising11-1)完全停止该广播，不要与API version 10开始支持的[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising)混用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH 或 (ohos.permission.ACCESS\_BLUETOOTH 和 ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME)

* 当使用[AdvertiseData](js-apis-bluetooth-ble.md#advertisedata)中的advertiseName字段时，需要同步申请[ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_bluetooth_advertiser_name)。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingParams | [AdvertisingParams](js-apis-bluetooth-ble.md#advertisingparams11) | 是 | 启动BLE广播的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 广播ID标识，通过promise形式获取。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900010 | The number of advertising resources reaches the upper limit. |
| 2900099 | Operation failed. |
| 2902054 | The length of the advertising data exceeds the upper limit. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit],
32. advertiseName:"testName" // 需申请ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME权限
33. };
34. let advResponse: ble.AdvertiseData = {
35. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
36. manufactureData:[manufactureDataUnit],
37. serviceData:[serviceDataUnit],
38. advertiseName:"testName" // 需申请ohos.permission.MANAGE_BLUETOOTH_ADVERTISER_NAME权限
39. };
40. let advertisingParams: ble.AdvertisingParams = {
41. advertisingSettings: setting,
42. advertisingData: advData,
43. advertisingResponse: advResponse,
44. duration: 0
45. }
46. let advHandle = 0xFF;
47. ble.startAdvertising(advertisingParams)
48. .then(outAdvHandle => {
49. advHandle = outAdvHandle;
50. });
51. } catch (err) {
52. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
53. }
```

## ble.enableAdvertising11+

PhonePC/2in1TabletTVWearable

enableAdvertising(advertisingEnableParams: AdvertisingEnableParams, callback: AsyncCallback<void>): void

重新启动指定标识的BLE广播。使用Callback异步回调。

* [AdvertisingEnableParams](js-apis-bluetooth-ble.md#advertisingenableparams11)中advertisingId对应的广播资源已在[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时分配。
* 若[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时指定了广播持续时间，超时后广播自动停止，调用此接口可重新启动同一路BLE广播。
* 通过[ble.disableAdvertising](js-apis-bluetooth-ble.md#bledisableadvertising11)停止的广播，调用此接口可重新启动同一路BLE广播。
* 通过[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)回调获取重新启动广播结果。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingEnableParams | [AdvertisingEnableParams](js-apis-bluetooth-ble.md#advertisingenableparams11) | 是 | 临时启动BLE广播的相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2902055 | Invalid advertising id. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advResponse: ble.AdvertiseData = {
34. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
35. manufactureData:[manufactureDataUnit],
36. serviceData:[serviceDataUnit]
37. };
38. let advertisingParams: ble.AdvertisingParams = {
39. advertisingSettings: setting,
40. advertisingData: advData,
41. advertisingResponse: advResponse,
42. duration: 300
43. }
44. let advHandle = 0xFF;
45. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
46. if (err) {
47. return;
48. } else {
49. advHandle = outAdvHandle;
50. console.info("advHandle: " + advHandle);
51. }
52. });

54. let advertisingEnableParams: ble.AdvertisingEnableParams = {
55. advertisingId: advHandle,
56. duration: 0
57. }

59. // after 3s, advertising disabled, then enable the advertising
60. ble.enableAdvertising(advertisingEnableParams, (err) => {
61. if (err) {
62. return;
63. }
64. });
65. } catch (err) {
66. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
67. }
```

## ble.enableAdvertising11+

PhonePC/2in1TabletTVWearable

enableAdvertising(advertisingEnableParams: AdvertisingEnableParams): Promise<void>

重新启动指定标识的BLE广播。使用Promise异步回调。

* [AdvertisingEnableParams](js-apis-bluetooth-ble.md#advertisingenableparams11)中advertisingId对应的广播资源已在[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时分配。
* 若[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时指定了广播持续时间，超时后广播自动停止，调用此接口可重新启动同一路BLE广播。
* 通过[ble.disableAdvertising](js-apis-bluetooth-ble.md#bledisableadvertising11)停止的广播，调用此接口可重新启动同一路BLE广播。
* 通过[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)回调获取启动广播结果。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingEnableParams | [AdvertisingEnableParams](js-apis-bluetooth-ble.md#advertisingenableparams11) | 是 | 临时启动BLE广播的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2902055 | Invalid advertising id. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advResponse: ble.AdvertiseData = {
34. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
35. manufactureData:[manufactureDataUnit],
36. serviceData:[serviceDataUnit]
37. };
38. let advertisingParams: ble.AdvertisingParams = {
39. advertisingSettings: setting,
40. advertisingData: advData,
41. advertisingResponse: advResponse,
42. duration: 300
43. }
44. let advHandle = 0xFF;
45. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
46. if (err) {
47. return;
48. } else {
49. advHandle = outAdvHandle;
50. console.info("advHandle: " + advHandle);
51. }
52. });

54. let advertisingEnableParams: ble.AdvertisingEnableParams = {
55. advertisingId: advHandle,
56. duration: 0
57. }

59. // after 3s, advertising disabled, then enable the advertising
60. ble.enableAdvertising(advertisingEnableParams)
61. .then(() => {
62. console.info("enable success");
63. });
64. } catch (err) {
65. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
66. }
```

## ble.disableAdvertising11+

PhonePC/2in1TabletTVWearable

disableAdvertising(advertisingDisableParams: AdvertisingDisableParams, callback: AsyncCallback<void>): void

停止指定标识的BLE广播。使用Callback异步回调。

* 停止BLE广播，但不释放已申请的广播资源，调用[ble.enableAdvertising](js-apis-bluetooth-ble.md#bleenableadvertising11)可重新启动此方法停止的广播。
* [AdvertisingDisableParams](js-apis-bluetooth-ble.md#advertisingdisableparams11)中advertisingId对应的广播资源已在[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时分配。
* 通过[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)回调获取停止广播结果。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingDisableParams | [AdvertisingDisableParams](js-apis-bluetooth-ble.md#advertisingdisableparams11) | 是 | 临时关闭BLE广播的相关参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2902055 | Invalid advertising id. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advResponse: ble.AdvertiseData = {
34. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
35. manufactureData:[manufactureDataUnit],
36. serviceData:[serviceDataUnit]
37. };
38. let advertisingParams: ble.AdvertisingParams = {
39. advertisingSettings: setting,
40. advertisingData: advData,
41. advertisingResponse: advResponse,
42. duration: 0
43. }
44. let advHandle = 0xFF;
45. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
46. if (err) {
47. return;
48. } else {
49. advHandle = outAdvHandle;
50. console.info("advHandle: " + advHandle);
51. }
52. });

54. let advertisingDisableParams: ble.AdvertisingDisableParams = {
55. advertisingId: advHandle
56. }
57. ble.disableAdvertising(advertisingDisableParams, (err) => {
58. if (err) {
59. return;
60. }
61. });
62. } catch (err) {
63. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
64. }
```

## ble.disableAdvertising11+

PhonePC/2in1TabletTVWearable

disableAdvertising(advertisingDisableParams: AdvertisingDisableParams): Promise<void>

停止指定标识的BLE广播。使用Promise异步回调。

* 停止BLE广播，但不释放已申请的广播资源，调用[ble.enableAdvertising](js-apis-bluetooth-ble.md#bleenableadvertising11)可重新启动此方法停止的广播。
* [AdvertisingDisableParams](js-apis-bluetooth-ble.md#advertisingdisableparams11)中advertisingId对应的广播资源已在[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时分配。
* 通过[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)回调获取停止广播结果。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingDisableParams | [AdvertisingDisableParams](js-apis-bluetooth-ble.md#advertisingdisableparams11) | 是 | 临时关闭BLE广播的相关参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2902055 | Invalid advertising id. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advResponse: ble.AdvertiseData = {
34. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
35. manufactureData:[manufactureDataUnit],
36. serviceData:[serviceDataUnit]
37. };
38. let advertisingParams: ble.AdvertisingParams = {
39. advertisingSettings: setting,
40. advertisingData: advData,
41. advertisingResponse: advResponse,
42. duration: 0
43. }
44. let advHandle = 0xFF;
45. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
46. if (err) {
47. return;
48. } else {
49. advHandle = outAdvHandle;
50. console.info("advHandle: " + advHandle);
51. }
52. });

54. let advertisingDisableParams: ble.AdvertisingDisableParams = {
55. advertisingId: advHandle
56. }
57. ble.disableAdvertising(advertisingDisableParams)
58. .then(() => {
59. console.info("enable success");
60. });
61. } catch (err) {
62. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
63. }
```

## ble.stopAdvertising11+

PhonePC/2in1TabletTVWearable

stopAdvertising(advertisingId: number, callback: AsyncCallback<void>): void

完全停止发送BLE广播。使用Callback异步回调。

* 与API version 11开始支持的[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)搭配使用，会释放已经申请的广播资源。
* [ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时分配的广播标识也将失效。
* 不可以和API version 10开始支持的[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising)接口搭配使用。
* 通过[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)回调获取完全停止广播结果。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingId | number | 是 | 需要停止的广播ID标识。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2902055 | Invalid advertising id. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advResponse: ble.AdvertiseData = {
34. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
35. manufactureData:[manufactureDataUnit],
36. serviceData:[serviceDataUnit]
37. };
38. let advertisingParams: ble.AdvertisingParams = {
39. advertisingSettings: setting,
40. advertisingData: advData,
41. advertisingResponse: advResponse,
42. duration: 0
43. }
44. let advHandle = 0xFF;
45. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
46. if (err) {
47. return;
48. } else {
49. advHandle = outAdvHandle;
50. console.info("advHandle: " + advHandle);
51. }
52. });

54. ble.stopAdvertising(advHandle, (err) => {
55. if (err) {
56. return;
57. }
58. });
59. } catch (err) {
60. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
61. }
```

## ble.stopAdvertising11+

PhonePC/2in1TabletTVWearable

stopAdvertising(advertisingId: number): Promise<void>

完全停止发送BLE广播。使用Promise异步回调。

* 与API version 11开始支持的[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)搭配使用，会释放已经申请的广播资源。
* [ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)首次启动广播时分配的广播标识也将失效。
* 不可以和API version 10开始支持的[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising)接口搭配使用。
* 通过[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)回调获取完全停止广播结果。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| advertisingId | number | 是 | 需要停止的广播ID标识。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2902055 | Invalid advertising id. |

**示例：**

```
1. let manufactureValueBuffer = new Uint8Array(4);
2. manufactureValueBuffer[0] = 1;
3. manufactureValueBuffer[1] = 2;
4. manufactureValueBuffer[2] = 3;
5. manufactureValueBuffer[3] = 4;

7. let serviceValueBuffer = new Uint8Array(4);
8. serviceValueBuffer[0] = 4;
9. serviceValueBuffer[1] = 6;
10. serviceValueBuffer[2] = 7;
11. serviceValueBuffer[3] = 8;
12. console.info('manufactureValueBuffer = '+ JSON.stringify(manufactureValueBuffer));
13. console.info('serviceValueBuffer = '+ JSON.stringify(serviceValueBuffer));
14. try {
15. let setting: ble.AdvertiseSetting = {
16. interval:150,
17. txPower:0,
18. connectable:true
19. };
20. let manufactureDataUnit: ble.ManufactureData = {
21. manufactureId:4567,
22. manufactureValue:manufactureValueBuffer.buffer
23. };
24. let serviceDataUnit: ble.ServiceData = {
25. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb",
26. serviceValue:serviceValueBuffer.buffer
27. };
28. let advData: ble.AdvertiseData = {
29. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
30. manufactureData:[manufactureDataUnit],
31. serviceData:[serviceDataUnit]
32. };
33. let advResponse: ble.AdvertiseData = {
34. serviceUuids:["00001888-0000-1000-8000-00805f9b34fb"],
35. manufactureData:[manufactureDataUnit],
36. serviceData:[serviceDataUnit]
37. };
38. let advertisingParams: ble.AdvertisingParams = {
39. advertisingSettings: setting,
40. advertisingData: advData,
41. advertisingResponse: advResponse,
42. duration: 0
43. }
44. let advHandle = 0xFF;
45. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
46. if (err) {
47. return;
48. } else {
49. advHandle = outAdvHandle;
50. console.info("advHandle: " + advHandle);
51. }
52. });

54. ble.stopAdvertising(advHandle)
55. .then(() => {
56. console.info("enable success");
57. });
58. } catch (err) {
59. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
60. }
```

## ble.on('advertisingStateChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void

订阅BLE广播状态。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'advertisingStateChange'，表示广播状态事件。  当调用[ble.startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)、[ble.stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising11)、[ble.enableAdvertising](js-apis-bluetooth-ble.md#bleenableadvertising11)、[ble.disableAdvertising](js-apis-bluetooth-ble.md#bledisableadvertising11)，广播状态改变时，均会触发该事件。 |
| callback | Callback<[AdvertisingStateChangeInfo](js-apis-bluetooth-ble.md#advertisingstatechangeinfo11)> | 是 | 指定订阅的回调函数，会携带广播状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: ble.AdvertisingStateChangeInfo) {
3. console.info('bluetooth advertising state = ' + JSON.stringify(data));
4. }
5. try {
6. ble.on('advertisingStateChange', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## ble.off('advertisingStateChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void

取消订阅BLE广播状态。广播停止或启动将不再收到通知。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'advertisingStateChange'，表示广播状态事件。 |
| callback | Callback<[AdvertisingStateChangeInfo](js-apis-bluetooth-ble.md#advertisingstatechangeinfo11)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[ble.on('advertisingStateChange')](js-apis-bluetooth-ble.md#bleonadvertisingstatechange11)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: ble.AdvertisingStateChangeInfo) {
3. console.info('bluetooth advertising state = ' + JSON.stringify(data));
4. }
5. try {
6. ble.on('advertisingStateChange', onReceiveEvent);
7. ble.off('advertisingStateChange', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## ble.on('BLEDeviceFind')

PhonePC/2in1TabletTVWearable

on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void

订阅BLE设备扫描结果上报事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEDeviceFind'，表示BLE设备扫描结果上报事件。  当调用[ble.startBLEScan](js-apis-bluetooth-ble.md#blestartblescan) 后，开始BLE扫描，若扫描到BLE设备，触发该事件。 |
| callback | Callback<Array<[ScanResult](js-apis-bluetooth-ble.md#scanresult)>> | 是 | 指定订阅的回调函数，会携带扫描结果的集合。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: Array<ble.ScanResult>) {
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. ble.on('BLEDeviceFind', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

## ble.off('BLEDeviceFind')

PhonePC/2in1TabletTVWearable

off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void

取消订阅BLE设备扫描结果上报事件。

* 若不再需要扫描BLE设备，调用[ble.stopBLEScan](js-apis-bluetooth-ble.md#blestopblescan)方法后，需要调用此方法取消订阅。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEDeviceFind'，表示BLE设备扫描结果上报事件。 |
| callback | Callback<Array<[ScanResult](js-apis-bluetooth-ble.md#scanresult)>> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[ble.on('BLEDeviceFind')](js-apis-bluetooth-ble.md#bleonbledevicefind)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function onReceiveEvent(data: Array<ble.ScanResult>) {
3. console.info('bluetooth device find = '+ JSON.stringify(data));
4. }
5. try {
6. ble.on('BLEDeviceFind', onReceiveEvent);
7. ble.off('BLEDeviceFind', onReceiveEvent);
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## GattServer

PhonePC/2in1TabletTVWearable

GATT通信中的服务端类。

* 通过[ble.createGattServer](js-apis-bluetooth-ble.md#blecreategattserver)方法可以构造server实例。
* 通过该实例可以操作server端的行为，如添加服务[addService](js-apis-bluetooth-ble.md#addservice)、通知特征值变化[notifyCharacteristicChanged](js-apis-bluetooth-ble.md#notifycharacteristicchanged)等。
* 可通过订阅[on('connectionStateChange')](js-apis-bluetooth-ble.md#onconnectionstatechange)事件来感知连接状态，以及发起连接的client端设备地址。

### addService

PhonePC/2in1TabletTVWearable

addService(service: GattService): void

server端添加服务。该操作会在蓝牙子系统中注册该服务，表示server端支持的能力。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| service | [GattService](js-apis-bluetooth-ble.md#gattservice) | 是 | server端的service数据。表示支持的特定功能。  例如：00001800-0000-1000-8000-00805f9b34fb表示通用访问服务；00001801-0000-1000-8000-00805f9b34fb表示通用属性服务等。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // 创建descriptors。
3. let descriptors: Array<ble.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(2);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
7. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;

12. // 创建characteristics。
13. let characteristics: Array<ble.BLECharacteristic> = [];
14. let arrayBufferC = new ArrayBuffer(8);
15. let cccV = new Uint8Array(arrayBufferC);
16. cccV[0] = 1;
17. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
18. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
19. characteristics[0] = characteristic;

21. // 创建gattService。
22. let gattService: ble.GattService = {serviceUuid:'00001810-0000-1000-8000-00805F9B34FB', isPrimary: true, characteristics:characteristics, includeServices:[]};

24. try {
25. let gattServer: ble.GattServer = ble.createGattServer();
26. gattServer.addService(gattService);
27. } catch (err) {
28. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
29. }
```

### removeService

PhonePC/2in1TabletTVWearable

removeService(serviceUuid: string): void

删除server端已添加的服务。

* 该服务曾通过[addService](js-apis-bluetooth-ble.md#addservice)添加。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | 即将删除的服务的UUID。例如：00001810-0000-1000-8000-00805F9B34FB。 |

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
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let server: ble.GattServer = ble.createGattServer();
3. try {
4. // 调用removeService接口前需要完成server端和client端的配对及连接。
5. server.removeService('00001810-0000-1000-8000-00805F9B34FB');
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

### getService22+

PhonePC/2in1TabletTVWearable

getService(serviceUuid: string): GattService

获取指定的server端服务能力。

* 该服务已经通过[addService](js-apis-bluetooth-ble.md#addservice)方法添加后才能返回有效值。
* 一个应用可以通过[ble.createGattServer](js-apis-bluetooth-ble.md#blecreategattserver)方法创建多个[GattServer](js-apis-bluetooth-ble.md#gattserver)实例。本方法仅支持获取当前实例添加过的服务，无法获取当前应用创建的其他实例或由其他应用创建的实例添加过的服务。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serviceUuid | string | 是 | 需要获取的服务的UUID。例如：00001810-0000-1000-8000-00805F9B34FB。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattService](js-apis-bluetooth-ble.md#gattservice) | 指定的GATT服务。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2901008 | Gatt service is not found. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let server: ble.GattServer = ble.createGattServer();
3. try {
4. // 调用getService接口前需要先使用addService添加该服务。
5. let service: ble.GattService = server.getService('00001810-0000-1000-8000-00805F9B34FB');
6. console.info('characteristics size is: ' + service.characteristics.length);
7. for (let i = 0; i < service.characteristics.length; i++) {
8. console.info('characterUuid is: ' + service.characteristics[i].characteristicUuid);
9. }
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### getServices22+

PhonePC/2in1TabletTVWearable

getServices(): GattService[]

server端获取本端已添加的服务能力。

* 一个应用可以通过[ble.createGattServer](js-apis-bluetooth-ble.md#blecreategattserver)方法创建多个[GattServer](js-apis-bluetooth-ble.md#gattserver)实例。本方法仅支持获取当前实例添加过的服务，无法获取当前应用创建的其他实例或由其他应用创建的实例添加过的服务。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [GattService](js-apis-bluetooth-ble.md#gattservice)[] | server端已添加的服务能力。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
2. let server: ble.GattServer = ble.createGattServer();
3. try {
4. let services: ble.GattService[] = server.getServices();
5. console.info('services size is: ' + services.length);
6. for (let i = 0; i < services.length; i++) {
7. console.info('serviceUuid is: ' + services[i].serviceUuid);
8. }
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### close

PhonePC/2in1TabletTVWearable

close(): void

销毁server端实例。销毁后，通过[ble.createGattServer](js-apis-bluetooth-ble.md#blecreategattserver)创建的实例将不可用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let server: ble.GattServer = ble.createGattServer();
3. try {
4. server.close();
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### notifyCharacteristicChanged

PhonePC/2in1TabletTVWearable

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic, callback: AsyncCallback<void>): void

server端发送特征值变化通知或者指示给client端。使用Callback异步回调。

* 建议该特征值的Client Characteristic Configuration描述符（UUID：00002902-0000-1000-8000-00805f9b34fb）notification（通知）或indication（指示）能力已被使能。
* 蓝牙标准协议规定Client Characteristic Configuration描述符的数据内容长度为2字节，bit0和bit1分别表示notification（通知）和indication（指示）能力是否使能，例如bit0 = 1表示notification enabled。
* 该特征值数据内容变化时调用。
* [notifyCharacteristic](js-apis-bluetooth-ble.md#notifycharacteristic)入参的characteristicValue数据长度默认限制为（MTU-3）字节，MTU大小可从订阅的回调[on('BLEMtuChange')](js-apis-bluetooth-ble.md#onblemtuchange)获取。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 接收通知的client设备地址。例如：“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | [NotifyCharacteristic](js-apis-bluetooth-ble.md#notifycharacteristic) | 是 | 通知给client的特征值数据对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当通知成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferC = new ArrayBuffer(8);
3. let notifyCharacter: ble.NotifyCharacteristic = {
4. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
5. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
6. characteristicValue: arrayBufferC,
7. confirm: true
8. };
9. try {
10. let gattServer: ble.GattServer = ble.createGattServer();
11. gattServer.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacter, (err: BusinessError) => {
12. if (err) {
13. console.error('notifyCharacteristicChanged callback failed');
14. } else {
15. console.info('notifyCharacteristicChanged callback successful');
16. }
17. });
18. } catch (err) {
19. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
20. }
```

### notifyCharacteristicChanged

PhonePC/2in1TabletTVWearable

notifyCharacteristicChanged(deviceId: string, notifyCharacteristic: NotifyCharacteristic): Promise<void>

server端发送特征值变化通知或者指示给对端设备。使用Promise异步回调。

* 建议该特征值的Client Characteristic Configuration描述符notification（通知）或indication（指示）能力已被使能。
* 蓝牙标准协议规定Client Characteristic Configuration描述符的数据内容长度为2字节，bit0和bit1分别表示notification（通知）和indication（指示）能力是否使能，例如bit0 = 1表示notification enabled。
* 该特征值数据内容变化时调用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 接收通知的client设备地址。例如：“XX:XX:XX:XX:XX:XX”。 |
| notifyCharacteristic | [NotifyCharacteristic](js-apis-bluetooth-ble.md#notifycharacteristic) | 是 | 通知给client的特征值数据对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferC = new ArrayBuffer(8);
3. let notifyCharacter: ble.NotifyCharacteristic = {
4. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
5. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
6. characteristicValue: arrayBufferC,
7. confirm: true
8. };
9. try {
10. let gattServer: ble.GattServer = ble.createGattServer();
11. gattServer.notifyCharacteristicChanged('XX:XX:XX:XX:XX:XX', notifyCharacter).then(() => {
12. console.info('notifyCharacteristicChanged promise successful');
13. });
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

### sendResponse

PhonePC/2in1TabletTVWearable

sendResponse(serverResponse: ServerResponse): void

server端收到client的请求操作后，需要调用此接口回复client，否则可能导致链路异常，超时后断连。

client请求是指通过下述接口订阅回调收到的请求消息：

* [on('characteristicRead')](js-apis-bluetooth-ble.md#oncharacteristicread)
* [on('characteristicWrite')](js-apis-bluetooth-ble.md#oncharacteristicwrite)，需根据[CharacteristicWriteRequest](js-apis-bluetooth-ble.md#characteristicwriterequest)中的needRsp决定是否需要回复。
* [on('descriptorRead')](js-apis-bluetooth-ble.md#ondescriptorread)
* [on('descriptorWrite')](js-apis-bluetooth-ble.md#ondescriptorwrite)，需根据[DescriptorWriteRequest](js-apis-bluetooth-ble.md#descriptorwriterequest)中的needRsp决定是否需要回复。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| serverResponse | [ServerResponse](js-apis-bluetooth-ble.md#serverresponse) | 是 | server端回复client的响应数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. /* send response */
3. let arrayBufferCCC = new ArrayBuffer(8);
4. let cccValue = new Uint8Array(arrayBufferCCC);
5. cccValue[0] = 1;
6. let serverResponse: ble.ServerResponse = {
7. deviceId: 'XX:XX:XX:XX:XX:XX',
8. transId: 0,
9. status: 0,
10. offset: 0,
11. value: arrayBufferCCC
12. };
13. try {
14. let gattServer: ble.GattServer = ble.createGattServer();
15. gattServer.sendResponse(serverResponse);
16. } catch (err) {
17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
18. }
```

### on('characteristicRead')

PhonePC/2in1TabletTVWearable

on(type: 'characteristicRead', callback: Callback<CharacteristicReadRequest>): void

server端订阅client的特征值读请求事件，server端收到该事件后需要调用[sendResponse](js-apis-bluetooth-ble.md#sendresponse)接口回复client。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'characteristicRead'，表示特征值读请求事件。  当收到client端设备的读取特征值请求时，触发该事件。 |
| callback | Callback<[CharacteristicReadRequest](js-apis-bluetooth-ble.md#characteristicreadrequest)> | 是 | 指定订阅的回调函数，会携带client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferCCC = new ArrayBuffer(8);
3. let cccValue = new Uint8Array(arrayBufferCCC);
4. cccValue[0] = 1;
5. let gattServer: ble.GattServer = ble.createGattServer();
6. function ReadCharacteristicReq(characteristicReadRequest: ble.CharacteristicReadRequest) {
7. let deviceId: string = characteristicReadRequest.deviceId;
8. let transId: number = characteristicReadRequest.transId;
9. let offset: number = characteristicReadRequest.offset;
10. let characteristicUuid: string = characteristicReadRequest.characteristicUuid;

12. let serverResponse: ble.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

14. try {
15. gattServer.sendResponse(serverResponse);
16. } catch (err) {
17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
18. }
19. }
20. gattServer.on('characteristicRead', ReadCharacteristicReq);
```

### off('characteristicRead')

PhonePC/2in1TabletTVWearable

off(type: 'characteristicRead', callback?: Callback<CharacteristicReadRequest>): void

server端取消订阅client的特征值读请求事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'characteristicRead'，表示特征值读请求事件。 |
| callback | Callback<[CharacteristicReadRequest](js-apis-bluetooth-ble.md#characteristicreadrequest)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('characteristicRead')](js-apis-bluetooth-ble.md#oncharacteristicread)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.off('characteristicRead');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('characteristicWrite')

PhonePC/2in1TabletTVWearable

on(type: 'characteristicWrite', callback: Callback<CharacteristicWriteRequest>): void

server端订阅client的特征值写请求事件，server端收到该事件后需要根据[CharacteristicWriteRequest](js-apis-bluetooth-ble.md#characteristicwriterequest)中的needRsp决定是否调用[sendResponse](js-apis-bluetooth-ble.md#sendresponse)接口回复client。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'characteristicWrite'，表示特征值写请求事件。  当收到client端设备的写特征值请求时，触发该事件。 |
| callback | Callback<[CharacteristicWriteRequest](js-apis-bluetooth-ble.md#characteristicwriterequest)> | 是 | 指定订阅的回调函数，会携带client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferCCC = new ArrayBuffer(8);
3. let cccValue = new Uint8Array(arrayBufferCCC);
4. let gattServer: ble.GattServer = ble.createGattServer();
5. function WriteCharacteristicReq(characteristicWriteRequest: ble.CharacteristicWriteRequest) {
6. let deviceId: string = characteristicWriteRequest.deviceId;
7. let transId: number = characteristicWriteRequest.transId;
8. let offset: number = characteristicWriteRequest.offset;
9. let isPrepared: boolean = characteristicWriteRequest.isPrepared;
10. let needRsp: boolean = characteristicWriteRequest.needRsp;
11. let value: Uint8Array =  new Uint8Array(characteristicWriteRequest.value);
12. let characteristicUuid: string = characteristicWriteRequest.characteristicUuid;

14. cccValue[0] = value[0];
15. let serverResponse: ble.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferCCC};

17. try {
18. gattServer.sendResponse(serverResponse);
19. } catch (err) {
20. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
21. }
22. }
23. gattServer.on('characteristicWrite', WriteCharacteristicReq);
```

### off('characteristicWrite')

PhonePC/2in1TabletTVWearable

off(type: 'characteristicWrite', callback?: Callback<CharacteristicWriteRequest>): void

server端取消订阅client的特征值写请求事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'characteristicWrite'，表示特征值写请求事件。 |
| callback | Callback<[CharacteristicWriteRequest](js-apis-bluetooth-ble.md#characteristicwriterequest)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('characteristicWrite')](js-apis-bluetooth-ble.md#oncharacteristicwrite)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.off('characteristicWrite');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('descriptorRead')

PhonePC/2in1TabletTVWearable

on(type: 'descriptorRead', callback: Callback<DescriptorReadRequest>): void

server端订阅client的描述符读请求事件，server端收到该事件后需要调用[sendResponse](js-apis-bluetooth-ble.md#sendresponse)接口回复client。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'descriptorRead'，表示描述符读请求事件。  当收到client端设备的读取描述符请求时，触发该事件。 |
| callback | Callback<[DescriptorReadRequest](js-apis-bluetooth-ble.md#descriptorreadrequest)> | 是 | 指定订阅的回调函数，会携带client端发送的读请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferDesc = new ArrayBuffer(8);
3. let descValue = new Uint8Array(arrayBufferDesc);
4. descValue[0] = 1;
5. let gattServer: ble.GattServer = ble.createGattServer();
6. function ReadDescriptorReq(descriptorReadRequest: ble.DescriptorReadRequest) {
7. let deviceId: string = descriptorReadRequest.deviceId;
8. let transId: number = descriptorReadRequest.transId;
9. let offset: number = descriptorReadRequest.offset;
10. let descriptorUuid: string = descriptorReadRequest.descriptorUuid;

12. let serverResponse: ble.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

14. try {
15. gattServer.sendResponse(serverResponse);
16. } catch (err) {
17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
18. }
19. }
20. gattServer.on('descriptorRead', ReadDescriptorReq);
```

### off('descriptorRead')

PhonePC/2in1TabletTVWearable

off(type: 'descriptorRead', callback?: Callback<DescriptorReadRequest>): void

server端取消订阅client的描述符读请求事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'descriptorRead'，表示描述符读请求事件。 |
| callback | Callback<[DescriptorReadRequest](js-apis-bluetooth-ble.md#descriptorreadrequest)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('descriptorRead')](js-apis-bluetooth-ble.md#ondescriptorread)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.off('descriptorRead');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('descriptorWrite')

PhonePC/2in1TabletTVWearable

on(type: 'descriptorWrite', callback: Callback<DescriptorWriteRequest>): void

server端订阅client的描述符写请求事件，server端收到该事件后需要根据[DescriptorWriteRequest](js-apis-bluetooth-ble.md#descriptorwriterequest)里的needRsp决定是否调用[sendResponse](js-apis-bluetooth-ble.md#sendresponse)接口回复client。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'descriptorWrite'，表示描述符写请求事件。  当收到client端设备的写描述符请求时，触发该事件。 |
| callback | Callback<[DescriptorWriteRequest](js-apis-bluetooth-ble.md#descriptorwriterequest)> | 是 | 指定订阅的回调函数，会携带client端发送的写请求数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let arrayBufferDesc = new ArrayBuffer(8);
3. let descValue = new Uint8Array(arrayBufferDesc);
4. let gattServer: ble.GattServer = ble.createGattServer();
5. function WriteDescriptorReq(descriptorWriteRequest: ble.DescriptorWriteRequest) {
6. let deviceId: string = descriptorWriteRequest.deviceId;
7. let transId: number = descriptorWriteRequest.transId;
8. let offset: number = descriptorWriteRequest.offset;
9. let isPrepared: boolean = descriptorWriteRequest.isPrepared;
10. let needRsp: boolean = descriptorWriteRequest.needRsp;
11. let value: Uint8Array = new Uint8Array(descriptorWriteRequest.value);
12. let descriptorUuid: string = descriptorWriteRequest.descriptorUuid;

14. descValue[0] = value[0];
15. let serverResponse: ble.ServerResponse = {deviceId: deviceId, transId: transId, status: 0, offset: offset, value:arrayBufferDesc};

17. try {
18. gattServer.sendResponse(serverResponse);
19. } catch (err) {
20. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
21. }
22. }
23. gattServer.on('descriptorWrite', WriteDescriptorReq);
```

### off('descriptorWrite')

PhonePC/2in1TabletTVWearable

off(type: 'descriptorWrite', callback?: Callback<DescriptorWriteRequest>): void

server端取消订阅client的描述符写请求事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'descriptorWrite'，表示描述符写请求事件。 |
| callback | Callback<[DescriptorWriteRequest](js-apis-bluetooth-ble.md#descriptorwriterequest)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('descriptorWrite')](js-apis-bluetooth-ble.md#ondescriptorwrite)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.off('descriptorWrite');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('connectionStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'connectionStateChange', callback: Callback<BLEConnectionChangeState>): void

server端订阅GATT profile协议的连接状态变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示GATT profile连接状态发生变化的事件。  当client和server端之间的连接状态发生变化时，触发该事件。  例如：收到连接请求或者断连请求时，可能引起连接状态生变化。 |
| callback | Callback<[BLEConnectionChangeState](js-apis-bluetooth-ble.md#bleconnectionchangestate)> | 是 | 指定订阅的回调函数，会携带连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { constant } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. let connected = (bleConnectionChangeState: ble.BLEConnectionChangeState) => {
4. let deviceId: string = bleConnectionChangeState.deviceId;
5. let status: constant.ProfileConnectionState = bleConnectionChangeState.state;
6. }
7. try {
8. let gattServer: ble.GattServer = ble.createGattServer();
9. gattServer.on('connectionStateChange', connected);
10. } catch (err) {
11. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
12. }
```

### off('connectionStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'connectionStateChange', callback?: Callback<BLEConnectionChangeState>): void

server端取消订阅GATT profile协议的连接状态变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'connectionStateChange'，表示GATT profile连接状态发生变化的事件。 |
| callback | Callback<[BLEConnectionChangeState](js-apis-bluetooth-ble.md#bleconnectionchangestate)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('connectionStateChange')](js-apis-bluetooth-ble.md#onconnectionstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.off('connectionStateChange');
5. } catch (err) {
6. console.error("errCode:" + (err as BusinessError).code + ",errMessage:" + (err as BusinessError).message);
7. }
```

### on('BLEMtuChange')

PhonePC/2in1TabletTVWearable

on(type: 'BLEMtuChange', callback: Callback<number>): void

server端订阅MTU（最大传输单元）大小变更事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEMtuChange'，表示MTU状态变化事件。  当收到了client端发起了MTU协商请求时，触发该事件。 |
| callback | Callback<number> | 是 | 指定订阅的回调函数，会携带协商后的MTU大小。单位：Byte。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.on('BLEMtuChange', (mtu: number) => {
5. console.info('BLEMtuChange, mtu: ' + mtu);
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

### off('BLEMtuChange')

PhonePC/2in1TabletTVWearable

off(type: 'BLEMtuChange', callback?: Callback<number>): void

server端取消订阅MTU（最大传输单元）大小变更事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为"BLEMtuChange"，表示MTU状态变化事件。 |
| callback | Callback<number> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('BLEMtuChange')](js-apis-bluetooth-ble.md#onblemtuchange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattServer: ble.GattServer = ble.createGattServer();
4. gattServer.off('BLEMtuChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### getConnectedState22+

PhonePC/2in1TabletTVWearable

getConnectedState(deviceId: string): ProfileConnectionState

获取当前与client端设备的连接状态。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 要查询连接状态的对端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth-ble.md#profileconnectionstate) | 蓝牙设备的profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
2. let gattServer: ble.GattServer = ble.createGattServer();
3. let deviceId: string = 'XX:XX:XX:XX:XX:XX';
4. try {
5. let result: ble.ProfileConnectionState = gattServer.getConnectedState(deviceId);
6. } catch (err) {
7. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
8. }
```

### readPhy23+

PhonePC/2in1TabletTVWearable

readPhy(deviceId: string): Promise<PhyValue>

获取server端和指定设备连接链路的物理通道类型。使用Promise异步回调。

* 需先由client端发起连接，并等待连接成功后，再调用该方法。
* deviceId为对端client的蓝牙设备地址，可从server端订阅的[on('connectionStateChange')](js-apis-bluetooth-ble.md#onconnectionstatechange)回调中获取。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 需要传输数据的client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PhyValue](js-apis-bluetooth-ble.md#phyvalue23)> | Promise对象，返回server端和指定设备连接链路的物理通道类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. let gattServer: ble.GattServer = ble.createGattServer();
2. let deviceId: string = 'XX:XX:XX:XX:XX:XX';
3. try {
4. gattServer.readPhy(deviceId).then((phyValue:ble.PhyValue) => {
5. console.info(`txPhy: ${phyValue.txPhy}, rxPhy: ${phyValue.rxPhy}`);
6. });
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### setPhy23+

PhonePC/2in1TabletTVWearable

setPhy(deviceId: string, phyValue: PhyValue): Promise<void>

server端设置和指定设备连接链路的物理通道类型。使用Promise异步回调。

* 需先由client端发起连接，并等待连接成功后，再调用该方法。
* 本端server调用setPhy设置和指定设备连接链路的物理通道类型后，底层会根据对端设备能力，协商出本端和对端设备均支持的物理通道类型作为最终结果。例如本端支持并设置[BLE\_PHY\_2M](js-apis-bluetooth-ble.md#blephy23)，但对端设备仅支持[BLE\_PHY\_1M](js-apis-bluetooth-ble.md#blephy23)，则最终设置的结果仍为[BLE\_PHY\_1M](js-apis-bluetooth-ble.md#blephy23)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceId | string | 是 | 需要传输数据的client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| phyValue | [PhyValue](js-apis-bluetooth-ble.md#phyvalue23) | 是 | 连接链路的物理通道类型配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. let gattServer: ble.GattServer = ble.createGattServer();
2. let deviceId: string = 'XX:XX:XX:XX:XX:XX';
3. try {
4. let phyValue:ble.PhyValue = {
5. txPhy: ble.BlePhy.BLE_PHY_1M,
6. rxPhy: ble.BlePhy.BLE_PHY_1M
7. };
8. gattServer.setPhy(deviceId,phyValue);
9. } catch (err) {
10. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
11. }
```

### onBlePhyUpdate23+

PhonePC/2in1TabletTVWearable

onBlePhyUpdate(callback: Callback<PhyValue>): void

订阅物理通道类型变更事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PhyValue](js-apis-bluetooth-ble.md#phyvalue23)> | 是 | 指定订阅的回调函数，会携带变更后最新的物理通道类型。  当本端server调用[setPhy](js-apis-bluetooth-ble.md#setphy23)或对端变更当前物理通道类型后，如订阅此事件，均会收到携带最新物理通道类型的回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function BlePhyCallback(data:ble.PhyValue) {
2. console.info(`txPhy: ${data.txPhy}, rxPhy: ${data.rxPhy}`);
3. }
4. let gattServer: ble.GattServer = ble.createGattServer();
5. try {
6. gattServer.onBlePhyUpdate(BlePhyCallback);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offBlePhyUpdate23+

PhonePC/2in1TabletTVWearable

offBlePhyUpdate(callback?: Callback<PhyValue>): void

取消订阅物理通道类型变更事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PhyValue](js-apis-bluetooth-ble.md#phyvalue23)> | 否 | 指定取消订阅的回调函数。若传参，则需与[onBlePhyUpdate](js-apis-bluetooth-ble.md#onblephyupdate23)中的回调函数一致，  若无传参，则取消订阅所有物理通道类型变更的回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function BlePhyCallback(data:ble.PhyValue) {
2. console.info(`txPhy: ${data.txPhy}, rxPhy: ${data.rxPhy}`);
3. }
4. let gattServer: ble.GattServer = ble.createGattServer();
5. try {
6. gattServer.offBlePhyUpdate(BlePhyCallback);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

## GattClientDevice

PhonePC/2in1TabletTVWearable

GATT客户端类，提供了和服务端进行连接和数据传输等操作方法。

* 使用该类的方法前，需通过[createGattClientDevice](js-apis-bluetooth-ble.md#blecreategattclientdevice)方法构造该类的实例。
* 通过创建不同的该类实例，可以管理多路GATT连接。

### connect

PhonePC/2in1TabletTVWearable

connect(): void

client端主动发起和server蓝牙设备的GATT协议连接。

* 远端设备地址已通过[createGattClientDevice](js-apis-bluetooth-ble.md#blecreategattclientdevice)方法中的deviceId参数指定。
* client可通过订阅[on('BLEConnectionStateChange')](js-apis-bluetooth-ble.md#onbleconnectionstatechange)事件来感知连接是否成功。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.connect();
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### disconnect

PhonePC/2in1TabletTVWearable

disconnect(): void

client断开与远端蓝牙低功耗设备的连接。

* client可通过订阅[on('BLEConnectionStateChange')](js-apis-bluetooth-ble.md#onbleconnectionstatechange)事件来感知连接是否成功。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.disconnect();
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### close

PhonePC/2in1TabletTVWearable

close(): void

销毁client端实例。销毁后，通过[GattClientDevice](js-apis-bluetooth-ble.md#gattclientdevice)创建的实例将不可用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.close();
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### getDeviceName

PhonePC/2in1TabletTVWearable

getDeviceName(callback: AsyncCallback<string>): void

client获取server端设备名称。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当读取成功，err为undefined，data为server端设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. let gattClient: ble.GattClientDevice = ble.createGattClientDevice("11:22:33:44:55:66");
4. function ConnectStateChanged(state: ble.BLEConnectionChangeState) {
5. console.info('bluetooth connect state changed');
6. let connectState: ble.ProfileConnectionState = state.state;
7. if (connectState == constant.ProfileConnectionState.STATE_CONNECTED) {
8. gattClient.getDeviceName((err: BusinessError, data: string)=> {
9. console.info('device name err ' + JSON.stringify(err));
10. console.info('device name' + JSON.stringify(data));
11. })
12. }
13. }
14. // callback
15. try {
16. gattClient.connect();
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

### getDeviceName

PhonePC/2in1TabletTVWearable

getDeviceName(): Promise<string>

client获取远端蓝牙低功耗设备的名称。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，携带server端设备名称。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. let gattClient: ble.GattClientDevice = ble.createGattClientDevice("11:22:33:44:55:66");
4. gattClient.on('BLEConnectionStateChange', ConnectStateChanged);
5. function ConnectStateChanged(state: ble.BLEConnectionChangeState) {
6. console.info('bluetooth connect state changed');
7. let connectState: ble.ProfileConnectionState = state.state;
8. if (connectState == constant.ProfileConnectionState.STATE_CONNECTED) {
9. gattClient.getDeviceName().then((data: string) => {
10. console.info('device name' + JSON.stringify(data));
11. })
12. }
13. }
14. // promise
15. try {
16. gattClient.connect();
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

### getServices

PhonePC/2in1TabletTVWearable

getServices(callback: AsyncCallback<Array<GattService>>): void

client获取server端支持的所有服务能力，即服务发现流程。使用Callback异步回调。

应用调用该方法后，才能调用其他读写特征值、描述符等其他方法，且需确保server支持的服务能力中包含需要操作的特征值或描述符。包含接口如下所示：

* [readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)
* [readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)
* [writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)
* [writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)
* [setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)
* [setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[GattService](js-apis-bluetooth-ble.md#gattservice)>> | 是 | 回调函数。当读取成功，err为undefined，data为server端的服务列表。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. // callback 模式。
4. let getServices = (code: BusinessError, gattServices: Array<ble.GattService>) => {
5. if (code && code.code != 0) {
6. console.info('bluetooth code is ' + code.code);
7. return;
8. }
9. let services: Array<ble.GattService> = gattServices;
10. console.info('bluetooth services size is ', services.length);
11. for (let i = 0; i < services.length; i++) {
12. console.info('bluetooth serviceUuid is ' + services[i].serviceUuid);
13. }
14. }
15. let device: ble.GattClientDevice = ble.createGattClientDevice("11:22:33:44:55:66");
16. function ConnectStateChanged(state: ble.BLEConnectionChangeState) {
17. console.info('bluetooth connect state changed');
18. let connectState: ble.ProfileConnectionState = state.state;
19. if (connectState == constant.ProfileConnectionState.STATE_CONNECTED) {
20. device.getServices(getServices);
21. }
22. }

24. try {
25. device.connect();
26. } catch (err) {
27. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
28. }
```

### getServices

PhonePC/2in1TabletTVWearable

getServices(): Promise<Array<GattService>>

client端获取蓝牙低功耗设备的所有服务，即服务发现。使用Promise异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[GattService](js-apis-bluetooth-ble.md#gattservice)>> | Promise对象，返回获取到的server端服务列表。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { ble, constant } from '@kit.ConnectivityKit';
2. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
3. // Promise 模式。
4. let device: ble.GattClientDevice = ble.createGattClientDevice("11:22:33:44:55:66");
5. function ConnectStateChanged(state: ble.BLEConnectionChangeState) {
6. console.info('bluetooth connect state changed');
7. let connectState: ble.ProfileConnectionState = state.state;
8. if (connectState == constant.ProfileConnectionState.STATE_CONNECTED) {
9. device.getServices().then((result: Array<ble.GattService>) => {
10. console.info('getServices successfully:' + JSON.stringify(result));
11. });
12. }
13. }
14. try {
15. device.connect();
16. } catch (err) {
17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
18. }
```

### readCharacteristicValue

PhonePC/2in1TabletTVWearable

readCharacteristicValue(characteristic: BLECharacteristic, callback: AsyncCallback<BLECharacteristic>): void

client端从指定的server端特征值读取数据。使用Callback异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参特征值UUID；否则会读取失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 读取特征值过程中，需确保[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)入参特征值的serviceUuid、characteristicUuid准确。characteristicValue表示的数据内容长度可由用户任意指定，不会影响实际读取到的特征值数据内容。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要读取的特征值。 |
| callback | AsyncCallback<[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)> | 是 | 回调函数。当读取成功，err为undefined，data为获取到的特征值对象，包含读取到的数据内容；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901000 | Read forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function readCcc(code: BusinessError, BLECharacteristic: ble.BLECharacteristic) {
3. if (code.code != 0) {
4. return;
5. }
6. console.info('bluetooth characteristic uuid: ' + BLECharacteristic.characteristicUuid);
7. let value = new Uint8Array(BLECharacteristic.characteristicValue);
8. console.info('bluetooth characteristic value: ' + value[0]);
9. }

11. let descriptors: Array<ble.BLEDescriptor> = [];
12. let bufferDesc = new ArrayBuffer(2);
13. let descV = new Uint8Array(bufferDesc);
14. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
15. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
16. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
17. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
18. descriptors[0] = descriptor;

20. let bufferCCC = new ArrayBuffer(8);
21. let cccV = new Uint8Array(bufferCCC);
22. cccV[0] = 1;
23. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
24. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
25. characteristicValue: bufferCCC, descriptors:descriptors};

27. try {
28. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
29. device.readCharacteristicValue(characteristic, readCcc);
30. } catch (err) {
31. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
32. }
```

### readCharacteristicValue

PhonePC/2in1TabletTVWearable

readCharacteristicValue(characteristic: BLECharacteristic): Promise<BLECharacteristic>

client端从指定的server端特征值读取数据。使用Promise异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参特征值UUID；否则会读取失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 读取特征值过程中，需确保[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)入参特征值的serviceUuid、characteristicUuid准确。characteristicValue表示的数据内容长度可由用户任意指定，不会影响实际读取到的特征值数据内容。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要读取的特征值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)> | Promise对象，返回获取到的特征值对象，包含读取到的数据内容。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901000 | Read forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let descriptors: Array<ble.BLEDescriptor> = [];
3. let bufferDesc = new ArrayBuffer(2);
4. let descV = new Uint8Array(bufferDesc);
5. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
6. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
9. descriptors[0] = descriptor;

11. let bufferCCC = new ArrayBuffer(8);
12. let cccV = new Uint8Array(bufferCCC);
13. cccV[0] = 1;
14. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
16. characteristicValue: bufferCCC, descriptors:descriptors};

18. try {
19. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
20. device.readCharacteristicValue(characteristic);
21. } catch (err) {
22. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
23. }
```

### readDescriptorValue

PhonePC/2in1TabletTVWearable

readDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<BLEDescriptor>): void

client端从指定的server端描述符读取数据。使用Callback异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参描述符UUID；否则会读取失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 读取描述符过程中，需确保[BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor)入参描述符的serviceUuid、characteristicUuid、descriptorUuid准确。descriptorValue表示的数据内容长度可由用户任意指定，不会影响实际读取到的描述符数据内容。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor) | 是 | 需要读取的描述符。 |
| callback | AsyncCallback<[BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor)> | 是 | 回调函数。当读取成功，err为undefined，data为获取到的描述符对象，包含读取到的数据内容；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901000 | Read forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function readDesc(code: BusinessError, BLEDescriptor: ble.BLEDescriptor) {
3. if (code.code != 0) {
4. return;
5. }
6. console.info('bluetooth descriptor uuid: ' + BLEDescriptor.descriptorUuid);
7. let value = new Uint8Array(BLEDescriptor.descriptorValue);
8. console.info('bluetooth descriptor value: ' + value[0]);
9. }

11. let bufferDesc = new ArrayBuffer(2);
12. let descV = new Uint8Array(bufferDesc);
13. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
14. let descriptor: ble.BLEDescriptor = {
15. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
16. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
17. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
18. descriptorValue: bufferDesc
19. };
20. try {
21. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
22. device.readDescriptorValue(descriptor, readDesc);
23. } catch (err) {
24. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
25. }
```

### readDescriptorValue

PhonePC/2in1TabletTVWearable

readDescriptorValue(descriptor: BLEDescriptor): Promise<BLEDescriptor>

client端从指定的server端描述符读取数据。使用Promise异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参描述符UUID；否则会读取失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 读取描述符过程中，需确保[BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor)入参描述符的serviceUuid、characteristicUuid、descriptorUuid准确。descriptorValue表示的数据内容长度可由用户任意指定，不会影响实际读取到的描述符数据内容。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor) | 是 | 需要读取的描述符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor)> | Promise对象，返回获取到的描述符对象，包含读取到的数据内容。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901000 | Read forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let bufferDesc = new ArrayBuffer(2);
3. let descV = new Uint8Array(bufferDesc);
4. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
5. let descriptor: ble.BLEDescriptor = {
6. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
9. descriptorValue: bufferDesc
10. };
11. try {
12. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
13. device.readDescriptorValue(descriptor);
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

### writeCharacteristicValue

PhonePC/2in1TabletTVWearable

writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType, callback: AsyncCallback<void>): void

client端向指定的server端特征值写入数据。使用Callback异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参特征值UUID；否则会写入失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 应用单次可写入的特征值数据长度限制为（MTU-3）字节。调用方可根据实际需要通过[setBLEMtuSize](js-apis-bluetooth-ble.md#setblemtusize)接口指定MTU大小，进而修改单次可写入的特征值数据长度。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要写入的特征值，包含写入的数据内容。 |
| writeType | [GattWriteType](js-apis-bluetooth-ble.md#gattwritetype) | 是 | 写入特征值的方式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901001 | Write forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let descriptors: Array<ble.BLEDescriptor> = [];
3. let bufferDesc = new ArrayBuffer(2);
4. let descV = new Uint8Array(bufferDesc);
5. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
6. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
9. descriptors[0] = descriptor;

11. let bufferCCC = new ArrayBuffer(8);
12. let cccV = new Uint8Array(bufferCCC);
13. cccV[0] = 1;
14. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
16. characteristicValue: bufferCCC, descriptors:descriptors};
17. function writeCharacteristicValueCallBack(code: BusinessError) {
18. if (code != null) {
19. return;
20. }
21. console.info('bluetooth writeCharacteristicValue success');
22. }
23. try {
24. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
25. device.writeCharacteristicValue(characteristic, ble.GattWriteType.WRITE, writeCharacteristicValueCallBack);
26. } catch (err) {
27. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
28. }
```

### writeCharacteristicValue

PhonePC/2in1TabletTVWearable

writeCharacteristicValue(characteristic: BLECharacteristic, writeType: GattWriteType): Promise<void>

client端向指定的server端特征值写入数据。使用Promise异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参特征值UUID；否则会写入失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 应用单次可写入的特征值数据长度限制为（MTU-3）字节。调用方可根据实际需要通过[setBLEMtuSize](js-apis-bluetooth-ble.md#setblemtusize)接口指定MTU大小，进而修改单次可写入的特征值数据长度。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要写入的特征值，包含写入的数据内容。 |
| writeType | [GattWriteType](js-apis-bluetooth-ble.md#gattwritetype) | 是 | 写入特征值的方式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901001 | Write forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let descriptors: Array<ble.BLEDescriptor>  = [];
3. let bufferDesc = new ArrayBuffer(2);
4. let descV = new Uint8Array(bufferDesc);
5. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
6. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: bufferDesc};
9. descriptors[0] = descriptor;

11. let bufferCCC = new ArrayBuffer(8);
12. let cccV = new Uint8Array(bufferCCC);
13. cccV[0] = 1;
14. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
15. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
16. characteristicValue: bufferCCC, descriptors:descriptors};
17. try {
18. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
19. device.writeCharacteristicValue(characteristic, ble.GattWriteType.WRITE);
20. } catch (err) {
21. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
22. }
```

### writeDescriptorValue

PhonePC/2in1TabletTVWearable

writeDescriptorValue(descriptor: BLEDescriptor, callback: AsyncCallback<void>): void

client端向指定的server端描述符写入数据。使用Callback异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参描述符UUID；否则会写入失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 应用单次可写入的描述符数据长度限制为（MTU-3）字节。调用方可根据实际需要通过[setBLEMtuSize](js-apis-bluetooth-ble.md#setblemtusize)接口指定MTU大小，进而修改单次可写入的描述符数据长度。
* Client Characteristic Configuration描述符（UUID：00002902-0000-1000-8000-00805f9b34fb）和 Server Characteristic Configuration描述符（UUID：00002903-0000-1000-8000-00805f9b34fb）较为特殊，蓝牙标准协议规定内容长度为2字节，写入内容长度应设置为2字节。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor) | 是 | 需要写入的描述符，包含写入的数据内容。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901001 | Write forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let bufferDesc = new ArrayBuffer(2);
3. let descV = new Uint8Array(bufferDesc);
4. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
5. let descriptor: ble.BLEDescriptor = {
6. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
9. descriptorValue: bufferDesc
10. };
11. try {
12. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
13. device.writeDescriptorValue(descriptor, (err: BusinessError) => {
14. if (err) {
15. console.error('writeDescriptorValue callback failed');
16. } else {
17. console.info('writeDescriptorValue callback successful');
18. }
19. });
20. } catch (err) {
21. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
22. }
```

### writeDescriptorValue

PhonePC/2in1TabletTVWearable

writeDescriptorValue(descriptor: BLEDescriptor): Promise<void>

client端向指定的server端描述符写入数据。使用Promise异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且包含指定的入参描述符UUID；否则会写入失败。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。
* 应用单次可写入的描述符数据长度限制为（MTU-3）字节。调用方可根据实际需要通过[setBLEMtuSize](js-apis-bluetooth-ble.md#setblemtusize)接口指定MTU大小，进而修改单次可写入的描述符数据长度。
* Client Characteristic Configuration描述符（UUID：00002902-0000-1000-8000-00805f9b34fb）和 Server Characteristic Configuration描述符（UUID：00002903-0000-1000-8000-00805f9b34fb）较为特殊，蓝牙标准协议规定内容长度为2字节，写入内容长度应设置为2字节。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| descriptor | [BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor) | 是 | 需要写入的描述符，包含写入的数据内容。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901001 | Write forbidden. |
| 2901003 | The connection is not established. |
| 2901004 | The connection is congested. |
| 2901005 | The connection is not encrypted. |
| 2901006 | The connection is not authenticated. |
| 2901007 | The connection is not authorized. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. let bufferDesc = new ArrayBuffer(2);
3. let descV = new Uint8Array(bufferDesc);
4. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
5. let descriptor: ble.BLEDescriptor = {
6. serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
7. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
8. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB',
9. descriptorValue: bufferDesc
10. };
11. try {
12. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
13. device.writeDescriptorValue(descriptor).then(() => {
14. console.info('writeDescriptorValue promise success');
15. });
16. } catch (err) {
17. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
18. }
```

### getRssiValue

PhonePC/2in1TabletTVWearable

getRssiValue(callback: AsyncCallback<number>): void

client端获取GATT连接链路信号强度 (Received Signal Strength Indication, RSSI)。使用Callback异步回调。

* 需先调用[connect](js-apis-bluetooth-ble.md#connect)方法，等GATT profile连接成功后才能使用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。获取链路信号强度成功，err为undefined，data为获取到的信号强度值，单位：dBm；否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // callback
3. try {
4. let gattClient: ble.GattClientDevice = ble.createGattClientDevice("XX:XX:XX:XX:XX:XX");
5. gattClient.connect();
6. let rssi = gattClient.getRssiValue((err: BusinessError, data: number)=> {
7. console.info('rssi err ' + JSON.stringify(err));
8. console.info('rssi value' + JSON.stringify(data));
9. })
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### getRssiValue

PhonePC/2in1TabletTVWearable

getRssiValue(): Promise<number>

client端获取GATT连接链路信号强度 (Received Signal Strength Indication, RSSI)。使用Promise异步回调。

* 需先调用[connect](js-apis-bluetooth-ble.md#connect)方法，等GATT profile连接成功后才能使用。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象。返回链路的信号强度，单位：dBm。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // promise
3. try {
4. let gattClient: ble.GattClientDevice = ble.createGattClientDevice("XX:XX:XX:XX:XX:XX");
5. gattClient.getRssiValue().then((data: number) => {
6. console.info('rssi' + JSON.stringify(data));
7. })
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

### setBLEMtuSize

PhonePC/2in1TabletTVWearable

setBLEMtuSize(mtu: number): void

client端同server端协商[MTU](../harmonyos-guides/terminology.md#mtu)（最大传输单元）大小。

* 需先调用[connect](js-apis-bluetooth-ble.md#connect)方法，等GATT profile连接成功后才能使用。
* 通过[on('BLEMtuChange')](js-apis-bluetooth-ble.md#onblemtuchange-1)，订阅MTU协商结果。
* 如果未协商，MTU大小默认为23字节。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| mtu | number | 是 | 需要协商的mtu大小，取值范围：[23, 517]，单位：Byte。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.setBLEMtuSize(128);
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### setCharacteristicChangeNotification

PhonePC/2in1TabletTVWearable

setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void

client端启用或者禁用接收server端特征值内容变更通知的能力。使用Callback异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且需包含指定的入参特征值UUID。
* server端对应的特征值需包含标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），server端才能支持发送变更通知。
* 若启用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，启用server端的通知能力。
* 若禁用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，禁用server端的通知能力。
* 通过[on('BLECharacteristicChange')](js-apis-bluetooth-ble.md#onblecharacteristicchange)接收server端特征值内容变更通知。
* 若client端收到server端特征值内容变更通知后，无需回复确认。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要管理的server端特征值。 |
| enable | boolean | 是 | 是否启用接收server端特征值通知的能力。  true表示启用，false表示禁用。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当调用成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // 创建descriptors。
3. let descriptors: Array<ble.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(2);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
7. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;
11. let arrayBufferC = new ArrayBuffer(8);
12. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
13. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
14. try {
15. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
16. device.setCharacteristicChangeNotification(characteristic, false, (err: BusinessError) => {
17. if (err) {
18. console.error('notifyCharacteristicChanged callback failed');
19. } else {
20. console.info('notifyCharacteristicChanged callback successful');
21. }
22. });
23. } catch (err) {
24. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
25. }
```

### setCharacteristicChangeNotification

PhonePC/2in1TabletTVWearable

setCharacteristicChangeNotification(characteristic: BLECharacteristic, enable: boolean): Promise<void>

client端启用或者禁用接收server端特征值内容变更通知的能力。使用Promise异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且需包含指定的入参特征值UUID。
* server端对应的特征值需包含标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），server端才能支持发送变更通知。
* 若启用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，启用server端的通知能力。
* 若禁用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，禁用server端的通知能力。
* 通过[on('BLECharacteristicChange')](js-apis-bluetooth-ble.md#onblecharacteristicchange)接收server端特征值内容变更通知。
* 若client端收到server端特征值内容变更通知后，无需回复确认。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要管理的server端特征值。 |
| enable | boolean | 是 | 是否启用接收server端特征值通知的能力。  true表示启用，false表示禁用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // 创建descriptors。
3. let descriptors: Array<ble.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(2);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
7. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;
11. let arrayBufferC = new ArrayBuffer(8);
12. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
13. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
14. try {
15. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
16. device.setCharacteristicChangeNotification(characteristic, false);
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

### setCharacteristicChangeIndication

PhonePC/2in1TabletTVWearable

setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean, callback: AsyncCallback<void>): void

client端启用或者禁用接收server端特征值内容变更指示的能力。使用Callback异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且需包含指定的入参特征值UUID。
* server端对应的特征值需包含标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），server端才能支持发送变更指示。
* 若启用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，启用server端的指示能力。
* 若禁用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，禁用server端的指示能力。
* 通过[on('BLECharacteristicChange')](js-apis-bluetooth-ble.md#onblecharacteristicchange)接收server端特征值内容变更指示。
* 若client端收到server端特征值内容变更指示后，系统蓝牙服务会主动回复确认，应用无需关注。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要管理的server端特征值。 |
| enable | boolean | 是 | 是否启用接收server端特征值指示的能力。  true表示启用，false表示禁用。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当调用成功，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // 创建descriptors。
3. let descriptors: Array<ble.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(2);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
7. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;
11. let arrayBufferC = new ArrayBuffer(8);
12. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
13. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
14. try {
15. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
16. device.setCharacteristicChangeIndication(characteristic, false, (err: BusinessError) => {
17. if (err) {
18. console.error('notifyCharacteristicChanged callback failed');
19. } else {
20. console.info('notifyCharacteristicChanged callback successful');
21. }
22. });
23. } catch (err) {
24. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
25. }
```

### setCharacteristicChangeIndication

PhonePC/2in1TabletTVWearable

setCharacteristicChangeIndication(characteristic: BLECharacteristic, enable: boolean): Promise<void>

client端启用或者禁用接收server端特征值内容变更指示的能力。使用Promise异步回调。

* 需要先调用[getServices](js-apis-bluetooth-ble.md#getservices)，获取到server端所有支持的能力，且需包含指定的入参特征值UUID。
* server端对应的特征值需包含标准协议定义的Client Characteristic Configuration描述符UUID（00002902-0000-1000-8000-00805f9b34fb），server端才能支持发送变更指示。
* 若启用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，启用server端的指示能力。
* 若禁用该能力，系统蓝牙服务会自动往server端写Client Characteristic Configuration描述符，禁用server端的指示能力。
* 通过[on('BLECharacteristicChange')](js-apis-bluetooth-ble.md#onblecharacteristicchange)接收server端特征值内容变更指示。
* 若client端收到server端特征值内容变更指示后，系统蓝牙服务会主动回复确认，应用无需关注。
* 异步回调结果返回后，才能调用下一次读取或者写入操作，如[readCharacteristicValue](js-apis-bluetooth-ble.md#readcharacteristicvalue)、[readDescriptorValue](js-apis-bluetooth-ble.md#readdescriptorvalue)、[writeCharacteristicValue](js-apis-bluetooth-ble.md#writecharacteristicvalue)、[writeDescriptorValue](js-apis-bluetooth-ble.md#writedescriptorvalue)、[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)和[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| characteristic | [BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic) | 是 | 需要管理的server端特征值。 |
| enable | boolean | 是 | 是否启用接收server端特征值指示的能力。  true表示启用，false表示禁用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900011 | The operation is busy. The last operation is not complete. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. // 创建descriptors。
3. let descriptors: Array<ble.BLEDescriptor> = [];
4. let arrayBuffer = new ArrayBuffer(2);
5. let descV = new Uint8Array(arrayBuffer);
6. descV[0] = 0; // 以Client Characteristic Configuration描述符为例，表示bit0、bit1均为0，notification和indication均不开启
7. let descriptor: ble.BLEDescriptor = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
8. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB',
9. descriptorUuid: '00002902-0000-1000-8000-00805F9B34FB', descriptorValue: arrayBuffer};
10. descriptors[0] = descriptor;
11. let arrayBufferC = new ArrayBuffer(8);
12. let characteristic: ble.BLECharacteristic = {serviceUuid: '00001810-0000-1000-8000-00805F9B34FB',
13. characteristicUuid: '00001820-0000-1000-8000-00805F9B34FB', characteristicValue: arrayBufferC, descriptors:descriptors};
14. try {
15. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
16. device.setCharacteristicChangeIndication(characteristic, false);
17. } catch (err) {
18. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
19. }
```

### on('BLECharacteristicChange')

PhonePC/2in1TabletTVWearable

on(type: 'BLECharacteristicChange', callback: Callback<BLECharacteristic>): void

client端订阅server端特征值变化事件。使用Callback异步回调。

* 需调用[setCharacteristicChangeNotification](js-apis-bluetooth-ble.md#setcharacteristicchangenotification)或者[setCharacteristicChangeIndication](js-apis-bluetooth-ble.md#setcharacteristicchangeindication)，且启用通知或者指示能力后，才能接收到server端的特征值内容变更通知或者指示。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLECharacteristicChange'，表示server端特征值变化事件。  当client端收到server端特征值内容变更的通知或者指示时，触发该事件。 |
| callback | Callback<[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)> | 是 | 指定订阅的回调函数，会携带server端变化后的特征值内容。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function CharacteristicChange(characteristicChangeReq: ble.BLECharacteristic) {
3. let serviceUuid: string = characteristicChangeReq.serviceUuid;
4. let characteristicUuid: string = characteristicChangeReq.characteristicUuid;
5. let value: Uint8Array = new Uint8Array(characteristicChangeReq.characteristicValue);
6. }
7. try {
8. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
9. device.on('BLECharacteristicChange', CharacteristicChange);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

### off('BLECharacteristicChange')

PhonePC/2in1TabletTVWearable

off(type: 'BLECharacteristicChange', callback?: Callback<BLECharacteristic>): void

client端取消订阅server端特征值变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLECharacteristicChange'，表示server端特征值变化事件。 |
| callback | Callback<[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('BLECharacteristicChange')](js-apis-bluetooth-ble.md#onblecharacteristicchange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.off('BLECharacteristicChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### on('BLEConnectionStateChange')

PhonePC/2in1TabletTVWearable

on(type: 'BLEConnectionStateChange', callback: Callback<BLEConnectionChangeState>): void

client端订阅GATT profile协议的连接状态变化事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEConnectionStateChange'，表示连接状态变化事件。  client和server端之间的连接状态发生变化时，触发该事件。  当client端调用[connect](js-apis-bluetooth-ble.md#connect)或[disconnect](js-apis-bluetooth-ble.md#disconnect)时，可能引起连接状态生变化。 |
| callback | Callback<[BLEConnectionChangeState](js-apis-bluetooth-ble.md#bleconnectionchangestate)> | 是 | 指定订阅的回调函数，会携带连接状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. function ConnectStateChanged(state: ble.BLEConnectionChangeState) {
3. console.info('bluetooth connect state changed');
4. let connectState: ble.ProfileConnectionState = state.state;
5. }
6. try {
7. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
8. device.on('BLEConnectionStateChange', ConnectStateChanged);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### off('BLEConnectionStateChange')

PhonePC/2in1TabletTVWearable

off(type: 'BLEConnectionStateChange', callback?: Callback<BLEConnectionChangeState>): void

client端取消订阅GATT profile协议的连接状态变化事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEConnectionStateChange'，表示连接状态变化事件。 |
| callback | Callback<[BLEConnectionChangeState](js-apis-bluetooth-ble.md#bleconnectionchangestate)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('BLEConnectionStateChange')](js-apis-bluetooth-ble.md#onbleconnectionstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.off('BLEConnectionStateChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### on('BLEMtuChange')

PhonePC/2in1TabletTVWearable

on(type: 'BLEMtuChange', callback: Callback<number>): void

client端订阅MTU（最大传输单元）大小变更事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEMtuChange'，表示MTU大小变更事件。  当调用[setBLEMtuSize](js-apis-bluetooth-ble.md#setblemtusize)方法，client端发起MTU大小协商后，会触发该事件。 |
| callback | Callback<number> | 是 | 指定订阅的回调函数，会携带协商后的MTU大小。单位：Byte。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. gattClient.on('BLEMtuChange', (mtu: number) => {
5. console.info('BLEMtuChange, mtu: ' + mtu);
6. });
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

### off('BLEMtuChange')

PhonePC/2in1TabletTVWearable

off(type: 'BLEMtuChange', callback?: Callback<number>): void

client端取消订阅MTU（最大传输单元）大小变更事件。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEMtuChange'，表示MTU大小变更事件。 |
| callback | Callback<number> | 否 | 指定取消订阅的回调函数通知。若传参，则需与[on('BLEMtuChange')](js-apis-bluetooth-ble.md#onblemtuchange-1)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. try {
3. let device: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
4. device.off('BLEMtuChange');
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### on('serviceChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'serviceChange', callback: Callback<void>): void

client端设备订阅server端设备服务变化的通知事件，使用Callback异步回调。

* 如client端已订阅该事件，当server端添加或删除服务时，client端均会收到服务变化通知。
* client端收到服务变化通知时，建议重新调用[getServices](js-apis-bluetooth-ble.md#getservices)获取server端设备支持的最新服务能力。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'serviceChange'，表示服务变化通知事件。  当server端添加或删除服务时，会触发该事件通知client端。 |
| callback | Callback<void> | 是 | 通知client端设备，server端服务已发生变更。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function ServiceChangedEvent() : void {
3. console.info("service has changed.");
4. }

6. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
7. // 需预先调用connect接口先连上server端设备
8. try {
9. gattClient.on('serviceChange', ServiceChangedEvent);
10. } catch (err) {
11. console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
12. }
```

### off('serviceChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'serviceChange', callback?: Callback<void>): void

client端设备取消订阅server端设备服务变化的通知事件。

* 取消订阅后，server端设备服务变化，client端将不再收到事件通知。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'serviceChange'，表示服务变化通知事件。  当server端添加或删除服务时，会触发该事件通知client端。 |
| callback | Callback<void> | 否 | 指定取消订阅服务变化的回调函数通知。若传参，则需与[on('serviceChange')](js-apis-bluetooth-ble.md#onservicechange22)中传入的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. function ServiceChangedEvent() : void {
3. console.info("service has changed.");
4. }

6. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
7. // 需预先调用connect接口先连上server端设备
8. try {
9. gattClient.off('serviceChange', ServiceChangedEvent);
10. } catch (err) {
11. console.error(`errCode: ${(err as BusinessError).code}, errMessage: ${(err as BusinessError).message}`);
12. }
```

### getConnectedState22+

PhonePC/2in1TabletTVWearable

getConnectedState(): ProfileConnectionState

获取当前与server端设备的连接状态。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ProfileConnectionState](js-apis-bluetooth-ble.md#profileconnectionstate) | 蓝牙设备的profile连接状态。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

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
2. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
3. try {
4. let result: ble.ProfileConnectionState = gattClient.getConnectedState();
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### updateConnectionParam22+

PhonePC/2in1TabletTVWearable

updateConnectionParam(param: ConnectionParam): Promise<void>

向对端设备发起连接参数更新请求，调用成功后可以切换与对端数据传输速度。使用Promise异步回调。

* 需先调用[connect](js-apis-bluetooth-ble.md#connect)方法，等GATT profile连接成功后才能使用。
* 不调用该接口时，默认连接参数类型为[ble.ConnectionParam.BALANCED](js-apis-bluetooth-ble.md#connectionparam22)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [ConnectionParam](js-apis-bluetooth-ble.md#connectionparam22) | 是 | 连接参数类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
3. try {
4. gattClient.updateConnectionParam(ble.ConnectionParam.LOW_POWER);
5. } catch (err) {
6. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
7. }
```

### readPhy23+

PhonePC/2in1TabletTVWearable

readPhy(): Promise<PhyValue>

获取client端连接链路的物理通道类型。使用Promise异步回调。

* 需先调用[connect](js-apis-bluetooth-ble.md#connect)方法发起连接，并等待连接成功后，再调用该方法。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[PhyValue](js-apis-bluetooth-ble.md#phyvalue23)> | Promise对象，返回client端连接链路的物理通道类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
2. try {
3. gattClient.readPhy().then((phyValue:ble.PhyValue) => {
4. console.info(`txPhy: ${phyValue.txPhy}, rxPhy: ${phyValue.rxPhy}`);
5. });
6. } catch (err) {
7. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
8. }
```

### setPhy23+

PhonePC/2in1TabletTVWearable

setPhy(phyValue: PhyValue): Promise<void>

client端设置连接链路的物理通道类型。使用Promise异步回调。

* 需先调用[connect](js-apis-bluetooth-ble.md#connect)方法发起连接，并等待连接成功后，再调用该方法。
* 本端client调用setPhy设置物理通道类型后，底层会根据对端设备能力，协商出本端和对端设备均支持的物理通道类型作为最终结果。例如本端支持并设置[BLE\_PHY\_2M](js-apis-bluetooth-ble.md#blephy23)，但对端设备仅支持[BLE\_PHY\_1M](js-apis-bluetooth-ble.md#blephy23)，则最终设置的结果仍为[BLE\_PHY\_1M](js-apis-bluetooth-ble.md#blephy23)。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| phyValue | [PhyValue](js-apis-bluetooth-ble.md#phyvalue23) | 是 | 连接链路的物理通道类型配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |
| 2901003 | The connection is not established. |

**示例：**

```
1. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
2. try {
3. let phyValue: ble.PhyValue = {
4. txPhy: ble.BlePhy.BLE_PHY_1M,
5. rxPhy: ble.BlePhy.BLE_PHY_1M
6. }
7. gattClient.setPhy(phyValue);
8. } catch (err) {
9. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
10. }
```

### onBlePhyUpdate23+

PhonePC/2in1TabletTVWearable

onBlePhyUpdate(callback: Callback<PhyValue>): void

订阅物理通道类型变更事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PhyValue](js-apis-bluetooth-ble.md#phyvalue23)> | 是 | 指定订阅的回调函数，会携带变更后最新的物理通道类型。  当本端client调用[setPhy](js-apis-bluetooth-ble.md#setphy23-1)或对端变更当前物理通道类型后，如订阅此事件，均会收到携带最新物理通道类型的回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function BlePhyCallback(data:ble.PhyValue) {
2. console.info(`txPhy: ${data.txPhy}, rxPhy: ${data.rxPhy}`);
3. }
4. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
5. try {
6. gattClient.onBlePhyUpdate(BlePhyCallback);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

### offBlePhyUpdate23+

PhonePC/2in1TabletTVWearable

offBlePhyUpdate(callback?: Callback<PhyValue>): void

取消订阅物理通道类型变更事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[PhyValue](js-apis-bluetooth-ble.md#phyvalue23)> | 否 | 指定取消订阅的回调函数。若传参，则需与[onBlePhyUpdate](js-apis-bluetooth-ble.md#onblephyupdate23-1)中的回调函数一致。  若无传参，则取消订阅所有物理通道类型变更的回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |

**示例：**

```
1. function BlePhyCallback(data:ble.PhyValue) {
2. console.info(`txPhy: ${data.txPhy}, rxPhy: ${data.rxPhy}`);
3. }
4. let gattClient: ble.GattClientDevice = ble.createGattClientDevice('XX:XX:XX:XX:XX:XX');
5. try {
6. gattClient.offBlePhyUpdate(BlePhyCallback);
7. } catch (err) {
8. console.error(`errCode: ${err.code}, errMessage: ${err.message}`);
9. }
```

## ble.createBleScanner15+

PhonePC/2in1TabletTVWearable

createBleScanner(): BleScanner

创建一个[BleScanner](js-apis-bluetooth-ble.md#blescanner15)实例对象，可用于发起或停止BLE扫描等流程。

**元服务API**: 从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BleScanner](js-apis-bluetooth-ble.md#blescanner15) | 返回一个BleScanner的实例。 |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. import { ble } from '@kit.ConnectivityKit';
3. let bleScanner: ble.BleScanner = ble.createBleScanner();
4. console.info('create bleScanner success');
```

## BleScanner15+

PhonePC/2in1TabletTVWearable

BLE扫描类，提供了扫描相关的操作方法。

* 使用该类的方法前，需通过[createBleScanner](js-apis-bluetooth-ble.md#blecreateblescanner15)方法构造该类的实例。
* 通过创建不同的该类实例，可以管理多路不同的扫描流程。

### startScan15+

PhonePC/2in1TabletTVWearable

startScan(filters: Array<ScanFilter>, options?: ScanOptions): Promise<void>

发起BLE扫描流程。使用Promise异步回调。

* 该接口只能扫描BLE设备。
* 扫描结果会通过[on('BLEDeviceFind')](js-apis-bluetooth-ble.md#onbledevicefind15)的回调函数获取到。
* 调用[stopScan](js-apis-bluetooth-ble.md#stopscan15)可以停止该方法开启的扫描流程。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filters | Array<[ScanFilter](js-apis-bluetooth-ble.md#scanfilter)> | 是 | 扫描BLE广播的过滤条件集合，符合过滤条件的设备会被上报。  - 若该参数设置为null，将扫描所有可发现的周边BLE设备，但是不建议使用此方式，可能扫描到非预期设备，并增加功耗。  - 围栏模式下（[ScanReportMode](js-apis-bluetooth-ble.md#scanreportmode15)设置为FENCE\_SENSITIVITY\_LOW或FENCE\_SENSITIVITY\_HIGH时），该参数不可设置为null，需传入非空过滤器。  - 过滤器资源为所有应用共享，建议单个应用使用过滤器数量不超过3个，否则过滤器资源占满将导致开启扫描失败，返回2900009错误码。 |
| options | [ScanOptions](js-apis-bluetooth-ble.md#scanoptions) | 否 | 扫描的配置参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900009 | Fails to start scan as it is out of hardware resources. |
| 2900099 | Operation failed. |
| 2902050 | Failed to start scan as Ble scan is already started by the app. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. import { ble } from '@kit.ConnectivityKit';
3. let bleScanner: ble.BleScanner = ble.createBleScanner();
4. function onReceiveEvent(scanReport: ble.ScanReport) {
5. console.info('BLE scan device find result = '+ JSON.stringify(scanReport));
6. }
7. try {
8. bleScanner.on("BLEDeviceFind", onReceiveEvent);
9. let scanFilter: ble.ScanFilter = {
10. deviceId:"XX:XX:XX:XX:XX:XX",
11. name:"test",
12. serviceUuid:"00001888-0000-1000-8000-00805f9b34fb"
13. };
14. let scanOptions: ble.ScanOptions = {
15. interval: 500,
16. dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
17. matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE,
18. reportMode: ble.ScanReportMode.FENCE_SENSITIVITY_LOW
19. }
20. bleScanner.startScan([scanFilter],scanOptions);
21. console.info('startScan success');
22. } catch (err) {
23. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
24. }
```

### stopScan15+

PhonePC/2in1TabletTVWearable

stopScan(): Promise<void>

停止正在进行的BLE扫描。使用Promise异步回调。

* 停止的扫描是由[startScan](js-apis-bluetooth-ble.md#startscan15)触发的。
* 当应用不再需要扫描BLE设备时，需主动调用该方法停止扫描。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

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
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. import { ble } from '@kit.ConnectivityKit';
3. let bleScanner: ble.BleScanner = ble.createBleScanner();
4. try {
5. bleScanner.stopScan();
6. console.info('stopScan success');
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

### on('BLEDeviceFind')15+

PhonePC/2in1TabletTVWearable

on(type: 'BLEDeviceFind', callback: Callback<ScanReport>): void

订阅BLE设备扫描结果上报事件。使用Callback异步回调。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEDeviceFind'，表示BLE设备扫描结果上报事件。  当调用[startScan](js-apis-bluetooth-ble.md#startscan15) 后，开始BLE扫描，若扫描到BLE设备，触发该事件。 |
| callback | Callback<[ScanReport](js-apis-bluetooth-ble.md#scanreport15)> | 是 | 指定订阅的回调函数，会携带扫描结果的集合。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. import { ble } from '@kit.ConnectivityKit';
3. function onReceiveEvent(scanReport: ble.ScanReport) {
4. console.info('bluetooth device find = '+ JSON.stringify(scanReport));
5. }
6. let bleScanner: ble.BleScanner = ble.createBleScanner();
7. try {
8. bleScanner.on('BLEDeviceFind', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### off('BLEDeviceFind')15+

PhonePC/2in1TabletTVWearable

off(type: 'BLEDeviceFind', callback?: Callback<ScanReport>): void

取消订阅BLE设备扫描结果上报事件。

* 若不再需要扫描BLE设备，调用[stopScan](js-apis-bluetooth-ble.md#stopscan15)方法后，需要调用此方法取消订阅。

**需要权限**：ohos.permission.ACCESS\_BLUETOOTH

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 事件回调类型，支持的事件为'BLEDeviceFind'，表示BLE设备扫描结果上报事件。 |
| callback | Callback<[ScanReport](js-apis-bluetooth-ble.md#scanreport15)> | 否 | 指定取消订阅的回调函数通知。  若传参，则需与[on('BLEDeviceFind')](js-apis-bluetooth-ble.md#onbledevicefind15)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[蓝牙服务子系统错误码](errorcode-bluetoothmanager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 2900099 | Operation failed. |

**示例：**

```
1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
2. import { ble } from '@kit.ConnectivityKit';
3. function onReceiveEvent(scanReport: ble.ScanReport) {
4. console.info('bluetooth device find = '+ JSON.stringify(scanReport));
5. }
6. let bleScanner: ble.BleScanner = ble.createBleScanner();
7. try {
8. bleScanner.on('BLEDeviceFind', onReceiveEvent);
9. bleScanner.off('BLEDeviceFind', onReceiveEvent);
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## GattService

PhonePC/2in1TabletTVWearable

GATT服务结构定义，可包含多个特征值[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)和依赖的其他服务。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 服务UUID，标识一个GATT服务。例如：00001888-0000-1000-8000-00805f9b34fb。 |
| isPrimary | boolean | 否 | 否 | 是否是主服务。true表示是主服务，false表示是次要服务。 |
| characteristics | Array<[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)> | 否 | 否 | 当前服务包含的特征值列表。 |
| includeServices | Array<[GattService](js-apis-bluetooth-ble.md#gattservice)> | 否 | 是 | 当前服务依赖的其它服务。 |

## BLECharacteristic

PhonePC/2in1TabletTVWearable

GATT特征值结构定义，是服务[GattService](js-apis-bluetooth-ble.md#gattservice)的核心数据单元。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| characteristicUuid | string | 否 | 否 | 特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征值的数据内容。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| descriptors | Array<[BLEDescriptor](js-apis-bluetooth-ble.md#bledescriptor)> | 否 | 否 | 特征值包含的描述符列表。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| properties | [GattProperties](js-apis-bluetooth-ble.md#gattproperties) | 否 | 是 | 特征值支持的属性。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| characteristicValueHandle18+ | number | 否 | 是 | 特征值的唯一标识句柄。当server端BLE蓝牙设备提供了多个相同UUID特征值时，可以通过此句柄区分不同的特征值。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| permissions20+ | [GattPermissions](js-apis-bluetooth-ble.md#gattpermissions20) | 否 | 是 | 特征值读写操作需要的权限。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## BLEDescriptor

PhonePC/2in1TabletTVWearable

GATT描述符结构定义，是特征值[BLECharacteristic](js-apis-bluetooth-ble.md#blecharacteristic)的数据单元，用于描述特征值的附加信息和属性。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| characteristicUuid | string | 否 | 否 | 描述符所属的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| descriptorUuid | string | 否 | 否 | 描述符UUID。例如：00002902-0000-1000-8000-00805f9b34fb。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| descriptorValue | ArrayBuffer | 否 | 否 | 描述符的数据内容。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| descriptorHandle18+ | number | 否 | 是 | 描述符的唯一标识句柄。当server端BLE蓝牙设备提供了多个相同UUID描述符时，可以通过此句柄区分不同的描述符。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| permissions20+ | [GattPermissions](js-apis-bluetooth-ble.md#gattpermissions20) | 否 | 是 | 描述符读写操作需要的权限。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## NotifyCharacteristic

PhonePC/2in1TabletTVWearable

描述server端特征值发生变化时，server端发送特征值通知的参数结构。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 内容发生变化的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| characteristicValue | ArrayBuffer | 否 | 否 | 特征值对应的数据内容。 |
| confirm | boolean | 否 | 否 | true表示发送的是指示，需要client端回复确认。false表示发送的是通知，不需要client端回复确认。 |

## CharacteristicReadRequest

PhonePC/2in1TabletTVWearable

描述server端订阅client端读特征值请求事件后，接收到的事件参数结构。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | client端读请求的标识符，server端回复时需填写相同的transId。 |
| offset | number | 否 | 否 | client端读数据的偏移值。例如：k表示从第k个字节开始读。  server端回复响应时需填写相同的offset。 |
| characteristicUuid | string | 否 | 否 | client端需要读取的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。 |

## CharacteristicWriteRequest

PhonePC/2in1TabletTVWearable

描述server端订阅client端写特征值请求事件后，接收到的事件参数结构。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | client端写请求的标识符，server端回复时需填写相同的transId。 |
| offset | number | 否 | 否 | client端写数据的偏移值。例如：k表示从第k个字节开始写。  server端回复时需填写相同的offset。 |
| isPrepared | boolean | 否 | 否 | 收到client端写请求后，是否立即回复。  true表示稍后回复，false表示立即回复。 |
| needRsp | boolean | 否 | 否 | 是否需要回复client端。  true表示需要回复，false表示不需要回复。 |
| value | ArrayBuffer | 否 | 否 | client端需要给特征值写入的数据。 |
| characteristicUuid | string | 否 | 否 | client端需要写入的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。 |

## DescriptorReadRequest

PhonePC/2in1TabletTVWearable

描述server端订阅client端读描述符请求事件后，接收到的事件参数结构。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | client端读请求的标识符，server端回复时需填写相同的transId。 |
| offset | number | 否 | 否 | client端读数据的偏移值。例如：k表示从第k个字节开始读。  server端回复响应时需填写相同的offset。 |
| descriptorUuid | string | 否 | 否 | client端需要读取的描述符UUID。例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 描述符所属的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。 |

## DescriptorWriteRequest

PhonePC/2in1TabletTVWearable

描述server端订阅client端写描述符请求事件后，接收到的事件参数结构。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | client端写请求的标识符，server端回复时需填写相同的transId。 |
| offset | number | 否 | 否 | client端写数据的偏移值。例如：k表示从第k个字节开始写。  server端回复时需填写相同的offset。 |
| isPrepared | boolean | 否 | 否 | 收到client端写请求后，是否立即回复。  true表示稍后回复，false表示立即回复。 |
| needRsp | boolean | 否 | 否 | 是否需要回复client端。  true表示需要回复，false表示不需要回复。 |
| value | ArrayBuffer | 否 | 否 | client端需要给描述符写入的数据。 |
| descriptorUuid | string | 否 | 否 | client端需要写入的描述符UUID。例如：00002902-0000-1000-8000-00805f9b34fb。 |
| characteristicUuid | string | 否 | 否 | 描述符所属的特征值UUID。例如：00002a11-0000-1000-8000-00805f9b34fb。 |
| serviceUuid | string | 否 | 否 | 特征值所属的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。 |

## ServerResponse

PhonePC/2in1TabletTVWearable

描述server端回复client端读或者写请求的响应参数结构。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | client端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。 |
| transId | number | 否 | 否 | 收到client端请求的标识符，与订阅client端读或者写请求事件携带的transId保持一致。 |
| status | number | 否 | 否 | 响应的状态，设置为0即可，表示正常。 |
| offset | number | 否 | 否 | client端读或者写请求的数据偏移值，与订阅client端读或者写请求事件携带的offset保持一致。 |
| value | ArrayBuffer | 否 | 否 | 回复的数据。 |

## BLEConnectionChangeState

PhonePC/2in1TabletTVWearable

描述GATT profile协议连接状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 对端蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| state | [ProfileConnectionState](js-apis-bluetooth-constant.md#profileconnectionstate) | 否 | 否 | GATT profile连接状态。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| reason20+ | [GattDisconnectReason](js-apis-bluetooth-ble.md#gattdisconnectreason20) | 否 | 是 | GATT链路断连原因，仅在连接状态为 [STATE\_DISCONNECTED](js-apis-bluetooth-constant.md#profileconnectionstate) 时提供，其他连接状态下断连原因默认为undefined。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## ScanResult

PhonePC/2in1TabletTVWearable

扫描到符合过滤条件的广播报文后，上报的扫描数据。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 否 | 扫描到的蓝牙设备地址。例如："XX:XX:XX:XX:XX:XX"。  基于信息安全考虑，若应用开启扫描时没有在[ScanFilter](js-apis-bluetooth-ble.md#scanfilter)中配置[实际MAC地址类型](js-apis-bluetooth-common.md#bluetoothaddresstype)的地址，则此处获取的设备地址为[虚拟MAC地址](js-apis-bluetooth-common.md#bluetoothaddresstype)。  - 若和该设备地址配对成功后，该地址不会变更。  - 若该设备重启蓝牙开关，重新获取到的虚拟地址会立即变更。  - 若取消配对，蓝牙子系统会根据该地址的实际使用情况，决策后续变更时机；若其他应用正在使用该地址，则不会立刻变更。  - 若要持久化保存该地址，可使用[access.addPersistentDeviceId](js-apis-bluetooth-access.md#accessaddpersistentdeviceid16)方法。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| address23+ | [BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 否 | 是 | 扫描到的蓝牙设备地址信息，包括地址与地址类型。 |
| rssi | number | 否 | 否 | 扫描到的设备信号强度，单位：dBm。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| data | ArrayBuffer | 否 | 否 | 扫描到的设备发送的原始未解析的广播报文内容。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| deviceName | string | 否 | 否 | 扫描到的设备名称，从原始数据data字段中解析而来，在蓝牙协议中广播数据类型为0x09。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| connectable | boolean | 否 | 否 | 扫描到的设备是否可连接。true表示可连接，false表示不可连接。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| advertiseFlags22+ | number | 否 | 是 | 扫描到的设备广播标记位，从原始数据data字段中解析而来，在蓝牙协议中广播数据类型为0x01。若广播报文中携带标记位，则该字段有值，否则内容为undefined。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| manufacturerDataMap22+ | Map<number, Uint8Array> | 否 | 是 | 扫描到的设备制造商数据集合，从原始数据data字段中解析而来，在蓝牙协议中广播数据类型为0xFF。若广播报文中携带设备制造商数据，则该字段有值，否则内容为undefined。  - Map的key表示制造商ID，value表示对应制造商数据的具体内容。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| serviceDataMap22+ | Map<string, Uint8Array> | 否 | 是 | 扫描到的设备服务数据集合，从原始数据data字段中解析而来，在蓝牙协议中广播数据类型为0x16。若广播报文中携带设备服务数据，则该字段有值，否则内容为undefined。  - Map的key表示服务UUID，value表示对应UUID服务的具体内容。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| serviceUuids22+ | string[] | 否 | 是 | 扫描到的设备服务UUID集合，从原始数据data字段中解析而来，在蓝牙协议中，16-bit UUID的广播数据类型为0x03，32-bit UUID类型为0x05，128-bit UUID类型为0x07。若广播报文中携带设备服务UUID，则该字段有值，否则内容为undefined。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| txPowerLevel22+ | number | 否 | 是 | 扫描到的设备广播发送功率，从原始数据data字段中解析而来，在蓝牙协议中广播数据类型为0x0A。若广播报文中携带设备广播发送功率，则该字段有值，否则内容为undefined。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |
| advertisingDataMap22+ | Map<number, Uint8Array> | 否 | 是 | 扫描到的设备广播数据集，从原始数据data字段中解析而来。  - Map的key表示广播数据类型，value表示对应数据类型的具体内容，如advertisingDataMap字段中key为0x0A的对应value含义为txPowerLevel值。  - 若广播报文中携带任意广播数据内容，则该字段有值，否则内容为undefined。  **元服务API**：从API version 22开始，该接口支持在元服务中使用。 |

## AdvertiseSetting

PhonePC/2in1TabletTVWearable

描述BLE广播的发送参数。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 广播发送间隔。  取值范围：[32, 16777215]，单位：slot（时间槽），一个slot代表0.625毫秒，默认值为1600。  其中传统广播的最大值是16384。 |
| txPower | number | 否 | 是 | 广播发送功率。取值范围：[-127, 1]，单位：dBm，默认值为-7。  考虑到发送广播的性能和功耗，建议高档取值为1，中档取为-7，低档取值为-15。 |
| connectable | boolean | 否 | 是 | 是否是可连接广播。true表示发送可连接广播，false表示发送不可连接广播，默认值为true。 |

## AdvertiseData

PhonePC/2in1TabletTVWearable

描述BLE广播报文数据内容，也可以用作回复扫描请求的广播报文数据内容。当前只支持传统广播，因此报文最大长度为31个字节。若超出最大长度（31个字节）限制，会导致启动广播失败。

* 若携带了所有参数，尤其是携带了广播名称（通过includeDeviceName或advertiseName进行设置），需要注意广播报文长度。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuids | Array<string> | 否 | 否 | 要携带的服务UUID。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| manufactureData | Array<[ManufactureData](js-apis-bluetooth-ble.md#manufacturedata)> | 否 | 否 | 要携带的制造商数据内容。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceData | Array<[ServiceData](js-apis-bluetooth-ble.md#servicedata)> | 否 | 否 | 要携带的服务数据内容。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| includeDeviceName | boolean | 否 | 是 | 是否携带本机的设备名称作为广播名称。  true表示携带，false表示不携带，默认值为false。  若应用需要自定义广播名称，可通过advertiseName进行设置。本参数不可与advertiseName同时使用。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| includeTxPower18+ | boolean | 否 | 是 | 是否携带广播发送功率。  true表示携带广播发送功率，false表示不携带广播发送功率，默认值为false。  携带该值后，广播报文长度将多占用3个字节。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| advertiseName23+ | string | 否 | 是 | 要携带的自定义广播名称。  不可与includeDeviceName同时使用。  **需要权限**：[ohos.permission.MANAGE\_BLUETOOTH\_ADVERTISER\_NAME](../harmonyos-guides/restricted-permissions.md#ohospermissionmanage_bluetooth_advertiser_name)  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |

## AdvertisingParams11+

PhonePC/2in1TabletTVWearable

首次启动BLE广播时设置的参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingSettings11+ | [AdvertiseSetting](js-apis-bluetooth-ble.md#advertisesetting) | 否 | 否 | 广播的发送参数。 |
| advertisingData11+ | [AdvertiseData](js-apis-bluetooth-ble.md#advertisedata) | 否 | 否 | 需要发送的广播报文数据内容。 |
| advertisingResponse11+ | [AdvertiseData](js-apis-bluetooth-ble.md#advertisedata) | 否 | 是 | 回复扫描请求的广播报文数据内容。 |
| duration11+ | number | 否 | 是 | 发送广播的持续时间。取值范围：[1, 65535]，单位：10ms。  如果未指定此参数或者将其设置为0，则会持续发送广播。 |

## AdvertisingEnableParams11+

PhonePC/2in1TabletTVWearable

启动指定标识的BLE广播时设置的参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingId | number | 否 | 否 | 需要启动的广播标识。 |
| duration | number | 否 | 是 | 发送广播的持续时间。取值范围：[1, 65535]，单位：10ms。  如果未指定此参数或者将其设置为0，则会持续发送广播。 |

## AdvertisingDisableParams11+

PhonePC/2in1TabletTVWearable

停止指定标识的BLE广播时设置的参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingId | number | 否 | 否 | 需要停止的广播标识。 |

## AdvertisingStateChangeInfo11+

PhonePC/2in1TabletTVWearable

描述BLE广播启动、停止的状态信息。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| advertisingId | number | 否 | 否 | 首次启动广播时会分配该值，后续用于标识当前操作的广播。 |
| state | [AdvertisingState](js-apis-bluetooth-ble.md#advertisingstate11) | 否 | 否 | 操作广播后，收到的BLE广播状态。 |

## ManufactureData

PhonePC/2in1TabletTVWearable

描述BLE广播报文中制造商数据内容。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| manufactureId | number | 否 | 否 | 制造商的标识，由蓝牙技术联盟分配。 |
| manufactureValue | ArrayBuffer | 否 | 否 | 制造商特定的数据。 |

## ServiceData

PhonePC/2in1TabletTVWearable

描述BLE广播报文中的服务数据内容。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| serviceUuid | string | 否 | 否 | 服务UUID。 |
| serviceValue | ArrayBuffer | 否 | 否 | 服务数据。 |

## ScanFilter

PhonePC/2in1TabletTVWearable

扫描BLE广播的过滤条件，只有符合该条件的广播报文才会上报。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| deviceId | string | 否 | 是 | 过滤该BLE设备地址的广播报文。例如："XX:XX:XX:XX:XX:XX"。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| address23+ | [BluetoothAddress](js-apis-bluetooth-common.md#bluetoothaddress) | 否 | 是 | 过滤该BLE设备地址和地址类型的广播报文。  与deviceId相比，本参数支持同时指定BLE设备地址和地址类型来对BLE广播报文进行过滤。  若deviceId与本参数同时指定，本参数生效，deviceId不生效。 |
| name | string | 否 | 是 | 过滤该BLE设备名称的广播报文。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceUuid | string | 否 | 是 | 过滤包含该服务UUID的广播报文，serviceUuid通常在外围设备的广播报文中携带，表示外围设备支持的服务UUID。例如：00001888-0000-1000-8000-00805f9b34fb。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceUuidMask | string | 否 | 是 | 搭配serviceUuid过滤器使用，可设置过滤部分服务UUID。例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceSolicitationUuid | string | 否 | 是 | 过滤包含该服务请求UUID的广播报文，serviceSolicitationUuid通常在中心设备的广播报文中携带，表示中心设备希望搜索到的服务UUID。例如：00001888-0000-1000-8000-00805F9B34FB。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceSolicitationUuidMask | string | 否 | 是 | 搭配serviceSolicitationUuid过滤器使用，可设置过滤部分服务请求UUID。例如：FFFFFFFF-FFFF-FFFF-FFFF-FFFFFFFFFFFF。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceData | ArrayBuffer | 否 | 是 | 过滤包含该服务数据的广播报文。例如：[0x90,0x00,0xF1,0xF2]。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| serviceDataMask | ArrayBuffer | 否 | 是 | 搭配serviceData过滤器使用，可设置过滤部分服务数据。例如：[0xFF,0xFF,0xFF,0xFF]。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| manufactureId | number | 否 | 是 | 过滤包含该制造商标识符的广播报文。例如：0x0006。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| manufactureData | ArrayBuffer | 否 | 是 | 搭配manufactureId过滤器使用，过滤包含该制造商数据的广播报文。例如：[0x1F,0x2F,0x3F]。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| manufactureDataMask | ArrayBuffer | 否 | 是 | 搭配manufactureData过滤器使用，可设置过滤部分制造商数据。例如：[0xFF,0xFF,0xFF]。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| rssiThreshold23+ | number | 否 | 是 | 过滤信号强度大于或等于该信号强度门限值的广播报文，蓝牙协议上规定可设置范围为[-128, 127]，建议设置[-90, 127]范围内的门限值。  **元服务API**：从API version 23开始，该接口支持在元服务中使用。 |

## ScanOptions

PhonePC/2in1TabletTVWearable

BLE扫描的配置参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| interval | number | 否 | 是 | 扫描结果上报的延迟时间，单位：ms，默认值为0。搭配[ScanReportMode](js-apis-bluetooth-ble.md#scanreportmode15)使用。  - 在常规或围栏扫描上报模式下，该值不生效，扫描到符合过滤条件的广播报文后立即上报。  - 在批量扫描上报模式下，该值生效，扫描到符合过滤条件的广播报文后，会存入缓存队列，延迟上报。若不设置该值或设置在[0, 5000)范围内，蓝牙子系统会默认设置延迟时间为5000ms。延迟时间内，若符合过滤条件的广播报文数量超过硬件缓存能力，蓝牙子系统会提前上报扫描结果。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| dutyMode | [ScanDuty](js-apis-bluetooth-ble.md#scanduty) | 否 | 是 | 扫描模式，默认值为SCAN\_MODE\_LOW\_POWER。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| matchMode | [MatchMode](js-apis-bluetooth-ble.md#matchmode) | 否 | 是 | 硬件的过滤匹配模式，默认值为MATCH\_MODE\_AGGRESSIVE。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| phyType12+ | [PhyType](js-apis-bluetooth-ble.md#phytype12) | 否 | 是 | 扫描中使用的物理通道类型，默认值为PHY\_LE\_1M。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| reportMode15+ | [ScanReportMode](js-apis-bluetooth-ble.md#scanreportmode15) | 否 | 是 | 扫描结果数据上报模式，默认值为NORMAL。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。 |

## GattProperties

PhonePC/2in1TabletTVWearable

描述GATT特征值支持的属性。决定了特征值内容和描述符如何被使用和访问。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| write | boolean | 否 | 是 | 该特征值是否支持写入操作。  true表示支持，且被写入时需要回复对端设备，false表示不支持。默认值为true。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| writeNoResponse | boolean | 否 | 是 | 该特征值是否支持写入操作。  true表示支持，且被写入时无需回复对端设备，false表示不支持。默认值为true。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| read | boolean | 否 | 是 | 该特征值是否支持读取操作。  true表示支持，false表示不支持。默认值为true。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| notify | boolean | 否 | 是 | 该特征值是否支持主动向对端设备通知特征值内容。  true表示支持，且对端设备不需要回复确认，false表示不支持。默认值为false。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| indicate | boolean | 否 | 是 | 该特征值是否支持向对端设备指示特征值内容。  true表示支持，对端设备需要回复确认，false表示不支持。默认值为false。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |
| broadcast20+ | boolean | 否 | 是 | 该特征值是否支持作为广播内容由server端发送。  true表示支持，server端可将特征值内容以[ServiceData](js-apis-bluetooth-ble.md#servicedata)类型在广播报文中携带，false表示不支持。默认值为false。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |
| authenticatedSignedWrite20+ | boolean | 否 | 是 | 该特征值是否支持签名写入操作，通过对写入内容进行签名校验替代加密流程。  true表示支持，且该特征值权限[GattPermissions](js-apis-bluetooth-ble.md#gattpermissions20)中的writeSigned或writeSignedMitm需设置为true，否则该属性不生效，false表示不支持。默认值为false。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |
| extendedProperties20+ | boolean | 否 | 是 | 该特征值是否存在扩展属性。  true表示存在扩展属性，false表示不存在。默认值为false。  **元服务API**：从API version 20开始，该接口支持在元服务中使用。 |

## GattPermissions20+

PhonePC/2in1TabletTVWearable

描述读写GATT特征值或描述符需具备的权限。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| read | boolean | 否 | 是 | 是否允许读取该特征值或描述符内容。  true表示允许，false表示不允许。默认值为true。 |
| readEncrypted | boolean | 否 | 是 | 读取该特征值或描述符内容是否需要加密。  true表示需要加密后，方可读取内容，false表示不需要普通方式加密。默认值为false。 |
| readEncryptedMitm | boolean | 否 | 是 | 读取该特征值或描述符内容是否需要防中间人攻击的加密。  防中间人攻击表示操作需要经过认证，防止数据被第三方篡改。true表示需要防中间人攻击的加密后才能读取内容，false表示不需要防中间人攻击的加密。默认值为false。 |
| write | boolean | 否 | 是 | 是否允许写入该特征值或描述符内容。  true表示允许，false表示不允许。默认值为true。 |
| writeEncrypted | boolean | 否 | 是 | 写入该特征值或描述符内容是否需要加密。  true表示需要加密后，方可写入内容，false表示不需要普通方式加密。默认值为false。 |
| writeEncryptedMitm | boolean | 否 | 是 | 写入该特征值或描述符内容是否需要防中间人攻击的加密。  true表示需要防中间人攻击的加密后才能写入内容，false表示不需要防中间人攻击的加密。默认值为false。 |
| writeSigned | boolean | 否 | 是 | 写入该特征值或描述符内容是否需要经过签名处理。  true表示内容需要签名处理后方可写入，false表示不需要签名处理。默认值为false。 |
| writeSignedMitm | boolean | 否 | 是 | 写入该特征值或描述符内容是否需要经过防中间人攻击方式的签名处理。  true表示需要防中间人攻击方式的签名处理后方可写入，false表示不需要以防中间人攻击方式签名处理。默认值为false。 |

## PhyValue23+

PhonePC/2in1TabletTVWearable

连接链路的物理通道类型配置参数。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| txPhy | [BlePhy](js-apis-bluetooth-ble.md#blephy23) | 否 | 否 | 发送端物理通道类型。 |
| rxPhy | [BlePhy](js-apis-bluetooth-ble.md#blephy23) | 否 | 否 | 接受端物理通道类型。 |
| phyMode | [CodedPhyMode](js-apis-bluetooth-ble.md#codedphymode23) | 否 | 是 | 用于指定物理通道类型为[BLE\_PHY\_CODED](js-apis-bluetooth-ble.md#blephy23)的编码方式。  默认值为0，表示不指定明确的编码方式，由蓝牙子系统决定。 |

## GattWriteType

PhonePC/2in1TabletTVWearable

枚举，写入特征值的方式（不同的取值，对端蓝牙设备的表现不一样）。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WRITE | 1 | 写入特征值后，对端蓝牙设备需要回复确认。 |
| WRITE\_NO\_RESPONSE | 2 | 写入特征值后，对端蓝牙设备不需要回复。 |

## ScanDuty

PhonePC/2in1TabletTVWearable

枚举，扫描模式，表示不同的扫描性能和功耗情况。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCAN\_MODE\_LOW\_POWER | 0 | 低功耗模式，扫描性能较低，功耗也较低。 |
| SCAN\_MODE\_BALANCED | 1 | 均衡模式，平衡扫描性能和功耗。 |
| SCAN\_MODE\_LOW\_LATENCY | 2 | 低延迟模式，扫描性能较高，但功耗也较高。 |

## MatchMode

PhonePC/2in1TabletTVWearable

枚举，硬件过滤匹配模式。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MATCH\_MODE\_AGGRESSIVE | 1 | 当广播报文信号强度较低或者短时间内广播报文的发送次数较少时，可以更快地上报。 |
| MATCH\_MODE\_STICKY | 2 | 广播报文信号强度较高或者短时间内广播报文的发送次数较多时，才会上报。 |

## AdvertisingState11+

PhonePC/2in1TabletTVWearable

枚举，不同操作对应的BLE广播状态。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTED11+ | 1 | 调用[startAdvertising](js-apis-bluetooth-ble.md#blestartadvertising11)方法后，广播首次启动成功，且会分配相关资源。 |
| ENABLED11+ | 2 | 调用[enableAdvertising](js-apis-bluetooth-ble.md#bleenableadvertising11)方法后，广播启动成功。 |
| DISABLED11+ | 3 | 调用[disableAdvertising](js-apis-bluetooth-ble.md#bledisableadvertising11)方法后，广播停止成功。 |
| STOPPED11+ | 4 | 调用[stopAdvertising](js-apis-bluetooth-ble.md#blestopadvertising11)方法后，广播停止成功，且会释放首次启动广播时分配的相关资源。 |

## PhyType12+

PhonePC/2in1TabletTVWearable

枚举，指定扫描过程中接收BLE广播报文的物理通道。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHY\_LE\_1M12+ | 1 | 使用1M PHY类型扫描。 |
| PHY\_LE\_ALL\_SUPPORTED12+ | 255 | 使用所有支持的PHY类型扫描。 |

## ScanReport15+

PhonePC/2in1TabletTVWearable

上报的扫描数据。

**元服务API**：从API version 15开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| reportType | [ScanReportType](js-apis-bluetooth-ble.md#scanreporttype15) | 否 | 否 | 扫描结果上报类型。 |
| scanResult | Array<[ScanResult](js-apis-bluetooth-ble.md#scanresult)> | 否 | 否 | 扫描到符合过滤条件的BLE广播报文后，上报的扫描数据。 |

## ScanReportType15+

PhonePC/2in1TabletTVWearable

枚举，扫描结果上报类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ON\_FOUND | 1 | 扫描到符合过滤条件的BLE广播报文时，触发上报，可搭配常规和围栏上报模式使用。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。 |
| ON\_LOST | 2 | 当不再扫描到符合过滤条件的BLE广播报文时，触发上报，只搭配围栏上报模式使用。  **元服务API**：从API version 15开始，该接口支持在元服务中使用 |
| ON\_BATCH19+ | 3 | 扫描到符合过滤条件的BLE广播报文时，以[ScanOptions](js-apis-bluetooth-ble.md#scanoptions)中的interval字段为周期触发上报。  **元服务API**：从API version 19开始，该接口支持在元服务中使用 |

## GattDisconnectReason20+

PhonePC/2in1TabletTVWearable

枚举，指定GATT链路断开的原因。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CONN\_TIMEOUT | 1 | 连接超时。 |
| CONN\_TERMINATE\_PEER\_USER | 2 | 对端设备主动断开连接。 |
| CONN\_TERMINATE\_LOCAL\_HOST | 3 | 本端设备主动断开连接。 |
| CONN\_UNKNOWN | 4 | 未知断连原因。 |

## BleProfile21+

PhonePC/2in1TabletTVWearable

枚举，指定当前设备的Profile协议类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| GATT | 1 | 当前设备在GATT链路中同时作为client端和server端。 |
| GATT\_CLIENT | 2 | 当前设备在GATT链路中作为client端。 |
| GATT\_SERVER | 3 | 当前设备在GATT链路中作为server端。 |

## ScanReportMode15+

PhonePC/2in1TabletTVWearable

枚举，扫描结果上报模式。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 1 | 常规扫描上报模式，扫描到符合过滤条件的BLE广播报文后就会立刻上报。  **元服务API**：从API version 15开始，该接口支持在元服务中使用。 |
| BATCH19+ | 2 | 批量扫描上报模式。  - 该模式可通过降低蓝牙芯片上报扫描结果频率，使系统更长时间地保持在休眠状态，从而降低整机功耗。  - 该模式下，扫描到符合过滤条件的BLE广播报文后不会立刻上报，需要缓存一段时间（[ScanOptions](js-apis-bluetooth-ble.md#scanoptions)中的interval字段）后上报。  **元服务API**：从API version 19开始，该接口支持在元服务中使用。 |
| FENCE\_SENSITIVITY\_LOW18+ | 10 | 低灵敏度围栏上报模式。  - 围栏模式表示只在广播进入或离开围栏时上报。  - 扫描到的广播信号强度高且广播数量多时，可进入低灵敏度围栏。  - 首次扫描到广播即进入围栏，触发一次上报。  - 一段时间内扫描不到广播即离开围栏，触发一次上报。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |
| FENCE\_SENSITIVITY\_HIGH18+ | 11 | 高灵敏度围栏上报模式。  - 围栏模式表示只在广播进入或离开围栏时上报。  - 扫描到的广播信号强度低且广播数量少时，可进入高灵敏度围栏。  - 首次扫描到广播即进入围栏，触发一次上报。  - 一段时间内扫描不到广播即离开围栏，触发一次上报。  **元服务API**：从API version 18开始，该接口支持在元服务中使用。 |

## ConnectionParam22+

PhonePC/2in1TabletTVWearable

枚举，连接参数类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LOW\_POWER | 1 | 低功耗模式，传输数据速度慢，但功耗少。 |
| BALANCED | 2 | 均衡模式，平衡延迟和功耗，如果没有请求连接参数更新，这是默认值。 |
| HIGH | 3 | 高速率模式，传输数据速度快，但功耗多。  - 当需要快速传输大量数据时应采用该连接参数，传输完成后，应请求BALANCED连接参数，以减少功耗。 |

## BlePhy23+

PhonePC/2in1TabletTVWearable

枚举，连接与广播的物理通道类型。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLE\_PHY\_1M | 1 | 1M物理通道类型，理论数据速率为1Mbit/s。 |
| BLE\_PHY\_2M | 2 | 2M物理通道类型，理论数据速率为2Mbit/s。 |
| BLE\_PHY\_CODED | 3 | CODED物理通道类型，适用于低速但覆盖范围广的场景。 |

## CodedPhyMode23+

PhonePC/2in1TabletTVWearable

枚举，BLE\_PHY\_CODED类型下的编码方式。

**系统能力**：SystemCapability.Communication.Bluetooth.Core

**模型约束**：此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLE\_PHY\_CODED\_S2 | 1 | 每发送1位有效数据，会添加1位冗余信息。传输速度较快，抗干扰较强，适合中等距离（10 - 100m），理论数据速率为500Kbit/s。 |
| BLE\_PHY\_CODED\_S8 | 2 | 每发送1位有效数据，会添加7位冗余信息。传输速度较慢，抗干扰更强，适合远距离（100 - 300m），理论数据速率为125Kbit/s。 |
