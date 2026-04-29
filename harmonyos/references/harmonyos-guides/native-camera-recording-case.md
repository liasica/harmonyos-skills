---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/native-camera-recording-case
title: 录像实践(C/C++)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(C/C++) > 录像实践(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:3e3567972008c97924312ba74382121f6a96c93618af1ade8d33cdb1f6dca412
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

当前示例提供完整的录像流程及其接口调用顺序的介绍。对于单个流程（如[设备输入](native-camera-device-input.md)、[会话管理](native-camera-session-management.md)、[录像](native-camera-recording.md)）的介绍请参考具体章节。

## 开发流程

在获取到相机支持的输出流能力后，开始创建录像流，开发流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/-kSonN8bTj6HvoaZ8-YGNg/zh-cn_image_0000002589324953.png?HW-CC-KV=V1&HW-CC-Date=20260429T053503Z&HW-CC-Expire=86400&HW-CC-Sign=293B3C0EDCEFF11C4C4A51537E9E3FF65EE382C7E757866A9CAC4570CC09AF0F)

## 完整示例

1. 在CMake脚本中链接相关动态库。

   ```
   1. target_link_libraries(entry PUBLIC
   2. libace_napi.z.so
   3. libohcamera.so
   4. libhilog_ndk.z.so
   5. )
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
   12. NDKCamera(char* previewId, char* videoId);
   13. };
   ```
