---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-metadata
title: 元数据(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 元数据(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b23c21812d96ad023877768ec8fb87548dad3186bcdfdbf9f8baf719113b899f
---

元数据（Metadata）是对相机返回的图像信息的描述和上下文。针对图像信息，提供更详细的数据，如照片或视频中，识别人像的取景框坐标等信息。

Metadata主要是通过一个TAG（Key），去找对应的Data（Value），用于传递参数和配置信息，减少内存拷贝操作。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，导入方法如下。

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
3. 调用OH\_CameraManager\_GetSupportedCameraOutputCapability()方法，获取当前设备支持的元数据类型metaDataObjectType，并通过OH\_CameraManager\_CreateMetadataOutput()方法创建元数据输出流。

   ```
   1. Camera_ErrorCode NDKCamera::CreateMetadataOutput(void)
   2. {
   3. metaDataObjectType_ = cameraOutputCapability_->supportedMetadataObjectTypes[0];
   4. if (metaDataObjectType_ == nullptr) {
   5. OH_LOG_ERROR(LOG_APP, "Get metaDataObjectType failed.");
   6. return CAMERA_INVALID_ARGUMENT;
   7. }
   8. ret_ = OH_CameraManager_CreateMetadataOutput(cameraManager_, metaDataObjectType_, &metadataOutput_);
   9. if (metadataOutput_ == nullptr || ret_ != CAMERA_OK) {
   10. OH_LOG_ERROR(LOG_APP, "CreateMetadataOutput failed.");
   11. return CAMERA_INVALID_ARGUMENT;
   12. }
   13. MetadataOutputRegisterCallback();
   14. return ret_;
   15. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L544-L560)
4. 调用[OH\_CameraManager\_CreateCaptureSession()](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createcapturesession)方法创建一个会话。

   ```
   1. ret = OH_CameraManager_CreateCaptureSession(cameraManager_, &captureSession_);
   2. if (captureSession_ == nullptr || ret != CAMERA_OK) {
   3. OH_LOG_ERROR(LOG_APP, "Create captureSession failed.");
   4. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L71-L76)
5. 配置session，完成后通过调用[OH\_CaptureSession\_Start()](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_start)方法输出metadata数据。接口调用失败会返回相应错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

   ```
   1. // 开始配置会话。
   2. Camera_ErrorCode ret = OH_CaptureSession_BeginConfig(captureSession_);

   4. // 将相机输入流加入会话。
   5. ret = OH_CaptureSession_AddInput(captureSession_, cameraInput_);

   7. // 将相机预览流加入会话。
   8. ret = OH_CaptureSession_AddPreviewOutput(captureSession_, previewOutput_);

   10. if (isVideo_) {
   11. // 将相机录像流加入会话。
   12. AddVideoOutput();
   13. if (isHdrVideo) {
   14. // HDR Vivid视频需要设置色彩空间为OH_COLORSPACE_BT2020_HLG_LIMIT。
   15. OH_NativeBuffer_ColorSpace colorSpace = OH_NativeBuffer_ColorSpace::OH_COLORSPACE_BT2020_HLG_LIMIT;
   16. SetColorSpace(colorSpace);
   17. }
   18. } else {
   19. // 将相机拍照流加入会话。
   20. AddPhotoOutput();
   21. ret = CreateMetadataOutput();
   22. ret = OH_CaptureSession_AddMetadataOutput(captureSession_, metadataOutput_);
   23. OH_NativeBuffer_ColorSpace colorSpace = OH_NativeBuffer_ColorSpace::OH_COLORSPACE_P3_FULL;
   24. SetColorSpace(colorSpace);
   25. }

   27. // 提交会话配置信息。
   28. ret = OH_CaptureSession_CommitConfig(captureSession_);
   29. // ...

   31. InitPreviewRotation();
   32. // 开始会话。
   33. OH_LOG_INFO(LOG_APP, "session start");
   34. ret = OH_CaptureSession_Start(captureSession_);
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L263-L311)
6. 调用stop()方法停止输出metadata数据，接口调用失败会返回相应错误码。

   ```
   1. Camera_ErrorCode StopMetadataOutput(Camera_MetadataOutput* metadataOutput)
   2. {
   3. Camera_ErrorCode ret = OH_MetadataOutput_Stop(metadataOutput);
   4. if (ret != CAMERA_OK) {
   5. OH_LOG_ERROR(LOG_APP, "OH_MetadataOutput_Stop failed.");
   6. }
   7. return ret;
   8. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听metadata数据以及输出流的状态。

* 通过注册监听获取metadata对象，监听事件固定为metadataObjectsAvailable。检测到有效metadata数据时，callback返回相应的metadata数据信息，metadataOutput创建成功时可监听。

  ```
  1. void OnMetadataObjectAvailable(Camera_MetadataOutput *metadataOutput, Camera_MetadataObject *metadataObject,
  2. uint32_t size)
  3. {
  4. OH_LOG_INFO(LOG_APP, "size = %{public}d", size);
  5. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1264-L1270)

  说明

  当前的元数据类型仅支持人脸检测（FACE\_DETECTION）功能。元数据信息对象为识别到的人脸区域的矩形信息（Rect），包含矩形区域的左上角x坐标、y坐标和矩形的宽高数据。
* 通过注册回调函数，获取监听metadata流的错误结果，callback返回metadata输出接口使用错误时返回的错误码，错误码类型参见[Camera\_ErrorCode](../harmonyos-references/capi-camera-h.md#camera_errorcode)。

  ```
  1. void OnMetadataOutputError(Camera_MetadataOutput *metadataOutput, Camera_ErrorCode errorCode)
  2. {
  3. OH_LOG_INFO(LOG_APP, "OnMetadataOutput errorCode = %{public}d", errorCode);
  4. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1272-L1277)

  ```
  1. MetadataOutput_Callbacks *NDKCamera::GetMetadataOutputListener(void)
  2. {
  3. static MetadataOutput_Callbacks metadataOutputListener = {
  4. .onMetadataObjectAvailable = OnMetadataObjectAvailable,
  5. .onError = OnMetadataOutputError
  6. };
  7. return &metadataOutputListener;
  8. }

  10. Camera_ErrorCode NDKCamera::MetadataOutputRegisterCallback(void)
  11. {
  12. ret_ = OH_MetadataOutput_RegisterCallback(metadataOutput_, GetMetadataOutputListener());
  13. if (ret_ != CAMERA_OK) {
  14. OH_LOG_ERROR(LOG_APP, "OH_MetadataOutput_RegisterCallback failed.");
  15. }
  16. return ret_;
  17. }
  ```

  [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKPhotoVideoSample/entry/src/main/cpp/camera_manager.cpp#L1279-L1297)
