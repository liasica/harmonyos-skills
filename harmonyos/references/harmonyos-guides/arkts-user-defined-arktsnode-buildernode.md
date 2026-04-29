---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-user-defined-arktsnode-buildernode
title: 自定义声明式节点 (BuilderNode)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用自定义能力 > 自定义节点 > 自定义声明式节点 (BuilderNode)
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:58e784a8144998b72de734c3a0b02a1888c59977cc39843cf0c076480c7d14b9
---

## 概述

自定义声明式节点 ([BuilderNode](../harmonyos-references/js-apis-arkui-buildernode.md))提供能够挂载系统组件的能力，支持采用无状态的UI方式，通过[全局自定义构建函数](arkts-builder.md#全局自定义构建函数)@Builder定制组件树。组件树的根[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点可通过[getFrameNode](../harmonyos-references/js-apis-arkui-buildernode.md#getframenode)获取，该节点既可直接由[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)返回并挂载于[NodeContainer](../harmonyos-references/ts-basic-components-nodecontainer.md)节点下，亦可在FrameNode树与[RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md)树中嵌入声明式组件，实现混合显示。同时，BuilderNode具备纹理导出功能，导出的纹理可在[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)中实现同层渲染。

由BuilderNode构建的ArkTS组件树，支持与自定义节点（如FrameNode、RenderNode）关联使用，确保了系统组件与自定义节点的混合显示效果。对于需与自定义节点对接的第三方框架，BuilderNode提供了嵌入系统组件的方法。

此外，BuilderNode还提供了组件预创建的能力，能够自定义系统组件的创建开始的时间，在后续业务中实现动态挂载与显示。此功能尤其适用于初始化耗时较长的声明式组件，如[Web](../harmonyos-references/arkts-basic-components-web.md)、[XComponent](../harmonyos-references/ts-basic-components-xcomponent.md)等，通过预创建，可以有效减少初始化时间，优化组件加载效率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/W0mp2jFWQsyGBZTVCi7Bdg/zh-cn_image_0000002558604844.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=6D4144938300722706305E358E2BFB2B0D807029980B0D8B9D87755E2721A8DE)

## 基本概念

* 系统组件：组件是UI的必要元素，形成了在界面中的样子，由ArkUI直接提供的称为[系统组件](arkts-ui-development-overview.md)。
* 实体节点：由后端创建的Native节点。

BuilderNode仅可作为叶子节点进行使用。如有更新需要，建议通过BuilderNode中的[update](../harmonyos-references/js-apis-arkui-buildernode.md#update)方式触发更新，不建议通过BuilderNode中获取的RenderNode对节点进行修改操作。

说明

* BuilderNode只支持一个由[wrapBuilder](arkts-wrapbuilder.md)包装的[全局自定义构建函数](arkts-builder.md#全局自定义构建函数)@Builder。
* 一个新建的BuilderNode在[build](../harmonyos-references/js-apis-arkui-buildernode.md#build)之后才能通过[getFrameNode](../harmonyos-references/js-apis-arkui-buildernode.md#getframenode)获取到一个指向根节点的FrameNode对象，否则返回null。
* 如果传入的Builder的根节点为语法节点（if/else/foreach/...），需要额外生成一个FrameNode，在节点树中的显示为“BuilderProxyNode”。
* 如果BuilderNode通过getFrameNode将节点挂载在另一个FrameNode上，或者将其作为子节点挂载在NodeContainer节点上。则节点中使用父组件的布局约束进行布局。
* 如果BuilderNode的FrameNode通过[getRenderNode](../harmonyos-references/js-apis-arkui-framenode.md#getrendernode)形式将自己的节点挂载在RenderNode节点上，由于其FrameNode未上树，其大小默认为0，需要通过构造函数中的[selfIdealSize](../harmonyos-references/js-apis-arkui-buildernode.md#renderoptions)显式指定布局约束大小，才能正常显示。
* BuilderNode的预加载并不会减少组件的创建时间。Web组件创建的时候需要在内核中加载资源，预创建不能减少Web组件的创建的时间，但是可以让内核进行预加载，减少正式使用时候内核的加载耗时。

## 创建BuilderNode对象

BuilderNode对象为一个模板类，需要在创建的时候指定类型。该类型需要与后续build方法中传入的[WrappedBuilder](arkts-wrapbuilder.md)的类型保持一致，否则会存在编译告警导致编译失败。

## 创建组件树

通过BuilderNode的build可以实现组件树的创建。依照传入的WrappedBuilder对象创建组件树，并持有组件树的根节点。

说明

无状态的UI方法全局@Builder最多拥有一个根节点。

build方法中对应的@Builder支持一个参数作为入参。

build中对于@Builder嵌套@Builder进行使用的场景，需要保证嵌套的参数与build的中提供的入参一致。

对于@Builder嵌套@Builder进行使用的场景，如果入参类型不一致，则要求增加[BuildOptions](../harmonyos-references/js-apis-arkui-buildernode.md#buildoptions12)字段作为[build](../harmonyos-references/js-apis-arkui-buildernode.md#build12)的入参。

需要操作BuilderNode中的对象时，需要保证其引用不被回收。当BuilderNode对象被虚拟机回收之后，它的FrameNode、RenderNode对象也会与后端节点解引用。即从BuilderNode中获取的FrameNode对象不对应任何一个节点。

创建离线节点以及组件树，结合FrameNode进行使用。

BuilderNode的根节点直接作为[NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md)的[makeNode](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode)返回值。

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';

3. class Params {
4. public text: string = '';

6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column() {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 36 })
18. }
19. }

21. class TextNodeController extends NodeController {
22. private textNode: BuilderNode<[Params]> | null = null;
23. private message: string = 'DEFAULT';

25. constructor(message: string) {
26. super();
27. this.message = message;
28. }

30. makeNode(context: UIContext): FrameNode | null {
31. this.textNode = new BuilderNode(context);
32. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message))
33. return this.textNode.getFrameNode();
34. }
35. }

37. @Entry
38. @Component
39. struct FrameNodePage {
40. @State message: string = 'hello';

42. build() {
43. Row() {
44. Column() {
45. NodeContainer(new TextNodeController(this.message))
46. .width('100%')
47. .height(100)
48. .backgroundColor('#FFF0F0F0')
49. }
50. .width('100%')
51. .height('100%')
52. }
53. .height('100%')
54. }
55. }
```

[FrameNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/FrameNode.ets#L15-L71)

将BuilderNode与RenderNode进行结合使用。

BuilderNode的RenderNode挂载其它RenderNode下时，需要明确定义[RenderOptions](../harmonyos-references/js-apis-arkui-buildernode.md#renderoptions)的selfIdealSize属性的大小作为BuilderNode的布局约束。不建议通过该方式挂载节点。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext, RenderNode } from '@kit.ArkUI';

3. class Params {
4. public text: string = '';

6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column() {
14. Text(params.text)
15. .fontSize(50)
16. .fontWeight(FontWeight.Bold)
17. .margin({ bottom: 36 })
18. }
19. }

21. class TextNodeController extends NodeController {
22. private rootNode: FrameNode | null = null;
23. private textNode: BuilderNode<[Params]> | null = null;
24. private message: string = 'DEFAULT';

26. constructor(message: string) {
27. super();
28. this.message = message;
29. }

31. makeNode(context: UIContext): FrameNode | null {
32. this.rootNode = new FrameNode(context);
33. let renderNode = new RenderNode();
34. renderNode.clipToFrame = false;
35. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
36. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
37. const textRenderNode = this.textNode?.getFrameNode()?.getRenderNode();

39. const rootRenderNode = this.rootNode.getRenderNode();
40. if (rootRenderNode !== null) {
41. rootRenderNode.appendChild(renderNode);
42. renderNode.appendChild(textRenderNode);
43. }

45. return this.rootNode;
46. }
47. }

49. @Entry
50. @Component
51. struct RenderNodePage {
52. @State message: string = 'hello world';

54. build() {
55. Row() {
56. Column() {
57. NodeContainer(new TextNodeController(this.message))
58. .width('100%')
59. .height(100)
60. .backgroundColor('#FFF0F0F0')
61. }
62. .width('100%')
63. .height('100%')
64. }
65. .height('100%')
66. }
67. }
```

[RenderNode.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/RenderNode.ets#L15-L83)

## 更新组件树

通过BuilderNode对象的build创建组件树。依照传入的WrappedBuilder对象创建组件树，并持有组件树的根节点。

自定义组件的更新遵循[状态管理](arkts-state-management-overview.md)的更新机制。WrappedBuilder中直接使用的自定义组件其父组件为BuilderNode对象。因此，更新子组件即WrappedBuilder中定义的自定义组件，需要遵循状态管理的定义将相关的状态变量定义为[@Prop](arkts-prop.md)或者[@ObjectLink](arkts-observed-and-objectlink.md)。装饰器的选择请参照状态管理的装饰器规格结合应用开发需求进行选择。

使用update更新BuilderNode中的节点。

使用[updateConfiguration](../harmonyos-references/js-apis-arkui-buildernode.md#updateconfiguration12)触发BuilderNode中节点的全量更新。

更新BuilderNode中的节点。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. class Params {
4. public text: string = '';
5. constructor(text: string) {
6. this.text = text;
7. }
8. }

10. // 自定义组件
11. @Component
12. struct TextBuilder {
13. // 作为自定义组件中需要更新的属性，数据类型为基础属性，定义为@Prop
14. @Prop message: string = 'TextBuilder';

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(40)
21. .fontWeight(FontWeight.Bold)
22. .margin({ bottom: 10 })
23. .backgroundColor(Color.Gray)
24. }
25. }
26. }
27. }

29. @Builder
30. function buildText(params: Params) {
31. Column() {
32. Text(params.text)
33. .fontSize(40)
34. .fontWeight(FontWeight.Bold)
35. .margin({ bottom: 10 })
36. TextBuilder({ message: params.text }) // 自定义组件
37. }
38. .width('100%')
39. .alignItems(HorizontalAlign.Center)
40. .justifyContent(FlexAlign.Center)

42. }

44. class TextNodeController extends NodeController {
45. private textNode: BuilderNode<[Params]> | null = null;
46. private message: string = '';

48. constructor(message: string) {
49. super();
50. this.message = message;
51. }

53. makeNode(context: UIContext): FrameNode | null {
54. this.textNode = new BuilderNode(context);
55. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
56. return this.textNode.getFrameNode();
57. }

59. update(message: string) {
60. if (this.textNode !== null) {
61. // 调用update进行更新。
62. this.textNode.update(new Params(message));
63. }
64. }
65. }

