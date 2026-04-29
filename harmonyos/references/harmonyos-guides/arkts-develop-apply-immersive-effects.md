---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects
title: 开发应用沉浸式效果
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 组件布局 > 开发应用沉浸式效果
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5e93eddc584e582a8b52d9132595bdeeb22f6093770b950b8813a885b2353de3
---

## 概述

典型应用全屏窗口UI元素包括顶部[状态栏](../design-guides/status-bar-0000001776775568.md)、应用界面和底部导航区域（根据用户设置可表现为[导航条](../design-guides/navigation-0000001957075737.md)或三键导航），其中状态栏和导航区域，通常在沉浸式布局下称为避让区；避让区之外的区域称为安全区。开发应用沉浸式效果主要指通过调整状态栏、应用界面和底部导航区域的显示效果来减少状态栏、导航条或三键导航等系统界面的突兀感，从而使用户获得最佳的UI体验。

**图1** 界面元素示意图（此处以导航区域表现为导航条为例给出示意）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/iSPjEjRTTaKjFxw39QXR7g/zh-cn_image_0000002589324115.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=1A42DF2ACB43F57012AAA35E13E62CC0F0AEFE856C9ABA64E755EA6DA66F461D)

开发应用沉浸式效果主要要考虑如下几个设计要素：

* UI元素避让处理：底部导航区域可以响应点击事件，除此之外的可交互UI元素和应用关键信息不建议放到导航区域。状态栏显示系统信息，如果与界面元素有冲突，需要考虑避让状态栏。
* 沉浸式效果处理：设置状态栏的颜色和导航区域的显隐与界面元素颜色相匹配，不出现明显的突兀感。

针对上面的设计要求，可以通过如下两种方式实现应用沉浸式效果：

