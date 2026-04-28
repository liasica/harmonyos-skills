---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dragcontroller
title: Class (DragController)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (DragController)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:21+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a7a1a4d6feb78402d7128044a8ccca369411d48048a1516029ac010fc98bd48e
---

提供发起主动拖拽的能力，当应用接收到触摸或长按等事件时可以主动发起拖拽的动作，并在其中携带拖拽信息。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 11开始支持。
* 以下API需先使用UIContext中的[getDragController()](arkts-apis-uicontext-uicontext.md#getdragcontroller11)方法获取DragController实例，再通过此实例调用对应方法。

## executeDrag11+

PhonePC/2in1TabletTVWearable

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo, callback: AsyncCallback<dragController.DragEventParam>): void

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。通过回调返回拖拽事件结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 拖拽发起后跟手效果所拖拽的对象。  **说明：**  不支持全局builder。如果builder中使用了[Image](ts-basic-components-image.md)组件，应尽量开启同步加载，即配置Image的[syncLoad](ts-basic-components-image.md#syncload8)为true。该builder只用于生成当次拖拽中显示的图片。builder的根组件宽高为0时，无法生成拖拽显示的图片导致拖拽失败。builder的修改不会同步到当前正在拖拽的图片，对builder的修改需要在下一次拖拽时生效。 |
| dragInfo | [dragController.DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息。 |
| callback | [AsyncCallback](js-apis-base.md#asynccallback)<[dragController.DragEventParam](js-apis-arkui-dragcontroller.md#drageventparam12)> | 是 | 拖拽结束返回结果的回调  - event：拖拽事件信息，仅包括拖拽结果。  - extraParams：拖拽事件额外信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

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
12. @Builder
13. DraggingBuilder() {
14. Column() {
15. Text("DraggingBuilder")
16. }
17. .width(100)
18. .height(100)
19. .backgroundColor(Color.Blue)
20. }

22. build() {
23. Column() {
24. Button('touch to execute drag')
25. .onTouch((event?: TouchEvent) => {
26. if (event) {
27. if (event.type == TouchType.Down) {
28. let text = new unifiedDataChannel.Text();
29. let unifiedData = new unifiedDataChannel.UnifiedData(text);

31. let dragInfo: dragController.DragInfo = {
32. pointerId: 0,
33. data: unifiedData,
34. extraParams: ''
35. };
36. let eve: DragInfo = new DragInfo();
37. this.getUIContext().getDragController().executeDrag(() => {
38. this.DraggingBuilder()
39. }, dragInfo, (err, eve) => {
40. if (eve.event) {
41. if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
42. // ...
43. } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
44. // ...
45. }
46. }
47. })
48. }
49. }
50. })
51. }
52. .width('100%')
53. .height('100%')
54. }
55. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/hY1xb5eLSM---c52Z6HsYw/zh-cn_image_0000002583439453.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=6ED1ED66DB9606E3BA059AF6686908A8E0D1C346A53B77531212438F66E8EEC6)

## executeDrag11+

PhonePC/2in1TabletTVWearable

executeDrag(custom: CustomBuilder | DragItemInfo, dragInfo: dragController.DragInfo): Promise<dragController.DragEventParam>

