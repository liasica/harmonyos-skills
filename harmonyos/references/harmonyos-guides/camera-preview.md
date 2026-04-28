---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-preview
title: 预览(ArkTS)
breadcrumb: 指南 > 媒体 > Camera Kit（相机服务） > 开发相机应用基础能力(ArkTS) > 预览(ArkTS)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:56+08:00
doc_updated_at: 2026-03-23
content_hash: sha256:c5270a212f172215319e746b1f81cfc3bfb6c2f7e94462a354b0b3814f0dce22
---

在开发相机应用时，需要先[申请相关权限](camera-preparation.md)。

预览是启动相机后看见的画面，通常在拍照和录像前执行。

## 开发步骤

详细的API说明请参考[@ohos.multimedia.camera (相机管理)](../harmonyos-references/arkts-apis-camera.md)。

1. 导入camera接口，接口中提供了相机相关的属性和方法，导入方法如下。

   ```
   1. import { camera } from '@kit.CameraKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 创建Surface。

   相机开发模型为Surface模型，该模型主要通过Surface实现数据交互。在开发相机应用界面时，首先需要通过创建XComponent组件为预览流提供Surface，再通过获取XComponent组件对应Surface的ID创建预览流，预览流画面即可直接在XComponent组件内渲染，详细获取surfaceId请参考[getXComponentSurfaceId](../harmonyos-references/ts-basic-components-xcomponent.md#getxcomponentsurfaceid9)方法。而XComponent的能力由UI提供，相关介绍可参考[XComponent组件参考](../harmonyos-references/ts-basic-components-xcomponent.md)。

   说明

   预览流与录像输出流的分辨率的宽高比要保持一致，如果设置XComponent组件中的Surface显示区域宽高比为1920:1080 = 16:9，则需要预览流中的分辨率的宽高比也为16:9，如分辨率选择640:360，或960:540，或1920:1080，以此类推。

   ```
   1. @Entry
   2. @Component
   3. struct example {
   4. xComponentCtl: XComponentController = new XComponentController();
   5. surfaceId:string = '';
   6. imageWidth: number = 1920;
   7. imageHeight: number = 1080;
   8. private uiContext: UIContext = this.getUIContext();
   9. private mXComponentOptions: XComponentOptions = {
   10. type: XComponentType.SURFACE,
   11. controller: this.xComponentCtl
   12. }

   14. build() {
   15. XComponent(this.mXComponentOptions)
   16. .onLoad(async () => {
   17. console.info('onLoad is called');
   18. this.surfaceId = this.xComponentCtl.getXComponentSurfaceId(); // 获取组件surfaceId。
   19. // 使用surfaceId创建预览流，开启相机，组件实时渲染每帧预览流数据。
   20. })
   21. // surface的宽、高设置与XComponent组件的宽、高设置相反，或使用.renderFit(RenderFit.RESIZE_CONTAIN)自动填充显示无需设置宽、高。
   22. .width(this.uiContext.px2vp(this.imageHeight))
   23. .height(this.uiContext.px2vp(this.imageWidth))
   24. }
   25. }
   ```
3. 通过[CameraOutputCapability](../harmonyos-references/arkts-apis-camera-i.md#cameraoutputcapability)中的previewProfiles属性获取当前设备支持的预览能力，返回previewProfilesArray数组 。通过[createPreviewOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput)方法创建预览输出流，其中，[createPreviewOutput](../harmonyos-references/arkts-apis-camera-cameramanager.md#createpreviewoutput)方法中的两个参数分别是当前设备支持的预览配置信息previewProfile和步骤二中获取的surfaceId。

   ```
   1. function getPreviewOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability, surfaceId: string): camera.PreviewOutput | undefined {
   2. if (!cameraOutputCapability || !cameraOutputCapability.previewProfiles) {
   3. return;
   4. }
   5. let previewProfilesArray: Array<camera.Profile> = cameraOutputCapability.previewProfiles;
   6. if (!previewProfilesArray || previewProfilesArray.length === 0) {
   7. console.error("previewProfilesArray is null or []");
   8. return;
   9. }
   10. let previewOutput: camera.PreviewOutput | undefined = undefined;
   11. try {
   12. // previewProfilesArray要选择与步骤二设置宽高比一致的previewProfile配置信息，此处选择数组第一项仅供接口使用示例参考。
   13. previewOutput = cameraManager.createPreviewOutput(previewProfilesArray[0], surfaceId);
   14. } catch (error) {
   15. let err = error as BusinessError;
   16. console.error("Failed to create the PreviewOutput instance. error code: " + err.code);
   17. }
   18. return previewOutput;
   19. }
   ```
4. 使能。通过[Session.start](../harmonyos-references/arkts-apis-camera-session.md#start11)方法输出预览流，接口调用失败会返回相应错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

   ```
   1. async function startPreviewOutput(cameraManager: camera.CameraManager, previewOutput: camera.PreviewOutput): Promise<void> {
   2. try {
   3. let cameraArray: Array<camera.CameraDevice> = [];
   4. cameraArray = cameraManager.getSupportedCameras();
   5. if (cameraArray.length == 0) {
   6. console.error('no camera.');
   7. return;
   8. }
   9. // 获取支持的模式类型。
   10. let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray[0]);
   11. let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL_PHOTO) >= 0;
   12. if (!isSupportPhotoMode) {
   13. console.error('photo mode not support');
   14. return;
   15. }
   16. let cameraInput: camera.CameraInput | undefined;
   17. cameraInput = cameraManager.createCameraInput(cameraArray[0]);
   18. if (cameraInput === undefined) {
   19. console.error('cameraInput is undefined');
   20. return;
   21. }
   22. // 打开相机。
   23. await cameraInput.open();
   24. let session = cameraManager.createSession(camera.SceneMode.NORMAL_PHOTO);
   25. if (!session) {
   26. console.error('session is null');
   27. return;
   28. }
   29. let photoSession: camera.PhotoSession = session as camera.PhotoSession;
   30. photoSession.beginConfig();
   31. photoSession.addInput(cameraInput);
   32. photoSession.addOutput(previewOutput);
   33. await photoSession.commitConfig();
   34. await photoSession.start();
   35. } catch (error) {
   36. console.error(`startPreviewOutput call failed, error: ${error}`);
   37. }
   38. }
   ```

## 状态监听

在相机应用开发过程中，可以随时监听预览输出流状态，包括预览流启动、预览流结束、预览流输出错误。

* 通过注册固定的[on('frameStart')](../harmonyos-references/arkts-apis-camera-previewoutput.md#onframestart)回调函数获取监听预览启动结果，previewOutput创建成功时即可监听，预览第一次曝光时触发，有该事件返回结果则认为预览流已启动。

  ```
  1. function onPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
  2. previewOutput.on('frameStart', (err: BusinessError) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info('Preview frame started');
  7. });
  8. }
  ```
* 通过注册固定的[on('frameEnd')](../harmonyos-references/arkts-apis-camera-previewoutput.md#onframeend)回调函数获取监听预览结束结果，previewOutput创建成功时即可监听，预览完成最后一帧时触发，有该事件返回结果则认为预览流已结束。

  ```
  1. function onPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
  2. previewOutput.on('frameEnd', (err: BusinessError) => {
  3. if (err !== undefined && err.code !== 0) {
  4. return;
  5. }
  6. console.info('Preview frame ended');
  7. });
  8. }
  ```
* 通过注册固定的error回调函数获取监听预览输出错误结果，回调返回预览输出接口使用错误时对应的错误码，错误码类型参见[CameraErrorCode](../harmonyos-references/arkts-apis-camera-e.md#cameraerrorcode)。

  ```
  1. function onPreviewOutputError(previewOutput: camera.PreviewOutput): void {
  2. previewOutput.on('error', (previewOutputError: BusinessError) => {
  3. console.error(`Preview output error code: ${previewOutputError.code}`);
  4. });
  5. }
  ```

## 完整示例

```
1. import { camera } from '@kit.CameraKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

