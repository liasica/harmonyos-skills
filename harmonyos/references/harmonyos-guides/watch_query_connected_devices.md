---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/watch_query_connected_devices
title: 已连接对端设备查询
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 穿戴侧应用开发 > 已连接对端设备查询
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:36+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:0d9b8fa219a52fe229165608b0112f294614f1e72a0289ccd26a763aa638f339
---

Wear Engine提供查询用户在穿戴侧已连接的对端设备列表的接口。

建议开发者在使用Wear Engine其他API接口前先实现该接口功能，从已连接的对端设备列表中选定设备。

1. 调用[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，查询用户已连接的对端设备列表。
3. 从已连接设备列表中选定需要通信的对端设备。
4. 查询对端设备的操作系统类型。

   ```typescript
   // 在使用Wear Engine服务前，请导入wearEngine与相关模块
   import { wearEngine } from '@kit.WearEngine';
   import { BusinessError } from '@kit.BasicServicesKit';

   // 步骤1：获取DeviceClient对象
   // this.getUIContext().getHostContext() 表示应用上下文Context对象
   let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   // 声明目标设备
   let targetDevice: wearEngine.Device;

   // 步骤2：调用getConnectedDevices方法，查询用户是否有已连接的对端设备
   deviceClient.getConnectedDevices().then(devices => {
     console.info(`Succeeded in getting deviceList, deviceList number is ${devices.length}`);
     // 步骤3：从已连接设备列表中选定需要通信的设备
     if (devices.length > 0) {
       targetDevice = devices[0];
       console.info(`Succeeded in getting target device.`);
       // 步骤4：查询对端设备的操作系统类型
       let osCategory: wearEngine.OsCategory | undefined = targetDevice.osCategory;
       console.info(`The osCategory of target device is ${osCategory}`);
     } else {
       console.error(`Failed to get target device. deviceList is empty.`);
     }
   }).catch((error: BusinessError) => {
     // 处理调用失败时捕获到的异常
     console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   });
   ```
