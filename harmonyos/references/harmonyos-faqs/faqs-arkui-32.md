---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-32
title: 如何解决子组件全屏后margin不会生效的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何解决子组件全屏后margin不会生效的问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d48543468b19058f3ea02235a866af4804fd3e1a8575db25e6710a59d64ac81c
---

父组件全屏显示，子组件默认撑满。设置左右margin值后，子组件可能会超出屏幕范围。可以使用`constraintSize`属性限制子组件的最大宽高。参考代码如下：

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = 'Hello World';

6. build() {
7. Row() {
8. Column() {
9. Text(this.message)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. .textAlign(TextAlign.Center)
13. .width('100%')
14. .constraintSize({ maxWidth: '100%' })
15. .backgroundColor(Color.Blue)
16. .margin({ left: 50, right: 50 })
17. }
18. .width('100%')
19. }
20. .height('100%')
21. }
22. }
```

[ResolveFullScreenNonEffectiveness.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ResolveFullScreenNonEffectiveness.ets#L21-L42)

**参考链接**

[尺寸设置](../harmonyos-references/ts-universal-attributes-size.md)中的constraintSize
