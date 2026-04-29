---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-background-recovery
title: 相机启动恢复实践(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 相机启动恢复实践(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:bce958a5f99d4d2dc7539a91d3ecae75ec5c07d8a09e4c790d00a9b25baac56d
---

当前示例提供完整的相机应用从后台切换至前台启动恢复的流程介绍，方便开发者了解完整的接口调用顺序。

相机应用在前后台切换过程中的状态变化说明：

* 当相机应用在退后台之后由于安全策略会被强制断流，并且此时相机状态回调会返回相机可用状态，表示当前相机设备已经被关闭，处于空闲状态。
* 当相机应用从后台切换至前台时，相机状态回调会返回相机不可用状态，表示当前相机设备被打开，处于忙碌状态。
* 相机应用从后台切换至前台时，需要重启相机设备的预览流、拍照流以及相机会话管理。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[相机管理](camera-device-management.md)、[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)等单个操作。

## 开发流程

相机应用从后台切换至前台启动恢复的调用流程建议如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oe_Mek7HQmCORfTX-Q6leA/zh-cn_image_0000002558765070.png?HW-CC-KV=V1&HW-CC-Date=20260429T053457Z&HW-CC-Expire=86400&HW-CC-Sign=3166552D1CD6539E0848BDABD50B015A5718D107BD9DD129063B50DDC013EFDD)

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

相机应用从后台切换至前台启动恢复需要在页面生命周期回调函数onPageShow中调用，重新初始化相机设备。

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { common } from '@kit.AbilityKit';

5. let context: common.BaseContext;
6. let surfaceId: string = '';
7. async function onPageShow(): Promise<void> {
8. // 当应用从后台切换至前台页面显示时，重新初始化相机设备。
9. await initCamera(context, surfaceId);
10. }

12. async function initCamera(baseContext: common.BaseContext, surfaceId: string): Promise<void> {
13. console.info('onForeGround recovery begin.');
14. let cameraManager: camera.CameraManager = camera.getCameraManager(baseContext);
15. if (!cameraManager) {
16. console.error("camera.getCameraManager error");
17. return;
18. }
19. // 监听相机状态变化。
20. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
21. if (err !== undefined && err.code !== 0) {
22. console.error('cameraStatus with errorCode = ' + err.code);
23. return;
24. }
25. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
26. console.info(`status: ${cameraStatusInfo.status}`);
27. });

29. // 获取相机列表。
30. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
31. if (cameraArray.length <= 0) {
32. console.error("cameraManager.getSupportedCameras error");
33. return;
34. }

36. for (let index = 0; index < cameraArray.length; index++) {
37. console.info('cameraId : ' + cameraArray[index].cameraId);                       // 获取相机ID。
38. console.info('cameraPosition : ' + cameraArray[index].cameraPosition);           // 获取相机位置。
39. console.info('cameraType : ' + cameraArray[index].cameraType);                   // 获取相机类型。
40. console.info('connectionType : ' + cameraArray[index].connectionType);           // 获取相机连接类型。
41. }

43. // 创建相机输入流。
44. let cameraInput: camera.CameraInput | undefined = undefined;
45. try {
46. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
47. } catch (error) {
48. let err = error as BusinessError;
49. console.error('Failed to createCameraInput errorCode = ' + err.code);
50. }
51. if (cameraInput === undefined) {
52. return;
53. }

55. // 监听cameraInput错误信息。
56. let cameraDevice: camera.CameraDevice = cameraArray[0];
57. cameraInput.on('error', cameraDevice, (error: BusinessError) => {
58. console.error(`Camera input error code: ${error.code}`);
59. });

61. // 打开相机。
62. await cameraInput.open();

64. // 获取支持的模式类型。
65. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
66. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
67. if (!isSupportPhotoMode) {
68. console.error('photo mode not support');
69. return;
70. }
71. // 获取相机设备支持的输出流能力。
72. let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
73. if (!cameraOutputCap) {
74. console.error("cameraManager.getSupportedOutputCapability error");
75. return;
76. }
77. console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

79. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
80. if (!previewProfilesArray) {
81. console.error("createOutput previewProfilesArray is null!");
82. return;
83. }

85. let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
86. if (!photoProfilesArray) {
87. console.error("createOutput photoProfilesArray is null!");
88. return;
89. }

91. // 创建预览输出流,其中参数surfaceId参考上文XComponent组件，预览流为XComponent组件提供的surface。
92. let previewOutput: camera.PreviewOutput | undefined = undefined;
93. try {
94. previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
95. } catch (error) {
96. let err = error as BusinessError;
97. console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
98. }
99. if (previewOutput === undefined) {
100. return;
101. }
102. // 监听预览输出错误信息。
103. previewOutput.on('error', (error: BusinessError) => {
104. console.error(`Preview output error code: ${error.code}`);
105. });

