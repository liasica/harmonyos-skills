---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-485
title: 如何判断组件遮挡情况，并主动隐藏被遮挡的组件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何判断组件遮挡情况，并主动隐藏被遮挡的组件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:10ad1f296c545b461680222e92ef39823570fddb43cedf2f282073d9b361b9bb
---

一般情况下，使用[onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)即可。 在一些特殊场景下，例如使用了层叠布局，或者在线性布局中使用位置使得并排的兄弟组件之间产生了遮挡，由于onVisibleAreaChange的局限性，此种情况需要自己手动计算遮挡关系。推荐使用[UIInspector](../harmonyos-references/arkts-apis-uicontext-uiinspector.md)注册监听回调、[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)的getPositionToWindowWithTransform、getMeasuredSize获取组件的位置和宽高信息。

场景1：页面的元素遮挡关系后续不再发生变化，可以在页面布局时判断遮挡关系，可以监听UIInspector的layout回调，避免频繁回调消耗性能。

```
1. import { inspector, UIInspector } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ComponentHide {
6. uiInspector: UIInspector = this.getUIContext().getUIInspector();
7. listener: inspector.ComponentObserver = this.uiInspector.createComponentObserver('inspectTarget');
8. @State x: number = 170;
9. @State button1Visibility: Visibility = Visibility.Visible;

11. aboutToAppear(): void {
12. let shouldShow: () => void = (): void => {
13. let button1Info = this.getUIContext().getFrameNodeById('button1')?.getPositionToWindowWithTransform(); // vp
14. let button1Size = this.getUIContext().getFrameNodeById('button1')?.getMeasuredSize(); // px
15. let button1TopLeftX = this.getUIContext().vp2px(button1Info?.x); // The x-coordinate of the upper left corner of button1, with the unit of px
16. let button1TopLeftY = this.getUIContext().vp2px(button1Info?.y); // The y-coordinate of the upper left corner of button1, with the unit of px
17. let button1BottomRightX = button1TopLeftX + (button1Size?.width ?? 0); // The x-coordinate at the lower right corner of button1, with the unit of px
18. let button1BottomRightY = button1TopLeftY + (button1Size?.height ?? 0); // The y-coordinate of the lower right corner of button1, with the unit of px

20. let button2Info = this.getUIContext().getFrameNodeById('button2')?.getPositionToWindowWithTransform(); // vp
21. let button2Size = this.getUIContext().getFrameNodeById('button2')?.getMeasuredSize(); // px
22. let button2TopLeftX = this.getUIContext().vp2px(button2Info?.x); // The x-coordinate of the upper left corner of button2, with the unit of px
23. let button2TopLeftY = this.getUIContext().vp2px(button2Info?.y); // The y-coordinate of the upper left corner of button2, with the unit of px
24. let button2BottomRightX = button2TopLeftX + (button2Size?.width ?? 0); // The x-coordinate at the lower right corner of button2, with the unit being px
25. let button2BottomRightY = button2TopLeftY + (button2Size?.height ?? 0); // The y-coordinate of the lower right corner of button2, with the unit of px

27. let xOverlap = (button1TopLeftX < button2BottomRightX) && (button2TopLeftX < button1BottomRightX);
28. let yOverlap = (button1TopLeftY < button2BottomRightY) && (button2TopLeftY < button1BottomRightY);
29. if (xOverlap && yOverlap) {
30. this.button1Visibility = Visibility.Hidden;
31. } else {
32. this.button1Visibility = Visibility.Visible;
33. }
34. this.listener.on('layout', shouldShow);
35. }
36. }

38. build() {
39. Column() {
40. Column() {
41. Button('button1')
42. .position({ x: 200, y: 200 })
43. .id('button1')
44. .visibility(this.button1Visibility)
45. }

47. Column() {
48. Button('button2')
49. .position({ x: this.x, y: 200 })
50. .onClick(() => {
51. this.x = 200 - this.x; // If the component position changes, the layout will not be reconfigured and the registered shouldShow callback will not be called
52. })
53. .id('button2')
54. }
55. }
56. .id('inspectTarget')
57. }
58. }
```

[ComponentOcclusionSceneOne.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentOcclusionSceneOne.ets#L21-L79)

场景2：页面的元素遮挡关系后续会发生变化，可以在页面绘制时判断遮挡关系，可以监听UIInspector的draw回调，会频繁回调。

```
1. import { inspector, UIInspector } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct ComponentHide {
6. uiInspector: UIInspector = this.getUIContext().getUIInspector();
7. listener: inspector.ComponentObserver = this.uiInspector.createComponentObserver('button2');
8. @State x: number = 170;
9. @State button1Visibility: Visibility = Visibility.Visible;

11. aboutToAppear(): void {
12. let shouldShow: () => void = (): void => {
13. let button1Info = this.getUIContext().getFrameNodeById('button1')?.getPositionToWindowWithTransform(); // vp
14. let button1Size = this.getUIContext().getFrameNodeById('button1')?.getMeasuredSize(); // px
15. let button1TopLeftX = this.getUIContext().vp2px(button1Info?.x); // The x-coordinate of the upper left corner of button1, with the unit of px
16. let button1TopLeftY = this.getUIContext().vp2px(button1Info?.y); // The y-coordinate of the upper left corner of button1, with the unit of px
17. let button1BottomRightX = button1TopLeftX + (button1Size?.width ?? 0); // The x-coordinate at the lower right corner of button1, with the unit of px
18. let button1BottomRightY = button1TopLeftY + (button1Size?.height ?? 0); // The y-coordinate of the lower right corner of button1, with the unit of px

20. let button2Info = this.getUIContext().getFrameNodeById('button2')?.getPositionToWindowWithTransform(); // vp
21. let button2Size = this.getUIContext().getFrameNodeById('button2')?.getMeasuredSize(); // px
22. let button2TopLeftX = this.getUIContext().vp2px(button2Info?.x); // The x-coordinate of the upper left corner of button2, with the unit of px
23. let button2TopLeftY = this.getUIContext().vp2px(button2Info?.y); // The y-coordinate of the upper left corner of button2, with the unit of px
24. let button2BottomRightX = button2TopLeftX + (button2Size?.width ?? 0); // The x-coordinate at the lower right corner of button2, with the unit being px
25. let button2BottomRightY = button2TopLeftY + (button2Size?.height ?? 0); // The y-coordinate of the lower right corner of button2, with the unit of px

27. let xOverlap = (button1TopLeftX < button2BottomRightX) && (button2TopLeftX < button1BottomRightX);
28. let yOverlap = (button1TopLeftY < button2BottomRightY) && (button2TopLeftY < button1BottomRightY);
29. if (xOverlap && yOverlap) {
30. this.button1Visibility = Visibility.Hidden;
31. } else {
32. this.button1Visibility = Visibility.Visible;
33. }
34. this.listener.on('draw', shouldShow); // The listener callbacks after the drawing is completed, with frequent calls, poor performance and high universality
35. }
36. }

38. build() {
39. Column() {
40. Column() {
41. Button('button1')
42. .position({ x: 200, y: 200 })
43. .id('button1')
44. .visibility(this.button1Visibility)
45. }

47. Column() {
48. Button('button2')
49. .position({ x: this.x, y: 200 })
50. .onClick(() => {
51. this.x = 200 - this.x; // If the component position changes, the layout will not be reconfigured and the registered shouldShow callback will not be called
52. })
53. .id('button2')
54. }
55. }
56. .id('inspectTarget')
57. }
58. }
```

[ComponentOcclusionSceneTwo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentOcclusionSceneTwo.ets#L21-L79)
