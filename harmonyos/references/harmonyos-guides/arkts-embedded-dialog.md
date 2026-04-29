---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-embedded-dialog
title: 页面级弹出框
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 页面级弹出框
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f74d05665f56ee2b087339d5c125fd1e2970d8c981feb8836158293a786606c0
---

ArkUI的弹出框默认设置为全局级别，弹窗节点作为页面根节点的子节点，显示层级高于应用中的所有路由/导航页面。当页面内进行路由跳转时，如果应用未主动调用close方法关闭弹出框，弹出框不会自动关闭，并且会在下一个跳转页面上继续显示。

从API version 15开始，如果开发者希望在路由跳转后，弹出框能够随前一个路由页面的切换而消失，并在路由返回后弹出框能够继续正常显示，可以通过页面级弹出框来实现。

说明

当且仅当弹出框为非子窗模式时，页面级能力才会生效。即showInSubWindow参数不设置或设置为false。

页面级弹出框通常与导航路由能力结合使用，可以参考[组件导航和页面路由概述](arkts-navigation-introduction.md)了解相关术语。

页面级弹出框的使用方式是在当前弹出框的入参之中新增了相关属性能力，使用前可以通过[弹出框概述](arkts-base-dialog-overview.md)了解基础的弹出框使用方法。

## 设置参数

说明

