---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/query_connected_devices
title: 已连接穿戴设备查询
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 已连接穿戴设备查询
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:38+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:90fa038398eec09d2559b096eeaeb32e68a6ad4ca523f6f789ae34d033bbcf52
---

**说明** 

该接口的调用前，需要在开发者联盟申请设备基础信息权限（具体请参考[申请接入Wear Engine服务](wearengine_apply.md)）。

Wear Engine提供查询用户已连接的穿戴设备列表（即支持Wear Engine能力且与手机侧运动健康App处于连接状态的穿戴设备）的接口。

建议开发者在使用Wear Engine其他API接口前先实现该接口功能。

1. 应用调用[wearEngine](../harmonyos-references/wearengine_api.md)中的[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，查询用户已连接的穿戴设备列表。

   ```typescript
   // 在使用Wear Engine服务前，请导入WearEngine与相关模块
   import { wearEngine } from '@kit.WearEngine';
   import { BusinessError } from '@kit.BasicServicesKit';

   // 步骤1：获取DeviceClient对象
   // this.getUIContext().getHostContext() 表示应用上下文Context对象
   let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   // 创建一个设备列表用于存储返回的设备
   let deviceList: wearEngine.Device[] = [];

   // 步骤2：调用getConnectedDevices方法，查询用户是否有已连接的穿戴设备
   deviceClient.getConnectedDevices().then(devices => {
     // 处理返回的设备列表
     deviceList = devices;
     console.info(`Succeeded in getting deviceList, deviceList number is ${deviceList.length}`);
   }).catch((error: BusinessError) => {
     // 处理调用失败时捕获到的异常
     console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   });
   ```