主动发起拖拽能力，传入拖拽发起后跟手效果所拖拽的对象以及携带拖拽信息。通过Promise返回拖拽事件结果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| custom | [CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo) | 是 | 拖拽发起后跟手效果所拖拽的对象。 |
| dragInfo | [dragController.DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[dragController.DragEventParam](js-apis-arkui-dragcontroller.md#drageventparam12)> | 拖拽结束返回结果的回调  - event：拖拽事件信息，仅包括拖拽结果。  - extraParams：拖拽事件额外信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

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
13. @State pixmap: image.PixelMap | null = null;

15. @Builder
16. DraggingBuilder() {
17. Column() {
18. Text("DraggingBuilder")
19. }
20. .width(100)
21. .height(100)
22. .backgroundColor(Color.Blue)
23. }

25. @Builder
26. PixmapBuilder() {
27. Column() {
28. Text("PixmapBuilder")
29. }
30. .width(100)
31. .height(100)
32. .backgroundColor(Color.Blue)
33. }

35. build() {
36. Column() {
37. Button('touch to execute drag')
38. .onTouch((event?: TouchEvent) => {
39. if (event) {
40. if (event.type == TouchType.Down) {
41. let text = new unifiedDataChannel.Text();
42. let unifiedData = new unifiedDataChannel.UnifiedData(text);

44. let dragInfo: dragController.DragInfo = {
45. pointerId: 0,
46. data: unifiedData,
47. extraParams: ''
48. };
49. let pb: CustomBuilder = (): void => {
50. this.PixmapBuilder()
51. };
52. this.getUIContext().getComponentSnapshot().createFromBuilder(pb).then((pix: image.PixelMap) => {
53. this.pixmap = pix;
54. let dragItemInfo: DragItemInfo = {
55. pixelMap: this.pixmap,
56. builder: () => {
57. this.DraggingBuilder()
58. },
59. extraInfo: "DragItemInfoTest"
60. };
61. let eve: DragInfo = new DragInfo();
62. this.getUIContext()
63. .getDragController()
64. .executeDrag(dragItemInfo, dragInfo)
65. .then((eve) => {
66. if (eve.event.getResult() == DragResult.DRAG_SUCCESSFUL) {
67. // ...
68. } else if (eve.event.getResult() == DragResult.DRAG_FAILED) {
69. // ...
70. }
71. })
72. .catch((err: Error) => {
73. })
74. })
75. }
76. }
77. })
78. }
79. .width('100%')
80. .height('100%')
81. }
82. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/eXEE2PRYS_eh8pS0wOQPhA/zh-cn_image_0000002552959408.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=C26F43CC0ACF77B0307789A52A79BC53D0D4C2A31CB55DCC670DC7265FE23C71)

## createDragAction11+

PhonePC/2in1TabletTVWearable

createDragAction(customArray: Array<CustomBuilder | DragItemInfo>, dragInfo: dragController.DragInfo): dragController.DragAction

创建拖拽的Action对象，需要显式指定拖拽背板图（可多个），以及拖拽的数据，跟手点等信息；当通过一个已创建的Action对象发起的拖拽未结束时，无法再次创建新的Action对象，接口会抛出异常；当Action对象的生命周期结束后，注册在该对象上的回调函数会失效，因此需要在一个尽量长的作用域下持有该对象，并在每次发起拖拽前通过createDragAction返回新的对象覆盖旧值。

说明

建议控制传递的拖拽背板数量，传递过多容易导致拖起的效率问题。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| customArray | Array<[CustomBuilder](ts-types.md#custombuilder8) | [DragItemInfo](ts-universal-events-drag-drop.md#dragiteminfo)> | 是 | 拖拽发起后跟手效果所拖拽的对象。 |
| dragInfo | [dragController.DragInfo](js-apis-arkui-dragcontroller.md#draginfo) | 是 | 拖拽信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [dragController.DragAction](js-apis-arkui-dragcontroller.md#dragaction11) | 创建拖拽Action对象，主要用于后面实现注册监听拖拽状态改变事件和启动拖拽服务。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2.Incorrect parameters types; 3. Parameter verification failed. |
| 100001 | Internal handling failed. |

**示例：**

1.在EntryAbility.ets中获取UI上下文并保存至LocalStorage中。

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
20. // Main window is created, set main page for this ability
21. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

23. windowStage.loadContent('pages/Index', this.storage, (err, data) => {
24. if (err.code) {
25. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
26. return;
27. }
28. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
29. windowStage.getMainWindow((err, data) => {
30. if (err.code) {
31. console.error(`Failed to obtain the main window. Cause:${err.message}`);
32. return;
33. }
34. let windowClass: window.Window = data;
35. uiContext = windowClass.getUIContext();
36. this.storage.setOrCreate<UIContext>('uiContext', uiContext);
37. // 获取UIContext实例
38. });
39. });
40. }

42. onWindowStageDestroy(): void {
43. // Main window is destroyed, release UI related resources
44. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
45. }

47. onForeground(): void {
48. // Ability has brought to foreground
49. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
50. }

52. onBackground(): void {
53. // Ability has back to background
54. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
55. }
56. }
```

2.通过this.getUIContext().getSharedLocalStorage()获取上下文，进而获取DragController对象实施后续操作。

```
1. import { dragController, componentSnapshot, UIContext, DragController } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';
3. import { unifiedDataChannel } from '@kit.ArkData';

5. @Entry()
6. @Component
7. struct DragControllerPage {
8. @State pixmap: image.PixelMap | null = null;
9. private dragAction: dragController.DragAction | null = null;
10. customBuilders: Array<CustomBuilder | DragItemInfo> = new Array<CustomBuilder | DragItemInfo>();
11. storages = this.getUIContext().getSharedLocalStorage();

13. @Builder
14. DraggingBuilder() {
15. Column() {
16. Text("DraggingBuilder")
17. }
18. .width(100)
19. .height(100)
20. .backgroundColor(Color.Blue)
21. }

23. build() {
24. Column() {
25. Button('多对象dragAction customBuilder拖拽').onTouch((event?: TouchEvent) => {
26. if (event) {
27. if (event.type == TouchType.Down) {
28. console.info("multi drag Down by listener");
29. this.customBuilders.push(() => {
30. this.DraggingBuilder()
31. });
32. this.customBuilders.push(() => {
33. this.DraggingBuilder()
34. });
35. this.customBuilders.push(() => {
36. this.DraggingBuilder()
37. });
38. let text = new unifiedDataChannel.Text();
39. let unifiedData = new unifiedDataChannel.UnifiedData(text);
40. let dragInfo: dragController.DragInfo = {
41. pointerId: 0,
42. data: unifiedData,
43. extraParams: ''
44. };
45. try {
46. let uiContext: UIContext = this.storages?.get<UIContext>('uiContext') as UIContext;
47. this.dragAction = uiContext.getDragController().createDragAction(this.customBuilders, dragInfo);
48. if (!this.dragAction) {
49. console.info("listener dragAction is null");
50. return;
51. }
52. this.dragAction.on('statusChange', (dragAndDropInfo) => {
53. if (dragAndDropInfo.status == dragController.DragStatus.STARTED) {
54. console.info("drag has start");
55. } else if (dragAndDropInfo.status == dragController.DragStatus.ENDED) {
56. console.info("drag has end");
57. if (!this.dragAction) {
58. return;
59. }
60. this.customBuilders.splice(0, this.customBuilders.length);
61. this.dragAction.off('statusChange');
62. }
63. })
64. this.dragAction.startDrag().then(() => {
65. }).catch((err: Error) => {
66. console.error(`start drag Error:${err.message}`);
67. })
68. } catch (err) {
69. console.error(`create dragAction Error:${err.message}`);
70. }
71. }
72. }
73. }).margin({ top: 20 })
74. }
75. .width('100%')
76. .height('100%')
77. }
78. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/4YVDJYbLTR2jK6KFBT9dJw/zh-cn_image_0000002583479409.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=FF4F1011B679D9D14D1B0C669067652A5054FF46A468D71AF62DAEF3FA5B3A94)

## getDragPreview11+

PhonePC/2in1TabletTVWearable

getDragPreview(): dragController.DragPreview

返回一个代表拖拽背板的对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [dragController.DragPreview](js-apis-arkui-dragcontroller.md#dragpreview11) | 一个代表拖拽背板的对象，提供背板样式设置的接口，在OnDrop和OnDragEnd回调中使用不生效。 |

**错误码：** 通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

**示例：**

请参考[animate](js-apis-arkui-dragcontroller.md#animate11)示例。

## setDragEventStrictReportingEnabled12+

PhonePC/2in1TabletTVWearable

setDragEventStrictReportingEnabled(enable: boolean): void

当目标从父组件拖拽到子组件时，通过该方法设置是否会触发父组件的onDragLeave的回调。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 将目标从父组件拖拽到子组件时，是否会触发父组件的onDragLeave的回调。true表示触发父组件的onDragLeave的回调，false表示不触发。 |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window, UIContext } from '@kit.ArkUI';

4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage): void {
6. windowStage.loadContent('pages/Index', (err, data) => {
7. if (err.code) {
8. return;
9. }
10. windowStage.getMainWindow((err, data) => {
11. if (err.code) {
12. return;
13. }
14. let windowClass: window.Window = data;
15. let uiContext: UIContext = windowClass.getUIContext();
16. uiContext.getDragController().setDragEventStrictReportingEnabled(true);
17. });
18. });
19. }
20. }
```

## cancelDataLoading15+

PhonePC/2in1TabletTVWearable

cancelDataLoading(key: string): void

当使用[startDataLoading](ts-universal-events-drag-drop.md#startdataloading15)获取拖拽数据时，可调用该接口取消数据传输。仅可在拖拽释放后调用。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 拖拽数据的标识，用于区分每次拖拽。key可通过startDataLoading接口获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[拖拽事件错误码](errorcode-drag-event.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. |
| 190004 | Operation failed. |

## notifyDragStartRequest18+

PhonePC/2in1TabletTVWearable

notifyDragStartRequest(requestStatus: dragController.DragStartRequestStatus): void

控制应用是否可以发起拖拽。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestStatus | [dragController.DragStartRequestStatus](js-apis-arkui-dragcontroller.md#dragstartrequeststatus18) | 是 | 定义应用是否可以发起拖拽。 |

**示例：**

```
1. // xxx.ets
2. import { unifiedDataChannel } from '@kit.ArkData';
3. import { image } from '@kit.ImageKit';
4. import { dragController } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct NormalEts {
9. @State finished: boolean = false;
10. @State timeout1: number = 1;
11. @State pixmap: image.PixelMap | undefined = undefined;
12. @State unifiedData1: unifiedDataChannel.UnifiedData | undefined = undefined;
13. @State previewData: DragItemInfo | undefined = undefined;

15. loadData() {
16. // 设置4s后才能发起拖拽
17. let timeout = setTimeout(() => {
18. this.getUIContext().getComponentSnapshot().get("image1", (error: Error, pixmap: image.PixelMap) => {
19. this.pixmap = pixmap;
20. this.previewData = {
21. pixelMap: this.pixmap
22. };
23. });

25. let data: unifiedDataChannel.Image = new unifiedDataChannel.Image();
26. data.imageUri = "app.media.startIcon";
27. let unifiedData = new unifiedDataChannel.UnifiedData(data);
28. this.unifiedData1 = unifiedData;

30. this.getUIContext().getDragController().notifyDragStartRequest(dragController.DragStartRequestStatus.READY);
31. }, 4000);
32. this.timeout1 = timeout;
33. }

35. build() {
36. Column({ space: 20 }) {
37. Image($r("app.media.startIcon"))
38. .width(150)
39. .height(150)
40. .id("image1")
41. .draggable(true)
42. .dragPreview(this.previewData)
43. .onPreDrag((status: PreDragStatus) => {
44. if (status == PreDragStatus.PREPARING_FOR_DRAG_DETECTION) {
45. this.loadData();
46. } else {
47. clearTimeout(this.timeout1);
48. }
49. })
50. .onDragStart((event: DragEvent) => {
51. if (this.finished == false) {
52. this.getUIContext()
53. .getDragController()
54. // 应用数据准备阶段，无法发起拖拽
55. .notifyDragStartRequest(dragController.DragStartRequestStatus.WAITING);
56. } else {
57. event.setData(this.unifiedData1);
58. }
59. })
60. .onDragEnd(() => {
61. this.finished = false;
62. })
63. }
64. .width('100%')
65. .height(400)
66. }
67. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/rY4Uyf63TKq8r3pcQe_tyA/zh-cn_image_0000002552799760.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=BD11689304503C5EA9832124116C1E9C4D86CBB2A200FD00660F8E390BD0043A)

