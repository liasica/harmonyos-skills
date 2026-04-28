---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-54
title: 输入框拉起键盘时，如何将底部布局弹起到键盘顶部
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 输入框拉起键盘时，如何将底部布局弹起到键盘顶部
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8a609215ca1c7f53ddd0ba52dc2559645295c5c910187d08710abab9669de8ef
---

**原因分析**

软键盘弹出时，默认顶起输入框，下方的显示组件将被遮挡。

**解决措施**

获取窗口内容规避的区域，规避区域类型为软键盘区域（TYPE\_KEYBOARD）。当软键盘弹出时，获取规避区域的高度，并通过设置margin-bottom顶起组件。参考代码如下：

```
1. import { window } from '@kit.ArkUI';

3. @Entry
4. struct BottomPopsUpAsTheTopOfKeyboard {
5. context = this.getUIContext();
6. scroller: Scroller = new Scroller();
7. private arr: number[] = [0, 1, 2, 3, 4, 5];
8. @State scrollHeight: number = 0;
9. @State isRebuild: boolean = false;
10. @State keyHeight: number = 0;
11. @State text: string = '';
12. aboutToAppear() {
13. window.getLastWindow(this.context.getHostContext()).then(currentWindow => {
14. // Set the layout of the window to immersive layout
15. currentWindow.setWindowLayoutFullScreen(true);
16. let property = currentWindow.getWindowProperties();
17. // Initialize window height
18. let avoidArea = currentWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_KEYBOARD);
19. this.scrollHeight = this.getUIContext().px2vp(property.windowRect.height - avoidArea.bottomRect.height);
20. // Monitor the hiding and showing of the soft keyboard
21. currentWindow.on('avoidAreaChange', data => {
22. if (data.type == window.AvoidAreaType.TYPE_KEYBOARD) {
23. this.keyHeight = this.getUIContext().px2vp(data.area.bottomRect.height);
24. this.scrollHeight =
25. this.getUIContext().px2vp(currentWindow.getWindowProperties().windowRect.height - data.area.bottomRect.height);
26. return;
27. }
28. })
29. })
30. }
31. build() {
32. Stack({ alignContent: Alignment.TopStart }) {
33. Column() {
34. Scroll(this.scroller) {
35. Column() {
36. TextInput({ text: this.text, placeholder: 'input your word...' })
37. .placeholderFont({
38. size: 14,
39. weight: 400
40. })
41. .width(320)
42. .height(40)
43. .margin(200)
44. .fontSize(14)
45. .fontColor(Color.Black)
46. .backgroundColor(Color.White)
47. ForEach(this.arr, (item: number) => {
48. Text(item.toString())
49. .width('90%')
50. .height(150)
51. .backgroundColor(0xFFFFFF)
52. .borderRadius(15)
53. .fontSize(16)
54. .textAlign(TextAlign.Center)
55. .margin({ top: 10 })
56. })
57. }
58. .width('100%')
59. }
60. .width('100%')
61. .height(this.scrollHeight)
62. .layoutWeight(1)
63. Text('This is a test text')
64. .width('100%')
65. .height(50)
66. .backgroundColor(Color.Red)
67. .margin({ bottom: this.keyHeight })
68. }
69. .width('100%')
70. .height('100%')
71. .justifyContent(FlexAlign.Start)
72. }
73. .width('100%')
74. .height('100%')
75. .backgroundColor(0xDCDCDC)
76. }
77. }
```

[BottomPopsUpAsTheTopOfKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/BottomPopsUpAsTheTopOfKeyboard.ets#L21-L97)

**参考链接**

[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)
