---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/br-pair-device-development-guide
title: 配对与连接设备
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 传统蓝牙 > 配对与连接设备
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:76b90e1d4b90fbf5edd1d61248458bdcaba73345e653e7448c4d3b20b5f617dc
---

## 简介

本指南主要提供了主动配对设备和连接设备可用profile能力的开发指导。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，具体操作请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### 导入所需API模块

导入connection、a2dp、 hfp、 hid、baseProfile、constant和错误码模块。

```
1. import { connection, a2dp, hfp, hid, baseProfile, constant, common } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 订阅配对状态变化事件

通过订阅配对状态变化事件，可以获取实时的配对状态。在整个配对过程中，涉及多种状态的跃迁，其中[BOND\_STATE\_BONDED](../harmonyos-references/js-apis-bluetooth-connection.md#bondstate)表示已配对。

应用主动发起配对其他设备，或者其他设备主动配对本机设备，都可以通过此事件获取配对情况。

```
1. // 定义配对状态变化函数回调
2. function onReceiveEvent(data: connection.BondStateParam) {
3. console.info('pair result: '+ JSON.stringify(data));
4. }

6. try {
7. // 发起订阅
8. connection.on('bondStateChange', onReceiveEvent);
9. } catch (err) {
10. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
11. }
```

### 发起配对

若目标设备的配对状态是[BOND\_STATE\_INVALID](../harmonyos-references/js-apis-bluetooth-connection.md#bondstate)，则可以主动配对目标设备。

* 目标设备可以通过发现设备流程获取，详情请参考：[传统蓝牙查找设备](br-discovery-development-guide.md)或者[低功耗蓝牙查找设备](ble-development-guide.md)。

配对过程中，系统会弹出对话框。不同配对类型，对话框样式可能不一样，其中“确认配对密钥（Confirm Passkey）”模式如下图1。若用户同意授权，才能配对成功。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/hOSScrsITJqwsPFnyDuVaQ/zh-cn_image_0000002558764920.png?HW-CC-KV=V1&HW-CC-Date=20260429T053227Z&HW-CC-Expire=86400&HW-CC-Sign=1538629D75F90B7032FA7966424D62A562C1E85AD89EB9E70ED28AF0DC9FF181)

**图1** 蓝牙配对请求对话框

蓝牙设备的实际MAC地址属于用户的隐私信息，在发现设备过程中，蓝牙子系统会给每个蓝牙外设分配一个虚拟MAC地址，并保存该虚拟MAC地址与外设实际MAC地址的映射关系。

若开发者不知道目标设备的[地址类型](../harmonyos-references/js-apis-bluetooth-common.md#bluetoothaddresstype)，推荐使用API version 20及以前的配对方式发起配对，详情请见[connection.pairDevice](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice)。

* 此配对方式不需要关注目标设备的MAC地址类型。

```
1. // 通过发现设备流程获取目标设备地址
2. let device = '11:22:33:44:55:66';

4. try {
5. // 发起配对
6. connection.pairDevice(device).then(() => {
7. console.info('pairDevice');
8. }, (error: BusinessError) => {
9. console.error('pairDevice: errCode:' + error.code + ', errMessage:' + error.message);
10. });
11. } catch (err) {
12. console.error('startPair: errCode:' + err.code + ', errMessage:' + err.message);
13. }
```

若开发者已知目标设备的[地址类型](../harmonyos-references/js-apis-bluetooth-common.md#bluetoothaddresstype)，推荐使用API version 21开始支持的配对方式发起配对，详情请见[connection.pairDevice](../harmonyos-references/js-apis-bluetooth-connection.md#connectionpairdevice21)。

* 此配对方式需要同时指定目标设备的MAC地址和地址类型。

```
1. let btAddr: common.BluetoothAddress = {
2. "address": '11:22:33:44:55:66', // 目标设备的实际MAC地址或虚拟MAC地址
3. "addressType": common.BluetoothAddressType.REAL, // 相应的地址类型
4. }

6. try {
7. // 发起配对
8. connection.pairDevice(btAddr).then(() => {
9. console.info('pairDevice');
10. }, (error: BusinessError) => {
11. console.error('pairDevice: errCode:' + error.code + ', errMessage:' + error.message);
12. });
13. } catch (err) {
14. console.error('startPair: errCode:' + err.code + ', errMessage:' + err.message);
15. }
```

### 连接已配对设备的profile

若应用配对完目标设备后，可以调用[connectAllowedProfiles](../harmonyos-references/js-apis-bluetooth-connection.md#connectionconnectallowedprofiles16)，发起连接该设备支持的profile能力（只包括A2DP、HFP和HID）。若应用需要使用SPP连接，请参考[连接和传输数据](spp-development-guide.md)。

* 蓝牙子系统会在配对过程中查询和保存目标设备支持的所有profile能力。
* 配对完成后，应用可以主动查询目标设备的profile能力，需调用[getRemoteProfileUuids](../harmonyos-references/js-apis-bluetooth-connection.md#connectiongetremoteprofileuuids12)。若存在应用需要的能力，则可以在配对完成后30s内，发起连接目标设备的profile。

```
1. // 设备地址是已配对的设备
2. let device = 'XX:XX:XX:XX:XX:XX';

4. // 创建A2DP/HFP/HID实例
5. let a2dpSrc = a2dp.createA2dpSrcProfile();
6. let hfpAg = hfp.createHfpAgProfile();
7. let hidHost = hid.createHidHostProfile();

