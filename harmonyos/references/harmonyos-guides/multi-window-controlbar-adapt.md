---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/multi-window-controlbar-adapt
title: 顶部窗口控制条避让适配智慧多窗
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > 窗口管理 > 智慧多窗应用开发指南 > 应用适配智慧多窗 > 顶部窗口控制条避让适配智慧多窗
category: harmonyos-guides
scraped_at: 2026-04-29T13:29:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9831ad163b9e9bd480b62bc441b14c067a11a18d8349e1323e88735fffc026d8
---

顶部窗口控制条是应用窗口处于智慧多窗模式下，应用顶部的操作横条 ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/UiB3dlAgSCWw3jGwUU4N6A/zh-cn_image_0000002589244497.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=4F42A551C9E8753BEF18BBBC3BDF9267125EA5F671AAF205E044D48BD810F1F3) 。

顶部窗口控制条示意图如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Tq57oUljS--JxtRKo29j7w/zh-cn_image_0000002558764690.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=1F2ABAE93FB6DF5C8621D5CF31AB61B5D5BEEB61E551DA5A8D683CB9E0A446A5)

顶部横条的避让可通过以下两种方式适配：

* 使用窗口的避让能力：通过[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置窗口布局是否为沉浸式布局。

  沉浸式布局是指应用布局不避让状态栏、导航栏以及智慧多窗顶部横条，这可能发生组件与顶部横条的重叠，导致文字遮挡、点击事件冲突等情况。非沉浸式布局是指布局避让状态栏、导航栏以及智慧多窗顶部横条，组件不会与其重叠。因此可设置isLayoutFullScreen值为false使窗口的布局为非沉浸式布局。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/YduSPlW2QNS5oWLAwibHLw/zh-cn_image_0000002558605036.png?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=D623866A7BBB0D42CDECC7796C0ECB76E1D25FE82F7B2A898D8E7C2E8580F7D5)

  示例：

  ```
  1. // Index.ets
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { window } from '@kit.ArkUI';
  4. import { common } from '@kit.AbilityKit';

  6. @Entry
  7. @Component
  8. struct Index {
  9. @State message: string = '非沉浸式布局';
  10. private windowClass: window.Window | undefined = undefined;

  12. aboutToAppear(): void {
  13. try {
  14. window.getLastWindow(this.getUIContext()?.getHostContext() as common.UIAbilityContext,
  15. (err: BusinessError, data) => {
  16. const errCode: number = err.code;
  17. if (errCode) {
  18. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
  19. return;
  20. }
  21. this.windowClass = data;
  22. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
  23. });
  24. } catch (exception) {
  25. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
  26. }
  27. }

  29. private setWindowLayoutFullScreen(isLayoutFullScreen: boolean) {
  30. if (!this.windowClass) {
  31. return;
  32. }
  33. this.windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
  34. console.info('Succeeded in setting the window layout to full-screen mode.');
  35. }).catch((err: BusinessError) => {
  36. const errCode: number = err.code;
  37. if (errCode) {
  38. console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(err));
  39. return;
  40. }
  41. });
  42. }

  44. build() {
  45. Stack({ alignContent: Alignment.TopStart }) {
  46. Column() {
  47. Text(this.message)
  48. .fontSize(25)
  49. .fontWeight(FontWeight.Bold)
  50. .margin({
  51. top: '2%',
  52. bottom: '40%'
  53. })

  55. Button() {
  56. Text('设置窗口为沉浸式布局')
  57. .fontSize(18)
  58. .fontWeight(FontWeight.Normal)
  59. }
  60. .type(ButtonType.Normal)
  61. .borderRadius(15)
  62. .margin({ top: 20 })
  63. .stateStyles({
  64. normal: {
  65. .backgroundColor('#ff6b89d4')
  66. },
  67. pressed: {
  68. .backgroundColor('#ffc81f2a')
  69. }
  70. })
  71. .width('60%')
  72. .height('6%')
  73. .onClick(() => {
  74. this.setWindowLayoutFullScreen(true);
  75. this.message = '沉浸式布局';
  76. })

  78. Button() {
  79. Text('设置窗口为非沉浸式布局')
  80. .fontSize(18)
  81. .fontWeight(FontWeight.Normal)
  82. }
  83. .type(ButtonType.Normal)
  84. .borderRadius(15)
  85. .margin({ top: 20 })
  86. .stateStyles({
  87. normal: {
  88. .backgroundColor('#ff6b89d4')
  89. },
  90. pressed: {
  91. .backgroundColor('#ffc81f2a')
  92. }
  93. })
  94. .width('60%')
  95. .height('6%')
  96. .onClick(() => {
  97. this.setWindowLayoutFullScreen(false);
  98. this.message = '非沉浸式布局';
  99. })
  100. }
  101. .width('100%')
  102. }
  103. .backgroundColor('#fceaeaea')
  104. .height('100%')
  105. }
  106. }
  ```

  图1 设置窗口是否为沉浸式布局

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/LJS8om3gT5qE_-rQLM8KUQ/zh-cn_image_0000002589324561.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=89C087A230A77A8C79157A028F4F3954736DF441B5D05A8C501525837D69C5D1)
* 应用主动避让：应用不使用窗口避让能力（即设置窗口为沉浸式布局）。首次通过[getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口可获取屏幕顶部需要规避的矩阵区域topRect，获取到该值后应用可对应做布局避让，并且注册[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听系统避让区域变化以进行布局的动态调整。

  ```
  1. // Index.ets
  2. import { BusinessError } from '@kit.BasicServicesKit';
  3. import { common } from '@kit.AbilityKit';
  4. import { window } from '@kit.ArkUI';

  6. @Entry
  7. @Component
  8. struct Index {
  9. @State topSafeHeight: number = 0;

  11. aboutToAppear(): void {
  12. try {
  13. let windowClass: window.Window | undefined = undefined;
  14. window.getLastWindow(this.getUIContext()?.getHostContext() as common.UIAbilityContext,
  15. (err: BusinessError, data) => {
  16. const errCode: number = err.code;
  17. if (errCode) {
  18. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(err));
  19. return;
  20. }
  21. windowClass = data;
  22. windowClass.setWindowLayoutFullScreen(true);
  23. this.topSafeHeight = this.getUIContext()?.px2vp(
  24. windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
  25. windowClass.on('avoidAreaChange', (data) => {
  26. if (data.type == window.AvoidAreaType.TYPE_SYSTEM) {
  27. this.topSafeHeight = this.getUIContext()?.px2vp(data.area.topRect.height)
  28. }
  29. })
  30. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
  31. });
  32. } catch (exception) {
  33. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(exception));
  34. }
  35. }

  37. build() {
  38. Stack({ alignContent: Alignment.TopStart }) {
  39. // 顶部避让区域
  40. Row() {
  41. }
  42. .height(this.topSafeHeight)
  43. .width("100%")
  44. .backgroundColor('#ccbbf375')
  45. // 根据topSafeHeight动态调整应用布局
  46. // ...
  47. }
  48. .height('100%')
  49. }
  50. }
  ```

  图2 应用主动做布局避让

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/9RuSI5YtR3mn2OG3MkYsfg/zh-cn_image_0000002589244499.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052907Z&HW-CC-Expire=86400&HW-CC-Sign=0B5E39C77AB547B98648D4B808900B9D60F1DAB9263BD5610F1D09D4A3EF226E)
