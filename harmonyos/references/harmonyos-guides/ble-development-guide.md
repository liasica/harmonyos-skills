---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ble-development-guide
title: 查找设备
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 低功耗蓝牙 > 查找设备
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a7ad053ae7c0b6aa2baeb6b559729b8c46eb39e23cce3928d3c9b0f5b2475544
---

## 简介

本指南主要提供了BLE扫描和BLE广播相关操作的开发指导。可以实现发现周边BLE设备和其他设备发现本机设备的场景。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### 导入所需API模块

导入ble和错误码模块。

```
1. import { ble } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### BLE扫描流程

**1. 订阅扫描结果上报事件**

* 推荐使用API version 15开始支持的扫描方式，该方式支持应用发起和管理多路扫描。该方式支持的上报事件请参考[on('BLEDeviceFind')](../harmonyos-references/js-apis-bluetooth-ble.md#onbledevicefind15)。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(scanReport: ble.ScanReport) {
3. console.info('BLE scan device find result: '+ JSON.stringify(scanReport));
4. }

6. // 创建ble扫描实例，可以管理该实例下创建的扫描流程
7. let bleScanner: ble.BleScanner = ble.createBleScanner();

9. try {
10. // 发起订阅
11. bleScanner.on('BLEDeviceFind', onReceiveEvent);
12. } catch (err) {
13. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
14. }
```

* API version 14及以前支持的扫描方式只支持应用发起单路扫描。该方式支持的上报事件请参考[ble.on('BLEDeviceFind')](../harmonyos-references/js-apis-bluetooth-ble.md#bleonbledevicefind)。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(data: Array<ble.ScanResult>) {
3. console.info('BLE scan device find result: '+ JSON.stringify(data));
4. }

