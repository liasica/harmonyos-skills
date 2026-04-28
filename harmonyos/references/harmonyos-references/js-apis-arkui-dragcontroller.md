---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-dragcontroller
title: @ohos.arkui.dragController (DragController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.dragController (DragController)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cacf32e25fa6f287d5b7fd29bddae6bb31b1b96128166f8e0e8acf940d176690
---

本模块提供发起主动拖拽的能力，当应用接收到触摸或长按等事件时可以主动发起拖拽的动作，并在其中携带拖拽信息。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](../harmonyos-guides/arkts-global-interface.md#ui上下文不明确)的地方使用，参见[UIContext](arkts-apis-uicontext-uicontext.md)说明。
* 示例效果请以真机运行为准，当前 DevEco Studio预览器不支持。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { dragController } from '@kit.ArkUI';
```

## dragController.executeDrag(deprecated)

PhonePC/2in1TabletTVWearable

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo,callback:AsyncCallback<DragEventParam>): void

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。使用callback异步回调。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[executeDrag](arkts-apis-uicontext-dragcontroller.md#executedrag11)替代。executeDrag需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取[DragController](arkts-apis-uicontext-dragcontroller.md)实例，然后通过该对象进行调用。
* 从API version 11开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的[DragController](arkts-apis-uicontext-dragcontroller.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 拖拽发起后跟手效果所拖拽的对象。  **说明：**  不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true。该builder只用于生成当次拖拽中显示的图片。builder的根组件宽高为0时，无法生成拖拽显示的图片导致拖拽失败。builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。 |
| dragInfo | [DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[DragEventParam](js-apis-arkui-dragcontroller.md#drageventparam12)> | 是 | 回调函数。当拖拽成功结束，err为undefined，data为获取到的DragEventParam；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```
1. import { dragController } from '@kit.ArkUI';
2. import { unifiedDataChannel } from '@kit.ArkData';

4. class DragInfo {
5. event: DragEvent | undefined = undefined;
6. extraParams: string = '';
7. }

9. @Entry
10. @Component
11. struct DragControllerPage {
12. @State text: string = ''

14. @Builder
15. DraggingBuilder() {
16. Column() {
17. Text("DraggingBuilder")
18. .fontColor(Color.White)
19. .fontSize(12)
20. }
21. .width(100)
22. .height(100)
23. .backgroundColor(Color.Blue)
24. }

26. build() {
27. Column() {
28. Button('touch to execute drag')
29. .margin(10)
30. .onTouch((event?: TouchEvent) => {
31. if (event) {
32. if (event.type == TouchType.Down) {
33. let text = new unifiedDataChannel.PlainText()
34. text.textContent = 'drag text'
35. text.abstract = 'abstract'
36. let unifiedData = new unifiedDataChannel.UnifiedData(text)

38. let dragInfo: dragController.DragInfo = {
39. pointerId: 0,
40. data: unifiedData,
41. extraParams: ''
42. }
43. let eve: DragInfo = new DragInfo();
44. this.getUIContext().getDragController().executeDrag(() => {
45. this.DraggingBuilder()
46. }, dragInfo, (err, eve) => { // 建议使用 this.getUIContext().getDragController().executeDrag()接口
47. if (eve.event) {
48. if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
49. // ...
50. } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
51. // ...
52. }
53. }
54. })
55. }
56. }
57. })
58. Text(this.text)
59. .height(100)
60. .width(150)
61. .margin({ top: 20 })
62. .border({ color: Color.Black, width: 1 })
63. .onDrop((dragEvent?: DragEvent) => {
64. if (dragEvent) {
65. let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
66. let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
67. this.text = plainText.textContent;
68. }
69. })
70. }
71. .width('100%')
72. .height('100%')
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/6PI6C38MSImO9YGMsMFOFQ/zh-cn_image_0000002552799752.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=6B0F65DD13ECB085F7D04F2B8BD0E11E90FC1E330A4435D95ED06E5B0EA2565C)

## dragController.executeDrag(deprecated)

PhonePC/2in1TabletTVWearable

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: DragInfo): Promise<DragEventParam>

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。使用Promise异步回调。

说明

