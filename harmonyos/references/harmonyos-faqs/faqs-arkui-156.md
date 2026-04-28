---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-156
title: Text组件设置maxLines后如何确定文本是否被隐藏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Text组件设置maxLines后如何确定文本是否被隐藏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1832c1f5e8a34f57ef3beabfeec829165a8f80d20ed3b11c74e7e3db065ee000
---

可以通过measureTextSize来判断Text文本的高度是否超出maxLines设置的高度进行判断。参考代码如下：

```
1. @Entry
2. @Component
3. struct TextInputExample {
4. @State text: string = '';
5. @State truncatedHint: string = "Text not truncated";
6. controller: TextInputController = new TextInputController();

8. build() {
9. Column() {
10. TextInput({ text: this.text, placeholder: 'input your word...', controller: this.controller })
11. .placeholderColor(Color.Grey)
12. .placeholderFont({ size: 14, weight: 400 })
13. .caretColor(Color.Blue)
14. .width(400)
15. .height(40)
16. .margin(20)
17. .fontSize(14)
18. .fontColor(Color.Black)
19. .onChange((value: string) => {
20. this.text = value;
21. let textSizeShow1: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
22. textContent: this.text,
23. constraintWidth: 100,
24. fontSize: 14,
25. overflow: TextOverflow.Ellipsis,
26. maxLines: 2
27. })
28. let textSizeShow2: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
29. textContent: this.text + " ",
30. constraintWidth: 100,
31. fontSize: 14,
32. overflow: TextOverflow.Ellipsis,
33. maxLines: 2000000
34. })
35. console.log("textSizeShow1.height=" + textSizeShow1.height);
36. console.log("textSizeShow2.height=" + textSizeShow2.height);

38. if (textSizeShow2 && textSizeShow1 && textSizeShow2?.height && textSizeShow1?.height && (textSizeShow2?.height > textSizeShow1?.height)) {
39. console.log("Text truncated");
40. this.truncatedHint = "Text truncated";
41. } else {
42. console.log("Text not truncated");
43. this.truncatedHint = "Text not truncated";
44. }
45. })
46. Text(this.text)
47. .maxLines(2)
48. .width(100)
49. .textOverflow({ overflow: TextOverflow.Ellipsis })
50. .border({ width: 1 })
51. .minFontSize(14)
52. .maxFontSize(24)
53. Text(this.truncatedHint)

55. }.width('100%')
56. }
57. }
```

[TextSetMaxlinesIsHideText.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TextSetMaxlinesIsHideText.ets#L21-L77)

**参考链接**

[measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)
