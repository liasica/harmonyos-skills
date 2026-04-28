---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-concurrent-open
title: 多摄同开(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 多摄同开(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:03+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f85f903a181281d6ad78cdc7cf22b5443f1ebcea4a174477b7a0ac12a3925309
---

从API version 18开始支持多摄同开，即应用同时开启前置/后置相机进行预览和录像（前置/后置相机同时拍照功能待开放）。

说明

由于多摄同开需要前置/后置相机同时运行，所以对于相机功能有较大限制。当前版本仅支持以下七项基础功能，请勿对多摄同开开启的相机进行超出以下七种基础功能范围之外的查询、设置和使能。

1. 闪光灯。
2. 曝光。
3. 变焦。
4. 曝光补偿。
5. 对焦。
6. 防抖。
7. 色彩空间。

## 开发步骤

详细的API说明请参考[Camera](../harmonyos-references/arkts-apis-camera.md)。

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

1. 需要导入相机框架、媒体库、图片等相关领域依赖。

   ```
   1. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   2. import { camera } from '@kit.CameraKit';
   3. import { media } from '@kit.MediaKit';
   4. import { fileIo } from '@kit.CoreFileKit';
   5. import { common } from '@kit.AbilityKit';
   6. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 通过[getCameraDevice](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameradevice18)获取对应的前置和后置相机。如果接口返回undefined，基于示例中的配置信息，表示当前设备不支持指定位置（前置/后置）的默认类型相机，无法实现多摄同开功能。

   ```
   1. function getSupportedCamerasFn(cameraManager: camera.CameraManager)
   2. {
   3. let cameras = cameraManager.getSupportedCameras();

   5. // 如果相机数量少于2，说明只存在单侧相机，返回。
   6. if (cameras.length < 2) {
   7. return;
   8. }

   10. // 获取逻辑后置和逻辑前置。
   11. let curCameraDeviceBack = cameraManager.getCameraDevice(camera.CameraPosition.CAMERA_POSITION_BACK, camera.CameraType.CAMERA_TYPE_DEFAULT);
   12. let curCameraDeviceFront = cameraManager.getCameraDevice(camera.CameraPosition.CAMERA_POSITION_FRONT, camera.CameraType.CAMERA_TYPE_DEFAULT);
   13. }
   ```
3. 获取对应的并发能力集。通过[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)获取相机的输出并发能力信息数组[CameraConcurrentInfo](../harmonyos-references/arkts-apis-camera-i.md#cameraconcurrentinfo18)，数组内部包含相机在对应并发模式下支持的模式和输出能力，**在多摄同开场景下设置的模式和输出能力必须在并发能力集的范围之内**。若[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)接口返回空数组，则表明当前设备不支持并发功能。

   ```
   1. function getSupportedOutputCapabilityFn(cameraManager: camera.CameraManager, curCameraDeviceFront: camera.CameraDevice, curCameraDeviceBack: camera.CameraDevice)
   2. {
   3. // 检查当前相机是否支持拍照模式，获取原始能力集。
   4. let sceneModes = cameraManager.getSupportedSceneModes(curCameraDeviceFront);
   5. if (sceneModes === undefined) {
   6. return;
   7. }
   8. let isSupported = sceneModes.findIndex((sceneMode: camera.SceneMode) => {
   9. return sceneMode === camera.SceneMode.NORMAL_PHOTO;
   10. });
   11. if (!isSupported) {
   12. return;
   13. }
   14. let cameraOutputCapability = cameraManager.getSupportedOutputCapability(curCameraDeviceFront, camera.SceneMode.NORMAL_PHOTO);

   16. let deviceArray: Array<camera.CameraDevice> = [curCameraDeviceFront, curCameraDeviceBack];

   18. // 获取并发能力集。
   19. let concurrentInfo: Array<camera.CameraConcurrentInfo> = cameraManager.getCameraConcurrentInfos(deviceArray);

   21. if (concurrentInfo.length === 0) {
   22. return;
   23. }

   25. // 用并发能力集替换原始能力集。
   26. for (let i = 0; i < concurrentInfo.length; i++) {
   27. if (concurrentInfo[i].device.cameraPosition == camera.CameraPosition.CAMERA_POSITION_FRONT) {
   28. cameraOutputCapability = concurrentInfo[i].outputCapabilities[0];
   29. break;
   30. }
   31. }
   32. }
   ```
4. 确定预览输出流。

   ```
   1. function getPreviewOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability, surfaceId: string)
   2. {
   3. // 此处创建预览输出流以format：1003，size：1920*1080的previewProfile为例。
   4. let previewProfileObj: camera.Profile = {
   5. format: 1003,
   6. size: {
   7. width: 1920,
   8. height: 1080
   9. }
   10. };
   11. // 查询对应previewProfile是否存在，对应的previewProfile必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
   12. let previewProfiles = cameraOutputCapability.previewProfiles;
   13. if (previewProfiles.length < 1) {
   14. return;
   15. }
   16. let index = previewProfiles.findIndex((previewProfile: camera.Profile) => {
   17. return previewProfile.size.width === previewProfileObj.size.width &&
   18. previewProfile.size.height === previewProfileObj.size.height &&
   19. previewProfile.format === previewProfileObj.format;
   20. });
   21. if (index === -1) {
   22. return;
   23. }

   25. // 创建previewOutput输出对象。
   26. let previewOutput = cameraManager.createPreviewOutput(previewProfileObj, surfaceId);
   27. if (previewOutput === undefined) {
   28. return;
   29. }
   30. }
   ```
5. 确定拍照输出流。

   ```
   1. function getPhotoOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability)
   2. {
   3. // 此处创建拍照输出流以format：2000，size：1920*1080的photoProfile为例。
   4. let photoProfileObj: camera.Profile = {
   5. format: 2000,
   6. size: {
   7. width: 1920,
   8. height: 1080
   9. }
   10. };
   11. // 查询对应photoProfile是否存在，对应的photoProfile必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
   12. let photoProfiles = cameraOutputCapability.photoProfiles;
   13. if (photoProfiles.length < 1) {
   14. return;
   15. }
   16. let index = photoProfiles.findIndex((photoProfile: camera.Profile) => {
   17. return photoProfile.size.width === photoProfileObj.size.width &&
   18. photoProfile.size.height === photoProfileObj.size.height &&
   19. photoProfile.format === photoProfileObj.format;
   20. });
   21. if (index === -1) {
   22. return;
   23. }
   24. let photoOutput = cameraManager.createPhotoOutput(photoProfileObj);
   25. if (photoOutput === undefined) {
   26. return;
   27. }
   28. }
   ```
6. 确定录像输出流。

   ```
   1. async function createAVRecorder(): Promise<media.AVRecorder | undefined> {
   2. let avRecorder: media.AVRecorder | undefined = undefined;
   3. try {
   4. avRecorder = await media.createAVRecorder();
   5. } catch (error) {
   6. console.error('createAVRecorder error')
   7. }
   8. return avRecorder;
   9. }

   11. function initFd(context: common.Context): number {
   12. let filesDir = context.filesDir;
   13. let filePath = filesDir + `/${Date.now()}.mp4`;
   14. AppStorage.setOrCreate<string>('filePath', filePath);
   15. let file: fileIo.File = fileIo.openSync(filePath, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   16. return file.fd;
   17. }

   19. async function prepareAVRecorder(videoProfileObj: camera.VideoProfile, curCameraDevice: camera.CameraDevice, avRecorder: media.AVRecorder, context: common.Context): Promise<void> {
   20. let fd = initFd(context);
   21. let videoConfig: media.AVRecorderConfig = {
   22. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
   23. videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
   24. profile: {
   25. audioBitrate: 48000,
   26. audioChannels: 2,
   27. audioCodec: media.CodecMimeType.AUDIO_AAC,
   28. audioSampleRate: 48000,
   29. fileFormat: media.ContainerFormatType.CFT_MPEG_4,
   30. videoBitrate: 512000,
   31. videoCodec: media.CodecMimeType.VIDEO_AVC,
   32. videoFrameWidth: videoProfileObj.size.width,
   33. videoFrameHeight: videoProfileObj.size.height,
   34. videoFrameRate: videoProfileObj.frameRateRange.min
   35. },
   36. url: `fd://${fd.toString()}`,
   37. rotation: curCameraDevice?.cameraOrientation
   38. };
   39. await avRecorder?.prepare(videoConfig).catch((err: BusinessError): void => {
   40. console.error(`prepareAVRecorder prepare err`);
   41. });
   42. }

   44. async function getVideoOutputFn(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability, concurrentInfo: Array<camera.CameraConcurrentInfo>, curCameraDeviceFront: camera.CameraDevice, context: common.Context)
   45. {
   46. // 此处创建录像输出流以format：1003，size：1920*1080的videoProfile为例，对应的videoProfile必须在getCameraConcurrentInfos获取到的并发能力信息数组范围内。
   47. let videoProfileObj: camera.VideoProfile = {
   48. format: 1003,
   49. size: {
   50. width: 1920,
   51. height: 1080
   52. },
   53. frameRateRange: {
   54. min: 30,
   55. max: 60
   56. }
   57. };

   59. // 替换相应能力集。
   60. for (let i = 0; i < concurrentInfo.length; i++) {
   61. if (concurrentInfo[i].device.cameraPosition == camera.CameraPosition.CAMERA_POSITION_FRONT) {
   62. cameraOutputCapability = concurrentInfo[i].outputCapabilities[1];
   63. break;
   64. }
   65. }
   66. let videoProfiles = cameraOutputCapability.videoProfiles;
   67. if (videoProfiles.length < 1) {
   68. return;
   69. }
   70. let index = videoProfiles.findIndex((videoProfile: camera.VideoProfile) => {
   71. return videoProfile.size.width === videoProfileObj.size.width &&
   72. videoProfile.size.height === videoProfileObj.size.height &&
   73. videoProfile.format === videoProfileObj.format &&
   74. videoProfile.frameRateRange.min <= 60 &&
   75. videoProfile.frameRateRange.max <= 60;
   76. });
   77. if (index === -1) {
   78. return;
   79. }
   80. videoProfileObj = videoProfiles[index];
   81. let avRecorder = await createAVRecorder();
   82. if (avRecorder === undefined) {
   83. return;
   84. }
   85. await prepareAVRecorder(videoProfileObj, curCameraDeviceFront, avRecorder, context);
   86. let videoSurfaceId = await avRecorder.getInputSurface();
   87. let videoOutput = cameraManager.createVideoOutput(videoProfileObj, videoSurfaceId);
   88. if (videoOutput === undefined) {
   89. return;
   90. }
   91. }
   ```
7. 打开相机。通过[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)以多摄同开状态打开指定相机。在使用[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)接口前，请先查询接口是否支持并发能力集，并优先调用[getCameraConcurrentInfos](../harmonyos-references/arkts-apis-camera-cameramanager.md#getcameraconcurrentinfos18)方法，获取多摄同开状态下的相机并发能力集。请勿在未查询并发能力集的情况下使用[open](../harmonyos-references/arkts-apis-camera-camerainput.md#open18)，否则会导致打开相机失败。

   ```
   1. async function initCamera(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice) {
   2. let cameraInput: camera.CameraInput | undefined = undefined;
   3. try {
   4. cameraInput = cameraManager.createCameraInput(cameraDevice);
   5. console.info('createCameraInputFn success');
   6. } catch (error) {
   7. console.error(`createCameraInputFn failed`);
   8. }
   9. if (cameraInput === undefined) {
   10. return;
   11. }
   12. let isOpenSuccess = false;
   13. try {

   15. // 当前版本支持camera.CameraConcurrentType.CAMERA_LIMITED_CAPABILITY模式并发打开相机。
   16. await cameraInput.open(camera.CameraConcurrentType.CAMERA_LIMITED_CAPABILITY);
   17. isOpenSuccess = true;
   18. } catch (error) {
   19. console.error(`createCameraInput failed`);
   20. }
   21. if (!isOpenSuccess) {
   22. return;
   23. }
   24. }
   ```
8. 会话流程。

   ```
   1. // 监听捕获会话错误变化。
   2. function onSessionErrorChange(session: camera.PhotoSession | camera.VideoSession): void {
   3. try {
   4. session.on('error', (captureSessionError: BusinessError): void => {
   5. });
   6. } catch (error) {
   7. console.error('onCaptureSessionErrorChange error');
   8. }
   9. }

   11. let handlePhotoAssetCb: (photoAsset: photoAccessHelper.PhotoAsset) => void = () => {
   12. };

   14. // 监听拍照事件。
   15. function photoOutputCallBack(photoOutput: camera.PhotoOutput): void {
   16. try {

   18. // 监听拍照开始。
   19. photoOutput.on('captureStartWithInfo', (err: BusinessError, captureStartInfo: camera.CaptureStartInfo): void => {
   20. });

   22. // 监听拍照帧输出捕获。
   23. photoOutput.on('frameShutter', (err: BusinessError, frameShutterInfo: camera.FrameShutterInfo): void => {
   24. });

   26. // 监听拍照结束。
   27. photoOutput.on('captureEnd', (err: BusinessError, captureEndInfo: camera.CaptureEndInfo): void => {
   28. });

   30. // 监听拍照异常。
   31. photoOutput.on('error', (data: BusinessError): void => {
   32. });
   33. photoOutput.on('photoAssetAvailable', (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset) => {
   34. if (photoAsset === undefined) {
   35. return;
   36. }
   37. handlePhotoAssetCb(photoAsset);
   38. });
   39. } catch (err) {
   40. }
   41. }

   43. // 会话流程。
   44. async function sessionFlowFn(cameraManager: camera.CameraManager, cameraInput: camera.CameraInput,
   45. previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput | undefined, videoOutput: camera.VideoOutput | undefined, curSceneMode: camera.SceneMode): Promise<void> {
   46. let session: camera.PhotoSession | camera.VideoSession | undefined = undefined;
   47. try {

   49. // 创建CaptureSession实例。
   50. if (curSceneMode === camera.SceneMode.NORMAL_PHOTO) {
   51. session = cameraManager.createSession(curSceneMode) as camera.PhotoSession;
   52. } else if (curSceneMode === camera.SceneMode.NORMAL_VIDEO) {
   53. session = cameraManager.createSession(curSceneMode) as camera.VideoSession;
   54. }
   55. if (session === undefined) {
   56. return;
   57. }
   58. onSessionErrorChange(session);

   60. // 开始配置会话。
   61. session.beginConfig();

   63. // 向会话中添加相机输入流。
   64. session.addInput(cameraInput);

   66. // 向会话中添加预览输出流。
   67. session.addOutput(previewOutput);

   69. if (curSceneMode === camera.SceneMode.NORMAL_PHOTO) {
   70. if (photoOutput === undefined) {
   71. return;
   72. }

   74. // 拍照监听事件。
   75. photoOutputCallBack(photoOutput);

   77. // 向会话中添加拍照输出流。
   78. session.addOutput(photoOutput);
   79. } else if (curSceneMode === camera.SceneMode.NORMAL_VIDEO) {
   80. if (videoOutput === undefined) {
   81. return;
   82. }

   84. // 向会话中添加录像输出流。
   85. session.addOutput(videoOutput);
   86. }

   88. // 提交配置信息。
   89. await session.commitConfig();
   90. } catch (error) {
   91. console.error(`sessionFlowFn fail`);
   92. }
   93. }
   ```
9. 拍照，通过步骤8中配置的photoOutput使用前置或后置相机进行拍照，多摄同开状态下不支持前后相机同时拍照。

   ```
   1. async function takePicture(photoOutput: camera.PhotoOutput): Promise<void> {
   2. if (photoOutput === undefined) {
   3. return;
   4. }
   5. if (photoOutput === null) {
   6. return;
   7. }

   9. if (photoOutput) {
   10. await photoOutput.capture();
   11. } else {
   12. console.info('photoOutput is undefined or null');
   13. }
   14. }
   ```
10. 录制。

    ```
    1. let isRecording = false;

    3. // 启动录制。
    4. async function startVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
    5. try {
    6. await videoOutput?.start();
    7. await avRecorder?.start();
    8. } catch (error) {
    9. console.error(`startVideo err`);
    10. }
    11. }

    13. // 停止录制。
    14. async function stopVideo(videoOutput: camera.VideoOutput, avRecorder: media.AVRecorder): Promise<void> {
    15. if (isRecording) {
    16. return;
    17. }
    18. try {
    19. if (avRecorder) {
    20. await avRecorder.stop();
    21. }
    22. if (videoOutput) {
    23. await videoOutput.stop();
    24. }
    25. isRecording = false;
    26. } catch (error) {
    27. console.error(`stopVideo err`);
    28. }
    29. }
    ```
11. 在多摄同开状态下，前/后置相机可配置的能力示例如下（当前版本仅支持本文开头部分所示的七项基础功能）。

    ```
    1. // 闪光灯。
    2. function hasFlashFn(flashMode: camera.FlashMode, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

    4. // 检测是否有闪光灯。
    5. let hasFlash = session?.hasFlash();

    7. // 检测闪光灯模式是否支持。
    8. let isFlashModeSupported = session?.isFlashModeSupported(flashMode);

    10. // 设置闪光灯模式。
    11. if (isFlashModeSupported) {
    12. session?.setFlashMode(flashMode);
    13. }
    14. }

    16. // 曝光。
    17. function hasExposureFn(ExposureMode: camera.ExposureMode, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

    19. // 检测曝光模式是否支持。
    20. let hasFlash = session?.isExposureModeSupported(ExposureMode);

    22. // 设置曝光模式。
    23. if (hasFlash) {
    24. session?.setExposureMode(ExposureMode);
    25. }
    26. }

    28. // 获取可变焦距范围。
    29. function getZoomRatioRange(session: camera.PhotoSession | camera.VideoSession | undefined = undefined): Array<number> {
    30. let zoomRatioRange: Array<number> = [];
    31. if (session !== undefined) {
    32. zoomRatioRange = session.getZoomRatioRange();
    33. }
    34. return zoomRatioRange;
    35. }

    37. // 变焦。
    38. function setZoomRatioFn(zoomRatio: number, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

    40. // 获取支持的变焦范围。
    41. let zoomRatioRange = getZoomRatioRange();
    42. try {
    43. session?.setZoomRatio(zoomRatio);
    44. } catch (error) {
    45. console.error(`setZoomRatioFn fail`);
    46. }
    47. }

    49. // 曝光补偿。
    50. function setExposureBiasFn(exposureBias: number, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

    52. // 查询曝光补偿范围。
    53. let biasRangeArray: Array<number> | undefined = [];
    54. biasRangeArray = session?.getExposureBiasRange();

    56. // 设置曝光补偿。
    57. session?.setExposureBias(exposureBias);
    58. }

    60. // 对焦模式。
    61. function setFocusMode(focusMode: camera.FocusMode, session: camera.PhotoSession | camera.VideoSession | undefined = undefined): void {

    63. // 检测对焦模式是否支持。
    64. let isSupported = session?.isFocusModeSupported(focusMode);

    66. // 设置对焦模式。
    67. if (!isSupported) {
    68. return;
    69. }
    70. session?.setFocusMode(focusMode);
    71. }
    ```
