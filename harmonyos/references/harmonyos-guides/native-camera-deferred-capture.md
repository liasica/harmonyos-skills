---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-deferred-capture
title: 分段式拍照(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 分段式拍照(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c59a0e285ec913ad334d10f1134cecbc3e745e19268152376c1c7437319c7248
---

分段式拍照是相机的最重要功能之一，相机输出低质量图用作快速显示，提升用户感知拍照速度，同时使用高质量图保证最后的成图质量达到系统相机的水平，既满足了后处理算法的需求，又不阻塞前台的拍照速度，构筑相机性能竞争力，提升了用户的体验。

* 在第一阶段，系统快速上报轻量处理的图片，轻量处理的图片比全质量图低，出图速度快。应用通过回调会收到一个PhotoAsset对象，通过该对象可调用媒体库接口，读取图片或落盘图片。
* 在第二阶段，相机框架会根据应用的请求图片诉求或者在系统闲时，进行图像增强处理得到全质量图，将处理好的图片传回给媒体库，替换轻量处理的图片。

## 开发步骤

详细的API说明请参考[OH\_Camera](../harmonyos-references/capi-oh-camera.md)。

1. 导入NDK接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. #include <cstdint>
   2. #include <unistd.h>
   3. #include <string>
   4. #include <thread>
   5. #include <cstdio>
   6. #include <fcntl.h>
   7. #include <map>
   8. #include <string>
   9. #include <vector>
   10. #include <native_buffer/native_buffer.h>
   11. #include "iostream"
   12. #include "mutex"

   14. #include "hilog/log.h"
   15. #include "ohcamera/camera.h"
   16. #include "ohcamera/camera_input.h"
   17. #include "ohcamera/capture_session.h"
   18. #include "ohcamera/photo_output.h"
   19. #include "ohcamera/preview_output.h"
   20. #include "ohcamera/video_output.h"
   21. #include "napi/native_api.h"
   22. #include "ohcamera/camera_manager.h"
   23. #include "common/log_common.h"

   25. #include "multimedia/image_framework/image/image_native.h"
   26. #include "multimedia/image_framework/image/image_source_native.h"
   27. #include "multimedia/image_framework/image/image_packer_native.h"
   28. #include "multimedia/media_library/media_access_helper_capi.h"
   29. #include "multimedia/media_library/media_asset_base_capi.h"
   30. #include "multimedia/media_library/media_asset_capi.h"
   31. #include "multimedia/media_library/media_asset_change_request_capi.h"
   32. #include "multimedia/media_library/media_asset_manager_capi.h"
   33. #include "multimedia/media_library/moving_photo_capi.h"
   34. #include "ohcamera/photo_native.h"
   35. #include <window_manager/oh_display_info.h>
   36. #include <window_manager/oh_display_manager.h>
   ```

   [camera\_manager.h](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKDeferredCaptureSample/entry/src/main/cpp/camera_manager.h#L18-L55)
2. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libohcamera.so
   5. libimage_source.so
   6. libmedia_asset_manager.so
   7. libimage_packer.so
   8. )
   ```
3. 相机初始化及拍照触发参考[拍照(C/C++)](native-camera-shooting.md)。
4. 注册分段式（PhotoAssetAvailable）拍照回调，对比单段式拍照，仅注册的拍照回调接口不同。

   注意

   如果已经注册了PhotoAssetAvailable回调，并且在Session开始之后又注册了PhotoAvailable回调，PhotoAssetAvailable和PhotoAvailable同时注册，会导致流被重启，仅PhotoAssetAvailable生效。

   不建议开发者同时注册PhotoAssetAvailable和PhotoAvailable。

   注册PhotoAssetAvailableCallback回调，接收分段式拍照回图示例：

   **分段式拍照开发流程（PhotoAssetAvailableCallback）**：

   * 在会话commitConfig前注册分段式拍照回调。
   * 通过分段式拍照回调，获取媒体库资源mediaAsset。
   * 通过mediaAsset直接落盘图片或者通过mediaAsset配置策略模式请求图像资源，业务处理后通过buffer保存图片，或显示图片(参考[拍照(C/C++)](native-camera-shooting.md)步骤5)。
   * 使用完后解注册分段式拍照回调函数。

   ```
   1. // 分段式拍照回调函数。
   2. void onPhotoAssetAvailable(Camera_PhotoOutput *photoOutput, OH_MediaAsset *mediaAsset)
   3. {
   4. if (mediaAsset == nullptr) {
   5. DRAWING_LOGI("onPhotoAssetAvailable mediaAsset is nullptr !");
   6. return;
   7. }
   8. DRAWING_LOGD("onPhotoAssetAvailable start!");
   9. NDKCamera::MediaAssetRelease();
   10. g_mediaAsset = mediaAsset;
   11. NDKCamera::MediaAssetGetUri(mediaAsset);
   12. NDKCamera::MediaAssetGetDisplayName(mediaAsset);
   13. NDKCamera::MediaAssetGetSize(mediaAsset);
   14. NDKCamera::MediaAssetGetDateModifiedMs(mediaAsset);
   15. NDKCamera::MediaAssetGetWidth(mediaAsset);
   16. NDKCamera::MediaAssetGetHeight(mediaAsset);
   17. NDKCamera::MediaAssetGetOrientation(mediaAsset);
   18. NDKCamera::MediaAssetManagerCreate();
   19. NDKCamera::MediaAssetChangeRequest(mediaAsset);
   20. DRAWING_LOGD("onPhotoAssetAvailable finish!");
   21. return;
   22. }

   24. // 注册分段式拍照回调。
   25. Camera_ErrorCode NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback(void)
   26. {
   27. DRAWING_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback start!");
   28. MediaAssetManagerCreate();
   29. ret_ = OH_PhotoOutput_RegisterPhotoAssetAvailableCallback(photoOutput_, onPhotoAssetAvailable);
   30. if (ret_ != CAMERA_OK) {
   31. DRAWING_LOGD("NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback failed.");
   32. }
   33. DRAWING_LOGD(
   34. "NDKCamera::PhotoOutputRegisterPhotoAssetAvailableCallback return with ret code: %{public}d!",
   35. ret_);
   36. return ret_;
   37. }

   39. MediaLibrary_ErrorCode NDKCamera::MediaAssetChangeRequest(OH_MediaAsset *mediaAsset)
   40. {
   41. DRAWING_LOGD("NDKCamera::MediaAssetChangeRequest start!");
   42. MediaAssetChangeRequestCreate(mediaAsset);
   43. MediaAssetManagerRequestImage(mediaAsset);
   44. DRAWING_LOGD("NDKCamera::MediaAssetChangeRequest finish!");
   45. return MEDIA_LIBRARY_OK;
   46. }

   48. MediaLibrary_ErrorCode NDKCamera::MediaAssetChangeRequestCreate(OH_MediaAsset *mediaAsset)
   49. {
   50. DRAWING_LOGD("NDKCamera::MediaAssetChangeRequestCreate start!");
   51. g_changeRequest = OH_MediaAssetChangeRequest_Create(mediaAsset);
   52. if (g_changeRequest == nullptr) {
   53. DRAWING_LOGD("NDKCamera::MediaAssetChangeRequestCreate failed.");
   54. }
   55. return MEDIA_LIBRARY_OK;
   56. }

   58. MediaLibrary_ErrorCode NDKCamera::MediaAssetManagerCreate(void)
   59. {
   60. DRAWING_LOGD("NDKCamera::MediaAssetManagerCreate start!");
   61. mediaAssetManager = OH_MediaAssetManager_Create();
   62. if (mediaAssetManager == nullptr) {
   63. DRAWING_LOGD("NDKCamera::MediaAssetManagerCreate failed.");
   64. }
   65. return MEDIA_LIBRARY_OK;
   66. }

   68. void OnRequsetImageDataPreparedWithDetails(MediaLibrary_ErrorCode result, MediaLibrary_RequestId requestId,
   69. MediaLibrary_MediaQuality mediaQuality, MediaLibrary_MediaContentType type, OH_ImageSourceNative *imageSourceNative)
   70. {
   71. auto cb = (void (*)(char *))(g_requestImageCallback);
   72. auto qCb = (void (*)(char *))(g_requestImageQualityCallback);
   73. DRAWING_LOGD("OnRequsetImageDataPreparedWithDetails start!");
   74. if (mediaQuality == MediaLibrary_MediaQuality::MEDIA_LIBRARY_QUALITY_FAST) {
   75. DRAWING_LOGD("OnRequsetImageDataPreparedWithDetails into fast quality mode!");
   76. g_mediaQualityCb = "fast";
   77. qCb(g_mediaQualityCb);
   78. } else {
   79. DRAWING_LOGD("OnRequsetImageDataPreparedWithDetails into high quality mode!");
   80. g_mediaQualityCb = "high";
   81. qCb(g_mediaQualityCb);
   82. }
   83. DRAWING_LOGD("OnRequsetImageDataPreparedWithDetails GetUri uri_ = %{public}s", URI);
   84. cb(const_cast<char *>(URI));
   85. NDKCamera::ChangeRequestAddResourceWithBuffer(imageSourceNative);
   86. return;
   87. }

   89. // 请求图片数据：deliveryMode/quality等通过requestOptions控制，完成后进回调OnRequsetImageDataPreparedWithDetails。
   90. MediaLibrary_ErrorCode NDKCamera::MediaAssetManagerRequestImage(OH_MediaAsset *mediaAsset)
   91. {
   92. DRAWING_LOGD("NDKCamera::MediaAssetManagerRequestImage start! g_deliveryMode = %{public}d",
   93. g_deliveryMode);
   94. requestOptions.deliveryMode = g_deliveryMode;
   95. result = OH_MediaAssetManager_RequestImage(mediaAssetManager, mediaAsset, requestOptions, &g_requestId,
   96. OnRequsetImageDataPreparedWithDetails);
   97. if (result != MEDIA_LIBRARY_OK) {
   98. DRAWING_LOGD("NDKCamera::MediaAssetManagerRequestImage failed.");
   99. }
   100. DRAWING_LOGD("NDKCamera::MediaAssetManagerRequestImage return with ret code: %{public}d!", result);
   101. return result;
   102. }

   104. MediaLibrary_ErrorCode NDKCamera::ChangeRequestAddResourceWithBuffer(OH_ImageSourceNative *imageSourceNative)
   105. {
   106. DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer start!");
   107. size_t bufferSize = BUFFER_SIZE;
   108. char buffer[BUFFER_SIZE];
   109. int fd = open("/data/storage/el2/base/haps/test.jpg", O_RDONLY);
   110. int fr = read(fd, buffer, bufferSize);
   111. if (fr == -1) {
   112. DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read failed.");
   113. return MEDIA_LIBRARY_OK;
   114. }
   115. if (fr == BUFFER_SIZE) {
   116. DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer read not complete.");
   117. return MEDIA_LIBRARY_OK;
   118. }
   119. result = OH_MediaAssetChangeRequest_AddResourceWithBuffer(g_changeRequest,
   120. MediaLibrary_ResourceType::MEDIA_LIBRARY_IMAGE_RESOURCE, (uint8_t *)buffer, (uint32_t)bufferSize);
   121. if (result != MEDIA_LIBRARY_OK) {
   122. DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed.");
   123. DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer failed %{public}d.", result);
   124. return MEDIA_LIBRARY_OK;
   125. }
   126. result = OH_MediaAccessHelper_ApplyChanges(g_changeRequest);
   127. if (result != MEDIA_LIBRARY_OK) {
   128. DRAWING_LOGD(
   129. "NDKCamera::ChangeRequestAddResourceWithBuffer OH_MediaAccessHelper_ApplyChanges failed.");
   130. return MEDIA_LIBRARY_OK;
   131. }
   132. DRAWING_LOGD("NDKCamera::ChangeRequestAddResourceWithBuffer OH_MediaAccessHelper_ApplyChanges return "
   133. "with ret code: %{public}d!",
   134. result);
   135. return result;
   136. }

   138. MediaLibrary_ErrorCode NDKCamera::ChangeRequestSaveCameraPhoto(void)
   139. {
   140. DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto start!");
   141. result = OH_MediaAssetChangeRequest_SaveCameraPhoto(g_changeRequest,
   142. MediaLibrary_ImageFileType::MEDIA_LIBRARY_IMAGE_JPEG);
   143. if (result != MEDIA_LIBRARY_OK) {
   144. DRAWING_LOGD(
   145. "NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAssetChangeRequest_SaveCameraPhoto failed.");
   146. }
   147. DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAssetChangeRequest_SaveCameraPhoto "
   148. "return with ret code: %{public}d!",
   149. result);
   150. result = OH_MediaAccessHelper_ApplyChanges(g_changeRequest);
   151. if (result != MEDIA_LIBRARY_OK) {
   152. DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAccessHelper_ApplyChanges failed.");
   153. }
   154. DRAWING_LOGD("NDKCamera::ChangeRequestSaveCameraPhoto OH_MediaAccessHelper_ApplyChanges return with "
   155. "ret code: %{public}d!",
   156. result);
   157. return result;
   158. }

   160. MediaLibrary_ErrorCode NDKCamera::ChangeRequestDiscardCameraPhoto(void)
   161. {
   162. DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto start!");
   163. result = OH_MediaAssetChangeRequest_DiscardCameraPhoto(g_changeRequest);
   164. if (result != MEDIA_LIBRARY_OK) {
   165. DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto "
   166. "OH_MediaAssetChangeRequest_DiscardCameraPhoto failed.");
   167. }
   168. DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH_MediaAssetChangeRequest_DiscardCameraPhoto "
   169. "return with ret code: %{public}d!",
   170. result);
   171. result = OH_MediaAccessHelper_ApplyChanges(g_changeRequest);
   172. if (result != MEDIA_LIBRARY_OK) {
   173. DRAWING_LOGD(
   174. "NDKCamera::ChangeRequestDiscardCameraPhoto OH_MediaAccessHelper_ApplyChanges failed.");
   175. }
   176. DRAWING_LOGD("NDKCamera::ChangeRequestDiscardCameraPhoto OH_MediaAccessHelper_ApplyChanges return with "
   177. "ret code: %{public}d!",
   178. result);
   179. return result;
   180. }

   182. MediaLibrary_ErrorCode NDKCamera::ChangeRequestRelease(void)
   183. {
   184. DRAWING_LOGD("NDKCamera::ChangeRequestRelease start!");
   185. result = OH_MediaAssetChangeRequest_Release(g_changeRequest);
   186. if (result != MEDIA_LIBRARY_OK) {
   187. DRAWING_LOGD("NDKCamera::ChangeRequestRelease failed.");
   188. }
   189. g_changeRequest = nullptr;
   190. DRAWING_LOGD("NDKCamera::ChangeRequestRelease return with ret code: %{public}d!", result);
   191. return result;
   192. }
   ```

   [camera\_manager.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Camera/NDKDeferredCaptureSample/entry/src/main/cpp/camera_manager.cpp#L1654-L1847)
