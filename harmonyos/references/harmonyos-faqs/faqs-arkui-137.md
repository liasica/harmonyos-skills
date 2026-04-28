---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-137
title: List组件如何设置两端的渐变效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > List组件如何设置两端的渐变效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8d8bda2a68b475b92804f3c2090ebc84e388c85ca7eb33072a7bbb046ea6753c
---

List组件本身不支持直接设置两端渐变效果，但可通过Stack布局结合LinearGradient对象实现效果。参考代码如下：

```
1. @Entry
2. @Component
3. struct ListExample {
4. @State arr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
5. private scroller: Scroller = new Scroller()

7. build() {
8. Stack() {
9. List({ space: 10 }) {
10. ForEach(this.arr, (item: string) => {
11. ListItem() {
12. Text("Hello World")
13. .width(100)
14. .height(64)
15. .fontColor(Color.White)
16. .backgroundColor(Color.Black)
17. .textAlign(TextAlign.Center)
18. }
19. }, (item: string) => item)
20. }
21. .listDirection(Axis.Horizontal)
22. .scrollBar(BarState.Off)
23. .padding({ top: 20, bottom: 20 })
24. .width("80%")
25. .height("100%")

27. Stack() {

29. }
30. .linearGradient({
31. angle: 90,
32. colors: [[0x000000, 0.0], ['rgba(0,0,0,0)', 0.1], ['rgba(0,0,0,0)', 0.9], [0x000000, 1.0]]
33. })
34. .width("80%")
35. .height("100%")
36. .hitTestBehavior(HitTestMode.None)
37. }.height(100).width('100%').backgroundColor(Color.Black)
38. }
39. }
```

[ListSettingGradientEffect.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ListSettingGradientEffect.ets#L21-L59)

**参考链接**

[颜色渐变](../harmonyos-references/ts-universal-attributes-gradient-color.md)
