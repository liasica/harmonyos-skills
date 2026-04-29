---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-typenode
title: 使用typeNode实现画中画功能开发（ArkTS）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 在应用程序中使用画中画功能 > 使用typeNode实现画中画功能开发（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d5e8cf478e962fd8a5250afa438977c65ecd04104095c03cc5879b06ce26d03a
---

说明

* 从API version 12开始，支持使用typeNode实现画中画功能开发。
* 在HarmonyOS 6.0.0之前，支持在Phone、Tablet设备使用typeNode实现画中画功能开发；从HarmonyOS 6.0.0开始，支持在Phone、PC/2in1、Tablet设备使用typeNode实现画中画功能开发。

该方式适用于任意场景下应用接入画中画功能，以下根据实际开发场景提供四个示例，分别介绍对应场景下画中画功能的实现步骤：

* [应用使用typeNode自由节点（不添加到布局）实现画中画功能](pipwindow-typenode.md#应用使用typenode自由节点不添加到布局实现画中画功能)。
* [应用使用router导航时通过typeNode实现画中画功能](pipwindow-typenode.md#应用使用router导航时通过typenode实现画中画功能)。
* [应用使用Navigation导航时通过typeNode实现画中画功能](pipwindow-typenode.md#应用使用navigation导航时通过typenode实现画中画功能)。
* [应用使用单界面Ability时通过typeNode实现画中画功能](pipwindow-typenode.md#应用使用单界面ability时通过typenode实现画中画功能)。

本文以视频播放为例，介绍通过typeNode实现画中画功能的基本开发步骤。

示例中的视频播放器简易实现参考：

```
1. // model/AVPlayer.ets
2. // 简易播放器实现
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { common } from '@kit.AbilityKit';
5. import { media } from '@kit.MediaKit';
6. import { Logger } from '../util/LogUtil';

8. export class AVPlayer {
9. private avPlayer?: media.AVPlayer;
10. public surfaceID: string = '';

12. setAVPlayerCallback() {
13. this.avPlayer?.on('seekDone', (seekDoneTime: number) => {
14. Logger.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
15. })
16. this.avPlayer?.on('stateChange', async (state, reason) => {
17. if (!this.avPlayer) {
18. return;
19. }
20. switch (state) {
21. case 'idle':
22. this.avPlayer.release();
23. break;
24. case 'initialized':
25. this.avPlayer.surfaceId = this.surfaceID;
26. this.avPlayer.prepare().then(() => {
27. Logger.info('AVPlayer prepare succeeded.');
28. }, (err: BusinessError) => {
29. Logger.error(`Invoke prepare failed, code is ${err.code}, message is ${err.message}`);
30. });
31. break;
32. case 'prepared':
33. this.avPlayer.play();
34. break;
35. case 'stopped':
36. this.avPlayer.reset();
37. break;
38. default:
39. break;
40. }
41. })
42. }

44. async avPlayerFdSrc() {

46. try {
47. this.avPlayer = await media.createAVPlayer();
48. } catch(err) {
49. Logger.error(`create AVPlayer failed`);
50. };
51. this.setAVPlayerCallback();
52. let uiContext = AppStorage.get('UIContext') as UIContext;
53. let context = uiContext.getHostContext() as common.UIAbilityContext;
54. let fileDescriptor = await context.resourceManager.getRawFd('xxx.mp4');

56. if (this.avPlayer) {
57. this.avPlayer.fdSrc = fileDescriptor;
58. }
59. }
60. }
```

## 约束与限制

* 构造PiPConfiguration参数时，建议传入contentWidth和contentHeight参数用以计算画中画初始比例，否则系统将以16:9的比例呈现画中画窗口。
* contentNode支持XComponentType.SURFACE类型，且创建typeNode时必须指定为"XComponent"类型。
* 在关闭画中画时，需要检查自定义组件节点是否释放，避免出现内存泄漏。

## 应用使用typeNode自由节点（不添加到布局）实现画中画功能

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 通过主窗口UIContext创建typeNode节点。
   * 通过create(config: PiPConfiguration, contentNode: typeNode.XComponent)接口创建画中画控制器实例。
   * 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。
   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。
   * 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调。
2. 启动画中画。

   创建画中画控制器实例后，通过startPiP接口启动画中画。
3. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。
4. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画。

```
1. // entryability/EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';
5. import { PipManager } from '../nodefree/PipManager';
6. import { Logger } from '../util/LogUtil';

8. export default class EntryAbility extends UIAbility {
9. // ...
10. onWindowStageCreate(windowStage: window.WindowStage): void {
11. // Main window is created, set main page for this ability
12. Logger.info('testTag', '%{public}s', 'Ability onWindowStageCreate');
13. let windowClass: window.Window | undefined = undefined;
14. let windowClassId: number = -1;

16. windowStage.getMainWindow().then((window) => {
17. if (window == null) {
18. Logger.error('Failed to obtaining the window. Cause: The data is empty');
19. return;
20. }
21. windowClass = window;
22. windowClass.setUIContent('pages/Index');
23. windowClassId = windowClass.getWindowProperties().id;
24. AppStorage.setOrCreate('windowId', windowClassId);
25. Logger.info('Succeeded in obtaining the window')

27. let ctx = window.getUIContext();
28. AppStorage.setOrCreate('UIContext', ctx);
29. // 通过主窗口UIContext创建typeNode节点
30. PipManager.getInstance().makeTypeNode(ctx);
31. }).catch((err: BusinessError) => {
32. Logger.error(`Failed to obtaining the window. Cause code: ${err.code}, message: ${err.message}`);
33. });
34. windowStage.loadContent('pages/Index', (err) => {
35. if (err.code) {
36. Logger.error('testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
37. return;
38. }
39. Logger.info('testTag', 'Succeeded in loading the content.');
40. });
41. }
42. // ...
43. }
```

```
1. // pages/Index.ets
2. // 应用首页
3. import { router } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. pathStack: NavPathStack = new NavPathStack();

10. build() {
11. Navigation(this.pathStack) {
12. Scroll() {
13. Flex({ direction: FlexDirection.Column }) {
14. // ...
15. this.featureButton('使用TypeNode自由节点实现画中画', this.typeNodeFree);
16. // ...
17. }
18. }
19. }
20. .hideBackButton(true)
21. .titleMode(NavigationTitleMode.Mini)
22. .backgroundColor('#FFF1F3F5')
23. .mode(NavigationMode.Stack)
24. .title('画中画SampleCode')
25. }

27. @Builder
28. featureButton(buttonText: string, callbackOnClick: () => void) {
29. Button({ type: ButtonType.Normal }) {
30. Row() {
31. Column() {
32. Text(buttonText)
33. .fontSize(24)
34. .fontWeight(FontWeight.Bold)
35. .fontColor('#000000')
36. Rect()
37. .radius(1)
38. .fill('#0A59F7')
39. .height(2)
40. .width(30)
41. }
42. .width('100%')
43. .alignItems(HorizontalAlign.Start)
44. }
45. .width('100%')
46. }
47. .width('90%')
48. .padding('5%')
49. .margin({ top: '3%', bottom: '2%', right: '3%' })
50. .backgroundColor('#FFFFFF')
51. .borderRadius(20)
52. .onClick(callbackOnClick)
53. }

55. // ...
56. private typeNodeFree = () => {
57. this.getUIContext().getRouter().pushUrl({ url: 'pages/TypeNodeFreePage' }, router.RouterMode.Standard)
58. }
59. // ...
60. }
```

```
1. // pages/TypeNodeFreePage.ets
2. // 该页面用于展示应用布局文件，创建的typeNode节点不会添加到该布局中
3. import { PipManager } from '../nodefree/PipManager';
4. import { Logger } from '../util/LogUtil';

6. const TAG = 'TypeNodeFreePage'
7. @Entry
8. @Component
9. struct TypeNodeFreePage {
10. build() {
11. Column() {
12. Text('This is MainPage')
13. .fontSize(30)
14. .fontWeight(FontWeight.Bold)
15. .margin({ bottom: 20 })

17. Text('This is not typeNode')
18. .size({ width: '100%', height: '800px' })
19. .fontSize(30)
20. .textAlign(TextAlign.Center)
21. .fontWeight(FontWeight.Bold)
22. .backgroundColor('#4d5b5858')

24. Row({ space: 20 }) {
25. Button('startPip') // 启动画中画
26. .onClick(() => {
27. PipManager.getInstance().startPip();
28. })

30. Button('stopPip') // 停止画中画
31. .onClick(() => {
32. PipManager.getInstance().stopPip();
33. })

35. Button('updateSize') // 更新视频尺寸
36. .onClick(() => {
37. PipManager.getInstance().updateContentSize(900, 1600);
38. })
39. }
40. .backgroundColor('#4da99797')
41. .size({ width: '100%', height: 60 })
42. .justifyContent(FlexAlign.SpaceAround)
43. }
44. .justifyContent(FlexAlign.Center)
45. .width('100%')
46. .height('100%')
47. }

49. aboutToDisappear(): void {
50. PipManager.getInstance().unregisterPipStateChangeListener(); // 注销画中画生命周期及状态回调
51. }

53. onPageShow(): void {
54. Logger.info(TAG, 'onPageShow')
55. PipManager.getInstance().init(this.getUIContext().getHostContext() as Context); // 创建画中画控制器
56. PipManager.getInstance().setAutoStart(true); // 设置应用退后台时自动启动画中画
57. }

59. onPageHide(): void {
60. Logger.info(TAG, 'onPageHide')
61. PipManager.getInstance().setAutoStart(false);
62. }
63. }
```

```
1. // nodeFree/PipManager.ets
2. // 画中画控制器单例
3. import { PiPWindow, typeNode } from '@kit.ArkUI'; // 引入PiPWindow模块
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { AVPlayer} from '../model/AVPlayer';
6. import { Logger } from '../util/LogUtil';

8. // 自定义XComponentController
9. class CustomXComponentController extends XComponentController {
10. // 监听onSurfaceCreated，并将surfaceId设置给播放器
11. onSurfaceCreated(surfaceId: string): void {
12. Logger.info(TAG, `onSurfaceCreated surfaceId: ${surfaceId}`);
13. if (PipManager.getInstance().player.surfaceID === surfaceId) {
14. return;
15. }
16. PipManager.getInstance().player.surfaceID = surfaceId;
17. PipManager.getInstance().player.avPlayerFdSrc();
18. }

20. onSurfaceDestroyed(surfaceId: string): void {
21. Logger.info(TAG, `onSurfaceDestroyed surfaceId: ${surfaceId}`);
22. }
23. }

25. const TAG = 'PipManager';

27. export class PipManager {
28. public player: AVPlayer;
29. private static instance: PipManager = new PipManager();
30. private pipController?: PiPWindow.PiPController = undefined;
31. private mXComponentController: XComponentController;
32. private xComponent: typeNode.XComponent| null = null; // typeNode节点

34. public static getInstance(): PipManager {
35. return PipManager.instance;
36. }

38. constructor() {
39. this.player = new AVPlayer();
40. this.mXComponentController = new CustomXComponentController();
41. }

43. onActionEvent(control: PiPWindow.ControlEventParam) {
44. switch (control.controlType) {
45. case PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE:
46. if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
47. //停止视频
48. } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
49. //播放视频
50. }
51. break;
52. case PiPWindow.PiPControlType.VIDEO_NEXT:
53. // 切换到下一个视频
54. break;
55. case PiPWindow.PiPControlType.VIDEO_PREVIOUS:
56. // 切换到上一个视频
57. break;
58. case PiPWindow.PiPControlType.FAST_FORWARD:
59. // 视频进度快进
60. break;
61. case PiPWindow.PiPControlType.FAST_BACKWARD:
62. // 视频进度后退
63. break;
64. default:
65. break;
66. }
67. Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
68. }

70. // 监听画中画生命周期
71. onStateChange(state: PiPWindow.PiPState, reason: string) {
72. let curState: string = '';
73. switch (state) {
74. case PiPWindow.PiPState.ABOUT_TO_START:
75. curState = 'ABOUT_TO_START';
76. break;
77. case PiPWindow.PiPState.STARTED:
78. curState = 'STARTED';
79. break;
80. case PiPWindow.PiPState.ABOUT_TO_STOP:
81. curState = 'ABOUT_TO_STOP';
82. break;
83. case PiPWindow.PiPState.STOPPED:
84. curState = 'STOPPED';
85. break;
86. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
87. curState = 'ABOUT_TO_RESTORE';
88. break;
89. case PiPWindow.PiPState.ERROR:
90. curState = 'ERROR';
91. break;
92. default:
93. break;
94. }
95. Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
96. }

98. // 注销监听
99. unregisterPipStateChangeListener() {
100. Logger.info(TAG, 'aboutToDisappear');
101. this.pipController?.off('stateChange');
102. this.pipController?.off('controlEvent');
103. }

105. getXComponentController(): CustomXComponentController {
106. return this.mXComponentController;
107. }

109. // 步骤1：创建画中画控制器，注册生命周期事件以及控制事件回调
110. init(ctx: Context) {
111. if (this.pipController !== null && this.pipController != undefined) {
112. return;
113. }
114. Logger.info(TAG, 'onPageShow');
115. if (!PiPWindow.isPiPEnabled()) {
116. Logger.error(TAG, `picture in picture disabled for current OS`);
117. return;
118. }

120. let config: PiPWindow.PiPConfiguration = {
121. context: ctx,
122. componentController: this.getXComponentController(),
123. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
124. contentWidth: 1920, // 使用typeNode启动画中画时，contentWidth需设置为大于0的值，否则将设置为16:9默认比例
125. contentHeight: 1080, // 使用typeNode启动画中画时，contentHeight需设置为大于0的值，否则将设置为16:9默认比例
126. };
127. // 通过create接口创建画中画控制器实例

129. PiPWindow.create(config, this.xComponent).then((controller: PiPWindow.PiPController) => {
130. this.pipController = controller;
131. // 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画
132. this.pipController.setAutoStartEnabled(true);
133. // 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调
134. this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
135. this.onStateChange(state, reason);
136. });
137. // 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调
138. this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
139. this.onActionEvent(control);
140. });
141. }).catch((err: BusinessError) => {
142. Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
143. });
144. }

146. // 步骤2：创建画中画控制器实例后，通过startPiP接口启动画中画
147. startPip() {
148. this.pipController?.startPiP().then(() => {
149. Logger.info(TAG, `Succeeded in starting pip.`);
150. }).catch((err: BusinessError) => {
151. Logger.error(TAG, `Failed to start pip. Cause:${err.code}, message:${err.message}`);
152. });
153. }

155. // 步骤3：更新媒体源尺寸信息
156. updateContentSize(width: number, height: number) {
157. if (this.pipController) {
158. this.pipController.updateContentSize(width, height);
159. }
160. }

162. // 步骤4：关闭画中画
163. stopPip() {
164. if (this.pipController === null || this.pipController === undefined) {
165. return;
166. }
167. let promise: Promise<void> = this.pipController.stopPiP();
168. promise.then(() => {
169. Logger.info(TAG, `Succeeded in stopping pip.`);
170. }).catch((err: BusinessError) => {
171. Logger.error(TAG, `Failed to stop pip. Cause:${err.code}, message:${err.message}`);
172. });
173. }

175. setAutoStart(autoStart: boolean): void {
176. this.pipController?.setAutoStartEnabled(autoStart);
177. }

179. // 创建typeNode节点
180. makeTypeNode(ctx: UIContext) {
181. if (this.xComponent === null || this.xComponent === undefined) {
182. // 创建XComponent类型的typeNode
183. this.xComponent = typeNode.createNode(ctx, 'XComponent', {
184. // 类型设置为SURFACE
185. type: XComponentType.SURFACE,
186. // 设置XComponentController
187. controller: PipManager.getInstance().getXComponentController(),
188. });
189. }
190. }
191. }
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/dFz3oNNOSDCC6SYosL3f9A/zh-cn_image_0000002589324541.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052903Z&HW-CC-Expire=86400&HW-CC-Sign=D57F19283FB9F799EC3394791CB04A820E72B7ADBEF125EC4F1A9DD9BE87AE7E)

## 应用使用router导航时通过typeNode实现画中画功能

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 创建自定义NodeController，实现makeNode方法，在该方法中创建typeNode。
   * 通过create(config: PiPConfiguration, contentNode: typeNode.XComponent)接口创建画中画控制器实例。
   * 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。
   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。
   * 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调。
2. 启动画中画。

   创建画中画控制器实例后，通过startPiP接口启动画中画，在画中画ABOUT\_TO\_START生命周期将typeNode节点从布局移除，并返回上级界面（可选）。如果启动画中画时返回了上级界面，需要在画中画ABOUT\_TO\_RESTORE（还原）时重新跳转到原界面。
3. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。
4. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画，在画中画ABOUT\_TO\_STOP生命周期将typeNode节点重新添加到布局中。

```
1. // entryability/EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';
5. import { PipManager } from '../nodefree/PipManager';
6. import { Logger } from '../util/LogUtil';

8. export default class EntryAbility extends UIAbility {
9. // ...
10. onWindowStageCreate(windowStage: window.WindowStage): void {
11. // ...
12. windowStage.loadContent('pages/Index', (err) => {
13. // ...
14. });
15. }
16. // ...
17. }
```

```
1. // pages/RouterImplementPage.ets
2. import { PipManager } from '../route/PipManager';
3. import { PiPWindow, router, Router } from '@kit.ArkUI'; // 引入PiPWindow模块
4. import { Logger } from '../util/LogUtil';

6. const TAG = 'RouterImplementPage'
7. @Entry
8. @Component
9. struct RouterImplementPage {
10. private page1: string = 'route/Page1';
11. private pageRouter: Router | null = null;

13. // 画中画生命周期事件监听，用于页面及节点操作
14. private callback: Function = (state: PiPWindow.PiPState) => {
15. Logger.info(TAG, `pipStateChange: state ${state}`);
16. if (state === PiPWindow.PiPState.ABOUT_TO_START) {
17. // 返回到上级页面（可选）
18. this.pageRouter?.back();
19. } else if (state === PiPWindow.PiPState.ABOUT_TO_STOP) {
20. // 重新将typeNode节点添加到布局中，例如还原场景
21. PipManager.getInstance().addNode();
22. } else if (state === PiPWindow.PiPState.ABOUT_TO_RESTORE) {
23. // 如果在ABOUT_TO_START时返回了上级界面，需要还原时push到原界面
24. this.jumpNext();
25. }
26. };

28. aboutToAppear(): void {
29. this.pageRouter = this.getUIContext().getRouter();
30. PipManager.getInstance().registerLifecycleCallback(this.callback);
31. }

33. aboutToDisappear(): void {
34. PipManager.getInstance().unregisterPipStateChangeListener();
35. PipManager.getInstance().unRegisterLifecycleCallback(this.callback);
36. }

38. jumpNext(): void {
39. let topPage = this.pageRouter?.getState();
40. if (topPage !== undefined && (this.page1.toString() === topPage.path + topPage.name)) {
41. Logger.info(TAG, `page1 aready at top`)
42. return;
43. }
44. this.pageRouter?.pushUrl({
45. url: this.page1 // 目标url
46. }, router.RouterMode.Standard, (err) => {
47. if (err) {
48. Logger.error(TAG, `Invoke pushUrl failed, code is ${err.code}: ${err.message}`);
49. return;
50. }
51. Logger.info(TAG, 'Invoke pushUrl succeeded.');
52. });
53. }

55. build() {
56. Row() {
57. Column() {
58. Text('Main Page')
59. .fontSize(50)
60. .fontWeight(FontWeight.Bold)

62. Button('Jump Next')
63. .onClick(() => {
64. this.jumpNext();
65. })
66. .margin({ top: 16, bottom: 16 })
67. }
68. .width('100%')
69. }
70. .height('100%')
71. }
72. }
```

```
1. // route/Page1.ets
2. import { PipManager } from '../route/PipManager';
3. import { Logger } from '../util/LogUtil';

5. const TAG = 'Page1';

7. @Entry
8. @Component
9. export struct Page1 {
10. build() {
11. Column() {
12. Text('This is Page1')
13. .fontSize(30)
14. .fontWeight(FontWeight.Bold)
15. .margin({bottom: 20})

17. // 将typeNode添加到页面布局中
18. NodeContainer(PipManager.getInstance().getNodeController())
19. .size({ width: '100%', height: '800px' })

21. Row({ space: 20 }) {
22. Button('startPip')// 启动画中画
23. .onClick(() => {
24. PipManager.getInstance().startPip();
25. })

27. Button('stopPip')// 停止画中画
28. .onClick(() => {
29. PipManager.getInstance().stopPip();
30. })

32. Button('updateSize')// 更新视频尺寸
33. .onClick(() => {
34. // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
35. // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
36. PipManager.getInstance().updateContentSize(900, 1600);
37. })
38. }
39. .backgroundColor('#4da99797')
40. .size({ width: '100%', height: 60 })
41. .justifyContent(FlexAlign.SpaceAround)
42. }
43. .justifyContent(FlexAlign.Center)
44. .width('100%')
45. .height('100%')
46. }

48. onPageShow(): void {
49. Logger.info(TAG, 'onPageShow')
50. PipManager.getInstance().initPipController(this.getUIContext().getHostContext() as Context);
51. PipManager.getInstance().setAutoStart(true);
52. }

54. onPageHide(): void {
55. Logger.info(TAG, 'onPageHide')
56. PipManager.getInstance().setAutoStart(false);
57. PipManager.getInstance().removeNode();
58. }
59. }
```

```
1. // route/PipManager.ets
2. import { PiPWindow, typeNode } from '@kit.ArkUI'; // 引入PiPWindow模块
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { XCNodeController } from './XCNodeController';
5. import { AVPlayer } from '../model/AVPlayer';
6. import { Logger } from '../util/LogUtil';

8. export class CustomXComponentController extends XComponentController {
9. onSurfaceCreated(surfaceId: string): void {
10. Logger.info(TAG, `onSurfaceCreated surfaceId: ${surfaceId}`);
11. if (PipManager.getInstance().player.surfaceID === surfaceId) {
12. return;
13. }
14. // 将surfaceId设置给媒体源
15. PipManager.getInstance().player.surfaceID = surfaceId;
16. PipManager.getInstance().player.avPlayerFdSrc();
17. }

19. onSurfaceDestroyed(surfaceId: string): void {
20. Logger.info(TAG, `onSurfaceDestroyed surfaceId: ${surfaceId}`);
21. }
22. }

24. const TAG = 'PipManager';

26. export class PipManager {
27. private static instance: PipManager = new PipManager();
28. private pipController?: PiPWindow.PiPController = undefined;
29. private xcNodeController: XCNodeController;
30. private mXComponentController: XComponentController;
31. private lifeCycleCallback: Set<Function> = new Set();
32. public player: AVPlayer;

34. public static getInstance(): PipManager {
35. return PipManager.instance;
36. }

38. constructor() {
39. this.xcNodeController = new XCNodeController();
40. this.player = new AVPlayer();
41. this.mXComponentController = new CustomXComponentController();
42. }

44. public registerLifecycleCallback(callBack: Function) {
45. this.lifeCycleCallback.add(callBack);
46. }

48. public unRegisterLifecycleCallback(callBack: Function): void {
49. this.lifeCycleCallback.delete(callBack);
50. }

52. getNode(): typeNode.XComponent | null {
53. return this.xcNodeController.getNode();
54. }

56. onActionEvent(control: PiPWindow.ControlEventParam) {
57. switch (control.controlType) {
58. case PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE:
59. if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
60. //停止视频
61. } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
62. //播放视频
63. }
64. break;
65. case PiPWindow.PiPControlType.VIDEO_NEXT:
66. // 切换到下一个视频
67. break;
68. case PiPWindow.PiPControlType.VIDEO_PREVIOUS:
69. // 切换到上一个视频
70. break;
71. case PiPWindow.PiPControlType.FAST_FORWARD:
72. // 视频进度快进
73. break;
74. case PiPWindow.PiPControlType.FAST_BACKWARD:
75. // 视频进度后退
76. break;
77. default:
78. break;
79. }
80. Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
81. }

83. onStateChange(state: PiPWindow.PiPState, reason: string) {
84. let curState: string = '';
85. this.xcNodeController.setCanAddNode(
86. state === PiPWindow.PiPState.ABOUT_TO_STOP || state === PiPWindow.PiPState.STOPPED)
87. if (this.lifeCycleCallback !== null) {
88. this.lifeCycleCallback.forEach((fun) => {
89. fun(state)
90. });
91. }
92. switch (state) {
93. case PiPWindow.PiPState.ABOUT_TO_START:
94. curState = 'ABOUT_TO_START';
95. // 将typeNode节点从布局移除
96. this.xcNodeController.removeNode();
97. break;
98. case PiPWindow.PiPState.STARTED:
99. curState = 'STARTED';
100. break;
101. case PiPWindow.PiPState.ABOUT_TO_STOP:
102. curState = 'ABOUT_TO_STOP';
103. this.xcNodeController.dispose();
104. break;
105. case PiPWindow.PiPState.STOPPED:
106. curState = 'STOPPED';
107. break;
108. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
109. curState = 'ABOUT_TO_RESTORE';
110. break;
111. case PiPWindow.PiPState.ERROR:
112. curState = 'ERROR';
113. break;
114. default:
115. break;
116. }
117. Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
118. }

120. unregisterPipStateChangeListener() {
121. Logger.info(`${TAG} aboutToDisappear`)
122. this.pipController?.off('stateChange');
123. this.pipController?.off('controlEvent');
124. this.pipController = undefined;
125. }

127. getXComponentController(): CustomXComponentController {
128. return this.mXComponentController;
129. }

131. // 步骤1：创建画中画控制器，注册生命周期事件以及控制事件回调
132. initPipController(ctx: Context) {
133. if (this.pipController !== null && this.pipController != undefined) {
134. return;
135. }
136. Logger.info(`${TAG} onPageShow`)
137. if (!PiPWindow.isPiPEnabled()) {
138. Logger.error(TAG, `picture in picture disabled for current OS`);
139. return;
140. }
141. let config: PiPWindow.PiPConfiguration = {
142. context: ctx,
143. componentController: this.getXComponentController(),
144. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
145. contentWidth: 1920, // 使用typeNode启动画中画时，contentWidth需设置为大于0的值，否则创建画中画失败
146. contentHeight: 1080, // 使用typeNode启动画中画时，contentHeight需设置为大于0的值，否则创建画中画失败
147. };
148. // 通过create接口创建画中画控制器实例

150. PiPWindow.create(config, this.getNode()).then((controller: PiPWindow.PiPController) => {
151. this.pipController = controller;
152. // 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画
153. this.pipController.setAutoStartEnabled(true)
154. // 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调
155. this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
156. this.onStateChange(state, reason);
157. });
158. // 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调
159. this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
160. this.onActionEvent(control);
161. });
162. }).catch((err: BusinessError) => {
163. Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
164. });
165. }

