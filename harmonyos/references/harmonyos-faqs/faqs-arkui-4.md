---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-4
title: 如何在长按手势回调方法里获取手指触摸点的坐标
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在长按手势回调方法里获取手指触摸点的坐标
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:00+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:f4577a41e0a6dc872c313f3fea2da897450a6db8c60965ad0b17cbc83d9c6966
---

使用[组合手势](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)的顺序识别，当长按手势事件结束后触发拖动手势事件。在手势回调方法里获取event（[GestureEvent](../harmonyos-references/ts-gesture-common.md#gestureevent对象说明)类型）的fingerList（[FingerInfo[]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-gesture-common#fingerinfo8对象说明)类型），获取到localX和localY数值，表示相对于当前组件元素原始区域左上角的坐标位置。可参考如下代码：

```
1. @Component
2. struct CoordinatesOfTheFingerTouchPoint {
3. @State count: number = 0;
4. private touchAreaRight: number = 0;
5. private touchAreaBottom: number = 0;
6. @State positionX: number = 0;
7. @State positionY: number = 0;
8. @State gestureEventInfo: string = '';

10. build() {
11. Column() {
12. Row() {
13. Column() {
14. Text('+')
15. .fontSize(28)
16. .position({ x: this.positionX, y: this.positionY })
17. }
18. .height(200)
19. .width('100%')
20. .backgroundColor('#F1F3F5')
21. .onAreaChange((oldValue: Area, newValue: Area) => {
22. this.touchAreaRight = newValue.width as number;
23. this.touchAreaBottom = newValue.height as number;
24. })
25. .gesture(
26. // The following combined gestures are recognized sequentially. If the long press gesture event is not triggered normally, the drag gesture event will not be triggered.
27. GestureGroup(GestureMode.Sequence,
28. LongPressGesture({ repeat: true })
29. .onAction((event: GestureEvent) => {
30. if (event.repeat) {
31. this.count++;
32. }
33. }),
34. PanGesture()
35. .onActionStart(() => {
36. this.getUIContext().getPromptAction().showToast({ message: 'Pan start', duration: 1000 });
37. })
38. .onActionUpdate((event: GestureEvent) => {
39. for (let i = 0; i < event.fingerList.length; i++) {
40. if (event.fingerList[i] == undefined
41. || event.fingerList[i].localX < 0
42. || event.fingerList[i].localY < 0
43. || event.fingerList[i].localX > this.touchAreaRight
44. || event.fingerList[i].localY > this.touchAreaBottom) {
45. return;
46. }
47. this.positionX = event.fingerList[i].localX;
48. this.positionY = event.fingerList[i].localY;
49. }
50. this.gestureEventInfo = 'sequence gesture\n' + 'LongPress onAction' + this.count
51. + '\nX:' + this.positionX + '\nY:' + this.positionY;
52. })
53. .onActionEnd(() => {
54. this.getUIContext().getPromptAction().showToast({ message: 'Pan end', duration: 1000 });
55. })
56. )
57. .onCancel(() => {
58. this.getUIContext().getPromptAction().showToast({ message: 'Cancel', duration: 1000 });
59. })
60. )
61. }
62. .padding(12)
63. .borderRadius(24)
64. .backgroundColor(Color.White)

66. Text(this.gestureEventInfo)
67. .fontSize(18)
68. .width('100%')
69. .textAlign(TextAlign.Start)
70. .padding({ left: 18, top: 30 })
71. }
72. .height('100%')
73. .width('100%')
74. .backgroundColor('#F1F3F5')
75. }
76. }
```

[GetCoordinatesFromTouchPoint.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetCoordinatesFromTouchPoint.ets#L21-L96)
