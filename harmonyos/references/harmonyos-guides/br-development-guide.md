---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/br-development-guide
title: 蓝牙设置
breadcrumb: 指南 > 系统 > 网络 > Connectivity Kit（短距通信服务） > 蓝牙 > 蓝牙设置
category: harmonyos-guides
scraped_at: 2026-04-29T13:32:28+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d61f98cf178aae0cb05e4a6961ba4de27fcad9399a86d0bc248a0ef445ba6e6d
---

## 简介

本指南主要提供了开启蓝牙、关闭蓝牙和获取蓝牙开关状态的开发指导。开发者在使用蓝牙其他功能时，应确保蓝牙子系统已正常开启。

## 开发步骤

### 申请蓝牙权限

需要申请权限ohos.permission.ACCESS\_BLUETOOTH。如何配置和申请权限，具体操作请参考[声明权限](declare-permissions.md)和[向用户申请授权](request-user-authorization.md)。

### 导入所需API模块

导入access和错误码模块。

```
1. import { access } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
```

### 订阅蓝牙开关状态变化事件

通过订阅开关状态变化事件，可以获取实时的蓝牙开关状态。蓝牙开启或者关闭过程中，涉及多种蓝牙状态的跃迁。其中[STATE\_OFF](../harmonyos-references/js-apis-bluetooth-access.md#bluetoothstate)表示蓝牙已关闭，此状态下，应用不可以使用蓝牙其他功能；[STATE\_ON](../harmonyos-references/js-apis-bluetooth-access.md#bluetoothstate)表示蓝牙已打开，此状态下，应用可以使用蓝牙其他功能。

```
1. // 定义蓝牙开关状态变化函数回调
2. function onReceiveEvent(data: access.BluetoothState) {
3. let btStateMessage = '';
4. switch (data) {
5. case access.BluetoothState.STATE_OFF:
6. // 表示蓝牙是关闭的
7. btStateMessage += 'STATE_OFF';
8. break;
9. case access.BluetoothState.STATE_TURNING_ON:
10. btStateMessage += 'STATE_TURNING_ON';
11. break;
12. case access.BluetoothState.STATE_ON:
13. // 表示蓝牙是开启的，此时应用才可以使用蓝牙其他功能
14. btStateMessage += 'STATE_ON';
15. break;
16. case access.BluetoothState.STATE_TURNING_OFF:
17. btStateMessage += 'STATE_TURNING_OFF';
18. break;
19. case access.BluetoothState.STATE_BLE_TURNING_ON:
20. btStateMessage += 'STATE_BLE_TURNING_ON';
21. break;
22. case access.BluetoothState.STATE_BLE_ON:
23. btStateMessage += 'STATE_BLE_ON';
24. break;
25. case access.BluetoothState.STATE_BLE_TURNING_OFF:
26. btStateMessage += 'STATE_BLE_TURNING_OFF';
27. break;
28. default:
29. btStateMessage += 'unknown state';
30. break;
31. }
32. console.info('bluetooth state: ' + btStateMessage);
33. }

35. try {
36. // 发起订阅
37. access.on('stateChange', onReceiveEvent);
38. } catch (err) {
39. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
40. }
```

### 开启蓝牙

若应用获取到的蓝牙开关状态是关闭的，当需要使用蓝牙时，则需要主动开启蓝牙。通过订阅蓝牙开关状态，判断蓝牙是否开启成功。

系统弹出对话框并提示应用“想要开启蓝牙”，如下图1。若用户同意授权，将开启蓝牙。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/wFGosIv0REGtiME-qtRUGw/zh-cn_image_0000002589324787.png?HW-CC-KV=V1&HW-CC-Date=20260429T053226Z&HW-CC-Expire=86400&HW-CC-Sign=8B574DA72ADD2F445ECF5DC5E3C3681943C19AC6512597F6F475C3D7FBA5CFB6)

**图1** 开启蓝牙对话框

```
1. try {
2. // 主动获取蓝牙当前的开关状态
3. let state = access.getState();
4. if (state == access.BluetoothState.STATE_OFF) {
5. // 若蓝牙是关闭的，则主动开启蓝牙
6. access.enableBluetooth();
7. }
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

### 关闭蓝牙

若应用不需要使用蓝牙时，可根据实际情况判断是否需要主动关闭蓝牙。通过订阅蓝牙开关状态，判断蓝牙是否关闭成功。

系统弹出对话框并提示应用“想要关闭蓝牙”，如下图2。若用户同意授权，将关闭蓝牙。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/M4OJVJ8CQ5yWT1CGwFCphg/zh-cn_image_0000002589244725.png?HW-CC-KV=V1&HW-CC-Date=20260429T053226Z&HW-CC-Expire=86400&HW-CC-Sign=515948FB661392F1CB1868048EE73D4035E7A7195B02817C222F18DA3094522F)

**图2** 关闭蓝牙对话框

```
1. try {
2. // 主动获取蓝牙当前的开关状态
3. let state = access.getState();
4. if (state == access.BluetoothState.STATE_ON) {
5. // 若蓝牙是开启的，则主动关闭蓝牙
6. access.disableBluetooth();
7. }
8. } catch (err) {
9. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
10. }
```

## 完整示例

```
1. import { access } from '@kit.ConnectivityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export class AdapterManager {
5. // 定义蓝牙开关状态变化函数回调
6. onReceiveEvent = (data: access.BluetoothState) => {
7. let btStateMessage = '';
8. switch (data) {
9. case access.BluetoothState.STATE_OFF:
10. // 表示蓝牙是关闭的
11. btStateMessage += 'STATE_OFF';
12. break;
13. case access.BluetoothState.STATE_TURNING_ON:
14. btStateMessage += 'STATE_TURNING_ON';
15. break;
16. case access.BluetoothState.STATE_ON:
17. // 表示蓝牙是开启的，此时应用才可以使用蓝牙其他功能
18. btStateMessage += 'STATE_ON';
19. break;
20. case access.BluetoothState.STATE_TURNING_OFF:
21. btStateMessage += 'STATE_TURNING_OFF';
22. break;
23. case access.BluetoothState.STATE_BLE_TURNING_ON:
24. btStateMessage += 'STATE_BLE_TURNING_ON';
25. break;
26. case access.BluetoothState.STATE_BLE_ON:
27. btStateMessage += 'STATE_BLE_ON';
28. break;
29. case access.BluetoothState.STATE_BLE_TURNING_OFF:
30. btStateMessage += 'STATE_BLE_TURNING_OFF';
31. break;
32. default:
33. btStateMessage += 'unknown state';
34. break;
35. }
36. console.info('bluetooth state: ' + btStateMessage);
37. };

39. // 开启蓝牙
40. public openBluetooth() {
41. try {
42. access.on('stateChange', this.onReceiveEvent);
43. } catch (err) {
44. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
45. }
46. try {
47. // 主动获取蓝牙当前的开关状态
48. let state = access.getState();
49. if (state == access.BluetoothState.STATE_OFF) {
50. // 若蓝牙是关闭的，则主动开启蓝牙
51. access.enableBluetooth();
52. }
53. } catch (err) {
54. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
55. }
56. }

58. // 关闭蓝牙
59. public closeBluetooth() {
60. try {
61. // 主动获取蓝牙当前的开关状态
62. let state = access.getState();
63. if (state == access.BluetoothState.STATE_ON) {
64. // 若蓝牙是开启的，则主动关闭蓝牙
65. access.disableBluetooth();
66. }
67. } catch (err) {
68. console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
69. }
70. }
71. }

73. let adapterManager = new AdapterManager();
74. export default adapterManager as AdapterManager;
```
