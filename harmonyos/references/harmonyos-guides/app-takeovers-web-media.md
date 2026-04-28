---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-takeovers-web-media
title: 托管网页中的媒体播放
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用网页多媒体 > 托管网页中的媒体播放
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9375cfcd5aca69da8411fe752b1991738d875672e618b1dbedac282714a4aa98
---

Web组件提供了应用接管网页中媒体播放的能力，用来支持应用增强网页的媒体播放，如画质增强等。

## 使用场景

网页播放媒体时，存在以下问题：网页清晰度低、网页播放器播放控件功能有限、某些视频无法播放。

应用开发者可以使用该功能，通过自己或者第三方播放器接管网页媒体播放，从而改善播放体验。

## 实现原理

### ArkWeb内核播放媒体的框架

不开启该功能时，ArkWeb内核的播放架构如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/GuTVthKOQxa-KpCtfeZWsQ/zh-cn_image_0000002583478231.png?HW-CC-KV=V1&HW-CC-Date=20260427T234102Z&HW-CC-Expire=86400&HW-CC-Sign=166D57D7A3D365FE56CD4A684D8A254143E8F7D0A043818C2475BA7916F84F7C)

说明

* 上图中1表示ArkWeb内核创建WebMediaPlayer来播放网页中的媒体资源。
* 上图中2表示WebMediaPlayer使用系统解码器来渲染媒体数据。

开启该功能后，ArkWeb内核的播放架构如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/ei95ykqjRAeALr7FVyFLMw/zh-cn_image_0000002552798582.png?HW-CC-KV=V1&HW-CC-Date=20260427T234102Z&HW-CC-Expire=86400&HW-CC-Sign=37CAD90DFBD5BB70502C59A781CB5170653E0A3908DD2954B904F2F6D364D1ED)

说明

* 上图中1表示ArkWeb内核创建WebMediaPlayer来播放网页中的媒体资源。
* 上图中2表示WebMediaPlayer使用应用提供的本地播放器（NativeMediaPlayer）来渲染媒体数据。

### ArkWeb内核与应用的交互

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/qyiFEz2eSLuRFVWSS35bOw/zh-cn_image_0000002583438277.png?HW-CC-KV=V1&HW-CC-Date=20260427T234102Z&HW-CC-Expire=86400&HW-CC-Sign=C318C107C61D6E3EC6DC7D7E49127776A0FD995CF93AE024061830B5091E985F)

说明

