---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-device-management
title: 相机管理(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(ArkTS) > 相机管理(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:55+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:4abe54400367c52973bae3b0b389966a36ad689f5e54d59053f3c6eb9f02e5ea
---

在开发一个相机应用前，需要先通过调用相机接口来创建一个相机管理实例。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   ```
2. 通过[getCameraManager](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)方法，获取cameraManager对象。

   Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. function getCameraManager(context: common.BaseContext): camera.CameraManager | undefined {
   2. let cameraManager: camera.CameraManager;
   3. try {
   4. cameraManager = camera.getCameraManager(context);
   5. } catch (error) {
   6. let err = error as BusinessError;
   7. console.error(`getCameraManager error, errCode: ${err.code}`);
   8. return undefined;
   9. }
   10. return cameraManager;
   11. }
   ```

   说明

   如果获取对象失败，说明相机可能被占用或无法使用。如果被占用，须等到相机被释放后才能重新获取。
3. 通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)方法，获取当前设备支持的相机列表，列表中存储了设备支持的所有相机ID。若列表不为空，则说明列表中的每个ID都支持独立创建相机对象；否则，说明当前设备无可用相机，无法进行后续操作。

   ```
   1. function getCameraDevices(cameraManager: camera.CameraManager): Array<camera.CameraDevice> {
   2. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
   3. if (cameraArray != undefined && cameraArray.length > 0) {
   4. for (let index = 0; index < cameraArray.length; index++) {
   5. console.info('cameraId : ' + cameraArray[index].cameraId);  // 获取相机ID。
   6. console.info('cameraPosition : ' + cameraArray[index].cameraPosition);  // 获取相机位置。
   7. console.info('cameraType : ' + cameraArray[index].cameraType);  // 获取相机类型。
   8. console.info('connectionType : ' + cameraArray[index].connectionType);  // 获取相机连接类型。
   9. }
   10. return cameraArray;
   11. } else {
   12. console.error("cameraManager.getSupportedCameras error");
   13. return [];
   14. }
   15. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听相机状态，包括新相机的出现、相机的移除、相机的可用状态。在回调函数中，通过相机ID、相机状态这两个参数进行监听，如当有新相机出现时，可以将新相机加入到应用的备用相机中。

通过注册cameraStatus事件，通过回调返回监听结果，callback返回CameraStatusInfo参数，参数的具体内容可参考相机管理器回调接口实例[CameraStatusInfo](../harmonyos-references/arkts-apis-camera-i.md#camerastatusinfo)。

```
1. function onCameraStatusChange(cameraManager: camera.CameraManager): void {
2. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
3. if (err !== undefined && err.code !== 0) {
4. console.error(`Callback Error, errorCode: ${err.code}`);
5. return;
6. }
7. // 如果当通过USB连接相机设备时，回调函数会返回新的相机出现状态。
8. if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_APPEAR) {
9. console.info(`New Camera device appear.`);
10. }
11. // 如果当断开相机设备USB连接时，回调函数会返回相机被移除状态。
12. if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_DISAPPEAR) {
13. console.info(`Camera device has been removed.`);
14. }
15. // 相机被关闭时，回调函数会返回相机可用状态。
16. if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_AVAILABLE) {
17. console.info(`Current Camera is available.`);
18. }
19. // 相机被打开/占用时，回调函数会返回相机不可用状态。
20. if (cameraStatusInfo.status == camera.CameraStatus.CAMERA_STATUS_UNAVAILABLE) {
21. console.info(`Current Camera has been occupied.`);
22. }
23. console.info(`camera: ${cameraStatusInfo.camera.cameraId}`);
24. console.info(`status: ${cameraStatusInfo.status}`);
25. });
26. }
```
