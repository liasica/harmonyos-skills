---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dialog-mask
title: 弹出框蒙层控制
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 弹出框蒙层控制
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:796bfc5cad7c9f20e0d18430d00069b32e012091a7f16e61118334538106a527
---

开发者对弹出框的定制不仅限于弹出框里的内容，对弹出框蒙层的定制需求也逐渐增加。本文介绍ArkUI弹出框的蒙层控制，包括点击蒙层时是否消失、蒙层区域、蒙层颜色和蒙层动画等特性。

## 使用约束

ArkUI提供多种弹出框，不同类型的弹出框具备不同的蒙层定制能力。详情请参阅下表：

| 接口&组件 | autoCancel | maskRect | isModal | immersiveMode |
| --- | --- | --- | --- | --- |
| [openCustomDialog](arkts-uicontext-custom-dialog.md) | 支持 | 支持 | 支持 | 支持 |
| [openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18) | 支持 | 支持 | 支持 | 支持 |
| [presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18) | 支持 | 支持 | 支持 | 支持 |
| [updateCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatecustomdialog12) | 支持 | 不支持 | 不支持 | 不支持 |
| [CustomDialog](arkts-common-components-custom-dialog.md) | 支持 | 支持 | 支持 | 支持 |
| [showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog) | 不支持 | 支持 | 支持 | 支持 |
| [showAlertDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showalertdialog) | 支持 | 支持 | 支持 | 支持 |
| [showActionSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showactionsheet) | 支持 | 支持 | 支持 | 支持 |
| [showActionMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showactionmenu11) | 不支持 | 不支持 | 支持 | 支持 |
| [showDatePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showdatepickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |
| [CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md) | 不支持 | 不支持 | 不支持 | 不支持 |
| [showTimePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtimepickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |
| [showTextPickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtextpickerdialog) | 不支持 | 支持 | 不支持 | 不支持 |

说明

* 设置autoCancel参数，可控制弹出框蒙层被点击时是否消失。
* 设置maskRect参数，可定制弹出框的蒙层的大小和位置。此外，蒙层范围内的事件无法透传，而蒙层范围外的事件可以透传。
* 设置isModal参数，可定制弹出框的模态状态：非模态弹出框无蒙层，支持与周围组件交互；模态弹出框有蒙层，禁止与周围组件交互。
* 从API version 15开始，当levelMode属性设置为LevelMode.EMBEDDED时，设置immersiveMode参数，可定制弹出框蒙层是否延伸至状态栏及导航栏。

| 接口&组件 | maskColor | transition | maskTransition |
| --- | --- | --- | --- |
| [openCustomDialog](arkts-uicontext-custom-dialog.md) | 支持 | 支持 | 支持 |
| [openCustomDialogWithController](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialogwithcontroller18) | 支持 | 支持 | 支持 |
| [presentCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#presentcustomdialog18) | 支持 | 支持 | 支持 |
| [updateCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#updatecustomdialog12) | 支持 | 不支持 | 不支持 |
| [CustomDialog](arkts-common-components-custom-dialog.md) | 支持 | 不支持（可由openAnimation和closeAnimation替代） | 不支持 |
| [showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog) | 不支持 | 不支持 | 不支持 |
| [showAlertDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showalertdialog) | 不支持 | 支持 | 不支持 |
| [showActionSheet](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showactionsheet) | 不支持 | 支持 | 不支持 |
| [showActionMenu](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showactionmenu11) | 不支持 | 不支持 | 不支持 |
| [showDatePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showdatepickerdialog) | 不支持 | 不支持 | 不支持 |
| [CalendarPickerDialog](../harmonyos-references/ts-methods-calendarpicker-dialog.md) | 不支持 | 不支持 | 不支持 |
| [showTimePickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtimepickerdialog) | 不支持 | 不支持 | 不支持 |
| [showTextPickerDialog](../harmonyos-references/arkts-apis-uicontext-uicontext.md#showtextpickerdialog) | 不支持 | 不支持 | 不支持 |

说明

* 设置maskColor参数，可定制弹出框蒙层的颜色。
* 设置openAnimation参数，可定制弹出框的进入动画，同时影响蒙层动画。该接口仅支持简单的动画设置，不支持复杂动画定制。
* 设置closeAnimation参数，可定制弹出框的退出动画，同时影响蒙层动画。该接口仅支持简单的动画设置，不支持复杂动画定制。
* 设置transition参数，可定制弹出框的进入和退出动画，同时影响蒙层动画。
* 从API version 19开始，设置maskTransition参数，可定制弹出框的蒙层动画。

## 弹出框蒙层显隐控制

通过autoCancel和isModal属性控制弹出框的蒙层显隐。

设置autoCancel为false，取消默认点击蒙层时弹窗消失。

```
1. autoCancelOpt: promptAction.CustomDialogOptions = {
2. builder: () => {
3. this.myBuilder();
4. },
5. autoCancel: false,
6. } as promptAction.CustomDialogOptions;
7. // ···
8. build() {
9. NavDestination() {
10. Column() {
11. Button('openCustomDialog autoCancel:false')
12. .width('100%')
13. .margin({ top: 10 })
14. .onClick(() => {
15. this.getUIContext().getPromptAction().openCustomDialog(this.autoCancelOpt)
16. })

18. // ···
19. }
20. .width('100%')
21. .height('100%')
22. }
23. }
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L27-L169)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/pRX0d8tbRWOYdPdHYAx1wQ/zh-cn_image_0000002589324269.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=2F67C45928FB23FA74E14671E0BC3170580C2158B00F191713C45EC28E5E7010)

设置isModal为false，将默认的模态弹出框变为非模态弹出框。

```
1. modalOpt: promptAction.CustomDialogOptions = {
2. builder: () => {
3. this.myBuilder();
4. },
5. isModal: false,
6. } as promptAction.CustomDialogOptions;
7. // ···
8. build() {
9. NavDestination() {
10. Column() {
11. // ···
12. Button('openCustomDialog isModal:false')
13. .width('100%')
14. .margin({ top: 10 })
15. .onClick(() => {
16. this.getUIContext().getPromptAction().openCustomDialog(this.modalOpt)
17. })

19. // ···
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L36-L168)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/Oh7IRATKQQ-7zXv5kL1AtA/zh-cn_image_0000002589244209.png?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=D69B75F8ADF27FCB8EC8C9B9F9109F6EE1812BA604B103992640A6C276EAC690)

## 弹出框蒙层样式控制

该示例通过maskRect、immersiveMode和maskColor展示弹出框在蒙层样式控制方面的能力。

设置maskRect和maskColor，实现蒙层区域和蒙层颜色的设置。

```
1. maskOpt: promptAction.CustomDialogOptions = {
2. builder: () => {
3. this.myBuilder();
4. },
5. maskRect: {
6. x: 0,
7. y: 10,
8. width: '100%',
9. height: '90%'
10. },
11. maskColor: '#33AA0000'
12. } as promptAction.CustomDialogOptions;
13. // ···
14. build() {
15. NavDestination() {
16. Column() {
17. // ···
18. Button('openCustomDialog maskOpt')
19. .width('100%')
20. .margin({ top: 10 })
21. .onClick(() => {
22. this.getUIContext().getPromptAction().openCustomDialog(this.maskOpt)
23. })

25. // ···
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L45-L167)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/uYGrpywvSdeqlIpKs0PJNQ/zh-cn_image_0000002558764402.png?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=99796869DD2420B6CDFECBCB32F2DC103B19A55D7FDAFAFC1A2E558389BE9D91)

在levelMode为LevelMode.EMBEDDED下，展示不同immersiveMode对蒙层在导航栏和状态栏的延伸效果。

```
1. @State immersiveMode: ImmersiveMode = ImmersiveMode.DEFAULT;
2. // ···
3. build() {
4. NavDestination() {
5. Column() {
6. // ···
7. Button('openCustomDialog immersiveMode')
8. .width('100%')
9. .margin({ top: 10 })
10. .onClick(() => {
11. this.immersiveMode =
12. this.immersiveMode == ImmersiveMode.DEFAULT ? ImmersiveMode.EXTEND : ImmersiveMode.DEFAULT;
13. this.getUIContext().getPromptAction().openCustomDialog({
14. builder: () => {
15. this.myBuilder();
16. },
17. levelMode: LevelMode.EMBEDDED,
18. immersiveMode: this.immersiveMode,
19. })
20. })

22. // ···
23. }
24. .width('100%')
25. .height('100%')
26. }
27. }
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L23-L170)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/yqyrB7faTy6Q6sGH1iocyg/zh-cn_image_0000002558604746.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=4E4A671BC6331F409396D363E9E7C6E5F1E9D99BCF01583A9CE32D0ED22C5DD4)

## 弹出框蒙层动画控制

该示例通过transition和maskTransition分别展示弹出框在蒙层动画方面的能力。

设置transition，实现弹出框与蒙层整体的动画。

```
1. transitionOpt: promptAction.CustomDialogOptions = {
2. builder: () => {
3. this.myBuilder();
4. },
5. transition: TransitionEffect.OPACITY.animation({ duration: 3000 })
6. } as promptAction.CustomDialogOptions;
7. // ···
8. build() {
9. NavDestination() {
10. Column() {
11. // ···
12. Button('openCustomDialog transition')
13. .width('100%')
14. .margin({ top: 10 })
15. .onClick(() => {
16. this.getUIContext().getPromptAction().openCustomDialog(this.transitionOpt);
17. })

19. // ···
20. }
21. .width('100%')
22. .height('100%')
23. }
24. }
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L60-L166)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/1sQ67MQ2RmiVap3Syn6skA/zh-cn_image_0000002589324271.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=794E37351C34E14DC984C9B1DE86DD1628F90D462C16CBD6F02CBA6AFC38304E)

设置maskTransition，实现弹出框中蒙层单独的动画定制能力。

```
1. Button('openCustomDialog maskTransition')
2. .width('100%')
3. .margin({ top: 10 })
4. .onClick(() => {
5. this.getUIContext().getPromptAction().openCustomDialog({
6. builder: () => {
7. this.myBuilder();
8. },
9. maskTransition: TransitionEffect.OPACITY.animation({ duration: 2000 })
10. .combine(TransitionEffect.rotate({ z: 1, angle: 180 })),
11. });
12. })
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L142-L155)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/dAjVSEi6TKmBCnGEFJ3VBQ/zh-cn_image_0000002589244211.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=AB3CC59D62959E2C67203E4BFD83EFE2040E9268330FF70E7AC309870663C74D)

[CustomDialog](arkts-common-components-custom-dialog.md)虽然不支持transition接口，但与之对应的openAnimation和closeAnimation接口在动画的打开和关闭时可进行定制，示例代码如下：

```
1. // xxx.ets

3. @CustomDialog
4. @Component
5. struct CustomDialogAnimationBuilder {
6. controller?: CustomDialogController;

8. build() {
9. Column() {
10. Text('title')
11. .margin(10)
12. .fontSize(20)
13. Button('button1')
14. .margin(10)
15. .fontSize(20)
16. .onClick(() => {
17. this.controller?.close();
18. })
19. Button('button2')
20. .margin(10)
21. .fontSize(20)
22. .onClick(() => {
23. this.controller?.close();
24. })
25. }.width('100%')
26. .height('50%')
27. }
28. }

30. @Entry
31. @Component
32. export struct CustomDialogAnimation {
33. animationController: CustomDialogController | null =
34. new CustomDialogController({
35. builder: CustomDialogAnimationBuilder(),
36. closeAnimation: { duration: 2000 },
37. openAnimation: { duration: 2000 }
38. });

40. aboutToDisappear(): void {
41. this.animationController = null;
42. }

44. build() {
45. NavDestination() {
46. Column() {
47. Button('CustomDialogController animate')
48. .width('100%')
49. .margin({ top: 10 })
50. .onClick(() => {
51. this.animationController?.open();
52. })
53. }
54. }
55. }
56. }
```

[CustomDialogAnimation.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogAnimation.ets#L16-L73)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/JTgloCzbRCudL2IVa2Tj1w/zh-cn_image_0000002558764404.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=5EFD19D74F33B5DB023310B45212B420A599952B6325FF2C7AE317F32549FC4A)

## 完整示例

```
1. // xxx.ets
2. import { ImmersiveMode, LevelMode, promptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. export struct CustomDialogControl {
7. @State immersiveMode: ImmersiveMode = ImmersiveMode.DEFAULT;

9. autoCancelOpt: promptAction.CustomDialogOptions = {
10. builder: () => {
11. this.myBuilder();
12. },
13. autoCancel: false,
14. } as promptAction.CustomDialogOptions;

16. modalOpt: promptAction.CustomDialogOptions = {
17. builder: () => {
18. this.myBuilder();
19. },
20. isModal: false,
21. } as promptAction.CustomDialogOptions;

23. maskOpt: promptAction.CustomDialogOptions = {
24. builder: () => {
25. this.myBuilder();
26. },
27. maskRect: {
28. x: 0,
29. y: 10,
30. width: '100%',
31. height: '90%'
32. },
33. maskColor: '#33AA0000'
34. } as promptAction.CustomDialogOptions;

36. transitionOpt: promptAction.CustomDialogOptions = {
37. builder: () => {
38. this.myBuilder();
39. },
40. transition: TransitionEffect.OPACITY.animation({ duration: 3000 })
41. } as promptAction.CustomDialogOptions;

43. @Builder
44. myBuilder() {
45. Column() {
46. Text('title').margin(10).fontSize(20)
47. Button('button1').margin(10).fontSize(20)
48. Button('button2').margin(10).fontSize(20)
49. }.width('100%').height('50%')
50. }

52. build() {
53. NavDestination() {
54. Column() {
55. Button('openCustomDialog autoCancel:false')
56. .width('100%')
57. .margin({ top: 10 })
58. .onClick(() => {
59. this.getUIContext().getPromptAction().openCustomDialog(this.autoCancelOpt)
60. })

62. Button('openCustomDialog isModal:false')
63. .width('100%')
64. .margin({ top: 10 })
65. .onClick(() => {
66. this.getUIContext().getPromptAction().openCustomDialog(this.modalOpt)
67. })

69. Button('openCustomDialog maskOpt')
70. .width('100%')
71. .margin({ top: 10 })
72. .onClick(() => {
73. this.getUIContext().getPromptAction().openCustomDialog(this.maskOpt)
74. })

76. Button('openCustomDialog transition')
77. .width('100%')
78. .margin({ top: 10 })
79. .onClick(() => {
80. this.getUIContext().getPromptAction().openCustomDialog(this.transitionOpt);
81. })

83. Button('openCustomDialog immersiveMode')
84. .width('100%')
85. .margin({ top: 10 })
86. .onClick(() => {
87. this.immersiveMode =
88. this.immersiveMode == ImmersiveMode.DEFAULT ? ImmersiveMode.EXTEND : ImmersiveMode.DEFAULT;
89. this.getUIContext().getPromptAction().openCustomDialog({
90. builder: () => {
91. this.myBuilder();
92. },
93. levelMode: LevelMode.EMBEDDED,
94. immersiveMode: this.immersiveMode,
95. })
96. })

98. Button('openCustomDialog maskTransition')
99. .width('100%')
100. .margin({ top: 10 })
101. .onClick(() => {
102. this.getUIContext().getPromptAction().openCustomDialog({
103. builder: () => {
104. this.myBuilder();
105. },
106. maskTransition: TransitionEffect.OPACITY.animation({ duration: 2000 })
107. .combine(TransitionEffect.rotate({ z: 1, angle: 180 })),
108. });
109. })
110. }
111. .width('100%')
112. .height('100%')
113. }
114. }
115. }
```

[CustomDialogControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/maskdialog/CustomDialogControl.ets#L16-L172)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/2YlvCAdCTPCQw2zg-PxGGw/zh-cn_image_0000002558604748.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052754Z&HW-CC-Expire=86400&HW-CC-Sign=BEDD05820314C0DD6795CED0950F06C44DEB09D1DF27318565D48BE196FB3C3C)