* 从API version 10开始支持，从API version 18开始废弃，建议使用[executeDrag](arkts-apis-uicontext-dragcontroller.md#executedrag11-1)替代。executeDrag需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取[DragController](arkts-apis-uicontext-dragcontroller.md)实例，然后通过该对象进行调用。
* 从API version 11开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的[DragController](arkts-apis-uicontext-dragcontroller.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 拖拽发起后跟手效果所拖拽的对象。 |
| dragInfo | [DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DragEventParam](js-apis-arkui-dragcontroller.md#drageventparam12)> | Promise对象，拖拽结束返回结果的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```
1. import { dragController } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { unifiedDataChannel } from '@kit.ArkData';

5. class DragInfo {
6. event: DragEvent | undefined = undefined;
7. extraParams: string = '';
8. }

10. @Entry
11. @Component
12. struct DragControllerPage {
13. @State pixmap: image.PixelMap | undefined = undefined
14. @State text: string = ''

16. @Builder
17. DraggingBuilder() {
18. Column() {
19. Text("DraggingBuilder")
20. .fontColor(Color.White)
21. }
22. .width(100)
23. .height(100)
24. .backgroundColor(Color.Blue)
25. }

27. @Builder
28. PixmapBuilder() {
29. Column() {
30. Text("PixmapBuilder")
31. .fontColor(Color.White)
32. .fontSize(15)
33. }
34. .width(100)
35. .height(100)
36. .backgroundColor(Color.Blue)
37. }

39. aboutToAppear() {
40. let pb: CustomBuilder = (): void => {
41. this.PixmapBuilder()
42. }
43. this.getUIContext().getComponentSnapshot().createFromBuilder(pb).then((pix: image.PixelMap) => {
44. this.pixmap = pix;
45. })
46. }

48. build() {
49. Column() {
50. Button('touch to execute drag')
51. .margin(10)
52. .onTouch((event?: TouchEvent) => {
53. if (event) {
54. if (event.type == TouchType.Down) {
55. let text = new unifiedDataChannel.PlainText()
56. text.textContent = 'drag text'
57. text.abstract = 'abstract'
58. let unifiedData = new unifiedDataChannel.UnifiedData(text)

60. let dragInfo: dragController.DragInfo = {
61. pointerId: 0,
62. data: unifiedData,
63. extraParams: ''
64. }
65. let dragItemInfo: DragItemInfo = {
66. pixelMap: this.pixmap,
67. builder: () => {
68. this.DraggingBuilder()
69. },
70. extraInfo: "DragItemInfoTest"
71. }
72. let eve: DragInfo = new DragInfo();
73. this.getUIContext()
74. .getDragController()
75. .executeDrag(dragItemInfo, dragInfo) // 建议使用 this.getUIContext().getDragController().executeDrag()接口
76. .then((eve) => {
77. if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
78. // ...
79. } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
80. // ...
81. }
82. })
83. .catch((err: Error) => {
84. })
85. }
86. }
87. })
88. Text(this.text)
89. .height(100)
90. .width(150)
91. .margin({ top: 20 })
92. .border({ color: Color.Black, width: 1 })
93. .onDrop((dragEvent?: DragEvent) => {
94. if (dragEvent) {
95. let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
96. let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
97. this.text = plainText.textContent;
98. }
99. })
100. }
101. .width('100%')
102. .height('100%')
103. }
104. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/4PHNcyB8SAizieGfYKiGDw/zh-cn_image_0000002583439447.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=460414EBF0FB7D908F756126817ACDF104F8AC18B69DC929364DBD02A5356A62)

## DragInfo

PhonePC/2in1TabletTVWearable

发起拖拽所需要的属性和拖拽时携带的信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pointerId | number | 否 | 否 | 设置启动拖拽时屏幕上触摸点的Id。取值范围为[0, 9]的整数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| data | [unifiedDataChannel.UnifiedData](js-apis-data-unifieddatachannel.md#unifieddata) | 否 | 是 | 设置拖拽过程中携带的数据。  默认值：空  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| extraParams | string | 否 | 是 | 设置拖拽事件额外信息，具体功能暂未实现。  默认值：空  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| touchPoint11+ | [TouchPoint](ts-types.md#touchpoint11) | 否 | 是 | 配置跟手点坐标。不配置时，左右居中，顶部向下偏移20%。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| previewOptions11+ | [DragPreviewOptions](ts-universal-attributes-drag-drop.md#dragpreviewoptions11-1) | 否 | 是 | 设置拖拽过程中背板图处理模式及数量角标的显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| dataLoadParams20+ | [unifiedDataChannel.DataLoadParams](js-apis-data-unifieddatachannel.md#dataloadparams20) | 否 | 是 | 设置拖起方延迟提供数据。调用此方法向系统提供数据加载参数，而非直接传入完整的数据对象。当用户将数据拖拽至目标应用程序并释放时，系统将使用此参数从起拖方请求实际数据。与data同时设置时，dataLoadParams生效。  默认值：空  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## dragController.createDragAction(deprecated)

PhonePC/2in1TabletTVWearable

createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: DragInfo): DragAction

创建拖拽的Action对象，需要显式指定拖拽背板图(可多个)，以及拖拽的数据，跟手点等信息；当通过一个已创建的 Action 对象发起的拖拽未结束时，无法再次创建新的 Action 对象，接口会抛出异常；当Action对象的生命周期结束后，注册在该对象上的回调函数会失效，因此需要在一个尽量长的作用域下持有该对象，并在每次发起拖拽前通过createDragAction返回新的对象覆盖旧值。

说明

* 从API version 11开始支持，从API version 18开始废弃，建议使用[createDragAction](arkts-apis-uicontext-dragcontroller.md#createdragaction11)替代。createDragAction需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取[DragController](arkts-apis-uicontext-dragcontroller.md)实例，然后通过该对象进行调用。
* 从API version 11开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的[DragController](arkts-apis-uicontext-dragcontroller.md)对象。
* 建议控制传递的拖拽背板数量，传递过多容易导致拖起的效率问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customArray | Array<[CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo)> | 是 | 拖拽发起后跟手效果所拖拽的对象。 |
| dragInfo | [DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DragAction](js-apis-arkui-dragcontroller.md#dragaction11) | 创建拖拽Action对象，主要用于后面实现注册监听拖拽状态改变事件和启动拖拽服务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```
1. import { dragController } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { unifiedDataChannel } from '@kit.ArkData';

5. @Entry
6. @Component
7. struct DragControllerPage {
8. @State pixmap: image.PixelMap | null = null
9. @State text: string = ''
10. private dragAction: dragController.DragAction | null = null;
11. customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

13. @Builder
14. DraggingBuilder() {
15. Column() {
16. Text("DraggingBuilder")
17. .fontColor(Color.White)
18. .fontSize(12)
19. }
20. .width(100)
21. .height(100)
22. .backgroundColor(Color.Blue)
23. }

25. build() {
26. Column() {

28. Column() {
29. Text(this.text)
30. .width('100%')
31. .height('100%')
32. .fontColor(Color.White)
33. .fontSize(18)
34. .onDrop((dragEvent?: DragEvent) => {
35. if (dragEvent) {
36. let records: Array<unifiedDataChannel.UnifiedRecord> = dragEvent.getData().getRecords();
37. let plainText: unifiedDataChannel.PlainText = records[0] as unifiedDataChannel.PlainText;
38. this.text = plainText.textContent;
39. }
40. })
41. }
42. .width(100)
43. .height(100)
44. .backgroundColor(Color.Red)
45. .margin(10)

47. Button('多对象dragAction customBuilder拖拽').onTouch((event?: TouchEvent) => {
48. if (event) {
49. if (event.type == TouchType.Down) {
50. console.info("multi drag Down by listener");
51. this.customBuilders.splice(0, this.customBuilders.length);
52. this.customBuilders.push(() => {
53. this.DraggingBuilder()
54. });
55. this.customBuilders.push(() => {
56. this.DraggingBuilder()
57. });
58. this.customBuilders.push(() => {
59. this.DraggingBuilder()
60. });
61. let text = new unifiedDataChannel.PlainText()
62. text.textContent = 'drag text'
63. let unifiedData = new unifiedDataChannel.UnifiedData(text)
64. let dragInfo: dragController.DragInfo = {
65. pointerId: 0,
66. data: unifiedData,
67. extraParams: ''
68. }
69. try {
70. this.dragAction = this.getUIContext()
71. .getDragController()
72. .createDragAction(this.customBuilders,
73. dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
74. if (!this.dragAction) {
75. console.info("listener dragAction is null");
76. return
77. }
78. this.dragAction.on('statusChange', (dragAndDropInfo: dragController.DragAndDropInfo) => {
79. if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
80. console.info("drag has start");
81. } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED) {
82. console.info("drag has end");
83. if (!this.dragAction) {
84. return
85. }
86. this.dragAction.off('statusChange')
87. }
88. })
89. this.dragAction.startDrag().then(() => {
90. }).catch((err: Error) => {
91. console.error(`start drag Error:${err.message}`);
92. })
93. } catch (err) {
94. console.error(`create dragAction Error:${err.message}`);
95. }
96. }
97. }
98. }).margin({ top: 20 })
99. }
100. }
101. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/yUsx_ef6SVy_WkIHR56V1w/zh-cn_image_0000002552959402.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=B4CD1166CCC846BC6F4BDFC5D7F29383FD2627F3C719B7F83B41ACC3B4172D6C)

## DragAction11+

PhonePC/2in1TabletTVWearable

监听状态改变，启动拖拽服务的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### startDrag11+

PhonePC/2in1TabletTVWearable

startDrag(): Promise<void>

启动拖拽服务。使用Promise异步回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Internal handling failed. |

**示例1：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```
1. import { dragController } from '@kit.ArkUI';
2. import { unifiedDataChannel } from '@kit.ArkData';

4. @Entry
5. @Component
6. struct DragControllerPage {
7. private dragAction: dragController.DragAction | null = null;
8. customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

10. @Builder
11. DraggingBuilder() {
12. Column() {
13. Text("DraggingBuilder")
14. .fontColor(Color.White)
15. .fontSize(12)
16. }
17. .width(100)
18. .height(100)
19. .backgroundColor(Color.Blue)
20. }

22. build() {
23. Column() {
24. Button('touch to execute drag').onTouch((event?: TouchEvent) => {
25. if (event) {
26. if (event.type == TouchType.Down) {
27. this.customBuilders.splice(0, this.customBuilders.length);
28. this.customBuilders.push(() => {
29. this.DraggingBuilder()
30. });
31. let text = new unifiedDataChannel.PlainText()
32. text.textContent = 'drag text'
33. let unifiedData = new unifiedDataChannel.UnifiedData(text)
34. let dragInfo: dragController.DragInfo = {
35. pointerId: 0,
36. data: unifiedData,
37. extraParams: ''
38. }
39. try {
40. this.dragAction = this.getUIContext()
41. .getDragController()
42. .createDragAction(this.customBuilders,
43. dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
44. if (!this.dragAction) {
45. console.info("listener dragAction is null");
46. return;
47. }
48. this.dragAction.startDrag().then(() => {
49. }).catch((err: Error) => {
50. console.error(`start drag Error: ${err.message}`);
51. })
52. } catch (err) {
53. console.error(`create dragAction Error: ${err.message}`);
54. }
55. }
56. }
57. }).margin({ top: 20 })
58. }
59. }
60. }
```

**示例2：**

从API version 20开始，在[DragInfo](js-apis-arkui-dragcontroller.md#draginfo)中配置dataLoadParams，设置拖起方延迟提供数据。

```
1. import { unifiedDataChannel, uniformTypeDescriptor, uniformDataStruct } from '@kit.ArkData';
2. import { fileUri, fileIo as fileIo } from '@kit.CoreFileKit';
3. import { common } from '@kit.AbilityKit';
4. import { dragController } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct ImageExample {
9. private dragAction: dragController.DragAction | null = null;
10. customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();
11. @State uri: string = "";
12. @State blockArr: string[] = [];
13. uiContext = this.getUIContext();
14. udKey: string = '';

16. @Builder
17. DraggingBuilder() {
18. Video({ src: $rawfile('test1.mp4'), controller: new VideoController() })
19. .width(100)
20. .height(100)
21. }

23. build() {
24. Column() {
25. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceAround }) {
26. Button('touch to execute drag')
27. .margin(10)
28. .onTouch((event?: TouchEvent) => {
29. if (event) {
30. if (event.type == TouchType.Down) {
31. this.customBuilders.splice(0, this.customBuilders.length);
32. this.customBuilders.push(() => {
33. this.DraggingBuilder()
34. });
35. const context: Context | undefined = this.uiContext.getHostContext();
36. if (context) {
37. let loadHandler: unifiedDataChannel.DataLoadHandler = () => {
38. let data =
39. context.resourceManager.getRawFdSync('test1.mp4');
40. let filePath = context.filesDir + '/test1.mp4';
41. let file = fileIo.openSync(filePath, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE);
42. let bufferSize = data.length as number;
43. let buf = new ArrayBuffer(bufferSize);
44. fileIo.readSync(data.fd, buf, { offset: data.offset, length: bufferSize });
45. fileIo.writeSync(file.fd, buf, { offset: 0, length: bufferSize });
46. fileIo.closeSync(file.fd);
47. context.resourceManager.closeRawFdSync('test1.mp4')
48. this.uri = fileUri.getUriFromPath(filePath);
49. let videoMp: uniformDataStruct.FileUri = {
50. uniformDataType: 'general.file-uri',
51. oriUri: this.uri,
52. fileType: 'general.video',
53. }
54. let unifiedRecord = new unifiedDataChannel.UnifiedRecord();
55. let unifiedData = new unifiedDataChannel.UnifiedData();
56. unifiedRecord.addEntry(uniformTypeDescriptor.UniformDataType.FILE_URI, videoMp);
57. unifiedData.addRecord(unifiedRecord);
58. return unifiedData;
59. }

61. let dragInfo: dragController.DragInfo = {
62. pointerId: 0,
63. extraParams: '',
64. dataLoadParams: {
65. loadHandler: loadHandler,
66. dataLoadInfo: { types: new Set([uniformTypeDescriptor.UniformDataType.VIDEO]), recordCount: 1 }
67. }
68. }

70. let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
71. console.info(`ndq Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}`);
72. }
73. try {
74. this.dragAction = this.getUIContext()
75. .getDragController()
76. .createDragAction(this.customBuilders,
77. dragInfo)
78. if (!this.dragAction) {
79. console.info("listener dragAction is null");
80. return;
81. }
82. this.dragAction.on('statusChange', func);
83. this.dragAction.startDrag().then(() => {
84. }).catch((err: Error) => {
85. console.error(`start drag Error: ${err.message}`);
86. })
87. } catch (err) {
88. console.error(`create dragAction Error: ${err.message}`);
89. }
90. }
91. }
92. }
93. })
94. }
95. .margin({ bottom: 20 })

97. Row() {
98. Column() {
99. Text('可释放区域')
100. .fontSize('15dp')
101. .height('10%')
102. List() {
103. ForEach(this.blockArr, (item: string, index) => {
104. ListItem() {
105. Video({ src: item, controller: new VideoController() })
106. .width(100)
107. .height(100)
108. .border({ width: 1 })
109. }
110. .margin({ left: 30, top: 30 })
111. }, (item: string) => item)
112. }
113. .border({ width: 1 })
114. .height('90%')
115. .width('100%')
116. .allowDrop([uniformTypeDescriptor.UniformDataType.VIDEO])
117. .onDrop((event?: DragEvent, extraParams?: string) => {
118. let context = this.uiContext.getHostContext() as common.UIAbilityContext;
119. let pathDir: string = context.distributedFilesDir;
120. let destUri = fileUri.getUriFromPath(pathDir);
121. let progressListener: unifiedDataChannel.DataProgressListener =
122. (progress: unifiedDataChannel.ProgressInfo, dragData: UnifiedData | null) => {
123. if (dragData != null) {
124. let arr: Array<unifiedDataChannel.UnifiedRecord> = dragData.getRecords();
125. if (arr.length > 0) {
126. if (arr[0].getType() === uniformTypeDescriptor.UniformDataType.VIDEO) {
127. this.blockArr.splice(JSON.parse(extraParams as string).insertIndex, 0, this.uri);
128. }
129. } else {
130. console.info('dragData arr is null');
131. }
132. } else {
133. console.info('dragData is undefined');
134. }
135. console.info(`percentage: ${progress.progress}`);
136. };
137. let options: DataSyncOptions = {
138. destUri: destUri,
139. fileConflictOptions: unifiedDataChannel.FileConflictOptions.OVERWRITE,
140. progressIndicator: unifiedDataChannel.ProgressIndicator.DEFAULT,
141. dataProgressListener: progressListener,
142. }
143. try {
144. this.udKey = (event as DragEvent).startDataLoading(options);
145. console.info('udKey: ', this.udKey);
146. } catch (e) {
147. console.error(`startDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
148. }
149. }, { disableDataPrefetch: true })
150. }
151. .height("50%")
152. .width("90%")
153. .border({ width: 1 })
154. }

