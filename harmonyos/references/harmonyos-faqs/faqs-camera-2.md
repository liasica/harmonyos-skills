---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-2
title: 如何获取前置摄像头的预览图像
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 如何获取前置摄像头的预览图像
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:25+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5b2125d19e8e6c5b6256a6956fb0c83faf187542997d8177fddc49f7192b18cd
---

获取前置摄像头预览图像示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { camera } from '@kit.CameraKit';
3. import { common } from '@kit.AbilityKit';

5. const context = AppStorage.get("context") as common.UIAbilityContext;

7. @Entry
8. @Component
9. struct GetFrontCameraImage {
10. private xComponentController: XComponentController = new XComponentController();

12. async getCameraImage() {
13. // 1、Use the system camera framework camera module to obtain physical camera information.
14. let cameraManager = camera.getCameraManager(context);
15. let camerasInfo: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
16. // Detecting camera status
17. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
18. console.log(`camera : ${cameraStatusInfo.camera.cameraId}`);
19. console.log(`status : : ${cameraStatusInfo.status}`);
20. });
21. // 2、Create and start a physical camera input stream channel
22. // Set as front camera camera.CameraPosition.CAMERA_POSITION_FRONT
23. let frontCamera = camerasInfo.find(cam => cam.cameraPosition === camera.CameraPosition.CAMERA_POSITION_FRONT);
24. let cameraInput = cameraManager.createCameraInput(frontCamera);
25. await cameraInput.open();
26. // 3、Retrieve the physical camera information and query the output formats supported by the preview stream of the camera. Create a preview output channel by combining it with the surfaceId provided by XComponent
27. let outputCapability = cameraManager.getSupportedOutputCapability(frontCamera, camera.SceneMode.NORMAL_PHOTO);
28. let previewProfile = outputCapability.previewProfiles[0];
29. let surfaceId = this.xComponentController.getXComponentSurfaceId();
30. let previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
31. // 4、Create a camera session, add the camera input stream and preview output stream in the session, then start the session, and the preview image will be displayed on the XComponent component.
32. let captureSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
33. captureSession.beginConfig();
34. captureSession.addInput(cameraInput);
35. captureSession.addOutput(previewOutput);
36. captureSession.commitConfig()
37. captureSession.start();
38. }

40. build() {
41. Row() {
42. Column({ space: 20 }) {
43. XComponent({ id: 'xComponentId1', type: 'surface', controller: this.xComponentController })
44. .height(300)
45. Button('Turn on the camera')
46. .onClick(() => {
47. // Ensure that camera permissions have been obtained before calling
48. this.getCameraImage();
49. })
50. }
51. .width('100%')
52. }
53. .height('100%')
54. }
55. }
```

[GetFrontCameraImage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CameraKit/entry/src/main/ets/pages/GetFrontCameraImage.ets#L21-L75)

**参考链接**

[拍照实践(ArkTS)](../harmonyos-guides/camera-shooting-case.md)
