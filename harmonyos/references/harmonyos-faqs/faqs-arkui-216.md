---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-216
title: 如何使用iconfont
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何使用iconfont
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:57+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ad4fa19be4e839b2636eca977e720c8cf358741a24cc19e462838d30c373914c
---

使用iconfont时，开发者需先获取字体库的ttf文件，再通过 `font.registerFont` 接口注册。在 `Text` 上使用对应的 unicode 编码即可。参考代码如下：

```
1. import { Font } from '@kit.ArkUI'
2. @Entry
3. @Component
4. struct UseIconFont {
5. // Assuming 0000 is the Unicode for the specified icon, developers actually need to obtain Unicode from the ttf file of the registered iconFont
6. @State unicode: string = '\u0000';
7. aboutToAppear(): void {
8. let font: Font = this.getUIContext().getFont();
9. font.registerFont({
10. familyName: 'iconfont',
11. familySrc: 'xxx.ttf'
12. })
13. }
14. build() {
15. Row() {
16. Column() {
17. Text(this.unicode)
18. .fontSize(50)
19. .fontWeight(FontWeight.Bold)
20. .fontFamily('iconfont')
21. }
22. .width('100%')
23. }
24. .height('100%')
25. }
26. }
```

[UsingIconfont.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/UsingIconfont.ets#L21-L46)

**参考链接**

[registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)