9. // 定义A2DP连接状态变化回调函数
10. function onA2dpConnectStateChange(data: baseProfile.StateChangeParam) {
11. console.info(`A2DP State: ${JSON.stringify(data)}`);
12. }

14. // 定义HFP连接状态变化回调函数
15. function onHfpConnectStateChange(data: baseProfile.StateChangeParam) {
16. console.info(`HFP State: ${JSON.stringify(data)}`);
17. }

19. // 定义HID连接状态变化回调函数
20. function onHidConnectStateChange(data: baseProfile.StateChangeParam) {
21. console.info(`HID State: ${JSON.stringify(data)}`);
22. }

24. try {
25. // 建议判断目标设备的profile能力是否存在A2DP/HFP/HID
26. // 订阅A2DP/HFP/HID连接状态变化事件
27. a2dpSrc.on('connectionStateChange', onA2dpConnectStateChange);
28. hfpAg.on('connectionStateChange', onHfpConnectStateChange);
29. hidHost.on('connectionStateChange', onHidConnectStateChange);

31. // 发起连接profile
32. connection.connectAllowedProfiles(device).then(() => {
33. console.info('connectAllowedProfiles');
34. }, (error: BusinessError) => {
35. console.error('errCode:' + error.code + ',errMessage' + error.message);
36. });
37. } catch (err) {
38. console.error('errCode:' + err.code + ',errMessage' + err.message);
39. }
```

## 完整示例

```
1. import { connection, a2dp, hfp, hid, baseProfile, constant } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export class PairDeviceManager {
5. device: string = '';
6. pairState: connection.BondState = connection.BondState.BOND_STATE_INVALID;
7. a2dpSrc = a2dp.createA2dpSrcProfile();
8. hfpAg = hfp.createHfpAgProfile();
9. hidHost = hid.createHidHostProfile();

11. // 定义配对状态变化回调函数
12. onBondStateEvent = (data: connection.BondStateParam) => {
13. console.info('pair result: '+ JSON.stringify(data));
14. if (data && data.deviceId == this.device) {
15. this.pairState = data.state; // 保存目标设备的配对状态
16. }
17. };

19. // 发起配对，设备地址可以通过查找设备流程获取
20. public startPair(device: string) {
21. this.device = device;
22. try {
23. // 发起订阅配对状态变化事件
24. connection.on('bondStateChange', this.onBondStateEvent);
25. } catch (err) {
26. console.error('bondStateChange errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
27. }

29. try {
30. // 发起配对
31. connection.pairDevice(device).then(() => {
32. console.info('pairDevice');
33. }, (error: BusinessError) => {
34. console.error('pairDevice: errCode:' + error.code + ',errMessage' + error.message);
35. });
36. } catch (err) {
37. console.error('startPair: errCode:' + err.code + ',errMessage' + err.message);
38. }
39. }

41. // 定义A2DP连接状态变化回调函数
42. onA2dpConnectStateChange = (data: baseProfile.StateChangeParam) => {
43. console.info(`A2DP State: ${JSON.stringify(data)}`);
44. };

46. // 定义HFP连接状态变化回调函数
47. onHfpConnectStateChange = (data: baseProfile.StateChangeParam) => {
48. console.info(`HFP State: ${JSON.stringify(data)}`);
49. };

51. // 定义HID连接状态变化回调函数
52. onHidConnectStateChange = (data: baseProfile.StateChangeParam) => {
53. console.info(`HID State: ${JSON.stringify(data)}`);
54. };

56. // 发起连接
57. public async connect(device: string) {
58. try {
59. let uuids = await connection.getRemoteProfileUuids(device);
60. console.info('device: ' + device + ' remoteUuids: '+ JSON.stringify(uuids));
61. let allowedProfiles = 0;
62. // 若存在应用需要的profile，则监听对应的profile连接状态
63. if (uuids.some(uuid => uuid == constant.ProfileUuids.PROFILE_UUID_A2DP_SINK.toLowerCase())) {
64. console.info('device supports a2dp');
65. allowedProfiles++;
66. this.a2dpSrc.on('connectionStateChange', this.onA2dpConnectStateChange);
67. }
68. if (uuids.some(uuid => uuid == constant.ProfileUuids.PROFILE_UUID_HFP_HF.toLowerCase())) {
69. console.info('device supports hfp');
70. allowedProfiles++;
71. this.hfpAg.on('connectionStateChange', this.onHfpConnectStateChange);
72. }
73. if (uuids.some(uuid => uuid == constant.ProfileUuids.PROFILE_UUID_HID.toLowerCase()) ||
74. uuids.some(uuid => uuid == constant.ProfileUuids.PROFILE_UUID_HOGP.toLowerCase())) {
75. console.info('device supports hid');
76. allowedProfiles++;
77. this.hidHost.on('connectionStateChange', this.onHidConnectStateChange);
78. }
79. if (allowedProfiles > 0) { // 若存在可用的profile，则发起连接
80. connection.connectAllowedProfiles(device).then(() => {
81. console.info('connectAllowedProfiles');
82. }, (error: BusinessError) => {
83. console.error('errCode:' + error.code + ',errMessage' + error.message);
84. });
85. }
86. } catch (err) {
87. console.error('errCode:' + err.code + ',errMessage' + err.message);
88. }
89. }
90. }

92. let pairDeviceManager = new PairDeviceManager();
93. export default pairDeviceManager as PairDeviceManager;
```
