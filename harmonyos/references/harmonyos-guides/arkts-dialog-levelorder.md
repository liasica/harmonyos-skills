---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-levelorder
title: 弹出框层级管理
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框层级管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:748d8714cb10333c57ae77c9138cbbe86b85fd35950a9e98e3a9f89f6b6347c1
---

ArkUI的弹出框节点都是直接挂载在根节点上，会根据层级从小到大依次挂载。根节点下，右边的弹出框节点会覆盖显示在左边的弹出框节点上，新创建的弹出框节点会根据层级大小插入到对应的位置，同一层级大小的弹窗节点按照创建的先后顺序进行挂载。

从API version 18开始，可以通过设置[levelOrder](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来管理弹出框的显示顺序，确保层级较高的弹出框覆盖在层级较低的弹出框之上，从而根据需要灵活控制各层弹出框的显示效果。

## 使用约束

目前[openCustomDialog](arkts-uicontext-custom-dialog.md)、[CustomDialog](arkts-common-components-custom-dialog.md)、[AlertDialog](arkts-fixes-style-dialog.md#警告弹窗-alertdialog)、[ActionSheet](arkts-fixes-style-dialog.md#列表选择弹窗-actionsheet)、[showDialog](arkts-fixes-style-dialog.md#对话框-showdialog)支持通过levelOrder参数来管理弹出框的层次。

说明

弹出框层级管理不支持子窗场景，即当showInSubWindow设置为true时，levelOrder参数设置无效。不支持动态刷新弹出框的显示顺序。

## 创建不同层级的弹出框

说明

详细变量定义请参考[完整示例](arkts-dialog-levelorder.md#完整示例)。

1. 初始化一个弹出框内容区，内部包含一个Text组件。

   ```
   1. @Builder
   2. normalCustomDialog(index: number) {
   3. Column() {
   4. // 请在resources\base\element\string.json文件中配置name为'open_normal_dialog'，value为非空字符串的资源
   5. Text(this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('open_normal_dialog') as string +
   6. index).fontSize(30)
   7. }.height(400).padding(5).justifyContent(FlexAlign.SpaceBetween)
   8. }
   ```

   [DialogBoxLayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxlayermanagement/DialogBoxLayer.ets#L29-L39)
2. 初始化另一个弹出框内容区，内部包含一个点击打开普通弹出框的按钮，点击事件中通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)接口，并且设置层级为0的[levelOrder](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来创建普通层级弹出框。

   ```
   1. @Builder
   2. topCustomDialog() {
   3. Column() {
   4. // 请将$r('app.string.top_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"我是置顶弹窗"
   5. Text($r('app.string.top_dialog')).fontSize(30)
   6. Row({ space: 50 }) {
   7. // 请将$r('app.string.open_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我打开普通弹窗"
   8. Button($r('app.string.open_dialog'))
   9. .onClick(() => {
   10. this.getUIContext().getPromptAction().openCustomDialog({
   11. builder: () => {
   12. this.normalCustomDialog(this.dialogIndex);
   13. },
   14. levelOrder: LevelOrder.clamp(0),
   15. })
   16. .catch((err: BusinessError) => {
   17. hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + '' + err.message);
   18. });
   19. this.dialogIndex++;
   20. })
   21. }
   22. }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
   23. }
   ```

   [DialogBoxLayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxlayermanagement/DialogBoxLayer.ets#L41-L68)
3. 通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12-1)接口，并且设置层级为100000的[levelOrder](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来创建最高层级弹出框。

   ```
   1. this.getUIContext().getPromptAction().openCustomDialog({
   2. builder: () => {
   3. this.topCustomDialog();
   4. },
   5. levelOrder: LevelOrder.clamp(100000)
   6. }).catch((err: BusinessError) => {
   7. hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
   8. });
   ```

   [DialogBoxLayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxlayermanagement/DialogBoxLayer.ets#L78-L87)

## 完整示例

```
1. import { LevelOrder } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const INDEX: number = 0;
6. const DOMAIN = 0x0000;

8. @Entry
9. @Component
10. export struct DialogBoxLayer {
11. @StorageLink('dialogIndex') dialogIndex: number = INDEX;

13. @Builder
14. normalCustomDialog(index: number) {
15. Column() {
16. // 请在resources\base\element\string.json文件中配置name为'open_normal_dialog'，value为非空字符串的资源
17. Text(this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('open_normal_dialog') as string +
18. index).fontSize(30)
19. }.height(400).padding(5).justifyContent(FlexAlign.SpaceBetween)
20. }

23. @Builder
24. topCustomDialog() {
25. Column() {
26. // 请将$r('app.string.top_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"我是置顶弹窗"
27. Text($r('app.string.top_dialog')).fontSize(30)
28. Row({ space: 50 }) {
29. // 请将$r('app.string.open_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我打开普通弹窗"
30. Button($r('app.string.open_dialog'))
31. .onClick(() => {
32. this.getUIContext().getPromptAction().openCustomDialog({
33. builder: () => {
34. this.normalCustomDialog(this.dialogIndex);
35. },
36. levelOrder: LevelOrder.clamp(0),
37. })
38. .catch((err: BusinessError) => {
39. hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + '' + err.message);
40. });
41. this.dialogIndex++;
42. })
43. }
44. }.height(200).padding(5).justifyContent(FlexAlign.SpaceBetween)
45. }

48. build() {
49. NavDestination() {
50. Row() {
51. Column({ space: 5 }) {
52. // 请将$r('app.string.click_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点击弹窗"
53. Button($r('app.string.click_dialog'))
54. .fontSize(20)
55. .onClick(() => {
56. this.getUIContext().getPromptAction().openCustomDialog({
57. builder: () => {
58. this.topCustomDialog();
59. },
60. levelOrder: LevelOrder.clamp(100000)
61. }).catch((err: BusinessError) => {
62. hilog.error(DOMAIN, 'dialogBoxLayer', 'openCustomDialog error: ' + err.code + ' ' + err.message);
63. });
64. })
65. }.width('100%')
66. }
67. }
68. }
69. }
```

[DialogBoxLayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxlayermanagement/DialogBoxLayer.ets#L16-L95)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/EXj1q9q1SSya3Yu5Oj0kMA/zh-cn_image_0000002583477909.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=EA41148ADB6988E245D6154C7894533BC57CB34EF31EEBFE513BCE752C97FD0B)
