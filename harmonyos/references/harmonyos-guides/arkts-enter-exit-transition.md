---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-enter-exit-transition
title: 出现/消失转场
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 转场动画 > 出现/消失转场
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6f29b4c0eb4ea27deccc14c2bc41e195094ee3223b65c917b227590f570ee5d3
---

[transition](../harmonyos-references/ts-transition-animation-component.md)是基础的组件转场接口，用于实现一个组件出现或者消失时的动画效果。可以通过[TransitionEffect对象](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)的组合使用，定义出各式效果。

**表1** 转场效果接口

| 转场效果 | 说明 | 动画 |
| --- | --- | --- |
| IDENTITY | 禁用转场效果。 | 无。 |
| OPACITY | 默认的转场效果，透明度转场。 | 出现时透明度从0到1，消失时透明度从1到0。 |
| SLIDE | 滑动转场效果。 | 出现时从窗口左侧滑入，消失时从窗口右侧滑出。 |
| translate | 通过设置组件平移创建转场效果。 | 出现时，平移参数的值从translate接口设置的值变化为默认值0，消失时从默认值0变化为translate接口设置的值。 |
| rotate | 通过设置组件旋转创建转场效果。 | 出现时，旋转参数的值从rotate接口设置的值变化为默认值0，消失时从默认值0变化为rotate接口设置的值。 |
| opacity | 通过设置透明度参数创建转场效果。 | 出现时，透明度参数的值从opacity设置的值变化为透明度默认值1，消失时从透明度默认值1变化为opacity设置的值。 |
| move | 通过[TransitionEdge](../harmonyos-references/ts-transition-animation-component.md#transitionedge10)创建从窗口哪条边缘出来的效果。 | 出现时从TransitionEdge方向滑入，消失时滑出到TransitionEdge方向。 |
| asymmetric | 通过此方法组合非对称的出现消失转场效果。  - appear：出现转场的效果。  - disappear：消失转场的效果。 | 出现时采用appear设置的TransitionEffect出现效果，消失时采用disappear设置的[TransitionEffect](../harmonyos-references/ts-transition-animation-component.md#transitioneffect10对象说明)消失效果。 |
| combine | 组合其他TransitionEffect。 | 组合其他TransitionEffect，一起生效。 |
| animation | 定义转场效果的动画参数：  - 如果不定义会跟随[animateTo](../harmonyos-references/ts-explicit-animation.md)的动画参数。  - 不支持通过控件的animation接口配置动画参数。  - TransitionEffect中animation的onFinish不生效。 | 调用顺序是从上往下，上面TransitionEffect的animation也会作用到下面TransitionEffect。 |

1. 创建TransitionEffect。

   ```
   1. // 出现时会是所有出现转场效果的叠加，消失时会是所有消失转场效果的叠加
   2. // 说明各个effect跟随的动画参数
   3. private effect: object =
   4. TransitionEffect.OPACITY // 创建了透明度转场效果，这里没有调用animation接口，会跟随animateTo的动画参数
   5. // 通过combine方法，添加缩放转场效果，并指定了springMotion(0.6, 1.2)曲线
   6. .combine(TransitionEffect.scale({ x: 0, y: 0 }).animation({ curve: curves.springMotion(0.6, 1.2) }))
   7. // 添加旋转转场效果，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion(0.6, 1.2)
   8. .combine(TransitionEffect.rotate({ angle: 90 }))
   9. // 添加平移转场效果，动画参数会跟随其之上带animation的TransitionEffect，也就是springMotion(0.6, 1.2)
   10. .combine(TransitionEffect.translate({ x: 150, y: 150 }))
   11. // 添加move转场效果，并指定了springMotion曲线
   12. .combine(TransitionEffect.move(TransitionEdge.END)).animation({curve: curves.springMotion()})
   13. // 添加非对称的转场效果，由于这里没有设置animation，会跟随上面的TransitionEffect的animation效果，也就是springMotion
   14. .combine(TransitionEffect.asymmetric(TransitionEffect.scale({
   15. x: 0,
   16. y: 0
   17. }), TransitionEffect.rotate({ angle: 90 })));
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/compTransition/template6/Index.ets#L21-L39)
2. 将转场效果通过[transition](../harmonyos-references/ts-transition-animation-component.md)接口设置到组件。

   ```
   1. Text('test')
   2. .transition(this.effect)
   ```
3. 新增或者删除组件触发转场。

   ```
   1. @State isPresent: boolean = true;
   2. // ...
   3. if (this.isPresent) {
   4. Text('test')
   5. .transition(this.effect)
   6. }
   7. // ...
   8. // 控制新增或者删除组件
   9. // 方式一：将控制变量放到animateTo闭包内，未通过animation接口定义动画参数的TransitionEffect将跟随animateTo的动画参数
   10. this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
   11. this.isPresent = false;
   12. })

   14. // 方式二：直接控制删除或者新增组件，动画参数由TransitionEffect的animation接口配置
   15. this.isPresent = false;
   ```

完整的示例代码和效果如下，示例中采用直接删除或新增组件的方式触发转场，也可以替换为在[animateTo](../harmonyos-references/ts-explicit-animation.md)闭包内改变控制变量触发转场。

```
1. import { curves } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TransitionEffectDemo {
6. @State isPresent: boolean = false;
7. // 第一步：创建TransitionEffect
8. private effect: TransitionEffect =
9. // 创建默认透明度转场效果，并指定了springMotion(0.6, 0.8)曲线
10. TransitionEffect.OPACITY.animation({
11. curve: curves.springMotion(0.6, 0.8)
12. })// 通过combine方法，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion(0.6, 0.8)
13. .combine(TransitionEffect.scale({
14. x: 0,
15. y: 0
16. }))// 添加旋转转场效果，这里的动画参数会跟随上面带animation的TransitionEffect，也就是springMotion(0.6, 0.8)
17. .combine(TransitionEffect.rotate({ angle: 90 }))// 添加平移转场效果，这里的动画参数使用指定的springMotion()
18. .combine(TransitionEffect.translate({ y: 150 })
19. .animation({ curve: curves.springMotion() }))// 添加move转场效果，这里的动画参数会跟随上面的TransitionEffect，也就是springMotion()
20. .combine(TransitionEffect.move(TransitionEdge.END));

22. build() {
23. Stack() {
24. if (this.isPresent) {
25. Column() {
26. Text('ArkUI')
27. .fontWeight(FontWeight.Bold)
28. .fontSize(20)
29. .fontColor(Color.White)
30. }
31. .justifyContent(FlexAlign.Center)
32. .width(150)
33. .height(150)
34. .borderRadius(10)
35. .backgroundColor(0xf56c6c)
36. // 第二步：将转场效果通过transition接口设置到组件
37. .transition(this.effect)
38. }

40. // 边框
41. Column()
42. .width(155)
43. .height(155)
44. .border({
45. width: 5,
46. radius: 10,
47. color: Color.Black
48. })

50. // 第三步：新增或者删除组件触发转场，控制新增或者删除组件
51. Button('Click')
52. .margin({ top: 320 })
53. .onClick(() => {
54. this.isPresent = !this.isPresent;
55. })
56. }
57. .width('100%')
58. .height('60%')
59. }
60. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/compTransition/template4/Index.ets#L15-L76)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/TGC3S9u6R_KFHXCFvwspiQ/zh-cn_image_0000002589244281.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=2DDF909FCAE424AA73A3C99E87383F1288915144DFD846ABDEABF1D191966A40)

对多个组件添加转场效果时，可以在[animation](../harmonyos-references/ts-animatorproperty.md#animation)动画参数中配置不同的delay值，实现组件渐次出现消失的效果：

```
1. const ITEM_COUNTS = 9;
2. const ITEM_COLOR = '#ED6F21';
3. const INTERVAL = 30;
4. const DURATION = 300;

6. @Entry
7. @Component
8. struct Index1 {
9. @State isGridShow: boolean = false;
10. private dataArray: number[] = new Array(ITEM_COUNTS);

12. aboutToAppear(): void {
13. for (let i = 0; i < ITEM_COUNTS; i++) {
14. this.dataArray[i] = i;
15. }
16. }

18. build() {
19. Stack() {
20. if (this.isGridShow) {
21. Grid() {
22. ForEach(this.dataArray, (item: number, index: number) => {
23. GridItem() {
24. Stack() {
25. Text((item + 1).toString())
26. }
27. .size({ width: 50, height: 50 })
28. .backgroundColor(ITEM_COLOR)
29. .transition(TransitionEffect.OPACITY
30. .combine(TransitionEffect.scale({ x: 0.5, y: 0.5 }))// 对每个方格的转场添加delay，实现组件的渐次出现消失效果
31. .animation({ duration: DURATION, curve: Curve.Friction, delay: INTERVAL * index }))
32. .borderRadius(10)
33. }
34. // 消失时，如果不对方格的所有父控件添加转场效果，则方格的消失转场不会生效
35. // 此处让方格的父控件在出现消失转场时一直以0.99的透明度显示，使得方格的转场效果不受影响
36. .transition(TransitionEffect.opacity(0.99))
37. }, (item: number) => item.toString())
38. }
39. .columnsTemplate('1fr 1fr 1fr')
40. .rowsGap(15)
41. .columnsGap(15)
42. .size({ width: 180, height: 180 })
43. // 消失时，如果不对方格的所有父控件添加转场效果，则方格的消失转场不会生效
44. // 此处让父控件在出现消失转场时一直以0.99的透明度显示，使得方格的转场效果不受影响
45. .transition(TransitionEffect.opacity(0.99))
46. }
47. }
48. .size({ width: '100%', height: '100%' })
49. .onClick(() => {
50. this.getUIContext()?.animateTo({
51. duration: DURATION + INTERVAL * (ITEM_COUNTS - 1),
52. curve: Curve.Friction
53. }, () => {
54. this.isGridShow = !this.isGridShow;
55. })
56. })
57. }
58. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/compTransition/template5/Index.ets#L15-L74)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/k3uVRfijQBeQCbcH7dO7Tw/zh-cn_image_0000002558764474.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052809Z&HW-CC-Expire=86400&HW-CC-Sign=AB506829D2C4A8B82E33D4D5621363D2CA2BD9F73DBD8BAEE5C96297AA6AA862)