167. // 步骤2：启动画中画
168. startPip() {
169. this.pipController?.startPiP().then(() => {
170. Logger.info(TAG, `Succeeded in starting pip.`);
171. }).catch((err: BusinessError) => {
172. Logger.error(TAG, `Failed to start pip. Cause:${err.code}, message:${err.message}`);
173. });
174. }

176. // 步骤3：更新媒体源尺寸信息
177. updateContentSize(width: number, height: number) {
178. if (this.pipController) {
179. this.pipController.updateContentSize(width, height);
180. }
181. }

183. // 步骤4：关闭画中画
184. stopPip() {
185. if (this.pipController) {
186. let promise: Promise<void> = this.pipController.stopPiP();
187. promise.then(() => {
188. Logger.info(TAG, `Succeeded in stopping pip.`);
189. }).catch((err: BusinessError) => {
190. Logger.error(TAG, `Failed to stop pip. Cause:${err.code}, message:${err.message}`);
191. });
192. }
193. }

195. getNodeController(): XCNodeController {
196. Logger.info(TAG, `getNodeController.`);
197. return this.xcNodeController;
198. }

200. setAutoStart(autoStart: boolean): void {
201. this.pipController?.setAutoStartEnabled(autoStart);
202. }

204. removeNode(): void {
205. this.xcNodeController.removeNode();
206. }

