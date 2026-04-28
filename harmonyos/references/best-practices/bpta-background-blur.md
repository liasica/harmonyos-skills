---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-background-blur
title: 图像模糊高效使用
breadcrumb: 最佳实践 > 图形 > 图像处理 > 图像模糊高效使用
category: best-practices
scraped_at: 2026-04-28T08:20:52+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:13c07b76592983c34d07150a6bd0217733389965c3ae100ae22ad0e0724d56b9
---

## **概述**

在图像处理中，模糊效果（Blur Effect）是一种通过算法降低图像局部或整体的清晰度、减少细节或噪声的技术。模糊常用于突出主体、模拟景深、隐藏敏感信息或为后续处理（如边缘检测）做准备。

本文介绍的背景模糊属于动态模糊，根据效果区分为材质模糊和普通模糊。背景模糊在实际应用中应用场景广泛，例如：在包含多个卡片的页面中，应用背景模糊效果可突出层次感；在页面转场时，添加背景模糊能使过渡更加平滑。为进一步提升效果，系统通过使用缓存技术优化动态模糊的性能。本文旨在探讨背景模糊技术的高效应用方法，结合应用场景进行说明。

|  |  |  |  |
| --- | --- | --- | --- |
| 层次类型 | 效果分类 | 接口 | 使用说明 |
| 背景模糊 | 材质模糊 | [.backgroundBlurStyle()](../harmonyos-references/ts-universal-attributes-background.md#backgroundblurstyle9) | 通过枚举值的方式封装了不同的模糊半径、亮度、饱和度、蒙版颜色。  适用场景：通过设置枚举值来使用系统已经封装好的效果。 |
| [.backgroundEffect()](../harmonyos-references/ts-universal-attributes-background.md#backgroundeffect11) | 可以自定义模糊半径、亮度、饱和度、蒙版颜色、取色方式以及灰阶参数。  适用场景：用户需要自定义效果的场景。 |
| 普通模糊 | [.backdropBlur()](../harmonyos-references/ts-universal-attributes-background.md#backdropblur) | 仅能设置模糊半径和灰阶参数。  适用场景：仅需设置模糊半径的场景，如：页面转场。 |

## **实现原理**

### **系统渲染工作流程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/tAcUlrLjSkGzJO6u-jb4vw/zh-cn_image_0000002483620621.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=04DA7340E7C911B7E220311979DF1C5BC80ABBCF2CF70B198161B2CF0E5B0A9E)

**RenderService (RS) ：**系统渲染服务进程，接收来自于其他系统服务进程（如桌面进程）及用户进程（如应用）的自渲染图层及ArkUI控件绘制指令，进行统一的组合以及渲染控制。其渲染动作会调用CPU/GPU等通用计算器件进行。

### **RS模糊缓存工作流程**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/tkP0U0ecQ8CpJ-QWE6ytgw/zh-cn_image_0000002483501177.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=9FF17FE87956E53F2CFBF28EF993C70EE6ACF2E9DB3309E74071EC9C77576B07)

**RenderThread (RT) ：**渲染线程，RS进程划分为主线程和RT线程，RT线程负责接收各种渲染参数，渲染各种图像效果并上屏。

基本逻辑：根据需要创建或者刷新Drawable，同步模糊参数；做模糊先截图（生成截图的缓存），再做模糊（生成模糊的缓存），最多存在一份缓存（截图或者模糊结果）。

（1）主线程：创建/刷新Drawable；判断模糊是否重绘：模糊区域改变、模糊参数改变、是否与脏区相交；同步模糊参数。

（2）RT线程：如缓存有效则复用缓存，否则RT线程重做模糊，并重新缓存。

## **合理使用背景模糊的取色方式**

### **场景描述**

如果需要设置背景模糊的蒙版颜色，有两种取色方式可以选择，这里推荐使用ColorPicker取色方式，性能更优。

**效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/2g9t56IMSzytmUXJak5TvQ/zh-cn_image_0000002282716904.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=D2D26A1B52D0EE70F85974D6B64B90ACEEAE3A608B6D38B920F38E39CD2ED857 "点击放大")

### **实现原理**

如果要设置背景模糊的蒙版颜色，有如下两种取色方式：

（1）方式1：直接设置AdaptiveColor.AVERAGE取色。此方式需要RS在CPU计算阶段，先用GPU绘制一遍取色区域，然后再计算区域平均颜色值。优点：开发方式简单，适合轻负载应用使用。缺点：性能较低。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/UnpfKNMsQIiaxjGGJhvDfA/zh-cn_image_0000002450542000.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=82F04E4169D3EE457F1A020C78FA2E4E8C1A733C72FCC8017BB0666198404729)

（2）方式2：创建ColorPicker取色。此方式先使用EffectKit接口创建ColorPicker进行取色，再赋值给模糊参数中的color属性。优点：由于绘制取色区域的过程在应用层进行，所以性能有所提升，适合静态模糊场景。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Glrh-xu8RWGmrfGqDlDpCg/zh-cn_image_0000002450542024.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=210ABF8526C71451A3DEA18F70F080700A49E020A97547DC60DE4CA53CC43874)

