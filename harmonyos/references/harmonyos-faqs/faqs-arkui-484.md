---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-484
title: 如何实现当长按触发成功后，移出组件取消当前长按手势
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现当长按触发成功后，移出组件取消当前长按手势
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:da32b40bcb2dc61bdfb7ae224356f86555f41109620a2c232e552410d61f0823
---

当前长按手势的规格为：触发成功后不会判断移动是否超出组件范围。如需实现该场景，可以结合onTouch判断手指位置是否在组件内自定义长按手势的业务逻辑是否执行。示例如下：

```
1. @Entry
2. @Component
3. struct CancelLongPressEventWhenRemovingComponents {
4. private recWidth: number = 200;
5. private recHeight: number = 100;
6. @State isLongPressing: boolean = false;
7. @State shouldCancel: boolean = false;
8. @State touchInBounds: boolean = true;

10. build() {
11. Column() {
12. // Touchable area.
13. Stack() {
14. Text(this.isLongPressing ? 'Long Pressing...' : 'Long press me')
15. .fontSize(20)
16. .fontColor(Color.White)
17. }
18. .width(this.recWidth)
19. .height(this.recHeight)
20. .backgroundColor(this.isLongPressing ? Color.Red : Color.Blue)
21. .gesture(
22. LongPressGesture({ repeat: false })
23. .onAction(() => {
24. if (!this.shouldCancel && this.touchInBounds) {
25. this.handleLongPressStart();
26. }
27. })
28. .onActionEnd(() => {
29. this.handleLongPressEnd();
30. })
31. )
32. .onTouch((event: TouchEvent) => {
33. this.handleTouchEvent(event);
34. })
35. .onClick(() => {
36. console.info('onClick');
37. })
38. .width(this.recWidth)
39. .height(this.recHeight)

41. }
42. .width('100%')
43. .height('100%')
44. .justifyContent(FlexAlign.Center)
45. .alignItems(HorizontalAlign.Center)
46. }

48. // Handling touch events.
49. private handleTouchEvent(event: TouchEvent) {
50. const touchX = event.touches[0].x;
51. const touchY = event.touches[0].y;
52. // Calculate whether the touch point is within the component boundary.
53. const inBounds = touchX >= 0 && touchX <= this.recWidth && touchY >= 0 && touchY <= this.recHeight;
54. switch (event.type) {
55. case TouchType.Down:
56. this.shouldCancel = false;
57. this.touchInBounds = true;
58. break;
59. case TouchType.Move:
60. // Update touch position status.
61. this.touchInBounds = inBounds;
62. // If moving out of the boundary and long pressing, cancel.
63. if (!inBounds && this.isLongPressing) {
64. this.shouldCancel = true;
65. this.isLongPressing = false;
66. console.info('LongPressCancel', 'Slide beyond the boundary, cancel long press.');
67. }
68. break;
69. case TouchType.Up:
70. this.shouldCancel = true;
71. this.touchInBounds = true;
72. break;
73. }
74. }

76. // Long press to start processing.
77. private handleLongPressStart() {
78. console.info('LongPress', 'Long press to start');
79. this.isLongPressing = true;
80. }

82. // Long press to end processing.
83. private handleLongPressEnd() {
84. console.info('LongPress', 'Long press to end');
85. this.isLongPressing = false;
86. this.shouldCancel = false;
87. }
88. }
```

[CancelLongPressEventWhenRemovingComponents.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CancelLongPressEventWhenRemovingComponents.ets#L21-L109)
