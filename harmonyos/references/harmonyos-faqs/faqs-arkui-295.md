---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-295
title: Scroll中嵌套List，可否设置事件响应顺序，让List不响应滚动事件，让外层的Scroll滚动整个布局
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Scroll中嵌套List，可否设置事件响应顺序，让List不响应滚动事件，让外层的Scroll滚动整个布局
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f757769057fd38e644775ea891b9cb925c4d8c14211809b859386e548c2f0e55
---

Scroll嵌套List的时候，如果List默认不设置高度是会默认全部展开的，可以实现Scroll滚动整个布局的效果，但是要注意这样会失去懒加载效果，推荐使用List组件的nestedScroll属性来实现嵌套滚动效果。

示例代码如下：

```
1. @Component
2. export struct ScrollNestingList {
3. build() {
4. Scroll() {
5. Column() {
6. Text('This is the title')
7. .fontSize(50)
8. .fontWeight(FontWeight.Bold)
9. List() {
10. ForEach(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], (item: string) => {
11. ListItem() {
12. Text(item)
13. .fontSize(50)
14. .height(150)
15. }
16. }, (item: string) => item)
17. }
18. .nestedScroll({
19. scrollForward: NestedScrollMode.PARENT_FIRST, // Triggering the parent scroll first when scrolling down
20. scrollBackward: NestedScrollMode.SELF_FIRST  // When scrolling up, the current List is triggered first
21. })
22. .divider({
23. strokeWidth: 1,
24. color: Color.Gray
25. })
26. .edgeEffect(EdgeEffect.None)
27. .height('100%')
28. .width('100%')
29. }
30. }
31. .width('100%')
32. .height('100%')
33. }
34. }
```

[TheOuterScrollScrollsTheEntireLayout.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TheOuterScrollScrollsTheEntireLayout.ets#L21-L54)
