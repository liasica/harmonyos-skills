---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-focusable
title: 弹出框焦点策略
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框焦点策略
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:98bd9d8b37f5f34a12c3d5e711d8116fc6284904ea62d45b88029154c7b08475
---

ArkUI的弹出框焦点策略可以设定是否中断用户当前操作，并聚焦到新弹出的弹出框。若设定弹出框不获取焦点，则新弹出时不会中断用户当前操作，例如，当用户正在文本框中输入内容时，新弹出的弹出框不会关闭软键盘，焦点仍保留在文本框中。

从API version 19开始，可以通过设置[focusable](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数来管理弹出框是否获取焦点。

## 使用约束

[openCustomDialog](arkts-uicontext-custom-dialog.md)和[CustomDialog](arkts-common-components-custom-dialog.md)支持通过focusable参数来管理弹出框是否获取焦点。

说明

只有弹出覆盖在当前窗口之上的弹出框才可以获取焦点。

## 创建不获取焦点的弹出框

说明

详细变量定义请参考[完整示例](arkts-dialog-focusable.md#完整示例)。

1. 初始化一个弹出框内容区域，内含一个Text组件。

   ```
   1. @State dialogIdIndex: number = 0;
   2. // 请在resources\base\element\string.json文件中配置name为'dialog_message'，value为非空字符串的资源
   3. private message: string =
   4. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('dialog_message') as string;

   6. @Builder
   7. customDialogComponent() {
   8. Column({ space: 5 }) {
   9. Text(this.message + this.dialogIdIndex)
   10. .fontSize(30)
   11. }
   12. .height(200)
   13. .padding(5)
   14. .justifyContent(FlexAlign.SpaceBetween)
   15. }
   ```

   [DialogFocusStrategy.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxfocuspolicy/DialogFocusStrategy.ets#L20-L37)
2. 创建一个TextInput组件，在onChange事件函数中通过调用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getPromptAction](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getpromptaction)方法获取[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)对象，再通过该对象调用[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)接口，并设置[focusable](../harmonyos-references/js-apis-promptaction.md#basedialogoptions11)参数为false，以创建弹出框。

   ```
   1. TextInput()
   2. .onChange(() => {
   3. this.dialogIdIndex++;
   4. this.getUIContext().getPromptAction().openCustomDialog({
   5. builder: () => {
   6. this.customDialogComponent();
   7. },
   8. focusable: false
   9. }).then((dialogId: number) => {
   10. setTimeout(() => {
   11. this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
   12. }, 3000);
   13. });
   14. })
   ```

   [DialogFocusStrategy.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxfocuspolicy/DialogFocusStrategy.ets#L42-L57)

## 完整示例

当用户正在文本框中输入内容时，新弹出的弹出框不会关闭软键盘，焦点仍保留在文本框中。

```
1. @Entry
2. @Component
3. export struct Index {
4. @State dialogIdIndex: number = 0;
5. // 请在resources\base\element\string.json文件中配置name为'dialog_message'，value为非空字符串的资源
6. private message: string =
7. this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('dialog_message') as string;

9. @Builder
10. customDialogComponent() {
11. Column({ space: 5 }) {
12. Text(this.message + this.dialogIdIndex)
13. .fontSize(30)
14. }
15. .height(200)
16. .padding(5)
17. .justifyContent(FlexAlign.SpaceBetween)
18. }

21. build() {
22. NavDestination() {
23. Column({ space: 5 }) {
24. TextInput()
25. .onChange(() => {
26. this.dialogIdIndex++;
27. this.getUIContext().getPromptAction().openCustomDialog({
28. builder: () => {
29. this.customDialogComponent();
30. },
31. focusable: false
32. }).then((dialogId: number) => {
33. setTimeout(() => {
34. this.getUIContext().getPromptAction().closeCustomDialog(dialogId);
35. }, 3000);
36. });
37. })
38. }.width('100%')
39. }
40. }
41. }
```

[DialogFocusStrategy.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/dialogboxfocuspolicy/DialogFocusStrategy.ets#L16-L63)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/WhMZcsuhRCiz_4TIviZy2A/zh-cn_image_0000002558604744.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=17726A73C1856A92F8DBEAE87572AD04390D0AB040BF7DF5A30A46B012E759A2)
