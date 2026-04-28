---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-hdr-recording
title: HDR Vivid相机录像(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > HDR Vivid相机录像(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:04+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:92d1884f8fa35de4292fed17fdc79f388fe23cb9ac39eecfed5725a4fc10a323
---

HarmonyOS支持调用接口，录制HDR Vivid视频，可以拍出层次表现更细腻、光影细节更丰富的画面，提升画面质感，呈现更卓越的视觉效果。

当前示例提供完整的HDR Vivid录像开发步骤，方便开发者实现录制HDR Vivid视频的功能。更多HDR Vivid的开发指导，请参考[使用HDR Vivid特性开发媒体应用](multimedia-hdr-vivid.md)。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[录像](camera-recording.md)等单个流程。

## 开发步骤

1. 导入接口。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { colorSpaceManager } from '@kit.ArkGraphics2D';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { media } from '@kit.MediaKit';
   5. import { common } from '@kit.AbilityKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   7. import { fileIo } from '@kit.CoreFileKit';
   ```
2. 获取预览、录像的配置项。

   HDR录像的输出格式需要设置成10bit的CAMERA\_FORMAT\_YCRCB\_P010。具体参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。

   说明

   预览流与录像输出流的分辨率的宽高比要保持一致，如果设置XComponent组件中的Surface显示区域宽高比为1920:1080 = 16:9，则需要预览流中的分辨率的宽高比也为16:9，如分辨率选择640:360，或960:540，或1920:1080，以此类推。

   ```
   1. function getPreviewProfile(previewProfiles: Array<camera.Profile>, size: camera.Size): undefined | camera.Profile {
   2. let previewProfile: undefined | camera.Profile = previewProfiles.find((profile: camera.Profile) => {
   3. return profile.format === camera.CameraFormat.CAMERA_FORMAT_YCRCB_P010 &&
   4. profile.size.width === size.width && profile.size.height == size.height
   5. });
   6. return previewProfile;
   7. }

   9. function getVideoProfile(videoProfiles: Array<camera.VideoProfile>, size: camera.Size): undefined | camera.VideoProfile {
   10. let videoProfile: undefined | camera.VideoProfile = videoProfiles.find((profile: camera.VideoProfile) => {
   11. return profile.format === camera.CameraFormat.CAMERA_FORMAT_YCRCB_P010 &&
   12. profile.size.width === size.width && profile.size.height == size.height
   13. });
   14. return videoProfile;
   15. }
   ```
3. 查询是否支持视频防抖。

   HDR录像需要支持视频防抖。

   ```
   1. function isVideoStabilizationModeSupported(session: camera.VideoSession, mode: camera.VideoStabilizationMode): boolean {
   2. let isSupported: boolean = false;
   3. try {
   4. isSupported = session.isVideoStabilizationModeSupported(mode);
   5. } catch (error) {
   6. // 失败返回错误码error.code并处理
   7. let err = error as BusinessError;
   8. console.error(`The isVideoStabilizationModeSupported call failed. error code: ${err.code}`);
   9. }
   10. return isSupported;
   11. }
   ```
4. 设置视频防抖。

   ```
   1. function setVideoStabilizationMode(session: camera.VideoSession): void {
   2. let mode: camera.VideoStabilizationMode = camera.VideoStabilizationMode.AUTO;
   3. // 查询是否支持视频防抖
   4. let isSupported: boolean = isVideoStabilizationModeSupported(session, mode);
   5. if (isSupported) {
   6. console.info(`setVideoStabilizationMode: ${mode}`);
   7. // 设置视频防抖
   8. try {
   9. session.setVideoStabilizationMode(mode);
   10. } catch (error) {
   11. // 失败返回错误码error.code并处理
   12. let err = error as BusinessError;
   13. console.error(`setVideoStabilizationMode call failed. error code: ${err.code}`);
   14. }
   15. let activeVideoStabilizationMode = session.getActiveVideoStabilizationMode();
   16. console.info(`activeVideoStabilizationMode: ${activeVideoStabilizationMode}`);
   17. } else {
   18. console.info(`videoStabilizationMode: ${mode} is not support`);
   19. }
   20. }
   ```
5. 查询支持的色彩空间。

   ```
   1. function getSupportedColorSpaces(session: camera.VideoSession): Array<colorSpaceManager.ColorSpace> {
   2. let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
   3. try {
   4. colorSpaces = session.getSupportedColorSpaces();
   5. } catch (error) {
   6. let err = error as BusinessError;
   7. console.error(`The getSupportedColorSpaces call failed. error code: ${err.code}`);
   8. }
   9. return colorSpaces;
   10. }
   ```
6. 设置色彩空间。

   如果是SDR录像色彩空间需要设置为BT709\_LIMIT，如果是HDR录像色彩空间需要设置为BT2020\_HLG\_LIMIT。具体参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。建议在提交会话配置之前调用[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。

   ```
   1. function setColorSpaceBeforeCommitConfig(session: camera.VideoSession, isHdr: boolean): void {
   2. let colorSpace: colorSpaceManager.ColorSpace = isHdr? colorSpaceManager.ColorSpace.BT2020_HLG_LIMIT : colorSpaceManager.ColorSpace.BT709_LIMIT;
   3. let colorSpaces: Array<colorSpaceManager.ColorSpace> = session.getSupportedColorSpaces();
   4. let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
   5. if (isSupportedColorSpaces) {
   6. console.info(`setColorSpace: ${colorSpace}`);
   7. try {
   8. session.setColorSpace(colorSpace);
   9. } catch (error) {
   10. // 失败返回错误码error.code并处理
   11. let err = error as BusinessError;
   12. console.error(`setColorSpace call failed. error code: ${err.code}`);
   13. }
   14. let activeColorSpace:colorSpaceManager.ColorSpace = session.getActiveColorSpace();
   15. console.info(`activeColorSpace: ${activeColorSpace}`);
   16. } else {
   17. console.info(`colorSpace: ${colorSpace} is not support`);
   18. }
   19. }
   ```
7. 实现HDR录像。

   在创建预览输出、录像输出前执行步骤2获取配置项，提交会话配置前执行步骤6设置色彩空间，提交会话配置后执行步骤4设置视频防抖，其余流程按照正常录像流程开发。

   说明

   如需在提交会话配置后，设置视频防抖模式和色彩空间，为避免相机输出流配置异常，请先通过[setVideoStabilizationMode](../harmonyos-references/arkts-apis-camera-stabilization.md#setvideostabilizationmode11)方法4. 设置视频防抖后，再通过[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)方法完成6.设置色彩空间。

   ```
   1. async function cameraHdrRecordingCase(context: common.Context, surfaceId: string): Promise<void> {
   2. // 创建CameraManager对象
   3. let cameraManager: camera.CameraManager = camera.getCameraManager(context);
   4. if (!cameraManager) {
   5. console.error("camera.getCameraManager error");
   6. return;
   7. }

   9. // 监听相机状态变化
   10. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
   11. if (err !== undefined && err.code !== 0) {
   12. console.error('cameraStatus with errorCode = ' + err.code);
   13. return;
   14. }
   15. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
   16. console.info(`status: ${cameraStatusInfo.status}`);
   17. });

   19. // 获取相机列表
   20. let cameraArray: Array<camera.CameraDevice> = [];
   21. try {
   22. cameraArray = cameraManager.getSupportedCameras();
   23. } catch (error) {
   24. let err = error as BusinessError;
   25. console.error(`getSupportedCameras call failed. error code: ${err.code}`);
   26. }

   28. if (cameraArray.length <= 0) {
   29. console.error("cameraManager.getSupportedCameras error");
   30. return;
   31. }

   33. // 获取支持的模式类型
   34. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
   35. let isSupportVideoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_VIDEO) >= 0;
   36. if (!isSupportVideoMode) {
   37. console.error('video mode not support');
   38. return;
   39. }

   41. // 获取相机设备支持的输出流能力
   42. let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_VIDEO);
   43. if (!cameraOutputCap) {
   44. console.error("cameraManager.getSupportedOutputCapability error")
   45. return;
   46. }
   47. console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

   49. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
   50. if (!previewProfilesArray) {
   51. console.error("createOutput previewProfilesArray == null || undefined");
   52. return;
   53. }

   55. let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
   56. if (!videoProfilesArray) {
   57. console.error("createOutput videoProfilesArray == null || undefined");
   58. return;
   59. }
   60. // videoProfile的宽高需要与AVRecorderProfile的宽高保持一致，并且需要使用AVRecorderProfile所支持的宽高
   61. let videoSize: camera.Size = {
   62. width: 640,
   63. height: 480
   64. }
   65. let previewProfile: undefined | camera.Profile = getPreviewProfile(previewProfilesArray, videoSize);
   66. if (!previewProfile) {
   67. console.error('previewProfile is not found');
   68. return;
   69. }
   70. let videoProfile: undefined | camera.VideoProfile = getVideoProfile(videoProfilesArray, videoSize);
   71. if (!videoProfile) {
   72. console.error('videoProfile is not found');
   73. return;
   74. }
   75. // 配置参数以实际硬件设备支持的范围为准
   76. let aVRecorderProfile: media.AVRecorderProfile = {
   77. audioBitrate: 48000,
   78. audioChannels: 2,
   79. audioCodec: media.CodecMimeType.AUDIO_AAC,
   80. audioSampleRate: 48000,
   81. fileFormat: media.ContainerFormatType.CFT_MPEG_4,
   82. videoBitrate: 2000000,
   83. videoCodec: media.CodecMimeType.VIDEO_HEVC,
   84. videoFrameWidth: videoSize.width,
   85. videoFrameHeight: videoSize.height,
   86. videoFrameRate: 30,
   87. isHdr: true
   88. };
   89. let options: photoAccessHelper.CreateOptions = {
   90. title: Date.now().toString()
   91. };
   92. let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
   93. let videoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.VIDEO, 'mp4', options);
   94. let file: fileIo.File = fileIo.openSync(videoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   95. let aVRecorderConfig: media.AVRecorderConfig = {
   96. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
   97. videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
   98. profile: aVRecorderProfile,
   99. url: `fd://${file.fd.toString()}`, // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数，eg.fd://45--file:///data/media/01.mp4
   100. rotation: 0, // 合理值0、90、180、270，非合理值prepare接口将报错
   101. location: { latitude: 30, longitude: 130 }
   102. };

   104. let avRecorder: media.AVRecorder | undefined = undefined;
   105. try {
   106. avRecorder = await media.createAVRecorder();
   107. } catch (error) {
   108. let err = error as BusinessError;
   109. console.error(`createAVRecorder call failed. error code: ${err.code}`);
   110. }

   112. if (avRecorder === undefined) {
   113. return;
   114. }

   116. try {
   117. await avRecorder.prepare(aVRecorderConfig);
   118. } catch (error) {
   119. let err = error as BusinessError;
   120. console.error(`prepare call failed. error code: ${err.code}`);
   121. }

   123. let videoSurfaceId: string | undefined = undefined; // 该surfaceID用于传递给相机接口创建videoOutput
   124. try {
   125. videoSurfaceId = await avRecorder.getInputSurface();
   126. } catch (error) {
   127. let err = error as BusinessError;
   128. console.error(`getInputSurface call failed. error code: ${err.code}`);
   129. }
   130. if (videoSurfaceId === undefined) {
   131. return;
   132. }
   133. // 创建VideoOutput对象
   134. let videoOutput: camera.VideoOutput | undefined = undefined;
   135. try {
   136. videoOutput = cameraManager.createVideoOutput(videoProfile, videoSurfaceId);
   137. } catch (error) {
   138. let err = error as BusinessError;
   139. console.error(`Failed to create the videoOutput instance. error: ${JSON.stringify(err)}`);
   140. }
   141. if (videoOutput === undefined) {
   142. return;
   143. }
   144. // 监听视频输出错误信息
   145. videoOutput.on('error', (error: BusinessError) => {
   146. console.error(`Preview output error code: ${error.code}`);
   147. });

   149. // 创建会话
   150. let videoSession: camera.VideoSession | undefined = undefined;
   151. try {
   152. videoSession = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
   153. } catch (error) {
   154. let err = error as BusinessError;
   155. console.error(`Failed to create the session instance. error: ${JSON.stringify(err)}`);
   156. }
   157. if (videoSession === undefined) {
   158. return;
   159. }
   160. // 监听session错误信息
   161. videoSession.on('error', (error: BusinessError) => {
   162. console.error(`Video session error code: ${error.code}`);
   163. });

   165. // 开始配置会话
   166. try {
   167. videoSession.beginConfig();
   168. } catch (error) {
   169. let err = error as BusinessError;
   170. console.error(`Failed to beginConfig. error: ${JSON.stringify(err)}`);
   171. }

   173. // 创建相机输入流
   174. let cameraInput: camera.CameraInput | undefined = undefined;
   175. try {
   176. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
   177. } catch (error) {
   178. let err = error as BusinessError;
   179. console.error(`Failed to createCameraInput. error: ${JSON.stringify(err)}`);
   180. }
   181. if (cameraInput === undefined) {
   182. return;
   183. }
   184. // 监听cameraInput错误信息
   185. let cameraDevice: camera.CameraDevice = cameraArray[0];
   186. cameraInput.on('error', cameraDevice, (error: BusinessError) => {
   187. console.error(`Camera input error code: ${error.code}`);
   188. });

   190. // 打开相机
   191. try {
   192. await cameraInput.open();
   193. } catch (error) {
   194. let err = error as BusinessError;
   195. console.error(`Failed to open cameraInput. error: ${JSON.stringify(err)}`);
   196. }

   198. // 向会话中添加相机输入流
   199. try {
   200. videoSession.addInput(cameraInput);
   201. } catch (error) {
   202. let err = error as BusinessError;
   203. console.error(`Failed to add cameraInput. error: ${JSON.stringify(err)}`);
   204. }

   206. // 创建预览输出流，其中参数 surfaceId 参考下面 XComponent 组件，预览流为XComponent组件提供的surface
   207. let previewOutput: camera.PreviewOutput | undefined = undefined;
   208. try {
   209. previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
   210. } catch (error) {
   211. let err = error as BusinessError;
   212. console.error(`Failed to create the PreviewOutput instance. error: ${JSON.stringify(err)}`);
   213. }

   215. if (previewOutput === undefined) {
   216. return;
   217. }
   218. // 向会话中添加预览输出流
   219. try {
   220. videoSession.addOutput(previewOutput);
   221. } catch (error) {
   222. let err = error as BusinessError;
   223. console.error(`Failed to add previewOutput. error: ${JSON.stringify(err)}`);
   224. }

   226. // 向会话中添加录像输出流
   227. try {
   228. videoSession.addOutput(videoOutput);
   229. } catch (error) {
   230. let err = error as BusinessError;
   231. console.error(`Failed to add videoOutput. error: ${JSON.stringify(err)}`);
   232. }

   234. // 设置色彩空间
   235. setColorSpaceBeforeCommitConfig(videoSession, true);

   237. // 提交会话配置
   238. try {
   239. await videoSession.commitConfig();
   240. } catch (error) {
   241. let err = error as BusinessError;
   242. console.error(`videoSession commitConfig error: ${JSON.stringify(err)}`);
   243. }

   245. // 设置视频防抖
   246. setVideoStabilizationMode(videoSession);

   248. // 启动会话
   249. try {
   250. await videoSession.start();
   251. } catch (error) {
   252. let err = error as BusinessError;
   253. console.error(`videoSession start error: ${JSON.stringify(err)}`);
   254. }

   256. // 启动录像输出流
   257. videoOutput.start((err: BusinessError) => {
   258. if (err) {
   259. console.error(`Failed to start the video output. error: ${JSON.stringify(err)}`);
   260. return;
   261. }
   262. console.info('Callback invoked to indicate the video output start success.');
   263. });

   265. // 开始录像
   266. try {
   267. await avRecorder.start();
   268. } catch (error) {
   269. let err = error as BusinessError;
   270. console.error(`avRecorder start error: ${JSON.stringify(err)}`);
   271. }

   273. // 停止录像输出流
   274. videoOutput.stop((err: BusinessError) => {
   275. if (err) {
   276. console.error(`Failed to stop the video output. error: ${JSON.stringify(err)}`);
   277. return;
   278. }
   279. console.info('Callback invoked to indicate the video output stop success.');
   280. });

   282. // 停止录像
   283. try {
   284. await avRecorder.stop();
   285. } catch (error) {
   286. let err = error as BusinessError;
   287. console.error(`avRecorder stop error: ${JSON.stringify(err)}`);
   288. }

   290. // 停止当前会话
   291. await videoSession.stop();

   293. // 关闭文件
   294. fileIo.closeSync(file);

   296. // 释放相机输入流
   297. await cameraInput.close();

   299. // 释放预览输出流
   300. await previewOutput.release();

   302. // 释放录像输出流
   303. await videoOutput.release();

   305. // 释放会话
   306. await videoSession.release();

   308. // 会话置空
   309. videoSession = undefined;
   310. }
   ```
