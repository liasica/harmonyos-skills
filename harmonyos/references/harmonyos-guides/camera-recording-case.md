---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-recording-case
title: 录像实践(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 录像实践(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:b84b74e9b265589e2dcdf707f10f6dfed251a1f3a0da741b9cff87171384476e
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

当前示例提供完整的录像流程介绍，方便开发者了解完整的接口调用顺序。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[录像](camera-recording.md)等单个流程。

如需要将视频保存到媒体库中可参考[保存媒体库资源](photoaccesshelper-savebutton.md)。

## 开发流程

在获取到相机支持的输出流能力后，开始创建录像流，开发流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Ki3cU-JFQVKaPBjBgIRB3Q/zh-cn_image_0000002583478567.png?HW-CC-KV=V1&HW-CC-Date=20260427T234556Z&HW-CC-Expire=86400&HW-CC-Sign=46DE5E0C78CDE626698CF801B505167F9A0B1BC0A320ACB28A1FFCE3A6EF2855)

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { media } from '@kit.MediaKit';
4. import { common } from '@kit.AbilityKit';
5. import { fileIo } from '@kit.CoreFileKit';
6. import { JSON } from '@kit.ArkTS';

8. interface RecordingResources {
9. avRecorder?: media.AVRecorder;
10. videoOutput?: camera.VideoOutput;
11. cameraInput?: camera.CameraInput;
12. previewOutput?: camera.PreviewOutput;
13. videoSession?: camera.VideoSession;
14. file?: fileIo.File;
15. }

17. // 全局资源跟踪。
18. const resources: RecordingResources = {};

20. async function releaseResources(): Promise<void> {
21. const releaseSteps = [
22. // 停止录像。
23. async () => await resources.avRecorder?.stop().catch((e: BusinessError) => console.error('停止录像失败:', e)),
24. // 停止视频输出。
25. async () => await resources.videoOutput?.stop().catch((e: BusinessError) => console.error('停止视频输出失败:', e)),
26. // 停止会话。
27. async () => await resources.videoSession?.stop().catch((e: BusinessError) => console.error('停止会话失败:', e)),
28. // 释放录像器。
29. async () => await resources.avRecorder?.release().catch((e: BusinessError) => console.error('释放录像器失败:', e)),
30. // 关闭相机输入。
31. async () => await resources.cameraInput?.close().catch((e: BusinessError) => console.error('关闭相机输入失败:', e)),
32. // 释放视频输出。
33. async () => await resources.videoOutput?.release().catch((e: BusinessError) => console.error('释放视频输出失败:', e)),
34. // 释放预览输出。
35. async () => await resources.previewOutput?.release().catch((e: BusinessError) => console.error('释放预览输出失败:', e)),
36. // 释放会话。
37. async () => await resources.videoSession?.release().catch((e: BusinessError) => console.error('释放会话失败:', e)),
38. // 关闭文件。
39. async () => {
40. if (resources.file) {
41. try {
42. await fileIo.close(resources.file);
43. } catch (e) {
44. console.error('Failure to close file');
45. }
46. }
47. },
48. ];

50. // 按顺序执行释放步骤。
51. for (const step of releaseSteps) {
52. await step();
53. }
54. // 清空资源引用。
55. resources.avRecorder = undefined;
56. resources.videoOutput = undefined;
57. resources.cameraInput = undefined;
58. resources.previewOutput = undefined;
59. resources.videoSession = undefined;
60. resources.file = undefined;
61. }

63. async function videoRecording(context: common.Context, surfaceId: string): Promise<void> {
64. // 创建CameraManager对象。
65. let cameraManager: camera.CameraManager | undefined = undefined;
66. try {
67. cameraManager = camera.getCameraManager(context);
68. } catch (error) {
69. console.error(`getCameraManager call failed, error: ${JSON.stringify(error)}`);
70. }

72. if (!cameraManager) {
73. console.error("cameraManager is null");
74. return;
75. }

77. // 获取相机列表。
78. let cameraArray: Array<camera.CameraDevice> = [];
79. try {
80. cameraArray = cameraManager.getSupportedCameras();
81. } catch (error) {
82. let err = error as BusinessError;
83. console.error(`getSupportedCameras call failed. error code: ${JSON.stringify(err)}`);
84. }

86. if (!cameraArray || cameraArray.length <= 0) {
87. console.error("cameraManager.getSupportedCameras error");
88. return;
89. }

91. // 获取支持的模式类型。
92. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
93. let isSupportVideoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_VIDEO) >= 0;
94. if (!isSupportVideoMode) {
95. console.error('video mode not support');
96. return;
97. }

99. // 示例代码默认选择第一个镜头，实际开发需根据所需镜头。
100. const cameraDevice: camera.CameraDevice = cameraArray[0];

102. // 获取相机设备支持的输出流能力。
103. let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraDevice,
104. camera.SceneMode.NORMAL_VIDEO);
105. if (!cameraOutputCap) {
106. console.error("cameraOutputCap is null");
107. return;
108. }
109. console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