107. // 创建拍照输出流。
108. let photoOutput: camera.PhotoOutput | undefined = undefined;
109. try {
110. photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
111. } catch (error) {
112. let err = error as BusinessError;
113. console.error('Failed to createPhotoOutput errorCode = ' + err.code);
114. }
115. if (photoOutput === undefined) {
116. return;
117. }

119. // 创建会话。
120. let photoSession: camera.PhotoSession | undefined = undefined;
121. try {
122. photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
123. } catch (error) {
124. let err = error as BusinessError;
125. console.error('Failed to create the session instance. errorCode = ' + err.code);
126. }
127. if (photoSession === undefined) {
128. return;
129. }
130. // 监听session错误信息。
131. photoSession.on('error', (error: BusinessError) => {
132. console.error(`Capture session error code: ${error.code}`);
133. });

135. // 开始配置会话。
136. try {
137. photoSession.beginConfig();
138. } catch (error) {
139. let err = error as BusinessError;
140. console.error('Failed to beginConfig. errorCode = ' + err.code);
141. }

143. // 向会话中添加相机输入流。
144. try {
145. photoSession.addInput(cameraInput);
146. } catch (error) {
147. let err = error as BusinessError;
148. console.error('Failed to addInput. errorCode = ' + err.code);
149. }

151. // 向会话中添加预览输出流。
152. try {
153. photoSession.addOutput(previewOutput);
154. } catch (error) {
155. let err = error as BusinessError;
156. console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
157. }

159. // 向会话中添加拍照输出流。
160. try {
161. photoSession.addOutput(photoOutput);
162. } catch (error) {
163. let err = error as BusinessError;
164. console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
165. }

167. // 提交会话配置。
168. await photoSession.commitConfig();

170. // 启动会话。
171. await photoSession.start().then(() => {
172. console.info('Promise returned to indicate the session start success.');
173. });
174. // 判断设备是否支持闪光灯。
175. let flashStatus: boolean = false;
176. try {
177. flashStatus = photoSession.hasFlash();
178. } catch (error) {
179. let err = error as BusinessError;
180. console.error('Failed to hasFlash. errorCode = ' + err.code);
181. }
182. console.info('Returned with the flash light support status:' + flashStatus);

184. if (flashStatus) {
185. // 判断是否支持自动闪光灯模式。
186. let flashModeStatus: boolean = false;
187. try {
188. let status: boolean = photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
189. flashModeStatus = status;
190. } catch (error) {
191. let err = error as BusinessError;
192. console.error('Failed to check whether the flash mode is supported. errorCode = ' + err.code);
193. }
194. if(flashModeStatus) {
195. // 设置自动闪光灯模式。
196. try {
197. photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
198. } catch (error) {
199. let err = error as BusinessError;
200. console.error('Failed to set the flash mode. errorCode = ' + err.code);
201. }
202. }
203. }

205. // 判断是否支持连续自动变焦模式。
206. let focusModeStatus: boolean = false;
207. try {
208. let status: boolean = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
209. focusModeStatus = status;
210. } catch (error) {
211. let err = error as BusinessError;
212. console.error('Failed to check whether the focus mode is supported. errorCode = ' + err.code);
213. }

215. if (focusModeStatus) {
216. // 设置连续自动变焦模式。
217. try {
218. photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
219. } catch (error) {
220. let err = error as BusinessError;
221. console.error('Failed to set the focus mode. errorCode = ' + err.code);
222. }
223. }

225. // 获取相机支持的可变焦距比范围。
226. let zoomRatioRange: Array<number> = [];
227. try {
228. zoomRatioRange = photoSession.getZoomRatioRange();
229. } catch (error) {
230. let err = error as BusinessError;
231. console.error('Failed to get the zoom ratio range. errorCode = ' + err.code);
232. }
233. if (zoomRatioRange.length <= 0) {
234. return;
235. }
236. // 设置可变焦距比。
237. try {
238. photoSession.setZoomRatio(zoomRatioRange[0]);
239. } catch (error) {
240. let err = error as BusinessError;
241. console.error('Failed to set the zoom ratio value. errorCode = ' + err.code);
242. }
243. let photoCaptureSetting: camera.PhotoCaptureSetting = {
244. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高。
245. rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0。
246. }
247. // 使用当前拍照设置进行拍照。
248. photoOutput.capture(photoCaptureSetting, (err: BusinessError) => {
249. if (err) {
250. console.error(`Failed to capture the photo ${err.message}`);
251. return;
252. }
253. console.info('Callback invoked to indicate the photo capture request success.');
254. });

256. console.info('onForeGround recovery end.');
257. }
```
