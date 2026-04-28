---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-framenode
title: 自定义组件节点 (FrameNode)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 自定义组件节点 (FrameNode)
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:826e0a8156a4ac7ea622e679e5fa8e52fa85ed157d2910938985f807169a9ba0
---

## 概述

对于拥有自定义前端的第三方框架（如JSON、XML、DOM树等），需将特定的DSL转换为ArkUI的声明式描述。如下图描述了JSON定义的前端框架和ArkUI声明式描述的对应关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/PXjdY_XbQg29o2FZGGE8Vg/zh-cn_image_0000002583438051.png?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=533D624E015E03BD49CF2A75FC9B68A602AAA7F4533DD7D8A52F7A5E861D1E49)

上述转换过程需要依赖额外的数据驱动，绑定至[Builder](arkts-builder.md)中，较为复杂且性能欠佳。这类框架通常依赖于ArkUI的布局、事件处理、基础的节点操作和自定义能力。大部分组件通过自定义实现，但需结合使用部分系统组件以实现混合显示，如下图示例既使用了FrameNode的自定义方法进行绘制，又使用了系统组件Column及其子组件Text，通过BuilderNode的方式将其挂载到根节点的FrameNode上混合显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/YOmru27WRpybmyYQlmxcwA/zh-cn_image_0000002552958006.png?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=124F8FE3B9A2E6CFDF457D0A4912D0C354B3FE752DB22FD3C2B494BD316580B7)

[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)的设计初衷正是为了解决上述转换问题。FrameNode表示组件树中的实体节点，与自定义占位容器组件[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)相配合，实现在占位容器内构建一棵自定义的节点树。该节点树支持动态操作，如节点的增加、修改和删除。基础的FrameNode具备设置通用属性和事件回调的功能，同时提供完整的自定义能力，涵盖自定义测量、布局和绘制等方面。

除此之外，ArkUI还提供了获取和遍历系统组件对应代理FrameNode对象的能力（下文简称代理节点）。代理节点能够用于遍历整个UI的树形结构，支持获取系统组件节点的详细信息，以及额外注册组件的事件监听回调。

## 创建和删除节点

