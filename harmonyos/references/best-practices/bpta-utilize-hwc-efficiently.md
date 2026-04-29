---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-utilize-hwc-efficiently
title: 高效利用HWC的低功耗设计
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 前台任务低功耗 > 高效利用HWC的低功耗设计
category: best-practices
scraped_at: 2026-04-29T14:13:49+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:b196c83091f353344c1d189cad3d1c3587919e812b918a363a19c4a630f7f980
---

## 概述

在应用开发中，开发者可以自由组合ArkUI定义控件、视频、图片、Web网页以及第三方渲染框架生成内容，以满足应用UI界面的需求。同时，HarmonyOS系统基于的芯片平台除了通用的CPU/GPU计算单元外，还提供了[Hardware Composer](bpta-utilize-hwc-efficiently.md#li10223152812152)（下文简称HWC）专用硬件辅助系统进行图形渲染送显，相对于通用计算单元，在图层叠加场景具有更高的处理效率和更低的能耗。作为专用硬件单元，HWC需要满足一定条件才能充分发挥其硬件能力，降低系统CPU/GPU开销，减少发热和卡顿现象的出现。

因此，在开发类似Web界面、视频播放等多图层叠加场景时，如果存在自渲染图层，可以通过以下两种方式调整视效设计，扩大HWC的生效范围：

* 避免非必要高阶视效控件与自渲染内容区域产生交叠。
* 合理调整ArkUI定义控件与自渲染图层间的交叠关系。

开发者可以根据实际业务适当调整界面视效设计，使系统能够充分发挥HWC的能效优势，降低对应操作场景的功耗，提升操作流畅性。

说明

高阶视效控件是指具有复杂视觉效果的控件，如模糊、反色等。这些效果需要对背景进行采样、颜色计算等操作。

## 实现原理

系统接收到应用的UI界面元素由两类组成，一类是直接使用ArkUI提供的现有接口定义的控件，如按钮、进度条、导航栏等，可以称为UI控件。另外一类是应用直接传递已经渲染好的内容，包括视频、图片、Web页面或调用自有或者三方渲染框架已经渲染好的内容（下文统一归类为应用自渲染内容）。

1. 直接调用ArkUI接口定义的控件，例如Row、Column、Text等。

   ```
   1. @Entry
   2. @Component
   3. struct ArkUISample {
   4. @State message: string = 'Hello World';
   5. build() {
   6. Row() {
   7. Column() {
   8. Text(this.message)
   9. .fontSize(50)
   10. .fontWeight(FontWeight.Bold)
   11. }
   12. .width('100%')
   13. }
   14. .height('100%')
   15. }
   16. }
   ```

   [ArkUISample.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/ArkUISample.ets#L5-L20)

   该内容将由系统根据组件定义及布局进行绘制，用户应用程序不感知具体的绘制过程。
2. 应用自渲染内容。
   * Web页面：此时页面内容将直接替换为url地址传递的内容，使用示例见：[ArkWeb使用指导](bpta-arkweb_rendering_framework.md)。
   * 视频场景：该类使用示例见[视频播放开发实践](bpta-video-playback-development-practice.md)。
   * 三方或者自有渲染框架生成内容：使用Native Xcomponent组件和接口直接传递内容，使用示例见[Native XComponent的使用指导](../harmonyos-references/capi-oh-nativexcomponent-native-xcomponent.md)。

   这类内容在应用进程中解码或调用GPU渲染，然后作为整体传递给系统渲染服务进程。

系统在处理这两类界面元素时，会根据界面视效要求，综合调用GPU或HWC，以实现最佳能效。

### 图形渲染系统工作流程

下图介绍了图形渲染系统从应用界面内容到最终屏幕显示的工作流程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/QKxQ694tR5ip_VYh8E8Q2Q/zh-cn_image_0000002194011600.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=9B109663D4D81ED55080EF5B703798E141BA081130761A5C92971704C12BBE0D "点击放大")

* **RenderService (RS) ：**系统渲染服务进程，接收来自于其他系统服务进程（如桌面进程）及用户进程（如应用）的自渲染图层及ArkUI控件绘制指令，进行统一的组合以及渲染控制。其渲染调用CPU/GPU等计算器件，能力灵活，兼容性强，但功耗和性能开销较大。
* **Hardware Composer (HWC)：**HWC基于专用硬件构建，主要用于多图层叠加送显。接受RS绘制的图层和应用自渲染图层，将多个图层叠加后传递至屏幕。相对于GPU，HWC功耗和性能优势明显，但不具备复杂渲染能力。

### 图形渲染送显策略

当前系统的整体渲染送显策略描述如下：

RS进程将ArkUI控件统一绘制到UI图层。UI内容来自应用定义的ArkUI控件和桌面进程传递的内容，如状态栏、系统导航等。根据UI图层和应用自渲染内容的Z序关系，优先使用HWC的图层叠加功能进行送显处理。

在该过程中，UI控件的视效和自渲染图层的Z序关系会影响HWC的使用。例如，若自渲染图层上方的UI控件使用了模糊等高阶视效，模糊算法需要实时读取背景自渲染图层的内容，并在图层叠加时进行额外处理。此时，HWC无法使能，RS将使用GPU进行图层叠加。

### 如何高效使能HWC

这里结合HWC的特点以及当前系统的渲染送显策略给出如下两点建议，以提升HWC的生效范围，降低应用操作期间可能产生的发热及卡顿概率。

* **在存在自渲染图层的情况下，合理使用高阶视效控件，避免与自渲染内容产生交叠**

  如果UI控件使用模糊等高阶视效并与自渲染图层区域交叠，RS在绘制该控件时，需读取自渲染图层内容以正确绘制。相比无高阶视效的情况，此时需要额外读取内容，并直接使用GPU载入自渲染图层进行渲染。

  如上过程会带来额外的CPU、GPU、DDR开销，导致功耗增加和性能下降。因此，建议开发者合理评估UI界面的视效需求，通过移除模糊等高阶视效或调整控件位置等方式，避免非必要高阶视效控件与自渲染图层交叠。

  说明

  上述优化建议仅从功耗优化角度出发，需要调整界面的视效设计，开发者可根据需要自行选择。

  **注****：****典型高阶视效动作****列表**

  |  |  |
  | --- | --- |
  | **视效类型** | **A****rkUI接口** |
  | 背景模糊 | .blur()；.backdropBlur() |
  | 提亮 | .backgroundBrightness() |
  | 灰阶 | .grayscale() |
  | 阴影取色 | .shadow() |
  | 压暗提亮 | .lightUpEffect() |
  | 前景模糊 | .foregroundEffect() |
* **在存在自渲染图层的情况下，合理调整ArkUI定义控件与自渲染图层间的交叠关系**

  这里存在以下两种情况：

  1. UI控件定义在自渲染图层下方，且自渲染图层设置了一定透明度，导致自渲染图层无法完全遮挡UI控件。进行渲染处理时，需要额外处理透明度，此时只能使用GPU，无法使用HWC叠加能力。

     建议开发者评估自渲染图层设定透明度的必要性。若全透明，应及时下树。若UI控件需位于自渲染图层下方，建议该控件也使用自渲染形式实现。
  2. 两个或以上自渲染图层所在控件设定圆角且存在区域交叠时，进行自渲染图层处理需要GPU额外绘制圆角，这会导致无法使用HWC叠加能力。

     建议评估是否需要多个自渲染图层交叠及底部图层圆角是否可以去除。

  以下是一些典型场景：

  1. UI控件上方的视频图层具有一定透明度。
  2. 在视频弹幕图层和视频图层间直接用ArkUI控件定义水印控件。
  3. 多个视频窗口存在交叠且视频窗口存在圆角。

## 场景案例

### 场景一：在视频区域上方合理使用模糊控件

**效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/Uo49-bfJQDaEAYrncyccZw/zh-cn_image_0000002194011604.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=D2B056636FB7BE7F7657419C22379F0B9087267CA7F38BE4A49019F9C47EDC3F "点击放大")

