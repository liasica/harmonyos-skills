---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arengine-c-body
title: 人体跟踪与骨骼关键点识别（C/C++）
breadcrumb: 指南 > 图形 > AR Engine（AR引擎服务） > 人体骨骼点识别与跟踪 > 人体跟踪与骨骼关键点识别（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:46:57+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:987f9370f1c91fff99a012c65c51eb15d4c082e06064a60a14933c299f63dc34
---

## 约束与限制

人体跟踪与骨骼关键点识别能力支持部分Phone、部分Tablet设备、TV设备。请参考[硬件要求](arengine-preparations.md#硬件要求)判断设备是否支持运动跟踪及平面识别特性（[ARENGINE\_FEATURE\_TYPE\_BODY](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)）。

## 接口说明

人体跟踪与骨骼关键点识别主要依赖ARBody，以下接口为AR Engine人体跟踪与骨骼关键点识别相关接口，详细接口和说明，请参考[AR Engine API参考](../harmonyos-references/arengine-capi-arengine.md)。

| 接口名 | 描述 |
| --- | --- |
| [HMS\_AREngine\_ARBody\_GetSkeletonConfidence](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconfidence) | 获取人体对象每个骨骼点检测的置信度。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonConnection](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnection) | 获取人体对象骨骼点之间的链接关系数据。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonConnectionSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonconnectionsize) | 获取人体对象骨骼点之间的链接关系总数。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonTypes](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletontypes) | 获取识别出的人体对象骨骼点类型。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonPointCount](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointcount) | 获取人体对象的骨骼点个数。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonPointData2D](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointdata2d) | 当运行2D骨骼跟踪算法时，返回人体骨骼点的坐标数据。 |
| [HMS\_AREngine\_ARBody\_GetSkeletonPointIsValid](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getskeletonpointisvalid) | 获取人体对象骨骼点的坐标是否有效，返回有效性数组。 |
| [HMS\_AREngine\_ARBody\_GetBodyTrackId](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getbodytrackid) | 获取指定人体对象的标识。 |
| [HMS\_AREngine\_ARBody\_GetBodyTimeStamp](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arbody_getbodytimestamp) | 获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。 |
| [HMS\_AREngine\_ARConfig\_SetBodyDetectedNum](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arconfig_setbodydetectednum) | 设置追踪人数。 |

## 开发步骤

### 引入AR Engine

