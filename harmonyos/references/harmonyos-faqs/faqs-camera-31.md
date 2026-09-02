---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-31
title: 应用打开前置摄像头拍摄，点击闪光灯应用闪退
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 应用打开前置摄像头拍摄，点击闪光灯应用闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:805e52828fd931ce40ac2a59fcc1bd393d154b00484ef8c7a5a5cd7afdc7329f
---

## 问题现象

打开应用，点击证件照拍摄按钮，启用前置摄像头拍摄证件照，此时点击页面上的闪光灯按钮，应用闪退。

## 背景知识

* 在开发相机应用时，需要先[申请相机开发的权限](../harmonyos-guides/camera-preparation.md)。
* [7400102](../harmonyos-references/errorcode-camera.md#section7400102-非法操作)：未按照既定方式操作。
* [FlashMode](../harmonyos-references/arkts-apis-camera-e.md#flashmode)：枚举，闪光灯模式。
* [hasFlash](../harmonyos-references/arkts-apis-camera-flashquery.md#hasflash11)：检测是否有闪光灯，通过注册回调函数获取结果。
* [isFlashModeSupported](../harmonyos-references/arkts-apis-camera-flashquery.md#isflashmodesupported11)：检测闪光灯模式是否支持。
* [setFlashMode](../harmonyos-references/arkts-apis-camera-flash.md#setflashmode11)：设置闪光灯模式。
* [CameraStatusInfo](../harmonyos-references/arkts-apis-camera-i.md#camerastatusinfo)：相机管理器回调返回的接口实例，该实例存储相机状态信息。
* [CameraDevice](../harmonyos-references/arkts-apis-camera-i.md#cameradevice)：相机设备信息。其中cameraId表示相机ID。
* [CameraStatus](../harmonyos-references/arkts-apis-camera-e.md#camerastatus)：枚举，相机状态。

## 问题定位

1. 查看hilog日志，搜索"CameraStatus"、"cameraId"等关键词，根据相机ID"device/1"可以看到应用拉起的是前置摄像头，"status: 2"表示相机可用。

   ```txt
   -    07-23 15:06:48.685   34484-42959   C02B01/com.hm.example/CAMERA  com.hm.example  I     {HandleOnCameraStatusChanged():52} HCameraServiceCallbackStub::HandleOnCameraStatusChanged called, cameraId = device/1, status = 2, bundleName = com.hm.example
   -    07-23 15:06:48.685   34484-42959   C02B01/com.hm.example/CAMERA  com.hm.example  I     {OnCameraStatusChanged():236} OnCameraStatusChanged cameraId: device/1, status: 2
   -    07-23 15:06:48.686   34484-34484   C02B01/com.hm.example/CAMERA  com.hm.example  I     {OnCameraStatusCallback():249} CameraId: device/1, CameraStatus: 2
   -    07-23 15:06:48.686   34484-34484   A0FF00/com.hm.example/cameraDemo  com.hm.example  I     CameraService, cameraId: device/1,status: 2
   -    07-23 15:06:48.696   34484-34484   C02B01/com.hm.example/CAMERA  com.hm.example  I     {InitCameraInput():110} CameraInput::CameraInput Contructor Camera: device/1
   ```
2. 搜索"Click accepted"、"flash"等关键词，得到如下报错日志。
   * 可以看到首先在触发闪光灯按钮点击事件后，日志显示"hasFlash: false"和"isFlashModeSupported: false"，这表示前置摄像头无法使用后置的闪光灯补光。
   * 接着FlashingLightComponent组件中调用了CameraService类中的setFlashMode方法设置闪光灯模式为1，即闪光灯打开。
   * 然后打印异常信息和错误码7400102，该错误码表示未按照既定方式操作。

     ```txt
     07-23 14:08:35.664   62657-62657   C03951/com.hm.example/InputKeyFlow  com.hm.example  I     [(100000:100000:scope)] Click accepted, tag: Image
     07-23 14:08:35.665   62657-62657   A0FF00/com.hm.example/cameraDemo  com.hm.example  I     FlashingLightComponent, flashMode: 1
     07-23 14:08:35.665   62657-62657   A0FF00/com.hm.example/cameraDemo  com.hm.example  I     CameraService, hasFlash: false
     07-23 14:08:35.665   62657-62657   A0FF00/com.hm.example/cameraDemo  com.hm.example  I     CameraService, isFlashModeSupported: false
     07-23 14:08:35.666   62657-62657   C02B01/com.hm.example/CAMERA  com.hm.example  I     {SetFlashMode():1736} CameraSessionNapi::SetFlashMode mode:1
     07-23 14:08:35.666   62657-62657   C02B01/com.hm.example/CAMERA  com.hm.example  I     {GetMode():3021} CaptureSession GetMode currentMode_ = 1, guestMode_ = 0
     07-23 14:08:35.666   62657-62657   C02B01/com.hm.example/CAMERA  com.hm.example  I     {UpdateSetting():1320} CaptureSession::UpdateSetting No configuration to update
     07-23 14:08:35.666   62657-62657   C03F00/com.hm.example/ArkCompiler  com.hm.example  E     [default] [Call:3482] occur exception need return
     07-23 14:08:35.666   62657-62657   C03F00/com.hm.example/ArkCompiler  com.hm.example  E     [ecmascript] Pending exception before ExecutePendingJob called, in line:5346, exception details as follows:
     07-23 14:08:35.666   62657-62657   C03F00/com.hm.example/ArkCompiler  com.hm.example  E     Error: 
                                                                                                   Cannot get SourceMap info, dump raw stack:
                                                                                                       at hasFlashFn (entry|entry|1.0.0|src/main/ets/service/CameraService.ts:631:631)
                                                                                                       at anonymous (entry|entry|1.0.0|src/main/ets/components/FlashingLightComponent.ts:84:84)
     07-23 14:08:35.666   62657-62657   C03900/com.hm.example/Ace  com.hm.example  W     [(100000:100000:scope)] after call jsFunction hasError, empty: 0, caught: 1
     07-23 14:08:35.667   62657-62657   C01311/com.hm.example/AppMS  com.hm.example  I     [app_mgr_proxy.cpp:1291]called
     07-23 14:08:35.668   62657-62657   C01317/com.hm.example/AppKit  com.hm.example  E     [main_thread.cpp:1604]
                                                                                                   com.hm.example is about to exit due to RuntimeError
                                                                                                   Error type:Error
                                                                                                   Error name:Error
                                                                                                   Error message:
                                                                                                   Error code:7400102
                                                                                                   Stacktrace:
                                                                                                   Cannot get SourceMap info, dump raw stack:
                                                                                                       at hasFlashFn (entry|entry|1.0.0|src/main/ets/service/CameraService.ts:631:631)
                                                                                                       at anonymous (entry|entry|1.0.0|src/main/ets/components/FlashingLightComponent.ts:84:84)
                                                                                                       at (entry/src/main/ets/pages/camera/Camera.ets:25:0)
                                                                                                       at (entry/src/main/ets/pages/camera/Camera.ets:32:0)
                                                                                                       at (entry/src/main/ets/pages/camera/Camera.ets:191:0)
     ```
3. 查看相关代码，结合以上报错日志，发现问题出现在setFlashMode方法，而"com.hm.example is about to exit due to RuntimeError"表示应用闪退是因为运行时异常。

   ```ts
   // CameraService.ets
   hasFlashFn(flashMode: camera.FlashMode): void {
     // 检测是否有闪光灯
     let hasFlash = this.session?.hasFlash();
     console.info(`hasFlash success, hasFlash: ${hasFlash}`);
     // 检测闪光灯模式是否支持
     let isFlashModeSupported = this.session?.isFlashModeSupported(flashMode);
     console.info(`isFlashModeSupported success, isFlashModeSupported: ${isFlashModeSupported}`);
     // 设置闪光灯模式
     this.session?.setFlashMode(flashMode);
   }
   ```

## 分析结论

前置摄像头无法使用后置的闪光灯补光，点击闪光灯按钮时，应用没有判断是否支持闪光灯就设置闪光灯模式，也没有进行异常捕获，导致应用闪退。

## 修改建议

建议应用在进入相机页面时，对当前调用的是前置还是后置摄像头进行判断，如果是前置摄像头，可以采取以下措施：

* 页面不展示闪光灯按钮。
* 闪光灯按钮置灰，不可点击。
* 用户点击闪光灯按钮，应用提示“前置摄像头不支持闪光灯”。
* 在设置闪光灯模式前加入if条件判断逻辑。
* 给设置闪光灯模式的代码块加上try/catch语句用来捕获异常，防止应用闪退。

设置闪光灯可以参考[实现自定义相机功能](https://gitee.com/harmonyos_samples/CustomCamera)示例代码项目的[CameraManager.ets](https://gitee.com/harmonyos_samples/CustomCamera/blob/master/camera/src/main/ets/cameramanagers/CameraManager.ets)文件中的setFlashMode方法。
