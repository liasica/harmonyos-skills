---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-macro
title: 微距能力设置(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 微距能力设置(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0180af3405f824c20fb3f3cd957be43c149dde5171106c5bbf0711d67c8cf589
---

从API version 19开始，支持设置微距能力。微距能力是指通过光学设计与算法优化，实现近距离对焦并清晰捕捉微小物体细节的相机功能。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口。选择系统提供的NDK接口能力，导入NDK接口的方法如下。

   ```
   1. #include <cstdint>
   2. #include <native_buffer/buffer_common.h>
   3. #include <unistd.h>
   4. #include <string>
   5. #include <thread>
   6. #include <cstdio>
   7. #include <fcntl.h>
   8. #include <map>
   9. #include <string>
   10. #include <vector>
   11. #include <native_buffer/native_buffer.h>
   12. #include "iostream"
   13. #include "mutex"

   15. #include "hilog/log.h"
   16. #include "ohcamera/camera.h"
   17. #include "ohcamera/camera_input.h"
   18. #include "ohcamera/capture_session.h"
   19. #include "ohcamera/photo_output.h"
   20. #include "ohcamera/preview_output.h"
   21. #include "ohcamera/video_output.h"
   22. #include "napi/native_api.h"
   23. #include "ohcamera/camera_manager.h"
   24. #include <window_manager/oh_display_info.h>
   25. #include <window_manager/oh_display_manager.h>

   27. namespace OHOS_CAMERA_SAMPLE {
   28. class NDKCamera {
   29. public:
   30. struct CameraBuildingConfig {
   31. char *str;
   32. uint32_t focusMode;
   33. uint32_t cameraDeviceIndex;
   34. bool isVideo;
   35. bool isHdr;
   36. char *videoId;
   37. };
   38. ~NDKCamera();
   39. explicit NDKCamera(CameraBuildingConfig config);
   40. // ...
   41. };
   42. } // namespace OHOS_CAMERA_SAMPLE
   ```

   [camera\_manager.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.h#L18-L196)
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libohcamera.so
   4. libhilog_ndk.z.so
   5. )
   ```
3. 通过[OH\_CaptureSession\_IsMacroSupported()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_ismacrosupported)方法，检测当前设备是否支持微距能力。

   ```
   1. bool NDKCamera::IsMacroSupported(Camera_CaptureSession* captureSession)
   2. {
   3. // 判断设备是否支持微距能力。
   4. bool isMacroSupported = false;
   5. if (captureSession == nullptr) {
   6. OH_LOG_ERROR(LOG_APP, "IsMacroSupported: session is nullptr.");
   7. return isMacroSupported;
   8. }
   9. Camera_ErrorCode ret = OH_CaptureSession_IsMacroSupported(captureSession, &isMacroSupported);
   10. if (ret != CAMERA_OK) {
   11. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsMacroSupported failed.");
   12. }
   13. if (isMacroSupported) {
   14. OH_LOG_INFO(LOG_APP, "support macro capability.");
   15. } else {
   16. OH_LOG_ERROR(LOG_APP, "No support macro capability.");
   17. }
   18. return isMacroSupported;
   19. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L870-L890)
4. 使用[OH\_CaptureSession\_EnableMacro()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_enablemacro)方法开启或关闭微距能力。

   ```
   1. void NDKCamera::EnableMacro(bool isMacro)
   2. {
   3. OH_LOG_INFO(LOG_APP, "EnableMacro: isMacro is %{public}d", isMacro);
   4. if (IsMacroSupported(captureSession_)) {
   5. Camera_ErrorCode ret = OH_CaptureSession_EnableMacro(captureSession_, isMacro);
   6. if (ret != CAMERA_OK) {
   7. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_EnableMacro failed.");
   8. }
   9. }
   10. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L892-L903)

## 状态监听

从API version 20开始，支持监听微距能力是否发生改变。

通过[OH\_CaptureSession\_RegisterMacroStatusChangeCallback()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_registermacrostatuschangecallback)函数注册回调，返回监听结果。

```
1. void MacroStatusCallback(Camera_CaptureSession *captureSession, bool isMacroDetected)
2. {
3. OH_LOG_INFO(LOG_APP, "MacroStatusCallback isMacro: %{public}d", isMacroDetected);
4. }

6. // 注册回调函数。
7. Camera_ErrorCode NDKCamera::RegisterMacroStatusCallback()
8. {
9. Camera_ErrorCode ret = OH_CaptureSession_RegisterMacroStatusChangeCallback(captureSession_, MacroStatusCallback);
10. if (ret != CAMERA_OK) {
11. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterMacroStatusChangeCallback failed.");
12. }
13. return ret;
14. }

16. // 解注册
17. Camera_ErrorCode NDKCamera::UnregisterMacroStatusCallback()
18. {
19. Camera_ErrorCode ret = OH_CaptureSession_UnregisterMacroStatusChangeCallback(captureSession_, MacroStatusCallback);
20. if (ret != CAMERA_OK) {
21. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_UnregisterMacroStatusChangeCallback failed.");
22. }
23. return ret;
24. }
```

[camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1517-L1542)