208. addNode(): void {
209. this.xcNodeController.addNode();
210. }
211. }
```

```
1. // route/XCNodeController.ets
2. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';
3. import { PipManager } from './PipManager';
4. import { Logger } from '../util/LogUtil';

6. const TAG = 'XCNodeController';
7. // 创建自定义NodeController
8. export class XCNodeController extends NodeController {
9. public xComponent: typeNode.XComponent | null = null;
10. private node: FrameNode | null = null;
11. private canAddNode: boolean = true;

13. // 设置是否可以添加节点
14. setCanAddNode(canAddNode: boolean) {
15. this.canAddNode = canAddNode;
16. }

18. // 实现makeNode方法，当自定义NodeController被添加到布局时，该方法会被调用
19. makeNode(context: UIContext): FrameNode | null {
20. this.node = new FrameNode(context);
21. this.node.commonAttribute
22. if (this.xComponent === null || this.xComponent === undefined) {
23. // 创建XComponent类型的typeNode
24. this.xComponent = typeNode.createNode(context, 'XComponent', {
25. // 类型设置为SURFACE
26. type: XComponentType.SURFACE,
27. // 设置XComponentController
28. controller: PipManager.getInstance().getXComponentController(),
29. });
30. }
31. if (this.canAddNode) {

33. try {
34. this.xComponent.getParent()?.removeChild(this.xComponent);
35. } catch (error) {
36. Logger.error(TAG, 'Failed to removeChild');
37. }
38. try {
39. this.node.appendChild(this.xComponent);
40. } catch (error) {
41. Logger.error(TAG, 'Failed to appendChild');
42. }
43. }
44. return this.node;
45. }

47. // 重新添加typeNode节点
48. addNode() {
49. if (this.node !== null && this.node !== undefined) {
50. Logger.info(TAG, 'addNode');

52. try {
53. this.node.appendChild(this.xComponent);
54. } catch (error) {
55. Logger.error(TAG, 'Failed to appendChild');
56. }
57. }
58. }

60. // 移除typeNode节点
61. removeNode() {
62. if (this.node !== null && this.node !== undefined) {
63. Logger.info(TAG, 'removeNode');

65. try {
66. this.node.removeChild(this.xComponent);
67. } catch (error) {
68. Logger.error(TAG, 'Failed to removeChild');
69. }
70. }
71. }

73. getNode(): typeNode.XComponent | null {
74. Logger.info(TAG, 'getNode is null: '+ (this.xComponent === null || this.xComponent === undefined));
75. return this.xComponent;
76. }

78. // 开发者需要定义该方法实现布局的注销，避免内存泄漏
79. dispose() {
80. Logger.info(TAG, 'execute node dispose');
81. if (this.node !== null) {
82. this.node.dispose();
83. }
84. }
85. }
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/LqdWzU3RR46zMfACWsDihg/zh-cn_image_0000002558764670.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052903Z&HW-CC-Expire=86400&HW-CC-Sign=D651059D9F46F0ECA51309DD8C4FC4AF27C39395CE416700D7E41650B1BC9AD3)