## enableDropDisallowedBadge20+

PhonePC/2in1TabletTVWearable

enableDropDisallowedBadge(enabled: boolean): void

当组件的类型与配置的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)无交集时可显示禁用角标。通常，当组件可以接收或处理拖拽数据，或当它返回DragBehavior.COPY向系统声明数据以复制方式处理时，拖拽对象会显示加号及数据编号的角标。如果返回DragBehavior.MOVE以向系统声明数据以剪切方式处理，拖拽对象将只显示数据编号的角标。当目标进行拖拽时，若系统决定或组件显式声明无法处理拖拽数据，可通过该方法检查是否应显示拖拽禁止角标。该接口暂不支持[UIExtension](js-apis-arkui-uiextension.md)。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 当组件的类型与配置的[allowDrop](ts-universal-attributes-drag-drop.md#allowdrop)无交集时可显示禁用角标，当目标进行拖拽时，通过enableDropDisallowedBadge方法检查是否显示拖拽禁止角标。true表示显示拖拽禁止角标，false表示不显示拖拽禁止角标。默认值为false。 |

**示例：**

该示例通过enableDropDisallowedBadge接口实现了对目标进行拖拽时显示拖拽禁止角标的功能。

1. 在EntryAbility.ets中调用enableDropDisallowedBadge接口，设置enabled参数为true。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { window, UIContext } from '@kit.ArkUI';

   4. export default class EntryAbility extends UIAbility {
   5. onWindowStageCreate(windowStage: window.WindowStage): void {
   6. windowStage.loadContent('pages/Index', (err, data) => {
   7. if (err.code) {
   8. return;
   9. }
   10. windowStage.getMainWindow((err, data) => {
   11. if (err.code) {
   12. return;
   13. }
   14. let windowClass: window.Window = data;
   15. let uiContext: UIContext = windowClass.getUIContext();
   16. uiContext.getDragController().enableDropDisallowedBadge(true);
   17. });
   18. });
   19. }
   20. }
   ```
2. 在Index.ets中拖拽图标icon至下方空白区域，显示拖拽禁止角标。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. build() {
   5. Column({ space: 20 }) {
   6. // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
   7. Image($r('app.media.startIcon'))
   8. .width(120)
   9. .height(120)
   10. Text('这里是不能落入区域')
   11. Column()
   12. .width('100%')
   13. .layoutWeight(1)
   14. .allowDrop(null)
   15. .onDrop(() => {
   16. })
   17. }.width('100%')
   18. }
   19. }
   ```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/5M9RmkGvRfC-YbmHl_IVig/zh-cn_image_0000002583439455.png?HW-CC-KV=V1&HW-CC-Date=20260428T000020Z&HW-CC-Expire=86400&HW-CC-Sign=0B4A848BD1FC99C6FB347BB8000E20C91A291A3341C376C9C2184C61E6A68F4C)
