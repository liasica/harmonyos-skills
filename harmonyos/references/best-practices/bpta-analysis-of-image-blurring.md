---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-analysis-of-image-blurring
title: 图像模糊卡顿问题分析
breadcrumb: 最佳实践 > 图形 > 图像处理 > 图像模糊卡顿问题分析
category: best-practices
scraped_at: 2026-04-28T08:20:53+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:87475c86c809592c6b9873ff18928572a7927b3a97912eae109354e6146d2c13
---

## 概述

在应用开发中，动态模糊效果虽然能够增强视觉体验，但不当使用（如对图片组件使用动态模糊、模糊半径过大等）可能导致性能问题，如图像卡顿、丢帧或渲染耗时增加等。这些问题不仅影响用户体验，还可能增加应用的功耗。通过合理优化代码逻辑，可有效降低渲染开销，提升用户体验。本文通过AppAnalyzer工具检测应用中存在的图像模糊卡顿问题，结合工具提示的故障原因，给出相应的优化解决方案，帮助开发者解决图像模糊性能问题。

## 图像模糊卡顿问题检测和分析

开发者可以通过AppAnalyzer工具对应用的图像模糊性能进行检测，并根据检测报告中的建议进行优化，确保图像模糊性能达标。使用AppAnalyzer工具检测图像模糊性能的步骤如下：

1. 在DevEco Studio中启动AppAnalyzer工具，详细请参见[AppAnalyzer](bpta-performance-detection.md#section135451444171)。
2. 默认选择场景化体检，点击任一手动性能体检项（页面间转场、页面内转场、页面滑动）即可进入对应体检界面。本文以“手动性能页面间转场体检”为例进行说明。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/hXKvrNuiSNK1Kk_q9D1v8Q/zh-cn_image_0000002539662815.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=A21E46C40BD4D8B9413BED3E6FC7E1EC49F002A50CB1C698AAD3559903A7B9BC "点击放大")
3. 完成体检后，打开体检报告并点击展开“转场卡顿率”部分。如果检测结果显示黄色或红色警告，且提示“可能故障原因”为“动态模糊绘制丢帧诊断”，则表明存在图像模糊性能问题。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/_LpEyaxOSYiBrf1KcYTviQ/zh-cn_image_0000002507943106.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=F1AE0246EF2D5B50CDD0529131CE901CD2A8EB12E2A3F48464CEBB7AFF9F95BF "点击放大")

在检测出的图像模糊报告中，若“可能故障原因”为“动态模糊绘制丢帧诊断”，可参考以下两点建议进行优化：

* 建议对图片组件使用静态模糊
* 建议缩小模糊半径

## 图像模糊卡顿问题优化方案

### 对图片组件使用静态模糊

在使用动态模糊对图片组件进行处理时，若检测结果异常，动态模糊绘制过程中出现丢帧情况。建议改用静态模糊，以优化图片模糊性能。动态模糊与静态模糊的概念及使用场景，请参阅相关文档：[使用场景](bpta-fuzzy-scene-performance-optimization.md#section4945532519)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/r1YoBEgkT72mS-0T_m7Gtg/zh-cn_image_0000002539782787.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=8383F09BA1B18407DFE903A9767401131DF03695EAD4794AB8AA16BFB8F27EE6 "点击放大")

例如，从检测报告中的可能故障原因中，点击组件所在源码文件，可跳转定位至TestStructPage.ets页面中的Column组件处。在示例代码中，使用了[blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur)动态模糊API对图片组件进行模糊处理，导致在检测中总耗时过长和丢帧。

**反例**

```
1. Column() {
2. Image($r('app.media.test'))
3. .width('100%')
4. .height('30%')
5. .objectFit(ImageFit.Auto)
6. .blur(13)
7. // ...
8. }
```

**优化建议**

针对图片模糊场景，建议使用静态模糊。通过静态模糊和动态模糊性能[效果对比](bpta-fuzzy-scene-performance-optimization.md#section12488810070)，可以发现在模糊效果类似的条件下，静态模糊的性能要优于动态模糊。建议开发者在组件背景和内容无需实时更新的场景中，优先使用静态模糊，可以减少应用卡顿与丢帧，提升用户体验。

**正例**

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

[StaticBlur.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/FuzzySceneOptimization/entry/src/main/ets/pages/StaticBlur.ets#L17-L127)

### 缩小模糊半径

在对非图片组件（如Text组件）或不适用静态模糊的场景（如Gif动图）使用模糊时，若检测结果显示动态模糊绘制时出现丢帧异常，可以考虑缩小模糊半径，以优化图片模糊性能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/6iMe3GX2SX-bWVIjeHCdxg/zh-cn_image_0000002508102952.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=34CEF203CD394EB7317CFF937F71AECF43E6288F8A124A4185BA95C8073C4E91 "点击放大")

例如，从检测报告中可能故障原因中，点击组件所在源码文件，可跳转定位至ReduceBlurRadius.ets页面中的Text组件处。在示例代码中，使用了[backdropBlur()](../harmonyos-references/ts-universal-attributes-background.md#backdropblur)对Text组件进行背景模糊，其模糊半径为2。

**反例**

```
1. Text('Backdrop Blur')
2. .padding(5)
3. .width('90%')
4. .height('50%')
5. .fontSize(20)
6. .fontColor(Color.White)
7. .textAlign(TextAlign.Center)
8. .backdropBlur(2) // Blurring radius is 2, detecting performance anomaly.
9. .backgroundImage($r('app.media.test'))
10. .backgroundImageSize({ width: '90%' })
11. .backgroundImagePosition(Alignment.Center)
```

**优化建议**

非图片模糊场景，建议缩小模糊半径。动态模糊每帧需重新计算，通过缩小半径，可降低性能消耗。

**正例**

```
1. Text('Backdrop Blur')
2. .padding(5)
3. .width('90%')
4. .height('50%')
5. .fontSize(2)
6. .fontColor(Color.White)
7. .textAlign(TextAlign.Center)
8. .backdropBlur(0.2) // The blur radius is reduced to 0.2,the specific value depends on actual requirements.
9. .backgroundImage($r('app.media.test')) // Here 'app.media.test' is just an example, developers should replace it with their own.
10. .backgroundImageSize({ width: '90%' })
11. .backgroundImagePosition(Alignment.Center)
```

[ReduceBlurRadius.ets](https://gitcode.com/HarmonyOS_Samples/BestPracticeSnippets/blob/master/BackgroundBlur/entry/src/main/ets/pages/ReduceBlurRadius.ets#L84-L94)

**表1** 常见的模糊API及其对应的优化建议

| 模糊API | 模糊类型 | 优化建议 |
| --- | --- | --- |
| [blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur) | 内容模糊 | 1、若是图片组件，建议使用静态模糊；  2、若是非图片组件或不适用静态模糊的场景，建议减小模糊半径； |
| [backdropBlur](../harmonyos-references/ts-universal-attributes-background.md#backdropblur) | 背景模糊 |
| [backgroundBlurStyle](../harmonyos-references/ts-universal-attributes-background.md#backgroundblurstyle9) | 背景模糊 |
| [foregroundBlurStyle](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle) | 内容模糊 |
| [backgroundEffect](../harmonyos-references/ts-universal-attributes-background.md#backgroundeffect11) | 背景模糊 |

## 示例代码

* [背景模糊示例](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/BackgroundBlur)