如上图，视频区域左上角的返回按钮控件带有模糊效果，需要进行视频图层采样，无法使用HWC叠加。可以通过移除控件的模糊效果或将其移动到非视频区域来启用HWC。

此处通过去除控件的模糊效果来使能HWC，从而优化场景功耗。相应对比代码如下：

**视频上方叠加带有模糊效果的Image组件**

```
1. @Entry
2. @Component
3. struct VideoWithBlur {
4. // ...
5. build() {
6. NavDestination() {
7. Stack() {
8. // Video Layer
9. Video({
10. src: $r('app.media.test_video')
11. })
12. .height('100%')
13. .width('100%')
14. .loop(true)
15. .autoPlay(true)
16. .controls(false)

18. RelativeContainer() {
19. Row() {
20. // The return button has a blurry effect
21. Image($r('app.media.chevron_left'))
22. .padding(12)
23. .width(40)
24. .height(40)
25. .borderRadius('50%')
26. .fillColor('rgba(255, 255, 255, 0.9)')
27. .backgroundColor('rgba(0, 0, 0, 0.1)')
28. .backdropBlur(40) // Set this component background blur
29. .backgroundBlurStyle(BlurStyle.BACKGROUND_REGULAR)
30. // ...
31. }
32. // ...
33. }
34. .width('100%')
35. .height('100%')
36. .padding({
37. left: 16,
38. right: 16,
39. top: 36,
40. bottom: 44
41. })
42. }
43. .width('100%')
44. .height('100%')
45. }
46. // ...
47. }
```