156. Button('取消数据传输')
157. .onClick(() => {
158. try {
159. this.getUIContext().getDragController().cancelDataLoading(this.udKey);
160. } catch (e) {
161. console.error(`cancelDataLoading errorCode: ${e.code}, errorMessage: ${e.message}`);
162. }
163. })
164. .margin({ top: 10 })
165. }.width('100%')
166. }
167. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/IZa8Yj3mRVqMX8cB6GR13g/zh-cn_image_0000002583479403.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=964FD8C566A2C79040DEDF5DE4E730EF2BE39F31F2C715AF623B5A33CACE61EB)

### on('statusChange')11+

PhonePC/2in1TabletTVWearable

on(type: 'statusChange', callback: Callback<[DragAndDropInfo](js-apis-arkui-dragcontroller.md#draganddropinfo11)>): void

注册监听拖拽状态改变事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'statusChange'，即注册监听拖拽状态改变事件。 |
| callback | Callback<[DragAndDropInfo](js-apis-arkui-dragcontroller.md#draganddropinfo11)> | 是 | 回调函数，返回当前的[DragAndDropInfo](js-apis-arkui-dragcontroller.md#draganddropinfo11)组件状态。 |

**示例：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```
1. import { dragController } from '@kit.ArkUI';
2. import { unifiedDataChannel } from '@kit.ArkData';

4. @Entry
5. @Component
6. struct DragControllerPage {
7. private dragAction: dragController.DragAction | null = null;
8. customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

10. @Builder
11. DraggingBuilder() {
12. Column() {
13. Text("DraggingBuilder")
14. .fontColor(Color.White)
15. .fontSize(12)
16. }
17. .width(100)
18. .height(100)
19. .backgroundColor(Color.Blue)
20. }

22. build() {
23. Column() {
24. Button('touch to execute drag').onTouch((event?: TouchEvent) => {
25. if (event) {
26. if (event.type == TouchType.Down) {
27. this.customBuilders.splice(0, this.customBuilders.length);
28. this.customBuilders.push(() => {
29. this.DraggingBuilder()
30. });
31. let text = new unifiedDataChannel.PlainText()
32. text.textContent = 'drag text'
33. let unifiedData = new unifiedDataChannel.UnifiedData(text)
34. let dragInfo: dragController.DragInfo = {
35. pointerId: 0,
36. data: unifiedData,
37. extraParams: ''
38. }
39. let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
40. console.info(`Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}`);
41. }
42. try {
43. this.dragAction = this.getUIContext()
44. .getDragController()
45. .createDragAction(this.customBuilders,
46. dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
47. if (!this.dragAction) {
48. console.info("listener dragAction is null");
49. return;
50. }
51. // 监听状态改变，触发后打印func中的日志
52. this.dragAction.on('statusChange', func);
53. this.dragAction.startDrag().then(() => {
54. }).catch((err: Error) => {
55. console.error(`start drag Error: ${err.message}`);
56. })
57. } catch (err) {
58. console.error(`create dragAction Error: ${err.message}`);
59. }
60. }
61. }
62. }).margin({ top: 20 })
63. }
64. }
65. }
```

### off('statusChange')11+

PhonePC/2in1TabletTVWearable

off(type: 'statusChange', callback?: Callback<[DragAndDropInfo](js-apis-arkui-dragcontroller.md#draganddropinfo11)>): void

取消注册监听拖拽状态改变事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'statusChange'，即取消监听拖拽状态改变事件。 |
| callback | Callback<[DragAndDropInfo](js-apis-arkui-dragcontroller.md#draganddropinfo11)> | 否 | 回调函数，返回当前的[DragAndDropInfo](js-apis-arkui-dragcontroller.md#draganddropinfo11)组件状态。 |

**示例：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

```
1. import { dragController } from '@kit.ArkUI';
2. import { unifiedDataChannel } from '@kit.ArkData';

4. @Entry
5. @Component
6. struct DragControllerPage {
7. private dragAction: dragController.DragAction | null = null;
8. customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();

10. @Builder
11. DraggingBuilder() {
12. Column() {
13. Text("DraggingBuilder")
14. .fontColor(Color.White)
15. .fontSize(12)
16. }
17. .width(100)
18. .height(100)
19. .backgroundColor(Color.Blue)
20. }

22. build() {
23. Column() {
24. Button('touch to execute drag').onTouch((event?: TouchEvent) => {
25. if (event) {
26. if (event.type == TouchType.Down) {
27. this.customBuilders.splice(0, this.customBuilders.length);
28. this.customBuilders.push(() => {
29. this.DraggingBuilder()
30. });
31. let text = new unifiedDataChannel.PlainText()
32. text.textContent = 'drag text'
33. let unifiedData = new unifiedDataChannel.UnifiedData(text)
34. let dragInfo: dragController.DragInfo = {
35. pointerId: 0,
36. data: unifiedData,
37. extraParams: ''
38. }
39. let func = (dragAndDropInfo: dragController.DragAndDropInfo) => {
40. console.info(`Register to listen on drag status ${JSON.stringify(dragAndDropInfo)}`);
41. }
42. this.dragAction = this.getUIContext()
43. .getDragController()
44. .createDragAction(this.customBuilders,
45. dragInfo) // 建议使用 this.getUIContext().getDragController().createDragAction()接口
46. if (!this.dragAction) {
47. console.info("listener dragAction is null");
48. return;
49. }
50. this.dragAction.on('statusChange', func);
51. // 取消监听，发起拖拽后不会打印func中的日志
52. this.dragAction.off('statusChange', func);
53. this.dragAction.startDrag().then(() => {
54. }).catch((err: Error) => {
55. console.error(`start drag Error: ${err.message}`);
56. })
57. }
58. }
59. }).margin({ top: 20 })
60. }
61. }
62. }
```

## DragAndDropInfo11+

PhonePC/2in1TabletTVWearable

拖拽过程中监听到status改变时上报的数据。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | [DragStatus](js-apis-arkui-dragcontroller.md#dragstatus11) | 否 | 否 | 当前拖拽状态（启动和结束）。 |
| event | [DragEvent](ts-universal-events-drag-drop.md#dragevent7) | 否 | 否 | 当前状态所对应的拖拽事件。通过dragController发起的dragEvent仅支持获取result和behavior，且用于拖拽结束状态。 |
| extraParams | string | 否 | 是 | 设置拖拽事件额外信息，具体功能暂未实现。默认值为空。 |

## DragStatus11+

PhonePC/2in1TabletTVWearable

拖拽开始和结束状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STARTED | 0 | 拖拽已成功发起。 |
| ENDED | 1 | 拖拽结束。 |

## AnimationOptions11+

PhonePC/2in1TabletTVWearable

拖拽相关的动效参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| duration | number | 否 | 是 | 动画持续时间，单位为毫秒。  默认值：1000  **说明：**  - 设置小于0的值时按0处理。  - 设置浮点型类型的值时，向下取整。例如，设置值为1.2，按照1处理。 |
| curve | [Curve](ts-appendix-enums.md#curve) | [ICurve](js-apis-curve.md#icurve9) | 否 | 是 | 设置动画曲线。  默认值：Curve.EaseInOut |

## DragEventParam12+

PhonePC/2in1TabletTVWearable

拖拽结束返回结果的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event10+ | [DragEvent](ts-universal-events-drag-drop.md#dragevent7) | 否 | 否 | 拖拽事件信息，仅包括拖拽结果。 |
| extraParams10+ | string | 否 | 否 | 拖拽事件额外信息。 |

## dragController.getDragPreview(deprecated)

PhonePC/2in1TabletTVWearable

getDragPreview(): DragPreview

返回一个代表拖拽背板的对象。

说明

* 从API version 11开始支持，从API version 18开始废弃，建议使用[getDragPreview](arkts-apis-uicontext-dragcontroller.md#getdragpreview11)替代。getDragPreview需先通过[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取[DragController](arkts-apis-uicontext-dragcontroller.md)实例，然后通过该对象进行调用。
* 从API version 11开始，可以通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的[DragController](arkts-apis-uicontext-dragcontroller.md)对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [DragPreview](js-apis-arkui-dragcontroller.md#dragpreview11) | 一个代表拖拽背板的对象，提供背板样式设置的接口，在OnDrop和OnDragEnd回调中使用不生效。 |

**示例：**

请参考[animate](js-apis-arkui-dragcontroller.md#animate11)

## DragPreview11+

PhonePC/2in1TabletTVWearable

拖拽背板的对象，在OnDrop和OnDragEnd回调中使用不生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setForegroundColor11+

PhonePC/2in1TabletTVWearable

setForegroundColor(color: ResourceColor): void

设置背板蒙版颜色，在OnDrop和OnDragEnd回调中使用不生效，仅支持通过 [getDragPreview()](arkts-apis-uicontext-dragcontroller.md#getdragpreview11) 方法获取到的对象上使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](ts-types.md#resourcecolor) | 是 | 背板蒙版颜色。 |

**示例：**

请参考[animate](js-apis-arkui-dragcontroller.md#animate11)

### animate11+

PhonePC/2in1TabletTVWearable

animate(options: AnimationOptions, handler: () => void): void

设置背板蒙版颜色变化动效，在OnDrop和OnDragEnd回调中使用不生效，仅支持通过 [getDragPreview()](arkts-apis-uicontext-dragcontroller.md#getdragpreview11) 方法获取到的对象上使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [AnimationOptions](js-apis-arkui-dragcontroller.md#animationoptions11) | 是 | 动效参数。 |
| handler | () => void | 是 | 用于修改背板蒙版颜色等属性的回调方法。 |

**示例：**

说明

推荐通过使用[UIContext](arkts-apis-uicontext-uicontext.md)中的[getDragController](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取当前UI上下文关联的DragController对象。

1. 在EntryAbility.ets中获取UI上下文并保存至LocalStorage中。

   ```
   1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { window, UIContext } from '@kit.ArkUI';

   5. let uiContext: UIContext;
   6. let localStorage: LocalStorage = new LocalStorage('uiContext');

   8. export default class EntryAbility extends UIAbility {
   9. storage: LocalStorage = localStorage;

   11. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
   12. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
   13. }

   15. onDestroy(): void {
   16. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
   17. }

   19. onWindowStageCreate(windowStage: window.WindowStage): void {
   20. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

   22. windowStage.loadContent('pages/Index', this.storage, (err, data) => {
   23. if (err.code) {
   24. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s',
   25. `Code is ${err.code}, message is ${err.message}`);
   26. return;
   27. }
   28. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s',
   29. `Code is ${err.code}, message is ${err.message}`);
   30. windowStage.getMainWindow((err, data) => {
   31. if (err.code) {
   32. hilog.error(0x0000, `Failed to obtain the main window. Cause: ${err.message}`, '');
   33. return;
   34. }
   35. uiContext = data.getUIContext();
   36. this.storage.setOrCreate<UIContext>('uiContext', uiContext);
   37. })
   38. });
   39. }
   40. }
   ```
2. 在Index.ets中通过this.getUIContext().getSharedLocalStorage()获取UI上下文，进而获取DragController对象实施后续操作。

   ```
   1. import { unifiedDataChannel } from '@kit.ArkData';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import { dragController, curves, promptAction, UIContext } from '@kit.ArkUI';
   4. import { image } from '@kit.ImageKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';

   7. class DragInfo {
   8. event: DragEvent | undefined = undefined;
   9. extraParams: string = '';
   10. }

   12. @Entry()
   13. @Component
   14. struct DragControllerPage {
   15. @State pixmap: image.PixelMap | null = null;
   16. storages = this.getUIContext().getSharedLocalStorage();

   18. @Builder
   19. DraggingBuilder() {
   20. Column() {
   21. Text("DraggingBuilder")
   22. .fontColor(Color.White)
   23. .fontSize(12)
   24. }
   25. .width(100)
   26. .height(100)
   27. .backgroundColor(Color.Blue)
   28. }

   30. @Builder
   31. PixmapBuilder() {
   32. Column() {
   33. Text("PixmapBuilder")
   34. }
   35. .width(100)
   36. .height(100)
   37. .backgroundColor(Color.Blue)
   38. }

   40. build() {
   41. Column() {
   42. Button('拖拽至此处')
   43. .margin(10)
   44. .onDragEnter(() => {
   45. try {
   46. let uiContext: UIContext = this.storages?.get<UIContext>('uiContext') as UIContext;
   47. let previewObj: dragController.DragPreview = uiContext.getDragController().getDragPreview();
   48. let foregroundColor: ResourceColor = Color.Green;

   50. let previewAnimation: dragController.AnimationOptions = {
   51. curve: curves.cubicBezierCurve(0.2, 0, 0, 1),
   52. }
   53. previewObj.animate(previewAnimation, () => {
   54. previewObj.setForegroundColor(foregroundColor);
   55. });
   56. } catch (error) {
   57. let msg = (error as BusinessError).message;
   58. let code = (error as BusinessError).code;
   59. hilog.error(0x0000, `show error code is ${code}, message is ${msg}`, '');
   60. }
   61. })
   62. .onDrop(() => {
   63. this.getUIContext().getPromptAction().showToast({ duration: 100, message: 'Drag Success', bottom: 400 })
   64. })
   65. Button('拖起').onTouch((event?: TouchEvent) => {
   66. if (event) {
   67. if (event.type == TouchType.Down) {
   68. let text = new unifiedDataChannel.Text()
   69. let unifiedData = new unifiedDataChannel.UnifiedData(text)
   70. let dragInfo: dragController.DragInfo = {
   71. pointerId: 0,
   72. data: unifiedData,
   73. extraParams: ''
   74. }
   75. let eve: DragInfo = new DragInfo();
   76. this.getUIContext()
   77. .getDragController()
   78. .executeDrag(() => { // 建议使用 this.getUIContext().getDragController().executeDrag()接口
   79. this.DraggingBuilder()
   80. }, dragInfo, (err, eve) => {
   81. hilog.info(0x0000, `${JSON.stringify(err)}`, '')
   82. if (eve && eve.event) {
   83. if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
   84. hilog.info(0x0000, 'success', '');
   85. } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
   86. hilog.info(0x0000, 'failed', '');
   87. }
   88. }
   89. })
   90. }
   91. }
   92. }).margin({ top: 100 })
   93. }
   94. .width('100%')
   95. .height('100%')
   96. }
   97. }
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/cpFyhXLFQm6jVvvwwUZxLw/zh-cn_image_0000002552799754.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000015Z&HW-CC-Expire=86400&HW-CC-Sign=3B7E55A530809C7952A630DD57B885EC4F585B7AC9A5ED50005B4A94591C99CC)

## DragStartRequestStatus18+

PhonePC/2in1TabletTVWearable

定义应用是否可以发起拖拽的枚举类型。仅在[onDragStart](ts-universal-events-drag-drop.md#ondragstart)调用时有效。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WAITING | 0 | 应用在准备数据阶段，无法发起拖拽。 |
| READY | 1 | 应用数据准备完成，可以发起拖拽。 |

## DragSpringLoadingState20+

PhonePC/2in1TabletTVWearable

定义拖拽的悬停检测状态的枚举类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BEGIN | - | 拖拽进入组件范围静止一段时间，被识别为悬停状态。此时允许进行一些悬停检测的准备操作。 |
| UPDATE | - | 拖拽已处于悬停状态，如果继续静止会定期触发UPDATE通知，以检查悬停状态。此时允许UI效果刷新以突出悬停状态。 |
| END | - | 如果最后一次UPDATE通知后拖拽继续静止会进入END，整个悬停检测结束。进入END后拖拽需要移出组件范围后再次进入组件或移入组件内子组件才会重新开始悬停检测。此时应用程序可进行清理、导航或视图切换操作。 |
| CANCEL | - | 拖拽进入BEGIN后，在手指/鼠标抬起、切换窗口、息屏、移出组件范围、移入组件内子组件或组件内移动超过检测阈值等场景会触发CANCEL通知，悬停检测中断。应用程序将恢复UI样式，并取消待定的导航及视图切换操作。 |

## DragSpringLoadingConfiguration20+

PhonePC/2in1TabletTVWearable

定义拖拽的悬停检测配置参数的接口。默认的配置参数通常已能满足需求。可以通过在绑定[onDragSpringLoading](ts-universal-events-drag-drop.md#ondragspringloading20)时指定配置，或者通过在BEGIN状态期间使用[updateConfiguration](js-apis-arkui-dragcontroller.md#updateconfiguration20)方法动态修改的方式以自定义该配置参数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stillTimeLimit | number | 否 | 是 | 进入悬停检测BEGIN状态所需保持静止的时间（ms）。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值500。 |
| updateInterval | number | 否 | 是 | 进入悬停检测UPDATE状态后，更新通知的时间间隔（ms）。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值100。 |
| updateNotifyCount | number | 否 | 是 | 进入悬停检测UPDATE状态后，更新通知的最大次数。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值3。 |
| updateToFinishInterval | number | 否 | 是 | 从UPDATE状态到END状态的最长等待时间（ms）。取值范围为[0, 231-1]的整数。输入浮点数时只取整数部分。输入非法值（负数、null、undefined、NaN）时取默认值100。 |

## SpringLoadingDragInfos20+

PhonePC/2in1TabletTVWearable

定义触发悬停检测时拖拽事件信息的接口。该接口提供了拖拽数据摘要和拖拽事件额外信息，应用程序可以据此决定是否响应悬停检测回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| dataSummary | [unifiedDataChannel.Summary](js-apis-data-unifieddatachannel.md#summary) | 否 | 是 | 拖拽数据的摘要，默认为null。 |
| extraInfos | string | 否 | 是 | 拖拽事件额外信息，默认为空字符串。 |

## SpringLoadingContext20+

PhonePC/2in1TabletTVWearable

定义回调上下文信息的类，用于在悬停检测回调中传递给应用程序，使其能访问拖拽状态、动态刷新UI效果以及访问拖拽数据以确定是否处理拖拽操作。

### 属性

PhonePC/2in1TabletTVWearable

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [DragSpringLoadingState](js-apis-arkui-dragcontroller.md#dragspringloadingstate20) | 否 | 否 | 当前悬停检测的状态。 |
| currentNotifySequence | number | 否 | 否 | 在一次悬停检测流转中的回调通知次数，从0开始。 |
| dragInfos | [SpringLoadingDragInfos](js-apis-arkui-dragcontroller.md#springloadingdraginfos20) | 否 | 是 | 拖拽信息，当悬停检测状态为CANCEL时缺失，为undefined时取[SpringLoadingDragInfos](js-apis-arkui-dragcontroller.md#springloadingdraginfos20)默认值。 |
| currentConfig | [DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20) | 否 | 是 | 当前回调中的配置信息，当悬停检测状态为CANCEL时缺失，为undefined时取[DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20)默认值。 |

### abort20+

PhonePC/2in1TabletTVWearable

abort(): void

终止后续的悬停检测。本方法不会触发CANCEL状态通知，应用程序需要在执行本方法时进行状态清理。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### updateConfiguration20+

PhonePC/2in1TabletTVWearable

updateConfiguration(config: DragSpringLoadingConfiguration): void

更新悬停检测的配置，仅在悬停检测状态为BEGIN时生效。应用程序通常在绑定[onDragSpringLoading](ts-universal-events-drag-drop.md#ondragspringloading20)时设置悬停检测配置或使用默认配置。该方法不会修改绑定时的原始配置，而是在后续悬停检测中更新动态的配置信息。请谨慎使用本方法，因为不同的拖拽数据类型可能需要不同的UX时间。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [DragSpringLoadingConfiguration](js-apis-arkui-dragcontroller.md#dragspringloadingconfiguration20) | 是 | 悬停检测配置。 |
