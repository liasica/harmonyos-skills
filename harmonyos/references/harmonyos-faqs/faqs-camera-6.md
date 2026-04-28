---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-6
title: 如何读取相机的预览图
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何读取相机的预览图
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:26+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5541ce55de37db6c4827559fa80842ec5584d1aca8f4b83ad9f6d8aaabdd5974
---

开发步骤：

1. 导入image接口。

创建双路预览流的SurfaceId时，除了XComponent组件的SurfaceId，还需要使用ImageReceiver组件创建的SurfaceId。使用image模块提供的接口完成此操作。

```
1. import { image } from '@kit.ImageKit';
```

[GetSurface.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetSurface.ets#L21-L21)

2. 创建ImageReceiver组件Surface。

```
1. async function getImageReceiverSurfaceId(): Promise<string | undefined> {
2. let receiver: image.ImageReceiver = image.createImageReceiver({ width: 640,height: 480 },4,8);
3. console.info('before ImageReceiver check');
4. let ImageReceiverSurfaceId: string | undefined = undefined;
5. if (receiver !== undefined) {
6. console.info('ImageReceiver is ok');
7. let ImageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
8. console.info(`ImageReceived id: ${ImageReceiverSurfaceId}`);
9. } else {
10. console.error('ImageReceiver is not ok');
11. }
12. return ImageReceiverSurfaceId;
13. }
```

[GetSurface.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetSurface.ets#L25-L38)

3. 创建XComponent组件Surface。

参考相机预览指导文档。

```
1. //xxx.ets
2. // 创建XComponentController
3. @Entry
4. @Component
5. struct XComponentPage {
6. // 创建XComponentController
7. mXComponentController: XComponentController = new XComponentController;

9. build() {
10. Flex() {
11. // Create XComponent
12. XComponent({
13. id: '',
14. type: 'surface',
15. libraryname: '',
16. controller: this.mXComponentController
17. })
18. .onLoad(() => {
19. // Set the width and height of the Surface (1920 * 1080), and set the preview size based on the preview resolution size supported
20. // by the current device obtained from previewProfilesArray earlier
21. this.mXComponentController.setXComponentSurfaceRect({surfaceWidth:1920,surfaceHeight:1080});
22. // Get Surface ID
23. let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
24. })
25. .width('1920px')
26. .height('1080px')
27. }
28. }
29. }
```

[GetSurface.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetSurface.ets#L42-L70)

4. 实现双路预览。

通过 `createPreviewOutput` 方法将步骤2和步骤3生成的两路 `SurfaceId` 传递到相机服务，创建两路预览流。其余流程按照正常预览流程开发。

```
1. import { camera } from '@kit.CameraKit';
2. import { image } from '@kit.ImageKit';

4. async function createDualChannelPreview(cameraManager: camera.CameraManager, XComponentSurfaceId: string, receiver: image.ImageReceiver): Promise<void> {
5. let camerasDevices: Array<camera.CameraDevice> = cameraManager.getSupportedCameras(); // 获取支持的相机设备对象

7. // Get profile object
8. let profiles: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(camerasDevices[0], camera.SceneMode.NORMAL_PHOTO); // 获取对应相机设备profiles
9. let previewProfiles: Array<camera.Profile> = profiles.previewProfiles;

11. // Preview Stream 1
12. let previewProfilesObj: camera.Profile = previewProfiles[0];

14. // Preview Stream 2
15. let previewProfilesObj2: camera.Profile = previewProfiles[0];

17. // Create preview stream 1 output object
18. let previewOutput: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfilesObj, XComponentSurfaceId);

20. // Create preview stream 2 output object
21. let imageReceiverSurfaceId: string = await receiver.getReceivingSurfaceId();
22. let previewOutput2: camera.PreviewOutput = cameraManager.createPreviewOutput(previewProfilesObj2, imageReceiverSurfaceId);

24. // Create cameraInput object
25. let cameraInput: camera.CameraInput = cameraManager.createCameraInput(camerasDevices[0]);

27. // Turn on the camera
28. await cameraInput.open();

30. // session flow
31. let captureSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);

33. // Start configuring session
34. captureSession.beginConfig();

36. // Add CameraInput to the conversation
37. captureSession.addInput(cameraInput);

39. // Add preview stream 1 to the session
40. captureSession.addOutput(previewOutput);

42. // Add preview stream 2 to the session
43. captureSession.addOutput(previewOutput2);

45. // Submit configuration information
46. await captureSession.commitConfig();

48. // session start
49. await captureSession.start();
50. }
```

[GetSurface4.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetSurface4.ets#L21-L70)

5. 通过ImageReceiver实时获取预览图像。

通过ImageReceiver组件的imageArrival事件监听获取底层返回的图像数据。有关详细的API说明，请参考Image API。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import image from '@ohos.multimedia.image';

4. function onImageArrival(receiver: image.ImageReceiver): void {
5. receiver.on('imageArrival', () => {
6. receiver.readNextImage((err: BusinessError, nextImage: image.Image) => {
7. if (err || nextImage === undefined) {
8. return;
9. }
10. // The current ImageReceiver does not support obtaining YUV data. You can use the JPEG data channel to receive YUV data, but using this method carries risks
11. nextImage.getComponent(image.ComponentType.JPEG, (err: BusinessError, imgComponent: image.Component) => {
12. if (err || imgComponent === undefined) {
13. return;
14. }
15. if (imgComponent.byteBuffer as ArrayBuffer) {
16. // Handle according to business demands
17. } else {
18. return;
19. }
20. })
21. })
22. })
23. }
```

[GetSurface5.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetSurface5.ets#L21-L43)

**参考链接**

[双路预览(ArkTS)](../harmonyos-guides/camera-dual-channel-preview.md)

[@ohos.multimedia.image (图片处理)](../harmonyos-references/js-apis-image.md)
