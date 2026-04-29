---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-migrate
title: Web组件在不同的窗口间迁移
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 管理网页加载与浏览记录 > Web组件在不同的窗口间迁移
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b62d0741fbd4cbcf4f14c63ad4d47ebf8b196f4d3c3f4001acbbcccef1111f4c
---

Web组件能够实现在不同窗口的组件树上进行挂载或移除操作，这一能力使得开发者可以将同一个Web组件在不同窗口间迁移。例如，将浏览器的Tab页拖出成独立窗口，或拖入浏览器的另一个窗口。

Web组件在不同窗口间迁移，是基于[自定义节点](arkts-user-defined-node.md)能力实现的。实现的基本原理是：通过[BuilderNode](arkts-user-defined-arktsnode-buildernode.md)，开发者可创建Web组件的离线节点，并结合[自定义占位节点](arkts-user-defined-place-holder.md)控制Web节点的挂载与移除。当从一个窗口上移除Web节点，并挂载到另一个窗口中，即完成Web组件在窗口间的迁移。

在以下示例中，主窗Ability启动时，通过命令式的方式创建了一个Web组件。开发者可以利用common.ets中提供的方法和类，实现Web组件的挂载和移除。Index.ets则提供了一种挂载和移除Web组件的实现方法。通过这种方式，开发者能够实现Web组件在不同窗口中页面的挂载与移除，即实现了Web组件在不同窗口间的迁移。下图是展示了这一迁移过程的示意图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/C6ywJi-EQHSaDHazbukxSA/zh-cn_image_0000002558605064.png?HW-CC-KV=V1&HW-CC-Date=20260429T052924Z&HW-CC-Expire=86400&HW-CC-Sign=FC067E1408BFE0BFB3861B4F842ABF6CC6FC7DD0AA42E9E87D52E4BBEBF68274)

说明

不要将一个Web组件同时挂载在两个父节点下，这会导致非预期行为。

```
1. // 主窗口Ability
2. import { createNWeb, defaultUrl } from '../pages/common';

4. // ...

6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

9. windowStage.loadContent('pages/Index', (err) => {
10. if (err && err.code) {
11. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
12. return;
13. }
14. // 创建Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建，应用仅创建一个Web组件
15. createNWeb(defaultUrl, windowStage.getMainWindowSync().getUIContext());
16. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
17. });
18. }

20. // ...
```

[Entry3Ability.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/NetReqInterceptCacheWinOps/entry3/src/main/ets/entry3ability/Entry3Ability.ets#L19-L49)

```
1. // 提供动态挂载Web组件能力
2. // pages/common.ets
3. import { UIContext, NodeController, BuilderNode, FrameNode } from '@kit.ArkUI';
4. import { webview } from '@kit.ArkWeb';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. export const defaultUrl : string = 'https://www.example.com';

9. // Data为入参封装类
10. class Data{
11. public url: string = '';
12. public webController: webview.WebviewController | null = null;

14. constructor(url: string, webController: webview.WebviewController) {
15. this.url = url;
16. this.webController = webController;
17. }
18. }

20. // @Builder中为动态组件的具体组件内容
21. @Builder
22. function webBuilder(data:Data) {
23. Web({ src: data.url, controller: data.webController })
24. .width('100%')
25. .height('100%')
26. .borderStyle(BorderStyle.Dashed)
27. .borderWidth(2)
28. }

30. let wrap = wrapBuilder<[Data]>(webBuilder);

32. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
33. export class MyNodeController extends NodeController {
34. private builderNode: BuilderNode<[Data]> | null | undefined = null;
35. private webController : webview.WebviewController | null | undefined = null;
36. private rootNode : FrameNode | null = null;

38. constructor(builderNode : BuilderNode<[Data]> | undefined, webController : webview.WebviewController | undefined) {
39. super();
40. this.builderNode = builderNode;
41. this.webController = webController;
42. }

44. // 必须要重写的方法，用于构建节点树、返回节点挂载在对应NodeContainer中
45. // 在对应NodeContainer创建的时候调用或者通过rebuild方法调用刷新
46. makeNode(uiContext: UIContext): FrameNode | null {
47. // 该节点会被挂载在NodeContainer的父节点下
48. return this.rootNode;
49. }

51. // 挂载Webview
52. attachWeb() : void {
53. if (this.builderNode) {
54. let frameNode : FrameNode | null = this.builderNode.getFrameNode();
55. if (frameNode?.getParent() != null) {
56. // 挂载自定义节点前判断该节点是否已经被挂载
57. hilog.error(0x0000, 'testTag', '%{public}s', 'The frameNode is already attached');
58. return;
59. }
60. this.rootNode = this.builderNode.getFrameNode();
61. }
62. }

64. // 卸载Webview
65. detachWeb() : void {
66. this.rootNode = null;
67. }

69. getWebController() : webview.WebviewController | null | undefined {
70. return this.webController;
71. }
72. }

74. // 创建Map保存所需要的BuilderNode
75. let builderNodeMap : Map<string, BuilderNode<[Data]> | undefined> = new Map();
76. // 创建Map保存所需要的webview.WebviewController
77. let webControllerMap : Map<string, webview.WebviewController | undefined> = new Map();

79. // 初始化需要UIContext对象，UIContext对象可通过窗口或自定义组件的getUIContext方法获取
80. export const createNWeb = (url: string, uiContext: UIContext) => {
81. // 创建WebviewController
82. let webController = new webview.WebviewController();
83. // 创建BuilderNode
84. let builderNode : BuilderNode<[Data]> = new BuilderNode(uiContext);
85. // 创建动态Web组件
86. builderNode.build(wrap, new Data(url, webController));

88. // 保存BuilderNode
89. builderNodeMap.set(url, builderNode);
90. // 保存WebviewController
91. webControllerMap.set(url, webController);
92. }

94. // 自定义获取BuilderNode的接口
95. export const getBuilderNode = (url: string) : BuilderNode<[Data]> | undefined => {
96. return builderNodeMap.get(url);
97. }
98. // 自定义获取WebviewController的接口
99. export const getWebviewController = (url : string) : webview.WebviewController | undefined => {
100. return webControllerMap.get(url);
101. }
```

[common.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/NetReqInterceptCacheWinOps/entry3/src/main/ets/pages/common.ets#L16-L118)

```
1. // 使用NodeController的Page页
2. // pages/Index.ets
3. import { getBuilderNode, MyNodeController, defaultUrl, getWebviewController } from "./common"

5. @Entry
6. @Component
7. struct Index {
8. private nodeController : MyNodeController =
9. new MyNodeController(getBuilderNode(defaultUrl), getWebviewController(defaultUrl));

11. build() {
12. Row() {
13. Column() {
14. Button("Attach Webview")
15. .onClick(() => {
16. // 注意不要将同一个节点同时挂载在不同的页面上！
17. this.nodeController.attachWeb();
18. this.nodeController.rebuild();
19. })
20. Button("Detach Webview")
21. .onClick(() => {
22. this.nodeController.detachWeb();
23. this.nodeController.rebuild();
24. })
25. // NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode
26. // Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示
27. NodeContainer(this.nodeController)
28. .height('80%')
29. .width('80%')
30. }
31. .width('100%')
32. }
33. .height('100%')
34. }
35. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/ManageWebPageLoadBrowse/NetReqInterceptCacheWinOps/entry3/src/main/ets/pages/Index.ets#L16-L52)
