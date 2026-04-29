---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-component-nesting-optimization
title: 组件嵌套优化
breadcrumb: 最佳实践 > 性能 > 性能场景优化案例 > 界面渲染性能优化 > 组件嵌套优化
category: best-practices
scraped_at: 2026-04-29T14:13:29+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:bb34eb08b8fac3b83eab5c35a4fbfce2140fdb82a918acab4ef074f051076216
---

本文通过原理概念、优化场景和实践数据对比三个角度，详细介绍了组件嵌套的优化，着重从优化场景角度为开发者阐明组件嵌套的优化场景以及优化策略。

## 原理概述

本章节将从原理角度分析，通过ArkUI框架的执行流程，以及自定义组件的生命周期两个角度，来分析组件过度嵌套对性能的影响。

### ArkUI框架执行流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/E4ZlOXJ0QVyDIbkWFrCIaQ/zh-cn_image_0000002427576872.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=447CAACABEA72B3DD5DE34D5E28EF15E8BB89FE14A0DAD3A586D2E8B3893BAAE "点击放大")

如上图所示，可以看到ArkUI框架的执行顺序：

1. 执行ArkTS中的UI描述信息，通过UI描述API创建后端的页面节点树，其中包含了处理UI组件属性更新、布局测算、事件处理等业务逻辑；
2. 通过FrameNode生成当前的界面描述数据结构——渲染树RenderTree，RenderTree描述了具体的元素在屏幕上的布局信息，包含大小、位置以及一些其他属性；
3. 最后渲染线程会根据RenderTree的信息执行相应的绘制工作。

### 自定义组件的生命周期

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/BVH4NDKCSBSmCDXIQl0hjg/zh-cn_image_0000002229451945.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=48ADC9956A692F0F6B1DFBFFB245FC48B0FC5D536BFA8B79A5BA1997E54E78C7 "点击放大")

如上图所示，自定义组件创建完成之后，在build函数执行之前，将先执行aboutToAppear()生命周期回调函数。执行完build函数后，还会有一些事件监听函数，例如可以使用onPageShow监听页面显示事件，onPageHide函数可以监听页面隐藏事件。最终在自定义组件析构销毁前执行aboutToDisappear函数。

具体的页面和自定义组件生命周期可以参考[自定义组件生命周期](../harmonyos-guides/arkts-page-custom-components-lifecycle.md)。

### 组件过度嵌套对性能的影响

组件嵌套是指一个组件包含另一个或多个组件的情况，这种嵌套关系可以形成组件树的结构。从最外层组件的类型来看，可以分为自定义组件嵌套和原生组件嵌套。

从ArkUI框架的执行流程上分析，布局时会采用递归遍历所有节点的方式进行组件位置和大小的计算。嵌套层级过深将带来更多的中间节点，在布局测算阶段下，额外的节点数将导致更多的计算过程，造成性能消耗。

从自定义组件的生命周期的角度上分析，如果自定义组件过度嵌套，则会有大量的生命周期函数需要执行，消耗性能。

