---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-offline-mode
title: 使用离线Web组件
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > 使用离线Web组件
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:07+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:71e3b734f9286f995b3806651ef2ec6701794d7f787278af03af657230f41533
---

Web组件能够实现在不同窗口的组件树上进行挂载或移除操作，这一能力使得开发者可以预先创建Web组件，从而实现性能优化。例如，Tab页为Web组件时，页面预先渲染，便于即时显示。

离线Web组件基于自定义占位组件[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)实现。基本原理是构建支持命令式创建的Web组件，此类组件创建后不会立即挂载到组件树中，状态为Hidden和Inactive，因此不会立即对用户呈现。开发者可以在后续使用中按需动态挂载这些组件，以实现更灵活的使用方式。

使用离线Web组件可以预启动渲染进程和预渲染Web页面。

* 预启动渲染进程：在未进入Web页面时，提前创建空Web组件，启动Web的渲染进程，为后续使用做好准备。
* 预渲染Web页面：在Web页面启动或跳转的场景下，预先在后台创建Web组件，加载数据并完成渲染，从而在Web页面启动或跳转时实现快速显示。

## 整体架构

如下图所示，在需要离屏创建Web组件时，定义一个自定义组件以封装Web组件，此Web组件在离线状态下被创建，封装于无状态的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)节点中，并与相应的[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)组件绑定。Web组件在后台预渲染完毕后，当需要展示时，通过[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)将其挂载到ViewTree的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)中，即与对应的[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)组件绑定，即可挂载上树并显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/gzul8_1fQLWOzlkPR9eHCw/zh-cn_image_0000002552958246.png?HW-CC-KV=V1&HW-CC-Date=20260427T234105Z&HW-CC-Expire=86400&HW-CC-Sign=94E1EF1B656A636DFDD3AAA91D9CCCA33E4F0013EE26FA6D4CD265726C109DE3)

## 创建离线Web组件

本示例展示了如何预先创建离线Web组件，并在需要的时候进行挂载和显示。在后续内容中，预启动渲染进程和预渲染Web页面作为性能优化措施，均利用离线Web组件实现。

说明

创建Web组件将占用内存（每个Web组件大约200MB）和计算资源，建议避免一次性创建大量离线Web组件，以减少资源消耗。