### **开发步骤**

**方式1：设置背景模糊的接口参数adaptiveColor为AdaptiveColor.AVERAGE**

对背景图片应用backgroundEffect接口设置模糊效果，设置adaptiveColor属性值为AdaptiveColor.AVERAGE。

**示例代码**

```
1. @Component
2. export struct AdaptiveColorMode {
3. @Consume('navPathStack') navPathStack: NavPathStack;

5. build() {
6. NavDestination() {
7. Column() {
8. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
9. Text('Background Material Blur').fontColor('#FFFFFF')
10. }
11. .height('50%')
12. .width('70%')
13. // just set the parameter adaptiveColor
14. .backgroundEffect({
15. radius: 20,
16. saturation: 1.0,
17. brightness: 1.0,
18. adaptiveColor: AdaptiveColor.AVERAGE
19. })
20. .position({ x: '15%', y: '30%' })
21. }
22. .height('100%')
23. .width('100%')
24. .backgroundImage($r('app.media.test'))
25. .backgroundImageSize(ImageSize.Cover)
26. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
27. }
28. .hideTitleBar(true)
29. }
30. }
```

[AdaptiveColorMode.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BackgroundBlur/entry/src/main/ets/pages/AdaptiveColorMode.ets#L17-L46)

**方式2：先使用ColorPicker进行取色，再给模糊接口的color参数赋值**

传入图片资源，创建pixMap，根据pixMap创建ColorPicker，调用ColorPicker的getAverageColor()方法获取颜色，转换成backgroundEffect接口参数color的格式，调用接口时替换成获取到的blurColor。

**示例代码**

```
1. import { image } from '@kit.ImageKit';
2. import { effectKit } from '@kit.ArkGraphics2D';

4. @Component
5. export struct ColorPickerMode {
6. @Consume('navPathStack') navPathStack: NavPathStack;
7. @State pixMap: image.PixelMap | null = null
8. @State kitColor: effectKit.Color = {
9. red: 255,
10. green: 255,
11. blue: 255,
12. alpha: 255
13. };
14. @State blurColor: string = 'rgba(255,255,255,255)';

16. async blurPix(resource: Resource) {
17. try {
18. const context: Context = this.getUIContext().getHostContext()!;
19. const fileData: Uint8Array = await context.resourceManager.getMediaContent(resource.id);
20. const buffer: ArrayBufferLike = fileData.buffer
21. let imageSource: image.ImageSource = image.createImageSource(buffer as ArrayBuffer)
22. this.pixMap = await imageSource.createPixelMap();
23. // create a color picker for color extraction
24. this.kitColor = (await effectKit.createColorPicker(this.pixMap, [0, 0, 1, 1])).getAverageColor();
25. // convert to the format of the blur interface color parameter
26. this.blurColor = 'rgba(' + this.kitColor.red + ',' + this.kitColor.green + ',' + this.kitColor.blue + ',0)';
27. } catch (err) {
28. }
29. }

31. build() {
32. NavDestination() {
33. Column() {
34. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
35. Text('Background Material Blur').fontColor('#FFFFFF')
36. }
37. .height('50%')
38. .width('70%')
39. // assign a value to the color parameter of a blur interface
40. .backgroundEffect({
41. radius: 20,
42. saturation: 1.0,
43. brightness: 1.0,
44. color: this.blurColor
45. })
46. .position({ x: '15%', y: '30%' })
47. }
48. .height('100%')
49. .width('100%')
50. .backgroundImage($r('app.media.test'))
51. .backgroundImageSize(ImageSize.Cover)
52. .onAppear(() => {
53. // import image resources
54. this.blurPix($r('app.media.test'));
55. })
56. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
57. }
58. .hideTitleBar(true)
59. }
60. }
```

[ColorPickerMode.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BackgroundBlur/entry/src/main/ets/pages/ColorPickerMode.ets#L17-L77)

**性能对比**

测试使用两种取色方式绘制背景模糊效果的单帧渲染耗时，最终使用DevEco Studio内置的Profiler中的帧率分析工具Frame抓取绘制背景模糊时的性能差异。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Rsamz8PrRey-wxun1aXcOA/zh-cn_image_0000002317356505.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=2FE66969DE4B604F401A5449E43B2DF2C5A8AB391157352D040752B27B4AA773 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/lXqXi6t2TsGMcdgSRHYfvQ/zh-cn_image_0000002282716908.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=F27E628AF46D7F3AA907BFBC37405028E3D4526E3546530B0EDB97D5ED122571 "点击放大")

如上图所示，通过RenderFrame（执行GPU绘制）标签可以看出，使用ColorPicker取色的单帧平均耗时为5.650ms；而直接设置背景模糊的接口参数为AdaptiveColor.Average的单帧平均耗时为9.400ms。

## **在背景模糊场景正确使用混合模式**

### **场景描述**

如果需要在背景模糊场景使用混合模式，需要结合实际场景选择合适的混合模式，才能得到预期的效果。以下是同一场景下使用两种不同的方式实现的效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/GgHFC-AbSBGguDQVDK6YyQ/zh-cn_image_0000002450382684.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=49D9542ECAE700BF7F80B38032506946F7D0D364DCBDD5911833F5DBC2BF6B43)

