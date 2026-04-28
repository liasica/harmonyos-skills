---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-node-faq
title: 自定义节点常见问题
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发调试调优 > UI开发常见问题 > 自定义节点常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:b9b1ea8e3c35d23fb2b677fe6023ccce2b90c73a151f8758b6085d02e0d9a7cc
---

本文档介绍自定义节点的常见问题并提供参考。

## 自定义组件的aboutToDisappear回调异常

**问题现象**

从API version 12开始，自定义节点的子节点在页面退出后未立即回调自定义组件的[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)方法。自定义组件的aboutToDisappear通常在其销毁的时候触发，页面销毁后未立即回调则说明该自定义组件在页面销毁后未立即销毁。

**可能原因**

* 自定义组件存在父节点且父节点未销毁。
* 自定义组件由[BuilderNode](arkts-user-defined-arktsnode-buildernode.md)创建，该前端对象既未被回收，也未解除对后端自定义组件的引用。BuilderNode创建时，默认持有后端节点的强引用。
* 通过调用[OH\_ArkUI\_GetNodeHandleFromNapiValue](../harmonyos-references/capi-native-node-napi-h.md#oh_arkui_getnodehandlefromnapivalue)方法，可以获取BuilderNode或ComponentContent对象中的root节点，此操作会使后端节点的引用计数加一。
* 在[NodeContent](../harmonyos-references/js-apis-arkui-nodecontent.md)中，通过[addFrameNode](../harmonyos-references/js-apis-arkui-nodecontent.md#addframenode12)方法增加了对被添加的FrameNode对象节点的引用关系。然而，该NodeContent对象未被回收，且未通过[removeFrameNode](../harmonyos-references/js-apis-arkui-nodecontent.md#removeframenode12)接口删除所增加的引用关系。

**解决措施**

* 将需要释放的自定义组件从父节点上移除，排除父节点对自定义组件生命周期的影响。
* 自定义组件由[BuilderNode](arkts-user-defined-arktsnode-buildernode.md)创建时，调用[dispose](../harmonyos-references/js-apis-arkui-buildernode.md#dispose12)接口，立即释放前端BuilderNode对象对于后端节点的强引用。
* 对于使用OH\_ArkUI\_GetNodeHandleFromNapiValue获取BuilderNode或ComponentContent对象的root节点，调用[disposeNode](../harmonyos-references/capi-arkui-nativemodule-arkui-nativenodeapi-1.md#disposenode)减少OH\_ArkUI\_GetNodeHandleFromNapiValue增加的引用计数。
* 未调用dispose时，当前端的BuilderNode对象在[GC](gc-introduction.md)中被回收会释放对后端根节点的引用。调试阶段可使用[hidumper](hidumper.md)指令触发GC或[查询堆内存](hidumper.md#查询虚拟机堆内存)来分析引用关系。

**示例代码**

下文中，根节点表示BuilderNode的根节点，aboutToDisappear表示BuilderNode中构建的自定义组件（即BuilderNodePage）中的回调。

* 跳转至pageOneTmp页面后返回，通过指令触发GC，继续操作设备后可以看到aboutToDisappear回调。根节点相关的引用关系和解决方案：

  + NodeContent对根节点的引用关系：需要触发NodeContent对象的回收，或主动调用removeFrameNode接口。
  + 全局对象对BuilderNode的引用关系：通过[ArrayList](../harmonyos-references/js-apis-arraylist.md)的[clear](../harmonyos-references/js-apis-arraylist.md#clear)方法清除对BuilderNode的引用。
  + BuilderNode对象对根节点的引用关系：确保BuilderNode对象无其他引用关系，触发该对象的回收可以解除其对根节点的引用。
* 跳转至pageTwoTmp页面后返回，可以直接看到aboutToDisappear回调。根节点相关的引用关系以及解决方案：

  + NodeContent对根节点的引用关系：通过NodeContent的removeFrameNode接口解除引用关系。
  + BuilderNode对象对根节点的引用关系：通过BuilderNode的dispose接口直接解除引用关系。
* 跳转至pageThreeTmp页面后返回，可以直接看到aboutToDisappear回调。根节点相关的引用关系以及解决方案：

  + 根节点的父节点对其的引用关系：由于父节点为FrameNode对象对应的节点，可以直接通过FrameNode的removeChild方法解除引用关系。
  + BuilderNode对象对根节点的引用关系：通过BuilderNode的dispose接口直接解除引用关系。

```
1. import { BuilderNode, FrameNode, NodeContent } from '@kit.ArkUI';
2. import { ArrayList } from '@kit.ArkTS';

4. const CUSTOM_COMPONENT_CONT: string = "CustomComponentCont"
5. AppStorage.setOrCreate<number>(CUSTOM_COMPONENT_CONT, 0);
6. let globalBuilderNodeList: ArrayList<BuilderNode<[]>> = new ArrayList<BuilderNode<[]>>();

8. @Component
9. struct BuilderNodePage {
10. aboutToAppear(): void {
11. const count: number | undefined = AppStorage.get<number>(CUSTOM_COMPONENT_CONT);
12. const current: number = count ? count + 1 : 1;
13. AppStorage.setOrCreate<number>(CUSTOM_COMPONENT_CONT, current);
14. console.info("BuilderNodePage", "aboutToAppear " + AppStorage.get<number>(CUSTOM_COMPONENT_CONT))
15. }

17. aboutToDisappear(): void {
18. setTimeout(() => {
19. const count: number | undefined = AppStorage.get<number>(CUSTOM_COMPONENT_CONT);
20. console.info("BuilderNodePage", "aboutToDisappear " + count)
21. const current: number = count ? count - 1 : -1;
22. AppStorage.set<number>(CUSTOM_COMPONENT_CONT, current)
23. console.info("BuilderNodePage", "aboutToDisappear " + AppStorage.get<number>(CUSTOM_COMPONENT_CONT))
24. }, 1)
25. }

27. build() {
28. Text("This is a BuilderNode")
29. }
30. }

32. @Builder
33. function BuilderNodeBuilder() {
34. BuilderNodePage();
35. }

37. @Entry
38. @Component
39. struct NavigationExample {
40. @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack()
41. private arr: number[] = [1, 2, 3];
42. @StorageProp(CUSTOM_COMPONENT_CONT) customComponentCount: number | undefined =
43. AppStorage.get<number>(CUSTOM_COMPONENT_CONT);

45. @Builder
46. pageMap(name: string) {
47. if (name === "NavDestinationTitle1") {
48. pageOneTmp();
49. } else if (name === "NavDestinationTitle2") {
50. pageTwoTmp();
51. } else if (name === "NavDestinationTitle3") {
52. pageThreeTmp();
53. }
54. }

56. onPageShow(): void {
57. console.info("NavigationExample " + this.customComponentCount);
58. }

60. build() {
61. Column() {
62. Navigation(this.pageInfos) {
63. Text("BuilderNode中自定义组件的遗留数量 " + this.customComponentCount)
64. .width("90%")
65. .height(40)
66. .backgroundColor('#FFFFFF')
67. Button("移除全局引用")
68. .onClick(() => {
69. // 清除所有全局引用。
70. // 可以使用hidumper指令触发GC验证引用关系是否清零。
71. globalBuilderNodeList.clear();
72. })
73. List({ space: 12 }) {
74. ForEach(this.arr, (item: number) => {
75. ListItem() {
76. Text("Page" + item)
77. .width("100%")
78. .height(72)
79. .backgroundColor('#FFFFFF')
80. .borderRadius(24)
81. .fontSize(16)
82. .fontWeight(500)
83. .textAlign(TextAlign.Center)
84. .onClick(() => {
85. this.pageInfos.pushPath({ name: "NavDestinationTitle" + item });
86. })
87. }
88. }, (item: number) => item.toString())
89. }
90. .width("100%")
91. .margin({ top: 12 })
92. }
93. .title("主标题")
94. .mode(NavigationMode.Stack)
95. .navDestination(this.pageMap)
96. }
97. .height('100%')
98. .width('100%')
99. .backgroundColor('#F1F3F5')
100. }
101. }

103. @Component
104. export struct pageOneTmp {
105. @Consume('pageInfos') pageInfos: NavPathStack;
106. private builderNode: BuilderNode<[]> = new BuilderNode(this.getUIContext());
107. private content: NodeContent = new NodeContent();

109. aboutToAppear(): void {
110. console.info("pageOneTmp", "aboutToAppear")
111. this.builderNode.build(wrapBuilder(BuilderNodeBuilder));
112. if (this.builderNode.getFrameNode()) {
113. this.content.addFrameNode(this.builderNode.getFrameNode());
114. }
115. // 添加全局引用，该对象在全局引用移除前无法被GC。
116. globalBuilderNodeList.add(this.builderNode);
117. }

119. aboutToDisappear(): void {
120. console.info("pageOneTmp", "aboutToDisappear")
121. }

123. build() {
124. NavDestination() {
125. Column() {
126. Text("pageOneTmp")
127. ContentSlot(this.content)
128. }.width('100%').height('100%')
129. }.title("NavDestinationTitle1")
130. .onBackPressed(() => {
131. const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素。
132. console.info('pop' + '返回值' + JSON.stringify(popDestinationInfo));
133. return true;
134. })
135. }
136. }

138. @Component
139. export struct pageTwoTmp {
140. @Consume('pageInfos') pageInfos: NavPathStack;
141. private builderNode: BuilderNode<[]> = new BuilderNode(this.getUIContext());
142. private content: NodeContent = new NodeContent();

144. aboutToAppear(): void {
145. console.info("pageTwoTmp", "aboutToAppear")
146. this.builderNode!.build(wrapBuilder(BuilderNodeBuilder));
147. if (this.builderNode!.getFrameNode()) {
148. // 将BuilderNode的根节点挂载至NodeContent对象中。
149. // 如果要触发builderNode的根节点的析构，需要主动从NodeContent对象中移除该节点，或者等待NodeContent对象被GC。
150. // 否则，BuilderNode的根节点无法触发析构。
151. this.content.addFrameNode(this.builderNode!.getFrameNode());
152. }
153. }

155. aboutToDisappear(): void {
156. console.info("pageTwoTmp", "aboutToDisappear")
157. if (this.builderNode?.getFrameNode()) {
158. // 将BuilderNode的根节点从NodeContent对象中移除。
159. // 需要在BuilderNode的dispose操作之前执行，否则无法获得该BuilderNode的根节点。
160. this.content.removeFrameNode(this.builderNode?.getFrameNode());
161. }
162. this.builderNode?.dispose();
163. }

165. build() {
166. NavDestination() {
167. Column() {
168. Text("pageTwoTmp")
169. ContentSlot(this.content)
170. }.width('100%').height('100%')
171. }.title("NavDestinationTitle2")
172. .onBackPressed(() => {
173. const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素。
174. console.info('pop' + '返回值' + JSON.stringify(popDestinationInfo));
175. return true;
176. })
177. }
178. }

180. @Component
181. export struct pageThreeTmp {
182. @Consume('pageInfos') pageInfos: NavPathStack;
183. private builderNode: BuilderNode<[]> = new BuilderNode(this.getUIContext());
184. private content: NodeContent = new NodeContent();
185. private rootNode: FrameNode = new FrameNode(this.getUIContext());

187. aboutToAppear(): void {
188. console.info("pageThreeTmp", "aboutToAppear")
189. this.builderNode!.build(wrapBuilder(BuilderNodeBuilder));
190. if (this.builderNode!.getFrameNode()) {
191. this.content.addFrameNode(this.rootNode);
192. // BuilderNode的根节点被挂载至FrameNode对象对应的节点中。
193. // BuilderNode的根节点如果要触发析构需要从主动从FrameNode对象对应的节点中移除，或者等待FrameNode对象对应的节点析构。
194. // 否则，BuilderNode的根节点无法触发析构。
195. this.rootNode.appendChild(this.builderNode.getFrameNode());
196. }
197. }

199. aboutToDisappear(): void {
200. console.info("pageThreeTmp", "aboutToDisappear")
201. if (this.builderNode?.getFrameNode()) {
202. // 将BuilderNode的根节点从FrameNode对象对应的节点中移除。
203. // 需要在BuilderNode的dispose操作以及FrameNode对象dispose之前执行，否则无法获得他们对应的节点。
204. this.rootNode.removeChild(this.builderNode?.getFrameNode());
205. }
206. this.builderNode?.dispose();
207. }

209. build() {
210. NavDestination() {
211. Column() {
212. Text("pageThreeTmp")
213. ContentSlot(this.content)
214. }.width('100%').height('100%')
215. }.title("NavDestinationTitle3")
216. .onBackPressed(() => {
217. const popDestinationInfo = this.pageInfos.pop(); // 弹出路由栈栈顶元素。
218. console.info('pop' + '返回值' + JSON.stringify(popDestinationInfo));
219. return true;
220. })
221. }
222. }
```

## BuilderNode前后端循环引用导致的内存泄漏问题

**问题现象**

使用[BuilderNode](arkts-user-defined-arktsnode-buildernode.md)创建自定义组件节点时，有可能出现前后端（ArkTS UI层与Native UI引擎层）之间的循环引用，使得自定义节点无法被销毁，进而引发内存泄漏。

**可能原因**

* 使用[BuilderNode](arkts-user-defined-arktsnode-buildernode.md)创建自定义节点，创建的前端BuilderNode对象默认持有后端节点的强引用，而后端节点可能通过某些路径（如事件回调、全局缓存）反过来引用前端BuilderNode对象，因此形成了前后端循环引用，前端对象无法被回收，后端节点也因为被前端对象持有强引用而无法释放，导致内存泄漏。
* BuilderNode会持有[build](../harmonyos-references/js-apis-arkui-buildernode.md#build)函数传递的参数对象，如果传递给BuilderNode的参数对象也引用了BuilderNode对象，会产生前端对象的循环引用。

**解决措施**

* 步骤一：如果传递给BuilderNode的参数持有了BuilderNode对象，当不再需要一个BuilderNode节点时，使用[update](../harmonyos-references/js-apis-arkui-buildernode.md#update)接口更新参数，解除参数对象对BuilderNode的引用。
* 步骤二：当不再需要一个BuilderNode节点时，将此BuilderNode节点从组件树上移除，并调用[dispose](../harmonyos-references/js-apis-arkui-buildernode.md#dispose12)接口，立即释放前端BuilderNode对象对于后端节点的强引用，解除前后端的引用关系。

**示例代码**

如下示例中，将BuilderNode前端对象作为参数传递给了自定义组件，构造了前后端循环引用的场景。

下文中，[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)表示BuilderNode中构建的自定义组件（即TestComponent）析构时的回调。

* 不调用dispose接口的情况（点击示例中的"Destroy"按钮），由于前后端循环引用，导致自定义组件无法析构，体现为[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)回调未触发。
* 调用dispose接口的情况（点击示例中的"Destroy with dispose"按钮），[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)回调能够触发。

```
1. import { FrameNode, NodeController, BuilderNode } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. // 定义传递参数的接口
5. interface ParamsInterface {
6. builderRootNode: BuilderNode<[ParamsInterface]> | null;
7. }

9. // 自定义组件
10. @Component
11. struct TestComponent {
12. builderRootNode: BuilderNode<[ParamsInterface]> | null = null;
13. build() {
14. Column() {
15. Text('This is a BuilderNode.')
16. .fontSize(16)
17. .fontWeight(FontWeight.Bold)
18. }
19. .width('100%')
20. .backgroundColor(Color.Gray)
21. }

23. // 自定义组件实例创建时的回调
24. aboutToAppear() {
25. hilog.info(0x0000, 'testTag', 'aboutToAppear');
26. }

28. // 自定义组件实例析构时的回调
29. aboutToDisappear() {
30. hilog.info(0x0000, 'testTag', 'aboutToDisappear');
31. }
32. }

34. @Builder
35. function buildComponent(params: ParamsInterface) {
36. TestComponent(params)
37. }

39. // 继承NodeController实现自定义UI控制器
40. class MyNodeController extends NodeController {
41. private builderNode: BuilderNode<[ParamsInterface]> | null = null;

43. makeNode(uiContext: UIContext): FrameNode | null {
44. this.builderNode = new BuilderNode(uiContext);

46. // 将builderNode自身作为参数传递给自定义组件，产生前后端循环引用场景
47. this.builderNode.build(new WrappedBuilder(buildComponent), {builderRootNode: this.builderNode});

49. return this.builderNode.getFrameNode();
50. }

52. // 解除当前builderNode与后端实体的引用关系，并置空为null
53. dispose() {
54. if (this.builderNode !== null) {
55. this.builderNode.dispose();
56. this.builderNode = null;
57. }
58. }

60. // 清理builderNode对象持有的参数，解除参数对象对builderNode对象的引用
61. clearParams() {
62. this.builderNode?.update({builderRootNode: null} as ParamsInterface)
63. }
64. }

66. @Entry
67. @Component
68. struct Index {
69. @State myNodeController: MyNodeController | undefined = new MyNodeController();
70. build() {
71. Column({ space: 4 }) {
72. NodeContainer(this.myNodeController)
73. Button('Destroy')
74. .onClick(() => {
75. this.myNodeController?.clearParams();
76. // 通过将传入NodeContainer的NodeController置为undefined，使BuilderNode节点下树
77. this.myNodeController = undefined;
78. })
79. .width('100%')
80. Button('Destroy with dispose')
81. .onClick(() => {
82. this.myNodeController?.clearParams();
83. this.myNodeController?.dispose();
84. this.myNodeController = undefined;
85. })
86. .width('100%')
87. Button('Create')
88. .onClick(() => {
89. if (this.myNodeController === undefined) {
90. this.myNodeController = new MyNodeController();
91. }
92. })
93. .width('100%')
94. }
95. }
96. }
```