111. let videoProfilesArray: Array<camera.VideoProfile> = cameraOutputCap.videoProfiles;
112. if (!videoProfilesArray || videoProfilesArray.length === 0) {
113. console.error("videoProfilesArray is null or []");
114. return;
115. }

117. // videoProfile的宽高需要与AVRecorderProfile的宽高保持一致，并且需要使用AVRecorderProfile所支持的宽高。
118. // 示例代码默认选择第一个videoProfile，实际开发需根据所需筛选videoProfile。
119. const videoProfile: camera.VideoProfile = cameraOutputCap.videoProfiles[0];
120. let videoUri: string = context.filesDir + '/' + 'VIDEO_' + Date.parse(new Date().toString()) + '.mp4'; // 本地沙箱路径。
121. try {
122. resources.file = fileIo.openSync(videoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
123. } catch (error) {
124. console.error(`openSync call failed, error: ${JSON.stringify(error)}`);
125. return;
126. }

128. // 创建并配置AVRecorder。
129. const isHdr: boolean = [
130. camera.CameraFormat.CAMERA_FORMAT_YCBCR_P010,
131. camera.CameraFormat.CAMERA_FORMAT_YCRCB_P010
132. ].includes(videoProfile.format);
133. // 配置参数以实际硬件设备支持的范围为准。
134. let aVRecorderProfile: media.AVRecorderProfile = {
135. audioBitrate: 48000,
136. audioChannels: 2,
137. audioCodec: media.CodecMimeType.AUDIO_AAC,
138. audioSampleRate: 48000,
139. fileFormat: media.ContainerFormatType.CFT_MPEG_4,
140. videoBitrate: 2000000,
141. videoCodec: isHdr ? media.CodecMimeType.VIDEO_HEVC : media.CodecMimeType.VIDEO_AVC,
142. videoFrameWidth: videoProfile.size.width,
143. videoFrameHeight: videoProfile.size.height,
144. videoFrameRate: 30,
145. isHdr: isHdr
146. };

148. let avMetadata: media.AVMetadata = {
149. videoOrientation: '0', // 合理值0、90、180、270，非合理值prepare接口将报错。
150. location: { latitude: 30, longitude: 130 }
151. }
152. let aVRecorderConfig: media.AVRecorderConfig = {
153. audioSourceType: media.AudioSourceType.AUDIO_SOURCE_TYPE_MIC,
154. videoSourceType: media.VideoSourceType.VIDEO_SOURCE_TYPE_SURFACE_YUV,
155. profile: aVRecorderProfile,
156. url: `fd://${resources.file.fd.toString()}`, // 文件需先由调用者创建，赋予读写权限，将文件fd传给此参数，eg.fd://45--file:///data/media/01.mp4
157. rotation: 0, // 合理值0、90、180、270，非合理值prepare接口将报错。
158. metadata: avMetadata
159. };

161. try {
162. resources.avRecorder = await media.createAVRecorder();
163. } catch (error) {
164. let err = error as BusinessError;
165. console.error(`createAVRecorder call failed. error code: ${JSON.stringify(err)}`);
166. return;
167. }

169. if (!resources.avRecorder) {
170. console.error(`avRecorder is null`);
171. return;
172. }

174. try {
175. await resources.avRecorder.prepare(aVRecorderConfig);
176. } catch (error) {
177. let err = error as BusinessError;
178. console.error(`prepare call failed. error code: ${JSON.stringify(err)}`);
179. await releaseResources();
180. return;
181. }

183. // 获取视频输入surface。
184. let videoSurfaceId: string | undefined = undefined; // 该surfaceID用于传递给相机接口创造videoOutput。
185. try {
186. videoSurfaceId = await resources.avRecorder.getInputSurface();
187. } catch (error) {
188. let err = error as BusinessError;
189. console.error(`getInputSurface call failed. error code: ${JSON.stringify(err)}`);
190. await releaseResources();
191. return;
192. }

194. if (!videoSurfaceId) {
195. await releaseResources();
196. return;
197. }

199. // 创建VideoOutput对象。
200. try {
201. resources.videoOutput = cameraManager.createVideoOutput(videoProfile, videoSurfaceId);
202. } catch (error) {
203. let err = error as BusinessError;
204. console.error(`Failed to create the videoOutput instance. error: ${JSON.stringify(err)}`);
205. await releaseResources();
206. return;
207. }
208. if (!resources.videoOutput) {
209. console.error('videoOutput is null');
210. await releaseResources();
211. return;
212. }

214. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
215. if (!previewProfilesArray || previewProfilesArray.length === 0) {
216. console.error("previewProfilesArray is null or []");
217. return;
218. }

220. // 创建预览输出流，其中参数surfaceId是由XComponent组件提供的。
221. const previewProfile = previewProfilesArray.find((previewProfile: camera.Profile) => {
222. return Math.abs((previewProfile.size.width / previewProfile.size.height) - (videoProfile.size.width / videoProfile.size.height)) < Number.EPSILON;
223. }); // 筛选与录像分辨率宽高比一致的预览分辨率。
224. if (!previewProfile) {
225. console.error('No preview resolution found that matches the aspect ratio of the video resolution');
226. await releaseResources();
227. return;
228. }

230. try {
231. resources.previewOutput = cameraManager.createPreviewOutput(previewProfile, surfaceId);
232. } catch (error) {
233. let err = error as BusinessError;
234. console.error(`createPreviewOutput call failed. error: ${JSON.stringify(err)}`);
235. await releaseResources();
236. return;
237. }
238. if (!resources.previewOutput) {
239. console.error('previewOutput is null');
240. await releaseResources();
241. return;
242. }

244. // 创建相机输入流。
245. try {
246. resources.cameraInput = cameraManager.createCameraInput(cameraDevice);
247. } catch (error) {
248. let err = error as BusinessError;
249. console.error(`Failed to createCameraInput. error: ${JSON.stringify(err)}`);
250. await releaseResources();
251. return;
252. }
253. if (!resources.cameraInput) {
254. console.error('cameraInput is null');
255. await releaseResources();
256. return;
257. }

259. // 监听cameraInput错误信息。
260. resources.cameraInput!.on('error', cameraDevice, (error: BusinessError) => {
261. console.error(`Camera input error code: ${error.code}`);
262. });

264. // 打开相机。
265. try {
266. await resources.cameraInput!.open();
267. } catch (error) {
268. let err = error as BusinessError;
269. console.error(`Failed to open cameraInput. error: ${err}`);
270. }

272. // 创建会话。
273. try {
274. resources.videoSession = cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO) as camera.VideoSession;
275. } catch (error) {
276. let err = error as BusinessError;
277. console.error(`Failed to create the session instance. error: ${JSON.stringify(err)}`);
278. await releaseResources();
279. return;
280. }
281. if (!resources.videoSession) {
282. console.error('videoSession is null');
283. await releaseResources();
284. return;
285. }
286. // 监听session错误信息。
287. resources.videoSession!.on('error', (error: BusinessError) => {
288. console.error(`Video session error code: ${error.code}`);
289. });