[VideoWithBlur.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/VideoWithBlur.ets#L26-L165)

**视频上方Image组件去除模糊效果**

```
1. @Component
2. struct NormalVideo {
3. // ...
4. build() {
5. NavDestination() {
6. Stack() {
7. // Video Layer
8. Video({
9. src: $r('app.media.test_video')
10. })
11. .height('100%')
12. .width('100%')
13. .loop(true)
14. .autoPlay(true)
15. .controls(false)

17. RelativeContainer() {
18. Row() {
19. // The return button does not have a blur effect
20. Image($r('app.media.chevron_left'))
21. .padding(12)
22. .width(40)
23. .height(40)
24. .borderRadius('50%')
25. .fillColor('rgba(255, 255, 255, 0.9)')
26. .backgroundColor('rgba(0, 0, 0, 0.1)')
27. // ...
28. }
29. // ...
30. }
31. .width('100%')
32. .height('100%')
33. .padding({
34. left: 16,
35. right: 16,
36. top: 36,
37. bottom: 44
38. })
39. }
40. .width('100%')
41. .height('100%')
42. }
43. // ...
44. }
```

[NormalVideo.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/NormalVideo.ets#L24-L151)

去除模糊后的效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/ZYCOkms5Q6G4RXBJjZt9oA/zh-cn_image_0000002193852036.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=749564A2539812ADECE87208AC2B4F2C737AA6853D7AE1A293D60FB713CDB932 "点击放大")

**功耗对比**

同一界面下，测试视频区域上方控件去除模糊效果前后的CPU模块、GPU模块的功耗，以及设备总功耗。测试方式为视频播放30s，以3s为一个节点，取设备从6s运行到21s5个节点的平均功耗。最终，使用DevEco Studio的Profiler工具检测得到的数据如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/1gWqVuM1Q-aPMuywNpqMUg/zh-cn_image_0000002194011620.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=C3ED5CE6D4AB0D61975B4335854730B4410C1D1E85E9FF13CA029FF6666462C6 "点击放大")

从测试数据可以看出：

1. 视频区域上方控件去除模糊效果后，CPU模块功耗下降64.7%，GPU模块功耗降至0，降幅100%。
2. 视频区域上方控件去除模糊效果后，总功耗明显下降，降幅约为22.8%。

测试数据表明，在视频播放场景下，去除视频区域上方控件的模糊效果并使能HWC，可以大幅减少GPU和CPU的功耗，同时显著降低设备总体功耗。

### **场景二：在Web类界面上方合理使用模糊控件**

**效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/9d9iNwLFRPmXxmaVD7tqAQ/zh-cn_image_0000002229337409.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=D786379F68463C2AF2D3F3F42BB07E0EA7CB1A6A823FC03B586132B47E492865 "点击放大")

在该场景下，底部TabBar区域使用模糊，且背景区域使用Web类组件或者Native Xcomponent组件导入自渲染内容，同样导致UI图层与自渲染内容无法使用HWC叠加。对此开发者可以通过去除TabBar区域的模糊视效或者裁剪组件区域避免Web内容与模糊控件相交两种方式进行修改，以达到使用HWC降低功耗的目的。

此处通过移除控件的模糊效果来启用HWC，从而优化场景功耗。相应对比代码如下：

**Web组件上方TabBar控件模糊**

