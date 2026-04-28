---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-worker
title: 在Worker线程中使用相机(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 在Worker线程中使用相机(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:59+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6a8926af0a3ee400d6d63731eedb779837c8db092a80694336da4bb942df032d
---

[Worker](worker-introduction.md)主要作用是为应用程序提供一个多线程的运行环境，可满足应用程序在执行过程中与主线程分离，在后台线程中运行一个脚本进行耗时操作，极大避免类似计算密集型或高延迟的任务阻塞主线程的运行。

通常开发者使用相机功能需要创建相机会话，并持续接收处理预览流、拍照流、录像流等从而实现相关相机功能，这些密集型操作如果都放在主线程即UI线程，可能会阻塞UI绘制，推荐开发者在worker线程中实现相机功能。

## 开发步骤

1. 导入依赖，本篇文档需要用到worker和相机框架等相关依赖包。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { camera } from '@kit.CameraKit';
   3. import { ErrorEvent, MessageEvents, ThreadWorkerGlobalScope, worker } from '@kit.ArkTS';
   ```
2. 创建相机服务代理类，调用CameraKit方法都放在这个类里执行。

   ```
   1. class CameraService {
   2. private imageWidth: number = 1920;
   3. private imageHeight: number = 1080;
   4. private cameraManager: camera.CameraManager | undefined = undefined;
   5. private cameras: Array<camera.CameraDevice> = [];
   6. private cameraInput: camera.CameraInput | undefined = undefined;
   7. private previewOutput: camera.PreviewOutput | undefined = undefined;
   8. private photoOutput: camera.PhotoOutput | undefined = undefined;
   9. private session: camera.PhotoSession | camera.VideoSession | undefined = undefined;

   11. // 初始化相机。
   12. async initCamera(context: Context, surfaceId: string): Promise<void> {
   13. console.info(`initCamera surfaceId: ${surfaceId}`);
   14. try {
   15. await this.releaseCamera();
   16. // 获取相机管理器实例。
   17. this.cameraManager = camera.getCameraManager(context);
   18. if (this.cameraManager === undefined) {
   19. console.error('cameraManager is undefined');
   20. return;
   21. }
   22. this.cameras = this.cameraManager.getSupportedCameras();
   23. if (!this.cameras || this.cameras.length <= 0) {
   24. console.error("cameraManager.getSupportedCameras error");
   25. return;
   26. }
   27. // 创建cameraInput输出对象。
   28. this.cameraInput = this.cameraManager.createCameraInput(this.cameras[0]);
   29. if (this.cameraInput === undefined) {
   30. console.error('Failed to create the camera input.');
   31. return;
   32. }
   33. // 打开相机。
   34. await this.cameraInput.open();

   36. let previewProfile: camera.Profile = {
   37. format: camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP,
   38. size: {
   39. width: this.imageWidth,
   40. height: this.imageHeight
   41. }
   42. };
   43. // 创建预览流输出。
   44. this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, surfaceId);
   45. if (this.previewOutput === undefined) {
   46. console.error('Failed to create the preview stream.');
   47. this.releaseCamera();
   48. return;
   49. }

   51. let photoProfile: camera.Profile = {
   52. format: camera.CameraFormat.CAMERA_FORMAT_JPEG,
   53. size: {
   54. width: this.imageWidth,
   55. height: this.imageHeight
   56. }
   57. };
   58. // 创建拍照流输出。
   59. this.photoOutput = this.cameraManager.createPhotoOutput(photoProfile);
   60. if (this.photoOutput === undefined) {
   61. console.error('Failed to create the photoOutput.');
   62. this.releaseCamera();
   63. return;
   64. }

   66. // 创建相机会话，启动会话。
   67. let session = this.cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
   68. if (!session) {
   69. console.error('session is null');
   70. this.releaseCamera();
   71. return;
   72. }
   73. this.session = session as camera.PhotoSession;
   74. this.session.beginConfig();
   75. this.session.addInput(this.cameraInput);
   76. this.session.addOutput(this.previewOutput);
   77. this.session.addOutput(this.photoOutput);
   78. await this.session.commitConfig();
   79. await this.session.start();
   80. } catch (error) {
   81. let err = error as BusinessError;
   82. console.error(`initCamera fail: ${err}`);
   83. this.releaseCamera();
   84. }
   85. }

   87. // 释放相机资源。
   88. async releaseCamera(): Promise<void> {
   89. console.info('releaseCamera is called');
   90. // 停止当前会话。
   91. await this.session?.stop().catch((e: BusinessError) => {console.error('Failed to stop session: ', e)});
   92. // 释放相机输入流。
   93. await this.cameraInput?.close().catch((e: BusinessError) => {console.error('Failed to close the camera: ', e)});
   94. // 释放预览输出流。
   95. await this.previewOutput?.release().catch((e: BusinessError) => {console.error('Failed to stop the preview stream: ', e)});
   96. // 释放拍照输出流。
   97. await this.photoOutput?.release().catch((e: BusinessError) => {console.error('Stop Photo Stream Failure: ', e)});
   98. // 释放会话。
   99. await this.session?.release().catch((e: BusinessError) => {console.error('Failed to release session: ', e)});
   100. console.info('releaseCamera success');
   101. }
   102. }
   ```
3. 创建worker线程文件，配置worker。

   DevEco Studio支持一键生成Worker，在对应的{moduleName}目录下任意位置，点击鼠标右键 > New > Worker，即可自动生成Worker的模板文件及配置信息，无需再手动在build-profile.json5中进行相关配置。

   CameraWorker.ets实现参考：

   ```
   1. let cameraService = new CameraService();
   2. const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

   4. // 自定义消息格式。
   5. interface MessageInfo {
   6. hasResolve: boolean;
   7. type: string;
   8. context: Context; // 注意worker线程中无法使用getContext()直接获取宿主线程context，需要通过消息从宿主线程通信到worker线程使用。
   9. surfaceId: string;
   10. }

   12. workerPort.onmessage = async (e: MessageEvents) => {
   13. const messageInfo: MessageInfo = e.data;
   14. console.info(`worker onmessage type:${messageInfo.type}`)
   15. if ('initCamera' === messageInfo.type) {
   16. // 在worker线程中收到宿主线程初始化相机的消息。
   17. console.info(`worker initCamera surfaceId:${messageInfo.surfaceId}`)
   18. // 在worker线程中初始化相机。
   19. await cameraService.initCamera(messageInfo.context, messageInfo.surfaceId);
   20. } else if ('releaseCamera' === messageInfo.type) {
   21. // 在worker线程中收到宿主线程释放相机的消息。
   22. console.info('worker releaseCamera.');
   23. // 在worker线程中释放相机。
   24. await cameraService.releaseCamera();
   25. }
   26. }

   28. workerPort.onmessageerror = (e: MessageEvents) => {
   29. }

   31. workerPort.onerror = (e: ErrorEvent) => {
   32. }
   ```
4. 创建组件，用于显示预览流，在页面相关生命周期中构造ThreadWorker实例，在worker线程中完成相机初始化和释放。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. private mXComponentController: XComponentController = new XComponentController();
   5. private surfaceId: string = '';
   6. @State imageWidth: number = 1920;
   7. @State imageHeight: number = 1080;
   8. // 创建ThreadWorker对象获取worker实例。
   9. private workerInstance: worker.ThreadWorker = new worker.ThreadWorker('entry/ets/workers/CameraWorker.ets');
   10. private uiContext: UIContext = this.getUIContext();
   11. private context: Context | undefined = this.uiContext.getHostContext();
   12. private mXComponentOptions: XComponentOptions = {
   13. type: XComponentType.SURFACE,
   14. controller: this.mXComponentController
   15. }

   17. onPageShow(): void {
   18. if ('' !== this.surfaceId) {
   19. // 通过worker实例向worker线程发送消息初始化相机。
   20. this.workerInstance.postMessage({
   21. type: 'initCamera',
   22. context: this.context,
   23. surfaceId: this.surfaceId,
   24. })
   25. }
   26. }

   28. onPageHide(): void {
   29. // 通过worker实例向worker线程发送消息销毁相机。
   30. this.workerInstance.postMessage({
   31. type: 'releaseCamera',
   32. })
   33. }

   35. build() {
   36. Column() {
   37. Column() {
   38. XComponent(this.mXComponentOptions)
   39. .onLoad(async () => {
   40. console.info('onLoad is called');
   41. // 初始化XComponent获取预览流surfaceId。
   42. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
   43. let surfaceRect: SurfaceRect = {
   44. surfaceWidth: this.imageHeight,
   45. surfaceHeight: this.imageWidth
   46. };
   47. this.mXComponentController.setXComponentSurfaceRect(surfaceRect);
   48. console.info(`onLoad surfaceId: ${this.surfaceId}`);
   49. if (!this.workerInstance) {
   50. console.error('create stage worker failed');
   51. return;
   52. }
   53. // 宿主线程向worker线程发送初始化相机消息。
   54. this.workerInstance.postMessage({
   55. type: 'initCamera',
   56. context: this.context, // 将宿主线程的context传给worker线程使用。
   57. surfaceId: this.surfaceId, // 将surfaceId传给worker线程使用。
   58. })
   59. })// The width and height of the surface are opposite to those of the XComponent.
   60. .width(this.uiContext.px2vp(this.imageHeight))
   61. .height(this.uiContext.px2vp(this.imageWidth))

   63. }.justifyContent(FlexAlign.Center)
   64. .height('90%')

   66. Text('WorkerDemo')
   67. .fontSize(36)
   68. }
   69. .justifyContent(FlexAlign.End)
   70. .height('100%')
   71. .width('100%')
   72. }
   73. }
   ```

## trace对比

不使用Worker：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/hxdIMDLDRBufbdCxv6SYAA/zh-cn_image_0000002552798920.png?HW-CC-KV=V1&HW-CC-Date=20260427T234558Z&HW-CC-Expire=86400&HW-CC-Sign=DF773AD820559E5D282C853D3FDFC5B65A7E19250FA1C62D91ECDF92B3357883)

使用Worker：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/pOOCxkpQSnW9cXsdXBAfGQ/zh-cn_image_0000002583438615.png?HW-CC-KV=V1&HW-CC-Date=20260427T234558Z&HW-CC-Expire=86400&HW-CC-Sign=8E8309D8DC6F1FCE4F01432308ECCBE0A55D56E024774522914F89A7E712D7F4)
