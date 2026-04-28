---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-animation-smoothing
title: 动画衔接
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 使用动画 > 动画衔接
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:59+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6f0d2c004bbd97f351983cfe4784c6482ff94783b46764a49c9e1f18c01bc4dc
---

UI界面除了运行动画之外，还承载着与用户进行实时交互的功能。当用户行为根据意图变化发生改变时，UI界面应做到即时响应。例如用户在应用启动过程中，上滑退出，那么启动动画应该立即过渡到退出动画，而不应该等启动动画完成后再退出，从而减少用户等待时间。对于桌面翻页类从跟手到离手触发动画的场景，离手后动画的初始速度应继承手势速度，避免由于速度不连续导致停顿感的产生。针对以上场景，系统已提供动画与动画、手势与动画之间的衔接能力，保证各类场景下动画平稳光滑地过渡的同时，尽可能降低开发难度。

假设对于某一可动画属性，存在正在运行的动画。当UI侧行为改变该属性终点值时，开发者仅需在[animateTo](../harmonyos-references/ts-explicit-animation.md)动画闭包中改变属性值或者改变[animation](../harmonyos-references/ts-animatorproperty.md)接口作用的属性值，即可产生动画。系统会自动衔接之前的动画和当前的动画，开发者仅需要关注当前单次动画的实现。

示例如下。通过点击Click，红色方块的缩放属性会发生变化。当连续快速点击Click时，缩放属性的终点值连续发生变化，当前动画也会平滑过渡到朝着新的缩放属性终点值运动。

```
1. import { curves } from '@kit.ArkUI';

3. class SetAnimationVariables {
4. isAnimation: boolean = true

6. set(): void {
7. this.isAnimation = !this.isAnimation;
8. }
9. }

11. @Entry
12. @Component
13. struct AnimationToAnimationDemo {
14. // 第一步：声明相关状态变量
15. @State animationController: SetAnimationVariables = new SetAnimationVariables();

17. build() {
18. Column() {
19. Text('ArkUI')
20. .fontWeight(FontWeight.Bold)
21. .fontSize(12)
22. .fontColor(Color.White)
23. .textAlign(TextAlign.Center)
24. .borderRadius(10)
25. .backgroundColor(0xf56c6c)
26. .width(100)
27. .height(100)
28. .scale({
29. // 第二步：将状态变量设置到相关可动画属性接口
30. x: this.animationController.isAnimation ? 2 : 1,
31. y: this.animationController.isAnimation ? 2 : 1
32. })
33. .animation({ curve: curves.springMotion(0.4, 0.8) }) // 第四步：通过animation接口开启动画，动画终点值改变时，系统自动添加衔接动画

35. Button('Click')
36. .margin({ top: 200 })
37. .onClick(() => {
38. // 第三步：通过点击事件改变状态变量值，影响可动画属性值
39. this.animationController.set()
40. })
41. }
42. .width('100%')
43. .height('100%')
44. .justifyContent(FlexAlign.Center)
45. }
46. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/cohesion/template1/Index.ets#L15-L62)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/BYE-0GskSGKCXWGCYPrFvg/zh-cn_image_0000002583438043.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233958Z&HW-CC-Expire=86400&HW-CC-Sign=9AE0746FBF13D3E8AAC48297C0D86E157524FF5C79B94D52E9AB429A8E78B083)

## 手势与动画的衔接

使用滑动、捏合、旋转等手势的场景中，跟手过程中一般会触发属性的改变。离手后，这部分属性往往会继续发生变化，直到到达属性终点值。

离手阶段的属性变化初始速度应与离手前一刻的属性改变速度保持一致。如果离手后属性变化速度从0开始，就好像正在运行的汽车紧急刹车，造成观感上的骤变是用户和开发者都不希望看到的。

针对在[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)和[动画](arkts-animation.md)之间进行衔接的场景（如列表滑动），可以在跟手阶段每一次更改组件属性时，都使用跟手弹簧曲线的属性动画。离手时再用离手弹簧曲线产生离手阶段的属性动画。对于采用[springMotion](../harmonyos-references/js-apis-curve.md#curvesspringmotion9)曲线的动画，离手阶段动画将自动继承跟手阶段动画的速度，并以跟手动画当前位置为起点，运动到指定的属性终点。

示例代码如下，小球跟手运动。

```
1. import { curves } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const TAG: string = '[AnimatorTest]';

7. @Entry
8. @Component
9. struct SpringMotionDemo {
10. // 第一步：声明相关状态变量
11. @State positionX: number = 100;
12. @State positionY: number = 100;
13. diameter: number = 50;

15. build() {
16. Column() {
17. Row() {
18. Circle({ width: this.diameter, height: this.diameter })
19. .fill(Color.Blue)
20. .position({ x: this.positionX, y: this.positionY })// 第二步：将状态变量设置到相关可动画属性接口
21. .onTouch((event?: TouchEvent) => {
22. // 第三步：在跟手过程改变状态变量值，并且采用responsiveSpringMotion动画运动到新的值
23. if (event) {
24. if (event.type === TouchType.Move) {
25. // 跟手过程，使用responsiveSpringMotion曲线
26. this.getUIContext()?.animateTo({ curve: curves.responsiveSpringMotion() }, () => {
27. // 减去半径，以使球的中心运动到手指位置
28. this.positionX = event.touches[0].windowX - this.diameter / 2;
29. this.positionY = event.touches[0].windowY - this.diameter / 2;
30. hilog.info(DOMAIN, TAG, `move, animateTo x:${this.positionX}, y:${this.positionY}`);
31. })
32. } else if (event.type === TouchType.Up) {
33. // 第四步：在离手过程设定状态变量终点值，并且用springMotion动画运动到新的值，springMotion动画将继承跟手阶段的动画速度
34. this.getUIContext()?.animateTo({ curve: curves.springMotion() }, () => {
35. this.positionX = 100;
36. this.positionY = 100;
37. hilog.info(DOMAIN, TAG, `touchUp, animateTo x:100, y:100`);
38. })
39. }
40. }
41. })
42. }
43. .width('100%').height('80%')
44. .clip(true) // 如果球超出父组件范围，使球不可见
45. .backgroundColor(Color.Orange)

47. Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.Center }) {
48. // 请将$r('app.string.drag')替换为实际资源文件，在本示例中该资源文件的value值为"拖动小球"
49. Text($r('app.string.drag')).fontSize(16)
50. }
51. .width('100%')

53. Row() {
54. // 请将$r('app.string.location')替换为实际资源文件，在本示例中该资源文件的value值为"点击位置:"
55. Text($r('app.string.location') + ' [x: ' + Math.round(this.positionX) + ', y:' + Math.round(this.positionY) + ']').fontSize(16)
56. }
57. .padding(10)
58. .width('100%')
59. }.height('100%').width('100%')
60. }
61. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Animation/entry/src/main/ets/pages/cohesion/template2/Index.ets#L15-L77)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/GEZEgyvrTzqz5QoqQTUPKQ/zh-cn_image_0000002552957998.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233958Z&HW-CC-Expire=86400&HW-CC-Sign=0B74CDFD8A42C67F17D4A45AC70B2875B1EFEDE9F7B64A9F2D8E42209FAB8B34)
