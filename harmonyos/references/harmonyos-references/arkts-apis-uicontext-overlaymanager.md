---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-overlaymanager
title: Class (OverlayManager)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (OverlayManager)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:26+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c52b5820e7cef561ebea769fa5f42f1d43b3bc216d1d8cd035d324da28a259a1
---

提供绘制浮层的能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 12开始支持。
* 以下API需先使用UIContext中的[getOverlayManager()](arkts-apis-uicontext-uicontext.md#getoverlaymanager12)方法获取到OverlayManager对象，再通过该对象调用对应方法。
* OverlayManager上节点的层级在Page页面层级之上，在Dialog、Popup、Menu、BindSheet、BindContentCover和Toast等之下。
* OverlayManager上节点安全区域内外的绘制方式与Page一致，键盘避让方式与Page一致。
* 与OverlayManager相关的属性推荐采用AppStorage来进行应用全局存储，以免切换页面后属性值发生变化从而导致业务错误。

## addComponentContent12+

PhonePC/2in1TabletTVWearable

addComponentContent(content: ComponentContent, index?: number): void

在OverlayManager上新增指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 在OverlayManager的指定节点上添加此content。  **说明：**  新增的节点默认处于页面居中，按层级堆叠。 |
| index | number | 否 | 新增节点在OverlayManager上的层级位置。  **说明：**  当index ≥ 0时，越大，ComponentContent的层级越高；若多个ComponentContent的index相同，ComponentContent添加的时间越晚层级越高。  当index < 0、index = null或index = undefined时，ComponentContent默认添加至最高层。  当同一个ComponentContent被添加多次时，只保留最后一次添加的ComponentContent。 |

**示例：**

```
1. import { ComponentContent, OverlayManager } from '@kit.ArkUI';

3. class Params {
4. text: string = "";
5. offset: Position;

7. constructor(text: string, offset: Position) {
8. this.text = text;
9. this.offset = offset;
10. }
11. }

13. @Builder
14. function builderText(params: Params) {
15. Column() {
16. Text(params.text)
17. .fontSize(30)
18. .fontWeight(FontWeight.Bold)
19. }.offset(params.offset)
20. }

22. @Entry
23. @Component
24. struct OverlayExample {
25. @State message: string = 'ComponentContent';
26. private uiContext: UIContext = this.getUIContext();
27. private overlayNode: OverlayManager = this.uiContext.getOverlayManager();
28. @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
29. @StorageLink('componentContentIndex') componentContentIndex: number = 0;
30. @StorageLink('arrayIndex') arrayIndex: number = 0;
31. @StorageLink("componentOffset") componentOffset: Position = { x: 0, y: 110 };

33. build() {
34. Column({ space: 5 }) {
35. Button("++componentContentIndex: " + this.componentContentIndex).onClick(() => {
36. ++this.componentContentIndex;
37. })
38. Button("--componentContentIndex: " + this.componentContentIndex).onClick(() => {
39. --this.componentContentIndex;
40. })
41. Button("增加ComponentContent" + this.contentArray.length).onClick(() => {
42. let componentContent = new ComponentContent(
43. this.uiContext, wrapBuilder<[Params]>(builderText),
44. new Params(this.message + (this.contentArray.length), this.componentOffset)
45. );
46. this.contentArray.push(componentContent);
47. this.overlayNode.addComponentContent(componentContent, this.componentContentIndex);
48. })
49. Button("++arrayIndex: " + this.arrayIndex).onClick(() => {
50. ++this.arrayIndex;
51. })
52. Button("--arrayIndex: " + this.arrayIndex).onClick(() => {
53. --this.arrayIndex;
54. })
55. Button("删除ComponentContent" + this.arrayIndex).onClick(() => {
56. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
57. let componentContent = this.contentArray.splice(this.arrayIndex, 1);
58. this.overlayNode.removeComponentContent(componentContent.pop());
59. } else {
60. console.info("arrayIndex有误");
61. }
62. })
63. Button("显示ComponentContent" + this.arrayIndex).onClick(() => {
64. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
65. let componentContent = this.contentArray[this.arrayIndex];
66. this.overlayNode.showComponentContent(componentContent);
67. } else {
68. console.info("arrayIndex有误");
69. }
70. })
71. Button("隐藏ComponentContent" + this.arrayIndex).onClick(() => {
72. if (this.arrayIndex >= 0 && this.arrayIndex < this.contentArray.length) {
73. let componentContent = this.contentArray[this.arrayIndex];
74. this.overlayNode.hideComponentContent(componentContent);
75. } else {
76. console.info("arrayIndex有误");
77. }
78. })
79. Button("显示所有ComponentContent").onClick(() => {
80. this.overlayNode.showAllComponentContents();
81. })
82. Button("隐藏所有ComponentContent").onClick(() => {
83. this.overlayNode.hideAllComponentContents();
84. })
85. }
86. .width('100%')
87. .height('100%')
88. }
89. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/_V90z4JnQ12ROtOi3rAHdg/zh-cn_image_0000002583439457.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000023Z&HW-CC-Expire=86400&HW-CC-Sign=6D533D6643036034F114BA8E4B73A3BCCDD93A201E48693FD3B35D81F2606D3B)

## addComponentContentWithOrder18+

PhonePC/2in1TabletTVWearable

addComponentContentWithOrder(content: ComponentContent, levelOrder?: LevelOrder): void

创建浮层节点时，指定显示顺序。

支持在浮层节点创建时指定显示的顺序。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 在OverlayManager的指定节点上添加此content。  **说明：**  新增的节点默认处于页面居中位置，按层级堆叠。 |
| levelOrder | [LevelOrder](js-apis-promptaction.md#levelorder18) | 否 | 新增浮层节点的显示顺序。  **说明：**  - 默认值：LevelOrder.clamp(0) |

**示例：**

该示例通过调用addComponentContentWithOrder接口，实现了按照指定显示顺序创建浮层节点的功能。

```
1. import { ComponentContent, PromptAction, LevelOrder, UIContext, OverlayManager } from '@kit.ArkUI';

3. class Params {
4. text: string = "";
5. offset: Position;
6. constructor(text: string, offset: Position) {
7. this.text = text;
8. this.offset = offset;
9. }
10. }
11. @Builder
12. function builderText(params: Params) {
13. Column() {
14. Text(params.text)
15. .fontSize(30)
16. .fontWeight(FontWeight.Bold)
17. }.offset(params.offset)
18. }

20. @Entry
21. @Component
22. struct Index {
23. @State message: string = '弹窗';
24. private ctx: UIContext = this.getUIContext();
25. private promptAction: PromptAction = this.ctx.getPromptAction();
26. private overlayNode: OverlayManager = this.ctx.getOverlayManager();
27. @StorageLink('contentArray') contentArray: ComponentContent<Params>[] = [];
28. @StorageLink('componentContentIndex') componentContentIndex: number = 0;
29. @StorageLink('arrayIndex') arrayIndex: number = 0;
30. @StorageLink("componentOffset") componentOffset: Position = { x: 0, y: 80 };

32. build() {
33. Row() {
34. Column({ space: 10 }) {
35. Button('OverlayManager下面弹窗')
36. .fontSize(20)
37. .onClick(() => {
38. let componentContent = new ComponentContent(
39. this.ctx, wrapBuilder<[Params]>(builderText),
40. new Params(this.message + (this.contentArray.length), this.componentOffset)
41. );
42. this.contentArray.push(componentContent);
43. this.overlayNode.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100.1));
44. let topOrder: LevelOrder = this.promptAction.getTopOrder();
45. if (topOrder !== undefined) {
46. console.error('topOrder: ' + topOrder.getOrder());
47. }
48. let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
49. if (bottomOrder !== undefined) {
50. console.error('bottomOrder: ' + bottomOrder.getOrder());
51. }
52. })
53. Button('OverlayManager上面弹窗')
54. .fontSize(20)
55. .onClick(() => {
56. let componentContent = new ComponentContent(
57. this.ctx, wrapBuilder<[Params]>(builderText),
58. new Params(this.message + (this.contentArray.length), this.componentOffset)
59. );
60. this.contentArray.push(componentContent);
61. this.overlayNode.addComponentContentWithOrder(componentContent, LevelOrder.clamp(100.2));
62. let topOrder: LevelOrder = this.promptAction.getTopOrder();
63. if (topOrder !== undefined) {
64. console.error('topOrder: ' + topOrder.getOrder());
65. }
66. let bottomOrder: LevelOrder = this.promptAction.getBottomOrder();
67. if (bottomOrder !== undefined) {
68. console.error('bottomOrder: ' + bottomOrder.getOrder());
69. }
70. })
71. }.width('100%')
72. }.height('100%')
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/R_CWf110R9GQ_1FWNbZw3g/zh-cn_image_0000002552959412.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000023Z&HW-CC-Expire=86400&HW-CC-Sign=3A9D0A8CB8D2A8F52A7C0CC31C182F0677771C1FA39E44A6788BF1E54B716002)

