---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-video-player
title: 视频播放 (Video)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 媒体展示 > 视频播放 (Video)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e9b244d76c4725c4f7ca507c5e37c68ed38e383a2ec82aa56fe0c6a1d9e268de
---

Video组件用于播放视频文件并控制其播放状态，常用于短视频和应用内部视频的列表页面。当视频完整出现时会自动播放，用户点击视频区域则会暂停播放，同时显示播放进度条，通过拖动播放进度条指定视频播放到具体位置。具体用法请参考[Video](../harmonyos-references/ts-media-components-video.md)。

## 创建视频组件

Video通过调用接口来创建，接口调用形式如下：

Video(value: VideoOptions)

## 加载视频资源

Video组件支持加载本地视频和网络视频。具体的数据源配置请参考[VideoOptions对象说明](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)。

### 加载本地视频

* 普通本地视频。

  加载本地视频时，需在工程资源的rawfile目录中放置视频文件，如下图所示。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/6kDrvhIPQlOYQcI8tB3Syg/zh-cn_image_0000002552798214.png?HW-CC-KV=V1&HW-CC-Date=20260427T233936Z&HW-CC-Expire=86400&HW-CC-Sign=AEDC40C3D712839BA8C7A89D57CF721AE9C8AAB53EEA30639248CC5B18FC7AEF)

  再使用资源访问符$rawfile()引用视频资源。

  ```
  1. // xxx.ets
  2. // ···
  3. @Component
  4. export struct LocalVideo {
  5. private controller: VideoController = new VideoController();
  6. private previewUris: Resource = $r('app.media.preview');
  7. private innerResource: Resource = $rawfile('videoTest.mp4');

  9. build() {
  10. Column() {
  11. Video({
  12. src: this.innerResource,  // 设置视频源
  13. previewUri: this.previewUris, // 设置预览图
  14. controller: this.controller // 设置视频控制器，可以控制视频的播放状态
  15. })
  16. }
  17. }
  18. }
  ```

  [LocalVideo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/LocalVideo.ets#L16-L37)
* [Data Ability](dataability-overview.md)提供的视频路径带有dataability://前缀，使用时确保对应视频资源存在。

  ```
  1. // xxx.ets
  2. // ...
  3. @Component
  4. export struct LocalVideoTwo {
  5. private controller: VideoController = new VideoController();
  6. // $r('app.media.preview')需要替换为开发者所需的图像资源文件
  7. private previewUris: Resource = $r('app.media.preview');
  8. // $rawfile('videoTest.mp4')需要替换为开发者所需的影像资源文件
  9. private videoSrc: string = 'dataability://device_id/com.domainname.dataability.videodata/video/10';

  11. build() {
  12. Column() {
  13. Video({
  14. src: this.videoSrc,
  15. previewUri: this.previewUris,
  16. controller: this.controller
  17. })
  18. }
  19. }
  20. }
  ```

  [DataAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/DataAbility.ets#L16-L39)

### 加载沙箱路径视频

支持file://路径前缀的字符串，用于读取应用沙箱路径内的资源，需要确保应用沙箱目录路径下的文件存在并且有可读权限。

```
1. // xxx.ets
2. // ···
3. @Component
4. export struct Sandbox {
5. private controller: VideoController = new VideoController();
6. private videoSrc: string = 'file:///data/storage/el2/base/haps/entry/files/show.mp4';

8. build() {
9. Column() {
10. Video({
11. src: this.videoSrc,
12. controller: this.controller
13. })
14. }
15. }
16. }
```

[Sandbox.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/Sandbox.ets#L16-L36)

### 加载网络视频

加载网络视频时，需要申请ohos.permission.INTERNET权限，具体申请方式请参考[声明权限](declare-permissions.md)。此时，Video的src属性为网络视频的链接。

```
1. // xxx.ets
2. // ···
3. @Component
4. export struct OnlineVideo {
5. private controller: VideoController = new VideoController();
6. private previewUris: Resource = $r('app.media.preview');
7. private videoSrc: string = 'www.example.com/example.mp4'; // 使用时请替换为实际视频加载网址

9. build() {
10. Column() {
11. Video({
12. src: this.videoSrc,
13. previewUri: this.previewUris,
14. controller: this.controller
15. })
16. }
17. }
18. }
```

[OnlineVideo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/OnlineVideo.ets#L16-L39)

## 添加属性

Video组件[属性](../harmonyos-references/ts-media-components-video.md#属性)主要用于设置视频的播放形式。例如设置视频播放是否静音、播放是否显示控制条等。

```
1. // xxx.ets
2. // ···
3. @Component
4. export struct AttributeVideo {
5. private controller: VideoController = new VideoController();

7. build() {
8. Column() {
9. Video({
10. controller: this.controller
11. })
12. .muted(false) // 设置是否静音
13. .controls(false) // 设置是否显示默认控制条
14. .autoPlay(false) // 设置是否自动播放
15. .loop(false) // 设置是否循环播放
16. .objectFit(ImageFit.Contain) // 设置视频填充模式
17. }
18. }
19. }
```

[AttributeVideo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/AttributeVideo.ets#L16-L41)

## 事件调用

Video组件回调事件主要包括播放开始、播放暂停、播放结束、播放失败、播放停止、视频准备和操作进度条等事件，除此之外，Video组件也支持通用事件的调用，如点击、触摸等事件的调用。详细事件请参考[事件说明](../harmonyos-references/ts-media-components-video.md#事件)。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct EventCall {
5. private controller: VideoController = new VideoController();
6. private previewUris: Resource = $r('app.media.preview');
7. private innerResource: Resource = $rawfile('videoTest.mp4');

9. build() {
10. Column() {
11. Video({
12. src: this.innerResource,
13. previewUri: this.previewUris,
14. controller: this.controller
15. })
16. .onUpdate((event) => { // 更新事件回调
17. })
18. .onPrepared((event) => { // 准备事件回调
19. })
20. .onError(() => { // 失败事件回调
21. })
22. .onStop(() => { // 停止事件回调
23. })
24. }
25. }
26. }
```

[EventCall.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/EventCall.ets#L16-L43)

## Video控制器使用

Video控制器主要用于控制视频的状态，包括播放、暂停、停止以及设置进度等，详细使用请参考[VideoController使用说明](../harmonyos-references/ts-media-components-video.md#videocontroller)。

* 默认控制器

  默认的控制器支持视频的开始、暂停、进度调整、全屏显示四项基本功能。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct VideoGuide {
  5. @State videoSrc: Resource = $rawfile('videoTest.mp4');
  6. @State previewUri: string = 'common/videoIcon.png';
  7. @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;

  9. build() {
  10. Row() {
  11. Column() {
  12. Video({
  13. src: this.videoSrc,
  14. previewUri: this.previewUri,
  15. currentProgressRate: this.curRate // 设置视频播放倍速
  16. })
  17. }
  18. .width('100%')
  19. }
  20. .height('100%')
  21. }
  22. }
  ```

  [VideoControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/VideoControl.ets#L16-L39)
* 自定义控制器

  使用自定义的控制器，先关闭默认控制器，然后使用[Button](../harmonyos-references/ts-basic-components-button.md)以及[Slider](../harmonyos-references/ts-basic-components-slider.md)等组件进行自定义的控制与显示，适合自定义较强的场景下使用。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct CustomizedControl {
  5. @State videoSrc: Resource = $rawfile('videoTest.mp4');
  6. @State previewUri: string = 'common/videoIcon.png';
  7. @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  8. // 初始化当前时间为0
  9. @State currentTime: number = 0;
  10. // 初始化持续时间为0
  11. @State durationTime: number = 0;
  12. controller: VideoController = new VideoController();

  14. build() {
  15. Row() {
  16. Column() {
  17. Video({
  18. src: this.videoSrc,
  19. previewUri: this.previewUri,
  20. currentProgressRate: this.curRate,
  21. controller: this.controller
  22. })
  23. .controls(false)
  24. .autoPlay(true)
  25. .onPrepared((event) => {
  26. if (event) {
  27. this.durationTime = event.duration
  28. }
  29. })
  30. .onUpdate((event) => {
  31. if (event) {
  32. this.currentTime = event.time
  33. }
  34. })
  35. Row() {
  36. Text(JSON.stringify(this.currentTime) + 's')
  37. Slider({
  38. value: this.currentTime,
  39. min: 0,
  40. max: this.durationTime
  41. })
  42. .onChange((value: number, mode: SliderChangeMode) => {
  43. this.controller.setCurrentTime(value); // 设置视频播放的进度跳转到value处
  44. })
  45. .width('90%')
  46. Text(JSON.stringify(this.durationTime) + 's')
  47. }
  48. .opacity(0.8)
  49. .width('100%')
  50. }
  51. .width('100%')
  52. }
  53. .height('40%')
  54. }
  55. }
  ```

  [CustomizedControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/VideoPlayer/entry/src/main/ets/pages/CustomizedControl.ets#L16-L72)

## 其他说明

Video组件已经封装好了视频播放的基础能力，开发者无需进行视频实例的创建，视频信息的设置获取，只需要设置数据源以及基础信息即可播放视频，相对扩展能力较弱。如果开发者想自定义视频播放，请使用[AVPlayer](media-kit-intro.md#avplayer)，下面是一个使用AVPlayer进行播放视频的简单示例，如果需要更详细信息或更复杂功能请参考[视频播放](video-playback.md)。

```
1. // xxx.ets
2. import { window } from '@kit.ArkUI';
3. import { AVPlayerController } from '../avplayertool/AVPlayerController';
4. import { emitter } from '@kit.BasicServicesKit';
5. import { CommonConstants, VideoDataType } from  '../common/constants/CommonConstants';
6. import { VideoData } from '../model/VideoData'
7. import { common } from '@kit.AbilityKit'

9. class VideoXComponentController extends XComponentController {
10. private avPlayerController: AVPlayerController;

12. constructor(avPlayerController: AVPlayerController) {
13. super();
14. this.avPlayerController = avPlayerController;
15. }

17. onSurfaceCreated(surfaceId: string): void {
18. let source: VideoData = {
19. type: VideoDataType.RAW_FILE,
20. videoSrc: 'videoTest.mp4'
21. };
22. // 将surfaceId和视频源信息传递给AVPlayer
23. this.avPlayerController.initAVPlayer(source, surfaceId);
24. }
25. }

27. const MINUTE_UNIT = 60000;
28. const SECOND_UNIT = 1000;
29. const SECOND_TEN = 10;
30. function timeCover(time: number): string {
31. let min: number = Math.floor(time / MINUTE_UNIT);
32. let second: string = ((time % MINUTE_UNIT) / SECOND_UNIT).toFixed(0);
33. return `${min}:${(Number(second) < SECOND_TEN ? '0' : '') + second}`;
34. }

36. @Entry
37. @Component
38. struct XComponentAVPlayer {
39. // 设置视频控制器，可以控制视频的播放状态。
40. @State avPlayerController: AVPlayerController = new AVPlayerController(this.getUIContext().getHostContext()!);
41. // 视频的总时长。
42. @State durationTime: number = 0;
43. // 视频当前进度。
44. @State currentTime: number = 0;
45. // 判断视频是否暂停播放。
46. @State isPause: boolean = true;
47. // 判断视频是否全屏播放。
48. @State isLayoutFullScreen: boolean = false;
49. // 设置XComponent组件控制器。
50. private videoXComponentController: XComponentController = new VideoXComponentController(this.avPlayerController);
51. // 判断窗口是否横屏。
52. @State isLandScape: boolean = false;
53. // 系统导航栏的标识。
54. private WINDOW_SYSTEM_BAR: Array<'status' | 'navigation'> = ['navigation', 'status'];
55. // 窗口宽度。
56. @State windowWidth:number = 0;
57. // 窗口高度。
58. @State windowHeight: number = 0;
59. // 窗口实例。
60. private windowClass: window.Window | null = null;

62. // 获取窗口实例。
63. getWindow(): window.Window {
64. const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
65. return context.windowStage!.getMainWindowSync();
66. }

68. aboutToAppear(): void {
69. this.windowClass = this.getWindow();
70. let properties = this.windowClass.getWindowProperties();
71. let context = this.getUIContext();
72. this.windowWidth = context.px2vp(properties.windowRect.width);
73. this.windowHeight = context.px2vp(properties.windowRect.height);
74. // 获取窗口横竖屏状态及其尺寸。
75. this.windowClass.on('windowSizeChange', (size: window.Size) => {
76. this.isLandScape = size.width > size.height;
77. this.windowWidth = context.px2vp(size.width);
78. this.windowHeight = context.px2vp(size.height);
79. })
80. emitter.on(CommonConstants.AVPLAYER_PREPARED, (res) => {
81. if (res.data) {
82. this.durationTime = this.avPlayerController.durationTime;
83. // 更新视频进度时间。
84. setInterval(() => {
85. this.currentTime = this.avPlayerController.currentTime;
86. }, 1000);
87. }
88. });
89. }

91. // 设置沉浸式窗口。
92. setFullScreen(isLayoutFullScreen: boolean) {
93. window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
94. if (isLayoutFullScreen) {
95. // 设置窗口全屏模式时导航栏、状态栏的可见模式。
96. win.setWindowSystemBarEnable([]);
97. } else {
98. // 设置窗口非全屏模式时导航栏、状态栏的可见模式。
99. win.setWindowSystemBarEnable(this.WINDOW_SYSTEM_BAR);
100. }
101. }).catch((err: string) => {
102. console.error(`setFullScreen failed, message is ${err}`);
103. });
104. }

106. build() {
107. Column() {
108. Stack() {
109. XComponent({ type: XComponentType.SURFACE, controller: this.videoXComponentController })
110. Column() {
111. Blank()
112. Column() {
113. Column() {
114. Row() {
115. Row() {
116. // 设置视频播放或暂停的按钮。
117. SymbolGlyph(this.isPause ? $r('sys.symbol.pause') : $r('sys.symbol.play_fill'))
118. .fontSize(30)
119. .fontWeight(FontWeight.Bolder)
120. .fontColor([Color.White])
121. .onClick(() => {
122. if (this.isPause) {
123. this.avPlayerController.videoPause();
124. } else {
125. this.avPlayerController.videoPlay();
126. }
127. this.isPause = !this.isPause;
128. })
129. // 视频当前进度。
130. Text(timeCover(this.currentTime))
131. .fontColor(Color.White)
132. .textAlign(TextAlign.End)
133. .fontWeight(FontWeight.Regular)
134. .margin({ left: 5 })
135. }
136. Row() {
137. // 视频进度条。
138. Slider({
139. value: this.currentTime,
140. min: 0,
141. max: this.durationTime,
142. style: SliderStyle.OutSet
143. })
144. .id('Slider')
145. .blockColor(Color.White)
146. .trackColor(Color.Gray)
147. .selectedColor('#317af7')
148. .showTips(false)
149. .onChange((value: number, mode: SliderChangeMode) => {
150. if (mode === SliderChangeMode.Begin) {
151. this.avPlayerController.videoPause();
152. }
153. this.avPlayerController.videoSeek(value);
154. this.currentTime = value;
155. if (mode === SliderChangeMode.End) {
156. this.isPause = true;
157. this.avPlayerController.videoPlay();
158. }
159. })
160. }
161. .layoutWeight(1)
162. Row() {
163. // 视频的总时长。
164. Text(timeCover(this.durationTime))
165. .fontColor(Color.White)
166. .fontWeight(FontWeight.Regular)
167. .margin({ right: 5 })
168. }
169. Row() {
170. // 设置是否全屏播放的按钮。
171. SymbolGlyph(this.isLayoutFullScreen ? $r('sys.symbol.arrow_down_right_and_arrow_up_left') : $r('sys.symbol.arrow_up_left_and_arrow_down_right'))
172. .fontSize(30)
173. .fontWeight(FontWeight.Bolder)
174. .fontColor([Color.White])
175. .onClick(()=> {
176. this.isLayoutFullScreen = !this.isLayoutFullScreen;
177. this.setFullScreen(this.isLayoutFullScreen);
178. })
179. }
180. }
181. .justifyContent(FlexAlign.Center)
182. .padding({ left: 12, right: 20, bottom: 28 })
183. .width('100%')
184. }
185. .backgroundColor(Color.Black)
186. }
187. .justifyContent(FlexAlign.Center)
188. }
189. .width('100%')
190. .height('100%')
191. }
192. .height(this.isLayoutFullScreen ? this.windowHeight : 300)
193. .width(this.isLayoutFullScreen ? this.windowWidth : 300)
194. }
195. .width('100%')
196. .height('100%')
197. .justifyContent(FlexAlign.Center)
198. .alignItems(HorizontalAlign.Center)
199. }
200. }
```

## 示例代码

* [媒体库视频](https://gitcode.com/harmonyos_samples/video-show)