## 应用使用Navigation导航时通过typeNode实现画中画功能

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 创建自定义NodeController，实现makeNode方法，在该方法中创建typeNode。
   * 通过create(config: PiPConfiguration, contentNode: typeNode.XComponent)接口创建画中画控制器实例。
   * 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。
   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。
   * 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调。
2. 启动画中画。

   创建画中画控制器实例后，通过startPiP接口启动画中画，在画中画ABOUT\_TO\_START生命周期将typeNode节点从布局移除，并返回上级界面（可选）。如果启动画中画时返回了上级界面，需要在画中画ABOUT\_TO\_RESTORE（还原）时重新跳转到原界面。
3. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。
4. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画，在画中画ABOUT\_TO\_STOP生命周期将typeNode节点重新添加到布局中。

```
1. // entryability/EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';
5. import { PipManager } from '../nodefree/PipManager';
6. import { Logger } from '../util/LogUtil';

8. export default class EntryAbility extends UIAbility {
9. // ...
10. onWindowStageCreate(windowStage: window.WindowStage): void {
11. // ...
12. windowStage.loadContent('pages/Index', (err) => {
13. // ...
14. });
15. }
16. // ...
17. }
```

```
1. // pages/NavigationImplementPage.ets
2. import { PipManager } from '../navigation/PipManager';
3. import { Page1 } from '../navigation/Page1';
4. import { PiPWindow } from '@kit.ArkUI';
5. import { Logger } from '../util/LogUtil';

7. const TAG = 'NavigationImplementPage';

9. @Entry
10. @Component
11. struct NavigationImplementPage {
12. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
13. // 画中画生命周期事件监听，用于页面及节点操作
14. private callback: Function = (state: PiPWindow.PiPState) => {
15. Logger.info(TAG, `pipStateChange: state ${state}`);
16. if (state === PiPWindow.PiPState.ABOUT_TO_START) {
17. // 返回到上级页面（可选）
18. this.pageInfos.pop();
19. } else if (state === PiPWindow.PiPState.ABOUT_TO_STOP) {
20. // 重新将typeNode节点添加到布局中，例如还原场景
21. PipManager.getInstance().addNode();
22. } else if (state === PiPWindow.PiPState.ABOUT_TO_RESTORE) {
23. // 如果在ABOUT_TO_START时返回了上级界面，需要还原时push到原界面
24. this.jumpNext();
25. }
26. };

28. jumpNext() {
29. if (this.pageInfos.getAllPathName()[0] === 'Page1') {
30. Logger.info(TAG, 'Page1 already at top');
31. return;
32. }
33. this.pageInfos.pushPath({ name: 'Page1' });
34. }

36. aboutToAppear(): void {
37. PipManager.getInstance().registerLifecycleCallback(this.callback);
38. }

40. aboutToDisappear(): void {
41. PipManager.getInstance().unregisterPipStateChangeListener();
42. PipManager.getInstance().unRegisterLifecycleCallback(this.callback);
43. }

45. @Builder
46. PageMap(name: string) {
47. if (name === 'Page1') {
48. Page1();
49. }
50. }

52. build() {
53. Navigation(this.pageInfos) {
54. Column() {
55. Text('This is Main Page')
56. Column()
57. .height('200px')
58. Row({ space: 12 }) {
59. Button('Jump Page1')
60. .width('80%')
61. .height(40)
62. .margin(20)
63. .onClick(() => {
64. this.jumpNext();
65. })
66. }
67. }
68. .height('100%')
69. .width('100%')
70. .justifyContent(FlexAlign.Center)
71. .backgroundColor('#DCDCDC')
72. }
73. .title('MainTitle')
74. .navDestination(this.PageMap)
75. }
76. }
```

