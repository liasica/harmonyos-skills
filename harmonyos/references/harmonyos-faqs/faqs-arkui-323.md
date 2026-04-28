---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-323
title: 如何在Text组件关闭bindSelection自定义菜单时，取消文本的选中状态
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在Text组件关闭bindSelection自定义菜单时，取消文本的选中状态
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b0add7ce3043e5d4029f0dba94dda2ed4e6053600b7be63943827be9ff039882
---

**问题现象**

当Text组件通过bindSelectionMenu绑定自定义菜单时，长按操作会弹出菜单，但调用closeSelectionMenu关闭菜单后，文本选中状态仍会保持。

**解决措施**

在该场景下，取消选中状态可通过重新设置selection来实现。调用closeSelectionMenu关闭自定义菜单时，在onDisappear回调中重新设置selection的start和end即可取消选中状态。示例代码如下：

```
1. @Entry
2. @Component
3. struct TextMenuUnchecked {
4. controller: TextController = new TextController();
5. options: TextOptions = { controller: this.controller };
6. @State start: number = -1; // Unchecked state
7. @State end: number = -1;

9. build() {
10. Column() {
11. Column() {
12. Text(undefined, this.options) {
13. Span('Hello World')
14. ImageSpan($r('app.media.app_icon'))
15. .width(50)
16. .height(50)
17. .objectFit(ImageFit.Fill)
18. .verticalAlign(ImageSpanAlignment.CENTER)
19. }
20. .selection(this.start, this.end)
21. .copyOption(CopyOptions.InApp)
22. // Long press to bring up a custom menu
23. .bindSelectionMenu(TextSpanType.TEXT, this.buildCustomSelectionMenu, TextResponseType.LONG_PRESS, {
24. onDisappear: () => {
25. console.info(`Custom selection menu callback when closed`);
26. },
27. onAppear: () => {
28. console.info(`Callback when custom selection menu pops up`);
29. }
30. })
31. // When the selected area changes, trigger a callback to update the starting and ending subscripts of the selected area
32. .onTextSelectionChange((selectionStart: number, selectionEnd: number) => {
33. this.start = selectionStart;
34. this.end = selectionEnd;
35. console.info(`Text selection area change callback, selectionStart: ${selectionStart}, selectionEnd: ${selectionEnd}`);
36. })
37. .borderWidth(1)
38. .borderColor(Color.Red)
39. .width(200)
40. .height(100)
41. }
42. .width('100%')
43. .backgroundColor(Color.White)
44. .alignItems(HorizontalAlign.Start)
45. .padding(25)
46. }
47. .height('100%')
48. }

50. @Builder
51. buildCustomSelectionMenu() {
52. Column() {
53. Menu() {
54. MenuItemGroup() {
55. MenuItem({
56. startIcon: $r('app.media.app_icon'),
57. content: 'Right Click Menu 1',
58. labelInfo: ''
59. })
60. .onClick(() => { //When clicking on the custom menu, reset the starting and ending subscripts of the selected area
61. this.start = -1;
62. this.end = -1;
63. try {
64. this.controller.closeSelectionMenu();
65. } catch (error) {
66. let err = error as BusinessError;
67. hilog.error(0x000, 'TextMenuUnchecked', `err code:${err.code},message${err.message}.`);
68. }
69. })
70. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'Select Mixed Menu 2', labelInfo: '' })
71. MenuItem({ startIcon: $r('app.media.app_icon'), content: 'Select Mixed Menu 3', labelInfo: '' })
72. }
73. }
74. .radius($r('sys.float.ohos_id_corner_radius_card'))
75. .clip(true)
76. .backgroundColor('#F0F0F0')
77. }
78. }
79. }
```

[UncheckTheSelectedStatusOfTheText.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/UncheckTheSelectedStatusOfTheText.ets#L23-L102)