```
1. import { webview } from '@kit.ArkWeb';
2. // ...
3. @Entry
4. @Component
5. struct WebWithBlur {
6. @State currentIndex: number = 0; // The index of the currently selected tab page
7. private controller: TabsController = new TabsController();
8. private webController: webview.WebviewController = new webview.WebviewController();
9. // ...
10. @Builder
11. tabBuilder(title: string, targetIndex: number, selectedImg: Resource, normalImg: Resource) {
12. // ...
13. }

15. build() {
16. // ...
17. Tabs({ barPosition: BarPosition.End, index: 0, controller: this.controller }) {
18. TabContent() {
19. Web({ src: $rawfile('test.html'), controller: this.webController })
20. }
21. .tabBar(this.tabBuilder('Tab', 0, $r('app.media.tab_icon_activated'), $r('app.media.tab_icon')))
22. // ...
23. }
24. .height('100%')
25. .width('100%')
26. .barOverlap(true) // Set TabBar to be blurred and overlay on top of TabContent
27. .barBackgroundColor('rgba(241, 243, 245, 0.3)')
28. // ...
29. }
30. }
```

[WebWithBlur.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/WebWithBlur.ets#L17-L102)

**Web组件上方TabBar控件去除模糊效果**

```
1. import { webview } from '@kit.ArkWeb';
2. // ...
3. @Entry
4. @Component
5. struct NormalWeb {
6. @State currentIndex: number = 0; // The index of the currently selected tab page
7. private controller: TabsController = new TabsController();
8. private webController: webview.WebviewController = new webview.WebviewController();
9. // ...
10. @Builder
11. tabBuilder(title: string, targetIndex: number, selectedImg: Resource, normalImg: Resource) {
12. // ...
13. }

15. build() {
16. // ...
17. Tabs({ barPosition: BarPosition.End, index: 0, controller: this.controller }) {
18. TabContent() {
19. Web({ src: $rawfile('test.html'), controller: this.webController })
20. }
21. .tabBar(this.tabBuilder('Tab', 0, $r('app.media.tab_icon_activated'), $r('app.media.tab_icon')))
22. // ...
23. }
24. .height('100%')
25. .width('100%')
26. .barOverlap(true) // Set TabBar to overlay on top of TabContent
27. .barBackgroundBlurStyle(BlurStyle.NONE) // Set TabBar to be not blurry
28. .barBackgroundColor('rgba(241, 243, 245, 1)')
29. // ...
30. }
31. }
```

[NormalWeb.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/NormalWeb.ets#L17-L102)

去除模糊后的效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/mf1Nul7vTMCd5x1vsQZXgQ/zh-cn_image_0000002229451905.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=59E09981D969ACAF9AC2BBA042E78EFBCEFE2DE1A3B8C3F3525C6329ECB96A6A "点击放大")

**功耗对比**

同一界面下，测试Web组件上方控件去除模糊效果前后的CPU模块、GPU模块的功耗，以及设备总功耗。测试方式为同样频率滑动界面30s，以3s为一个节点，取设备从6s运行到21s5个节点的平均功耗。最终，使用DevEco Studio的Profiler工具检测得到的数据如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Zvq-KCl6ThWXpnb_UCAK8A/zh-cn_image_0000002229451901.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=F6EF578C0AC2757D83D8D8A8C6A7019206ACC9350CC01A62A4A00DFF67298492 "点击放大")

从测试数据可以看出：

1. Web组件上方控件去除模糊效果的效用主要体现在GPU模块，降幅约为70.4%。
2. Web组件上方控件去除模糊效果后，总功耗和CPU模块功耗均有下降，总功耗下降约25.5%，CPU模块下降约30.7%。

测试数据表明，在Web场景下，去除Web上方控件的模糊效果并启用HWC可以显著降低GPU模块的功耗，同时也能有效减少CPU模块和设备总体的功耗。

### 场景三：避免UI控件上方自渲染图层设置透明度

**效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/yClMfxwOS6WXbLwKtpfaNQ/zh-cn_image_0000002193852020.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=29E1533E7FEAC4D26EE9AE49FE4D6DCF4D2A5483BFDB462CF970276EAE8CD0FD "点击放大")