FrameNode提供了节点创建和删除的能力。可以通过FrameNode的构造函数创建自定义FrameNode节点，通过构造函数创建的节点对应一个实体的节点。同时，可以通过FrameNode中的[dispose](../harmonyos-references/js-apis-arkui-framenode.md#dispose12)接口来实现与实体节点的绑定关系的解除。

说明

* 在创建FrameNode对象的时候需要传入必选参数UIContext，若未传入UIContext对象或者传入不合法，则节点创建抛出异常。
* 自定义占位组件将节点进行显示的时候需要保证UI上下文一致，否则会出现显示异常。
* 若不持有FrameNode对象，则该对象会在GC的时候被回收。

## 判断节点是否可修改

[isModifiable](../harmonyos-references/js-apis-arkui-framenode.md#ismodifiable12)用于查询当前节点类型是否为系统组件的代理节点。当FrameNode节点作为系统组件的代理节点的时候，该节点不可修改。即无法修改代理节点的自身属性以及其子节点的结构。

## 获取对应的RenderNode节点

FrameNode提供了[getRenderNode](../harmonyos-references/js-apis-arkui-framenode.md#getrendernode)接口，用于获取FrameNode中的RenderNode。可以通过对获取到的RenderNode对象进行操作，动态修改FrameNode上绘制相关的属性，具体可修改的属性参考[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)的接口。

说明

* 无法获取系统组件代理FrameNode的RenderNode对象。
* BuilderNode中调用[getFrameNode](../harmonyos-references/js-apis-arkui-buildernode.md#getframenode)获取得到的FrameNode节点对象中，可以通过getRenderNode获取对应的根节点的RenderNode对象。

## 操作节点树

FrameNode提供了节点的增、删、查、改的能力，能够修改非代理节点的子树结构。可以对所有FrameNode的节点的父子节点做出查询操作，并返回查询结果。

说明

对节点进行增、删、改操作的时候，会对非法操作抛出异常信息。

通过查询获得的系统组件的代理节点，仅具备查询节点信息的作用，不具备修改节点属性的功能。代理节点不持有组件的实体节点，即不影响对应的节点的生命周期。

查询节点仅查询获得UI相关的节点，不返回语法节点。

使用自定义组件的场景下，可能查询获得自定义组件的新增节点，节点类型为“\_\_Common\_\_”。

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TEST_TAG: string = 'FrameNode'

7. class Params {
8. public text: string = 'this is a text'
9. }

11. @Builder
12. function buttonBuilder(params: Params) {
13. Column({ space: 10 }) {
14. Button(params.text)
15. .fontSize(12)
16. .borderRadius(8)
17. .borderWidth(2)
18. .backgroundColor(Color.Orange)

20. Button(params.text)
21. .fontSize(12)
22. .borderRadius(8)
23. .borderWidth(2)
24. .backgroundColor(Color.Pink)
25. }
26. }

28. class MyNodeController extends NodeController {
29. public buttonNode: BuilderNode<[Params]> | null = null;
30. public frameNode: FrameNode | null = null;
31. public childList: Array<FrameNode> = new Array<FrameNode>();
32. public rootNode: FrameNode | null = null;
33. private uiContext: UIContext | null = null;
34. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

36. makeNode(uiContext: UIContext): FrameNode | null {
37. this.uiContext = uiContext;
38. if (this.rootNode === null) {
39. this.rootNode = new FrameNode(uiContext);
40. this.rootNode.commonAttribute
41. .width('50%')
42. .height(100)
43. .borderWidth(1)
44. .backgroundColor(Color.Gray)
45. }

47. if (this.frameNode === null) {
48. this.frameNode = new FrameNode(uiContext);
49. this.frameNode.commonAttribute
50. .width('100%')
51. .height(50)
52. .borderWidth(1)
53. .position({ x: 200, y: 0 })
54. .backgroundColor(Color.Pink);
55. this.rootNode.appendChild(this.frameNode);
56. }
57. if (this.buttonNode === null) {
58. this.buttonNode = new BuilderNode<[Params]>(uiContext);
59. this.buttonNode.build(this.wrapBuilder, { text: 'This is a Button' })
60. this.rootNode.appendChild(this.buttonNode.getFrameNode())
61. }
62. return this.rootNode;
63. }

65. operationFrameNodeWithFrameNode(frameNode: FrameNode | undefined | null) {
66. if (frameNode) {
67. hilog.info(0x0000, `${TEST_TAG} get ArkTSNode success.`, 'success')
68. hilog.info(0x0000, `${TEST_TAG} check rootNode whether is modifiable ${frameNode.isModifiable()}`,
69. 'isModifiable');
70. }
71. if (this.uiContext) {
72. let frameNode1 = new FrameNode(this.uiContext);
73. let frameNode2 = new FrameNode(this.uiContext);
74. frameNode1.commonAttribute.size({ width: 50, height: 50 })
75. .backgroundColor(Color.Black)
76. .position({ x: 50, y: 60 })
77. frameNode2.commonAttribute.size({ width: 50, height: 50 })
78. .backgroundColor(Color.Orange)
79. .position({ x: 120, y: 60 })
80. try {
81. frameNode?.appendChild(frameNode1);
82. hilog.info(0x0000, `${TEST_TAG} appendChild success`, 'success');
83. } catch (err) {
84. hilog.error(0x0000, `${TEST_TAG} appendChild fail :${(err as BusinessError).code}:
85. ${(err as BusinessError).message}`, 'appendChild error');
86. }
87. try {
88. frameNode?.insertChildAfter(frameNode2, null);
89. hilog.info(0x0000, `${TEST_TAG} insertChildAfter success `, 'success');
90. } catch (err) {
91. hilog.error(0x0000, `${TEST_TAG} insertChildAfter fail :${(err as BusinessError).code}:
92. ${(err as BusinessError).message}`, 'insertChildAfter error');
93. }
94. setTimeout(() => {
95. try {
96. frameNode?.removeChild(frameNode?.getChild(0))
97. hilog.info(0x0000, `${TEST_TAG} removeChild success`, 'success');
98. } catch (err) {
99. hilog.error(0x0000, `${TEST_TAG} removeChild fail :${(err as BusinessError).code} :
100. ${(err as BusinessError).message}`, 'removeChild error');
101. }
102. }, 2000)
103. setTimeout(() => {
104. try {
105. frameNode?.clearChildren();
106. hilog.info(0x0000, `${TEST_TAG} clearChildren success `, 'success');
107. } catch (err) {
108. hilog.error(0x0000, `${TEST_TAG} clearChildren fail: (err as BusinessError).code:
109. ${(err as BusinessError).message}`, 'clearChildren error');
110. }
111. }, 4000)
112. }
113. }

115. testInterfaceAboutSearch(frameNode: FrameNode | undefined | null): string {
116. let result: string = '';
117. if (frameNode) {
118. result = result + `current node is ${frameNode.getNodeType()} \n`;
119. result = result + `parent node is ${frameNode.getParent()?.getNodeType()} \n`;
120. result = result + `child count is ${frameNode.getChildrenCount()} \n`;
121. result = result + `first child node is ${frameNode.getFirstChild()?.getNodeType()} \n`;
122. result = result + `second child node is ${frameNode.getChild(1)?.getNodeType()} \n`;
123. result = result + `previousSibling node is ${frameNode.getPreviousSibling()?.getNodeType()} \n`;
124. result = result + `nextSibling node is ${frameNode.getNextSibling()?.getNodeType()} \n`;
125. }
126. return result;
127. }

129. checkAppendChild(parent: FrameNode | undefined | null, child: FrameNode | undefined | null) {
130. try {
131. if (parent && child) {
132. parent.appendChild(child);
133. hilog.info(0x0000, `${TEST_TAG} appendChild success`, 'success');
134. }
135. } catch (err) {
136. console.error(`${TEST_TAG} appendChild fail : ${(err as BusinessError).code} : ${(err as BusinessError).message}`);
137. }
138. }
139. }

141. @Entry
142. @Component
143. struct Index {
144. @State index: number = 0;
145. @State result: string = ''
146. private myNodeController: MyNodeController = new MyNodeController();

148. build() {
149. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
150. List({ space: 20, initialIndex: 0 }) {
151. ListItem() {
152. Column({ space: 5 }) {
153. /**
154. * 请将$r('app.string.Verify_The_Child_Node_Function_Of_FrameNode')替换为实际资源文件，
155. * 在本示例中该资源文件的value值为"验证FrameNode子节点的增、删、改功能"
156. */
157. Text($r('app.string.Verify_The_Child_Node_Function_Of_FrameNode'))
158. // 请将$r('app.string.Operate_On_Custom_FrameNode')替换为实际资源文件，在本示例中该资源文件的value值为"对自定义FrameNode进行操作"
159. Button($r('app.string.Operate_On_Custom_FrameNode'))
160. .fontSize(16)
161. .width(400)
162. .onClick(() => {
163. // 对FrameNode节点进行增、删、改操作，正常实现。
164. this.myNodeController.operationFrameNodeWithFrameNode(this.myNodeController?.frameNode);
165. })
166. /**
167. * 请将$r('app.string.Operate_On_Proxy_Nodes_In_BuilderNode')替换为实际资源文件，
168. * 在本示例中该资源文件的value值为"对BuilderNode中的代理节点进行操作"
169. */
170. Button($r('app.string.Operate_On_Proxy_Nodes_In_BuilderNode'))
171. .fontSize(16)
172. .width(400)
173. .onClick(() => {
174. // 对BuilderNode代理节点进行增、删、改操作，捕获异常信息。
175. this.myNodeController.operationFrameNodeWithFrameNode
176. (this.myNodeController?.buttonNode?.getFrameNode());
177. })
178. /**
179. * 请将$r('app.string.Operate_On_Proxy_Nodes_In_System_Components')替换为实际资源文件，
180. * 在本示例中该资源文件的value值为"对系统组件中的代理节点进行操作"
181. */
182. Button($r('app.string.Operate_On_Proxy_Nodes_In_System_Components'))
183. .fontSize(16)
184. .width(400)
185. .onClick(() => {
186. // 对代理节点进行增、删、改操作，捕获异常信息。
187. this.myNodeController.operationFrameNodeWithFrameNode(this.myNodeController?.rootNode?.getParent());
188. })
189. }
190. }

192. ListItem() {
193. Column({ space: 5 }) {
194. /**
195. * 请将$r('app.string.Verify_Special_Scenarios_Of_FrameNode_Adding_Child_Nodes')替换为实际资源文件，
196. * 在本示例中该资源文件的value值为"验证FrameNode添加子节点的特殊场景"
197. */
198. Text($r('app.string.Verify_Special_Scenarios_Of_FrameNode_Adding_Child_Nodes'))
199. // 请将$r('app.string.Add_Proxy_Nodes_Of_BuilderNode')替换为实际资源文件，在本示例中该资源文件的value值为"新增BuilderNode的代理节点"
200. Button($r('app.string.Add_Proxy_Nodes_Of_BuilderNode'))
201. .fontSize(16)
202. .width(400)
203. .onClick(() => {
204. let buttonNode = new BuilderNode<[Params]>(this.getUIContext());
205. buttonNode.build(wrapBuilder<[Params]>(buttonBuilder), { text: 'BUTTON' })
206. this.myNodeController.checkAppendChild(this.myNodeController?.frameNode, buttonNode?.getFrameNode());
207. })
208. // 请将$r('app.string.Add_Proxy_Nodes_Of_System_Components')替换为实际资源文件，在本示例中该资源文件的value值为"新增系统组件代理节点"
209. Button($r('app.string.Add_Proxy_Nodes_Of_System_Components'))
210. .fontSize(16)
211. .width(400)
212. .onClick(() => {
213. this.myNodeController.checkAppendChild(this.myNodeController?.frameNode,
214. this.myNodeController?.rootNode?.getParent());
215. })
216. // 请将$r('app.string.Add_Custom_Nodes_With_Existing_Parent_Nodes')替换为实际资源文件，在本示例中该资源文件的value值为"新增已有父节点的自定义节点"
217. Button($r('app.string.Add_Custom_Nodes_With_Existing_Parent_Nodes'))
218. .fontSize(16)
219. .width(400)
220. .onClick(() => {
221. this.myNodeController.checkAppendChild(this.myNodeController?.frameNode,
222. this.myNodeController?.rootNode);
223. })
224. }
225. }

227. ListItem() {
228. Column({ space: 5 }) {
229. // 请将$r('app.string.Verify_Query_Function_Of_FrameNode')替换为实际资源文件，在本示例中该资源文件的value值为"验证FrameNode节点的查询功能"
230. Text($r('app.string.Verify_Query_Function_Of_FrameNode'))
231. // 请将$r('app.string.Operate_On_Custom_FrameNode_Again')替换为实际资源文件，在本示例中该资源文件的value值为"对自定义FrameNode进行操作"
232. Button($r('app.string.Operate_On_Custom_FrameNode_Again'))
233. .fontSize(16)
234. .width(400)
235. .onClick(() => {
236. // 对FrameNode节点进行进行查询。当前节点为NodeContainer的子节点。
237. this.result = this.myNodeController.testInterfaceAboutSearch(this.myNodeController?.rootNode);
238. setTimeout(() => {
239. // 对FrameNode节点进行进行查询。rootNode下的第一个子节点。
240. this.result = this.myNodeController.testInterfaceAboutSearch(this.myNodeController?.frameNode);
241. }, 2000)
242. })
243. /**
244. * 请将$r('app.string.Operate_On_Proxy_Nodes_In_BuilderNode_Again')替换为实际资源文件，
245. * 在本示例中该资源文件的value值为"对BuilderNode中的代理节点进行操作"
246. */
247. Button($r('app.string.Operate_On_Proxy_Nodes_In_BuilderNode_Again'))
248. .fontSize(16)
249. .width(400)
250. .onClick(() => {
251. // 对BuilderNode代理节点进行进行查询。当前节点为BuilderNode中的Column节点。
252. this.result =
253. this.myNodeController.testInterfaceAboutSearch(this.myNodeController?.buttonNode?.getFrameNode());
254. })
255. /**
256. * 请将$r('app.string.Operate_On_Proxy_Nodes_In_System_Components_Again')替换为实际资源文件，
257. * 在本示例中该资源文件的value值为"对系统组件中的代理节点进行操作"
258. */
259. Button($r('app.string.Operate_On_Proxy_Nodes_In_System_Components_Again'))
260. .fontSize(16)
261. .width(400)
262. .onClick(() => {
263. // 对代理节点进行查询。当前节点为NodeContainer。
264. this.result =
265. this.myNodeController.testInterfaceAboutSearch(this.myNodeController?.rootNode?.getParent());
266. })
267. }
268. }
269. }.height('50%')

271. Text(`Result：\n${this.result}`)
272. .fontSize(16)
273. .width(400)
274. .height(200)
275. .padding(30)
276. .borderWidth(1)
277. Column() {
278. Text('This is a NodeContainer.')
279. .textAlign(TextAlign.Center)
280. .borderRadius(10)
281. .backgroundColor(0xFFFFFF)
282. .width('100%')
283. .fontSize(16)
284. NodeContainer(this.myNodeController)
285. .borderWidth(1)
286. .width(400)
287. .height(150)
288. }
289. }
290. .padding({
291. left: 35,
292. right: 35,
293. top: 35,
294. bottom: 35
295. })
296. .width('100%')
297. .height('100%')
298. }
299. }
```

[FrameNodeTree.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeTree.ets#L16-L306)

## 使用moveTo移动命令式节点

使用[moveTo](../harmonyos-references/js-apis-arkui-framenode.md#moveto18)接口可以将FrameNode节点移动到新的父节点下，从而按需改变节点树结构。

说明

当前FrameNode如果不可修改，抛出异常信息。

目标父节点为[typeNode](../harmonyos-references/js-apis-arkui-framenode.md#typenode12)时会校验子组件类型或个数，不满足抛出异常信息，限制情况请查看[typeNode](../harmonyos-references/js-apis-arkui-framenode.md#typenode12)描述。

当前不支持对无组件类型的命令式节点进行移动。

当前仅支持以下类型的[TypedFrameNode](../harmonyos-references/js-apis-arkui-framenode.md#typedframenode12)进行移动操作：[Stack](../harmonyos-references/js-apis-arkui-framenode.md#stack12)、[XComponent](../harmonyos-references/js-apis-arkui-framenode.md#xcomponent12)。对于其他类型的节点，移动操作不会生效。

当前仅支持根节点为以下类型组件的[BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md#buildernode-1)进行移动操作：[Stack](../harmonyos-references/ts-container-stack.md)、[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)、[EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md)。对于其他类型的组件，移动操作不会生效。

```
1. import { FrameNode, NodeController, UIContext, typeNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. public uiContext: UIContext | null = null;
5. public rootNode: FrameNode | null = null;
6. public rowNode: FrameNode | null = null;
7. public stackNode1: FrameNode | null = null;
8. public stackNode2: FrameNode | null = null;
9. public stackNode3: FrameNode | null = null;

11. makeNode(uiContext: UIContext): FrameNode | null {
12. this.uiContext = uiContext;
13. this.rootNode = new FrameNode(uiContext);

15. const row = typeNode.createNode(this.uiContext, 'Row');
16. row.initialize({ space: 10 });
17. this.rowNode = row;
18. this.rootNode.appendChild(this.rowNode);

20. const stack1 = typeNode.createNode(this.uiContext, 'Stack');
21. stack1.commonAttribute.width(50).height(50).backgroundColor(Color.Pink);
22. this.stackNode1 = stack1;
23. this.rowNode?.appendChild(this.stackNode1);
24. const stack2 = typeNode.createNode(this.uiContext, 'Stack');
25. stack2.commonAttribute.width(50).height(50).backgroundColor(Color.Yellow);
26. this.stackNode2 = stack2;
27. this.rowNode?.appendChild(this.stackNode2);
28. const stack3 = typeNode.createNode(this.uiContext, 'Stack');
29. stack3.commonAttribute.width(50).height(50).backgroundColor(Color.Green);
30. this.stackNode3 = stack3;
31. this.rowNode?.appendChild(this.stackNode3);

33. return this.rootNode;
34. }
35. }

37. @Entry
38. @Component
39. struct Index {
40. private myNodeController1: MyNodeController = new MyNodeController()
41. private myNodeController2: MyNodeController = new MyNodeController()

43. build() {
44. Column({ space: 20 }) {
45. NodeContainer(this.myNodeController1)
46. NodeContainer(this.myNodeController2)
47. Button('move')
48. .onClick(() => {
49. this.myNodeController1.stackNode1?.moveTo(this.myNodeController2.rowNode, 2);
50. })
51. }
52. .height('100%')
53. .width('100%')
54. }
55. }
```

[FrameNodeMoveTo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeMoveTo.ets#L16-L72)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/Rc7tMzWuRb-3g6yoNsQvqQ/zh-cn_image_0000002583478007.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=C9B892B707C1301303251F99D9F6FE4166FDB42D2BDA9CD68545A8A666DCF581)

## 设置节点通用属性和事件回调

FrameNode提供了[commonAttribute](../harmonyos-references/js-apis-arkui-framenode.md#commonattribute12)和[commonEvent](../harmonyos-references/js-apis-arkui-framenode.md#commonevent12)两个对象用于设置节点的[通用属性](../harmonyos-references/ts-component-general-attributes.md)和[设置事件回调](../harmonyos-references/ts-uicommonevent.md)。

说明

* 由于代理节点的属性不可修改，因此通过代理节点的commonAttribute修改节点的基础属性不生效。
* 设置的基础事件与系统组件定义的事件平行，参与事件竞争。设置的基础事件不覆盖系统组件事件。同时设置两个事件回调的时候，优先回调系统组件事件。

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Params {
5. public text: string = 'this is a text';
6. }

8. @Builder
9. function buttonBuilder(params: Params) {
10. Button(params.text)
11. .fontSize(12)
12. .borderRadius(8)
13. .borderWidth(2)
14. .backgroundColor(Color.Orange)
15. .onClick((event: ClickEvent) => {
16. hilog.info(0x0000, `Button ${JSON.stringify(event)}`, 'isClicked');
17. })
18. }

20. class MyNodeController extends NodeController {
21. public buttonNode: BuilderNode<[Params]> | null = null;
22. public frameNode: FrameNode | null = null;
23. public rootNode: FrameNode | null = null;
24. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

26. makeNode(uiContext: UIContext): FrameNode | null {
27. if (this.rootNode === null) {
28. this.rootNode = new FrameNode(uiContext);
29. // 对rootNode进行属性修改，该节点为自定义的FrameNode节点，修改生效
30. this.rootNode.commonAttribute
31. .width('100%')
32. .height(100)
33. .borderWidth(1)
34. .backgroundColor(Color.Gray)
35. }

37. if (this.frameNode === null) {
38. this.frameNode = new FrameNode(uiContext);
39. // 对frameNode进行属性修改，该节点为自定义的FrameNode节点，修改生效
40. this.frameNode.commonAttribute
41. .width('50%')
42. .height(50)
43. .borderWidth(1)
44. .backgroundColor(Color.Pink);
45. this.rootNode.appendChild(this.frameNode);
46. }
47. if (this.buttonNode === null) {
48. this.buttonNode = new BuilderNode<[Params]>(uiContext);
49. this.buttonNode.build(this.wrapBuilder, { text: 'This is a Button' });
50. // 对BuilderNode中获取的FrameNode进行属性修改，该节点非自定义的FrameNode节点，修改不生效
51. this.buttonNode?.getFrameNode()?.commonAttribute.position({ x: 100, y: 100 });
52. this.rootNode.appendChild(this.buttonNode.getFrameNode());
53. }
54. return this.rootNode;
55. }

57. modifyNode(frameNode: FrameNode | null | undefined, sizeValue: SizeOptions, positionValue: Position) {
58. if (frameNode) {
59. frameNode.commonAttribute.size(sizeValue).position(positionValue);
60. }
61. }

63. addClickEvent(frameNode: FrameNode | null | undefined) {
64. if (frameNode) {
65. frameNode.commonEvent.setOnClick((event: ClickEvent) => {
66. console.info(`FrameNode ${JSON.stringify(event)}`);
67. })
68. }
69. }
70. }

72. @Entry
73. @Component
74. struct Index {
75. private myNodeController: MyNodeController = new MyNodeController();

77. build() {
78. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
79. Column({ space: 10 }) {
80. // 请将$r('app.string.Modify_Node_Common_Properties_Width_And_Height')替换为实际资源文件，在本示例中该资源文件的value值为"修改节点通用属性-宽高"
81. Text($r('app.string.Modify_Node_Common_Properties_Width_And_Height'))
82. Button('modify ArkTS-FrameNode')
83. .onClick(() => {
84. // 获取到的是当前页面中的开发者创建的FrameNode对象，该节点可修改。即节点大小与位置。
85. hilog.info(0x0000, `Check the weather the node can be modified ${this.myNodeController?.frameNode
86. ?.isModifiable()}`, 'isClicked');
87. this.myNodeController.modifyNode(this.myNodeController?.frameNode, { width: 150, height: 100 }, {
88. x: 100,
89. y: 0
90. });
91. })
92. Button('modify FrameNode get by BuilderNode')
93. .onClick(() => {
94. // 获取到的是当前页面中的BuilderNode的根节点，该节点不可修改。即节点大小与位置未发生改变。
95. hilog.info(0x0000, `Check the weather the node can be modified
96. ${this.myNodeController?.buttonNode?.getFrameNode()
97. ?.isModifiable()}`, 'isClicked');
98. this.myNodeController.modifyNode(this.myNodeController?.buttonNode?.getFrameNode(), {
99. width: 100,
100. height: 100
101. }, { x: 50, y: 50 });
102. })
103. Button('modify proxyFrameNode get by search')
104. .onClick(() => {
105. // rootNode调用getParent()获取到的是当前页面中的NodeContainer节点，该节点不可修改。即节点大小与位置未发生改变。
106. hilog.info(0x0000,
107. `Check the weather the node can be modified ${this.myNodeController?.rootNode?.getParent()
108. ?.isModifiable()}`, 'isClicked');
109. this.myNodeController.modifyNode(this.myNodeController?.rootNode?.getParent(), {
110. width: 500,
111. height: 500
112. }, {
113. x: 0,
114. y: 0
115. });
116. })
117. }
118. .padding({
119. left: 35,
120. right: 35,
121. top: 35,
122. bottom: 35
123. })

125. Column({ space: 10 }) {
126. // 请将$r('app.string.Modify_Node_Click_Event')替换为实际资源文件，在本示例中该资源文件的value值为"修改节点点击事件"
127. Text($r('app.string.Modify_Node_Click_Event'))
128. Button('add click event to ArkTS-FrameNode')
129. .onClick(() => {
130. // 获取到的是当前页面中的开发者创建的FrameNode对象，该节点可增加点击事件。
131. // 增加的点击事件参与事件竞争，即点击事件会在该节点被消费且不不再向父组件冒泡。
132. hilog.info(0x0000,
133. `Check the weather the node can be modified ${this.myNodeController?.rootNode?.getParent()
134. ?.isModifiable()}`, 'isClicked');
135. this.myNodeController.addClickEvent(this.myNodeController?.frameNode);
136. })
137. Button('add click event to FrameNode get by BuilderNode')
138. .onClick(() => {
139. // 获取到的是当前页面中的BuilderNode的根节点，该类节点可增加点击事件。
140. // 点击的时候优先回调通过系统组件接口设置的click事件回调，然后回调通过commonEvent增加的click监听。
141. hilog.info(0x0000, `Check the weather the node can be modified
142. ${this.myNodeController?.buttonNode?.getFrameNode()
143. ?.isModifiable()}`, 'isClicked');
144. this.myNodeController.addClickEvent(this.myNodeController?.buttonNode?.getFrameNode());
145. })
146. Button('add click event to proxyFrameNode get by search')
147. .onClick(() => {
148. // rootNode调用getParent()获取到的是当前页面中的NodeContainer节点，该类节点可增加点击事件。
149. hilog.info(0x0000,
150. `Check the weather the node can be modified ${this.myNodeController?.rootNode?.getParent()
151. ?.isModifiable()}`, 'isClicked');
152. this.myNodeController.addClickEvent(this.myNodeController?.rootNode?.getParent());
153. })
154. }
155. .padding({
156. left: 35,
157. right: 35,
158. top: 35,
159. bottom: 35
160. })

162. NodeContainer(this.myNodeController)
163. .borderWidth(1)
164. .width('100%')
165. .height(100)
166. .onClick((event: ClickEvent) => {
167. hilog.info(0x0000, `NodeContainer ${JSON.stringify(event)}`, 'isClicked');
168. })
169. }
170. .padding({
171. left: 35,
172. right: 35,
173. top: 35,
174. bottom: 35
175. })
176. .width('100%')
177. .height('100%')
178. }
179. }
```

[FrameNodeCommon.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeCommon.ets#L16-L196)

## 自定义测量布局与绘制

通过重写[onDraw](../harmonyos-references/js-apis-arkui-framenode.md#ondraw12)方法，可以自定义FrameNode的绘制内容。[invalidate](../harmonyos-references/js-apis-arkui-framenode.md#invalidate12)接口可以主动触发节点的重新绘制。

通过重写[onMeasure](../harmonyos-references/js-apis-arkui-framenode.md#onmeasure12)可以自定义FrameNode的测量方式，使用[measure](../harmonyos-references/js-apis-arkui-framenode.md#measure12)可以主动传递布局约束触发重新测量。

通过重写[onLayout](../harmonyos-references/js-apis-arkui-framenode.md#onlayout12)方法可以自定义FrameNode的布局方式，使用[layout](../harmonyos-references/js-apis-arkui-framenode.md#layout12)方法可以主动传递位置信息并触发重新布局。

[setNeedsLayout](../harmonyos-references/js-apis-arkui-framenode.md#setneedslayout12)可以将当前节点标记，在下一帧触发重新布局。

说明

* 对节点进行dispose解引用后，由于FrameNode对象不再对应一个实体节点，invalidate无法触发原有绑定节点的刷新。
* 通过onDraw方法进行的自定义绘制，绘制内容大小无法超出组件大小。

```
1. import { DrawContext, FrameNode, NodeController, Position, Size, UIContext, LayoutConstraint } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. function getChildLayoutConstraint(constraint: LayoutConstraint, child: FrameNode): LayoutConstraint {
6. // 获取子节点用户设置的宽高
7. const size = child.getUserConfigSize();

9. // 计算子节点宽度
10. const width = Math.max(
11. Math.min(constraint.maxSize.width, size.width.value),
12. constraint.minSize.width
13. );

15. // 计算子节点高度
16. const height = Math.max(
17. Math.min(constraint.maxSize.height, size.height.value),
18. constraint.minSize.height
19. );
20. const finalSize: Size = { width, height };
21. const res: LayoutConstraint = {
22. maxSize: finalSize,
23. minSize: finalSize,
24. percentReference: finalSize
25. };

27. return res;
28. }

30. class MyFrameNode extends FrameNode {
31. public width: number = 100;
32. public offsetY: number = 0;
33. private space: number = 1;
34. private uiContext: UIContext;

36. constructor(uiContext: UIContext) {
37. super(uiContext);
38. this.uiContext = uiContext;
39. }

41. // 重写布局测量方法
42. onMeasure(constraint: LayoutConstraint): void {
43. let sizeRes: Size = { width: this.uiContext.vp2px(100), height: this.uiContext.vp2px(100) };

45. // 遍历所有子节点，计算总尺寸
46. for (let i = 0; i < this.getChildrenCount(); i++) {
47. let child = this.getChild(i);
48. if (child) {
49. let childConstraint = getChildLayoutConstraint(constraint, child);
50. child.measure(childConstraint); // 触发子节点的测量
51. let size = child.getMeasuredSize();
52. sizeRes.height += size.height + this.space;
53. sizeRes.width = Math.max(sizeRes.width, size.width);
54. }
55. }
56. this.setMeasuredSize(sizeRes);
57. }

59. // 重写布局排列方法
60. onLayout(position: Position): void {
61. for (let i = 0; i < this.getChildrenCount(); i++) {
62. let child = this.getChild(i);
63. if (child) {
64. child.layout({
65. x: this.uiContext.vp2px(100),
66. y: this.uiContext.vp2px(this.offsetY)
67. });
68. let layoutPosition = child.getLayoutPosition();
69. hilog.info(0x0000, 'testTag', `child position: ${JSON.stringify(layoutPosition)}`);
70. }
71. }
72. this.setLayoutPosition(position);
73. }

75. // 重写自定义绘制方法
76. onDraw(context: DrawContext) {
77. const canvas = context.canvas;
78. const pen = new drawing.Pen();
79. pen.setStrokeWidth(15);
80. pen.setColor({
81. alpha: 255,
82. red: 255,
83. green: 0,
84. blue: 0
85. });
86. canvas.attachPen(pen);
87. canvas.drawRect({
88. left: 50,
89. right: this.width + 50,
90. top: 50,
91. bottom: this.width + 50,
92. });
93. canvas.detachPen();
94. }

96. addWidth() {
97. this.width = (this.width + 10) % 50 + 100;
98. }
99. }

101. class MyNodeController extends NodeController {
102. public rootNode: MyFrameNode | null = null;

104. makeNode(context: UIContext): FrameNode | null {
105. this.rootNode = new MyFrameNode(context);
106. this.rootNode?.commonAttribute?.size({ width: 100, height: 100 }).backgroundColor(Color.Green);
107. let frameNode: FrameNode = new FrameNode(context);
108. this.rootNode.appendChild(frameNode);
109. frameNode.commonAttribute.width(10).height(10).backgroundColor(Color.Pink);
110. return this.rootNode;
111. }
112. }

114. @Entry
115. @Component
116. struct Index {
117. private nodeController: MyNodeController = new MyNodeController();

119. build() {
120. Row() {
121. Column() {
122. NodeContainer(this.nodeController)
123. .width('100%')
124. .height(200)
125. .backgroundColor('#FFF0F0F0')

127. // 触发节点重绘
128. Button('Invalidate')
129. .margin(10)
130. .onClick(() => {
131. this.nodeController?.rootNode?.addWidth();
132. this.nodeController?.rootNode?.invalidate();
133. })

135. // 触发布局更新
136. Button('UpdateLayout')
137. .onClick(() => {
138. let node = this.nodeController.rootNode;
139. node!.offsetY = (node!.offsetY + 10) % 110;
140. this.nodeController?.rootNode?.setNeedsLayout();
141. })
142. }
143. .width('100%')
144. .height('100%')
145. }
146. .height('100%')
147. }
148. }
```

[FrameNodeDraw.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeDraw.ets#L16-L166)

## 查找节点及获取基础信息

FrameNode提供了查询接口用于返回实体节点的基础信息。具体返回的信息内容参考FrameNode中提供的接口。

查找获得FrameNode的方式包括三种：

1. 使用[getFrameNodeById](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getframenodebyid12)获取。
2. 使用[getFrameNodeByUniqueId](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getframenodebyuniqueid12)获取。
3. 通过[无感监听](../harmonyos-references/js-apis-arkui-observer.md)获取。

说明

1、当前接口提供的可查询的信息包括：

* 节点大小：[getMeasuredSize](../harmonyos-references/js-apis-arkui-framenode.md#getmeasuredsize12)，[getUserConfigSize](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigsize12)
* 布局信息：[getPositionToWindow](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontowindow12)，[getPositionToParent](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoparent12)，[getLayoutPosition](../harmonyos-references/js-apis-arkui-framenode.md#getlayoutposition12)，[getUserConfigBorderWidth](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigborderwidth12)，[getUserConfigPadding](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigpadding12)，[getUserConfigMargin](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigmargin12)
* 节点信息：[getId](../harmonyos-references/js-apis-arkui-framenode.md#getid12)，[getUniqueId](../harmonyos-references/js-apis-arkui-framenode.md#getuniqueid12)，[getNodeType](../harmonyos-references/js-apis-arkui-framenode.md#getnodetype12)，[getOpacity](../harmonyos-references/js-apis-arkui-framenode.md#getopacity12)，[isVisible](../harmonyos-references/js-apis-arkui-framenode.md#isvisible12)，[isClipToFrame](../harmonyos-references/js-apis-arkui-framenode.md#iscliptoframe12)，[isAttached](../harmonyos-references/js-apis-arkui-framenode.md#isattached12)，[getInspectorInfo](../harmonyos-references/js-apis-arkui-framenode.md#getinspectorinfo12)，[getCustomProperty](../harmonyos-references/js-apis-arkui-framenode.md#getcustomproperty12)

2、无法获取UINode类型节点，例如：JsView节点、[Span](../harmonyos-references/ts-basic-components-span.md)、[ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md)、[ContentSlot](../harmonyos-references/ts-components-contentslot.md)、[ForEach](../harmonyos-references/ts-rendering-control-foreach.md)、[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)、if/else组件等。

## 获取节点位置偏移信息

FrameNode提供了查询节点相对窗口、父组件以及屏幕位置偏移的信息接口（[getPositionToWindow](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontowindow12)，[getPositionToParent](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoparent12)，[getPositionToScreen](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoscreen12)，[getGlobalPositionOnDisplay](../harmonyos-references/js-apis-arkui-framenode.md#getglobalpositionondisplay20)，[getPositionToWindowWithTransform](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontowindowwithtransform12)，[getPositionToParentWithTransform](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoparentwithtransform12)，[getPositionToScreenWithTransform](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoscreenwithtransform12)，[getLayoutPosition](../harmonyos-references/js-apis-arkui-framenode.md#getlayoutposition12)，[getUserConfigBorderWidth](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigborderwidth12)，[getUserConfigPadding](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigpadding12)，[getUserConfigMargin](../harmonyos-references/js-apis-arkui-framenode.md#getuserconfigmargin12)）。

[getPositionToWindow](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontowindow12)，[getPositionToParent](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoparent12)，[getPositionToScreen](../harmonyos-references/js-apis-arkui-framenode.md#getpositiontoscreen12)三个接口获取到的位置信息关系如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/lhK6jafNSUq5Uz_yqaaZeA/zh-cn_image_0000002552798358.png?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=9B6F9CED5ABB9C10D8E8717F7AD42550356722F610059C3B76CCC466277C6F05)

```
1. import { NodeController, FrameNode, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TEST_TAG: string = 'FrameNode'

6. class MyNodeController extends NodeController {
7. public frameNode: FrameNode | null = null;
8. private rootNode: FrameNode | null = null;

10. makeNode(uiContext: UIContext): FrameNode | null {
11. this.rootNode = new FrameNode(uiContext);
12. this.frameNode = new FrameNode(uiContext);
13. this.rootNode.appendChild(this.frameNode);
14. return this.rootNode;
15. }

17. getPositionToWindow() {
18. let positionToWindow = this.rootNode?.getPositionToWindow(); // 获取FrameNode相对于窗口的位置偏移
19. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionToWindow)}`, 'positionToWindow');
20. }

22. getPositionToParent() {
23. let positionToParent = this.rootNode?.getPositionToParent(); // 获取FrameNode相对于父组件的位置偏移
24. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionToParent)}`, 'positionToParent');
25. }

27. getPositionToScreen() {
28. let positionToScreen = this.rootNode?.getPositionToScreen(); // 获取FrameNode相对于屏幕的位置偏移
29. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionToScreen)}`, 'positionToScreen');
30. }

32. getGlobalPositionOnDisplay() {
33. let positionOnGlobalDisplay = this.rootNode?.getGlobalPositionOnDisplay(); // 获取FrameNode相对于全局屏幕的位置偏移
34. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionOnGlobalDisplay)}`, 'positionOnGlobalDisplay');
35. }

37. getPositionToWindowWithTransform() {
38. let positionToWindowWithTransform =
39. this.rootNode?.getPositionToWindowWithTransform(); // 获取FrameNode相对于窗口带有绘制属性的位置偏移
40. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionToWindowWithTransform)}`, 'positionToWindowWithTransform');
41. }

43. getPositionToParentWithTransform() {
44. let positionToParentWithTransform =
45. this.rootNode?.getPositionToParentWithTransform(); // 获取FrameNode相对于父组件带有绘制属性的位置偏移
46. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionToParentWithTransform)}`, 'positionToParentWithTransform');
47. }

49. getPositionToScreenWithTransform() {
50. let positionToScreenWithTransform =
51. this.rootNode?.getPositionToScreenWithTransform(); // 获取FrameNode相对于屏幕带有绘制属性的位置偏移
52. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(positionToScreenWithTransform)}`, 'positionToScreenWithTransform');
53. }
54. }

56. @Entry
57. @Component
58. struct Index {
59. private myNodeController: MyNodeController = new MyNodeController();

61. build() {
62. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
63. Button('getPositionToWindow')
64. .width(300)
65. .onClick(() => {
66. this.myNodeController.getPositionToWindow();
67. })
68. Button('getPositionToParent')
69. .width(300)
70. .onClick(() => {
71. this.myNodeController.getPositionToParent();
72. })
73. Button('getPositionToScreen')
74. .width(300)
75. .onClick(() => {
76. this.myNodeController.getPositionToScreen();
77. })
78. Button('getGlobalPositionOnDisplay')
79. .width(300)
80. .onClick(() => {
81. this.myNodeController.getGlobalPositionOnDisplay();
82. })
83. Button('getPositionToParentWithTransform')
84. .width(300)
85. .onClick(() => {
86. this.myNodeController.getPositionToParentWithTransform();
87. })
88. Button('getPositionToWindowWithTransform')
89. .width(300)
90. .onClick(() => {
91. this.myNodeController.getPositionToWindowWithTransform();
92. })
93. Button('getPositionToScreenWithTransform')
94. .width(300)
95. .onClick(() => {
96. this.myNodeController.getPositionToScreenWithTransform();
97. })
98. Column() {
99. Text('This is a NodeContainer.')
100. .textAlign(TextAlign.Center)
101. .borderRadius(10)
102. .backgroundColor(0xFFFFFF)
103. .width('100%')
104. .fontSize(16)
105. NodeContainer(this.myNodeController)
106. .borderWidth(1)
107. .width(300)
108. .height(100)
109. }
110. }
111. .padding({
112. left: 35,
113. right: 35,
114. top: 35,
115. bottom: 35
116. })
117. .width('100%')
118. .height('100%')
119. }
120. }
```

[FrameNodePosition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodePosition.ets#L16-L137)

## 通过typeNode创建具体类型的FrameNode节点

通过TypeNode创建具体类型的FrameNode节点，可以根据属性获取接口来检索用户设置的属性信息。

```
1. import { NodeController, FrameNode, UIContext, BuilderNode, typeNode } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Params {
5. text: string = '';

7. constructor(text: string) {
8. this.text = text;
9. }
10. }

12. @Builder
13. function buildText(params: Params) {
14. Column() {
15. Text(params.text)
16. .id('buildText')
17. .border({ width: 1 })
18. .padding(1)
19. .fontSize(25)
20. .fontWeight(FontWeight.Bold)
21. .margin({ top: 10 })
22. .visibility(Visibility.Visible)
23. .opacity(0.7)
24. .customProperty('key1', 'value1')
25. .width(300)
26. }
27. }

29. const TEST_TAG: string = 'FrameNode'

31. class MyNodeController extends NodeController {
32. public frameNode: typeNode.Column | null = null;
33. public uiContext: UIContext | undefined = undefined;
34. private rootNode: FrameNode | null = null;
35. private textNode: BuilderNode<[Params]> | null = null;
36. public textTypeNode: typeNode.Text | null = null;
37. private message: string = 'DEFAULT';

39. makeNode(uiContext: UIContext): FrameNode | null {
40. this.rootNode = new FrameNode(uiContext);
41. this.uiContext = uiContext;
42. this.frameNode = typeNode.createNode(uiContext, 'Column');
43. this.frameNode.attribute
44. .width('100%')
45. .height('100%')
46. this.rootNode.appendChild(this.frameNode);
47. this.textNode = new BuilderNode(uiContext);
48. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
49. this.frameNode.appendChild(this.textNode.getFrameNode());
50. this.textTypeNode = typeNode.createNode(uiContext, 'Text');
51. this.textTypeNode.initialize('textTypeNode')
52. .fontSize(25)
53. .visibility(Visibility.Visible)
54. .id('textTypeNode')
55. this.frameNode.appendChild(this.textTypeNode);
56. return this.rootNode;
57. }

59. removeChild(frameNode: FrameNode) {
60. let parent = frameNode.getParent();
61. if (parent) {
62. parent.removeChild(frameNode);

64. }
65. }

67. getUserConfigBorderWidth(frameNode: FrameNode) {
68. let userConfigBorderWidth = frameNode?.getUserConfigBorderWidth(); // 获取用户设置的边框宽度
69. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(userConfigBorderWidth)}`, 'userConfigBorderWidth');
70. }

72. getUserConfigPadding(frameNode: FrameNode) {
73. let userConfigPadding = frameNode?.getUserConfigPadding(); // 获取用户设置的内边距
74. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(userConfigPadding)}`, 'userConfigPadding');
75. }