详细变量定义请参考[完整示例](arkts-embedded-dialog.md#完整示例)。

在弹出框的options入参中设置[levelMode](../harmonyos-references/js-apis-promptaction.md#levelmode15枚举说明)属性，值为LevelMode.EMBEDDED表示开启页面级弹出框能力。

当弹出框弹出时，会自动获取当前显示的Page页面并将弹出框节点挂载在此页面下。此时弹出框的显示层级高于此Page页面下的所有Navigation页面。

```
1. this.getUIContext().getPromptAction().openCustomDialog({
2. builder: () => {
3. this.customDialogComponent();
4. },
5. levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
6. // ···
7. })
```

如果希望弹出框显示在某个指定页面内，需通过第二个参数[levelUniqueId](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)来实现。此参数接收页面内的节点id，设置后，弹出框显示时会自动查询此id对应的节点所在的[Navigation](../harmonyos-references/ts-basic-components-navigation.md)页面，并将其挂载在子页面的[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)节点下。

说明

* 当levelMode参数设置为LevelMode.EMBEDDED，但是levelUniqueId传入的ID无法正确找到节点时，页面级能力不生效。如果levelUniqueId所映射的节点存在但向上遍历不存在NavDestination节点则会将弹出框节点挂载在Page节点下。
* levelUniqueId必须传入[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md#framenode-1)的uniqueId，建议使用FrameNode的[getUniqueId](../harmonyos-references/js-apis-arkui-framenode.md#getuniqueid12)方法获取uniqueId。

如下代码示例所示，Text节点为指定页面的节点，设置自定义id后，通过[getFrameNodeById](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getframenodebyid12)方法获取该节点，再通过[getUniqueId](../harmonyos-references/js-apis-arkui-framenode.md#getuniqueid12)获取节点的内部id，并将其作为levelUniqueId的值传入。

```
1. Text(this.message).id('test_text')
2. .onClick(() => {
3. const node: FrameNode | null = this.getUIContext().getFrameNodeById('test_text') || null;
4. this.getUIContext().getPromptAction().openCustomDialog({
5. builder: () => {
6. this.customDialogComponent();
7. },
8. // ···
9. levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
10. levelUniqueId: node?.getUniqueId(), // 设置页面级弹出框所在页面的任意节点ID
11. })
12. .then((dialogId: number) => {
13. customDialogId = dialogId;
14. });
15. })
```

如果弹出框配置了蒙层，蒙层的遮盖范围会根据页面层级的变化进行调整，默认遮罩范围为弹出框父节点的显示区域（Page页面或者Navigation页面）。此时，状态栏和导航条不会被蒙层遮挡。若希望遮挡状态栏和导航条，可将[immersiveMode](../harmonyos-references/js-apis-promptaction.md#immersivemode15枚举说明)参数的值设为ImmersiveMode.EXTEND。

```
1. Text(this.message).id('test_text')
2. .fontSize(50)
3. .fontWeight(FontWeight.Bold)
4. .onClick(() => {
5. const node: FrameNode | null = this.getUIContext().getFrameNodeById('test_text') || null;
6. this.getUIContext().getPromptAction().openCustomDialog({
7. builder: () => {
8. this.customDialogComponent();
9. },
10. levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
11. levelUniqueId: node?.getUniqueId(), // 设置页面级弹出框所在页面的任意节点ID
12. immersiveMode: ImmersiveMode.EXTEND, // 设置页面级弹出框蒙层的显示模式
13. })
14. .then((dialogId: number) => {
15. customDialogId = dialogId;
16. });
17. })
```

[PageLevelDialogBox.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/pageleveldialogbox/PageLevelDialogBox.ets#L53-L77)

## 交互说明

页面内弹出框在部分交互逻辑上依然遵循部分弹出框指定的交互策略：

1. 侧滑时先关闭弹出框。通过侧滑手势返回上一页时，如果页面上存在弹出框，弹出框会优先关闭并结束本次手势行为。如果期望返回上一页，需要再次触发侧滑手势。
2. 点击弹出框的蒙层，默认会关闭弹出框，点击蒙层以外的区域则不会。

## 完整示例

下述示例为基于Router路由模式下的页面级弹出框。

```
1. import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

3. let customDialogId: number = 0;

5. @Builder
6. function customDialogBuilder(uiContext: UIContext) {
7. Column() {
8. Text('Custom dialog Message').fontSize(20).height(100)
9. Row() {
10. Button('Next').onClick(() => {
11. // 在弹窗内部进行路由跳转。
12. uiContext.getRouter().pushUrl({ url: 'pages/Next' });
13. })
14. Blank().width(50)
15. Button('Close').onClick(() => {
16. uiContext.getPromptAction().closeCustomDialog(customDialogId);
17. })
18. }
19. }.padding(20)
20. }

22. @Entry
23. @Component
24. export struct PageLevelDialogBox {
25. @State message: string = 'Hello World';
26. private uiContext: UIContext = this.getUIContext();

28. @Builder
29. customDialogComponent() {
30. customDialogBuilder(this.uiContext);
31. }

33. build() {
34. NavDestination() {
35. Row() {
36. Column() {
37. Text(this.message).id('test_text')
38. .fontSize(50)
39. .fontWeight(FontWeight.Bold)
40. .onClick(() => {
41. const node: FrameNode | null = this.getUIContext().getFrameNodeById('test_text') || null;
42. this.getUIContext().getPromptAction().openCustomDialog({
43. builder: () => {
44. this.customDialogComponent();
45. },
46. levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
47. levelUniqueId: node?.getUniqueId(), // 设置页面级弹出框所在页面的任意节点ID
48. immersiveMode: ImmersiveMode.EXTEND, // 设置页面级弹出框蒙层的显示模式
49. })
50. .then((dialogId: number) => {
51. customDialogId = dialogId;
52. });
53. })
54. }
55. .width('100%')
56. }
57. .height('100%')
58. }
59. }
60. }
```

```
1. // Next.ets
2. @Entry
3. @Component
4. struct Next {
5. @State message: string = 'Back';

7. build() {
8. Row() {
9. Column() {
10. Button(this.message)
11. .fontSize(20)
12. .fontWeight(FontWeight.Bold)
13. .onClick(() => {
14. this.getUIContext().getRouter().back();
15. })
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }
```

[Next.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/pageleveldialogbox/Next.ets#L16-L38)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/AfWdqZ2kR6uRH7ckIoDG4Q/zh-cn_image_0000002558604742.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052753Z&HW-CC-Expire=86400&HW-CC-Sign=EFA62CA0293764EFF12C06D515480958B7C0E24614AA8A4DCB9DB828B28EA30E)

下述示例为基于Navigation导航模式下的页面级弹出框。使用本示例前需要参考[Navigation使用NavDestination作为导航页](../harmonyos-references/ts-basic-components-navigation.md#示例16navigation使用navdestination作为导航页)文档完成Index首页和router\_map.json的创建与配置。并使用下述示例代码中的PageLevelDialogInNavigation和PageLevelDialogInNavigationTestTwo组件替换Navigation参考文档中的PageHome和PageOne组件。

```
1. import { LevelMode, ImmersiveMode } from '@kit.ArkUI';

3. let customDialogId: number = 0;

5. @Builder
6. function customDialogBuilder(uiContext: UIContext, stack: NavPathStack | undefined) {
7. Column() {
8. Text('Custom dialog Message').fontSize(20).height(100)
9. Row() {
10. Button('Next').onClick(() => {
11. // 在弹窗内部进行路由跳转。
12. if (stack) {
13. stack.pushPath({ name: 'Custom_ROUTE_PREFIX/PageLevelDialogInNavigationPageTwo'})
14. }
15. })
16. Blank().width(50)
17. Button('Close').onClick(() => {
18. uiContext.getPromptAction().closeCustomDialog(customDialogId);
19. })
20. }
21. }.padding(20)
22. }

24. @Component
25. export struct PageLevelDialogInNavigation {
26. @State info: string = '';
27. private stack: NavPathStack | undefined = undefined;
28. private uiContext: UIContext = this.getUIContext();
29. @State message: string = 'Hello World';

31. @Builder
32. customDialogComponent() {
33. customDialogBuilder(this.uiContext, this.stack);
34. }

36. build() {
37. NavDestination() {
38. Stack({alignContent: Alignment.Center}) {
39. Column() {
40. Text(this.message).id('test_text')
41. .fontSize(50)
42. .fontWeight(FontWeight.Bold)
43. .onClick(() => {
44. const node: FrameNode | null = this.getUIContext().getFrameNodeById('test_text') || null;
45. this.uiContext.getPromptAction().openCustomDialog({
46. builder: () => {
47. this.customDialogComponent();
48. },
49. levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
50. levelUniqueId: node?.getUniqueId(), // 设置页面级弹出框所在页面的任意节点ID
51. immersiveMode: ImmersiveMode.EXTEND, // 设置页面级弹出框蒙层的显示模式
52. }).then((dialogId: number) => {
53. customDialogId = dialogId;
54. })
55. })
56. }
57. .width('100%')
58. }.width('100%').height('100%')
59. }
60. .width('100%').height('100%')
61. .title('PageOne')
62. .onReady((ctx: NavDestinationContext) => {
63. this.stack = ctx.pathStack;
64. })
65. }
66. }

68. @Component
69. export struct PageLevelDialogInNavigationTestTwo {
70. @State message: string = 'Back';
71. private stack: NavPathStack | undefined = undefined;

73. build() {
74. NavDestination() {
75. Stack({alignContent: Alignment.Center}) {
76. Column() {
77. Button(this.message)
78. .fontSize(20)
79. .fontWeight(FontWeight.Bold)
80. .onClick(() => {
81. if (this.stack) {
82. this.stack.pop()
83. }
84. })
85. }
86. .width('100%')
87. }.width('100%').height('100%')
88. }
89. .width('100%').height('100%')
90. .title('PageTwo')
91. .onReady((ctx: NavDestinationContext) => {
92. this.stack = ctx.pathStack;
93. })
94. }
95. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/94baSOxiTg6c9hSXWHa11w/zh-cn_image_0000002589324267.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052753Z&HW-CC-Expire=86400&HW-CC-Sign=117114C2FA2922365F2F3A76C2E8A2A53345C948B4CBDDB38F34470F0D95D5DA)
