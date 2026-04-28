---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-372
title: 如何设置customspan不同位置的点击事件
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置customspan不同位置的点击事件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:61dfa832875647fe0264924cef45962b6f59c144865572f5ff03d0d12479eef5
---

CustomSpan 是最小单位的组件。若需实现特定功能，建议在多个 CustomSpan 上分别进行。如果必须在同一 CustomSpan 上实现，可从点击事件回调的 ClickEvent 中，根据属性判断实际点击位置，从而做出差异化响应。示例代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. controller: RichEditorController = new RichEditorController();
5. option: RichEditorOptions = { controller: this.controller };

7. @Builder
8. comment() {
9. Row() {
10. Text() {
11. Span('123123123')
12. ImageSpan($r('app.media.startIcon')).width(20).height(20)
13. Span('ggggggggggggggggggggggxxxxxxxxxxxxxxxxxxxxxxx')
14. }
15. .maxLines(1)
16. .wordBreak(WordBreak.BREAK_ALL)
17. .textOverflow({ overflow: TextOverflow.Ellipsis })
18. .constraintSize({
19. maxWidth: '90%'
20. })

22. Image($r('app.media.startIcon'))
23. .width(25)
24. .height(25)
25. .onClick(() => {
26. this.getUIContext().getPromptAction().showToast({
27. message: 'Click to delete'
28. })
29. })
30. }
31. .width('100%')
32. .align(Alignment.Center)
33. .padding({
34. top: 5,
35. bottom: 5
36. })
37. .borderRadius(20)
38. .backgroundColor(Color.Gray)
39. }

41. build() {
42. Column() {
43. Column() {
44. RichEditor(this.option)
45. .onReady(() => {
46. this.controller.addBuilderSpan(() => this.comment())
47. })
48. .borderWidth(1)
49. .borderColor(Color.Green)
50. .width('100%')
51. .height('30%')
52. }
53. .borderWidth(1)
54. .borderColor(Color.Red)
55. .width('100%')
56. .height('70%')
57. }
58. }
59. }
```

[SetClickEventInCustomspan.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetClickEventInCustomspan.ets#L21-L79)