77. getUserConfigMargin(frameNode: FrameNode) {
78. let userConfigMargin = frameNode?.getUserConfigMargin(); // 获取用户设置的外边距
79. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(userConfigMargin)}`, 'userConfigMargin');
80. }

82. getUserConfigSize(frameNode: FrameNode) {
83. let userConfigSize = frameNode?.getUserConfigSize(); // 获取用户设置的宽高
84. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(userConfigSize)}`, 'userConfigSize');
85. }

87. getId(frameNode: FrameNode) {
88. let id = frameNode?.getId(); // 获取用户设置的节点ID
89. hilog.info(0x0000, `${TEST_TAG} ${id}`, 'getId');
90. }

92. getUniqueId(frameNode: FrameNode) {
93. let uniqueId = frameNode?.getUniqueId(); // 获取系统分配的唯一标识的节点UniqueID
94. hilog.info(0x0000, `${TEST_TAG} ${uniqueId}`, 'uniqueId');
95. }

97. getNodeType(frameNode: FrameNode) {
98. let nodeType = frameNode?.getNodeType(); // 获取节点的类型
99. hilog.info(0x0000, `${TEST_TAG} ${nodeType}`, 'nodeType');
100. }

102. getOpacity(frameNode: FrameNode) {
103. let opacity = frameNode?.getOpacity(); // 获取节点的不透明度
104. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(opacity)}`, 'opacity');
105. }

107. isVisible(frameNode: FrameNode) {
108. let visible = frameNode?.isVisible(); // 获取节点是否可见
109. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(visible)}`, 'visible');
110. }