### **实现原理**

**BlendMode****（混合模式）：**这是一种图形处理技术，用于控制两个或多个图层（或图形元素）在叠加时如何混合颜色。它决定了上层像素与下层像素的交互方式，从而产生不同的视觉效果。

BlendMode的类型有两种：一种是FAST类型，另一种是OFFSCREEN类型。FAST类型使各个图层的效果按顺序进行混合，而OFFSCREEN类型使用离屏画布，组件内容先绘制到离屏画布上，然后再整体进行混合。

因此当场景中同时存在BlendMode和背景模糊时，需要注意BlendMode的类型。BlendMode设置为OFFSCREEN类型时使用离屏画布进行绘制，而模糊处理过程需要对背景进行截图，如果离屏画布未完成绘制，模糊流程已经进行了对背景的截图并绘制，那么绘制结果可能是非预期的。

两种类型的差异见下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Bwa_eaJBSOWFQ2KZ8ShUjg/zh-cn_image_0000002483502589.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=56D5890D42255BD32CC72F2170555769A0D681AF2D34A1995F18D4F941F31EFB)

### **开发步骤**

如果想得到最底层是背景图片，其上是地图，在地图上叠加模糊的效果，应使用FAST方式。

**预期效果图**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Rg9oBZ4QRPKXaD-DldbPCQ/zh-cn_image_0000002317356509.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=5C333748B62A3BD108A8A201467BCCCBBFCB547850EE53788DFDD1831A9122BB "点击放大")

设置blendMode为FAST类型使各个图层的效果按顺序进行混合，所以可以实现预期的效果。

