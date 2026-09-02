---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-avscreencapture-for-file-with-window
title: 使用AVScreenCapture实现窗口级录屏(C/C++)
breadcrumb: 指南 > 媒体 > Media Kit（媒体服务） > 媒体开发指导(C/C++) > 录制 > 使用AVScreenCapture实现窗口级录屏(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6aa4c6525e715c482a05c1917097b529b103083ad2c79b248b0d4168e037e1a6
---

从API version 10开始，开发者可通过AVScreenCapture模块的C API接口实现窗口/屏幕录屏，采集麦克风和设备的音视频源数据。

本开发指导以指定窗口录屏为例，介绍如何使用AVScreenCapture的C API实现精准窗口捕获。该方案聚焦特定窗口内容，避免全屏干扰，适用于教学演示、在线课程、会议记录及特定内容采集等场景。

* 方式一（推荐）：使用屏幕捕获Picker列表弹窗，选择期望录屏的窗口。使用[OH\_AVScreenCapture\_StrategyForPickerPopUp](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_strategyforpickerpopup)设置是否弹出屏幕捕获Picker。从API version 20开始，支持在PC/2in1设备上设置弹出屏幕捕获Picker；从API version 23开始，支持在Phone/Tablet设备上设置弹出屏幕捕获Picker。
* 方式二：录屏某个指定窗口，需要设置指定窗口ID。该场景下，启动录屏后，会弹出共享内容选择对话框。详细的API声明请参考[OH\_CaptureMode](../harmonyos-references/capi-native-avscreen-capture-base-h.md#oh_capturemode)中的OH\_CAPTURE\_SPECIFIED\_WINDOW模式。

## 申请权限

在开发此功能前，开发者应根据实际需求申请相关权限：

* 如果配置了采集麦克风音频数据，需[向用户申请授权](request-user-authorization.md)麦克风权限**ohos.permission.MICROPHONE**和申请[长时任务（ArkTS）](continuous-task.md)。
* 从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.TIMEOUT\_SCREENOFF\_DISABLE\_LOCK**，实现在屏幕熄灭但不锁屏的场景下，继续保持录屏的效果。配置方式请参见[声明权限](declare-permissions.md)。
* 从API version 22开始，在PC/2in1设备上对应用进行录屏时，可通过申请权限**ohos.permission.CUSTOM\_SCREEN\_RECORDING**，实现在录屏时不再弹出隐私警告弹窗。配置方式请参见[受限开放权限](restricted-permissions.md)。

## 开发步骤及注意事项

**在CMake脚本中链接动态库**

```c
target_link_libraries(entry PUBLIC libnative_avscreen_capture.so libability_runtime.so libnative_display_manager.so)
```

1. 添加头文件。

   ```c
   #include "hilog/log.h"
   #include "napi/native_api.h"
   #include <window_manager/oh_display_info.h>
   #include <window_manager/oh_display_manager.h>
   #include <AbilityKit/ability_runtime/application_context.h>
   #include <multimedia/player_framework/native_avscreen_capture.h>
   #include <multimedia/player_framework/native_avscreen_capture_base.h>
   #include <multimedia/player_framework/native_avscreen_capture_errors.h>
   #include <unistd.h>
   #include <fcntl.h>
   #include <string>
   ```
2. 调用[OH\_AVScreenCapture\_Create](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_create)方法创建AVScreenCapture实例g\_avCapture。

   ```
   g_avCapture = OH_AVScreenCapture_Create();
   ```
3. 调用[OH\_AVScreenCapture\_Init](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_init)方法配置屏幕录屏参数。

   创建AVScreenCapture实例capture后，可以设置录屏所需要的参数。

   ```
   void SetConfig02(OH_AVScreenCaptureConfig &config, OH_RecorderInfo &recorderInfo)
   {
       // 录屏时获取麦克风或者内录，内录参数必填，如果都设置了，内录和麦克风的参数设置需要一致。
       OH_AudioCaptureInfo micCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_MIC};

       OH_AudioCaptureInfo innerCapInfo = {.audioSampleRate = 48000, .audioChannels = 2, .audioSource = OH_ALL_PLAYBACK};
       // 录屏音频输出规格配置。audioBitrate保证输出文件的比特率为设置的预期比特率，和audioSampleRate无强关联。
       // 为保证音频质量，此处音频比特率取值128000。如果录屏内容以语音为主，不包含音乐、游戏音效等，可以降低为96000或48000。
       OH_AudioEncInfo audioEncInfo = {
           .audioBitrate = 128000,
           .audioCodecformat = OH_AAC_LC
       };

       // 获取屏幕信息。
       uint64_t displayId = 0;
       NativeDisplayManager_ErrorCode ret = OH_NativeDisplayManager_GetDefaultDisplayId(&displayId);

       NativeDisplayManager_DisplayInfo* displayInfo = nullptr;
       ret = OH_NativeDisplayManager_CreateDisplayById(displayId, &displayInfo);
       if (ret != DISPLAY_MANAGER_OK || !displayInfo) {
           return;
       }
       int32_t screenWidth = displayInfo->width;
       int32_t screenHeight = displayInfo->height;
       OH_NativeDisplayManager_DestroyDisplay(displayInfo);
       displayInfo = nullptr;
       OH_VideoCaptureInfo videoCapInfo = {
           .videoFrameWidth = screenWidth,
           .videoFrameHeight = screenHeight,
           .videoSource = OH_VIDEO_SOURCE_SURFACE_RGBA
       };

       OH_VideoEncInfo videoEncInfo = {
           .videoCodec = OH_H264,
           .videoBitrate = 2000000,
           .videoFrameRate = 30
       };

       OH_AudioInfo audioInfo = {
           .micCapInfo = micCapInfo,
           .innerCapInfo = innerCapInfo,
           .audioEncInfo = audioEncInfo
       };

       OH_VideoInfo videoInfo = {
           .videoCapInfo = videoCapInfo,
           .videoEncInfo = videoEncInfo
       };

       config = {
           .captureMode = OH_CAPTURE_HOME_SCREEN,
           .dataType = OH_CAPTURE_FILE, // 录屏数据类型，文件。
           .audioInfo = audioInfo,
           .videoInfo = videoInfo,
           .recorderInfo = recorderInfo // 录制文件信息。
       };
       // 设置状态回调函数、错误回调函数和录屏屏幕ID回调函数等。
       SetCallbackFile(g_avCapture);
   }
   ```

   方式一（推荐）：通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。

   ```
   // 通过弹出屏幕捕获Picker列表方式，选择已打开的应用窗口进行窗口级录屏。
   OH_AVScreenCapture_CaptureStrategy *strategy = OH_AVScreenCapture_CreateCaptureStrategy();
   OH_AVScreenCapture_StrategyForPickerPopUp(strategy, true);
   OH_AVScreenCapture_SetCaptureStrategy(g_avCapture, strategy);
   OH_AVScreenCapture_ReleaseCaptureStrategy(strategy);
   ```

   方式二：需传入期望录制的窗口ID进行录屏。

   ```
   // 如果期望录制单个窗口，需传入单个窗口ID；如果期望同时录制多个窗口，需传入期望录制的窗口ID列表。
   g_missionIds = {g_windowId}; // 指定录制的窗口ID。
   config.videoInfo.videoCapInfo.missionIDs = g_missionIds.data();
   config.videoInfo.videoCapInfo.missionIDsLen = static_cast<int32_t>(g_missionIds.size());
   config.captureMode = OH_CAPTURE_SPECIFIED_WINDOW; // 设置录屏模式为录制指定窗口。

   // 设置为false，代表录屏启动后不弹出系统Picker，弹出隐私提示弹窗。
   OH_AVScreenCapture_CaptureStrategy* strategy = OH_AVScreenCapture_CreateCaptureStrategy();
   OH_AVScreenCapture_StrategyForPickerPopUp(strategy, false);
   OH_AVScreenCapture_SetCaptureStrategy(g_avCapture, strategy);
   OH_AVScreenCapture_ReleaseCaptureStrategy(strategy);
   ```
4. 调用[OH\_AVScreenCapture\_StartScreenRecording](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_startscreenrecording)方法开始进行窗口级录屏。

   ```
   result = OH_AVScreenCapture_StartScreenRecording(g_avCapture);
   ```
5. 调用[OH\_AVScreenCapture\_StopScreenRecording](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_stopscreenrecording)方法停止录屏。

   ```
   result = OH_AVScreenCapture_StopScreenRecording(g_avCapture);
   ```
6. 调用[OH\_AVScreenCapture\_Release](../harmonyos-references/capi-native-avscreen-capture-h.md#oh_avscreencapture_release)方法销毁实例，释放资源。

   ```
   OH_AVScreenCapture_Release(g_avCapture);
   g_avCapture = nullptr;
   ```