```
1. // navigation/Page1.ets
2. import { PipManager } from './PipManager';
3. import { Logger } from '../util/LogUtil';

5. const TAG = 'Page1';

7. @Entry
8. @Component
9. export struct Page1 {
10. build() {
11. NavDestination() {
12. Column() {
13. Text('This is Page1')
14. .fontSize(30)
15. .fontWeight(FontWeight.Bold)
16. .margin({ bottom: 20 })

18. // 将typeNode添加到页面布局中
19. NodeContainer(PipManager.getInstance().getNodeController())
20. .size({ width: '100%', height: '800px' })

22. Row({ space: 20 }) {
23. Button('startPip') // 启动画中画
24. .onClick(() => {
25. PipManager.getInstance().startPip();
26. })
27. Button('stopPip') // 停止画中画
28. .onClick(() => {
29. PipManager.getInstance().stopPip();
30. })
31. Button('updateSize') // 更新视频尺寸
32. .onClick(() => {
33. // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
34. // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
35. PipManager.getInstance().updateContentSize(900, 1600);
36. })
37. }
38. .backgroundColor('#4da99797')
39. .size({ width: '100%', height: 60 })
40. .justifyContent(FlexAlign.SpaceAround)
41. }
42. .justifyContent(FlexAlign.Center)
43. .width('100%')
44. .height('100%')
45. }
46. .title('page1')
47. .onShown(() => {
48. Logger.info(TAG, 'onShown')
49. PipManager.getInstance().init(this.getUIContext().getHostContext() as Context);
50. PipManager.getInstance().setAutoStart(true);
51. })
52. .onHidden(() => {
53. Logger.info(TAG, 'onHidden')
54. PipManager.getInstance().setAutoStart(false);
55. PipManager.getInstance().removeNode();
56. })
57. }
58. }
```

