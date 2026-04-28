---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-117
title: 文本组件是否支持分段设置字体样式
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 文本组件是否支持分段设置字体样式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5b935615655643c7edad419b9b53940846b1f738772a3f7d98e131a10f31f876
---

单个组件只能设置一种字体样式，可以通过多个Span子组件实现一行文本展示不同样式。参考代码如下：

```
1. @Entry
2. @Component
3. struct TestDemoPage {
4. @State message: string = "Hello World";

6. build() {
7. Row() {
8. Column() {
9. Text() {
10. // Using the Span subcomponent to implement segmented style settings
11. Span('test text: ')
12. .fontSize(20)
13. .fontWeight(FontWeight.Bolder)
14. .fontColor(Color.Black)
15. Span(this.message)
16. .fontSize(15)
17. .fontColor(Color.Red)
18. }
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

[SegmentedFontStyleSetting.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SegmentedFontStyleSetting.ets#L21-L44)

**参考链接**

[Text](../harmonyos-references/ts-basic-components-text.md)
