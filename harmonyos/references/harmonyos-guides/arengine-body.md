---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-body
title: 人体跟踪与骨骼关键点识别（ArkTS）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人体骨骼点识别与跟踪 > 人体跟踪与骨骼关键点识别（ArkTS）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:56+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:754e6881b30de693494b908d55ef1a19d0352f1c648ac4438d30dbc15df289bf
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

37. aboutToAppear() {
38. console.info('aboutToAppear');
39. this.initARView();
40. }

42. aboutToDisappear() {
43. console.info('aboutToDisappear');
44. this.stopARView();
45. }

47. private async initARView(): Promise<void> {
48. Scene.load().then(async (scene: Scene) => {
49. let viewContext: arViewController.ARViewContext = new arViewController.ARViewContext();
50. viewContext.scene = scene;
51. let callback = new ARViewCallbackImpl();
52. callback.setCallback(this.onBodyInfoCb);
53. viewContext.callback = callback;
54. viewContext.config = {
55. type: arEngine.ARType.BODY,
56. planeFindingMode: arEngine.ARPlaneFindingMode.DISABLED,
57. powerMode: arEngine.ARPowerMode.NORMAL,
58. semanticMode: arEngine.ARSemanticMode.NONE,
59. poseMode: arEngine.ARPoseMode.GRAVITY,
60. depthMode: arEngine.ARDepthMode.DISABLED,
61. meshMode: arEngine.ARMeshMode.DISABLED,
62. focusMode: arEngine.ARFocusMode.AUTO,
63. maxDetectedBodyNum: this.params?.maxDetectedBodyNum ?? 1,
64. cameraLensFacing: this.params?.cameraLensFacing ?? 0
65. };
66. viewContext.init().then(() => {
67. this.arContext = viewContext;
68. console.info('Succeeded in initializing ARView.');
69. }).catch((err: BusinessError) => {
70. console.error(`Failed to init ARView. Code is ${err.code}, message is ${err.message}.`);
71. })
72. })
73. }

75. private stopARView(): void {
76. if (!this.arContext) {
77. return;
78. }
79. try {
80. this.arContext.destroy();
81. } catch (error) {
82. const err: BusinessError = error as BusinessError;
83. console.error(`Failed to stop context. Code is ${err.code}, message is ${err.message}`);
84. }
85. }

87. private pauseARView(): void {
88. if (!this.arContext) {
89. return;
90. }
91. try {
92. this.arContext.pause();
93. } catch (error) {
94. const err: BusinessError = error as BusinessError;
95. console.error(`Failed to pause context. Code is ${err.code}, message is ${err.message}.`);
96. }
97. }

99. private resumeARView(): void {
100. if (!this.arContext) {
101. return;
102. }
103. try {
104. this.arContext.resume();
105. } catch (error) {
106. const err: BusinessError = error as BusinessError;
107. console.error(`Failed to resume context. Code is ${err.code}, message is ${err.message}.`);
108. }
109. }

111. build() {
112. NavDestination() {
113. Stack() {
114. Column() {
115. RelativeContainer() {
116. if (this.arContext) {
117. ARView({ context: this.arContext })
118. .height(FULL_SCREEN_SIZE)
119. .width(FULL_SCREEN_SIZE)
120. .alignRules({
121. center: { anchor: '__container__', align: VerticalAlign.Center },
122. middle: { anchor: '__container__', align: HorizontalAlign.Center }
123. })
124. }
125. }
126. }
127. .width(this.uiContext.px2vp(this.displayWidth))
128. .height(this.uiContext.px2vp(this.displayHeight))
129. .justifyContent(FlexAlign.Center)
130. .alignItems(HorizontalAlign.Center)

132. this.drawBodyPerception()
133. }
134. .width(FULL_SCREEN_SIZE)
135. .height(FULL_SCREEN_SIZE)
136. }
137. .onAppear(() => {
138. this.initARView();
139. })
140. .onWillDisappear(() => {
141. this.stopARView();
142. })
143. .onShown(() => {
144. this.resumeARView();
145. })
146. .onHidden(() => {
147. this.pauseARView();
148. })
149. .onReady(ctx => {
150. this.params = ctx.pathInfo.param as arEngine.ARConfig;
151. this.params['type'] = arEngine.ARType.BODY;
152. })
153. .hideTitleBar(true)
154. .hideBackButton(true)
155. .hideToolBar(true)
156. }

