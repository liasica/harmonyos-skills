---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pop-up-controls-focus
title: 弹窗类控件走焦的场景
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 提升应用的无障碍体验 > 提升屏幕朗读无障碍体验 > 弹窗类控件走焦的场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:594206af46c5e66f78cbdf37c669a55e5ba1f27a7764999d0006ddc9f5db6930
---

## 设计场景

根据用户交互操作场景，弹窗可分为模态弹窗和非模态弹窗两种类型，其区别在于用户是否必须对其做出响应。

* 模态弹窗为强交互形式，会中断用户当前的操作流程，要求用户必须做出响应才能继续其他操作，通常用于需要向用户传达重要信息的场景。屏幕朗读模式下，模态弹窗弹出时，焦点会自动聚焦到模态弹窗上，在弹窗关闭前无法聚焦到弹窗外节点。
* 非模态弹窗为弱交互形式，不会影响用户当前操作行为，用户可不进行回应，通常都有时间限制，出现一段时间后会自动消失，一般用于向用户传递信息并引导用户执行功能操作的场景。屏幕朗读模式下，非模态弹窗弹出时，焦点默认自动聚焦到非模态弹窗上，弹窗关闭前允许聚焦到弹窗外节点。特别地，如果弹窗是以子窗形式出现，则只能通过不抬手走焦或触摸聚焦的方式聚焦到弹窗外节点，而无法通过抬手走焦的方式聚焦到弹窗外节点。

支持设置模态类型的弹窗控件包括[Popup](../harmonyos-references/ohos-arkui-advanced-popup.md)、[Menu](../harmonyos-references/ts-basic-components-menu.md)、[Diaglog](../harmonyos-references/ohos-arkui-advanced-dialog.md)、[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)。

## 开发实例

如下示例实现一个模态弹窗和一个非模态弹窗，可以通过点击不同的按钮打开：

```
1. @Entry
2. @Component
3. struct Rule_2_1_17 {
4. title: string = 'Rule 2.1.17';
5. // 模态对话框控制器
6. private modelDialogController: CustomDialogController = this.createDialogController(true);
7. // 非模态对话框控制器
8. private nonModelDialogController: CustomDialogController = this.createDialogController(false);

10. /**
11. * 创建对话框控制器
12. * @param isModel 是否为模态对话框
13. * @returns 返回创建的对话框控制器
14. */
15. private createDialogController(isModel: boolean): CustomDialogController {
16. return new CustomDialogController({
17. builder: CustomDialogExample({
18. controller: isModel ? this.modelDialogController : this.nonModelDialogController,
19. isModel: isModel,
20. cancel: () => {
21. if (isModel) {
22. this.modelDialogController.close();
23. } else {
24. this.nonModelDialogController.close();
25. }
26. }
27. }),
28. autoCancel: true,
29. isModal: isModel,
30. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
31. if (dismissDialogAction.reason == DismissReason.PRESS_BACK) {
32. dismissDialogAction.dismiss();
33. }
34. if (dismissDialogAction.reason == DismissReason.TOUCH_OUTSIDE) {
35. dismissDialogAction.dismiss();
36. }
37. },
38. showInSubWindow: true,
39. alignment: DialogAlignment.Center,
40. width: 300,
41. height: 250,
42. })
43. }

45. build() {
46. NavDestination() {
47. Scroll() {
48. Column() {
49. // 模态对话框按钮
50. Button('模态dialog')
51. .margin({ bottom: 5 })
52. .onClick(() => {
53. this.modelDialogController.open();
54. })

56. // 非模态对话框按钮
57. Button('非模态dialog')
58. .onClick(() => {
59. this.nonModelDialogController.open();
60. })
61. }.margin({ bottom: 5 })
62. }
63. }.title(this.title)
64. }
65. }

67. @CustomDialog
68. struct CustomDialogExample {
69. // 是否为模态对话框
70. isModel?: boolean;
71. // 对话框控制器
72. controller?: CustomDialogController;
73. // 关闭对话框的回调函数
74. cancel: () => void = () => {};

76. build() {
77. Column() {
78. // 显示对话框的标题
79. Text(this.isModel ? '模态弹窗' : '非模态弹窗')
80. .fontSize(30)
81. .height(100)
82. Text('测试节点1')
83. Text('测试节点2')
84. Text('测试节点3')
85. // 关闭对话框按钮
86. Button('关闭')
87. .onClick(() => {
88. this.cancel?.();
89. })
90. .margin(20)
91. }
92. }
93. }
```
