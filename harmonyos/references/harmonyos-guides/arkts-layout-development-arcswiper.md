---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-arcswiper
title: 创建弧形轮播 (ArcSwiper)（圆形屏幕推荐使用）
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 媒体展示 > 创建弧形轮播 (ArcSwiper)（圆形屏幕推荐使用）
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f40acbce75b44248380ef4265b7dba9fdee817613b66196a724088df6816ebbe
---

ArcSwiper是弧形轮播组件，在圆形屏幕场景下使用，提供弧形轮播显示能力。具体用法请参考[ArcSwiper](../harmonyos-references/ts-container-arcswiper.md)。

在使用ArcSwiper组件之前，需要在代码中先导入ArcSwiper模块。

```
1. import {
2. ArcSwiper,
3. ArcSwiperAttribute,
4. ArcDotIndicator,
5. ArcDirection,
6. ArcSwiperController
7. } from '@kit.ArkUI';
```

[ArcSwiperStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperStyles.ets#L16-L24)

## 设置导航点样式

ArcSwiper提供了默认的弧形导航点样式，导航点默认显示在ArcSwiper下方居中位置，开发者也可以通过[indicator](../harmonyos-references/ts-container-arcswiper.md#indicator)属性自定义弧形导航点的样式。

通过indicator属性，开发者可以设置弧形导航点的方向，同时也可以设置导航点和被选中导航点的颜色。

* 导航点使用默认样式

  ```
  1. ArcSwiper() {
  2. Text('0')
  3. .width(233)
  4. .height(233)
  5. .backgroundColor(Color.Gray)
  6. .textAlign(TextAlign.Center)
  7. .fontSize(30)

  9. Text('1')
  10. .width(233)
  11. .height(233)
  12. .backgroundColor(Color.Green)
  13. .textAlign(TextAlign.Center)
  14. .fontSize(30)

  16. Text('2')
  17. .width(233)
  18. .height(233)
  19. .backgroundColor(Color.Pink)
  20. .textAlign(TextAlign.Center)
  21. .fontSize(30)
  22. }
  ```

  [ArcSwiperStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperStyles.ets#L36-L59)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/BcO4ypvASzGS2YXT8PQoNg/zh-cn_image_0000002558764362.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=922AE1126349EA17452985B6329089C7D3F3BCF3FF30BE7345E5A32032364F27)
* 自定义导航点样式

  导航点位于ArcSwiper组件6点钟方向，导航点颜色设为红色，被选中导航点颜色为蓝色。

  ```
  1. ArcSwiper() {
  2. // ···
  3. }
  4. .indicator(
  5. new ArcDotIndicator()
  6. .arcDirection(ArcDirection.SIX_CLOCK_DIRECTION) // 设置导航点位于6点钟方向
  7. .itemColor(Color.Red) // 设置导航点颜色为红色
  8. .selectedItemColor(Color.Blue) // 设置选中导航点颜色为蓝色
  9. )
  ```

  [ArcSwiperStyles.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperStyles.ets#L63-L94)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/zOgE3hW6Tv-kEedq_CX3Jg/zh-cn_image_0000002558604706.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=854A0A0D6125830AD0625D23EBFCB5B683F95D9E7DFE8695A0782DD878B6B76E)

## 控制页面切换方式

ArcSwiper支持滑动手指、点击导航点、旋转表冠和控制控制器四种方式切换页面。以下示例展示通过控制控制器和旋转表冠翻页的方法。

* 控制控制器翻页。

  ```
  1. // 导入ArcButton和ArcSwiper模块
  2. import {
  3. ArcButton,
  4. ArcButtonOptions,
  5. ArcButtonStatus,
  6. ArcButtonStyleMode,
  7. ArcButtonPosition,
  8. ArcSwiper,
  9. ArcSwiperAttribute, // ArcSwiper的属性依赖ArcSwiperAttribute对象导入，不建议删除该对象的引入。
  10. ArcSwiperController,
  11. // ...
  12. } from '@kit.ArkUI';
  13. // ...

  15. // 如需作为页面入口，请取消@Entry的注释并删除export关键字
  16. // @Entry
  17. @Component
  18. export struct ArcSwiperToggle {
  19. private wearableSwiperController: ArcSwiperController = new ArcSwiperController();

  21. build() {
  22. // ...
  23. Column({ space: 12 }) {
  24. // ...
  25. Stack() {
  26. ArcSwiper(
  27. this.wearableSwiperController
  28. ) {
  29. // ...
  30. }
  31. .vertical(true)
  32. .indicator(false)

  34. // ...

  37. Column() {
  38. ArcButton({
  39. options: new ArcButtonOptions({
  40. label: 'previous',
  41. position: ArcButtonPosition.TOP_EDGE,
  42. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  43. onClick: () => {
  44. this.wearableSwiperController.showPrevious(); // 通过controller切换到前一页
  45. }
  46. })
  47. })

  49. Blank()

  51. ArcButton({
  52. options: new ArcButtonOptions({
  53. label: 'next',
  54. position: ArcButtonPosition.BOTTOM_EDGE,
  55. styleMode: ArcButtonStyleMode.EMPHASIZED_LIGHT,
  56. onClick: () => {
  57. this.wearableSwiperController.showNext(); // 通过controller切换到后一页
  58. }
  59. })
  60. })
  61. }.width('100%').height('100%')
  62. }
  63. // ...
  64. }
  65. // ...
  66. }
  67. }
  ```

  [ArcSwiperToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperToggle.ets#L16-L143)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/yi-WYyV-SiKHhQ1Ij9ahTA/zh-cn_image_0000002589324231.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=8BA6D7AA0E634F9956AAC1C6A795FEDCD0AB089B9F161C70FB73AE5C89B84F43)
* 旋转表冠翻页。

  ArcSwiper在获得焦点时能够响应旋转表冠的操作，用户可以通过旋转表冠来滑动ArcSwiper，从而浏览数据。

  ```
  1. ArcSwiper(
  2. // ···
  3. ) {
  4. // ···
  5. }
  6. // ···

  8. .focusable(true)
  9. .focusOnTouch(true)
  10. .defaultFocus(true)
  ```

  [ArcSwiperToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperToggle.ets#L50-L96)

  还可以通过设置[digitalCrownSensitivity](../harmonyos-references/ts-container-arcswiper.md#digitalcrownsensitivity)属性来调整表冠对事件响应的灵敏度，以适应不同规模的数据处理。在处理大量数据时，可以提高响应事件的灵敏度；而在处理少量数据时，则可以降低灵敏度设置。

  ```
  1. ArcSwiper(
  2. // ···
  3. ) {
  4. // ···
  5. }
  6. // ···

  8. .digitalCrownSensitivity(CrownSensitivity.MEDIUM)
  ```

  [ArcSwiperToggle.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperToggle.ets#L49-L100)

## 设置轮播方向

ArcSwiper支持水平和垂直方向上进行轮播，主要通过[vertical](../harmonyos-references/ts-container-arcswiper.md#vertical)属性控制。

当vertical为true时，表示在垂直方向上进行轮播；为false时，表示在水平方向上进行轮播。vertical默认值为false。

* 设置水平方向上轮播。

  ```
  1. ArcSwiper() {
  2. // ···
  3. }
  4. .indicator(true)
  5. .vertical(false)
  ```

  [ArcSwiperHorizontal.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperHorizontal.ets#L31-L58)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/ovcMzPnhRgW-17m5k8uXdQ/zh-cn_image_0000002558764362.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=3121F6252F12DD9C66A6F3E648B5AB12B0C45AA16BE7F527F8F919D8E989CDC8)
* 设置垂直方向轮播，导航点设为3点钟方向。

  ```
  1. ArcSwiper() {
  2. // ···
  3. }
  4. .indicator(new ArcDotIndicator()
  5. .arcDirection(ArcDirection.THREE_CLOCK_DIRECTION))
  6. .vertical(true)
  ```

  [ArcSwiperVertical.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperVertical.ets#L34-L62)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/5Kiw4w8OQcCcuOIHzwmG3g/zh-cn_image_0000002589244171.png?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=D86410263EFDC2DA45A07124E58B583FE417D1B06E1CA7158090D74251FF9F69)

## 自定义切换动画

ArcSwiper支持通过[customContentTransition](../harmonyos-references/ts-container-arcswiper.md#customcontenttransition)设置自定义切换动画，可以在回调中对视窗内所有页面逐帧设置透明度、缩放比例、位移、渲染层级等属性，从而实现自定义切换动画效果。

```
1. import { Decimal } from '@kit.ArkTS';
2. import {
3. ArcSwiper,
4. ArcSwiperAttribute, // ArcSwiper的属性依赖ArcSwiperAttribute对象导入，不建议删除该对象的引入。
5. } from '@kit.ArkUI';
6. // ...

8. // 如需作为页面入口，请取消@Entry的注释并删除export关键字
9. // @Entry
10. @Component
11. export struct ArcSwiperAction {
12. private MIN_SCALE: number = 0.1;
13. @State backgroundColors: Color[] = [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange];
14. @State opacityList: number[] = [];
15. @State scaleList: number[] = [];

17. aboutToAppear(): void {
18. for (let i = 0; i < this.backgroundColors.length; i++) {
19. this.opacityList.push(1.0);
20. this.scaleList.push(1.0);
21. }
22. }

24. build() {
25. // ...
26. Column({ space: 12 }) {
27. // ...
28. ArcSwiper() {
29. ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
30. Text(index.toString())
31. .width(233)
32. .height(233)
33. .fontSize(50)
34. .textAlign(TextAlign.Center)
35. .backgroundColor(backgroundColor)
36. .opacity(this.opacityList[index])
37. .scale({ x: this.scaleList[index], y: this.scaleList[index] })
38. })
39. }
40. .customContentTransition({
41. timeout: 1000,
42. transition: (proxy: SwiperContentTransitionProxy) => {
43. if (proxy.position <= -1 || proxy.position >= 1) {
44. // 页面完全滑出视窗外时，重置属性值
45. this.opacityList[proxy.index] = 1.0;
46. this.scaleList[proxy.index] = 1.0;
47. } else {
48. let position: number = Decimal.abs(proxy.position).toNumber();
49. this.opacityList[proxy.index] = 1 - position;
50. this.scaleList[proxy.index] =
51. this.MIN_SCALE + (1 - this.MIN_SCALE) * (1 - position);
52. }
53. }
54. })
55. // ...
56. }
57. .width('100%')
58. // ...
59. }
60. }
```

[ArcSwiperAction.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperAction.ets#L16-L93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/OYVow7YET5ylX7AdERi0Ng/zh-cn_image_0000002558764364.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=B8203074AEE6B798737BDA537D7F975694F5F1DA7B85C8BE02C1ECA7EA8A341F)

## 实现侧滑返回

ArcSwiper的滑动事件会与侧滑返回冲突，可以通过[onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin)去判断ArcSwiper是否滑动到开头去拦截ArcSwiper的滑动手势，实现再次左滑返回上一页的功能。

```
1. import {
2. ArcSwiper,
3. ArcSwiperAttribute, // ArcSwiper的属性依赖ArcSwiperAttribute对象导入，不建议删除该对象的引入。
4. } from '@kit.ArkUI';
5. // ...

7. // 如需作为页面入口，请取消@Entry的注释并删除export关键字
8. // @Entry
9. @Component
10. export struct ArcSwiperSideSlip {
11. @State backgroundColors: Color[] = [Color.Green, Color.Blue, Color.Yellow, Color.Pink, Color.Gray, Color.Orange];
12. innerSelectedIndex: number = 0;

14. build() {
15. // ...
16. Column({ space: 12 }) {
17. // ...
18. ArcSwiper() {
19. ForEach(this.backgroundColors, (backgroundColor: Color, index: number) => {
20. Text(index.toString())
21. .width(233)
22. .height(233)
23. .fontSize(50)
24. .textAlign(TextAlign.Center)
25. .backgroundColor(backgroundColor)
26. })
27. }
28. .onAnimationStart((index: number, targetIndex: number) => {
29. this.innerSelectedIndex = targetIndex;
30. })
31. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
32. others: Array<GestureRecognizer>): GestureJudgeResult => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
33. if (current) {
34. let target = current.getEventTargetInfo();
35. if (target && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
36. let swiperTarget = target as ScrollableTargetInfo;
37. if (swiperTarget instanceof ScrollableTargetInfo &&
38. (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) { // 此处判断swiperTarget.isBegin()或innerSelectedIndex === 0，表明ArcSwiper滑动到开头
39. let panEvent = event as PanGestureEvent;
40. if (panEvent && panEvent.offsetX > 0 && (swiperTarget.isBegin() || this.innerSelectedIndex === 0)) {
41. return GestureJudgeResult.REJECT;
42. }
43. }
44. }
45. }
46. return GestureJudgeResult.CONTINUE;
47. })
48. // ...
49. }
50. .width('100%')
51. // ...
52. }
53. }
```

[ArcSwiperSideSlip.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/ScrollableComponent/entry/src/main/ets/pages/arcSwiper/ArcSwiperSideSlip.ets#L16-L86)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Bsq63anJSQ606k3dl4-EJg/zh-cn_image_0000002558604708.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052749Z&HW-CC-Expire=86400&HW-CC-Sign=6339438635EF36E9FAA73AE672107D5D0CF5CACF9FF3C0EB69F3D7A0A0731428)
