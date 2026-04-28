---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-popup-and-menu-components-uicontext-popup
title: 不依赖UI组件的全局气泡提示 (openPopup)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 气泡提示 > 不依赖UI组件的全局气泡提示 (openPopup)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6122887a7713c660fb8034a0dfa31098ce8573efbd6b2244e2904d014874f517
---

[气泡提示（Popup）](arkts-popup-and-menu-components-popup.md)在使用时依赖绑定UI组件，否则无法使用。从API version 18开始，可以通过使用全局接口[openPopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openpopup18)的方式，在无UI组件的场景下直接或封装使用，例如在事件回调中使用或封装后对外提供能力。

## 弹出气泡

通过[openPopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#openpopup18)可以弹出气泡。

```
1. this.promptAction.openPopup(this.contentNode, { id: targetId }, {
2. enableArrow: true
3. })
4. .then(() => {
5. hilog.info(0xFF00, 'popupBuildText', 'openPopup success');
6. })
7. .catch((err: BusinessError) => {
8. hilog.error(0xFF00, 'popupBuildText', 'openPopup error: ' + err.code + ' ' + err.message);
9. });
```

[PopupBuildText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/PopupBuildText.ets#L93-L103)

### 创建ComponentContent

通过调用openPopup接口弹出气泡，需要定义ComponentContent，以提供自定义弹出框的内容。详细规格可参考[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)说明。

```
1. private contentNode: ComponentContent<Object> =
2. new ComponentContent(this.uiContext, wrapBuilder(buildText), this.message);
```

[OpenPopup.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/OpenPopup.ets#L63-L66)

如果在wrapBuilder中包含其他组件（例如：[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Chip](../harmonyos-references/ohos-arkui-advanced-chip.md)组件），则应在创建ComponentContent时设置[nestingBuilderSupported](../harmonyos-references/js-apis-arkui-buildernode.md#buildoptions12)属性为true。

```
1. @Builder
2. export function buildText(params: Params) {
3. Popup({
4. // 类型设置图标内容。
5. icon: {
6. // 请将$r('app.media.app_icon')替换为实际资源文件
7. image: $r('app.media.app_icon'),
8. width: 32,
9. height: 32,
10. fillColor: Color.White,
11. borderRadius: 10
12. } as PopupIconOptions,
13. // 设置文字内容。
14. title: {
15. text: `This is a Popup title 1`,
16. fontSize: 20,
17. fontColor: Color.Black,
18. fontWeight: FontWeight.Normal
19. } as PopupTextOptions,
20. // 设置文字内容。
21. message: {
22. text: `This is a Popup message 1`,
23. fontSize: 15,
24. fontColor: Color.Black
25. } as PopupTextOptions,
26. // 设置按钮内容。
27. buttons: [{
28. text: 'confirm',
29. action: () => {
30. hilog.info(0xFF00, 'popupBuildText', 'confirm button click');
31. },
32. fontSize: 15,
33. fontColor: Color.Black,
34. },
35. {
36. text: 'cancel',
37. action: () => {
38. hilog.info(0xFF00, 'popupBuildText', 'cancel button click');
39. },
40. fontSize: 15,
41. fontColor: Color.Black
42. },] as [PopupButtonOptions?, PopupButtonOptions?]
43. });
44. }

46. let contentNode: ComponentContent<Object> =
47. new ComponentContent(uiContext, wrapBuilder(buildText), message, { nestingBuilderSupported: true });
```

[PopupBuildText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/PopupBuildText.ets#L32-L81)

### 绑定组件信息

通过调用openPopup接口弹出气泡，需要提供绑定组件的信息[TargetInfo](../harmonyos-references/arkts-apis-uicontext-i.md#targetinfo18)。若未传入有效的target，气泡将无法弹出。

目前有两种设置target的方式。

* target的id属性设置为number类型，此时需要将id设置为对应组件的UniqueID，组件的UniqueID由系统保证唯一性。

  ```
  1. let frameNode: FrameNode | null = this.uiContext.getFrameNodeByUniqueId(this.getUniqueId());
  2. let targetId = frameNode?.getChild(0)?.getUniqueId();
  ```

  [OpenPopup.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/OpenPopup.ets#L78-L81)
* target的id属性设置为string类型，此时需要将id设置为对应组件的通用属性[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)值。当无法保证id的唯一性时，如多团队开发或者复用自定义组件，可以通过设置componentId属性明确指定此id的范围来精确指定target，此时componentId属性可以设置为对应组件的父组件或者所在自定义组件的UniqueID。

  ```
  1. build() {
  2. NavDestination() {
  3. Column() {
  4. Row() {
  5. Button('button1')
  6. .id(this.targetIdString)
  7. }

  9. Row() {
  10. Button('button2')
  11. .id(this.targetIdString)
  12. }

  14. Button('openPopup')
  15. .onClick(() => {
  16. let frameNode: FrameNode | null = this.uiContext.getFrameNodeByUniqueId(this.getUniqueId());
  17. let componentId = frameNode?.getChild(1)?.getChild(0)?.getChild(1)?.getUniqueId();
  18. if (componentId == undefined) {
  19. this.componentId = 0;
  20. } else {
  21. this.componentId = componentId;
  22. }
  23. this.promptActionClass.setPromptAction(this.promptAction);
  24. this.promptActionClass.setContentNode(this.contentNode);
  25. this.promptActionClass.setOptions(this.options);
  26. this.promptActionClass.setIsPartialUpdate(false);
  27. this.promptActionClass.setTarget({ id: this.targetIdString, componentId: this.componentId });
  28. this.promptActionClass.openPopup();
  29. })
  30. }
  31. }
  32. }
  ```

  [OpenPopupWithTargetIdString.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/OpenPopupWithTargetIdString.ets#L65-L98)

### 设置弹出气泡样式

通过调用openPopup接口弹出气泡，可以设置[PopupCommonOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupcommonoptions18类型说明)属性调整气泡样式。

```
1. private options: PopupCommonOptions = { enableArrow: true };
```

[OpenPopup.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/OpenPopup.ets#L67-L70)

## 更新气泡样式

从API version 18开始，通过[updatePopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatepopup18)可以更新气泡的样式。支持全量更新和增量更新其气泡样式，不支持更新[PopupCommonOptions](../harmonyos-references/ts-universal-attributes-popup.md#popupcommonoptions18类型说明)中的showInSubWindow、focusable、onStateChange、onWillDismiss和transition属性。

```
1. this.promptAction.updatePopup(this.contentNode, {
2. enableArrow: false
3. }, true)
4. .then(() => {
5. hilog.info(0xFF00, 'popupBuildText', 'updatePopup success');
6. })
7. .catch((err: BusinessError) => {
8. hilog.error(0xFF00, 'popupBuildText', 'updatePopup error: ' + err.code + ' ' + err.message);
9. });
```

[PopupBuildText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/PopupBuildText.ets#L107-L117)

## 关闭气泡

从API version 18开始，通过调用[closePopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closepopup18)可以关闭气泡。

```
1. this.promptAction.closePopup(this.contentNode)
2. .then(() => {
3. hilog.info(0xFF00, 'popupBuildText', 'closePopup success');
4. })
5. .catch((err: BusinessError) => {
6. hilog.error(0xFF00, 'popupBuildText', 'closePopup error: ' + err.code + ' ' + err.message);
7. });
```

[PopupBuildText.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/PopupBuildText.ets#L121-L129)

说明

由于[updatePopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatepopup18)和[closePopup](../harmonyos-references/arkts-apis-uicontext-promptaction.md#closepopup18)依赖content来更新或者关闭指定的气泡，开发者需自行维护传入的content。

## 在HAR包中使用全局气泡提示

以下示例通过[HAR](har-package.md)包封装一个Popup，从而对外提供气泡的弹出、更新和关闭能力。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent, TargetInfo, PromptAction } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. export class PromptActionClass {
6. private promptAction: PromptAction | null = null;
7. private contentNode: ComponentContent<Object> | null = null;
8. private options: PopupCommonOptions | null = null;
9. private target: TargetInfo | null = null;
10. private isPartialUpdate: boolean = false;

12. public setPromptAction(promptAction: PromptAction) {
13. this.promptAction = promptAction;
14. }

16. public setContentNode(node: ComponentContent<Object>) {
17. this.contentNode = node;
18. }

20. public setTarget(target: TargetInfo) {
21. this.target = target;
22. }

24. public setOptions(options: PopupCommonOptions) {
25. this.options = options;
26. }

28. public setIsPartialUpdate(isPartialUpdate: boolean) {
29. this.isPartialUpdate = isPartialUpdate;
30. }

32. public openPopup() {
33. if (this.promptAction != null) {
34. this.promptAction.openPopup(this.contentNode, this.target, this.options)
35. .then(() => {
36. hilog.info(0xFF00, 'popupMainPage', 'openPopup success');
37. })
38. .catch((err: BusinessError) => {
39. hilog.error(0xFF00, 'popupMainPage', 'openPopup error: ' + err.code + ' ' + err.message);
40. });
41. }
42. }

44. public closePopup() {
45. if (this.promptAction != null) {
46. this.promptAction.closePopup(this.contentNode)
47. .then(() => {
48. hilog.info(0xFF00, 'popupMainPage', 'closePopup success');
49. })
50. .catch((err: BusinessError) => {
51. hilog.error(0xFF00, 'popupMainPage', 'closePopup error: ' + err.code + ' ' + err.message);
52. });
53. }
54. }

56. public updatePopup(options: PopupCommonOptions) {
57. if (this.promptAction != null) {
58. this.promptAction.updatePopup(this.contentNode, options, this.isPartialUpdate)
59. .then(() => {
60. hilog.info(0xFF00, 'popupMainPage', 'updatePopup success');
61. })
62. .catch((err: BusinessError) => {
63. hilog.error(0xFF00, 'popupMainPage', 'updatePopup error: ' + err.code + ' ' + err.message);
64. });
65. }
66. }
67. }
```

[PopupMainPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/PopupMainPage.ets#L16-L85)

```
1. import { PromptActionClass } from './PopupMainPage';
2. import { ComponentContent, PromptAction } from '@kit.ArkUI';

4. const ID: number = 0;

6. class Params {
7. public text: string = '';
8. public promptActionClass: PromptActionClass = new PromptActionClass();

10. constructor(text: string, promptActionClass: PromptActionClass) {
11. this.text = text;
12. this.promptActionClass = promptActionClass;
13. }
14. }

16. @Builder
17. function buildText(params: Params) {
18. Column() {
19. Text(params.text)
20. .fontSize(20)
21. .margin({ top: 10 })
22. Button('Update')
23. .margin({ top: 10 })
24. .width(100)
25. .onClick(() => {
26. params.promptActionClass.updatePopup({
27. enableArrow: false,
28. });
29. })
30. Button('Close')
31. .margin({ top: 10 })
32. .width(100)
33. .onClick(() => {
34. params.promptActionClass.closePopup();
35. })
36. }.width(130).height(150)
37. }

39. @Entry
40. @Component
41. export struct OpenPopup {
42. @State message: string = 'hello';
43. private uiContext: UIContext = this.getUIContext();
44. private promptAction: PromptAction = this.uiContext.getPromptAction();
45. private promptActionClass: PromptActionClass = new PromptActionClass();
46. private targetId: number = ID;
47. private contentNode: ComponentContent<Object> =
48. new ComponentContent(this.uiContext, wrapBuilder(buildText), this.message);
49. private options: PopupCommonOptions = { enableArrow: true };

52. build() {
53. NavDestination() {
54. Column() {
55. Button('openPopup')
56. .margin({ top: 50, left: 100 })
57. .onClick(() => {
58. let frameNode: FrameNode | null = this.uiContext.getFrameNodeByUniqueId(this.getUniqueId());
59. let targetId = frameNode?.getChild(0)?.getUniqueId();
60. if (targetId == undefined) {
61. this.targetId = 0;
62. } else {
63. this.targetId = targetId;
64. }
65. this.promptActionClass.setPromptAction(this.promptAction);
66. this.promptActionClass.setContentNode(this.contentNode);
67. this.promptActionClass.setOptions(this.options);
68. this.promptActionClass.setIsPartialUpdate(false);
69. this.promptActionClass.setTarget({ id: this.targetId });
70. this.promptActionClass.openPopup();
71. })
72. }
73. }
74. }
75. }
```

[OpenPopup.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/popup/globalpopupsindependentofuicomponents/OpenPopup.ets#L16-L99)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/301qFRi_QFypMqVUcgtg1w/zh-cn_image_0000002552798272.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233945Z&HW-CC-Expire=86400&HW-CC-Sign=1E524CACFF21151AEE7D102156400E45E973BBFFFD8487B3712003657BA0F86B)
