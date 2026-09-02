---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-system-pressure
title: 压力管控(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 压力管控(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fe4594c312f8411a93123c6317bc0a64c5f9f622157a9cd8e3dcea9caf4e3559
---

从API version 20开始，相机框架提供对系统压力等级的监听。

在长时间使用相机的场景（如直播业务）中，相机应用可以通过监听系统压力等级变化，动态调整画质（如帧率、分辨率等），平衡功耗、发热和系统负载，保证功能长时间可用。

## 状态监听

可以通过注册[OH\_CaptureSession\_OnSystemPressureLevelChange](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_onsystempressurelevelchange)的回调函数获取系统压力的监听结果。

当系统压力发生变化时，callback返回Camera\_SystemPressureLevel参数。

参数的具体内容可参考相机管理器回调接口实例[Camera\_SystemPressureLevel](../harmonyos-references/capi-camera-h.md#camera_systempressurelevel)。

```
void SystemPressureLevelChangeCallback(Camera_CaptureSession *captureSession,
    Camera_SystemPressureLevel systemPressureLevel)
{
    OH_LOG_INFO(LOG_APP, "SystemPressureLevelChangeCallback level: %{public}d", systemPressureLevel);
}

Camera_ErrorCode NDKCamera::RegisterSystemPressureCallback()
{
    Camera_ErrorCode ret = OH_CaptureSession_RegisterSystemPressureLevelChangeCallback(
        captureSession_, SystemPressureLevelChangeCallback);
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP,
            "OH_CaptureSession_RegisterSystemPressureLevelChangeCallback failed.");
    }
    return ret;
}
```