```
1. // navigation/XCNodeController.ets
2. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';
3. import { PipManager } from './PipManager';
4. import { Logger } from '../util/LogUtil';

6. const TAG = 'XCNodeController';

8. // 创建自定义NodeController
9. export class XCNodeController extends NodeController {
10. public xComponent: typeNode.XComponent| null = null;
11. private node: FrameNode | null = null;
12. private canAddNode: boolean = true;

14. // 设置是否可以添加节点
15. setCanAddNode(canAddNode: boolean) {
16. this.canAddNode = canAddNode;
17. }

19. // 实现makeNode方法，当自定义NodeController被添加到布局时，该方法会被调用
20. makeNode(context: UIContext): FrameNode | null {
21. Logger.info(TAG, 'makeNode');
22. this.node = new FrameNode(context);
23. if (this.xComponent === null || this.xComponent === undefined) {
24. // 创建XComponent类型的typeNode
25. this.xComponent = typeNode.createNode(context, 'XComponent', {
26. type: XComponentType.SURFACE, // 类型设置为SURFACE
27. controller: PipManager.getInstance().getXComponentController(), // 设置XComponentController
28. });
29. }
30. if (this.canAddNode) {

32. try {
33. this.xComponent.getParent()?.removeChild(this.xComponent);
34. } catch (error) {
35. Logger.error(TAG, 'Failed to removeChild');
36. }
37. try {
38. this.node.appendChild(this.xComponent);
39. } catch (error) {
40. Logger.error(TAG, 'Failed to appendChild');
41. }
42. }
43. return this.node;
44. }

46. // 重新添加typeNode节点
47. addNode() {
48. if (this.node !== null && this.node !== undefined) {
49. Logger.info(TAG, 'addNode id:'+(this.node?.getUniqueId())+' '+this.xComponent?.getUniqueId());
50. try {
51. this.node.appendChild(this.xComponent);
52. } catch (error) {
53. Logger.error(TAG, 'Failed to appendChild');
54. }
55. }
56. }

58. // 移除typeNode节点
59. removeNode() {
60. if (this.node !== null && this.node !== undefined) {
61. Logger.info(TAG, 'removeNode');

63. try {
64. this.node.removeChild(this.xComponent);
65. } catch (error) {
66. Logger.error(TAG, 'Failed to removeChild');
67. }
68. }
69. }

71. getNode(): typeNode.XComponent | null {
72. Logger.info(TAG, 'getNode is null:'+ (this.xComponent === null || this.xComponent === undefined))
73. return this.xComponent;
74. }

76. // 开发者需要定义该方法实现布局的注销，避免内存泄漏
77. dispose() {
78. Logger.info(TAG, 'execute node dispose');
79. if (this.node !== null) {
80. this.node.dispose();
81. }
82. }
83. }
```

```
1. // navigation/PipManager.ets
2. import { PiPWindow, typeNode } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { XCNodeController } from './XCNodeController';
5. import { AVPlayer } from '../model/AVPlayer';
6. import { Logger } from '../util/LogUtil';

8. export class CustomXComponentController extends XComponentController {
9. onSurfaceCreated(surfaceId: string): void {
10. Logger.info(TAG, `onSurfaceCreated surfaceId: ${surfaceId}`);
11. if (PipManager.getInstance().player.surfaceID === surfaceId) {
12. return;
13. }
14. // 将surfaceId设置给媒体源
15. PipManager.getInstance().player.surfaceID = surfaceId;
16. PipManager.getInstance().player.avPlayerFdSrc();
17. }

19. onSurfaceDestroyed(surfaceId: string): void {
20. Logger.info(TAG, `onSurfaceDestroyed surfaceId: ${surfaceId}`);
21. }
22. }

24. const TAG = 'PipManager';

26. export class PipManager {
27. private static instance: PipManager = new PipManager();
28. private pipController?: PiPWindow.PiPController = undefined;
29. private xcNodeController: XCNodeController;
30. private mXComponentController: XComponentController;
31. private lifeCycleCallback: Set<Function> = new Set();
32. public player: AVPlayer;

34. public static getInstance(): PipManager {
35. return PipManager.instance;
36. }

38. constructor() {
39. this.xcNodeController = new XCNodeController();
40. this.player = new AVPlayer();
41. this.mXComponentController = new CustomXComponentController();
42. }

44. public registerLifecycleCallback(callBack: Function) {
45. this.lifeCycleCallback.add(callBack);
46. }

48. public unRegisterLifecycleCallback(callBack: Function): void {
49. this.lifeCycleCallback.delete(callBack);
50. }

52. getNode(): typeNode.XComponent | null {
53. return this.xcNodeController.getNode();
54. }

56. onActionEvent(control: PiPWindow.ControlEventParam) {
57. switch (control.controlType) {
58. case PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE:
59. if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
60. //停止视频
61. } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
62. //播放视频
63. }
64. break;
65. case PiPWindow.PiPControlType.VIDEO_NEXT:
66. // 切换到下一个视频
67. break;
68. case PiPWindow.PiPControlType.VIDEO_PREVIOUS:
69. // 切换到上一个视频
70. break;
71. case PiPWindow.PiPControlType.FAST_FORWARD:
72. // 视频进度快进
73. break;
74. case PiPWindow.PiPControlType.FAST_BACKWARD:
75. // 视频进度后退
76. break;
77. default:
78. break;
79. }
80. Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
81. }

83. onStateChange(state: PiPWindow.PiPState, reason: string) {
84. let curState: string = '';
85. this.xcNodeController.setCanAddNode(
86. state === PiPWindow.PiPState.ABOUT_TO_STOP || state === PiPWindow.PiPState.STOPPED)
87. if (this.lifeCycleCallback !== null) {
88. this.lifeCycleCallback.forEach((fun) => {
89. fun(state);
90. });
91. }
92. switch (state) {
93. case PiPWindow.PiPState.ABOUT_TO_START:
94. curState = 'ABOUT_TO_START';
95. // 将typeNode节点从布局移除
96. this.xcNodeController.removeNode();
97. break;
98. case PiPWindow.PiPState.STARTED:
99. curState = 'STARTED';
100. break;
101. case PiPWindow.PiPState.ABOUT_TO_STOP:
102. curState = 'ABOUT_TO_STOP';
103. this.xcNodeController.dispose();
104. break;
105. case PiPWindow.PiPState.STOPPED:
106. curState = 'STOPPED';
107. break;
108. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
109. curState = 'ABOUT_TO_RESTORE';
110. break;
111. case PiPWindow.PiPState.ERROR:
112. curState = 'ERROR';
113. break;
114. default:
115. break;
116. }
117. Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
118. }

120. unregisterPipStateChangeListener() {
121. Logger.info(`${TAG} aboutToDisappear`);
122. this.pipController?.off('stateChange');
123. this.pipController?.off('controlEvent');
124. this.pipController = undefined;
125. }

127. getXComponentController(): CustomXComponentController {
128. return this.mXComponentController;
129. }

131. // 步骤1：创建画中画控制器，注册生命周期事件以及控制事件回调
132. init(ctx: Context) {
133. if (this.pipController !== null && this.pipController != undefined) {
134. return;
135. }
136. Logger.info(`${TAG} onPageShow`)
137. if (!PiPWindow.isPiPEnabled()) {
138. Logger.error(TAG, `picture in picture disabled for current OS`);
139. return;
140. }

142. let config: PiPWindow.PiPConfiguration = {
143. context: ctx,
144. componentController: this.getXComponentController(),
145. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
146. contentWidth: 1920, // 使用typeNode启动画中画时，contentWidth需设置为大于0的值，否则创建画中画失败
147. contentHeight: 1080, // 使用typeNode启动画中画时，contentHeight需设置为大于0的值，否则创建画中画失败
148. };
149. // 通过create接口创建画中画控制器实例

151. PiPWindow.create(config, this.xcNodeController.getNode()).then((controller: PiPWindow.PiPController) => {
152. this.pipController = controller;
153. // 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画
154. this.pipController?.setAutoStartEnabled(true);
155. // 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调
156. this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
157. this.onStateChange(state, reason);
158. });
159. // 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调
160. this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
161. this.onActionEvent(control);
162. });
163. }).catch((err: BusinessError) => {
164. Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
165. });
166. }

168. // 步骤2：启动画中画
169. startPip() {
170. this.pipController?.startPiP().then(() => {
171. Logger.info(TAG, `Succeeded in starting pip.`);
172. }).catch((err: BusinessError) => {
173. Logger.error(TAG, `Failed to start pip. Cause:${err.code}, message:${err.message}`);
174. });
175. }

177. // 步骤3：更新媒体源尺寸信息
178. updateContentSize(width: number, height: number) {
179. if (this.pipController) {
180. this.pipController.updateContentSize(width, height);
181. }
182. }

184. // 步骤4：关闭画中画
185. stopPip() {
186. if (this.pipController === null || this.pipController === undefined) {
187. return;
188. }
189. let promise: Promise<void> = this.pipController.stopPiP();
190. promise.then(() => {
191. Logger.info(TAG, `Succeeded in stopping pip.`);
192. }).catch((err: BusinessError) => {
193. Logger.error(TAG, `Failed to stop pip. Cause:${err.code}, message:${err.message}`);
194. });
195. }

197. getNodeController(): XCNodeController {
198. Logger.info(TAG, `getNodeController.`);
199. return this.xcNodeController;
200. }

202. setAutoStart(autoStart: boolean): void {
203. this.pipController?.setAutoStartEnabled(autoStart);
204. }

206. removeNode() {
207. this.xcNodeController.removeNode();
208. }

210. addNode(): void {
211. this.xcNodeController.addNode();
212. }
213. }
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/g9ZmpRSATpqgId61ebM1eQ/zh-cn_image_0000002558764670.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052903Z&HW-CC-Expire=86400&HW-CC-Sign=18CE9DC1AE2F29DEEF564CE2893FF04022754627D4E3CEEAA472FEDCC815D9C4)

## 应用使用单界面Ability时通过typeNode实现画中画功能

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 创建自定义NodeController，实现makeNode方法，在该方法中创建typeNode。
   * 通过create(config: PiPConfiguration, contentNode: typeNode.XComponent)接口创建画中画控制器实例。
   * 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。
   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。
   * 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调。
2. 启动画中画。

   创建画中画控制器实例后，通过startPiP接口启动画中画，在画中画ABOUT\_TO\_START生命周期将typeNode节点从布局移除。
3. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。
4. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画，在画中画ABOUT\_TO\_STOP生命周期将typeNode节点重新添加到布局中。

```
1. // entryability/EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
4. import { window } from '@kit.ArkUI';
5. import { PipManager } from '../nodefree/PipManager';
6. import { Logger } from '../util/LogUtil';

