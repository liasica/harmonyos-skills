---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-system-pressure
title: 压力管控(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 压力管控(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cb6422c1f94722d8ea776de15a69401d55e4cd1c69bb3df432de723fcf656974
---

从API version 20开始，相机框架提供对系统压力等级的监听。

在长时间使用相机的场景（如直播业务）中，相机应用可以通过监听系统压力等级变化，动态调整画质（如帧率、分辨率等），平衡功耗、发热和系统负载，保证功能长时间可用。

## 状态监听

可以通过注册[OH\_CaptureSession\_OnSystemPressureLevelChange](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_onsystempressurelevelchange)的回调函数获取系统压力的监听结果。

当系统压力发生变化时，callback返回Camera\_SystemPressureLevel参数。

参数的具体内容可参考相机管理器回调接口实例[Camera\_SystemPressureLevel](../harmonyos-references/capi-camera-h.md#camera_systempressurelevel)。

```
1. void SystemPressureLevelChangeCallback(Camera_CaptureSession *captureSession,
2. Camera_SystemPressureLevel systemPressureLevel)
3. {
4. OH_LOG_INFO(LOG_APP, "SystemPressureLevelChangeCallback level: %{public}d", systemPressureLevel);
5. }

7. Camera_ErrorCode NDKCamera::RegisterSystemPressureCallback()
8. {
9. Camera_ErrorCode ret = OH_CaptureSession_RegisterSystemPressureLevelChangeCallback(
10. captureSession_, SystemPressureLevelChangeCallback);
11. if (ret != CAMERA_OK) {
12. OH_LOG_ERROR(LOG_APP,
13. "OH_CaptureSession_RegisterSystemPressureLevelChangeCallback failed.");
14. }
15. return ret;
16. }
```

[camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1544-L1561)
