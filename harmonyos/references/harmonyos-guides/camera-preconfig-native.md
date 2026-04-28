---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preconfig-native
title: 使用相机预配置(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 使用相机预配置(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:10+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7054bdb4736980c933ba1d61a2440586fb6b6f9d5469eda86a5e333f6336a595
---

相机预配置（Preconfig），对常用的场景和分辨率进行了预配置集成，可简化开发相机应用流程，提高应用的开发效率。

开发者在开发相机应用时，在获取到CameraDevice之后，如果遵循通用流程开发，步骤较为繁琐。需要先查询当前相机在指定模式下所支持的各类输出的配置信息，拿到[Camera\_OutputCapability](../harmonyos-references/capi-oh-camera-camera-outputcapability.md)之后，应用开发者还需要对里面的各类数据进行解析，筛选，找到自己需要的配置数据[Camera\_Profile](../harmonyos-references/capi-oh-camera-camera-profile.md)和[Camera\_VideoProfile](../harmonyos-references/capi-oh-camera-camera-videoprofile.md)。最后使用对应的Profile以及VideoProfile创建对应的[Camera\_PreviewOutput](../harmonyos-references/capi-oh-camera-camera-previewoutput.md)、[Camera\_PhotoOutput](../harmonyos-references/capi-oh-camera-camera-photooutput.md)以及[Camera\_VideoOutput](../harmonyos-references/capi-oh-camera-camera-videooutput.md)。

为了解决上述问题，优化应用开发流程，系统针对拍照、录像两类场景（即[Camera\_SceneMode](../harmonyos-references/capi-camera-h.md#camera_scenemode)为NORMAL\_PHOTO或NORMAL\_VIDEO），提供了[OH\_CameraManager\_CreatePreviewOutputUsedInPreconfig](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createpreviewoutputusedinpreconfig)、[OH\_CameraManager\_CreatePhotoOutputUsedInPreconfig](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createphotooutputusedinpreconfig)、[OH\_CameraManager\_CreateVideoOutputUsedInPreconfig](../harmonyos-references/capi-camera-manager-h.md#oh_cameramanager_createvideooutputusedinpreconfig)接口帮助开发者快速完成相机参数配置。推荐仅需要自定义拍照界面的无需开发专业相机应用的开发者，使用相机预配置功能快速开发应用。

## 规格说明

系统提供了4种预配置类型（[Camera\_PreconfigType](../harmonyos-references/capi-camera-h.md#camera_preconfigtype)），分别为PRECONFIG\_720P、PRECONFIG\_1080P、PRECONFIG\_4K、PRECONFIG\_HIGH\_QUALITY。以及3种画幅比例规格（[Camera\_PreconfigRatio](../harmonyos-references/capi-camera-h.md#camera_preconfigratio)），1:1画幅（PRECONFIG\_RATIO\_1\_1）、4:3画幅（PRECONFIG\_RATIO\_4\_3）、16:9画幅（PRECONFIG\_RATIO\_16\_9）。

注意

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

   ```
   1. target_link_libraries(entry PUBLIC libohcamera.so libhilog_ndk.z.so)
   ```
2. cpp侧导入NDK接口，并根据传入的SurfaceId进行拍照。

   ```
   1. #include "hilog/log.h"
   2. #include "ohcamera/camera.h"
   3. #include "ohcamera/camera_input.h"
   4. #include "ohcamera/capture_session.h"
   5. #include "ohcamera/photo_output.h"
   6. #include "ohcamera/preview_output.h"
   7. #include "ohcamera/video_output.h"
   8. #include "ohcamera/camera_manager.h"
   9. class NDKCamera {
   10. public:
   11. NDKCamera(char *previewId, char *photoId);
   12. };

   14. void CaptureSessionOnFocusStateChange(Camera_CaptureSession *session, Camera_FocusState focusState) {
   15. OH_LOG_INFO(LOG_APP, "CaptureSessionOnFocusStateChange");
   16. }

   18. void CaptureSessionOnError(Camera_CaptureSession *session, Camera_ErrorCode errorCode) {
   19. OH_LOG_INFO(LOG_APP, "CaptureSessionOnError = %{public}d", errorCode);
   20. }

   22. CaptureSession_Callbacks *GetCaptureSessionRegister(void) {
   23. static CaptureSession_Callbacks captureSessionCallbacks = {.onFocusStateChange = CaptureSessionOnFocusStateChange,
   24. .onError = CaptureSessionOnError};
   25. return &captureSessionCallbacks;
   26. }

   28. void PreviewOutputOnFrameStart(Camera_PreviewOutput *previewOutput) {
   29. OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
   30. }

   32. void PreviewOutputOnFrameEnd(Camera_PreviewOutput *previewOutput, int32_t frameCount) {
   33. OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
   34. }

   36. void PreviewOutputOnError(Camera_PreviewOutput *previewOutput, Camera_ErrorCode errorCode) {
   37. OH_LOG_INFO(LOG_APP, "PreviewOutputOnError = %{public}d", errorCode);
   38. }

   40. PreviewOutput_Callbacks *GetPreviewOutputListener(void) {
   41. static PreviewOutput_Callbacks previewOutputListener = {.onFrameStart = PreviewOutputOnFrameStart,
   42. .onFrameEnd = PreviewOutputOnFrameEnd,
   43. .onError = PreviewOutputOnError};
   44. return &previewOutputListener;
   45. }

   47. void OnCameraInputError(const Camera_Input *cameraInput, Camera_ErrorCode errorCode) {
   48. OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode = %{public}d", errorCode);
   49. }

   51. CameraInput_Callbacks *GetCameraInputListener(void) {
   52. static CameraInput_Callbacks cameraInputCallbacks = {.onError = OnCameraInputError};
   53. return &cameraInputCallbacks;
   54. }

   56. void CameraManagerStatusCallback(Camera_Manager *cameraManager, Camera_StatusInfo *status) {
   57. OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
   58. }

   60. CameraManager_Callbacks *GetCameraManagerListener() {
   61. static CameraManager_Callbacks cameraManagerListener = {.onCameraStatus = CameraManagerStatusCallback};
   62. return &cameraManagerListener;
   63. }

   65. NDKCamera::NDKCamera(char *previewId, char *photoId) {
   66. Camera_Manager *cameraManager = nullptr;
   67. Camera_Device *cameras = nullptr;
   68. Camera_CaptureSession *captureSession = nullptr;
   69. Camera_PreviewOutput *previewOutput = nullptr;
   70. Camera_PhotoOutput *photoOutput = nullptr;
   71. Camera_Input *cameraInput = nullptr;
   72. uint32_t size = 0;
   73. uint32_t cameraDeviceIndex = 0;
   74. char *previewSurfaceId = previewId;
   75. char *photoSurfaceId = photoId;
   76. // 创建CameraManager对象
   77. Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
   78. if (cameraManager == nullptr || ret != CAMERA_OK) {
   79. OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraMananger failed.");
   80. }
   81. // 监听相机状态变化
   82. ret = OH_CameraManager_RegisterCallback(cameraManager, GetCameraManagerListener());
   83. if (ret != CAMERA_OK) {
   84. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
   85. }

   87. // 获取相机列表
   88. ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
   89. if (cameras == nullptr || size < 0 || ret != CAMERA_OK) {
   90. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
   91. }

   93. // 创建相机输入流
   94. ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[cameraDeviceIndex], &cameraInput);
   95. if (cameraInput == nullptr || ret != CAMERA_OK) {
   96. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
   97. }

   99. // 监听cameraInput错误信息
   100. ret = OH_CameraInput_RegisterCallback(cameraInput, GetCameraInputListener());
   101. if (ret != CAMERA_OK) {
   102. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
   103. }

   105. // 打开相机
   106. ret = OH_CameraInput_Open(cameraInput);
   107. if (ret != CAMERA_OK) {
   108. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Open failed.");
   109. }

   111. // 创建会话
   112. ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
   113. if (captureSession == nullptr || ret != CAMERA_OK) {
   114. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
   115. }

   117. // 监听session错误信息
   118. ret = OH_CaptureSession_RegisterCallback(captureSession, GetCaptureSessionRegister());
   119. if (ret != CAMERA_OK) {
   120. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.");
   121. }

   123. // 查询Preconfig能力
   124. bool canPreconfigResult = false;
   125. ret = OH_CaptureSession_CanPreconfig(captureSession, PRECONFIG_1080P, &canPreconfigResult);
   126. if (ret != CAMERA_OK || !canPreconfigResult) {
   127. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CanPreconfig failed.");
   128. }

   130. // 配置Preconfig
   131. ret = OH_CaptureSession_Preconfig(captureSession, PRECONFIG_1080P);
   132. if (ret != CAMERA_OK) {
   133. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Preconfig failed.");
   134. }

   136. // 创建预览输出流,其中参数 previewSurfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
   137. ret = OH_CameraManager_CreatePreviewOutputUsedInPreconfig(cameraManager, previewSurfaceId, &previewOutput);
   138. if (previewOutput == nullptr || ret != CAMERA_OK) {
   139. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
   140. }

   142. // 监听预览输出错误信息
   143. ret = OH_PreviewOutput_RegisterCallback(previewOutput, GetPreviewOutputListener());
   144. if (ret != CAMERA_OK) {
   145. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
   146. }

   148. // 创建拍照输出流，其中参数 photoSurfaceId 参考上文 ImageReceiver获取的surface
   149. ret = OH_CameraManager_CreatePhotoOutputUsedInPreconfig(cameraManager, photoSurfaceId, &photoOutput);
   150. if (photoOutput == nullptr || ret != CAMERA_OK) {
   151. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePhotoOutput failed.");
   152. }

   154. // 开始配置会话
   155. ret = OH_CaptureSession_BeginConfig(captureSession);
   156. if (ret != CAMERA_OK) {
   157. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
   158. }

   160. // 向会话中添加相机输入流
   161. ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
   162. if (ret != CAMERA_OK) {
   163. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
   164. }

   166. // 向会话中添加预览输出流
   167. ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
   168. if (ret != CAMERA_OK) {
   169. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
   170. }

   172. // 向会话中添加拍照输出流
   173. ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
   174. if (ret != CAMERA_OK) {
   175. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
   176. }

   178. // 提交会话配置
   179. ret = OH_CaptureSession_CommitConfig(captureSession);
   180. if (ret != CAMERA_OK) {
   181. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
   182. }

   184. // 启动会话
   185. ret = OH_CaptureSession_Start(captureSession);
   186. if (ret != CAMERA_OK) {
   187. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
   188. }

   190. // 判断设备是否支持闪光灯
   191. Camera_FlashMode flashMode = FLASH_MODE_AUTO;
   192. bool hasFlash = false;
   193. ret = OH_CaptureSession_HasFlash(captureSession, &hasFlash);
   194. if (ret != CAMERA_OK) {
   195. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_HasFlash failed.");
   196. }
   197. if (hasFlash) {
   198. OH_LOG_INFO(LOG_APP, "hasFlash success");
   199. } else {
   200. OH_LOG_ERROR(LOG_APP, "hasFlash fail");
   201. }
   202. // 检测闪光灯模式是否支持
   203. bool isSupported = false;
   204. ret = OH_CaptureSession_IsFlashModeSupported(captureSession, flashMode, &isSupported);
   205. if (ret != CAMERA_OK) {
   206. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFlashModeSupported failed.");
   207. }
   208. if (isSupported) {
   209. OH_LOG_INFO(LOG_APP, "isFlashModeSupported success");
   210. // 设置闪光灯模式
   211. ret = OH_CaptureSession_SetFlashMode(captureSession, flashMode);
   212. if (ret == CAMERA_OK) {
   213. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFlashMode success.");
   214. } else {
   215. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFlashMode failed. %{public}d ", ret);
   216. }
   217. // 获取当前设备的闪光灯模式
   218. ret = OH_CaptureSession_GetFlashMode(captureSession, &flashMode);
   219. if (ret == CAMERA_OK) {
   220. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFlashMode success. flashMode：%{public}d ", flashMode);
   221. } else {
   222. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFlashMode failed. %d ", ret);
   223. }
   224. } else {
   225. OH_LOG_ERROR(LOG_APP, "isFlashModeSupported fail");
   226. }

   228. // 判断是否支持连续自动变焦模式
   229. Camera_FocusMode focusMode = FOCUS_MODE_CONTINUOUS_AUTO;
   230. bool isFocusModeSupported = false;
   231. ret = OH_CaptureSession_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
   232. if (ret != CAMERA_OK) {
   233. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFocusModeSupported failed.");
   234. }
   235. if (isFocusModeSupported) {
   236. OH_LOG_INFO(LOG_APP, "isFocusModeSupported success");
   237. ret = OH_CaptureSession_SetFocusMode(captureSession, focusMode);
   238. if (ret != CAMERA_OK) {
   239. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFocusMode failed. %{public}d ", ret);
   240. }
   241. ret = OH_CaptureSession_GetFocusMode(captureSession, &focusMode);
   242. if (ret == CAMERA_OK) {
   243. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFocusMode success. focusMode%{public}d ", focusMode);
   244. } else {
   245. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFocusMode failed. %d ", ret);
   246. }
   247. } else {
   248. OH_LOG_ERROR(LOG_APP, "isFocusModeSupported fail");
   249. }

   251. // 获取相机支持的可变焦距比范围
   252. float minZoom;
   253. float maxZoom;
   254. ret = OH_CaptureSession_GetZoomRatioRange(captureSession, &minZoom, &maxZoom);
   255. if (ret != CAMERA_OK) {
   256. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatioRange failed.");
   257. } else {
   258. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
   259. minZoom, maxZoom);
   260. }
   261. // 设置变焦
   262. ret = OH_CaptureSession_SetZoomRatio(captureSession, maxZoom);
   263. if (ret == CAMERA_OK) {
   264. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetZoomRatio success.");
   265. } else {
   266. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetZoomRatio failed. %{public}d ", ret);
   267. }
   268. // 获取当前设备的变焦值
   269. ret = OH_CaptureSession_GetZoomRatio(captureSession, &maxZoom);
   270. if (ret == CAMERA_OK) {
   271. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatio success. zoom：%{public}f ", maxZoom);
   272. } else {
   273. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatio failed. %{public}d ", ret);
   274. }

   276. // 无拍照设置进行拍照
   277. ret = OH_PhotoOutput_Capture(photoOutput);
   278. if (ret == CAMERA_OK) {
   279. OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Capture success ");
   280. } else {
   281. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Capture failed. %d ", ret);
   282. }

   284. // 停止当前会话
   285. ret = OH_CaptureSession_Stop(captureSession);
   286. if (ret == CAMERA_OK) {
   287. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success ");
   288. } else {
   289. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
   290. }

   292. // 释放相机输入流
   293. ret = OH_CameraInput_Close(cameraInput);
   294. if (ret == CAMERA_OK) {
   295. OH_LOG_INFO(LOG_APP, "OH_CameraInput_Close success ");
   296. } else {
   297. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Close failed. %d ", ret);
   298. }

   300. // 释放预览输出流
   301. ret = OH_PreviewOutput_Release(previewOutput);
   302. if (ret == CAMERA_OK) {
   303. OH_LOG_INFO(LOG_APP, "OH_PreviewOutput_Release success ");
   304. } else {
   305. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_Release failed. %d ", ret);
   306. }

   308. // 释放拍照输出流
   309. ret = OH_PhotoOutput_Release(photoOutput);
   310. if (ret == CAMERA_OK) {
   311. OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Release success ");
   312. } else {
   313. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Release failed. %d ", ret);
   314. }

   316. // 释放会话
   317. ret = OH_CaptureSession_Release(captureSession);
   318. if (ret == CAMERA_OK) {
   319. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Release success ");
   320. } else {
   321. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Release failed. %d ", ret);
   322. }

   324. // 资源释放
   325. ret = OH_CameraManager_DeleteSupportedCameras(cameraManager, cameras, size);
   326. if (ret != CAMERA_OK) {
   327. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   328. } else {
   329. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_DeleteSupportedCameras. ok");
   330. }

   332. ret = OH_Camera_DeleteCameraManager(cameraManager);
   333. if (ret != CAMERA_OK) {
   334. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   335. } else {
   336. OH_LOG_ERROR(LOG_APP, "OH_Camera_DeleteCameraManager. ok");
   337. }
   338. }
   ```
