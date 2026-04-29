---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-window-practice
title: 智慧多窗
breadcrumb: 最佳实践 > 应用框架 > 窗口与屏幕管理 > 智慧多窗
category: best-practices
scraped_at: 2026-04-29T14:10:59+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:01d2667ec33f41a9ab9ba3be07dfaf9578d153a5ac9c44d88360d7bcca1223fb
---

## 概述

智慧多窗是一种多任务处理解决方案，允许用户在同一时间、同一屏幕上以悬浮窗或分屏的方式同时运行多个应用窗口。在智慧多窗的显示模式下，用户可以根据自己的需求，合理安排应用窗口的位置和大小。目前智慧多窗的形式，主要包含悬浮窗和分屏。

* **悬浮窗**：设备屏幕上悬浮的、非全屏的应用窗口。一般用于在已有全屏任务运行的基础上，临时处理另一个任务，或短时间多任务并行使用。如浏览网页的同时回复消息。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/fQ1TY8phRweTpgeUVmS_zQ/zh-cn_image_0000002193851416.png?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=43E4CF01A6A4C14EDB44541AABDBAB093F08DEED7B8C713C4581AEB34998A288 "点击放大")
* **分屏**：分屏一般用于两个应用长时间并行使用的场景。例如边看购物攻略、边浏览商品；边看视频、边玩游戏；看学习类视频的同时做笔记等。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/PNaltTAmTmKmPcKJ6BGCrw/zh-cn_image_0000002193851376.png?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=AA144BB849F0B91DFE593FA271E9BC5F86F7B3C9A10165ED5C72C20A8B7E5293 "点击放大")

由于应用从全屏进入智慧多窗（悬浮窗/分屏）模式后，窗口尺寸、宽高比例会发生变化，往往会产生一些布局的适配问题。例如，分屏后页面内容显示不全无法滑动、视频被压缩导致宽高比不正确，应用开启悬浮窗后内容和状态栏的重叠区域无法响应用户操作等。

本文将主要介绍悬浮窗/分屏布局适配方案，以及智慧多窗开发过程中的一些常见问题以及解决方案，来帮助开发者快速适配智慧多窗布局开发，提升用户使用体验。

在阅读本文前开发者可以先了解下关于智慧多窗的UX设计规范，具体可以参考[多窗口交互](../design-guides/system-features-multi-window-interaction-0000001795392917.md)。

## 智慧多窗适配方案

悬浮窗和分屏功能是由系统提供的能力，不需要开发者单独开发功能，所以开发者只需要考虑应用悬浮或者分屏之后应用界面的适配问题。

首先开发者需要考虑应用是否需要支持悬浮窗/分屏能力，如果确定应用需要支持悬浮窗/分屏能力，则需要考虑布局适配问题，进行布局一多适配。在一些特殊的场景下，比如沉浸模式下，顶部窗口控制条遮挡住了重要信息或者重叠区域有事件需要响应的时候，需要考虑控制条的避让适配；横向游戏和视频需要考虑横向悬浮窗适配。开发者可以参考下面的流程图进行智慧多窗适配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/YmanDLNlTkGcuHvctTDUtw/zh-cn_image_0000002193851392.png?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=09BD326F88BEAA560A0A2AC0545C94186C0EA030C4C961FF149F0D6D57B295AE "点击放大")

### 配置声明支持智慧多窗

当应用需要配置是否支持悬浮窗/分屏能力时，可以通过在module.json5配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下添加supportWindowMode字段来实现，supportWindowMode属性主要标识当前UIAbility所支持的窗口模式，详细请参见[应用声明支持智慧多窗](../harmonyos-guides/multi-window-support.md)。

### 一多布局适配

在使用多窗口功能时，窗口的尺寸会发生变化，可能影响布局。以下是两种情况的具体描述：

* **进入分屏模式**：当手机设备进入分屏模式时，窗口高度缩小为原来的1/2或1/3，宽度保持不变。由于内容页面大小未作相应调整，垂直方向的内容可能被截断，且页面无法滚动查看完整内容。
* **进入竖向悬浮窗模式**：在这种模式中，窗口内容会根据窗口大小进行等比缩放。但是，窗口的高宽比变为3:4.575，这与全屏模式（通常为16:9或4:3）的比例不同。纵向比例相对于横向较小，这也可能导致内容截断现象。