112. isClipToFrame(frameNode: FrameNode) {
113. let clipToFrame = frameNode?.isClipToFrame(); // 获取节点是否是剪裁到组件区域
114. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(clipToFrame)}`, 'clipToFrame');
115. }

117. isAttached(frameNode: FrameNode) {
118. let attached = frameNode?.isAttached(); // 获取节点是否被挂载到主节点树上
119. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(attached)}`, 'attached');
120. }

122. getInspectorInfo(frameNode: FrameNode) {
123. let inspectorInfo = frameNode?.getInspectorInfo(); // 获取节点的结构信息
124. hilog.info(0x0000, `${TEST_TAG} ${JSON.stringify(inspectorInfo)}`, 'inspectorInfo');
125. }
126. }

128. @Entry
129. @Component
130. struct Index {
131. private myNodeController: MyNodeController = new MyNodeController();
132. @State index: number = 0;

134. build() {
135. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
136. Column() {
137. Text('This is a NodeContainer.')
138. .textAlign(TextAlign.Center)
139. .borderRadius(10)
140. .backgroundColor(0xFFFFFF)
141. .width('100%')
142. .fontSize(16)
143. NodeContainer(this.myNodeController)
144. .borderWidth(1)
145. .width(300)
146. .height(100)
147. }

149. Button('getUserConfigBorderWidth')
150. .width(300)
151. .onClick(() => {
152. const uiContext: UIContext = this.getUIContext();
153. if (uiContext) {
154. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
155. if (node) {
156. this.myNodeController.getUserConfigBorderWidth(node);
157. }
158. }
159. })
160. Button('getUserConfigPadding')
161. .width(300)
162. .onClick(() => {
163. const uiContext: UIContext = this.getUIContext();
164. if (uiContext) {
165. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
166. if (node) {
167. this.myNodeController.getUserConfigPadding(node);
168. }
169. }
170. })
171. Button('getUserConfigMargin')
172. .width(300)
173. .onClick(() => {
174. const uiContext: UIContext = this.getUIContext();
175. if (uiContext) {
176. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
177. if (node) {
178. this.myNodeController.getUserConfigMargin(node);
179. }
180. }
181. })
182. Button('getUserConfigSize')
183. .width(300)
184. .onClick(() => {
185. const uiContext: UIContext = this.getUIContext();
186. if (uiContext) {
187. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
188. if (node) {
189. this.myNodeController.getUserConfigSize(node);
190. }
191. }
192. })
193. Button('getId')
194. .width(300)
195. .onClick(() => {
196. const uiContext: UIContext = this.getUIContext();
197. if (uiContext) {
198. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
199. if (node) {
200. this.myNodeController.getId(node);
201. }
202. }
203. })
204. Button('getUniqueId')
205. .width(300)
206. .onClick(() => {
207. const uiContext: UIContext = this.getUIContext();
208. if (uiContext) {
209. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
210. if (node) {
211. this.myNodeController.getUniqueId(node);
212. }
213. }
214. })
215. Button('getNodeType')
216. .width(300)
217. .onClick(() => {
218. const uiContext: UIContext = this.getUIContext();
219. if (uiContext) {
220. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
221. if (node) {
222. this.myNodeController.getNodeType(node);
223. }
224. }
225. })
226. Button('getOpacity')
227. .width(300)
228. .onClick(() => {
229. const uiContext: UIContext = this.getUIContext();
230. if (uiContext) {
231. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
232. if (node) {
233. this.myNodeController.getOpacity(node);
234. }
235. }
236. })
237. Button('isVisible')
238. .width(300)
239. .onClick(() => {
240. const uiContext: UIContext = this.getUIContext();
241. if (uiContext) {
242. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
243. if (node) {
244. this.myNodeController.isVisible(node);
245. }
246. }
247. })
248. Button('isClipToFrame')
249. .width(300)
250. .onClick(() => {
251. const uiContext: UIContext = this.getUIContext();
252. if (uiContext) {
253. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
254. if (node) {
255. this.myNodeController.isClipToFrame(node);
256. }
257. }
258. })
259. Button('isAttached')
260. .width(300)
261. .onClick(() => {
262. const uiContext: UIContext = this.getUIContext();
263. if (uiContext) {
264. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
265. if (node) {
266. this.myNodeController.isAttached(node);
267. }
268. }
269. })
270. Button('remove Text')
271. .width(300)
272. .onClick(() => {
273. const uiContext: UIContext = this.getUIContext();
274. if (uiContext) {
275. const node: FrameNode | null = uiContext.getFrameNodeById('textTypeNode') || null;
276. if (node) {
277. this.myNodeController.removeChild(node);
278. this.myNodeController.isAttached(node);
279. }
280. }
281. })
282. Button('getInspectorInfo')
283. .width(300)
284. .onClick(() => {
285. const uiContext: UIContext = this.getUIContext();
286. if (uiContext) {
287. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
288. if (node) {
289. this.myNodeController.getInspectorInfo(node);
290. }
291. }
292. })
293. Button('getCustomProperty')
294. .width(300)
295. .onClick(() => {
296. const uiContext: UIContext = this.getUIContext();
297. if (uiContext) {
298. const node: FrameNode | null = uiContext.getFrameNodeById('buildText') || null;
299. if (node) {
300. const property = node.getCustomProperty('key1');
301. hilog.info(0x0000, TEST_TAG, JSON.stringify(property));
302. }
303. }
304. })
305. }
306. .padding({
307. left: 35,
308. right: 35,
309. top: 35,
310. bottom: 35
311. })
312. .width('100%')
313. .height('100%')
314. }
315. }
```

[FrameNodeTypeNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeTypeNode.ets#L16-L332)

## 解除当前FrameNode对象对实体FrameNode节点的引用关系

使用[dispose](../harmonyos-references/js-apis-arkui-framenode.md#dispose12)接口可以立即解除当前FrameNode对象对实体FrameNode节点的引用关系。

说明

在调用dispose方法后，FrameNode对象不再对应任何实际的FrameNode节点。此时，若尝试调用以下查询接口：getMeasuredSize、getLayoutPosition、getUserConfigBorderWidth、getUserConfigPadding、getUserConfigMargin、getUserConfigSize，将导致应用程序触发[jscrash](arkts-stability-guide.md#jscrash)。

通过[getUniqueId](../harmonyos-references/js-apis-arkui-framenode.md#getuniqueid12)可以判断当前FrameNode是否对应一个实体FrameNode节点。当UniqueId大于0时表示该对象对应一个实体FrameNode节点。

```
1. import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TEST_TAG: string = 'FrameNode';

