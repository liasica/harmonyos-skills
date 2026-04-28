---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-image-track
title: 图像跟踪（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 图像跟踪 > 图像跟踪（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:59+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:e069ef276d5bcfa8e00cda0fcad3603b2b689a0935d7107dc1b565c7b2654424
---

本章节给出了关键开发步骤，完整代码可以参考[示例代码](https://gitcode.com/harmonyos_samples/arengine_-sample-code_-clientdemo_cpp)。

## 约束与限制

图像跟踪能力支持部分Phone、部分Tablet设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_IMAGE](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

以下接口为AR图像跟踪相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARSession\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create) | 创建一个新的[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARSession\_Update](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_update) | 更新AR Engine的计算结果。 |
| [HMS\_AREngine\_ARSession\_Configure](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_configure) | 配置[AREngine\_ARSession](../harmonyos-references/arengine-capi-arengine.md#arengine_arsession)会话。 |
| [HMS\_AREngine\_ARFrame\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_create) | 创建一个新的[AREngine\_ARFrame](../harmonyos-references/arengine-capi-arengine.md#arengine_arframe)对象，将指针存储到中\*outFrame。 |
| [HMS\_AREngine\_ARSession\_SetDisplayGeometry](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setdisplaygeometry) | 设置显示的高和宽（以Pixel为单位）。该高度和宽度是显示视图的高度和宽度，如果不一致，会导致显示相机预览出错。 |
| [HMS\_AREngine\_ARSession\_SetCameraGLTexture](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_setcameragltexture) | 设置可用于存储相机预览流数据的openGL纹理。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_AcquireItem](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_acquireitem) | 从可跟踪列表中获取指定index的对象。 |
| [HMS\_AREngine\_ARPlane\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arplane_getcenterpose) | 获取从平面的局部坐标系到世界坐标系转换的位姿信息。 |
| [HMS\_AREngine\_ARFrame\_AcquireCamera](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arframe_acquirecamera) | 获取当前帧的相机参数对象。 |
| [HMS\_AREngine\_ARPose\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arpose_create) | 分配并初始化一个新的位姿对象。 |
| [HMS\_AREngine\_ARCamera\_GetPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arcamera_getpose) | 获取当前相机对象在AR世界空间中的位姿。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_create) | 创建一个空的跟踪图像数据。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_addimage) | 将图像添加到图像数据库并输出对应图像的索引。 |
| [HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables) | 获取所有指定类型的可跟踪对象集合。 |
| [HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize) | 获取此列表中的可跟踪对象的数量。 |
| [HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getcenterpose) | 获取跟踪图像中心点在世界坐标系中的位姿信息。 |
| [HMS\_AREngine\_ARAugmentedImage\_GetExtendX](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendx) | 获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到X轴上的估计值。 |
| [HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendz) | 获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到Z轴上的估计值。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_Serialize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_serialize) | 序列化特征数据库，在添加完图片后，可以将特征库序列化为buffer，用户可以保存此buffer以供下次使用。 |
| [HMS\_AREngine\_ARAugmentedImageDatabase\_Deserialize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_deserialize) | 反序列化特征数据库，用户可以将上次生成的或者保存的buffer数据反序列化为特征数据库后直接使用。 |

## 开发步骤

### 声明Native接口