6. try {
7. // 发起订阅
8. ble.on('BLEDeviceFind', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

* 如何解析扫描到的广播报文，具体可参考本章节[完整示例](ble-development-guide.md#完整示例)。

**2. 发起扫描**

通过BLE扫描周边其他设备发出的BLE广播，可以发现或者查找到应用需要的目标设备，适用于查找设备场景。

若本机设备扫描到可连接的BLE广播，则可以和该设备进行通用属性协议（Generic Attribute Profile，GATT）的连接和数据传输，此时本机设备角色也被称为GATT客户端。具体操作请参考[连接和传输数据](gatt-development-guide.md)。

* 推荐使用API version 15开始支持的扫描方式，该方式支持应用发起和管理多路扫描。可通过[createBleScanner](../harmonyos-references/js-apis-bluetooth-ble.md#blecreateblescanner15)创建扫描实例[BleScanner](../harmonyos-references/js-apis-bluetooth-ble.md#blescanner15)，并调用[startScan](../harmonyos-references/js-apis-bluetooth-ble.md#startscan15)。

```
1. // 创建ble扫描实例
2. let bleScanner: ble.BleScanner = ble.createBleScanner();

4. // 构造扫描BLE广播的过滤条件，目标BLE广播报文需符合该过滤条件
5. let manufactureId = 4567;
6. let manufactureData: Uint8Array = new Uint8Array([1, 2, 3, 4]);
7. let manufactureDataMask: Uint8Array = new Uint8Array([0xFF, 0xFF, 0xFF, 0xFF]);
8. let scanFilter: ble.ScanFilter = { // 根据业务实际情况定义过滤器
9. manufactureId: manufactureId,
10. manufactureData: manufactureData.buffer,
11. manufactureDataMask: manufactureDataMask.buffer
12. };

14. // 构造扫描配置参数
15. let scanOptions: ble.ScanOptions = {
16. interval: 0,
17. dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
18. matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
19. }

21. try {
22. // 发起扫描
23. bleScanner.startScan([scanFilter], scanOptions);
24. console.info('startBleScan success');
25. } catch (err) {
26. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
27. }
```

* API version 14及以前支持的扫描方式只支持应用发起单路扫描。若要再次发起扫描，必须先停止上一路的扫描流程。详情请见[ble.startBLEScan](../harmonyos-references/js-apis-bluetooth-ble.md#blestartblescan)。

```
1. // 构造扫描BLE广播的过滤条件，目标BLE广播报文需符合该过滤条件
2. let manufactureId = 4567;
3. let manufactureData: Uint8Array = new Uint8Array([1, 2, 3, 4]);
4. let manufactureDataMask: Uint8Array = new Uint8Array([0xFF, 0xFF, 0xFF, 0xFF]);
5. let scanFilter: ble.ScanFilter = { // 根据业务实际情况定义过滤器
6. manufactureId: manufactureId,
7. manufactureData: manufactureData.buffer,
8. manufactureDataMask: manufactureDataMask.buffer
9. };

11. // 构造扫描配置参数
12. let scanOptions: ble.ScanOptions = {
13. interval: 0,
14. dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
15. matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
16. }
17. try {
18. // 发起扫描
19. ble.startBLEScan([scanFilter], scanOptions);
20. console.info('startBleScan success');
21. } catch (err) {
22. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
23. }
```

**3. 停止扫描**

扫描流程会消耗蓝牙硬件资源和影响设备功耗。当应用不再需要该扫描时，需要主动停止。

* 搭配API version 15开始支持的多路扫描方式。详情请见[stopScan](../harmonyos-references/js-apis-bluetooth-ble.md#stopscan15)。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(scanReport: ble.ScanReport) {
3. console.info('BLE scan device find result: '+ JSON.stringify(scanReport));
4. }

6. // 创建ble扫描实例
7. let bleScanner: ble.BleScanner = ble.createBleScanner();

9. try {
10. bleScanner.off('BLEDeviceFind', onReceiveEvent);
11. // 停止扫描
12. bleScanner.stopScan();
13. console.info('stopBleScan success');
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }
```

* 搭配API version 14及以前支持的单路扫描方式。详情请见[ble.stopBLEScan](../harmonyos-references/js-apis-bluetooth-ble.md#blestopblescan)。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(data: Array<ble.ScanResult>) {
3. console.info('BLE scan device find result: '+ JSON.stringify(data));
4. }

6. try {
7. // 取消订阅
8. ble.off('BLEDeviceFind', onReceiveEvent);
9. // 停止扫描
10. ble.stopBLEScan();
11. } catch (err) {
12. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
13. }
```

### BLE广播流程

本机设备发送BLE广播后，可以实现被其他设备发现的功能。

若本机设备发送的是可连接广播，则可以接受其他设备发起的通用属性协议（Generic Attribute Profile，GATT）连接，此时本机设备角色也被称为GATT服务端。具体操作请参考[连接和传输数据](gatt-development-guide.md)。

推荐使用API version 11及以后开始支持的广播操作方式。

**1. 订阅广播状态上报事件**

搭配API version 11开始支持的广播操作方式。

```
1. function onReceiveEvent(data: ble.AdvertisingStateChangeInfo) {
2. console.info('bluetooth advertising state = ' + JSON.stringify(data));
3. }

5. try {
6. ble.on('advertisingStateChange', onReceiveEvent);
7. } catch (err) {
8. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
9. }
```

**2. 启动广播**

* 推荐使用API version 11开始支持的广播操作方式。支持在不释放相关广播资源情况下，多次操作启动或者停止指定标识的广播，且支持设置广播持续发送的时间。

  相关API请参考[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising11)和[ble.enableAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#bleenableadvertising11)。

  首次启动广播接口[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising11)会分配广播相关资源，从API version 15开始，该接口支持应用多次调用，实现启动多路广播的功能，并通过不同的广播标识进行管理。

```
1. // 设置广播发送的参数
2. let setting: ble.AdvertiseSetting = {
3. interval: 160,
4. txPower: 0,
5. connectable: true // 发送支持连接的广播
6. };
7. // 构造广播数据
8. let manufactureValueBuffer = new Uint8Array(4);
9. manufactureValueBuffer[0] = 1;
10. manufactureValueBuffer[1] = 2;
11. manufactureValueBuffer[2] = 3;
12. manufactureValueBuffer[3] = 4;
13. let serviceValueBuffer = new Uint8Array(4);
14. serviceValueBuffer[0] = 5;
15. serviceValueBuffer[1] = 6;
16. serviceValueBuffer[2] = 7;
17. serviceValueBuffer[3] = 8;
18. let manufactureDataUnit: ble.ManufactureData = {
19. manufactureId: 4567,
20. manufactureValue: manufactureValueBuffer.buffer
21. };
22. let serviceDataUnit1: ble.ServiceData = {
23. serviceUuid: "00001999-0000-1000-8000-00805f9b34fb",
24. serviceValue: serviceValueBuffer.buffer
25. };
26. let serviceDataUnit2: ble.ServiceData = {
27. serviceUuid: "19991999-0000-1000-8000-00805f9b34fb",
28. serviceValue: serviceValueBuffer.buffer
29. };
30. let advData: ble.AdvertiseData = {
31. serviceUuids: ["00001888-0000-1000-8000-00805f9b34fb", "18881888-0000-1000-8000-00805f9b34fb"],
32. manufactureData: [manufactureDataUnit],
33. serviceData: [],
34. includeDeviceName: false // 表示是否携带设备名，可选参数。注意：带上设备名时，容易导致广播报文长度超出31个字节，使得广播启动失败
35. };
36. let advResponse: ble.AdvertiseData = {
37. serviceUuids: [],
38. manufactureData: [],
39. serviceData: [serviceDataUnit1, serviceDataUnit2]
40. };
41. // 构造广播启动完整参数AdvertisingParams
42. let advertisingParams: ble.AdvertisingParams = {
43. advertisingSettings: setting,
44. advertisingData: advData, // 注意: 广播报文长度不能超过31个字节
45. advertisingResponse: advResponse, // 注意: 广播报文长度不能超过31个字节
46. duration: 0 // 可选参数，若大于0，则广播发送一段时间后，则会停止，但分配的广播资源还在，可重新启动发送
47. }

49. let advHandle = 0xFF; // 定义广播标识

51. // 首次启动广播，蓝牙子系统会分配相关资源，包括应用获取到的广播的标识ID
52. try {
53. ble.startAdvertising(advertisingParams, (err, outAdvHandle) => {
54. if (err) {
55. return;
56. } else {
57. advHandle = outAdvHandle;
58. console.info("advHandle: " + advHandle);
59. }
60. });
61. } catch (err) {
62. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
63. }

65. // 构造启动广播参数
66. let advertisingEnableParams: ble.AdvertisingEnableParams = {
67. advertisingId: advHandle, // 使用首次启动广播时获取到的广播标识ID
68. duration: 300
69. }
70. try {
71. // 再次启动
72. ble.enableAdvertising(advertisingEnableParams, (err) => {
73. if (err) {
74. return;
75. }
76. });
77. } catch (err) {
78. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
79. }
```

* API version 10及以前支持的广播操作方式只支持应用启动单路广播。若要再次启动广播，必须先停止上一路的广播流程。详情请见[ble.startAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestartadvertising)。

```
1. // 设置广播发送的参数
2. let setting: ble.AdvertiseSetting = {
3. interval: 160,
4. txPower: 0,
5. connectable: true
6. };
7. // 构造广播数据
8. let manufactureValueBuffer = new Uint8Array(4);
9. manufactureValueBuffer[0] = 1;
10. manufactureValueBuffer[1] = 2;
11. manufactureValueBuffer[2] = 3;
12. manufactureValueBuffer[3] = 4;
13. let serviceValueBuffer = new Uint8Array(4);
14. serviceValueBuffer[0] = 5;
15. serviceValueBuffer[1] = 6;
16. serviceValueBuffer[2] = 7;
17. serviceValueBuffer[3] = 8;
18. let manufactureDataUnit: ble.ManufactureData = {
19. manufactureId: 4567,
20. manufactureValue: manufactureValueBuffer.buffer
21. };
22. let serviceDataUnit1: ble.ServiceData = {
23. serviceUuid: "00001999-0000-1000-8000-00805f9b34fb",
24. serviceValue: serviceValueBuffer.buffer
25. };
26. let serviceDataUnit2: ble.ServiceData = {
27. serviceUuid: "19991999-0000-1000-8000-00805f9b34fb",
28. serviceValue: serviceValueBuffer.buffer
29. };
30. let advData: ble.AdvertiseData = {
31. serviceUuids: ["00001888-0000-1000-8000-00805f9b34fb", "18881888-0000-1000-8000-00805f9b34fb"],
32. manufactureData: [manufactureDataUnit],
33. serviceData: [],
34. includeDeviceName: false // 表示是否携带设备名，可选参数。注意：带上设备名时，容易导致广播报文长度超出31个字节
35. };
36. let advResponse: ble.AdvertiseData = {
37. serviceUuids: [],
38. manufactureData: [],
39. serviceData: [serviceDataUnit1, serviceDataUnit2]
40. };
41. try {
42. // 启动广播
43. ble.startAdvertising(setting, advData ,advResponse);
44. } catch (err) {
45. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
46. }
```

**3. 停止广播**

广播流程会消耗蓝牙硬件资源和影响设备功耗。当应用不再需要该广播时，需要主动停止。

* 搭配API version 11开始支持的广播方式。相关API请参考[ble.disableAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#bledisableadvertising11)和[ble.stopAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestopadvertising11)。

  完全停止广播接口[ble.stopAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestopadvertising11)会释放所有广播资源，因此首次启动广播分配的广播标识将无效。

```
1. let advHandle = 1; // 注意：该值是首次启动广播时获取到的广播标识，此处是伪代码ID

3. // 构造停止广播参数
4. let advertisingDisableParams: ble.AdvertisingDisableParams = {
5. advertisingId: advHandle // 使用首次启动广播时获取到的广播标识ID
6. }
7. try {
8. // 停止
9. ble.disableAdvertising(advertisingDisableParams, (err) => {
10. if (err) {
11. return;
12. }
13. });
14. } catch (err) {
15. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
16. }

18. try {
19. // 完全停止
20. ble.stopAdvertising(advHandle, (err) => {
21. if (err) {
22. return;
23. }
24. });
25. } catch (err) {
26. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
27. }
```

* 搭配API version 11及以前支持的单路广播方式。相关API请参考[ble.stopAdvertising](../harmonyos-references/js-apis-bluetooth-ble.md#blestopadvertising)。

```
1. try {
2. // 停止
3. ble.stopAdvertising();
4. } catch (err) {
5. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
6. }
```

## 完整示例

### BLE扫描流程

```
1. import { ble } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@ohos.base';

4. const TAG: string = 'BleScanManager';

6. // 参考蓝牙标准协议规范Core Assigned Numbers
7. const BLE_ADV_TYPE_FLAG = 0x01;
8. const BLE_ADV_TYPE_16_BIT_SERVICE_UUIDS_INCOMPLETE = 0x02;
9. const BLE_ADV_TYPE_16_BIT_SERVICE_UUIDS_COMPLETE = 0x03;
10. const BLE_ADV_TYPE_32_BIT_SERVICE_UUIDS_INCOMPLETE = 0x04;
11. const BLE_ADV_TYPE_32_BIT_SERVICE_UUIDS_COMPLETE = 0x05;
12. const BLE_ADV_TYPE_128_BIT_SERVICE_UUIDS_INCOMPLETE = 0x06;
13. const BLE_ADV_TYPE_128_BIT_SERVICE_UUIDS_COMPLETE = 0x07;
14. const BLE_ADV_TYPE_LOCAL_NAME_SHORT = 0x08;
15. const BLE_ADV_TYPE_LOCAL_NAME_COMPLETE = 0x09;
16. const BLE_ADV_TYPE_TX_POWER_LEVEL = 0x0A;
17. const BLE_ADV_TYPE_16_BIT_SERVICE_SOLICITATION_UUIDS = 0x14;
18. const BLE_ADV_TYPE_128_BIT_SERVICE_SOLICITATION_UUIDS = 0x15;
19. const BLE_ADV_TYPE_32_BIT_SERVICE_SOLICITATION_UUIDS = 0x1F;
20. const BLE_ADV_TYPE_16_BIT_SERVICE_DATA = 0x16;
21. const BLE_ADV_TYPE_32_BIT_SERVICE_DATA = 0x20;
22. const BLE_ADV_TYPE_128_BIT_SERVICE_DATA = 0x21;
23. const BLE_ADV_TYPE_MANUFACTURER_SPECIFIC_DATA = 0xFF;

25. const BLUETOOTH_UUID_16_BIT_LENGTH = 2;
26. const BLUETOOTH_UUID_32_BIT_LENGTH = 4;
27. const BLUETOOTH_UUID_128_BIT_LENGTH = 16;

29. const BLUETOOTH_MANUFACTURE_ID_LENGTH = 2;

31. export class BleScanManager {
32. bleScanner: ble.BleScanner = ble.createBleScanner();

34. // 1. 定义扫描结果上报回调函数
35. onReceiveEvent = (scanReport: ble.ScanReport) => {
36. console.info(TAG, 'BLE scan device find result: '+ JSON.stringify(scanReport));
37. if (scanReport.scanResult.length > 0) {
38. console.info(TAG, 'BLE scan result: ' + scanReport.scanResult[0].deviceId);
39. this.parseScanResult(scanReport.scanResult[0].data);
40. }
41. };

43. public parseScanResult(data: ArrayBuffer) {
44. let advData = new Uint8Array(data);
45. if (advData.byteLength == 0) {
46. console.warn(TAG, 'adv data length is 0');
47. return;
48. }

50. let advertiseFlags: number = -1;
51. let txPowerLevel: number = -1;
52. let localName: string = '';
53. let serviceUuids: string[] = [];
54. let serviceSolicitationUuids: string[] = [];
55. let manufactureSpecificDatas: Record<number, Uint8Array> = {};
56. let serviceDatas: Record<string, Uint8Array> = {};

58. let curPos = 0;
59. while (curPos < advData.byteLength) {
60. let length = advData[curPos++]; // 获取当前广播类型的长度（length+data），curPos指向下一个位置
61. if (length == 0) {
62. break;
63. }

65. // 获取当前广播类型内容长度（data）
66. let advDataLength = length - 1;

68. // 获取当前广播类型，curPos指向下一个位置，从该位置解析实际内容，参考Core Specification Supplement, PartA
69. let advDataType = advData[curPos++];
70. switch (advDataType) {
71. case BLE_ADV_TYPE_FLAG:
72. advertiseFlags = advData[curPos];
73. break;
74. case BLE_ADV_TYPE_LOCAL_NAME_SHORT:
75. case BLE_ADV_TYPE_LOCAL_NAME_COMPLETE:
76. localName = advData.slice(curPos, curPos + advDataLength).toString();
77. break;
78. case BLE_ADV_TYPE_TX_POWER_LEVEL:
79. txPowerLevel = advData[curPos];
80. break;
81. case BLE_ADV_TYPE_16_BIT_SERVICE_UUIDS_INCOMPLETE:
82. case BLE_ADV_TYPE_16_BIT_SERVICE_UUIDS_COMPLETE:
83. this.parseServiceUuid(BLUETOOTH_UUID_16_BIT_LENGTH, curPos, advDataLength, advData, serviceUuids);
84. break;
85. case BLE_ADV_TYPE_32_BIT_SERVICE_UUIDS_INCOMPLETE:
86. case BLE_ADV_TYPE_32_BIT_SERVICE_UUIDS_COMPLETE:
87. this.parseServiceUuid(BLUETOOTH_UUID_32_BIT_LENGTH, curPos, advDataLength, advData, serviceUuids);
88. break;
89. case BLE_ADV_TYPE_128_BIT_SERVICE_UUIDS_INCOMPLETE:
90. case BLE_ADV_TYPE_128_BIT_SERVICE_UUIDS_COMPLETE:
91. this.parseServiceUuid(BLUETOOTH_UUID_128_BIT_LENGTH, curPos, advDataLength, advData, serviceUuids);
92. break;
93. case BLE_ADV_TYPE_16_BIT_SERVICE_SOLICITATION_UUIDS:
94. this.parseServiceSolicitationUuid(BLUETOOTH_UUID_16_BIT_LENGTH, curPos, advDataLength,
95. advData, serviceSolicitationUuids);
96. break;
97. case BLE_ADV_TYPE_32_BIT_SERVICE_SOLICITATION_UUIDS:
98. this.parseServiceSolicitationUuid(BLUETOOTH_UUID_32_BIT_LENGTH, curPos, advDataLength,
99. advData, serviceSolicitationUuids);
100. break;
101. case BLE_ADV_TYPE_128_BIT_SERVICE_SOLICITATION_UUIDS:
102. this.parseServiceSolicitationUuid(BLUETOOTH_UUID_128_BIT_LENGTH, curPos, advDataLength,
103. advData, serviceSolicitationUuids);
104. break;
105. case BLE_ADV_TYPE_16_BIT_SERVICE_DATA:
106. this.parseServiceData(BLUETOOTH_UUID_16_BIT_LENGTH, curPos, advDataLength, advData, serviceDatas);
107. break;
108. case BLE_ADV_TYPE_32_BIT_SERVICE_DATA:
109. this.parseServiceData(BLUETOOTH_UUID_32_BIT_LENGTH, curPos, advDataLength, advData, serviceDatas);
110. break;
111. case BLE_ADV_TYPE_128_BIT_SERVICE_DATA:
112. this.parseServiceData(BLUETOOTH_UUID_128_BIT_LENGTH, curPos, advDataLength, advData, serviceDatas);
113. break;
114. case BLE_ADV_TYPE_MANUFACTURER_SPECIFIC_DATA:
115. this.parseManufactureData(curPos, advDataLength, advData, manufactureSpecificDatas);
116. break;
117. default:
118. break;
119. }
120. curPos += advDataLength; // curPos指向下一个字段类型
121. }
122. console.info(TAG, 'advertiseFlags: ' + advertiseFlags);
123. console.info(TAG, 'txPowerLevel: ' + txPowerLevel);
124. console.info(TAG, 'localName: ' + localName);
125. console.info(TAG, 'serviceUuids: ' + JSON.stringify(serviceUuids));
126. console.info(TAG, 'serviceSolicitationUuids: ' + JSON.stringify(serviceSolicitationUuids));
127. console.info(TAG, 'manufactureSpecificDatas: ' + JSON.stringify(manufactureSpecificDatas));
128. console.info(TAG, 'serviceDatas: ' + JSON.stringify(serviceDatas));
129. }

131. private parseServiceUuid(uuidLength: number, curPos: number, advDataLength: number,
132. advData: Uint8Array, serviceUuids: string[]) {
133. while (advDataLength > 0) {
134. let tmpData: Uint8Array = advData.slice(curPos, curPos + uuidLength);
135. serviceUuids.push(this.getUuidFromUint8Array(uuidLength, tmpData));
136. advDataLength -= uuidLength;
137. curPos += uuidLength;
138. }
139. }

141. private parseServiceSolicitationUuid(uuidLength: number, curPos: number, advDataLength: number,
142. advData: Uint8Array, serviceSolicitationUuids: string[]) {
143. while (advDataLength > 0) {
144. let tmpData: Uint8Array = advData.slice(curPos, curPos + uuidLength);
145. serviceSolicitationUuids.push(this.getUuidFromUint8Array(uuidLength, tmpData));
146. advDataLength -= uuidLength;
147. curPos += uuidLength;
148. }
149. }

151. private getUuidFromUint8Array(uuidLength: number, uuidData: Uint8Array): string {
152. let uuid = "";
153. let temp: string = "";
154. for (let i = uuidLength - 1; i > -1; i--) {
155. temp += uuidData[i].toString(16).padStart(2, "0");
156. }
157. switch (uuidLength) {
158. case BLUETOOTH_UUID_16_BIT_LENGTH:
159. uuid = `0000${temp}-0000-1000-8000-00805F9B34FB`;
160. break;
161. case BLUETOOTH_UUID_32_BIT_LENGTH:
162. uuid = `${temp}-0000-1000-8000-00805F9B34FB`;
163. break;
164. case BLUETOOTH_UUID_128_BIT_LENGTH:
165. uuid = `${temp.substring(0, 8)}-${temp.substring(8, 12)}-${temp.substring(12, 16)}-${temp.substring(16, 20)}-${temp.substring(20, 32)}`;
166. break;
167. default:
168. break;
169. }
170. return uuid;
171. }

173. private parseServiceData(uuidLength: number, curPos: number, advDataLength: number,
174. advData: Uint8Array, serviceDatas: Record<number, Uint8Array>) {
175. let uuid: Uint8Array = advData.slice(curPos, curPos + uuidLength);
176. let data: Uint8Array = advData.slice(curPos + uuidLength, curPos + advDataLength);
177. serviceDatas[this.getUuidFromUint8Array(uuidLength, uuid)] = data;
178. }

180. private parseManufactureData(curPos: number, advDataLength: number,
181. advData: Uint8Array, manufactureSpecificDatas: Record<number, Uint8Array>) {
182. let manufactureId: number = (advData[curPos + 1] << 8) + advData[curPos];
183. let data: Uint8Array = advData.slice(curPos + BLUETOOTH_MANUFACTURE_ID_LENGTH, curPos + advDataLength);
184. manufactureSpecificDatas[manufactureId] = data;
185. }

187. // 2. 开启扫描
188. public startScan() {
189. // 2.1 构造扫描BLE广播的过滤条件，目标BLE广播报文需符合该过滤条件
190. let manufactureId = 4567;
191. let manufactureData: Uint8Array = new Uint8Array([1, 2, 3, 4]);
192. let manufactureDataMask: Uint8Array = new Uint8Array([0xFF, 0xFF, 0xFF, 0xFF]);
193. let scanFilter: ble.ScanFilter = { // 根据业务实际情况定义过滤器
194. manufactureId: manufactureId,
195. manufactureData: manufactureData.buffer,
196. manufactureDataMask: manufactureDataMask.buffer
197. };

199. // 2.2 构造扫描配置参数
200. let scanOptions: ble.ScanOptions = {
201. interval: 0,
202. dutyMode: ble.ScanDuty.SCAN_MODE_LOW_POWER,
203. matchMode: ble.MatchMode.MATCH_MODE_AGGRESSIVE
204. }
205. try {
206. // 发起订阅
207. this.bleScanner.on('BLEDeviceFind', this.onReceiveEvent);
208. // 发起扫描
209. this.bleScanner.startScan([scanFilter], scanOptions);
210. console.info('startBleScan success');
211. } catch (err) {
212. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
213. }
214. }

216. // 3. 关闭扫描
217. public stopScan() {
218. try {
219. // 取消订阅
220. this.bleScanner.off('BLEDeviceFind', this.onReceiveEvent);
221. // 停止扫描
222. this.bleScanner.stopScan();
223. console.info('stopBleScan success');
224. } catch (err) {
225. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
226. }
227. }
228. }

230. let bleScanManager = new BleScanManager();
231. export default bleScanManager as BleScanManager;
```

### BLE广播流程

```
1. import { ble } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = 'BleAdvertisingManager';

6. export class BleAdvertisingManager {
7. private advHandle: number = 0xFF; // 初始的无效值

9. // 1. 定义广播状态上报事件
10. onReceiveEvent = (data: ble.AdvertisingStateChangeInfo) => {
11. console.info(TAG, 'bluetooth advertising state = ' + JSON.stringify(data));
12. AppStorage.setOrCreate('advertiserState', data.state);
13. };

15. // 2. 首次启动广播
16. public async startAdvertising() {
17. // 2.1 设置广播发送的参数
18. let setting: ble.AdvertiseSetting = {
19. interval: 160,
20. txPower: 0,
21. connectable: true
22. };
23. // 2.2 构造广播数据
24. let manufactureValueBuffer = new Uint8Array(4);
25. manufactureValueBuffer[0] = 1;
26. manufactureValueBuffer[1] = 2;
27. manufactureValueBuffer[2] = 3;
28. manufactureValueBuffer[3] = 4;
29. let serviceValueBuffer = new Uint8Array(4);
30. serviceValueBuffer[0] = 5;
31. serviceValueBuffer[1] = 6;
32. serviceValueBuffer[2] = 7;
33. serviceValueBuffer[3] = 8;
34. let manufactureDataUnit: ble.ManufactureData = {
35. manufactureId: 4567,
36. manufactureValue: manufactureValueBuffer.buffer
37. };
38. let serviceDataUnit1: ble.ServiceData = {
39. serviceUuid: "00001999-0000-1000-8000-00805f9b34fb",
40. serviceValue: serviceValueBuffer.buffer
41. };
42. let serviceDataUnit2: ble.ServiceData = {
43. serviceUuid: "19991999-0000-1000-8000-00805f9b34fb",
44. serviceValue: serviceValueBuffer.buffer
45. };
46. let advData: ble.AdvertiseData = {
47. serviceUuids: ["00001888-0000-1000-8000-00805f9b34fb", "18881888-0000-1000-8000-00805f9b34fb"],
48. manufactureData: [manufactureDataUnit],
49. serviceData: [],
50. includeDeviceName: false // 表示是否携带设备名，可选参数。注意：带上设备名时，容易导致广播报文长度超出31个字节，使得广播启动失败
51. };
52. let advResponse: ble.AdvertiseData = {
53. serviceUuids: [],
54. manufactureData: [],
55. serviceData: [serviceDataUnit1, serviceDataUnit2]
56. };
57. // 2.3 构造广播启动完整参数AdvertisingParams
58. let advertisingParams: ble.AdvertisingParams = {
59. advertisingSettings: setting,
60. advertisingData: advData, // 注意: 广播报文长度不能超过31个字节
61. advertisingResponse: advResponse, // 注意: 广播报文长度不能超过31个字节
62. duration: 0 // 可选参数，若参数大于0，则广播发送一段时间后会停止，但分配的广播资源还在，可重新启动发送
63. }

65. // 2.4 首次启动广播，蓝牙子系统会分配相关资源，包括应用获取到的广播标识ID
66. try {
67. ble.on('advertisingStateChange', this.onReceiveEvent);
68. this.advHandle = await ble.startAdvertising(advertisingParams);
69. } catch (err) {
70. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
71. }
72. }

74. // 3. 停止指定标识的广播，即首次启动时分配的标识，停止后，该路广播资源仍然存在
75. public async disableAdvertising() {
76. // 3.1 构造停止广播参数
77. let advertisingDisableParams: ble.AdvertisingDisableParams = {
78. advertisingId: this.advHandle // 使用首次启动广播时获取到的广播标识ID
79. }
80. try {
81. // 3.2 停止
82. await ble.disableAdvertising(advertisingDisableParams);
83. } catch (err) {
84. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
85. }
86. }

88. // 4. 启动指定标识的广播，即首次启动时分配的标识
89. public async enableAdvertising(enableDuration: number) {
90. // 4.1 构造启动广播参数
91. let advertisingEnableParams: ble.AdvertisingEnableParams = {
92. advertisingId: this.advHandle, // 使用首次启动广播时获取到的广播标识ID
93. duration: enableDuration
94. }
95. try {
96. // 4.2 再次启动
97. await ble.enableAdvertising(advertisingEnableParams);
98. } catch (err) {
99. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
100. }
101. }

103. // 5. 完全停止广播，释放广播资源
104. public async stopAdvertising() {
105. try {
106. await ble.stopAdvertising(this.advHandle);
107. ble.off('advertisingStateChange', this.onReceiveEvent);
108. } catch (err) {
109. console.error(TAG, 'errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
110. }
111. }
112. }

114. let bleAdvertisingManager = new BleAdvertisingManager();
115. export default bleAdvertisingManager as BleAdvertisingManager;
```