* [窗口全屏布局方案](arkts-develop-apply-immersive-effects.md#窗口全屏布局方案)：调整布局系统为全屏布局，界面元素延伸到状态栏和导航区域实现沉浸式效果。当不隐藏避让区时，可通过接口查询状态栏和导航区域进行可交互元素避让处理，并设置状态栏或导航区域的颜色或显隐等属性与界面元素匹配。当隐藏避让区时，通过对应接口设置全屏布局即可。
* [组件安全区方案](arkts-develop-apply-immersive-effects.md#组件安全区方案)：布局系统保持安全区内布局，然后通过接口延伸绘制内容（如背景色，背景图）到状态栏和导航区域实现沉浸式效果。该方案下，界面元素仅做绘制延伸，无法单独布局到状态栏和导航区域，针对需要单独布局UI元素到状态栏和导航区域的场景建议使用窗口全屏布局方案处理。

## 窗口全屏布局方案

窗口全屏布局方案主要涉及以下[应用扩展布局，全屏显示，不隐藏避让区](arkts-develop-apply-immersive-effects.md#应用扩展布局全屏显示不隐藏避让区)和[应用扩展布局，隐藏避让区](arkts-develop-apply-immersive-effects.md#应用扩展布局隐藏避让区)两个应用场景。

### 应用扩展布局，全屏显示，不隐藏避让区

可以通过调用窗口强制全屏布局接口[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)实现界面元素延伸到状态栏和导航区域；然后通过接口[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)和[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)获取并动态监听避让区域的变更信息，页面布局根据避让区域信息进行动态调整；设置状态栏或导航区域的颜色或显隐等属性与界面元素进行匹配。

1. 调用setWindowLayoutFullScreen()接口设置窗口全屏。

   ```
   1. // EntryAbility.ets
   2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. export default class EntryAbility extends UIAbility {
   7. // ...

   9. onWindowStageCreate(windowStage: window.WindowStage): void {
   10. windowStage.loadContent('pages/Index', (err, data) => {
   11. if (err.code) {
   12. return;
   13. }

   15. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
   16. // 1. 设置窗口全屏
   17. let isLayoutFullScreen = true;
   18. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
   19. console.info('Succeeded in setting the window layout to full-screen mode.');
   20. }).catch((err: BusinessError) => {
   21. console.error(`Failed to set the window layout to full-screen mode. Code is ${err.code}, message is ${err.message}`);
   22. });
   23. // 进行后续步骤2-3中的操作
   24. });
   25. }
   26. }
   ```
2. 使用[getWindowAvoidArea()](../harmonyos-references/arkts-apis-window-window.md#getwindowavoidarea9)接口获取当前布局遮挡区域（此处以状态栏、导航区域为例）。

   ```
   1. // EntryAbility.ets
   2. // 2. 获取布局避让遮挡的区域
   3. let type = window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR; // 此处以导航条避让为例
   4. let avoidArea = windowClass.getWindowAvoidArea(type);
   5. let bottomRectHeight = avoidArea.bottomRect.height; // 获取到导航区域的高度
   6. AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);

   8. type = window.AvoidAreaType.TYPE_SYSTEM; // 以状态栏避让为例
   9. avoidArea = windowClass.getWindowAvoidArea(type);
   10. let topRectHeight = avoidArea.topRect.height; // 获取状态栏区域高度
   11. AppStorage.setOrCreate('topRectHeight', topRectHeight);
   ```
3. 注册监听函数，动态获取避让区域的实时数据。常见的触发避让区回调的场景如下：应用窗口在全屏模式、悬浮模式、分屏模式之间的切换；应用窗口旋转；多折叠设备在屏幕折叠态和展开态之间的切换；应用窗口在多设备之间的流转。

   ```
   1. // EntryAbility.ets
   2. // 3. 注册监听函数，动态获取避让区域数据
   3. windowClass.on('avoidAreaChange', (data) => {
   4. if (data.type === window.AvoidAreaType.TYPE_SYSTEM) {
   5. let topRectHeight = data.area.topRect.height;
   6. AppStorage.setOrCreate('topRectHeight', topRectHeight);
   7. } else if (data.type == window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR) {
   8. let bottomRectHeight = data.area.bottomRect.height;
   9. AppStorage.setOrCreate('bottomRectHeight', bottomRectHeight);
   10. }
   11. });
   ```
4. 布局中的UI元素需要避让状态栏和导航区域，否则可能产生UI元素重叠等情况。

   说明

   避让区域存在大小为0的情况，当获取到的避让区域为0时，开发者需注意针对性处理适配此时的页面区域和布局，避免贴边、内容裁剪等问题，影响应用界面正常显示或美观性。

   如下例子中，对控件顶部设置padding（具体数值与状态栏高度一致），实现对状态栏的避让；对底部设置padding（具体数值与底部导航区域高度一致），实现对导航条的避让。如果去掉顶部和底部的padding设置，即不避让状态栏和导航条，UI元素就会发生重叠。具体可见下文步骤中图2和图3的效果对比。

   ```
   1. // Index.ets
   2. @Entry
   3. @Component
   4. struct Index {
   5. @StorageProp('bottomRectHeight')
   6. bottomRectHeight: number = 0;
   7. @StorageProp('topRectHeight')
   8. topRectHeight: number = 0;

   10. build() {
   11. Column() {
   12. Row() {
   13. Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
   14. }.backgroundColor('#2786d9')

   16. Row() {
   17. Text('Display Content 2').fontSize(30)
   18. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   20. Row() {
   21. Text('Display Content 3').fontSize(30)
   22. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   24. Row() {
   25. Text('Display Content 4').fontSize(30)
   26. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   28. Row() {
   29. Text('Display Content 5').fontSize(30)
   30. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   32. Row() {
   33. Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
   34. }.backgroundColor('#96dffa')
   35. }
   36. .width('100%')
   37. .height('100%')
   38. .alignItems(HorizontalAlign.Center)
   39. .backgroundColor('#d5d5d5')
   40. .justifyContent(FlexAlign.SpaceBetween)
   41. // top数值与状态栏区域高度保持一致；bottom数值与导航区域高度保持一致
   42. .padding({
   43. top: this.getUIContext().px2vp(this.topRectHeight),
   44. bottom: this.getUIContext().px2vp(this.bottomRectHeight)
   45. })
   46. }
   47. }
   ```
5. 根据实际的UI界面显示或相关UI元素背景颜色等，还可以按需设置状态栏的文字颜色、背景色或设置导航区域的显示或隐藏，以使UI界面效果呈现和谐。状态栏和导航区域默认是透明的，透传的是应用界面的背景色。

   此例中UI颜色主要有两种，比较简单，故未对状态栏文字颜色、背景色进行设置，未对导航区域进行隐藏。

   **图2** 布局避让状态栏和导航区域（此处以导航区域表现为导航条为例给出示意）

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/NpO18eUFTU2POQIVrK3POQ/zh-cn_image_0000002589244055.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=70531CB68D3888AF9D24A49DD89E89C7E8DFFD12E63A6E3DDC6EB0218C27D0FF)

   **图3** 布局未避让状态栏和导航区域，UI元素重叠（此处以导航区域表现为导航条为例给出示意）

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/b4URPLEQSci386e1NB6yEw/zh-cn_image_0000002558764248.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=822ED9C9AD42AFE184E73D1727A53AC7918A8D0F15293AE7EC8267509917A043)

### 应用扩展布局，隐藏避让区

此场景下状态栏和导航区域需要隐藏，适用于游戏、电影等应用场景。用户可以通过从底部上滑唤出导航条或三键导航。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Z5yrPDIbSQOzDqfZq7OYQw/zh-cn_image_0000002558604592.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=F13F5C677A9B22BB0EFB8D96FF2AEE2A3D34A8394FF7C58767F4A095638048FF)

1. 调用setWindowLayoutFullScreen()接口设置窗口全屏。

   ```
   1. // EntryAbility.ets
   2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   3. import { window } from '@kit.ArkUI';
   4. import { BusinessError } from '@kit.BasicServicesKit';

   6. export default class EntryAbility extends UIAbility {
   7. // ...

   9. onWindowStageCreate(windowStage: window.WindowStage): void {
   10. windowStage.loadContent('pages/Index', (err, data) => {
   11. if (err.code) {
   12. return;
   13. }

   15. let windowClass: window.Window = windowStage.getMainWindowSync(); // 获取应用主窗口
   16. // 1. 设置窗口全屏
   17. let isLayoutFullScreen = true;
   18. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen).then(() => {
   19. console.info('Succeeded in setting the window layout to full-screen mode.');
   20. }).catch((err: BusinessError) => {
   21. console.error(`Failed to set the window layout to full-screen mode. Code is ${err.code}, message is ${err.message}`);
   22. });
   23. // 进行后续步骤2中的状态栏和导航区域的隐藏操作
   24. });
   25. }
   26. }
   ```
2. 调用[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)接口设置状态栏和导航区域的具体显隐状态，此场景下将其设置为隐藏。

   ```
   1. // EntryAbility.ets
   2. // 2. 设置状态栏隐藏
   3. windowClass.setSpecificSystemBarEnabled('status', false).then(() => {
   4. console.info('Succeeded in setting the status bar to be invisible.');
   5. }).catch((err: BusinessError) => {
   6. console.error(`Failed to set the status bar to be invisible. Code is ${err.code}, message is ${err.message}`);
   7. });
   8. // 2. 设置导航区域隐藏
   9. windowClass.setSpecificSystemBarEnabled('navigationIndicator', false).then(() => {
   10. console.info('Succeeded in setting the navigation indicator to be invisible.');
   11. }).catch((err: BusinessError) => {
   12. console.error(`Failed to set the navigation indicator to be invisible. Code is ${err.code}, message is ${err.message}`);
   13. });
   ```
3. 在界面中无需进行导航区域避让操作。

   ```
   1. // Index.ets
   2. @Entry()
   3. @Component
   4. struct Index {
   5. build() {
   6. Row() {
   7. Column() {
   8. Row() {
   9. Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
   10. }.backgroundColor('#2786d9')

   12. Row() {
   13. Text('Display Content 2').fontSize(30)
   14. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   16. Row() {
   17. Text('Display Content 3').fontSize(30)
   18. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   20. Row() {
   21. Text('Display Content 4').fontSize(30)
   22. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   24. Row() {
   25. Text('Display Content 5').fontSize(30)
   26. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

   28. Row() {
   29. Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
   30. }.backgroundColor('#96dffa')
   31. }
   32. .width('100%')
   33. .height('100%')
   34. .alignItems(HorizontalAlign.Center)
   35. .justifyContent(FlexAlign.SpaceBetween)
   36. .backgroundColor('#d5d5d5')
   37. }
   38. }
   39. }
   ```

## 组件安全区方案

应用未使用setWindowLayoutFullScreen()接口设置窗口全屏布局时，默认采取组件安全区布局方案。

应用在默认情况下窗口背景绘制范围是全屏，但UI元素被限制在安全区内（自动排除状态栏和导航区域）进行布局，来避免界面元素被状态栏和导航区域遮盖。

**图4** 界面元素自动避让状态栏和导航区域示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/vwQW-nuDQ7GAGItbklZSyg/zh-cn_image_0000002589324117.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=5A993B250B6BCF514B6F018E0407392C81EE85E599EDBE645B1AF54DD82A0415)