开发者可参考AR物体摆放章节的[声明Native接口](arengine-c-arworld.md#声明native接口)。

### 创建UI界面

首先创建一个起始UI页面“ARImage.ets”，设置两个按钮，用于实现“添加本地图片”和“读取本地数据库”两个功能，分别命名“ARImageByAdd.ets”和“ARImageByDatabase.ets”。配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARImage.ets。
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Builder
6. export function ARImageBuilder() {
7. ARImage();
8. }

10. @Component
11. struct ARImage {
12. pageInfo: NavPathStack = new NavPathStack();
13. private imagePathArray: string[] = [];

15. build(): void {
16. NavDestination() {
17. Column() {
18. Button('选择本地图片', { type: ButtonType.Normal, stateEffect: true })
19. .borderRadius(8)
20. .width('50%')
21. .height('5%')
22. .onClick(async () => {

24. try {
25. let photoOption: photoAccessHelper.PhotoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
26. photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE;
27. photoOption.maxSelectNumber = 50;
28. photoOption.isEditSupported = false;
29. let photoPicker: photoAccessHelper.PhotoViewPicker = new photoAccessHelper.PhotoViewPicker();

31. let photoResult: photoAccessHelper.PhotoSelectResult = await photoPicker.select(photoOption);
32. if (photoResult.photoUris.length > 0 && photoResult.photoUris[0].length > 0) {
33. this.imagePathArray = photoResult.photoUris;
34. this.pageInfo.pushDestinationByName('ARImageByAdd', this.imagePathArray).catch((error: BusinessError) => {
35. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
36. });
37. }
38. } catch (error) {
39. const err: BusinessError = error as BusinessError;
40. console.error(`Failed to select by photoPicker. Code: ${err.code}, message is ${err.message}.`);
41. }
42. })

44. Button('加载本地数据库', { type: ButtonType.Normal, stateEffect: true })
45. .borderRadius(8)
46. .width('50%')
47. .height('5%')
48. .onClick(() => {
49. this.pageInfo.pushDestinationByName('ARImageByDatabase', null).catch((error: BusinessError) => {
50. console.error(`[pushDestinationByName]failed. Code: ${error.code}.`);
51. });
52. })
53. }
54. .justifyContent(FlexAlign.SpaceEvenly)
55. .width('100%')
56. .height('100%')
57. }
58. .onReady((context: NavDestinationContext) => {
59. this.pageInfo = context.pathStack;
60. })
61. .hideTitleBar(true)
62. .hideBackButton(true)
63. .hideToolBar(true)
64. }
65. }
```

创建一个ARImageByAdd.ets，用于选择图片，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件加载相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARImageByAdd.ets。
2. import { taskpool } from '@kit.ArkTS';
3. import { BusinessError, deviceInfo, emitter } from '@kit.BasicServicesKit';
4. import { fileIo } from '@kit.CoreFileKit';
5. import { image } from '@kit.ImageKit';
6. import { resourceManager } from '@kit.LocalizationKit';
7. import arEngineDemo from 'libentry.so';

9. @Builder
10. export function ARImageByAddBuilder() {
11. ARImageByAdd();
12. }

14. @Component
15. struct ARImageByAdd {
16. pageInfo: NavPathStack = new NavPathStack();
17. private imageAddFailedNumbers: number = 0;
18. private imageAddNumbers: number = 0;
19. private imagePathList: string[] = [];
20. private isSurfaceDestroy: boolean = false;
21. private interval: number = -1;
22. private isUpdate: boolean = false;
23. private xComponentId = 'ARImage';
24. @State addImageLog: string = '';
25. @State context: Context = this.getUIContext().getHostContext() as Context;
26. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
27. @State imageTotalNumbers: number = 0;
28. @State private isImageAddComplete: boolean = false;
29. @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;
30. @State showPage: boolean = true;

32. build(): void {
33. NavDestination() {
34. RelativeContainer() {
35. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
36. .width('100%')
37. .height('100%')
38. .visibility(this.showPage ? Visibility.Visible : Visibility.None)
39. .alignRules({
40. center: { anchor: '__container__', align: VerticalAlign.Center },
41. middle: { anchor: '__container__', align: HorizontalAlign.Center }
42. })
43. .onLoad(() => {
44. console.info(`XComponent onLoad ${this.xComponentId}.`);
45. this.interval = setInterval(() => {
46. if (!this.isUpdate || !this.isImageAddComplete || this.imageAddNumbers === 0) {
47. return;
48. }
49. arEngineDemo.update(this.xComponentId);
50. }, 33) // 将帧率设置为30fps（每33ms 刷新一次帧）。
51. })
52. .onDestroy(() => {
53. console.info(`XComponent onDestroy ${this.xComponentId}.`);
54. this.isSurfaceDestroy = true;
55. clearInterval(this.interval);
56. })

58. Text('添加图片进度：' +
59. this.imageTotalNumbers.toString() + '/' + this.imagePathList.length.toString() + '\n ' +
60. '添加成功数量：' +
61. this.imageAddNumbers + ' \n' +
62. '添加失败数量：' +
63. this.imageAddFailedNumbers + '\n' + this.addImageLog)
64. .width(300)
65. .textAlign(TextAlign.Center)
66. .fontColor(Color.Red)
67. .visibility(!this.isImageAddComplete ? Visibility.Visible : Visibility.None)
68. .alignRules({
69. center: { anchor: '__container__', align: VerticalAlign.Center },
70. middle: { anchor: '__container__', align: HorizontalAlign.Center }
71. })
72. }
73. }
74. .onBackPressed(() => {
75. console.error('Failed to onBackPressed.');
76. return false;
77. })
78. .onAppear(() => {
79. arEngineDemo.init(this.resMgr);
80. let config: Int32Array = new Int32Array([1, this.rotation]);
81. arEngineDemo.start(this.xComponentId, config);

83. try {
84. console.info(`Image path length: ${this.imagePathList.length}.`);
85. this.RegisterAddImageCallback();
86. taskpool.execute(addImage, this.xComponentId, this.imagePathList, errcode).then(() => {
87. console.info('Add image task complete.');
88. emitter.emit('checkAddImageResult');
89. })
90. } catch (error) {
91. const err: BusinessError = error as BusinessError;
92. console.error(`Failed to promise options error. Code: ${err.code}, message is ${err.message}.`);
93. }
94. })
95. .onWillDisappear(() => {
96. if (this.imageAddNumbers > 0) {
97. arEngineDemo.saveImageDataBaseToLocal(this.xComponentId, this.context.filesDir);
98. }
99. arEngineDemo.stop(this.xComponentId);
100. })
101. .onShown(() => {
102. this.isUpdate = true;
103. arEngineDemo.show(this.xComponentId);
104. })
105. .onHidden(() => {
106. this.isUpdate = false;
107. if (!this.isSurfaceDestroy) {
108. arEngineDemo.hide(this.xComponentId);
109. }
110. })
111. .onReady((context: NavDestinationContext) => {
112. this.pageInfo = context.pathStack;
113. this.imagePathList = context.pathInfo.param as string[];
114. })
115. .hideTitleBar(true)
116. .hideBackButton(false)
117. .hideToolBar(true)
118. }

120. private ShowDialog(msg: string): void {
121. this.getUIContext().showAlertDialog({
122. title: '警告',
123. message: msg,
124. autoCancel: true,
125. alignment: DialogAlignment.Center,
126. offset: { dx: 0, dy: -20 },
127. gridCount: 3,
128. transition: TransitionEffect
129. .asymmetric(TransitionEffect.OPACITY
130. .animation({ duration: 1000, curve: Curve.Sharp })
131. .combine(TransitionEffect
132. .scale({ x: 1.5, y: 1.5 })
133. .animation({ duration: 1000, curve: Curve.Sharp })
134. ),
135. TransitionEffect.OPACITY
136. .animation({ duration: 100, curve: Curve.Smooth })
137. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
138. .animation({ duration: 100, curve: Curve.Smooth })
139. )
140. ),
141. buttons: [{
142. enabled: true,
143. defaultFocus: true,
144. style: DialogButtonStyle.HIGHLIGHT,
145. value: '退出',
146. action: () => {
147. console.info('Callback when the second button is clicked')
148. this.pageInfo.pop();
149. }
150. }]
151. })
152. }

154. private RegisterAddImageCallback(): void {
155. emitter.on('addImage', (data: emitter.EventData) => {
156. if (data.data?.addImageReason === 0) {
157. this.imageAddNumbers++;
158. console.info(`Succeeded in adding image, image numbers: ${this.imageAddNumbers}.`);
159. } else {
160. this.imageAddFailedNumbers++;
161. this.addImageLog += '失败图片名：' +
162. data.data?.imageName + '\n' +
163. '失败原因：' +
164. errcode.get(data.data?.addImageReason) + '\n';
165. console.error(`Failed to add image, image numbers: ${this.imageAddFailedNumbers}.`);
166. }
167. this.imageTotalNumbers++;
168. })

170. emitter.on('checkAddImageResult', () => {
171. if (this.imageAddNumbers === 0 && this.isUpdate) {
172. this.showPage = false;
173. this.ShowDialog('请添加有效图片');
174. }
175. emitter.off('addImage');
176. this.isImageAddComplete = true;
177. emitter.off('checkAddImageResult');
178. })
179. }
180. }

182. let errcode: Map<number, string> = new Map<number, string>([[0, 'success'], [1, 'size not match'],
183. [2, 'too bright or too dark'], [3, 'image color is relatively single'], [4, 'other error']]);

185. // 异步执行添加图片任务。
186. @Concurrent
187. async function addImage(componentId: string, imagePathList: string[],
188. errcode: Map<number, string>): Promise<void> {
189. for (let index = 0; index < imagePathList.length; index++) {
190. const imagePath: string = imagePathList[index];
191. let file: fileIo.File;
192. try {
193. file = fileIo.openSync(imagePath, fileIo.OpenMode.READ_ONLY);
194. } catch (error) {
195. const err: BusinessError = error as BusinessError;
196. console.error(`Failed to open image. Code is ${err.code}, message is ${err.message}`);
197. this.addFailedImageCounts += 1;
198. continue
199. }
200. let imageName: string = file.name;
201. const imageSourceApi: image.ImageSource = image.createImageSource(file.fd);
202. try {
203. fileIo.closeSync(file);
204. } catch (error) {
205. const err: BusinessError = error as BusinessError;
206. console.error(`Failed to closeSync. Code is ${err.code}, message is ${err.message}.`);
207. imageSourceApi.release();
208. continue;
209. }
210. const imageInfo: image.ImageInfo = imageSourceApi.getImageInfoSync();
211. if (!imageInfo) {
212. console.error(`Failed to obtain the image pixel map information.`);
213. imageSourceApi.release();
214. continue;
215. }
216. const opts: image.DecodingOptions = {
217. editable: true,
218. desiredPixelFormat: image.PixelMapFormat.RGBA_8888,
219. desiredSize: { width: imageInfo.size.width, height: imageInfo.size.height }
220. }
221. const pixelMap: image.PixelMap = imageSourceApi.createPixelMapSync(opts);
222. if (!pixelMap) {
223. console.error('Failed to create pixelMap.');
224. imageSourceApi.release();
225. continue;
226. }
227. const readBuffer: ArrayBuffer = new ArrayBuffer(pixelMap.getPixelBytesNumber());
228. await pixelMap.readPixelsToBuffer(readBuffer);
229. await pixelMap.release();

231. let result: number = arEngineDemo.initImage(componentId, imageInfo.size.width, imageInfo.size.height, readBuffer);
232. if (errcode.has(result) === false) {
233. console.error('Failed to add image, break.');
234. imageSourceApi.release();
235. break;
236. }
237. if (result !== 0) {
238. console.error(`Failed to Add image, reason is: ${errcode.get(result)}, imageName is: ${imageName}.`);
239. }
240. let eventData: emitter.EventData = {
241. data: {
242. 'addImageReason': result,
243. 'imageName': imageName,
244. }
245. }
246. emitter.emit('addImage', eventData);
247. imageSourceApi.release();
248. }
249. }
```

创建一个ARImageByDatabase.ets，用于加载本地数据库，加载相机预览画面，并定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARImageByDatabase.ets。
2. import { deviceInfo } from '@kit.BasicServicesKit';
3. import { resourceManager } from '@kit.LocalizationKit';
4. import arEngineDemo from 'libentry.so';

6. @Builder
7. export function ARImageByDatabaseBuilder() {
8. ARImageByDatabase();
9. }

11. @Component
12. struct ARImageByDatabase {
13. pageInfo: NavPathStack = new NavPathStack();
14. private isSurfaceDestroy: boolean = false;
15. private interval: number = -1;
16. private isUpdate: boolean = false;
17. private xComponentId = 'ARImage';
18. @State context: Context = this.getUIContext().getHostContext() as Context;
19. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
20. @State rotation: number = deviceInfo.deviceType === 'tablet' ? 3 : 0;
21. @State showPage: boolean = true;

23. build(): void {
24. NavDestination() {
25. RelativeContainer() {
26. XComponent({ id: this.xComponentId, type: XComponentType.SURFACE, libraryname: 'entry' })
27. .width('100%')
28. .height('100%')
29. .visibility(this.showPage ? Visibility.Visible : Visibility.None)
30. .alignRules({
31. center: { anchor: '__container__', align: VerticalAlign.Center },
32. middle: { anchor: '__container__', align: HorizontalAlign.Center }
33. })
34. .onLoad(() => {
35. console.info(`XComponent onLoad ${this.xComponentId}.`);
36. this.interval = setInterval(() => {
37. if (this.isUpdate) {
38. arEngineDemo.update(this.xComponentId);
39. }
40. }, 33) // 将帧率设置为30fps（每33毫秒刷新一次帧）。
41. })
42. .onDestroy(() => {
43. console.info(`XComponent onDestroy ${this.xComponentId}.`);
44. this.isSurfaceDestroy = true;
45. clearInterval(this.interval);
46. })
47. }
48. }
49. .onAppear(() => {
50. arEngineDemo.init(this.resMgr);
51. let config: Int32Array = new Int32Array([1, this.rotation]);
52. arEngineDemo.start(this.xComponentId, config);

54. arEngineDemo.setPath(this.xComponentId, this.context.filesDir);

56. let imageCountInDatabase: number = arEngineDemo.getImageCount(this.xComponentId);
57. console.info(`ImageCountInDatabase: ${imageCountInDatabase}.`);
58. if (imageCountInDatabase <= 0) {
59. this.ShowDialog('请添加有效图片');
60. }
61. })
62. .onWillDisappear(() => {
63. arEngineDemo.stop(this.xComponentId);
64. })
65. .onShown(() => {
66. this.isUpdate = true;
67. arEngineDemo.show(this.xComponentId);
68. })
69. .onHidden(() => {
70. this.isUpdate = false;
71. if (!this.isSurfaceDestroy) {
72. arEngineDemo.hide(this.xComponentId);
73. }
74. })
75. .onReady((context: NavDestinationContext) => {
76. this.pageInfo = context.pathStack;
77. })
78. .hideTitleBar(true)
79. .hideBackButton(true)
80. .hideToolBar(true)
81. }

83. ShowDialog(msg: string): void {
84. this.getUIContext().showAlertDialog({
85. title: '警告',
86. message: msg,
87. autoCancel: true,
88. alignment: DialogAlignment.Center,
89. offset: { dx: 0, dy: -20 },
90. gridCount: 3,
91. transition: TransitionEffect
92. .asymmetric(TransitionEffect.OPACITY
93. .animation({ duration: 1000, curve: Curve.Sharp })
94. .combine(TransitionEffect
95. .scale({ x: 1.5, y: 1.5 })
96. .animation({ duration: 1000, curve: Curve.Sharp })
97. ),
98. TransitionEffect.OPACITY.animation({ duration: 100, curve: Curve.Smooth })
99. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 })
100. .animation({ duration: 100, curve: Curve.Smooth })
101. )
102. ),
103. buttons: [{
104. enabled: true,
105. defaultFocus: true,
106. style: DialogButtonStyle.HIGHLIGHT,
107. value: '退出',
108. action: () => {
109. console.info('Callback when the second button is clicked.');
110. this.pageInfo.pop();
111. }
112. }]
113. })
114. }
115. }
```

配置路由进行页面间跳转，页面路由配置详细可查看[组件导航(Navigation) (推荐)](arkts-navigation-navigation.md)。

### 引入AR Engine

开发者可参考AR物体摆放章节的[引入AR Engine](arengine-c-arworld.md#引入ar-engine)。

### 创建AR会话

创建AR会话并配置ARType为图像跟踪。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置ARType为ARENGINE_TYPE_IMAGE
8. HMS_AREngine_ARConfig_SetARType(arSession, arConfig, ARENGINE_TYPE_IMAGE);
9. // 配置器设置给AR会话。
10. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### 创建跟踪图像数据库并添加图像

1.调用[HMS\_AREngine\_ARAugmentedImageDatabase\_Create](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_create)函数，创建跟踪图像数据库。

```
1. // 创建跟踪图像数据库
2. AREngine_ARAugmentedImageDatabase *mDataBase = nullptr;
3. HMS_AREngine_ARAugmentedImageDatabase_Create(&mDataBase);
```

2.调用[HMS\_AREngine\_ARAugmentedImageDatabase\_AddImage](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimagedatabase_addimage)函数，添加图像到数据库，将添加失败的结果保存在reason中。

```
1. // 添加图像到数据库
2. AREngine_ARAddAugmentedImageReason reason = ARENGINE_ADD_AUGMENTED_IMAGE_REASON_NONE;
3. AREngine_ARAugmentedImageSource image;
4. uint32_t outputIndex = 0;
5. // 通过输入的图片构造image,具体可参考示例代码
6. auto addRet = HMS_AREngine_ARAugmentedImageDatabase_AddImage(mDataBase, &image, &outputIndex, &reason);
```

### 识别环境中的可跟踪图像

调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有跟踪图像，并将结果存放在augmentList中。

```
1. AREngine_ARTrackableList *augmentList = nullptr;
2. HMS_AREngine_ARTrackableList_Create(arSession, &augmentList);
3. HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_AUGMENTED_IMAGE, augmentList);
```

### 获取环境中的可跟踪图像数量

调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取平面数量，结果存放在augmentSize中。

```
1. int32_t augmentSize = 0;
2. HMS_AREngine_ARTrackableList_GetSize(arSession, augmentList, &augmentSize);
```

应用环境中，可能存在0个、1个或多个可跟踪图像。

当augmentSize等于0时，表示当前环境中不存在可跟踪图像。

当augmentSize等于1时，表示当前环境中仅存在1个可跟踪图像。

当augmentSize大于1时，表示当前环境中存在多个可跟踪图像。

### 获取跟踪图像示例

当存在1个或多个跟踪图像时，可以依次遍历augmentList获取所有跟踪图像。

```
1. for (int i = 0; i < augmentSize; ++i) {
2. // 遍历所有可跟踪对象，根据应用进行处理。
3. }
```

对于第i个跟踪图像，创建并获取跟踪对象，并将其转化为跟踪图像对象[AREngine\_ARAugmentedImage](../harmonyos-references/arengine-capi-arengine.md#arengine_araugmentedimage)。

```
1. AREngine_ARTrackable *augment = nullptr;
2. HMS_AREngine_ARTrackableList_AcquireItem(arSession, augmentList, i, &augment);
3. AREngine_ARAugmentedImage *arImage = reinterpret_cast<AREngine_ARAugmentedImage*>(augment);
```

### 获取跟踪图像中心点在世界坐标系中的位姿信息

调用[HMS\_AREngine\_ARAugmentedImage\_GetCenterPose](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getcenterpose)函数，获取跟踪图像中心点的位姿信息，位姿信息可参考[获取设备位姿](arengine-c-get-pose.md)。

```
1. AREngine_ARPose *imagePose = nullptr;
2. HMS_AREngine_ARPose_Create(arSession, nullptr, 0, &imagePose);
3. HMS_AREngine_ARAugmentedImage_GetCenterPose(arSession, arImage, imagePose);
```

### 获取跟踪图像的宽度

调用[HMS\_AREngine\_ARAugmentedImage\_GetExtendX](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendx)函数，获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到X轴上的估计值。

```
1. float extent_x;
2. HMS_AREngine_ARAugmentedImage_GetExtendX(arSession, arImage, &extent_x);
```

调用[HMS\_AREngine\_ARAugmentedImage\_GetExtendZ](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_araugmentedimage_getextendz)函数，获取图像的中心点为坐标原点，物理图像的宽度（单位为米），得到Z轴上的估计值。

```
1. float extent_z;
2. HMS_AREngine_ARAugmentedImage_GetExtendZ(arSession, arImage, &extent_z);
```
