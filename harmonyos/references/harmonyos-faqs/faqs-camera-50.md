---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-camera-50
title: 设备熄屏或者应用退后台能否继续维持相机录制状态
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 相机开发（Camera） > 设备熄屏或者应用退后台能否继续维持相机录制状态
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:41+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4b59edc3c7bda45b29dbf4053f1dd41277a22f11a8b2448be31a6233f089a5e0
---

## 问题现象

在应用退到后台或者设备熄屏状态下，相机录制就会停止，闪光灯也会关闭，请问这种情况如何处理？如何能够在这种场景下维持相机的录制状态？

## 背景知识

出于隐私保护的考虑，相机模块会注册监听隐私的回调，在应用退后台或者设备熄屏状态下，如果应用未主动关闭相机，隐私会通知相机模块主动释放相机资源。在主动释放相机资源的过程中，也会关闭闪光灯等资源。

## 问题定位

1. hilog日志中通过关键词“C02B0”搜索相机框架相关日志：

   ```txt
   01-15 09:52:56.073   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {Release():1401} HStreamOperator::Release execute success
   01-15 09:52:56.073   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {~AudioCapturerSession()-audio_capturer_session.cpp:96} ~AudioCapturerSession enter
   01-15 09:52:56.073   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {Stop()-audio_capturer_session.cpp:199} Audio capture stop enter
   01-15 09:52:56.073   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {Stop()-audio_capturer_session.cpp:207} Audio capture stop out
   01-15 09:52:56.073   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {Release()-audio_capturer_session.cpp:215} current audioCapturer is nullptr
   01-15 09:52:56.073   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {Release()-audio_capturer_session.cpp:223} Audio capture released
   01-15 09:52:56.076   48280-48280   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  I     {GetLensEquivalentFocalLength():400} CameraDevice::GetLensEquivalentFocalLength, lensEquivalentFocalLength size: 3, lensEquivalentFocalLength: [13,24,90]
   01-15 09:52:56.076   48280-48280   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  I     {operator()():244} CameraId: device/0, CameraStatus: 2
   01-15 09:52:56.084   1706-2569     C02B02/camera_...ce/CAMERA_DPS  camera_service        I     {SetDefaultExecutionMode():211} DPS_PHOTO: SetDefaultExecutionMode to ive, ret: 0
   01-15 09:52:56.084   1706-2569     C02B02/camera_...ce/CAMERA_DPS  camera_service        I     {ReevaluateSchedulerInfo():308} DPS_EVENT: Video stop schedule, hdi: 0, mediaLibrary: 0, camera: 0, screen: 1, temperature: 0, photoRunning: 0
   01-15 09:52:56.084   1706-2569     C02B02/camera_...ce/CAMERA_DPS  camera_service        I     {OnSchedulerChanged():106} DPS_VIDEO: Video isNeedStop: 1, isCharging: 1
   01-15 09:52:56.129   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {OnFlashlightStatus_V1_2():681} CameraHostInfo::OnFlashlightStatus_V1_2, torch status is off
   01-15 09:52:56.129   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {OnFlashlightStatus_V1_2():681} CameraHostInfo::OnFlashlightStatus_V1_2, torch status is off
   01-15 09:52:56.129   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {OnTorchStatus():1235} HCameraService::OnTorchtStatus callbacks.size = 2, status = 0, pid = 1001
   01-15 09:52:56.129   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {OnTorchStatus():1235} HCameraService::OnTorchtStatus callbacks.size = 2, status = 0, pid = 1001
   01-15 09:52:56.129   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {OnTorchStatus():1235} HCameraService::OnTorchtStatus callbacks.size = 2, status = 0, pid = 1001
   01-15 09:52:56.130   5747-5747     A01B06/com.ohos.sceneboard/KG   com.ohos.sceneboard   I     QuickTool-FlashUtil: onTorchStatusChange torchLevel:0,isTorchAvailable:true
   01-15 09:52:56.130   5747-5747     A01B06/com.ohos.sceneboard/KG   com.ohos.sceneboard   I     QuickTool-FlashUtil: onTorchStatusChange torchLevel:0,isTorchAvailable:true
   01-15 09:52:56.130   5747-5747     A01B06/com.ohos.sceneboard/KG   com.ohos.sceneboard   I     QuickTool-FlashUtil: onTorchStatusChange torchLevel:0,isTorchAvailable:true
   01-15 09:52:56.130   5747-5747     C02B01/com.oho...eboard/CAMERA  com.ohos.sceneboard   I     {GetTorchMode():2051} GetTorchMode is called
   01-15 09:52:56.130   5747-5747     C02B01/com.oho...eboard/CAMERA  com.ohos.sceneboard   I     {GetTorchMode():2051} GetTorchMode is called
   01-15 09:52:56.130   5747-5747     C02B01/com.oho...eboard/CAMERA  com.ohos.sceneboard   I     {GetTorchMode():2051} GetTorchMode is called
   ```

   从上述日志可以看出，是相机模块调用了Release()方法释放相机资源，在这一过程中也释放了闪光灯资源，并重置了闪光灯的状态。
2. 正常情况下，相机框架只会在应用退后台或者设备熄屏状态下才会主动释放应用的相机资源，因此继续向上查找“StateChangeNotify”关键词：

   ```txt
   01-15 09:52:55.412   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {StateChangeNotify():88} CameraUseStateChangeCb::StateChangeNotify is called, isShowing: 0
   01-15 09:52:55.412   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {StateChangeNotify():100} CameraUseStateChangeCb::StateChangeNotify ClientName: com.example.customcamera, isSystemCamera: 0
   01-15 09:52:55.509   48280-48280   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  I     {GetPreviewRotation():867} PreviewOutput GetPreviewRotation is called, imageRotation: 0
   01-15 09:52:55.509   48280-48280   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  I     {GetPreviewRotation():891} PreviewOutput GetPreviewRotation :result 90, sensorOrientation:90
   01-15 09:52:55.509   48280-48280   C02B01/com.exa...camera/CAMERA  com.examp...omcamera  I     {GetPreviewRotation():916} PreviewOutputNapi GetPreviewRotation! 90
   01-15 09:52:55.912   1706-1706     C02B01/camera_service/CAMERA    camera_service        I     {StateChangeNotify():102} CameraUseStateChangeCb::StateChangeNotify wait timeout
   ```

   从上述日志可以看出，相机框架通过调用StateChangeNotify()方法检查应用状态，发现“wait timeout”后主动释放相机资源。

## 分析结论

相机退至后台运行或者设备熄屏状态下，相机模块会主动释放相机资源，这一过程中会顺带关闭闪光灯。

## 修改建议

应用退后台或者设备熄屏时，相机模块释放相机资源的动作是出于对用户隐私保护的考虑，无法绕过。

开发者可以通过[ApplicationContext.on('applicationStateChange')](../harmonyos-references/js-apis-inner-application-applicationcontext.md#applicationcontextonapplicationstatechange10)接口注册应用进程状态变化的监听，在onApplicationBackground事件中主动停止录制并释放相机资源，在onApplicationForeground事件中再重新启动相机资源恢复录制。
