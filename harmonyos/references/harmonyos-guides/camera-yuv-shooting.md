---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-yuv-shooting
title: YUV拍照(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > YUV拍照(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:02+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c2ddff9a5e3f6e581818376ab50d498608c1b2e6ec1d707a50f361ad623e5e1c
---

从API version 23开始，相机框架提供YUV格式图片拍照能力。与普通拍照相比，YUV拍照获取到的是未经过编码的图像数据，完整保留了传感器捕获的原始亮度和色度信息，适用于视频编码或专业处理。同时，拍摄过程会产生更高的能耗开销，保存会占用更多的存储空间。

## 开发步骤

详细的相机功能API说明请参考Camera模块描述[OH\_Camera](../harmonyos-references/arkts-apis-camera.md)。

1. 导入依赖模块。

   获取拍照输出的数据需要用到系统提供的image、dataSharePredicates、photoAccessHelper接口能力，方法如下。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { camera } from '@kit.CameraKit';
   3. import { dataSharePredicates } from '@kit.ArkData';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { image } from '@kit.ImageKit';
   6. import { photoAccessHelper} from '@kit.MediaLibraryKit';
   ```
2. 获取相机设备完整输出能力。

   通过[getSupportedFullOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedfulloutputcapability23)方法，获取当前相机设备支持的所有输出流的能力，包含预览流、拍照流、录像流等。输出流在[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的各个profile字段中，其中拍照流支持YUV格式。

   ```
   1. function getFullOutputCapability(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice, sceneMode: camera.SceneMode): camera.CameraOutputCapability | undefined {
   2. let cameraOutputCapability = cameraManager.getSupportedFullOutputCapability(cameraDevice, sceneMode);
   3. if (!cameraOutputCapability) {
   4. console.error("cameraManager.getSupportedFullOutputCapability error");
   5. return undefined;
   6. }
   7. return cameraOutputCapability;
   8. }
   ```
3. 创建拍照输出流。

   通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的photoProfiles属性，可获取当前设备支持的拍照输出流。

   通过[createPhotoOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createphotooutput11)方法传入支持的某一个输出流[Profile](../harmonyos-references/arkts-apis-camera-i.md#profile)，创建拍照输出流。

   通过[getSupportedFullOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedfulloutputcapability23)获取相机支持的完整输出能力cameraOutputCapability，参考步骤2。在cameraOutputCapability的photoProfiles中选择支持YUV格式的Profile，作为创建拍照输出流的参数photoProfile。

   ```
   1. function getPhotoOutput(cameraManager: camera.CameraManager, photoProfile: camera.Profile): camera.PhotoOutput | undefined {
   2. // 创建拍照输出流。
   3. let photoOutput: camera.PhotoOutput | undefined = undefined;
   4. try {
   5. photoOutput = cameraManager.createPhotoOutput(photoProfile);
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. console.error("Failed to createPhotoOutput. error: ${err}");
   9. }
   10. return photoOutput;
   11. }
   ```
4. 设置拍照输出流的回调。

   设置单段式拍照[onCapturePhotoAvailable](../harmonyos-references/arkts-apis-camera-photooutput.md#oncapturephotoavailable23)或分段式拍照[on('photoAssetAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoassetavailable12)的回调，并将拍照的pixelMap数据保存为图片。如果应用需要快速得到回图，推荐使用分段式拍照回调。

   Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   如果需要在图库中看到所保存的图片、视频资源，需要先将其保存到媒体库，保存方式请参考：[保存媒体库资源](photoaccesshelper-savebutton.md)。

   如果需要在[onCapturePhotoAvailable](../harmonyos-references/arkts-apis-camera-photooutput.md#oncapturephotoavailable23)接口获取到buffer，先将[PixelMap](../harmonyos-references/arkts-apis-image-pixelmap.md)数据在安全控件中保存到媒体库。

   * **单段式拍照（onCapturePhotoAvailable）开发流程**：

     + 在会话[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11-1)前注册单段式拍照回调。
     + 在单段式拍照回调函数中获取图片信息，解析出pixelMap数据，做自定义业务处理。
     + 将处理完的pixelMap通过回调回传，做图片显示或通过安全控件写文件保存图片。
     + 使用完后解注册单段式拍照回调函数。

     ```
     1. // 单段式拍照回调函数。
     2. function setPhotoOutputSingleCb(context: Context, photoOutput: camera.PhotoOutput)
     3. {
     4. // 设置回调之后，调用photoOutput的capture方法，就会将拍照的pixelMap回传到回调中。
     5. photoOutput.onCapturePhotoAvailable(async (capturePhoto: camera.CapturePhoto): Promise<void> => {
     6. console.info("getPhoto start");
     7. if (capturePhoto === undefined) {
     8. console.error("getPhoto failed, capturePhoto is null or undefined");
     9. return;
     10. }
     11. let pictureObj: image.Picture = capturePhoto.main as image.Picture;
     12. if (pictureObj === undefined) {
     13. console.error("getPhoto failed, pictureObj is null or undefined");
     14. return;
     15. }
     16. // 获取拍照的主图的pixelMap。
     17. let mainPixelMap: image.PixelMap = pictureObj.getMainPixelmap();
     18. if (mainPixelMap === undefined) {
     19. console.error("getPhoto failed, mainPixelMap is null or undefined");
     20. return;
     21. }
     22. // 对pixelMap中的数据做编码处理。
     23. const imagePackerApi = image.createImagePacker();
     24. let packOpts: image.PackingOption = {format: 'image/jpeg', quality: 95};
     25. const path: string = context.cacheDir + '/pixel_map.jpg';
     26. let srcFileUri: string = '';
     27. let file = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
     28. try {
     29. await imagePackerApi.packToFile(mainPixelMap, file.fd, packOpts);
     30. srcFileUri = file.path;
     31. } catch (error) {
     32. console.error("Failed to pack the pixelMap to file. And the errorcode: ${error.code} ,error.message: ${error.message}");
     33. }
     34. // 对图片做保存操作。
     35. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
     36. try {
     37. // 指定待保存到媒体库的位于应用沙箱的图片uri。
     38. let srcFileUris: string[] = [
     39. srcFileUri
     40. ];
     41. // 指定待保存照片的创建选项，包括文件后缀和照片类型，标题和照片子类型可选。
     42. let photoCreationConfigs: photoAccessHelper.PhotoCreationConfig[] = [
     43. {
     44. title: 'test', // 可选。
     45. fileNameExtension: 'jpg',
     46. photoType: photoAccessHelper.PhotoType.IMAGE,
     47. subtype: photoAccessHelper.PhotoSubtype.DEFAULT, // 可选。
     48. }
     49. ];
     50. // 基于弹窗授权的方式获取媒体库的目标uri。
     51. let desFileUris: string[] = await phAccessHelper.showAssetsCreationDialog(srcFileUris, photoCreationConfigs);
     52. // 将来源于应用沙箱的照片内容写入媒体库的目标uri。
     53. let desFile: fileIo.File = await fileIo.open(desFileUris[0], fileIo.OpenMode.WRITE_ONLY);
     54. let srcFile: fileIo.File = await fileIo.open(srcFileUri, fileIo.OpenMode.READ_ONLY);
     55. await fileIo.copyFile(srcFile.fd, desFile.fd);
     56. fileIo.closeSync(srcFile);
     57. fileIo.closeSync(desFile);
     58. console.info("create asset by dialog successfully");
     59. } catch (err) {
     60. console.error("failed to create asset by dialog successfully errCode is: ${err.code}, ${err.message}");
     61. }
     62. // 从PixelMap中获取元数据。
     63. let metadataType: image.MetadataType = image.MetadataType.EXIF_METADATA;
     64. let pictureMetadata: Promise<image.Metadata>  = pictureObj.getMetadata(metadataType);
     65. if (pictureMetadata != undefined) {
     66. console.info("Get picture metadata with EXIF_METADATA successfully");
     67. } else {
     68. console.error("Get picture metadata with EXIF_METADATA failed");
     69. }
     70. // 释放资源。
     71. mainPixelMap.release();
     72. pictureObj.release();
     73. });
     74. }
     ```
   * **分段式拍照（PhotoAvailable）开发流程**：

     + 在会话[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11-1)前注册分段式拍照回调。
     + 在分段式拍照回调函数中获取图片信息，解析出pixelMap数据，做自定义业务处理。
     + 将处理完的pixelMap回传，做图片显示或通过安全控件写文件保存图片。
     + 调用[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-2)拍照后，需要及时调用[saveCameraPhoto](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#savecameraphoto12)保存图片或[discardCameraPhoto](../harmonyos-references/kts-apis-photoaccesshelper-mediaassetchangerequest.md#discardcameraphoto12)取消保存图片，否则会影响后续图片的拍摄。
     + 使用完后解注册分段式拍照回调函数。

     ```
     1. // 分段式拍照回调函数。
     2. function setPhotoOutputDefferCb(photoOutput: camera.PhotoOutput, context: Context, callback: (pixelMap: image.PixelMap, uri: string) => void)
     3. {
     4. photoOutput.on('photoAssetAvailable', async (_err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): Promise<void> => {
     5. try {
     6. console.info("On photoAssetAvailable callback uri: ${photoAsset.uri}");
     7. let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
     8. // 保存图片。
     9. try {
     10. // 创建媒体资产变更请求。
     11. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest = new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
     12. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
     13. console.info("Start to save camera photo");
     14. // 保存相机拍摄的照片。
     15. await assetChangeRequest.saveCameraPhoto(photoAccessHelper.ImageFileType.JPEG);
     16. // 提交媒体变更请求。
     17. await phAccessHelper.applyChanges(assetChangeRequest);
     18. console.info("Save camera photo end");
     19. await phAccessHelper.release();
     20. } catch (error) {
     21. console.error("On photoAssetAvailable save camera photo error:  ${error.code}, ${error.message}");
     22. }
     23. // 获取图片pixelmap信息。
     24. try {
     25. class MediaDataHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
     26. onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
     27. if (data != undefined) {
     28. console.info("On photoAssetAvailable callback data is not undefined");
     29. let pixelMap: image.PixelMap = data.getMainPixelmap();
     30. pixelMap.getImageInfo().then((info) => {
     31. console.info("On photoAssetAvailable pixelMap.width: " + info.size.width + ", pixelMap.height: " +
     32. info.size.height + ", pixelMap.pixelFormat: " + info.pixelFormat);
     33. })
     34. callback(pixelMap, photoAsset.uri);
     35. } else if (data === undefined && imageSource != undefined) {
     36. console.info("On photoAssetAvailable callback data is undefined, and imageSource is not undefined");
     37. imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
     38. callback(pixelMap, photoAsset.uri);
     39. }).catch((error: BusinessError) => {
     40. console.error("On photoAssetAvailable callback createPixelMap failed, error: ${error.message}");
     41. })
     42. } else {
     43. console.error("On photoAssetAvailable callback data and imageSource are both undefined");
     44. return;
     45. }
     46. }
     47. }
     48. // 创建数据共享谓词。
     49. let predicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
     50. // 配置媒体资产检索条件。
     51. let fetchOptions: photoAccessHelper.FetchOptions = {
     52. fetchColumns: [],
     53. predicates: predicates,
     54. };
     55. // 配置请求策略为平衡模式。
     56. let requestOptions: photoAccessHelper.RequestOptions = {
     57. deliveryMode: photoAccessHelper.DeliveryMode.BALANCE_MODE
     58. };
     59. const handler = new MediaDataHandler();
     60. await photoAccessHelper.MediaAssetManager.quickRequestImage(context, photoAsset, requestOptions, handler);
     61. console.info("On photoAssetAvailable callback end");
     62. } catch (error) {
     63. console.error("On photoAssetAvailable quickRequest error:  ${error.code}, ${error.message}");
     64. }
     65. } catch (error) {
     66. console.error("On photoAssetAvailable callback error:  ${error.code}, ${error.message}");
     67. }
     68. });
     69. console.info("Set photoAssetAvailable callback end");
     70. }
     ```
5. 触发拍照。

   通过photoOutput的[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-2)方法，执行拍照任务。该方法有两个参数，第一个参数为拍照设置setting，setting中可以设置图片质量，图片旋转角度等信息。第二参数为异步回调函数，用于获取结果。接口调用失败会返回相应错误码。

   通过PhotoOutput中的[getPhotoRotation](../harmonyos-references/arkts-apis-camera-photooutput.md#getphotorotation12)方法，可以获取拍照旋转角度。

   通过geoLocationManager中的[geoLocationManager.getCurrentLocation](../harmonyos-references/js-apis-geolocationmanager.md#geolocationmanagergetcurrentlocation)方法，可以获取图片地理位置信息。使用方法可参考[capture](../harmonyos-references/arkts-apis-camera-photooutput.md#capture-3)示例。

   ```
   1. function capture(captureLocation: camera.Location, photoOutput: camera.PhotoOutput): void {
   2. let settings: camera.PhotoCaptureSetting = {
   3. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,  // 设置图片质量为高质量。
   4. rotation: camera.ImageRotation.ROTATION_0,  // 设置图片旋转角度0度。
   5. location: captureLocation,  // 设置图片地理位置。
   6. mirror: false  // 设置镜像使能开关（默认关）。
   7. };
   8. try {
   9. photoOutput.capture(settings, (err: BusinessError) => {
   10. if (err) {
   11. console.error("Failed to capture the photo. error: ${err}");
   12. return;
   13. }
   14. console.info("Callback invoked to indicate the photo capture request success.");
   15. });
   16. } catch (error) {
   17. console.error("capture call failed. error: ${error}");
   18. }
   19. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听拍照输出流状态，包括拍照流开始、拍照帧的开始与结束、拍摄下一张图片是否就绪、拍照输出流的错误等。

* 通过注册固定的captureStart回调函数监听拍照开始结果，当photoOutput创建成功时，即可监听。在相机设备准备开始当前拍照时触发，该事件返回此次拍照的captureId。

  ```
  1. function onPhotoOutputCaptureStart(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('captureStartWithInfo', (err: BusinessError, captureStartInfo: camera.CaptureStartInfo) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info("photo capture started, captureId : ${captureStartInfo.captureId}");
  7. });
  8. }
  ```
* 通过注册固定的captureEnd回调函数监听拍照结束结果，当photoOutput创建成功时，即可监听。该事件返回结果为拍照完全结束后的相关信息[CaptureEndInfo](../harmonyos-references/arkts-apis-camera-i.md#captureendinfo)。

  ```
  1. function onPhotoOutputCaptureEnd(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('captureEnd', (err: BusinessError, captureEndInfo: camera.CaptureEndInfo) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info("photo capture end, captureId : ${captureEndInfo.captureId}");
  7. console.info("frameCount : ${captureEndInfo.frameCount}");
  8. });
  9. }
  ```
* 通过注册固定的captureReady回调函数获取监听能否继续拍摄下一张的结果，当photoOutput创建成功时，即可监听。当下一张可拍时触发，该事件返回结果为下一张可拍的相关信息。

  ```
  1. function onPhotoOutputCaptureReady(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('captureReady', (err: BusinessError) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info("photo capture ready");
  7. });
  8. }
  ```
* 通过注册固定的error回调函数获取监听拍照输出流的错误结果。回调返回拍照输出接口使用错误时的对应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```
  1. function onPhotoOutputError(photoOutput: camera.PhotoOutput): void {
  2. photoOutput.on('error', (error: BusinessError) => {
  3. console.error("Photo output error code: ${error.code}");
  4. });
  5. }
  ```
