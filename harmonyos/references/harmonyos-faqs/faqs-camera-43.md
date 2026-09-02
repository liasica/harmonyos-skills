---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-43
title: 自定义相机在用户未授权的情况下，预览画面黑屏，用户点击拍照，应用闪退
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 自定义相机在用户未授权的情况下，预览画面黑屏，用户点击拍照，应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cf8de9e1b819a038b948597e5999158557ff1f2fc873f94b4a4fe719e40a72c3
---

## 问题现象

* 自定义相机在用户未授权的情况下，预览画面黑屏，用户点击拍照，应用闪退。jscrash报错如下：

  ```screen
  Reason:TypeError
  Error name:TypeError
  Error message:Cannot read property capture of undefined
  ```
* 申请相机相关资源代码：

  ```screen
  export async function cameraShooting(cameraPosition: number, surfaceId: string, context: Context, ratio: boolean):
    Promise<number[]> {
    currentContext = context;
    releaseCamera();
    let cameraManager: camera.CameraManager = camera.getCameraManager(context);
    // ... 
    let cameraArray: camera.CameraDevice[] = cameraManager.getSupportedCameras();
    // ... 
    cameraInput = cameraManager.createCameraInput(cameraArray[cameraPosition]);
    await cameraInput.open();
    let cameraOutputCap: camera.CameraOutputCapability =
      cameraManager.getSupportedOutputCapability(cameraArray[cameraPosition], camera.SceneMode.NORMAL_PHOTO);
    // ... 
    let previewProfilesArray: camera.Profile[] = cameraOutputCap.previewProfiles;
    let photoProfilesArray: camera.Profile[] = cameraOutputCap.photoProfiles;
    previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
    // ... 
    photoOutPut = cameraManager.createPhotoOutput(photoProfile);
    // ... 
    setPhotoOutputCb(photoOutPut);
    photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
    // ... 
    photoSession.beginConfig();
    photoSession.addInput(cameraInput);
    photoSession.addOutput(previewOutput);
    photoSession.addOutput(photoOutPut);
    photoSession.setColorSpace(colorSpaceManager.ColorSpace.DISPLAY_P3);
    await photoSession.commitConfig();
    await photoSession.start();
  }
  ```
* 相机拍照相关代码参考如下：

  ```screen
  export function capture(isFront: boolean): void {
    let settings: camera.PhotoCaptureSetting = {
      quality: camera.QualityLevel.QUALITY_LEVEL_HIGH,
      rotation: camera.ImageRotation.ROTATION_0,
      mirror: isFront
    };
    photoOutPut.capture(settings);
  }
  ```

## 背景知识

* [相机管理](../harmonyos-guides/camera-overview.md)通过调用Camera Kit(相机服务)提供的接口可以开发相机应用，应用通过访问和操作相机硬件，实现基础操作，如预览、拍照和录像；还可以通过接口组合完成更多操作，如控制闪光灯和曝光时间、对焦或调焦等。
* [相机权限](../harmonyos-guides/camera-preparation.md)需要先申请相机相关权限，确保应用拥有访问相机硬件及其他功能的权限。

## 问题定位

1. 通过jscrash日志分析为camera.PhotoOutput没有capture属性。
2. 通过createCameraInput创建输入流为空，使用try-catch抛出错误Error: not allowed, because have no permission。

## 分析结论

1. 由于没有相机权限，无法创建相机输入流导致最终无法申请相机资源，执行createCameraInput会报错无法继续执行后续代码，最终导致photoOutPut拍照输出流为空。
2. 在拍照函数中没有进行判空，导致photoOutPut拍照输出流类为空时错误调用，最终引起jscrash问题。

## 修改建议

1. 在初始化相机时检查相机权限是否已授予，已授予才可以申请相机权限，并且申请相机资源时如果遇到异常抛出异常，详细代码可参考官网示例代码[自定义相机定时拍摄](../architecture-guides/capture_timer-0000002352218316.md)中index.ets文件的aboutToAppear和onPageShow函数中检查相机权限处理过程。
2. 在拍照时应进行判空保护防止异常发生，详细代码可以参考官网示例代码[自定义相机定时拍摄](../architecture-guides/capture_timer-0000002352218316.md)中CameraUtils.ets文件中的capture函数对变量photoOutPut进行判空。

## 总结

1. 在申请相机资源时必须确保应用获取相机权限，否则相机在创建输入流时会异常，无法执行后续申请资源操作。
2. jscrash发生情况可以通过日志查看，其中一种情况为类为空时，调用类中属性会直接导致应用崩溃，在使用过程中一定要进行类判空保护。
