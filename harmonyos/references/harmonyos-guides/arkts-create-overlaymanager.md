---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-overlaymanager
title: 设置浮层（OverlayManager）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 设置浮层（OverlayManager）
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5baa48f11ec5eb4805a2547400176a13e1b62d23ebee0a9aa19b447b1ceb91c6
---

浮层（OverlayManager）用于在页面（Page）之上展示自定义的UI内容，位于Dialog、Popup、Menu、BindSheet、BindContentCover和Toast等组件之下，展示范围为当前窗口的安全区内，适用于常驻悬浮等场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/dhcFI2sDTiqroLYZxCaVqA/zh-cn_image_0000002589324285.png?HW-CC-KV=V1&HW-CC-Date=20260429T052759Z&HW-CC-Expire=86400&HW-CC-Sign=9D9E9AEE53D83B9748C215BE38C55BFB1AC2C0B8603710F2C132BD09BFC76951)

可以通过使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getOverlayManager](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getoverlaymanager12)方法获取当前UI上下文关联的[OverlayManager](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md)对象，再通过该对象调用对应方法。

## 规格约束

* OverlayManager上节点的层级在Page页面层级之上，在Dialog、Popup、Menu、BindSheet、BindContentCover和Toast等组件之下。
* OverlayManager添加的节点显示和消失时没有默认动画。
* OverlayManager上节点安全区域内外的绘制方式与Page一致，键盘避让方式与Page一致。
* 推荐使用AppStorage存储与OverlayManager相关的属性，以避免页面切换时属性值变化导致业务错误。
* 当使用API version 19以下版本时，OverlayManager不支持侧滑（左滑/右滑）关闭，需在[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)中添加OverlayManager关闭的逻辑。API 19及以上版本可通过配置[OverlayManagerOptions](../harmonyos-references/arkts-apis-uicontext-i.md#overlaymanageroptions15)中的enableBackPressedEvent属性设置OverlayManager是否响应侧滑手势。
* OverlayManager中的事件机制优先被[WrappedBuilder](arkts-wrapbuilder.md)装饰的组件接收。若需实现浮层底部接收事件，可通过设置[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)为HitTestMode.Transparent将事件传递至底层。

## 设置浮层

在OverlayManager上[新增指定节点（addComponentContent）](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md#addcomponentcontent12)、[删除指定节点（removeComponentContent）](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md#removecomponentcontent12)、[显示所有节点（showAllComponentContents）](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md#showallcomponentcontents12)和[隐藏所有节点（hideAllComponentContents）](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md#hideallcomponentcontents12)。

```
1. import { ComponentContent, OverlayManager } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[Sample_dialogproject]';
5. const DOMAIN: number = 0xFF00;

7. class Params {
8. public text: string = '';
9. public offset: Position;

11. constructor(text: string, offset: Position) {
12. this.text = text;
13. this.offset = offset;
14. }
15. }

17. @Builder
18. function builderText(params: Params) {
19. Column() {
20. Text(params.text)
21. .fontSize(30)
22. .fontWeight(FontWeight.Bold)
23. }.offset(params.offset)
24. }

26. @Entry
27. @Component
28. export struct OverlayManagerComponent {
29. @State message: string = 'ComponentContent';
30. private uiContext: UIContext = this.getUIContext();
31. private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
32. @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
33. @StorageLink('componentContentIndex') componentContentIndex: number = 0;
34. @StorageLink('arrayIndex') arrayIndex: number = 0;
35. @StorageLink('componentOffset') componentOffset: Position = { x: 0, y: 30 };

37. build() {
38. // ...
39. Column({ space: 10 }) {
40. Button('Increment componentContentIndex:' + this.componentContentIndex)
41. .onClick(() => {
42. ++this.componentContentIndex;
43. })
44. Button('Decrement componentContentIndex:' + this.componentContentIndex)
45. .onClick(() => {
46. --this.componentContentIndex;
47. })
48. Button('Add ComponentContent:' + this.contentArray.length)
49. .onClick(() => {
50. let componentContent = new ComponentContent(
51. this.uiContext, wrapBuilder<[Params]>(builderText),
52. new Params(this.message + (this.contentArray.length), this.componentOffset)
53. )
54. this.contentArray.push(componentContent);
55. this.overlayNode.addComponentContent(componentContent, this.componentContentIndex);
56. })
57. Button('Increment arrayIndex:' + this.arrayIndex)
58. .onClick(() => {
59. ++this.arrayIndex;
60. })
61. Button('Decrement arrayIndex:' + this.arrayIndex)
62. .onClick(() => {
63. --this.arrayIndex;
64. })
65. Button('Delete ComponentContent:' + this.arrayIndex)
66. .onClick(() => {
67. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
68. let componentContent = this.contentArray.splice(this.arrayIndex, 1);
69. this.overlayNode.removeComponentContent(componentContent.pop());
70. } else {
71. hilog.info(DOMAIN, TAG, '%{public}s', 'arrayIndex error');
72. }
73. })
74. Button('Show ComponentContent:' + this.arrayIndex)
75. .onClick(() => {
76. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
77. let componentContent = this.contentArray[this.arrayIndex];
78. this.overlayNode.showComponentContent(componentContent);
79. } else {
80. hilog.info(DOMAIN, TAG, '%{public}s', 'arrayIndex error');
81. }
82. })
83. Button('Hide ComponentContent:' + this.arrayIndex)
84. .onClick(() => {
85. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
86. let componentContent = this.contentArray[this.arrayIndex];
87. this.overlayNode.hideComponentContent(componentContent);
88. } else {
89. hilog.info(DOMAIN, TAG, '%{public}s', 'arrayIndex error');
90. }
91. })
92. Button('Show All ComponentContent')
93. .onClick(() => {
94. this.overlayNode.showAllComponentContents();
95. })
96. Button('Hide All ComponentContent')
97. .onClick(() => {
98. this.overlayNode.hideAllComponentContents();
99. })

101. Button('Go')
102. .onClick(() => {
103. this.getUIContext().getRouter().pushUrl({
104. url: 'pages/Second'
105. })
106. })
107. }
108. .width('100%')
109. .height('100%')
110. // ...
111. }
112. }
```

[OverlayManagerComponent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/OverlayManager/OverlayManagerComponent.ets#L16-L136)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/rDj-E1EIQZ6KXAKaiIBU7g/zh-cn_image_0000002589244225.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052759Z&HW-CC-Expire=86400&HW-CC-Sign=48512132D992C6E75B7847E6CD2BEAAC3E116EBE9B510BD6C8763CAFE03C05AE)

显示一个始终在屏幕左侧的悬浮球，点击可以弹出alertDialog弹窗。

```
1. import { ComponentContent, OverlayManager } from '@kit.ArkUI';

3. class Params {
4. public context: UIContext;
5. public offset: Position;
6. constructor(context: UIContext, offset: Position) {
7. this.context = context;
8. this.offset = offset;
9. }
10. }
11. @Builder
12. function builderOverlay(params: Params) {
13. Column() {
14. Stack(){
15. }.width(50).height(50).backgroundColor(Color.Yellow).position(params.offset).borderRadius(50)
16. .onClick(() => {
17. params.context.showAlertDialog(
18. {
19. title: 'title',
20. message: 'Text',
21. autoCancel: true,
22. alignment: DialogAlignment.Center,
23. gridCount: 3,
24. confirm: {
25. value: 'Button',
26. action: () => {}
27. },
28. cancel: () => {}
29. }
30. )
31. })
32. }.focusable(false).width('100%').height('100%').hitTestBehavior(HitTestMode.Transparent)
33. }

35. @Entry
36. @Component
37. export struct OverlayManagerAlertDialog {
38. private uiContext: UIContext = this.getUIContext();
39. private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
40. private overlayContent:ComponentContent<Params>[] = [];
41. controller: TextInputController = new TextInputController();

43. aboutToAppear(): void {
44. let uiContext = this.getUIContext();
45. let componentContent = new ComponentContent(
46. this.uiContext, wrapBuilder<[Params]>(builderOverlay),
47. new Params(uiContext, {x:0, y: 100})
48. );
49. this.overlayNode.addComponentContent(componentContent, 0);
50. this.overlayContent.push(componentContent);
51. }

53. aboutToDisappear(): void {
54. let componentContent = this.overlayContent.pop();
55. this.overlayNode.removeComponentContent(componentContent);
56. }

58. build() {
59. // ...
60. Column() {

62. }
63. .width('100%')
64. .height('100%')
65. // ...
66. }
67. }
```

[OverlayManagerAlertDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/OverlayManager/OverlayManagerAlertDialog.ets#L16-L91)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/NTbrXnWjRuOOD9L1Vw3PVA/zh-cn_image_0000002558764418.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052759Z&HW-CC-Expire=86400&HW-CC-Sign=ECD5A88F6B9A2ADFDB108253AEBE93432BFCC21088B71ED54BC08E27CEB1251B)

从API version 18开始，可以通过调用UIContext中getOverlayManager方法获取OverlayManager对象，并利用该对象在指定层级上新增指定节点（[addComponentContentWithOrder](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md#addcomponentcontentwithorder18)），层次高的浮层会覆盖在层级低的浮层之上。

```
1. import { ComponentContent, LevelOrder, OverlayManager } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[Sample_dialogproject]';
5. const DOMAIN: number = 0xFF00;

7. class Params {
8. public text: string = '';
9. public offset: Position;

11. constructor(text: string, offset: Position) {
12. this.text = text;
13. this.offset = offset;
14. }
15. }

17. @Builder
18. function builderTopText(params: Params) {
19. Column() {
20. Stack() {
21. Text(params.text)
22. .fontSize(30)
23. .fontWeight(FontWeight.Bold)
24. }
25. .width(300)
26. .height(200)
27. .padding(5)
28. .backgroundColor('#F7F7F7')
29. .alignContent(Alignment.Top)
30. }.offset(params.offset)
31. }

33. @Builder
34. function builderNormalText(params: Params) {
35. Column() {
36. Stack() {
37. Text(params.text)
38. .fontSize(30)
39. .fontWeight(FontWeight.Bold)
40. }
41. .width(300)
42. .height(400)
43. .padding(5)
44. .backgroundColor('#D5D5D5')
45. .alignContent(Alignment.Top)
46. }.offset(params.offset)
47. }

49. @Entry
50. @Component
51. export struct OverlayManagerWithOrder {
52. private ctx: UIContext = this.getUIContext();
53. private overlayManager: OverlayManager = this.ctx.getOverlayManager();
54. @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
55. @StorageLink('componentContentIndex') componentContentIndex: number = 0;
56. @StorageLink('arrayIndex') arrayIndex: number = 0;
57. @StorageLink('componentOffset') componentOffset: Position = { x: 0, y: 80 };

59. build() {
60. // ...
61. Row() {
62. Column({ space: 5 }) {
63. Button('Open Top-Level Dialog Box')
64. .onClick(() => {
65. let componentContent = new ComponentContent(
66. this.ctx, wrapBuilder<[Params]>(builderTopText),
67. new Params('I am a top-level dialog box', this.componentOffset)
68. );
69. this.contentArray.push(componentContent);
70. this.overlayManager.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100000));
71. })
72. Button('Open Normal Dialog Box')
73. .onClick(() => {
74. let componentContent = new ComponentContent(
75. this.ctx, wrapBuilder<[Params]>(builderNormalText),
76. new Params('I am a normal dialog box', this.componentOffset)
77. );
78. this.contentArray.push(componentContent);
79. this.overlayManager.addComponentContentWithOrder(componentContent, LevelOrder.clamp(0));
80. })
81. Button('Remove Dialog Box').onClick(() => {
82. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
83. let componentContent = this.contentArray.splice(this.arrayIndex, 1);
84. this.overlayManager.removeComponentContent(componentContent.pop());
85. } else {
86. hilog.info(DOMAIN, TAG, '%{public}s', 'arrayIndex error');
87. }
88. })
89. }.width('100%')
90. }
91. // ...
92. }
93. }
```

[OverlayManagerWithOrder.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/OverlayManager/OverlayManagerWithOrder.ets#L16-L117)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/u8XKBk7mQyGScqL81ia2Pw/zh-cn_image_0000002558604762.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052759Z&HW-CC-Expire=86400&HW-CC-Sign=B5D38FCE1288E6BE15BF9C40B4FB32C95F95D873BC75D2EC8A420995191032ED)