```
1. onWindowStageCreate(windowStage: window.WindowStage): void {
2. windowStage.loadContent('pages/Index', (err, data) => {
3. // 创建Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建
4. createNWeb('www.example.com', windowStage.getMainWindowSync().getUIContext());
5. if (err.code) {
6. return;
7. }
8. });
9. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry/src/main/ets/entryability/EntryAbility.ets#L16-L47)

```
1. // 创建NodeController
2. // Common.ets
3. import { UIContext, NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';
4. import { webview } from '@kit.ArkWeb';

6. // @Builder中为动态组件的具体组件内容
7. // Data为入参封装类
8. class Data {
9. public url: ResourceStr = 'www.example.com';
10. public controller: WebviewController = new webview.WebviewController();
11. }

13. @Builder
14. function webBuilder(data: Data) {
15. Column() {
16. Web({ src: data.url, controller: data.controller })
17. .width('100%')
18. .height('100%')
19. }
20. }

22. let wrap = wrapBuilder<Data[]>(webBuilder);

24. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
25. export class MyNodeController extends NodeController {
26. private rootNode: BuilderNode<Data[]> | null = null;

28. // 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中
29. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新
30. makeNode(uiContext: UIContext): FrameNode | null {
31. console.info('uicontext is undefined : ' + (uiContext === undefined));
32. if (this.rootNode !== null) {
33. // 返回FrameNode节点
34. return this.rootNode.getFrameNode();
35. }
36. // 返回null控制动态组件脱离绑定节点
37. return null;
38. }

40. // 当布局大小发生变化时进行回调
41. aboutToResize(size: Size) {
42. console.info('aboutToResize width : ' + size.width + ' height : ' + size.height);
43. }

45. // 当controller对应的NodeContainer在Appear的时候进行回调
46. aboutToAppear() {
47. console.info('aboutToAppear');
48. }

50. // 当controller对应的NodeContainer在Disappear的时候进行回调
51. aboutToDisappear() {
52. console.info('aboutToDisappear');
53. }

55. // 此函数为自定义函数，可作为初始化函数使用
56. // 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容
57. initWeb(url: ResourceStr, uiContext: UIContext, control: WebviewController) {
58. if (this.rootNode !== null) {
59. return;
60. }
61. // 创建节点，需要uiContext
62. this.rootNode = new BuilderNode(uiContext);
63. // 创建动态Web组件
64. this.rootNode.build(wrap, { url: url, controller: control });
65. }
66. }

68. // 创建Map保存所需要的NodeController
69. let nodeMap: Map<ResourceStr, MyNodeController | undefined> = new Map();
70. // 创建Map保存所需要的WebViewController
71. let controllerMap: Map<ResourceStr, WebviewController | undefined> = new Map();

73. // 初始化需要UIContext 需在Ability获取
74. export const createNWeb = (url: ResourceStr, uiContext: UIContext) => {
75. // 创建NodeController
76. let baseNode = new MyNodeController();
77. let controller = new webview.WebviewController();
78. // 初始化自定义Web组件
79. baseNode.initWeb(url, uiContext, controller);
80. controllerMap.set(url, controller);
81. nodeMap.set(url, baseNode);
82. }

84. // 自定义获取NodeController接口
85. export const getNWeb = (url: ResourceStr): MyNodeController | undefined => {
86. return nodeMap.get(url);
87. }
```

```
1. import { getNWeb } from './Common'
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Row() {
7. Column() {
8. // NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode
9. // Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示
10. NodeContainer(getNWeb('www.example.com'))
11. .height('90%')
12. .width('100%')
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry/src/main/ets/pages/Index.ets#L17-L37)

## 预启动渲染进程

在后台预先创建一个Web组件，以启动用于渲染的Web渲染进程，这样可以节省后续Web组件加载时启动Web渲染进程所需的时间。

说明

仅在采用单渲染进程模式的应用中，即全局共享一个Web渲染进程时，优化效果显著。Web渲染进程仅在所有Web组件都被销毁后才会终止。因此，建议应用至少保持一个Web组件处于活动状态。

创建额外的Web组件会产生内存开销。

示例在onWindowStageCreate时预创建Web组件加载blank页面，提前启动Render进程，从index跳转到index2时，优化了Web渲染进程启动和初始化的耗时。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import { createNWeb } from '../pages/Common';
5. // ...
6. onWindowStageCreate(windowStage: window.WindowStage): void {
7. windowStage.loadContent('pages/Index', (err, data) => {
8. if (err && err.code) {
9. console.info('loadContent failed. errorCode: ' + err.code);
10. return;
11. }
12. let windowClass: window.Window = windowStage.getMainWindowSync(); // Obtain the main window of the application.
13. if (!windowClass) {
14. console.info('windowClass is null');
15. return;
16. }
17. // 创建空的Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建
18. createNWeb('about:blank', windowClass.getUIContext());
19. });
20. }
```

[Entry1Ability.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry1/src/main/ets/entry1ability/Entry1Ability.ets#L16-L47)

```
1. // 创建NodeController
2. // Common.ets
3. import { UIContext, NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';
4. import { webview } from '@kit.ArkWeb';

6. // @Builder中为动态组件的具体组件内容
7. // Data为入参封装类
8. class Data {
9. public url: ResourceStr = 'www.example.com';
10. public controller: WebviewController = new webview.WebviewController();
11. }

13. @Builder
14. function webBuilder(data: Data) {
15. Column() {
16. Web({ src: data.url, controller: data.controller })
17. .width('100%')
18. .height('100%')
19. }
20. }

22. let wrap = wrapBuilder<Data[]>(webBuilder);

24. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
25. export class MyNodeController extends NodeController {
26. private rootNode: BuilderNode<Data[]> | null = null;

28. // 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中
29. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新
30. makeNode(uiContext: UIContext): FrameNode | null {
31. console.info('uicontext is undefined : ' + (uiContext === undefined));
32. if (this.rootNode !== null) {
33. // 返回FrameNode节点
34. return this.rootNode.getFrameNode();
35. }
36. // 返回null控制动态组件脱离绑定节点
37. return null;
38. }

40. // 当布局大小发生变化时进行回调
41. aboutToResize(size: Size) {
42. console.info('aboutToResize width : ' + size.width + ' height : ' + size.height);
43. }

45. // 当controller对应的NodeContainer在Appear的时候进行回调
46. aboutToAppear() {
47. console.info('aboutToAppear');
48. }

50. // 当controller对应的NodeContainer在Disappear的时候进行回调
51. aboutToDisappear() {
52. console.info('aboutToDisappear');
53. }

55. // 此函数为自定义函数，可作为初始化函数使用
56. // 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容
57. initWeb(url: ResourceStr, uiContext: UIContext, control: WebviewController) {
58. if (this.rootNode !== null) {
59. return;
60. }
61. // 创建节点，需要uiContext
62. this.rootNode = new BuilderNode(uiContext);
63. // 创建动态Web组件
64. this.rootNode.build(wrap, { url: url, controller: control });
65. }
66. }

68. // 创建Map保存所需要的NodeController
69. let nodeMap: Map<ResourceStr, MyNodeController | undefined> = new Map();
70. // 创建Map保存所需要的WebViewController
71. let controllerMap: Map<ResourceStr, WebviewController | undefined> = new Map();

73. // 初始化需要UIContext 需在Ability获取
74. export const createNWeb = (url: ResourceStr, uiContext: UIContext) => {
75. // 创建NodeController
76. let baseNode = new MyNodeController();
77. let controller = new webview.WebviewController();
78. // 初始化自定义Web组件
79. baseNode.initWeb(url, uiContext, controller);
80. controllerMap.set(url, controller);
81. nodeMap.set(url, baseNode);
82. }

84. // 自定义获取NodeController接口
85. export const getNWeb = (url: ResourceStr): MyNodeController | undefined => {
86. return nodeMap.get(url);
87. }
```

```
1. // index.ets
2. import { webview } from '@kit.ArkWeb';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. @Entry
7. @Component
8. struct Index1 {
9. webviewController: webview.WebviewController = new webview.WebviewController();

11. build() {
12. Column() {
13. Button('Jump to web page').onClick(()=> {
14. this.getUIContext().getRouter().pushUrl({ url: 'pages/Index2' }).catch((error: BusinessError) => {
15. hilog.info(0x0000, 'testTag', 'pushUrl error, %{public}s', error);
16. })
17. }).width('100%').height('100%')
18. }
19. }
20. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry1/src/main/ets/pages/Index.ets#L16-L36)

```
1. import { webview } from '@kit.ArkWeb';

3. @Entry
4. @Component
5. struct Index2 {
6. webviewController: webview.WebviewController = new webview.WebviewController();

8. build() {
9. Row() {
10. Column() {
11. Web({src: $r('app.string.ExampleUrl'), controller: this.webviewController})
12. .width('100%')
13. .height('100%')
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
```

## 预渲染Web页面

预渲染Web页面优化方案适用于Web页面启动和跳转场景，例如，进入首页后，跳转到其他子页。建议在高命中率的页面使用该方案。

预渲染Web页面的实现是提前创建离线Web组件，设置Web为Active状态来开启渲染引擎，进行后台渲染。

说明

1. 预渲染Web页面时，需要明确加载的资源。
2. 由于该方案会将不可见的后台Web设置为Active状态，建议不要预渲染包含自动播放音视频的页面。应用开发者请自行检查和管理页面行为。
3. 预渲染的网页会在后台不断进行渲染，建议在预渲染完成后立即停止渲染，以防止发热和功耗问题。可以参考以下示例，使用 [onFirstMeaningfulPaint](../harmonyos-references/arkts-basic-components-web-events.md#onfirstmeaningfulpaint12) 来确定停止时机，该接口适用于http和https网页。

```
1. onWindowStageCreate(windowStage: window.WindowStage): void {
2. windowStage.loadContent('pages/Index', (err, data) => {
3. // 创建Web动态组件（需传入UIContext），loadContent之后的任意时机均可创建
4. createNWeb('www.example.com', windowStage.getMainWindowSync().getUIContext());
5. if (err.code) {
6. return;
7. }
8. });
9. }
```

[EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry/src/main/ets/entryability/EntryAbility.ets#L16-L47)

```
1. // 创建NodeController
2. // Common.ets
3. import { UIContext } from '@kit.ArkUI';
4. import { webview } from '@kit.ArkWeb';
5. import { NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';

7. // @Builder中为动态组件的具体组件内容
8. // Data为入参封装类
9. class Data {
10. public url: string = 'www.example.com';
11. public controller: WebviewController = new webview.WebviewController();
12. }

14. // 通过布尔变量shouldInactive控制网页在后台完成预渲染后停止渲染
15. let shouldInactive: boolean = true;

17. @Builder
18. function webBuilder(data: Data) {
19. Column() {
20. Web({ src: data.url, controller: data.controller })
21. .onPageBegin(() => {
22. // 调用onActive，开启渲染
23. data.controller.onActive();
24. })
25. .onFirstMeaningfulPaint(() => {
26. if (!shouldInactive) {
27. return;
28. }
29. // 在预渲染完成时触发，停止渲染
30. data.controller.onInactive();
31. shouldInactive = false;
32. })
33. .width('100%')
34. .height('100%')
35. }
36. }

38. let wrap = wrapBuilder<Data[]>(webBuilder);

40. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用
41. export class MyNodeController extends NodeController {
42. private rootNode: BuilderNode<Data[]> | null = null;

44. // 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中
45. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新
46. makeNode(uiContext: UIContext): FrameNode | null {
47. console.info('uiContext is undefined : ' + (uiContext === undefined));
48. if (this.rootNode !== null) {
49. // 返回FrameNode节点
50. return this.rootNode.getFrameNode();
51. }
52. // 返回null控制动态组件脱离绑定节点
53. return null;
54. }

56. // 当布局大小发生变化时进行回调
57. aboutToResize(size: Size) {
58. console.info('aboutToResize width : ' + size.width + ' height : ' + size.height);
59. }

61. // 当controller对应的NodeContainer在Appear的时候进行回调
62. aboutToAppear() {
63. console.info('aboutToAppear');
64. // 切换到前台后，不需要停止渲染
65. shouldInactive = false;
66. }

68. // 当controller对应的NodeContainer在Disappear的时候进行回调
69. aboutToDisappear() {
70. console.info('aboutToDisappear');
71. }

73. // 此函数为自定义函数，可作为初始化函数使用
74. // 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容
75. initWeb(url: string, uiContext: UIContext, control: WebviewController) {
76. if (this.rootNode !== null) {
77. return;
78. }
79. // 创建节点，需要uiContext
80. this.rootNode = new BuilderNode(uiContext);
81. // 创建动态Web组件
82. this.rootNode.build(wrap, { url: url, controller: control });
83. }
84. }

86. // 创建Map保存所需要的NodeController
87. let nodeMap: Map<string, MyNodeController | undefined> = new Map();
88. // 创建Map保存所需要的WebViewController
89. let controllerMap: Map<string, WebviewController | undefined> = new Map();

91. // 初始化需要UIContext 需在Ability获取
92. export const createNWeb = (url: string, uiContext: UIContext) => {
93. // 创建NodeController
94. let baseNode = new MyNodeController();
95. let controller = new webview.WebviewController();
96. // 初始化自定义Web组件
97. baseNode.initWeb(url, uiContext, controller);
98. controllerMap.set(url, controller)
99. nodeMap.set(url, baseNode);
100. }

102. // 自定义获取NodeController接口
103. export const getNWeb = (url: string): MyNodeController | undefined => {
104. return nodeMap.get(url);
105. }
```

```
1. import { getNWeb } from './Common'
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Row() {
7. Column() {
8. // NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode
9. // Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示
10. NodeContainer(getNWeb('www.example.com'))
11. .height('90%')
12. .width('100%')
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry/src/main/ets/pages/Index.ets#L17-L37)

## 复用和释放离线Web组件

通过复用和释放离线Web组件，可以优化内存占用，降低应用因内存占用过高被系统终止的概率。

说明

* 每个窗口推荐只使用一个Web组件。
* 建议复用离线Web组件。
* 建议释放不需要的离线Web组件。

### 复用离线Web组件

应用有多个UI页面都需要显示Web内容时，建议复用离线Web组件，减少组件创建和销毁的性能消耗以及创建多个Web组件的内存占用。

**复用方法**：

1. 离线Web组件不再被使用时，调用WebController的loadUrl方法加载about:blank空页面，为下次其他UI页面复用这个离线Web组件做准备。
2. 新UI页面复用这个离线Web组件时，再调用WebController的loadUrl方法加载需要的Web页面。

### 释放离线Web组件

应用退至后台，或者明确在特定时间段内不再需要使用离线Web组件时，建议释放该组件以减少应用的内存占用。

说明

* 仅当离线Web组件未绑定到UI页面时，才能释放该组件，否则可能导致NodeContainer组件显示空白。
* 可以通过NodeController的onBind和onUnbind回调来跟踪离线Web组件的绑定状态。

**代码实现：**

```
1. // 创建Map保存所需要的NodeController
2. let nodeMap: Map<ResourceStr, MyNodeController | undefined> = new Map();

4. // 创建保存uiContext的全局变量
5. let globalUiContext: UIContext | undefined = undefined;

7. // 创建Set保存已释放的离线组件url信息
8. let recycledNWebs: Set<ResourceStr> = new Set()

10. // 初始化需要UIContext 需在Ability获取
11. export const createNWeb = (url: ResourceStr, uiContext: UIContext) => {
12. // 创建NodeController
13. console.info('createNWeb, url = ' + url);
14. if (!globalUiContext) {
15. globalUiContext = uiContext;
16. }
17. if (getNWeb(url)) {
18. console.info('createNWeb, already exit this node, url:' + url);
19. return;
20. }

22. let baseNode = new MyNodeController();
23. // 初始化自定义Web组件
24. baseNode.initWeb(url, uiContext);
25. nodeMap.set(url, baseNode);
26. recycledNWebs.delete(url);
27. }

29. // 自定义释放/回收离线Web组件的接口，可作为释放离线Web组件函数使用，释放成功返回true
30. // 当离线组件没有被NodeContainer绑定时，允许安全释放，否则节点在不重绘时会显示空白
31. export const recycleNWeb = (url: ResourceStr, force: boolean = false): boolean => {
32. console.info('recycleNWeb, url = ' + url);
33. let baseNode = nodeMap.get(url);
34. if (!baseNode) {
35. console.info('no such node, url = ' + url);
36. return false;
37. }
38. if (!force && baseNode.isBound()) {
39. console.info('the node is in bound and not force, can not delete');
40. return false;
41. }
42. baseNode.rootNode?.dispose();
43. baseNode.rebuild();
44. nodeMap.delete(url);
45. recycledNWebs.add(url);
46. return true;
47. }

49. // 自定义释放所有离线Web组件的接口
50. export const recycleNWebs = (force: boolean = false) => {
51. nodeMap.forEach((_node: MyNodeController | undefined, url: ResourceStr) => {
52. recycleNWeb(url, force);
53. });
54. }

56. // 自定义恢复之前释放离线Web组件的接口
57. export const restoreNWebs = (uiContext: UIContext | undefined = undefined) => {
58. if (!uiContext) {
59. uiContext = globalUiContext;
60. }
61. for (let url of recycledNWebs) {
62. if (uiContext) {
63. createNWeb(url, uiContext);
64. }
65. }
66. recycledNWebs.clear()
67. }
```

[Common.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry3/src/main/ets/pages/Common.ets#L144-L213)

### 复用和释放离线Web组件完整示例

**示例功能说明**

本示例演示了如何复用和释放离线Web组件，以及如何执行预渲染。需要注意的是，示例中使用了多个离线Web组件，这仅用于完整演示相关功能和离线Web组件的使用方法，原则上每个窗口推荐只使用一个Web组件。示例主要演示了以下功能：

1. 对比离线Web组件执行预渲染和不执行预渲染的效果。
2. 在应用退后台时，释放离线Web组件的具体实现步骤。
3. 复用离线Web组件的具体实现步骤。

示例演示了如何让应用退后台释放离线Web组件以及切前台恢复离线Web组件，在[UIAbility](../harmonyos-references/js-apis-app-ability-uiability.md)的onBackground和onForeground回调中分别进行了离线Web组件的释放和恢复。

```
1. onForeground(): void {
2. // Ability has brought to foreground
3. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
4. restoreNWebs()
5. }

7. onBackground(): void {
8. // Ability has back to background
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
10. recycleNWebs()
11. }
```

[Entry3Ability.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry3/src/main/ets/entry3ability/Entry3Ability.ets#L48-L60)

**UI页面功能说明**

示例包括Index页面、Home页面、Page1页面和Page2页面4个UI页面，其中每个UI页面的核心功能如下：

* Index页面作为入口页面，演示页面跳转、离线Web组件的回收，恢复及统计信息展示。

  + 用于跳转至Home页面的按钮；
  + 回收离线Web组件按钮（仅回收没有被绑定的离线Web组件）。
  + 强制回收离线Web组件按钮（演示强制回收所有离线Web组件，包括已绑定和未绑定的组件，会导致对应的NodeContainer白屏）。
  + 恢复离线Web组件按钮。
  + 显示离线Web组件的数量、状态及URL等详细信息。
* Home页面为UI主页，演示离线Web组件的创建，预渲染的执行方法和时机：

  + 页面在创建时会创建3个离线组件，其中一个加载指定网页并进行预渲染，另外两个为空白离线Web组件。
  + 页面提供导航按钮用于跳转至Page1或Page2页面。
* Page1页面同时显示了两个Web页面，每个页面使用了一个离线Web组件，加载并显示相同URL的内容。该页面用于演示预渲染与不预渲染的效果对比，以及如何复用离线组件。

  + 第一个离线Web组件执行了预渲染，可以直接显示页面内容，比第二个离线Web组件更快。
  + 第二个离线Web组件是复用空闲的离线Web组件，其在UI页面的aboutToAppear的生命周期中动态加载这个url。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/xR3Pw3yJQyeTYyLhOfOPjA/zh-cn_image_0000002583478247.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234105Z&HW-CC-Expire=86400&HW-CC-Sign=B5E1153E29D5947F5465D8C39674281B8BFE2B1C0C4CA37276B5DEEE4B67443C)
* Page2页面显示单个Web页面，使用复用空闲离线Web组件的方式加载指定url。

  + Page2页面可以通过传入参数加载指定url，并允许用户在加载后跳转到其他url。
  + Page2会在NavDestination的onWillHide回调中，让当前Web组件加载空白页并取消与当前UI的关联，为下次复用做准备。
  + Page2页面支持嵌套，即使有多层UI页面嵌套，由于采用复用离线Web组件的方式，Web组件数量不会增加。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/hQkbKmvQSZOQI90P-FHfjQ/zh-cn_image_0000002552798598.gif?HW-CC-KV=V1&HW-CC-Date=20260427T234105Z&HW-CC-Expire=86400&HW-CC-Sign=189C2088E3F610642C26C8F72E86D76DD39BF43D13FE2EDA93CFD4B6C761087F)

**完整示例**

[复用和释放离线Web组件示例代码](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkWeb/UseOfflineWebComp/entry3)

## 常见白屏问题排查

1.排查应用上网权限配置。

检查是否已在module.json5中添加网络权限，添加方法请参考[在配置文件中声明权限](declare-permissions.md#在配置文件中声明权限)。

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.INTERNET"
4. }
5. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkWeb/UseOfflineWebComp/entry2/src/main/module.json5#L41-L47)

2.排查[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)与节点绑定的逻辑。

检查节点是否已上组件树，建议在已有的Web组件上方加上Text（请参考以下例子），如果白屏的时候没有出现Text，建议检查[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)与节点绑定的情况。

```
1. @Builder
2. function WebBuilder(data:Data) {
3. Column() {
4. Text('test')
5. Web({ src: data.url, controller: data.controller })
6. .width("100%")
7. .height("100%")
8. }
9. }
```

3.排查Web可见性状态。

如果整个节点已上树，可通过日志[WebPattern::OnVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)查看Web组件可见性状态是否正确，不可见的Web组件可能会造成白屏。