6. @Entry
7. @Component
8. struct Index {
9. private xComponentCtl: XComponentController = new XComponentController();
10. private xComponentSurfaceId: string = '';
11. @State imageWidth: number = 1920;
12. @State imageHeight: number = 1080;
13. private cameraManager: camera.CameraManager | undefined = undefined;
14. private cameras: Array<camera.CameraDevice> | undefined = [];
15. private cameraInput: camera.CameraInput | undefined = undefined;
16. private previewOutput: camera.PreviewOutput | undefined = undefined;
17. private session: camera.VideoSession | undefined = undefined;
18. private uiContext: UIContext = this.getUIContext();
19. private context: Context | undefined = this.uiContext.getHostContext();
20. private cameraPermission: Permissions = 'ohos.permission.CAMERA'; // 申请权限相关问题可参考本篇开头的申请相关权限文档
21. @State isShow: boolean = false;
22. private mXComponentOptions: XComponentOptions = {
23. type: XComponentType.SURFACE,
24. controller: this.xComponentCtl
25. }

27. async requestPermissionsFn(): Promise<void> {
28. let atManager = abilityAccessCtrl.createAtManager();
29. if (this.context) {
30. let res = await atManager.requestPermissionsFromUser(this.context, [this.cameraPermission]);
31. for (let i = 0; i < res.permissions.length; i++) {
32. if (this.cameraPermission.toString() === res.permissions[i] && res.authResults[i] === 0) {
33. this.isShow = true;
34. }
35. }
36. }
37. }

39. aboutToAppear(): void {
40. this.requestPermissionsFn();
41. }

43. onPageShow(): void {
44. console.info('onPageShow');
45. if (this.xComponentSurfaceId !== '') {
46. this.initCamera();
47. }
48. }

50. onPageHide(): void {
51. console.info('onPageHide');
52. this.releaseCamera();
53. }

55. build() {
56. Column() {
57. if (this.isShow) {
58. XComponent(this.mXComponentOptions)
59. .onLoad(async () => {
60. console.info('onLoad is called');
61. this.xComponentSurfaceId = this.xComponentCtl.getXComponentSurfaceId(); // 获取组件surfaceId。
62. // 初始化相机，组件实时渲染每帧预览流数据。
63. this.initCamera()
64. })
65. .width(this.uiContext.px2vp(this.imageHeight))
66. .height(this.uiContext.px2vp(this.imageWidth))
67. }
68. }
69. .justifyContent(FlexAlign.Center)
70. .height('100%')
71. .width('100%')
72. }

75. // 初始化相机。
76. async initCamera(): Promise<void> {
77. console.info(`initCamera previewOutput xComponentSurfaceId:${this.xComponentSurfaceId}`);
78. try {
79. // 获取相机管理器实例。
80. this.cameraManager = camera.getCameraManager(this.context);
81. if (!this.cameraManager) {
82. console.error('initCamera getCameraManager');
83. return;
84. }
85. // 获取当前设备支持的相机device列表。
86. this.cameras = this.cameraManager.getSupportedCameras();
87. if (!this.cameras) {
88. console.error('initCamera getSupportedCameras');
89. }
90. // 选择一个相机device，创建cameraInput输出对象。
91. this.cameraInput = this.cameraManager.createCameraInput(this.cameras[0]);
92. if (!this.cameraInput) {
93. console.error('initCamera createCameraInput');
94. return;
95. }
96. // 打开相机。
97. await this.cameraInput.open();
98. // 获取相机device支持的profile。
99. let capability: camera.CameraOutputCapability =
100. this.cameraManager.getSupportedOutputCapability(this.cameras[0], camera.SceneMode.NORMAL_VIDEO);
101. if (!capability || capability.previewProfiles.length === 0) {
102. console.error('capability is null || []');
103. this.releaseCamera();
104. return;
105. }
106. let minRatioDiff : number = 0.1;
107. let surfaceRatio : number = this.imageWidth / this.imageHeight; // 最接近16:9宽高比。
108. let previewProfile: camera.Profile = capability.previewProfiles[0];
109. // 应用开发者根据实际业务需求选择一个支持的预览流previewProfile。
110. // 此处以选择CAMERA_FORMAT_YUV_420_SP（NV21）格式、满足限定条件分辨率的预览流previewProfile为例。
111. for (let index = 0; index < capability.previewProfiles.length; index++) {
112. const tempProfile = capability.previewProfiles[index];
113. let tempRatio = tempProfile.size.width >= tempProfile.size.height ?
114. tempProfile.size.width / tempProfile.size.height : tempProfile.size.height / tempProfile.size.width;
115. let currentRatio = Math.abs(tempRatio - surfaceRatio);
116. if (currentRatio <= minRatioDiff && tempProfile.format == camera.CameraFormat.CAMERA_FORMAT_YUV_420_SP) {
117. previewProfile = tempProfile;
118. break;
119. }
120. }
121. this.imageWidth = previewProfile.size.width; // 更新xComponent组件的宽。
122. this.imageHeight = previewProfile.size.height; // 更新xComponent组件的高。
123. console.info(`initCamera imageWidth:${this.imageWidth} imageHeight:${this.imageHeight}`);

125. // 使用xComponentSurfaceId创建预览。
126. this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);
127. if (!this.previewOutput) {
128. console.error('initCamera createPreviewOutput');
129. this.releaseCamera();
130. return;
131. }
132. // 创建录像模式相机会话。
133. let session = this.cameraManager.createSession(camera.SceneMode.NORMAL_VIDEO);
134. if (!session) {
135. console.error('session is null');
136. this.releaseCamera();
137. return;
138. }
139. this.session = session as camera.VideoSession;
140. // 开始配置会话。
141. this.session.beginConfig();
142. // 添加相机设备输入。
143. this.session.addInput(this.cameraInput);
144. // 添加预览流输出。
145. this.session.addOutput(this.previewOutput);
146. // 提交会话配置。
147. await this.session.commitConfig();
148. // 开始启动已配置的输入输出流。
149. await this.session.start();
150. } catch (error) {
151. console.error(`initCamera fail: ${JSON.stringify(error)}`);
152. this.releaseCamera();
153. }
154. }

156. // 释放相机。
157. async releaseCamera(): Promise<void> {
158. console.info('releaseCamera');
159. // 停止当前会话。
160. await this.session?.stop().catch((e: BusinessError) => {console.error('Failed to stop session: ', e)});
161. // 释放相机输入流。
162. await this.cameraInput?.close().catch((e: BusinessError) => {console.error('Failed to close the camera: ', e)});
163. // 释放预览输出流。
164. await this.previewOutput?.release().catch((e: BusinessError) => {console.error('Failed to stop the preview stream: ', e)});
165. // 释放会话。
166. await this.session?.release().catch((e: BusinessError) => {console.error('Failed to release session: ', e)});
167. }
168. }
```
