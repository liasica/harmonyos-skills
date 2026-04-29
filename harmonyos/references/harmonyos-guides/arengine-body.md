---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-body
title: 人体跟踪与骨骼关键点识别（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人体骨骼点识别与跟踪 > 人体跟踪与骨骼关键点识别（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-29T13:35:58+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:df577f91bea8d63046c4b1750c933c8e65f3490d144da50f04e48cfb483136b2
---

## 约束与限制

管理AR会话能力支持部分Phone、部分Tablet、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_BODY](../harmonyos-references/arengine-api-arengine.md#arfeaturetype)）。

## 接口说明

人体跟踪与骨骼关键点识别主要依赖ARBody，以下接口为人体跟踪与骨骼关键点识别的相关接口。详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-api-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe) | 获取AR Engine处理后的一帧数据。 |
| [ARFrame.acquireBodySkeleton](../harmonyos-references/arengine-api-arengine.md#arframeacquirebodyskeleton) | 返回人体跟踪的人体对象数组。 |
| [ARBody.getLandmarks2D](../harmonyos-references/arengine-api-arengine.md#arbodygetlandmarks2d) | 返回一个人体对象的骨骼关键点数组。 |

## 开发步骤

对于使用ArkTS的任何AR应用，首先需要创建一个AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)，用于管理AR Engine的系统状态。AR会话[ARViewContext](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcontext)的创建可以参考[管理AR会话](arengine-arsession.md)章节。

### 导入模块

人体跟踪与骨骼关键点识别能力需要导入的模块如下：

```
1. import { arEngine, ARView, arViewController } from '@kit.AREngine';
2. import { Node, Scene } from '@kit.ArkGraphics3D';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { display } from '@kit.ArkUI';
```

### 结构定义

```
1. interface BodyInfo {
2. trackId: number,
3. landmarks: arEngine.ARBodyLandmark2D[]
4. }

6. function arLandmarksToMap(arLandmarks: arEngine.ARBodyLandmark2D[]): Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D> {
7. let typeToLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D> = new Map();
8. for (let arLandmark of arLandmarks) {
9. typeToLandmarks.set(arLandmark.type, arLandmark);
10. }
11. return typeToLandmarks;
12. }

14. type OnBodyInfoCallback = (bodyInfo: arEngine.ARBody[]) => void;

16. const DEFAULT_CONVERT_FACTOR: number = 4 / 3;
17. const FULL_SCREEN_SIZE: string = '100%';
```

### 显示预览流

首先初始化AR会话和AR场景，可以参考[初始化AR会话和AR场景](arengine-arsession.md#初始化ar会话和ar场景)章节。

更改type为[ARType](../harmonyos-references/arengine-api-arengine.md#artype).BODY。

```
1. @Builder
2. export function ARBodyBuilder() {
3. ARBody();
4. }

6. @ComponentV2
7. struct ARBody {
8. @Local arContext?: arViewController.ARViewContext = undefined;
9. @Local bodyInfos: BodyInfo[] = [];
10. @Local displayWidth: number = display.getDefaultDisplaySync().width;
11. @Local displayHeight: number = display.getDefaultDisplaySync().height;
12. private params: arEngine.ARConfig = { type: arEngine.ARType.BODY };
13. private uiContext: UIContext = this.getUIContext();
14. private onBodyInfoCb: OnBodyInfoCallback = (bodyInfos: arEngine.ARBody[]) => {
15. if (display.getDefaultDisplaySync().width * 3 < display.getDefaultDisplaySync().height * 4) {
16. this.displayWidth = display.getDefaultDisplaySync().width;
17. this.displayHeight = this.displayWidth * DEFAULT_CONVERT_FACTOR;
18. } else {
19. this.displayHeight = display.getDefaultDisplaySync().height;
20. this.displayWidth = this.displayHeight * DEFAULT_CONVERT_FACTOR;
21. }

23. this.bodyInfos = bodyInfos.map((value: arEngine.ARBody) => {
24. let landmarks: arEngine.ARBodyLandmark2D[] = value.getLandmarks2D();
25. landmarks.forEach((value: arEngine.ARBodyLandmark2D) => {
26. value.x = value.x * this.displayWidth;
27. value.y = value.y * this.displayHeight;
28. })
29. let info: BodyInfo = {
30. trackId: value.trackId,
31. landmarks: landmarks
32. }
33. return info;
34. })
35. }

37. private async initARView(): Promise<void> {
38. await Scene.load().then(async (scene: Scene) => {
39. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
40. viewContext.scene = scene;
41. let callback = new ARViewCallbackImpl();
42. callback.setCallback(this.onBodyInfoCb);
43. viewContext.callback = callback;
44. viewContext.config = {
45. type: arEngine.ARType.BODY,
46. planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
47. powerMode: arEngine.ARPowerMode.NORMAL,
48. semanticMode: arEngine.ARSemanticMode.NONE,
49. poseMode: arEngine.ARPoseMode.GRAVITY,
50. depthMode: arEngine.ARDepthMode.DISABLED,
51. meshMode: arEngine.ARMeshMode.DISABLED,
52. focusMode: arEngine.ARFocusMode.AUTO,
53. maxDetectedBodyNum: this.params?.maxDetectedBodyNum ?? 1,
54. cameraLensFacing: this.params?.cameraLensFacing ?? 0
55. };
56. viewContext.init().then(() => {
57. this.arContext = viewContext;
58. console.info('Succeeded in initializing ARView.');
59. }).catch((err: BusinessError) => {
60. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
61. })
62. })
63. }

65. private stopARView(): void {
66. if (!this.arContext) {
67. return;
68. }
69. try {
70. this.arContext.destroy();
71. } catch (error) {
72. const err: BusinessError = error as BusinessError;
73. console.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
74. }
75. }

77. private pauseARView(): void {
78. if (!this.arContext) {
79. return;
80. }
81. try {
82. this.arContext.pause();
83. } catch (error) {
84. const err: BusinessError = error as BusinessError;
85. console.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}.`);
86. }
87. }