这种对比说明，在多窗口使用时，需要特别注意布局的可视性和内容的可访问性，以确保用户体验。

说明

关于不同设备悬浮窗宽高比、应用分屏窗口高度比例详细请参见[应用布局适配智慧多窗](../harmonyos-guides/multi-window-layout-adapt.md#section4402545164612)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/5T2TZZ_zSL2amhLOak2GBA/zh-cn_image_0000002229451269.png?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=F1A05DADBDBC7C0A0F850D79D5AA5955D2BE9196993ACA48EED5C0B7E9A30701 "点击放大")

针对应用进入悬浮窗/分屏出现的页面内容截断、挤压、堆叠等问题，开发者可以参考[一次开发，多端部署](bpta-multi-device-overview.md)中关于页面开发的[多设备界面开发](bpta-multi-device-page.md)，通过[自适应布局](bpta-multi-device-adaptive-layout.md)和[响应式布局](bpta-multi-device-responsive-layout.md)**，**来使应用自适应窗口的大小变化。例如示例[布局适配问题](bpta-multi-window-practice.md#section3687216112915)节：界面被截断，无法上下滑动，使用了一多的[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)。

### 沉浸模式下顶部窗口控制条避让适配

沉浸式布局是指应用布局不避让状态栏、导航栏以及智慧多窗顶部横条，这可能发生组件与顶部横条的重叠，导致文字遮挡、点击事件冲突等情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/fD_hYpUISTq9y5pUgyNpOQ/zh-cn_image_0000002229336757.png?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=70BFFE7A1FB757DBA3CBF489844FD7A44671F49168D793CF84726F87E9607DDB "点击放大")

顶部横条的避让可通过以下两种方式适配，具体可以参考[顶部窗口控制条避让适配智慧多窗](../harmonyos-guides/multi-window-controlbar-adapt.md)。

* **使用窗口的避让能力**：通过[setWindowLayoutFullScreen](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)设置窗口布局是否为沉浸式布局。根据业务需要，可以先通过[on('windowStatusChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowstatuschange11)方法监听窗口模式变化，当窗口模式为全屏的时候，设置setWindowLayoutFullScreen为false，当窗口模式为非全屏的时候（包括分屏和悬浮窗）设置为true。
* **应用主动避让**：应用不使用窗口避让能力（即设置窗口为沉浸式布局），还通过[getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口可获取屏幕顶部需要规避的矩阵区域topRect，获取到该值后应用可对应做布局避让。同时可通过[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听系统规避区域变化以进行布局的动态调整。

顶部横条的避让具体实践可以参考：[沉浸模式下顶部窗口控制条避让问题](bpta-multi-window-practice.md#section533165015358)。

### 横向游戏和视频横向悬浮窗适配

悬浮窗默认是竖向的，但是对于横向游戏和视频应用，横向的悬浮窗体验会更好。开发者可以通过在module.json5配置文件中abilities标签下的preferMultiWindowOrientation属性增加“landscape”或者“landscape\_auto”配合API以声明应用支持横向悬浮窗或上下分屏模式。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. "name": "EntryAbility",
7. // ...
8. "preferMultiWindowOrientation": "landscape_auto"
9. }
10. ],
11. // ...
12. }
13. }
```

[module.json5](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/module.json5#L2-L59)

preferMultiWindowOrientation属性主要标识当前UIAbility多窗布局方向，具体可以参考[声明支持悬浮窗](../harmonyos-guides/multi-window-support.md#section14646185913211)中关于preferMultiWindowOrientation的属性的描述**。**当设置preferMultiWindowOrientation属性为“landscape\_auto”表示多窗布局动态可变为横向，需要配合API（[enableLandscapeMultiWindow](../harmonyos-references/arkts-apis-window-window.md#enablelandscapemultiwindow12) / [disableLandscapeMultiWindow](../harmonyos-references/arkts-apis-window-window.md#disablelandscapemultiwindow12)）使用，建议视频类应用配置，视频播放界面适配横屏悬浮窗效果图如下，具体使用可以参考：[横向悬浮窗适配问题](bpta-multi-window-practice.md#section4595191593711)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/1QDS6ny5QL6ZxZB72XAuvQ/zh-cn_image_0000002193851396.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=6831F8382BA3DB0B57C853700C7D7C86183566C80A2252BBD63E61839F4E99B5 "点击放大")

## 常见问题

为了帮助开发者快速对智慧多窗进行布局适配，下面列举了一些常见的智慧多窗布局适配问题，接下来介绍如何使用前面讲到的一些适配方案来解决这些问题。

下面将常见问题分为以下三类，开发者可以使用前面对应的适配方案进行适配：

* 布局适配问题：这类问题一般是由于进入分屏/悬浮窗时，由于窗口高度缩小，导致的布局混乱、被截断等问题。
* 沉浸模式下顶部窗口控制条避让问题：在沉浸模式下，应用分屏后视图和悬浮窗顶部重合的区域无法响应操作的问题。
* 横屏悬浮窗适配问题：对于横向游戏和视频应用横向的悬浮窗体适配问题。

### 布局适配问题

1. 界面被截断，无法上下滑动。

   **问题现象**

   应用分屏后内容显示不全，无法通过上下滑动展示未显示的内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/WImC7mKGTECJH5iMtwoy8g/zh-cn_image_0000002229336817.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=F25A7B33168C836C3828B32D5EB5E08CDF91D62EE4278D5D7794AEF6A765572C "点击放大")

   优化前示例代码如下：

   ```
   1. @Component
   2. export struct Question1Incorrect {
   3. build() {
   4. NavDestination() {
   5. Column({ space: 12 }) {
   6. Text('Text1')
   7. .fontSize(50)
   8. .width('100%')
   9. .textAlign(TextAlign.Center)
   10. .height(350)
   11. .backgroundColor(Color.Brown)

   13. Text('Text2')
   14. .fontSize(50)
   15. .width('100%')
   16. .textAlign(TextAlign.Center)
   17. .height(350)
   18. .backgroundColor(Color.Orange)
   19. }
   20. // ...
   21. }
   22. // ...
   23. }
   24. }
   ```

   [Question1Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question1Incorrect.ets#L22-L58)

   **可能原因**

   应用只适配了全屏大小，当应用分屏/悬浮窗后，窗口会变小，导致页面显示不全，超出窗口的区域无法显示。

   **解决措施**

   使用一多的[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)，增加Scroll组件，让列表或者文字区域可以按照指定方向滑动，优化后示例代码如下：

   ```
   1. @Component
   2. export struct Question1Correct {
   3. build() {
   4. NavDestination() {
   5. Scroll() {
   6. Column({ space: 12 }) {
   7. Text('Text1')
   8. .fontSize(50)
   9. .width('100%')
   10. .textAlign(TextAlign.Center)
   11. .height(350)
   12. .backgroundColor(Color.Brown)

   14. Text('Text2')
   15. .fontSize(50)
   16. .width('100%')
   17. .textAlign(TextAlign.Center)
   18. .height(350)
   19. .backgroundColor(Color.Orange)
   20. }
   21. }
   22. // ...
   23. }
   24. // ...
   25. }
   26. }
   ```

   [Question1Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question1Correct.ets#L21-L57)

   优化后效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/0VMwge1JS0CE-olBrThgqg/zh-cn_image_0000002194010960.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=B87DC65051B0F9C606208B1AA36EAF8073EC9764712AAB4668791F338272DC65 "点击放大")
2. Xcomponent视频画面在分屏页面显示不全。

   **问题现象**

   视频播放界面分屏后，视频被截断显示不全。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/b8n3LI4GSt2YPbYvf7vY5g/zh-cn_image_0000002229451293.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=E5704EA61A3409013CF56220D904159499B2659BBCA4CDFA2AA552E2B2DFE67D "点击放大")

   **可能原因**

   在进入分屏页面，窗口的height变成了屏幕的1/2，应用没有对这种情况进行适配，导致Xcomponent宽度没变为之前的1/2导致视频形变。优化前示例代码如下：

   ```
   1. @Component
   2. export struct Question2Incorrect {
   3. @State aspect: number = 9 / 16; // default video height/width ratio value
   4. @State xComponentWidth: number = this.getUIContext().px2vp(display.getDefaultDisplaySync().width);
   5. @State xComponentHeight: number = this.getUIContext().px2vp(display.getDefaultDisplaySync().width * this.aspect);
   6. // ...

   8. build() {
   9. NavDestination() {
   10. Stack() {
   11. XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.xComponentController })
   12. // ...
   13. .width(this.xComponentWidth)
   14. .height(this.xComponentHeight)
   15. }
   16. .width('100%')
   17. .height('100%')
   18. .backgroundColor(Color.Black)
   19. }
   20. .hideTitleBar(true)
   21. }
   22. }
   ```

   [Question2Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question2Incorrect.ets#L24-L62)

   **解决措施**

   使用[布局约束](../harmonyos-references/ts-universal-attributes-layout-constraints.md)的[aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)属性指定XComponent组件的宽高比，设置aspectRatio属性后，组件宽高会受父组件内容区大小限制。

   ```
   1. @Component
   2. export struct Question2Correct {
   3. @State aspect: number = 9 / 16; // default video width/height ratio value
   4. // ...

   6. build() {
   7. NavDestination() {
   8. Stack() {
   9. XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.xComponentController })
   10. // ...
   11. .aspectRatio(this.aspect)
   12. }
   13. .width('100%')
   14. .height('100%')
   15. .backgroundColor(Color.Black)
   16. }
   17. // ...
   18. }
   19. }
   ```

   [Question2Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question2Correct.ets#L24-L59)

   优化后效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/Y_hvdrgsQzeKDJWipFKtQg/zh-cn_image_0000002193851424.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=80670A32C15E5103BACF5595B0EAAA716D895DC067375ABF092FA1EF728BB7B3 "点击放大")
3. Video组件在分屏状态下截断。

   **问题现象**

   Video组件在分屏状态下，视频播放界面被截断显示不全。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/_NayO_zsThyAu5SsKpH56w/zh-cn_image_0000002193851404.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=0EAE5A029C8A3E08F63BA09F352E1A062803FDA4A7341F02203130C8B8C1A2E9 "点击放大")

   优化前示例代码如下：

   ```
   1. @Component
   2. export struct Question3Incorrect {
   3. build() {
   4. NavDestination() {
   5. Column() {
   6. Video({ src: $rawfile('testVideo2.mp4') })
   7. .height('100%')
   8. .width('100%')
   9. .autoPlay(true)
   10. .controls(false)
   11. }
   12. .height('100%')
   13. .width('100%')
   14. }
   15. .hideTitleBar(true)
   16. }
   17. }
   ```

   [Question3Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question3Incorrect.ets#L21-L37)

   **可能原因**

   给Video组件宽高设置的均为100%，Video组件默认保持宽高比进行缩小或者放大，使得视频铺满屏幕。当应用分屏后，由于窗口宽度不变，高度变为原来的1/2，Video组件的高度会超出窗口高度，导致视频显示不全。

   **解决措施**

   给Video组件设置.objectFit(ImageFit.Contain)属性，使视频保持宽高进行缩小或者放大，使得视频完全显示在Video组件边界内，优化后示例代码如下：

   ```
   1. @Component
   2. export struct Question3Correct {
   3. build() {
   4. NavDestination() {
   5. Column() {
   6. Video({ src: $rawfile('testVideo2.mp4') })
   7. // ...
   8. .objectFit(ImageFit.Contain)
   9. }
   10. .height('100%')
   11. .width('100%')
   12. }
   13. .hideTitleBar(true)
   14. }
   15. }
   ```

   [Question3Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question3Correct.ets#L22-L41)

   优化后效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Mf2Iv_J0RPahGG6IRpN-FA/zh-cn_image_0000002229336797.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=7261414AE9A82F67A625C87C2BAB689BA7824A55753A37C5846D875A607721EA "点击放大")
4. 子组件超出父组件的范围。

   **问题现象**

   子组件显示超出了父组件范围，无法通过上下滑动显示完全。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/B0G2s14wROOLH66JHepv9Q/zh-cn_image_0000002229336773.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=7CF5F689E0F2ECD70751AC3675268EE5F79FDCB214E57A7CBFDFEBFB399B8F79 "点击放大")

   优化前示例代码如下：

   ```
   1. @Component
   2. export struct Question4Incorrect {

   4. @Builder
   5. customDialogComp() {
   6. Column() {
   7. Text('Top')
   8. // ...

   10. Scroll() {
   11. Text('Middle')
   12. // ...
   13. }
   14. .layoutWeight(1)

   16. Text('Bottom')
   17. // ...
   18. }
   19. .height(500)
   20. .justifyContent(FlexAlign.SpaceBetween)
   21. }

   23. build() {
   24. // ...
   25. }
   26. }
   ```

   [Question4Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question4Incorrect.ets#L23-L96)

   **可能原因**

   子组件设置为了固定值，当应用分屏的时候，屏幕高度变为原来的1/2，父组件高度会随之变小。如果此时子组件高度大于父组件，就会导致子组件无法完全显示。

   **解决措施**

   子组件使用constraintSize约束子组件跟随父容器的大小，建议用子组件占用父组件的高度百分比，而不是绝对值，优化后示例代码如下：

   ```
   1. @Builder
   2. customDialogComp() {
   3. Column() {
   4. Text('Top')
   5. // ...

   7. Scroll() {
   8. Text('Middle')
   9. // ...
   10. }
   11. .layoutWeight(1)

   13. Text('Bottom')
   14. // ...
   15. }
   16. .height(500)
   17. .justifyContent(FlexAlign.SpaceBetween)
   18. .constraintSize({
   19. maxHeight: '90%'
   20. })
   21. }
   ```

   [Question4Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question4Correct.ets#L26-L67)

   优化后效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/-CmNNvvIQIqwDObgyZ4Q_w/zh-cn_image_0000002194010984.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=65A0ABC9232228D586AC04FA0272DD7C6839ED50D8A871D34AD3D5CDC8A2269C "点击放大")
5. Image组件在分屏状态下显示异常。

   **问题现象**

   应用进入分屏后，随着窗口变小，Image组件显示不全，页面布局显示异常。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/RhXwoztqRrGkEolFSxbX1w/zh-cn_image_0000002194011000.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=5A7AD6DFE77215C05945135FA1C7C032FDF42C24A680D2728C35F8F87FE43EFB "点击放大")

   优化前示例代码如下：

   ```
   1. @Component
   2. export struct Question5Incorrect {
   3. build() {
   4. NavDestination() {
   5. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
   6. Text("Login Page")
   7. // ...
   8. Text("Login in to access more services")
   9. // ...

   11. Image($r('app.media.login_pic'))
   12. // ...

   14. Column() {
   15. TextInput({ placeholder:  "Account" })
   16. // ...

   18. TextInput({ placeholder:"Password" })
   19. // ...
   20. }
   21. // ...

   23. Button($r('app.string.login'))
   24. // ...
   25. }
   26. // ...
   27. }
   28. // ...
   29. }
   30. }
   ```

   [Question5Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question5Incorrect.ets#L22-L102)

   **可能原因**

   在进入分屏页面，窗口的height变成了屏幕的1/2，导致image组件的height变小，image图片形变。

   **解决措施**

   推荐开发者通过一多的[隐藏能力](bpta-multi-device-adaptive-layout.md#隐藏能力)来实现，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏，通过设置布局优先级（displayPriority属性）来控制显隐。示例代码如下：

   ```
   1. @Component
   2. export struct Question5Correct {
   3. build() {
   4. NavDestination() {
   5. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
   6. Text("Login Page")
   7. // ...
   8. .displayPriority(4)

   10. Text("Login in to access more services")
   11. // ...
   12. .displayPriority(3)

   14. Image($r('app.media.login_pic'))
   15. // ...
   16. .displayPriority(2)

   18. Column() {
   19. TextInput({ placeholder: "Account" })
   20. // ...

   22. TextInput({ placeholder: "Password" })
   23. // ...
   24. }
   25. // ...
   26. .displayPriority(5)
   27. // ...
   28. Button($r('app.string.login'))
   29. // ...
   30. .displayPriority(5)
   31. }
   32. // ...
   33. }
   34. // ...
   35. }
   36. }
   ```

   [Question5Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question5Correct.ets#L22-L102)

   优化后效果如下图所示：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/2qrzZwwyQZCVxv9R3Lf8WA/zh-cn_image_0000002193851432.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=DB2A8A1D5F4674D28D576C38CFC4936D8C77A681C879263EE4465893580E8BA3 "点击放大")
6. 弹窗布局错乱。

   **问题现象**

   进入分屏后弹窗页面内容显示错乱，底部按钮挡住弹窗内容。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/kjgBUdQITJO6IqM1WSTPMw/zh-cn_image_0000002229336789.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=1C91F3F7B58AC309256E202DF7544E04AA2A83257A76AC8DE353FBCF768593A2 "点击放大")

   优化前示例代码如下：

   ```
   1. @CustomDialog
   2. struct CustomDialogComp1 {
   3. controller: CustomDialogController = new CustomDialogController({ 'builder': '' });

   5. build() {
   6. Column() {
   7. Text($r('app.string.welcome'))
   8. // ...

   10. Column() {
   11. Scroll() {
   12. Text($r('app.string.dialog_content'))
   13. // ...
   14. }
   15. }

   17. Row({ space: 12 }) {
   18. Button($r('app.string.disagree'))
   19. // ...
   20. Button($r('app.string.agree'))
   21. // ...
   22. }
   23. .height(56)
   24. .alignItems(VerticalAlign.Top)
   25. .position({
   26. bottom: 0,
   27. left: 0
   28. })
   29. }
   30. .constraintSize({
   31. maxHeight: '80%'
   32. })
   33. // ...
   34. }
   35. }
   ```

   [Question6Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question6Incorrect.ets#L22-L83)

   **可能原因**

   应用未考虑分屏窗口尺寸变小的情况，弹窗高度设置为固定值，且底部按钮使用position属性设置了固定位置，导致整体布局错乱。

   **解决措施**

   使用constraintSize属性给弹窗高度限定最大值，同时使用Scroll组件包裹弹窗内容区域（一多的[延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力)），通过给内容区域的Column组件设置layoutWeight（一多的[占比能力](bpta-multi-device-adaptive-layout.md#占比能力)）属性，使其占据剩余空间，使操作按钮居于底部显示。当内容高度超过内容区域高度的时候可以滚动进行查看，优化后示例代码如下：

   ```
   1. @CustomDialog
   2. struct CustomDialogComp {
   3. controller: CustomDialogController = new CustomDialogController({ 'builder': '' });

   5. build() {
   6. Column() {
   7. Text($r('app.string.welcome'))
   8. // ...

   10. Column() {
   11. Scroll() {
   12. Text($r('app.string.dialog_content'))
   13. // ...
   14. }
   15. }
   16. .layoutWeight(1)

   18. Row({ space: 12 }) {
   19. Button($r('app.string.disagree'))
   20. // ...
   21. Button($r('app.string.agree'))
   22. // ...
   23. }
   24. .height(56)
   25. .alignItems(VerticalAlign.Top)
   26. }
   27. .constraintSize({
   28. maxHeight: '80%'
   29. })
   30. .height(400)
   31. // ...
   32. }
   33. }
   ```

   [Question6Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question6Correct.ets#L22-L80)

   优化后效果如下图所示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/NDYptKDbQRKR4A7E1PBCXg/zh-cn_image_0000002229336769.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=9E2202256C50EA68E54D0693C2241CCF57FC2D8747AFE20E130BE5C2664522C5 "点击放大")

### 沉浸模式下顶部窗口控制条避让问题

**沉浸式应用在悬浮窗场景下顶部操作栏无法操作**

**问题现象**

应用分屏后视图和悬浮窗顶部重合的区域无法响应操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/jSu3xgZNRT-kYQ0rg9hhrA/zh-cn_image_0000002193851420.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=4491659F281333C76E78C7E7ED12E6A501035F2DE13C9C1F041AB6BAAE5E189D "点击放大")

优化前示例代码如下：

```
1. @Component
2. export struct Question7Incorrect {
3. private windowClass: window.Window | undefined = undefined;

5. aboutToAppear(): void {
6. try {
7. this.windowClass=(this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
8. this.windowClass.setSpecificSystemBarEnabled('status', false).catch((error:BusinessError) => {
9. Logger.error(TAG, `setSpecificSystemBarEnabled err, code: ${error.code}, message: ${error.message}`);
10. });
11. } catch (err) {
12. let error = err as BusinessError;
13. Logger.error(TAG, `aboutToAppear err, code: ${error.code}, message: ${error.message}`);
14. }
15. }

17. aboutToDisappear(): void {
18. this.windowClass?.setSpecificSystemBarEnabled('status', true).catch((error:BusinessError) => {
19. Logger.error(TAG, `setSpecificSystemBarEnabled err, code: ${error.code}, message: ${error.message}`);
20. });
21. }

23. build() {
24. NavDestination() {
25. Stack() {
26. // ...

28. Row() {
29. Image($r('app.media.icon_pause'))
30. // ...
31. .onClick(() => {
32. try {
33. this.getUIContext().getPromptAction().showToast({
34. message: 'Action success'
35. });
36. } catch (err) {
37. let error = err as BusinessError;
38. Logger.error(TAG, `showToast err, code: ${error.code}, message: ${error.message}`);
39. }
40. })
41. }
42. .height('100%')
43. .width('100%')
44. .justifyContent(FlexAlign.End)
45. .alignItems(VerticalAlign.Top)
46. }
47. }
48. .hideTitleBar(true)
49. }
50. }
```

[Question7Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question7Incorrect.ets#L28-L86)

**可能原因**

沉浸式应用顶部没有避让，导致悬浮窗顶部bar与应用的顶部区域重叠，重叠区域中的按钮无法响应点击事件。

**解决措施**

通过[getWindowAvoidArea](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口可获取屏幕顶部需要规避的矩阵区域topRect，获取到该值后应用可对应做布局避让。同时可通过[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)监听系统规避区域变化以进行布局的动态调整。具体可以参考[顶部窗口控制条避让适配智慧多窗](../harmonyos-guides/multi-window-controlbar-adapt.md)，优化后示例代码如下：

```
1. @Component
2. export struct Question7Correct {
3. private windowClass: window.Window | undefined = undefined;
4. @State topSafeHeight: number = 0;
5. @State windowStatus: WindowStatusType = window.WindowStatusType.FULL_SCREEN;

7. aboutToAppear(): void {
8. try {
9. this.windowClass=(this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
10. this.windowClass.setSpecificSystemBarEnabled('status', false).catch((error:BusinessError) => {
11. Logger.error(TAG, `setSpecificSystemBarEnabled err, code: ${error.code}, message: ${error.message}`);
12. });
13. this.windowStatus = this.windowClass.getWindowStatus();

15. if (this.windowStatus === window.WindowStatusType.FLOATING) {
16. this.topSafeHeight = this.getUIContext()
17. .px2vp(this.windowClass.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
18. }

20. this.windowClass.on('windowStatusChange', data => {
21. if (data === window.WindowStatusType.FLOATING) {
22. this.topSafeHeight =
23. this.getUIContext()
24. .px2vp(this.windowClass?.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM).topRect.height);
25. } else {
26. this.topSafeHeight = 0;
27. }
28. })
29. } catch (err) {
30. let error = err as BusinessError;
31. Logger.error(TAG, `aboutToAppear err, code: ${error.code}, message: ${error.message}`);
32. }
33. }

35. aboutToDisappear(): void {
36. this.windowClass?.setSpecificSystemBarEnabled('status', true).catch((error:BusinessError) => {
37. Logger.error(TAG, `setSpecificSystemBarEnabled err, code: ${error.code}, message: ${error.message}`);
38. });
39. }

41. build() {
42. // ...
43. }
44. }
```

[Question7Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question7Correct.ets#L28-L102)

优化后效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/NIQ98VZrTT6FcMWIFOfN0g/zh-cn_image_0000002229451253.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=478CE2E683EA0949967082B3E579C8A9CCA7CD1D93C434E31C4BD1B9D193618C "点击放大")

### 横向悬浮窗适配问题

**视频播放未适配横向悬浮窗**

**问题现象**

视频或者游戏类应用在横屏模式下，开启悬浮窗后，页面没有适配横屏，导致内容显示不全或者观看体验不好。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/t9ENWV-iSVi0WX_GzGHvbg/zh-cn_image_0000002229451281.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=C8F1E90F66C674B0EC801D12009147214E52A869B71B5871E3E223C8B89180A4 "点击放大")

优化前示例代码如下：

```
1. @Component
2. export struct Question8Incorrect {
3. build() {
4. NavDestination() {
5. Column() {
6. Video({ src: $rawfile('testVideo1.mp4') })
7. .height('100%')
8. .width('100%')
9. .autoPlay(true)
10. .objectFit(ImageFit.Contain)
11. .controls(false)
12. }
13. .height('100%')
14. .width('100%')
15. }
16. .hideTitleBar(true)
17. }
18. }
```

[Question8Incorrect.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question8Incorrect.ets#L21-L38)

**可能原因**

悬浮窗默认是竖屏，需要应用主动适配横屏的属性值。

**解决措施**

开发者可以通过在module.json5配置文件中abilities标签下的preferMultiWindowOrientation属性增加“landscape\_auto”。

```
1. {
2. "module": {
3. // ...
4. "abilities": [
5. {
6. "name": "EntryAbility",
7. // ...
8. "preferMultiWindowOrientation": "landscape_auto"
9. }
10. ],
11. // ...
12. }
13. }
```

[module.json5](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/module.json5#L2-L59)

该场景下多窗布局动态可变为横向，需要配合API（enableLandscapeMultiWindow / disableLandscapeMultiWindow）使用。

```
1. @Component
2. export struct Question8Correct {
3. private windowClass: window.Window | undefined = undefined;

5. aboutToAppear(): void {
6. try {
7. this.windowClass=(this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindowSync();
8. this.windowClass.enableLandscapeMultiWindow().catch((error:BusinessError) => {
9. Logger.error(TAG, `enableLandscapeMultiWindow err, code: ${error.code}, message: ${error.message}`);
10. });
11. } catch (err) {
12. let error = err as BusinessError;
13. Logger.error(TAG, `aboutToAppear err, code: ${error.code}, message: ${error.message}`);
14. }

17. }

19. aboutToDisappear(): void {
20. this.windowClass?.disableLandscapeMultiWindow().catch((error:BusinessError) => {
21. Logger.error(TAG, `disableLandscapeMultiWindow err, code: ${error.code}, message: ${error.message}`);
22. });
23. }

25. build() {
26. // ...
27. }
28. }
```

[Question8Correct.ets](https://gitcode.com/harmonyos_samples/MultiWindowPractice/blob/master/entry/src/main/ets/pages/Question8Correct.ets#L29-L70)

优化后效果如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/pkGNX8OvRImIe3Y2EiqAfg/zh-cn_image_0000002194010976.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061050Z&HW-CC-Expire=86400&HW-CC-Sign=00700E8EA9CFEF521CFB412E4DA865DE3D300FF9EAB54EB322F0B2B1BFBBE26A "点击放大")

## 总结

智慧多窗中的悬浮窗和分屏能力是系统提供的，开发者不需要人为进行功能开发，但是开发者需要重点关注是悬浮窗/分屏模式下的应用的布局适配问题。下面总结了一些常见的布局适配经验：

* 如果应用不需要使用悬浮窗/分屏能力，建议只声明supportWindowMode的值为“fullscreen”。
* 开发者可以参考[一次开发，多端部署概览](bpta-multi-device-overview.md)中关于页面开发的[多设备界面开发](bpta-multi-device-page.md)，避免应用在使用悬浮窗/分屏能力时，页面出现截断、挤压、堆叠等现象。
* 通过[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法来动态的设置应用是否沉浸，从而确认是否规避状态栏。
* 在悬浮窗模式下，通过[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)方法来获取状态栏高度，使应用内容区域规避状态栏。
