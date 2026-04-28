---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/query_device_info
title: 穿戴设备信息查询
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 穿戴设备信息查询
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9c8552bc801d9d70f3303f432a30942b460142ca4cba84e6eb3a5aaefa44d910
---

```
1. // 在使用Wear Engine服务前，请导入WearEngine与相关模块
2. import { wearEngine } from '@kit.WearEngine';
3. import { BusinessError } from '@kit.BasicServicesKit';
```

## 查询穿戴设备是否支持某种WearEngine能力集

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

通过[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[isWearEngineCapabilitySupported](../harmonyos-references/wearengine_api.md#iswearenginecapabilitysupported)查询穿戴设备是否支持某种WearEngine能力集。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。

   ```
   1. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   ```
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，获取已连接的设备列表。

   ```
   1. let deviceList: wearEngine.Device[] = [];
   2. deviceClient.getConnectedDevices().then(devices => {
   3. // 存储已连接的设备列表
   4. deviceList = devices;
   5. console.info(`Succeeded in getting deviceList, devices number is ${deviceList.length}`);
   6. }).catch((error: BusinessError) => {
   7. // 处理调用失败时捕获到的异常
   8. console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   9. })
   ```
3. 从设备列表中选取需要操作的设备。
4. 调用[Device](../harmonyos-references/wearengine_api.md#device)对象中的[isWearEngineCapabilitySupported](../harmonyos-references/wearengine_api.md#iswearenginecapabilitysupported)接口可查询该设备是否支持传入的WearEngine能力（true：支持；false：不支持），以P2P能力为例。

   ```
   1. if (deviceList.length > 0) {
   2. // 步骤3 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
   3. let targetDevice: wearEngine.Device = deviceList[0];

   5. // 步骤4 调用设备的方法查询是否支持某种WearEngine能力（以P2P为例）
   6. targetDevice.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P_COMMUNICATION).then((isSupportP2P) => {
   7. console.info(`Succeeded in checking p2p capability, result is ${isSupportP2P}`);
   8. }).catch((error: BusinessError) => {
   9. console.error(`Failed to check p2p capability. Code is ${error.code}, message is ${error.message}`);
   10. })
   11. }
   ```

## 查询穿戴设备是否支持某种Device能力集

说明

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

通过[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[isDeviceCapabilitySupported](../harmonyos-references/wearengine_api.md#isdevicecapabilitysupported)查询穿戴设备是否支持某种Device能力集。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。

   ```
   1. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   ```
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，获取已连接的设备列表。

   ```
   1. let deviceList: wearEngine.Device[] = [];
   2. deviceClient.getConnectedDevices().then(devices => {
   3. // 存储已连接的设备列表
   4. deviceList = devices;
   5. console.info(`Succeeded in getting deviceList, devices number is ${deviceList.length}`);
   6. }).catch((error: BusinessError) => {
   7. // 处理调用失败时捕获到的异常
   8. console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   9. })
   ```
3. 从设备列表中选取需要操作的设备。
4. 调用[Device](../harmonyos-references/wearengine_api.md#device)对象中的[isDeviceCapabilitySupported](../harmonyos-references/wearengine_api.md#isdevicecapabilitysupported)接口可查询该设备是否支持传入的Device能力（true：支持；false：不支持）。

   ```
   1. if (deviceList.length > 0) {
   2. // 步骤3 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
   3. let targetDevice: wearEngine.Device = deviceList[0];

   5. // 步骤4 调用设备的方法查询是否支持某种Device能力（以是否支持应用安装为例）
   6. targetDevice.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION).then((isSupportInstall) => {
   7. console.info(`Succeeded in checking install app capability, result is ${isSupportInstall}`);
   8. }).catch((error: BusinessError) => {
   9. console.error(`Failed to check install app capability. Code is ${error.code}, message is ${error.message}`);
   10. })
   11. }
   ```

## 查询设备SN

说明

该接口的调用需要在开发者联盟申请设备标识符权限（受限开放）并获得用户授权（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

通过[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[getSerialNumber](../harmonyos-references/wearengine_api.md#getserialnumber)查询穿戴设备的SN。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。

   ```
   1. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   ```
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，获取已连接的设备列表。

   ```
   1. let deviceList: wearEngine.Device[] = [];
   2. deviceClient.getConnectedDevices().then(devices => {
   3. // 存储已连接的设备列表
   4. deviceList = devices;
   5. console.info(`Succeeded in getting deviceList, devices number is ${deviceList.length}`);
   6. }).catch((error: BusinessError) => {
   7. // 处理调用失败时捕获到的异常
   8. console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   9. })
   ```
3. 从设备列表中选取需要操作的设备。
4. 调用[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[getSerialNumber](../harmonyos-references/wearengine_api.md#getserialnumber)查询穿戴设备的SN。

   ```
   1. if (deviceList.length > 0) {
   2. // 步骤3 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
   3. let targetDevice: wearEngine.Device = deviceList[0];

   5. // 步骤4 调用设备的方法查询SN
   6. targetDevice.getSerialNumber().then((sn) => {
   7. console.info(`Succeeded in getting device SN, result is ${sn}`);
   8. }).catch((error: BusinessError) => {
   9. console.error(`Failed to get device SN. Code is ${error.code}, message is ${error.message}`);
   10. })
   11. }
   ```