89. private resumeARView(): void {
90. if (!this.arContext) {
91. return;
92. }
93. try {
94. this.arContext.resume();
95. } catch (error) {
96. const err: BusinessError = error as BusinessError;
97. console.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}.`);
98. }
99. }

101. build() {
102. NavDestination() {
103. Stack() {
104. Column() {
105. RelativeContainer() {
106. if (this.arContext) {
107. ARView({ context: this.arContext })
108. .height(FULL_SCREEN_SIZE)
109. .width(FULL_SCREEN_SIZE)
110. .alignRules({
111. center: { anchor: '__container__', align: VerticalAlign.Center },
112. middle: { anchor: '__container__', align: HorizontalAlign.Center }
113. })
114. }
115. }
116. }
117. .width(this.uiContext.px2vp(this.displayWidth))
118. .height(this.uiContext.px2vp(this.displayHeight))
119. .justifyContent(FlexAlign.Center)
120. .alignItems(HorizontalAlign.Center)

122. this.drawBodyPerception();
123. }
124. .width(FULL_SCREEN_SIZE)
125. .height(FULL_SCREEN_SIZE)
126. }
127. .onAppear(() => {
128. this.initARView();
129. })
130. .onWillDisappear(() => {
131. this.stopARView();
132. })
133. .onShown(() => {
134. this.resumeARView();
135. })
136. .onHidden(() => {
137. this.pauseARView();
138. })
139. .onReady(ctx => {
140. this.params = ctx.pathInfo.param as arEngine.ARConfig;
141. this.params['type'] = arEngine.ARType.BODY;
142. })
143. .hideTitleBar(true)
144. .hideBackButton(true)
145. .hideToolBar(true)
146. }

148. @Builder
149. drawBodyPerception() {
150. Shape() {
151. ForEach(this.bodyInfos, (bodyInfo: BodyInfo, idx: number) => {
152. this.drawBodyBones(arLandmarksToMap(bodyInfo.landmarks));
153. this.drawBodyLandmarks(bodyInfo.landmarks);
154. })
155. }
156. .width(this.uiContext.px2vp(this.displayWidth))
157. .height(this.uiContext.px2vp(this.displayHeight))
158. }

160. @Builder
161. drawBodyLandmarks(bodyLandmarks: arEngine.ARBodyLandmark2D[]) {
162. ForEach(bodyLandmarks, (landmark: arEngine.ARBodyLandmark2D, index: number) => {
163. Circle({ width: 4, height: 4 })
164. .position({
165. x: this.uiContext.px2vp(landmark.x),
166. y: this.uiContext.px2vp(landmark.y)
167. })
168. .fillOpacity(1)
169. .fill(Color.White)
170. })
171. }

173. @Builder
174. drawBodyBones(bodyLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D>) {
175. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.NOSE, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
176. Color.Orange);
177. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.NOSE, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
178. Color.Orange);

180. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
181. arEngine.ARBodyLandmarkType.RIGHT_SHOULDER, Color.Orange);
182. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
183. arEngine.ARBodyLandmarkType.RIGHT_HIP, Color.Orange);
184. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_HIP, arEngine.ARBodyLandmarkType.LEFT_HIP,
185. Color.Orange);
186. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_HIP,
187. arEngine.ARBodyLandmarkType.LEFT_SHOULDER, Color.Orange);

189. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
190. arEngine.ARBodyLandmarkType.LEFT_ELBOW, Color.Green);
191. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_ELBOW, arEngine.ARBodyLandmarkType.LEFT_WRIST,
192. Color.Green);
193. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_HIP, arEngine.ARBodyLandmarkType.LEFT_KNEE,
194. Color.Green);
195. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_KNEE, arEngine.ARBodyLandmarkType.LEFT_ANKLE,
196. Color.Green);

198. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
199. arEngine.ARBodyLandmarkType.RIGHT_ELBOW, Color.Blue);
200. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_ELBOW,
201. arEngine.ARBodyLandmarkType.RIGHT_WRIST, Color.Blue);
202. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_HIP, arEngine.ARBodyLandmarkType.RIGHT_KNEE,
203. Color.Blue);
204. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_KNEE,
205. arEngine.ARBodyLandmarkType.RIGHT_ANKLE, Color.Blue);
206. }

208. @Builder
209. drawBodyBoneLine(bodyLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D>,
210. start: arEngine.ARBodyLandmarkType, end: arEngine.ARBodyLandmarkType, color: Color) {
211. if (bodyLandmarks.has(start) && bodyLandmarks.has(end)) {
212. Line()
213. .startPoint([this.uiContext.px2vp(bodyLandmarks.get(start)?.x),
214. this.uiContext.px2vp(bodyLandmarks.get(start)?.y)])
215. .endPoint([this.uiContext.px2vp(bodyLandmarks.get(end)?.x), this.uiContext.px2vp(bodyLandmarks.get(end)?.y)])
216. .stroke(color)
217. .strokeWidth(3)
218. }
219. }
220. }
```

### 获取人体跟踪对象数组和人体骨骼关键点数据

1. 调用[ARViewCallback](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallback)，使用其中的[onFrameUpdate](../harmonyos-references/arengine-api-arviewcontroller.md#arviewcallbackonframeupdate)方法进行帧数据更新。
2. 通过[ARSession.getFrame](../harmonyos-references/arengine-api-arengine.md#arsessiongetframe)方法获取当前帧。
3. 通过[ARFrame.acquireBodySkeleton](../harmonyos-references/arengine-api-arengine.md#arframeacquirebodyskeleton)获得当前会话包含的人体对象数组。
4. 通过[ARBody.getLandmarks2D](../harmonyos-references/arengine-api-arengine.md#arbodygetlandmarks2d)获取人体对象骨骼关键点数组。

```
1. class ARViewCallbackImpl extends arViewController.ARViewCallback {
2. private callback?: OnBodyInfoCallback;

4. setCallback(cb: OnBodyInfoCallback) {
5. this.callback = cb;
6. }

8. onAnchorAdd(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
9. // ...
10. }

12. onAnchorUpdate(ctx: arViewController.ARViewContext, node: Node, anchor: arEngine.ARAnchor): void {
13. // ...
14. }

16. async onFrameUpdate(ctx: arViewController.ARViewContext, sysBootTs: number): Promise<void> {
17. if (!ctx.session) {
18. return;
19. }
20. console.info('onFrameUpdate enter');
21. const arSession: arEngine.ARSession = ctx.session;
22. try {
23. const frame: arEngine.ARFrame = arSession.getFrame();
24. const bodies: arEngine.ARBody[] = frame.acquireBodySkeleton();
25. this.callback ? this.callback(bodies) : console.error(`callback not set`);
26. } catch (error) {
27. const err: BusinessError = error as BusinessError;
28. console.error(`Failed to update data. Code is ${err.code}, message is ${err.message}.`);
29. }
30. }
31. }
```