**示例代码**

```
1. @Component
2. export struct FastMode {
3. @Consume('navPathStack') navPathStack: NavPathStack;

5. build() {
6. NavDestination() {
7. Stack() {
8. Stack() {
9. Image($r('app.media.map')).width('100%').height('100%').borderRadius(15)
10. Flex({ direction: FlexDirection.ColumnReverse }) {
11. }
12. .height(80)
13. .backgroundBlurStyle(BlurStyle.COMPONENT_ULTRA_THIN, { scale: 0.3 })
14. .flexShrink(0)
15. .width('100%')
16. .padding(0)
17. .borderRadius({
18. topLeft: 0,
19. topRight: 0,
20. bottomLeft: 15,
21. bottomRight: 15
22. })
23. .position({ x: 0, y: 220 })
24. }.margin({ left: '16', right: '16' })
25. .height(300)
26. .borderRadius(15)
27. // blend mode is set to fast mode
28. .blendMode(BlendMode.SRC_OVER, BlendApplyType.FAST)
29. }
30. .width('100%')
31. .height('100%')
32. .backgroundImage($r('app.media.img'))
33. .backgroundImageSize(ImageSize.Cover)
34. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
35. }
36. .hideTitleBar(true)
37. }
38. }
```

[FastMode.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BackgroundBlur/entry/src/main/ets/pages/FastMode.ets#L17-L54)

**非预期效果图**

如果使用OFFSCREEN方式，将得到非预期的效果：背景模糊对背景图片进行模糊，而后与地图的图层进行效果混合。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/R6I34jRLSIiuax1_JDcNqA/zh-cn_image_0000002282716916.png?HW-CC-KV=V1&HW-CC-Date=20260428T002051Z&HW-CC-Expire=86400&HW-CC-Sign=06C074F08D1BDB637E7E1D9EF3AB13321D9B25DAB3D8C1FD01B4593E33093D71 "点击放大")

设置blendMode为OFFSCREEN类型会创建离屏画布，而模糊处理过程需要对背景进行截图，当离屏画布未完成绘制回到屏幕上时，模糊流程已经进行了背景的截图并绘制，所以混合后的效果非预期。

**示例代码**

```
1. @Component
2. export struct OffscreenMode {
3. @Consume('navPathStack') navPathStack: NavPathStack;

5. build() {
6. NavDestination() {
7. Stack() {
8. Stack() {
9. Image($r('app.media.map')).width('100%').height('100%').borderRadius(15)
10. Flex({ direction: FlexDirection.ColumnReverse }) {
11. }
12. .height(80)
13. .backgroundBlurStyle(BlurStyle.COMPONENT_ULTRA_THIN, { scale: 0.3 })
14. .flexShrink(0)
15. .width('100%')
16. .padding(0)
17. .borderRadius({
18. topLeft: 0,
19. topRight: 0,
20. bottomLeft: 15,
21. bottomRight: 15
22. })
23. .position({ x: 0, y: 220 })
24. }.margin({ left: '16', right: '16' })
25. .height(300)
26. .borderRadius(15)
27. // blend mode is set to offscreen mode
28. .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
29. }
30. .width('100%')
31. .height('100%')
32. .backgroundImage($r('app.media.img'))
33. .backgroundImageSize(ImageSize.Cover)
34. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM])
35. }
36. .hideTitleBar(true)
37. }
38. }
```

[OffscreenMode.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/BackgroundBlur/entry/src/main/ets/pages/OffscreenMode.ets#L17-L54)

## **总结**

本文针对系统的背景模糊特性，深度解析其技术原理与实现机制，并基于不同应用场景提出高效实施方案。在涉及取色功能的开发场景中，建议开发者通过性能开销和视觉效果的量化评估，选择最优实现方案；对于需要使用混合模式进行上下层图层混合的场景，开发者应当结合混合模式和背景模糊的工作原理，选择合适的混合类型。

## **示例代码**

* [高效使用背景模糊开发实践](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/BackgroundBlur)