6. @Component
7. struct TestComponent {
8. build() {
9. Column() {
10. Text('This is a BuilderNode.')
11. .fontSize(16)
12. .fontWeight(FontWeight.Bold)
13. }
14. .width('100%')
15. .backgroundColor(Color.Gray)
16. }

18. aboutToAppear() {
19. console.info(`${TEST_TAG} aboutToAppear`);
20. }

22. aboutToDisappear() {
23. console.info(`${TEST_TAG} aboutToDisappear`);
24. }
25. }

27. @Builder
28. function buildComponent() {
29. TestComponent()
30. }

32. class MyNodeController extends NodeController {
33. private rootNode: FrameNode | null = null;
34. private builderNode: BuilderNode<[]> | null = null;

36. // 创建并初始化自定义节点树
37. makeNode(uiContext: UIContext): FrameNode | null {
38. this.rootNode = new FrameNode(uiContext);
39. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 200, height: 100 } });
40. this.builderNode.build(new WrappedBuilder(buildComponent));

42. const rootRenderNode = this.rootNode.getRenderNode();
43. if (rootRenderNode !== null) {
44. rootRenderNode.size = { width: 200, height: 200 };
45. rootRenderNode.backgroundColor = 0xff00ff00;
46. rootRenderNode.appendChild(this.builderNode!.getFrameNode()!.getRenderNode());
47. }

49. return this.rootNode;
50. }

52. // 打印节点的唯一ID
53. printUniqueId(): void {
54. if (this.rootNode !== null && this.builderNode !== null) {
55. hilog.info(0x0000, `${TEST_TAG} rootNode's uniqueId: ${this.rootNode.getUniqueId()}`, 'isClicked');
56. const frameNode = this.builderNode.getFrameNode();
57. if (frameNode) {
58. hilog.info(0x0000, `${TEST_TAG} the uniqueId of builderNode's framenode: ${frameNode.getUniqueId()}`,
59. 'isClicked');
60. } else {
61. hilog.info(0x0000, `${TEST_TAG} builderNode's framenode is undefined`, 'isClicked');
62. }
63. }
64. }