8. export default class EntryAbility extends UIAbility {
9. // ...
10. onWindowStageCreate(windowStage: window.WindowStage): void {
11. // ...
12. windowStage.loadContent('pages/Index', (err) => {
13. // ...
14. });
15. }
16. // ...
17. }
```

```
1. // pages/AbilityImplementPage.ets
2. import { PipManager } from '../ability/PipManager';
3. import { PiPWindow } from '@kit.ArkUI'; // 引入PiPWindow模块
4. import { Logger } from '../util/LogUtil';

6. const TAG = 'AbilityImplementPage'
7. @Entry
8. @Component
9. struct AbilityImplementPage {
10. private callback: Function = (state: PiPWindow.PiPState) => {
11. if (state === PiPWindow.PiPState.ABOUT_TO_STOP) {
12. // 画中画关闭或还原时触发ABOUT_TO_STOP生命周期，此时需要重新添加节点
13. PipManager.getInstance().addNode();
14. }
15. };

17. build() {
18. Column() {
19. Text('This is MainPage')
20. .fontSize(30)
21. .fontWeight(FontWeight.Bold)
22. .margin({ bottom: 20 })

24. // 将typeNode添加到页面布局中
25. NodeContainer(PipManager.getInstance().getNodeController())
26. .size({ width: '100%', height: '800px' })

28. Row({ space: 20 }) {
29. Button('startPip') // 启动画中画
30. .onClick(() => {
31. PipManager.getInstance().startPip();
32. })

34. Button('stopPip') // 停止画中画
35. .onClick(() => {
36. PipManager.getInstance().stopPip();
37. })

39. Button('updateSize') // 更新视频尺寸
40. .onClick(() => {
41. // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
42. // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
43. PipManager.getInstance().updateContentSize(900, 1600);
44. })
45. }
46. .backgroundColor('#4da99797')
47. .size({ width: '100%', height: 60 })
48. .justifyContent(FlexAlign.SpaceAround)
49. }
50. .justifyContent(FlexAlign.Center)
51. .width('100%')
52. .height('100%')
53. }

55. aboutToAppear(): void {
56. PipManager.getInstance().registerLifecycleCallback(this.callback);
57. }

59. aboutToDisappear(): void {
60. PipManager.getInstance().unregisterPipStateChangeListener();
61. PipManager.getInstance().unRegisterLifecycleCallback(this.callback);
62. }

64. onPageShow(): void {
65. Logger.info(TAG, 'onPageShow')
66. PipManager.getInstance().init(this.getUIContext().getHostContext() as Context);
67. PipManager.getInstance().setAutoStart(true);
68. }

70. onPageHide(): void {
71. Logger.info(TAG, 'onPageHide')
72. PipManager.getInstance().setAutoStart(false);
73. }
74. }
```

```
1. // ability/XCNodeController.ets
2. import { FrameNode, NodeController, typeNode } from '@kit.ArkUI';
3. import { PipManager } from './PipManager';
4. import { Logger } from '../util/LogUtil';

6. const TAG = 'XCNodeController';

8. // 创建自定义NodeController
9. export class XCNodeController extends NodeController {
10. public xComponent: typeNode.XComponent | null = null;
11. private node: FrameNode | null = null;
12. private canAddNode: boolean = true;

14. // 设置是否可以添加节点
15. setCanAddNode(canAddNode: boolean) {
16. this.canAddNode = canAddNode;
17. }

19. // 实现makeNode方法，当自定义NodeController被添加到布局时，该方法会被调用
20. makeNode(context: UIContext): FrameNode | null {
21. this.node = new FrameNode(context);
22. this.node.commonAttribute
23. if (this.xComponent === null || this.xComponent === undefined) {
24. // 创建XComponent类型的typeNode
25. this.xComponent = typeNode.createNode(context, 'XComponent', {
26. type: XComponentType.SURFACE, // 类型设置为SURFACE
27. controller: PipManager.getInstance().getXComponentController(), // 设置XComponentController
28. });
29. }
30. if (this.canAddNode) {

32. try {
33. this.xComponent.getParent()?.removeChild(this.xComponent);
34. } catch (error) {
35. Logger.error(TAG, 'Failed to removeChild');
36. }
37. try {
38. this.node.appendChild(this.xComponent);
39. } catch (error) {
40. Logger.error(TAG, 'Failed to appendChild');
41. }
42. }
43. return this.node;
44. }

46. // 重新添加typeNode节点
47. addNode() {
48. if (this.node !== null && this.node !== undefined) {
49. Logger.info(TAG, 'addNode');

51. try {
52. this.node.appendChild(this.xComponent);
53. } catch (error) {
54. Logger.error(TAG, 'Failed to appendChild');
55. }
56. }
57. }

59. // 移除typeNode节点
60. removeNode() {
61. if (this.node !== null && this.node !== undefined) {
62. Logger.info(TAG, 'removeNode');

64. try {
65. this.node.removeChild(this.xComponent);
66. } catch (error) {
67. Logger.error(TAG, 'Failed to removeChild');
68. }
69. }
70. }

72. getNode(): typeNode.XComponent | null {
73. Logger.info(TAG, 'getNode is null: '+ (this.xComponent === null || this.xComponent === undefined));
74. return this.xComponent;
75. }

77. // 开发者需要定义该方法实现布局的注销，避免内存泄漏
78. dispose() {
79. Logger.info(TAG, 'execute node dispose');
80. if (this.node !== null) {
81. this.node.dispose();
82. }
83. }
84. }
```

```
1. // ability/PipManager.ets
2. import { PiPWindow, typeNode } from '@kit.ArkUI'; // 引入PiPWindow模块
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { XCNodeController } from './XCNodeController';
5. import { AVPlayer } from '../model/AVPlayer';
6. import { Logger } from '../util/LogUtil';