3. cpp侧导入NDK接口，并根据传入的SurfaceId进行录像。

   ```
   1. #include "hilog/log.h"
   2. #include <cmath>

   4. bool IsAspectRatioEqual(float videoAspectRatio, float previewAspectRatio)
   5. {
   6. float epsilon = 1e-6f;
   7. return fabsf(videoAspectRatio - previewAspectRatio) <= epsilon;
   8. }

   10. void OnCameraInputError(const Camera_Input* cameraInput, Camera_ErrorCode errorCode)
   11. {
   12. OH_LOG_INFO(LOG_APP, "OnCameraInput errorCode = %{public}d", errorCode);
   13. }

   15. CameraInput_Callbacks* GetCameraInputListener(void)
   16. {
   17. static CameraInput_Callbacks cameraInputCallbacks = {
   18. .onError = OnCameraInputError
   19. };
   20. return &cameraInputCallbacks;
   21. }

   23. void CaptureSessionOnFocusStateChange(Camera_CaptureSession* session, Camera_FocusState focusState)
   24. {
   25. OH_LOG_INFO(LOG_APP, "CaptureSessionOnFocusStateChange");
   26. }

   28. void CaptureSessionOnError(Camera_CaptureSession* session, Camera_ErrorCode errorCode)
   29. {
   30. OH_LOG_INFO(LOG_APP, "CaptureSessionOnError = %{public}d", errorCode);
   31. }

   33. CaptureSession_Callbacks* GetCaptureSessionRegister(void)
   34. {
   35. static CaptureSession_Callbacks captureSessionCallbacks = {
   36. .onFocusStateChange = CaptureSessionOnFocusStateChange,
   37. .onError = CaptureSessionOnError
   38. };
   39. return &captureSessionCallbacks;
   40. }

   42. void VideoOutputOnFrameStart(Camera_VideoOutput* videoOutput)
   43. {
   44. OH_LOG_INFO(LOG_APP, "VideoOutputOnFrameStart");
   45. }

   47. void VideoOutputOnFrameEnd(Camera_VideoOutput* videoOutput, int32_t frameCount)
   48. {
   49. OH_LOG_INFO(LOG_APP, "VideoOutput frameCount = %{public}d", frameCount);
   50. }

   52. void VideoOutputOnError(Camera_VideoOutput* videoOutput, Camera_ErrorCode errorCode)
   53. {
   54. OH_LOG_INFO(LOG_APP, "VideoOutput errorCode = %{public}d", errorCode);
   55. }

   57. VideoOutput_Callbacks* GetVideoOutputListener(void)
   58. {
   59. static VideoOutput_Callbacks videoOutputListener = {
   60. .onFrameStart = VideoOutputOnFrameStart,
   61. .onFrameEnd = VideoOutputOnFrameEnd,
   62. .onError = VideoOutputOnError
   63. };
   64. return &videoOutputListener;
   65. }

   67. void CameraManagerStatusCallback(Camera_Manager* cameraManager, Camera_StatusInfo* status)
   68. {
   69. OH_LOG_INFO(LOG_APP, "CameraManagerStatusCallback is called");
   70. }

   72. CameraManager_Callbacks* GetCameraManagerListener()
   73. {
   74. static CameraManager_Callbacks cameraManagerListener = {
   75. .onCameraStatus = CameraManagerStatusCallback
   76. };
   77. return &cameraManagerListener;
   78. }

   80. NDKCamera::NDKCamera(char* previewId, char* videoId)
   81. {
   82. Camera_Manager* cameraManager = nullptr;
   83. Camera_Device* cameras = nullptr;
   84. Camera_CaptureSession* captureSession = nullptr;
   85. Camera_OutputCapability* cameraOutputCapability = nullptr;
   86. Camera_VideoOutput* videoOutput = nullptr;
   87. const Camera_Profile* previewProfile = nullptr;
   88. const Camera_Profile* photoProfile = nullptr;
   89. const Camera_VideoProfile* videoProfile = nullptr;
   90. Camera_PreviewOutput* previewOutput = nullptr;
   91. Camera_PhotoOutput* photoOutput = nullptr;
   92. Camera_Input* cameraInput = nullptr;
   93. uint32_t size = 0;
   94. uint32_t cameraDeviceIndex = 0;
   95. char* videoSurfaceId = videoId;
   96. char* previewSurfaceId = previewId;
   97. // 创建CameraManager对象。
   98. Camera_ErrorCode ret = OH_Camera_GetCameraManager(&cameraManager);
   99. if (cameraManager == nullptr || ret != CAMERA_OK) {
   100. OH_LOG_ERROR(LOG_APP, "OH_Camera_GetCameraManager failed.");
   101. return;
   102. }
   103. // 监听相机状态变化。
   104. ret = OH_CameraManager_RegisterCallback(cameraManager, GetCameraManagerListener());
   105. if (ret != CAMERA_OK) {
   106. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_RegisterCallback failed.");
   107. return;
   108. }

   110. // 获取相机列表。
   111. ret = OH_CameraManager_GetSupportedCameras(cameraManager, &cameras, &size);
   112. if (cameras == nullptr || size <= 0 || ret != CAMERA_OK) {
   113. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameras failed.");
   114. return;
   115. }

   117. for (int index = 0; index < size; index++) {
   118. OH_LOG_ERROR(LOG_APP, "cameraId  =  %{public}s ", cameras[index].cameraId);              // 获取相机ID。
   119. OH_LOG_ERROR(LOG_APP, "cameraPosition  =  %{public}d ", cameras[index].cameraPosition);  // 获取相机位置。
   120. OH_LOG_ERROR(LOG_APP, "cameraType  =  %{public}d ", cameras[index].cameraType);          // 获取相机类型。
   121. OH_LOG_ERROR(LOG_APP, "connectionType  =  %{public}d ", cameras[index].connectionType);  // 获取相机连接类型。
   122. }

   124. if (size < cameraDeviceIndex + 1) {
   125. OH_LOG_ERROR(LOG_APP, "cameraDeviceIndex is invalid.");
   126. return;
   127. }

   129. // 获取相机设备支持的输出流能力。
   130. ret = OH_CameraManager_GetSupportedCameraOutputCapability(cameraManager, &cameras[cameraDeviceIndex],
   131. &cameraOutputCapability);
   132. if (cameraOutputCapability == nullptr || ret != CAMERA_OK) {
   133. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_GetSupportedCameraOutputCapability failed.");
   134. return;
   135. }

   137. if (cameraOutputCapability->previewProfiles == nullptr) {
   138. OH_LOG_ERROR(LOG_APP, "previewProfiles == null");
   139. return;
   140. }
   141. previewProfile = cameraOutputCapability->previewProfiles[0];
   142. OH_LOG_INFO(LOG_APP, "previewProfile width: %{public}d, height: %{public}d.", previewProfile->size.width,
   143. previewProfile->size.height);
   144. if (cameraOutputCapability->photoProfiles == nullptr) {
   145. OH_LOG_ERROR(LOG_APP, "photoProfiles == null");
   146. return;
   147. }
   148. photoProfile = cameraOutputCapability->photoProfiles[0];

   150. if (cameraOutputCapability->videoProfiles == nullptr) {
   151. OH_LOG_ERROR(LOG_APP, "videoProfiles == null");
   152. return;
   153. }
   154. // 预览流宽高比要与录像流的宽高比一致，如果录制的是hdr视频，请筛选支持hdr的Camera_VideoProfile。
   155. Camera_VideoProfile** videoProfiles = cameraOutputCapability->videoProfiles;
   156. for (int index = 0; index < cameraOutputCapability->videoProfilesSize; index++) {
   157. bool isEqual = IsAspectRatioEqual((float)videoProfiles[index]->size.width / videoProfiles[index]->size.height,
   158. (float)previewProfile->size.width / previewProfile->size.height);
   159. // 默认筛选CAMERA_FORMAT_YUV_420_SP的profile。
   160. if (isEqual && videoProfiles[index]->format == Camera_Format::CAMERA_FORMAT_YUV_420_SP) {
   161. videoProfile = videoProfiles[index];
   162. OH_LOG_INFO(LOG_APP, "videoProfile width: %{public}d, height: %{public}d.", videoProfile->size.width,
   163. videoProfile->size.height);
   164. break;
   165. }
   166. }
   167. if (videoProfile == nullptr) {
   168. OH_LOG_ERROR(LOG_APP, "Get videoProfile failed.");
   169. return;
   170. }
   171. // 创建VideoOutput对象。
   172. ret = OH_CameraManager_CreateVideoOutput(cameraManager, videoProfile, videoSurfaceId, &videoOutput);
   173. if (videoOutput == nullptr || ret != CAMERA_OK) {
   174. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateVideoOutput failed.");
   175. return;
   176. }

   178. // 监听视频输出错误信息。
   179. ret = OH_VideoOutput_RegisterCallback(videoOutput, GetVideoOutputListener());
   180. if (ret != CAMERA_OK) {
   181. OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_RegisterCallback failed.");
   182. }

   184. // 创建会话。
   185. ret = OH_CameraManager_CreateCaptureSession(cameraManager, &captureSession);
   186. if (captureSession == nullptr || ret != CAMERA_OK) {
   187. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCaptureSession failed.");
   188. return;
   189. }
   190. // 监听session错误信息。
   191. ret = OH_CaptureSession_RegisterCallback(captureSession, GetCaptureSessionRegister());
   192. if (ret != CAMERA_OK) {
   193. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_RegisterCallback failed.");
   194. }

   196. // 开始配置会话。
   197. ret = OH_CaptureSession_BeginConfig(captureSession);
   198. if (ret != CAMERA_OK) {
   199. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_BeginConfig failed.");
   200. return;
   201. }

   203. // 创建相机输入流。
   204. ret = OH_CameraManager_CreateCameraInput(cameraManager, &cameras[cameraDeviceIndex], &cameraInput);
   205. if (cameraInput == nullptr || ret != CAMERA_OK) {
   206. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreateCameraInput failed.");
   207. return;
   208. }

   210. // 监听cameraInput错误信息。
   211. ret = OH_CameraInput_RegisterCallback(cameraInput, GetCameraInputListener());
   212. if (ret != CAMERA_OK) {
   213. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_RegisterCallback failed.");
   214. }

   216. // 打开相机。
   217. ret = OH_CameraInput_Open(cameraInput);
   218. if (ret != CAMERA_OK) {
   219. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Open failed.");
   220. return;
   221. }

   223. // 向会话中添加相机输入流。
   224. ret = OH_CaptureSession_AddInput(captureSession, cameraInput);
   225. if (ret != CAMERA_OK) {
   226. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddInput failed.");
   227. return;
   228. }

   230. // 创建预览输出流,其中参数 surfaceId 参考下面 XComponent 组件，预览流为XComponent组件提供的surface。
   231. ret = OH_CameraManager_CreatePreviewOutput(cameraManager, previewProfile, previewSurfaceId, &previewOutput);
   232. if (previewProfile == nullptr || previewOutput == nullptr || ret != CAMERA_OK) {
   233. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_CreatePreviewOutput failed.");
   234. return;
   235. }

   237. // 向会话中添加预览输出流。
   238. ret = OH_CaptureSession_AddPreviewOutput(captureSession, previewOutput);
   239. if (ret != CAMERA_OK) {
   240. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddPreviewOutput failed.");
   241. return;
   242. }

   244. // 向会话中添加录像输出流。
   245. ret = OH_CaptureSession_AddVideoOutput(captureSession, videoOutput);
   246. if (ret != CAMERA_OK) {
   247. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_AddVideoOutput failed.");
   248. return;
   249. }

   251. // 提交会话配置。
   252. ret = OH_CaptureSession_CommitConfig(captureSession);
   253. if (ret != CAMERA_OK) {
   254. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_CommitConfig failed.");
   255. return;
   256. }

   258. // 启动会话。
   259. ret = OH_CaptureSession_Start(captureSession);
   260. if (ret != CAMERA_OK) {
   261. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Start failed.");
   262. return;
   263. }

   265. // 启动录像输出流。
   266. ret = OH_VideoOutput_Start(videoOutput);
   267. if (ret != CAMERA_OK) {
   268. OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_Start failed.");
   269. return;
   270. }

   272. // 开始录像 ts侧调用avRecorder.start()。

   274. // 停止录像输出流。
   275. ret = OH_VideoOutput_Stop(videoOutput);
   276. if (ret != CAMERA_OK) {
   277. OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_Stop failed.");
   278. }

   280. // 停止录像 ts侧调用avRecorder.stop()。

   282. // 停止当前会话。
   283. ret = OH_CaptureSession_Stop(captureSession);
   284. if (ret == CAMERA_OK) {
   285. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Stop success ");
   286. } else {
   287. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Stop failed. %d ", ret);
   288. }

   290. // 释放相机输入流。
   291. ret = OH_CameraInput_Close(cameraInput);
   292. if (ret == CAMERA_OK) {
   293. OH_LOG_INFO(LOG_APP, "OH_CameraInput_Close success ");
   294. } else {
   295. OH_LOG_ERROR(LOG_APP, "OH_CameraInput_Close failed. %d ", ret);
   296. }

   298. // 释放预览输出流。
   299. ret = OH_PreviewOutput_Release(previewOutput);
   300. if (ret == CAMERA_OK) {
   301. OH_LOG_INFO(LOG_APP, "OH_PreviewOutput_Release success ");
   302. } else {
   303. OH_LOG_ERROR(LOG_APP, "OH_PreviewOutput_Release failed. %d ", ret);
   304. }

   306. // 释放录像输出流。
   307. ret = OH_VideoOutput_Release(videoOutput);
   308. if (ret == CAMERA_OK) {
   309. OH_LOG_INFO(LOG_APP, "OH_VideoOutput_Release success ");
   310. } else {
   311. OH_LOG_ERROR(LOG_APP, "OH_VideoOutput_Release failed. %d ", ret);
   312. }

   314. // 释放会话。
   315. ret = OH_CaptureSession_Release(captureSession);
   316. if (ret == CAMERA_OK) {
   317. OH_LOG_INFO(LOG_APP, "OH_CaptureSession_Release success ");
   318. } else {
   319. OH_LOG_ERROR(LOG_APP, "OH_CaptureSession_Release failed. %d ", ret);
   320. }

   322. // 资源释放。
   323. ret = OH_CameraManager_DeleteSupportedCameras(cameraManager, cameras, size);
   324. if (ret != CAMERA_OK) {
   325. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   326. } else {
   327. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_DeleteSupportedCameras. ok");
   328. }
   329. ret = OH_CameraManager_DeleteSupportedCameraOutputCapability(cameraManager, cameraOutputCapability);
   330. if (ret != CAMERA_OK) {
   331. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   332. } else {
   333. OH_LOG_ERROR(LOG_APP, "OH_CameraManager_DeleteSupportedCameraOutputCapability success");
   334. }
   335. ret = OH_Camera_DeleteCameraManager(cameraManager);
   336. if (ret != CAMERA_OK) {
   337. OH_LOG_ERROR(LOG_APP, "Delete Cameras failed.");
   338. } else {
   339. OH_LOG_ERROR(LOG_APP, "OH_Camera_DeleteCameraManager success");
   340. }
   341. }
   ```

## 示例代码

* 录像示例代码请参考[NDKPhotoVideoSample(C/C++)](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/CameraKit/NDKPhotoVideoSample)。