开发者可参考管理AR会话章节的[引入AR Engine](arengine-c-arsession.md#引入ar-engine)。

### 检查设备是否支持人体骨骼特性

调用[HMS\_AREngine\_CheckSupported](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_checksupported)方法，检查设备是否支持[ARENGINE\_FEATURE\_TYPE\_BODY](../harmonyos-references/arengine-capi-arengine.md#arengine_featuretype)人体骨骼特性。

### 创建UI界面

创建一个UI界面，使用[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)组件显示相机预览画面，定时触发每一帧绘制。

```
1. // 此代码可参考示例代码：ARSample/entry/src/main/ets/pages/ARBody.ets。
2. import { Landmark } from '../body/ArBodyInterface';
3. import { arEngine, arViewController } from '@kit.AREngine';
4. import { resourceManager } from '@kit.LocalizationKit';
5. import { ARConfig } from '../utils/Utils';
6. import { display } from '@kit.ArkUI';
7. import { systemDateTime } from '@kit.BasicServicesKit';
8. import arEngineDemo from 'libarenginedemo.so';

10. @Builder
11. export function ARBodyBuilder() {
12. ARBody();
13. }

15. interface ARBodyBoneLine {
16. start: arEngine.ARBodyLandmarkType,
17. end: arEngine.ARBodyLandmarkType,
18. }

20. @Entry
21. @ComponentV2
22. struct ARBody {
23. private interval: number = -1;
24. @Local context: Context = this.getUIContext().getHostContext() as Context;
25. private idStr: string = systemDateTime.getTime(false).toString() + 'ARBody';
26. private resMgr: resourceManager.ResourceManager = this.context.resourceManager;
27. private params: ARConfig = new ARConfig();
28. private isUpdate: boolean = false;
29. private DEFAULT_CONVERT_FACTOR: number = 4 / 3;
30. private boneLineNum: number = 26;
31. private landMarkNum: number = 20;
32. @Local displayWidth: number = display.getDefaultDisplaySync().width;
33. @Local displayHeight: number = display.getDefaultDisplaySync().height;
34. @Local rotation: number = display.getDefaultDisplaySync().rotation;
35. @Local arContext?: arViewController.ARViewContext = undefined;
36. @Local landmarks: Landmark[][] = [];
37. @Local boneLines: ARBodyBoneLine[][] = [];
38. @Local showPage: boolean = true;
39. private uiContext: UIContext = this.getUIContext();

41. @Builder
42. drawBodyPerception() {
43. Shape() {
44. ForEach(this.landmarks, (landmarks: Landmark[], index: number) => {
45. this.drawBodyLandmarks(index);
46. this.drawBodyBones(index);
47. })
48. }
49. .width(this.uiContext.px2vp(this.displayWidth))
50. .height(this.uiContext.px2vp(this.displayHeight))
51. }

53. @Builder
54. drawBodyLandmarks(bodyIndex: number) {
55. ForEach(this.landmarks[bodyIndex], (landmark: Landmark, index: number) => {
56. Circle({ width: 4, height: 4 })
57. .position({
58. x: this.uiContext.px2vp(landmark.x),
59. y: this.uiContext.px2vp(landmark.y)
60. })
61. .fill(Color.White)
62. })
63. }

65. @Builder
66. drawBodyBones(bodyIndex: number) {
67. if (this.boneLines.length > bodyIndex && this.landmarks[bodyIndex].length > 0) {
68. ForEach(this.boneLines[bodyIndex], (bone: ARBodyBoneLine, index: number) => {
69. this.drawBodyBoneLine(bone.start, bone.end, this.getLineColorByLineEnd(bone.end), bodyIndex);
70. })
71. }
72. }

74. @Builder
75. drawBodyBoneLine(start: arEngine.ARBodyLandmarkType, end: arEngine.ARBodyLandmarkType, color: Color, index: number) {
76. Line()
77. .startPoint([this.uiContext.px2vp(this.landmarks[index][start - 1]?.x),
78. this.uiContext.px2vp(this.landmarks[index][start - 1]?.y)])
79. .endPoint([this.uiContext.px2vp(this.landmarks[index][end - 1]?.x),
80. this.uiContext.px2vp(this.landmarks[index][end - 1]?.y)])
81. .stroke(color)
82. .strokeWidth(3)
83. }

85. private processLandMarks(res: Landmark[]): Landmark[][] {
86. if (display.getDefaultDisplaySync().width * 3 < display.getDefaultDisplaySync().height * 4) {
87. this.displayWidth = display.getDefaultDisplaySync().width;
88. this.displayHeight = this.displayWidth * this.DEFAULT_CONVERT_FACTOR;
89. } else {
90. this.displayHeight = display.getDefaultDisplaySync().height;
91. this.displayWidth = this.displayHeight * this.DEFAULT_CONVERT_FACTOR;
92. }

94. let ret: Landmark[][] = [];
95. let num = 0;
96. for (let i = 0; i < Math.min(this.params.maxDetectedBodyNum, res.length / this.landMarkNum); i++) {
97. ret.push([]);
98. for (let j = 0; j < this.landMarkNum; j++) {
99. ret[i].push({
100. x: res[num].x * this.displayWidth,
101. y: res[num].y * this.displayHeight
102. })
103. num++;
104. }
105. }
106. return ret;
107. }

109. private getBoneLines(res: number[]): ARBodyBoneLine[][] {
110. let ret: ARBodyBoneLine[][] = [];
111. let num = 0;
112. for (let i = 0; i < Math.min(this.params.maxDetectedBodyNum, res.length / this.boneLineNum); ++i) {
113. ret.push([]);
114. for (let j = 0; j < this.boneLineNum; j += 2) {
115. ret[i].push({
116. start: res[num],
117. end: res[num + 1]
118. });
119. num += 2;
120. }
121. }
122. return ret;
123. }

125. private runArBodyCheck(): void {
126. let config =
127. new Int32Array([0, this.params.powerMode, 1, this.params.previewMode, 2, this.rotation, 9,
128. this.params.cameraLensFacing, 10, this.params.maxDetectedBodyNum]);
129. arEngineDemo.init(this.resMgr);
130. arEngineDemo.start(this.idStr, config);
131. this.interval = setInterval(() => {
132. if (!this.isUpdate) {
133. return;
134. }
135. this.rotation = display.getDefaultDisplaySync().rotation;
136. arEngineDemo.update(this.idStr, this.rotation);
137. this.landmarks = this.processLandMarks(arEngineDemo.getLandmark(this.idStr));
138. const boneLines: number[] = arEngineDemo.getBoneLine(this.idStr).skeletonConnections;
139. this.boneLines = this.getBoneLines(boneLines)
140. }, 66);
141. }

143. private getLineColorByLineEnd(lineEnd: arEngine.ARBodyLandmarkType): Color {
144. switch (lineEnd) {
145. case arEngine.ARBodyLandmarkType.LEFT_ELBOW:
146. case arEngine.ARBodyLandmarkType.LEFT_WRIST:
147. case arEngine.ARBodyLandmarkType.LEFT_KNEE:
148. case arEngine.ARBodyLandmarkType.LEFT_ANKLE:
149. return Color.Green;
150. case arEngine.ARBodyLandmarkType.RIGHT_ELBOW:
151. case arEngine.ARBodyLandmarkType.RIGHT_WRIST:
152. case arEngine.ARBodyLandmarkType.RIGHT_KNEE:
153. case arEngine.ARBodyLandmarkType.RIGHT_ANKLE:
154. return Color.Blue;
155. case arEngine.ARBodyLandmarkType.RIGHT_SHOULDER:
156. case arEngine.ARBodyLandmarkType.RIGHT_HIP:
157. case arEngine.ARBodyLandmarkType.LEFT_SHOULDER:
158. case arEngine.ARBodyLandmarkType.LEFT_HIP:
159. default:
160. return Color.Orange;
161. }
162. }

164. build() {
165. NavDestination() {
166. RelativeContainer() {
167. Stack() {
168. XComponent({ id: this.idStr, type: XComponentType.SURFACE, libraryname: 'arenginedemo' })
169. .width(this.uiContext.px2vp(this.displayWidth))
170. .height(this.uiContext.px2vp(this.displayHeight))
171. .visibility(this.showPage ? Visibility.Visible : Visibility.None)
172. .alignRules({
173. center: { anchor: "__container__", align: VerticalAlign.Center },
174. middle: { anchor: "__container__", align: HorizontalAlign.Center }
175. })
176. this.drawBodyPerception()
177. }
178. .width('100%')
179. .height('100%')
180. }
181. }
182. .onAppear(async () => {
183. this.runArBodyCheck();
184. })
185. .onWillDisappear(() => {
186. clearInterval(this.interval);
187. arEngineDemo.stop(this.idStr);
188. })
189. .onShown(() => {
190. this.isUpdate = true;
191. arEngineDemo.show(this.idStr);
192. })
193. .onHidden(() => {
194. this.isUpdate = false;
195. arEngineDemo.hide(this.idStr);
196. })
197. .onReady(ctx => {
198. this.params = ctx.pathInfo.param as ARConfig;
199. })
200. .hideTitleBar(true)
201. .hideBackButton(true)
202. .hideToolBar(true)
203. .width('100%')
204. .height('100%')
205. }
206. }
```

### 创建AR会话

创建AR会话，配置人体跟踪模式。使用人体跟踪与骨骼关键点识别能力时请使用[HMS\_AREngine\_ARSession\_Create\_Human\_Perception](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_create_human_perception)创建AR会话。

```
1. AREngine_ARSession *arSession = nullptr;
2. // 创建AR会话。
3. HMS_AREngine_ARSession_Create_Human_Perception(nullptr, nullptr, &arSession);
4. AREngine_ARConfig *arConfig = nullptr;
5. // 创建AR会话配置器。
6. HMS_AREngine_ARConfig_Create(arSession, &arConfig);
7. // 设置人体跟踪模式的AR类型。
8. HMS_AREngine_ARConfig_SetARType(arSession, arConfig, ARENGINE_TYPE_BODY);
9. // 设置追踪人数，当前支持1或2
10. HMS_AREngine_ARConfig_SetBodyDetectedNum(arSession, arConfig, 1);
11. // 配置器设置给AR会话。
12. HMS_AREngine_ARSession_Configure(arSession, arConfig);
```

### 创建可跟踪对象列表

创建一个可跟踪对象列表targetList，用于存放AR Engine运行过程中检测到的所有可跟踪对象。

```
1. AREngine_ARTrackableList *targetList = nullptr;
2. HMS_AREngine_ARTrackableList_Create(arSession, &targetList);
```

### 获取人体追踪对象

调用[HMS\_AREngine\_ARSession\_GetAllTrackables](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_arsession_getalltrackables)函数，检测当前环境中的所有人体追踪对象，并将结果存放在targetList中。

```
1. HMS_AREngine_ARSession_GetAllTrackables(arSession, ARENGINE_TRACKABLE_BODY, targetList);
```

### 获取可跟踪对象数量

调用[HMS\_AREngine\_ARTrackableList\_GetSize](../harmonyos-references/arengine-capi-arengine.md#hms_arengine_artrackablelist_getsize)函数获取当前可跟踪对象数量，结果存放在targetSize中。

```
1. int32_t targetSize = 0;
2. HMS_AREngine_ARTrackableList_GetSize(arSession, targetList, &targetSize);
```

### 获取骨骼点相关信息

```
1. for (int i = 0; i < targetSize; i++) {
2. AREngine_ARTrackable *arTrackable = nullptr;
3. // 从可跟踪列表中获取指定index的对象。
4. HMS_AREngine_ARTrackableList_AcquireItem(arSession, targetList, i, &arTrackable);
5. // 转换为人体对象AREngine_ARBody。
6. AREngine_ARBody *arBody = reinterpret_cast<AREngine_ARBody *>(arTrackable);
7. int32_t pointCnt = 0;
8. // 获取人体对象的骨骼点个数。
9. HMS_AREngine_ARBody_GetSkeletonPointCount(arSession, arBody, &pointCnt);
10. const float *skeletonPoints2D = nullptr;
11. // 获取人体骨骼点的2D坐标数据。
12. HMS_AREngine_ARBody_GetSkeletonPointData2D(arSession, arBody, &skeletonPoints2D);
13. std::vector<float> skeletonPoints2Ds;
14. for (int j = 0; j < pointCnt * 2; j++) {
15. skeletonPoints2Ds.push_back(skeletonPoints2D[j]);
16. }
17. coord.push_back(skeletonPoints2Ds);
18. const float *skeletonConfidences = nullptr;
19. // 获取人体对象每个骨骼点检测的置信度。
20. HMS_AREngine_ARBody_GetSkeletonConfidence(arSession, arBody, &skeletonConfidences);
21. std::vector<float> skeletonConfidence2Ds;
22. for (int j = 0; j < pointCnt; j++) {
23. skeletonConfidence2Ds.push_back(skeletonConfidences[j]);
24. }
25. confidence.push_back(skeletonConfidence2Ds);
26. const int32_t *isValids = nullptr;
27. // 获取人体对象骨骼点的坐标是否有效。
28. HMS_AREngine_ARBody_GetSkeletonPointIsValid(arSession, arBody, &isValids);
29. std::vector<int32_t> skeletonValid2Ds;
30. for (int j = 0; j < pointCnt; j++) {
31. skeletonValid2Ds.push_back(isValids[j]);
32. }
33. valid.push_back(skeletonValid2Ds);
34. int32_t outBodyTrackId = 0;
35. // 获取指定人体对象的标识。
36. HMS_AREngine_ARBody_GetBodyTrackId(arSession, arBody, &outBodyTrackId);
37. int64_t timeStampNanoSec = 0;
38. // 获取人体对象的检测时间点，表示触发检测人体对象距离启动相机的时间间隔，单位为ns。
39. HMS_AREngine_ARBody_GetBodyTimeStamp(arSession, arBody, &timeStampNanoSec);
40. int32_t connectionSize = 0;
41. // 获取人体对象骨骼点之间的链接关系总数。
42. HMS_AREngine_ARBody_GetSkeletonConnectionSize(arSession, arBody, &connectionSize);
43. const AREngine_ARBodySkeletonType *skeletonConnections2D = nullptr;
44. // 获取人体对象骨骼点之间的链接关系数据。
45. HMS_AREngine_ARBody_GetSkeletonConnection(arSession, arBody, &skeletonConnections2D);
46. const AREngine_ARBodySkeletonType *skeletonTypes = nullptr;
47. // 获取识别出的人体对象骨骼点类型。
48. HMS_AREngine_ARBody_GetSkeletonTypes(arSession, arBody, &skeletonTypes);
49. std::vector<int32_t> skeletonValid2Ds;
50. for (int j = 0; j < connectionSize * 2; j++) {
51. skeletonValid2Ds.push_back(skeletonConnections2D[j]);
52. }
53. std::vector<int32_t> skeletonTypesVec;
54. for (int j = 0; j < sizeof(std::underlying_type_t<AREngine_ARBodySkeletonType>); j++) {
55. skeletonTypesVec.push_back(skeletonConnections2D[j]);
56. }
57. connections.push_back(skeletonValid2Ds);
58. types.push_back(skeletonTypesVec);
59. }
```

### 销毁可跟踪对象列表

可跟踪对象列表targetList不再使用后需销毁：

```
1. HMS_AREngine_ARTrackableList_Destroy(targetList);
```
