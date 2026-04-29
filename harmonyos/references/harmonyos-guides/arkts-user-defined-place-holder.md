---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-place-holder
title: 自定义占位节点
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 自定义占位节点
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:156bc409873eb93c0537e1d00f785e555f6eb3f8ca4b74cfd5c89ea5f45c82af
---

ArkUI提供了系统组件[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)和[ContentSlot](../harmonyos-references/ts-components-contentslot.md)作为自定义节点的占位节点。主要用于自定义节点以及自定义节点树的显示。

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)作为容器节点存在，具备通用属性，是UI节点。[ContentSlot](arkts-rendering-control-contentslot.md)只是一个语法节点，无通用属性，不参与布局和渲染。支持混合模式开发，当容器是ArkTS组件，子组件在Native侧创建时，推荐使用ContentSlot占位组件。具体使用参考[ContentSlot](../harmonyos-references/ts-components-contentslot.md)的接口文档说明。

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)是用来占位的系统组件，主要用于自定义节点以及自定义节点树的显示，支持组件的通用属性，对通用属性的处理请参考默认左上角对齐的[Stack](../harmonyos-references/ts-container-stack.md)组件。

[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)提供了一系列生命周期回调，通过[makeNode](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)回调返回一个[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点树的根节点。将[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点树挂载到对应的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)下。同时提供了[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)、[aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)、[aboutToResize](../harmonyos-references/js-apis-arkui-nodecontroller.md#abouttoresize)、[onTouchEvent](../harmonyos-references/js-apis-arkui-nodecontroller.md#ontouchevent)、[rebuild](../harmonyos-references/js-apis-arkui-nodecontroller.md#rebuild)五个回调方法用于监听对应的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)的状态。

每个生命周期的回调的具体含义参考[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)的接口文档说明。

说明

* NodeContainer下仅支持挂载自定义的FrameNode节点以及BuilderNode创建的组件树的根节点。
* 从API Version 12开始支持的接口，可以通过FrameNode的查询接口返回系统组件的代理节点，代理节点可以作为makeNode的返回值进行返回，但代理节点无法成功挂载在组件树上，最终的显示结果为代理节点挂载失败。
* 需要保证一个节点只能作为一个父节点的子节点去使用，否则可能存在显示异常或者功能异常，尤其是页面路由场景或者动效场景。例如，如果通过NodeController将同一个节点挂载在多个NodeContainer上，仅一个占位容器下会显示节点，且多个NodeContainer的可见性、透明度等影响子组件状态的属性更新均会影响被挂载的子节点。

## 基本概念

* 自定义节点：使用ArkUI提供的接口，以命令式创建的节点。包括自定义组件节点（FrameNode）、自定义渲染节点（RenderNode）、自定义声明式节点（BuilderNode）、[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)等。
* 自定义节点树：根节点为自定义节点的节点树。
* 声明式节点树：根节点为声明式节点的节点树。
* 节点树：一种常见的数据结构，用于表示节点的层级关系。
* 占位节点：用于在声明式节点树上为自定义节点树预留位置的节点，主要包括NodeContainer和ContentSlot。鉴于页面的主树采用声明式节点树，因此，唯有借助占位节点，才能将命令式构建的自定义节点成功挂载至声明式节点树上。

## 使用NodeContainer挂载自定义节点

通过NodeController在NodeContainer下挂载自定义节点。

```
1. // common.ets
2. import { BuilderNode, UIContext } from '@kit.ArkUI';

4. class Params {
5. public text: string = 'this is a text';
6. }

8. let buttonNode: BuilderNode<[Params]> | null = null;

10. @Builder
11. function buttonBuilder(params: Params) {
12. Column() {
13. Button(params.text)
14. .fontSize(12)
15. .borderRadius(8)
16. .borderWidth(2)
17. .backgroundColor(Color.Orange)
18. }
19. }

21. export function createNode(uiContext: UIContext) {
22. buttonNode = new BuilderNode<[Params]>(uiContext);
23. buttonNode.build(wrapBuilder(buttonBuilder), { text: 'This is a Button' });
24. return buttonNode;
25. }

27. export function getOrCreateNode(uiContext: UIContext): BuilderNode<[Params]> | null {
28. if (buttonNode?.getFrameNode() && buttonNode?.getFrameNode()?.getUniqueId() != -1) {
29. return buttonNode;
30. } else {
31. return createNode(uiContext);
32. }
33. }
```

[Common.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkTSUserPlaceHolder/entry/src/main/ets/pages/Common.ets#L15-L49)

```
1. // Index.ets
2. import { FrameNode, NodeController, Size, UIContext } from '@kit.ArkUI';
3. import { getOrCreateNode } from './Common';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. const DOMAIN = 0xF811
7. const TAG = '[Sample_ArkTSUserPlaceHolder]';

9. class MyNodeController extends NodeController {
10. private isShow: boolean = false;

12. constructor(isShow: boolean) {
13. super();
14. this.isShow = isShow;
15. }

17. makeNode(uiContext: UIContext): FrameNode | null {
18. if (!this.isShow) {
19. return null;
20. }
21. let frameNode = getOrCreateNode(uiContext)?.getFrameNode();
22. return frameNode ? frameNode : null;
23. }

25. aboutToResize(size: Size) {
26. hilog.info(DOMAIN, TAG,' aboutToResize width : ' + size.width + ' height : ' + size.height);
27. }

29. aboutToAppear() {
30. hilog.info(DOMAIN, TAG,' aboutToAppear');
31. }

33. aboutToDisappear() {
34. hilog.info(DOMAIN, TAG,' aboutToDisappear');
35. }

37. onTouchEvent(event: TouchEvent) {
38. hilog.info(DOMAIN, TAG,' onTouchEvent');
39. }

41. toShow() {
42. this.isShow = true;
43. this.rebuild();
44. }

46. toHide() {
47. this.isShow = false;
48. this.rebuild();
49. }
50. }

52. @Entry
53. @Component
54. struct Index {
55. private myNodeController1: MyNodeController = new MyNodeController(true);
56. private myNodeController2: MyNodeController = new MyNodeController(false);

58. build() {
59. Column() {
60. NodeContainer(this.myNodeController1)
61. .width('100%')
62. .height('40%')
63. .backgroundColor(Color.Brown)
64. NodeContainer(this.myNodeController2)
65. .width('100%')
66. .height('40%')
67. .backgroundColor(Color.Gray)
68. Button('Change the place of button')
69. .onClick(() => {
70. // 先在原始占位节点中下树
71. // 后在新的占位节点中上树
72. // 保证自定义节点仅作为一个节点的子节点存在
73. this.myNodeController1.toHide();
74. this.myNodeController2.toShow();
75. })
76. }
77. .padding({ left: 35, right: 35, top: 35 })
78. .width('100%')
79. .height('100%')
80. }
81. }
```

[CustomNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkTSUserPlaceHolder/entry/src/main/ets/pages/CustomNode.ets#L15-L97)

## NodeContainer和ContentSlot添加子节点布局差异

[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)是一个容器节点，布局参考左上角对齐的[Stack](../harmonyos-references/ts-container-stack.md)组件，不会按照父容器的布局规则进行布局。[ContentSlot](../harmonyos-references/ts-components-contentslot.md)只是一个语法节点，不参与布局，添加的子节点会按照父容器的布局规则进行布局。

```
1. import { FrameNode, NodeContent, NodeController, typeNode, UIContext } from '@kit.ArkUI';

3. class NodeContentCtrl {
4. public content: NodeContent
5. public textNode: Array<typeNode.Text> = [];
6. public uiContext: UIContext
7. public width: number

9. constructor(uiContext: UIContext) {
10. this.content = new NodeContent();
11. this.uiContext = uiContext;
12. this.width = Infinity;
13. }

15. AddNode() {
16. let node = typeNode.createNode(this.uiContext, 'Text');
17. node.initialize('ContentText:' + this.textNode.length).fontSize(20);
18. this.textNode.push(node);
19. this.content.addFrameNode(node);
20. }

22. RemoveNode() {
23. let node = this.textNode.pop();
24. this.content.removeFrameNode(node);
25. }

27. RemoveFront() {
28. let node = this.textNode.shift();
29. this.content.removeFrameNode(node);
30. }

32. GetContent(): NodeContent {
33. return this.content;
34. }
35. }

37. class MyNodeController extends NodeController {
38. public rootNode: FrameNode | null = null;
39. public textNode: Array<typeNode.Text> = [];

41. makeNode(uiContext: UIContext): FrameNode {
42. this.rootNode = new FrameNode(uiContext);
43. return this.rootNode;
44. }

46. AddNode(frameNode: FrameNode | null, uiContext: UIContext) {
47. let node = typeNode.createNode(uiContext, 'Text');
48. node.initialize('ControllerText:' + this.textNode.length).fontSize(20);
49. this.textNode.push(node);
50. frameNode?.appendChild(node);
51. }

53. RemoveNode(frameNode: FrameNode | null) {
54. let node = this.textNode.pop();
55. frameNode?.removeChild(node);
56. }

58. RemoveFront(frameNode: FrameNode | null) {
59. let node = this.textNode.shift();
60. frameNode?.removeChild(node);
61. }
62. }

64. @Entry
65. @Component
66. struct Index {
67. @State message: string = 'Hello World';
68. controller = new NodeContentCtrl(this.getUIContext());
69. myNodeController = new MyNodeController();

71. build() {
72. Row() {
73. Column() {
74. ContentSlot(this.controller.GetContent())
75. Button('AddToSlot')
76. .onClick(() => {
77. this.controller.AddNode();
78. })
79. .margin(10)
80. Button('RemoveBack')
81. .onClick(() => {
82. this.controller.RemoveNode();
83. })
84. .margin(10)
85. Button('RemoveFront')
86. .onClick(() => {
87. this.controller.RemoveFront();
88. })
89. .margin(10)
90. }
91. .width('50%')

93. Column() {
94. NodeContainer(this.myNodeController)
95. Button('AddToNodeContainer')
96. .onClick(() => {
97. this.myNodeController.AddNode(this.myNodeController.rootNode, this.getUIContext());
98. })
99. .margin(10)
100. Button('RemoveBack')
101. .onClick(() => {
102. this.myNodeController.RemoveNode(this.myNodeController.rootNode);
103. })
104. .margin(10)
105. Button('RemoveFront')
106. .onClick(() => {
107. this.myNodeController.RemoveFront(this.myNodeController.rootNode);
108. })
109. .margin(10)
110. }
111. .width('50%')
112. }
113. .height('100%')
114. }
115. }
```

[LayoutDiff.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ArkTSUserPlaceHolder/entry/src/main/ets/pages/LayoutDiff.ets#L15-L131)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/4cdcbZ8qSBGq4OGiwYPL1A/zh-cn_image_0000002558764496.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=02A6D1A8AF86A1C19317BB66EBA8DDD699DF99BD781950E969A95007F98AC66E)
