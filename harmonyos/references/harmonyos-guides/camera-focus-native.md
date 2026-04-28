---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-focus-native
title: 对焦(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 对焦(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:da7447c0aaf6f4b45ad9ccbc880b72a31b6386c3e8adf331f67ec8e95327e76e
---

相机框架提供对设备对焦的能力，业务应用可以根据使用场景进行对焦模式和对焦点的设置。

## 开发步骤

详细的API说明请参考[Camera API参考](../harmonyos-references/capi-capture-session-h.md)。

1. 导入NDK接口，导入方法如下。

   ```
   1. // 导入NDK接口头文件
   2. #include "hilog/log.h"
   3. #include "ohcamera/camera.h"
   4. #include "ohcamera/camera_input.h"
   5. #include "ohcamera/capture_session.h"
   6. #include "ohcamera/photo_output.h"
   7. #include "ohcamera/preview_output.h"
   8. #include "ohcamera/video_output.h"
   9. #include "ohcamera/camera_manager.h"
   ```
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
   ```
3. 调用[OH\_CaptureSession\_SetFocusMode](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setfocusmode)设置对焦模式。

   说明

   * 需要先调用[OH\_CaptureSession\_IsFocusModeSupported](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_isfocusmodesupported)检查设备是否支持指定的焦距模式。
   * 需要在Session调用[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)完成配流之后调用。

   ```
   1. Camera_ErrorCode SetFocusMode(Camera_CaptureSession *captureSession, uint32_t mode)
   2. {
   3. bool isFocusModeSupported = false;
   4. Camera_FocusMode focusMode = static_cast<Camera_FocusMode>(mode);
   5. Camera_ErrorCode ret = OH_CaptureSession_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
   6. if (&isFocusModeSupported == nullptr || ret != CAMERA_OK) {
   7. OH_LOG_ERROR(LOG_APP, "IsFocusModeSupported failed.");
   8. return CAMERA_INVALID_ARGUMENT;
   9. }

   11. if (!isFocusModeSupported) {
   12. OH_LOG_INFO(LOG_APP, "current focusMode(%{public}d) is not supported.", focusMode);
   13. return CAMERA_OK;
   14. }

   16. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFocusMode focusMode(%{public}d).", focusMode);
   17. ret = OH_CaptureSession_SetFocusMode(captureSession, focusMode);
   18. if (ret != CAMERA_OK) {
   19. OH_LOG_ERROR(LOG_APP, "SetFocusMode failed.");
   20. return CAMERA_INVALID_ARGUMENT;
   21. }
   22. return ret;
   23. }
   ```
4. 如果通过[OH\_CaptureSession\_SetFocusMode](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setfocusmode)设置对焦模式为自动对焦模式，支持调用[OH\_CaptureSession\_SetFocusPoint](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setfocuspoint)设置对焦点，根据对焦点执行一次自动对焦。

   说明

   需要在Session调用[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)完成配流之后调用。

   ```
   1. Camera_ErrorCode SetFocusPoint(Camera_CaptureSession *captureSession, float x, float y)
   2. {
   3. Camera_Point focusPoint;
   4. focusPoint.x = x;
   5. focusPoint.y = y;
   6. Camera_ErrorCode ret = OH_CaptureSession_SetFocusPoint(captureSession, focusPoint);
   7. if (ret != CAMERA_OK) {
   8. OH_LOG_ERROR(LOG_APP, "SetFocusPoint failed.");
   9. return CAMERA_INVALID_ARGUMENT;
   10. }
   11. return ret;
   12. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听相机聚焦的状态变化。

通过注册[OnFocusStateChange](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_onfocusstatechange)的回调函数获取监听结果，仅当自动对焦模式时，且相机对焦状态发生改变时触发该事件。

```
1. void CaptureSessionOnFocusStateChange(Camera_CaptureSession* captureSession, Camera_FocusState focusState)
2. {
3. OH_LOG_INFO(LOG_APP, "CaptureSession_Callbacks CaptureSessionOnFocusStateChange");
4. OH_LOG_INFO(LOG_APP, "CaptureSession focusState = %{public}d", focusState);
5. // 为保证对焦功能的用户体验，在自动对焦成功后，可将对焦模式设置为连续自动对焦
6. if (focusState == Camera_FocusState::FOCUS_STATE_FOCUSED) {
7. Camera_ErrorCode ret = SetFocusMode(captureSession, Camera_FocusMode::FOCUS_MODE_CONTINUOUS_AUTO);
8. }
9. }

11. void CaptureSessionOnError(Camera_CaptureSession* captureSession, Camera_ErrorCode errorCode)
12. {
13. OH_LOG_INFO(LOG_APP, "CaptureSession_Callbacks CaptureSessionOnError");
14. OH_LOG_INFO(LOG_APP, "CaptureSession errorCode = %{public}d", errorCode);
15. }

17. CaptureSession_Callbacks* GetCaptureSessionRegister(void)
18. {
19. static CaptureSession_Callbacks captureSessionCallbacks = {
20. .onFocusStateChange = CaptureSessionOnFocusStateChange,
21. .onError = CaptureSessionOnError
22. };
23. return &captureSessionCallbacks;
24. }
```

```
1. Camera_ErrorCode RegisterCallback(Camera_CaptureSession* captureSession)
2. {
3. Camera_ErrorCode ret = OH_CaptureSession_RegisterCallback(captureSession, GetCaptureSessionRegister());
4. if (ret != CAMERA_OK) {
5. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.");
6. }
7. return ret;
8. }
```
