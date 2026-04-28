---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-combined-gestures
title: 组合手势
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 组合手势
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:974a9355d216c56487d107dfc263480803490a9edbbde1d57a4914914c9f530c
---

组合手势由多种单一手势组合而成，通过在[GestureGroup](../harmonyos-references/ts-combined-gestures.md#接口)中使用不同的[GestureMode](../harmonyos-references/ts-combined-gestures.md#gesturemode枚举说明)来声明该组合手势的类型，支持[顺序识别](arkts-gesture-events-combined-gestures.md#顺序识别)、[并行识别](arkts-gesture-events-combined-gestures.md#并行识别)和[互斥识别](arkts-gesture-events-combined-gestures.md#互斥识别)三种类型。

```
1. GestureGroup(mode:GestureMode, gesture:GestureType[])
```

* mode：为GestureMode枚举类。用于声明该组合手势的类型。
* gesture：由多个手势组合而成的数组。用于声明该组合手势的各个手势。

## 顺序识别

顺序识别组合手势对应的GestureMode为Sequence。顺序识别组合手势将按照手势的注册顺序识别手势，直到所有的手势识别成功。当顺序识别组合手势中有一个手势识别失败时，后续手势识别均失败。顺序识别手势中仅有最后一个手势可以响应[onActionEnd](../harmonyos-references/ts-gesturehandler.md#onactionend)。

以一个由长按手势和滑动手势组合而成的顺序识别手势为例：

在一个Column组件上绑定了[translate](../harmonyos-references/ts-universal-attributes-transformation.md#translate)属性，通过修改该属性可以设置组件的位置移动。然后在该组件上绑定[LongPressGesture](../harmonyos-references/ts-basic-gestures-longpressgesture.md)和[PanGesture](../harmonyos-references/ts-basic-gestures-pangesture.md)组合而成的Sequence组合手势。当触发LongPressGesture时，更新显示的数字。当长按后进行拖动时，根据滑动手势的回调函数，实现组件的拖动。

```
1. // xxx.ets
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0001;
5. const TAG = 'Sample_gesturegroup';

7. @Entry
8. @Component
9. struct sequenceIdentification {
10. @State offsetX: number = 0;
11. @State offsetY: number = 0;
12. @State count: number = 0;
13. @State positionX: number = 0;
14. @State positionY: number = 0;
15. @State borderStyles: BorderStyle = BorderStyle.Solid;

17. build() {
18. Column() {
19. Text('sequence gesture\n' + 'LongPress onAction:' + this.count + '\nPanGesture offset:\nX: ' + this.offsetX +
20. '\n' + 'Y: ' + this.offsetY)
21. .fontSize(28)
22. }
23. .margin(10)
24. .borderWidth(1)
25. // 绑定translate属性可以实现组件的位置移动
26. .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
27. .height(250)
28. .width(300)
29. // 以下组合手势为顺序识别，当长按手势事件未正常触发时不会触发滑动手势事件
30. .gesture(
31. // 声明该组合手势的类型为Sequence类型
32. GestureGroup(GestureMode.Sequence,
33. // 该组合手势第一个触发的手势为长按手势，且长按手势可多次响应
34. LongPressGesture({ repeat: true })
35. // 当长按手势识别成功，增加Text组件上显示的count次数
36. .onAction((event: GestureEvent | undefined) => {
37. if (event) {
38. if (event.repeat) {
39. this.count++;
40. }
41. ;
42. }
43. ;
44. hilog.info(DOMAIN, TAG, 'LongPress onAction');
45. })
46. .onActionEnd(() => {
47. hilog.info(DOMAIN, TAG, 'LongPress end');
48. }),
49. // 当长按之后进行拖动，PanGesture手势被触发
50. PanGesture()
51. .onActionStart(() => {
52. this.borderStyles = BorderStyle.Dashed;
53. hilog.info(DOMAIN, TAG, 'pan start');
54. })
55. // 当该手势被触发时，根据回调获得拖动的距离，修改该组件的位移距离从而实现组件的移动
56. .onActionUpdate((event: GestureEvent | undefined) => {
57. if (event) {
58. this.offsetX = (this.positionX + event.offsetX);
59. this.offsetY = this.positionY + event.offsetY;
60. }
61. ;
62. hilog.info(DOMAIN, TAG, 'pan update');
63. })
64. .onActionEnd(() => {
65. this.positionX = this.offsetX;
66. this.positionY = this.offsetY;
67. this.borderStyles = BorderStyle.Solid;
68. })
69. )
70. .onCancel(() => {
71. hilog.info(DOMAIN, TAG, 'sequence gesture canceled');
72. })
73. )
74. }
75. }
```

[Sequence.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureGroup/entry/src/main/ets/pages/Sequence.ets#L15-L91)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/ZVhjhhF9Re6WNE4MHWctdA/zh-cn_image_0000002583438005.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=13BD284AA28BCD11EF1107560BC338AAFFF27CDF0420863AB19C02D63CB95619)

说明

拖拽事件是一种典型的顺序识别组合手势事件，由长按手势事件和滑动手势事件组合而成。只有先长按达到长按手势事件预设置的时间后进行滑动才会触发拖拽事件。如果长按事件未达到或者长按后未进行滑动，拖拽事件均识别失败。

## 并行识别

并行识别组合手势对应的GestureMode为Parallel。并行识别组合手势中注册的手势将同时进行识别，直到所有手势识别结束。并行识别手势组合中的手势进行识别时互不影响。

以在一个Column组件上绑定点击手势和双击手势组成的并行识别手势为例，由于单击手势和双击手势是并行识别，因此两个手势可以同时进行识别，二者互不干涉。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct parallelRecognition {
5. @State count1: number = 0;
6. @State count2: number = 0;

8. build() {
9. Column() {
10. Text('Parallel gesture\n' + 'tapGesture count is 1:' + this.count1 + '\ntapGesture count is 2:' + this.count2 +
11. '\n')
12. .fontSize(28);
13. }
14. .height(200)
15. .width('100%')
16. // 以下组合手势为并行识别，单击手势识别成功后，若在规定时间内再次点击，双击手势也会识别成功
17. .gesture(
18. GestureGroup(GestureMode.Parallel,
19. TapGesture({ count: 1 })
20. .onAction(() => {
21. this.count1++;
22. }),
23. TapGesture({ count: 2 })
24. .onAction(() => {
25. this.count2++;
26. })
27. )
28. )
29. }
30. }
```

[Parallel.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureGroup/entry/src/main/ets/pages/Parallel.ets#L16-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/E7oO98f6SmKt1o6oOF8RLA/zh-cn_image_0000002552957960.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=E33851CC4982E668DFA10958C5EC8958AB8A9D54155AB31F88F0351AC8932D70)

说明

* 当由单击手势和双击手势组成一个并行识别组合手势后，在区域内进行点击时，单击手势和双击手势将同时进行识别。
* 当只有单次点击时，单击手势识别成功，双击手势识别失败。
* 当有两次点击时，若两次点击相距时间在规定时间内（默认规定时间为300毫秒），触发两次单击事件和一次双击事件。
* 当有两次点击时，若两次点击相距时间超出规定时间，触发两次单击事件不触发双击事件。

## 互斥识别

互斥识别组合手势对应的GestureMode为Exclusive。互斥识别组合手势中注册的手势将同时进行识别，若有一个手势识别成功，则结束手势识别，其他所有手势识别失败。

以在一个Column组件上绑定单击手势和双击手势组合而成的互斥识别组合手势为例。若先绑定单击手势后绑定双击手势，由于单击手势只需要一次点击即可触发而双击手势需要两次，每次的点击事件均被单击手势消费而不能积累成双击手势，所以双击手势无法触发。若先绑定双击手势后绑定单击手势，则触发双击手势不触发单击手势。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct MutualExclusion {
5. @State count1: number = 0;
6. @State count2: number = 0;

8. build() {
9. Column() {
10. Text('Exclusive gesture\n' + 'tapGesture count is 1:' + this.count1 + '\ntapGesture count is 2:' + this.count2 +
11. '\n')
12. .fontSize(28)
13. }
14. .height(200)
15. .width('100%')
16. // 以下组合手势为互斥识别，单击手势识别成功后，双击手势会识别失败
17. .gesture(
18. GestureGroup(GestureMode.Exclusive,
19. TapGesture({ count: 1 })
20. .onAction(() => {
21. this.count1++;
22. }),
23. TapGesture({ count: 2 })
24. .onAction(() => {
25. this.count2++;
26. })
27. )
28. )
29. }
30. }
```

[Exclusive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureGroup/entry/src/main/ets/pages/Exclusive.ets#L16-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/NP-24REZRL-SU8hYuf_4Vg/zh-cn_image_0000002583477961.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=772AA1A59462F1CE3F13CAE66874B8D7A3D73876EE195F6A9AE7A8DD2710A550)

说明

* 当由单击手势和双击手势组成一个互斥识别组合手势后，在区域内进行点击时，单击手势和双击手势将同时进行识别。
* 当只有单次点击时，单击手势识别成功，双击手势识别失败。
* 当有两次点击时，手势响应取决于绑定手势的顺序。若先绑定单击手势后绑定双击手势，单击手势在第一次点击时即宣告识别成功，此时双击手势已经失败。即使在规定时间内进行了第二次点击，双击手势事件也不会进行响应，此时会触发单击手势事件的第二次识别成功。若先绑定双击手势后绑定单击手势，则会响应双击手势而不响应单击手势。

## 场景示例

以下示例实现了子组件绑定长按和滑动手势，长按手势和滑动手势可以同时触发，但是在长按手势未成功时，需要让父组件Swiper的内置滑动手势触发功能。由于子组件的滑动手势和父组件的内置滑动手势是竞争关系，且子组件的滑动手势的优先级更高，因此需要通过动态控制子组件的滑动手势是否触发。

```
1. // xxx.ets
2. import { PromptAction } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct CombinedGestureDemo {
7. @State isLongPress: boolean = false;
8. promptAction: PromptAction = this.getUIContext().getPromptAction();

10. build() {
11. Swiper() {
12. // 页面1
13. Row()
14. .width('100%')
15. .height('100%')
16. .backgroundColor(Color.Grey)
17. .borderRadius(12)
18. // 通过自定义手势判定回调，判断在长按手势未成功时，拒绝子组件的滑动手势，从而让父组件Swiper的滑动手势成功
19. .onGestureRecognizerJudgeBegin(
20. (event: BaseGestureEvent, current: GestureRecognizer, others: Array<GestureRecognizer>) => {
21. if (current.getType() !== GestureControl.GestureType.PAN_GESTURE) {
22. return GestureJudgeResult.CONTINUE;
23. }
24. ;
25. if (this.isLongPress) {
26. return GestureJudgeResult.CONTINUE;
27. }
28. ;
29. return GestureJudgeResult.REJECT;
30. })
31. .gesture(
32. // 绑定并行手势组，实现长按手势和滑动手势可以同时触发
33. GestureGroup(GestureMode.Parallel,
34. LongPressGesture()
35. .onAction(() => {
36. this.isLongPress = true;
37. this.promptAction.showToast({ message: 'LongPress trigger' });
38. })
39. .onActionEnd(() => {
40. this.isLongPress = false;
41. })
42. ,
43. PanGesture()
44. .onActionStart(() => {
45. this.promptAction.showToast({ message: 'child pan start' });
46. })
47. )
48. )
49. // 页面2
50. Row()
51. .width('100%')
52. .height('100%')
53. .backgroundColor(Color.Pink)
54. .borderRadius(12)
55. }
56. .borderWidth(2)
57. .width('100%')
58. .height(300)
59. .padding(20)
60. }
61. }
```

[SceneExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureGroup/entry/src/main/ets/pages/SceneExample.ets#L16-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/o1UDTd90TtaKkPS-pkjc7Q/zh-cn_image_0000002552798312.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=84EF15043AA736F8A5EB261FBAC99855F2A396CEAA5067681A74B30A9E6A06E7)