67. @Entry
68. @Component
69. struct WrappedBuilderPage {
70. @State message: string = 'hello';
71. private textNodeController: TextNodeController = new TextNodeController(this.message);
72. private count = 0;

74. build() {
75. Row() {
76. Column({ space: 25}) {
77. NodeContainer(this.textNodeController)
78. .width('100%')
79. .height(110)
80. .backgroundColor('#FFF0F0F0')
81. Button('Update')
82. .onClick(() => {
83. this.count += 1;
84. const message = 'Update' + this.count.toString();
85. this.textNodeController.update(message);
86. })
87. .fontSize(20)
88. .fontWeight(FontWeight.Bold)
89. }
90. .width('100%')
91. .height('100%')
92. }
93. .height('100%')
94. }
95. }
```

[WrappedBuilder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/WrappedBuilder.ets#L15-L105)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/dWECJ6efS72bTW9lrqjj3g/zh-cn_image_0000002589324369.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=A9D9D64F46DE8CA394A42EC5DF38A4367926BC270849A4011598A8A1F125239C)

## 解除实体节点引用关系

由于BuilderNode对应的是后端的实体节点，正常的内存释放依赖前端对象的回收。如果期望直接释放后端的节点对象，则可以通过调用[dispose](../harmonyos-references/js-apis-arkui-buildernode.md#dispose12)与实体节点解除引用关系，此时持有的前端BuilderNode对象不再影响实体节点的生命周期。

说明

当BuilderNode对象调用dispose之后，不仅BuilderNode对象与后端实体节点解除引用关系，BuilderNode中的FrameNode与RenderNode也会同步和实体节点解除引用关系。

若前端对象BuilderNode无法释放，容易导致内存泄漏。建议在不再需要对该BuilderNode对象进行操作时，开发者应主动调用dispose释放后端节点，以减少引用关系的复杂性，降低内存泄漏的风险。

## 注入触摸事件

BuilderNode中提供了[postTouchEvent](../harmonyos-references/js-apis-arkui-buildernode.md#posttouchevent)，可以通过该接口向BuilderNode中绑定的组件注入[触摸事件](../harmonyos-references/ts-universal-events-touch.md)，实现事件的模拟转发。

通过postTouchEvent向BuilderNode对应的节点树中注入触摸事件。

向BuilderNode中的Column组件转发另一个Column接收的事件，即点击下方的Column组件，上方的Column组件也会收到同样的触摸事件。当Button中的事件被成功识别的时候，返回值为true。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. class Params {
5. public text: string = 'this is a text';
6. }

8. @Builder
9. function buttonBuilder(params: Params) {
10. Column() {
11. Button(`button ` + params.text)
12. .borderWidth(2)
13. .backgroundColor(Color.Orange)
14. .width('100%')
15. .height('100%')
16. .gesture(
17. TapGesture()
18. .onAction((event: GestureEvent) => {
19. hilog.info(0xF811, 'testTag', '%{public}s', 'TapGesture');
20. })
21. )
22. }
23. .width(500)
24. .height(300)
25. .backgroundColor(Color.Gray)
26. }

28. // 创建并初始化BuilderNode
29. class MyNodeController extends NodeController {
30. private rootNode: BuilderNode<[Params]> | null = null;
31. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(buttonBuilder);

33. makeNode(uiContext: UIContext): FrameNode | null {
34. this.rootNode = new BuilderNode(uiContext);
35. this.rootNode.build(this.wrapBuilder, { text: 'this is a string' });
36. return this.rootNode.getFrameNode();
37. }

39. // 转发触摸事件到BuilderNode
40. postTouchEvent(touchEvent: TouchEvent): void {
41. if (this.rootNode == null) {
42. return;
43. }
44. let result = this.rootNode.postTouchEvent(touchEvent);
45. hilog.info(0xF811, 'testTag', '%{public}s', 'result' + result);
46. }
47. }

49. @Entry
50. @Component
51. struct postTouchEventPage {
52. private nodeController: MyNodeController = new MyNodeController();
53. @State bgColor: Color = Color.Pink;

55. build() {
56. Column() {
57. NodeContainer(this.nodeController)
58. .height(300)
59. .width(500)
60. Column()
61. .id('onTouch')
62. .width(500)
63. .height(300)
64. .backgroundColor(this.bgColor)
65. .onTouch((event) => {
66. // 事件非空时，将触摸事件转发给节点控制器
67. if (event != undefined) {
68. this.nodeController.postTouchEvent(event);
69. this.bgColor = Color.Blue;
70. }
71. })
72. }
73. }
74. }
```

[PostTouchEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/PostTouchEvent.ets#L15-L90)

## BuilderNode内的BuilderProxyNode导致树结构发生变化

若传入的Builder的根节点为语法节点（if/else/foreach/…）或自定义组件，将额外生成一个FrameNode，在节点树中显示为“BuilderProxyNode”，这会导致树结构变化，影响某些测试的传递过程。

在以下示例中，Column和Row绑定了触摸事件，同时Column设置了[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性为[HitTestMode.Transparent](../harmonyos-references/ts-appendix-enums.md#hittestmode9)。然而，由于生成了BuilderProxyNode，且BuilderProxyNode无法设置属性，因此在触摸Column时，Column的触摸测试无法传递到Row上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/8YcEbJ6zQkiiYkx7dYoMUw/zh-cn_image_0000002589244309.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=9FEE5A0F5DD962B6877B53648DFF5C8AE5FE90C3E724B0F64A6BD5154CD8AD6F)

```
1. import { BuilderNode, typeNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Component
5. struct BlueRowComponent {
6. build() {
7. Row() {
8. Row() {
9. }
10. .width('100%')
11. .height('200vp')
12. .backgroundColor(0xFF2787D9)
13. .onTouch((event: TouchEvent) => {
14. // 触摸绿色Column，蓝色Row的触摸事件不触发。
15. hilog.info(0xF811, 'testTag', '%{public}s', 'blue touched: ' + event.type);
16. })
17. }
18. }
19. }

21. @Component
22. struct GreenColumnComponent {
23. build() {
24. Column() {
25. }
26. .id('BuilderProxyNode01')
27. .width('100%')
28. .height('100vp')
29. .backgroundColor(0xFF17A98D)
30. .hitTestBehavior(HitTestMode.Transparent)
31. .onTouch((event: TouchEvent) => {
32. hilog.info(0xF811, 'testTag', '%{public}s', 'green touched: ' + event.type);
33. })
34. }
35. }

37. @Builder
38. function buildBlueRow() {
39. // Builder直接挂载自定义组件，生成BuilderProxyNode。
40. BlueRowComponent()
41. }

43. @Builder
44. function buildGreenColumn() {
45. // Builder直接挂载自定义组件，生成BuilderProxyNode。
46. GreenColumnComponent()
47. }

49. class MyNodeController extends NodeController {
50. makeNode(uiContext: UIContext): FrameNode | null {
51. const relativeContainer = typeNode.createNode(uiContext, 'RelativeContainer');

53. const blueRowNode = new BuilderNode(uiContext);
54. blueRowNode.build(wrapBuilder(buildBlueRow));

56. const greenColumnNode = new BuilderNode(uiContext);
57. greenColumnNode.build(wrapBuilder(buildGreenColumn));

59. // greenColumnNode覆盖在blueRowNode上。
60. relativeContainer.appendChild(blueRowNode.getFrameNode());
61. relativeContainer.appendChild(greenColumnNode.getFrameNode());

63. return relativeContainer;
64. }
65. }

67. @Entry
68. @Component
69. struct BuilderProxyNode01 {
70. build() {
71. Column() {
72. NodeContainer(new MyNodeController())
73. }
74. }
75. }
```

[BuilderProxyNode01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/BuilderProxyNode01.ets#L15-L91)

在上述场景中，若要实现触摸测试的传递，可以使用一个容器组件包裹语法节点或自定义组件，以避免生成BuilderProxyNode，并将容器组件的hitTestBehavior设置为HitTestMode.Transparent，从而向兄弟节点传递触摸测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/2CsVPuQlQe-lI7kY73JxYQ/zh-cn_image_0000002558764502.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=DF6CCA080E5CDF32D1D354A833D80C980E1C81F4D830225DE2CF2DC8AC2E501A)

```
1. import { BuilderNode, typeNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Component
5. struct BlueRowComponent {
6. build() {
7. Row() {
8. Row() {
9. }
10. .width('100%')
11. .height('200vp')
12. .backgroundColor(0xFF2787D9)
13. .onTouch((event: TouchEvent) => {
14. // 触摸绿色Column，蓝色Row的触摸事件触发。
15. hilog.info(0xF811, 'testTag', '%{public}s', 'blue touched: ' + event.type);
16. })
17. }
18. }
19. }

21. @Component
22. struct GreenColumnComponent {
23. build() {
24. Column() {
25. }
26. .width('100%')
27. .height('100vp')
28. .backgroundColor(0xFF17A98D)
29. .hitTestBehavior(HitTestMode.Transparent)
30. .onTouch((event: TouchEvent) => {
31. hilog.info(0xF811, 'testTag', '%{public}s', 'green touched: ' + event.type);
32. })
33. }
34. }

36. @Builder
37. function buildBlueRow() {
38. // Builder直接挂载自定义组件，生成BuilderProxyNode。
39. BlueRowComponent()
40. }

42. @Builder
43. function buildGreenColumn() {
44. // Builder根节点为容器组件，不会生成BuilderProxyNode，可以设置属性。
45. Stack() {
46. GreenColumnComponent()
47. }
48. .hitTestBehavior(HitTestMode.Transparent)
49. }

51. class MyNodeController extends NodeController {
52. makeNode(uiContext: UIContext): FrameNode | null {
53. const relativeContainer = typeNode.createNode(uiContext, 'RelativeContainer');

55. const blueRowNode = new BuilderNode(uiContext);
56. blueRowNode.build(wrapBuilder(buildBlueRow));

58. const greenColumnNode = new BuilderNode(uiContext);
59. greenColumnNode.build(wrapBuilder(buildGreenColumn));

61. // greenColumnNode覆盖在blueRowNode上。
62. relativeContainer.appendChild(blueRowNode.getFrameNode());
63. relativeContainer.appendChild(greenColumnNode.getFrameNode());

65. return relativeContainer;
66. }
67. }

69. @Entry
70. @Component
71. struct Index {
72. build() {
73. Column() {
74. NodeContainer(new MyNodeController())
75. .id('BuilderProxyNode02')
76. }
77. }
78. }
```

[BuilderProxyNode02.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/BuilderProxyNode02.ets#L15-L94)

此外，对于自定义组件，可以直接设置属性，此时将额外生成节点\_\_Common\_\_，自定义组件的属性将挂载于\_\_Common\_\_上，同样能够实现上述效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/JplKQ4zVSf6id_W06TQE8g/zh-cn_image_0000002558604846.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=914016B2DF6511870A1A7FF274C66F86A032C79A8D675BE2337FAED898032945)

```
1. import { BuilderNode, typeNode, NodeController, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. @Component
5. struct BlueRowComponent {
6. build() {
7. Row() {
8. Row() {
9. }
10. .width('100%')
11. .height('200vp')
12. .backgroundColor(0xFF2787D9)
13. .onTouch((event: TouchEvent) => {
14. // 触摸绿色Column，蓝色Row的触摸事件触发。
15. hilog.info(0xF811, 'testTag', '%{public}s', 'blue touched: ' + event.type);
16. })
17. }
18. }
19. }

21. @Component
22. struct GreenColumnComponent {
23. build() {
24. Column() {
25. }
26. .width('100%')
27. .height('100vp')
28. .backgroundColor(0xFF17A98D)
29. .hitTestBehavior(HitTestMode.Transparent)
30. .onTouch((event: TouchEvent) => {
31. hilog.info(0xF811, 'testTag', '%{public}s', 'green touched: ' + event.type);
32. })
33. }
34. }

36. @Builder
37. function buildBlueRow() {
38. // Builder直接挂载自定义组件，生成BuilderProxyNode。
39. BlueRowComponent()
40. }

42. @Builder
43. function buildGreenColumn() {
44. // 给自定义组件设置属性生成__Common__节点，Builder根节点为__Common__节点，不会生成BuilderProxyNode。
45. GreenColumnComponent()
46. .hitTestBehavior(HitTestMode.Transparent)
47. }

49. class MyNodeController extends NodeController {
50. makeNode(uiContext: UIContext): FrameNode | null {
51. const relativeContainer = typeNode.createNode(uiContext, 'RelativeContainer');

53. const blueRowNode = new BuilderNode(uiContext);
54. blueRowNode.build(wrapBuilder(buildBlueRow));

56. const greenColumnNode = new BuilderNode(uiContext);
57. greenColumnNode.build(wrapBuilder(buildGreenColumn));

59. // greenColumnNode覆盖在blueRowNode上。
60. relativeContainer.appendChild(blueRowNode.getFrameNode());
61. relativeContainer.appendChild(greenColumnNode.getFrameNode());

63. return relativeContainer;
64. }
65. }

67. @Entry
68. @Component
69. struct Index {
70. build() {
71. Column() {
72. NodeContainer(new MyNodeController())
73. }
74. }
75. }
```

[BuilderProxyNode03.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/BuilderProxyNode03.ets#L15-L91)

## BuilderNode调用reuse和recycle接口实现节点复用能力

调用[reuse](../harmonyos-references/js-apis-arkui-buildernode.md#reuse12)接口和[recycle](../harmonyos-references/js-apis-arkui-buildernode.md#recycle12)接口，将复用和回收事件传递至BuilderNode中的自定义组件，以实现BuilderNode节点内部的自定义组件的复用。

以下面的Demo为例，被复用的自定义组件ReusableChildComponent可以传递复用和回收事件到其下的自定义组件ChildComponent3，但无法传递给自定义组件ChildComponent2，因为被BuilderNode所隔断。因此需要主动调用BuilderNode的reuse和recycle接口，将复用和回收事件传递给自定义组件ChildComponent2，以实现复用效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/6gBrgdg2Skqt-5k7O0nqjw/zh-cn_image_0000002589324371.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=E6C5D558B5A2CB1F3D93A47822529CD6BEE660F46762E5765439EECAFAFA0C89)

```
1. import { FrameNode, NodeController, BuilderNode, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TEST_TAG: string = 'Reuse+Recycle';

6. class MyDataSource {
7. private dataArray: string[] = [];
8. private listener: DataChangeListener | null = null;

10. public totalCount(): number {
11. return this.dataArray.length;
12. }

14. public getData(index: number) {
15. return this.dataArray[index];
16. }

18. public pushData(data: string) {
19. this.dataArray.push(data);
20. }

22. public reloadListener(): void {
23. this.listener?.onDataReloaded();
24. }

26. public registerDataChangeListener(listener: DataChangeListener): void {
27. this.listener = listener;
28. }

30. public unregisterDataChangeListener(): void {
31. this.listener = null;
32. }
33. }

35. class Params {
36. public item: string = '';

38. constructor(item: string) {
39. this.item = item;
40. }
41. }

43. @Builder
44. function buildNode(param: Params = new Params('hello')) {
45. Row() {
46. Text(`C${param.item} -- `)
47. // 该自定义组件在BuilderNode中无法被正确复用
48. ChildComponent2({ item: param.item })
49. }
50. }

52. class MyNodeController extends NodeController {
53. public builderNode: BuilderNode<[Params]> | null = null;
54. public item: string = '';

56. makeNode(uiContext: UIContext): FrameNode | null {
57. if (this.builderNode == null) {
58. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 300, height: 200 } });
59. this.builderNode.build(wrapBuilder<[Params]>(buildNode), new Params(this.item));
60. }
61. return this.builderNode.getFrameNode();
62. }
63. }

65. // 被回收复用的自定义组件，其状态变量会更新，而子自定义组件ChildComponent3中的状态变量也会更新，但BuilderNode会阻断这一传递过程。
66. @Reusable
67. @Component
68. struct ReusableChildComponent {
69. @Prop item: string = '';
70. @Prop switch: string = '';
71. private controller: MyNodeController = new MyNodeController();

73. aboutToAppear() {
74. this.controller.item = this.item;
75. }

77. aboutToRecycle(): void {
78. hilog.info(0xF811,'testTag','%{public}s',`${TEST_TAG} ReusableChildComponent aboutToRecycle ${this.item}`);

80. // 当开关为open，通过BuilderNode的reuse接口和recycle接口传递给其下的自定义组件，例如ChildComponent2，完成复用。
81. if (this.switch === 'open') {
82. this.controller?.builderNode?.recycle();
83. }
84. }

86. aboutToReuse(params: object): void {
87. hilog.info(0xF811,'testTag','%{public}s',`${TEST_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}`);

89. // 当开关为open，通过BuilderNode的reuse接口和recycle接口传递给其下的自定义组件，例如ChildComponent2，完成复用。
90. if (this.switch === 'open') {
91. this.controller?.builderNode?.reuse(params);
92. }
93. }

95. build() {
96. Row() {
97. Text(`A${this.item}--`)
98. ChildComponent3({ item: this.item })
99. NodeContainer(this.controller);
100. }
101. }
102. }

104. @Component
105. struct ChildComponent2 {
106. @Prop item: string = 'false';

108. aboutToReuse(params: Record<string, object>) {
109. hilog.info(0xF811,'testTag','%{public}s',`${TEST_TAG} ChildComponent2 aboutToReuse ${JSON.stringify(params)}`);
110. }

112. aboutToRecycle(): void {
113. hilog.info(0xF811,'testTag','%{public}s',`${TEST_TAG} ChildComponent2 aboutToRecycle ${this.item}`);
114. }

116. build() {
117. Row() {
118. Text(`D${this.item}`)
119. .fontSize(20)
120. .backgroundColor(Color.Yellow)
121. .margin({ left: 10 })
122. }.margin({ left: 10, right: 10 })
123. }
124. }

126. @Component
127. struct ChildComponent3 {
128. @Prop item: string = 'false';

130. aboutToReuse(params: Record<string, object>) {
131. hilog.info(0xF811,'testTag','%{public}s',`${TEST_TAG} ChildComponent3 aboutToReuse ${JSON.stringify(params)}`);
132. }

134. aboutToRecycle(): void {
135. hilog.info(0xF811,'testTag','%{public}s',`${TEST_TAG} ChildComponent3 aboutToRecycle ${this.item}`);
136. }

138. build() {
139. Row() {
140. Text(`B${this.item}`)
141. .fontSize(20)
142. .backgroundColor(Color.Yellow)
143. .margin({ left: 10 })
144. }.margin({ left: 10, right: 10 })
145. }
146. }

149. @Entry
150. @Component
151. struct Index {
152. @State data: MyDataSource = new MyDataSource();

154. aboutToAppear() {
155. for (let i = 0; i < 100; i++) {
156. this.data.pushData(i.toString());
157. }
158. }

160. build() {
161. Column() {
162. List({ space: 3 }) {
163. LazyForEach(this.data, (item: string) => {
164. ListItem() {
165. ReusableChildComponent({
166. item: item,
167. switch: 'open' // 将open改为close可观察到，BuilderNode不通过reuse和recycle接口传递复用时，BuilderNode内部的自定义组件的行为表现。
168. })
169. }
170. }, (item: string) => item)
171. }
172. .id('List')
173. .width('100%')
174. .height('100%')
175. }
176. }
177. }
```

[ReusablePage01.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/ReusablePage01.ets#L15-L192)

## BuilderNode在子自定义组件中使用@Reusable装饰器

BuilderNode节点的复用机制与使用[@Reusable](arkts-reusable.md)装饰器的自定义组件的复用机制会相互冲突。因此，当BuilderNode的子节点为自定义组件时，不支持该自定义组件使用@Reusable装饰器标记，否则将导致应用程序触发JSCrash。若需要使用@Reusable装饰器，应使用一个普通自定义组件包裹该自定义组件。

在下面的示例中，ReusableChildComponent作为BuilderNode的子自定义组件，无法标记为@Reusable。通过ChildComponent2对其包裹，ReusableChildComponent可以使用@Reusable装饰器标记。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/cfVx2OQ2SQevNCndc23y7w/zh-cn_image_0000002589244311.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=C6BF675184859AD5718CEB075F0B2A1C16C14955DC829759CFA3CBE74114B427)

```
1. import { FrameNode, NodeController, BuilderNode, UIContext } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TEST_TAG: string = 'Reusable';

6. class Params {
7. public item: string = '';

9. constructor(item: string) {
10. this.item = item;
11. }
12. }

14. @Builder
15. function buildNode(param: Params = new Params('Hello')) {
16. ChildComponent2({ item: param.item })
17. }

19. class MyNodeController extends NodeController {
20. public builderNode: BuilderNode<[Params]> | null = null;
21. public item: string = '';

23. constructor(item: string) {
24. super();
25. this.item = item;
26. }

28. makeNode(uiContext: UIContext): FrameNode | null {
29. if (this.builderNode == null) {
30. this.builderNode = new BuilderNode(uiContext, { selfIdealSize: { width: 300, height: 200 } });
31. this.builderNode.build(wrapBuilder<[Params]>(buildNode), new Params(this.item));
32. }
33. return this.builderNode.getFrameNode();
34. }
35. }

37. // 标记了@Reusable的自定义组件，无法直接被BuilderNode挂载为子节点。
38. @Reusable
39. @Component
40. struct ReusableChildComponent {
41. @Prop item: string = '';

43. aboutToReuse(params: object): void {
44. hilog.info(0xF811, 'testTag', '%{public}s',
45. `${TEST_TAG} ReusableChildComponent aboutToReuse ${JSON.stringify(params)}`);
46. }

48. aboutToRecycle(): void {
49. hilog.info(0xF811, 'testTag', '%{public}s', `${TEST_TAG} ReusableChildComponent aboutToRecycle ${this.item}`);
50. }

52. build() {
53. Text(`A--${this.item}`)
54. .id('ReusablePage02')
55. }
56. }

58. // 未标记@Reusable的自定义组件。
59. @Component
60. struct ChildComponent2 {
61. @Prop item: string = '';

63. aboutToReuse(params: Record<string, object>) {
64. hilog.info(0xF811, 'testTag', '%{public}s', `${TEST_TAG} ChildComponent2 aboutToReuse ${JSON.stringify(params)}`);
65. }

67. aboutToRecycle(): void {
68. hilog.info(0xF811, 'testTag', '%{public}s', `${TEST_TAG} ChildComponent2 aboutToRecycle ${this.item}`);
69. }

71. build() {
72. ReusableChildComponent({ item: this.item })
73. }
74. }

77. @Entry
78. @Component
79. struct Index {
80. @State controller: MyNodeController = new MyNodeController('Child');

82. build() {
83. Column() {
84. NodeContainer(this.controller)
85. }
86. .width('100%')
87. .height('100%')
88. }
89. }
```

[ReusablePage02.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/ReusablePage02.ets#L15-L104)

## 通过系统环境变化更新节点

使用[updateConfiguration](../harmonyos-references/js-apis-arkui-buildernode.md#updateconfiguration12)来监听[系统环境变化](../harmonyos-references/js-apis-app-ability-configuration.md)事件，以触发节点的全量更新。

说明

updateConfiguration接口用于通知对象进行更新，更新所使用的系统环境取决于应用当前系统环境的变化。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
2. import { AbilityConstant, Configuration, EnvironmentCallback } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. class Params {
6. public text: string = '';

8. constructor(text: string) {
9. this.text = text;
10. }
11. }

13. // 自定义组件
14. @Component
15. struct TextBuilder {
16. // 作为自定义组件中需要更新的属性，数据类型为基础属性，定义为@Prop
17. @Prop message: string = 'TextBuilder';

19. build() {
20. Row() {
21. Column() {
22. Text(this.message)
23. .fontSize(50)
24. .fontWeight(FontWeight.Bold)
25. .margin({ bottom: 36 })
26. .fontColor($r(`app.color.text_color`)) // 开发者可在资源目录下的color.json文件中自定义颜色
27. .backgroundColor($r(`app.color.start_window_background`))
28. }
29. }
30. }
31. }

33. @Builder
34. function buildText(params: Params) {
35. Column() {
36. Text(params.text)
37. .fontSize(50)
38. .fontWeight(FontWeight.Bold)
39. .margin({ bottom: 36 })
40. .fontColor($r(`app.color.text_color`))
41. TextBuilder({ message: params.text }) // 自定义组件
42. }.backgroundColor($r(`app.color.start_window_background`))
43. }

45. class TextNodeController extends NodeController {
46. private textNode: BuilderNode<[Params]> | null = null;
47. private message: string = '';

49. constructor(message: string) {
50. super();
51. this.message = message;
52. }

54. makeNode(context: UIContext): FrameNode | null {
55. return this.textNode?.getFrameNode() ? this.textNode?.getFrameNode() : null;
56. }

58. createNode(context: UIContext) {
59. this.textNode = new BuilderNode(context);
60. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
61. builderNodeMap.push(this.textNode);
62. }

64. deleteNode() {
65. let node = builderNodeMap.pop();
66. node?.dispose();
67. }

69. update(message: string) {
70. if (this.textNode !== null) {
71. // 调用update进行更新。
72. this.textNode.update(new Params(message));
73. }
74. }
75. }

77. // 记录创建的自定义节点对象
78. const builderNodeMap: BuilderNode<[Params]>[] = [];

80. function updateColorMode() {
81. builderNodeMap.forEach((value, index) => {
82. // 通知BuilderNode环境变量改变
83. value.updateConfiguration();
84. });
85. }

87. @Entry
88. @Component
89. struct Index {
90. @State message: string = 'hello';
91. private textNodeController: TextNodeController = new TextNodeController(this.message);
92. private count = 0;

94. aboutToAppear(): void {
95. let environmentCallback: EnvironmentCallback = {
96. onMemoryLevel: (level: AbilityConstant.MemoryLevel): void => {
97. hilog.info(0xF811, 'testTag', '%{public}s', 'onMemoryLevel');
98. },
99. onConfigurationUpdated: (config: Configuration): void => {
100. hilog.info(0xF811, 'testTag', '%{public}s', 'onConfigurationUpdated ' + JSON.stringify(config));
101. updateColorMode();
102. }
103. };
104. // 注册监听回调
105. this.getUIContext().getHostContext()?.getApplicationContext().on('environment', environmentCallback);
106. // 创建自定义节点并添加至map
107. this.textNodeController.createNode(this.getUIContext());
108. }

110. aboutToDisappear(): void {
111. // 移除map中的引用，并将自定义节点释放
112. this.textNodeController.deleteNode();
113. }

115. build() {
116. Row() {
117. Column() {
118. NodeContainer(this.textNodeController)
119. .width('100%')
120. .height(200)
121. .backgroundColor('#FFF0F0F0')
122. Button('Update')
123. .onClick(() => {
124. this.count += 1;
125. const message = 'Update ' + this.count.toString();
126. this.textNodeController.update(message);
127. })
128. }
129. .width('100%')
130. .height('100%')
131. }
132. .height('100%')
133. }
134. }
```

[EnvironmentCallbackPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/EnvironmentCallbackPage.ets#L15-L150)

## 跨页面复用注意事项

在使用[路由](../harmonyos-references/arkts-apis-uicontext-router.md)接口[router.replaceUrl](../harmonyos-references/arkts-apis-uicontext-router.md#replaceurl)、[router.back](../harmonyos-references/arkts-apis-uicontext-router.md#back)、[router.clear](../harmonyos-references/arkts-apis-uicontext-router.md#clear)、[router.replaceNamedRoute](../harmonyos-references/arkts-apis-uicontext-router.md#replacenamedroute)操作页面时，若某个被缓存的BuilderNode位于即将销毁的页面内，那么在新页面中复用该BuilderNode时，可能会存在数据无法更新或新创建节点无法显示的问题。以[router.replaceNamedRoute](../harmonyos-references/arkts-apis-uicontext-router.md#replacenamedroute)为例，在以下示例代码中，当点击“router replace”按钮后，页面将切换至PageTwo，同时标志位isShowText会被设定为false。

```
1. // ets/pages/RouterPage3.ets
2. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
3. import 'ets/pages/RouterPage2';

5. @Builder
6. function buildText() {
7. // @Builder中使用语法节点生成BuilderProxyNode。
8. if (true) {
9. MyComponent()
10. }
11. }

13. @Component
14. struct MyComponent {
15. @StorageLink('isShowText') isShowText: boolean = true;

17. build() {
18. if (this.isShowText) {
19. Column() {
20. Text('BuilderNode Reuse')
21. .fontSize(36)
22. .fontWeight(FontWeight.Bold)
23. .padding(16)
24. }
25. }
26. }
27. }

29. class TextNodeController extends NodeController {
30. private rootNode: FrameNode | null = null;
31. private textNode: BuilderNode<[]> | null = null;

33. makeNode(context: UIContext): FrameNode | null {
34. this.rootNode = new FrameNode(context);

36. if (AppStorage.has('textNode')) {
37. // 复用AppStorage中的BuilderNode。
38. this.textNode = AppStorage.get<BuilderNode<[]>>('textNode') as BuilderNode<[]>;
39. const parent = this.textNode.getFrameNode()?.getParent();
40. if (parent) {
41. parent.removeChild(this.textNode.getFrameNode());
42. }
43. } else {
44. this.textNode = new BuilderNode(context);
45. this.textNode.build(wrapBuilder<[]>(buildText));
46. // 将创建的BuilderNode存入AppStorage。
47. AppStorage.setOrCreate<BuilderNode<[]>>('textNode', this.textNode);
48. }
49. this.rootNode.appendChild(this.textNode.getFrameNode());

51. return this.rootNode;
52. }
53. }

55. @Entry({ routeName: 'myIndex' })
56. @Component
57. struct Index {
58. aboutToAppear(): void {
59. AppStorage.setOrCreate<boolean>('isShowText', true);
60. }

62. build() {
63. Row() {
64. Column() {
65. NodeContainer(new TextNodeController())
66. .width('100%')
67. .backgroundColor('#FFF0F0F0')
68. Button('Router pageTwo')
69. .onClick(() => {
70. // 改变AppStorage中的状态变量触发Text节点的重新创建。
71. AppStorage.setOrCreate<boolean>('isShowText', false);
72. // 将BuilderNode从AppStorage中移除。
73. AppStorage.delete('textNode');

75. this.getUIContext().getRouter().replaceNamedRoute({ name: 'pageTwo' });
76. })
77. .margin({ top: 16 })
78. }
79. .width('100%')
80. .height('100%')
81. .padding(16)
82. }
83. .height('100%')
84. }
85. }
```

[RouterPage3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/RouterPage3.ets#L16-L102)

PageTwo的实现如下：

```
1. // ets/pages/RouterPage2.ets
2. // 该页面中存在一个按钮，可跳转回主页面，回到主页面后，原有的文字消失。
3. import 'ets/pages/RouterPage1';

5. @Entry({ routeName: 'pageTwo' })
6. @Component
7. struct PageTwo {
8. build() {
9. Column() {
10. Button('Router replace to index')
11. .onClick(() => {
12. this.getUIContext().getRouter().replaceNamedRoute({ name: 'myIndex' });
13. })
14. }
15. .height('100%')
16. .width('100%')
17. .alignItems(HorizontalAlign.Center)
18. .padding(16)
19. }
20. }
```

[RouterPage2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/RouterPage2.ets#L16-L37)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/GFSpHgBdTTKbuvphOttRIA/zh-cn_image_0000002558764504.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=EC13F6CD86B1422D071C31EC2128C863C7F6BEBA8CCAAA729D344A7BFCC77509)

在API version 16之前，解决该问题的方法是在页面销毁时，将页面上的BuilderNode从缓存中移除。以上述例子为例，可以在页面跳转前，通过点击事件将BuilderNode从[AppStorage](arkts-appstorage.md)中移除，以此达到预期效果。

API version 16及之后版本，BuilderNode在新页面被复用时，会自动刷新自身内容，无需在页面销毁时将BuilderNode从缓存中移除，如下所示。

```
1. // ets/pages/RouterPage1.ets
2. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';
3. import 'ets/pages/RouterPage2';

5. @Builder
6. function buildText() {
7. // @Builder中使用语法节点生成BuilderProxyNode
8. if (true) {
9. MyComponent()
10. }
11. }

13. @Component
14. struct MyComponent {
15. @StorageLink('isShowText') isShowText: boolean = true;

17. build() {
18. if (this.isShowText) {
19. Column() {
20. Text('BuilderNode Reuse')
21. .fontSize(36)
22. .fontWeight(FontWeight.Bold)
23. .padding(16)
24. }
25. }
26. }
27. }

29. class TextNodeController extends NodeController {
30. private rootNode: FrameNode | null = null;
31. private textNode: BuilderNode<[]> | null = null;

33. makeNode(context: UIContext): FrameNode | null {
34. this.rootNode = new FrameNode(context);

36. if (AppStorage.has('textNode')) {
37. // 复用AppStorage中的BuilderNode
38. this.textNode = AppStorage.get<BuilderNode<[]>>('textNode') as BuilderNode<[]>;
39. const parent = this.textNode.getFrameNode()?.getParent();
40. if (parent) {
41. parent.removeChild(this.textNode.getFrameNode());
42. }
43. } else {
44. this.textNode = new BuilderNode(context);
45. this.textNode.build(wrapBuilder<[]>(buildText));
46. // 将创建的BuilderNode存入AppStorage
47. AppStorage.setOrCreate<BuilderNode<[]>>('textNode', this.textNode);
48. }
49. this.rootNode.appendChild(this.textNode.getFrameNode());

51. return this.rootNode;
52. }
53. }

55. @Entry({ routeName: 'myIndex' })
56. @Component
57. struct Index {
58. aboutToAppear(): void {
59. AppStorage.setOrCreate<boolean>('isShowText', true);
60. }

62. build() {
63. Row() {
64. Column() {
65. NodeContainer(new TextNodeController())
66. .width('100%')
67. .backgroundColor('#FFF0F0F0')
68. Button('Router pageTwo')
69. .onClick(() => {
70. // 改变AppStorage中的状态变量触发Text节点的重新创建
71. AppStorage.setOrCreate<boolean>('isShowText', false);

73. this.getUIContext().getRouter().replaceNamedRoute({ name: 'pageTwo' });
74. })
75. .margin({ top: 16 })
76. }
77. .width('100%')
78. .height('100%')
79. .padding(16)
80. }
81. .height('100%')
82. }
83. }
```

[RouterPage1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/RouterPage1.ets#L16-L100)

## BuilderNode中使用LocalStorage

从API version 12开始，自定义组件支持接收[LocalStorage](arkts-localstorage.md)实例。可以通过[传递LocalStorage实例](arkts-localstorage.md#自定义组件接收localstorage实例)来使用LocalStorage相关的装饰器[@LocalStorageProp](arkts-localstorage.md#localstorageprop)、[@LocalStorageLink](arkts-localstorage.md#localstoragelink)。

```
1. import { BuilderNode, NodeController, UIContext } from '@kit.ArkUI';

3. let localStorage1: LocalStorage = new LocalStorage();
4. localStorage1.setOrCreate('propA', 'propA');

6. let localStorage2: LocalStorage = new LocalStorage();
7. localStorage2.setOrCreate('propB', 'propB');

9. @Entry(localStorage1)
10. @Component
11. struct Index {
12. @LocalStorageLink('propA') propA: string = 'Hello World';
13. @State count: number = 0;
14. private controller: NodeController = new MyNodeController(this.count, localStorage2);

16. build() {
17. Row() {
18. Column() {
19. Text(this.propA)
20. .fontSize(50)
21. .fontWeight(FontWeight.Bold)
22. // 使用LocalStorage 实例localStorage2
23. Child({ count: this.count }, localStorage2)
24. NodeContainer(this.controller)
25. }
26. .id('LocalStoragePage')
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }

33. interface Params {
34. count: number;
35. localStorage: LocalStorage;
36. }

38. @Builder
39. function createChild(params: Params) {
40. // 构造过程中传递localStorage
41. Child({ count: params.count }, params.localStorage)
42. }

44. class MyNodeController extends NodeController {
45. private count?: number;
46. private localStorage ?: LocalStorage;

48. constructor(count: number, localStorage: LocalStorage) {
49. super();
50. this.count = count;
51. this.localStorage = localStorage;
52. }

54. makeNode(uiContext: UIContext): FrameNode | null {
55. let builderNode = new BuilderNode<[Params]>(uiContext);
56. // 构造过程中传递localStorage
57. builderNode.build(wrapBuilder(createChild), { count: this.count, localStorage: this.localStorage });
58. return builderNode.getFrameNode();
59. }
60. }

62. @Component
63. struct Child {
64. @Prop count: number;
65. @LocalStorageLink('propB') propB: string = 'Hello World';

67. build() {
68. Text(this.propB)
69. .fontSize(50)
70. .fontWeight(FontWeight.Bold)
71. }
72. }
```

[LocalStoragePage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/LocalStoragePage.ets#L15-L88)

## 查询当前BuilderNode是否解除引用

前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。

从API version 20开始，使用[isDisposed](../harmonyos-references/js-apis-arkui-buildernode.md#isdisposed20)接口查询当前BuilderNode对象是否已解除与后端实体节点的引用关系，从而可以在操作节点前检查其有效性，避免潜在风险。

```
1. import { NodeController, FrameNode, BuilderNode } from '@kit.ArkUI';

3. @Builder
4. function buildText() {
5. Text('Test')
6. .fontSize(20)
7. .fontWeight(FontWeight.Bold)
8. }

10. class MyNodeController extends NodeController {
11. private rootNode: FrameNode | null = null;
12. private builderNode: BuilderNode<[]> | null = null;

14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext);
16. this.rootNode.commonAttribute.width(100)
17. .height(100)
18. .backgroundColor(Color.Pink);
19. this.builderNode = new BuilderNode<[]>(uiContext);
20. this.builderNode.build(wrapBuilder<[]>(buildText));

22. // 挂载BuilderNode。
23. this.rootNode.appendChild(this.builderNode.getFrameNode());
24. return this.rootNode;
25. }

27. disposeBuilderNode() {
28. // 解除BuilderNode与后端实体节点的引用关系。
29. this.builderNode?.dispose();
30. }

32. isDisposed(): string {
33. if (this.builderNode !== null) {
34. // 查询BuilderNode是否解除引用。
35. if (this.builderNode.isDisposed()) {
36. return 'builderNode isDisposed is true';
37. } else {
38. return 'builderNode isDisposed is false';
39. }
40. }
41. return 'builderNode is null';
42. }
43. }

45. @Entry
46. @Component
47. struct Index {
48. @State text: string = '';
49. private myNodeController: MyNodeController = new MyNodeController();

51. build() {
52. Column({ space: 4 }) {
53. NodeContainer(this.myNodeController)
54. Button('BuilderNode dispose')
55. .onClick(() => {
56. this.myNodeController.disposeBuilderNode();
57. this.text = '';
58. })
59. .width(200)
60. .height(50)
61. Button('BuilderNode isDisposed')
62. .onClick(() => {
63. this.text = this.myNodeController.isDisposed();
64. })
65. .width(200)
66. .height(50)
67. Text(this.text)
68. .fontSize(25)
69. }
70. .width('100%')
71. .height('100%')
72. }
73. }
```

[IsDisposedPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/IsDisposedPage.ets#L15-L89)

## 设置BuilderNode继承冻结能力

ArkUI支持[自定义组件冻结](arkts-custom-components-freeze.md)，该功能冻结非激活状态组件的刷新能力。当组件处于非激活状态时，即便其绑定状态变量发生变化，也不会触发组件UI的重新渲染，从而减少复杂UI场景的刷新负载。

从API version 20开始，BuilderNode节点可以通过[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)接口继承父自定义组件（即从该BuilderNode节点向上查找的第一个自定义组件）的冻结策略。当BuilderNode节点继承父自定义组件的冻结策略时，若父自定义组件的冻结策略设置为开启组件冻结（即[freezeWhenInactive](../harmonyos-references/ts-custom-component-parameter.md#componentoptions)选项设为true），则BuilderNode节点在不活跃时将会冻结，当切换至活跃状态时解冻，并使用缓存的数据更新节点。

BuilderNode节点只有通过以下方式上下树时，才会根据该节点是否继承父自定义组件的冻结策略，来更新自己的冻结策略：

| 类 | 接口 |
| --- | --- |
| [FrameNode](../harmonyos-references/js-apis-arkui-framenode.md) | [appendChild](../harmonyos-references/js-apis-arkui-framenode.md#appendchild12)、[insertChildAfter](../harmonyos-references/js-apis-arkui-framenode.md#insertchildafter12)、[removeChild](../harmonyos-references/js-apis-arkui-framenode.md#removechild12)、[clearChildren](../harmonyos-references/js-apis-arkui-framenode.md#clearchildren12)、[addComponentContent](../harmonyos-references/js-apis-arkui-framenode.md#addcomponentcontent12) |
| [NodeContent](../harmonyos-references/js-apis-arkui-nodecontent.md) | [addFrameNode](../harmonyos-references/js-apis-arkui-nodecontent.md#addframenode12)、[removeFrameNode](../harmonyos-references/js-apis-arkui-nodecontent.md#removeframenode12) |
| [NodeController](../harmonyos-references/js-apis-arkui-nodecontroller.md) | [makeNode](../harmonyos-references/js-apis-arkui-nodecontroller.md#makenode) |
| [RenderNode](../harmonyos-references/js-apis-arkui-rendernode.md) | [appendChild](../harmonyos-references/js-apis-arkui-rendernode.md#appendchild)、[insertChildAfter](../harmonyos-references/js-apis-arkui-rendernode.md#insertchildafter)、[removeChild](../harmonyos-references/js-apis-arkui-rendernode.md#removechild)、[clearChildren](../harmonyos-references/js-apis-arkui-rendernode.md#clearchildren) |
| [NodeAdapter](../harmonyos-references/js-apis-arkui-framenode.md#nodeadapter12) | 节点通过[懒加载](../harmonyos-references/ts-rendering-control-lazyforeach.md)方式上下树时 |

说明

当BuilderNode节点设置为继承父自定义组件的冻结策略时，BuilderNode节点的冻结策略将与其上层最近的自定义组件或BuilderNode节点的冻结策略保持一致。

当BuilderNode节点被冻结时，调用[update](../harmonyos-references/js-apis-arkui-buildernode.md#update)接口不会触发节点的更新，等其被解冻时再更新节点。

### BuilderNode常用冻结场景（状态管理V1）

从API version 20开始，在状态管理V1中，当BuilderNode节点开启冻结（即[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)设置为true）并继承父自定义组件的冻结策略时，如果父自定义组件的冻结策略设置为开启组件冻结（即freezeWhenInactive选项设为true），则BuilderNode节点在不活跃时将会冻结。当切换至活跃状态时，节点将解冻并使用缓存的数据进行更新，示例如下。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { common } from '@kit.AbilityKit';

5. const PAGE_ONE_INDEX = 1;
6. const PAGE_TWO_INDEX = 2;

8. class Params {
9. public count: number = 0;

11. constructor(count: number) {
12. this.count = count;
13. }
14. }

16. @Builder
17. function buildText(params: Params) {

19. Column() {
20. TextBuilder({ message: params.count })
21. }
22. }

24. class TextNodeController extends NodeController {
25. private rootNode: FrameNode | null = null;
26. private textNode: BuilderNode<[Params]> | null = null;
27. private count: number = 0;

29. makeNode(context: UIContext): FrameNode | null {
30. this.rootNode = new FrameNode(context);
31. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
32. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.count));
33. this.textNode.inheritFreezeOptions(true); // 设置BuilderNode的冻结继承状态为true
34. if (this.rootNode !== null) {
35. this.rootNode.appendChild(this.textNode.getFrameNode()); // 将BuilderNode上树
36. }
37. return this.rootNode;
38. }

40. update(): void {
41. if (this.textNode !== null) {
42. this.count += 1;
43. this.textNode.update(new Params(this.count)); // 更新BuilderNode中的数据，可以触发Log
44. }

46. }
47. }

49. const textNodeController: TextNodeController = new TextNodeController();

51. @Entry
52. @Component
53. struct MyNavigationTestStack {
54. @Provide('pageInfo') pageInfo: NavPathStack = new NavPathStack();
55. @State message: number = 0;
56. @State logNumber: number = 0;

58. @Builder
59. PageMap(name: string) {
60. if (name === 'pageOne') {
61. pageOneStack({ message: this.message, logNumber: this.logNumber })
62. } else if (name === 'pageTwo') {
63. pageTwoStack({ message: this.message, logNumber: this.logNumber })
64. }
65. }

67. build() {
68. Column() {
69. Button('update builderNode') // 点击更新BuilderNode
70. .onClick(() => {
71. textNodeController.update();
72. })
73. Navigation(this.pageInfo) {
74. Column() {
75. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
76. .width('80%')
77. .height(40)
78. .margin(20)
79. .onClick(() => {
80. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈
81. })
82. }
83. }.title('NavIndex')
84. .navDestination(this.PageMap)
85. .mode(NavigationMode.Stack)
86. }
87. }
88. }

90. @Component
91. struct pageOneStack {
92. @Consume('pageInfo') pageInfo: NavPathStack;
93. @State index: number = PAGE_ONE_INDEX;
94. @Link message: number;
95. @Link logNumber: number;

97. build() {
98. NavDestination() {
99. Column() {
100. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
101. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
102. .width('80%')
103. .height(40)
104. .margin(20)
105. .onClick(() => {
106. this.pageInfo.pushPathByName('pageTwo', null);
107. })
108. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
109. .width('80%')
110. .height(40)
111. .margin(20)
112. .onClick(() => {
113. this.pageInfo.pop();
114. })
115. }.width('100%').height('100%')
116. }.title('pageOne')
117. .onBackPressed(() => {
118. this.pageInfo.pop();
119. return true;
120. })
121. }
122. }

124. @Component
125. struct pageTwoStack {
126. @Consume('pageInfo') pageInfo: NavPathStack;
127. @State index: number = PAGE_TWO_INDEX;
128. @Link message: number;
129. @Link logNumber: number;

131. build() {
132. NavDestination() {
133. Column() {
134. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
135. // 请将$r('app.string.text1')替换为实际资源文件，在本示例中该资源文件的value值为"BuilderNode处于冻结"
136. Text($r('app.string.text1'))
137. .fontWeight(FontWeight.Bold)
138. .margin({ top: 48, bottom: 48 })
139. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
140. .width('80%')
141. .height(40)
142. .margin(20)
143. .onClick(() => {
144. this.pageInfo.pop();
145. })
146. }.width('100%').height('100%')
147. }.title('pageTwo')
148. .onBackPressed(() => {
149. this.pageInfo.pop();
150. return true;
151. })
152. }
153. }

155. @Component({ freezeWhenInactive: true })
156. // 设置冻结策略为不活跃冻结
157. struct NavigationContentMsgStack {
158. @Link message: number;
159. @Link index: number;
160. @Link logNumber: number;

162. build() {
163. Column() {
164. if (this.index === 1) {
165. NodeContainer(textNodeController)
166. }
167. }
168. }
169. }

171. @Component({ freezeWhenInactive: true })
172. // 设置冻结策略为不活跃冻结
173. struct TextBuilder {
174. @Prop @Watch('info') message: number = 0;
175. private context = this.getUIContext().getHostContext() as common.UIAbilityContext;

177. info(): void {
178. hilog.info(0xF811, 'testTag', '%{public}s',
179. `freeze-test TextBuilder message callback ${this.message}`); // 根据message内容变化来打印日志来判断是否冻结
180. }

182. build() {
183. Row() {
184. Column() {
185. // 请在resources\base\element\string.json文件中配置name为'text2' ，value为非空字符串的资源
186. Text(this.context.resourceManager.getStringByNameSync('text2') + `${this.message}`)
187. .fontWeight(FontWeight.Bold)
188. .margin({ top: 48, bottom: 48 })
189. }
190. }
191. }
192. }
```

[InheritFreezeOptionsPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/InheritFreezeOptionsPage.ets#L15-L209)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/HcAIIiFQQxWTedHF3BE8bg/zh-cn_image_0000002558604848.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=1D1894965CC7597BB90BC1B9746F173D1A20D7F3336147B426AC06FF04182037)

### BuilderNode常用冻结场景（状态管理V2）

从API version 22开始，在状态管理V2中，BuilderNode冻结开启方式和在状态管理V1中的开启方式一致，当BuilderNode节点开启冻结（即[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)设置为true）并继承父自定义组件的冻结策略时，如果父自定义组件的冻结策略设置为开启组件冻结（即freezeWhenInactive选项设为true），则BuilderNode节点在不活跃时将会冻结。当切换至活跃状态时，节点将解冻并使用缓存的数据进行更新。以下示例展示了几种状态管理V2常用的BuilderNode冻结场景。

**页面路由**

当BuilderNode节点开启冻结（即[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)设置为true）并且继承父自定义组件的冻结策略设置为开启组件冻结（即freezeWhenInactive选项设为true）时，页面1调用router.pushUrl接口跳转到页面2时，页面1为隐藏不可见状态，此时如果更新页面1中的状态变量，不会触发页面1刷新。图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/ruUEEZPuSpKSVpL9mJZ2XQ/zh-cn_image_0000002589323919.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=91B6DE6CA5B1556EDBAAFF1CC767A071F6D05F9B015A8EDBFC093FCDAD47FD6A)

页面1示例代码如下：

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. @ObservedV2
4. export class Book {
5. @Trace name: string = "100";

7. constructor(name: string) {
8. this.name = name;
9. }
10. }

12. @Builder
13. function buildText(book: Book) {
14. Column() {
15. BuildNodeChild()
16. }
17. }

19. class TextNodeController extends NodeController {
20. private rootNode: FrameNode | null = null;
21. private textNode: BuilderNode<[Book]> | null = null;
22. index: number = 0;
23. name: string = "100";

25. makeNode(context: UIContext): FrameNode | null {
26. this.rootNode = new FrameNode(context);
27. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
28. this.textNode.build(wrapBuilder<[Book]>(buildText), new Book(this.name));
29. this.textNode.inheritFreezeOptions(true); // 设置BuilderNode的冻结继承状态为true。
30. if (this.rootNode !== null) {
31. this.rootNode.appendChild(this.textNode.getFrameNode()); // 将BuilderNode上树。
32. }
33. return this.rootNode;
34. }
35. }

37. const textNodeController: TextNodeController = new TextNodeController();

39. @Entry
40. @ComponentV2({ freezeWhenInactive: true })
41. export struct Index3 {
42. build() {
43. Column() {
44. NodeContainer(textNodeController)
45. }
46. }
47. }

49. @ComponentV2({ freezeWhenInactive: true })
50. struct BuildNodeChild {
51. @Local bookTest: Book = new Book("A Midsummer Night’s Dream");

53. @Monitor("bookTest.name")
54. onMessageChange(monitor: IMonitor) {
55. console.info(`The book name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
56. }

58. build() {
59. Column() {
60. Text(`Book name is  ${this.bookTest.name}`).fontSize(30)
61. Button('change')
62. .width('60%')
63. .height(40)
64. .fontSize(30)
65. .onClick(() => {
66. this.bookTest.name = "The Old Man and the Sea";
67. })
68. .margin(5)
69. Button('next').width('60%').height(40).fontSize(30)
70. .onClick(() => {
71. this.getUIContext().getRouter().pushUrl({ url: 'pages/routing' });
72. setTimeout(() => {
73. this.bookTest = new Book("Jane Austen's Pride and Prejudice");
74. }, 1000)
75. })
76. }
77. }
78. }
```

页面2-Routing2（即页面1的下一页）示例代码如下：

```
1. @Entry
2. @ComponentV2
3. struct Page2 {
4. build() {
5. Column() {
6. Text(`This is the page2`).fontSize(25)
7. Button('Back')
8. .onClick(() => {
9. this.getUIContext().getRouter().back();
10. })
11. }
12. }
13. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/nS0PCwTtT0-lewxlORofWA/zh-cn_image_0000002589324373.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=C9C6A7007D443ACC6172C676B34B044A5E67A9C7EBA172CE32488607CC345E4C)

在上面的示例中：

在页面1中点击change按钮，bookTest变量的name属性改变，@Monitor中注册的方法onMessageChange会被调用。

在页面1中点击next按钮，跳转到页面2，然后延迟1s更新状态变量bookTest。在更新bookTest的时候，已经跳转到页面2，页面1处于inactive状态，@Local装饰的状态变量bookTest将不响应更新，其@Monitor不会调用，关联的节点不会刷新。

**TabContent**

当BuilderNode节点开启冻结（即[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)设置为true）并且继承父自定义组件的冻结策略设置为开启组件冻结（即freezeWhenInactive选项设为true）时，BuilderNode的子组件在不活跃时将会冻结，当切换至活跃状态时解冻。

在首次渲染的时候，Tabs只会创建当前正在显示的TabContent，当切换全部的TabContent后，TabContent才会被全部创建。

图示如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/6KxVIphWSG2NZ8opVZYTnA/zh-cn_image_0000002589243859.png?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=37540FB70EA1F415FF9CEF3BE4E078AB9774E85DD2248BAEEC3FEE4BE2B2E1F2)

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. class Params {
4. message: number = 0;

6. constructor( message: number) {
7. this.message = message;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {
13. Column() {
14. buildNodeChild({ message: params.message});
15. }
16. }

18. class TextNodeController extends NodeController {
19. private rootNode: FrameNode | null = null;
20. private textNode: BuilderNode<[Params]> | null = null;
21. private message: number = 0;

23. makeNode(context: UIContext): FrameNode | null {
24. this.rootNode = new FrameNode(context);
25. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
26. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
27. this.textNode.inheritFreezeOptions(true); // 设置BuilderNode的冻结继承状态为true。
28. if (this.rootNode !== null) {
29. this.rootNode.appendChild(this.textNode.getFrameNode()); // 将BuilderNode上树。
30. }
31. return this.rootNode;
32. }

34. update(): void {
35. if (this.textNode !== null) {
36. this.message += 1;
37. this.textNode.update(new Params(this.message)); // 更新BuilderNode中的数据，可以触发Log。
38. }
39. }
40. }

42. const textNodeController: TextNodeController = new TextNodeController();

44. @Entry
45. @ComponentV2
46. struct TabContentTest {
47. @Local message: number = 0;
48. @Local index:number = 0;

50. build() {
51. Row() {
52. Column() {
53. Button('change message').onClick(() => {
54. textNodeController.update();
55. })
56. .fontSize(25)
57. .height(40)

59. Tabs() {
60. TabContent() {
61. Column() {
62. FreezeBuildNode({ message: this.message })
63. Text('Tabs遍历后BuilderNode处于冻结')
64. .fontWeight(FontWeight.Bold)
65. .margin({ top: 48, bottom: 48 })
66. .fontSize(30)
67. }
68. }.tabBar(`tab`+`${this.index}`)
69. TabContent() {
70. Column() {
71. FreezeBuildNode({ message: this.message })
72. }
73. }.tabBar(`tab`+`${this.index+1}`)
74. }
75. }
76. .width('100%')
77. }
78. .height('100%')
79. }
80. }

82. @ComponentV2({ freezeWhenInactive: true })
83. struct FreezeBuildNode {
84. @Param message: number = 0;
85. @Param index: number = 0;
86. @Monitor('message') onMessageUpdated(mon: IMonitor) {
87. console.info(`FreezeBuildNode message callback func ${this.message}`);
88. }
89. build() {
90. if (this.index === 0) {
91. NodeContainer(textNodeController);
92. }
93. }
94. }

96. @ComponentV2({ freezeWhenInactive: true }) // BuilderNode下面的子组件开启冻结。
97. struct buildNodeChild {
98. @Param message: number = 0;
99. @Param index: number = 0;

101. @Monitor('message') onMessageUpdated(mon: IMonitor) {
102. console.info(`FreezeBuildNode buildNodeChild message callback func ${this.message}`);
103. }

105. build() {
106. Text('message' + `${this.message}`)
107. .fontSize(40)
108. .fontWeight(FontWeight.Bold)
109. }
110. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/LUsGThKjSbavv16RVlpksA/zh-cn_image_0000002589244313.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=4211F658665966B9D63448CAF696ED0F094E20D46DE844904E499B93D809C2D2)

在上面的示例中：

1.点击change message更改message的值，当前正在显示的BuilderNode下面的子组件buildNodeChild的message属性会被更新，buildNodeChild组件中@Monitor注册的方法onMessageUpdated被触发。

2.点击tab1切换到另一个TabContent，该TabContent的状态由inactive变为active，对应的@Monitor注册的方法onMessageUpdated被触发。

3.点击tab0切换回第一个TabContent，再切换到其他TabContent后点击change message更改message的值，此时tab0冻结，tab0的@Monitor注册的方法onMessageUpdated不会被触发。

**Navigation**

Navigation组件的BuilderNode冻结功能（通过配置[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)为true）是组件冻结机制在导航场景下的延伸，核心作用是优化包含BuilderNode的Navigation组件在页面切换或状态更新时的性能，避免非活跃状态下的冗余计算和渲染。当BuilderNode所在的Navigation页面处于非活跃状态（如被切换到后台、隐藏在Tab页/侧边栏后等），系统会将其标记为 “冻结”。冻结状态下，该BuilderNode的子组件会暂停状态更新、事件响应和渲染刷新（如@State、@Prop等状态变化不会触发重新渲染，生命周期回调暂时失效）。通过配置[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)为true，BuilderNode会继承父组件（如Navigation）的冻结状态，确保其下的整个子组件树同步进入冻结状态，避免局部未冻结导致的性能浪费。

```
1. import { BuilderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. class Params {
4. count: number = 0;

6. constructor(count: number) {
7. this.count = count;
8. }
9. }

11. @Builder
12. function buildText(params: Params) {

14. Column() {
15. TextBuilder({ message: params.count });
16. }
17. }

19. class TextNodeController extends NodeController {
20. private rootNode: FrameNode | null = null;
21. private textNode: BuilderNode<[Params]> | null = null;
22. private count: number = 0;

24. makeNode(context: UIContext): FrameNode | null {
25. this.rootNode = new FrameNode(context);
26. this.textNode = new BuilderNode(context, { selfIdealSize: { width: 150, height: 150 } });
27. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.count));
28. this.textNode.inheritFreezeOptions(true); // 设置BuilderNode的冻结继承状态为true。
29. if (this.rootNode !== null) {
30. this.rootNode.appendChild(this.textNode.getFrameNode()); // 将BuilderNode上树。
31. }
32. return this.rootNode;
33. }

35. update(): void {
36. if (this.textNode !== null) {
37. this.count += 1;
38. this.textNode.update(new Params(this.count)); // 更新BuilderNode中的数据，可以触发Log。
39. }
40. }
41. }

43. const textNodeController: TextNodeController = new TextNodeController();

45. @Entry
46. @ComponentV2
47. struct MyNavigationTestStack {
48. @Provider('pageInfo') pageInfo: NavPathStack = new NavPathStack();
49. @Local message: number = 0;
50. @Local logNumber: number = 0;

52. @Builder
53. PageMap(name: string) {
54. if (name === 'pageOne') {
55. PageOneStack({ message: this.message, logNumber: this.logNumber })
56. } else if (name === 'pageTwo') {
57. PageTwoStack({ message: this.message, logNumber: this.logNumber })
58. }
59. }

61. build() {
62. Column() {
63. Button('update builderNode') // 点击更新BuilderNode。
64. .onClick(() => {
65. textNodeController.update();
66. })
67. Navigation(this.pageInfo) {
68. Column() {
69. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
70. .width('80%')
71. .height(40)
72. .margin(20)
73. .onClick(() => {
74. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。
75. })
76. }
77. }.title('NavIndex')
78. .navDestination(this.PageMap)
79. .mode(NavigationMode.Stack)
80. }
81. }
82. }

84. @ComponentV2
85. struct PageOneStack {
86. @Consumer('pageInfo') pageInfo: NavPathStack=new NavPathStack();
87. @Local index: number = 1;
88. @Param @Require  message: number;
89. @Param @Require logNumber: number;

91. build() {
92. NavDestination() {
93. Column() {
94. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
95. Button('Next Page', { stateEffect: true, type: ButtonType.Capsule })
96. .width('80%')
97. .height(40)
98. .margin(20)
99. .onClick(() => {
100. this.pageInfo.pushPathByName('pageTwo', null);
101. })
102. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
103. .width('80%')
104. .height(40)
105. .margin(20)
106. .onClick(() => {
107. this.pageInfo.pop();
108. })
109. }.width('100%').height('100%')
110. }.title('pageOne')
111. .onBackPressed(() => {
112. this.pageInfo.pop();
113. return true;
114. })
115. }
116. }

118. @ComponentV2
119. struct PageTwoStack {
120. @Consumer('pageInfo') pageInfo: NavPathStack=new NavPathStack();
121. @Local index: number = 2;
122. @Param @Require message: number;
123. @Param @Require logNumber: number;

125. build() {
126. NavDestination() {
127. Column() {
128. NavigationContentMsgStack({ message: this.message, index: this.index, logNumber: this.logNumber })
129. Text('BuilderNode处于冻结')
130. .fontWeight(FontWeight.Bold)
131. .margin({ top: 48, bottom: 48 })
132. Button('Back Page', { stateEffect: true, type: ButtonType.Capsule })
133. .width('80%')
134. .height(40)
135. .margin(20)
136. .onClick(() => {
137. this.pageInfo.pop();
138. })
139. }.width('100%').height('100%')
140. }.title('pageTwo')
141. .onBackPressed(() => {
142. this.pageInfo.pop();
143. return true;
144. })
145. }
146. }

148. @ComponentV2({ freezeWhenInactive: true }) // 设置冻结策略为不活跃冻结。
149. struct NavigationContentMsgStack {
150. @Param @Require message: number;
151. @Param @Require index: number;
152. @Param @Require logNumber: number;

154. build() {
155. Column() {
156. if (this.index === 1) {
157. NodeContainer(textNodeController);
158. }
159. }
160. }
161. }

163. @ComponentV2({ freezeWhenInactive: true }) // 设置冻结策略为不活跃冻结。
164. struct TextBuilder {
165. @Param  message: number = 0;

167. @Monitor('message')
168. info() {
169. console.info(` freeze-test TextBuilder message callback ${this.message}`); // 根据message内容变化来打印日志来判断是否冻结。
170. }
171. build() {
172. Row() {
173. Column() {
174. Text(`文本更新次数： ${this.message}`)
175. .fontWeight(FontWeight.Bold)
176. .margin({ top: 48, bottom: 48 })
177. }
178. }
179. }
180. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/o12n1jX3SSOnhpwNiYm2IQ/zh-cn_image_0000002558764506.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=92FBFDC51550C2370C503E49D59F19379697020A5087769A35E8EF37A2C68C0D)

在上面的示例中：

1.进入Pageone页面，点击update builderNode按钮更改message的值，当前正在显示的BuilderNode下面的子组件TextBuilder组件中@Monitor注册的方法info被触发。

2.点击Next Page切换到PageTwo页面，点击update builderNode按钮，因为页面属于冻结状态，@Monitor注册的方法info不会被触发。

3.点击Back Page回到PageOne页面，因为在PageTwo页面时，message的值发生了变化，@Monitor注册的方法info被触发。

**Repeat**

Repeat组件（用于循环生成子组件）的BuilderNode冻结功能（通过设置BuilderNode的[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)为true启用），是组件冻结机制在循环列表场景下的具体应用，核心目的是优化列表中重复生成的子组件在非活跃状态下的性能，减少不必要的资源消耗。当BuilderNode生成的子组件处于非活跃状态（如列表项被滚动出屏幕、父组件进入冻结状态、或整个列表不可见时），系统会将该BuilderNode及其子组件树标记为“冻结”。冻结状态下，该BuilderNode对应的列表项会暂停状态更新（如@Local、@Param等状态变化不会触发重新渲染）、事件响应（如点击、滑动等事件暂时失效）和生命周期回调，避免后台无效计算。通过[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)设置为true，BuilderNode会继承Repeat父组件的冻结状态，确保循环生成的每个子组件都能同步遵循冻结规则，避免局部未冻结导致的性能浪费。

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';

3. // 定义一个Params类，用于传递参数。
4. @ObservedV2
5. class Params {
6. // 单例模式，确保只有一个Params实例。
7. static singleton_: Params;

9. // 获取Params实例的方法。
10. static instance() {
11. if (!Params.singleton_) {
12. Params.singleton_ = new Params('');
13. }
14. return Params.singleton_;
15. }

17. // 使用@Trace装饰器装饰message、bgColor属性，以便跟踪其变化。
18. @Trace message: string = '';
19. @Trace bgColor: Color = Color.Pink;
20. index: number = 0;

22. constructor( message: string) {
23. this. message = message;
24. }
25. }

27. @Builder
28. function buildText(params: Params) {
29. Column() {
30. BuildNodeChild({ message: params.message });
31. }
32. }

34. class TextNodeController extends NodeController {
35. private textNode: BuilderNode<[Params]> | null = null;
36. private message: string = '';
37. // 构造函数接收一个message参数。
38. constructor(message: string){
39. super();
40. this.message = message;
41. }
42. // 创建并返回一个FrameNode。
43. makeNode(context: UIContext): FrameNode | null {
44. this.textNode = new BuilderNode(context);
45. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.message));
46. this.textNode.inheritFreezeOptions(true); // BuilderNode开启冻结。
47. return this.textNode.getFrameNode();
48. }
49. }

51. @Entry
52. @ComponentV2
53. export struct RepeatVirtualScrollFreeze {
54. @Local simpleList: Array<string> = [];
55. storage: Params = Params.instance();

57. aboutToAppear(): void {
58. for (let i = 0; i < 7; i++) {
59. this.simpleList.push(`item${i}`);
60. }
61. }

63. build() {
64. Column() {
65. Button('Reduce length to 5').width('60%').height(40).fontSize(25)
66. .onClick(() => {
67. this.simpleList = this.simpleList.slice(0, 5);
68. })
69. .margin(5)
70. Button('Change bgColor').width('60%').height(40).fontSize(25)
71. .onClick(() => {
72. this.storage.bgColor = this.storage.bgColor == Color.Pink ? Color.Yellow : Color.Pink;
73. })

75. List() {
76. Repeat(this.simpleList)
77. .each((obj: RepeatItem<string>) => {
78. })
79. .virtualScroll({ totalCount: this.simpleList.length })
80. .templateId(() => 'a')
81. .template('a', (ri) => {
82. FreezeBuildNode({
83. message: ri.item,
84. bgColor: this.storage.bgColor
85. })
86. }, { cachedCount: 2 })
87. }
88. .cachedCount(0)
89. .margin({top: 12, left: 180 })
90. }
91. .height('80%')
92. .justifyContent(FlexAlign.Center)
93. .margin({ top: 5 })
94. }
95. }

97. // 开启组件冻结。
98. @ComponentV2({ freezeWhenInactive: true })
99. struct FreezeBuildNode {
100. storage: Params = Params.instance();
101. @Param @Require message: string ;
102. @Param @Require bgColor: Color;
103. @Monitor('storage.bgColor')
104. onBgColorChange(monitor: IMonitor) {
105. // bgColor改变时，缓存池中组件不刷新，不会打印日志。
106. console.info(`repeat---bgColor change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
107. }
108. build() {
109. NodeContainer(new TextNodeController(this.message))
110. }
111. }

113. @ComponentV2({ freezeWhenInactive: true })
114. struct BuildNodeChild {
115. // 使用Params实例作为storage属性。
116. storage: Params = Params.instance();
117. @Param message: string = '';

119. // 使用@Monitor装饰器监听storage.message的变化。
120. @Monitor('storage.bgColor')
121. onMessageChange(monitor: IMonitor) {
122. console.info(`FreezeBuildNode buildNodeChild message callback func ${this.message}`);
123. }

125. build() {
126. Text(`[a]: ${this.message}`)
127. .fontSize(25)
128. .backgroundColor(this.storage.bgColor)
129. .margin(2)
130. }
131. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/O3_0MLeFRZ6uz40n0WiW0Q/zh-cn_image_0000002558604850.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=7A82B83C0FCB4097AE12989E4A4648FF3BD44EDA66CDA324F9A945308E0BF0F7)

在上面的示例中：

点击Reduce length to 5后，被移除的两个组件会进入Repeat缓存池，然后点击Change bgColor更改bgColor的值触发节点刷新。

开启组件冻结（freezeWhenInactive: true）和BuilderNode节点开启冻结（即[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20): true），只有剩余节点中@Monitor装饰的方法onMessageChange被触发，如示例中屏上的5个节点会刷新并打印BuilderNode子组件monitor的5条日志，缓存池中的节点则不会。

**Repeat和TabContent混用**

BuilderNode节点开启冻结功能（即通过设置[inheritFreezeOptions](../harmonyos-references/js-apis-arkui-buildernode.md#inheritfreezeoptions20)为true）后，支持与Repeat、TabContent等不同组件混合使用，示例如下：

```
1. import { BuilderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';

3. // 定义一个Params类，用于传递参数。
4. @ObservedV2
5. class Params {
6. // 单例模式，确保只有一个Params实例。
7. static singleton_: Params;

9. // 获取Params实例的方法。
10. static instance() {
11. if (!Params.singleton_) {
12. Params.singleton_ = new Params(0);
13. }
14. return Params.singleton_;
15. }

17. // 使用@Trace装饰器装饰message属性，以便跟踪其变化。
18. @Trace message: string = "Hello";
19. index: number = 0;

21. constructor(index: number) {
22. this.index = index;
23. }
24. }

26. // 定义一个buildNodeChild组件。
27. @ComponentV2({ freezeWhenInactive: true }) // BuilderNode下面的子组件开启冻结。
28. struct buildNodeChild {
29. // 使用Params实例作为storage属性。
30. storage: Params = Params.instance();
31. @Param index: number = 0;

33. // 使用@Monitor装饰器监听storage.message的变化。
34. @Monitor("storage.message")
35. onMessageChange(monitor: IMonitor) {
36. console.info(`FreezeBuildNode buildNodeChild message callback func ${this.storage.message}, index:${this.index}`);
37. }

39. build() {
40. Text(`buildNode Child message: ` +`\n` + `${this.storage.message}`).fontSize(30)
41. }
42. }

44. // 定义一个buildText函数。
45. @Builder
46. function buildText(params: Params) {
47. Column() {
48. buildNodeChild({ index: params.index })
49. }
50. }

52. class TextNodeController extends NodeController {
53. private textNode: BuilderNode<[Params]> | null = null;
54. private index: number = 0;

56. // 构造函数接收一个index参数。
57. constructor(index: number) {
58. super();
59. this.index = index;
60. }

62. // 创建并返回一个FrameNode。
63. makeNode(context: UIContext): FrameNode | null {
64. this.textNode = new BuilderNode(context);
65. this.textNode.build(wrapBuilder<[Params]>(buildText), new Params(this.index));
66. this.textNode.inheritFreezeOptions(true); // BuilderNode开启冻结。
67. return this.textNode.getFrameNode();
68. }
69. }

71. // 定义一个Index组件。
72. @Entry
73. @ComponentV2
74. export struct RepeatTab {
75. // 使用Params实例作为storage属性。
76. storage: Params = Params.instance();
77. private data: number[] = [0, 1];

79. build() {
80. Row() {
81. Column() {
82. Button("change").width('80%').height(40).fontSize(30)
83. .onClick(() => {
84. this.storage.message += 'a';
85. })

87. Tabs() {
88. // 使用Repeat重复渲染TabContent组件。
89. Repeat<number>(this.data)
90. .each((obj: RepeatItem<number>) => {
91. TabContent() {
92. FreezeBuildNode({ index: obj.item })
93. .margin({ top:20,bottom:5,left:5,right:5 })
94. }.tabBar(`tab${obj.item}`)
95. })
96. .key((item: number) => item.toString())
97. }
98. }
99. }
100. .width('100%')
101. .height('100%')
102. }
103. }

105. // 定义一个FreezeBuildNode组件。
106. @ComponentV2({ freezeWhenInactive: true })
107. struct FreezeBuildNode {
108. // 使用Params实例作为storage属性。
109. storage: Params = Params.instance();
110. @Param index: number = 0;

112. // 使用@Monitor装饰器监听storage.message的变化。
113. @Monitor("storage.message")
114. onMessageChange(monitor: IMonitor) {
115. console.info(`FreezeBuildNode message callback func ${this.storage.message}, index: ${this.index}`);
116. }

118. build() {
119. NodeContainer(new TextNodeController(this.index))
120. .width('100%')
121. .height('100%')
122. }
123. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/5mWf_ikmTgqZXpGXMNw3vA/zh-cn_image_0000002589324375.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052817Z&HW-CC-Expire=86400&HW-CC-Sign=6A1ABCC5BF5A84580689485A9F5C49155B96C0502BDC6BC71398481DBFC243AC)

在上面的示例中：

1.点击change更改message的值，当前正在显示的BuilderNode下面的子组件buildNodeChild组件中@Monitor注册的方法onMessageUpdated被触发。

2.点击tab1切换到另外的TabContent，该TabContent的状态由inactive变为active，对应的BuilderNode下面的子组件buildNodeChild组件中@Monitor注册的方法onMessageUpdated被触发。

3.再次点击change更改message的值，仅当前显示的TabContent子组件中@Monitor注册的方法onMessageUpdated被触发。其他inactive的TabContent组件不会触发@Monitor。

## 设置BuilderNode支持内部@Consume接收外部的@Provide数据（状态管理V1）

从API version 20开始，通过配置BuildOptions参数，BuilderNode内部自定义组件的[@Consume](arkts-provide-and-consume.md)支持接收所在页面的[@Provide](arkts-provide-and-consume.md)数据。

参见[示例代码](../harmonyos-references/js-apis-arkui-buildernode.md#示例5buildernode支持内部consume接收外部的provide数据)。

## 设置BuilderNode支持内部@Consumer接收外部的@Provider数据（状态管理V2）

从API version 23开始，通过配置BuildOptions参数，BuilderNode内部自定义组件的[@Consumer](arkts-new-provider-and-consumer.md)支持接收所在页面的[@Provider](arkts-new-provider-and-consumer.md)数据。

参见[示例代码](../harmonyos-references/js-apis-arkui-buildernode.md#示例6buildernode支持内部consumer接收外部的provider数据)。

## BuilderNode结合ArkWeb组件实现预渲染页面

预渲染适用于Web页面启动与跳转等场景。通过结合BuilderNode，可以将ArkWeb组件提前进行离线预渲染，组件不会即时挂载至页面，而是在需要时通过NodeController动态挂载与显示。此举能够提高页面切换的流畅度及用户体验。

说明

访问在线网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](declare-permissions.md)。

1. 创建载体Ability，并创建Web组件。

   ```
   1. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { createNWeb } from '../Common/CommonIndex';
   3. import { hilog } from '@kit.PerformanceAnalysisKit';
   4. import { window } from '@kit.ArkUI';

   6. const DOMAIN = 0x0000;

   8. export default class EntryAbility extends UIAbility {
   9. // ···

   11. onWindowStageCreate(windowStage: window.WindowStage): void {
   12. // Main window is created, set main page for this ability
   13. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   15. windowStage.loadContent('pages/Index', (err) => {
   16. createNWeb('', windowStage.getMainWindowSync().getUIContext());
   17. if (err.code) {
   18. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
   19. return;
   20. }
   21. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
   22. });
   23. }

   25. // ···
   26. }
   ```

   [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/entryability/EntryAbility.ets#L16-L70)
2. 创建NodeContainer和对应的NodeController，渲染后台Web组件。

   ```
   1. import { UIContext } from '@kit.ArkUI';
   2. import { webview } from '@kit.ArkWeb';
   3. import { NodeController, BuilderNode, Size, FrameNode } from '@kit.ArkUI';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';

   6. // @Builder中为动态组件的具体组件内容。
   7. // Data为入参封装类。
   8. class Data {
   9. public url: string = '';
   10. public controller: WebviewController = new webview.WebviewController();
   11. }

   13. // 通过布尔变量shouldInactive控制网页在后台完成预渲染后停止渲染。
   14. let shouldInactive: boolean = true;

   16. @Builder
   17. function webBuilder(data: Data) {
   18. Column() {
   19. Web({ src: data.url, controller: data.controller })
   20. .onPageBegin(() => {
   21. // 调用onActive，开启渲染。
   22. data.controller.onActive();
   23. })
   24. .onFirstMeaningfulPaint(() => {
   25. if (!shouldInactive) {
   26. return;
   27. }
   28. // 在预渲染完成时触发，停止渲染。
   29. data.controller.onInactive();
   30. shouldInactive = false;
   31. })
   32. .width('100%')
   33. .height('100%')
   34. }
   35. }

   37. let wrap = wrapBuilder<Data[]>(webBuilder);

   39. // 用于控制和反馈对应的NodeContainer上的节点的行为，需要与NodeContainer一起使用。
   40. export class MyNodeController2 extends NodeController {
   41. private rootnode: BuilderNode<Data[]> | null = null;

   43. // 必须要重写的方法，用于构建节点数、返回节点挂载在对应NodeContainer中。
   44. // 在对应NodeContainer创建的时候调用、或者通过rebuild方法调用刷新。
   45. makeNode(uiContext: UIContext): FrameNode | null {
   46. hilog.info(0xF811, 'testTag', '%{public}s', ' uicontext is undefined :' + (uiContext === undefined));
   47. if (this.rootnode != null) {
   48. // 返回FrameNode节点。
   49. return this.rootnode.getFrameNode();
   50. }
   51. // 返回null控制动态组件脱离绑定节点。
   52. return null;
   53. }

   55. // 当布局大小发生变化时进行回调。
   56. aboutToResize(size: Size) {
   57. hilog.info(0xF811, 'testTag', '%{public}s', 'aboutToResize   width   : ' + size.width + ' height : ' + size.height);
   58. }

   60. // 当controller对应的NodeContainer在Appear的时候进行回调。
   61. aboutToAppear() {
   62. hilog.info(0xF811, 'testTag', '%{public}s', 'aboutToAppear');
   63. // 切换到前台后，不需要停止渲染。
   64. shouldInactive = false;
   65. }

   67. // 当controller对应的NodeContainer在Disappear的时候进行回调。
   68. aboutToDisappear() {
   69. hilog.info(0xF811, 'testTag', '%{public}s', 'aboutToDisappear');
   70. }

   72. // 此函数为自定义函数，可作为初始化函数使用。
   73. // 通过UIContext初始化BuilderNode，再通过BuilderNode中的build接口初始化@Builder中的内容。
   74. initWeb(url: string, uiContext: UIContext, control: WebviewController) {
   75. if (this.rootnode != null) {
   76. return;
   77. }
   78. // 创建节点，需要uiContext。
   79. this.rootnode = new BuilderNode(uiContext);
   80. // 创建动态Web组件。
   81. this.rootnode.build(wrap, { url: url, controller: control });
   82. }
   83. }

   85. // 创建Map保存所需要的NodeController。
   86. let nodeMap: Map<string, MyNodeController2 | undefined> = new Map();
   87. // 创建Map保存所需要的WebViewController。
   88. let controllerMap: Map<string, WebviewController | undefined> = new Map();

   90. // 初始化需要UIContext 需在Ability获取。
   91. export const createNWeb = (url: string, uiContext: UIContext) => {
   92. // 创建NodeController。
   93. let baseNode = new MyNodeController2();
   94. let controller = new webview.WebviewController();
   95. // 初始化自定义Web组件。
   96. baseNode.initWeb(url, uiContext, controller);
   97. controllerMap.set(url, controller);
   98. nodeMap.set(url, baseNode);
   99. }

   101. // 自定义获取NodeController接口。
   102. export const getNWeb = (url: string): MyNodeController2 | undefined => {
   103. return nodeMap.get(url);
   104. }
   ```

   [CommonIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/Common/CommonIndex.ets#L18-L111)
3. 通过NodeContainer使用已经预渲染的页面。

   ```
   1. // 使用NodeController的Page页。
   2. // pages/ArkWebPage.ets
   3. import { createNWeb, getNWeb } from '../Common/CommonIndex';

   5. @Entry
   6. @Component
   7. struct Index {
   8. build() {
   9. Row() {
   10. Column() {
   11. // NodeContainer用于与NodeController节点绑定，rebuild会触发makeNode。
   12. // Page页通过NodeContainer接口绑定NodeController，实现动态组件页面显示。
   13. NodeContainer(getNWeb(''))
   14. .height('90%')
   15. .width('100%')
   16. .id('ArkWebPage')
   17. }
   18. .width('100%')
   19. }
   20. .height('100%')
   21. }
   22. }
   ```

   [ArkWebPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/BuilderNode/entry/src/main/ets/pages/ArkWebPage.ets#L15-L38)
