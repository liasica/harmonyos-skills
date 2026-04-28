---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pipwindow-xcomponent
title: 使用XComponent实现画中画功能开发（ArkTS）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 在应用程序中使用画中画功能 > 使用XComponent实现画中画功能开发（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f84df0ea9dac5c7fbbbb76f1020c425c97ed8d3af224af10dd54b6bf7426876c
---

本文以视频播放为例，介绍通过XComponent实现画中画功能的基本开发步骤。

## 约束与限制

* HarmonyOS 6.0.0之前，支持在Phone、Tablet设备使用XComponent实现画中画功能开发；从HarmonyOS 6.0.0开始，支持在Phone、PC/2in1、Tablet设备使用XComponent实现画中画功能开发。
* 仅支持以[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)作为媒体流播放组件的界面进入画中画模式，XComponent的type必须为XComponentType.SURFACE。
* UIAbility使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)管理页面时，需要设置Navigation控件的id属性，并将该id传递给画中画控制器，确保还原时可以正常恢复原页面。
* 如果应用主窗口不在前台，不建议在画中画回调方法中执行UI操作，例如页面push/pop等，这些操作不会立即执行，可能产生预期之外的结果。
* 在关闭画中画时，需要检查自定义组件节点是否释放，避免出现内存泄漏。

## 开发步骤

1. 创建画中画控制器，注册生命周期事件以及控制事件回调。

   * 通过create(config: PiPConfiguration)接口创建画中画控制器实例。
   * 通过画中画控制器实例的setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画。
   * 通过画中画控制器实例的on('stateChange')接口注册生命周期事件回调。
   * 通过画中画控制器实例的on('controlPanelActionEvent')接口注册控制事件回调。
2. 启动画中画。

   创建画中画控制器实例后，通过startPiP接口启动画中画。
3. 更新媒体源尺寸信息。

   画中画媒体源更新后（如切换视频），通过画中画控制器实例的updateContentSize接口更新媒体源尺寸信息，以调整画中画窗口比例。
4. 关闭画中画。

   当不再需要显示画中画时，可根据业务需要，通过画中画控制器实例的stopPiP接口关闭画中画。

```
1. // pages/XComponentImplementPage.ets
2. // 该页面用于展示Navigation在画中画场景的使用。如果UIAbility是单页面，则无需使用Navigation
3. import { Page1 } from '../xcomponent/Page1'

5. @Entry
6. @Component
7. struct XComponentImplementPage {
8. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
9. private navId: string = 'navId';

11. @Builder
12. PageMap(name: string) {
13. if (name === 'pageOne') {
14. Page1({ navId: this.navId });
15. }
16. }

18. build() {
19. Navigation(this.pageInfos) {
20. Column() {
21. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
22. .width('80%')
23. .height(40)
24. .margin(20)
25. .onClick(() => {
26. this.pageInfos.pushPath({ name: 'pageOne' }) // 将name指定的NavDestination页面信息入栈
27. })
28. .stateStyles({
29. pressed: {
30. .backgroundColor(Color.Red);
31. },
32. normal: {
33. .backgroundColor(Color.Blue);
34. }
35. })
36. }
37. }
38. .title('NavIndex')
39. .navDestination(this.PageMap)
40. .id(this.navId) // 设置Navigation组件的id属性
41. }
42. }
```

示例中的视频播放需要使用AVPlayer，具体示例可参考[视频播放](video-playback.md)。

