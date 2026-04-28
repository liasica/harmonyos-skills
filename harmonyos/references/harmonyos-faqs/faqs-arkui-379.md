---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-379
title: 如何模拟点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何模拟点击事件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d46d193ae4ea1c242c2dcb1cd3294aa0efa265f73e5749806394f772b557dcc5
---

模拟点击事件是指在程序中通过代码模拟触摸操作，模拟用户在界面上的点击行为，常用于自动化测试或绕过UI限制的场景。例如，使用onTouch触发按钮外区域的触摸事件，通过BuilderNode的方法传递touchEvent事件，从而实现模拟点击按钮的[TapGesture](../harmonyos-references/ts-basic-gestures-tapgesture.md)手势点击事件。

```
1. import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

3. class Params {
4. text: string = 'this is a text';
5. }

7. @Builder
8. function ButtonBuilder(params: Params) {
9. Column() {
10. Button(`button ` + params.text)
11. .backgroundColor(Color.Orange)
12. .width('100%')
13. .gesture(
14. TapGesture()
15. .onAction((event: GestureEvent) => {
16. console.info('TapGesture');
17. })
18. )
19. }
20. .width('100%')
21. .height(300)
22. .padding({
23. left: 16,
24. right: 16
25. })
26. .justifyContent(FlexAlign.Center)
27. .backgroundColor(Color.Gray)
28. }

30. class MyNodeController extends NodeController {
31. private rootNode: BuilderNode<[Params]> | null = null;
32. private wrapBuilder: WrappedBuilder<[Params]> = wrapBuilder(ButtonBuilder);

34. makeNode(uiContext: UIContext): FrameNode | null {
35. this.rootNode = new BuilderNode(uiContext);
36. this.rootNode.build(this.wrapBuilder, { text: 'this is a string' });
37. return this.rootNode.getFrameNode();
38. }

40. // Coordinate Conversion Example
41. postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
42. if (this.rootNode == null) {
43. return false;
44. }
45. let node: FrameNode | null = this.rootNode.getFrameNode();
46. if (node == null) {
47. return false;
48. }
49. let offsetX: number | null | undefined = node?.getPositionToParent().x;
50. let offsetY: number | null | undefined = node?.getPositionToParent().y;
51. let changedTouchLen = event.changedTouches.length;
52. for (let i = 0; i < changedTouchLen; i++) {
53. if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
54. event.changedTouches[i].x = uiContext.vp2px(offsetX + event.changedTouches[i].x);
55. event.changedTouches[i].y = uiContext.vp2px(offsetY + event.changedTouches[i].y);
56. }
57. }
58. let result = this.rootNode.postTouchEvent(event);
59. console.info('result:' + result);
60. return result;
61. }
62. }

64. @Entry
65. @Component
66. struct MyComponent {
67. private nodeController: MyNodeController = new MyNodeController();

69. build() {
70. Column() {
71. NodeContainer(this.nodeController)
72. .height(300)
73. .width('100%')

75. Column()
76. .width(500)
77. .height(300)
78. .backgroundColor('#0A59F7')
79. .onTouch((event) => {
80. if (event != undefined) {
81. let uiContext = this.getUIContext();
82. // Dispatch event events to the FrameNode created by the nodeController by touching them with fingers
83. this.nodeController.postTouchEvent(event, uiContext);
84. }
85. })
86. }
87. }
88. }
```

[MockOnclick.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MockOnclick.ets#L21-L108)
