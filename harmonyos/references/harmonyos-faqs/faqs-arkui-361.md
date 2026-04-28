---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-361
title: Button组件无法设置字体最大、最小值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Button组件无法设置字体最大、最小值
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:32+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d5586611c667674b6490bbbca7571d4bce03a664709ae604ebb516ae2d4a8da9
---

Button组件的[labelStyle](../harmonyos-references/ts-basic-components-button.md#labelstyle10)属性可以设置按钮标签文本和字体的样式。示例代码如下

```
1. @Entry
2. @Component
3. struct FontSizeButtonExample {
4. @State text: string = 'hello';
5. @State widthShortSize: number = 300;

8. build() {
9. Row() {
10. Button(this.text)
11. .width(this.widthShortSize)
12. .height(100)
13. //// Set the font size range to 20-40vp，Automatically adjust during actual rendering.
14. .labelStyle({
15. overflow: TextOverflow.Clip,
16. maxLines: 1,
17. minFontSize: 20,
18. maxFontSize: 40,
19. font: {
20. size: 30,
21. weight: FontWeight.Bolder,
22. family: 'cursive',
23. style: FontStyle.Italic
24. }
25. })
26. }
27. }
28. }
```

[ButtonCannotSetFont.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ButtonCannotSetFont.ets#L21-L48)

**参考链接**

[Button](../harmonyos-references/ts-basic-components-button.md)
