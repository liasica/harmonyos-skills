---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/watch_query_connected_devices
title: 已连接对端设备查询
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 穿戴侧应用开发 > 已连接对端设备查询
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5317f596c8ce23447e4b62fa1d888a74563dd99dd2eb1ec77ce6ed2a890bccd5
---

Wear Engine提供查询用户在穿戴侧已连接的对端设备列表的接口。

建议开发者在使用Wear Engine其他API接口前先实现该接口功能，从已连接的对端设备列表中选定设备。

1. 调用[getDeviceClient](../harmonyos-references/wearengine_api.md#wearenginegetdeviceclient)方法，获取[DeviceClient](../harmonyos-references/wearengine_api.md#deviceclient)对象。
2. 调用[getConnectedDevices](../harmonyos-references/wearengine_api.md#getconnecteddevices)方法，查询用户已连接的穿戴设备列表。
3. 从已连接设备列表中选定需要通信的对端设备。
4. 查询对端设备的操作系统类型。

   ```
   1. // 在使用Wear Engine服务前，请导入wearEngine与相关模块
   2. import { wearEngine } from '@kit.WearEngine';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. // 步骤1：获取DeviceClient对象
   6. // this.getUIContext().getHostContext() 表示应用上下文Context对象
   7. let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
   8. // 声明目标设备
   9. let targetDevice: wearEngine.Device;

   11. // 步骤2：调用getConnectedDevices方法，查询用户是否有已连接的对端设备
   12. deviceClient.getConnectedDevices().then(devices => {
   13. console.info(`Succeeded in getting deviceList, deviceList number is ${devices.length}`);
   14. // 步骤3：从已连接设备列表中选定需要通信的设备
   15. if (devices.length > 0) {
   16. targetDevice = devices[0];
   17. console.info(`Succeeded to get target device.`);
   18. // 步骤4：查询对端设备的操作系统类型
   19. let osCategory: wearEngine.OsCategory | undefined = targetDevice.osCategory;
   20. console.info(`The osCategory of target device is ${osCategory}`);
   21. } else {
   22. console.warn(`Failed to get target device. deviceList is empty.`);
   23. }
   24. }).catch((error: BusinessError) => {
   25. // 处理调用失败时捕获到的异常
   26. console.error(`Failed to get deviceList. Code is ${error.code}, message is ${error.message}`);
   27. })
   ```
