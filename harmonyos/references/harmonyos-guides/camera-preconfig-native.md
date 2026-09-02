---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preconfig-native
title: 使用相机预配置(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 使用相机预配置(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:28d7c1879e8911932c8308cfd57e1d5eb16764687300598903ca150e1fddc7e8
---

相机预配置（Preconfig），对常用的场景和分辨率进行了预配置集成，可简化开发相机应用流程，提高应用的开发效率。

开发者在开发相机应用时，在获取到CameraDevice之后，如果遵循通用流程开发，步骤较为繁琐。需要先查询当前相机在指定模式下所支持的各类输出的配置信息，拿到[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)之后，应用开发者还需要对里面的各类数据进行解析，筛选，找到自己需要的配置数据[Camera\_Profile](../harmonyos-references/capi-oh-camera-camera-profile.md)和[Camera\_VideoProfile](../harmonyos-references/capi-oh-camera-camera-videoprofile.md)。最后使用对应的Profile以及VideoProfile创建对应的[Camera\_PreviewOutput](../harmonyos-references/capi-oh-camera-camera-previewoutput.md)、[Camera\_PhotoOutput](../harmonyos-references/capi-oh-camera-camera-photooutput.md)以及[Camera\_VideoOutput](../harmonyos-references/capi-oh-camera-camera-videooutput.md)。

为了解决上述问题，优化应用开发流程，系统针对拍照、录像两类场景（即[Camera\_SceneMode](../harmonyos-references/capi-camera-h.md#camera_scenemode)为NORMAL\_PHOTO或NORMAL\_VIDEO），提供了[OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createpreviewoutputusedinpreconfig)、[OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createphotooutputusedinpreconfig)、[OH\_CameraManager\_CreateVideoOutputUsedInPreconfig](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createvideooutputusedinpreconfig)接口帮助开发者快速完成相机参数配置。推荐仅需要自定义拍照界面的无需开发专业相机应用的开发者，使用相机预配置功能快速开发应用。

## 规格说明

系统提供了4种预配置类型（[Camera\_PreconfigType](../harmonyos-references/capi-camera-h.md#camera_preconfigtype)），分别为PRECONFIG\_720P、PRECONFIG\_1080P、PRECONFIG\_4K、PRECONFIG\_HIGH\_QUALITY。以及3种画幅比例规格（[Camera\_PreconfigRatio](../harmonyos-references/capi-camera-h.md#camera_preconfigratio)），1:1画幅（PRECONFIG\_RATIO\_1\_1）、4:3画幅（PRECONFIG\_RATIO\_4\_3）、16:9画幅（PRECONFIG\_RATIO\_16\_9）。

**注意** 

由于不同的设备所支持的能力不同。使用相机预配置（preconfig）功能时，需要先调用[OH\_CaptureSession\_CanPreconfig](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_canpreconfig)或[OH\_CaptureSession\_CanPreconfigWithRatio](../harmonyos-references/capi-capture-session-h.md#oh_capturesession_canpreconfigwithratio)检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。

在不同的画幅比例下，其分辨率规格不同，详见下表。

* 普通拍照模式下的预览输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_HIGH\_QUALITY | 1440x1440 | 1920x1440 | 2560x1440 |
* 普通拍照模式下的拍照输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 2160x2160 | 2880x2160 | 3840x2160 |
  | PRECONFIG\_HIGH\_QUALITY | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
* 普通录像模式下的预览输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_HIGH\_QUALITY | 1080x1080 | 1440x1080 | 1920x1080 |
* 普通录像模式下的录像输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 720x720 | 960x720 | 1280x720 |
  | PRECONFIG\_1080P | 1080x1080 | 1440x1080 | 1920x1080 |
  | PRECONFIG\_4K | 2160x2160 | 2880x2160 | 3840x2160 |
  | PRECONFIG\_HIGH\_QUALITY | 2160x2160 | 2880x2160 | 3840x2160 |
* 普通录像模式下的拍照输出

  | 预配置类型PreconfigType | PRECONFIG\_RATIO\_1\_1 | PRECONFIG\_RATIO\_4\_3 | PRECONFIG\_RATIO\_16\_9 |
  | --- | --- | --- | --- |
  | PRECONFIG\_720P | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
  | PRECONFIG\_1080P | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
  | PRECONFIG\_4K | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |
  | PRECONFIG\_HIGH\_QUALITY | 跟随Sensor最大能力 | 跟随Sensor最大能力 | 跟随Sensor最大能力 |

## 开发示例

1. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
   ```
2. cpp侧导入NDK接口，并根据传入的SurfaceId进行拍照。

   ```cpp
   #include "hilog/log.h"
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/capture_session.h"
   #include "ohcamera/photo_output.h"
   #include "ohcamera/preview_output.h"
   #include "ohcamera/video_output.h"
   #include "ohcamera/camera_manager.h"
   class NDKCamera {
   public:
       NDKCamera(char *previewId, char *photoId);
   };

   void CaptureSessionOnFocusStateChange(Camera_CaptureSession *session, Camera_FocusState focusState) {
       OH_LOG_INFO(LOG_APP, "CaptureSessionOnFocusStateChange");
   }

   void CaptureSessionOnError(Camera_CaptureSession *session, Camera_ErrorCode errorCode) {
       OH_LOG_INFO(LOG_APP, "CaptureSessionOnError = %{public}d", errorCode);
   }

   CaptureSession_Callbacks *GetCaptureSessionRegister(void) {
       static CaptureSession_Callbacks captureSessionCallbacks = {.onFocusStateChange = CaptureSessionOnFocusStateChange,
                                                                  .onError = CaptureSessionOnError};
       return &captureSessionCallbacks;
   }

   void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput) {
       OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
   }

   void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount) {
       OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
   }

   void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode) {
       OH_LOG_INFO(LOG_APP, "PreviewOutputOnError = %{public}d", errorCode);
   }

   PreviewOutput_Callbacks *GetPreviewOutputListener(void) {
       static PreviewOutput_Callbacks previewOutputListener = {.onFrameStart = PreviewOutputOnFrameStart,
                                                               .onFrameEnd = PreviewOutputOnFrameEnd,
                                                               .onError = PreviewOutputOnError};
       return &previewOutputListener;
   }

   void OnCameraInputError(const Camera_Input *cameraInput, Camera_ErrorCode errorCode) {
       OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode = %{public}d", errorCode);
   }

   CameraInput_Callbacks *GetCameraInputListener(void) {
       static CameraInput_Callbacks cameraInputCallbacks = {.onError = OnCameraInputError};
       return &cameraInputCallbacks;
   }

   void CameraManagerStatusCallback(Camera_Manager *cameraManager, Camera_StatusInfo *status) {
       OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
   }

   CameraManager_Callbacks *GetCameraManagerListener() {
       static CameraManager_Callbacks cameraManagerListener = {.onCameraStatus = CameraManagerStatusCallback};
       return &cameraManagerListener;
   }

   NDKCamera::NDKCamera(char *previewId, char *photoId) {
       Camera_Manager *cameraManager = nullptr;
       Camera_Device *cameras = nullptr;
       Camera_CaptureSession *captureSession = nullptr;
       Camera_PreviewOutput *previewOutput = nullptr;
       Camera_PhotoOutput *photoOutput = nullptr;
       Camera_Input *cameraInput = nullptr;
       uint32_t size = 0;
       uint32_t cameraDeviceIndex = 0;
       char *previewSurfaceId = previewId;
       char *photoSurfaceId = photoId;
       // 创建CameraManager对象
       Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
       if (cameraManager == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraMananger failed.");
       }
       // 监听相机状态变化
       ret = OH_CameraManager_RegisterCallback(cameraManager, GetCameraManagerListener());
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
       }

       // 获取相机列表
       ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
       if (cameras == nullptr || size < 0 || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
       }

       // 创建相机输入流
       ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[cameraDeviceIndex], &cameraInput);
       if (cameraInput == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
       }

       // 监听cameraInput错误信息
       ret = OH_CameraInput_RegisterCallback(cameraInput, GetCameraInputListener());
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
       }

       // 打开相机
       ret = OH_CameraInput_Open(cameraInput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Open failed.");
       }

       // 创建会话
       ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
       if (captureSession == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
       }

       // 监听session错误信息
       ret = OH_CaptureSession_RegisterCallback(captureSession, GetCaptureSessionRegister());
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.");
       }

       // 查询Preconfig能力
       bool canPreconfigResult = false;
       ret = OH_CaptureSession_CanPreconfig(captureSession, PRECONFIG_1080P, &canPreconfigResult);
       if (ret != CAMERA_OK || !canPreconfigResult) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CanPreconfig failed.");
       }

       // 配置Preconfig
       ret = OH_CaptureSession_Preconfig(captureSession, PRECONFIG_1080P);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Preconfig failed.");
       }

       // 创建预览输出流,其中参数 previewSurfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
       ret = OH_CameraManager_CreatePreviewOutputUsedInPreconfig(cameraManager, previewSurfaceId, &previewOutput);
       if (previewOutput == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
       }

       // 监听预览输出错误信息
       ret = OH_PreviewOutput_RegisterCallback(previewOutput, GetPreviewOutputListener());
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
       }

       // 创建拍照输出流，其中参数 photoSurfaceId 参考上文 ImageReceiver获取的surface
       ret = OH_CameraManager_CreatePhotoOutputUsedInPreconfig(cameraManager, photoSurfaceId, &photoOutput);
       if (photoOutput == nullptr || ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePhotoOutput failed.");
       }

       // 开始配置会话
       ret = OH_CaptureSession_BeginConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
       }

       // 向会话中添加相机输入流
       ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
       }

       // 向会话中添加预览输出流
       ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
       }

       // 向会话中添加拍照输出流
       ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
       }

       // 提交会话配置
       ret = OH_CaptureSession_CommitConfig(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
       }

       // 启动会话
       ret = OH_CaptureSession_Start(captureSession);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
       }

       // 判断设备是否支持闪光灯
       Camera_FlashMode flashMode = FLASH_MODE_AUTO;
       bool hasFlash = false;
       ret = OH_CaptureSession_HasFlash(captureSession, &hasFlash);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_HasFlash failed.");
       }
       if (hasFlash) {
           OH_LOG_INFO(LOG_APP, "hasFlash success");
       } else {
           OH_LOG_ERROR(LOG_APP, "hasFlash fail");
       }
       // 检测闪光灯模式是否支持
       bool isSupported = false;
       ret = OH_CaptureSession_IsFlashModeSupported(captureSession, flashMode, &isSupported);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFlashModeSupported failed.");
       }
       if (isSupported) {
           OH_LOG_INFO(LOG_APP, "isFlashModeSupported success");
           // 设置闪光灯模式
           ret = OH_CaptureSession_SetFlashMode(captureSession, flashMode);
           if (ret == CAMERA_OK) {
               OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFlashMode success.");
           } else {
               OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFlashMode failed. %{public}d ", ret);
           }
           // 获取当前设备的闪光灯模式
           ret = OH_CaptureSession_GetFlashMode(captureSession, &flashMode);
           if (ret == CAMERA_OK) {
               OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFlashMode success. flashMode：%{public}d ", flashMode);
           } else {
               OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFlashMode failed. %d ", ret);
           }
       } else {
           OH_LOG_ERROR(LOG_APP, "isFlashModeSupported fail");
       }

       // 判断是否支持连续自动变焦模式
       Camera_FocusMode focusMode = FOCUS_MODE_CONTINUOUS_AUTO;
       bool isFocusModeSupported = false;
       ret = OH_CaptureSession_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFocusModeSupported failed.");
       }
       if (isFocusModeSupported) {
           OH_LOG_INFO(LOG_APP, "isFocusModeSupported success");
           ret = OH_CaptureSession_SetFocusMode(captureSession, focusMode);
           if (ret != CAMERA_OK) {
               OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFocusMode failed. %{public}d ", ret);
           }
           ret = OH_CaptureSession_GetFocusMode(captureSession, &focusMode);
           if (ret == CAMERA_OK) {
               OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFocusMode success. focusMode%{public}d ", focusMode);
           } else {
               OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFocusMode failed. %d ", ret);
           }
       } else {
           OH_LOG_ERROR(LOG_APP, "isFocusModeSupported fail");
       }

       // 获取相机支持的可变焦距比范围
       float minZoom;
       float maxZoom;
       ret = OH_CaptureSession_GetZoomRatioRange(captureSession, &minZoom, &maxZoom);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatioRange failed.");
       } else {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
                       minZoom, maxZoom);
       }
       // 设置变焦
       ret = OH_CaptureSession_SetZoomRatio(captureSession, maxZoom);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetZoomRatio success.");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetZoomRatio failed. %{public}d ", ret);
       }
       // 获取当前设备的变焦值
       ret = OH_CaptureSession_GetZoomRatio(captureSession, &maxZoom);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatio success. zoom：%{public}f ", maxZoom);
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatio failed. %{public}d ", ret);
       }

       // 无拍照设置进行拍照
       ret = OH_PhotoOutput_Capture(photoOutput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Capture success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Capture failed. %d ", ret);
       }

       // 停止当前会话
       ret = OH_CaptureSession_Stop(captureSession);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
       }

       // 释放相机输入流
       ret = OH_CameraInput_Close(cameraInput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CameraInput_Close success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Close failed. %d ", ret);
       }

       // 释放预览输出流
       ret = OH_PreviewOutput_Release(previewOutput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_PreviewOutput_Release success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_Release failed. %d ", ret);
       }

       // 释放拍照输出流
       ret = OH_PhotoOutput_Release(photoOutput);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Release success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Release failed. %d ", ret);
       }

       // 释放会话
       ret = OH_CaptureSession_Release(captureSession);
       if (ret == CAMERA_OK) {
           OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Release success ");
       } else {
           OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Release failed. %d ", ret);
       }

       // 资源释放
       ret = OH_CameraManager_DeleteSupportedCameras(cameraManager, cameras, size);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
       } else {
           OH_LOG_INFO(LOG_APP, "OH_CameraManager_DeleteSupportedCameras. ok");
       }

       ret = OH_Camera_DeleteCameraManager(cameraManager);
       if (ret != CAMERA_OK) {
           OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
       } else {
           OH_LOG_INFO(LOG_APP, "OH_Camera_DeleteCameraManager. ok");
       }
   }
   ```
