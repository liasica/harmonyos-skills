---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-session-management
title: 会话管理(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(ArkTS) > 会话管理(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:55+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:233a7752adcd5326a1a19f5c5ac29702ab8c99b9c294179f7991057131caec71
---

相机使用预览、拍照、录像、元数据功能前，均需要创建相机会话。

在会话中，可以完成以下功能：

* 配置相机的输入流和输出流。相机在拍摄前，必须完成输入输出流的配置。

  配置输入流即添加设备输入，对用户而言，相当于选择设备的某一相机拍摄；配置输出流，即选择数据将以什么形式输出。当应用需要实现拍照时，输出流应配置为预览流和拍照流，预览流的数据将显示在[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件上，拍照流的数据将通过[ImageReceiver](../harmonyos-references/arkts-apis-image-imagereceiver.md)接口的能力保存到相册中。
* 添加闪光灯、调整焦距等配置。具体支持的配置及接口说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。
* 会话切换控制。应用可以通过移除和添加输出流的方式，切换相机模式。如当前会话的输出流为拍照流，应用可以将拍照流移除，然后添加视频流作为输出流，即完成了拍照到录像的切换。

完成会话配置后，应用提交和开启会话，可以开始调用相机相关功能。

## 开发步骤

1. 导入相关接口，导入方法如下。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[cameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)方法创建一个会话。

   ```
   1. // 此处以videoSession为例。
   2. function getSession(cameraManager: camera.CameraManager): camera.VideoSession | undefined {
   3. let videoSession: camera.VideoSession | undefined = undefined;
   4. try {
   5. videoSession = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. console.error(`Failed to create the session instance. error: ${err.code}`);
   9. }
   10. return videoSession;
   11. }
   ```
3. 调用[VideoSession](../harmonyos-references/arkts-apis-camera-videosession.md)中的[beginConfig](../harmonyos-references/arkts-apis-camera-session.md#beginconfig11)方法配置会话。

   ```
   1. function beginConfig(videoSession: camera.VideoSession): void {
   2. try {
   3. videoSession.beginConfig();
   4. } catch (error) {
   5. let err = error as BusinessError;
   6. console.error(`Failed to beginConfig. error: ${err.code}`);
   7. }
   8. }
   ```
4. 使能。向会话中添加相机的输入流和输出流，调用[addInput](../harmonyos-references/arkts-apis-camera-session.md#addinput11)添加相机的输入流；调用[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)添加相机的输出流。以下示例代码以添加预览流previewOutput和拍照流photoOutput为例，即当前模式支持拍照和预览。

   调用VideoSession中的[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)和[start](../harmonyos-references/arkts-apis-camera-session.md#start11)方法提交相关配置，并启动会话。

   说明

   在调用[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)添加相机的输出流前，可通过[canAddOutput](../harmonyos-references/arkts-apis-camera-session.md#canaddoutput11)判断当前相机输出流是否可以添加到session中。

   相机输入流cameraInput创建流程请参考[设备输入](camera-device-input.md)，相机预览输出流previewOutput和拍照输出流photoOutput创建流程请分别参考[预览](camera-preview.md)和[拍照](camera-shooting.md)。

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
   56. }
   ```
5. 会话控制。调用VideoSession中的[stop](../harmonyos-references/arkts-apis-camera-session.md#stop11)方法可以停止当前会话。调用[removeOutput](../harmonyos-references/arkts-apis-camera-session.md#removeoutput11)和[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)方法可以完成会话切换控制。以下示例代码以移除拍照流photoOutput，添加视频流videoOutput为例，完成了拍照到录像的切换。

   ```
   1. async function switchOutput(videoSession: camera.VideoSession, videoOutput: camera.VideoOutput, photoOutput: camera.PhotoOutput): Promise<void> {
   2. try {
   3. await videoSession.stop();
   4. } catch (error) {
   5. let err = error as BusinessError;
   6. console.error(`Failed to stop. error: ${err.code}`);
   7. }

   9. try {
   10. videoSession.beginConfig();
   11. } catch (error) {
   12. let err = error as BusinessError;
   13. console.error(`Failed to beginConfig. error: ${err.code}`);
   14. }
   15. // 从会话中移除拍照输出流。
   16. try {
   17. videoSession.removeOutput(photoOutput);
   18. } catch (error) {
   19. let err = error as BusinessError;
   20. console.error(`Failed to remove photoOutput. error: ${err.code}`);
   21. }
   22. try {
   23. videoSession.canAddOutput(videoOutput);
   24. } catch (error) {
   25. let err = error as BusinessError;
   26. console.error(`Failed to add videoOutput error: ${err.code}`);
   27. }
   28. // 向会话中添加视频输出流。
   29. try {
   30. videoSession.addOutput(videoOutput);
   31. } catch (error) {
   32. let err = error as BusinessError;
   33. console.error(`Failed to add videoOutput. error: ${err.code}`);
   34. }
   35. try {
   36. await videoSession.commitConfig();
   37. } catch (error) {
   38. let err = error as BusinessError;
   39. console.error(`Failed to commitConfig. error: ${err.code}`);
   40. }

   42. try {
   43. await videoSession.start();
   44. } catch (error) {
   45. let err = error as BusinessError;
   46. console.error(`Failed to start. error: ${err.code}`);
   47. }
   48. }
   ```
