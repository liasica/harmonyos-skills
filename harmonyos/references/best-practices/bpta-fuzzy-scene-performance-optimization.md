---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-fuzzy-scene-performance-optimization
title: 图像模糊动效优化
breadcrumb: 最佳实践 > 图形 > 图像处理 > 图像模糊动效优化
category: best-practices
scraped_at: 2026-04-28T08:20:52+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:ca852ad119076c9fce00e48d3795429927703b29c97dc93a22768320f5c2e760
---

## 概述

模糊效果是一种常见的图像处理技术，它通过弱化图像细节来突出主体，使焦点更加鲜明。如下图所示，模糊效果不仅能增强界面空间感，还能清晰区分元素层级。当这一效果融入动态变化，便催生了模糊动效。模糊动效被广泛应用于页面转场、图像元素缩放等需要突出内容或改变用户关注点的场景中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/IdB7LlOXTKqKAGgM0DI0dw/zh-cn_image_0000002337772197.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=E674FE68D6784D182C2204DAE8DA067B45BA3D8E7C45A7291AE8FF0BFB7A58AF)

由于模糊算法需要进行精细的像素级处理，因而在组件需要实时渲染时，这要求在极短的周期内完成模糊化处理。尤其是在组件同时执行动画渲染任务时，则会进一步加剧计算资源的消耗，容易导致模糊效果处理时间不足，无法按时完成模糊动效，最终引发卡顿、丢帧等不良现象。

因此，随着应用的广泛普及，模糊动效的性能优化愈发显得至关重要。鉴于系统为开发者提供的静态模糊和动态模糊两种动效能力，本文将在“转场结合图片模糊”的应用场景下，对静态模糊与动态模糊的性能进行差异性对比。同时，建议开发者在组件背景和内容无需实时更新的场景中，优先使用静态模糊，可以减少应用卡顿与丢帧，提升用户体验。

## 使用场景

在介绍静态模糊和动态模糊之前，需要说明静态模糊和动态模糊的区别在于要模糊的内容是不是动态更新的，如对视频做模糊就是动态模糊，对图片做模糊就是静态模糊。

