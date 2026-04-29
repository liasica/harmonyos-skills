---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/br-discovery-development-guide
title: 查找设备
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 传统蓝牙 > 查找设备
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:28+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:97a47d321ba8fccbb46fec07289f19a0bc7f5ff09c7bb8248a28490ccacb3a8b
---

## 简介

本指南主要提供了查找设备相关的开发指导，包括如何扫描周边设备、设置本机蓝牙扫描模式以及查找已配对设备信息。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，具体操作请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### 导入所需API模块

导入connection和错误码模块。

```
1. import { connection } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 扫描周边蓝牙设备

用于扫描周边支持蓝牙能力的设备，并获取到蓝牙设备的部分信息。此过程也可被称为“搜索”、“发现”或“查找”。只有周边蓝牙设备处于可被发现的状态时，才能被本机蓝牙设备扫描到。

**1. 订阅扫描设备结果上报事件**

* 推荐使用API version 18开始支持的扫描结果上报方式。该方式可获取到更多设备信息，包括设备地址、设备信号强度、设备名称和设备类型。详情请见[connection.on('discoveryResult')](../harmonyos-references/js-apis-bluetooth-connection.md#connectionondiscoveryresult18)。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(data: Array<connection.DiscoveryResult>) {
3. console.info('bluetooth device: '+ JSON.stringify(data));
4. }

6. try {
7. // 发起订阅
8. connection.on('discoveryResult', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

* API version 17及以前的扫描结果上报方式只支持获取设备地址信息。详情请见[connection.on('bluetoothDeviceFind')](../harmonyos-references/js-apis-bluetooth-connection.md#connectiononbluetoothdevicefind)。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(data: Array<string>) {
3. console.info('bluetooth device: '+ JSON.stringify(data));
4. }

6. try {
7. // 发起订阅
8. connection.on('bluetoothDeviceFind', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

**2. 发起设备扫描**

应用发起扫描后，整个扫描过程大约持续12s。应用可以对扫描到的蓝牙设备发起配对、连接和传输数据流程。具体操作请参考[配对与连接设备](br-pair-device-development-guide.md)、[连接和传输数据](spp-development-guide.md)。

```
1. try {
2. // 判断本机设备是否正在进行扫描
3. let scan = connection.isBluetoothDiscovering();
4. if (!scan) {
5. // 若当前不处于扫描过程，则开始扫描设备
6. connection.startBluetoothDiscovery();
7. }
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

**3. 停止设备扫描**

扫描是一个很消耗蓝牙硬件资源的过程。当扫描到应用所需的蓝牙设备后，在发起连接前，必须停止设备扫描。

```
1. // 定义扫描结果上报回调函数
2. function onReceiveEvent(data: Array<string>) {
3. console.info('bluetooth device: '+ JSON.stringify(data));
4. }

6. try {
7. // 判断本机设备是否正在进行扫描
8. let scan = connection.isBluetoothDiscovering();
9. if (scan) {
10. // 若当前处于扫描过程，则停止扫描设备
11. connection.stopBluetoothDiscovery();
12. }
13. // 若不再需要使用扫描，可以取消订阅扫描上报结果
14. connection.off('bluetoothDeviceFind', onReceiveEvent);
15. } catch (err) {
16. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
17. }
```

### 设置本机蓝牙扫描模式

本机蓝牙扫描模式用于控制本机设备是否可以被周边其他蓝牙设备扫描到或连接上。非系统应用一般不用关注这个模式，系统设置应用会决定如何设置。

* 系统设置应用打开蓝牙后，若系统蓝牙设置界面在前台，会将本机蓝牙扫描模式设置为可被扫描和可被连接，即[SCAN\_MODE\_CONNECTABLE\_GENERAL\_DISCOVERABLE](../harmonyos-references/js-apis-bluetooth-connection.md#scanmode)。
* 系统设置应用打开蓝牙后，若系统蓝牙设置界面在后台，会将本机蓝牙扫描模式设置为可被连接，即[SCAN\_MODE\_CONNECTABLE](../harmonyos-references/js-apis-bluetooth-connection.md#scanmode)。

```
1. try {
2. // 获取当前本机的扫描模式
3. let scanMode: connection.ScanMode = connection.getBluetoothScanMode();
4. console.info('scanMode: ' + scanMode);
5. if (scanMode != connection.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE) {
6. // 将本机设备的扫描模式设置为可被发现和可被连接
7. connection.setBluetoothScanMode(connection.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 0);
8. }
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### 查找已配对设备信息

在发起扫描设备前，可以查找该设备是否是已配对的设备，以减少扫描设备的流程。也可以对已配对设备发起连接和传输数据流程，具体操作请参考[配对与连接设备](br-pair-device-development-guide.md)和[传输数据](spp-development-guide.md)。

```
1. try {
2. // 获取已配对设备信息
3. let devices = connection.getPairedDevices();
4. console.info('pairedDevices: ' + JSON.stringify(devices));
5. // 若已知设备地址，可主动查询该设备是否是已配对的
6. if (devices.length > 0) {
7. let pairState = connection.getPairState(devices[0]);
8. console.info('device: '+ devices[0] + ' pairState is ' + pairState);
9. }
10. } catch (err) {
11. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
12. }
```

## 完整示例

```
1. import { connection } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export class DiscoveryDeviceManager {
5. // 定义扫描结果上报回调函数
6. onReceiveEvent = (data: Array<string>) => {
7. console.info('bluetooth device: '+ JSON.stringify(data));
8. };

10. public startDiscovery() {
11. try {
12. connection.on('bluetoothDeviceFind', this.onReceiveEvent);
13. } catch (err) {
14. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
15. }
16. try {
17. // 判断本机设备是否正在进行扫描
18. let scan = connection.isBluetoothDiscovering();
19. if (!scan) {
20. // 若当前不处于扫描过程，则开始扫描设备
21. connection.startBluetoothDiscovery();
22. }
23. } catch (err) {
24. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
25. }
26. }

28. public stopDiscovery() {
29. try {
30. // 判断本机设备是否正在进行扫描
31. let scan = connection.isBluetoothDiscovering();
32. if (scan) {
33. // 若当前处于扫描过程，则停止扫描设备
34. connection.stopBluetoothDiscovery();
35. }
36. // 若不再需要使用扫描，可以取消订阅扫描上报结果
37. connection.off('bluetoothDeviceFind', this.onReceiveEvent);
38. } catch (err) {
39. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
40. }
41. }

43. public setScanMode() {
44. try {
45. // 获取当前本机的扫描模式
46. let scanMode: connection.ScanMode = connection.getBluetoothScanMode();
47. console.info('scanMode: ' + scanMode);
48. if (scanMode != connection.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE) {
49. // 将本机设备的扫描模式设为可被发现和可被连接
50. connection.setBluetoothScanMode(connection.ScanMode.SCAN_MODE_CONNECTABLE_GENERAL_DISCOVERABLE, 0);
51. }
52. } catch (err) {
53. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
54. }
55. }

57. public getPairedDevices() {
58. try {
59. // 获取已配对设备信息
60. let devices = connection.getPairedDevices();
61. console.info('pairedDevices: ' + JSON.stringify(devices));
62. // 若已知设备地址，可主动查询该设备是否是已配对的
63. if (devices.length > 0) {
64. let pairState = connection.getPairState(devices[0]);
65. console.info('device: '+ devices[0] + ' pairState is ' + pairState);
66. }
67. } catch (err) {
68. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
69. }
70. }
71. }

73. let discoveryDeviceManager = new DiscoveryDeviceManager();
74. export default discoveryDeviceManager as DiscoveryDeviceManager;
```
