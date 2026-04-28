---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-secure-photo
title: 安全相机(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 安全相机(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:02+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3ba596dcd55799dbb1d07a05d349c69c1bebca38d4dd4e7099d0fda01696eba3
---

安全相机主要为银行等有活体检测等安全诉求的应用提供，安全相机的使用需要加密算法框架及可信应用服务。

应用具体使用步骤如下：

* 通过Camera Kit打开安全摄像头，成功打开安全摄像头后，Camera Kit会返回给应用一个**安全摄像头序列号**。
* 通过[Device Security Kit](devicesecurity-introduction.md)来创建证明密钥（安全摄像头序列号会作为入参）、初始化证明会话。Device Security Kit初始化证明会话完成后会返回给应用**匿名证书链**。
* 通过Camera Kit配置安全相机输入输出流，重点是配置**安全数据流**，注册安全数据流每帧安全图像回调监听。
* 解析安全数据流每帧安全图像，在服务器侧完成安全图像的签名验证。

说明

当前文档主要说明通过Camera Kit完成的步骤，证明会话相关步骤需通过Device Security Kit完成，具体可参考[可信应用服务-安全摄像头](devicesecurity-taas-securecamera.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/FiVNZ2YlSsKP6JBNwowLUQ/zh-cn_image_0000002552798932.png?HW-CC-KV=V1&HW-CC-Date=20260427T234601Z&HW-CC-Expire=86400&HW-CC-Sign=612562CBE0E8C5ABC2BE46B249310BAAD2E934E12E99D26CA405E66813F34035)

## 开发步骤

详细的API说明请参考[Camera API参考](../harmonyos-references/js-apis-camera.md)。

1. 导入依赖，需要导入相机框架相关领域依赖。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { image } from '@kit.ImageKit';
   ```
2. 选择支持安全相机的设备。

   通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[getSupportedSceneModes](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedscenemodes11)方法，可以获取当前设备支持的所有模式，如果当前设备支持安全相机模式，即可使用该设备做后续安全相机操作。

   当前安全相机仅支持手机前置镜头。

   ```
   1. function isSecureCamera(cameraManager: camera.CameraManager, cameraDevice: camera.CameraDevice): boolean {
   2. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraDevice);
   3. const secureMode = sceneModes.find(mode => mode === camera.SceneMode.SECURE_PHOTO);
   4. if (secureMode) {
   5. console.info('current device support secure camera!');
   6. return true;
   7. } else {
   8. console.info('current device not support secure camera!');
   9. return false;
   10. }
   11. }

   13. let secureCamera: camera.CameraDevice;

   15. function getSecureCamera(cameraManager: camera.CameraManager): void {
   16. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
   17. for (let index = 0; index < cameraArray.length; index++) {
   18. if (isSecureCamera(cameraManager, cameraArray[index])) {
   19. secureCamera = cameraArray[index];
   20. }
   21. }
   22. }
   ```
3. 查询相机设备在安全模式下支持的输出能力。

   通过[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)的[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)方法，可获取设备在安全模式下支持的输出能力。

   当前安全相机仅支持输出预览流，推荐预览流使用640 \* 480分辨率。

   ```
   1. function getSupportedOutputCapability(cameraManager: camera.CameraManager, secureCamera: camera.CameraDevice): void {
   2. let outputCap: camera.CameraOutputCapability =
   3. cameraManager.getSupportedOutputCapability(secureCamera, camera.SceneMode.SECURE_PHOTO);
   4. let previewProfilesArray: Array<camera.Profile> = outputCap.previewProfiles;
   5. }
   ```
4. 创建设备输入输出。

   安全相机需要创建两路输出流：

   * 一路是普通的预览流，用于界面显示，普通预览流的创建流程请参考[预览开发指导](camera-preview.md)。
   * 一路是安全数据流，用于安全服务校验，安全数据流需要通过[image.createImageReceiver](../harmonyos-references/arkts-apis-image-f.md#imagecreateimagereceiver11)创建图像接收类[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)，再通过其[getReceivingSurfaceId](../harmonyos-references/arkts-apis-image-imagereceiver.md#getreceivingsurfaceid9)方法获取surfaceId。

     说明

     安全数据流没有单独的数据类型，同属于预览流，输出能力与预览流保持一致，创建ImageReceiver仅支持JPEG格式。

   ```
   1. async function createInputAndOutputs(cameraManager: camera.CameraManager,
   2. secureCamera: camera.CameraDevice,
   3. previewProfile: camera.Profile,
   4. previewSurfaceId: string): Promise<void> {
   5. // 创建输入流
   6. let cameraInput: camera.CameraInput = cameraManager.createCameraInput(secureCamera);
   7. // 创建普通预览输出流
   8. let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfile, previewSurfaceId);
   9. // 创建安全数据输出流
   10. const receiver: image.ImageReceiver =
   11. image.createImageReceiver({ width: previewProfile.size.width, height: previewProfile.size.height },
   12. image.ImageFormat.JPEG, 8);
   13. const secureSurfaceId: string = await receiver.getReceivingSurfaceId();
   14. let secureOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfile, secureSurfaceId);
   15. }
   ```
5. 打开安全设备。

   [CameraInput](../harmonyos-references/arkts-apis-camera-camerainput.md)提供了[open(isSecureEnabled)](../harmonyos-references/arkts-apis-camera-camerainput.md#open12)方法用于打开安全相机并返回安全摄像头序列号，该序列号是安全模块创建证明会话的必需参数。

   仅当isSecureEnabled为true时，才会打开安全相机，并有安全序列号返回。

   ```
   1. async function openCamera(cameraInput: camera.CameraInput) {
   2. const seqId: bigint = await cameraInput.open(true);
   3. }
   ```
6. 使用Device Security Kit的能力，创建证明密钥、打开证明会话。请参考Device Security Kit（设备安全服务）的开发指导：[可信应用服务-安全摄像头](devicesecurity-taas-securecamera.md)。
7. 创建安全相机会话，配流启流。

   创建安全相机模式的会话，将输入流、输出流加入会话，需要将安全数据流通过[SecureSession](../harmonyos-references/arkts-apis-camera-securesession.md)的[addSecureOutput](../harmonyos-references/arkts-apis-camera-securesession.md#addsecureoutput12)方法标记成安全输出。

   ```
   1. async function openSession(cameraManager: camera.CameraManager,
   2. cameraInput: camera.CameraInput,
   3. previewOutput: camera.PreviewOutput,
   4. secureOutput: camera.PreviewOutput): Promise<void> {
   5. try {
   6. let secureSession: camera.SecureSession = cameraManager.createSession(camera.SceneMode.SECURE_PHOTO);
   7. if (secureSession === undefined) {
   8. console.error('create secureSession failed!');
   9. }
   10. secureSession.beginConfig();
   11. secureSession.addInput(cameraInput);
   12. secureSession.addOutput(previewOutput);
   13. secureSession.addOutput(secureOutput);
   14. secureSession.addSecureOutput(secureOutput); // 把secureOutput标记成安全输出
   15. await secureSession.commitConfig();
   16. await secureSession.start();
   17. } catch (err) {
   18. console.error('openSession failed!');
   19. }
   20. }
   ```
8. 安全模式会话正常启动后，预览流和安全数据流数据逐帧上报，安全数据流每帧数据可以通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)注册[imageArrival](../harmonyos-references/arkts-apis-image-imagereceiver.md#on9)回调获取。

   ```
   1. function onBuffer(receiver: image.ImageReceiver): void {
   2. receiver.on('imageArrival', () => {
   3. // 从ImageReceiver读取下一张图片
   4. receiver.readNextImage().then((img: image.Image) => {
   5. // 从图像中获取组件缓存
   6. img.getComponent(image.ComponentType.JPEG).then((component: image.Component) => {
   7. // 安全数据流内容，应用通过解析该buffer内容完成签名认证
   8. const buffer = component.byteBuffer;
   9. console.info('Succeeded in getting component byteBuffer.');
   10. })
   11. })
   12. })
   13. }
   ```

   解析安全数据流每帧安全图像，在服务器侧完成安全图像的签名验证。

   如果有在端侧验证图像数据或地理位置数据签名的需求，可参考[验证签名](devicesecurity-taas-verifysignature.md)中与安全图像相关的部分。
9. 释放安全相机，使用[Session](../harmonyos-references/arkts-apis-camera-session.md)的[release](../harmonyos-references/arkts-apis-camera-session.md#release11-1)方法。
