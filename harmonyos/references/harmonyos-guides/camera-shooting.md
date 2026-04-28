---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting
title: 拍照(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 拍照(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:56+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ef049c69c551cecb508db6f7500c18b879de45515065951d32da8ee9d24eff32
---

## 概述

拍照是相机的重要功能之一，拍照模块基于相机复杂的逻辑，为了保证用户拍出的照片质量，在中间步骤可以设置分辨率、闪光灯、焦距、照片质量及旋转角度等信息。

目前相机开发有两种相机拍照方案，分别是相机[分段式拍照](camera-deferred-capture.md)和相机单段式拍照（**本文将以单段式拍照为基础进行说明**）。

* 分段式拍照是指相机拍照既可以输出低质量图用作缩略图，提升用户感知拍照速度，也可以使用高质量图保证最后的成图质量达到系统相机的水平。满足了图像处理算法的需求的同时，又不会阻塞前台的拍照速度，构筑相机性能竞争力，提升用户体验。
* 单段式拍照是指在拍照过程中通过多帧融合以及多个底层算法处理之后返回一张高质量图片，所以Shot2See（用户点击拍照控件到在缩略图显示区域显示缩略图的过程）完成时延较长。此外，单段式拍照支持通过[高性能拍照](camera-shooting.md#高性能拍照)功能调整[画质优先策略](camera-shooting.md#画质优先策略)，以加快出图速度或提升图片质量。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入[Image](../harmonyos-references/arkts-apis-image-image.md)接口。获取拍照输出的数据需要用到系统提供的Image接口能力，导入Image接口的方法如下。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { camera } from '@kit.CameraKit';
   3. import { fileIo } from '@kit.CoreFileKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建拍照输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的photoProfiles属性，可获取当前设备支持的拍照输出流。通过[createPhotoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法传入支持的某一个输出流[Profile](../harmonyos-references/arkts-apis-camera-i.md#profile)创建拍照输出流。

   ```
   1. function getPhotoOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
   2. let photoProfilesArray: Array<camera.Profile> = cameraOutputCapability.photoProfiles;
   3. if (!photoProfilesArray || photoProfilesArray.length === 0) {
   4. console.error("photoProfilesArray is null or []");
   5. }
   6. let photoOutput: camera.PhotoOutput | undefined = undefined;
   7. try {
   8. photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
   9. } catch (error) {
   10. let err = error as BusinessError;
   11. console.error(`Failed to createPhotoOutput. error: ${err}`);
   12. }
   13. return photoOutput;
   14. }
   ```
3. 设置拍照[on('photoAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)的回调，并将拍照的buffer保存为图片。

   Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   如需要在图库中看到所保存的图片、视频资源，需要将其保存到媒体库，保存方式请参考：[保存媒体库资源](photoaccesshelper-savebutton.md)。

   需要在[photoOutput.on('photoAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)接口获取到buffer时，将buffer在安全控件中保存到媒体库。

   ```
   1. function setPhotoOutputCb(photoOutput: camera.PhotoOutput) {
   2. // 设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中。
   3. photoOutput.on('photoAvailable', (errCode: BusinessError, photo: camera.Photo): void => {
   4. console.info('getPhoto start');
   5. if (errCode || photo === undefined) {
   6. console.error('getPhoto failed, err: ${errCode}');
   7. return;
   8. }
   9. let imageObj: image.Image = photo.main;
   10. imageObj.getComponent(image.ComponentType.JPEG, (errCode: BusinessError, component: image.Component): void => {
   11. console.info('getComponent start');
   12. if (errCode || component === undefined) {
   13. console.error('getComponent failed');
   14. return;
   15. }
   16. let buffer: ArrayBuffer;
   17. if (component.byteBuffer) {
   18. buffer = component.byteBuffer;
   19. } else {
   20. console.error('byteBuffer is null');
   21. return;
   22. }
   23. // 如需要在图库中看到所保存的图片、视频资源，请使用用户无感的安全控件创建媒体资源。

   25. // buffer处理结束后需要释放该资源，如果未正确释放资源会导致后续拍照获取不到buffer。
   26. imageObj.release();
   27. });
   28. });
   29. }
   ```
4. 参数配置。

   配置相机的参数可以调整拍照的一些功能，包括闪光灯、变焦、焦距等。

   ```
   1. function configuringSession(photoSession: camera.PhotoSession): void {
   2. // 判断设备是否支持闪光灯。
   3. let flashStatus: boolean = false;
   4. try {
   5. flashStatus = photoSession.hasFlash();
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. console.error(`Failed to hasFlash. error: ${err}`);
   9. }
   10. console.info(`Returned with the flash light support status: ${flashStatus}`);
   11. if (flashStatus) {
   12. // 判断是否支持自动闪光灯模式。
   13. let flashModeStatus: boolean = false;
   14. try {
   15. flashModeStatus = photoSession?.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. console.error(`Failed to check whether the flash mode is supported. error: ${err}`);
   19. }
   20. if (flashModeStatus) {
   21. // 设置自动闪光灯模式。
   22. try {
   23. photoSession?.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
   24. } catch (error) {
   25. let err = error as BusinessError;
   26. console.error(`Failed to set the flash mode. error: ${err}`);
   27. }
   28. }
   29. }
   30. // 判断是否支持连续自动变焦模式。
   31. let focusModeStatus: boolean = false;
   32. try {
   33. focusModeStatus = photoSession?.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
   34. } catch (error) {
   35. let err = error as BusinessError;
   36. console.error(`Failed to check whether the focus mode is supported. error: ${err}`);
   37. }
   38. if (focusModeStatus) {
   39. // 设置连续自动变焦模式。
   40. try {
   41. photoSession?.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
   42. } catch (error) {
   43. let err = error as BusinessError;
   44. console.error(`Failed to set the focus mode. error: ${err}`);
   45. }
   46. }
   47. // 获取相机支持的可变焦距比范围。
   48. let zoomRatioRange: Array<number> = [];
   49. try {
   50. zoomRatioRange = photoSession?.getZoomRatioRange();
   51. } catch (error) {
   52. let err = error as BusinessError;
   53. console.error(`Failed to get the zoom ratio range. error: ${err}`);
   54. }
   55. if (zoomRatioRange.length <= 0 ) {
   56. return;
   57. }
   58. // 设置可变焦距比。
   59. try {
   60. photoSession?.setZoomRatio(zoomRatioRange[0]);
   61. } catch (error) {
   62. let err = error as BusinessError;
   63. console.error(`Failed to set the zoom ratio value. error: ${err}`);
   64. }
   65. }
   ```
5. 触发拍照。

   通过photoOutput的[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-2)方法，执行拍照任务。该方法有两个参数，第一个参数为拍照设置参数的setting，setting中可以设置照片的质量和旋转角度，第二参数为回调函数。

   获取拍照旋转角度的方法为，通过[PhotoOutput](../harmonyos-references/arkts-apis-camera-photooutput.md)中的[getPhotoRotation](../harmonyos-references/arkts-apis-camera-photooutput.md#getphotorotation12)方法获取rotation实际的值。

   说明

   图片地理位置信息[Location](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)，使用方法可参考[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-3)示例。

   ```
   1. function capture(captureLocation: camera.Location, photoOutput: camera.PhotoOutput): void {
   2. let settings: camera.PhotoCaptureSetting = {
   3. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,  // 设置图片质量高。
   4. rotation: camera.ImageRotation.ROTATION_0,  // 设置图片旋转角度的camera.ImageRotation.ROTATION_0是通过说明中获取拍照角度的getPhotoRotation方法获取的值进行设置。
   5. location: captureLocation,  // 设置图片地理位置。
   6. mirror: false  // 设置镜像使能开关(默认关)。
   7. };
   8. try {
   9. photoOutput.capture(settings, (err: BusinessError) => {
   10. if (err) {
   11. console.error(`Failed to capture the photo. error: ${err}`);
   12. return;
   13. }
   14. console.info('Callback invoked to indicate the photo capture request success.');
   15. });
   16. } catch (error) {
   17. console.error(`capture call failed. error: ${error}`);
   18. }
   19. }
   ```

## 高性能拍照

从API version 21开始支持高性能拍照功能，即在进行单段式拍照时设置明确的[画质优先策略](camera-shooting.md#画质优先策略)。

单段式拍照的体验主要由出图速度和最终图片质量衡量。因此，为满足开发者在不同场景下的差异化需求，对这两项指标的侧重也不同。例如，街头抓拍要求快速捕捉瞬间，而风景或人像拍摄则更追求极致的画质。

注意

仅单段式拍照支持设置画质优先策略。若在分段式拍照中设置画质优先策略，该设置将无效。

### 画质优先策略

在使用单段式拍照时，支持设置速度优先和画质优先两种画质优先策略类型，并且分别对应着不同的[PhotoQualityPrioritization](../harmonyos-references/arkts-apis-camera-e.md#photoqualityprioritization21)枚举类型。

* [SPEED](../harmonyos-references/arkts-apis-camera-e.md#photoqualityprioritization21)对应着速度优先，表示降低画质来提升拍照的速度。如果开发者在进行单段式拍照时没有设置明确的画质优先策略，**单段式拍照就默认为速度优先状态**。
* [HIGH\_QUALITY](../harmonyos-references/arkts-apis-camera-e.md#photoqualityprioritization21)对应着画质优先，表示通过较长的耗时来得到画质更高的图片。

### 如何正确设置画质优先策略

为了正确的在单段式拍照中设置画质优先策略，高性能拍照功能提供了如下两个接口：

* [isPhotoQualityPrioritizationSupported](../harmonyos-references/arkts-apis-camera-photooutput.md#isphotoqualityprioritizationsupported21)：查询当前设备是否支持指定的画质优先策略。返回true表示支持，返回false表示不支持。在进行设置画质优先策略之前，必须先查询将要设置的画质优先策略在当前设备上是否可用。
* [setPhotoQualityPrioritization](../harmonyos-references/arkts-apis-camera-photooutput.md#setphotoqualityprioritization21)：画质优先策略设置接口，通过该接口设置对应的画质优先策略，实现高性能拍照。

### 开发步骤

高性能拍照相关接口需要在[会话管理(ArkTS)](camera-session-management.md)流程的使能步骤中进行调用。

具体调用时机如下：

* 在[会话管理(ArkTS)](camera-session-management.md)流程的使能步骤中的[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)结束之后进行调用。

  ```
  1. async function startSession(videoSession: camera.VideoSession, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput): Promise<void> {
  2. try {
  3. videoSession.addInput(cameraInput);
  4. } catch (error) {
  5. let err = error as BusinessError;
  6. console.error(`Failed to addInput. error: ${err.code}`);
  7. }
  8. let canAddPreviewOutput : boolean = false;
  9. try {
  10. canAddPreviewOutput = videoSession.canAddOutput(previewOutput);
  11. } catch (error) {
  12. let err = error as BusinessError;
  13. console.error(`Failed to add previewOutput. error: ${err.code}`);
  14. }
  15. if (!canAddPreviewOutput) {
  16. console.error(`Failed to add preview output.`);
  17. return;
  18. }
  19. try {
  20. videoSession.addOutput(previewOutput);
  21. } catch (error) {
  22. let err = error as BusinessError;
  23. console.error(`Failed to add previewOutput. error: ${err.code}`);
  24. }
  25. let canAddPhotoOutput : boolean = false
  26. try {
  27. canAddPhotoOutput = videoSession.canAddOutput(photoOutput);
  28. } catch (error) {
  29. let err = error as BusinessError;
  30. console.error(`Failed to add photoOutput error: ${err.code}`);
  31. }
  32. if (!canAddPhotoOutput) {
  33. console.error(`Failed to add photo output.`);
  34. return;
  35. }
  36. try {
  37. videoSession.addOutput(photoOutput);
  38. } catch (error) {
  39. let err = error as BusinessError;
  40. console.error(`Failed to add photoOutput. error: ${err.code}`);
  41. }
  42. try {
  43. await videoSession.commitConfig();
  44. } catch (error) {
  45. let err = error as BusinessError;
  46. console.error(`Failed to commitConfig. error: ${err.code}`);
  47. return;
  48. }

  50. try {
  51. await videoSession.start();
  52. } catch (error) {
  53. let err = error as BusinessError;
  54. console.error(`Failed to start. error: ${err.code}`);
  55. }
  56. modeSwitchToHigh(videoSession, photoOutput);
  57. }

  59. async function modeSwitchToHigh(videoSession: camera.VideoSession, photoOutput: camera.PhotoOutput): Promise<void> {
  60. try {
  61. if (videoSession) {
  62. let quality: camera.PhotoQualityPrioritization = camera.PhotoQualityPrioritization.HIGH_QUALITY;
  63. let isSupported = false;
  64. isSupported = photoOutput.isPhotoQualityPrioritizationSupported(quality);
  65. if (isSupported) {
  66. photoOutput.setPhotoQualityPrioritization(quality);
  67. } else {
  68. console.error(`session is not supported`);
  69. }
  70. } else {
  71. console.error(`session is null`);
  72. }
  73. } catch {
  74. console.error(`catch error`);
  75. }
  76. }
  ```
* 在[会话管理(ArkTS)](camera-session-management.md)流程的使能步骤中的[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)之前调用。

  ```
  1. async function startSession(videoSession: camera.VideoSession, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput): Promise<void> {
  2. try {
  3. videoSession.addInput(cameraInput);
  4. } catch (error) {
  5. let err = error as BusinessError;
  6. console.error(`Failed to addInput. error: ${err.code}`);
  7. }
  8. let canAddPreviewOutput : boolean = false;
  9. try {
  10. canAddPreviewOutput = videoSession.canAddOutput(previewOutput);
  11. } catch (error) {
  12. let err = error as BusinessError;
  13. console.error(`Failed to add previewOutput. error: ${err.code}`);
  14. }
  15. if (!canAddPreviewOutput) {
  16. console.error(`Failed to add preview output.`);
  17. return;
  18. }
  19. try {
  20. videoSession.addOutput(previewOutput);
  21. } catch (error) {
  22. let err = error as BusinessError;
  23. console.error(`Failed to add previewOutput. error: ${err.code}`);
  24. }
  25. let canAddPhotoOutput : boolean = false
  26. try {
  27. canAddPhotoOutput = videoSession.canAddOutput(photoOutput);
  28. } catch (error) {
  29. let err = error as BusinessError;
  30. console.error(`Failed to add photoOutput error: ${err.code}`);
  31. }
  32. if (!canAddPhotoOutput) {
  33. console.error(`Failed to add photo output.`);
  34. return;
  35. }
  36. try {
  37. videoSession.addOutput(photoOutput);
  38. } catch (error) {
  39. let err = error as BusinessError;
  40. console.error(`Failed to add photoOutput. error: ${err.code}`);
  41. }
  42. modeSwitchToHigh(videoSession, photoOutput);
  43. try {
  44. await videoSession.commitConfig();
  45. } catch (error) {
  46. let err = error as BusinessError;
  47. console.error(`Failed to commitConfig. error: ${err.code}`);
  48. return;
  49. }

  51. try {
  52. await videoSession.start();
  53. } catch (error) {
  54. let err = error as BusinessError;
  55. console.error(`Failed to start. error: ${err.code}`);
  56. }
  57. }

  59. async function modeSwitchToHigh(videoSession: camera.VideoSession, photoOutput: camera.PhotoOutput): Promise<void> {
  60. try {
  61. if (videoSession) {
  62. let quality: camera.PhotoQualityPrioritization = camera.PhotoQualityPrioritization.HIGH_QUALITY;
  63. let isSupported = false;
  64. isSupported = photoOutput.isPhotoQualityPrioritizationSupported(quality);
  65. if (isSupported) {
  66. photoOutput.setPhotoQualityPrioritization(quality);
  67. } else {
  68. console.error(`session is not supported`);
  69. }
  70. } else {
  71. console.error(`session is null`);
  72. }
  73. } catch {
  74. console.error(`catch error`);
  75. }
  76. }
  ```

## 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍照输出流的错误。

* 通过注册固定的captureStart回调函数获取监听拍照开始结果，photoOutput创建成功时即可监听，相机设备已经准备开始这次拍照时触发，该事件返回此次拍照的captureId。

  ```
  1. function onPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('captureStartWithInfo', (err: BusinessError, captureStartInfo: camera.CaptureStartInfo) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info(`photo capture started, captureId : ${captureStartInfo.captureId}`);
  7. });
  8. }
  ```
* 通过注册固定的captureEnd回调函数获取监听拍照结束结果，photoOutput创建成功时即可监听，该事件返回结果为拍照完全结束后的相关信息[CaptureEndInfo](../harmonyos-references/arkts-apis-camera-i.md#captureendinfo)。

  ```
  1. function onPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('captureEnd', (err: BusinessError, captureEndInfo: camera.CaptureEndInfo) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info(`photo capture end, captureId : ${captureEndInfo.captureId}`);
  7. console.info(`frameCount : ${captureEndInfo.frameCount}`);
  8. });
  9. }
  ```
* 通过注册固定的captureReady回调函数获取监听可拍下一张结果，photoOutput创建成功时即可监听，当下一张可拍时触发，该事件返回结果为下一张可拍的相关信息。

  ```
  1. function onPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('captureReady', (err: BusinessError) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info(`photo capture ready`);
  7. });
  8. }
  ```
* 通过注册固定的error回调函数获取监听拍照输出流的错误结果。回调返回拍照输出接口使用错误时的对应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```
  1. function onPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('error', (error: BusinessError) => {
  3. console.error(`Photo output error code: ${error.code}`);
  4. });
  5. }
  ```
