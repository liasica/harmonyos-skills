---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preconfig
title: 使用相机预配置(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 使用相机预配置(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:01+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:f5f14e1e29373f27e778bcce4b31d1df9a7d3820a8d44a85b661d04ec5b22dab
---

相机预配置（Preconfig），对常用的场景和分辨率进行了预配置集成，可简化开发相机应用流程，提高应用的开发效率。

开发者在开发相机应用时，在获取到[CameraDevice](../harmonyos-references/arkts-apis-camera-i.md#cameradevice)之后，如果遵循通用流程开发，步骤较为繁琐。需要先调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)的[getSupportedOutputCapability](../harmonyos-references/arkts-apis-camera-cameramanager.md#getsupportedoutputcapability11)来查询当前相机在指定模式下所支持的各类输出的配置信息，拿到[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)之后，应用开发者还需要对里面的各类数据进行解析，筛选，找到自己需要的配置数据[Profile](../harmonyos-references/arkts-apis-camera-i.md#profile)以及[VideoProfile](../harmonyos-references/arkts-apis-camera-i.md#videoprofile)。最后使用对应的Profile以及VideoProfile创建对应的[PreviewOutput](../harmonyos-references/arkts-apis-camera-previewoutput.md)、[PhotoOutput](../harmonyos-references/arkts-apis-camera-photooutput.md)以及[VideoOutput](../harmonyos-references/arkts-apis-camera-videooutput.md)。

为了解决上述问题，优化应用开发流程，系统针对拍照（[PhotoSession](../harmonyos-references/arkts-apis-camera-photosession.md)）、录像（[VideoSession](../harmonyos-references/arkts-apis-camera-videosession.md)）两类场景，提供了[preconfig](../harmonyos-references/arkts-apis-camera-photosession.md#preconfig12)接口帮助开发者快速完成相机参数配置。推荐仅需要自定义拍照界面的无需开发专业相机应用的开发者，使用相机预配置功能快速开发应用。

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。以拍照（PhotoSession）为例，相机预配置（Preconfig）开发流程与[通用流程](camera-shooting-case.md)开发，存在以下差异：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/UPqFp2MfSNqIlG8m5CIiXA/zh-cn_image_0000002558765082.png?HW-CC-KV=V1&HW-CC-Date=20260429T053500Z&HW-CC-Expire=86400&HW-CC-Sign=B1A0509ECD9FF3B7D50520D9C1B730A40EABAD203EC377BA161760658389223E)

**其他相关能力：**

* [CameraPicker](camera-picker.md)：无需开发相机功能，拉起系统相机获取照片或视频。
* [调用全量相机接口开发](camera-overview.md)：可开发自定义界面、分辨率、图像效果的专业相机应用。

## 规格说明

系统提供了4种预配置类型（[PreconfigType](../harmonyos-references/arkts-apis-camera-e.md#preconfigtype12)），分别为PRECONFIG\_720P、PRECONFIG\_1080P、PRECONFIG\_4K、PRECONFIG\_HIGH\_QUALITY。以及3种画幅比例规格（[PreconfigRatio](../harmonyos-references/arkts-apis-camera-e.md#preconfigratio12)），1:1画幅（PRECONFIG\_RATIO\_1\_1）、4:3画幅（PRECONFIG\_RATIO\_4\_3）、16:9画幅（PRECONFIG\_RATIO\_16\_9）。

注意

由于不同的设备所支持的能力不同。使用相机预配置（Preconfig）功能时，需要先调用[canPreconfig](../harmonyos-references/arkts-apis-camera-photosession.md#canpreconfig12)检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。

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
  | PRECONFIG\_HIGH\_QUALITY | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
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
  | PRECONFIG\_720P | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
  | PRECONFIG\_1080P | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
  | PRECONFIG\_4K | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |
  | PRECONFIG\_HIGH\_QUALITY | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 | 跟随Sensor（镜头）最大能力 |

## 开发步骤

详细的API说明请参考[Camera API参考](../harmonyos-references/js-apis-camera.md)。

1. 导入相关接口。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   ```
2. 创建输出流Output。

   此处以创建预览流和拍照流为例。

   创建预览输出流时，涉及参数surfaceId。XComponent组件为预览流提供Surface（获取surfaceId请参考[getXcomponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)方法），而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。

   创建cameraManager对象的方法可参考[getCameraManager](../harmonyos-references/arkts-apis-camera-f.md#cameragetcameramanager)。

   Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

   ```
   1. function createCameraOutput(context: common.BaseContext, surfaceId: string) : void {
   2. // 创建预览输出流
   3. let previewOutput: camera.PreviewOutput | undefined = undefined;
   4. let cameraManager = camera.getCameraManager(context);
   5. try {
   6. previewOutput = cameraManager.createPreviewOutput(surfaceId);
   7. } catch (error) {
   8. let err = error as BusinessError;
   9. console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
   10. }
   11. if (previewOutput === undefined) {
   12. return;
   13. }

   15. // 创建拍照输出流
   16. let photoOutput: camera.PhotoOutput | undefined = undefined;
   17. try {
   18. photoOutput = cameraManager.createPhotoOutput();
   19. } catch (error) {
   20. let err = error as BusinessError;
   21. console.error('Failed to createPhotoOutput errorCode = ' + err.code);
   22. }
   23. if (photoOutput === undefined) {
   24. return;
   25. }
   26. }
   ```
3. 调用[CameraManager](../harmonyos-references/arkts-apis-camera-cameramanager.md)中的[createCameraInput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createcamerainput)方法，创建输入流Input。

   ```
   1. async function createAndOpenCameraInput(cameraManager: camera.CameraManager) : Promise<void> {
   2. // 获取相机列表
   3. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
   4. if (cameraArray.length <= 0) {
   5. console.error("cameraManager.getSupportedCameras error");
   6. return;
   7. }
   8. let cameraInput: camera.CameraInput | undefined = undefined;
   9. try {
   10. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
   11. } catch (error) {
   12. let err = error as BusinessError;
   13. console.error('Failed to createCameraInput errorCode = ' + err.code);
   14. }
   15. if (cameraInput === undefined) {
   16. return;
   17. }
   18. // 打开相机
   19. await cameraInput.open();
   20. }
   ```
4. 调用[createSession](../harmonyos-references/arkts-apis-camera-cameramanager.md#createsession11)创建会话（Session）。

   说明

   SceneMode需要指定为NORMAL\_PHOTO或NORMAL\_VIDEO，对应拍照场景[PhotoSession](../harmonyos-references/arkts-apis-camera-photosession.md)和录像场景[VideoSession](../harmonyos-references/arkts-apis-camera-videosession.md)。

   ```
   1. function createCameraSession(cameraManager: camera.CameraManager) : void {
   2. // 创建会话
   3. let photoSession: camera.PhotoSession | undefined = undefined;
   4. try {
   5. photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. console.error('Failed to create the session instance. errorCode = ' + err.code);
   9. }
   10. if (photoSession === undefined) {
   11. return;
   12. }
   13. }
   ```
5. 调用[canPreconfig](../harmonyos-references/arkts-apis-camera-photosession.md#canpreconfig12)检查对应的PreconfigType和PreconfigRatio的组合在当前设备上是否支持。确认支持后，调用[preconfig](../harmonyos-references/arkts-apis-camera-photosession.md#preconfig12)启用Preconfig配置。

   ```
   1. function GetPreconfig(photoSession: camera.PhotoSession) : void {
   2. // 查询Preconfig能力
   3. try {
   4. let isPreconfigSupport = photoSession.canPreconfig(camera.PreconfigType.PRECONFIG_1080P);
   5. if (!isPreconfigSupport) {
   6. console.error('PhotoSession canPreconfig check fail.');
   7. return;
   8. }
   9. } catch (error) {
   10. let err = error as BusinessError;
   11. console.error('Failed to call canPreconfig. errorCode = ' + err.code);
   12. return;
   13. }

   15. // 配置Preconfig
   16. try {
   17. photoSession.preconfig(camera.PreconfigType.PRECONFIG_1080P);
   18. } catch (error) {
   19. let err = error as BusinessError;
   20. console.error('Failed to call preconfig. errorCode = ' + err.code);
   21. return;
   22. }
   23. }
   ```

   说明

   若当前模式为普通录像模式，且[PreconfigType](../harmonyos-references/arkts-apis-camera-e.md#preconfigtype12)使用PRECONFIG\_HIGH\_QUALITY类型时，为避免录制失败，请务必将[AVRecorderProfile](../harmonyos-references/arkts-apis-media-i.md#avrecorderprofile9)配置文件中videoCodec参数必须配置为[VIDEO\_HEVC](../harmonyos-references/arkts-apis-media-e.md#codecmimetype8)，isHdr参数配置为true。
6. Session添加Input和Output。

   说明

   Session调用preconfig接口成功之后，Session内部会将预置数据准备好，如果向Session中进行添加未配置Profile的Output，Session则会对相应的Output进行配置对应Profile。如果向Session中添加已配置Profile的Output，则Session的预配置数据不生效。

   ```
   1. async function initCamera(photoSession: camera.PhotoSession, cameraInput: camera.CameraInput,
   2. previewOutput: camera.PreviewOutput, photoOutput: camera.PhotoOutput) : Promise<void> {
   3. // 开始配置会话
   4. try {
   5. photoSession.beginConfig();
   6. } catch (error) {
   7. let err = error as BusinessError;
   8. console.error('Failed to beginConfig. errorCode = ' + err.code);
   9. }

   11. // 向会话中添加相机输入流
   12. try {
   13. photoSession.addInput(cameraInput);
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. console.error('Failed to addInput. errorCode = ' + err.code);
   17. }

   19. // 向会话中添加预览输出流
   20. try {
   21. photoSession.addOutput(previewOutput);
   22. } catch (error) {
   23. let err = error as BusinessError;
   24. console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
   25. }

   27. // 向会话中添加拍照输出流
   28. try {
   29. photoSession.addOutput(photoOutput);
   30. } catch (error) {
   31. let err = error as BusinessError;
   32. console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
   33. }
   34. // 提交会话配置
   35. await photoSession.commitConfig();
   36. }
   ```
7. 启动Session。

   ```
   1. async function startCamera(photoSession: camera.PhotoSession) : Promise<void> {
   2. // 启动会话
   3. await photoSession.start().then(() => {
   4. console.info('Promise returned to indicate the session start success.');
   5. });
   6. }
   ```

## 完整示例

Context获取方式请参考：[获取UIAbility的上下文信息](uiability-usage.md#获取uiability的上下文信息)。

```
1. import { camera } from '@kit.CameraKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { photoAccessHelper } from '@kit.MediaLibraryKit';

7. async function savePicture(buffer: ArrayBuffer, img: image.Image, context: Context): Promise<void> {
8. let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
9. let options: photoAccessHelper.CreateOptions = {
10. title: Date.now().toString()
11. };
12. let photoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg', options);
13. let file: fileIo.File = fileIo.openSync(photoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
14. fileIo.writeSync(file.fd, buffer);
15. fileIo.closeSync(file);
16. await img.release();
17. }

19. function setPhotoOutputCb(photoOutput: camera.PhotoOutput, context: Context): void {
20. // 设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中
21. photoOutput.on('photoAvailable', (errCode: BusinessError, photo: camera.Photo): void => {
22. console.info('getPhoto start');
23. console.info(`err: ${JSON.stringify(errCode)}`);
24. if (errCode || photo === undefined) {
25. console.error('getPhoto failed');
26. return;
27. }
28. let imageObj = photo.main;
29. imageObj.getComponent(image.ComponentType.JPEG, (errCode: BusinessError, component: image.Component): void => {
30. console.info('getComponent start');
31. if (errCode || component === undefined) {
32. console.error('getComponent failed');
33. return;
34. }
35. let buffer: ArrayBuffer;
36. if (component.byteBuffer) {
37. buffer = component.byteBuffer;
38. } else {
39. console.error('byteBuffer is null');
40. return;
41. }
42. savePicture(buffer, imageObj, context);
43. });
44. });
45. }

47. async function cameraShootingCase(context: Context, surfaceId: string): Promise<void> {
48. // 创建CameraManager对象
49. let cameraManager: camera.CameraManager = camera.getCameraManager(context);
50. if (!cameraManager) {
51. console.error("camera.getCameraManager error");
52. return;
53. }
54. // 监听相机状态变化
55. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
56. if (err !== undefined && err.code !== 0) {
57. console.error('cameraStatus with errorCode = ' + err.code);
58. return;
59. }
60. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
61. console.info(`status: ${cameraStatusInfo.status}`);
62. });

64. // 获取相机列表
65. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
66. if (cameraArray.length <= 0) {
67. console.error("cameraManager.getSupportedCameras error");
68. return;
69. }

71. for (let index = 0; index < cameraArray.length; index++) {
72. console.info('cameraId : ' + cameraArray[index].cameraId); // 获取相机ID
73. console.info('cameraPosition : ' + cameraArray[index].cameraPosition); // 获取相机位置
74. console.info('cameraType : ' + cameraArray[index].cameraType); // 获取相机类型
75. console.info('connectionType : ' + cameraArray[index].connectionType); // 获取相机连接类型
76. }

78. // 创建相机输入流
79. let cameraInput: camera.CameraInput | undefined = undefined;
80. try {
81. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
82. } catch (error) {
83. let err = error as BusinessError;
84. console.error('Failed to createCameraInput errorCode = ' + err.code);
85. }
86. if (cameraInput === undefined) {
87. return;
88. }

90. // 监听cameraInput错误信息
91. let cameraDevice: camera.CameraDevice = cameraArray[0];
92. cameraInput.on('error', cameraDevice, (error: BusinessError) => {
93. console.error(`Camera input error code: ${error.code}`);
94. })

96. // 打开相机
97. await cameraInput.open();

99. // 获取支持的模式类型
100. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
101. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
102. if (!isSupportPhotoMode) {
103. console.error('photo mode not support');
104. return;
105. }

107. // 创建会话
108. let photoSession: camera.PhotoSession | undefined = undefined;
109. try {
110. photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
111. } catch (error) {
112. let err = error as BusinessError;
113. console.error('Failed to create the session instance. errorCode = ' + err.code);
114. }
115. if (photoSession === undefined) {
116. return;
117. }

119. // 监听session错误信息
120. photoSession.on('error', (error: BusinessError) => {
121. console.error(`Capture session error code: ${error.code}`);
122. });

124. // 查询Preconfig能力
125. try {
126. let isPreconfigSupport = photoSession.canPreconfig(camera.PreconfigType.PRECONFIG_1080P);
127. if (!isPreconfigSupport) {
128. console.error('PhotoSession canPreconfig check fail.');
129. return;
130. }
131. } catch (error) {
132. let err = error as BusinessError;
133. console.error('Failed to call canPreconfig. errorCode = ' + err.code);
134. return;
135. }

137. // 配置Preconfig
138. try {
139. photoSession.preconfig(camera.PreconfigType.PRECONFIG_1080P);
140. } catch (error) {
141. let err = error as BusinessError;
142. console.error('Failed to call preconfig. errorCode = ' + err.code);
143. return;
144. }

146. // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
147. let previewOutput: camera.PreviewOutput | undefined = undefined;
148. try {
149. previewOutput = cameraManager.createPreviewOutput(surfaceId);
150. } catch (error) {
151. let err = error as BusinessError;
152. console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
153. }
154. if (previewOutput === undefined) {
155. return;
156. }
157. // 监听预览输出错误信息
158. previewOutput.on('error', (error: BusinessError) => {
159. console.error(`Preview output error code: ${error.code}`);
160. });

162. // 创建拍照输出流
163. let photoOutput: camera.PhotoOutput | undefined = undefined;
164. try {
165. photoOutput = cameraManager.createPhotoOutput();
166. } catch (error) {
167. let err = error as BusinessError;
168. console.error('Failed to createPhotoOutput errorCode = ' + err.code);
169. }
170. if (photoOutput === undefined) {
171. return;
172. }

174. // 调用上面的回调函数来保存图片
175. setPhotoOutputCb(photoOutput, context);

177. // 开始配置会话
178. try {
179. photoSession.beginConfig();
180. } catch (error) {
181. let err = error as BusinessError;
182. console.error('Failed to beginConfig. errorCode = ' + err.code);
183. }

185. // 向会话中添加相机输入流
186. try {
187. photoSession.addInput(cameraInput);
188. } catch (error) {
189. let err = error as BusinessError;
190. console.error('Failed to addInput. errorCode = ' + err.code);
191. }

193. // 向会话中添加预览输出流
194. try {
195. photoSession.addOutput(previewOutput);
196. } catch (error) {
197. let err = error as BusinessError;
198. console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
199. }

201. // 向会话中添加拍照输出流
202. try {
203. photoSession.addOutput(photoOutput);
204. } catch (error) {
205. let err = error as BusinessError;
206. console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
207. }

209. // 提交会话配置
210. await photoSession.commitConfig();

212. // 启动会话
213. await photoSession.start().then(() => {
214. console.info('Promise returned to indicate the session start success.');
215. });
216. // 判断设备是否支持闪光灯
217. let flashStatus: boolean = false;
218. try {
219. flashStatus = photoSession.hasFlash();
220. } catch (error) {
221. let err = error as BusinessError;
222. console.error('Failed to hasFlash. errorCode = ' + err.code);
223. }
224. console.info('Returned with the flash light support status:' + flashStatus);

226. if (flashStatus) {
227. // 判断是否支持自动闪光灯模式
228. let flashModeStatus: boolean = false;
229. try {
230. let status: boolean = photoSession.isFlashModeSupported(camera.FlashMode.FLASH_MODE_AUTO);
231. flashModeStatus = status;
232. } catch (error) {
233. let err = error as BusinessError;
234. console.error('Failed to check whether the flash mode is supported. errorCode = ' + err.code);
235. }
236. if(flashModeStatus) {
237. // 设置自动闪光灯模式
238. try {
239. photoSession.setFlashMode(camera.FlashMode.FLASH_MODE_AUTO);
240. } catch (error) {
241. let err = error as BusinessError;
242. console.error('Failed to set the flash mode. errorCode = ' + err.code);
243. }
244. }
245. }

247. // 判断是否支持连续自动变焦模式
248. let focusModeStatus: boolean = false;
249. try {
250. let status: boolean = photoSession.isFocusModeSupported(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
251. focusModeStatus = status;
252. } catch (error) {
253. let err = error as BusinessError;
254. console.error('Failed to check whether the focus mode is supported. errorCode = ' + err.code);
255. }

257. if (focusModeStatus) {
258. // 设置连续自动变焦模式
259. try {
260. photoSession.setFocusMode(camera.FocusMode.FOCUS_MODE_CONTINUOUS_AUTO);
261. } catch (error) {
262. let err = error as BusinessError;
263. console.error('Failed to set the focus mode. errorCode = ' + err.code);
264. }
265. }

267. // 获取相机支持的可变焦距比范围
268. let zoomRatioRange: Array<number> = [];
269. try {
270. zoomRatioRange = photoSession.getZoomRatioRange();
271. } catch (error) {
272. let err = error as BusinessError;
273. console.error('Failed to get the zoom ratio range. errorCode = ' + err.code);
274. }
275. if (zoomRatioRange.length <= 0) {
276. return;
277. }
278. // 设置可变焦距比
279. try {
280. photoSession.setZoomRatio(zoomRatioRange[0]);
281. } catch (error) {
282. let err = error as BusinessError;
283. console.error('Failed to set the zoom ratio value. errorCode = ' + err.code);
284. }
285. let photoCaptureSetting: camera.PhotoCaptureSetting = {
286. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高
287. rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0
288. }
289. // 使用当前拍照设置进行拍照，需要在拍照时主动调用该接口拍摄图片。
290. photoOutput.capture(photoCaptureSetting, (err: BusinessError) => {
291. if (err) {
292. console.error(`Failed to capture the photo ${err.message}`);
293. return;
294. }
295. console.info('Callback invoked to indicate the photo capture request success.');
296. });

298. // 需要在拍照结束之后调用以下关闭摄像头和释放会话流程，避免拍照未结束就将会话释放。
299. // 停止当前会话
300. await photoSession.stop();

302. // 释放相机输入流
303. await cameraInput.close();

305. // 释放预览输出流
306. await previewOutput.release();

308. // 释放拍照输出流
309. await photoOutput.release();

311. // 释放会话
312. await photoSession.release();

314. // 会话置空
315. photoSession = undefined;
316. }
```
