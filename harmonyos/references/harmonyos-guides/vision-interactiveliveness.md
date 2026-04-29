---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/vision-interactiveliveness
title: 人脸活体检测
breadcrumb: 指南 > AI > Vision Kit（场景化视觉服务） > 人脸活体检测
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f641010a69f20e5f19135366544239a54ef7caa598468362feae2d82375c2ba5
---

## 场景介绍

人脸活体检测支持动作活体检测模式。

动作活体检测支持实时捕捉人脸，需要用户配合做指定动作就可以判断是真实活体，还是非活体攻击（比如：打印图片、人脸翻拍视频以及人脸面具等）。

说明

活体检测是一项纯端侧算法、试用期免费的系统基础服务，推荐开发者使用在考勤打卡、辅助登录和实名认证等低危业务场景中。

端侧算法在HarmonyOS NEXT/5.0.x已完成权威机构（CFCA）检测认证。鉴于支付和金融应用的高风险性，建议开发者基于现有的安全性，针对不同的功能场景进行风险评估和风控策略评估，并采取必要的安全措施。

**图1** 权威认证**增强级**检测报告

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/GhSwIdwFScyF4sWC7uojzQ/zh-cn_image_0000002589245663.png?HW-CC-KV=V1&HW-CC-Date=20260429T054349Z&HW-CC-Expire=86400&HW-CC-Sign=8B458D8E9B307B7E385AE3E668AD085C9AD242E580D22D6016E9CEE9B1BFABDC)

**图2** 活体检测示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/4V-SRmn6SY-3_9iMZ9p_QA/zh-cn_image_0000002558765854.png?HW-CC-KV=V1&HW-CC-Date=20260429T054349Z&HW-CC-Expire=86400&HW-CC-Sign=251A9E8A397DE12C876E87759E0537878EC1512D79EC5CD1691DA49AE72F0717)

## 约束与限制

* 平板仅支持竖屏检测，大折叠屏仅支持折叠时使用，小折叠屏仅支持展开时使用。
* 支持的文本语种类型：简体中文、繁体中文、英文、维吾尔文、藏文。
* 支持的播报语种类型：简体中文、英文。
* 人脸活体检测服务暂不支持横屏、分屏进行检测。

## 接口说明

以下仅列出demo中调用的部分主要接口，具体API说明详见[API参考](../harmonyos-references/vision-interactive-liveness.md)。

| 接口名 | 描述 |
| --- | --- |
| [startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)(config: InteractiveLivenessConfig): Promise<boolean> | 跳转到人脸活体检测页面的入口 |
| [getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)(): Promise<InteractiveLivenessResult> | 获取人脸活体检测的结果。使用Promise异步回调 |

## 开发步骤

