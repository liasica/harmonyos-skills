---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-347
title: 如何解决Text组件文本为中文、数字、英文混合时显示省略号截断异常的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决Text组件文本为中文、数字、英文混合时显示省略号截断异常的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c19196f20fc165a0c5e62eefe464e26620812c8397d252a4d51158b36184185f
---

文本截断按语言单位进行：中文按字，英文默认按单词，若需按字母截断，可在字母间添加零宽空格：\u200B。

从API 11开始，建议优先使用将 wordBreak 属性设置为 WordBreak.BREAK\_ALL 的方式，以实现按字母截断。示例代码如下：

```
1. @Entry
2. @Component
3. struct TextEllipsisDemo {
4. @State text: string = '2 years · VIP membership for 3 months · 8GB · 230mm · Product color';

6. build() {
7. RelativeContainer() {
8. Text(this.text)
9. .width(200)// Set maximum number of rows
10. .maxLines(1)
11. .textOverflow({ overflow: TextOverflow.Ellipsis })// Long text display ellipsis
12. .ellipsisMode(EllipsisMode.END)// Set the line breaking rule WordBreak.BREAK_ALL and implement truncation on a letter by letter basis
13. .wordBreak(WordBreak.BREAK_ALL)// API11+ required, for letter-level truncation
14. .textAlign(TextAlign.JUSTIFY)
15. .backgroundColor(Color.Green)
16. .fontSize(16)
17. }
18. .height('100%')
19. .width('100%')
20. }
21. }
```

[ResolveTextTruncationException.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveTextTruncationException.ets#L21-L42)