针对状态栏和导航区域颜色与界面元素颜色不匹配问题，可以通过如下两种方式实现沉浸式效果：

* 状态栏和导航区域颜色相同场景，可以通过设置窗口的背景色来实现沉浸式效果。窗口背景色可通过[setWindowBackgroundColor()](../harmonyos-references/arkts-apis-window-window.md#setwindowbackgroundcolor9)进行设置。

  ```
  1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
  2. import { window } from '@kit.ArkUI';

  4. export default class EntryAbility extends UIAbility {
  5. // ...

  7. onWindowStageCreate(windowStage: window.WindowStage): void {
  8. windowStage.loadContent('pages/Index', (err) => {
  9. if (err.code) {
  10. return;
  11. }

  13. // 设置全窗颜色和应用元素颜色一致
  14. windowStage.getMainWindowSync().setWindowBackgroundColor('#d5d5d5');
  15. });
  16. }
  17. }
  ```

  界面状态栏和导航区域颜色相同场景。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct Example {
  5. build() {
  6. Column() {
  7. Row() {
  8. Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
  9. }.backgroundColor('#2786d9')

  11. Row() {
  12. Text('Display Content 2').fontSize(30)
  13. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  15. Row() {
  16. Text('Display Content 3').fontSize(30)
  17. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  19. Row() {
  20. Text('Display Content 4').fontSize(30)
  21. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  23. Row() {
  24. Text('Display Content 5').fontSize(30)
  25. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  27. Row() {
  28. Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
  29. }.backgroundColor('#96dffa')
  30. }
  31. .width('100%').height('100%')
  32. .alignItems(HorizontalAlign.Center)
  33. .backgroundColor('#d5d5d5')
  34. .justifyContent(FlexAlign.SpaceBetween)
  35. }
  36. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/iKbliZvjSRus7C6fOcKBYg/zh-cn_image_0000002589244057.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=955724528F344147EB0A66715EFECFAFBBCFB77FAAE4789C6FF130D858FB3287)
* 状态栏和导航区域颜色不同时，可以使用[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性扩展安全区域属性进行调整。

  ```
  1. // xxx.ets
  2. @Entry
  3. @Component
  4. struct Example {
  5. build() {
  6. Column() {
  7. Row() {
  8. Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
  9. }.backgroundColor('#2786d9')
  10. // 设置顶部绘制延伸到状态栏
  11. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

  13. Row() {
  14. Text('Display Content 2').fontSize(30)
  15. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  17. Row() {
  18. Text('Display Content 3').fontSize(30)
  19. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  21. Row() {
  22. Text('Display Content 4').fontSize(30)
  23. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  25. Row() {
  26. Text('Display Content 5').fontSize(30)
  27. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

  29. Row() {
  30. Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
  31. }.backgroundColor('#96dffa')
  32. // 设置底部绘制延伸到导航区域
  33. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
  34. }
  35. .width('100%').height('100%')
  36. .alignItems(HorizontalAlign.Center)
  37. .backgroundColor('#d5d5d5')
  38. .justifyContent(FlexAlign.SpaceBetween)
  39. }
  40. }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/bmFzvYOgQ8mNiw7WgtgiVQ/zh-cn_image_0000002558764250.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=52CAAC2D27E5307846EEAB39F69A2F79BEEA39A45105E5086BBE4BF161F9DA7C)

### 扩展安全区域属性原理

* 布局阶段按照安全区范围大小进行UI元素布局。
* 布局完成后查看设置了expandSafeArea的组件边界（不包括margin）是否和安全区边界相交。
* 如果设置了expandSafeArea的组件和安全区边界相交，根据expandSafeArea传递的属性则进一步扩大组件绘制区域大小覆盖状态栏、导航区域这些非安全区域。
* 上述过程仅改变组件自身绘制大小，不进行二次布局，不影响子节点和兄弟节点的大小和位置。
* 子节点可以单独设置该属性，只需要自身边界和安全区域重合就可以延伸自身大小至非安全区域内，需要确保父组件未设置clip等裁剪属性。
* 配置expandSafeArea属性组件进行绘制扩展时，需要关注组件不能配置固定宽高尺寸，百分比除外。
* 组件可以设置通用属性safeAreaPadding，给自身添加组件级安全区域。该属性作为一种特殊边距，在提供布局约束的同时作为安全区可以被一些系统组件利用。

  + safeAreaPadding位于原有的padding内侧。容器自外向内各层分别为border、padding、safeAreaPadding、内容区。当border和padding确定后，若容器可用空间不足以满足safeAreaPadding的设置，则优先分配给左侧和上侧safeAreaPadding、其次分配给右侧和下侧safeAreaPadding。safeAreaPadding实际尺寸确定后，余下空间为内容区。

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/cDjUfbKKSEybJQeK0sV-Qg/zh-cn_image_0000002558604594.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=9F0A80C517BE3360FF004AE7DAE984E85F0F31589A2A8AC5AEF40B116C960D35)
  + 系统组件如Navigation、List、Scroll、Tabs等可以利用外层或容器自身safeAreaPadding实现扩大裁剪范围等能力。

### 背景图和视频场景

设置背景图、视频组件大小为安全区域大小并配置expandSafeArea属性。

说明

Video组件在使用expandSafeArea扩展到安全区域时，组件视频显示内容区域不支持扩展。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SafeAreaExample1 {
5. build() {
6. Stack() {
7. Image($r('app.media.bg'))
8. .height('100%').width('100%')
9. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]) // 图片组件的绘制区域扩展至状态栏和导航区域。
10. }.height('100%').width('100%')
11. }
12. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/ZbhkFqQpSrqWxlrOw7P26Q/zh-cn_image_0000002589324119.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=3108EB894D95B8881366844B23661AD4C173BFDBC4D77AAA07067BBFA915A854)

### 滚动类场景

滚动容器设置expandSafeArea属性生效，但当父组件是滚动容器时，子组件设置expandSafeArea属性不生效。对于滚动容器的子组件，有两种方法实现沉浸式效果：

1. 设置父组件滚动容器和子组件相同的背景色，给父组件设置expandSafeArea属性扩展安全区。

   ```
   1. // xxx.ets
   2. @Entry
   3. @Component
   4. struct ScrollExample {
   5. scroller: Scroller = new Scroller()
   6. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

   8. build() {
   9. Stack({ alignContent: Alignment.TopStart }) {
   10. Scroll(this.scroller) {
   11. Column() {
   12. ForEach(this.arr, (item: number) => {
   13. Stack() {
   14. Text('Display Content ' + item.toString()).fontSize(30)
   15. }
   16. .width('80%').padding(20).borderRadius(15).backgroundColor(Color.White).margin({ top:30, bottom:30 })
   17. }, (item: string) => item)
   18. }.width('100%').backgroundColor('rgb(213,213,213)')
   19. }.backgroundColor('rgb(213,213,213)')
   20. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
   21. }.width('100%').height('100%')
   22. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
   23. }
   24. }
   ```

   **图5** 滚动类容器设置expandSafeArea属性实现沉浸式效果

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/gXsPhRBxSUiNJmeCGBmaDw/zh-cn_image_0000002589244059.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=4C20BBABC05A5333F38FFC055FCE0644A43D67A49C038B7C5257E02189D9B37A)
2. 设置父组件滚动容器和子组件相同的背景色，设置滚动容器的内容裁剪属性clipContent(ContentClipMode.SAFE\_AREA)，将内容层裁剪区域扩展至避让区。

   ```
   1. // xxx.ets
   2. @Entry
   3. @Component
   4. struct ScrollExample {
   5. scroller: Scroller = new Scroller()
   6. private arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

   8. build() {
   9. Stack({ alignContent: Alignment.TopStart }) {
   10. Scroll(this.scroller) {
   11. Column() {
   12. ForEach(this.arr, (item: number) => {
   13. Stack() {
   14. Text('Display Content ' + item.toString()).fontSize(30)
   15. }
   16. .width('80%').padding(20).borderRadius(15).backgroundColor(Color.White).margin({ top:30, bottom:30 })
   17. }, (item: string) => item)
   18. }.width('100%').backgroundColor('rgb(213,213,213)')
   19. }.backgroundColor('rgb(213,213,213)')
   20. .clipContent(ContentClipMode.SAFE_AREA)
   21. }.width('100%').height('100%')
   22. }
   23. }
   ```

**图6** 滚动类容器设置clipContent属性实现沉浸式效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/dn54Ke99SmGodLt9OB5R6w/zh-cn_image_0000002558764252.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=78AD70EBE5F8D90512CE2B9F19A3A977A61573086EE6E4649418C532906765B3)

### 底部页签场景

要求页签背景色能够延伸到导航区域（此处以导航区域表现为导航条为例给出示意），但页签内部可操作元素需要在导航区域之上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/jLfWCBUVRzOC7njR2pm7qA/zh-cn_image_0000002558604596.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=8ACDFF7B8374464B4BCD2981FF2D7663C22AC7739AC2E4C332E5DBC09BF18640)

针对底部的页签部分，Navigation组件和Tabs组件默认实现了页签的延伸处理，开发者只需要保证Navigation和Tabs组件的底部边界和底部导航区域重合即可。若开发者显式调用expandSafeArea接口，则安全区效果由expandSafeArea参数指定。

如果未使用上述组件而是采用自定义方式实现页签的场景，可以针对底部元素设置expandSafeArea属性实现底部元素的背景扩展。

**图7** 顶部和底部UI元素未设置和设置expandSafeArea属性效果对比

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/etOWWHpfSOCvEISnG7XMrQ/zh-cn_image_0000002589324121.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=09A1CA5B9DBCD97B38B98B0E9362A23D1C6B994D569594F45739A48B63B6A1B3)

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Example {
5. build() {
6. Column() {
7. Row() {
8. Text('Top Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
9. }.backgroundColor('#2786d9')
10. // 设置顶部绘制延伸到状态栏
11. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

13. Row() {
14. Text('Display Content 2').fontSize(30)
15. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

17. Row() {
18. Text('Display Content 3').fontSize(30)
19. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

21. Row() {
22. Text('Display Content 4').fontSize(30)
23. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

25. Row() {
26. Text('Display Content 5').fontSize(30)
27. }.backgroundColor(Color.White).padding(20).borderRadius(15).width('80%')

29. Row() {
30. Text('Bottom Content').fontSize(40).textAlign(TextAlign.Center).width('100%')
31. }.backgroundColor('#96dffa')
32. // 设置底部绘制延伸到导航区域
33. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
34. }
35. .width('100%').height('100%')
36. .alignItems(HorizontalAlign.Center)
37. .backgroundColor('#d5d5d5')
38. .justifyContent(FlexAlign.SpaceBetween)
39. }
40. }
```

### 图文场景

当状态栏元素和底部导航区域元素不同时，无法单纯通过窗口背景色或者背景图组件延伸实现，此时需要对顶部元素和底部元素分别配置expandSafeArea属性，顶部元素配置expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.TOP])，底部元素配置expandSafeArea([SafeAreaType.SYSTEM],[SafeAreaEdge.BOTTOM])。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/9YPZ7GUwR8eQhmobLLJvmQ/zh-cn_image_0000002589244061.png?HW-CC-KV=V1&HW-CC-Date=20260429T052739Z&HW-CC-Expire=86400&HW-CC-Sign=A07483D387E5CD06683E188A5C4324764E16AEB7676904A6DD48DE332D344A86)

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Swiper() {
6. Column() {
7. Image($r('app.media.start'))
8. .height('50%').width('100%')
9. // 设置图片延伸到状态栏
10. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])
11. Column() {
12. Text('HarmonyOS 第一课')
13. .fontSize(32)
14. .margin(30)
15. Text('通过循序渐进的学习路径，无经验和有经验的开发者都可以掌握ArkTS语言声明式开发范式，体验更简洁、更友好的HarmonyOS应用开发旅程。')
16. .fontSize(20).margin(20)
17. }.height('50%').width('100%')
18. .backgroundColor(Color.White)
19. // 设置文本内容区背景延伸到导航栏
20. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
21. }
22. }
23. .width('100%')
24. .height('100%')
25. // 关闭Swiper组件默认的裁剪效果以便子节点可以绘制在Swiper外。
26. .clip(false)
27. }
28. }
```
