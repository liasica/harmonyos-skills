---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-210
title: 如何在自定义弹窗中再次弹窗
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在自定义弹窗中再次弹窗
category: harmonyos-faqs
scraped_at: 2026-04-29T14:16:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fa4fea6b8e303e520c9da2e0a77605db6aa04906cd69224945558bf794adfb8a
---

通过[openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)打开弹窗A，在弹窗A中点击按钮打开弹窗B。通过[getDialogController](../harmonyos-references/ts-custom-component-api.md#getdialogcontroller18)获取PromptActionDialogController实例对象并调用close()方法关闭当前弹窗。具体可参考示例代码：

```
1. import { ComponentContent } from '@kit.ArkUI';

3. @Component
4. struct DialogAComponent {
5. build() {
6. Column() {
7. Column() {
8. Text('dialog A')
9. .fontSize(20)
10. .fontWeight(FontWeight.Bold)
11. }
12. .justifyContent(FlexAlign.Center)
13. .height(120)

15. Row() {
16. Text('close')
17. .fontColor('#0A59F7')
18. .onClick(() => {
19. // close self.
20. this.getDialogController()?.close();
21. })
22. .width('50%')
23. .height('100%')
24. .textAlign(TextAlign.Center)

26. Text('open dialog B')
27. .fontColor('#0A59F7')
28. .onClick(() => {
29. // Open dialog B.
30. let uiContext = this.getUIContext();
31. let promptAction = uiContext.getPromptAction();
32. promptAction.openCustomDialog(new ComponentContent(uiContext, wrapBuilder(dialogBBuilder)));
33. })
34. .width('50%')
35. .height('100%')
36. .textAlign(TextAlign.Center)
37. }
38. .height(50)
39. }
40. .width(360)
41. .borderRadius(32)
42. .backgroundColor(Color.White)
43. }
44. }

46. @Builder
47. function dialogABuilder() {
48. DialogAComponent()
49. }

51. @Component
52. struct DialogBComponent {
53. build() {
54. Column() {
55. Column() {
56. Text('dialog B')
57. .fontSize(20)
58. .fontWeight(FontWeight.Bold)
59. }
60. .justifyContent(FlexAlign.Center)
61. .height(120)

63. Row() {
64. Text('close')
65. .fontColor('#0A59F7')
66. .onClick(() => {
67. // close self.
68. this.getDialogController()?.close();
69. })
70. .width('50%')
71. .height('100%')
72. .textAlign(TextAlign.Center)
73. }
74. .height(50)
75. }
76. .width(320)
77. .borderRadius(32)
78. .backgroundColor(Color.White)
79. }
80. }

82. @Builder
83. function dialogBBuilder() {
84. DialogBComponent()
85. }

87. @Entry
88. @Component
89. struct PopUpDialogAgainInCustomDialog {
90. build() {
91. Column() {
92. Button('open Dialog A')
93. .onClick(() => {
94. // Open dialog A.
95. let uiContext = this.getUIContext();
96. let promptAction = uiContext.getPromptAction();
97. promptAction.openCustomDialog(new ComponentContent(uiContext, wrapBuilder(dialogABuilder)));
98. })
99. }
100. .width('100%')
101. .height('100%')
102. .alignItems(HorizontalAlign.Center)
103. .justifyContent(FlexAlign.Center)
104. }
105. }
```

[PopUpDialogAgainInCustomDialog.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/308f3dc63a3e58fa81cfc108edcb6d345ce16b02/ArkUI/entry/src/main/ets/pages/PopUpDialogAgainInCustomDialog.ets#L21-L126)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/EFw03cEnRQ68xYrfeWfXhg/zh-cn_image_0000002399678053.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061651Z&HW-CC-Expire=86400&HW-CC-Sign=9891463A98BD633E13C7322C83B972D99ADAC013221CA029D15137A1C8069569 "点击放大")
