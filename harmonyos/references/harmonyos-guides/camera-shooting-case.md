---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-shooting-case
title: 拍照实践(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 拍照实践(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ff43dd0dc344b8de2da36635c7a27c934fd7150497d55533d6e0a06a43047b66
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

当前示例提供完整的拍照流程介绍，方便开发者了解完整的接口调用顺序。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[拍照](camera-shooting.md)等单个流程。

## 开发流程

在获取到相机支持的输出流能力后，开始创建拍照流，开发流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/hRuZ6gcvSWuMSmYLKE_i1A/zh-cn_image_0000002552958566.png?HW-CC-KV=V1&HW-CC-Date=20260427T234555Z&HW-CC-Expire=86400&HW-CC-Sign=19BF24FDFF518FE204DEB82E30EA53CA12FA3773892DDC39EE36F625024CC51D)

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

如需要在图库中看到所保存的图片、视频资源，需要将其保存到媒体库，保存方式请参考：[保存媒体库资源](photoaccesshelper-savebutton.md)。

需要在[photoOutput.on('photoAvailable')](../harmonyos-references/arkts-apis-camera-photooutput.md#onphotoavailable11)接口获取到buffer时，将buffer在安全控件中保存到媒体库。

```
1. import { camera } from '@kit.CameraKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. interface ShootingResources {
6. cameraInput?: camera.CameraInput;
7. previewOutput?: camera.PreviewOutput;
8. photoOutput?: camera.PhotoOutput;
9. photoSession?: camera.PhotoSession;
10. }

12. const resources: ShootingResources = {};

14. function setPhotoOutputCb(photoOutput: camera.PhotoOutput): void {
15. if (!photoOutput) {
16. console.error('photoOutput is null');
17. return;
18. }
19. // 设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中。
20. photoOutput?.on('photoAvailable', (err: BusinessError, photo: camera.Photo): void => {
21. console.info('getPhoto start');
22. console.error(`err: ${err}`);
23. if (err && err.code != 0) {
24. console.error('getPhoto failed');
25. return;
26. }
27. if (!photo || !photo.main) {
28. console.error('photo is null');
29. return;
30. }
31. let imageObj = photo.main;
32. imageObj.getComponent(image.ComponentType.JPEG, (errCode: BusinessError, component: image.Component): void => {
33. console.info('getComponent start');
34. if (errCode && errCode.code != 0 ) {
35. console.error('getComponent failed');
36. imageObj.release();
37. return;
38. }
39. let buffer: ArrayBuffer;
40. if (component && component.byteBuffer) {
41. buffer = component.byteBuffer;
42. } else {
43. console.error('byteBuffer is null');
44. imageObj.release();
45. return;
46. }
47. // 如需要在图库中看到所保存的图片、视频资源，请使用用户无感的安全控件创建媒体资源。

49. // buffer处理结束后需要释放该资源，如果未正确释放资源会导致后续拍照获取不到buffer。
50. imageObj.release();
51. });
52. });
53. }

55. async function cameraShootingCase(context: Context, surfaceId: string): Promise<void> {
56. try {
57. // 创建CameraManager对象。
58. let cameraManager: camera.CameraManager = camera.getCameraManager(context);
59. if (!cameraManager) {
60. console.error("camera.getCameraManager error");
61. return;
62. }
63. // 监听相机状态变化。
64. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
65. if (err !== undefined && err.code !== 0) {
66. console.error('cameraStatus with errorCode = ' + err.code);
67. return;
68. }
69. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
70. console.info(`status: ${cameraStatusInfo.status}`);
71. });

73. // 获取相机列表。
74. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
75. if (!cameraArray || cameraArray.length <= 0) {
76. console.error("cameraManager.getSupportedCameras error");
77. return;
78. }

80. for (let index = 0; index < cameraArray.length; index++) {
81. console.info('cameraId : ' + cameraArray[index].cameraId);                          // 获取相机ID。
82. console.info('cameraPosition : ' + cameraArray[index].cameraPosition);              // 获取相机位置。
83. console.info('cameraType : ' + cameraArray[index].cameraType);                      // 获取相机类型。
84. console.info('connectionType : ' + cameraArray[index].connectionType);              // 获取相机连接类型。
85. }

87. // 创建相机输入流。
88. resources.cameraInput = cameraManager.createCameraInput(cameraArray[0]);
89. if (!resources.cameraInput) {
90. console.error('cameraInput is null');
91. return;
92. }

94. // 监听cameraInput错误信息。
95. let cameraDevice: camera.CameraDevice = cameraArray[0];
96. resources.cameraInput.on('error', cameraDevice, (error: BusinessError) => {
97. console.error(`Camera input error code: ${error.code}`);
98. })

100. // 打开相机。
101. await resources.cameraInput.open();

103. // 获取支持的模式类型。
104. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
105. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
106. if (!isSupportPhotoMode) {
107. console.error('photo mode not support');
108. releaseResources();
109. return;
110. }
111. // 获取相机设备支持的输出流能力。
112. let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
113. if (!cameraOutputCap) {
114. console.error("cameraManager.getSupportedOutputCapability error");
115. return;
116. }
117. console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

119. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
120. if (!previewProfilesArray || previewProfilesArray.length <= 0) {
121. console.error("previewProfilesArray is null or []");
122. releaseResources();
123. return;
124. }

126. let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
127. if (!photoProfilesArray || photoProfilesArray.length <= 0) {
128. console.error("photoProfilesArray is null or []");
129. releaseResources();
130. return;
131. }

133. // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface。
134. resources.previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
135. if (!resources.previewOutput) {
136. console.error('previewOutput is null');
137. releaseResources();
138. return;
139. }
140. try {
141. // 监听预览输出错误信息。
142. resources.previewOutput.on('error', (error: BusinessError) => {
143. console.error(`Preview output error code: ${error.code}`);
144. });
145. } catch (e) {
146. console.error(`previewOutput.on call failed, error: ${JSON.stringify(e)}`);
147. }

149. // 创建拍照输出流。
150. resources.photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
151. if (!resources.photoOutput) {
152. console.error('photoOutput is null');
153. releaseResources();
154. return;
155. }

157. // 调用上面的回调函数来保存图片。
158. setPhotoOutputCb(resources.photoOutput);

160. // 创建会话。
161. let photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
162. if (!photoSession) {
163. console.error('photoSession is null');
164. releaseResources();
165. return;
166. }
167. resources.photoSession =  photoSession as camera.PhotoSession;
168. try {
169. // 监听session错误信息。
170. resources.photoSession.on('error', (error: BusinessError) => {
171. console.error(`Capture session error code: ${error.code}`);
172. });
173. } catch (e) {
174. console.error(`photoSession.on call failed, error: ${JSON.stringify(e)}`);
175. }

177. // 开始配置会话。
178. resources.photoSession.beginConfig();

180. // 向会话中添加相机输入流。
181. resources.photoSession.addInput(resources.cameraInput);

183. // 向会话中添加预览输出流。
184. resources.photoSession.addOutput(resources.previewOutput);

186. // 向会话中添加拍照输出流。
187. resources.photoSession.addOutput(resources.photoOutput);

189. // 提交会话配置。
190. await resources.photoSession.commitConfig();

192. // 启动会话。
193. await resources.photoSession.start()
194. // 判断设备是否支持闪光灯。
195. let flashStatus: boolean = false;
196. flashStatus = resources.photoSession.hasFlash();
197. console.info('Returned with the flash light support status:' + flashStatus);

199. if (flashStatus) {
200. // 判断是否支持自动闪光灯模式。
201. let flashModeStatus: boolean = resources.photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
202. if(flashModeStatus) {
203. // 设置自动闪光灯模式。
204. resources.photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
205. }
206. }

208. // 判断是否支持连续自动变焦模式。
209. let focusModeStatus: boolean = resources.photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);

211. if (focusModeStatus) {
212. // 设置连续自动变焦模式。
213. resources.photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
214. }

216. // 获取相机支持的可变焦距比范围。
217. let zoomRatioRange: Array<number> = [];
218. try {
219. zoomRatioRange = resources.photoSession.getZoomRatioRange();
220. } catch (error) {
221. let err = error as BusinessError;
222. console.error('Failed to get the zoom ratio range. errorCode = ' + err.code);
223. }
224. if (zoomRatioRange.length > 0) {
225. // 设置可变焦距比。
226. try {
227. resources.photoSession.setZoomRatio(zoomRatioRange[0]);
228. } catch (error) {
229. let err = error as BusinessError;
230. console.error('Failed to set the zoom ratio value. errorCode = ' + err.code);
231. }
232. }

234. let photoCaptureSetting: camera.PhotoCaptureSetting = {
235. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高。
236. rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0。
237. }
238. // 使用当前拍照设置进行拍照。
239. try {
240. await resources.photoOutput.capture(photoCaptureSetting);
241. } catch (error) {
242. let err = error as BusinessError;
243. console.error(`capture call failed, err: ${JSON.stringify(err)}`);
244. }

246. // 需要在拍照结束之后调用以下关闭相机和释放会话流程，避免拍照未结束就将会话释放。

249. // 会话置空。
250. resources.photoSession = undefined;
251. } catch (error) {
252. console.error(`cameraShootingCase call failed, error: ${JSON.stringify(error)}`);
253. releaseResources();
254. }
255. }

257. async function releaseResources(): Promise<void> {
258. // 停止当前会话。
259. await resources.photoSession?.stop().catch((e: BusinessError) => {console.error('停止会话失败:', e)});

261. // 释放相机输入流。
262. await resources.cameraInput?.close().catch((e: BusinessError) => {console.error('关闭相机失败:', e)});

264. // 释放预览输出流。
265. await resources.previewOutput?.release().catch((e: BusinessError) => {console.error('停止预览流失败:', e)});

267. // 释放拍照输出流。
268. await resources.photoOutput?.release().catch((e: BusinessError) => {console.error('停止拍照流失败:', e)});

270. // 释放会话。
271. await resources.photoSession?.release().catch((e: BusinessError) => {console.error('释放会话失败:', e)});
272. }
```
