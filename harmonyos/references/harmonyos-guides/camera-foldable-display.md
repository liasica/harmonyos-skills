---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-foldable-display
title: 适配不同折叠状态的摄像头变更(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 适配不同折叠状态的摄像头变更(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:58+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:1632ce1224163d54815a7c875918636fe89211c83a5a571e258a06ef447a7fa4
---

折叠设备形态各异，在相机应用的开发过程中需要统一的摄像头切换方案，以确保用户在拍照、录像过程中获得更好的体验。

一台可折叠设备在不同折叠状态下，可使用不同的相机。系统会标识所有摄像头，每个摄像头与一个折叠状态相对应，表示该摄像头可在对应的折叠状态下使用。应用可调用[CameraManager.on('foldStatusChange')](../harmonyos-references/arkts-apis-camera-cameramanager.md#onfoldstatuschange12)或[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)监听设备的折叠状态变化，并调用[CameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)获取当前状态下可用相机，完成相应适配，确保应用在折叠状态变更时的用户体验。

不同折叠设备在不同折叠状态下支持的摄像头数量不同。

例如，折叠设备拥有三颗摄像头：后置摄像头A、前置摄像头B和前置摄像头C。在展开状态下，通过[CameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口可获取到后置摄像头A和前置摄像头B；在折叠状态下，可获取到后置摄像头A和前置摄像头C。不同的折叠状态获取到的镜头不同，因此，在折叠状态变化时，需要重新获取镜头信息。

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

在开发相机应用时，需要先申请相机相关权限，请参考[申请相关权限](camera-preparation.md)。

## 创建XComponent

使用两个[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)分别展示折叠态和展开态，防止切换折叠屏状态亮屏的时候上一个相机还未关闭，残留上一个相机的画面。

```
1. @Entry
2. @Component
3. struct Index {
4. @State reloadXComponentFlag: boolean = false;
5. @StorageLink('foldStatus') @Watch('reloadXComponent') foldStatus: number = 0;
6. private mXComponentController: XComponentController = new XComponentController();
7. private mXComponentOptions: XComponentOptions = {
8. type: XComponentType.SURFACE,
9. controller: this.mXComponentController
10. }

12. reloadXComponent() {
13. this.reloadXComponentFlag = !this.reloadXComponentFlag;
14. }

16. async loadXComponent() {
17. // 初始化XComponent。
18. }

20. build() {
21. Stack() {
22. if (this.reloadXComponentFlag) {
23. XComponent(this.mXComponentOptions)
24. .onLoad(async () => {
25. await this.loadXComponent();
26. })
27. .width(this.getUIContext().px2vp(1080))
28. .height(this.getUIContext().px2vp(1920))
29. } else {
30. XComponent(this.mXComponentOptions)
31. .onLoad(async () => {
32. await this.loadXComponent();
33. })
34. .width(this.getUIContext().px2vp(1080))
35. .height(this.getUIContext().px2vp(1920))
36. }
37. }
38. .size({ width: '100%', height: '100%' })
39. .backgroundColor(Color.Black)
40. }
41. }
```

## 获取设备折叠状态

此处提供两种方案供开发者选择。

* **方案一：使用相机框架提供的[CameraManager.on('foldStatusChange')](../harmonyos-references/arkts-apis-camera-cameramanager.md#onfoldstatuschange12)监听设备折叠态变化。**

  ```
  1. import { camera } from '@kit.CameraKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. function registerFoldStatusChanged(err: BusinessError, foldStatusInfo: camera.FoldStatusInfo) {
  5. // foldStatus 变量用来控制显示XComponent组件。
  6. AppStorage.setOrCreate<number>('foldStatus', foldStatusInfo.foldStatus);
  7. }

  9. function onFoldStatusChange(cameraManager: camera.CameraManager) {
  10. cameraManager.on('foldStatusChange', registerFoldStatusChanged);
  11. }

  13. function offFoldStatusChange(cameraManager: camera.CameraManager) {
  14. cameraManager.off('foldStatusChange', registerFoldStatusChanged);
  15. }
  ```
* **方案二：使用图形图像的[display.on('foldStatusChange')](../harmonyos-references/js-apis-display.md#displayonfoldstatuschange10)监听设备折叠态变化。**

  ```
  1. import { display } from '@kit.ArkUI';

  3. function getFoldStatus(): display.FoldStatus {
  4. let curFoldStatus: display.FoldStatus = display.FoldStatus.FOLD_STATUS_UNKNOWN;
  5. try {
  6. curFoldStatus = display.getFoldStatus();
  7. } catch (error) {
  8. console.error('getFoldStatus call failed');
  9. }
  10. return curFoldStatus;
  11. }

  13. let preFoldStatus: display.FoldStatus = getFoldStatus();
  14. display.on('foldStatusChange', (foldStatus: display.FoldStatus) => {
  15. // 从半折叠态（FOLD_STATUS_HALF_FOLDED）到展开态（FOLD_STATUS_EXPANDED），相机框架返回所支持的相机是一致的，所以从半折叠态到展开态不需要重新配流，从展开态到半折叠态也是一样的。
  16. if ((preFoldStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED &&
  17. foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED) ||
  18. (preFoldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED &&
  19. foldStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED)) {
  20. preFoldStatus = foldStatus;
  21. return;
  22. }
  23. preFoldStatus = foldStatus;
  24. // foldStatus 变量用来控制显示XComponent组件。
  25. AppStorage.setOrCreate<number>('foldStatus', foldStatus);
  26. })
  ```

## 判断是否存在对应位置摄像头

通过[CameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口可获取到当前设备折叠状态下支持的所有镜头，遍历获取到的结果，通过[CameraPosition](../harmonyos-references/arkts-apis-camera-e.md#cameraposition)判断镜头是否存在。

```
1. import { camera } from '@kit.CameraKit';

3. // connectionType默认为camera.ConnectionType.CAMERA_CONNECTION_BUILT_IN，表示设备的内置镜头。
4. function hasCameraAt(cameraManager: camera.CameraManager, cameraPosition: camera.CameraPosition,
5. connectionType: camera.ConnectionType = camera.ConnectionType.CAMERA_CONNECTION_BUILT_IN): boolean {
6. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
7. if (cameraArray.length <= 0) {
8. console.error('cameraManager.getSupportedCameras error');
9. return false;
10. }
11. for (let index = 0; index < cameraArray.length; index++) {
12. if (cameraArray[index].cameraPosition === cameraPosition &&
13. cameraArray[index].connectionType === connectionType) {
14. return true;
15. }
16. }
17. return false;
18. }
```

## 摄像头切换逻辑

在监听到折叠状态发生变化时通过设置被[@StorageLink](arkts-appstorage.md#storagelink)修饰的foldStatus变量改变，触发reloadXComponent方法重新加载XComponent组件，从而实现相机的切换逻辑。

## 完整示例

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { abilityAccessCtrl } from '@kit.AbilityKit';
4. import { display } from '@kit.ArkUI';

6. const TAG = 'FoldScreenCameraAdaptationDemo ';

8. @Entry
9. @Component
10. struct Index {
11. @State isShow: boolean = false;
12. @State reloadXComponentFlag: boolean = false;
13. @StorageLink('foldStatus') @Watch('reloadXComponent') foldStatus: number = 0;
14. private mXComponentController: XComponentController = new XComponentController();
15. private mXComponentOptions: XComponentOptions = {
16. type: XComponentType.SURFACE,
17. controller: this.mXComponentController
18. }
19. private mSurfaceId: string = '';
20. private mCameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK;
21. private mCameraManager: camera.CameraManager | undefined = undefined;
22. // surface宽高根据需要自行选择。
23. private surfaceRect: SurfaceRect = {
24. surfaceWidth: 1080,
25. surfaceHeight: 1920
26. };
27. private curCameraDevice: camera.CameraDevice | undefined = undefined;
28. private mCameraInput: camera.CameraInput | undefined = undefined;
29. private mPreviewOutput: camera.PreviewOutput | undefined = undefined;
30. private mPhotoSession: camera.PhotoSession | undefined = undefined;
31. // 请根据实际业务诉求选择符合需求场景的预览流Profile，此处以分辨率1080P，CameraFormat：1003为例。
32. private previewProfileObj: camera.Profile = {
33. format: 1003,
34. size: {
35. width: 1920,
36. height: 1080
37. }
38. };
39. private mContext: Context | undefined = undefined;

41. private preFoldStatus: display.FoldStatus = this.getFoldStatus();
42. // 监听折叠屏状态，可以使用cameraManager.on(type: 'foldStatusChange', callback: AsyncCallback<FoldStatusInfo>): void;
43. // 也可以使用display.on(type: 'foldStatusChange', callback: Callback<FoldStatus>): void;
44. private foldStatusCallback =
45. (err: BusinessError, info: camera.FoldStatusInfo): void => this.registerFoldStatusChanged(err, info);
46. private displayFoldStatusCallback =
47. (foldStatus: display.FoldStatus): void => this.onDisplayFoldStatusChange(foldStatus);

49. getFoldStatus(): display.FoldStatus {
50. let curFoldStatus: display.FoldStatus = display.FoldStatus.FOLD_STATUS_UNKNOWN;
51. try {
52. curFoldStatus = display.getFoldStatus();
53. } catch (error) {
54. console.info(`${TAG} getFoldStatus call failed, error: ${error.code}`);
55. }
56. return curFoldStatus;
57. }

59. registerFoldStatusChanged(err: BusinessError, foldStatusInfo: camera.FoldStatusInfo) {
60. if (err !== undefined && err.code !== 0) {
61. console.info(`${TAG} registerFoldStatusChanged call failed, error: ${err.code}`);
62. return;
63. }
64. console.info(TAG + 'foldStatusChanged foldStatus: ' + foldStatusInfo.foldStatus);
65. for (let i = 0; i < foldStatusInfo.supportedCameras.length; i++) {
66. console.info(TAG +
67. `foldStatusChanged camera[${i}]: ${foldStatusInfo.supportedCameras[i].cameraId},cameraPosition: ${foldStatusInfo.supportedCameras[i].cameraPosition}`);
68. }
69. AppStorage.setOrCreate<number>('foldStatus', foldStatusInfo.foldStatus);
70. }

72. onDisplayFoldStatusChange(foldStatus: display.FoldStatus): void {
73. console.info(TAG + `onDisplayFoldStatusChange foldStatus: ${foldStatus}`);
74. if ((this.preFoldStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED &&
75. foldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED) ||
76. (this.preFoldStatus === display.FoldStatus.FOLD_STATUS_EXPANDED &&
77. foldStatus === display.FoldStatus.FOLD_STATUS_HALF_FOLDED)) {
78. this.preFoldStatus = foldStatus;
79. return;
80. }
81. this.preFoldStatus = foldStatus;
82. if (!this.curCameraDevice) {
83. return;
84. }
85. // foldStatus 变量用来控制显示XComponent组件。
86. AppStorage.setOrCreate<number>('foldStatus', foldStatus);
87. }

89. requestPermissionsFn(): void {
90. let atManager = abilityAccessCtrl.createAtManager();
91. atManager.requestPermissionsFromUser(this.mContext, [
92. 'ohos.permission.CAMERA'
93. ]).then((): void => {
94. this.isShow = true;
95. }).catch((error: BusinessError): void => {
96. console.error(`${TAG} requestPermissionsFromUser call failed, error: ${error.code}`);
97. });
98. }

100. initContext(): void {
101. let uiContext = this.getUIContext();
102. this.mContext = uiContext.getHostContext();
103. }

105. initCameraManager(): void {
106. try {
107. this.mCameraManager = camera.getCameraManager(this.mContext);
108. } catch (error) {
109. console.error(`${TAG} getCameraManager call failed, error: ${error.code}`);
110. }
111. }

113. aboutToAppear(): void {
114. console.info(TAG + 'aboutToAppear is called');
115. this.initContext();
116. this.initCameraManager();
117. this.requestPermissionsFn();
118. this.onFoldStatusChange();
119. }

121. async aboutToDisappear(): Promise<void> {
122. await this.releaseCamera();
123. // 解注册。
124. this.offFoldStatusChange();
125. }

127. async onPageShow(): Promise<void> {
128. await this.initCamera(this.mSurfaceId, this.mCameraPosition);
129. }

131. async releaseCamera(): Promise<void> {
132. // 停止当前会话。
133. try {
134. await this.mPhotoSession?.stop();
135. } catch (error) {
136. let err = error as BusinessError;
137. console.error(TAG + 'Failed to stop session, errorCode = ' + err.code);
138. }

140. // 释放相机输入流。
141. try {
142. await this.mCameraInput?.close();
143. } catch (error) {
144. let err = error as BusinessError;
145. console.error(TAG + 'Failed to close device, errorCode = ' + err.code);
146. }

148. // 释放预览输出流。
149. try {
150. await this.mPreviewOutput?.release();
151. } catch (error) {
152. let err = error as BusinessError;
153. console.error(TAG + 'Failed to release previewOutput, errorCode = ' + err.code);
154. }

156. this.mPreviewOutput = undefined;

158. // 释放会话。
159. try {
160. await this.mPhotoSession?.release();
161. } catch (error) {
162. let err = error as BusinessError;
163. console.error(TAG + 'Failed to release photoSession, errorCode = ' + err.code);
164. }

166. // 会话置空。
167. this.mPhotoSession = undefined;
168. }

170. onFoldStatusChange(): void {
171. this.mCameraManager?.on('foldStatusChange', this.foldStatusCallback);
172. // display.on('foldStatusChange', this.displayFoldStatusCallback);
173. }

175. offFoldStatusChange(): void {
176. this.mCameraManager?.off('foldStatusChange', this.foldStatusCallback);
177. // display.off('foldStatusChange', this.displayFoldStatusCallback);
178. }

180. reloadXComponent(): void {
181. this.reloadXComponentFlag = !this.reloadXComponentFlag;
182. }

184. async loadXComponent(): Promise<void> {
185. if (!this.mXComponentController) {
186. console.error(TAG + 'mXComponentController is null');
187. return;
188. }
189. this.mSurfaceId = this.mXComponentController.getXComponentSurfaceId();
190. this.mXComponentController.setXComponentSurfaceRect(this.surfaceRect);
191. console.info(TAG + `mCameraPosition: ${this.mCameraPosition}`)
192. await this.initCamera(this.mSurfaceId, this.mCameraPosition);
193. }

195. getPreviewProfile(cameraOutputCapability: camera.CameraOutputCapability): camera.Profile | undefined {
196. let previewProfiles = cameraOutputCapability.previewProfiles;
197. if (previewProfiles.length < 1) {
198. return undefined;
199. }
200. let index = previewProfiles.findIndex((previewProfile: camera.Profile) => {
201. return previewProfile.size.width === this.previewProfileObj.size.width &&
202. previewProfile.size.height === this.previewProfileObj.size.height &&
203. previewProfile.format === this.previewProfileObj.format;
204. })
205. if (index === -1) {
206. return undefined;
207. }
208. return previewProfiles[index];
209. }

211. async initCamera(surfaceId: string, cameraPosition: camera.CameraPosition,
212. connectionType: camera.ConnectionType = camera.ConnectionType.CAMERA_CONNECTION_BUILT_IN): Promise<void> {
213. await this.releaseCamera();
214. // 创建CameraManager对象。
215. if (!this.mCameraManager) {
216. console.error(TAG + 'camera.getCameraManager error');
217. return;
218. }

220. // 获取相机列表。
221. let cameraArray: Array<camera.CameraDevice> = this.mCameraManager.getSupportedCameras();
222. if (!cameraArray || cameraArray.length == 0) {
223. console.error(TAG + 'cameraManager.getSupportedCameras error');
224. return;
225. }

227. for (let index = 0; index < cameraArray.length; index++) {
228. console.info(TAG + 'cameraId : ' + cameraArray[index].cameraId); // 获取相机ID。
229. console.info(TAG + 'cameraPosition : ' + cameraArray[index].cameraPosition); // 获取相机位置。
230. console.info(TAG + 'cameraType : ' + cameraArray[index].cameraType); // 获取相机类型。
231. console.info(TAG + 'connectionType : ' + cameraArray[index].connectionType); // 获取相机连接类型。
232. }

234. let deviceIndex = cameraArray.findIndex((cameraDevice: camera.CameraDevice) => {
235. return cameraDevice.cameraPosition === cameraPosition && cameraDevice.connectionType === connectionType;
236. })
237. // 没有找到对应位置的摄像头，可选择其他摄像头，具体场景具体对待。
238. if (deviceIndex === -1) {
239. deviceIndex = 0;
240. console.error(TAG + 'not found camera');
241. }
242. this.curCameraDevice = cameraArray[deviceIndex];

244. // 创建相机输入流。
245. try {
246. this.mCameraInput = this.mCameraManager.createCameraInput(this.curCameraDevice);
247. } catch (error) {
248. let err = error as BusinessError;
249. console.error(TAG + 'Failed to createCameraInput errorCode = ' + err.code);
250. }
251. if (this.mCameraInput === undefined) {
252. return;
253. }

255. // 打开相机。
256. try {
257. await this.mCameraInput.open();
258. } catch (error) {
259. let err = error as BusinessError;
260. console.error(TAG + 'Failed to open device, errorCode = ' + err.code);
261. }

263. // 获取支持的模式类型。
264. let sceneModes: Array<camera.SceneMode> = this.mCameraManager.getSupportedSceneModes(this.curCameraDevice);
265. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
266. if (!isSupportPhotoMode) {
267. console.error(TAG + 'photo mode not support');
268. await this.releaseCamera();
269. return;
270. }

272. // 获取相机设备支持的输出流能力。
273. let cameraOutputCapability: camera.CameraOutputCapability =
274. this.mCameraManager.getSupportedOutputCapability(this.curCameraDevice, camera.SceneMode.NORMAL_PHOTO);
275. if (!cameraOutputCapability) {
276. console.error(TAG + 'cameraManager.getSupportedOutputCapability error');
277. return;
278. }
279. console.info(TAG + 'outputCapability: ' + JSON.stringify(cameraOutputCapability));
280. let previewProfile = this.getPreviewProfile(cameraOutputCapability);
281. if (!previewProfile) {
282. console.error(TAG + 'The resolution of the current preview stream is not supported.');
283. await this.releaseCamera();
284. return;
285. }
286. this.previewProfileObj = previewProfile;

288. // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface。
289. try {
290. this.mPreviewOutput = this.mCameraManager.createPreviewOutput(this.previewProfileObj, surfaceId);
291. } catch (error) {
292. let err = error as BusinessError;
293. console.error(TAG + `Failed to create the PreviewOutput instance. error code: ${err.code}`);
294. }
295. if (!this.mPreviewOutput) {
296. await this.releaseCamera();
297. return;
298. }

300. // 创建会话。
301. try {
302. let session = this.mCameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
303. if (!session) {
304. await this.releaseCamera();
305. return;
306. }
307. this.mPhotoSession = session as camera.PhotoSession;
308. } catch (error) {
309. let err = error as BusinessError;
310. console.error(TAG + 'Failed to create the session instance. errorCode = ' + err.code);
311. }

313. if (!this.mPhotoSession) {
314. await this.releaseCamera();
315. return;
316. }

318. // 开始配置会话。
319. try {
320. this.mPhotoSession.beginConfig();
321. } catch (error) {
322. let err = error as BusinessError;
323. console.error(TAG + 'Failed to beginConfig. errorCode = ' + err.code);
324. }

326. // 向会话中添加相机输入流。
327. try {
328. this.mPhotoSession.addInput(this.mCameraInput);
329. } catch (error) {
330. let err = error as BusinessError;
331. console.error(TAG + 'Failed to addInput. errorCode = ' + err.code);
332. }

334. // 向会话中添加预览输出流。
335. try {
336. this.mPhotoSession.addOutput(this.mPreviewOutput);
337. } catch (error) {
338. let err = error as BusinessError;
339. console.error(TAG + 'Failed to addOutput(previewOutput). errorCode = ' + err.code);
340. }

342. // 提交会话配置。
343. try {
344. await this.mPhotoSession.commitConfig();
345. } catch (error) {
346. let err = error as BusinessError;
347. console.error(TAG + 'Failed to commit session configuration, errorCode = ' + err.code);
348. }

350. // 启动会话。
351. try {
352. await this.mPhotoSession.start()
353. } catch (error) {
354. let err = error as BusinessError;
355. console.error(TAG + 'Failed to start session. errorCode = ' + err.code);
356. }
357. }

359. build() {
360. if (this.isShow) {
361. Stack() {
362. if (this.reloadXComponentFlag) {
363. XComponent(this.mXComponentOptions)
364. .onLoad(async () => {
365. await this.loadXComponent();
366. })
367. .width(this.getUIContext().px2vp(1080))
368. .height(this.getUIContext().px2vp(1920))
369. } else {
370. XComponent(this.mXComponentOptions)
371. .onLoad(async () => {
372. await this.loadXComponent();
373. })
374. .width(this.getUIContext().px2vp(1080))
375. .height(this.getUIContext().px2vp(1920))
376. }
377. Text('切换相机')
378. .size({ width: 80, height: 48 })
379. .position({ x: 1, y: 1 })
380. .backgroundColor(Color.White)
381. .textAlign(TextAlign.Center)
382. .borderRadius(24)
383. .onClick(async () => {
384. this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
385. camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
386. this.reloadXComponentFlag = !this.reloadXComponentFlag;
387. })
388. }
389. .size({ width: '100%', height: '100%' })
390. .backgroundColor(Color.Black)
391. }
392. }
393. }
```
