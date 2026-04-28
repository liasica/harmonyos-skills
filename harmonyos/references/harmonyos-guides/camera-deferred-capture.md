---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-deferred-capture
title: 分段式拍照(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 分段式拍照(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:58+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:8f1749c766fbe1c0788b49d4dd498ab2b1c2a600bfe4091b31792529afca965b
---

分段式拍照是相机的重要功能之一，即应用下发拍照任务后，系统将分多阶段上报不同质量的图片。

* 在第一阶段，系统快速上报轻量处理的图片，轻量处理的图片比全质量图低，出图速度快。应用通过回调会收到一个[PhotoAsset](../harmonyos-references/arkts-apis-photoaccesshelper-photoasset.md)对象，通过该对象可调用媒体库接口，读取图片或落盘图片。
* 在第二阶段，相机框架会根据应用的请求图片诉求或在相机进入后台时，进行图像增强处理得到全质量图，并将处理好的图片传回给媒体库，替换轻量处理的图片。

通过分段式拍照，优化了系统的拍照响应时延，从而提升用户体验。

应用开发分段式拍照主要分为以下步骤：

* 通过PhotoOutput，监听photoAssetAvailable回调，获取[photoAccessHelper](../harmonyos-references/arkts-apis-photoaccesshelper.md)的PhotoAsset对象。
* 通过PhotoAsset对象，调用媒体库相关接口，读取或落盘图片。

说明

* 分段式拍照能力由**设备**和**模式**决定，不同的设备支持的模式各异，对应分段式能力也有所差异，因此应用在切换设备或模式后分段式能力可能会发生变化。
* 应用无需主动使能分段式拍照能力，相机框架会在配流期间判断设备和模式是否支持分段式，如果支持会使能该功能。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入依赖，需要导入相机框架、媒体库、图片相关领域依赖。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 确定拍照输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的photoProfiles属性，可获取当前设备支持的拍照输出流，通过[createPhotoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法创建拍照输出流。

   ```
   1. function getPhotoOutput(cameraManager: camera.CameraManager,
   2. cameraOutputCapability: camera.CameraOutputCapability): camera.PhotoOutput | undefined {
   3. let photoProfilesArray: Array<camera.Profile> = cameraOutputCapability.photoProfiles;
   4. if (photoProfilesArray===null || photoProfilesArray===undefined) {
   5. console.error("createOutput photoProfilesArray is null!");
   6. return undefined;
   7. }
   8. let photoOutput: camera.PhotoOutput | undefined = undefined;
   9. try {
   10. if (photoProfilesArray.length > 0) {
   11. photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
   12. } else {
   13. console.error("the length of photoProfilesArray<=0!");
   14. return undefined;
   15. }
   16. } catch (error) {
   17. let err = error as BusinessError;
   18. console.error(`Failed to createPhotoOutput. error: ${err}`);
   19. }
   20. return photoOutput;
   21. }
   ```
3. 设置拍照photoAssetAvailable的回调。

   注意

   如果已经注册了photoAssetAvailable回调，并且在Session开始之后又注册了photoAvailable回调，photoAssetAvailable和photoAvailable同时注册，会导致流被重启，仅photoAssetAvailable生效。

   不建议开发者同时注册[photoAvailable](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)和[photoAssetAvailable](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoassetavailable12)。

   ```
   1. function getPhotoAccessHelper(context: Context): photoAccessHelper.PhotoAccessHelper {
   2. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
   3. return phAccessHelper;
   4. }

   6. function onPhotoOutputPhotoAssetAvailable(photoOutput: camera.PhotoOutput, context: Context): void {
   7. photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
   8. if (err) {
   9. console.error(`photoAssetAvailable error: ${err}.`);
   10. return;
   11. }
   12. console.info('photoOutPutCallBack photoAssetAvailable');
   13. // 开发者可通过photoAsset调用媒体库相关接口，自定义处理图片。
   14. // 处理方式一：调用媒体库落盘接口保存一阶段图，二阶段图就绪后媒体库会主动帮应用替换落盘图片。
   15. mediaLibSavePhoto(photoAsset, getPhotoAccessHelper(context));
   16. // 处理方式二：调用媒体库接口请求图片并注册一阶段图或二阶段图buffer回调，自定义使用。
   17. mediaLibRequestBuffer(photoAsset, context);
   18. });
   19. }

   21. async function mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
   22. phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
   23. try {
   24. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
   25. assetChangeRequest.saveCameraPhoto();
   26. await phAccessHelper.applyChanges(assetChangeRequest);
   27. console.info('apply saveCameraPhoto successfully');
   28. } catch (err) {
   29. console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
   30. }
   31. }

   33. class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
   34. onDataPrepared(data: ArrayBuffer) {
   35. if (data === undefined) {
   36. console.error('Error occurred when preparing data');
   37. return;
   38. }
   39. // 应用获取到图片buffer后可自定义处理。
   40. console.info('on image data prepared');
   41. }
   42. }

   44. async function mediaLibRequestBuffer(photoAsset: photoAccessHelper.PhotoAsset, context: Context) {
   45. let requestOptions: photoAccessHelper.RequestOptions = {
   46. // 按照业务需求配置回图模式。
   47. // FAST_MODE：仅接收一阶段低质量图回调。
   48. // HIGH_QUALITY_MODE：仅接收二阶段全质量图回调。
   49. // BALANCE_MODE：接收一阶段及二阶段图片回调。
   50. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
   51. }
   52. const handler = new MediaDataHandler();
   53. await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
   54. console.info('requestImageData successfully');
   55. }
   ```

   落盘图片参考媒体库接口：[saveCameraPhoto](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#savecameraphoto12)

   请求图片参考媒体库接口：[requestImageData](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetmanager.md#requestimagedata11) 和 [onDataPrepared](../harmonyos-references/arkts-apis-photoaccesshelper-mediaassetdatahandler.md#ondataprepared11)
4. 拍照时的会话配置及触发拍照的方式，与普通拍照相同，请参考[拍照](camera-shooting.md)的步骤4-5。

## 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍照输出流的错误。

* 通过注册固定的captureStartWithInfo回调函数获取监听拍照开始结果，photoOutput创建成功时即可监听，相机设备已经准备开始这次拍照时触发，该事件返回此次拍照的captureId。

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
* 通过注册固定的error回调函数获取监听拍照输出流的错误结果。callback返回拍照输出接口使用错误时的对应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```
  1. function onPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('error', (error: BusinessError) => {
  3. console.error(`Photo output error code: ${error.code}`);
  4. });
  5. }
  ```
