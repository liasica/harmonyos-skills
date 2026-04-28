---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-399
title: Navigation自定义标题栏不生效，可能是什么原因
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Navigation自定义标题栏不生效，可能是什么原因
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:45+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2c0d331f3720e7985295620b1725cf990500d8ebc88ed29ffdfc1fa516ccb6b5
---

**问题描述**

使用Navigation时，自定义标题栏布局，使用其中的title方法无效。

**解决措施**

NavigationCustomTitle里builder传入方法需使用装饰器@LocalBuilder。由于是对象内部作用域，需要通过@LocalBuilder保证this始终指向自定义组件本身，@LocalBuilder装饰器用于确保builder方法在Navigation组件内部正确绑定this上下文，避免作用域丢失问题。示例代码如下：

```
1. @Entry
2. @Component
3. export struct MainPage {
4. myTitle: NavigationCustomTitle = {
5. builder: this.customTitleBuilder,
6. height: TitleHeight.MainOnly
7. };

9. @LocalBuilder
10. customTitleBuilder() {
11. Row() {
12. Text('Title1')
13. .fontSize(12)
14. .fontWeight(FontWeight.Bold)
15. .margin({ left: 7, right: 7, top: 7 })

17. Text('Title2')
18. .fontSize(12)
19. .fontWeight(FontWeight.Bold)
20. .margin({ left: 7, right: 7, top: 7 })

22. Text('Title3')
23. .fontSize(12)
24. .fontWeight(FontWeight.Bold)
25. .margin({ left: 7, right: 7, top: 7 })
26. }
27. }

29. build() {
30. Navigation() {
31. Column() {
32. Text('hello world')
33. .fontSize('24')
34. .fontWeight(FontWeight.Bold)
35. .fontFamily('HarmonyHeiTi-Bold')
36. .textAlign(TextAlign.Center)
37. .width('100%')
38. }
39. .height('100%')
40. .width('100%')
41. .background('#F1F3F5')
42. }
43. .title(this.myTitle)
44. }
45. }
```

[CustomTitleInNavigation.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CustomTitleInNavigation.ets#L21-L65)
