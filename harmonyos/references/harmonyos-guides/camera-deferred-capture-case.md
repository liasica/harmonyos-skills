---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-deferred-capture-case
title: 分段式拍照实践(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 分段式拍照实践(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:77c885b5461196c6a9bf83cccffd7d5fd946f587f0f2623d668841e8819e35ad
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

当前示例提供完整的分段式拍照流程介绍，方便开发者了解完整的接口调用顺序。

在参考以下示例前，建议开发者查看[分段式拍照(ArkTS)](camera-deferred-capture.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[拍照](camera-shooting.md)等单个流程。

## 开发流程

在获取到相机支持的输出流能力后，开始创建拍照流，开发流程如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/uzdhk94uSYqd6hVRDhl0zw/zh-cn_image_0000002552798918.png?HW-CC-KV=V1&HW-CC-Date=20260427T234557Z&HW-CC-Expire=86400&HW-CC-Sign=BDC9A5BCD90236AF2D99C40F07F2EAF52CB3BED60D44FEA47DA71C1AD95F8478)

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
4. import { photoAccessHelper } from '@kit.MediaLibraryKit';

6. let photoSession: camera.PhotoSession | undefined = undefined;
7. let cameraInput: camera.CameraInput | undefined = undefined;
8. let previewOutput: camera.PreviewOutput | undefined = undefined;
9. let photoOutput: camera.PhotoOutput | undefined = undefined;

11. function getPhotoAccessHelper(context: Context): photoAccessHelper.PhotoAccessHelper {
12. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
13. return phAccessHelper;
14. }

16. class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
17. onDataPrepared(data: ArrayBuffer) {
18. if (data === undefined) {
19. console.error('Error occurred when preparing data');
20. return;
21. }
22. console.info('on image data prepared');
23. // 请在获取到拍照buffer后，再释放session，提前释放session，会导致无法正常出图。
24. releaseCamSession();
25. }
26. }

28. async function mediaLibRequestBuffer(photoAsset: photoAccessHelper.PhotoAsset, context: Context) {
29. let requestOptions: photoAccessHelper.RequestOptions = {
30. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
31. }
32. const handler = new MediaDataHandler();
33. await photoAccessHelper.MediaAssetManager.requestImageData(context, photoAsset, requestOptions, handler);
34. console.info('requestImageData successfully');
35. }

37. async function mediaLibSavePhoto(photoAsset: photoAccessHelper.PhotoAsset,
38. phAccessHelper: photoAccessHelper.PhotoAccessHelper): Promise<void> {
39. try {
40. let assetChangeRequest: photoAccessHelper.MediaAssetChangeRequest =
41. new photoAccessHelper.MediaAssetChangeRequest(photoAsset);
42. assetChangeRequest.saveCameraPhoto();
43. await phAccessHelper.applyChanges(assetChangeRequest);
44. console.info('apply saveCameraPhoto successfully');
45. } catch (err) {
46. console.error(`apply saveCameraPhoto failed with error: ${err.code}, ${err.message}`);
47. }
48. }

50. function setPhotoOutputCb(photoOutput: camera.PhotoOutput, context: Context): void {
51. // 监听回调之后，调用photoOutput的capture方法，低质量图上报后触发回调。
52. photoOutput.on('photoAssetAvailable', async (err: BusinessError, photoAsset: photoAccessHelper.PhotoAsset): Promise<void> => {
53. console.info('getPhotoAsset start');
54. console.error(`err: ${err}`);
55. if ((err !== undefined && err.code !== 0) || photoAsset === undefined) {
56. console.error('getPhotoAsset failed');
57. return;
58. }
59. // 调用媒体库落盘接口保存一阶段低质量图，二阶段真图就绪后媒体库会主动帮应用替换落盘图片。
60. await mediaLibSavePhoto(photoAsset, getPhotoAccessHelper(context));
61. // 调用媒体库接口注册低质量图或高质量图buffer回调，自定义处理。
62. // mediaLibRequestBuffer(photoAsset, context);
63. });
64. }

67. async function deferredCaptureCase(context: Context, surfaceId: string): Promise<void> {
68. // 创建CameraManager对象。
69. let cameraManager: camera.CameraManager = camera.getCameraManager(context);
70. if (!cameraManager) {
71. console.error('camera.getCameraManager error');
72. return;
73. }
74. // 监听相机状态变化。
75. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
76. if (err !== undefined && err.code !== 0) {
77. console.error('cameraStatus with errorCode = ' + err.code);
78. return;
79. }
80. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
81. console.info(`status: ${cameraStatusInfo.status}`);
82. });

84. // 获取相机列表。
85. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
86. if (cameraArray.length <= 0) {
87. console.error('cameraManager.getSupportedCameras error');
88. return;
89. }