66. // 销毁所有自定义节点
67. disposeFrameNode(): void {
68. if (this.rootNode !== null && this.builderNode !== null) {
69. hilog.info(0x0000, `${TEST_TAG} disposeFrameNode`, 'isCLicked');
70. this.rootNode.removeChild(this.builderNode.getFrameNode());
71. this.builderNode.dispose();

73. this.rootNode.dispose();
74. }
75. }

77. removeBuilderNode(): void {
78. const rootRenderNode = this.rootNode!.getRenderNode();
79. if (rootRenderNode !== null && this.builderNode !== null && this.builderNode.getFrameNode() !== null) {
80. // 从根渲染节点中移除BuilderNode的渲染节点
81. rootRenderNode.removeChild(this.builderNode!.getFrameNode()!.getRenderNode());
82. }
83. }
84. }

86. @Entry
87. @Component
88. struct Index {
89. private myNodeController: MyNodeController = new MyNodeController();

91. build() {
92. Column({ space: 4 }) {
93. NodeContainer(this.myNodeController)
94. Button('FrameNode dispose')
95. .onClick(() => {
96. this.myNodeController.printUniqueId();
97. this.myNodeController.disposeFrameNode(); // 执行节点销毁
98. this.myNodeController.printUniqueId();
99. })
100. .width('100%')
101. }
102. }
103. }
```

[FrameNodeDisposed.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeDisposed.ets#L16-L120)

## 查询当前FrameNode是否解除引用

前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。

从API version 20开始，使用[isDisposed](../harmonyos-references/js-apis-arkui-framenode.md#isdisposed20)接口查询当前FrameNode对象是否已解除与后端实体节点的引用关系，从而可以在操作节点前检查其有效性，避免潜在风险。

```
1. import { NodeController, FrameNode } from '@kit.ArkUI';

3. class MyNodeController extends NodeController {
4. private rootNode: FrameNode | null = null;

6. makeNode(uiContext: UIContext): FrameNode | null {
7. this.rootNode = new FrameNode(uiContext);
8. this.rootNode.commonAttribute.width(100)
9. .height(100)
10. .backgroundColor(Color.Pink);

12. return this.rootNode;
13. }

15. disposeFrameNode() {
16. // 解除当前FrameNode对象对实体FrameNode节点的引用关系
17. this.rootNode?.dispose();
18. }

20. isDisposed(): string {
21. if (this.rootNode !== null) {
22. // 查询FrameNode是否解除引用
23. if (this.rootNode.isDisposed()) {
24. return 'frameNode isDisposed is true';
25. } else {
26. return 'frameNode isDisposed is false';
27. }
28. }
29. return 'frameNode is null';
30. }
31. }

