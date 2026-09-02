---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-session-management
title: 会话管理(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用必选能力(ArkTS) > 会话管理(ArkTS)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:44+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:6321b3b1b2908f41df7618586d6f7304daa96797440d5e92a5ac2f0ffd008f4f
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

   ```ts
   import { camera } from '@kit.CameraKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用[cameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)方法创建一个会话。

   ```ts
   // 此处以videoSession为例。
   function getSession(cameraManager: camera.CameraManager): camera.VideoSession | undefined {
     let videoSession: camera.VideoSession | undefined = undefined;
     try {
       videoSession = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to create the session instance. error: ${err.code}`);
     }
     return videoSession;
   }
   ```
3. 调用[VideoSession](../harmonyos-references/arkts-apis-camera-videosession.md)中的[beginConfig](../harmonyos-references/arkts-apis-camera-session.md#beginconfig11)方法配置会话。

   ```ts
   function beginConfig(videoSession: camera.VideoSession): void {
     try {
       videoSession.beginConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to beginConfig. error: ${err.code}`);
     }
   }
   ```
4. 使能。向会话中添加相机的输入流和输出流，调用[addInput](../harmonyos-references/arkts-apis-camera-session.md#addinput11)添加相机的输入流；调用[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)添加相机的输出流。以下示例代码以添加预览流previewOutput和拍照流photoOutput为例，即当前模式支持拍照和预览。

   调用VideoSession中的[commitConfig](../harmonyos-references/arkts-apis-camera-session.md#commitconfig11)和[start](../harmonyos-references/arkts-apis-camera-session.md#start11)方法提交相关配置，并启动会话。

   **说明** 

   在调用[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)添加相机的输出流前，可通过[canAddOutput](../harmonyos-references/arkts-apis-camera-session.md#canaddoutput11)判断当前相机输出流是否可以添加到session中。

   相机输入流cameraInput创建流程请参考[设备输入](camera-device-input.md)，相机预览输出流previewOutput和拍照输出流photoOutput创建流程请分别参考[预览](camera-preview.md)和[拍照](camera-shooting.md)。

   ```ts
   async function startSession(videoSession: camera.VideoSession, cameraInput: camera.CameraInput, previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput): Promise<void> {
     try {
       videoSession.addInput(cameraInput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to addInput. error: ${err.code}`);
     }
     let canAddPreviewOutput : boolean = false;
     try {
       canAddPreviewOutput = videoSession.canAddOutput(previewOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add previewOutput. error: ${err.code}`);
     }
     if (!canAddPreviewOutput) {
       console.error(`Failed to add preview output.`);
       return;
     }
     try {
       videoSession.addOutput(previewOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add previewOutput. error: ${err.code}`);
     }
     let canAddPhotoOutput : boolean = false
     try {
       canAddPhotoOutput = videoSession.canAddOutput(photoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add photoOutput error: ${err.code}`);
     }
     if (!canAddPhotoOutput) {
       console.error(`Failed to add photo output.`);
       return;
     }
     try {
       videoSession.addOutput(photoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add photoOutput. error: ${err.code}`);
     }
     try {
       await videoSession.commitConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to commitConfig. error: ${err.code}`);
      return;
     }

     try {
       await videoSession.start();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to start. error: ${err.code}`);
     }
   }
   ```
5. 会话控制。调用VideoSession中的[stop](../harmonyos-references/arkts-apis-camera-session.md#stop11)方法可以停止当前会话。调用[removeOutput](../harmonyos-references/arkts-apis-camera-session.md#removeoutput11)和[addOutput](../harmonyos-references/arkts-apis-camera-session.md#addoutput11)方法可以完成会话切换控制。以下示例代码以移除拍照流photoOutput，添加视频流videoOutput为例，完成了拍照到录像的切换。

   ```ts
   async function switchOutput(videoSession: camera.VideoSession, videoOutput: camera.VideoOutput, photoOutput: camera.PhotoOutput): Promise<void> {
     try {
       await videoSession.stop();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to stop. error: ${err.code}`);
     }

     try {
       videoSession.beginConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to beginConfig. error: ${err.code}`);
     }
     // 从会话中移除拍照输出流。
     try {
       videoSession.removeOutput(photoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to remove photoOutput. error: ${err.code}`);
     }
     try {
       videoSession.canAddOutput(videoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add videoOutput error: ${err.code}`);
     }
     // 向会话中添加视频输出流。
     try {
       videoSession.addOutput(videoOutput);
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to add videoOutput. error: ${err.code}`);
     }
     try {
       await videoSession.commitConfig();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to commitConfig. error: ${err.code}`);
     }

     try {
       await videoSession.start();
     } catch (error) {
       let err = error as BusinessError;
       console.error(`Failed to start. error: ${err.code}`);
     }
   }
   ```
