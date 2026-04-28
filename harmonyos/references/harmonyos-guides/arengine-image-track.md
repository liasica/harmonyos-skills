---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-image-track
title: 图像跟踪（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 图像跟踪 > 图像跟踪（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:58+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:016c82ea7cdd6fb1f10afd79ca9f1d860b06d817aa8e9c45e99e9459f5322e07
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/HarmonyOS_Samples/arengine_samplecode_clientdemo_arkts)。

## 约束与限制

图像跟踪能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_IMAGE](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

图像识别主要依赖[ARAugmentedImageDatabase](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabase)、[ARImage](../harmonyos-references/arengine-api-arengine.md#arimage)，以下接口为图像识别相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [arEngine.createARAugmentedImageDatabase](../harmonyos-references/arengine-api-arengine.md#arenginecreatearaugmentedimagedatabase) | 创建一个增强型图像数据库。 |
| [ARAugmentedImageDatabase.deserialize](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasedeserialize) | 将增强图像数据库缓冲区反序列化为一个新的增强图像数据库对象。 |
| [ARAugmentedImageDatabase.serialize](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabaseserialize) | 将增强图像数据库序列化为一个缓冲区。 |
| [ARAugmentedImageDatabase.addImage](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabaseaddimage) | 将图像添加到图像数据库，并输出对应图像的索引。 |
| [ARAugmentedImageDatabase.getImageCount](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasegetimagecount) | 获取图像数据库中图像的数量。 |
| [ARAugmentedImageDatabase.getCapacity](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasegetcapacity) | 可以添加的最大图像数量。 |
| [ARAugmentedImageDatabase.getImageAddMode](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasegetimageaddmode) | 获取图片添加模式。 |
| [ARAugmentedImageDatabase.setImageAddMode](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabasesetimageaddmode) | 设置图片添加模式。 |
| [ARAugmentedImageDatabase.release](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabaserelease) | 释放增强图像数据库对象[ARAugmentedImageDatabase](../harmonyos-references/arengine-api-arengine.md#araugmentedimagedatabase)占用的内存。 |
| [ARImage.release](../harmonyos-references/arengine-api-arengine.md#arimagerelease) | 释放相机视频流帧对象[ARImage](../harmonyos-references/arengine-api-arengine.md#arimage)占用的内存。 |
| [ARAugmentedImage](../harmonyos-references/arengine-api-arengine.md#araugmentedimage) | 表示可被追踪的增强图像对象。 |

## 开发步骤

AR Engine仅输出识别到的平面数据。为便于用户观察，可使用AGP（Ark Graphics Platform）渲染引擎或者[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)绘制识别的平面。关于AGP的介绍可以查看[ArkGraphics 3D简介](arkgraphics3d-overview.md)和[AGP引擎](https://gitcode.com/openharmony/graphic_graphic_3d)。

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 创建UI页面

首先创建一个初始UI页面“ARImage.ets”，设置两个按钮，用于实现“添加本地图片”和“读取本地数据库”两个功能，分别命名“ARImageByAdd.ets”和“ARImageByDatabase.ets”。并配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

### ARImage页面

```
1. // ARImage.ets
2. // 导入图片模块
3. import { photoAccessHelper } from '@kit.MediaLibraryKit';

5. @Builder
6. export function ARImageBuilder(): void {
7. ARImage();
8. }

10. @Component
11. struct ARImage {
12. pageInfo: NavPathStack = new NavPathStack();

14. // UI配置
15. build(): void {
16. NavDestination() {
17. Column() {
18. Button('选择本地图片', { type: ButtonType.Normal, stateEffect: true })
19. .borderRadius(8)
20. .width('50%')
21. .height('5%')
22. .onClick(async () => {
23. await this.chooseImageToTrack();
24. })

26. Button('加载本地数据库', { type: ButtonType.Normal, stateEffect: true })
27. .borderRadius(8)
28. .width('50%')
29. .height('5%')
30. .onClick(() => {
31. this.loadDatabaseToTrack();
32. })
33. }
34. .justifyContent(FlexAlign.SpaceEvenly)
35. .width('100%')
36. .height('100%')
37. }
38. .onReady((context: NavDestinationContext) => {
39. this.pageInfo = context.pathStack;
40. })
41. .hideTitleBar(true)
42. .hideBackButton(true)
43. .hideToolBar(true)
44. }

46. // 选择本地图片模式
47. private async chooseImageToTrack(): Promise<void> {
48. try {
49. let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
50. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
51. photoOption.maxSelectNumber = 50; // Default
52. photoOption.isEditSupported = false;
53. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

55. await photoPicker.select(photoOption).then((photoResult) => {
56. if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
57. this.pageInfo.pushDestinationByName('ARImageByAdd', photoResult.photoUris).catch((error: BusinessError) => {
58. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
59. });
60. }
61. }).catch((error: BusinessError) => {
62. // ...
63. })
64. } catch (error) {
65. console.error(`Failed to select by photoPicker. Code: ${error.code}.`);
66. }
67. }

69. // 加载本地数据库模式
70. private loadDatabaseToTrack(): void {
71. this.pageInfo.pushDestinationByName('ARImageByDatabase', null).catch((error: BusinessError) => {
72. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
73. });
74. }
75. }
```

### ARImageByAdd页面

加载本地图片模式。

1. 选择本地图片进行图像识别能力所需要导入的模块如下：

   ```
   1. // ARImageByAdd.ets

   3. import { arEngine, ARView, arViewController } from '@kit.AREngine';
   4. import { Node, Scene } from '@kit.ArkGraphics3D';
   5. import { collections } from '@kit.ArkTS';
   6. import { BusinessError } from '@kit.BasicServicesKit';
   7. import { fileIo } from '@kit.CoreFileKit';
   8. import { image } from '@kit.ImageKit';
   ```
2. 配置页面路由信息，定义数据库dataBase。

   ```
   1. // ARImageByAdd.ets

   3. // 页面路由
   4. @Builder
   5. export function ARImageByAddBuilder(): void {
   6. ARImageByAdd();
   7. }

   9. let dataBase: arEngine.ARAugmentedImageDatabase;
   ```
3. 在设备界面上显示图片添加情况，无可用图片则弹窗提示，加载AR场景。

   ```
   1. // ARImageByAdd.ets

   3. @Component
   4. struct ARImageByAdd {
   5. pageInfo: NavPathStack = new NavPathStack();
   6. private imagePathArray: string[] = [];
   7. private isProgramExits: boolean = false;
   8. private isSaveDatabase: boolean = false;
   9. @State arContext?: arViewController.ARViewContext = undefined;
   10. @State context: Context = this.getUIContext().getHostContext() as Context;
   11. @State totalImageCounts: number = this.imagePathArray.length;
   12. @State addFailedImageCounts: number = 0;
   13. @State succeedImageCounts: number = 0;
   14. @State addFailedMessage: string[] = [];

   16. build(): void {
   17. NavDestination() {
   18. RelativeContainer() {
   19. Column() {
   20. Text(`添加图片进度：${this.succeedImageCounts + this.addFailedImageCounts} / ${this.totalImageCounts}`)
   21. Text(`添加成功数量：${this.succeedImageCounts}`)
   22. Text(`添加失败数量：${this.addFailedImageCounts}`)

   24. if (this.addFailedMessage) {
   25. ForEach(this.addFailedMessage, (item: string) => {
   26. Text(`${item}`)
   27. .fontColor(Color.Red)
   28. })
   29. }
   30. }
   31. .visibility(this.addFailedImageCounts + this.succeedImageCounts < this.totalImageCounts ? Visibility.Visible :
   32. Visibility.None)
   33. .foregroundColor(Color.Red)
   34. .zIndex(1)
   35. .alignRules({
   36. center: { anchor: '__container__', align: VerticalAlign.Center },
   37. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   38. })

   40. if (this.arContext) {
   41. ARView({ context: this.arContext })
   42. .height('100%')
   43. .width('100%')
   44. .alignRules({
   45. center: { anchor: '__container__', align: VerticalAlign.Center },
   46. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   47. })
   48. }
   49. }
   50. }
   51. // 创建数据库，加载本地缓存，初始化AR场景，创建AR会话
   52. .onAppear(async () => {
   53. await arEngine.createARAugmentedImageDatabase()
   54. .then(async (arDataBase) => {
   55. dataBase = arDataBase;

   57. await this.addImage(dataBase).then(() => {
   58. if (this.addFailedImageCounts === this.totalImageCounts) {
   59. this.ShowDialog('请添加有效图片。');
   60. }
   61. this.initARView();
   62. })
   63. })
   64. .catch((error: BusinessError) => {
   65. console.error(`Failed to create AR Augmented Database.Code is ${error.code}, message is ${error.message}`);
   66. });
   67. })
   68. .onWillDisappear(async () => {
   69. await this.stopARView();
   70. })
   71. .onShown(() => {
   72. this.resumeARView();
   73. })
   74. .onHidden(() => {
   75. this.pauseARView();
   76. })
   77. .onReady((context: NavDestinationContext) => {
   78. this.pageInfo = context.pathStack;
   79. this.imagePathArray = context.pathInfo.param as string[];
   80. this.totalImageCounts = this.imagePathArray.length;
   81. })
   82. .hideTitleBar(true)
   83. .hideBackButton(true)
   84. .hideToolBar(true)
   85. }

   87. // 初始化AR场景，创建AR会话
   88. private initARView(): void {
   89. Scene.load().then((scene: Scene) => {
   90. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
   91. viewContext.scene = scene;
   92. viewContext.callback = new ARViewCallbackImpl();
   93. viewContext.config = {
   94. type: arEngine.ARType.IMAGE,  // 使用图像跟踪模式
   95. planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
   96. powerMode: arEngine.ARPowerMode.NORMAL,
   97. semanticMode: arEngine.ARSemanticMode.NONE,
   98. poseMode: arEngine.ARPoseMode.GRAVITY,
   99. depthMode: arEngine.ARDepthMode.AUTOMATIC,
   100. meshMode: arEngine.ARMeshMode.DISABLED,
   101. focusMode: arEngine.ARFocusMode.AUTO
   102. }
   103. viewContext.init().then(() => {
   104. this.arContext = viewContext;
   105. console.info('Succeeded in initializing ARView.');
   106. }).catch((err: BusinessError) => {
   107. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
   108. })
   109. })
   110. }

   112. private async stopARView(): Promise<void> {
   113. if (!this.arContext) {
   114. return;
   115. }
   116. try {
   117. this.isProgramExits = true;
   118. if (this.isSaveDatabase) {
   119. SaveBufferToLocal(dataBase, this.context);
   120. }

   122. await dataBase.release();
   123. await this.arContext?.destroy();
   124. } catch (error) {
   125. const err: BusinessError = error as BusinessError;
   126. console.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
   127. }
   128. }

   130. private resumeARView(): void {
   131. // ...
   132. }
   133. private pauseARView(): void {
   134. // ...
   135. }

   137. // 异步执行添加图片的任务
   138. async addImage(dataBase: arEngine.ARAugmentedImageDatabase): Promise<void> {
   139. for (let index = 0; index < this.totalImageCounts; index++) {
   140. const imagePath: string = this.imagePathArray[index];
   141. let file: fileIo.File;
   142. try {
   143. file = fileIo.openSync(imagePath, fileIo.OpenMode.READ_ONLY);
   144. } catch (error) {
   145. const err: BusinessError = error as BusinessError;
   146. console.error(`Failed to open image. Code is ${err.code}, message is ${err.message}`);
   147. this.addFailedImageCounts += 1;
   148. continue
   149. }
   150. let imageName: string = file.name;
   151. const imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
   152. try {
   153. fileIo.closeSync(file);
   154. } catch (error) {
   155. const err: BusinessError = error as BusinessError;
   156. console.error(`Failed to closeSync. Code: ${err.code}.`);
   157. this.addFailedImageCounts += 1;
   158. continue;
   159. }
   160. const imageInfo: image.ImageInfo = imageSourceApi.getImageInfoSync(0);
   161. if (!imageInfo) {
   162. console.error('Failed to obtain the image pixel map information.');
   163. this.addFailedImageCounts += 1;
   164. continue;
   165. }
   166. const opts: image.DecodingOptions = {
   167. editable: true,
   168. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
   169. desiredSize: { width: imageInfo.size.width, height: imageInfo.size.height }
   170. }
   171. let pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync(opts);

   173. if (this.isProgramExits) {
   174. break;
   175. }

   177. await dataBase.addImage(imageName, pixelMap, 10).then((result: arEngine.ARAddAugmentedImageResult) => {
   178. console.info(`The imageResult: ${result.index} ${result.stateReason}.`);
   179. if (result.stateReason !== arEngine.ARAddAugmentedImageReason.NONE) {
   180. this.addFailedImageCounts += 1;
   181. this.addFailedMessage.push('失败图片名：' + imageName + '失败原因：' + errcode.get(result.stateReason) + ' ');
   182. } else {
   183. this.succeedImageCounts += 1;
   184. }
   185. }).catch(() => {
   186. this.addFailedImageCounts += 1;
   187. })

   189. await imageSourceApi.release();
   190. await pixelMap.release();
   191. }
   192. }

   194. // 自定义的弹窗提示
   195. ShowDialog(msg: string): void {
   196. this.getUIContext().showAlertDialog(
   197. {
   198. title: '警告',
   199. message: msg,
   200. autoCancel: true,
   201. alignment: DialogAlignment.Center,
   202. offset: { dx: 0, dy: -20 },
   203. gridCount: 3,
   204. transition: TransitionEffect
   205. .asymmetric(TransitionEffect.OPACITY
   206. .animation({ duration: 1000, curve: Curve.Sharp })
   207. .combine(TransitionEffect
   208. .scale({ x: 1.5, y: 1.5 })
   209. .animation({ duration: 1000, curve: Curve.Sharp })
   210. ),
   211. TransitionEffect.OPACITY
   212. .animation({ duration: 100, curve: Curve.Smooth })
   213. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
   214. .animation({ duration: 100, curve: Curve.Smooth })
   215. )
   216. ),
   217. buttons: [{
   218. enabled: true,
   219. defaultFocus: true,
   220. style: DialogButtonStyle.HIGHLIGHT,
   221. value: '退出',
   222. action: () => {
   223. console.info('Callback when the second button is clicked.');
   224. this.pageInfo.pop();
   225. return;
   226. }
   227. }]
   228. })
   229. }
   230. }
   ```
4. 退出应用时，缓存图片特征到本地。

   ```
   1. // ARImageByAdd.ets

   3. async function SaveBufferToLocal(dataBase: arEngine.ARAugmentedImageDatabase, context: Context): Promise<void> {
   4. let filesDir: string = context.filesDir;
   5. let file: fileIo.File;
   6. try {
   7. file = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC);
   8. } catch (e) {
   9. // ...
   10. }
   11. let buf: ArrayBuffer;
   12. try {
   13. buf = await dataBase.serialize()
   14. } catch (error) {
   15. // ...
   16. return;
   17. }
   18. let writeLen: number = fileIo.writeSync(file.fd, buf);
   19. console.info(`The length of buffer is: ${writeLen}`);
   20. try {
   21. fileIo.closeSync(file);
   22. } catch (error) {
   23. // ...
   24. }
   25. }
   ```
5. 调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，识别到目标图像则打印日志。

   ```
   1. // ARImageByAdd.ets

   3. class ARViewCallbackImpl extends arViewController.ARViewCallback {
   4. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
   5. // ...
   6. }

   8. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
   9. // ...
   10. }

   12. onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
   13. if (!ctx.session || !dataBase) {
   14. return;
   15. }

   17. let session: arEngine.ARSession = ctx.session; // 获取AR会话

   19. try {
   20. let imageNumber: number = dataBase.getImageCount();
   21. console.info(`The number of images in the database is ${imageNumber}.`);

   23. let imageCapacity: number = dataBase.getCapacity();
   24. console.info(`The dataBase image capacity is: ${imageCapacity}.`);

   26. let trackable: arEngine.ARTrackable[] = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);

   28. console.info(`The image trackable size: ${trackable.length}.`);
   29. for (let i = 0; i < trackable.length; ++i) {
   30. if (trackable[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
   31. let arimage: arEngine.ARAugmentedImage = trackable[i] as arEngine.ARAugmentedImage;
   32. if (arEngine.ARTrackingState.TRACKING !== arimage.state) {
   33. continue;
   34. }
   35. let centerPose: arEngine.ARPose = arimage.getPose();
   36. console.info(`The image width: ${arimage.extendX}, height: ${arimage.extendZ}, pose: ${centerPose.getMatrix()}.`);  // 打印目标图像的信息
   37. }
   38. }

   40. } catch (error) {
   41. const err: BusinessError = error as BusinessError;
   42. console.error(`Failed to got image count. Code is ${err.code}, message is ${err.message}`);
   43. }
   44. }
   45. }

   47. // 图像添加失败原因
   48. const errcode: collections.Map<number, string> = new collections.Map<number, string>([
   49. [0, 'success'],
   50. [1, 'size not match'],
   51. [2, 'too bright or too dark'],
   52. [3, 'image color is relatively single'],
   53. [4, 'other error']
   54. ])
   ```

### ARImageByDatabase页面

加载本地数据库模式。

1. 选择本地数据库进行图像识别能力所需要导入的模块如下：

   ```
   1. // ARImageByDatabase.ets

   3. import { arEngine, ARView, arViewController } from '@kit.AREngine';
   4. import { Node, Scene } from '@kit.ArkGraphics3D';
   5. import { BusinessError } from '@kit.BasicServicesKit';
   6. import { fileIo, ReadOptions } from '@kit.CoreFileKit';
   ```
2. 配置页面路由信息，定义数据库dataBase。

   ```
   1. // ARImageByDatabase.ets

   3. // 页面路由
   4. @Builder
   5. export function ARImageByDatabaseBuilder(): void {
   6. ARImageByDatabase();
   7. }

   9. let dataBase: arEngine.ARAugmentedImageDatabase;
   ```
3. 加载AR场景，加载图像数据库，无可用数据库则弹窗提示。

   ```
   1. // ARImageByDatabase.ets

   3. @Component
   4. struct ARImageByDatabase {
   5. pageInfo: NavPathStack = new NavPathStack();
   6. @State arContext?: arViewController.ARViewContext = undefined;
   7. @State context: Context = this.getUIContext().getHostContext() as Context;

   9. build() {
   10. NavDestination() {
   11. RelativeContainer() {
   12. if (this.arContext) {
   13. ARView({ context: this.arContext })
   14. .height('100%')
   15. .width('100%')
   16. .alignRules({
   17. center: { anchor: '__container__', align: VerticalAlign.Center },
   18. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   19. })
   20. }
   21. }
   22. }
   23. // 创建数据库，加载本地缓存，初始化AR场景，创建AR会话
   24. .onAppear(() => {
   25. arEngine.createARAugmentedImageDatabase()
   26. .then((arDataBase) => {
   27. dataBase = arDataBase;

   29. try {
   30. let databaseBuffer: ArrayBuffer = ReadBuffer(this.context);
   31. dataBase.deserialize(databaseBuffer).then(() => {
   32. this.initARView();
   33. })
   34. } catch (error) {
   35. const err: BusinessError = error as BusinessError;
   36. console.error(`Failed to init context. Code is ${err.code}, message is ${err.message}.`);
   37. this.ShowDialog('请添加有效图片。');
   38. }
   39. })
   40. .catch((error: BusinessError) => {
   41. console.error(`Failed to create AR Augmented Database.Code is ${error.code}, message is ${error.message}`);
   42. });
   43. })
   44. .onWillDisappear(async () => {
   45. await this.stopARView();
   46. })
   47. .onShown(() => {
   48. this.resumeARView();
   49. })
   50. .onHidden(() => {
   51. this.pauseARView();
   52. })
   53. .onReady((context: NavDestinationContext) => {
   54. this.pageInfo = context.pathStack;
   55. })
   56. .hideTitleBar(true)
   57. .hideBackButton(true)
   58. .hideToolBar(true)
   59. }

   61. // 初始化AR场景，创建AR会话
   62. private initARView(): void {
   63. Scene.load().then((scene: Scene) => {
   64. let context: arViewController.ARViewContext = new arViewController.ARViewContext();
   65. context.scene = scene;
   66. context.callback = new ARViewCallbackImpl();
   67. context.config = {
   68. type: arEngine.ARType.IMAGE,  // 使用图像跟踪模式
   69. planeFindingMode: arEngine.ARPlaneFindingMode.HORIZONTAL_AND_VERTICAL,
   70. powerMode: arEngine.ARPowerMode.NORMAL,
   71. semanticMode: arEngine.ARSemanticMode.NONE,
   72. poseMode: arEngine.ARPoseMode.GRAVITY,
   73. depthMode: arEngine.ARDepthMode.AUTOMATIC,
   74. meshMode: arEngine.ARMeshMode.ENABLE
   75. }
   76. context.init().then(() => {
   77. this.arContext = context;
   78. console.info('Succeeded in initializing ARView.');
   79. }).catch((err: BusinessError) => {
   80. console.error(`Failed to init context. Code is ${err.code}, message is ${err.message}.`);
   81. })
   82. })
   83. }

   85. private async stopARView(): Promise<void> {
   86. if (!this.arContext) {
   87. return;
   88. }
   89. try {
   90. await dataBase.release();
   91. await this.arContext?.destroy();
   92. } catch (error) {
   93. const err: BusinessError = error as BusinessError;
   94. console.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
   95. }
   96. }

   98. private resumeARView(): void {
   99. // ...
   100. }
   101. private pauseARView(): void {
   102. // ...
   103. }

   105. // 自定义的弹窗提示
   106. ShowDialog(msg: string): void {
   107. this.getUIContext().showAlertDialog(
   108. {
   109. title: '警告',
   110. message: msg,
   111. autoCancel: true,
   112. alignment: DialogAlignment.Center,
   113. offset: { dx: 0, dy: -20 },
   114. gridCount: 3,
   115. transition: TransitionEffect
   116. .asymmetric(TransitionEffect.OPACITY
   117. .animation({ duration: 1000, curve: Curve.Sharp })
   118. .combine(TransitionEffect
   119. .scale({ x: 1.5, y: 1.5 })
   120. .animation({ duration: 1000, curve: Curve.Sharp })
   121. ),
   122. TransitionEffect.OPACITY
   123. .animation({ duration: 100, curve: Curve.Smooth })
   124. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
   125. .animation({ duration: 100, curve: Curve.Smooth })
   126. )
   127. ),
   128. buttons: [{
   129. enabled: true,
   130. defaultFocus: true,
   131. style: DialogButtonStyle.HIGHLIGHT,
   132. value: '退出',
   133. action: () => {
   134. console.info('Callback when the second button is clicked.');
   135. this.pageInfo.pop();
   136. return;
   137. }
   138. }]
   139. })
   140. }
   141. }
   ```
4. 读取本地数据库缓存文件的方法。

   ```
   1. // ARImageByDatabase.ets

   3. function ReadBuffer(context: Context): ArrayBuffer {
   4. let filesDir: string = context.filesDir;
   5. let srcFile: fileIo.File;
   6. try {
   7. srcFile = fileIo.openSync(filesDir + '/test.bin', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   8. const fileStat: fileIo.Stat = fileIo.statSync(srcFile.fd);
   9. // 读取源文件的内容并写入目标文件
   10. let readSize: number = 0;
   11. let buf: ArrayBuffer = new ArrayBuffer(fileStat.size);
   12. let readOptions: ReadOptions = {
   13. offset: readSize,
   14. length: fileStat.size
   15. }
   16. let readLen: number = fileIo.readSync(srcFile.fd, buf, readOptions);
   17. console.info(`The length of buffer is: ${readLen}.`);
   18. fileIo.closeSync(srcFile);
   19. return buf;
   20. } catch (e) {
   21. // ...
   22. }
   23. }
   ```
5. 调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新，识别到目标图像则打印日志。

   ```
   1. // ARImageByDatabase.ets

   3. class ARViewCallbackImpl extends arViewController.ARViewCallback {
   4. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
   5. // ...
   6. }

   8. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
   9. // ...
   10. }

   12. onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): void {
   13. if (!ctx.session || !dataBase) {
   14. return;
   15. }

   17. let session: arEngine.ARSession = ctx.session;

   19. try {
   20. let imageNumber: number = dataBase.getImageCount();
   21. console.info(`The number of images in the database is ${imageNumber}.`);

   23. let imageCapacity: number = dataBase.getCapacity();
   24. console.info(`The dataBase image capacity = ${imageCapacity}.`);

   26. let trackable: arEngine.ARTrackable[] = session.getAllTrackables(arEngine.ARTrackableType.AUGMENTED_IMAGE);

   28. console.info(`The image trackable size: ${trackable.length}.`);
   29. for (let i = 0; i < trackable.length; ++i) {
   30. if (trackable[i].type === arEngine.ARTrackableType.AUGMENTED_IMAGE) {
   31. let arimage: arEngine.ARAugmentedImage = trackable[i] as arEngine.ARAugmentedImage;
   32. if (arEngine.ARTrackingState.TRACKING !== arimage.state) {
   33. continue;
   34. }
   35. let centerPose: arEngine.ARPose = arimage.getPose();
   36. console.info(`The image width: ${arimage.extendX}, height: ${arimage.extendZ}, pose: ${centerPose.getMatrix()}.`);  // 打印目标图像的信息
   37. }
   38. }

   40. } catch (error) {
   41. const err: BusinessError = error as BusinessError;
   42. console.error(`Failed to got image count. Code is ${err.code}, message is ${err.message}.`);
   43. }
   44. }
   45. }
   ```