```
1. // xcomponent/Page1.ets
2. // 该页面用于展示画中画功能的基本使用
3. import { AVPlayer } from '../model/AVPlayer';
4. import { BuilderNode, FrameNode, NodeController, UIContext, PiPWindow } from '@kit.ArkUI';
5. import { BusinessError } from '@kit.BasicServicesKit';
6. import { Logger } from '../util/LogUtil';

8. const TAG = 'Page1';

10. class Params {
11. public text: string = '';

13. constructor(text: string) {
14. this.text = text;
15. }
16. }

18. // 开发者可以通过@Builder装饰器实现布局构建
19. @Builder
20. function buildText(params: Params) {
21. Column() {
22. Text(params.text)
23. .fontSize(20)
24. .fontColor(Color.Red)
25. }
26. .width('100%') // 宽度方向充满画中画窗口
27. .height('100%') // 高度方向充满画中画窗口
28. }

30. // 开发者可通过继承NodeController实现自定义UI控制器
31. class TextNodeController extends NodeController {
32. private message: string;
33. private textNode: BuilderNode<[Params]> | null = null;

35. constructor(message: string) {
36. super();
37. this.message = message;
38. }

40. // 通过BuilderNode加载自定义布局
41. makeNode(context: UIContext): FrameNode | null {
42. this.textNode = new BuilderNode(context);
43. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
44. return this.textNode.getFrameNode();
45. }

47. // 开发者可自定义该方法实现布局更新
48. update(message: string) {
49. Logger.info(`update message: ${message}`);
50. if (this.textNode !== null) {
51. this.textNode.update(new Params(message));
52. }
53. }

55. // 开发者需要定义该方法实现布局的注销，避免内存泄漏
56. dispose() {
57. Logger.info('dispose message: execute node dispose');
58. if (this.textNode !== null) {
59. this.textNode.dispose();
60. }
61. }
62. }

64. @Entry
65. @Component
66. export struct Page1 {
67. @Consume('pageInfos') pageInfos: NavPathStack;
68. private surfaceId: string = ''; // surfaceId，用于关联XComponent与视频播放器
69. private mXComponentController: XComponentController = new XComponentController();
70. private player?: AVPlayer = undefined;
71. private pipController?: PiPWindow.PiPController = undefined;
72. private nodeController: TextNodeController = new TextNodeController('this is custom UI');
73. navId: string = '';
74. private options: XComponentOptions = {
75. type: XComponentType.SURFACE,
76. controller: this.mXComponentController
77. }

79. build() {
80. NavDestination() {
81. Column() {
82. // XComponent控件，用于播放视频流
83. XComponent(this.options)
84. .onLoad(() => {
85. this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
86. // 需要设置AVPlayer的surfaceId为XComponentController的surfaceId
87. this.player = new AVPlayer();
88. this.player.surfaceID = this.surfaceId;
89. this.player.avPlayerFdSrc();
90. })
91. .onDestroy(() => {
92. Logger.info(`[${TAG}] XComponent onDestroy`);
93. })
94. .size({ width: '100%', height: '800px' })
95. Row({ space: 20 }) {
96. Button('startPip') // 启动画中画
97. .onClick(() => {
98. this.startPip();
99. })
100. .stateStyles({
101. pressed: {
102. .backgroundColor(Color.Red);
103. },
104. normal: {
105. .backgroundColor(Color.Blue);
106. }
107. })
108. Button('stopPip') // 停止画中画
109. .onClick(() => {
110. this.stopPip();
111. })
112. .stateStyles({
113. pressed: {
114. .backgroundColor(Color.Red);
115. },
116. normal: {
117. .backgroundColor(Color.Blue);
118. }
119. })
120. Button('updateSize') // 更新视频尺寸
121. .onClick(() => {
122. // 此处设置的宽高应为媒体内容宽高，需要通过媒体相关接口或回调获取
123. // 例如使用AVPlayer播放视频时，可通过videoSizeChange回调获取媒体源更新后的尺寸
124. this.updateContentSize(900, 1600);
125. })
126. .stateStyles({
127. pressed: {
128. .backgroundColor(Color.Red);
129. },
130. normal: {
131. .backgroundColor(Color.Blue);
132. }
133. })
134. }
135. .size({ width: '100%', height: 60 })
136. .justifyContent(FlexAlign.SpaceAround)
137. }
138. .justifyContent(FlexAlign.Center)
139. .height('100%')
140. .width('100%')
141. }
142. }

144. startPip() {
145. if (!PiPWindow.isPiPEnabled()) {
146. Logger.error(`picture in picture disabled for current OS`);
147. return;
148. }
149. let config: PiPWindow.PiPConfiguration = {
150. context: this.getUIContext().getHostContext() as Context,
151. componentController: this.mXComponentController,
152. // 当前page导航id
153. // 1、UIAbility使用Navigation管理页面，需要设置Navigation控件的id属性，并将该id设置给画中画控制器，确保还原场景下能够从画中画窗口恢复到原页面
154. // 2、UIAbility使用Router管理页面时（画中画场景不推荐该导航方式），无需设置navigationId。注意：该场景下启动画中画后，不要进行页面切换，否则还原场景可能出现异常
155. // 3、UIAbility只有单页面时，无需设置navigationId，还原场景下也能够从画中画窗口恢复到原页面
156. navigationId: this.navId,
157. // 对于视频通话、视频会议等场景，需要设置相应的模板类型
158. templateType: PiPWindow.PiPTemplateType.VIDEO_PLAY,
159. // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
160. contentWidth: 1920,
161. // 可选，创建画中画控制器时系统可通过XComponent组件大小设置画中画窗口比例
162. contentHeight: 1080,
163. // 可选，对于视频通话、视频会议和视频直播场景，可通过该属性选择对应模板类型下需显示的的控件组
164. controlGroups: [PiPWindow.VideoPlayControlGroup.VIDEO_PREVIOUS_NEXT],
165. // 可选，如果需要在画中画显示内容上方展示自定义UI，可设置该参数。
166. customUIController: this.nodeController,
167. };
168. // 步骤1：创建画中画控制器，通过create接口创建画中画控制器实例
169. PiPWindow.create(config).then((controller: PiPWindow.PiPController) => {
170. this.pipController = controller;
171. // 步骤1：初始化画中画控制器
172. this.initPipController();
173. // 步骤2：通过startPiP接口启动画中画
174. this.pipController.startPiP().then(() => {
175. Logger.info(`Succeeded in starting pip.`);
176. }).catch((err: BusinessError) => {
177. Logger.error(`Failed to start pip. Cause:${err.code}, message:${err.message}`);
178. });
179. }).catch((err: BusinessError) => {
180. Logger.error(`Failed to create pip controller. Cause:${err.code}, message:${err.message}`);
181. });
182. }

184. initPipController() {
185. if (!this.pipController) {
186. return;
187. }
188. // 步骤1：通过setAutoStartEnabled接口设置是否需要在应用返回桌面时自动启动画中画，注册stateChange和controlPanelActionEvent回调
189. this.pipController.setAutoStartEnabled(false /*or true if necessary*/); // 默认为false
190. this.pipController.on('stateChange', (state: PiPWindow.PiPState, reason: string) => {
191. this.onStateChange(state, reason);
192. });
193. this.pipController.on('controlPanelActionEvent', (event: PiPWindow.PiPActionEventType, status?: number) => {
194. this.onActionEvent(event, status);
195. });
196. }

198. onStateChange(state: PiPWindow.PiPState, reason: string) {
199. let curState: string = '';
200. switch (state) {
201. case PiPWindow.PiPState.ABOUT_TO_START:
202. curState = 'ABOUT_TO_START';
203. break;
204. case PiPWindow.PiPState.STARTED:
205. curState = 'STARTED';
206. break;
207. case PiPWindow.PiPState.ABOUT_TO_STOP:
208. curState = 'ABOUT_TO_STOP';
209. this.nodeController?.dispose();
210. break;
211. case PiPWindow.PiPState.STOPPED:
212. curState = 'STOPPED';
213. break;
214. case PiPWindow.PiPState.ABOUT_TO_RESTORE:
215. curState = 'ABOUT_TO_RESTORE';
216. break;
217. case PiPWindow.PiPState.ERROR:
218. curState = 'ERROR';
219. break;
220. default:
221. break;
222. }
223. Logger.info(`[${TAG}] onStateChange: ${curState}, reason: ${reason}`);
224. }

226. onActionEvent(event: PiPWindow.PiPActionEventType, status?: number) {
227. switch (event) {
228. case 'playbackStateChanged':
229. // 开始或停止视频
230. if (status === 0) {
231. // 停止视频
232. } else if (status === 1) {
233. // 播放视频
234. }
235. break;
236. case 'nextVideo':
237. // 播放下一个视频
238. break;
239. case 'previousVideo':
240. // 播放上一个视频
241. break;
242. default:
243. break;
244. }
245. }

247. // 步骤3：视频内容变化时，向画中画控制器更新视频尺寸信息，用于调整画中画窗口比例
248. updateContentSize(width: number, height: number) {
249. if (this.pipController) {
250. this.pipController.updateContentSize(width, height);
251. }
252. }

254. // 步骤4：当不再需要显示画中画时，通过stopPiP接口关闭画中画
255. stopPip() {
256. if (this.pipController) {
257. let promise: Promise<void> = this.pipController.stopPiP();
258. promise.then(() => {
259. Logger.info(`Succeeded in stopping pip.`);
260. this.pipController?.off('stateChange'); // 如果已注册stateChange回调，停止画中画时取消注册该回调
261. this.pipController?.off('controlPanelActionEvent'); // 如果已注册controlPanelActionEvent回调，停止画中画时取消注册该回调
262. }).catch((err: BusinessError) => {
263. Logger.error(`Failed to stop pip. Cause:${err.code}, message:${err.message}`);
264. });
265. }
266. }
267. }
```

以上示例代码对应的示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/Aa4xDEp3QtC3bOCKZjJEKQ/zh-cn_image_0000002552798530.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234042Z&HW-CC-Expire=86400&HW-CC-Sign=DF503F62D30403848B7056D4258D3B88B38932136E31B12393E8905C3D51D956)
