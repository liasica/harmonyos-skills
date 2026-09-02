---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture
title: 分段式拍照(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 分段式拍照(C/C++)
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:45+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:be1b3652fe1e6d69976c3c98f59d50d02f87266fc7d89c2b2a893838b90a54d1
---

分段式拍照是相机的最重要功能之一，相机输出低质量图用作快速显示，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平，既满足了后处理算法的需求，又不阻塞前台的拍照速度，构筑相机性能竞争力，提升了用户的体验。

* 在第一阶段，系统快速上报轻量处理的图片，轻量处理的图片比全质量图低，出图速度快。应用通过回调会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。
* 在第二阶段，相机框架会根据应用的请求图片诉求或者在系统闲时，进行图像增强处理得到全质量图，将处理好的图片传回给媒体库，替换轻量处理的图片。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```c
   #include <cstdint>
   #include <unistd.h>
   #include <string>
   #include <thread>
   #include <cstdio>
   #include <fcntl.h>
   #include <map>
   #include <string>
   #include <vector>
   #include <native_buffer/native_buffer.h>
   #include "iostream"
   #include "mutex"

   #include "hilog/log.h"
   #include "ohcamera/camera.h"
   #include "ohcamera/camera_input.h"
   #include "ohcamera/capture_session.h"
   #include "ohcamera/photo_output.h"
   #include "ohcamera/preview_output.h"
   #include "ohcamera/video_output.h"
   #include "napi/native_api.h"
   #include "ohcamera/camera_manager.h"
   #include "common/log_common.h"

   #include "multimedia/image_framework/image/image_native.h"
   #include "multimedia/image_framework/image/image_source_native.h"
   #include "multimedia/image_framework/image/image_packer_native.h"
   #include "multimedia/media_library/media_access_helper_capi.h"
   #include "multimedia/media_library/media_asset_base_capi.h"
   #include "multimedia/media_library/media_asset_capi.h"
   #include "multimedia/media_library/media_asset_change_request_capi.h"
   #include "multimedia/media_library/media_asset_manager_capi.h"
   #include "multimedia/media_library/moving_photo_capi.h"
   #include "ohcamera/photo_native.h"
   #include <window_manager/oh_display_info.h>
   #include <window_manager/oh_display_manager.h>
   ```
2. 在CMake脚本中链接相关动态库。

   ```txt
   target_link_libraries(entry PUBLIC
       libace_napi.z.so
       libhilog_ndk.z.so
       libohcamera.so
       libimage_source.so
       libmedia_asset_manager.so
       libimage_packer.so
   )
   ```
3. 相机初始化及拍照触发参考[拍照(C/C++)](native-camera-shooting.md)。
4. 注册分段式（PhotoAssetAvailable）拍照回调，对比单段式拍照，仅注册的拍照回调接口不同。

   **注意** 

   如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册，会导致流被重启，仅PhotoAssetAvailable生效。

   不建议开发者同时注册PhotoAssetAvailable和PhotoAvailable。

   注册PhotoAssetAvailableCallback回调，接收分段式拍照回图示例：

   **分段式拍照开发流程（PhotoAssetAvailableCallback）**：

   * 在会话commitConfig前注册分段式拍照回调。
   * 通过分段式拍照回调，获取媒体库资源mediaAsset。
   * 通过mediaAsset直接落盘图片或者通过mediaAsset配置策略模式请求图像资源，业务处理后通过buffer保存图片，或显示图片(参考[拍照(C/C++)](native-camera-shooting.md)步骤5)。
   * 使用完后解注册分段式拍照回调函数。

   ```
   // 分段式拍照回调函数。
   void onPhotoAssetAvailable(Camera_PhotoOutput *photoOutput, OH_MediaAsset *mediaAsset)
   {
       if (mediaAsset == nullptr) {
           DRAWING_LOGI("onPhotoAssetAvailable mediaAsset is nullptr !");
           return;
       }
       DRAWING_LOGD("onPhotoAssetAvailable start!");
       NDKCamera::MediaAssetRelease();
       g_mediaAsset = mediaAsset;
       NDKCamera::MediaAssetGetUri(mediaAsset);
       NDKCamera::MediaAssetGetDisplayName(mediaAsset);
       NDKCamera::MediaAssetGetSize(mediaAsset);
       NDKCamera::MediaAssetGetDateModifiedMs(mediaAsset);
       NDKCamera::MediaAssetGetWidth(mediaAsset);
       NDKCamera::MediaAssetGetHeight(mediaAsset);
       NDKCamera::MediaAssetGetOrientation(mediaAsset);
       NDKCamera::MediaAssetManagerCreate();
       NDKCamera::MediaAssetChangeRequest(mediaAsset);
       DRAWING_LOGD("onPhotoAssetAvailable finish!");
       return;
   }

   // 注册分段式拍照回调。
   Camera_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback(void)
   {
       DRAWING_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback start!");
       MediaAssetManagerCreate();
       ret_ = OH_PhotoOutput_RegisterPhotoAssetAvailableCallback(photoOutput_, onPhotoAssetAvailable);
       if (ret_ != CAMERA_OK) {
           DRAWING_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback failed.");
       }
       DRAWING_LOGD(
           "NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback return with ret code: %{public}d!",
           ret_);
       return ret_;
   }

   MediaLibrary_ErrorCode NDKCamera::MediaAssetChangeRequest(OH_MediaAsset *mediaAsset)
   {
       DRAWING_LOGD("NDKCamera::MediaAssetChangeRequest start!");
       MediaAssetChangeRequestCreate(mediaAsset);
       MediaAssetManagerRequestImage(mediaAsset);
       DRAWING_LOGD("NDKCamera::MediaAssetChangeRequest finish!");
       return MEDIA_LIBRARY_OK;
   }

   MediaLibrary_ErrorCode NDKCamera::MediaAssetChangeRequestCreate(OH_MediaAsset *mediaAsset)
   {
       DRAWING_LOGD("NDKCamera::MediaAssetChangeRequestCreate start!");
       g_changeRequest = OH_MediaAssetChangeRequest_Create(mediaAsset);
       if (g_changeRequest == nullptr) {
           DRAWING_LOGD("NDKCamera::MediaAssetChangeRequestCreate failed.");
       }
       return MEDIA_LIBRARY_OK;
   }

   MediaLibrary_ErrorCode NDKCamera::MediaAssetManagerCreate(void)
   {
       DRAWING_LOGD("NDKCamera::MediaAssetManagerCreate start!");
       mediaAssetManager = OH_MediaAssetManager_Create();
       if (mediaAssetManager == nullptr) {
           DRAWING_LOGD("NDKCamera::MediaAssetManagerCreate failed.");
       }
       return MEDIA_LIBRARY_OK;
   }

   void OnRequestImageDataPreparedWithDetails(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId,
       MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type, OH_ImageSourceNative *imageSourceNative)
   {
       auto cb = (void (*)(char *))(g_requestImageCallback);
       auto qCb = (void (*)(char *))(g_requestImageQualityCallback);
       DRAWING_LOGD("OnRequestImageDataPreparedWithDetails start!");
       if (mediaQuality == MediaLibrary_MediaQuality::MEDIA_LIBRARY_QUALITY_FAST) {
           DRAWING_LOGD("OnRequestImageDataPreparedWithDetails into fast quality mode!");
           g_mediaQualityCb = "fast";
           qCb(g_mediaQualityCb);
       } else {
           DRAWING_LOGD("OnRequestImageDataPreparedWithDetails into high quality mode!");
           g_mediaQualityCb = "high";
           qCb(g_mediaQualityCb);
       }
       DRAWING_LOGD("OnRequestImageDataPreparedWithDetails GetUri uri_ = %{public}s", URI);
       cb(const_cast<char *>(URI));
       NDKCamera::ChangeRequestAddResourceWithBuffer(imageSourceNative);
       return;
   }

   // 请求图片数据：deliveryMode/quality等通过requestOptions控制，完成后进回调OnRequestImageDataPreparedWithDetails。
   MediaLibrary_ErrorCode NDKCamera::MediaAssetManagerRequestImage(OH_MediaAsset *mediaAsset)
   {
       DRAWING_LOGD("NDKCamera::MediaAssetManagerRequestImage start! g_deliveryMode = %{public}d",
           g_deliveryMode);
       requestOptions.deliveryMode = g_deliveryMode;
       result = OH_MediaAssetManager_RequestImage(mediaAssetManager, mediaAsset, requestOptions, &g_requestId,
           OnRequestImageDataPreparedWithDetails);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD("NDKCamera::MediaAssetManagerRequestImage failed.");
       }
       DRAWING_LOGD("NDKCamera::MediaAssetManagerRequestImage return with ret code: %{public}d!", result);
       return result;
   }

   MediaLibrary_ErrorCode NDKCamera::ChangeRequestAddResourceWithBuffer(OH_ImageSourceNative *imageSourceNative)
   {
       DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer start!");
       size_t bufferSize = BUFFER_SIZE;
       char buffer[BUFFER_SIZE];
       int fd = open("/data/storage/el2/base/haps/test.jpg", O_RDONLY);
       int fr = read(fd, buffer, bufferSize);
       if (fr == -1) {
           DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read failed.");
           return MEDIA_LIBRARY_OK;
       }
       if (fr == BUFFER_SIZE) {
           DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read not complete.");
           return MEDIA_LIBRARY_OK;
       }
       result = OH_MediaAssetChangeRequest_AddResourceWithBuffer(g_changeRequest,
           MediaLibrary_ResourceType::MEDIA_LIBRARY_IMAGE_RESOURCE, (uint8_t *)buffer, (uint32_t)bufferSize);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed.");
           DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed %{public}d.", result);
           return MEDIA_LIBRARY_OK;
       }
       result = OH_MediaAccessHelper_ApplyChanges(g_changeRequest);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD(
               "NDKCamera::ChangeRequestAddResourceWithBuffer OH_MediaAccessHelper_ApplyChanges failed.");
           return MEDIA_LIBRARY_OK;
       }
       DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer OH_MediaAccessHelper_ApplyChanges return "
                    "with ret code: %{public}d!",
           result);
       return result;
   }

   MediaLibrary_ErrorCode NDKCamera::ChangeRequestSaveCameraPhoto(void)
   {
       DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto start!");
       result = OH_MediaAssetChangeRequest_SaveCameraPhoto(g_changeRequest,
           MediaLibrary_ImageFileType::MEDIA_LIBRARY_IMAGE_JPEG);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD(
               "NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAssetChangeRequest_SaveCameraPhoto failed.");
       }
       DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAssetChangeRequest_SaveCameraPhoto "
                    "return with ret code: %{public}d!",
           result);
       result = OH_MediaAccessHelper_ApplyChanges(g_changeRequest);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAccessHelper_ApplyChanges failed.");
       }
       DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAccessHelper_ApplyChanges return with "
                    "ret code: %{public}d!",
           result);
       return result;
   }

   MediaLibrary_ErrorCode NDKCamera::ChangeRequestDiscardCameraPhoto(void)
   {
       DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto start!");
       result = OH_MediaAssetChangeRequest_DiscardCameraPhoto(g_changeRequest);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto "
                        "OH_MediaAssetChangeRequest_DiscardCameraPhoto failed.");
       }
       DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH_MediaAssetChangeRequest_DiscardCameraPhoto "
                    "return with ret code: %{public}d!",
           result);
       result = OH_MediaAccessHelper_ApplyChanges(g_changeRequest);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD(
               "NDKCamera::ChangeRequestDiscardCameraPhoto OH_MediaAccessHelper_ApplyChanges failed.");
       }
       DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH_MediaAccessHelper_ApplyChanges return with "
                    "ret code: %{public}d!",
           result);
       return result;
   }

   MediaLibrary_ErrorCode NDKCamera::ChangeRequestRelease(void)
   {
       DRAWING_LOGD("NDKCamera::ChangeRequestRelease start!");
       result = OH_MediaAssetChangeRequest_Release(g_changeRequest);
       if (result != MEDIA_LIBRARY_OK) {
           DRAWING_LOGD("NDKCamera::ChangeRequestRelease failed.");
       }
       g_changeRequest = nullptr;
       DRAWING_LOGD("NDKCamera::ChangeRequestRelease return with ret code: %{public}d!", result);
       return result;
   }
   ```