1. 将实现人脸活体检测相关的类添加至工程。

   ```
   1. import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
   2. import { interactiveLiveness } from '@kit.VisionKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在module.json5文件中添加CAMERA权限，其中reason，abilities标签必填，配置方式参见[requestPermissions标签说明](declare-permissions.md#在配置文件中声明权限)。

   ```
   1. "requestPermissions":[
   2. {
   3. "name": "ohos.permission.CAMERA",
   4. "reason": "$string:camera_desc",
   5. "usedScene": {"abilities": []}
   6. }
   7. ]
   ```
3. 简单配置页面的布局，选择人脸活体检测验证完后的跳转模式。如果使用back跳转模式，表示人脸活体检测完成后返回到上一页。如果使用replace跳转模式，表示人脸活体检测完跳转到成功或失败页面。默认选择的是replace跳转模式。

   ```
   1. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
   2. Text("验证完的跳转模式：")
   3. .fontSize(18)
   4. .width("25%")
   5. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
   6. Row() {
   7. Radio({ value: "replace", group: "routeMode" }).checked(true)
   8. .height(24)
   9. .width(24)
   10. .onChange((isChecked: boolean) => {
   11. this.routeMode = "replace"
   12. })
   13. Text("replace")
   14. .fontSize(16)
   15. }
   16. .margin({ right: 15 })

   18. Row() {
   19. Radio({ value: "back", group: "routeMode" }).checked(false)
   20. .height(24)
   21. .width(24)
   22. .onChange((isChecked: boolean) => {
   23. this.routeMode = "back";
   24. })
   25. Text("back")
   26. .fontSize(16)
   27. }
   28. }
   29. .width("75%")
   30. }
   ```
4. 如果选择动作活体模式，可填写验证的动作个数。

   ```
   1. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
   2. Text("动作数量：")
   3. .fontSize(18)
   4. .width("25%")
   5. TextInput({
   6. placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : "动作数量为3或4个"
   7. })
   8. .type(InputType.Number)
   9. .placeholderFont({
   10. size: 18,
   11. weight: FontWeight.Normal,
   12. family: "HarmonyHeiTi",
   13. style: FontStyle.Normal
   14. })
   15. .fontSize(18)
   16. .fontWeight(FontWeight.Bold)
   17. .fontFamily("HarmonyHeiTi")
   18. .fontStyle(FontStyle.Normal)
   19. .width("65%")
   20. .onChange((value: string) => {
   21. this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
   22. })
   23. }
   ```
5. 点击“开始检测“按钮，触发点击事件。

   ```
   1. Button("开始检测", { type: ButtonType.Normal, stateEffect: true })
   2. .width(192)
   3. .height(40)
   4. .fontSize(16)
   5. .backgroundColor(0x317aff)
   6. .borderRadius(20)
   7. .margin({
   8. bottom: 56
   9. })
   10. .onClick(() => {
   11. this.startDetection();
   12. })
   ```
6. 触发CAMERA权限校验。

   ```
   1. private context: common.UIAbilityContext = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
   2. private array: Array<Permissions> = ["ohos.permission.CAMERA"];
   3. // 校验CAMERA权限
   4. private startDetection() {
   5. abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
   6. for (let i = 0; i < res.permissions.length; i++) {
   7. if (res.permissions[i] === "ohos.permission.CAMERA" && res.authResults[i] === 0) {
   8. this.routerLibrary();
   9. }
   10. }
   11. }).catch((err: BusinessError) => {
   12. hilog.error(0x0001, "LivenessCollectionIndex", `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
   13. })
   14. }
   ```
7. 配置人脸活体检测控件的配置项[InteractiveLivenessConfig](../harmonyos-references/vision-interactive-liveness.md#interactivelivenessconfig)，用于跳转到人脸活体检测控件。

   配置中具体的参数可参考[API文档](../harmonyos-references/vision-interactive-liveness.md)。

   ```
   1. let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
   2. isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
   3. routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
   4. actionsNum: this.actionsNum
   5. };
   ```
8. 调用interactiveLiveness的[startLivenessDetection](../harmonyos-references/vision-interactive-liveness.md#startlivenessdetection)接口，判断跳转到人脸活体检测控件是否成功。

   ```
   1. // 跳转到人脸活体检测控件
   2. private routerLibrary() {
   3. if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
   4. interactiveLiveness.startLivenessDetection(routerOptions).then((isSuccess) => {
   5. if (isSuccess) {
   6. hilog.info(0x0001, "LivenessCollectionIndex", `Succeeded in jumping.`);
   7. } else {
   8. hilog.info(0x0001, "LivenessCollectionIndex", `Redirection failed.`);
   9. }
   10. }).catch((err: BusinessError) => {
   11. hilog.error(0x0001, "LivenessCollectionIndex", `Failed to jump. Code: ${err.code}, message: ${err.message}`);
   12. })
   13. } else {
   14. hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
   15. }
   16. }
   ```
9. 检测结束后回到当前界面，可调用interactiveLiveness的[getInteractiveLivenessResult](../harmonyos-references/vision-interactive-liveness.md#getinteractivelivenessresult)接口，验证人脸活体检测的结果。

   ```
   1. // 获取验证结果
   2. private getDetectionResultInfo() {
   3. // getInteractiveLivenessResult接口调用完会释放资源
   4. if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
   5. let resultInfo = interactiveLiveness.getInteractiveLivenessResult();
   6. resultInfo.then(data => {
   7. this.resultInfo = data;
   8. }).catch((err: BusinessError) => {
   9. this.failResult = {
   10. "code": err.code,
   11. "message": err.message
   12. }
   13. })
   14. } else {
   15. hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
   16. }
   17. }
   ```

## 开发实例

### Index.ets

```
1. import { common, abilityAccessCtrl, Permissions } from '@kit.AbilityKit';
2. import { interactiveLiveness } from '@kit.VisionKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. @Entry
7. @Component
8. struct LivenessCollectionIndex{
9. private context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
10. private array: Array<Permissions> = ["ohos.permission.CAMERA"];
11. @State actionsNum: number = 0;
12. @State isSilentMode: string = "INTERACTIVE_MODE";
13. @State routeMode: string = "replace";
14. @State resultInfo: interactiveLiveness.InteractiveLivenessResult = {
15. livenessType: 0
16. };
17. @State failResult: Record<string, number | string> = {
18. "code": 1008302000,
19. "message": ""
20. };

22. build() {
23. Stack({
24. alignContent: Alignment.Top
25. }) {
26. Column() {
27. Row() {
28. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
29. Text("验证完的跳转模式：")
30. .fontSize(18)
31. .width("25%")
32. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
33. Row() {
34. Radio({ value: "replace", group: "routeMode" }).checked(true)
35. .height(24)
36. .width(24)
37. .onChange(() => {
38. this.routeMode = "replace"
39. })
40. Text("replace")
41. .fontSize(16)
42. }
43. .margin({ right: 15 })

45. Row() {
46. Radio({ value: "back", group: "routeMode" }).checked(false)
47. .height(24)
48. .width(24)
49. .onChange(() => {
50. this.routeMode = "back";
51. })
52. Text("back")
53. .fontSize(16)
54. }
55. }
56. .width("75%")
57. }
58. }
59. .margin({ bottom: 30 })

61. Row() {
62. Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Start, alignItems: ItemAlign.Center }) {
63. Text("动作数量：")
64. .fontSize(18)
65. .width("25%")
66. TextInput({
67. placeholder: this.actionsNum != 0 ? this.actionsNum.toString() : "动作数量为3或4个"
68. })
69. .type(InputType.Number)
70. .placeholderFont({
71. size: 18,
72. weight: FontWeight.Normal,
73. family: "HarmonyHeiTi",
74. style: FontStyle.Normal
75. })
76. .fontSize(18)
77. .fontWeight(FontWeight.Bold)
78. .fontFamily("HarmonyHeiTi")
79. .fontStyle(FontStyle.Normal)
80. .width("65%")
81. .onChange((value: string) => {
82. this.actionsNum = Number(value) as interactiveLiveness.ActionsNumber;
83. })
84. }
85. }
86. }
87. .margin({ left: 24, top: 80 })
88. .zIndex(1)

90. Stack({
91. alignContent: Alignment.Bottom
92. }) {
93. if (this.resultInfo?.mPixelMap) {
94. Image(this.resultInfo?.mPixelMap)
95. .width(260)
96. .height(260)
97. .align(Alignment.Center)
98. .margin({ bottom: 260 })
99. Circle()
100. .width(300)
101. .height(300)
102. .fillOpacity(0)
103. .strokeWidth(60)
104. .stroke(Color.White)
105. .margin({ bottom: 250, left: 0 })
106. }

108. Text(this.resultInfo.mPixelMap ?
109. "检测成功" :
110. this.failResult.code != 1008302000 ?
111. "检测失败" :
112. "")
113. .width("100%")
114. .height(26)
115. .fontSize(20)
116. .fontColor("#000000")
117. .fontFamily("HarmonyHeiTi")
118. .margin({ top: 50 })
119. .textAlign(TextAlign.Center)
120. .fontWeight("Medium")
121. .margin({ bottom: 240 })

123. if(this.failResult.code != 1008302000) {
124. Text(this.failResult.message as string)
125. .width("100%")
126. .height(26)
127. .fontSize(16)
128. .fontColor(Color.Gray)
129. .textAlign(TextAlign.Center)
130. .fontFamily("HarmonyHeiTi")
131. .fontWeight("Medium")
132. .margin({ bottom: 200 })
133. }

135. Button("开始检测", { type: ButtonType.Normal, stateEffect: true })
136. .width(192)
137. .height(40)
138. .fontSize(16)
139. .backgroundColor(0x317aff)
140. .borderRadius(20)
141. .margin({
142. bottom: 56
143. })
144. .onClick(() => {
145. this.startDetection();
146. })
147. }
148. .height("100%")
149. }
150. }

152. onPageShow() {
153. this.resultRelease();
154. this.getDetectionResultInfo();
155. }

157. // 跳转到人脸活体检测控件
158. private routerLibrary() {
159. let routerOptions: interactiveLiveness.InteractiveLivenessConfig = {
160. isSilentMode: this.isSilentMode as interactiveLiveness.DetectionMode,
161. routeMode: this.routeMode as interactiveLiveness.RouteRedirectionMode,
162. actionsNum: this.actionsNum
163. }

165. if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
166. interactiveLiveness.startLivenessDetection(routerOptions).then((isSuccess) => {
167. if (isSuccess) {
168. hilog.info(0x0001, "LivenessCollectionIndex", `Succeeded in jumping.`);
169. } else {
170. hilog.info(0x0001, "LivenessCollectionIndex", `Redirection failed.`);
171. }
172. }).catch((err: BusinessError) => {
173. hilog.error(0x0001, "LivenessCollectionIndex", `Failed to jump. Code: ${err.code}, message: ${err.message}`);
174. })
175. } else {
176. hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
177. }
178. }

180. // 校验CAMERA权限
181. private startDetection() {
182. abilityAccessCtrl.createAtManager().requestPermissionsFromUser(this.context, this.array).then((res) => {
183. for (let i = 0; i < res.permissions.length; i++) {
184. if (res.permissions[i] === "ohos.permission.CAMERA" && res.authResults[i] === 0) {
185. this.routerLibrary();
186. }
187. }
188. }).catch((err: BusinessError) => {
189. hilog.error(0x0001, "LivenessCollectionIndex", `Failed to request permissions from user. Code is ${err.code}, message is ${err.message}`);
190. })
191. }

193. // 获取验证结果
194. private getDetectionResultInfo() {
195. // getInteractiveLivenessResult接口调用完会释放资源
196. if (canIUse("SystemCapability.AI.Component.LivenessDetect")) {
197. interactiveLiveness.getInteractiveLivenessResult().then(data => {
198. this.resultInfo = data;
199. }).catch((err: BusinessError) => {
200. this.failResult = {
201. "code": err.code,
202. "message": err.message
203. }
204. })
205. } else {
206. hilog.error(0x0001, "LivenessCollectionIndex", 'this api is not supported on this device');
207. }
208. }

210. // result release
211. private resultRelease() {
212. this.resultInfo = {
213. livenessType: 0
214. }
215. this.failResult = {
216. "code": 1008302000,
217. "message": ""
218. }
219. }
220. }
```