* 上图中1的详细说明见[开启接管网页媒体播放](app-takeovers-web-media.md#开启接管网页媒体播放)。
* 上图中2的详细说明见[创建本地播放器](app-takeovers-web-media.md#创建本地播放器nativemediaplayer)。
* 上图中3的详细说明见[绘制本地播放器组件](app-takeovers-web-media.md#绘制本地播放器组件)。
* 上图中4的详细说明见[执行ArkWeb内核发送给本地播放器的播控命令](app-takeovers-web-media.md#执行arkweb内核发送给本地播放器的播控命令)。
* 上图中5的详细说明见[将本地播放器的状态信息通知给ArkWeb内核](app-takeovers-web-media.md#将本地播放器的状态信息通知给arkweb内核)。

## 开发指导

### 开启接管网页媒体播放

需要先通过[enableNativeMediaPlayer](../harmonyos-references/arkts-basic-components-web-attributes.md#enablenativemediaplayer12)接口开启接管网页媒体播放的功能。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. @Entry
5. @Component
6. struct WebComponent {
7. controller: webview.WebviewController = new webview.WebviewController();

9. build() {
10. Column() {
11. Web({ src: 'www.example.com', controller: this.controller })
12. .enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
13. }
14. }
15. }
```

### 创建本地播放器(NativeMediaPlayer)

该功能开启后，网页中有媒体需要播放时，ArkWeb内核会触发[onCreateNativeMediaPlayer](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)注册的回调函数。

应用则需要调用onCreateNativeMediaPlayer来注册一个创建本地播放器的回调函数。

该回调函数需要根据媒体信息来判断是否要创建一个本地播放器来接管当前的网页媒体资源。

* 如果应用不接管当前的网页媒体资源， 需在回调函数里返回null。
* 如果应用接管当前的网页媒体资源， 需在回调函数里返回一个本地播放器实例。

本地播放器需要实现[NativeMediaPlayerBridge](../harmonyos-references/arkts-apis-webview-nativemediaplayerbridge.md)接口，以便ArkWeb内核对本地播放器进行播控操作。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. // 实现 webview.NativeMediaPlayerBridge 接口。
5. // ArkWeb 内核调用该类的方法来对 NativeMediaPlayer 进行播控。
6. class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
7. // ... 实现 NativeMediaPlayerBridge 里的接口方法 ...
8. constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {}
9. updateRect(x: number, y: number, width: number, height: number) {}
10. play() {}
11. pause() {}
12. seek(targetTime: number) {}
13. release() {}
14. setVolume(volume: number) {}
15. setMuted(muted: boolean) {}
16. setPlaybackRate(playbackRate: number) {}
17. enterFullscreen() {}
18. exitFullscreen() {}
19. }

21. @Entry
22. @Component
23. struct WebComponent {
24. controller: webview.WebviewController = new webview.WebviewController();

26. build() {
27. Column() {
28. Web({ src: 'www.example.com', controller: this.controller })
29. .enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
30. .onPageBegin((event) => {
31. this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
32. // 判断需不需要接管当前的媒体。
33. if (!shouldHandle(mediaInfo)) {
34. // 本地播放器不接管该媒体。
35. // 返回 null 。ArkWeb 内核将用自己的播放器来播放该媒体。
36. return null;
37. }
38. // 接管当前的媒体。
39. // 返回一个本地播放器实例给 ArkWeb 内核。
40. let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
41. return nativePlayer;
42. });
43. })
44. }
45. }
46. }

48. // stub
49. function shouldHandle(mediaInfo: webview.MediaInfo) {
50. return true;
51. }
```

### 绘制本地播放器组件

应用接管网页媒体后，应用需要将本地播放器组件及视频画面绘制到ArkWeb内核提供的Surface上。ArkWeb内核再将Surface与网页进行合成并显示。

该流程与[同层渲染](web-same-layer.md)绘制一致。

1. 在应用启动阶段，应用应保存[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)，以便后续的同层渲染绘制流程能够使用该UIContext。

   ```
   1. import { window } from '@kit.ArkUI';

   3. export default class Entry2Ability extends UIAbility {
   4. // ...
   5. onWindowStageCreate(windowStage: window.WindowStage): void {
   6. windowStage.loadContent('pages/Index', (err, data) => {
   7. if (err && err.code) {
   8. return;
   9. }

   11. let mainWindow = windowStage.getMainWindowSync();
   12. if (mainWindow) {
   13. // 保存UIContext， 在后续的同层渲染绘制中使用。
   14. AppStorage.setOrCreate<UIContext>('UIContext', mainWindow.getUIContext());
   15. } else {
   16. console.error('Failed to get the main window');
   17. }
   18. });
   19. }
   20. // ...
   21. }
   ```

   [Entry2Ability.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UsingWebMultimedia/entry2/src/main/ets/entry2ability/Entry2Ability.ets#L18-L63)
2. 应用使用ArkWeb内核创建的Surface进行同层渲染绘制。

   ```
   1. // xxx.ets
   2. import { webview } from '@kit.ArkWeb';
   3. import { BuilderNode, FrameNode, NodeController, NodeRenderType } from '@kit.ArkUI';

   5. interface ComponentParams {}

   7. class MyNodeController extends NodeController {
   8. private rootNode: BuilderNode<[ComponentParams]> | undefined;

   10. constructor(surfaceId: string, renderType: NodeRenderType) {
   11. super();

   13. // 获取之前保存的 UIContext 。
   14. let uiContext = AppStorage.get<UIContext>("UIContext");
   15. this.rootNode = new BuilderNode(uiContext as UIContext, { surfaceId: surfaceId, type: renderType });
   16. }

   18. makeNode(uiContext: UIContext): FrameNode | null {
   19. if (this.rootNode) {
   20. return this.rootNode.getFrameNode() as FrameNode;
   21. }
   22. return null;
   23. }

   25. build() {
   26. // 构造本地播放器组件
   27. }
   28. }

   30. @Entry
   31. @Component
   32. struct WebComponent {
   33. node_controller?: MyNodeController;
   34. controller: webview.WebviewController = new webview.WebviewController();
   35. @State show_native_media_player: boolean = false;

   37. build() {
   38. Column() {
   39. Stack({ alignContent: Alignment.TopStart }) {
   40. if (this.show_native_media_player) {
   41. NodeContainer(this.node_controller)
   42. .width(300)
   43. .height(150)
   44. .backgroundColor(Color.Transparent)
   45. .border({ width: 2, color: Color.Orange })
   46. }
   47. Web({ src: 'www.example.com', controller: this.controller })
   48. .enableNativeMediaPlayer({ enable: true, shouldOverlay: false })
   49. .onPageBegin((event) => {
   50. this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
   51. // 接管当前的媒体。
   52. // 使用同层渲染流程提供的 surface 来构造一个本地播放器组件。
   53. this.node_controller = new MyNodeController(mediaInfo.surfaceInfo.id, NodeRenderType.RENDER_TYPE_TEXTURE);
   54. this.node_controller.build();

   56. // 展示本地播放器组件。
   57. this.show_native_media_player = true;

   59. // 返回一个本地播放器实例给 ArkWeb 内核。
   60. let nativePlayer: webview.NativeMediaPlayerBridge = new NativeMediaPlayerImpl(handler, mediaInfo);
   61. return nativePlayer;
   62. });
   63. })
   64. }
   65. }
   66. }
   67. }
   ```

动态创建组件并绘制到Surface上的详细介绍见[同层渲染](web-same-layer.md)。

### 执行ArkWeb内核发送给本地播放器的播控命令

为了方便ArkWeb内核对本地播放器进行播控操作，应用需要令本地播放器实现[NativeMediaPlayerBridge](../harmonyos-references/arkts-apis-webview-nativemediaplayerbridge.md)接口，并根据每个接口方法的功能对本地播放器进行相应操作。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. class ActualNativeMediaPlayerListener {
5. constructor(handler: webview.NativeMediaPlayerHandler) {}
6. }

8. class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
9. constructor(handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) {
10. // 1. 创建一个本地播放器的状态监听。
11. let listener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
12. // 2. 创建一个本地播放器。
13. // 3. 监听该本地播放器。
14. // ...
15. }

17. updateRect(x: number, y: number, width: number, height: number) {
18. // <video> 标签的位置和大小发生了变化。
19. // 根据该信息变化，作出相应的改变。
20. }

22. play() {
23. // 启动本地播放器播放。
24. }

26. pause() {
27. // 暂停本地播放器播放。
28. }

30. seek(targetTime: number) {
31. // 本地播放器跳转到指定的时间点。
32. }

34. release() {
35. // 销毁本地播放器。
36. }

38. setVolume(volume: number) {
39. // ArkWeb 内核要求调整本地播放器的音量。
40. // 设置本地播放器的音量。
41. }

43. setMuted(muted: boolean) {
44. // 将本地播放器静音或取消静音。
45. }

47. setPlaybackRate(playbackRate: number) {
48. // 调整本地播放器的播放速度。
49. }

51. enterFullscreen() {
52. // 将本地播放器设置为全屏播放。
53. }

55. exitFullscreen() {
56. // 将本地播放器退出全屏播放。
57. }
58. }
```

### 将本地播放器的状态信息通知给ArkWeb内核

ArkWeb内核需要本地播放器的状态信息来更新到网页（例如：视频的宽高、播放时间、缓存时间等），因此，应用需要将本地播放器的状态信息通知给ArkWeb内核。

在[onCreateNativeMediaPlayer](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#oncreatenativemediaplayer12)接口中， ArkWeb内核传递一个[NativeMediaPlayerHandler](../harmonyos-references/arkts-apis-webview-nativemediaplayerhandler.md)对象给应用。应用需要通过该对象，将本地播放器的最新状态信息通知给ArkWeb内核。

```
1. // xxx.ets
2. import { webview } from '@kit.ArkWeb';

4. class ActualNativeMediaPlayerListener {
5. handler: webview.NativeMediaPlayerHandler;

7. constructor(handler: webview.NativeMediaPlayerHandler) {
8. this.handler = handler;
9. }

11. onPlaying() {
12. // 本地播放器开始播放。
13. this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
14. }
15. onPaused() {
16. // 本地播放器暂停播放。
17. this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
18. }
19. onSeeking() {
20. // 本地播放器开始执行跳转到目标时间点。
21. this.handler.handleSeeking();
22. }
23. onSeekDone() {
24. // 本地播放器 seek 完成。
25. this.handler.handleSeekFinished();
26. }
27. onEnded() {
28. // 本地播放器播放完成。
29. this.handler.handleEnded();
30. }
31. onVolumeChanged() {
32. // 获取本地播放器的音量。
33. let volume: number = getVolume();
34. this.handler.handleVolumeChanged(volume);
35. }
36. onCurrentPlayingTimeUpdate() {
37. // 更新播放时间。
38. let currentTime: number = getCurrentPlayingTime();
39. // 将时间单位换算成秒。
40. let currentTimeInSeconds = convertToSeconds(currentTime);
41. this.handler.handleTimeUpdate(currentTimeInSeconds);
42. }
43. onBufferedChanged() {
44. // 缓存发生了变化。
45. // 获取本地播放器的缓存时长。
46. let bufferedEndTime: number = getCurrentBufferedTime();
47. // 将时间单位换算成秒。
48. let bufferedEndTimeInSeconds = convertToSeconds(bufferedEndTime);
49. this.handler.handleBufferedEndTimeChanged(bufferedEndTimeInSeconds);

51. // 检查缓存状态。
52. // 如果缓存状态发生了变化，则向 ArkWeb 内核通知缓存状态。
53. let lastReadyState: webview.ReadyState = getLastReadyState();
54. let currentReadyState: webview.ReadyState = getCurrentReadyState();
55. if (lastReadyState != currentReadyState) {
56. this.handler.handleReadyStateChanged(currentReadyState);
57. }
58. }
59. onEnterFullscreen() {
60. // 本地播放器进入了全屏状态。
61. let isFullscreen: boolean = true;
62. this.handler.handleFullscreenChanged(isFullscreen);
63. }
64. onExitFullscreen() {
65. // 本地播放器退出了全屏状态。
66. let isFullscreen: boolean = false;
67. this.handler.handleFullscreenChanged(isFullscreen);
68. }
69. onUpdateVideoSize(width: number, height: number) {
70. // 当本地播放器解析出视频宽高时， 通知 ArkWeb 内核。
71. this.handler.handleVideoSizeChanged(width, height);
72. }
73. onDurationChanged(duration: number) {
74. // 本地播放器解析到了新的媒体时长， 通知 ArkWeb 内核。
75. this.handler.handleDurationChanged(duration);
76. }
77. onError(error: webview.MediaError, errorMessage: string) {
78. // 本地播放器出错了，通知 ArkWeb 内核。
79. this.handler.handleError(error, errorMessage);
80. }
81. onNetworkStateChanged(state: webview.NetworkState) {
82. // 本地播放器的网络状态发生了变化， 通知 ArkWeb 内核。
83. this.handler.handleNetworkStateChanged(state);
84. }
85. onPlaybackRateChanged(playbackRate: number) {
86. // 本地播放器的播放速率发生了变化， 通知 ArkWeb 内核。
87. this.handler.handlePlaybackRateChanged(playbackRate);
88. }
89. onMutedChanged(muted: boolean) {
90. // 本地播放器的静音状态发生了变化， 通知 ArkWeb 内核。
91. this.handler.handleMutedChanged(muted);
92. }

94. // ... 监听本地播放器其他的状态 ...
95. }
96. @Entry
97. @Component
98. struct WebComponent {
99. controller: webview.WebviewController = new webview.WebviewController();
100. @State show_native_media_player: boolean = false;

102. build() {
103. Column() {
104. Web({ src: 'www.example.com', controller: this.controller })
105. .enableNativeMediaPlayer({enable: true, shouldOverlay: false})
106. .onPageBegin((event) => {
107. this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
108. // 接管当前的媒体。

110. // 创建一个本地播放器实例。
111. // let nativePlayer: NativeMediaPlayerImpl = new NativeMediaPlayerImpl(handler, mediaInfo);

113. // 创建一个本地播放器状态监听对象。
114. let nativeMediaPlayerListener: ActualNativeMediaPlayerListener = new ActualNativeMediaPlayerListener(handler);
115. // 监听本地播放器状态。
116. // nativePlayer.setListener(nativeMediaPlayerListener);

118. // 返回这个本地播放器实例给 ArkWeb 内核。
119. return null;
120. });
121. })
122. }
123. }
124. }

126. // stub
127. function getVolume() {
128. return 1;
129. }
130. function getCurrentPlayingTime() {
131. return 1;
132. }
133. function getCurrentBufferedTime() {
134. return 1;
135. }
136. function convertToSeconds(input: number) {
137. return input;
138. }
139. function getLastReadyState() {
140. return webview.ReadyState.HAVE_NOTHING;
141. }
142. function getCurrentReadyState() {
143. return webview.ReadyState.HAVE_NOTHING;
144. }
```

## 完整示例

* 涉及网页媒体播放，需在配置文件中配置网络访问权限。添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

  ```
  1. // src/main/module.json5
  2. "requestPermissions":[
  3. {
  4. "name" : "ohos.permission.INTERNET"
  5. }
  6. ]
  ```
* 在应用启动阶段保存[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)。

  ```
  1. // xxxAbility.ets

  3. import { UIAbility } from '@kit.AbilityKit';
  4. import { window } from '@kit.ArkUI';

  6. export default class EntryAbility extends UIAbility {
  7. onWindowStageCreate(windowStage: window.WindowStage): void {
  8. windowStage.loadContent('pages/Index', (err, data) => {
  9. if (err && err.code) {
  10. return;
  11. }

  13. let mainWindow = windowStage.getMainWindowSync();
  14. if (mainWindow) {
  15. // 保存UIContext， 在后续的同层渲染绘制中使用。
  16. AppStorage.setOrCreate<UIContext>("UIContext", mainWindow.getUIContext());
  17. } else {
  18. console.error("Failed to get the main window");
  19. }
  20. });
  21. }

  23. // ... 其他需要重写的方法 ...
  24. }
  ```
* 应用侧代码，视频托管使用示例。通过[AVPlayer](media-kit-intro.md#avplayer)托管Web媒体的播放。

  ```
  1. // Index.ets
  2. import { webview } from '@kit.ArkWeb';
  3. import { BuilderNode, FrameNode, NodeController, NodeRenderType } from '@kit.ArkUI';
  4. import { AVPlayerDemo, AVPlayerListener } from './PlayerDemo';

  6. // 实现 webview.NativeMediaPlayerBridge 接口。
  7. // ArkWeb 内核调用该类的方法来对 NativeMediaPlayer 进行播控。
  8. class NativeMediaPlayerImpl implements webview.NativeMediaPlayerBridge {
  9. private surfaceId: string;
  10. mediaSource: string;
  11. private mediaHandler: webview.NativeMediaPlayerHandler;
  12. nativePlayerInfo: NativePlayerInfo;
  13. nativePlayer: AVPlayerDemo;
  14. httpHeaders: Record<string, string>;
  15. uiContext?: UIContext;

  17. constructor(nativePlayerInfo: NativePlayerInfo, handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo, uiContext: UIContext) {
  18. this.uiContext = uiContext;
  19. console.info(`NativeMediaPlayerImpl.constructor, surface_id[${mediaInfo.surfaceInfo.id}]`);
  20. this.nativePlayerInfo = nativePlayerInfo;
  21. this.mediaHandler = handler;
  22. this.surfaceId = mediaInfo.surfaceInfo.id;
  23. this.mediaSource = mediaInfo.mediaSrcList.find((item) => item.source.indexOf('.mp4') > 0)?.source
  24. || mediaInfo.mediaSrcList[0].source;
  25. this.httpHeaders = mediaInfo.headers;
  26. this.nativePlayer = new AVPlayerDemo();

  28. // 使用同层渲染功能，将视频及其播控组件绘制到网页中
  29. this.nativePlayerInfo.node_controller = new MyNodeController(
  30. this.nativePlayerInfo, this.surfaceId, this.mediaHandler, this, NodeRenderType.RENDER_TYPE_TEXTURE);
  31. this.nativePlayerInfo.node_controller.build();
  32. this.nativePlayerInfo.show_native_media_player = true;

  34. console.info(`NativeMediaPlayerImpl.mediaSource: ${this.mediaSource}, headers: ${JSON.stringify(this.httpHeaders)}`);
  35. }

  37. updateRect(x: number, y: number, width: number, height: number): void {
  38. // <video> 标签的位置和大小发生了变化。
  39. // 根据该信息变化，作出相应的改变。
  40. let width_in_vp = this.uiContext!.px2vp(width);
  41. let height_in_vp = this.uiContext!.px2vp(height);
  42. console.info(`updateRect(${x}, ${y}, ${width}, ${height}), vp:{${width_in_vp}, ${height_in_vp}}`);

  44. this.nativePlayerInfo.updateNativePlayerRect(x, y, width, height);
  45. }

  47. play() {
  48. // 启动本地播放器播放。
  49. console.info('NativeMediaPlayerImpl.play');
  50. this.nativePlayer.play();
  51. }
  52. pause() {
  53. // 暂停本地播放器播放。
  54. console.info('NativeMediaPlayerImpl.pause');
  55. this.nativePlayer.pause();
  56. }
  57. seek(targetTime: number) {
  58. // 本地播放器跳转到指定的时间点。
  59. console.info(`NativeMediaPlayerImpl.seek(${targetTime})`);
  60. this.nativePlayer.seek(targetTime);
  61. }
  62. setVolume(volume: number) {
  63. // ArkWeb 内核要求调整本地播放器的音量。
  64. // 设置本地播放器的音量。
  65. console.info(`NativeMediaPlayerImpl.setVolume(${volume})`);
  66. this.nativePlayer.setVolume(volume);
  67. }
  68. setMuted(muted: boolean) {
  69. // 将本地播放器静音或取消静音。
  70. console.info(`NativeMediaPlayerImpl.setMuted(${muted})`);
  71. }
  72. setPlaybackRate(playbackRate: number) {
  73. // 调整本地播放器的播放速度。
  74. console.info(`NativeMediaPlayerImpl.setPlaybackRate(${playbackRate})`);
  75. this.nativePlayer.setPlaybackRate(playbackRate);
  76. }
  77. release() {
  78. // 销毁本地播放器。
  79. console.info('NativeMediaPlayerImpl.release');
  80. this.nativePlayer?.release();
  81. this.nativePlayerInfo.show_native_media_player = false;
  82. this.nativePlayerInfo.node_width = 300;
  83. this.nativePlayerInfo.node_height = 150;
  84. this.nativePlayerInfo.destroyed();
  85. }
  86. enterFullscreen() {
  87. // 将本地播放器设置为全屏播放。
  88. console.info('NativeMediaPlayerImpl.enterFullscreen');
  89. }
  90. exitFullscreen() {
  91. // 将本地播放器退出全屏播放。
  92. console.info('NativeMediaPlayerImpl.exitFullscreen');
  93. }
  94. }

  96. // 监听NativeMediaPlayer的状态，然后通过 webview.NativeMediaPlayerHandler 将状态上报给 ArkWeb 内核。
  97. class AVPlayerListenerImpl implements AVPlayerListener {
  98. handler: webview.NativeMediaPlayerHandler;
  99. component: NativePlayerComponent;

  101. constructor(handler: webview.NativeMediaPlayerHandler, component: NativePlayerComponent) {
  102. this.handler = handler;
  103. this.component = component;
  104. }
  105. onPlaying() {
  106. // 通知ArkWeb内核，本地播放器开始播放
  107. console.info('AVPlayerListenerImpl.onPlaying');
  108. this.handler.handleStatusChanged(webview.PlaybackStatus.PLAYING);
  109. }
  110. onPaused() {
  111. // 通知ArkWeb内核，本地播放器暂停播放
  112. console.info('AVPlayerListenerImpl.onPaused');
  113. this.handler.handleStatusChanged(webview.PlaybackStatus.PAUSED);
  114. }
  115. onDurationChanged(duration: number) {
  116. // 通知ArkWeb内核，本地播放器解析到了新的媒体时长
  117. console.info(`AVPlayerListenerImpl.onDurationChanged(${duration})`);
  118. this.handler.handleDurationChanged(duration);
  119. }
  120. onBufferedTimeChanged(buffered: number) {
  121. // 通知ArkWeb内核，本地播放器的缓存时长变化
  122. console.info(`AVPlayerListenerImpl.onBufferedTimeChanged(${buffered})`);
  123. this.handler.handleBufferedEndTimeChanged(buffered);
  124. }
  125. onTimeUpdate(time: number) {
  126. // 通知ArkWeb内核，本地播放进度发生变化
  127. this.handler.handleTimeUpdate(time);
  128. }
  129. onEnded() {
  130. // 通知ArkWeb内核，本地播放器播放完成
  131. console.info('AVPlayerListenerImpl.onEnded');
  132. this.handler.handleEnded();
  133. }
  134. onError() {
  135. // 通知ArkWeb内核，本地播放器出错了
  136. console.info('AVPlayerListenerImpl.onError');
  137. this.component.has_error = true;
  138. setTimeout(()=>{
  139. this.handler.handleError(1, "Oops!");
  140. }, 200);
  141. }
  142. onVideoSizeChanged(width: number, height: number) {
  143. // 通知ArkWeb内核，视频尺寸发生变化
  144. console.info(`AVPlayerListenerImpl.onVideoSizeChanged(${width}, ${height})`);
  145. this.handler.handleVideoSizeChanged(width, height);
  146. this.component.onSizeChanged(width, height);
  147. }
  148. onDestroyed(): void {
  149. // 播放器销毁
  150. console.info('AVPlayerListenerImpl.onDestroyed');
  151. }
  152. }

  154. interface ComponentParams {
  155. text: string;
  156. text2: string;
  157. playerInfo: NativePlayerInfo;
  158. handler: webview.NativeMediaPlayerHandler;
  159. player: NativeMediaPlayerImpl;
  160. }

  162. // 自定义的播放器组件
  163. @Component
  164. struct NativePlayerComponent {
  165. params?: ComponentParams;
  166. @State bgColor: Color = Color.Red;
  167. mXComponentController: XComponentController = new XComponentController();

  169. videoController: VideoController = new VideoController();
  170. offset_x: number = 0;
  171. offset_y: number = 0;
  172. @State video_width_percent: number = 100;
  173. @State video_height_percent: number = 100;
  174. view_width: number = 0;
  175. view_height: number = 0;
  176. video_width: number = 0;
  177. video_height: number = 0;

  179. fullscreen: boolean = false;
  180. @State has_error: boolean = false;

  182. onSizeChanged(width: number, height: number) {
  183. // 更新播放区域比例
  184. this.video_width = width;
  185. this.video_height = height;
  186. let scale: number = this.view_width / width;
  187. let scaled_video_height: number = scale * height;
  188. this.video_height_percent = scaled_video_height / this.view_height * 100;
  189. console.info(`NativePlayerComponent.onSizeChanged(${width},${height}), video_height_percent[${this.video_height_percent }]`);
  190. }

  192. build() {
  193. Column() {
  194. Stack() {
  195. XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.mXComponentController })
  196. .width(this.video_width_percent + '%')
  197. .height(this.video_height_percent + '%')
  198. .onLoad(()=>{
  199. if (!this.params) {
  200. console.info('this.params is null');
  201. return;
  202. }
  203. console.info('NativePlayerComponent.onLoad, params[' + this.params
  204. + '], text[' + this.params.text + '], text2[' + this.params.text2
  205. + '], web_tab[' + this.params.playerInfo + '], handler[' + this.params.handler + ']');
  206. // 设置Surface ID到播放器
  207. this.params.player.nativePlayer.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());

  209. this.params.player.nativePlayer.avPlayerLiveDemo({
  210. url: this.params.player.mediaSource,
  211. listener: new AVPlayerListenerImpl(this.params.handler, this),
  212. httpHeaders: this.params.player.httpHeaders,
  213. });
  214. })
  215. Column() {
  216. Row() {
  217. Button(this.params?.text)
  218. .height(50)
  219. .border({ width: 2, color: Color.Red })
  220. .backgroundColor(this.bgColor)
  221. .onClick(()=>{
  222. console.info(`NativePlayerComponent.Button[${this.params?.text}] is clicked`);
  223. this.params?.player.nativePlayer?.play();
  224. })
  225. .onTouch((event: TouchEvent) => {
  226. event.stopPropagation();
  227. })
  228. Button(this.params?.text2)
  229. .height(50)
  230. .border({ width: 2, color: Color.Red })
  231. .onClick(()=>{
  232. console.info(`NativePlayerComponent.Button[${this.params?.text2}] is clicked`);
  233. this.params?.player.nativePlayer?.pause();
  234. })
  235. .onTouch((event: TouchEvent) => {
  236. event.stopPropagation();
  237. })
  238. }
  239. .width('100%')
  240. .justifyContent(FlexAlign.SpaceEvenly)
  241. }
  242. if (this.has_error) {
  243. Column() {
  244. Text('Error')
  245. .fontSize(30)
  246. }
  247. .backgroundColor('#eb5555')
  248. .width('100%')
  249. .height('100%')
  250. .justifyContent(FlexAlign.Center)
  251. }
  252. }
  253. }
  254. .width('100%')
  255. .height('100%')
  256. .onAreaChange((oldValue: Area, newValue: Area) => {
  257. // 当组件区域发生变化时触发
  258. console.info(`NativePlayerComponent.onAreaChange(${JSON.stringify(oldValue)}, ${JSON.stringify(newValue)})`);
  259. this.view_width = new Number(newValue.width).valueOf();
  260. this.view_height = new Number(newValue.height).valueOf();
  261. this.onSizeChanged(this.video_width, this.video_height);
  262. })
  263. }
  264. }

  266. @Builder
  267. function NativePlayerComponentBuilder(params: ComponentParams) {
  268. NativePlayerComponent({ params: params })
  269. .backgroundColor(Color.Green)
  270. .border({ width: 1, color: Color.Brown })
  271. .width('100%')
  272. .height('100%')
  273. }

  275. // 通过 NodeController 动态创建自定义的播放器组件， 并将组件内容绘制到 surface 上。
  276. class MyNodeController extends NodeController {
  277. private rootNode: BuilderNode<[ComponentParams]> | undefined;
  278. playerInfo: NativePlayerInfo;
  279. listener: webview.NativeMediaPlayerHandler;
  280. player: NativeMediaPlayerImpl;

  282. constructor(playerInfo: NativePlayerInfo,
  283. surfaceId: string,
  284. listener: webview.NativeMediaPlayerHandler,
  285. player: NativeMediaPlayerImpl,
  286. renderType: NodeRenderType) {
  287. super();
  288. this.playerInfo = playerInfo;
  289. this.listener = listener;
  290. this.player = player;
  291. let uiContext = AppStorage.get<UIContext>("UIContext");
  292. this.rootNode = new BuilderNode(uiContext as UIContext, { surfaceId: surfaceId, type: renderType });
  293. console.info(`MyNodeController, rootNode[${this.rootNode}], playerInfo[${playerInfo}], listener[${listener}], surfaceId[${surfaceId}]`);
  294. }

  296. makeNode(): FrameNode | null {
  297. if (this.rootNode) {
  298. return this.rootNode.getFrameNode() as FrameNode;
  299. }
  300. return null;
  301. }

  303. build() {
  304. let params: ComponentParams = {
  305. "text": "play",
  306. "text2": "pause",
  307. playerInfo: this.playerInfo,
  308. handler: this.listener,
  309. player: this.player
  310. };
  311. if (this.rootNode) {
  312. this.rootNode.build(wrapBuilder(NativePlayerComponentBuilder), params);
  313. }
  314. }

  316. postTouchEvent(event: TouchEvent) {
  317. return this.rootNode?.postTouchEvent(event);
  318. }
  319. }

  321. class Rect {
  322. x: number = 0;
  323. y: number = 0;
  324. width: number = 0;
  325. height: number = 0;

  327. static toNodeRect(rectInPx: webview.RectEvent, uiContext: UIContext) : Rect {
  328. let rect = new Rect();
  329. rect.x = uiContext.px2vp(rectInPx.x);
  330. rect.y = uiContext.px2vp(rectInPx.y);
  331. rect.width = uiContext.px2vp(rectInPx.width);
  332. rect.height = uiContext.px2vp(rectInPx.height);
  333. return rect;
  334. }
  335. }

  337. @Observed
  338. class NativePlayerInfo {
  339. public web: WebComponent;
  340. public embed_id: string;
  341. public player: webview.NativeMediaPlayerBridge;
  342. public node_controller?: MyNodeController;
  343. public show_native_media_player: boolean = false;
  344. public node_pos_x: number;
  345. public node_pos_y: number;
  346. public node_width: number;
  347. public node_height: number;

  349. playerComponent?: NativeMediaPlayerComponent;

  351. constructor(web: WebComponent, handler: webview.NativeMediaPlayerHandler, videoInfo: webview.MediaInfo, uiContext: UIContext) {
  352. this.web = web;
  353. this.embed_id = videoInfo.embedID;

  355. let node_rect = Rect.toNodeRect(videoInfo.surfaceInfo.rect, uiContext);
  356. this.node_pos_x = node_rect.x;
  357. this.node_pos_y = node_rect.y;
  358. this.node_width = node_rect.width;
  359. this.node_height = node_rect.height;

  361. this.player = new NativeMediaPlayerImpl(this, handler, videoInfo, uiContext);
  362. }

  364. updateNativePlayerRect(x: number, y: number, width: number, height: number) {
  365. // 更新播放器的位置和大小
  366. this.playerComponent?.updateNativePlayerRect(x, y, width, height);
  367. }

  369. destroyed() {
  370. let info_list = this.web.native_player_info_list;
  371. console.info(`NativePlayerInfo[${this.embed_id}] destroyed, list.size[${info_list.length}]`);
  372. this.web.native_player_info_list = info_list.filter((item) => item.embed_id != this.embed_id);
  373. console.info(`NativePlayerInfo after destroyed, new_list.size[${this.web.native_player_info_list.length}]`);
  374. }
  375. }

  377. @Component
  378. struct NativeMediaPlayerComponent {
  379. @ObjectLink playerInfo: NativePlayerInfo;

  381. aboutToAppear() {
  382. this.playerInfo.playerComponent = this;
  383. }

  385. build() {
  386. NodeContainer(this.playerInfo.node_controller)
  387. .width(this.playerInfo.node_width)
  388. .height(this.playerInfo.node_height)
  389. .offset({x: this.playerInfo.node_pos_x, y: this.playerInfo.node_pos_y})
  390. .backgroundColor(Color.Transparent)
  391. .border({ width: 2, color: Color.Orange })
  392. .onAreaChange((oldValue, newValue) => {
  393. console.info(`NodeContainer[${this.playerInfo.embed_id}].onAreaChange([${oldValue.width} x ${oldValue.height}]->[${newValue.width} x ${newValue.height}]`);
  394. })
  395. }

  397. updateNativePlayerRect(x: number, y: number, width: number, height: number) {
  398. let node_rect = Rect.toNodeRect({x, y, width, height}, this.getUIContext());
  399. this.playerInfo.node_pos_x = node_rect.x;
  400. this.playerInfo.node_pos_y = node_rect.y;
  401. this.playerInfo.node_width = node_rect.width;
  402. this.playerInfo.node_height = node_rect.height;
  403. }
  404. }

  406. @Entry
  407. @Component
  408. struct WebComponent {
  409. controller: WebviewController = new webview.WebviewController();
  410. page_url: Resource = $rawfile('main.html');

  412. @State native_player_info_list: NativePlayerInfo[] = [];

  414. area?: Area;

  416. build() {
  417. Column() {
  418. Stack({alignContent: Alignment.TopStart}) {
  419. ForEach(this.native_player_info_list, (item: NativePlayerInfo) => {
  420. if (item.show_native_media_player) {
  421. NativeMediaPlayerComponent({ playerInfo: item })
  422. }
  423. }, (item: NativePlayerInfo) => {
  424. return item.embed_id;
  425. })
  426. Web({ src: this.page_url, controller: this.controller })
  427. .enableNativeMediaPlayer({ enable: true, shouldOverlay: true })
  428. .onPageBegin(() => {
  429. // 页面开始加载时，注册播放器创建回调
  430. this.controller.onCreateNativeMediaPlayer((handler: webview.NativeMediaPlayerHandler, mediaInfo: webview.MediaInfo) => {
  431. console.info('onCreateNativeMediaPlayer(' + JSON.stringify(mediaInfo) + ')');
  432. let nativePlayerInfo = new NativePlayerInfo(this, handler, mediaInfo, this.getUIContext());
  433. this.native_player_info_list.push(nativePlayerInfo);
  434. return nativePlayerInfo.player;
  435. });
  436. })
  437. .onNativeEmbedGestureEvent((event)=>{
  438. // 处理触摸事件
  439. if (!event.touchEvent || !event.embedId) {
  440. event.result?.setGestureEventResult(false);
  441. return;
  442. }
  443. console.info(`WebComponent.onNativeEmbedGestureEvent, embedId[${event.embedId}]`);
  444. // 查找对应的播放器信息
  445. let native_player_info = this.getNativePlayerInfoByEmbedId(event.embedId);
  446. if (!native_player_info) {
  447. console.info(`WebComponent.onNativeEmbedGestureEvent, embedId[${event.embedId}], no native_player_info`);
  448. event.result?.setGestureEventResult(false);
  449. return;
  450. }
  451. if (!native_player_info.node_controller) {
  452. console.info(`WebComponent.onNativeEmbedGestureEvent, embedId[${event.embedId}], no node_controller`);
  453. event.result?.setGestureEventResult(false);
  454. return;
  455. }
  456. // 将触摸事件传递给NodeContrloller
  457. let ret = native_player_info.node_controller.postTouchEvent(event.touchEvent);
  458. console.info(`WebComponent.postTouchEvent, ret[${ret}], touchEvent[${JSON.stringify(event.touchEvent)}]`);
  459. event.result?.setGestureEventResult(ret);
  460. })
  461. .width('100%')
  462. .height('100%')
  463. .onAreaChange((oldValue: Area, newValue: Area) => {
  464. oldValue;
  465. this.area = newValue;
  466. })
  467. }
  468. }
  469. }

  471. getNativePlayerInfoByEmbedId(embedId: string) : NativePlayerInfo | undefined {
  472. return this.native_player_info_list.find((item)=> item.embed_id == embedId);
  473. }
  474. }
  ```
* 应用侧代码，视频播放示例, ./PlayerDemo.ets。

  ```
  1. import { media } from '@kit.MediaKit';
  2. import { BusinessError } from '@kit.BasicServicesKit';

  4. export interface AVPlayerListener {
  5. onPlaying() : void;
  6. onPaused() : void;
  7. onDurationChanged(duration: number) : void;
  8. onBufferedTimeChanged(buffered: number) : void;
  9. onTimeUpdate(time: number) : void;
  10. onEnded() : void;
  11. onError() : void;
  12. onVideoSizeChanged(width: number, height: number): void;
  13. onDestroyed(): void;
  14. }

  16. interface PlayerParam {
  17. url: string;
  18. listener?: AVPlayerListener;
  19. httpHeaders?: Record<string, string>;
  20. }

  22. interface PlayCommand {
  23. func: Function;
  24. name?: string;
  25. }

  27. interface CheckPlayCommandResult {
  28. ignore: boolean;
  29. index_to_remove: number;
  30. }

  32. export class AVPlayerDemo {
  33. private surfaceID: string = ''; // surfaceID用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法

  35. avPlayer?: media.AVPlayer;
  36. prepared: boolean = false;

  38. commands: PlayCommand[] = [];

  40. setSurfaceID(surface_id: string) {
  41. console.info(`AVPlayerDemo.setSurfaceID : ${surface_id}`);
  42. this.surfaceID = surface_id;
  43. }
  44. // 注册avplayer回调函数
  45. setAVPlayerCallback(avPlayer: media.AVPlayer, listener?: AVPlayerListener) {
  46. // seek操作结果回调函数
  47. avPlayer.on('seekDone', (seekDoneTime: number) => {
  48. console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
  49. });
  50. // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程
  51. avPlayer.on('error', (err: BusinessError) => {
  52. console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
  53. listener?.onError();
  54. avPlayer.reset(); // 调用reset重置资源，触发idle状态
  55. });
  56. // 状态机变化回调函数
  57. avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
  58. switch (state) {
  59. case 'idle': // 成功调用reset接口后触发该状态机上报
  60. console.info('AVPlayer state idle called.');
  61. avPlayer.release(); // 调用release接口销毁实例对象
  62. break;
  63. case 'initialized': // avplayer 设置播放源后触发该状态上报
  64. console.info('AVPlayer state initialized called.');
  65. avPlayer.surfaceId = this.surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置
  66. avPlayer.prepare();
  67. break;
  68. case 'prepared': // prepare调用成功后上报该状态机
  69. console.info('AVPlayer state prepared called.');
  70. this.prepared = true;
  71. this.schedule();
  72. break;
  73. case 'playing': // play成功调用后触发该状态机上报
  74. console.info('AVPlayer state playing called.');
  75. listener?.onPlaying();
  76. break;
  77. case 'paused': // pause成功调用后触发该状态机上报
  78. console.info('AVPlayer state paused called.');
  79. listener?.onPaused();
  80. break;
  81. case 'completed': // 播放结束后触发该状态机上报
  82. console.info('AVPlayer state completed called.');
  83. avPlayer.stop(); // 调用播放结束接口
  84. break;
  85. case 'stopped': // stop接口成功调用后触发该状态机上报
  86. console.info('AVPlayer state stopped called.');
  87. listener?.onEnded();
  88. break;
  89. case 'released':
  90. this.prepared = false;
  91. listener?.onDestroyed();
  92. console.info('AVPlayer state released called.');
  93. break;
  94. default:
  95. console.info('AVPlayer state unknown called.');
  96. break;
  97. }
  98. });
  99. avPlayer.on('durationUpdate', (duration: number) => {
  100. console.info(`AVPlayer state durationUpdate success,new duration is :${duration}`);
  101. listener?.onDurationChanged(duration/1000);
  102. });
  103. avPlayer.on('timeUpdate', (time:number) => {
  104. listener?.onTimeUpdate(time/1000);
  105. });
  106. avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
  107. console.info(`AVPlayer state bufferingUpdate success,and infoType value is:${infoType}, value is : ${value}`);
  108. listener?.onBufferedTimeChanged(value);
  109. })
  110. avPlayer.on('videoSizeChange', (width: number, height: number) => {
  111. console.info(`AVPlayer state videoSizeChange success,and width is:${width}, height is : ${height}`);
  112. listener?.onVideoSizeChanged(width, height);
  113. })
  114. }

  116. // 以下示例通过URL设置网络地址来播放直播码流
  117. async avPlayerLiveDemo(playerParam: PlayerParam) {
  118. // 创建avPlayer实例对象
  119. this.avPlayer = await media.createAVPlayer();
  120. // 创建状态机变化回调函数
  121. this.setAVPlayerCallback(this.avPlayer, playerParam.listener);

  123. let mediaSource: media.MediaSource = media.createMediaSourceWithUrl(playerParam.url, playerParam.httpHeaders);
  124. let strategy: media.PlaybackStrategy = {
  125. preferredWidth: 100,
  126. preferredHeight: 100,
  127. preferredBufferDuration: 100,
  128. preferredHdr: false
  129. };
  130. this.avPlayer.setMediaSource(mediaSource, strategy);
  131. console.info(`AVPlayer url:[${playerParam.url}]`);
  132. }

  134. // 按顺序执行待处理的播放控制命令
  135. schedule() {
  136. if (!this.avPlayer) {
  137. return;
  138. }
  139. if (!this.prepared) {
  140. return;
  141. }
  142. if (this.commands.length > 0) {
  143. let command = this.commands.shift();
  144. if (command) {
  145. command.func();
  146. }
  147. if (this.commands.length > 0) {
  148. setTimeout(() => {
  149. this.schedule();
  150. });
  151. }
  152. }
  153. }

  155. private checkCommand(selfName: string, oppositeName: string) {
  156. let index_to_remove = -1;
  157. let ignore_this_action = false;
  158. let index = this.commands.length - 1;
  159. while (index >= 0) {
  160. if (this.commands[index].name == selfName) {
  161. ignore_this_action = true;
  162. break;
  163. }
  164. if (this.commands[index].name == oppositeName) {
  165. index_to_remove = index;
  166. break;
  167. }
  168. index--;
  169. }

  171. let result : CheckPlayCommandResult = {
  172. ignore: ignore_this_action,
  173. index_to_remove: index_to_remove,
  174. };
  175. return result;
  176. }

  178. // 执行播放命令
  179. play() {
  180. let commandName = 'play';
  181. let checkResult = this.checkCommand(commandName, 'pause');
  182. if (checkResult.ignore) {
  183. console.info(`AVPlayer ${commandName} ignored.`);
  184. this.schedule();
  185. return;
  186. }
  187. if (checkResult.index_to_remove >= 0) {
  188. let removedCommand = this.commands.splice(checkResult.index_to_remove, 1);
  189. console.info(`AVPlayer ${JSON.stringify(removedCommand)} removed.`);
  190. return;
  191. }
  192. this.commands.push({ func: ()=>{
  193. console.info('AVPlayer.play()');
  194. this.avPlayer?.play();
  195. }, name: commandName});
  196. this.schedule();
  197. }
  198. // 执行暂停命令
  199. pause() {
  200. let commandName = 'pause';
  201. let checkResult = this.checkCommand(commandName, 'play');
  202. console.info(`checkResult:${JSON.stringify(checkResult)}`);
  203. if (checkResult.ignore) {
  204. console.info(`AVPlayer ${commandName} ignored.`);
  205. this.schedule();
  206. return;
  207. }
  208. if (checkResult.index_to_remove >= 0) {
  209. let removedCommand = this.commands.splice(checkResult.index_to_remove, 1);
  210. console.info(`AVPlayer ${JSON.stringify(removedCommand)} removed.`);
  211. return;
  212. }
  213. this.commands.push({ func: ()=>{
  214. console.info('AVPlayer.pause()');
  215. this.avPlayer?.pause();
  216. }, name: commandName});
  217. this.schedule();
  218. }
  219. // 执行资源释放命令
  220. release() {
  221. this.commands.push({ func: ()=>{
  222. console.info('AVPlayer.release()');
  223. this.avPlayer?.release();
  224. }});
  225. this.schedule();
  226. }
  227. // 执行跳转命令
  228. seek(time: number) {
  229. this.commands.push({ func: ()=>{
  230. console.info(`AVPlayer.seek(${time})`);
  231. this.avPlayer?.seek(time * 1000);
  232. }});
  233. this.schedule();
  234. }
  235. // 执行设置音量命令
  236. setVolume(volume: number) {
  237. this.commands.push({ func: ()=>{
  238. console.info(`AVPlayer.setVolume(${volume})`);
  239. this.avPlayer?.setVolume(volume);
  240. }});
  241. this.schedule();
  242. }
  243. // 执行设置播放速度命令
  244. setPlaybackRate(playbackRate: number) {
  245. let speed = media.PlaybackSpeed.SPEED_FORWARD_1_00_X;
  246. let delta = 0.05;
  247. playbackRate += delta;
  248. if (playbackRate < 1) {
  249. speed = media.PlaybackSpeed.SPEED_FORWARD_0_75_X;
  250. } else if (playbackRate < 1.25) {
  251. speed = media.PlaybackSpeed.SPEED_FORWARD_1_00_X;
  252. } else if (playbackRate < 1.5) {
  253. speed = media.PlaybackSpeed.SPEED_FORWARD_1_25_X;
  254. } else if (playbackRate < 2) {
  255. speed = media.PlaybackSpeed.SPEED_FORWARD_1_75_X;
  256. } else {
  257. speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
  258. }
  259. this.commands.push({ func: ()=>{
  260. console.info(`AVPlayer.setSpeed(${speed})`);
  261. this.avPlayer?.setSpeed(speed);
  262. }});
  263. this.schedule();
  264. }
  265. }
  ```
* 前端页面示例。通过[AVPlayer](media-kit-intro.md#avplayer)托管Web媒体的播放，支持的媒体资源可以参考AVPlayer[支持的格式与协议](media-kit-intro.md#支持的格式与协议)。

  ```
  1. <!-- main.html -->
  2. <html>
  3. <head>
  4. <title>视频托管测试html</title>
  5. <meta name="viewport" content="width=device-width">
  6. </head>
  7. <body>
  8. <div>
  9. <!-- 使用时需要自行替换视频链接 -->
  10. <video src='https://xxx.xxx/demo.mp4' style='width: 100%'></video>
  11. </div>
  12. </body>
  13. </html>
  ```