* **静态模糊**：静态模糊是指对输入的静态内容进行模糊处理并获取一张模糊后的图像的模糊。适用于需要为静态图像提供模糊化效果的场景。[Effect Kit](../harmonyos-references/js-apis-effectkit.md)在Filter图像效果类中提供了[blur](../harmonyos-references/js-apis-effectkit.md#blur)接口，可用于定义模糊半径，数值越大模糊效果越明显。

* **动态模糊**：动态模糊是指模糊效果会随着每帧模糊内容和模糊半径的变化，进行实时变化的模糊。适用于模糊内容需要实时刷新和更改的场景。系统针对组件内容、背景的动态模糊提供了两种实现动态模糊的方法：[backgroundBlurStyle](../harmonyos-references/ts-universal-attributes-background.md#backgroundblurstyle9)和[foregroundBlurStyle](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle)。这两个方法不能指定模糊半径、提亮、饱和度、蒙版颜色等具体参数，只能调用底层将这些参数封装好的[模糊样式](../harmonyos-references/ts-universal-attributes-background.md#blurstyle9)来实现不同风格的模糊效果。同时系统也为开发者提供了能够自定义参数的[backgroundEffect](../harmonyos-references/ts-universal-attributes-background.md#backgroundeffect11)，可以对组件背景实现自定义模糊动效。如果只需要对组件进行简单的模糊处理，系统还提供了与静态模糊类似的简单方法[blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur)和[backdropBlur](../harmonyos-references/ts-universal-attributes-background.md#backdropblur)，只需要定义模糊半径即可。

## 场景示例

下面将在常见的“转场结合图片模糊”的应用场景下（全屏模态转场拉起一个图片设置模糊的模态页面），分别采用动态模糊和静态模糊，进行性能分析对比。需要说明，由于静态模糊和动态模糊底层采用的算法不同，动态模糊blur和静态模糊blur设置的模糊半径数值并不等效。为了从效果一致性的维度来更准确的比较两者的性能差异，这里将动态模糊和静态模糊场景的模糊半径的数值尽可能的调整到类似的模糊效果来进行对比。动态模糊blur设置13，静态模糊blur设置3的图片模糊效果较为接近，作为本例中效果一致性较为近似的等效条件。

下面是使用动态模糊对图片进行模糊处理的场景示例。通过直接对Image组件设置blur，为Image添加模糊效果。

```
1. import { window } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Component
6. export struct MotionBlur {
7. @Consume('navPathStack') navPathStack: NavPathStack;
8. @State isShowMotionBlur: boolean = false;
9. @State bottomSafeHeight: number = 0; // bottom navigation bar height

11. aboutToAppear(): void {
12. window.getLastWindow(this.getUIContext().getHostContext()!, (err, windowBar) => {
13. if (err.code) {
14. return;
15. }

17. try {
18. // get the height of the bottom navigation bar
19. this.bottomSafeHeight =
20. this.getUIContext()
21. .px2vp(windowBar.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height);
22. } catch (error) {
23. let err: BusinessError = error as BusinessError;
24. hilog.warn(0x000, 'testTag', `getWindowAvoidArea failed, code=${err.code}, message=${err.message}`);
25. }
26. windowBar.setWindowLayoutFullScreen(true)
27. .catch((err: BusinessError) => {
28. hilog.error(0x000, 'testTag', `setWindowLayoutFullScreen failed, code=${err.code}, message=${err.message}`);
29. })

31. });
32. }

34. // modal page with dynamically blurred image settings
35. @Builder
36. motionBlurBuilder() {
37. Stack({ alignContent: Alignment.Bottom }) {
38. Image($r('app.media.test'))
39. .width('100%')
40. .height('100%')
41. .objectFit(ImageFit.Fill)
42. .blur(13) // add motion blur effect
43. Button('close')
44. .width('90%')
45. .height(40)
46. .margin({ bottom: this.bottomSafeHeight + 16 })
47. .onClick(() => {
48. this.isShowMotionBlur = false;
49. })
50. }
51. .width('100%')
52. .height('100%')
53. }

55. build() {
56. NavDestination() {
57. Column() {
58. Button('motion blur')
59. .width('90%')
60. .height(40)
61. .onClick(() => {
62. this.isShowMotionBlur = true;
63. })
64. .bindContentCover(this.isShowMotionBlur, this.motionBlurBuilder(), {
65. modalTransition: ModalTransition.DEFAULT
66. })
67. }
68. .padding({ bottom: this.bottomSafeHeight + 16 })
69. .width('100%')
70. .height('100%')
71. .justifyContent(FlexAlign.End)
72. }
73. .hideTitleBar(true)
74. }
75. }
```

[MotionBlur.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FuzzySceneOptimization/entry/src/main/ets/pages/MotionBlur.ets#L17-L92)

**图1** 动态模糊  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/psurXvlFTu-kSD_c1xRSMA/zh-cn_image_0000002193850416.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=BC503E55124272E9570B98795F681E45D585D709212B3A07B2F651667BB41EEF "点击放大")

下面是使用静态模糊对图片进行模糊处理的场景示例。主要步骤如下：

1. 通过createPixelMap创建图片的PixelMap。
2. 通过createEffect创建Filter实例。
3. 通过Filter图像效果类中的blur，为Image添加模糊效果。

   ```
   1. import { image } from '@kit.ImageKit';
   2. import { effectKit } from '@kit.ArkGraphics2D';
   3. import { window } from '@kit.ArkUI';
   4. import { hilog } from '@kit.PerformanceAnalysisKit';
   5. import { BusinessError } from '@kit.BasicServicesKit';

   7. @Component
   8. export struct StaticBlur {
   9. @Consume('navPathStack') navPathStack: NavPathStack;
   10. @State isShowStaticBlur: boolean = false;
   11. @State pixelMap: image.PixelMap | undefined = undefined;
   12. @State imgSource: image.ImageSource | undefined = undefined;
   13. @State bottomSafeHeight: number = 0; // bottom navigation bar height

   15. aboutToAppear(): void {
   16. window.getLastWindow(this.getUIContext().getHostContext()!, (err, windowBar) => {
   17. if (err.code) {
   18. return;
   19. }
   20. try {
   21. // get the height of the bottom navigation bar
   22. this.bottomSafeHeight =
   23. this.getUIContext()
   24. .px2vp(windowBar.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR).bottomRect.height);
   25. } catch (error) {
   26. let err: BusinessError = error as BusinessError;
   27. hilog.warn(0x000, 'testTag', `getWindowAvoidArea failed, code=${err.code}, message=${err.message}`);
   28. }
   29. windowBar.setWindowLayoutFullScreen(true)
   30. .catch((err: BusinessError) => {
   31. hilog.error(0x000, 'testTag', `setWindowLayoutFullScreen failed, code=${err.code}, message=${err.message}`);
   32. })
   33. });
   34. }

   36. async staticBlur(): Promise<void> {
   37. let context: Context = this.getUIContext().getHostContext()!;
   38. await context.resourceManager.getRawFileContent('test.png') // retrieve images from the rawfile directory
   39. .then((fileData: Uint8Array) => {
   40. let buffer: ArrayBuffer = fileData.buffer.slice(0); // create an ArrayBuffer instance
   41. this.imgSource = image.createImageSource(buffer); // create an image source instance
   42. })
   43. .catch((err: BusinessError) => {
   44. hilog.error(0x000, 'testTag', `getRawFileContent failed, code=${err.code}, message=${err.message}`);
   45. })
   46. // create attributes for pixels
   47. let opts: image.InitializationOptions = {
   48. editable: true, // is it editable
   49. pixelFormat: 3, // pixel format. 3 represents RGBA_8888
   50. size: {
   51. // create image size
   52. height: 4,
   53. width: 6
   54. }
   55. };
   56. // create PixelMap
   57. await this.imgSource!.createPixelMap(opts).then((pixelMap: image.PixelMap) => {
   58. const blurRadius: number = 3;
   59. let headFilter: effectKit.Filter = effectKit.createEffect(pixelMap); // create Filter Instance
   60. if (headFilter !== null) {
   61. headFilter.blur(blurRadius); // set static blur. Add the blur effect to the effect list
   62. // retrieve the image of the source image with the added linked list effect PixelMap
   63. headFilter.getEffectPixelMap().then((pixelMap: image.PixelMap) => {
   64. this.pixelMap = pixelMap;
   65. });
   66. }
   67. })
   68. }

   70. @Builder
   71. staticBlurBuilder() {
   72. Stack({ alignContent: Alignment.Bottom }) {
   73. Image(this.pixelMap)
   74. .width('100%')
   75. .height('100%')
   76. .objectFit(ImageFit.Fill)
   77. Button('close')
   78. .width('90%')
   79. .height(40)
   80. .margin({ bottom: this.bottomSafeHeight + 16 })
   81. .onClick(() => {
   82. this.isShowStaticBlur = false;
   83. })
   84. }
   85. .width('100%')
   86. .height('100%')
   87. }

   89. build() {
   90. NavDestination() {
   91. Column() {
   92. Button('static blur')
   93. .width('90%')
   94. .height(40)
   95. .onClick(() => {
   96. this.isShowStaticBlur = true;
   97. // set static blur
   98. this.staticBlur();
   99. })
   100. .bindContentCover(this.isShowStaticBlur, this.staticBlurBuilder(), {
   101. modalTransition: ModalTransition.DEFAULT
   102. })
   103. }
   104. .padding({ bottom: this.bottomSafeHeight + 16 })
   105. .width('100%')
   106. .height('100%')
   107. .justifyContent(FlexAlign.End)
   108. }
   109. .hideTitleBar(true)
   110. }
   111. }
   ```

   [StaticBlur.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/FuzzySceneOptimization/entry/src/main/ets/pages/StaticBlur.ets#L17-L127)

**图2** 静态模糊

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/0x26v_O2T8WW72GzocZt7Q/zh-cn_image_0000002229450281.gif?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=34E2D0A3F33C17770B6944204A02FFFA9B55DD6C5E3DB459F37F03A632858831 "点击放大")

## 效果对比

下面使用DevEco Studio内置的Profiler中的帧率分析工具Frame抓取点击按钮触发转场过程的trace来分析静态模糊和动态模糊场景下的性能差异。需要说明，由于场景示例通过点击按钮触发转场，所以可以通过User Events（用户输入事件）的Click标签定位到转场过程的起点为Click标签结束位置。转场过程的终点为连续的RenderFrame（执行GPU绘制）标签不再连续的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/e5pqj4A0StacLsazyLfObg/zh-cn_image_0000002229450285.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=9E9B6CFFCB36633041A3E67132F792C09AC78C11B16E58471ECC928CEFEF8120 "点击放大")

如上图所示，通过RenderFrame（执行GPU绘制）标签可以看出，动态模糊转场平均渲染耗时为6.113ms。同时从Present Fence（图形上屏信号）标签可以看出动态模糊转场平均帧率为108.0fps。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/nU-FrpdGRTWsRBAV-IpPDA/zh-cn_image_0000002229335801.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=E226A8D2D2CBC10BC397AB3990EEA721D965A2925ED34589199878786B096CA7 "点击放大")

如上图所示，通过RenderFrame标签可以看出，静态模糊转场平均渲染耗时为3.357ms。同时从Present Fence标签可以看出静态模糊转场平均帧率为119.9fps。和动态模糊转场相比平均渲染耗时减少了约45%（性能耗时数据因应用场景、设备型号版本而异，以实测为准）。

由此可见，在模糊效果类似的条件下，静态模糊的性能要优于动态模糊。这源于底层实现机制的差异：静态模糊只需完成一次性的模糊处理，有效减轻了实时渲染的负担；而动态模糊则需要对每一帧进行连续的模糊计算，尽管在理想情况下能够营造出更为平滑和连贯的视觉过渡效果，但同时也显著增加了渲染的复杂度和资源消耗，若页面过于复杂，反而可能导致卡顿或丢帧现象的发生。

## 示例代码

* [图像模糊动效优化](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/FuzzySceneOptimization)
