---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-adaptive-layout
title: 自适应布局
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 界面元素自适应变化 > 自适应布局
category: best-practices
scraped_at: 2026-04-29T14:12:07+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:d21ad6ca2cf8b7963d6ef8cffe907d0159985a48a8b694356d22501c666b3a7d
---

针对常见的开发场景，方舟开发框架提炼了七种自适应布局能力，这些布局可以独立使用，也可多种布局叠加使用。

| 自适应布局类别 | 自适应布局能力 | 使用场景 | 实现方式 |
| --- | --- | --- | --- |
| 自适应拉伸 | [拉伸能力](bpta-multi-device-adaptive-layout.md#拉伸能力) | 容器组件尺寸发生变化时，增加或减小的空间**全部分配**给容器组件内**指定区域**。 | [Flex布局](../harmonyos-references/ts-universal-attributes-flex-layout.md)的flexGrow和flexShrink属性 |
|  | [均分能力](bpta-multi-device-adaptive-layout.md#均分能力) | 容器组件尺寸发生变化时，增加或减小的空间**均匀分配**给容器组件内**所有空白区域**。 | [Row组件](../harmonyos-references/ts-container-row.md)、[Column组件](../harmonyos-references/ts-container-column.md)或[Flex组件](../harmonyos-references/ts-container-flex.md)的justifyContent属性设置为FlexAlign.SpaceEvenly |
| 自适应缩放 | [占比能力](bpta-multi-device-adaptive-layout.md#占比能力) | 子组件的宽或高**按照预设的比例**，随容器组件发生变化。 | 基于通用属性的两种实现方式：  - 将子组件的宽高设置为父组件宽高的百分比  - layoutWeight属性 |
|  | [缩放能力](bpta-multi-device-adaptive-layout.md#缩放能力) | 子组件的宽高**按照预设的比例**，随容器组件发生变化，且变化过程中子组件的**宽高比不变**。 | [布局约束](../harmonyos-references/ts-universal-attributes-layout-constraints.md)的aspectRatio属性 |
| 自适应延伸 | [延伸能力](bpta-multi-device-adaptive-layout.md#延伸能力) | 容器组件内的子组件，按照其**在列表中的先后顺序**，随容器组件尺寸变化显示或隐藏。 | 基于容器组件的两种实现方式：  - 通过[List组件](../harmonyos-references/ts-container-list.md)实现  - 通过[Scroll组件](../harmonyos-references/ts-container-scroll.md)配合[Row组件](../harmonyos-references/ts-container-row.md)或[Column组件](../harmonyos-references/ts-container-column.md)实现 |
|  | [隐藏能力](bpta-multi-device-adaptive-layout.md#隐藏能力) | 容器组件内的子组件，按照其**预设的显示优先级**，随容器组件尺寸变化显示或隐藏。**相同显示优先级的子组件同时显示或隐藏**。 | [布局约束](../harmonyos-references/ts-universal-attributes-layout-constraints.md)的displayPriority属性 |
| 自适应折行 | [折行能力](bpta-multi-device-adaptive-layout.md#折行能力) | 容器组件尺寸发生变化时，如果布局方向尺寸不足以显示完整内容，**自动换行**。 | [Flex组件](../harmonyos-references/ts-container-flex.md)的wrap属性设置为FlexWrap.Wrap |

下面我们依次介绍这几种自适应布局能力。

## 拉伸能力

拉伸能力是指容器组件尺寸发生变化时，增加或减小的空间全部分配给容器组件内指定区域。

拉伸能力通常通过[Flex布局](../harmonyos-references/ts-universal-attributes-flex-layout.md)中的flexGrow和flexShrink属性实现，flexGrow和flexShrink属性常与flexBasis属性搭配使用，故将这三个属性放在一起介绍。

| 属性 | 类型 | 默认值 | 描述 |
| --- | --- | --- | --- |
| flexGrow | number | 0 | 仅当父容器宽度大于所有子组件宽度的总和时，该属性生效。配置了此属性的子组件，按照比例拉伸，分配父容器的多余空间。 |
| flexShrink | number | 1 | 仅当父容器宽度小于所有子组件宽度的总和时，该属性生效。配置了此属性的子组件，按照比例收缩，分配父容器的不足空间。 |
| flexBasis | 'auto' | [Length](../harmonyos-references/ts-types.md#length) | 'auto' | 设置组件在Flex容器中主轴方向上基准尺寸。'auto'意味着使用组件原始的尺寸，不做修改。  flexBasis属性不是必须的，通过width或height也可以达到同样的效果。当flexBasis属性与width或height发生冲突时，以flexBasis属性为准。 |

说明

* 开发者期望将父容器的剩余空间全部分配给某空白区域时，也可以通过[Blank组件](../harmonyos-references/ts-basic-components-blank.md)实现。注意仅当父组件为Row\Column\Flex组件时，Blank组件才会生效。
* 类Web开发范式也是通过flex-grow和flex-shrink实现拉伸能力，同时也支持配置flex-basis，详见[通用样式](../harmonyos-references/js-components-common-styles.md)。
* 类Web开发范式没有提供blank组件，但可以通过div组件模拟blank组件的行为，如“<div style='flex-grow: 1; flex-shrink: 0; flex-basis: 0'></div>”。

**示例1**

本示例中的页面由中间的内容区（包含一张图片）以及两侧的留白区组成，各区域的属性配置如下。

* 中间内容区的宽度设置为400vp，同时将flexGrow属性设置为1，flexShrink属性设置为0。
* 两侧留白区的宽度设置为150vp，同时将flexGrow属性设置为0，flexShrink属性设置为1。

由上可知，父容器的基准尺寸是700vp（150vp+400vp+150vp）。

可以通过拖动底部的滑动条改变父容器的尺寸，查看布局变化。

* 当父容器的尺寸大于700vp时，父容器中多余的空间全部分配给中间内容区。
* 当父容器的尺寸小于700vp时，左右两侧的留白区按照“1:1”的比例收缩（即平均分配父容器的不足空间）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/IHhZSvIXTHiMbsIkJQYnKA/zh-cn_image_0000002355147005.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=43A30C8402B7A16C0448474B1C32E580DF67EE5EA2CCE881C7652115A3AA7F99)

```
1. @Entry
2. @Component
3. struct FlexibleCapability1 {
4. @State sliderWidth: number = 1000;

6. // Bottom slider - adjust container size by dragging the slider.
7. @Builder
8. slider() {
9. Slider({ value: this.sliderWidth, min: 300, max: 1000 })
10. .blockColor(Color.White)
11. .width('60%')
12. .onChange((value: number) => {
13. this.sliderWidth = value;
14. })
15. .position({ x: '20%', y: '80%' })
16. }

18. build() {
19. Column() {
20. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
21. // Distribute all extra space to the image using flexGrow and allocate all insufficient space to the side margins using flexShrink.
22. Row()
23. .width(150)
24. .height(400)
25. .backgroundColor($r('sys.color.comp_background_primary'))
26. .flexGrow(0)
27. .flexShrink(1)
28. Image($r('app.media.illustrator'))
29. .width(300)
30. .height(400)
31. .objectFit(ImageFit.Contain)
32. .backgroundColor('#66F1CCB8')
33. .flexGrow(1)
34. .flexShrink(0)
35. Row()
36. .width(150)
37. .height(400)
38. .backgroundColor($r('sys.color.comp_background_primary'))
39. .flexGrow(0)
40. .flexShrink(1)
41. }
42. .width(this.sliderWidth)

44. this.slider()
45. }
46. .width('100%')
47. .height('100%')
48. .backgroundColor($r('sys.color.background_secondary'))
49. .alignItems(HorizontalAlign.Center)
50. .justifyContent(FlexAlign.Center)
51. }
52. }
```

[FlexibleCapability1.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/flexibleCapability/FlexibleCapability1.ets#L17-L69)

**示例2**

文字和开关的尺寸固定，仅有中间空白区域（Blank组件）随父容器尺寸变化而伸缩。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/iw6dkuLCS4WwQk1iE6uS-Q/zh-cn_image_0000002321148306.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=FB0FD4333510E06E79022F15E4BD75680EF03E64228261A274750683CD32F9D1)

```
1. @Entry
2. @Component
3. struct FlexibleCapability2 {
4. @State rate: number = 0.8;

6. // Bottom slider - resize container by dragging the slider control.
7. @Builder
8. slider() {
9. Slider({ value: this.rate * 100, min: 55, max: 80 })
10. .blockColor(Color.White)
11. .width('60%')
12. .onChange((value: number) => {
13. this.rate = value / 100;
14. })
15. .position({ x: '20%', y: '80%' })
16. }

18. build() {
19. Row() {
20. Row() {
21. Text($r('app.string.healthy_use_phone'))
22. .fontSize(16)
23. .width(135)
24. .height(22)
25. .fontWeight(FontWeight.Medium)
26. .lineHeight(22)
27. // Implement stretch capability using the Blank component.
28. Blank()
29. Toggle({ type: ToggleType.Switch })
30. .width(36)
31. .height(20)
32. }
33. .height(55)
34. .borderRadius(12)
35. .padding({ left: 13, right: 13 })
36. .backgroundColor($r('sys.color.comp_background_primary'))
37. .width(this.rate * 100 + '%')

39. this.slider()
40. }
41. .width('100%')
42. .height('100%')
43. .backgroundColor($r('sys.color.background_secondary'))
44. .alignItems(VerticalAlign.Center)
45. .justifyContent(FlexAlign.Center)
46. }
47. }
```

[FlexibleCapability2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/flexibleCapability/FlexibleCapability2.ets#L17-L63)

## 均分能力

均分能力是指容器组件尺寸发生变化时，增加或减小的空间均匀分配给容器组件内所有空白区域。它常用于内容数量固定、均分显示的场景，比如工具栏、底部菜单栏等。

均分能力可以通过将[Row组件](../harmonyos-references/ts-container-row.md)、[Column组件](../harmonyos-references/ts-container-column.md)或[Flex组件](../harmonyos-references/ts-container-flex.md)的justifyContent属性设置为FlexAlign.SpaceEvenly实现，即子元素在父容器主轴方向等间距布局，相邻元素之间的间距、第一个元素与行首的间距、最后一个元素到行尾的间距都完全一样。

说明

* 均分能力还可以通过其它方式实现，如使用[Grid组件](../harmonyos-references/ts-container-grid.md)或在每个组件间添加Blank组件等。
* 类Web开发范式中，通过将[div组件](../harmonyos-references/js-components-container-div.md)的justify-content属性设置为space-evenly来实现均分布局。

**示例：**

父容器尺寸变化过程中，图标及文字的尺寸不变，图标间的间距及图标离左右边缘的距离同时均等改变。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/FLGUvCaaROSemSrcF82_mg/zh-cn_image_0000002355266889.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=5F74FA8F86838847FACD13FEEA866C59D37E07ADE7D17B9E41ED13E1E09F24CC)

```
1. @Entry
2. @Component
3. struct EquipartitionCapability {
4. @State rate: number = 0.6;
5. private list: number [] = [0, 1, 2, 3];

7. // Bottom slider - adjust container dimensions via slider drag interaction.
8. @Builder
9. slider() {
10. Slider({ value: this.rate * 100, min: 30, max: 60 })
11. .blockColor(Color.White)
12. .width('60%')
13. .height(50)
14. .onChange((value: number) => {
15. this.rate = value / 100;
16. })
17. .position({ x: '20%', y: '80%' })
18. }

20. @Builder
21. Item() {
22. Column() {
23. Image($r('app.media.icon'))
24. .width(48)
25. .height(48)
26. .margin(({ top: 8 }))
27. Text($r('app.string.show_app_name'))
28. .width(64)
29. .height(30)
30. .lineHeight(15)
31. .fontSize(12)
32. .textAlign(TextAlign.Center)
33. .margin({ top: 8 })
34. .padding({ bottom: 15 })
35. }
36. .width(80)
37. .height(102)
38. }

40. build() {
41. Row() {
42. Column() {
43. // Distribute remaining space evenly along the main axis of the parent container.
44. Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
45. ForEach(this.list, () => {
46. this.Item();
47. }, (item: number, index: number) => item.toString() + index)
48. }

50. // Distribute remaining space evenly along the main axis of the parent container.
51. Flex({ justifyContent: FlexAlign.SpaceEvenly }) {
52. ForEach(this.list, () => {
53. this.Item();
54. }, (item: number, index: number) => item.toString() + index)
55. }
56. }
57. .width(this.rate * 100 + '%')
58. .height(222)
59. .padding({ top: 16 })
60. .backgroundColor($r('sys.color.font_on_primary'))
61. .borderRadius(16)

63. this.slider()
64. }
65. .width('100%')
66. .height('100%')
67. .backgroundColor($r('sys.color.background_secondary'))
68. .alignItems(VerticalAlign.Center)
69. .justifyContent(FlexAlign.Center)
70. }
71. }
```

[EquipartitionCapability.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/equipartitionCapability/EquipartitionCapability.ets#L17-L87)

## 占比能力

占比能力是指子组件的宽高按照预设的比例，随父容器组件发生变化。

占比能力通常有两种实现方式：

* 将子组件的宽高设置为父组件宽高的百分比，详见[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)及[长度类型](../harmonyos-references/ts-types.md#length)。
* 通过layoutWeight属性配置互为兄弟关系的组件在父容器主轴方向的布局权重，详见[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)。

  + 当父容器尺寸确定时，其子组件按照开发者配置的权重比例分配父容器中主轴方向的空间。
  + 仅当父容器是Row、Column或者Flex时，layoutWeight属性才会生效。
  + 设置layoutWeight属性后，组件本身的尺寸会失效。比如同时设置了.width('40%')和.layoutWeight(1)，那么只有.layoutWeight(1)会生效。

layoutWeight存在使用限制，所以实际使用过程中大多通过将子组件宽高设置为父组件的百分比来实现占比能力。

说明

* 占比能力在实际开发中使用的非常广泛，可以通过很多不同的方式实现占比能力，如还可以通过[Grid组件](../harmonyos-references/ts-container-grid.md)的columnsTemplate属性设置网格容器中列的数量及其宽度比例，或通过配置子组件在[栅格](bpta-multi-device-responsive-layout.md#section1061332817545)中占据不同的列数来实现占比能力。
* 类Web开发范式同样支持以百分比的形式设置组件的宽高，详见[通用样式](../harmonyos-references/js-components-common-styles.md)中关于width和height的介绍以及[长度类型](../harmonyos-references/js-appendix-types.md#长度类型)。
* 与声明式开发范式中的layoutWeight属性类似，类Web开发范式提供了[flex-weight样式](../harmonyos-references/js-components-common-atomic-layout.md#占比能力)用于配置互为兄弟关系的组件在父容器主轴方向的布局权重。

**示例：**

简单的播放控制栏，其中“上一首”、“播放/暂停”、“下一首”的layoutWeight属性都设置为1，因此它们按照“1:1:1”的比例均分父容器主轴方向的空间。

将三个按钮的.layoutWeight(1)分别替换为.width('33%')、.width('34%')、.width('33%')，也可以实现与当前同样的显示效果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/sRcMUoYfSkCXrGHbN5EyCA/zh-cn_image_0000002321308190.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=4EAE1B38CC396A7C5042FEB065349478D15533B463ED999C73582DFD850AEBDF)

```
1. @Entry
2. @Component
3. struct ProportionCapability {
4. @State rate: number = 0.5;

6. // Bottom slider - adjust container size through slider drag interaction.
7. @Builder
8. slider() {
9. Slider({ value: 100, min: 25, max: 50 })
10. .blockColor(Color.White)
11. .width('60%')
12. .height(50)
13. .onChange((value: number) => {
14. this.rate = value / 100;
15. })
16. .position({ x: '20%', y: '80%' })
17. }

19. build() {
20. Row() {
21. Row() {
22. Column() {
23. Image($r('app.media.down'))
24. .width(48)
25. .height(48)
26. }
27. .height(96)
28. // Set the layout weight of child components along the main axis of the parent container.
29. .layoutWeight(1)
30. .justifyContent(FlexAlign.Center)

32. Column() {
33. Image($r('app.media.pause'))
34. .width(48)
35. .height(48)
36. }
37. .height(96)
38. .layoutWeight(1)
39. .backgroundColor('#66F1CCB8')
40. .justifyContent(FlexAlign.Center)

42. Column() {
43. Image($r("app.media.next"))
44. .width(48)
45. .height(48)
46. }
47. .height(96)
48. .layoutWeight(1)
49. .justifyContent(FlexAlign.Center)
50. }
51. .width(this.rate * 100 + '%')
52. .height(96)
53. .borderRadius(16)
54. .backgroundColor($r('sys.color.comp_background_primary'))

56. this.slider()
57. }
58. .width('100%')
59. .height('100%')
60. .backgroundColor($r('sys.color.background_secondary'))
61. .alignItems(VerticalAlign.Center)
62. .justifyContent(FlexAlign.Center)
63. }
64. }
```

[ProportionCapability.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/proportionCapability/ProportionCapability.ets#L17-L80)

## 缩放能力

缩放能力是指子组件的宽高按照预设的比例，随容器组件发生变化，且变化过程中子组件的宽高比不变。

缩放能力通过使用百分比布局配合**固定宽高比**（aspectRatio属性）实现当容器尺寸发生变化时，内容自适应调整。

可以访问[布局约束](../harmonyos-references/ts-universal-attributes-layout-constraints.md)，了解aspectRatio属性的详细信息。

说明

类Web开发范式同样提供了[aspect-ratio样式](../harmonyos-references/js-components-common-atomic-layout.md#固定比例)，用于固定组件的宽高比。

**示例：**

为方便查看效果，示例中特意给Column组件加了边框。可以看到Column组件随着其Flex父组件尺寸变化而缩放的过程中，始终保持预设的宽高比，其中的图片也始终正常显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/PNm0wsOMSXyyW-0XsIkWZg/zh-cn_image_0000002355147069.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=1DBD393A675A4D776584BA95B4B5D281903D0868865A7792439BBF515BB94587)

```
1. @Entry
2. @Component
3. struct ScaleCapability {
4. @State sliderWidth: number = 400;
5. @State sliderHeight: number = 400;

7. // Bottom slider - adjust container size through slider drag interaction.
8. @Builder
9. slider() {
10. Slider({
11. value: this.sliderWidth,
12. min: 100,
13. max: 400,
14. style: SliderStyle.OutSet
15. })
16. .blockColor(Color.White)
17. .width('60%')
18. .height(50)
19. .onChange((value: number) => {
20. this.sliderWidth = value;
21. })
22. .position({ x: '20%', y: '80%' })
23. Slider({
24. value: this.sliderHeight,
25. min: 100,
26. max: 400,
27. style: SliderStyle.OutSet
28. })
29. .blockColor(Color.White)
30. .width('60%')
31. .height(50)
32. .onChange((value: number) => {
33. this.sliderHeight = value;
34. })
35. .position({ x: '20%', y: '87%' })
36. }

38. build() {
39. Column() {
40. Column() {
41. Column() {
42. Image($r('app.media.illustrator'))
43. .width('100%')
44. .height('100%')
45. }
46. // Maintain fixed aspect ratio.
47. .aspectRatio(1)
48. // Decorative border (purely for visual demonstration purposes).
49. .border({ width: 2, color: '#66F1CCB8' })
50. }
51. .backgroundColor($r('sys.color.comp_background_primary'))
52. .height(this.sliderHeight)
53. .width(this.sliderWidth)
54. .alignItems(HorizontalAlign.Center)
55. .justifyContent(FlexAlign.Center)

57. this.slider()
58. }
59. .height('100%')
60. .width('100%')
61. .backgroundColor($r('sys.color.background_secondary'))
62. .alignItems(HorizontalAlign.Center)
63. .justifyContent(FlexAlign.Center)
64. }
65. }
```

[ScaleCapability.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/scaleCapability/ScaleCapability.ets#L17-L81)

## 延伸能力

延伸能力是指容器组件内的子组件，按照其在列表中的先后顺序，随容器组件尺寸变化显示或隐藏。它可以根据显示区域的尺寸，显示不同数量的元素。

延伸能力通常有两种实现方式：

* 通过[List组件](../harmonyos-references/ts-container-list.md)实现。
* 通过[Scroll组件](../harmonyos-references/ts-container-scroll.md)配合[Row组件](../harmonyos-references/ts-container-row.md)或[Column组件](../harmonyos-references/ts-container-column.md)实现。

说明

* List、Row或Column组件中子节点在页面显示时就已全部完成布局计算及渲染，只不过受限于父容器尺寸，用户只能看到一部分。随着父容器尺寸增大，用户可以看到的子节点数目也相应的增加。用户还可以通过手指滑动触发列表滑动，查看被隐藏的子节点。
* 类Web开发范式同样可以使用[list组件](../harmonyos-references/js-components-container-list.md)实现延伸能力。
* 类Web开发范式没有提供scroll组件，但可以将[div组件](../harmonyos-references/js-components-container-div.md)的overflow样式设置为scroll（即div组件主轴方向上子元素的尺寸超过div组件本身的尺寸时进行滚动显示）来模拟scroll组件的行为。

**示例：**

当父容器的尺寸发生改变时，页面中显示的图标数量随之发生改变。

分别通过List组件实现及通过Scroll组件配合Row组件实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/zil54D1WRJi8ohu38_7FMQ/zh-cn_image_0000002321148358.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=6250B832068E559C42993FC2875EEE91A1D5BDD6ACD56BA4788D016FA84F3A88)

（1）通过List组件实现。

```
1. @Entry
2. @Component
3. struct ExtensionCapability2 {
4. @State rate: number = 0.60;
5. private appList: number [] = [0, 1, 2, 3, 4, 5, 6, 7];

7. @Builder
8. slider() {
9. Slider({ value: this.rate * 100, min: 8, max: 60 })
10. .blockColor(Color.White)
11. .width('60%')
12. .height(50)
13. .onChange((value: number) => {
14. this.rate = value / 100;
15. })
16. .position({ x: '20%', y: '80%' })
17. }

19. build() {
20. Row() {
21. Row({ space: 10 }) {
22. // Implement extension capability through List component.
23. List({ space: 10 }) {
24. ForEach(this.appList, () => {
25. ListItem() {
26. Column() {
27. Image($r('app.media.icon'))
28. .width(48)
29. .height(48)
30. .margin({ top: 8 })
31. Text($r('app.string.show_app_name'))
32. .width(64)
33. .height(30)
34. .lineHeight(15)
35. .fontSize(12)
36. .textAlign(TextAlign.Center)
37. .margin({ top: 8 })
38. .padding({ bottom: 15 })
39. }
40. .width(80)
41. .height(102)
42. }
43. .width(80)
44. .height(102)
45. }, (item: number, index: number) => item.toString() + index)
46. }
47. .padding({ top: 16, left: 10 })
48. .listDirection(Axis.Horizontal)
49. .width('100%')
50. .height(118)
51. .borderRadius(16)
52. .backgroundColor(Color.White)
53. }
54. .width(this.rate * 100 + '%')

56. this.slider()
57. }
58. .width('100%')
59. .height('100%')
60. .justifyContent(FlexAlign.Center)
61. .alignItems(VerticalAlign.Center)
62. }
63. }
```

[ExtensionCapability2.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/extensionCapability/ExtensionCapability2.ets#L17-L79)

（2）通过Scroll组件配合Row组件实现。

```
1. @Entry
2. @Component
3. struct ExtensionCapability1 {
4. @State rate: number = 0.60;
5. private appList: number [] = [0, 1, 2, 3, 4, 5, 6, 7];

7. @Builder
8. slider() {
9. Slider({ value: this.rate * 100, min: 8, max: 60 })
10. .blockColor(Color.White)
11. .width('60%')
12. .height(50)
13. .onChange((value: number) => {
14. this.rate = value / 100;
15. })
16. .position({ x: '20%', y: '80%' })
17. }

19. build() {
20. Row() {
21. // Implement extension capability through Scroll and Row(or Column) components.
22. Scroll() {
23. Row({ space: 10 }) {
24. ForEach(this.appList, () => {
25. Column() {
26. Image($r('app.media.icon'))
27. .width(48)
28. .height(48)
29. .margin({ top: 8 })
30. Text($r('app.string.show_app_name'))
31. .width(64)
32. .height(30)
33. .lineHeight(15)
34. .fontSize(12)
35. .textAlign(TextAlign.Center)
36. .margin({ top: 8 })
37. .padding({ bottom: 15 })
38. }
39. .width(80)
40. .height(102)
41. }, (item: number, index: number) => item.toString() + index)
42. }
43. .padding({ top: 16, left: 10 })
44. .height(118)
45. .borderRadius(16)
46. .backgroundColor(Color.White)
47. }
48. .scrollable(ScrollDirection.Horizontal)
49. .width(this.rate * 100 + '%')

51. this.slider()
52. }
53. .width('100%')
54. .height('100%')
55. .alignItems(VerticalAlign.Center)
56. .justifyContent(FlexAlign.Center)
57. }
58. }
```

[ExtensionCapability1.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/extensionCapability/ExtensionCapability1.ets#L17-L75)

## 隐藏能力

隐藏能力是指容器组件内的子组件，按照其预设的显示优先级，随容器组件尺寸变化显示或隐藏，其中相同显示优先级的子组件同时显示或隐藏。它是一种比较高级的布局方式，常用于分辨率变化较大，且不同分辨率下显示内容有所差异的场景。主要思想是通过增加或减少显示内容，来保持最佳的显示效果。

隐藏能力通过设置**布局优先级**（displayPriority属性）来控制显隐，当布局主轴方向剩余尺寸不足以满足全部元素时，按照布局优先级大小，从小到大依次隐藏，直到容器能够完整显示剩余元素。具有相同布局优先级的元素将同时显示或者隐藏。

可以访问[布局约束](../harmonyos-references/ts-universal-attributes-layout-constraints.md)，了解displayPriority属性的详细信息。

说明

类Web开发范式同样支持[display-index样式](../harmonyos-references/js-components-common-atomic-layout.md#隐藏能力)，用于设置布局优先级。

**示例：**

父容器尺寸发生变化时，其子元素按照预设的优先级显示或隐藏。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/JXHFhPI9SMi2MYZXNQEvSg/zh-cn_image_0000002355266913.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=B2E3B66D6EF5B0B7985AD0EDA61FD6051D6277EF96B4EE1EAE66952D6AD76519)

```
1. @Entry
2. @Component
3. struct HiddenCapability {
4. @State rate: number = 0.8;

6. @Builder
7. slider() {
8. Slider({ value: this.rate * 100, min: 10, max: 80 })
9. .blockColor(Color.White)
10. .width('60%')
11. .height(50)
12. .onChange((value: number) => {
13. this.rate = value / 100;
14. })
15. .position({ x: '20%', y: '80%' })
16. }

18. build() {
19. Column() {
20. Row() {
21. Row() {
22. Image($r('app.media.favorite'))
23. .width(48)
24. .height(48)
25. .objectFit(ImageFit.Contain)
26. }
27. // Layout priority.
28. .displayPriority(1)
29. .padding({ left: 12, right: 12 })

31. Row() {
32. Image($r('app.media.down'))
33. .width(48)
34. .height(48)
35. .objectFit(ImageFit.Contain)
36. }
37. // Layout priority.
38. .displayPriority(2)
39. .padding({ left: 12, right: 12 })

41. Row() {
42. Image($r('app.media.pause'))
43. .width(48)
44. .height(48)
45. .objectFit(ImageFit.Contain)
46. }
47. // Layout priority.
48. .displayPriority(3)
49. .padding({ left: 12, right: 12 })

51. Row() {
52. Image($r('app.media.next'))
53. .width(48)
54. .height(48)
55. .objectFit(ImageFit.Contain)
56. }
57. // Layout priority.
58. .displayPriority(2)
59. .padding({ left: 12, right: 12 })

61. Row() {
62. Image($r('app.media.list'))
63. .width(48)
64. .height(48)
65. .objectFit(ImageFit.Contain)
66. }
67. // Layout priority.
68. .displayPriority(1)
69. .padding({ left: 12, right: 12 })
70. }
71. .width(this.rate * 100 + '%')
72. .height(96)
73. .borderRadius(16)
74. .backgroundColor($r('sys.color.comp_background_primary'))
75. .justifyContent(FlexAlign.Center)

77. this.slider()
78. }
79. .width('100%')
80. .height('100%')
81. .backgroundColor($r('sys.color.background_secondary'))
82. .alignItems(HorizontalAlign.Center)
83. .justifyContent(FlexAlign.Center)
84. }
85. }
```

[HiddenCapability.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/hiddenCapability/HiddenCapability.ets#L17-L102)

## 折行能力

折行能力是指容器组件尺寸发生变化，当布局方向尺寸不足以显示完整内容时自动换行。它常用于横竖屏适配或默认设备向平板切换的场景。

折行能力通过使用 **Flex折行布局** （将wrap属性设置为FlexWrap.Wrap）实现，当横向布局尺寸不足以完整显示内容元素时，通过折行的方式，将元素显示在下方。

可以访问[Flex组件](../harmonyos-references/ts-container-flex.md)，了解Flex组件的详细用法。

说明

类Web开发范式通过将[div组件](../harmonyos-references/js-components-container-div.md)的flex-warp样式设置为wrap来使用折行能力。

**示例：**

父容器中的图片尺寸固定，当父容器尺寸发生变化，其中的内容做自适应换行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/G8uPvcyhRJGSrdwh0X-c1A/zh-cn_image_0000002321308202.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061156Z&HW-CC-Expire=86400&HW-CC-Sign=EABF8B5C97E2420634460C59073E306403560D96388BF0062169F783BBE926C9)

```
1. @Entry
2. @Component
3. struct WrapCapabilitySample {
4. @State rate: number = 0.7;
5. imageList: Resource [] = [
6. $r('app.media.flexWrap1'),
7. $r('app.media.flexWrap2'),
8. $r('app.media.flexWrap3'),
9. $r('app.media.flexWrap4'),
10. $r('app.media.flexWrap5'),
11. $r('app.media.flexWrap6')
12. ];

14. @Builder
15. slider() {
16. Slider({ value: this.rate * 100, min: 50, max: 70 })
17. .blockColor(Color.White)
18. .width('60%')
19. .height(50)
20. .onChange((value: number) => {
21. this.rate = value / 100;
22. })
23. .position({ x: '20%', y: '87%' })
24. }

26. build() {
27. Column() {
28. Flex({
29. alignItems: ItemAlign.Center,
30. justifyContent: FlexAlign.Center,
31. wrap: FlexWrap.Wrap
32. }) {
33. ForEach(this.imageList, (item: Resource) => {
34. Image(item)
35. .width(192)
36. .height(138)
37. .padding(10)
38. }, (item: Resource, index: number) => item.toString() + index)
39. }
40. .backgroundColor($r('sys.color.comp_background_primary'))
41. .padding(20)
42. .width(this.rate * 100 + '%')
43. .borderRadius(16)

45. this.slider()
46. }
47. .width('100%')
48. .height('100%')
49. .backgroundColor($r('sys.color.background_secondary'))
50. .alignItems(HorizontalAlign.Center)
51. .justifyContent(FlexAlign.Center)
52. }
53. }
```

[WrapCapability.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AdaptiveCapabilities/entry/src/main/ets/pages/atomicLayoutCapability/wrapCapability/WrapCapability.ets#L17-L69)