8. // 自定义XComponentController
9. export class CustomXComponentController extends XComponentController {
10. onSurfaceCreated(surfaceId: string): void {
11. Logger.info(TAG, `onSurfaceCreated surfaceId: ${surfaceId}`);
12. if (PipManager.getInstance().player.surfaceID === surfaceId) {
13. return;
14. }
15. PipManager.getInstance().player.surfaceID = surfaceId;
16. PipManager.getInstance().player.avPlayerFdSrc();
17. }

19. onSurfaceDestroyed(surfaceId: string): void {
20. Logger.info(TAG, `onSurfaceDestroyed surfaceId: ${surfaceId}`);
21. }
22. }

24. const TAG = 'PipManager';

26. export class PipManager {
27. private static instance: PipManager = new PipManager();
28. private pipController?: PiPWindow.PiPController = undefined;
29. private xcNodeController: XCNodeController;
30. private mXComponentController: XComponentController;
31. private lifeCycleCallback: Set<Function> = new Set();
32. public player: AVPlayer;

34. public static getInstance(): PipManager {
35. return PipManager.instance;
36. }

38. constructor() {
39. this.xcNodeController = new XCNodeController();
40. this.player = new AVPlayer();
41. this.mXComponentController = new CustomXComponentController();
42. }

44. public registerLifecycleCallback(callBack: Function) {
45. this.lifeCycleCallback.add(callBack);
46. }

48. public unRegisterLifecycleCallback(callBack: Function): void {
49. this.lifeCycleCallback.delete(callBack);
50. }

52. getNode(): typeNode.XComponent | null {
53. return this.xcNodeController.getNode();
54. }

56. onActionEvent(control: PiPWindow.ControlEventParam) {
57. switch (control.controlType) {
58. case PiPWindow.PiPControlType.VIDEO_PLAY_PAUSE:
59. if (control.status === PiPWindow.PiPControlStatus.PAUSE) {
60. //停止视频
61. } else if (control.status === PiPWindow.PiPControlStatus.PLAY) {
62. //播放视频
63. }
64. break;
65. case PiPWindow.PiPControlType.VIDEO_NEXT:
66. // 切换到下一个视频
67. break;
68. case PiPWindow.PiPControlType.VIDEO_PREVIOUS:
69. // 切换到上一个视频
70. break;
71. case PiPWindow.PiPControlType.FAST_FORWARD:
72. // 视频进度快进
73. break;
74. case PiPWindow.PiPControlType.FAST_BACKWARD:
75. // 视频进度后退
76. break;
77. default:
78. break;
79. }
80. Logger.info('onActionEvent, controlType:' + control.controlType + ', status' + control.status);
81. }

83. onStateChange(state: PiPWindow.PiPState, reason: string) {
84. let curState: string = '';
85. this.xcNodeController.setCanAddNode(
86. state === PiPWindow.PiPState.ABOUT_TO_STOP || state === PiPWindow.PiPState.STOPPED);
87. if (this.lifeCycleCallback !== null) {
88. this.lifeCycleCallback.forEach((fun) => {
89. fun(state);
90. });
91. }
92. switch (state) {
93. case PiPWindow.PiPState.ABOUT_TO_START:
94. curState = 'ABOUT_TO_START';
95. // 将typeNode节点从布局移除
96. this.xcNodeController.removeNode();
97. break;
98. case PiPWindow.PiPState.STARTED:
99. curState = 'STARTED';
100. break;
101. case PiPWindow.PiPState.ABOUT_TO_STOP:
102. curState = 'ABOUT_TO_STOP';
103. this.xcNodeController.dispose();
104. break;
105. case PiPWindow.PiPState.STOPPED:
106. curState = 'STOPPED';
107. break;
108. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
109. curState = 'ABOUT_TO_RESTORE';
110. break;
111. case PiPWindow.PiPState.ERROR:
112. curState = 'ERROR';
113. break;
114. default:
115. break;
116. }
117. Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
118. }

120. unregisterPipStateChangeListener() {
121. Logger.info(`${TAG} aboutToDisappear`);
122. this.pipController?.off('stateChange');
123. this.pipController?.off('controlEvent');
124. }

126. getXComponentController(): CustomXComponentController {
127. return this.mXComponentController;
128. }

130. // 步骤1：创建画中画控制器，注册生命周期事件以及控制事件回调
131. init(ctx: Context) {
132. if (this.pipController !== null && this.pipController != undefined) {
133. return;
134. }
135. Logger.info(`${TAG} onPageShow`)
136. if (!PiPWindow.isPiPEnabled()) {
137. Logger.error(TAG, `picture in picture disabled for current OS`);
138. return;
139. }
140. let config: PiPWindow.PiPConfiguration = {
141. context: ctx,
142. componentController: this.getXComponentController(),
143. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
144. contentWidth: 1920, // 使用typeNode启动画中画时，contentWidth需设置为大于0的值，否则创建画中画失败
145. contentHeight: 1080, // 使用typeNode启动画中画时，contentHeight需设置为大于0的值，否则创建画中画失败
146. };
147. // 通过create接口创建画中画控制器实例

149. PiPWindow.create(config, this.xcNodeController.getNode()).then((controller: PiPWindow.PiPController) => {
150. this.pipController = controller;
151. // 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画
152. this.pipController?.setAutoStartEnabled(true);
153. // 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调
154. this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
155. this.onStateChange(state, reason);
156. });
157. // 通过画中画控制器实例的on('controlEvent')接口注册控制事件回调
158. this.pipController.on('controlEvent', (control: PiPWindow.ControlEventParam) => {
159. this.onActionEvent(control);
160. });
161. }).catch((err: BusinessError) => {
162. Logger.error(TAG, `Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
163. });
164. }

166. // 步骤2：启动画中画
167. startPip() {
168. this.pipController?.startPiP().then(() => {
169. Logger.info(TAG, `Succeeded in starting pip.`);
170. }).catch((err: BusinessError) => {
171. Logger.error(TAG, `Failed to start pip. Cause:${err.code}, message:${err.message}`);
172. });
173. }

175. // 步骤3：更新媒体源尺寸信息
176. updateContentSize(width: number, height: number) {
177. if (this.pipController) {
178. this.pipController.updateContentSize(width, height);
179. }
180. }

182. // 步骤4：关闭画中画
183. stopPip() {
184. if (this.pipController === null || this.pipController === undefined) {
185. return;
186. }
187. let promise: Promise<void> = this.pipController.stopPiP();
188. promise.then(() => {
189. Logger.info(TAG, `Succeeded in stopping pip.`);
190. }).catch((err: BusinessError) => {
191. Logger.error(TAG, `Failed to stop pip. Cause:${err.code}, message:${err.message}`);
192. });
193. }

195. getNodeController(): XCNodeController {
196. Logger.info(TAG, `getNodeController.`);
197. return this.xcNodeController;
198. }

200. setAutoStart(autoStart: boolean): void {
201. this.pipController?.setAutoStartEnabled(autoStart);
202. }

204. // 将typeNode节点添加到原父节点
205. addNode(): void {
206. this.xcNodeController.addNode();
207. }
208. }
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/bU_nkrOvQc2MS4oYTJhllw/zh-cn_image_0000002558764670.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052903Z&HW-CC-Expire=86400&HW-CC-Sign=8C448A4A97FD021BEBAC3E32ED11457074738313E5F661C4EE2B3B0C7766FF49)