## removeComponentContent12+

PhonePC/2in1TabletTVWearable

removeComponentContent(content: ComponentContent): void

删除overlay上的指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 在OverlayManager上删除此content。 |

**示例：**

请参考[addComponentContent示例](arkts-apis-uicontext-overlaymanager.md#addcomponentcontent12)。

## showComponentContent12+

PhonePC/2in1TabletTVWearable

showComponentContent(content: ComponentContent): void

在OverlayManager上显示指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 在OverlayManager上显示此content。 |

**示例：**

请参考[addComponentContent示例](arkts-apis-uicontext-overlaymanager.md#addcomponentcontent12)。

## hideComponentContent12+

PhonePC/2in1TabletTVWearable

hideComponentContent(content: ComponentContent): void

隐藏OverlayManager上的指定节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| content | [ComponentContent](js-apis-arkui-componentcontent.md) | 是 | 在OverlayManager上隐藏此content。 |

**示例：**

请参考[addComponentContent示例](arkts-apis-uicontext-overlaymanager.md#addcomponentcontent12)。

## showAllComponentContents12+

PhonePC/2in1TabletTVWearable

showAllComponentContents(): void

显示OverlayManager上所有的ComponentContent。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[addComponentContent示例](arkts-apis-uicontext-overlaymanager.md#addcomponentcontent12)。

## hideAllComponentContents12+

PhonePC/2in1TabletTVWearable

hideAllComponentContents(): void

隐藏OverlayManager上的所有ComponentContent。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

请参考[addComponentContent示例](arkts-apis-uicontext-overlaymanager.md#addcomponentcontent12)。
