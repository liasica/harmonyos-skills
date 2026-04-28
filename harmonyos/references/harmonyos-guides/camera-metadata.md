---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-metadata
title: 元数据(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 元数据(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:57+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:5870a783850bf6873db10550b687e3046a2a647efe963971f481f7351b3e4e38
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

元数据（Metadata）是对相机返回的图像信息的描述和上下文。针对图像信息，提供更详细的数据，如照片或视频中，识别人像的取景框坐标的信息等。

Metadata主要是通过一个TAG（Key），去找对应的Data，用于传递参数和配置信息，减少内存拷贝操作。

## 适用场景

检测图片中的人脸，返回高精度的人脸矩形框坐标。应用可基于人脸定位结果，灵活集成后处理算法，将其应用于多样化场景。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入相关接口，导入方法如下。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的supportedMetadataObjectTypes属性，获取当前设备支持的元数据类型，并通过[createMetadataOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createmetadataoutput)方法创建元数据输出流。

   ```
   1. function getMetadataOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability): camera.MetadataOutput | undefined {
   2. let metadataObjectTypes: Array<camera.MetadataObjectType> = cameraOutputCapability.supportedMetadataObjectTypes;
   3. let metadataOutput: camera.MetadataOutput | undefined = undefined;
   4. try {
   5. metadataOutput = cameraManager.createMetadataOutput(metadataObjectTypes);
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. console.error(`Failed to createMetadataOutput, error code: ${err.code}`);
   9. }
   10. return metadataOutput;
   11. }
   ```
3. 调用[Session.start](../harmonyos-references/arkts-apis-camera-session.md#start11)方法开启metadata数据输出，再通过监听事件metadataObjectsAvailable回调拿到数据，接口调用失败时，会返回相应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

   previewOutput获取方式请参考[相机预览开发步骤](camera-preview.md#开发步骤)。

   ```
   1. async function startMetadataOutput(previewOutput: camera.PreviewOutput, metadataOutput: camera.MetadataOutput, cameraManager: camera.CameraManager): Promise<void> {
   2. let cameraArray: Array<camera.CameraDevice> = [];
   3. try {
   4. cameraArray = cameraManager.getSupportedCameras();
   5. if (cameraArray.length == 0) {
   6. console.error('no camera.');
   7. return;
   8. }
   9. // 示例代码默认选择第一个镜头，实际开发需根据所需镜头。
   10. const cameraDevice: camera.CameraDevice = cameraArray[0];
   11. // 获取支持的模式类型。
   12. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraDevice);
   13. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
   14. if (!isSupportPhotoMode) {
   15. console.error('photo mode not support');
   16. return;
   17. }
   18. let cameraInput: camera.CameraInput | undefined = undefined;
   19. cameraInput = cameraManager.createCameraInput(cameraDevice);
   20. if (cameraInput === undefined) {
   21. console.error('cameraInput is undefined');
   22. return;
   23. }
   24. // 打开相机。
   25. await cameraInput.open();
   26. let session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
   27. if (!session) {
   28. console.error('session is null');
   29. return;
   30. }
   31. let photoSession: camera.PhotoSession = session as camera.PhotoSession;
   32. photoSession.beginConfig();
   33. photoSession.addInput(cameraInput);
   34. photoSession.addOutput(previewOutput);
   35. photoSession.addOutput(metadataOutput);
   36. await photoSession.commitConfig();
   37. await photoSession.start();
   38. } catch (error) {
   39. console.error('startMetadataOutput call failed');
   40. }
   41. }
   ```
4. 调用[Session.stop](../harmonyos-references/arkts-apis-camera-session.md#stop11)方法停止输出metadata数据，接口调用失败会返回相应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

   ```
   1. function stopMetadataOutput(session: camera.Session): void {
   2. session.stop().then(() => {
   3. console.info('Callback returned with session stopped.');
   4. }).catch((err: BusinessError) => {
   5. console.error(`Failed to session stop, error code: ${err.code}`);
   6. });
   7. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听metadata数据以及输出流的状态。

* 通过注册监听获取metadata对象，监听事件固定为metadataObjectsAvailable。检测到有效metadata数据时，callback返回相应的metadata数据信息，metadataOutput创建成功时可监听。

  ```
  1. function onMetadataObjectsAvailable(metadataOutput: camera.MetadataOutput): void {
  2. metadataOutput.on('metadataObjectsAvailable', (err: BusinessError, metadataObjectArr: Array<camera.MetadataObject>) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info('metadata output metadataObjectsAvailable');
  7. });
  8. }
  ```

  说明

  当前的元数据类型仅支持人脸检测（FACE\_DETECTION）功能。元数据信息对象为识别到的人脸区域的矩形信息（Rect），包含矩形区域的左上角x坐标、y坐标和矩形的宽高数据。
* 通过注册回调函数，获取监听metadata流的错误结果，callback返回metadata输出接口使用错误时返回的错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```
  1. function onMetadataError(metadataOutput: camera.MetadataOutput): void {
  2. metadataOutput.on('error', (metadataOutputError: BusinessError) => {
  3. console.error(`Metadata output error code: ${metadataOutputError.code}`);
  4. });
  5. }
  ```
