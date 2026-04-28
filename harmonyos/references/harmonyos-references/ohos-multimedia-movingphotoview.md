---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-movingphotoview
title: @ohos.multimedia.movingphotoview (动态照片)
breadcrumb: API参考 > 媒体 > Media Library Kit（媒体文件管理服务） > ArkTS组件 > @ohos.multimedia.movingphotoview (动态照片)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:19+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:f304ad1cec5661d53e0a300a2e17d28cd57b1881e75aadd07811647d51203299
---

用于播放动态照片文件并控制其播放状态的组件。

说明

该组件从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

当前不支持在预览器中使用MovingPhotoView组件。

## 导入模块

PhonePC/2in1TabletTV

说明

* MovingPhotoViewAttribute是用于配置MovingPhotoView组件属性的关键接口。API version 21及之前版本，导入MovingPhotoView组件后需要开发者手动导入MovingPhotoViewAttribute，否则会编译报错。从API version 22开始，编译工具链识别到导入MovingPhotoView组件后，会自动导入MovingPhotoViewAttribute，无需开发者手动导入。
* 如果开发者手动导入MovingPhotoViewAttribute，DevEco Studio会将其显示置灰，API version 21及之前版本删除会编译报错，从API version 22开始，删除对功能无影响。

API version 21及之前版本：

```
1. import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
```

API version 22及之后版本：

```
1. import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';
```

## MovingPhotoView

PhonePC/2in1TabletTV

说明

* 当前不支持动态属性设置。
* 当前不支持ArkUI通用属性ComponentOptions中expandSafeArea属性设置。
* 该组件长按触发播放时组件区域放大为1.1倍。
* 该组件使用[AVPlayer](arkts-apis-media-avplayer.md)进行播放，同时开启的AVPlayer个数不建议超过3个，超过3个可能会出现视频播放卡顿现象。

MovingPhotoView(options: MovingPhotoViewOptions)

**参数：**

