---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-custom-dialog
title: 基础自定义弹出框 (CustomDialog)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用弹窗 > 弹出框 (Dialog) > 基础自定义弹出框 (CustomDialog)
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9b1d3deae177ae0b74890c6a4aa7a16ef308c38cda0f5c4585920a160988d86c
---

CustomDialog是自定义弹出框，可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹出框。具体用法请参考[自定义弹出框](../harmonyos-references/ts-methods-custom-dialog-box.md)。

说明

当前，ArkUI弹出框默认为非页面级弹出框，在页面路由跳转时，如果开发者未调用close方法将其关闭，弹出框将不会自动关闭。若需实现在跳转页面时覆盖弹出框的场景，可以使用[组件导航子页面显示类型的弹窗类型](arkts-navigation-navdestination.md#页面显示类型)或者[页面级弹出框](arkts-embedded-dialog.md)。

默认为模态弹窗且有蒙层，不可与蒙层下方控件进行交互（不支持点击和手势等向下透传）。可以通过配置[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的isModal属性来实现模态和非模态弹窗，详细说明可参考[弹窗的种类](arkts-dialog-overview.md#弹窗的种类)。

当isModal为true时，弹出框为模态弹窗，且弹窗周围的蒙层区不支持透传。isModal为false时，弹出框为非模态弹窗，且弹窗周围的蒙层区可以透传。因此如果需要同时允许弹出框的交互和弹出框外页面的交互行为，需要将弹出框设置为非模态。

## 生命周期

从API version 19开始，自定义弹出框提供了生命周期函数用于通知用户该弹出框的生命周期。生命周期的触发时序依次为：onWillAppear -> onDidAppear -> onWillDisappear -> onDidDisappear。

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| onWillAppear | Callback<void> | 弹出框显示动效前的事件回调。 |
| onDidAppear | Callback<void> | 弹出框弹出后的事件回调。 |
| onWillDisappear | Callback<void> | 弹出框退出动效前的事件回调。 |
| onDidDisappear | Callback<void> | 弹出框消失后的事件回调。 |

## 创建自定义弹出框

1. 使用@CustomDialog装饰器装饰自定义弹出框，可在此装饰器内自定义弹出框内容。CustomDialogController需在@Component内定义。

   ```
   1. @CustomDialog
   2. struct CustomDialogExample {
   3. controller?: CustomDialogController;

   5. build() {
   6. Column() {
   7. // 请将$r('app.string.i_am_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是内容"
   8. Text($r('app.string.i_am_content'))
   9. .fontSize(20)
   10. }.height(60).justifyContent(FlexAlign.Center)
   11. }
   12. }
   ```

   [CreateCustomDialogNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/CreateCustomDialogNew.ets#L17-L30)
2. 创建构造器，与装饰器相互连接。

   ```
   1. @Entry
   2. @Component
   3. export struct CreateCustomDialogNew {
   4. dialogController: CustomDialogController = new CustomDialogController({
   5. builder: CustomDialogExample(),
   6. })
   7. // ···
   8. }
   ```

   [CreateCustomDialogNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/CreateCustomDialogNew.ets#L33-L53)
3. 点击与onClick事件绑定的组件使弹出框弹出。

   ```
   1. @Entry
   2. @Component
   3. export struct CreateCustomDialogNew {
   4. dialogController: CustomDialogController = new CustomDialogController({
   5. builder: CustomDialogExample(),
   6. })
   7. build() {
   8. NavDestination() {
   9. Column() {
   10. Button('click me')
   11. .onClick(() => {
   12. this.dialogController.open();
   13. })
   14. }.width('100%').margin({ top: 5 })
   15. }
   16. }
   17. }
   ```

   [CreateCustomDialogNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/CreateCustomDialogNew.ets#L32-L54)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/oflGDnDZSWubNQoyoCmJog/zh-cn_image_0000002552798250.png?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=D1F84D26DF25D56083B5D98F353793B90E6B4CFA35DFC70F036B5B22DD1869EA)

## 弹出框的交互

弹出框可用于数据交互，完成用户一系列响应操作。

1. 在@CustomDialog装饰器内添加按钮和数据函数。

   ```
   1. @CustomDialog
   2. struct CustomDialogExample {
   3. cancel: () => void = () => {
   4. }
   5. confirm: () => void = () => {
   6. }
   7. controller?: CustomDialogController;

   9. build() {
   10. Column() {
   11. // 请将$r('app.string.i_am_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是内容"
   12. Text($r('app.string.i_am_content')).fontSize(20).margin({ top: 10, bottom: 10 })
   13. Flex({ justifyContent: FlexAlign.SpaceAround }) {
   14. Button('cancel')
   15. .onClick(() => {
   16. this.controller?.close();
   17. if (this.cancel) {
   18. this.cancel();
   19. }
   20. }).backgroundColor(0xffffff).fontColor(Color.Black)
   21. Button('confirm')
   22. .onClick(() => {
   23. this.controller?.close();
   24. if (this.confirm) {
   25. this.confirm();
   26. }
   27. }).backgroundColor(0xffffff).fontColor(Color.Red)
   28. }.margin({ bottom: 10 })
   29. }
   30. }
   31. }
   ```

   [DialogInteractionUseConstructor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogInteractionUseConstructor.ets#L19-L51)
2. 页面内需要在构造器内进行接收，同时创建相应的函数操作。

   ```
   1. @Entry
   2. @Component
   3. export struct DialogInteractionUseConstructor {
   4. dialogController: CustomDialogController = new CustomDialogController({
   5. builder: CustomDialogExample({
   6. cancel: ()=> { this.onCancel() },
   7. confirm: ()=> { this.onAccept() },
   8. }),
   9. });

   11. onCancel() {
   12. hilog.info(DOMAIN, 'testTag', 'Callback when the first button is clicked');
   13. }

   15. onAccept() {
   16. hilog.info(DOMAIN, 'testTag', 'Callback when the second button is clicked');
   17. }

   19. build() {
   20. Column() {
   21. NavDestination() {
   22. Button('click me')
   23. .onClick(() => {
   24. this.dialogController.open();
   25. })
   26. }.width('100%').margin({ top: 5 })
   27. }
   28. }
   29. }
   ```

   [DialogInteractionUseConstructor.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogInteractionUseConstructor.ets#L53-L83)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/fT8sUZ0vRL2INnxBF0R9IQ/zh-cn_image_0000002583437945.png?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=A290C06834F10540C04B9C5F2DEC80E40E9E399A63E97184783B57CEF79C3E21)
3. 可通过弹出框中的按钮实现路由跳转，同时获取跳转页面向当前页传入的参数。

   ```
   1. @CustomDialog
   2. struct CustomDialogExample {
   3. @Link textValue: string;
   4. controller?: CustomDialogController;
   5. cancel: () => void = () => {
   6. }
   7. confirm: () => void = () => {
   8. }

   10. build() {
   11. Column({ space: 20 }) {
   12. if (this.textValue !== '') {
   13. // 请将$r('app.string.the_second_page_is')替换为实际资源文件，在本示例中该资源文件的value值为"第二个页面的内容为"
   14. Text($r('app.string.the_second_page_is')+`：${this.textValue}`)
   15. .fontSize(20)
   16. } else {
   17. // 请将$r('app.string.whether_to_get_the_second_page')替换为实际资源文件，在本示例中该资源文件的value值为"是否获取第二个页面的内容"
   18. Text($r('app.string.whether_to_get_the_second_page'))
   19. .fontSize(20)
   20. }
   21. Flex({ justifyContent: FlexAlign.SpaceAround }) {
   22. Button('cancel')
   23. .onClick(() => {
   24. if (this.controller !== undefined) {
   25. this.controller.close();
   26. this.cancel();
   27. }
   28. }).backgroundColor(0xffffff).fontColor(Color.Black)
   29. Button('confirm')
   30. .onClick(() => {
   31. if (this.controller !== undefined && this.textValue !== '') {
   32. this.controller.close();
   33. } else if (this.controller !== undefined) {
   34. this.getUIContext().getRouter().pushUrl({
   35. url: 'pages/Index2'
   36. });
   37. this.controller.close();
   38. }
   39. }).backgroundColor(0xffffff).fontColor(Color.Red)
   40. }.margin({ bottom: 10 })
   41. }.borderRadius(10).padding({ top: 20 })
   42. }
   43. }

   45. @Entry
   46. @Component
   47. export struct DialogInteractionUseButton {
   48. @State textValue: string = '';
   49. dialogController: CustomDialogController | null = new CustomDialogController({
   50. builder: CustomDialogExample({
   51. cancel: () => {
   52. this.onCancel()
   53. },
   54. confirm: () => {
   55. this.onAccept()
   56. },
   57. textValue: this.textValue
   58. })
   59. });

   61. // 在自定义组件即将析构销毁时将dialogController置空
   62. aboutToDisappear() {
   63. this.dialogController = null; // 将dialogController置空
   64. }

   66. onPageShow() {
   67. const params = this.getUIContext().getRouter().getParams() as Record<string, string>; // 获取传递过来的参数对象
   68. if (params) {
   69. this.dialogController?.open();
   70. this.textValue = params.info as string; // 获取info属性的值
   71. }
   72. }

   74. onCancel() {
   75. hilog.info(DOMAIN, 'testTag', 'testTag', 'Callback when the first button is clicked');
   76. }

   78. onAccept() {
   79. hilog.info(DOMAIN, 'testTag', 'testTag', 'Callback when the second button is clicked');
   80. }

   82. exitApp() {
   83. hilog.info(DOMAIN, 'testTag', 'testTag', 'Click the callback in the blank area');
   84. }

   86. build() {
   87. Column() {
   88. NavDestination() {
   89. Button('click me')
   90. .onClick(() => {
   91. if (this.dialogController !== null) {
   92. this.dialogController.open();
   93. }
   94. }).backgroundColor(0x317aff)
   95. }.width('100%').margin({ top: 5 })
   96. }
   97. }
   98. }
   ```

   [DialogInteractionUseButton.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogInteractionUseButton.ets#L18-L117)

   ```
   1. @Entry
   2. @Component
   3. struct IndexNew {
   4. // 请将$r('app.string.click_and_return')替换为实际资源文件，在本示例中该资源文件的value值为"点击返回"
   5. @State message: string = $r('app.string.click_and_return');

   7. build() {
   8. NavDestination() {
   9. Column() {
   10. Button(this.message)
   11. .type(ButtonType.Capsule)
   12. .onClick(() => {
   13. this.getUIContext().getRouter().back({
   14. url: 'pages/Index',
   15. params: {
   16. info: 'Hello World'
   17. }
   18. });
   19. })
   20. }.width('100%').height('100%').margin({ top: 20 })
   21. }
   22. }
   23. }
   ```

   [IndexNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/IndexNew.ets#L16-L40)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/IKTmNs8pQIOBfZQPNg7ClA/zh-cn_image_0000002552957900.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=7224440A02C3DAAC2B6C597DAB0A2B1394B39ACB66F2E592D243A6F49C28AC30)

## 弹出框的动画

弹出框通过定义[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的openAnimation属性控制出现动画的持续时间，速度等参数。

```
1. @CustomDialog
2. struct CustomDialogExample {
3. controller?: CustomDialogController;

5. build() {
6. NavDestination() {
7. Column() {
8. Text('Whether to change a text?').fontSize(16).margin({ bottom: 10 })
9. }
10. }
11. }
12. }

14. @Entry
15. @Component
16. export struct DialogAnimationNew {
17. @State textValue: string = '';
18. @State inputValue: string = 'click me';
19. dialogController: CustomDialogController | null = new CustomDialogController({
20. builder: CustomDialogExample(),
21. openAnimation: {
22. duration: 1200,
23. curve: Curve.Friction,
24. delay: 500,
25. playMode: PlayMode.Alternate,
26. onFinish: () => {
27. hilog.info(DOMAIN, 'testTag', 'play end')
28. }
29. },
30. autoCancel: true,
31. alignment: DialogAlignment.Bottom,
32. offset: { dx: 0, dy: -20 },
33. gridCount: 4,
34. customStyle: false,
35. backgroundColor: 0xd9ffffff,
36. cornerRadius: 10,
37. });

39. // 在自定义组件即将析构销毁时将dialogController置空
40. aboutToDisappear() {
41. this.dialogController = null; // 将dialogController置空
42. }

44. build() {
45. NavDestination() {
46. Column() {
47. Button(this.inputValue)
48. .onClick(() => {
49. if (this.dialogController !== null) {
50. this.dialogController.open();
51. }
52. }).backgroundColor(0x317aff)
53. }.width('100%').margin({ top: 5 })
54. }
55. }
56. }
```

[DialogAnimationNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogAnimationNew.ets#L18-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/ZwBpEDTeTMakXAxrXeh6RA/zh-cn_image_0000002583477901.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=2FD00352EE6E49E7AAA6197A2771F9D7586431BEDC62762F7EC8C6AFD9DF70F6)

## 弹出框的样式

通过定义弹出框的宽度、高度、背景色、阴影等参数，控制其样式。

```
1. @CustomDialog
2. struct CustomDialogExample {
3. controller?: CustomDialogController;

5. build() {
6. Column() {
7. // 请将$r('app.string.i_am_content')替换为实际资源文件，在本示例中该资源文件的value值为"我是内容"
8. Text($r('app.string.i_am_content')).fontSize(16).margin({ bottom: 10 })
9. }
10. }
11. }

13. @Entry
14. @Component
15. export struct DialogStyleNew {
16. @State textValue: string = '';
17. @State inputValue: string = 'click me';
18. dialogController: CustomDialogController | null = new CustomDialogController({
19. builder: CustomDialogExample(),
20. autoCancel: true,
21. alignment: DialogAlignment.Center,
22. offset: { dx: 0, dy: -20 },
23. gridCount: 4,
24. customStyle: false,
25. backgroundColor: 0xd9ffffff,
26. cornerRadius: 20,
27. width: '80%',
28. height: '100px',
29. borderWidth: 1,
30. borderStyle: BorderStyle.Dashed, //使用borderStyle属性，需要和borderWidth属性一起使用
31. borderColor: Color.Blue, //使用borderColor属性，需要和borderWidth属性一起使用
32. shadow: ({
33. radius: 20,
34. color: Color.Grey,
35. offsetX: 50,
36. offsetY: 0
37. }),
38. });

40. // 在自定义组件即将析构销毁时将dialogController置空
41. aboutToDisappear() {
42. this.dialogController = null; // 将dialogController置空
43. }

45. build() {
46. NavDestination() {
47. Column() {
48. Button(this.inputValue)
49. .onClick(() => {
50. if (this.dialogController !== null) {
51. this.dialogController.open();
52. }
53. }).backgroundColor(0x317aff)
54. }.width('100%').margin({ top: 5 })
55. }
56. }
57. }
```

[DialogStyleNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogStyleNew.ets#L16-L75)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/JW1eEbiKTo2-Q_maJ_7SNg/zh-cn_image_0000002552798252.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=7554D0954DDEACAD238C3489F1D69FC1E92927FFCAC29BC06CCF4BB0A0AF5D63)

## 嵌套自定义弹出框

通过第一个弹出框打开第二个弹出框时，最好将第二个弹出框定义在第一个弹出框的父组件处，通过父组件传给第一个弹出框的回调来打开第二个弹出框。

```
1. @CustomDialog
2. struct CustomDialogExampleTwo {
3. controllerTwo?: CustomDialogController;
4. @State message: string = 'I am the second dialog box.';
5. @State showIf: boolean = false;

7. build() {
8. Column() {
9. if (this.showIf) {
10. Text('Text')
11. .fontSize(30)
12. .height(100)
13. }
14. Text(this.message)
15. .fontSize(30)
16. .height(100)
17. Button('Create Text')
18. .onClick(() => {
19. this.showIf = true;
20. })
21. Button('Close Second Dialog Box')
22. .onClick(() => {
23. if (this.controllerTwo !== undefined) {
24. this.controllerTwo.close();
25. }
26. })
27. .margin(20)
28. }
29. }
30. }

32. @CustomDialog
33. struct CustomDialogExample {
34. openSecondBox?: () => void;
35. controller?: CustomDialogController;

37. build() {
38. Column() {
39. Button('Open Second Dialog Box and close this box')
40. .onClick(() => {
41. this.controller!.close();
42. this.openSecondBox!();
43. })
44. .margin(20)
45. }.borderRadius(10)
46. }
47. }

49. @Entry
50. @Component
51. export struct NestDialogNew {
52. @State inputValue: string = 'Click Me';
53. dialogController: CustomDialogController | null = new CustomDialogController({
54. builder: CustomDialogExample({
55. openSecondBox: () => {
56. if (this.dialogControllerTwo !== null) {
57. this.dialogControllerTwo.open()
58. }
59. }
60. }),
61. cancel: this.exitApp,
62. autoCancel: true,
63. alignment: DialogAlignment.Bottom,
64. offset: { dx: 0, dy: -20 },
65. gridCount: 4,
66. customStyle: false
67. });
68. dialogControllerTwo: CustomDialogController | null = new CustomDialogController({
69. builder: CustomDialogExampleTwo(),
70. alignment: DialogAlignment.Bottom,
71. offset: { dx: 0, dy: -25 }
72. });

74. aboutToDisappear() {
75. this.dialogController = null;
76. this.dialogControllerTwo = null;
77. }

79. onCancel() {
80. hilog.info(DOMAIN, 'testTag', 'Callback when the first button is clicked');
81. }

83. onAccept() {
84. hilog.info(DOMAIN, 'testTag', 'Callback when the second button is clicked');
85. }

87. exitApp() {
88. hilog.info(DOMAIN, 'testTag', 'Click the callback in the blank area');
89. }

91. build() {
92. NavDestination() {
93. Column() {
94. Button(this.inputValue)
95. .onClick(() => {
96. if (this.dialogController !== null) {
97. this.dialogController.open();
98. }
99. }).backgroundColor(0x317aff)
100. }.width('100%').margin({ top: 5 })
101. }
102. }
103. }
```

[NestDialogNew.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/NestDialogNew.ets#L18-L122)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/uhwXxn-1RwiYKV9qmkwOYg/zh-cn_image_0000002583437947.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=7D3F2099E43DD96A53B8F044493DB3D80993802F1B89ADFE8EA66745953F326E)

由于自定义弹出框在状态管理侧有父子关系，如果将第二个弹出框定义在第一个弹出框内，那么当父组件（第一个弹出框）被销毁（关闭）时，子组件（第二个弹出框）内无法再继续创建新的组件。

## 实现弹出框的物理返回拦截

执行点击遮障层关闭、侧滑（左滑或右滑）、三键Back、键盘ESC关闭等交互操作时，如果注册了[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的onWillDismiss回调函数，弹出框不会立即关闭。在回调函数中，通过[DismissDialogAction](../harmonyos-references/ts-methods-custom-dialog-box.md#dismissdialogaction12)中的reason属性获取阻拦关闭弹出框的操作类型，根据原因决定是否关闭弹出框。

```
1. @CustomDialog
2. struct CustomDialogExample {
3. cancel: () => void = () => {
4. }
5. confirm: () => void = () => {
6. }
7. controller?: CustomDialogController;

9. build() {
10. Column() {
11. Text('Are you sure?')
12. .fontSize(20)
13. .margin({
14. top: 10,
15. bottom: 10
16. })
17. Row() {
18. Button('cancel')
19. .onClick(() => {
20. if (this.controller !== undefined) {
21. this.controller.close();
22. }
23. })
24. .backgroundColor(0xffffff)
25. .fontColor(Color.Black)
26. Button('confirm')
27. .onClick(() => {
28. if (this.controller !== undefined) {
29. this.controller.close();
30. }
31. })
32. .backgroundColor(0xffffff)
33. .fontColor(Color.Red)
34. }
35. .width('100%')
36. .justifyContent(FlexAlign.SpaceAround)
37. .margin({ bottom: 10 })
38. }
39. }
40. }

42. @Entry
43. @Component
44. export struct DialogWithPhysicalBack {
45. dialogController: CustomDialogController = new CustomDialogController({
46. builder: CustomDialogExample({
47. cancel: () => {
48. this.onCancel();
49. },
50. confirm: () => {
51. this.onAccept();
52. }
53. }),
54. onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
55. hilog.info(DOMAIN, 'testTag', 'dialog onWillDismiss reason: ' + dismissDialogAction.reason);
56. // 1、PRESS_BACK    点击三键back、侧滑（左滑/右滑）、键盘ESC。
57. // 2、TOUCH_OUTSIDE    点击遮障层时
58. // 3、CLOSE_BUTTON    点击关闭按钮
59. if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
60. // 处理业务逻辑后通过dismiss主动关闭对话框
61. dismissDialogAction.dismiss();
62. }
63. if (dismissDialogAction.reason === DismissReason.TOUCH_OUTSIDE) {
64. dismissDialogAction.dismiss();
65. }
66. },
67. alignment: DialogAlignment.Bottom,
68. offset: { dx: 0, dy: -20 }
69. })

71. onCancel() {
72. hilog.info(DOMAIN, 'testTag', 'Callback when the first button is clicked');
73. }

75. onAccept() {
76. hilog.info(DOMAIN, 'testTag', 'Callback when the second button is clicked');
77. }

79. build() {
80. NavDestination() {
81. Column() {
82. Button('click me')
83. .onClick(() => {
84. this.dialogController.open();
85. })
86. }
87. .width('100%')
88. }
89. }
90. }
```

[DialogWithPhysicalBack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogWithPhysicalBack.ets#L18-L109)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/-9CRe-2-TguhAg75VFwl_g/zh-cn_image_0000002552957902.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=7328E3F8A9D35B859C36C10D668CB49229584FA6E7A1B647B7118670B8005C75)

## 设置弹出框避让软键盘的距离

为显示弹出框的独立性，弹出框弹出时会与周边进行避让，包括状态栏、导航条以及键盘等留有间距。故当软键盘弹出时，默认情况下，弹出框会自动避开软键盘，并与之保持16vp的距离。从API version 15开始，开发者可以利用[CustomDialogControllerOptions](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontrolleroptions对象说明)中的keyboardAvoidMode和keyboardAvoidDistance这两个配置项，来设置弹出框在软键盘弹出时的行为，包括是否需要避开软键盘以及与软键盘之间的距离。

设置软键盘间距时，需要将keyboardAvoidMode值设为KeyboardAvoidMode.DEFAULT。

```
1. // xxx.ets
2. import { LengthMetrics } from '@kit.ArkUI';

4. @CustomDialog
5. struct CustomDialogExample {
6. controller?: CustomDialogController;

8. build() {
9. Column() {
10. Column() {
11. Text('keyboardAvoidDistance: 0vp')
12. .fontSize(20)
13. .margin({ bottom: 36 })
14. TextInput({ placeholder: '' })
15. }.backgroundColor('#FFF0F0F0')
16. }
17. }
18. }

20. @Entry
21. @Component
22. export struct DialogAvoidSoftKeyboard {
23. dialogController: CustomDialogController | null = new CustomDialogController({
24. builder: CustomDialogExample({}),
25. autoCancel: true,
26. gridCount: 4,
27. showInSubWindow: true,
28. isModal: true,
29. customStyle: false,
30. cornerRadius: 30,
31. alignment: DialogAlignment.Bottom,
32. keyboardAvoidMode: KeyboardAvoidMode.DEFAULT, // 软键盘弹出时，弹出框自动避让
33. keyboardAvoidDistance: LengthMetrics.vp(0) // 软键盘弹出时与弹出框的距离为0vp
34. })

36. build() {
37. NavDestination() {
38. Row() {
39. Row({ space: 20 }) {
40. // 请将$r('app.string.open_windows')替换为实际资源文件，在本示例中该资源文件的value值为"打开弹窗"
41. Text($r('app.string.open_windows'))
42. .fontSize(30)
43. .onClick(() => {
44. if (this.dialogController !== null) {
45. this.dialogController.open();
46. }
47. })
48. }
49. .width('100%')
50. }
51. .height('100%')
52. }
53. }
54. }
```

[DialogAvoidSoftKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/DialogAvoidSoftKeyboard.ets#L16-L72)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/V6LxjISWRL2yg3KBHffA2A/zh-cn_image_0000002552957898.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=436EC9E9F76AACCB8C3C609BF9EEC80327DB141D0E88A563FDA30212A2338455)

## 获取弹出框的状态

在业务模块中，页面上可能会同时出现多个弹出框。为避免重复打开相同的弹出框，建议在显示弹出框前，先通过控制器检查其当前状态。如果弹出框已处于显示状态，则不应再次打开。

从API version 20开始，新增了getState接口，用于获取弹出框的当前状态。具体的弹出框状态信息，请参见[CommonState](../harmonyos-references/js-apis-promptaction.md#commonstate20枚举说明)枚举的详细说明。

以下示例通过[getDialogController](../harmonyos-references/ts-custom-component-api.md#getdialogcontroller18)和[CustomDialogController](../harmonyos-references/ts-methods-custom-dialog-box.md#customdialogcontroller)两种方法，实现了获取弹出框当前状态的功能。

```
1. // xxx.ets
2. @CustomDialog
3. struct CustomDialogExample {
4. controller?: CustomDialogController;

6. build() {
7. Column() {
8. // 请将$r('app.string.search_by_dialog')替换为实际资源文件，在本示例中该资源文件的value值为"点我查询弹窗状态:通过自定义组件自带controller"
9. Button($r('app.string.search_by_dialog'))
10. .onClick(() => {
11. if (this.getDialogController() !== undefined) {
12. hilog.info(DOMAIN, 'testTag', 'state:' + this.getDialogController().getState());
13. } else {
14. hilog.info(DOMAIN, 'testTag', 'state: no exist');
15. }
16. }).margin(20)
17. // 请将$r('app.string.search_by_dialog_controller')替换为实际资源文件，在本示例中该资源文件的value值为"点我查询弹窗状态:通过CustomDialogController"
18. Button($r('app.string.search_by_dialog_controller'))
19. .onClick(() => {
20. hilog.info(DOMAIN, 'testTag', 'state:' + this.controller?.getState());
21. }).margin(20)
22. // 请将$r('app.string.close_widows')替换为实际资源文件，在本示例中该资源文件的value值为"点我关闭弹窗"
23. Button($r('app.string.close_widows'))
24. .onClick(() => {
25. if (this.getDialogController() !== undefined) {
26. this.getDialogController().close()
27. }
28. }).margin(20)

30. }
31. }
32. }

34. @Entry
35. @Component
36. export struct GetDialogStatus {
37. dialogController: CustomDialogController | null = new CustomDialogController({
38. builder: CustomDialogExample({
39. }),
40. autoCancel: false
41. })

43. build() {
44. NavDestination() {
45. Column() {
46. Button('click me')
47. .onClick(() => {
48. if (this.dialogController !== null) {
49. this.dialogController.open()
50. }
51. })
52. }.width('100%').margin({ top: 5 })
53. }
54. }
55. }
```

[GetDialogStatus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/DialogProject/entry/src/main/ets/pages/customdialog/GetDialogStatus.ets#L18-L74)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/K8tV0rTPQgCiLotEZPW5Cw/zh-cn_image_0000002583477903.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233942Z&HW-CC-Expire=86400&HW-CC-Sign=6CA79CD747C63F8208EFB5A2978FDBA587C13827455577328E84E1ED509433F1)