91. for (let index = 0; index < cameraArray.length; index++) {
92. console.info('cameraId : ' + cameraArray[index].cameraId); // 获取相机ID。
93. console.info('cameraPosition : ' + cameraArray[index].cameraPosition); // 获取相机位置。
94. console.info('cameraType : ' + cameraArray[index].cameraType); // 获取相机类型。
95. console.info('connectionType : ' + cameraArray[index].connectionType); // 获取相机连接类型。
96. }

98. // 创建相机输入流。
99. try {
100. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
101. } catch (error) {
102. let err = error as BusinessError;
103. console.error('Failed to createCameraInput errorCode = ' + err.code);
104. }
105. if (cameraInput === undefined) {
106. return;
107. }

109. // 监听cameraInput错误信息。
110. let cameraDevice: camera.CameraDevice = cameraArray[0];
111. cameraInput.on('error', cameraDevice, (error: BusinessError) => {
112. console.error(`Camera input error code: ${error.code}`);
113. });

115. // 打开相机。
116. await cameraInput.open();

118. // 获取支持的模式类型。
119. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
120. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
121. if (!isSupportPhotoMode) {
122. console.error('photo mode not support');
123. return;
124. }
125. // 获取相机设备支持的输出流能力。
126. let cameraOutputCap: camera.CameraOutputCapability =
127. cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
128. if (!cameraOutputCap) {
129. console.error('cameraManager.getSupportedOutputCapability error');
130. return;
131. }
132. console.info('outputCapability: ' + JSON.stringify(cameraOutputCap));

134. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
135. if (!previewProfilesArray) {
136. console.error('createOutput previewProfilesArray == null || undefined');
137. }

139. let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
140. if (!photoProfilesArray) {
141. console.error('createOutput photoProfilesArray == null || undefined');
142. }

144. // 创建预览输出流,其中参数surfaceId参考上文XComponent组件，预览流为XComponent组件提供的surface。
145. try {
146. previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
147. } catch (error) {
148. let err = error as BusinessError;
149. console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
150. }
151. if (previewOutput === undefined) {
152. return;
153. }

155. // 监听预览输出错误信息。
156. previewOutput.on('error', (error: BusinessError) => {
157. console.error(`Preview output error code: ${error.code}`);
158. });

160. // 创建拍照输出流。
161. try {
162. photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
163. } catch (error) {
164. let err = error as BusinessError;
165. console.error('Failed to createPhotoOutput errorCode = ' + err.code);
166. }
167. if (photoOutput === undefined) {
168. return;
169. }

171. // 注册监听photoAssetAvailable回调。
172. setPhotoOutputCb(photoOutput, context);

174. // 创建会话。
175. try {
176. photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
177. } catch (error) {
178. let err = error as BusinessError;
179. console.error('Failed to create the session instance. errorCode = ' + err.code);
180. }
181. if (photoSession === undefined) {
182. return;
183. }
184. // 监听session错误信息。
185. photoSession.on('error', (error: BusinessError) => {
186. console.error(`Capture session error code: ${error.code}`);
187. });

189. // 开始配置会话。
190. try {
191. photoSession.beginConfig();
192. } catch (error) {
193. let err = error as BusinessError;
194. console.error('Failed to beginConfig. errorCode = ' + err.code);
195. }

197. // 向会话中添加相机输入流。
198. try {
199. photoSession.addInput(cameraInput);
200. } catch (error) {
201. let err = error as BusinessError;
202. console.error('Failed to addInput. errorCode = ' + err.code);
203. }

205. // 向会话中添加预览输出流。
206. try {
207. photoSession.addOutput(previewOutput);
208. } catch (error) {
209. let err = error as BusinessError;
210. console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
211. }

213. // 向会话中添加拍照输出流。
214. try {
215. photoSession.addOutput(photoOutput);
216. } catch (error) {
217. let err = error as BusinessError;
218. console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
219. }

221. // 提交会话配置。
222. await photoSession.commitConfig();

224. // 启动会话。
225. await photoSession.start().then(() => {
226. console.info('Promise returned to indicate the session start success.');
227. });
228. // 判断设备是否支持闪光灯。
229. let flashStatus: boolean = false;
230. try {
231. flashStatus = photoSession.hasFlash();
232. } catch (error) {
233. let err = error as BusinessError;
234. console.error('Failed to hasFlash. errorCode = ' + err.code);
235. }
236. console.info('Returned with the flash light support status:' + flashStatus);

