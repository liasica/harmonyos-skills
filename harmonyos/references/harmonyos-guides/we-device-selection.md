---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/we-device-selection
title: 目标设备选择
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > 手机侧应用开发 > 应用开发 > 目标设备选择
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:52+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0f265cb82e8809dd2fdc48042bc24987b8b924a6117d3944b3b15ed4dd118c65
---

当获取到的已连接设备列表中包含多个设备时，需要根据业务需求正确挑选目标设备。

## 选择某种类型的设备

获取到的设备[Device](../harmonyos-references/wearengine_api.md#device)类中，包含有[DeviceCategory](../harmonyos-references/wearengine_api.md#devicecategory)字段，表明了当前设备的类型，可根据设备的类型挑选目标设备。

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 从已连接设备列表中根据设备类型选定需要通信的设备。

   ```
   1. // 声明目标设备
   2. let targetDevice: wearEngine.Device;
   3. for (let index = 0; index < deviceList.length; index++) {
   4. // 挑选类型为手表的设备
   5. if (deviceList[index].category === wearEngine.DeviceCategory.WATCH) {
   6. targetDevice = deviceList[index];
   7. break;
   8. }
   9. if (index === deviceList.length - 1) {
   10. // 若不存在目标设备则抛出错误
   11. throw new Error('cannot find target device');
   12. }
   13. }
   14. // targetDevice为undefined则抛出错误
   15. if (!targetDevice) {
   16. throw new Error('The value of targetDevice is undefined');
   17. }
   ```

## 选择支持某种能力集的设备

获取到的设备中包含了查询能力集的方法，可参考[穿戴设备信息查询](query_device_info.md)章节。

### 根据设备支持的WearEngine能力集挑选目标设备

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 从已连接设备列表中根据WearEngine能力集选定需要通信的设备。

   ```
   1. async function fun() {
   2. // 声明目标设备
   3. let targetDevice: wearEngine.Device;
   4. for (let index = 0; index < deviceList.length; index++) {
   5. // 挑选类型为手表的设备
   6. if (await device.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.MONITOR)) {
   7. targetDevice = deviceList[index];
   8. break;
   9. }
   10. if (index === deviceList.length - 1) {
   11. // 若不存在目标设备则抛出错误
   12. throw new Error('cannot find target device');
   13. }
   14. }
   15. // targetDevice为undefined则抛出错误
   16. if (!targetDevice) {
   17. throw new Error('The value of targetDevice is undefined.');
   18. }
   19. }
   ```

### 根据设备支持的Device能力集挑选目标设备

1. 参见[已连接穿戴设备查询](query_connected_devices.md)章节，获取已连接设备列表。
2. 从已连接设备列表中根据Device能力集选定需要通信的设备。

   ```
   1. async function fun() {
   2. // 声明目标设备
   3. let targetDevice: wearEngine.Device;
   4. for (let index = 0; index < deviceList.length; index++) {
   5. // 挑选类型为手表的设备
   6. if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP_INSTALLATION)) {
   7. targetDevice = deviceList[index];
   8. break;
   9. }
   10. if (index === deviceList.length - 1) {
   11. // 若不存在目标设备则抛出错误
   12. throw new Error('cannot find target device');
   13. }
   14. }
   15. // targetDevice为undefined则抛出错误
   16. if (!targetDevice) {
   17. throw new Error('The value of targetDevice is undefined.');
   18. }
   19. }
   ```