291. // 开始配置会话。
292. try {
293. resources.videoSession!.beginConfig();
294. resources.videoSession!.addInput(resources.cameraInput!);
295. resources.videoSession!.addOutput(resources.videoOutput!);
296. resources.videoSession!.addOutput(resources.previewOutput!);
297. await resources.videoSession!.commitConfig();
298. await resources.videoSession!.start();
299. } catch (error) {
300. let err = error as BusinessError;
301. console.error(`Session Configuration Failure. error: ${err}`);
302. await releaseResources();
303. return;
304. }

306. // 启动录像。
307. try {
308. await resources.videoOutput!.start();
309. await resources.avRecorder!.start();
310. } catch (error) {
311. let err = error as BusinessError;
312. console.error(`avRecorder start error: ${err}`);
313. }

315. // 停止录像。
316. try {
317. await resources.avRecorder!.stop();
318. await resources.videoOutput!.stop();
319. } catch (error) {
320. let err = error as BusinessError;
321. console.error(`avRecorder stop error: ${err}`);
322. }

324. // 停止当前会话。
325. await resources.videoSession.stop();

327. // 关闭文件。
328. try {
329. fileIo.closeSync(resources.file);
330. } catch (error) {
331. let err = error as BusinessError;
332. console.error(`closeSync failed, error: ${err}`);
333. }

336. // 释放相机输入流。
337. await resources.cameraInput.close();

339. // 释放预览输出流。
340. try {
341. await resources.previewOutput.release();
342. } catch (error) {
343. let err = error as BusinessError;
344. console.error(`release previewOutput failed, error: ${err.code}`);
345. }

348. // 释放录像输出流。
349. try {
350. await resources.videoOutput.release();
351. } catch (error) {
352. let err = error as BusinessError;
353. console.error(`release videoOutput failed, error: ${err.code}`);
354. }

356. // 释放会话。
357. try {
358. await resources.videoSession.release();
359. } catch (error) {
360. let err = error as BusinessError;
361. console.error(`release videoSession failed, error: ${err.code}`);
362. }

364. // 会话置空。
365. resources.videoSession = undefined;
366. }
```