238. if (flashStatus) {
239. // 判断是否支持自动闪光灯模式。
240. let flashModeStatus: boolean = false;
241. try {
242. let status: boolean = photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
243. flashModeStatus = status;
244. } catch (error) {
245. let err = error as BusinessError;
246. console.error('Failed to check whether the flash mode is supported. errorCode = ' + err.code);
247. }
248. if (flashModeStatus) {
249. // 设置自动闪光灯模式。
250. try {
251. photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
252. } catch (error) {
253. let err = error as BusinessError;
254. console.error('Failed to set the flash mode. errorCode = ' + err.code);
255. }
256. }
257. }

259. // 判断是否支持连续自动变焦模式。
260. let focusModeStatus: boolean = false;
261. try {
262. let status: boolean = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
263. focusModeStatus = status;
264. } catch (error) {
265. let err = error as BusinessError;
266. console.error('Failed to check whether the focus mode is supported. errorCode = ' + err.code);
267. }

269. if (focusModeStatus) {
270. // 设置连续自动变焦模式。
271. try {
272. photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
273. } catch (error) {
274. let err = error as BusinessError;
275. console.error('Failed to set the focus mode. errorCode = ' + err.code);
276. }
277. }

279. // 获取相机支持的可变焦距比范围。
280. let zoomRatioRange: Array<number> = [];
281. try {
282. zoomRatioRange = photoSession.getZoomRatioRange();
283. } catch (error) {
284. let err = error as BusinessError;
285. console.error('Failed to get the zoom ratio range. errorCode = ' + err.code);
286. }
287. if (zoomRatioRange.length <= 0) {
288. return;
289. }

291. // 设置可变焦距比。
292. try {
293. photoSession.setZoomRatio(zoomRatioRange[0]);
294. } catch (error) {
295. let err = error as BusinessError;
296. console.error('Failed to set the zoom ratio value. errorCode = ' + err.code);
297. }
298. let photoCaptureSetting: camera.PhotoCaptureSetting = {
299. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高。
300. rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0。
301. }

303. // 使用当前拍照设置触发一次拍照。
304. photoOutput.capture(photoCaptureSetting, (err: BusinessError) => {
305. if (err) {
306. console.error(`Failed to capture the photo ${err.message}`);
307. return;
308. }
309. console.info('Callback invoked to indicate the photo capture request success.');
310. });
311. }

313. async function releaseCamSession() {
314. // 停止当前会话。
315. await photoSession?.stop();

317. // 释放拍照输出流。
318. await photoOutput?.release();

320. // 释放预览输出流。
321. await previewOutput?.release();

323. // 释放相机输入流。
324. await cameraInput?.close();

326. // 释放会话。
327. await photoSession?.release();

329. // 会话置空。
330. photoSession = undefined;
331. }

333. @Entry
334. @Component
335. struct Index {
336. @State message: string = 'PhotoAssetDemo';
337. @State isShow: boolean = false;
338. private mXComponentController: XComponentController = new XComponentController();
339. private surfaceId = '';
340. private uiContext: UIContext = this.getUIContext();
341. private context: Context | undefined = this.uiContext.getHostContext();
342. private cameraPermission: Permissions = 'ohos.permission.CAMERA'; // 申请权限相关问题可参考本篇开头的申请相关权限文档
343. private mXComponentOptions: XComponentOptions = {
344. type: XComponentType.SURFACE,
345. controller: this.mXComponentController
346. }

349. async requestPermissionsFn(): Promise<void> {
350. let atManager = abilityAccessCtrl.createAtManager();
351. if (this.context) {
352. let res = await atManager.requestPermissionsFromUser(this.context, [this.cameraPermission]);
353. for (let i = 0; i < res.permissions.length; i++) {
354. if (this.cameraPermission.toString() === res.permissions[i] && res.authResults[i] === 0) {
355. this.isShow = true;
356. }
357. }
358. }
359. }

361. aboutToAppear(): void {
362. this.requestPermissionsFn();
363. }

365. build() {
366. Column() {
367. Column() {
368. if (this.isShow) {
369. XComponent(this.mXComponentOptions)
370. .onLoad(async () => {
371. console.info('onLoad is called');
372. if (this.context) {
373. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
374. console.info(`onLoad surfaceId: ${this.surfaceId}`);
375. deferredCaptureCase(this.context, this.surfaceId);
376. }
377. })
378. .renderFit(RenderFit.RESIZE_CONTAIN)
379. }
380. }
381. .height('95%')
382. .justifyContent(FlexAlign.Center)

384. Text(this.message)
385. .id('PhotoAssetDemo')
386. .fontSize(38)
387. .fontWeight(FontWeight.Bold)
388. .alignRules({
389. center: { anchor: '__container__', align: VerticalAlign.Center },
390. middle: { anchor: '__container__', align: HorizontalAlign.Center }
391. })
392. }
393. .height('100%')
394. .width('100%')
395. }
396. }
```