视频图层设置透明度后，可以透视底部UI控件，但需要GPU进行额外处理，无法使用HWC叠加。建议评估透明度设置的必要性，考虑调整视频图层为不透明。若必须设置透明度，可将UI控件置于视频图层上方或使用自绘制方式实现UI控件，以支持HWC。

通过调整视频图层的不透明度来使能HWC，从而优化功耗。相应对比代码如下：

**视频图层设置透明度**

```
1. @Entry
2. @Component
3. struct TransparentVideo {
4. // ...
5. build() {
6. // ...
7. RelativeContainer() {
8. // Bottom UI component
9. Image($r('app.media.watermark'))
10. .width(200)
11. .height(80)
12. .alignRules({
13. center: { anchor: '__container__', align: VerticalAlign.Center },
14. middle: { anchor: '__container__', align: HorizontalAlign.Center }
15. })
16. // Video Layer
17. Video({
18. src: $r('app.media.test_video')
19. })
20. .height('100%')
21. .width('100%')
22. .loop(true)
23. .autoPlay(true)
24. .controls(false)
25. .alignRules({
26. top: { anchor: '__container__', align: VerticalAlign.Top },
27. middle: { anchor: '__container__', align: HorizontalAlign.Center }
28. })
29. .opacity(0.7) // Set the transparency of the video layer
30. }
31. .height('100%')
32. .width('100%')
33. }
34. // ...
35. }
```

[TransparentVideo.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/TransparentVideo.ets#L24-L81)

**视频图层不透明**

```
1. @Entry
2. @Component
3. struct OpaqueVideo {
4. // ...
5. build() {
6. // ...
7. RelativeContainer() {
8. // Bottom UI component
9. Image($r('app.media.watermark'))
10. .width(200)
11. .height(80)
12. .alignRules({
13. center: { anchor: '__container__', align: VerticalAlign.Center },
14. middle: { anchor: '__container__', align: HorizontalAlign.Center }
15. })
16. // Video Layer
17. Video({
18. src: $r('app.media.test_video')
19. })
20. .height('100%')
21. .width('100%')
22. .loop(true)
23. .autoPlay(true)
24. .controls(false)
25. .alignRules({
26. top: { anchor: '__container__', align: VerticalAlign.Top },
27. middle: { anchor: '__container__', align: HorizontalAlign.Center }
28. })
29. .opacity(1) // Set the video layer to be fully opaque
30. }
31. .height('100%')
32. .width('100%')
33. }
34. // ...
35. }
```

[OpaqueVideo.ets](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently/blob/master/entry/src/main/ets/pages/OpaqueVideo.ets#L24-L81)

设置视频不透明后的效果图如下所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/O5lDIUbdQDOJ3ztaqVsYmQ/zh-cn_image_0000002193852024.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=36AFE338534F0B1EF2BE320E1E06811AF070E2D00D4CE5C141B98708F07F6622 "点击放大")

**功耗对比**

同一界面下，测试视频图层设置不透明前后的CPU模块、GPU模块的功耗，以及设备总功耗。测试方式为视频播放30s，以3s为一个节点，取设备从6s运行到21s5个节点的平均功耗。最终，使用DevEco Studio的Profiler工具检测得到的数据如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/HpimpoOrRuaD8Lb9iDpQmg/zh-cn_image_0000002193852016.png?HW-CC-KV=V1&HW-CC-Date=20260429T061347Z&HW-CC-Expire=86400&HW-CC-Sign=825514F226C802A8761CFEAB6E5283C36FF5E984B7820A622FECAAC38E928B1C "点击放大")

从测试数据可以看出：

1. 视频图层设置为不透明后，CPU模块功耗下降约64.7%，GPU模块功耗降至0，降幅为100%。
2. 视频图层设置为不透明后，设备总功耗下降约10.7%。

测试数据表明，视频位于UI控件上方播放时，设置视频不透明并启用HWC可以显著降低GPU和CPU的功耗，从而有效降低设备总体功耗。

## 总结

本文基于HarmonyOS系统，介绍了如何充分利用HWC减少应用发热和卡顿的方案。通过Web界面和视频播放等常见场景的示例，展示了具体实施方法和效果。开发者可以参考这些建议，综合考虑视效、功耗和性能，提升应用的综合体验。

## 示例代码

* [高效利用HWC的低功耗设计](https://gitcode.com/harmonyos_samples/UtilizeHWCEfficiently)
