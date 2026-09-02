---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/query_device_info
title: 穿戴设备信息查询
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 穿戴设备信息查询
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:38+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:1cee79d7a1c0c80358755462c019bc9198d2dfb11fa6fbcc762ff92c88d7c433
---

```typescript
// 在使用Wear Engine服务前，请导入WearEngine与相关模块
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';
```

## 查询穿戴设备是否支持某种WearEngine能力集

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

通过[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[isWearEngineCapabilitySupported](../harmonyos-references/wearengine_api.md#iswearenginecapabilitysupported)查询穿戴设备是否支持某种WearEngine能力集。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。

   ```typescript
   let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   ```
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，获取已连接的设备列表。

   ```typescript
   let deviceList: wearEngine.Device[] = [];
   deviceClient.getConnectedDevices().then(devices => {
     // 存储已连接的设备列表
     deviceList = devices;
     console.info(`Succeeded in getting deviceList, devices number is ${deviceList.length}`);
   }).catch((error: BusinessError) => {
     // 处理调用失败时捕获到的异常
     console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   });
   ```
3. 从设备列表中选取需要操作的设备。
4. 调用[Device](../harmonyos-references/wearengine_api.md#device)对象中的[isWearEngineCapabilitySupported](../harmonyos-references/wearengine_api.md#iswearenginecapabilitysupported)接口可查询该设备是否支持传入的WearEngine能力（true：支持；false：不支持），以P2P能力为例。

   ```typescript
   if (deviceList.length > 0) {
     // 步骤3 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
     let targetDevice: wearEngine.Device = deviceList[0];

     // 步骤4 调用设备的方法查询是否支持某种WearEngine能力（以P2P为例）
     targetDevice.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P_COMMUNICATION).then((isSupportP2P) => {
       console.info(`Succeeded in checking p2p capability, result is ${isSupportP2P}`);
     }).catch((error: BusinessError) => {
       console.error(`Failed to check p2p capability. Code is ${error.code}, message is ${error.message}`);
     });
   }
   ```

## 查询穿戴设备是否支持某种Device能力集

**说明** 

该接口的调用需要在开发者联盟申请设备基础信息权限（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

通过[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[isDeviceCapabilitySupported](../harmonyos-references/wearengine_api.md#isdevicecapabilitysupported)查询穿戴设备是否支持某种Device能力集。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。

   ```typescript
   let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   ```
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，获取已连接的设备列表。

   ```typescript
   let deviceList: wearEngine.Device[] = [];
   deviceClient.getConnectedDevices().then(devices => {
     // 存储已连接的设备列表
     deviceList = devices;
     console.info(`Succeeded in getting deviceList, devices number is ${deviceList.length}`);
   }).catch((error: BusinessError) => {
     // 处理调用失败时捕获到的异常
     console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   });
   ```
3. 从设备列表中选取需要操作的设备。
4. 调用[Device](../harmonyos-references/wearengine_api.md#device)对象中的[isDeviceCapabilitySupported](../harmonyos-references/wearengine_api.md#isdevicecapabilitysupported)接口可查询该设备是否支持传入的Device能力（true：支持；false：不支持）。

   ```typescript
   if (deviceList.length > 0) {
     // 步骤3 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
     let targetDevice: wearEngine.Device = deviceList[0];

     // 步骤4 调用设备的方法查询是否支持某种Device能力（以是否支持应用安装为例）
     targetDevice.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION).then((isSupportInstall) => {
       console.info(`Succeeded in checking install app capability, result is ${isSupportInstall}`);
     }).catch((error: BusinessError) => {
       console.error(`Failed to check install app capability. Code is ${error.code}, message is ${error.message}`);
     });
   }
   ```

## 查询设备SN

**说明** 

该接口的调用需要在开发者联盟申请设备标识符权限（受限开放）并获得用户授权（请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

通过[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[getSerialNumber](../harmonyos-references/wearengine_api.md#getserialnumber)查询穿戴设备的SN。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。

   ```typescript
   let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   ```
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，获取已连接的设备列表。

   ```typescript
   let deviceList: wearEngine.Device[] = [];
   deviceClient.getConnectedDevices().then(devices => {
     // 存储已连接的设备列表
     deviceList = devices;
     console.info(`Succeeded in getting deviceList, devices number is ${deviceList.length}`);
   }).catch((error: BusinessError) => {
     // 处理调用失败时捕获到的异常
     console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   });
   ```
3. 从设备列表中选取需要操作的设备。
4. 调用[Device](../harmonyos-references/wearengine_api.md#device)对象中的方法[getSerialNumber](../harmonyos-references/wearengine_api.md#getserialnumber)查询穿戴设备的SN。

   ```typescript
   if (deviceList.length > 0) {
     // 步骤3 从得到的设备列表中选取目标设备，并定义为device(假设数组中存在已连接设备且第一位即为目标设备)
     let targetDevice: wearEngine.Device = deviceList[0];

     // 步骤4 调用设备的方法查询SN
     targetDevice.getSerialNumber().then((sn) => {
       console.info(`Succeeded in getting device SN, result is ${sn}`);
     }).catch((error: BusinessError) => {
       console.error(`Failed to get device SN. Code is ${error.code}, message is ${error.message}`);
     });
   }
   ```