33. @Entry
34. @Component
35. struct Index {
36. @State text: string = ''
37. private myNodeController: MyNodeController = new MyNodeController();

39. build() {
40. Column({ space: 4 }) {
41. NodeContainer(this.myNodeController)
42. Button('FrameNode dispose')
43. .onClick(() => {
44. this.myNodeController.disposeFrameNode();
45. this.text = '';
46. })
47. .width(200)
48. .height(50)
49. Button('FrameNode isDisposed')
50. .onClick(() => {
51. this.text = this.myNodeController.isDisposed();
52. })
53. .width(200)
54. .height(50)
55. Text(this.text)
56. .fontSize(25)
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

[FrameNodeIsDisposed.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeIsDisposed.ets#L16-L78)

## FrameNode的数据懒加载能力

提供[NodeAdapter](../harmonyos-references/js-apis-arkui-framenode.md#nodeadapter12)对象替代ArkTS侧的LazyForEach功能，提供自定义节点的数据懒加载功能，实现按需迭代数据。

说明

入参不能为负数，入参为负数时不做处理。

```
1. import { FrameNode, NodeController, NodeAdapter, typeNode } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TEST_TAG: string = 'FrameNode';

6. class MyNodeAdapter extends NodeAdapter {
7. uiContext: UIContext;
8. cachePool: FrameNode[] = new Array();
9. changed: boolean = false;
10. reloadTimes: number = 0;
11. data: Array<string> = new Array();
12. hostNode?: FrameNode;

14. constructor(uiContext: UIContext, count: number) {
15. super();
16. this.uiContext = uiContext;
17. this.totalNodeCount = count;
18. this.loadData();
19. }

21. // 重新加载列表数据
22. reloadData(count: number): void {
23. this.reloadTimes++;
24. NodeAdapter.attachNodeAdapter(this, this.hostNode);
25. this.totalNodeCount = count;
26. this.loadData();
27. this.reloadAllItems();
28. }

30. // 刷新数据
31. refreshData(): void {
32. let items = this.getAllAvailableItems()
33. hilog.info(0x0000, `TEST_TAG ' get All items:' + ${items.length}`, 'isCLicked');
34. this.totalNodeCount -= 1;
35. this.reloadAllItems();
36. }

38. // 解除适配器与宿主节点的绑定
39. detachData(): void {
40. NodeAdapter.detachNodeAdapter(this.hostNode);
41. this.reloadTimes = 0;
42. }

44. // 根据当前节点总数和重载次数生成列表项的文本数据
45. loadData(): void {
46. for (let i = 0; i < this.totalNodeCount; i++) {
47. this.data[i] = 'Adapter ListItem ' + i + ' r:' + this.reloadTimes;
48. }
49. }

51. // 修改指定范围的列表数据
52. changeData(from: number, count: number): void {
53. this.changed = !this.changed;
54. for (let i = 0; i < count; i++) {
55. let index = i + from;
56. this.data[index] = 'Adapter ListItem ' + (this.changed ? 'changed:' : '') + index + ' r:' + this.reloadTimes;
57. }
58. this.reloadItem(from, count);
59. }

61. // 插入数据到指定位置
62. insertData(from: number, count: number): void {
63. for (let i = 0; i < count; i++) {
64. let index = i + from;
65. this.data.splice(index, 0, 'Adapter ListItem ' + from + '-' + i);
66. }
67. this.insertItem(from, count); // 通知列表插入对应节点
68. this.totalNodeCount += count;
69. hilog.info(0x0000, `TEST_TAG after insert count ${this.totalNodeCount}`, 'insertData');
70. }

72. // 从指定位置删除数据
73. removeData(from: number, count: number): void {
74. let arr = this.data.splice(from, count);
75. this.removeItem(from, count);
76. this.totalNodeCount -= arr.length;
77. hilog.info(0x0000, `TEST_TAG after remove count: ${this.totalNodeCount}`, 'removeData');
78. }

80. moveData(from: number, to: number): void {
81. let tmp = this.data.splice(from, 1);
82. this.data.splice(to, 0, tmp[0]);
83. this.moveItem(from, to); // 通知列表移动节点位置
84. }

86. onAttachToNode(target: FrameNode): void {
87. hilog.info(0x0000, `TEST_TAG onAttachToNode id: ${target.getUniqueId()}`, 'onAttachToNode');
88. this.hostNode = target;
89. }

91. // 适配器从宿主节点解绑时触发
92. onDetachFromNode(): void {
93. hilog.info(0x0000, 'TEST_TAG onDetachFromNode', 'onDetachFromNode');
94. }

96. // 获取指定索引的子节点ID
97. onGetChildId(index: number): number {
98. hilog.info(0x0000, `TEST_TAG onGetChildId: ${index}`, 'onGetChildId');
99. return index;
100. }

102. onCreateChild(index: number): FrameNode {
103. hilog.info(0x0000, `TEST_TAG + ' onCreateChild:' + ${index}`, 'onCreateChild');
104. // 缓存池有可用节点时，优先复用
105. if (this.cachePool.length > 0) {
106. let cacheNode = this.cachePool.pop();
107. if (cacheNode !== undefined) {
108. hilog.info(0x0000, `TEST_TAG onCreateChild reused id: ${cacheNode.getUniqueId()}`, 'getUniqueId');
109. let text = cacheNode?.getFirstChild();
110. let textNode = text as typeNode.Text;
111. textNode?.initialize(this.data[index]).fontSize(20);
112. return cacheNode;
113. }
114. }
115. // 无缓存时创建新节点
116. hilog.info(0x0000, 'TEST_TAG onCreateChild createNew', 'createNew');
117. let itemNode = typeNode.createNode(this.uiContext, 'ListItem');
118. let textNode = typeNode.createNode(this.uiContext, 'Text');
119. textNode.initialize(this.data[index]).fontSize(20);
120. itemNode.appendChild(textNode);
121. return itemNode;
122. }

124. onDisposeChild(id: number, node: FrameNode): void {
125. hilog.info(0x0000, `TEST_TAG onDisposeChild: ${id}`, 'onDisposeChild');
126. if (this.cachePool.length < 10) {
127. if (!this.cachePool.includes(node)) {
128. hilog.info(0x0000, `TEST_TAG caching node id: ${node.getUniqueId()}`, 'getUniqueId');
129. this.cachePool.push(node);
130. }
131. } else {
132. node.dispose();
133. }
134. }

136. onUpdateChild(id: number, node: FrameNode): void {
137. let index = id;
138. let text = node.getFirstChild();
139. let textNode = text as typeNode.Text;
140. textNode?.initialize(this.data[index]).fontSize(20);
141. }
142. }

144. class MyNodeAdapterController extends NodeController {
145. private rootNode: FrameNode | null = null;
146. public nodeAdapter: MyNodeAdapter | null = null;

148. makeNode(uiContext: UIContext): FrameNode | null {
149. this.rootNode = new FrameNode(uiContext);
150. // 创建List节点并配置样式
151. let listNode = typeNode.createNode(uiContext, 'List');
152. listNode.initialize({ space: 3 }).borderWidth(2).borderColor(Color.Black);
153. this.rootNode.appendChild(listNode);
154. // 初始化适配器并关联到List节点
155. this.nodeAdapter = new MyNodeAdapter(uiContext, 100);
156. NodeAdapter.attachNodeAdapter(this.nodeAdapter, listNode);
157. return this.rootNode;
158. }
159. }

161. @Entry
162. @Component
163. struct Index {
164. adapterController: MyNodeAdapterController = new MyNodeAdapterController();
165. aboutToDisappear(): void {
166. this.adapterController.nodeAdapter?.dispose();
167. }
168. build() {
169. Column() {
170. Text('ListNode Adapter');
171. NodeContainer(this.adapterController)
172. .width(300).height(300)
173. .borderWidth(1).borderColor(Color.Black)
174. Row() {
175. Button('Reload')
176. .onClick(() => {
177. this.adapterController.nodeAdapter?.reloadData(50);
178. })
179. Button('Change')
180. .onClick(() => {
181. this.adapterController.nodeAdapter?.changeData(5, 10)
182. })
183. Button('Insert')
184. .onClick(() => {
185. this.adapterController.nodeAdapter?.insertData(10, 10);
186. })
187. }

189. Row() {
190. Button('Remove')
191. .onClick(() => {
192. this.adapterController.nodeAdapter?.removeData(10, 10);
193. })
194. Button('Move')
195. .onClick(() => {
196. this.adapterController.nodeAdapter?.moveData(2, 5);
197. })
198. Button('Refresh')
199. .onClick(() => {
200. this.adapterController.nodeAdapter?.refreshData();
201. })
202. Button('Detach')
203. .onClick(() => {
204. this.adapterController.nodeAdapter?.detachData();
205. })
206. }
207. }.borderWidth(1)
208. .width('100%')
209. }
210. }
```

[FrameNodeLazyForEach.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeLazyForEach.ets#L16-L227)

## 查询LazyForEach中的FrameNode节点信息

如果FrameNode子节点中包含[LazyForEach](../harmonyos-references/ts-rendering-control-lazyforeach.md)节点，[getChild](../harmonyos-references/js-apis-arkui-framenode.md#getchild15)接口支持指定子节点展开模式[ExpandMode](../harmonyos-references/js-apis-arkui-framenode.md#expandmode15)，以不同展开模式获取子节点。

当前支持如下子节点展开模式：

* ExpandMode.NOT\_EXPAND：表示不展开当前FrameNode的子节点。如果FrameNode子节点中包含LazyForEach节点，获取在主节点树上的子节点时，不展开当前FrameNode的子节点。子节点序列号按在主节点树上的子节点计算。
* ExpandMode.EXPAND：表示展开当前FrameNode的子节点。如果FrameNode子节点中包含LazyForEach节点，获取任何子节点时，展开当前FrameNode的子节点。子节点序列号按所有子节点计算。
* ExpandMode.LAZY\_EXPAND：表示按需展开当前FrameNode的子节点。如果FrameNode子节点中包含LazyForEach节点，获取在主节点树上的子节点时，不展开当前FrameNode的子节点；获取不在主节点树上的子节点时，展开当前FrameNode的子节点。子节点序列号按所有子节点计算。

可以使用[getFirstChildIndexWithoutExpand](../harmonyos-references/js-apis-arkui-framenode.md#getfirstchildindexwithoutexpand15)和[getLastChildIndexWithoutExpand](../harmonyos-references/js-apis-arkui-framenode.md#getlastchildindexwithoutexpand15)获取当前节点第一个和最后一个在主节点树上的子节点的序列号，其中子节点序列号按所有子节点计算。

```
1. import { NodeController, FrameNode, UIContext, BuilderNode, ExpandMode, LengthUnit } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TEST_TAG: string = 'FrameNode ';

6. // BasicDataSource实现了IDataSource接口，用于管理listener监听，以及通知LazyForEach数据更新
7. class BasicDataSource implements IDataSource {
8. private listeners: DataChangeListener[] = [];
9. private originDataArray: string[] = [];

11. public totalCount(): number {
12. return 0;
13. }

15. public getData(index: number): string {
16. return this.originDataArray[index];
17. }

19. // 该方法为框架侧调用，为LazyForEach组件向其数据源处添加listener监听
20. registerDataChangeListener(listener: DataChangeListener): void {
21. if (this.listeners.indexOf(listener) < 0) {
22. hilog.info(0x0000, 'add listener', 'registerDataChangeListener');
23. this.listeners.push(listener);
24. }
25. }

27. // 该方法为框架侧调用，为对应的LazyForEach组件在数据源处去除listener监听
28. unregisterDataChangeListener(listener: DataChangeListener): void {
29. const pos = this.listeners.indexOf(listener);
30. if (pos >= 0) {
31. hilog.info(0x0000, 'remove listener', 'unregisterDataChangeListener');
32. this.listeners.splice(pos, 1);
33. }
34. }

36. // 通知LazyForEach组件需要重载所有子组件
37. notifyDataReload(): void {
38. this.listeners.forEach(listener => {
39. listener.onDataReloaded();
40. })
41. }

43. // 通知LazyForEach组件需要在index对应索引处添加子组件
44. notifyDataAdd(index: number): void {
45. this.listeners.forEach(listener => {
46. listener.onDataAdd(index);
47. // 写法2：listener.onDatasetChange([{type: DataOperationType.ADD, index: index}]);
48. })
49. }

51. // 通知LazyForEach组件在index对应索引处数据有变化，需要重建该子组件
52. notifyDataChange(index: number): void {
53. this.listeners.forEach(listener => {
54. listener.onDataChange(index);
55. // 写法2：listener.onDatasetChange([{type: DataOperationType.CHANGE, index: index}]);
56. })
57. }

59. // 通知LazyForEach组件需要在index对应索引处删除该子组件
60. notifyDataDelete(index: number): void {
61. this.listeners.forEach(listener => {
62. listener.onDataDelete(index);
63. // 写法2：listener.onDatasetChange([{type: DataOperationType.DELETE, index: index}]);
64. })
65. }

67. // 通知LazyForEach组件将from索引和to索引处的子组件进行交换
68. notifyDataMove(from: number, to: number): void {
69. this.listeners.forEach(listener => {
70. listener.onDataMove(from, to);
71. // 写法2：listener.onDatasetChange([{type: DataOperationType.EXCHANGE, index: {start: from, end: to}}]);
72. })
73. }

75. notifyDatasetChange(operations: DataOperation[]): void {
76. this.listeners.forEach(listener => {
77. listener.onDatasetChange(operations);
78. })
79. }
80. }

82. class MyDataSource extends BasicDataSource {
83. private dataArray: string[] = [];

85. public totalCount(): number {
86. return this.dataArray.length;
87. }

89. public getData(index: number): string {
90. return this.dataArray[index];
91. }

93. public addData(index: number, data: string): void {
94. this.dataArray.splice(index, 0, data);
95. this.notifyDataAdd(index);
96. }

98. public pushData(data: string): void {
99. this.dataArray.push(data);
100. this.notifyDataAdd(this.dataArray.length - 1);
101. }
102. }

104. class Params {
105. public data: MyDataSource | null = null;
106. public scroller: Scroller | null = null;

108. constructor(data: MyDataSource, scroller: Scroller) {
109. this.data = data;
110. this.scroller = scroller;
111. }
112. }

114. @Builder
115. function buildData(params: Params) {
116. List({ scroller: params.scroller }) {
117. LazyForEach(params.data, (item: string) => {
118. ListItem() {
119. Column() {
120. Text(item)
121. .fontSize(20)
122. .onAppear(() => {
123. hilog.info(0x0000, `TEST_TAG node appear: ${item}`, 'item');
124. })
125. .backgroundColor(Color.Pink)
126. .margin({
127. top: 30,
128. bottom: 30,
129. left: 10,
130. right: 10
131. })
132. }
133. }
134. .id(item)
135. }, (item: string) => item)
136. }
137. .cachedCount(5)
138. .listDirection(Axis.Horizontal)
139. }

141. class MyNodeController extends NodeController {
142. private rootNode: FrameNode | null = null;
143. private uiContext: UIContext | null = null;
144. private data: MyDataSource = new MyDataSource();
145. private scroller: Scroller = new Scroller();

147. makeNode(uiContext: UIContext): FrameNode | null {
148. this.uiContext = uiContext;
149. for (let i = 0; i <= 20; i++) {
150. this.data.pushData(`N${i}`);
151. }
152. const params: Params = new Params(this.data, this.scroller);
153. const dataNode: BuilderNode<[Params]> = new BuilderNode(uiContext);
154. dataNode.build(wrapBuilder<[Params]>(buildData), params);
155. this.rootNode = dataNode.getFrameNode();
156. const scrollToIndexOptions: ScrollToIndexOptions = {
157. extraOffset: {
158. value: 20, unit: LengthUnit.VP
159. }
160. };
161. this.scroller.scrollToIndex(6, true, ScrollAlign.START, scrollToIndexOptions);
162. return this.rootNode;
163. }

165. getFirstChildIndexWithoutExpand() {
166. hilog.info(0x0000,
167. `${TEST_TAG} getFirstChildIndexWithoutExpand: ${this.rootNode!.getFirstChildIndexWithoutExpand()}`,
168. 'getFirstChildIndexWithoutExpand');
169. }

171. getLastChildIndexWithoutExpand() {
172. hilog.info(0x0000,
173. `${TEST_TAG} getLastChildIndexWithoutExpand: ${this.rootNode!.getLastChildIndexWithoutExpand()}`,
174. 'getLastChildIndexWithoutExpand');
175. }

177. getChildWithNotExpand() {
178. const childNode = this.rootNode!.getChild(3, ExpandMode.NOT_EXPAND);
179. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND): ${childNode!.getId()}`, 'getId');
180. if (childNode!.getId() === 'N9') {
181. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND) result: success.`, 'success');
182. } else {
183. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.NOT_EXPAND)  result: fail.`, 'fail');
184. }
185. }

187. getChildWithExpand() {
188. const childNode = this.rootNode!.getChild(3, ExpandMode.EXPAND);
189. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.EXPAND): childNode!.getId()`, 'getId');
190. if (childNode!.getId() === 'N3') {
191. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.EXPAND)  result: success.`, 'success');
192. } else {
193. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.EXPAND)  result: fail.`, 'fail');
194. }
195. }

197. getChildWithLazyExpand() {
198. const childNode = this.rootNode!.getChild(3, ExpandMode.LAZY_EXPAND);
199. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND): childNode!.getId()`, 'getId');
200. if (childNode!.getId() === 'N3') {
201. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND) result: success.`, 'success');
202. } else {
203. hilog.info(0x0000, `${TEST_TAG} getChild(3, ExpandMode.LAZY_EXPAND)  result: fail.`, 'fail');
204. }
205. }
206. }

208. @Entry
209. @Component
210. struct Index {
211. private myNodeController: MyNodeController = new MyNodeController();
212. private scroller: Scroller = new Scroller();

214. build() {
215. Scroll(this.scroller) {
216. Column({ space: 8 }) {
217. Column() {
218. Text('This is a NodeContainer.')
219. .textAlign(TextAlign.Center)
220. .borderRadius(10)
221. .backgroundColor(0xFFFFFF)
222. .width('100%')
223. .fontSize(16)
224. NodeContainer(this.myNodeController)
225. .borderWidth(1)
226. .width(300)
227. .height(100)
228. }

230. Button('getFirstChildIndexWithoutExpand')
231. .width(300)
232. .onClick(() => {
233. this.myNodeController.getFirstChildIndexWithoutExpand();
234. })
235. Button('getLastChildIndexWithoutExpand')
236. .width(300)
237. .onClick(() => {
238. this.myNodeController.getLastChildIndexWithoutExpand();
239. })
240. Button('getChildWithNotExpand')
241. .width(300)
242. .onClick(() => {
243. this.myNodeController.getChildWithNotExpand();
244. })
245. Button('getChildWithExpand')
246. .width(300)
247. .onClick(() => {
248. this.myNodeController.getChildWithExpand();
249. })
250. Button('getChildWithLazyExpand')
251. .width(300)
252. .onClick(() => {
253. this.myNodeController.getChildWithLazyExpand();
254. })
255. }
256. .width('100%')
257. }
258. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
259. }
260. }
```

[FrameNodeLazyForEachSelect.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeLazyForEachSelect.ets#L16-L278)

## 调整自定义绘制Canvas的变换矩阵

从API version 12开始，通过重写FrameNode的[onDraw](../harmonyos-references/js-apis-arkui-framenode.md#ondraw12)方法，可以重写默认绘制方法。

通过[concatMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#concatmatrix12)可以调整自定义绘制画布的变换矩阵。

说明

* [getTotalMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#gettotalmatrix12)获取的是用来记录绘制指令的临时canvas的变换矩阵。
* 如果开发者希望对画布进行预期的变换，应使用[concatMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#concatmatrix12)而不是[setMatrix](../harmonyos-references/arkts-apis-graphics-drawing-canvas.md#setmatrix12)，因为setMatrix会覆盖原本真实canvas上存在的变换矩阵。

**ArkTS接口调用示例：**

```
1. import { NodeController, UIContext, DrawContext, FrameNode } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. function drawImage(canvas: DrawingCanvas) {
5. let matrix = new drawing.Matrix();
6. matrix.setTranslation(100, 100);
7. canvas.concatMatrix(matrix);
8. const pen = new drawing.Pen();
9. pen.setStrokeWidth(5);
10. pen.setColor({
11. alpha: 255,
12. red: 0,
13. green: 0,
14. blue: 255
15. });
16. canvas.attachPen(pen);
17. const brush = new drawing.Brush();
18. brush.setColor({
19. alpha: 255,
20. red: 0,
21. green: 0,
22. blue: 255
23. });
24. canvas.attachBrush(brush);
25. canvas.drawRect({
26. left: 10,
27. top: 10,
28. right: 110,
29. bottom: 60
30. });
31. canvas.detachPen();
32. }

34. function drawImage1(canvas: DrawingCanvas) {
35. let matrix = new drawing.Matrix();
36. matrix.setTranslation(100, 100);

38. // 1. getTotalMatrix获取的是用来记录绘制指令的临时canvas的变换矩阵
39. // 2. 如果开发者希望这个画布进行一个预期的变换，应该使用concatMatrix而不是setMatrix，因为setMatrix会覆盖原本真实canvas上存在的变换矩阵
40. canvas.getTotalMatrix();
41. canvas.setMatrix(matrix);
42. const pen = new drawing.Pen();
43. pen.setStrokeWidth(5);
44. pen.setColor({
45. alpha: 255,
46. red: 0,
47. green: 0,
48. blue: 255
49. });
50. canvas.attachPen(pen);
51. const brush = new drawing.Brush();
52. brush.setColor({
53. alpha: 255,
54. red: 0,
55. green: 0,
56. blue: 255
57. });
58. canvas.attachBrush(brush);
59. canvas.drawRect({
60. left: 10,
61. top: 10,
62. right: 110,
63. bottom: 60
64. });
65. canvas.detachPen();
66. }

68. class MyFrameNode extends FrameNode {
69. onDraw(context: DrawContext): void {
70. drawImage(context.canvas);
71. }
72. }

74. class MyFrameNode1 extends FrameNode {
75. onDraw(context: DrawContext): void {
76. drawImage1(context.canvas);
77. }
78. }

80. class MyNodeController extends NodeController {
81. makeNode(uiContext: UIContext): FrameNode | null {
82. const rootNode: FrameNode = new FrameNode(uiContext);
83. rootNode.commonAttribute.width(300).height(300);
84. const theFrameNode: MyFrameNode = new MyFrameNode(uiContext)
85. theFrameNode.commonAttribute.width(100)
86. .height(50)
87. .position({ x: 10, y: 20 })
88. .backgroundColor(0xFF2787D9);
89. rootNode.appendChild(theFrameNode);
90. return rootNode;
91. }
92. }

94. class MyNodeController1 extends NodeController {
95. makeNode(uiContext: UIContext): FrameNode | null {
96. const rootNode: FrameNode = new FrameNode(uiContext);
97. rootNode.commonAttribute.width(300).height(300);
98. const theFrameNode: MyFrameNode1 = new MyFrameNode1(uiContext);
99. theFrameNode.commonAttribute.width(100)
100. .height(50)
101. .position({ x: 10, y: 20 })
102. .backgroundColor(0xFF2787D9);
103. rootNode.appendChild(theFrameNode);
104. return rootNode;
105. }
106. }

108. @Entry
109. @Component
110. struct Index {
111. myNodeController: MyNodeController = new MyNodeController();
112. myNodeController1: MyNodeController = new MyNodeController1();

114. build() {
115. Row() {
116. Column() {
117. NodeContainer(this.myNodeController);
118. }
119. .height('100%')
120. .width('45%')

122. Column() {
123. NodeContainer(this.myNodeController1);
124. }
125. .height('100%')
126. .width('45%')
127. }.height('100%')
128. .width('100%')

130. }
131. }
```

[FrameNodeCanvas.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/FrameNode/entry/src/main/ets/pages/framenode/FrameNodeCanvas.ets#L16-L148)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/EnptaQx4SFW5g-6PRq8_WA/zh-cn_image_0000002583438053.png?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=45EABC212DEC8DFBDECBFDD25B774C595CA748D48BAC5C59ACB3E1C55AA6DB87)

## 更新当前帧节点

从API version 21开始，通过使用frameNode的[invalidateAttributes](../harmonyos-references/js-apis-arkui-framenode.md#invalidateattributes21)方法，可以在当前帧触发节点更新，避免组件切换过程中出现闪烁。

```
1. import { FrameNode, NodeController, typeNode, NodeContent } from '@kit.ArkUI';

3. // 继承NodeController实现自定义NodeAdapter控制器
4. class MyNodeAdapterController extends NodeController {
5. rootNode: FrameNode | null = null;
6. imageUrl: string = "";

8. constructor(imageUrl: string) {
9. super();
10. this.imageUrl = imageUrl;
11. }

13. makeNode(uiContext: UIContext): FrameNode | null {
14. let imageNode = typeNode.createNode(uiContext, "Image");
15. imageNode.initialize($r(this.imageUrl))
16. imageNode.commonAttribute.margin({ left: 100 })
17. imageNode.attribute.syncLoad(true).width(100).height(100);
18. // 强制当前帧内即时节点更新，避免出现切换闪烁
19. imageNode.invalidateAttributes();
20. return imageNode;
21. }
22. }

24. // 自定义挂载事件的自定义组件，挂载前加载样例图片
25. @Component
26. struct NodeComponent3 {
27. private rootSlot: NodeContent = new NodeContent();

29. aboutToAppear(): void {
30. const uiContext = this.getUIContext();
31. let imageNode = typeNode.createNode(uiContext, "Image");
32. imageNode.initialize($r('app.media.startIcon'))
33. imageNode.attribute.syncLoad(true).width(100).height(100);
34. imageNode.invalidateAttributes();
35. this.rootSlot.addFrameNode(imageNode);
36. }

38. build() {
39. ContentSlot(this.rootSlot)
40. }
41. }

43. // 自定义挂载事件的自定义组件，挂载前加载样例图片
44. @Component
45. struct NodeComponent4 {
46. private rootSlot: NodeContent = new NodeContent();

48. aboutToAppear(): void {
49. const uiContext = this.getUIContext();
50. let imageNode = typeNode.createNode(uiContext, "Image");
51. imageNode.initialize($r('app.media.startIcon'))
52. imageNode.attribute.syncLoad(true).width(100).height(100);
53. imageNode.invalidateAttributes();
54. this.rootSlot.addFrameNode(imageNode);
55. }

57. build() {
58. ContentSlot(this.rootSlot)
59. }
60. }

62. @Entry
63. @Component
64. struct ListNodeTest {
65. @State flag: boolean = true;
66. adapterController: MyNodeAdapterController = new MyNodeAdapterController('app.media.startIcon');

68. build() {
69. Column() {
70. Text("NodeComponent")
71. if (this.flag) {
72. NodeComponent3()
73. } else {
74. NodeComponent4()
75. }
76. Text("NodeContainer").margin({ top: 20 })
77. if (this.flag) {
78. NodeContainer(this.adapterController)
79. .width(300).height(100)
80. } else {
81. NodeContainer(this.adapterController)
82. .width(300).height(100)
83. }
84. // 点击后图片正常切换不闪烁
85. Button('change').onClick(() => {
86. this.flag = !this.flag;
87. }).margin({ top: 20 })
88. }
89. .width("100%")
90. }
91. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/TG3eeDuIRJyq7xp64_cMQQ/zh-cn_image_0000002552958008.png?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=55FC7115960BC0F3F2931F5747A7FE3436F7BF1AC2C5167278A9C718AB2BBA85)

## 判断节点是否处于渲染状态

从API version 23开始，通过使用FrameNode的[isInRenderState](../harmonyos-references/js-apis-arkui-framenode.md#isinrenderstate23)方法，判断FrameNode节点是否处于渲染状态。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. @Entry
4. @Component
5. struct Index {
6. @State message: string = 'is on render tree';
7. @State @Watch('change') isShow: boolean = true;
8. data: Array<string> = ['hello1', 'hello2', 'hello3', 'hello4', 'hello5', 'hello6', 'hello7', 'hello8'];

10. // 监听状态变化后打印是否处于渲染状态
11. change() {
12. let buttonNode = this.getUIContext().getFrameNodeById("testButton");
13. if (buttonNode == null) {
14. return;
15. }
16. let isOnRenderTree = buttonNode!.isInRenderState();
17. if (isOnRenderTree) {
18. hilog.info(1, 'frameNode', 'is on render tree');
19. } else {
20. hilog.info(1, 'frameNode', 'is not no render tree');
21. }
22. }

24. build() {
25. Column() {
26. Button('change button visibility').onClick(() => {
27. // 修改button的visibility状态
28. this.isShow = !this.isShow;
29. })
30. .margin({ top: 20 })
31. Button('test button')
32. .visibility(this.isShow ? Visibility.Visible : Visibility.Hidden)
33. .margin(20).id('testButton')

35. List() {
36. ForEach(this.data, (item: string, index: number) => {
37. ListItem() {
38. Text(item).id(item)
39. }.alignSelf(ItemAlign.Center).width('100%')
40. })
41. }
42. .width('30%')
43. .alignSelf(ItemAlign.Center)
44. .height("10%")
45. .onReachEnd(() => {
46. let textNode8 = this.getUIContext().getFrameNodeById("hello8");
47. if (textNode8 != null) {
48. let isOnRenderTree = textNode8!.isInRenderState();
49. hilog.info(1, 'frameNode', 'is hello8 on RenderTree: %{public}s', isOnRenderTree);
50. }
51. let textNode1 = this.getUIContext().getFrameNodeById("hello1");
52. if (textNode1 != null) {
53. let isOnRenderTree = textNode1!.isInRenderState();
54. isOnRenderTree ? this.message = 'is on render tree' : 'is not no render tree'
55. hilog.info(1, 'frameNode', 'is hello1 on RenderTree: %{public}s', isOnRenderTree);
56. }
57. })
58. }
59. .height('100%')
60. .width('100%')
61. }
62. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/XvBpYB68TliYEkcKBlJ88A/zh-cn_image_0000002583478009.png?HW-CC-KV=V1&HW-CC-Date=20260427T234001Z&HW-CC-Expire=86400&HW-CC-Sign=CD386B6CAA3A484AFE83417B7882ED592EE6773D85F6CAF7B5D9AB371F577E94)
