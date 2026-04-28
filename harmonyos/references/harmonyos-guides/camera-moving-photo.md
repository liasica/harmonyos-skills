---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-moving-photo
title: 动态照片拍摄(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 动态照片拍摄(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a294e61f3d482f95b098bbc626a8ee44e78f18593b8825d014fdc0a3f6a36ff0
---

相机框架提供动态照片拍摄能力，业务应用可以类似拍摄普通照片一样，一键式拍摄得到动态照片。

应用开发动态照片主要分为以下步骤：

* 应用开发动态照片前，请参考[申请相机开发的权限](camera-preparation.md)、[相机管理](camera-device-management.md)、[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)等流程完成相机应用开发必选能力配置。
* 查询当前设备的当前模式是否支持拍摄动态照片。
* 如果支持动态照片，可以调用相机框架提供的使能接口**使能**动态照片能力。
* 监听照片回调，将照片存入媒体库。可参考[MediaLibrary Kit-访问和管理动态照片资源](photoaccesshelper-movingphoto.md)。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

说明

* 拍摄动态照片需要麦克风权限ohos.permission.MICROPHONE，权限申请和校验的方式请参考[开发准备](camera-preparation.md)。否则拍摄的照片没有声音。

1. 导入依赖，需要导入相机框架、媒体库、图片相关领域依赖。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 确定拍照输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的photoProfiles属性，可获取当前设备支持的拍照输出流，通过[createPhotoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法创建拍照输出流。

   ```
   1. function getPhotoOutput(cameraManager: camera.CameraManager,
   2. cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
   3. if (!cameraOutputCapability || !cameraOutputCapability.photoProfiles) {
   4. return;
   5. }
   6. let photoProfilesArray: Array<camera.Profile> = cameraOutputCapability.photoProfiles;
   7. if (!photoProfilesArray || photoProfilesArray.length === 0) {
   8. console.error("photoProfilesArray is null or []");
   9. return;
   10. }
   11. let photoOutput: camera.PhotoOutput | undefined = undefined;
   12. try {
   13. photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. console.error(`Failed to createPhotoOutput. error: ${err}`);
   17. }
   18. return photoOutput;
   19. }
   ```
3. 查询当前设备当前模式是否支持动态照片能力。

   说明

   查询是否支持动态照片前需要先完成相机会话配置、提交和启动会话，详细开发步骤请参考[会话管理](camera-session-management.md)。

   ```
   1. function isMovingPhotoSupported(photoOutput: camera.PhotoOutput): boolean {
   2. let isSupported: boolean = false;
   3. try {
   4. isSupported = photoOutput.isMovingPhotoSupported();
   5. } catch (error) {
   6. // 失败返回错误码error.code并处理。
   7. let err = error as BusinessError;
   8. console.error(`The isMovingPhotoSupported call failed. error code: ${err.code}`);
   9. }
   10. return isSupported;
   11. }
   ```
4. 使能动态照片拍照能力。

   说明

   使能动态照片前需要使能[分段式拍照](camera-deferred-capture.md)能力。

   ```
   1. function enableMovingPhoto(photoOutput: camera.PhotoOutput): void {
   2. try {
   3. photoOutput.enableMovingPhoto(true);
   4. } catch (error) {
   5. // 失败返回错误码error.code并处理。
   6. let err = error as BusinessError;
   7. console.error(`The enableMovingPhoto call failed. error code: ${err.code}`);
   8. }
   9. }
   ```
5. 触发拍照，与普通拍照方式相同，请参考[拍照](camera-shooting.md)。

## 状态监听

在相机应用开发过程中，可以随时监听动态照片拍照输出流状态。通过注册photoAsset的回调函数获取监听结果，photoOutput创建成功时即可监听。

```
1. function getPhotoAccessHelper(context: Context): photoAccessHelper.PhotoAccessHelper {
2. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
3. return phAccessHelper;
4. }

6. async function mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
7. phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
8. try {
9. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
10. assetChangeRequest.saveCameraPhoto();
11. await phAccessHelper.applyChanges(assetChangeRequest);
12. console.info('apply saveCameraPhoto successfully');
13. } catch (err) {
14. console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
15. }
16. }

18. function onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput, context: Context): void {
19. photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): void => {
20. if (err) {
21. console.error(`photoAssetAvailable error: ${err}.`);
22. return;
23. }
24. console.info('photoOutPutCallBack photoAssetAvailable');
25. // 调用媒体库落盘接口保存一阶段图和动态照片视频。
26. mediaLibSavePhoto(photoAsset, getPhotoAccessHelper(context));
27. });
28. }
```

## HDR动态照片

从API version 23开始，相机提供HDR动态照片拍摄能力，即组成动态照片的静态图片与动态短视频均为高动态范围（HDR）内容，能够在高光与暗部细节、色彩层次和整体质感方面优于SDR成片效果。

应用可以通过配置预览输出格式（Profile.format）和色彩空间（ColorSpace）灵活决定输出SDR/HDR动态照片。具体对应关系如下表所示，所有能力需先查后用，支持的预览输出格式通过接口[getSupportedFullOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedfulloutputcapability23)查询，支持的色彩空间通过接口[getSupportedColorSpaces](../harmonyos-references/arkts-apis-camera-colormanagementquery.md#getsupportedcolorspaces12)查询。

| 静图动态范围 | 短视频动态范围 | 预览输出格式 | 色彩空间 |
| --- | --- | --- | --- |
| SDR | SDR | CAMERA\_FORMAT\_YUV\_420\_SP | SRGB |
| HDR | SDR | CAMERA\_FORMAT\_YUV\_420\_SP | DISPLAY\_P3 |
| HDR | HDR | CAMERA\_FORMAT\_YCRCB\_P010、  CAMERA\_FORMAT\_YCBCR\_P010 | BT2020\_HLG |

**HDR配置说明**

* 在配置预览输出流时，需要先通过接口[getSupportedFullOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedfulloutputcapability23)查询当前镜头和模式支持的完整能力，选择的预览输出格式为P010（CAMERA\_FORMAT\_YCRCB\_P010/CAMERA\_FORMAT\_YCBCR\_P010）。
* 在配置色彩空间时，需要先通过接口[getSupportedColorSpaces](../harmonyos-references/arkts-apis-camera-colormanagementquery.md#getsupportedcolorspaces12)获取当前设备所支持的色彩空间，再通过接口[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)设置色彩空间为BT2020\_HLG。具体请参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)说明。