| 参数名 | 参数类型 | 必填 | 参数描述 |
| --- | --- | --- | --- |
| options | [MovingPhotoViewOptions](ohos-multimedia-movingphotoview.md#movingphotoviewoptions) | 是 | 动态照片信息。 |

## MovingPhotoViewOptions

PhonePC/2in1TabletTV

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| movingPhoto | [photoAccessHelper.MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md) | 否 | 否 | 支持媒体库MovingPhoto数据源，具体信息详见[MovingPhoto](arkts-apis-photoaccesshelper-movingphoto.md)说明。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| controller | [MovingPhotoViewController](ohos-multimedia-movingphotoview.md#movingphotoviewcontroller) | 否 | 是 | 设置动态照片控制器，可以控制动态照片的播放状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| imageAIOptions18+ | [ImageAIOptions](ts-image-common.md#imageaioptions12) | 否 | 是 | 设置动态照片AI分析选项，可配置分析类型或绑定一个分析控制器。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTV

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### muted

PhonePC/2in1TabletTV

muted(isMuted: boolean)

设置是否静音。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isMuted | boolean | 是 | 是否静音。  默认值：false。  false：非静音。  true：静音。 |

### objectFit

PhonePC/2in1TabletTV

objectFit(value: ImageFit)

设置动态照片显示模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](ts-appendix-enums.md#imagefit) | 是 | 视频显示模式。  默认值：Cover。 |

### autoPlayPeriod13+

PhonePC/2in1TabletTV

autoPlayPeriod(startTime: number, endTime: number)

设置自动播放区间，附属于autoPlay的子配置项。

在调用此方法前，需将[autoPlay](ohos-multimedia-movingphotoview.md#autoplay13)设置为true，设置自动播放，否则指定的视频区间(startTime, endTime)无法生效。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startTime | number | 是 | 区间播放开始时间，单位：ms。  取值范围：大于等于0。 |
| endTime | number | 是 | 区间播放结束时间，单位：ms。  取值范围：大于startTime。 |

### autoPlay13+

PhonePC/2in1TabletTV

autoPlay(isAutoPlay: boolean)

设置自动播放，自动播放一遍视频。

动态照片加载完成后，准备播放时可以调用，播放完成后显示静态图。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAutoPlay | boolean | 是 | 是否自动播放。  false：不自动播放。  true：自动播放。  默认值：false。 |

### repeatPlay13+

PhonePC/2in1TabletTV

repeatPlay(isRepeatPlay: boolean)

设置循环播放，重复播放视频。 repeatPlay与autoPlay及长按播放互斥，repeatPlay设置时，autoPlay和长按播放均不生效。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isRepeatPlay | boolean | 是 | 是否循环播放。  false：不循环播放。  true：循环播放。  默认值：false。 |

### enableAnalyzer18+

PhonePC/2in1TabletTV

enableAnalyzer(enabled: boolean)

设置该图片是否支持AI分析，当前支持主体识别、文字识别和对象查找等功能。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 是否开启AI分析。  false：不开启AI分析。  true：开启AI分析。  默认值：true。 |

## 事件

PhonePC/2in1TabletTV

除支持[通用事件](ts-component-general-events.md)外，还支持以下事件：

### onComplete13+

PhonePC/2in1TabletTV

onComplete(callback: MovingPhotoViewEventCallback)

动态照片加载完成图片时触发该事件。使用callback异步回调。

**元服务API：** 从API version 13开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片加载完成图片的回调。 |

### onStart

PhonePC/2in1TabletTV

onStart(callback: MovingPhotoViewEventCallback)

播放时触发该事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片开始播放时触发的回调。 |

### onPause

PhonePC/2in1TabletTV

onPause(callback: MovingPhotoViewEventCallback)

播放暂停时触发该事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片播放暂停时触发的回调。 |

### onFinish

PhonePC/2in1TabletTV

onFinish(callback: MovingPhotoViewEventCallback)

播放结束时触发该事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片播放结束时触发的回调。 |

### onError

PhonePC/2in1TabletTV

onError(callback: MovingPhotoViewEventCallback)

播放失败时触发该事件。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片播放失败时触发的回调。 |

### onStop

PhonePC/2in1TabletTV

onStop(callback: MovingPhotoViewEventCallback)

播放停止时触发该事件(当stop()方法被调用后触发)。使用callback异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片停止播放时触发的回调。 |

### onPrepared20+

PhonePC/2in1TabletTV

onPrepared(callback: MovingPhotoViewEventCallback)

动态照片准备播放时触发该事件。使用callback异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MovingPhotoViewEventCallback](ohos-multimedia-movingphotoview.md#movingphotovieweventcallback) | 是 | 动态照片准备播放时的回调。 |

## MovingPhotoViewEventCallback

PhonePC/2in1TabletTV

declare type MovingPhotoViewEventCallback = () => void

动态照片播放状态发生变化时触发的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## MovingPhotoViewController

PhonePC/2in1TabletTV

一个MovingPhotoViewController对象可以控制一个MovingPhotoView，可用视频播放实例请参考[@ohos.multimedia.media](arkts-apis-media.md)。

### constructor

PhonePC/2in1TabletTV

constructor()

MovingPhotoViewController的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

### startPlayback

PhonePC/2in1TabletTV

startPlayback()

开始播放，动态照片加载完成后，在播放准备，暂停，完成时调用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

### stopPlayback

PhonePC/2in1TabletTV

stopPlayback()

停止播放，再次播放时从头开始播放。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

### refreshMovingPhoto18+

PhonePC/2in1TabletTV

refreshMovingPhoto()

强制刷新动态照片组件加载的视频和图片资源，会打断组件当前的行为，使用时要谨慎。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 示例1：多种形式播放动态照片

PhonePC/2in1TabletTV

```
1. // xxx.ets
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { emitter } from '@kit.BasicServicesKit';
4. import { dataSharePredicates } from '@kit.ArkData';
5. // API version 21及之前版本导入方式：import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
6. // API version 22及之后版本导入方式如下：
7. import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

9. const PHOTO_SELECT_EVENT_ID: number = 80001

11. @Entry
12. @Component
13. struct MovingPhotoViewDemo {
14. @State src: photoAccessHelper.MovingPhoto | undefined = undefined
15. @State isMuted: boolean = false
16. controller: MovingPhotoViewController = new MovingPhotoViewController()
17. private uiContext: UIContext = this.getUIContext()

19. aboutToAppear(): void {
20. emitter.on({
21. eventId: PHOTO_SELECT_EVENT_ID,
22. priority: emitter.EventPriority.IMMEDIATE,
23. }, (eventData: emitter.EventData) => {
24. this.src = AppStorage.get<photoAccessHelper.MovingPhoto>('mv_data') as photoAccessHelper.MovingPhoto
25. })
26. }

28. aboutToDisappear(): void {
29. emitter.off(PHOTO_SELECT_EVENT_ID)
30. }

32. build() {
33. Column() {
34. Row() {
35. Button('PICK')
36. .margin(5)
37. .onClick(async () => {
38. try {
39. let uris: Array<string> = []
40. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions()
41. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE
42. photoSelectOptions.maxSelectNumber = 2
43. const photoViewPicker = new photoAccessHelper.PhotoViewPicker()
44. let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoViewPicker.select(photoSelectOptions)
45. uris = photoSelectResult.photoUris
46. if (uris[0]) {
47. this.handlePickerResult(this.uiContext.getHostContext()!, uris[0], new MediaDataHandlerMovingPhoto())
48. }
49. } catch (e) {
50. console.error(`pick file failed`)
51. }
52. })
53. }
54. .alignItems(VerticalAlign.Center)
55. .justifyContent(FlexAlign.Center)
56. .height('15%')

58. Row() {
59. Column() {
60. MovingPhotoView({
61. movingPhoto: this.src,
62. controller: this.controller
63. })
64. .width('100%')
65. .height('100%')
66. .muted(this.isMuted)
67. .autoPlay(true)
68. .repeatPlay(false)
69. .autoPlayPeriod(0, 600)
70. .objectFit(ImageFit.Cover)
71. .onComplete(() => {
72. console.info('Completed');
73. })
74. .onStart(() => {
75. console.info('onStart')
76. })
77. .onFinish(() => {
78. console.info('onFinish')
79. })
80. .onStop(() => {
81. console.info('onStop')
82. })
83. .onError(() => {
84. console.error('onError')
85. })
86. }
87. }
88. .height('70%')

90. Row() {
91. Button('start')
92. .onClick(() => {
93. this.controller.startPlayback()
94. })
95. .margin(5)
96. Button('stop')
97. .onClick(() => {
98. this.controller.stopPlayback()
99. })
100. .margin(5)
101. Button('mute')
102. .onClick(() => {
103. this.isMuted = !this.isMuted
104. })
105. .margin(5)
106. }
107. .alignItems(VerticalAlign.Center)
108. .justifyContent(FlexAlign.Center)
109. .height('15%')
110. }
111. }

113. async handlePickerResult(context: Context, uri: string, handler: photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto>): Promise<void> {
114. let uriPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
115. uriPredicates.equalTo('uri', uri)
116. let fetchOptions: photoAccessHelper.FetchOptions = {
117. fetchColumns: [],
118. predicates: uriPredicates
119. };
120. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context)
121. let assetResult = await phAccessHelper.getAssets(fetchOptions)
122. let asset = await assetResult.getFirstObject()
123. let requestOptions: photoAccessHelper.RequestOptions = {
124. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
125. }
126. try {
127. photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler)
128. } catch (err) {
129. console.error("request error: ", err)
130. }
131. }
132. }

134. class MediaDataHandlerMovingPhoto implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
135. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
136. AppStorage.setOrCreate('mv_data', movingPhoto)
137. emitter.emit({
138. eventId: PHOTO_SELECT_EVENT_ID,
139. priority: emitter.EventPriority.IMMEDIATE,
140. }, {
141. })
142. }
143. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/GuLLxJqUR5e2vi1ViLpI6Q/zh-cn_image_0000002583440901.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001418Z&HW-CC-Expire=86400&HW-CC-Sign=E55479DE9724EDD4C01774D795D3EE0D5C230D4B14CE837D9E3B84BE34D6EE4A)

## 示例2：在元服务中使用动态照片

PhonePC/2in1TabletTV

```
1. // xxx.ets
2. // API version 21及之前版本导入方式：import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
3. // API version 22及之后版本导入方式如下：
4. import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';

6. let data: photoAccessHelper.MovingPhoto
7. async function loading(context: Context) {
8. try {
9. // 需要确保imageFileUri和videoFileUri对应的资源在应用沙箱存在。
10. let imageFileUri = 'file://{bundleName}/data/storage/el2/base/haps/entry/files/xxx.jpg';
11. let videoFileUri = 'file://{bundleName}/data/storage/el2/base/haps/entry/files/xxx.mp4';
12. data = await photoAccessHelper.MediaAssetManager.loadMovingPhoto(context, imageFileUri, videoFileUri);
13. console.info('load moving photo successfully');
14. } catch (err) {
15. console.error(`load moving photo failed with error: ${err.code}, ${err.message}`);
16. }
17. }
18. @Entry
19. @Component
20. struct Index {
21. controller: MovingPhotoViewController = new MovingPhotoViewController()
22. private uiContext: UIContext = this.getUIContext()
23. @State ImageFit: ImageFit | undefined | null = ImageFit.Contain;
24. @State flag: boolean = true;
25. @State autoPlayFlag: boolean = true;
26. @State repeatPlayFlag: boolean = false;
27. @State autoPlayPeriodStart: number = 0;
28. @State autoPlayPeriodEnd: number = 500;
29. aboutToAppear(): void {
30. loading(this.uiContext.getHostContext()!)
31. }

33. build() {
34. NavDestination() {
35. Column() {
36. Stack({ alignContent: Alignment.BottomStart }) {
37. MovingPhotoView({
38. movingPhoto: data,
39. controller: this.controller
40. })
41. .width(300)
42. .height(400)
43. .muted(this.flag)
44. .objectFit(this.ImageFit)
45. .autoPlay(this.autoPlayFlag)
46. .autoPlayPeriod(this.autoPlayPeriodStart, this.autoPlayPeriodEnd)
47. .repeatPlay(this.repeatPlayFlag)
48. .onComplete(() => {
49. console.info('onComplete')
50. })
51. .onStart(() => {
52. console.info('onStart')
53. })
54. .onStop(() => {
55. console.info('onStop')
56. })
57. .onPause(() => {
58. console.info('onPause')
59. })
60. .onFinish(() => {
61. console.info('onFinish')
62. })
63. .onError(() => {
64. console.info('onError')
65. })
66. }

68. Row() {
69. Button('Play')
70. .onClick(() => {
71. this.controller.startPlayback()
72. })
73. Button('StopPlay')
74. .onClick(() => {
75. this.controller.stopPlayback()
76. })
77. Button('refreshMovingPhoto')
78. .onClick(() => {
79. this.controller.refreshMovingPhoto()
80. })
81. Button('mute').id('MovingPhotoView_true')
82. .onClick(() => {
83. this.flag = false
84. })
85. }
86. }
87. }
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Oz9TCtupS12rxMCZuwGHQw/zh-cn_image_0000002552960856.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001418Z&HW-CC-Expire=86400&HW-CC-Sign=5B5E6D62598C69B73E220CF74C4AA7C1E79C3A4A58CBC86003C5E3172E41AB84)

## 示例3：图像分析功能使用

PhonePC/2in1TabletTV

```
1. // xxx.ets
2. import { photoAccessHelper } from '@kit.MediaLibraryKit';
3. import { emitter } from '@kit.BasicServicesKit';
4. import { dataSharePredicates } from '@kit.ArkData';
5. import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
6. import { visionImageAnalyzer } from '@kit.VisionKit';
7. const PHOTO_SELECT_EVENT_ID: number = 80001

9. @Entry
10. @Component
11. struct MovingPhotoViewDemo {
12. @State src: photoAccessHelper.MovingPhoto | undefined = undefined
13. @State isMuted: boolean = false
14. controller: MovingPhotoViewController = new MovingPhotoViewController()
15. private aiController: visionImageAnalyzer.VisionImageAnalyzerController =
16. new visionImageAnalyzer.VisionImageAnalyzerController()
17. private options: ImageAIOptions = {
18. types: [ImageAnalyzerType.SUBJECT, ImageAnalyzerType.TEXT, ImageAnalyzerType.OBJECT_LOOKUP],
19. aiController: this.aiController
20. }
21. private uiContext: UIContext = this.getUIContext()

23. aboutToAppear(): void {
24. emitter.on({
25. eventId: PHOTO_SELECT_EVENT_ID,
26. priority: emitter.EventPriority.IMMEDIATE,
27. }, (eventData: emitter.EventData) => {
28. this.src = AppStorage.get<photoAccessHelper.MovingPhoto>('mv_data') as photoAccessHelper.MovingPhoto
29. })
30. }

32. aboutToDisappear(): void {
33. emitter.off(PHOTO_SELECT_EVENT_ID)
34. }

36. build() {
37. Column() {
38. Row() {
39. Button('PICK')
40. .margin(5)
41. .onClick(async () => {
42. try {
43. let uris: Array<string> = []
44. const photoSelectOptions = new photoAccessHelper.PhotoSelectOptions()
45. photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE_VIDEO_TYPE
46. photoSelectOptions.maxSelectNumber = 2
47. const photoViewPicker = new photoAccessHelper.PhotoViewPicker()
48. let photoSelectResult: photoAccessHelper.PhotoSelectResult = await photoViewPicker.select(photoSelectOptions)
49. uris = photoSelectResult.photoUris
50. if (uris[0]) {
51. this.handlePickerResult(this.uiContext.getHostContext()!, uris[0], new MediaDataHandlerMovingPhoto())
52. }
53. } catch (e) {
54. console.error(`pick file failed`)
55. }
56. })
57. }
58. .alignItems(VerticalAlign.Center)
59. .justifyContent(FlexAlign.Center)
60. .height('15%')

62. Row() {
63. Column() {
64. MovingPhotoView({
65. movingPhoto: this.src,
66. controller: this.controller,
67. imageAIOptions: this.options
68. })
69. .width('100%')
70. .height('100%')
71. .muted(this.isMuted)
72. .autoPlay(true)
73. .repeatPlay(false)
74. .autoPlayPeriod(0, 600)
75. .objectFit(ImageFit.Cover)
76. .enableAnalyzer(true)
77. .onComplete(() => {
78. console.log('Completed');
79. })
80. .onStart(() => {
81. console.log('onStart')
82. })
83. .onFinish(() => {
84. console.log('onFinish')
85. })
86. .onStop(() => {
87. console.log('onStop')
88. })
89. .onError(() => {
90. console.log('onError')
91. })
92. }
93. }
94. .height('70%')

96. Row() {
97. Button('start')
98. .onClick(() => {
99. this.controller.startPlayback()
100. })
101. .margin(5)
102. Button('stop')
103. .onClick(() => {
104. this.controller.stopPlayback()
105. })
106. .margin(5)
107. Button('mute')
108. .onClick(() => {
109. this.isMuted = !this.isMuted
110. })
111. .margin(5)
112. }
113. .alignItems(VerticalAlign.Center)
114. .justifyContent(FlexAlign.Center)
115. .height('15%')
116. }
117. }

119. async handlePickerResult(context: Context, uri: string, handler: photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto>): Promise<void> {
120. let uriPredicates: dataSharePredicates.DataSharePredicates = new dataSharePredicates.DataSharePredicates();
121. uriPredicates.equalTo('uri', uri)
122. let fetchOptions: photoAccessHelper.FetchOptions = {
123. fetchColumns: [],
124. predicates: uriPredicates
125. };
126. let phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context)
127. let assetResult = await phAccessHelper.getAssets(fetchOptions)
128. let asset = await assetResult.getFirstObject()
129. let requestOptions: photoAccessHelper.RequestOptions = {
130. deliveryMode: photoAccessHelper.DeliveryMode.FAST_MODE,
131. }
132. try {
133. photoAccessHelper.MediaAssetManager.requestMovingPhoto(context, asset, requestOptions, handler)
134. } catch (err) {
135. console.error("request error: ", err)
136. }
137. }
138. }

140. class MediaDataHandlerMovingPhoto implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
141. async onDataPrepared(movingPhoto: photoAccessHelper.MovingPhoto) {
142. AppStorage.setOrCreate('mv_data', movingPhoto)
143. emitter.emit({
144. eventId: PHOTO_SELECT_EVENT_ID,
145. priority: emitter.EventPriority.IMMEDIATE,
146. }, {
147. })
148. }
149. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/G-U4WPc1TuuCl8b4k00fuw/zh-cn_image_0000002583480857.gif?HW-CC-KV=V1&HW-CC-Date=20260428T001418Z&HW-CC-Expire=86400&HW-CC-Sign=D75EF25EDB5DFE00E5697E13187F50E15763C9869870A8091AA17C7B1C239A12)
