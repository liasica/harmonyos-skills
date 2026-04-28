---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-shooting-case
title: 拍照实践(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 拍照实践(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:07+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dae47ee48d698a46c77a111592488dded2af8405d880842e7a41955a552cd69b
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

当前示例提供完整的拍照流程及其接口调用顺序的介绍。对于单个流程（如设备输入、会话管理、拍照）的介绍请参考[相机开发指导(Native)](native-camera-device-management.md)的具体章节。

## 开发流程

在获取到相机支持的输出流能力后，开始创建拍照流，开发流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/7IsByVOpTAqEjmU-2wXz6g/zh-cn_image_0000002583478583.png?HW-CC-KV=V1&HW-CC-Date=20260427T234605Z&HW-CC-Expire=86400&HW-CC-Sign=C19E05D7567F3EF16F714B800F1AB5CA6F9E329B730E1ADCC784DCB971C6BF61)

## 完整示例

1. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libhilog_ndk.z.so
   4. libnative_buffer.so
   5. libohcamera.so
   6. libohimage.so
   7. libohfileuri.so
   8. )
   ```
2. 创建头文件ndk\_camera.h。

   ```
   1. #include "ohcamera/camera.h"
   2. #include "ohcamera/camera_input.h"
   3. #include "ohcamera/capture_session.h"
   4. #include "ohcamera/photo_output.h"
   5. #include "ohcamera/preview_output.h"
   6. #include "ohcamera/video_output.h"
   7. #include "ohcamera/camera_manager.h"

   9. class NDKCamera {
   10. public:
   11. ~NDKCamera();
   12. NDKCamera(char* previewId);
   13. Camera_ErrorCode RegisterBufferCb(void* cb);
   14. };
   ```
3. cpp侧导入NDK接口，并根据传入的SurfaceId进行拍照。

   ```
   1. #include "hilog/log.h"

   3. void CaptureSessionOnFocusStateChange(Camera_CaptureSession* session, Camera_FocusState focusState)
   4. {
   5. OH_LOG_INFO(LOG_APP, "CaptureSessionOnFocusStateChange");
   6. }

   8. void CaptureSessionOnError(Camera_CaptureSession* session, Camera_ErrorCode errorCode)
   9. {
   10. OH_LOG_INFO(LOG_APP, "CaptureSessionOnError = %{public}d", errorCode);
   11. }

   13. CaptureSession_Callbacks* GetCaptureSessionRegister(void)
   14. {
   15. static CaptureSession_Callbacks captureSessionCallbacks = {
   16. .onFocusStateChange = CaptureSessionOnFocusStateChange,
   17. .onError = CaptureSessionOnError
   18. };
   19. return &captureSessionCallbacks;
   20. }

   22. void PreviewOutputOnFrameStart(Camera_PreviewOutput* previewOutput)
   23. {
   24. OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameStart");
   25. }

   27. void PreviewOutputOnFrameEnd(Camera_PreviewOutput* previewOutput, int32_t frameCount)
   28. {
   29. OH_LOG_INFO(LOG_APP, "PreviewOutputOnFrameEnd = %{public}d", frameCount);
   30. }

   32. void PreviewOutputOnError(Camera_PreviewOutput* previewOutput, Camera_ErrorCode errorCode)
   33. {
   34. OH_LOG_INFO(LOG_APP, "PreviewOutputOnError = %{public}d", errorCode);
   35. }

   37. PreviewOutput_Callbacks* GetPreviewOutputListener(void)
   38. {
   39. static PreviewOutput_Callbacks previewOutputListener = {
   40. .onFrameStart = PreviewOutputOnFrameStart,
   41. .onFrameEnd = PreviewOutputOnFrameEnd,
   42. .onError = PreviewOutputOnError
   43. };
   44. return &previewOutputListener;
   45. }

   47. void OnCameraInputError(const Camera_Input* cameraInput, Camera_ErrorCode errorCode)
   48. {
   49. OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode = %{public}d", errorCode);
   50. }

   52. CameraInput_Callbacks* GetCameraInputListener(void)
   53. {
   54. static CameraInput_Callbacks cameraInputCallbacks = {
   55. .onError = OnCameraInputError
   56. };
   57. return &cameraInputCallbacks;
   58. }

   60. void CameraManagerStatusCallback(Camera_Manager* cameraManager, Camera_StatusInfo* status)
   61. {
   62. OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
   63. }

   65. CameraManager_Callbacks* GetCameraManagerListener()
   66. {
   67. static CameraManager_Callbacks cameraManagerListener = {
   68. .onCameraStatus = CameraManagerStatusCallback
   69. };
   70. return &cameraManagerListener;
   71. }

   73. static void* bufferCb = nullptr;
   74. Camera_ErrorCode NDKCamera::RegisterBufferCb(void* cb) {
   75. OH_LOG_INFO(LOG_APP, " RegisterBufferCb start");
   76. if (cb == nullptr) {
   77. OH_LOG_INFO(LOG_APP, " RegisterBufferCb invalid error");
   78. return CAMERA_INVALID_ARGUMENT;
   79. }
   80. bufferCb = cb;

   82. return CAMERA_OK;
   83. }
   84. void OnPhotoAvailable(Camera_PhotoOutput* photoOutput, OH_PhotoNative* photo) {
   85. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable start!");
   86. OH_ImageNative* imageNative;
   87. Camera_ErrorCode errCode = OH_PhotoNative_GetMainImage(photo, &imageNative);
   88. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable errCode:%{public}d imageNative:%{public}p", errCode, imageNative);
   89. // 读取 OH_ImageNative 的 size 属性。
   90. Image_Size size;
   91. Image_ErrorCode imageErr = OH_ImageNative_GetImageSize(imageNative, &size);
   92. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable imageErr:%{public}d width:%{public}d height:%{public}d", imageErr,
   93. size.width, size.height);
   94. // 读取 OH_ImageNative 的组件列表的元素个数。
   95. size_t componentTypeSize = 0;
   96. imageErr = OH_ImageNative_GetComponentTypes(imageNative, nullptr, &componentTypeSize);
   97. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable imageErr:%{public}d componentTypeSize:%{public}zu", imageErr,
   98. componentTypeSize);
   99. // 读取 OH_ImageNative 的组件列表。
   100. uint32_t* components = new uint32_t[componentTypeSize];
   101. imageErr = OH_ImageNative_GetComponentTypes(imageNative, &components, &componentTypeSize);
   102. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable OH_ImageNative_GetComponentTypes imageErr:%{public}d", imageErr);
   103. // 读取 OH_ImageNative 的第一个组件所对应的缓冲区对象。
   104. OH_NativeBuffer* nativeBuffer = nullptr;
   105. imageErr = OH_ImageNative_GetByteBuffer(imageNative, components[0], &nativeBuffer);
   106. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable OH_ImageNative_GetByteBuffer imageErr:%{public}d", imageErr);
   107. // 读取 OH_ImageNative 的第一个组件所对应的缓冲区大小。
   108. size_t nativeBufferSize = 0;
   109. imageErr = OH_ImageNative_GetBufferSize(imageNative, components[0], &nativeBufferSize);
   110. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable imageErr:%{public}d nativeBufferSize:%{public}zu", imageErr,
   111. nativeBufferSize);
   112. // 读取 OH_ImageNative 的第一个组件所对应的像素行宽。
   113. int32_t rowStride = 0;
   114. imageErr = OH_ImageNative_GetRowStride(imageNative, components[0], &rowStride);
   115. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable imageErr:%{public}d rowStride:%{public}d", imageErr, rowStride);
   116. // 读取 OH_ImageNative 的第一个组件所对应的像素大小。
   117. int32_t pixelStride = 0;
   118. imageErr = OH_ImageNative_GetPixelStride(imageNative, components[0], &pixelStride);
   119. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable imageErr:%{public}d pixelStride:%{public}d", imageErr, pixelStride);
   120. // 将ION内存映射到进程空间。
   121. void* virAddr = nullptr; // 指向映射内存的虚拟地址，解除映射后这个指针将不再有效。
   122. int32_t ret = OH_NativeBuffer_Map(nativeBuffer, &virAddr); // 映射后通过第二个参数virAddr返回内存的首地址。
   123. OH_LOG_INFO(LOG_APP, "OnPhotoAvailable OH_NativeBuffer_Map err:%{public}d", ret);
   124. // 通过回调函数，将处理完的buffer传给ArkTS侧做显示或通过安全控件写文件保存，参考拍照(C/C++)开发指导。
   125. if (bufferCb == nullptr) {
   126. OH_LOG_INFO(LOG_APP, "Current bufferCb invalid error");
   127. return;
   128. }
   129. auto cb = (void (*)(void *, size_t))(bufferCb);
   130. cb(virAddr, nativeBufferSize);
   131. // 在处理完之后，解除映射并释放缓冲区。
   132. ret = OH_NativeBuffer_Unmap(nativeBuffer);
   133. if (ret != 0) {
   134. OH_LOG_ERROR(LOG_APP, "OnPhotoAvailable OH_NativeBuffer_Unmap error:%{public}d", ret);
   135. }
   136. }

   138. NDKCamera::NDKCamera(char* previewId)
   139. {
   140. Camera_Manager* cameraManager = nullptr;
   141. Camera_Device* cameras = nullptr;
   142. Camera_CaptureSession* captureSession = nullptr;
   143. Camera_OutputCapability* cameraOutputCapability = nullptr;
   144. const Camera_Profile* previewProfile = nullptr;
   145. const Camera_Profile* photoProfile = nullptr;
   146. Camera_PreviewOutput* previewOutput = nullptr;
   147. Camera_PhotoOutput* photoOutput = nullptr;
   148. Camera_Input* cameraInput = nullptr;
   149. uint32_t size = 0;
   150. uint32_t cameraDeviceIndex = 0;
   151. char* previewSurfaceId = previewId;
   152. // 创建CameraManager对象。
   153. Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
   154. if (cameraManager == nullptr || ret != CAMERA_OK) {
   155. OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
   156. return;
   157. }
   158. // 监听相机状态变化。
   159. ret = OH_CameraManager_RegisterCallback(cameraManager, GetCameraManagerListener());
   160. if (ret != CAMERA_OK) {
   161. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
   162. }

   164. // 获取相机列表。
   165. ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
   166. if (cameras == nullptr || size <= 0 || ret != CAMERA_OK) {
   167. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
   168. return;
   169. }

   171. if (size < cameraDeviceIndex + 1) {
   172. OH_LOG_ERROR(LOG_APP, "cameraDeviceIndex is invalid.");
   173. return;
   174. }

   176. // 创建相机输入流。
   177. ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[cameraDeviceIndex], &cameraInput);
   178. if (cameraInput == nullptr || ret != CAMERA_OK) {
   179. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
   180. return;
   181. }

   183. // 监听cameraInput错误信息。
   184. ret = OH_CameraInput_RegisterCallback(cameraInput, GetCameraInputListener());
   185. if (ret != CAMERA_OK) {
   186. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
   187. return;
   188. }

   190. // 打开相机。
   191. ret = OH_CameraInput_Open(cameraInput);
   192. if (ret != CAMERA_OK) {
   193. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Open failed.");
   194. return;
   195. }

   197. // 获取相机设备支持的输出流能力。
   198. ret = OH_CameraManager_GetSupportedCameraOutputCapability(cameraManager, &cameras[cameraDeviceIndex],
   199. &cameraOutputCapability);
   200. if (cameraOutputCapability == nullptr || ret != CAMERA_OK) {
   201. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
   202. return;
   203. }

   205. if (cameraOutputCapability->previewProfiles == nullptr) {
   206. OH_LOG_ERROR(LOG_APP, "previewProfiles == null");
   207. return;
   208. }
   209. // 根据所需从cameraOutputCapability->previewProfiles中选择合适的预览分辨率
   210. previewProfile = cameraOutputCapability->previewProfiles[0];

   212. if (cameraOutputCapability->photoProfiles == nullptr) {
   213. OH_LOG_ERROR(LOG_APP, "photoProfiles == null");
   214. return;
   215. }
   216. // 根据所需从cameraOutputCapability->photoProfiles中选择合适的拍照分辨率
   217. photoProfile = cameraOutputCapability->photoProfiles[0];

   219. // 创建预览输出流,其中参数 previewSurfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface。
   220. ret = OH_CameraManager_CreatePreviewOutput(cameraManager, previewProfile, previewSurfaceId, &previewOutput);
   221. if (previewProfile == nullptr || previewOutput == nullptr || ret != CAMERA_OK) {
   222. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
   223. return;
   224. }

   226. // 监听预览输出错误信息。
   227. ret = OH_PreviewOutput_RegisterCallback(previewOutput, GetPreviewOutputListener());
   228. if (ret != CAMERA_OK) {
   229. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_RegisterCallback failed.");
   230. }

   232. // 创建拍照输出流。
   233. ret = OH_CameraManager_CreatePhotoOutputWithoutSurface(cameraManager, photoProfile, &photoOutput);

   235. // 监听单段式拍照回调。
   236. ret = OH_PhotoOutput_RegisterPhotoAvailableCallback(photoOutput, OnPhotoAvailable);

   238. // 创建会话。
   239. ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
   240. if (captureSession == nullptr || ret != CAMERA_OK) {
   241. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
   242. return;
   243. }

   245. // 监听session错误信息。
   246. ret = OH_CaptureSession_RegisterCallback(captureSession, GetCaptureSessionRegister());
   247. if (ret != CAMERA_OK) {
   248. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.");
   249. }

   251. // 开始配置会话。
   252. ret = OH_CaptureSession_BeginConfig(captureSession);
   253. if (ret != CAMERA_OK) {
   254. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
   255. return;
   256. }

   258. // 向会话中添加相机输入流。
   259. ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
   260. if (ret != CAMERA_OK) {
   261. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
   262. return;
   263. }

   265. // 向会话中添加预览输出流。
   266. ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
   267. if (ret != CAMERA_OK) {
   268. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
   269. return;
   270. }

   272. // 向会话中添加拍照输出流。
   273. ret = OH_CaptureSession_AddPhotoOutput(captureSession, photoOutput);
   274. if (ret != CAMERA_OK) {
   275. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPhotoOutput failed.");
   276. return;
   277. }

   279. // 提交会话配置。
   280. ret = OH_CaptureSession_CommitConfig(captureSession);
   281. if (ret != CAMERA_OK) {
   282. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
   283. return;
   284. }

   286. // 启动会话。
   287. ret = OH_CaptureSession_Start(captureSession);
   288. if (ret != CAMERA_OK) {
   289. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
   290. return;
   291. }

   293. // 判断设备是否支持闪光灯。
   294. Camera_FlashMode flashMode = FLASH_MODE_AUTO;
   295. bool hasFlash = false;
   296. ret = OH_CaptureSession_HasFlash(captureSession, &hasFlash);
   297. if (ret != CAMERA_OK) {
   298. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_HasFlash failed.");
   299. }
   300. if (hasFlash) {
   301. OH_LOG_INFO(LOG_APP, "hasFlash success");
   302. } else {
   303. OH_LOG_ERROR(LOG_APP, "hasFlash fail");
   304. }

   306. // 检测闪光灯模式是否支持。
   307. bool isSupported = false;
   308. ret = OH_CaptureSession_IsFlashModeSupported(captureSession, flashMode, &isSupported);
   309. if (ret != CAMERA_OK) {
   310. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFlashModeSupported failed.");
   311. }
   312. if (isSupported) {
   313. OH_LOG_INFO(LOG_APP, "isFlashModeSupported success");

   315. // 设置闪光灯模式。
   316. ret = OH_CaptureSession_SetFlashMode(captureSession, flashMode);
   317. if (ret == CAMERA_OK) {
   318. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetFlashMode success.");
   319. } else {
   320. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFlashMode failed. ret : %{public}d ", ret);
   321. }

   323. // 获取当前设备的闪光灯模式。
   324. ret = OH_CaptureSession_GetFlashMode(captureSession, &flashMode);
   325. if (ret == CAMERA_OK) {
   326. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFlashMode success. flashMode：%{public}d ", flashMode);
   327. } else {
   328. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFlashMode failed. ret : %{public}d ", ret);
   329. }
   330. } else {
   331. OH_LOG_ERROR(LOG_APP, "isFlashModeSupported fail");
   332. }

   334. // 判断是否支持连续自动变焦模式。
   335. Camera_FocusMode focusMode = FOCUS_MODE_CONTINUOUS_AUTO;
   336. bool isFocusModeSupported = false;
   337. ret = OH_CaptureSession_IsFocusModeSupported(captureSession, focusMode, &isFocusModeSupported);
   338. if (ret != CAMERA_OK) {
   339. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_IsFocusModeSupported failed.");
   340. }
   341. if (isFocusModeSupported) {
   342. OH_LOG_INFO(LOG_APP, "isFocusModeSupported success");
   343. ret = OH_CaptureSession_SetFocusMode(captureSession, focusMode);
   344. if (ret != CAMERA_OK) {
   345. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetFocusMode failed. ret : %{public}d ", ret);
   346. }
   347. ret = OH_CaptureSession_GetFocusMode(captureSession, &focusMode);
   348. if (ret == CAMERA_OK) {
   349. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetFocusMode success. focusMode%{public}d ", focusMode);
   350. } else {
   351. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetFocusMode failed. ret : %{public}d ", ret);
   352. }
   353. } else {
   354. OH_LOG_ERROR(LOG_APP, "isFocusModeSupported fail");
   355. }

   357. // 获取相机支持的可变焦距比范围。
   358. float minZoom;
   359. float maxZoom;
   360. ret = OH_CaptureSession_GetZoomRatioRange(captureSession, &minZoom, &maxZoom);
   361. if (ret != CAMERA_OK) {
   362. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatioRange failed.");
   363. } else {
   364. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatioRange success. minZoom: %{public}f, maxZoom:%{public}f",
   365. minZoom, maxZoom);
   366. }

   368. // 设置变焦。
   369. ret = OH_CaptureSession_SetZoomRatio(captureSession, maxZoom);
   370. if (ret == CAMERA_OK) {
   371. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_SetZoomRatio success.");
   372. } else {
   373. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_SetZoomRatio failed. ret : %{public}d ", ret);
   374. }

   376. // 获取当前设备的变焦值。
   377. ret = OH_CaptureSession_GetZoomRatio(captureSession, &maxZoom);
   378. if (ret == CAMERA_OK) {
   379. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_GetZoomRatio success. zoom：%{public}f ", maxZoom);
   380. } else {
   381. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_GetZoomRatio failed. ret : %{public}d ", ret);
   382. }

   384. // 无拍照设置进行拍照。
   385. ret = OH_PhotoOutput_Capture(photoOutput);
   386. if (ret == CAMERA_OK) {
   387. OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Capture success ");
   388. } else {
   389. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Capture failed. ret : %{public}d ", ret);
   390. }

   392. // 停止当前会话。
   393. ret = OH_CaptureSession_Stop(captureSession);
   394. if (ret == CAMERA_OK) {
   395. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success ");
   396. } else {
   397. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. ret : %{public}d ", ret);
   398. }

   400. // 释放相机输入流。
   401. ret = OH_CameraInput_Close(cameraInput);
   402. if (ret == CAMERA_OK) {
   403. OH_LOG_INFO(LOG_APP, "OH_CameraInput_Close success ");
   404. } else {
   405. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Close failed. ret : %{public}d ", ret);
   406. }

   408. // 释放预览输出流。
   409. ret = OH_PreviewOutput_Release(previewOutput);
   410. if (ret == CAMERA_OK) {
   411. OH_LOG_INFO(LOG_APP, "OH_PreviewOutput_Release success ");
   412. } else {
   413. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_Release failed. ret : %{public}d ", ret);
   414. }

   416. // 释放拍照输出流。
   417. ret = OH_PhotoOutput_Release(photoOutput);
   418. if (ret == CAMERA_OK) {
   419. OH_LOG_INFO(LOG_APP, "OH_PhotoOutput_Release success ");
   420. } else {
   421. OH_LOG_ERROR(LOG_APP, "OH_PhotoOutput_Release failed. ret : %{public}d ", ret);
   422. }

   424. // 释放会话。
   425. ret = OH_CaptureSession_Release(captureSession);
   426. if (ret == CAMERA_OK) {
   427. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Release success ");
   428. } else {
   429. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Release failed. ret : %{public}d ", ret);
   430. }

   432. // 资源释放。
   433. ret = OH_CameraManager_DeleteSupportedCameras(cameraManager, cameras, size);
   434. if (ret != CAMERA_OK) {
   435. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   436. } else {
   437. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_DeleteSupportedCameras. ok");
   438. }
   439. ret = OH_CameraManager_DeleteSupportedCameraOutputCapability(cameraManager, cameraOutputCapability);
   440. if (ret != CAMERA_OK) {
   441. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   442. } else {
   443. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_DeleteSupportedCameraOutputCapability. ok");
   444. }
   445. ret = OH_Camera_DeleteCameraManager(cameraManager);
   446. if (ret != CAMERA_OK) {
   447. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   448. } else {
   449. OH_LOG_ERROR(LOG_APP, "OH_Camera_DeleteCameraManager. ok");
   450. }
   451. }
   ```
