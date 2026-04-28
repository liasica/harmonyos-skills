---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-auto-switch
title: 自动切换摄像头实践(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 自动切换摄像头实践(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:00+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:fef12c57a70cdb5790c6a470cafd7f38b5779bdcd0ee87cc6ba779a1a5a7b911
---

应用适配折叠屏时，在简单UX交互场景下，如人脸识别场景推荐使用相机镜头自动切换能力。在有多个前置镜头的折叠设备上，应用使能自动切换镜头能力后，系统能够自动完成镜头切换、会话配置，在不同的折叠状态下，可自动切换到当前可使用的前置镜头，避免前置镜头被折入内部导致黑屏。

例如，折叠设备拥有三颗摄像头：后置摄像头A、前置摄像头B和前置摄像头C。在展开状态下，通过[CameraManager.getSupportedCameras](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedcameras)接口可获取到后置摄像头A和前置摄像头B；在折叠状态下，可获取到后置摄像头A和前置摄像头C。在当前折叠状态下启用前置摄像头，并调用[enableAutoDeviceSwitch](../harmonyos-references/arkts-apis-camera-autodeviceswitch.md#enableautodeviceswitch13)开启自动切换镜头；这样，在下次折叠屏状态变化时，会自动切换到对应折叠状态下的前置摄像头。

注意

自动切换镜头功能由系统自动完成输入设备切换，会话配置和参数接续。当系统发现镜头切换时，两颗镜头的变焦范围不一致，则会通过AutoDeviceSwitchStatus中的isDeviceCapabilityChanged字段告知应用，此时需要应用自己处理UX的变更（如变焦范围的调整，需要重新通过getZoomRatioRange接口获取数据并更新UX）。因此如相机拍照或录像等复杂场景的镜头选择，请参阅[适配不同折叠状态的摄像头变更](camera-foldable-display.md)。

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

## 导入相关依赖

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { abilityAccessCtrl } from '@kit.AbilityKit';
```

## 创建XComponent

使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)展示摄像头的预览画面。

```
1. @Entry
2. @Component
3. struct Index {
4. private mXComponentController: XComponentController = new XComponentController();
5. private mCameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK;
6. private mXComponentOptions: XComponentOptions = {
7. type: XComponentType.SURFACE,
8. controller: this.mXComponentController
9. }

11. async loadXComponent() {
12. // 初始化XComponent。
13. }

15. build() {
16. Stack() {
17. XComponent(this.mXComponentOptions)
18. .onLoad(async () => {
19. await this.loadXComponent();
20. })
21. .width(this.getUIContext().px2vp(1080))
22. .height(this.getUIContext().px2vp(1920))
23. Text('切换相机')
24. .size({ width: 80, height: 48 })
25. .position({ x: 1, y: 1 })
26. .backgroundColor(Color.White)
27. .textAlign(TextAlign.Center)
28. .borderRadius(24)
29. .onClick(async () => {
30. this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
31. camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
32. await this.loadXComponent();
33. })
34. }
35. .size({ width: '100%', height: '100%' })
36. .backgroundColor(Color.Black)
37. }
38. }
```

## 开启自动切换摄像头

调用[enableAutoDeviceSwitch](../harmonyos-references/arkts-apis-camera-autodeviceswitch.md#enableautodeviceswitch13)接口前需要通过[isAutoDeviceSwitchSupported](../harmonyos-references/arkts-apis-camera-autodeviceswitchquery.md#isautodeviceswitchsupported13)接口查询当前设备是否支持自动切换摄像头能力。

```
1. function enableAutoDeviceSwitch(session: camera.PhotoSession) {
2. if (session.isAutoDeviceSwitchSupported()) {
3. try {
4. session.enableAutoDeviceSwitch(true);
5. } catch (error) {
6. let err = error as BusinessError;
7. console.error(`The enableAutoDeviceSwitch call failed, error code: ${err.code}, error message: ${err.message}`);
8. }
9. }
10. }
```

## 监听或解监听自动切换摄像头状态

可以通过[on('autoDeviceSwitchStatusChange')](../harmonyos-references/arkts-apis-camera-photosession.md#onautodeviceswitchstatuschange13)监听自动切换摄像头的结果。系统自动切换镜头结束后会触发该回调。

自动切换摄像头期间，禁止调用任何[session](../harmonyos-references/arkts-apis-camera-session.md)相关接口。

```
1. function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
2. if (err !== undefined && err.code !== 0) {
3. console.error(`Callback Error, errorCode: ${err.code}`);
4. return;
5. }
6. console.info(`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}`);
7. }

9. function registerAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
10. photoSession.on('autoDeviceSwitchStatusChange', callback);
11. }
12. function unregisterAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
13. photoSession.off('autoDeviceSwitchStatusChange', callback);
14. }
```

## 完整示例代码

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { abilityAccessCtrl } from '@kit.AbilityKit';

5. const TAG = 'AutoSwitchCameraDemo ';

7. @Entry
8. @Component
9. struct Index {
10. @State isShow: boolean = false;
11. @State reloadXComponentFlag: boolean = false;
12. private mXComponentController: XComponentController = new XComponentController();
13. private mXComponentOptions: XComponentOptions = {
14. type: XComponentType.SURFACE,
15. controller: this.mXComponentController
16. }
17. private mSurfaceId: string = '';
18. private mCameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA_POSITION_BACK;
19. private mCameraManager: camera.CameraManager | undefined = undefined;
20. private curCameraDevice: camera.CameraDevice | undefined = undefined;
21. private mCameraInput: camera.CameraInput | undefined = undefined;
22. private mPreviewOutput: camera.PreviewOutput | undefined = undefined;
23. private mPhotoSession: camera.PhotoSession | undefined = undefined;
24. // One of the recommended preview resolutions.
25. private previewProfileObj: camera.Profile = {
26. format: 1003,
27. size: {
28. width: 1920,
29. height: 1080
30. }
31. };
32. private mContext: Context | undefined = undefined;
33. autoDeviceSwitchCallback: (err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus) => void =
34. (err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus) => {
35. if (err !== undefined && err.code !== 0) {
36. console.error(`${TAG} Callback Error, errorCode: ${err.code}`);
37. return;
38. }
39. console.info(`${TAG} isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}`);
40. }

42. requestPermissionsFn(): void {
43. let atManager = abilityAccessCtrl.createAtManager();
44. atManager.requestPermissionsFromUser(this.mContext, [
45. 'ohos.permission.CAMERA'
46. ]).then((): void => {
47. this.isShow = true;
48. }).catch((error: BusinessError): void => {
49. console.error(TAG + `ohos.permission.CAMERA no permission, error: ${error.code}`);
50. });
51. }

53. initContext(): void {
54. let uiContext = this.getUIContext();
55. this.mContext = uiContext.getHostContext();
56. }

58. initCameraManager(): void {
59. try {
60. this.mCameraManager = camera.getCameraManager(this.mContext);
61. } catch (error) {
62. let err = error as BusinessError;
63. console.error(`getCameraManager failed, error: ${err.code}`);
64. }
65. }

67. aboutToAppear(): void {
68. console.info(TAG + 'aboutToAppear is called');
69. this.initContext();
70. this.requestPermissionsFn();
71. this.initCameraManager();
72. }

74. async aboutToDisappear(): Promise<void> {
75. await this.releaseCamera();
76. }

78. async onPageShow(): Promise<void> {
79. await this.initCamera(this.mSurfaceId, this.mCameraPosition);
80. }

82. async releaseCamera(): Promise<void> {
83. // 停止当前会话。
84. try {
85. await this.mPhotoSession?.stop();
86. } catch (error) {
87. let err = error as BusinessError;
88. console.error(TAG + 'Failed to stop session, errorCode = ' + err.code);
89. }

91. // 释放相机输入流。
92. try {
93. await this.mCameraInput?.close();
94. } catch (error) {
95. let err = error as BusinessError;
96. console.error(TAG + 'Failed to close device, errorCode = ' + err.code);
97. }

99. // 释放预览输出流。
100. try {
101. await this.mPreviewOutput?.release();
102. } catch (error) {
103. let err = error as BusinessError;
104. console.error(TAG + 'Failed to release previewOutput, errorCode = ' + err.code);
105. }

107. this.mPreviewOutput = undefined;

109. // 释放会话。
110. try {
111. await this.mPhotoSession?.release();
112. } catch (error) {
113. let err = error as BusinessError;
114. console.error(TAG + 'Failed to release photoSession, errorCode = ' + err.code);
115. }

117. // 会话置空。
118. this.mPhotoSession = undefined;
119. }

121. async loadXComponent(): Promise<void> {
122. this.mSurfaceId = this.mXComponentController.getXComponentSurfaceId();
123. console.info(TAG + `mCameraPosition: ${this.mCameraPosition}`)
124. await this.initCamera(this.mSurfaceId, this.mCameraPosition);
125. }

127. getPreviewProfile(cameraOutputCapability: camera.CameraOutputCapability): camera.Profile | undefined {
128. let previewProfiles = cameraOutputCapability.previewProfiles;
129. if (previewProfiles.length < 1) {
130. return undefined;
131. }
132. let index = previewProfiles.findIndex((previewProfile: camera.Profile) => {
133. return previewProfile.size.width === this.previewProfileObj.size.width &&
134. previewProfile.size.height === this.previewProfileObj.size.height &&
135. previewProfile.format === this.previewProfileObj.format;
136. })
137. if (index === -1) {
138. return undefined;
139. }
140. return previewProfiles[index];
141. }

143. async initCamera(surfaceId: string, cameraPosition: camera.CameraPosition,
144. connectionType: camera.ConnectionType = camera.ConnectionType.CAMERA_CONNECTION_BUILT_IN): Promise<void> {
145. await this.releaseCamera();
146. // 创建CameraManager对象。
147. if (!this.mCameraManager) {
148. console.error(TAG + 'camera.getCameraManager error');
149. return;
150. }

152. // 获取相机列表。
153. let cameraArray: Array<camera.CameraDevice> = this.mCameraManager.getSupportedCameras();
154. if (cameraArray.length <= 0) {
155. console.error(TAG + 'cameraManager.getSupportedCameras error');
156. return;
157. }

159. for (let index = 0; index < cameraArray.length; index++) {
160. console.info(TAG + 'cameraId : ' + cameraArray[index].cameraId); // 获取相机ID。
161. console.info(TAG + 'cameraPosition : ' + cameraArray[index].cameraPosition); // 获取相机位置。
162. console.info(TAG + 'cameraType : ' + cameraArray[index].cameraType); // 获取相机类型。
163. console.info(TAG + 'connectionType : ' + cameraArray[index].connectionType); // 获取相机连接类型。
164. }

166. let deviceIndex = cameraArray.findIndex((cameraDevice: camera.CameraDevice) => {
167. return cameraDevice.cameraPosition === cameraPosition && cameraDevice.connectionType === connectionType;
168. })
169. // 没有找到对应位置的摄像头，可选择其他摄像头，具体场景具体对待。
170. if (deviceIndex === -1) {
171. deviceIndex = 0;
172. console.error(TAG + 'not found camera');
173. }
174. this.curCameraDevice = cameraArray[deviceIndex];

176. // 创建相机输入流。
177. try {
178. this.mCameraInput = this.mCameraManager.createCameraInput(this.curCameraDevice);
179. } catch (error) {
180. let err = error as BusinessError;
181. console.error(TAG + 'Failed to createCameraInput errorCode = ' + err.code);
182. }
183. if (this.mCameraInput === undefined) {
184. return;
185. }

187. // 打开相机。
188. try {
189. await this.mCameraInput.open();
190. } catch (error) {
191. let err = error as BusinessError;
192. console.error(TAG + 'Failed to open device, errorCode = ' + err.code);
193. }

195. // 获取支持的模式类型。
196. let sceneModes: Array<camera.SceneMode> = this.mCameraManager.getSupportedSceneModes(this.curCameraDevice);
197. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
198. if (!isSupportPhotoMode) {
199. console.error(TAG + 'photo mode not support');
200. return;
201. }

203. // 获取相机设备支持的输出流能力。
204. let cameraOutputCapability: camera.CameraOutputCapability =
205. this.mCameraManager.getSupportedOutputCapability(this.curCameraDevice, camera.SceneMode.NORMAL_PHOTO);
206. if (!cameraOutputCapability) {
207. console.error(TAG + 'cameraManager.getSupportedOutputCapability error');
208. return;
209. }
210. console.info(TAG + 'outputCapability: ' + JSON.stringify(cameraOutputCapability));
211. let previewProfile = this.getPreviewProfile(cameraOutputCapability);
212. if (previewProfile === undefined) {
213. console.error(TAG + 'The resolution of the current preview stream is not supported.');
214. return;
215. }
216. this.previewProfileObj = previewProfile;

218. // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface。
219. try {
220. this.mPreviewOutput = this.mCameraManager.createPreviewOutput(this.previewProfileObj, surfaceId);
221. } catch (error) {
222. let err = error as BusinessError;
223. console.error(TAG + `Failed to create the PreviewOutput instance. error code: ${err.code}`);
224. }
225. if (this.mPreviewOutput === undefined) {
226. return;
227. }

229. // 创建会话。
230. try {
231. this.mPhotoSession = this.mCameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
232. } catch (error) {
233. let err = error as BusinessError;
234. console.error(TAG + 'Failed to create the session instance. errorCode = ' + err.code);
235. }
236. if (this.mPhotoSession === undefined) {
237. return;
238. }
239. if (this.mPhotoSession.isAutoDeviceSwitchSupported()) {
240. this.mPhotoSession.enableAutoDeviceSwitch(true);
241. this.mPhotoSession.on('autoDeviceSwitchStatusChange', this.autoDeviceSwitchCallback);
242. }
243. // 开始配置会话。
244. try {
245. this.mPhotoSession.beginConfig();
246. } catch (error) {
247. let err = error as BusinessError;
248. console.error(TAG + 'Failed to beginConfig. errorCode = ' + err.code);
249. }

251. // 向会话中添加相机输入流。
252. try {
253. this.mPhotoSession.addInput(this.mCameraInput);
254. } catch (error) {
255. let err = error as BusinessError;
256. console.error(TAG + 'Failed to addInput. errorCode = ' + err.code);
257. }

259. // 向会话中添加预览输出流。
260. try {
261. this.mPhotoSession.addOutput(this.mPreviewOutput);
262. } catch (error) {
263. let err = error as BusinessError;
264. console.error(TAG + 'Failed to addOutput(previewOutput). errorCode = ' + err.code);
265. }

267. // 提交会话配置。
268. try {
269. await this.mPhotoSession.commitConfig();
270. } catch (error) {
271. let err = error as BusinessError;
272. console.error(TAG + 'Failed to commit session configuration, errorCode = ' + err.code);
273. }

275. // 启动会话。
276. try {
277. await this.mPhotoSession.start()
278. } catch (error) {
279. let err = error as BusinessError;
280. console.error(TAG + 'Failed to start session. errorCode = ' + err.code);
281. }
282. }

284. build() {
285. if (this.isShow) {
286. Stack() {
287. XComponent(this.mXComponentOptions)
288. .onLoad(async () => {
289. await this.loadXComponent();
290. })
291. .width(this.getUIContext().px2vp(1080))
292. .height(this.getUIContext().px2vp(1920))
293. Text('切换相机')
294. .size({ width: 80, height: 48 })
295. .position({ x: 1, y: 1 })
296. .backgroundColor(Color.White)
297. .textAlign(TextAlign.Center)
298. .borderRadius(24)
299. .onClick(async () => {
300. this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA_POSITION_BACK ?
301. camera.CameraPosition.CAMERA_POSITION_FRONT : camera.CameraPosition.CAMERA_POSITION_BACK;
302. await this.loadXComponent();
303. })
304. }
305. .size({ width: '100%', height: '100%' })
306. .backgroundColor(Color.Black)
307. }
308. }
309. }
```
