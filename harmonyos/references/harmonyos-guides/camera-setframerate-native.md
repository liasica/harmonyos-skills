---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-setframerate-native
title: 动态调整预览帧率(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 动态调整预览帧率(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:10+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c78bf6566ffc355668d6e650ceb4c26e44e0d29a9d076df9f8eb4630a6f00184
---

动态调整帧率是直播、视频等场景下控制预览效果的重要能力之一。应用可通过此能力，显式地控制流输出帧率，以适应不同帧率下的业务目标。

某些场景下降低帧率可在相机设备启用时降低功耗。

## 约束与限制

支持的帧率范围及帧率的设置依赖于硬件能力的实现，不同的硬件平台可能拥有不同的默认帧率。

## 开发流程

相机使用预览功能前，均需要创建相机会话。完成会话配置后，应用提交和开启会话，才可以开始调用相机相关功能。

流程图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/kGVAHc46TEOw5kuxLy4Prg/zh-cn_image_0000002583438629.png?HW-CC-KV=V1&HW-CC-Date=20260427T234608Z&HW-CC-Expire=86400&HW-CC-Sign=81C0A7894CF91B0C59F61B830FD49C393EEAED1BF3294EEC89EB41C6A2DAE08E)

与普通的[预览](native-camera-preview.md)流程相比，动态调整预览帧率的注意点如图上标识：

1. 调用[OH\_CameraManager\_CreateCaptureSession](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createcapturesession)创建会话（Session）时，需要指定模式为NORMAL\_PHOTO或NORMAL\_VIDEO。

   仅当Session处于NORMAL\_PHOTO或NORMAL\_VIDEO模式时，支持调整预览流帧率。调整帧率的创建会话方式见[创建Session会话并指定模式](camera-setframerate-native.md#创建session会话并指定模式)。
2. [动态调整帧率](camera-setframerate-native.md#动态调整帧率)的操作，可在启动预览前后任意时刻调用。
3. [动态调整帧率](camera-setframerate-native.md#动态调整帧率)在预览里属于可选操作，可以完成：

   * 查询当前支持调整的帧率范围
   * 设置当前帧率
   * 获取当前生效的帧率设置

如何配置会话（Session）、释放资源，请参考[会话管理](native-camera-session-management.md) > [预览](native-camera-preview.md)。

## 导入模块

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

## 创建Session会话并指定模式

相机使用预览等功能前，均需创建相机会话，调用[OH\_CameraManager\_CreateCaptureSession](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createcapturesession)创建一个会话。

创建会话时调用[OH\_CaptureSession\_SetSessionMode](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_setsessionmode)指定[Camera\_SceneMode](../harmonyos-references/capi-camera-h.md#camera_scenemode)为NORMAL\_PHOTO或NORMAL\_VIDEO，创建出的Session处于拍照或录像模式。

以创建Session会话并指定为NORMAL\_PHOTO模式为例：

```
1. Camera_ErrorCode CreateCaptureSession(Camera_Manager *cameraManager, Camera_CaptureSession *captureSession) {
2. Camera_ErrorCode ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
3. if (captureSession == nullptr || ret != CAMERA_OK) {
4. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
5. }
6. // 设置会话模式为拍照或录像模式，此处以拍照模式为例
7. ret = OH_CaptureSession_SetSessionMode(captureSession, Camera_SceneMode::NORMAL_PHOTO);
8. return ret;
9. }
```

## 动态调整帧率

1. 调用[OH\_PreviewOutput\_GetSupportedFrameRates](../harmonyos-references/capi-preview-output-h.md#oh_previewoutput_getsupportedframerates)，查询当前previewOutput支持的帧率范围。

   说明

   **调用时机**：

   需要在Session调用[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)完成配流之后调用。

   **OH\_PreviewOutput\_GetSupportedFrameRates调用限制：**

   * 在调用OH\_PreviewOutput\_GetSupportedFrameRates接口设置非固定帧率后，不支持再次调用该接口重新设置动态帧率。
   * 在调用OH\_PreviewOutput\_GetSupportedFrameRates接口设置固定帧率后，支持重新设置固定帧率，但必须保证新设置的帧率可以整除之前设置的帧率或者被之前设置的帧率整除。

   ```
   1. Camera_ErrorCode PreviewOutputGetSupportedFrameRates(Camera_PreviewOutput* previewOutput,
   2. Camera_FrameRateRange** frameRateRange, uint32_t* size) {
   3. Camera_ErrorCode ret = OH_PreviewOutput_GetSupportedFrameRates(previewOutput, frameRateRange, size);

   5. if (ret != CAMERA_OK) {
   6. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_GetSupportedFrameRates failed.");
   7. return CAMERA_INVALID_ARGUMENT;
   8. }
   9. for (uint32_t i = 0; i < *size; i++) {
   10. OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates min %{public}d", (*frameRateRange)[i].min);
   11. OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetSupportedFrameRates: SupportedFrameRates max %{public}d", (*frameRateRange)[i].max);
   12. }
   13. return ret;
   14. }
   ```
2. 根据实际开发需求，调用[OH\_PreviewOutput\_SetFrameRate](../harmonyos-references/capi-preview-output-h.md#oh_previewoutput_setframerate)接口对帧率进行动态调整。

   说明

   * 需要在Session调用[OH\_CaptureSession\_CommitConfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_commitconfig)完成配流之后调用。
   * 可在Session调用[OH\_PreviewOutput\_Start](../harmonyos-references/capi-preview-output-h.md#oh_previewoutput_start)启动预览前后任意时刻调用。

   ```
   1. Camera_ErrorCode PreviewOutputSetFrameRate(Camera_PreviewOutput* previewOutput,
   2. uint32_t minFps, uint32_t maxFps){
   3. Camera_ErrorCode ret = OH_PreviewOutput_SetFrameRate(previewOutput, minFps, maxFps);
   4. if (ret != CAMERA_OK) {
   5. return CAMERA_INVALID_ARGUMENT;
   6. }
   7. return ret;
   8. }
   ```
3. （可选）通过[OH\_PreviewOutput\_GetActiveFrameRate](../harmonyos-references/capi-preview-output-h.md#oh_previewoutput_getactiveframerate)接口查询已设置过并生效的帧率。

   仅通过[OH\_PreviewOutput\_SetFrameRate](../harmonyos-references/capi-preview-output-h.md#oh_previewoutput_setframerate)接口显式设置过帧率才可查询当前生效帧率信息。

   ```
   1. Camera_ErrorCode PreviewOutputGetActiveFrameRate(Camera_PreviewOutput* previewOutput,
   2. Camera_FrameRateRange* frameRateRange){
   3. Camera_ErrorCode ret = OH_PreviewOutput_GetActiveFrameRate(previewOutput, frameRateRange);
   4. if (ret != CAMERA_OK) {
   5. return CAMERA_INVALID_ARGUMENT;
   6. }
   7. OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ min %{public}d", (*frameRateRange).min);
   8. OH_LOG_DEBUG(LOG_APP, "PreviewOutputGetActiveFrameRate: ActiveFrameRate frameRateRange_ max %{public}d", (*frameRateRange).max);
   9. return ret;
   10. }
   ```
