---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-6
title: 如何读取相机的预览图
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何读取相机的预览图
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dfdc137a3a0bc2143f71715c94271f5701323f15c8de68be7b891ae0bff62ba4
---

开发步骤：

1. 导入image接口。

   创建双路预览流的SurfaceId时，除了XComponent组件的SurfaceId，还需要使用ImageReceiver组件创建的SurfaceId。使用image模块提供的接口完成此操作。

   ```ts
   import { image } from '@kit.ImageKit';
   ```
2. 创建ImageReceiver组件Surface。

   ```ts
   async function getImageReceiverSurfaceId(): Promise<string | undefined> {
     let receiver: image.ImageReceiver = image.createImageReceiver({ width: 640,height: 480 },4,8);
     console.info('before ImageReceiver check');
     let ImageReceiverSurfaceId: string | undefined = undefined;
     if (receiver !== undefined) {
       console.info('ImageReceiver is ok');
       let ImageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
       console.info(`ImageReceived id: ${ImageReceiverSurfaceId}`);
     } else {
       console.error('ImageReceiver is not ok');
     }
     return ImageReceiverSurfaceId;
   }
   ```
3. 创建XComponent组件Surface。

   参考相机预览指导文档。

   ```ts
   //xxx.ets
   // 创建XComponentController
   @Entry
   @Component
   struct XComponentPage {
     // 创建XComponentController
     mXComponentController: XComponentController = new XComponentController;

     build() {
       Flex() {
         // Create XComponent
         XComponent({
           id: '',
           type: 'surface',
           libraryname: '',
           controller: this.mXComponentController
         })
           .onLoad(() => {
             // Set the width and height of the Surface (1920 * 1080), and set the preview size based on the preview resolution size supported
             // by the current device obtained from previewProfilesArray earlier
             this.mXComponentController.setXComponentSurfaceRect({surfaceWidth:1920,surfaceHeight:1080});
             // Get Surface ID
             let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
           })
           .width('1920px')
           .height('1080px')
       }
     }
   }
   ```
4. 实现双路预览。

   通过 `createPreviewOutput` 方法将步骤2和步骤3生成的两路 `SurfaceId` 传递到相机服务，创建两路预览流。其余流程按照正常预览流程开发。

   ```ts
   import { camera } from '@kit.CameraKit';
   import { image } from '@kit.ImageKit';

   async function createDualChannelPreview(cameraManager: camera.CameraManager, XComponentSurfaceId: string, receiver: image.ImageReceiver): Promise<void> {
     let camerasDevices: Array<camera.CameraDevice> = cameraManager.getSupportedCameras(); // 获取支持的相机设备对象

     // Get profile object
     let profiles: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camerasDevices[0], camera.SceneMode.NORMAL_PHOTO); // 获取对应相机设备profiles
     let previewProfiles: Array<camera.Profile> = profiles.previewProfiles;

     // Preview Stream 1
     let previewProfilesObj: camera.Profile = previewProfiles[0];

     // Preview Stream 2
     let previewProfilesObj2: camera.Profile = previewProfiles[0];

     // Create preview stream 1 output object
     let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfilesObj, XComponentSurfaceId);

     // Create preview stream 2 output object
     let imageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
     let previewOutput2: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfilesObj2, imageReceiverSurfaceId);

     // Create cameraInput object
     let cameraInput: camera.CameraInput = cameraManager.createCameraInput(camerasDevices[0]);

     // Turn on the camera
     await cameraInput.open();

     // session flow
     let captureSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);

     // Start configuring session
     captureSession.beginConfig();

     // Add CameraInput to the conversation
     captureSession.addInput(cameraInput);

     // Add preview stream 1 to the session
     captureSession.addOutput(previewOutput);

     // Add preview stream 2 to the session
     captureSession.addOutput(previewOutput2);

     // Submit configuration information
     await captureSession.commitConfig();

     // session start
     await captureSession.start();
   }
   ```
5. 通过ImageReceiver实时获取预览图像。

   通过ImageReceiver组件的imageArrival事件监听获取底层返回的图像数据。有关详细的API说明，请参考Image API。

   ```ts
   import { BusinessError } from '@kit.BasicServicesKit';
   import image from '@ohos.multimedia.image';

   function onImageArrival(receiver: image.ImageReceiver): void {
     receiver.on('imageArrival', () => {
       receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
         if (err || nextImage === undefined) {
           return;
         }
         // The current ImageReceiver does not support obtaining YUV data. You can use the JPEG data channel to receive YUV data, but using this method carries risks
         nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
           if (err || imgComponent === undefined) {
             return;
           }
           if (imgComponent.byteBuffer as ArrayBuffer) {
             // Handle according to business demands
           } else {
             return;
           }
         })
       })
     })
   }
   ```

## 参考链接

[双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)

[@ohos.multimedia.image (图片处理)](../harmonyos-references/js-apis-image.md)