详细的组件嵌套性能数据分析可参考[《精简节点数》](bpta-improve-layout-performance.md#section9293918175210)。

## 优化场景

### 优先使用@Builder方法代替自定义组件

自定义组件与自定义构建函数概念定义如下：

自定义组件：用@Component修饰的struct结构体称为自定义组件，在自定义组件中可以定义函数/变量、build()方法、组件的生命周期回调等。自定义组件具有可组合、可重用和数据驱动UI更新的特点。

自定义构建函数：@Builder装饰的函数称为“自定义构建函数”，分为组件内自定义构建函数和全局自定义构建函数。@Builder所装饰的函数遵循build()函数语法规则，开发者可以将重复使用的UI元素抽象成一个方法，在build方法里调用。

自定义组件和自定义构建函数（@Builder）的主要区别如下：

1. 自定义构建函数（@Builder）更轻量，其作为UI元素抽象的方法，实现和调用相较于自定义组件比较简洁。
2. 在自定义组件中，可以定义成员函数/变量、自定义组件生命周期等。自定义构建函数（@Builder）不支持定义状态变量和自定义生命周期。
3. 在自定义组件中，可直接通过状态变量的改变，来驱动UI的刷新。而自定义构建函数（@Builder）默认的按值参数传递方式不支持动态改变组件，当传递的参数为状态变量时，状态变量的改变不会引起@Builder方法内的UI刷新，要实现UI动态刷新需要按引用传递参数。
4. 在自定义组件中要实现插槽功能，需要使用@Builder和@BuilderParam实现。具体实现可参考：[@BuilderParam装饰器：引用@Builder函数](../harmonyos-guides/arkts-builderparam.md)。
5. 自定义构建函数（@Builder）中使用了自定义组件，那么该方法每次被调用时，对应的自定义组件均会重新创建。

整体上，自定义组件在实际应用开发场景中更加通用、灵活。自定义构建函数（@Builder）由于不支持定义变量和生命周期等限制，在使用场景上灵活性受限，多用在插槽或系统提供的组件/方法里面属性传值类型为Builder类型场景中。

根据上面自定义组件与自定义构建函数的区别可以看出，由于@Builder不涉及生命周期，在自定义组件大量嵌套的场景中，更加轻量级的@Builder在性能方面更加出色。

因此，当自定义组件不涉及到状态变量和自定义生命周期时，可以优先使用@Builder替换自定义组件，提升性能。

优化策略

自定义组件示例代码：

```
1. @Component
2. export struct example {
3. build() {
4. Column(){
5. Text('Custom Component Sample Code')
6. // ...
7. }
8. }
9. }
```

[segment1.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment1.ets#L2-L10)

自定义构建函数示例代码：

```
1. @Builder
2. export function example1(){
3. Column(){
4. Text('Sample code for customizing the constructor')
5. // ...
6. }
7. }
```

[segment1.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment1.ets#L14-L20)

具体可以参考[优先使用@Builder方法代替自定义组件](bpta-ui-component-performance-optimization.md#section18773182614502)。

### 减少自定义组件产生多余节点

自定义组件自身为非渲染节点，仅是组件树和状态数据的组合，常规使用自定义组件时并不会产生多余的节点。但是给自定义组件添加属性后，会将自定义组件作为一个整体节点进行处理。对内部的组件树进行操作，如背景色绘制、圆角绘制等都会作用在该节点上。

通过DevEco Studio内置ArkUI Inspector工具，查看组件树结构可以看到，相比使用@Builder方法，组件树多一个自定义组件节点，所以[优先使用@Builder方法代替自定义组件](bpta-component-nesting-optimization.md#section1012953161217)减少了自定义组件节点数量。而给自定义组件添加属性，会在自定义组件外部会创建一个“\_\_Common\_\_”类型的节点，如下图所示。为了避免这类“\_\_Common\_\_”节点的创建，可以将自定义组件的属性移至内部，或者动态设置自定义组件的属性。减少自定义组件产生多余节点，可以使总节点数量降低，从而提升性能。

**图1** 自定义组件树变化示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/whD4P4LoRUCdpYQVY3pzLA/zh-cn_image_0000002229337457.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=2FDE68E3F0E0CC13F6B905CF132A581101A62431E25D446AC5E8426AED948010 "点击放大")

**将自定义组件的属性移至内部**

当需要给自定义组件添加属性时，一般少量属性的场景下，可以将这些属性移至自定义组件内部，具体优化示例如下所示。

反例：

```
1. @Component
2. export struct Example {
3. build() {
4. Column() {
5. // Custom Components
6. FlowListStruct(
7. // Custom Component Passing Parameters
8. // ...
9. ).backgroundColor('#FFFFFF')
10. }
11. .width('100%')
12. .height('100%')
13. }
14. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment2.ets#L8-L22)

正例：

```
1. @Component
2. export struct FlowListStruct2 {
3. build() {
4. Column() {
5. // ...
6. }
7. .backgroundColor('#FFFFFF')
8. }
9. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment2.ets#L26-L35)

**动态设置自定义组件的属性**

ArkUI提供了[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)的接口，支持使用自定义AttributeModifier构建组件并配置属性。当需要给自定义组件设置较多属性时，如果将所有的属性设置都内移，会出现传递参数过多的问题，同时也会创建更多状态变量，增加参数的传递耗时。虽然减少了节点数量，但是性能没有得到有效提升。推荐使用自定义AttributeModifier的方式来动态设置自定义组件的属性，减少节点数量的同时，也避免了参数过多导致耗时的问题，具体优化示例如下所示。

```
1. @Entry
2. @Component
3. struct CustomComponentModifier {
4. modifier: ColumnModifier = new ColumnModifier();

6. aboutToAppear(): void {
7. this.modifier.width = 100;
8. this.modifier.height = 100;
9. this.modifier.backgroundColor = Color.Red;
10. }

12. build() {
13. Column() {
14. ModifierCustom({ modifier: this.modifier })
15. }
16. }
17. }

20. @Component
21. struct ModifierCustom {
22. @Require @Prop modifier: AttributeModifier<ColumnAttribute>;

24. build() {
25. Column() {
26. Text('Hello World')
27. }.attributeModifier(this.modifier)
28. }
29. }

31. // When using dynamic attribute setting, you need to inherit AttributeModifier, implement a Modifier by yourself, and then set it to the required component.
32. class ColumnModifier implements AttributeModifier<ColumnAttribute> {
33. width: number = 0;
34. height: number = 0;
35. backgroundColor: ResourceColor | undefined = undefined;

37. applyNormalAttribute(instance: ColumnAttribute): void {
38. instance.width(this.width);
39. instance.height(this.height);
40. instance.backgroundColor(this.backgroundColor);
41. }
42. }
```

[segment2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment2.ets#L39-L81)

### 选择合适的布局组件

复杂布局提供了场景化的能力，解决一种或者多种布局场景。但是在一些场景下，不恰当的使用这些高级组件，可能带来更多的性能消耗。

优化策略：

* 在相同嵌套层级的情况下，如果多种布局方式可以实现相同布局效果，优选低耗时的布局，如使用Column、Row替代Flex实现相同的单行布局。
* 在能够通过其他布局大幅优化节点数的情况下，可以使用高级组件替代，如使用RelativeContainer替代Row、Column实现扁平化布局，此时其收益大于布局组件本身的性能差距。
* 仅在必要的场景下使用高耗时的布局组件，如使用Flex实现折行布局、使用Grid实现二维网格布局等。

具体可以参考[合理使用布局组件](bpta-improve-layout-performance.md#section12745188175420)

### 删除无用的Stack/Column/Row嵌套，移除冗余节点

在组件嵌套的情况中，可以找到一些无用的容器组件嵌套。在考虑组件嵌套优化中，可以删除掉无用容器组件嵌套，移除冗余节点，从而避免冗余节点对性能的消耗。

优化方式：

反例：

```
1. @Component
2. export struct example {
3. build() {
4. Column() {
5. Row() {
6. // Custom Components
7. FlowListStruct(
8. // Custom Component Passing Parameters
9. // ...
10. )
11. }
12. .width('100%')
13. }
14. .width('100%')
15. .height('100%')
16. }
17. }
```

[segment3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment3.ets#L8-L25)

正例：

```
1. @Component
2. export struct example2 {
3. build() {
4. Column() {
5. // Custom Components
6. FlowListStruct(
7. // Custom Component Passing Parameters
8. // ...
9. )
10. }
11. .width('100%')
12. .height('100%')
13. }
14. }
```

[segment3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment3.ets#L28-L42)

### 优先使用组件属性代替嵌套组件

在实现文本浮层、按压遮罩或颜色叠加等场景时，通常会采用Stack布局嵌套组件的方式。实际上有些场景直接使用组件属性或借助系统API的能力就能实现，例如使用[overlay](../harmonyos-references/ts-universal-attributes-overlay.md#overlay)属性可以实现浮层场景，使用[ColorMetrics](../harmonyos-references/js-apis-arkui-graphics.md#colormetrics12)可以实现颜色叠加效果。直接使用组件属性的方式可以减少Stack布局嵌套组件的使用，从而减少嵌套组件带来的节点数。以文本浮层场景为例，如下图所示，使用overlay属性实现文本浮层比Stack组件嵌套方式少了一层Stack节点。开发这一类场景时，推荐优先使用组件属性代替嵌套组件。

**图2** 使用组件属性代替嵌套组件示意图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/UPq0ipapSKWuftM8WghsXw/zh-cn_image_0000002194011652.png?HW-CC-KV=V1&HW-CC-Date=20260429T061328Z&HW-CC-Expire=86400&HW-CC-Sign=1B5FDF8C0EA4EBE08106EBE0E6E058A932D5FF919BFBF9F41E69AAD482AE7F96 "点击放大")

**使用overlay属性实现浮层**

使用overlay属性可以直接给组件添加浮层，实现堆叠的效果，常见的场景有文本浮层、按压遮罩等。相较于Stack布局嵌套组件的方式，使用overlay属性减少了Stack组件节点的创建。以增加文本浮层为例，具体优化示例如下所示。更多使用overlay属性实现浮层场景的示例可参考[浮层-示例](../harmonyos-references/ts-universal-attributes-overlay.md#示例)。

反例：

```
1. @Entry
2. @Component
3. struct StackNesting {
4. build() {
5. Column() {
6. Stack() {
7. Image($r('app.media.startIcon'))
8. .objectFit(ImageFit.Contain)
9. Text('fragmentary text')
10. .fontSize(20)
11. .fontColor(Color.Black)
12. }
13. }
14. }
15. }
```

[segment3.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment3.ets#L46-L61)

正例：

```
1. @Entry
2. @Component
3. struct OverlayExample {
4. @Builder
5. OverlayNode() {
6. Text('fragmentary text')
7. .fontSize(20)
8. .fontColor(Color.Black)
9. }

11. build() {
12. Column() {
13. Image($r('app.media.startIcon'))
14. .overlay(this.OverlayNode(), { align: Alignment.Center })
15. .objectFit(ImageFit.Contain)
16. }
17. }
18. }
```

[segment4.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment4.ets#L2-L20)

**使用****ColorMetrics****实现****颜色叠加**

系统通过[ColorMetrics](../harmonyos-references/js-apis-arkui-graphics.md#colormetrics12)接口提供了颜色计算能力，可以用于颜色叠加显示的场景。同样，与Stack布局嵌套组件的方式相比，直接使用ColorMetrics能力可以减少Stack层的布局节点，具体优化示例如下所示。

反例：

```
1. @Component
2. struct ColorNormal {
3. @Prop isSelected: boolean = false;

5. build() {
6. Stack() {
7. Column()
8. .width('100%')
9. .height(100)
10. .backgroundColor(this.isSelected ? Color.Blue : Color.Grey)
11. .borderRadius(12)
12. .alignItems(HorizontalAlign.Center)
13. .justifyContent(FlexAlign.Center)
14. Column()
15. .width('100%')
16. .height(100)
17. .backgroundColor(this.isSelected ? "#99000000" : Color.Grey)
18. .borderRadius(12)
19. .alignItems(HorizontalAlign.Center)
20. .justifyContent(FlexAlign.Center)
21. }
22. }
23. }

25. @Entry
26. @Component
27. struct ColorOverlayStackExample {
28. @State isSelected: boolean = false;

30. build() {
31. Scroll() {
32. Column() {
33. ColorNormal({ isSelected: this.isSelected })
34. .onClick(() => {
35. this.isSelected = !this.isSelected;
36. })
37. }
38. }
39. }
40. }
```

[segment5.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment5.ets#L2-L41)

正例：

```
1. import { ColorMetrics } from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. @Component
6. struct ColorMeasure {
7. @Prop isSelected: boolean = false;

9. build() {
10. Column()
11. .width('100%')
12. .height(100)
13. .backgroundColor(this.isSelected ? this.getBlendColor(Color.Blue, "#99000000").color : Color.Grey)
14. .borderRadius(12)
15. .alignItems(HorizontalAlign.Center)
16. .justifyContent(FlexAlign.Center)
17. }

19. getBlendColor(baseColor: ResourceColor, addColor: ResourceColor): ColorMetrics {
20. if (!baseColor || !addColor) {
21. try {
22. return ColorMetrics.resourceColor(Color.Black);
23. } catch (error) {
24. let err = error as BusinessError;
25. hilog.warn(0x000, 'testTag', `showToast failed, code=${err.code}, message=${err.message}`);
26. }
27. }
28. let sourceColor: ColorMetrics;
29. try {
30. sourceColor = ColorMetrics.resourceColor(baseColor).blendColor(ColorMetrics.resourceColor(addColor));
31. } catch (err) {
32. let error = err as BusinessError;
33. console.error(`Failed to blend color, code = ${error.code}, message =${error.message}`);
34. sourceColor = ColorMetrics.resourceColor(addColor);
35. }
36. return sourceColor;
37. }
38. }

40. @Entry
41. @Component
42. struct ColorMetricsExample {
43. @State isSelected: boolean = false;

45. build() {
46. Scroll() {
47. Column() {
48. ColorMeasure({ isSelected: this.isSelected })
49. .onClick(() => {
50. this.isSelected = !this.isSelected;
51. })
52. }
53. }
54. }
55. }
```

[segment6.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/ArkUI/Component_Nesting_Optimization/entry/src/main/ets/segment/segment6.ets#L2-L57)

## 实践数据对比

关于实践数据对比部分，具体可以参考[布局优化指导](bpta-improve-layout-performance.md)和[UI组件性能优化](bpta-ui-component-performance-optimization.md)的数据对比部分。

## 示例代码

* [不同场景下组件嵌套的性能优化策略](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/tree/master/ArkUI/Component_Nesting_Optimization)
