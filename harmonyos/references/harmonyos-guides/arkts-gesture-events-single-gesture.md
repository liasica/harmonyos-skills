---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-single-gesture
title: 单一手势
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 单一手势
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:63ea3863278eef99a0e7b63fe3672ca464134013421e57e3d96750b341aaca01
---

## 点击事件（onClick）

单击作为常用的手势，可以方便地使用[onClick](../harmonyos-references/ts-universal-events-click.md#onclick)接口实现。尽管被称为事件，它实际上是基本手势类型，等同于将count配置为1的TapGesture，即单击手势。

onClick与其他手势类型相同，也会参与命中测试、响应链收集等过程。可以使用[干预手势处理](rkts-interaction-development-guide-support-gesture.md#干预手势处理)机制对onClick的响应进行动态决策。

```
1. @Entry
2. @Component
3. export struct OnClickGesture {
4. private judgeCount: number = 0;

6. increaseJudgeGuard(): void {
7. this.judgeCount++;
8. }

10. build() {
11. NavDestination() {
12. Column() {
13. Column() {
14. Column()
15. .width('60%')
16. .height('50%')
17. .backgroundColor(Color.Grey)
18. .onClick(() => {
19. // 1. 子组件上注册了点击事件，正常情况下点击在子组件上时，优先得到响应
20. console.info('Clicked on child');
21. this.increaseJudgeGuard();
22. })
23. .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
24. // 3. 当数字增长为5的倍数时禁用子组件上的点击手势，此时父组件上的点击可以得到响应
25. if (this.judgeCount % 5 == 0 && gestureInfo.type == GestureControl.GestureType.CLICK) {
26. return GestureJudgeResult.REJECT;
27. } else {
28. return GestureJudgeResult.CONTINUE;
29. }
30. })
31. }
32. .width('80%')
33. .height('80%')
34. .justifyContent(FlexAlign.Center)
35. .backgroundColor(Color.Green)
36. .gesture(
37. // 2. 父组件上注册了点击手势，正常情况下点击在子组件区域时，父组件上的手势优先级低于子组件
38. TapGesture()
39. .onAction(() => {
40. console.info('Clicked on parent');
41. this.increaseJudgeGuard();
42. }))
43. }
44. .height('100%')
45. .width('100%')
46. .justifyContent(FlexAlign.Center)
47. }
48. .backgroundColor('#f1f2f3')
49. // 请将$r('app.string.singlegesture_Index_Click_title')替换为实际资源文件，在本示例中该资源文件的value值为"点击事件"
50. .title($r('app.string.singlegesture_Index_Click_title'))
51. }
52. }
```

[OnClickGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/OnClickGesture.ets#L16-L67)

示例中，每点击5次，子组件的点击事件将临时禁用1次，确保父组件点击优先响应。

## 点击手势（TapGesture）

```
1. TapGesture(value?: TapGestureParameters)
```

点击手势支持单次点击和多次点击，参数定义参考[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)。

```
1. @Entry
2. @Component
3. export struct Tap {
4. @State value: string = '';

6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {
9. Column() {
10. Text('Click twice').fontSize(28)
11. .gesture(
12. // 绑定count为2的TapGesture
13. TapGesture({ count: 2 })
14. .onAction((event: GestureEvent|undefined) => {
15. if(event){
16. this.value = JSON.stringify(event.fingerList[0]);
17. }
18. }))
19. Text(this.value)
20. }
21. .height(300)
22. .width(250)
23. .padding(20)
24. .border({ width: 3 })
25. .margin(30)
26. }
27. .width('100%')
28. .height('100%')
29. .padding({ left: 12, right: 12 })
30. }
31. .backgroundColor('#f1f2f3')
32. // 请将$r('app.string.singlegesture_TapGesture_title')替换为实际资源文件，在本示例中该资源文件的value值为"点击手势"
33. .title($r('app.string.singlegesture_TapGesture_title'))
34. }
35. }
```

[TapGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/TapGesture.ets#L16-L52)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/wTSLSpbXQ3-J5aZ5hWDhxw/zh-cn_image_0000002589244255.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=CA749B0E4917DFA26D798074E46CE3CE2D4235671F6E9B8BDEA5AEB231BBF2CC)

## 长按手势（LongPressGesture）

```
1. LongPressGesture(value?:{fingers?:number, repeat?:boolean, duration?:number})
```

长按手势用于触发长按手势事件，参数定义参考[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)。

以在Text组件上绑定可以重复触发的长按手势为例：

```
1. @Entry
2. @Component
3. export struct LongPress {
4. @State count: number = 0;

6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {
9. Column() {
10. Text('LongPress OnAction:' + this.count).fontSize(28)
11. .gesture(
12. // 绑定可以重复触发的LongPressGesture
13. LongPressGesture({ repeat: true })
14. .onAction((event: GestureEvent | undefined) => {
15. if (event) {
16. if (event.repeat) {
17. this.count++;
18. }
19. }
20. })
21. .onActionEnd(() => {
22. this.count = 0;
23. })
24. )
25. }
26. .height(200)
27. .width(250)
28. .padding(20)
29. .border({ width: 3 })
30. .margin(30)
31. }
32. .width('100%')
33. .height('100%')
34. .padding({ left: 12, right: 12 })
35. }
36. .backgroundColor('#f1f2f3')
37. // 请将$r('app.string.singlegesture_LongPressGesture_title')替换为实际资源文件，在本示例中该资源文件的value值为"长按手势"
38. .title($r('app.string.singlegesture_LongPressGesture_title'))
39. }
40. }
```

[LongPressGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/LongPressGesture.ets#L16-L57)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/rQ5tEGgPT2Okvk2xnffqAg/zh-cn_image_0000002558764448.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=A32D10F00219E9CB8A0297A5B004573398D9DA799FF0542BD1F4FFC6C00D059D)

## 滑动手势（PanGesture）

```
1. PanGesture(value?: { fingers?: number; direction?: PanDirection; distance?: number } | PanGestureOptions)
```

滑动手势用于触发滑动手势事件，滑动达到最小滑动距离（默认值为5vp）时滑动手势识别成功，参数定义参考[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)。

以下以实现一个简单的音量控制为例，可以通过滑动手势的回调函数处理多种不同的输入情况下的音量值增减的逻辑。

支持以下五种操作方式：

1. 单指上下滑动；
2. 按住鼠标左键上下滑动；
3. 鼠标滚轮滚动；
4. 单指按住触控板上下滑动；
5. 使用触控板双指滑动。

```
1. @Entry
2. @Component
3. export struct VolumeControlDemo {
4. @State currentVolume: number = 50;
5. private readonly MAX_VOLUME: number = 100;
6. private readonly MIN_VOLUME: number = 0;

8. private handlePanUpdate(event: GestureEvent) {
9. const volumeChange = -event.offsetY * 0.1;
10. this.handleVolumeChange(volumeChange);
11. }

13. private handleWheelEvent(event: GestureEvent) {
14. const volumeChange = event.offsetY * 0.1;
15. this.handleVolumeChange(volumeChange);
16. }

18. private handleTouchPadScroll(event: GestureEvent) {
19. const volumeChange = -event.offsetY * 0.02;
20. this.handleVolumeChange(volumeChange);
21. }

23. private handleVolumeChange(delta: number) {
24. this.currentVolume = Math.min(
25. this.MAX_VOLUME,
26. Math.max(this.MIN_VOLUME, this.currentVolume + delta)
27. );
28. }

30. build() {
31. NavDestination() {
32. Column() {
33. Row() {
34. // 请将$r('app.string.video')替换为实际资源文件，在本示例中该资源文件的value值为"音量"
35. Text($r('app.string.video'))
36. Text(`： ${this.currentVolume}`).fontSize(20)
37. }.margin(10)
38. Column()
39. .width('100%')
40. .height(250)
41. .backgroundColor('#F5F5F5')
42. .borderRadius(12)
43. .gesture(
44. PanGesture()
45. .onActionStart(() => {
46. console.info('Pan start');
47. })
48. .onActionUpdate((event: GestureEvent) => {
49. if (event.source === SourceType.TouchScreen) {
50. console.info('finger move triggered PanGesture');
51. this.handlePanUpdate(event);
52. }
53. if (event.source === SourceType.Mouse && event.sourceTool === SourceTool.MOUSE) {
54. if (event.axisHorizontal === 0 && event.axisVertical === 0) {
55. console.info('mouse move with left button pressed triggered PanGesture');
56. this.handlePanUpdate(event);
57. } else {
58. console.info('mouse wheel triggered PanGesture');
59. this.handleWheelEvent(event);
60. }
61. }
62. if (event.sourceTool === SourceTool.TOUCHPAD &&
63. (event.axisHorizontal !== 0 || event.axisVertical !== 0)) {
64. console.info('touchpad double finger move triggered PanGesture');
65. this.handleTouchPadScroll(event);
66. }
67. })
68. )
69. }
70. .width('100%')
71. .height('100%')
72. .padding(20)
73. }
74. .backgroundColor('#f1f2f3')
75. // 请将$r('app.string.singlegesture_Index_Pancom_title')替换为实际资源文件，在本示例中该资源文件的value值为"滑动手势"
76. .title($r('app.string.singlegesture_Index_Pancom_title'))
77. }
78. }
```

[PanCombinationGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/PanCombinationGesture.ets#L16-L95)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/r5IWmwHPR0efJSEsZw4oLQ/zh-cn_image_0000002558604792.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=7F477A0ABE1A5DEFBAB633D5A9790399CCD219075CE68013C4DA87B31A6427C0)

说明

* 大部分可滑动组件，如List、Grid、Scroll、Tab等组件是通过PanGesture实现滑动，在组件内部的子组件绑定[滑动手势（PanGesture）](arkts-gesture-events-single-gesture.md#滑动手势pangesture)或者[快滑手势（SwipeGesture）](arkts-gesture-events-single-gesture.md#快滑手势swipegesture)会导致手势竞争。
* 当在子组件绑定PanGesture时，在子组件区域进行滑动仅触发子组件的PanGesture。如果需要父组件响应，需要通过修改手势绑定方法或者子组件向父组件传递消息进行实现，或者通过修改父子组件的PanGesture参数distance使得滑动更灵敏。当子组件绑定SwipeGesture时，由于PanGesture和SwipeGesture触发条件不同，需要修改PanGesture和SwipeGesture的参数以达到所需效果。
* 不合理的阈值设置会导致滑动不跟手（响应时延慢）的问题。

## 捏合手势（PinchGesture）

```
1. PinchGesture(value?: { fingers?: number; distance?: number })
```

捏合手势用于触发捏合手势事件，参数定义参考[PinchGesture](../harmonyos-references/ts-basic-gestures-pinchgesture.md)。

以在Column组件上绑定三指捏合手势为例，可以通过在捏合手势的函数回调中获取缩放比例，实现对组件的缩小或放大：

```
1. @Entry
2. @Component
3. export struct Pinch {
4. @State scaleValue: number = 1;
5. @State pinchValue: number = 1;
6. @State pinchX: number = 0;
7. @State pinchY: number = 0;

9. build() {
10. NavDestination() {
11. Column({ space: 12 }) {
12. Column() {
13. Column() {
14. Text('PinchGesture scale:\n' + this.scaleValue)
15. Text('PinchGesture center:\n(' + this.pinchX + ',' + this.pinchY + ')')
16. }
17. .height(200)
18. .width(300)
19. .border({ width: 3 })
20. .margin({ top: 100 })
21. // 在组件上绑定缩放比例，可以通过修改缩放比例来实现组件的缩小或者放大
22. .scale({ x: this.scaleValue, y: this.scaleValue, z: 1 })
23. .gesture(
24. // 在组件上绑定三指触发的捏合手势
25. PinchGesture({ fingers: 3 })
26. .onActionStart((event: GestureEvent | undefined) => {
27. console.info('Pinch start');
28. })// 当捏合手势触发时，可以通过回调函数获取缩放比例，从而修改组件的缩放比例
29. .onActionUpdate((event: GestureEvent | undefined) => {
30. if (event) {
31. this.scaleValue = this.pinchValue * event.scale;
32. this.pinchX = event.pinchCenterX;
33. this.pinchY = event.pinchCenterY;
34. }
35. })
36. .onActionEnd(() => {
37. this.pinchValue = this.scaleValue;
38. console.info('Pinch end');
39. })
40. )
41. }
42. }
43. .width('100%')
44. .height('100%')
45. .padding({ left: 12, right: 12 })
46. }
47. .backgroundColor('#f1f2f3')
48. // 请将$r('app.string.singlegesture_PinchGesture_title')替换为实际资源文件，在本示例中该资源文件的value值为"捏合手势"
49. .title($r('app.string.singlegesture_PinchGesture_title'))
50. }
51. }
```

[PinchGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/PinchGesture.ets#L16-L68)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/FV4z6exfQsiob7ByzMWacg/zh-cn_image_0000002589324317.png?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=4C934822141930B1F8D58AF58527CFA254F52B7ECEFEDDFE6BBB8C8AE467A15F)

## 旋转手势（RotationGesture）

```
1. RotationGesture(value?: { fingers?: number; angle?: number })
```

旋转手势用于触发旋转手势事件，参数定义参考[RotationGesture](../harmonyos-references/ts-basic-gestures-rotationgesture.md)。

以在Text组件上绑定旋转手势实现组件的旋转为例，可以通过在旋转手势的回调函数中获取旋转角度，从而实现组件的旋转：

```
1. @Entry
2. @Component
3. export struct Rotation {
4. @State angle: number = 0;
5. @State rotateValue: number = 0;

7. build() {
8. NavDestination() {
9. Column({ space: 12 }) {
10. Column() {
11. Text('RotationGesture angle:' + this.angle).fontSize(28)
12. // 在组件上绑定旋转布局，可以通过修改旋转角度来实现组件的旋转
13. .rotate({ angle: this.angle })
14. .gesture(
15. RotationGesture()
16. .onActionStart((event: GestureEvent|undefined) => {
17. console.info('RotationGesture is onActionStart');
18. })
19. // 当旋转手势生效时，通过旋转手势的回调函数获取旋转角度，从而修改组件的旋转角度
20. .onActionUpdate((event: GestureEvent|undefined) => {
21. if(event){
22. this.angle = this.rotateValue + event.angle;
23. }
24. console.info('RotationGesture is onActionEnd');
25. })
26. // 当旋转结束抬手时，固定组件在旋转结束时的角度
27. .onActionEnd(() => {
28. this.rotateValue = this.angle;
29. console.info('RotationGesture is onActionEnd');
30. })
31. .onActionCancel(() => {
32. console.info('RotationGesture is onActionCancel');
33. })
34. )
35. .height(200)
36. .width(300)
37. .padding(20)
38. .border({ width: 3 })
39. .margin(100)
40. }
41. }
42. .width('100%')
43. .height('100%')
44. .padding({ left: 12, right: 12 })
45. }
46. .backgroundColor('#f1f2f3')
47. // 请将$r('app.string.singlegesture_RotationGesture_title')替换为实际资源文件，在本示例中该资源文件的value值为"旋转手势"
48. .title($r('app.string.singlegesture_RotationGesture_title'))
49. }
50. }
```

[RotationGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/RotationGesture.ets#L16-L67)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/S7t4bCMbT4GElNkWQeDeuw/zh-cn_image_0000002589244257.png?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=0A59EEA6A7D27DA8117D872B8AE06A375395C0DF25E2F87C91E1122C56CD0E6C)

## 快滑手势（SwipeGesture）

```
1. SwipeGesture(value?: { fingers?: number; direction?: SwipeDirection; speed?: number })
```

快滑手势用于触发快滑事件，当滑动速度大于100vp/s时可以识别成功，参数定义参考[SwipeGesture](../harmonyos-references/ts-basic-gestures-swipegesture.md)。

以在Column组件上绑定快滑手势实现组件的旋转为例：

```
1. @Entry
2. @Component
3. export struct Swipe {
4. @State rotateAngle: number = 0;
5. @State speed: number = 1;

7. build() {
8. NavDestination() {
9. Column({ space: 12 }) {
10. Column() {
11. Column() {
12. Text('SwipeGesture speed\n' + this.speed)
13. Text('SwipeGesture angle\n' + this.rotateAngle)
14. }
15. .border({ width: 3 })
16. .width(300)
17. .height(200)
18. .margin(100)
19. // 在Column组件上绑定旋转，通过滑动手势的滑动速度和角度修改旋转的角度
20. .rotate({ angle: this.rotateAngle })
21. .gesture(
22. // 绑定滑动手势且限制仅在竖直方向滑动时触发
23. SwipeGesture({ direction: SwipeDirection.Vertical })
24. // 当滑动手势触发时，获取滑动的速度和角度，实现对组件的布局参数的修改
25. .onAction((event: GestureEvent|undefined) => {
26. if(event){
27. this.speed = event.speed;
28. this.rotateAngle = event.angle;
29. }
30. })
31. )
32. }
33. }
34. .width('100%')
35. .height('100%')
36. .padding({ left: 12, right: 12 })
37. }
38. .backgroundColor('#f1f2f3')
39. // 请将$r('app.string.singlegesture_SwipeGesture_title')替换为实际资源文件，在本示例中该资源文件的value值为"快滑手势"
40. .title($r('app.string.singlegesture_SwipeGesture_title'))
41. }
42. }
```

[SwipeGesture.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/singlegesture/SwipeGesture.ets#L16-L59)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/-LE45bHyQ0a44UR3Ji0T9g/zh-cn_image_0000002558764450.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=3BFCF0F28F046C1150CCA3CD5A8BF8DABF1232A7F045C503544F6332AC06EFCC)

说明

当SwipeGesture和PanGesture同时绑定时，若二者是以默认方式或者互斥方式进行绑定时，会发生竞争。SwipeGesture的触发条件为滑动速度达到100vp/s，PanGesture的触发条件为滑动距离达到5vp，先达到触发条件的手势触发。可以通过修改SwipeGesture和PanGesture的参数以达到不同的效果。
