---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-hdr-shooting
title: HDR Vivid相机拍照(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > HDR Vivid相机拍照(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:04+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:c24d43deb65823524d8756850366a4828f03a98cdce414904ea0046759792be8
---

HarmonyOS支持调用接口拍摄HDR Vivid照片，可以拍出层次表现更细腻、光影细节更丰富的画面，提升画面质感，呈现更卓越的视觉效果。

当前示例提供完整的HDR Vivid拍照开发步骤，方便开发者实现HDR拍照的功能。更多HDR Vivid的开发指导，请参考[使用HDR Vivid特性开发媒体应用](multimedia-hdr-vivid.md)。

在参考以下示例前，建议开发者查看[相机开发指导(ArkTS)](camera-device-management.md)的具体章节，了解[设备输入](camera-device-input.md)、[会话管理](camera-session-management.md)、[拍照](camera-shooting.md)等单个流程。

## 开发步骤

1. 导入接口。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { colorSpaceManager } from '@kit.ArkGraphics2D';
   3. import { image } from '@kit.ImageKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { fileIo } from '@kit.CoreFileKit';
   6. import { photoAccessHelper } from '@kit.MediaLibraryKit';
   ```
2. 查询支持的色彩空间。

   ```
   1. function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
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
3. 设置色彩空间。

   如果是SDR拍照色彩空间需要设置为SRGB，如果是HDR拍照色彩空间需要设置为DISPLAY\_P3。具体参考[setColorSpace](../harmonyos-references/arkts-apis-camera-colormanagement.md#setcolorspace12)。

   ```
   1. function setColorSpaceBeforeCommitConfig(session: camera.PhotoSession, isHdr: boolean): void {
   2. let colorSpace: colorSpaceManager.ColorSpace = isHdr? colorSpaceManager.ColorSpace.DISPLAY_P3 : colorSpaceManager.ColorSpace.SRGB;
   3. let colorSpaces: Array<colorSpaceManager.ColorSpace> = getSupportedColorSpaces(session);
   4. let isSupportedColorSpaces = colorSpaces.indexOf(colorSpace) >= 0;
   5. if (isSupportedColorSpaces) {
   6. console.info(`setColorSpace: ${colorSpace}`);
   7. session.setColorSpace(colorSpace);
   8. let activeColorSpace:colorSpaceManager.ColorSpace = session.getActiveColorSpace();
   9. console.info(`activeColorSpace: ${activeColorSpace}`);
   10. } else {
   11. console.info(`colorSpace: ${colorSpace} is not support`);
   12. }
   13. }
   ```
4. 实现HDR拍照。

   在提交会话配置前执行步骤3设置色彩空间，其余流程按照正常拍照流程开发。

   ```
   1. async function savePicture(buffer: ArrayBuffer, img: image.Image, context: Context): Promise<void> {
   2. let accessHelper: photoAccessHelper.PhotoAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
   3. let options: photoAccessHelper.CreateOptions = {
   4. title: Date.now().toString()
   5. };
   6. let photoUri: string = await accessHelper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'jpg', options);
   7. // createAsset的调用需要ohos.permission.READ_IMAGEVIDEO和ohos.permission.WRITE_IMAGEVIDEO的权限
   8. let file: fileIo.File = fileIo.openSync(photoUri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   9. await fileIo.write(file.fd, buffer);
   10. fileIo.closeSync(file);
   11. img.release();
   12. }

   14. function setPhotoOutputCb(photoOutput: camera.PhotoOutput, context: Context): void {
   15. // 设置回调之后，调用photoOutput的capture方法，就会将拍照的buffer回传到回调中
   16. photoOutput.on('photoAvailable', (errCode: BusinessError, photo: camera.Photo): void => {
   17. console.info('getPhoto start');
   18. console.info(`err: ${JSON.stringify(errCode)}`);
   19. if (errCode || photo === undefined) {
   20. console.error('getPhoto failed');
   21. return;
   22. }
   23. let imageObj = photo.main;
   24. imageObj.getComponent(image.ComponentType.JPEG, (errCode: BusinessError, component: image.Component): void => {
   25. console.info('getComponent start');
   26. if (errCode || component === undefined) {
   27. console.error('getComponent failed');
   28. return;
   29. }
   30. let buffer: ArrayBuffer;
   31. if (component.byteBuffer) {
   32. buffer = component.byteBuffer;
   33. } else {
   34. console.error('byteBuffer is null');
   35. return;
   36. }
   37. savePicture(buffer, imageObj, context);
   38. });
   39. });
   40. }

   42. async function cameraHdrShootingCase(context: Context, surfaceId: string): Promise<void> {
   43. // 创建CameraManager对象
   44. let cameraManager: camera.CameraManager = camera.getCameraManager(context);
   45. if (!cameraManager) {
   46. console.error("camera.getCameraManager error");
   47. return;
   48. }
   49. // 监听相机状态变化
   50. cameraManager.on('cameraStatus', (err: BusinessError, cameraStatusInfo: camera.CameraStatusInfo) => {
   51. if (err !== undefined && err.code !== 0) {
   52. console.error('cameraStatus with errorCode = ' + err.code);
   53. return;
   54. }
   55. console.info(`camera : ${cameraStatusInfo.camera.cameraId}`);
   56. console.info(`status: ${cameraStatusInfo.status}`);
   57. });

   59. // 获取相机列表
   60. let cameraArray: Array<camera.CameraDevice> = cameraManager.getSupportedCameras();
   61. if (cameraArray.length <= 0) {
   62. console.error("cameraManager.getSupportedCameras error");
   63. return;
   64. }

   66. for (let index = 0; index < cameraArray.length; index++) {
   67. console.info('cameraId : ' + cameraArray[index].cameraId);                          // 获取相机ID
   68. console.info('cameraPosition : ' + cameraArray[index].cameraPosition);              // 获取相机位置
   69. console.info('cameraType : ' + cameraArray[index].cameraType);                      // 获取相机类型
   70. console.info('connectionType : ' + cameraArray[index].connectionType);              // 获取相机连接类型
   71. }

   73. // 创建相机输入流
   74. let cameraInput: camera.CameraInput | undefined = undefined;
   75. try {
   76. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
   77. } catch (error) {
   78. let err = error as BusinessError;
   79. console.error('Failed to createCameraInput errorCode = ' + err.code);
   80. }
   81. if (cameraInput === undefined) {
   82. return;
   83. }

   85. // 监听cameraInput错误信息
   86. let cameraDevice: camera.CameraDevice = cameraArray[0];
   87. cameraInput.on('error', cameraDevice, (error: BusinessError) => {
   88. console.error(`Camera input error code: ${error.code}`);
   89. })

   91. // 打开相机
   92. await cameraInput.open();

   94. // 获取支持的模式类型
   95. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
   96. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
   97. if (!isSupportPhotoMode) {
   98. console.error('photo mode not support');
   99. return;
   100. }
   101. // 获取相机设备支持的输出流能力
   102. let cameraOutputCap: camera.CameraOutputCapability = cameraManager.getSupportedOutputCapability(cameraArray[0], camera.SceneMode.NORMAL_PHOTO);
   103. if (!cameraOutputCap) {
   104. console.error("cameraManager.getSupportedOutputCapability error");
   105. return;
   106. }
   107. console.info("outputCapability: " + JSON.stringify(cameraOutputCap));

   109. let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
   110. if (!previewProfilesArray) {
   111. console.error("createOutput previewProfilesArray == null || undefined");
   112. }

   114. let photoProfilesArray: Array<camera.Profile> = cameraOutputCap.photoProfiles;
   115. if (!photoProfilesArray) {
   116. console.error("createOutput photoProfilesArray == null || undefined");
   117. }

   119. // 创建预览输出流,其中参数 surfaceId 参考上文 XComponent 组件，预览流为XComponent组件提供的surface
   120. let previewOutput: camera.PreviewOutput | undefined = undefined;
   121. try {
   122. previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
   123. } catch (error) {
   124. let err = error as BusinessError;
   125. console.error(`Failed to create the PreviewOutput instance. error code: ${err.code}`);
   126. }
   127. if (previewOutput === undefined) {
   128. return;
   129. }
   130. // 监听预览输出错误信息
   131. previewOutput.on('error', (error: BusinessError) => {
   132. console.error(`Preview output error code: ${error.code}`);
   133. });

   135. // 创建拍照输出流
   136. let photoOutput: camera.PhotoOutput | undefined = undefined;
   137. try {
   138. photoOutput = cameraManager.createPhotoOutput(photoProfilesArray[0]);
   139. } catch (error) {
   140. let err = error as BusinessError;
   141. console.error('Failed to createPhotoOutput errorCode = ' + err.code);
   142. }
   143. if (photoOutput === undefined) {
   144. return;
   145. }

   147. // 调用上面的回调函数来保存图片
   148. setPhotoOutputCb(photoOutput, context);

   150. // 创建会话
   151. let photoSession: camera.PhotoSession | undefined = undefined;
   152. try {
   153. photoSession = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO) as camera.PhotoSession;
   154. } catch (error) {
   155. let err = error as BusinessError;
   156. console.error('Failed to create the session instance. errorCode = ' + err.code);
   157. }
   158. if (photoSession === undefined) {
   159. return;
   160. }
   161. // 监听session错误信息
   162. photoSession.on('error', (error: BusinessError) => {
   163. console.error(`Capture session error code: ${error.code}`);
   164. });

   166. // 开始配置会话
   167. try {
   168. photoSession.beginConfig();
   169. } catch (error) {
   170. let err = error as BusinessError;
   171. console.error('Failed to beginConfig. errorCode = ' + err.code);
   172. }

   174. // 向会话中添加相机输入流
   175. try {
   176. photoSession.addInput(cameraInput);
   177. } catch (error) {
   178. let err = error as BusinessError;
   179. console.error('Failed to addInput. errorCode = ' + err.code);
   180. }

   182. // 向会话中添加预览输出流
   183. try {
   184. photoSession.addOutput(previewOutput);
   185. } catch (error) {
   186. let err = error as BusinessError;
   187. console.error('Failed to addOutput(previewOutput). errorCode = ' + err.code);
   188. }

   190. // 向会话中添加拍照输出流
   191. try {
   192. photoSession.addOutput(photoOutput);
   193. } catch (error) {
   194. let err = error as BusinessError;
   195. console.error('Failed to addOutput(photoOutput). errorCode = ' + err.code);
   196. }

   198. // 设置色彩空间
   199. setColorSpaceBeforeCommitConfig(photoSession, true);

   201. // 提交会话配置
   202. await photoSession.commitConfig();

   204. // 启动会话
   205. await photoSession.start().then(() => {
   206. console.info('Promise returned to indicate the session start success.');
   207. });

   209. let photoCaptureSetting: camera.PhotoCaptureSetting = {
   210. quality: camera.QualityLevel.QUALITY_LEVEL_HIGH, // 设置图片质量高
   211. rotation: camera.ImageRotation.ROTATION_0 // 设置图片旋转角度0
   212. }
   213. // 使用当前拍照设置进行拍照
   214. photoOutput.capture(photoCaptureSetting, (err: BusinessError) => {
   215. if (err) {
   216. console.error(`Failed to capture the photo ${err.message}`);
   217. return;
   218. }
   219. console.info('Callback invoked to indicate the photo capture request success.');
   220. });

   222. // 需要在拍照结束之后调用以下关闭摄像头和释放会话流程，避免拍照未结束就将会话释放。
   223. // 停止当前会话
   224. await photoSession.stop();

   226. // 释放相机输入流
   227. await cameraInput.close();

   229. // 释放预览输出流
   230. await previewOutput.release();

   232. // 释放拍照输出流
   233. await photoOutput.release();

   235. // 释放会话
   236. await photoSession.release();

   238. // 会话置空
   239. photoSession = undefined;
   240. }
   ```