158. @Builder
159. drawBodyPerception() {
160. Shape() {
161. ForEach(this.bodyInfos, (bodyInfo: BodyInfo, idx: number) => {
162. this.drawBodyBones(arLandmarksToMap(bodyInfo.landmarks));
163. this.drawBodyLandmarks(bodyInfo.landmarks);
164. })
165. }
166. .width(this.uiContext.px2vp(this.displayWidth))
167. .height(this.uiContext.px2vp(this.displayHeight))
168. }

170. @Builder
171. drawBodyLandmarks(bodyLandmarks: arEngine.ARBodyLandmark2D[]) {
172. ForEach(bodyLandmarks, (landmark: arEngine.ARBodyLandmark2D, index: number) => {
173. Circle({ width: 4, height: 4 })
174. .position({
175. x: this.uiContext.px2vp(landmark.x),
176. y: this.uiContext.px2vp(landmark.y)
177. })
178. .fillOpacity(1)
179. .fill(Color.White)
180. })
181. }

183. @Builder
184. drawBodyBones(bodyLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D>) {
185. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.NOSE, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
186. Color.Orange);
187. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.NOSE, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
188. Color.Orange);

190. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
191. arEngine.ARBodyLandmarkType.RIGHT_SHOULDER, Color.Orange);
192. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
193. arEngine.ARBodyLandmarkType.RIGHT_HIP, Color.Orange);
194. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_HIP, arEngine.ARBodyLandmarkType.LEFT_HIP,
195. Color.Orange);
196. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_HIP,
197. arEngine.ARBodyLandmarkType.LEFT_SHOULDER, Color.Orange);

199. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_SHOULDER,
200. arEngine.ARBodyLandmarkType.LEFT_ELBOW, Color.Green);
201. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_ELBOW, arEngine.ARBodyLandmarkType.LEFT_WRIST,
202. Color.Green);
203. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_HIP, arEngine.ARBodyLandmarkType.LEFT_KNEE,
204. Color.Green);
205. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.LEFT_KNEE, arEngine.ARBodyLandmarkType.LEFT_ANKLE,
206. Color.Green);

208. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_SHOULDER,
209. arEngine.ARBodyLandmarkType.RIGHT_ELBOW, Color.Blue);
210. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_ELBOW,
211. arEngine.ARBodyLandmarkType.RIGHT_WRIST, Color.Blue);
212. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_HIP, arEngine.ARBodyLandmarkType.RIGHT_KNEE,
213. Color.Blue);
214. this.drawBodyBoneLine(bodyLandmarks, arEngine.ARBodyLandmarkType.RIGHT_KNEE,
215. arEngine.ARBodyLandmarkType.RIGHT_ANKLE, Color.Blue);
216. }

218. @Builder
219. drawBodyBoneLine(bodyLandmarks: Map<arEngine.ARBodyLandmarkType, arEngine.ARBodyLandmark2D>,
220. start: arEngine.ARBodyLandmarkType, end: arEngine.ARBodyLandmarkType, color: Color) {
221. if (bodyLandmarks.has(start) && bodyLandmarks.has(end)) {
222. Line()
223. .startPoint([this.uiContext.px2vp(bodyLandmarks.get(start)?.x),
224. this.uiContext.px2vp(bodyLandmarks.get(start)?.y)])
225. .endPoint([this.uiContext.px2vp(bodyLandmarks.get(end)?.x), this.uiContext.px2vp(bodyLandmarks.get(end)?.y)])
226. .stroke(color)
227. .strokeWidth(3)
228. }
229. }
230. }
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
