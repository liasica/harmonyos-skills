---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-focus-native
title: 对焦(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 对焦(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2b1ab98bd9433cf6baca123508baf9c2d6a8b575be77910543bea42021005995
---

相机框架提供对设备对焦的能力，业务应用可以根据使用场景进行对焦模式和对焦点的设置。

## 开发步骤

详细的API说明请参考[Camera API参考](../harmonyos-references/capi-capture-session-h.md)。

1. 导入NDK接口，导入方法如下。

   ```
   // 导入NDK接口头文件
   #include "hilog/log.h"
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/capture_session.h"
   #include "ohcamera/photo_output.h"
   #include "ohcamera/preview_output.h"
   #include "ohcamera/video_output.h"
   #include "ohcamera/camera_manager.h"
   ```
2. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
   ```
3. 调用[OH\_CaptureSession\_SetFocusMode](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setfocusmode)设置对焦模式。

   **说明** 

   * 需要先调用[OH\_CaptureSession\_IsFocusModeSupported](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_isfocusmodesupported)检查设备是否支持指定的焦距模式。
   * 需要在Session调用[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)完成配流之后调用。

   ```
   Camera_ErrorCode SetFocusMode(Camera_CaptureSession *captureSession, uint32_t mode)
   {
       bool isFocusModeSupported = false;
       Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
       Camera_ErrorCode ret = OH_CaptureSession_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
       if (&isFocusModeSupported == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
           return CAMERA_INVALID_ARGUMENT;
       }

       if (!isFocusModeSupported) {
           OH_LOG_INFO(LOG_APP, "current focusMode(%{public}d) is not supported.", focusMode);
           return CAMERA_OK;
       }

       OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFocusMode focusMode(%{public}d).", focusMode);
       ret = OH_CaptureSession_SetFocusMode(captureSession, focusMode);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "SetFocusMode failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       return ret;
   }
   ```
4. 如果通过[OH\_CaptureSession\_SetFocusMode](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setfocusmode)设置对焦模式为自动对焦模式，支持调用[OH\_CaptureSession\_SetFocusPoint](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setfocuspoint)设置对焦点，根据对焦点执行一次自动对焦。

   **说明** 

   需要在Session调用[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)完成配流之后调用。

   ```
   Camera_ErrorCode SetFocusPoint(Camera_CaptureSession *captureSession, float x, float y)
   {
       Camera_Point focusPoint;
       focusPoint.x = x;
       focusPoint.y = y;
       Camera_ErrorCode ret = OH_CaptureSession_SetFocusPoint(captureSession, focusPoint);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "SetFocusPoint failed.");
           return CAMERA_INVALID_ARGUMENT;
       }
       return ret;
   }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听相机聚焦的状态变化。

通过注册[OnFocusStateChange](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_onfocusstatechange)的回调函数获取监听结果，仅当自动对焦模式时，且相机对焦状态发生改变时触发该事件。

```
void CaptureSessionOnFocusStateChange(Camera_CaptureSession* captureSession, Camera_FocusState focusState)
    {
        OH_LOG_INFO(LOG_APP, "CaptureSession_Callbacks CaptureSessionOnFocusStateChange");
        OH_LOG_INFO(LOG_APP, "CaptureSession focusState = %{public}d", focusState);
        // 为保证对焦功能的用户体验，在自动对焦成功后，可将对焦模式设置为连续自动对焦
        if (focusState == Camera_FocusState::FOCUS_STATE_FOCUSED) {
            Camera_ErrorCode ret = SetFocusMode(captureSession, Camera_FocusMode::FOCUS_MODE_CONTINUOUS_AUTO);
        }
    }

    void CaptureSessionOnError(Camera_CaptureSession* captureSession, Camera_ErrorCode errorCode)
    {
        OH_LOG_INFO(LOG_APP, "CaptureSession_Callbacks CaptureSessionOnError");
        OH_LOG_INFO(LOG_APP, "CaptureSession errorCode = %{public}d", errorCode);
    }

    CaptureSession_Callbacks* GetCaptureSessionRegister(void)
    {
        static CaptureSession_Callbacks captureSessionCallbacks = {
            .onFocusStateChange = CaptureSessionOnFocusStateChange,
            .onError = CaptureSessionOnError
        };
        return &captureSessionCallbacks;
    }
```

```
Camera_ErrorCode RegisterCallback(Camera_CaptureSession* captureSession)
{
    Camera_ErrorCode ret = OH_CaptureSession_RegisterCallback(captureSession, GetCaptureSessionRegister());
    if (ret != CAMERA_OK) {
        OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.");
    }
    return ret;
}
```
