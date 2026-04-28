---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-371
title: 如何理解AspectRatio对布局的影响
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何理解AspectRatio对布局的影响
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d92dbff52613bf622d0785919798df37c7f6a51b73817568d925497d60819b4a
---

aspectRatio在布局中发挥两个主要作用：

* 第一个作用是和其他属性一起共同计算组件的约束以测量尺寸。
* 第二个作用是在组件测量完尺寸之后确保仍然遵守宽高比。

在布局过程中，父组件提供的约束由父组件的规格决定，子组件如何利用约束由子组件的规格决定。父组件给出约束后，aspectRatio和开发者设置的其他属性（如size、margin、constraintSize等）会共同影响约束数值，然后子组件才会基于这一处理过的约束测量自身尺寸。

**示例代码**

```
1. @Entry
2. @Component
3. struct VideoAdaptPage {
4. build() {
5. Column() {
6. Column() {
7. Video({})
8. .layoutWeight(1)
9. .borderRadius(12)
10. .clip(true)
11. .aspectRatio(1)
12. .loop(true)
13. .autoPlay(true)
14. .muted(true)
15. .margin({
16. left: 20,
17. top: 20,
18. right: 20,
19. })
20. }
21. }.height(2000)
22. }
23. }
```

[UnderstandTheAspectRatioLayout.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/UnderstandTheAspectRatioLayout.ets#L21-L43)

上述代码中，Column子元素在垂直方向上排列，具有高度约束但无宽度约束。示例代码中，为了便于数值计算，外层Column的高度被固定为2000。以下示例中的Column均为嵌套在顶层Column内部的子组件。

* Column受到高度约束2000，宽度约束为无。
* Column向Video传递高度约束2000，宽度约束为无。
* aspectRatio的作用使得Video受到高度约束2000，宽度约束2000。
* margin的作用使得Video受到高度约束1980，宽度约束1960。
* aspectRatio的作用使得Video的测量尺寸为高度1960，宽度1960。
* Column被子组件撑起，测量尺寸为高度1980，宽度2000。

由于Column的宽度约束无效，在交叉轴上子组件可以超出容器边界。在这种情况下，Video的实际宽度为1960，但只有1080的部分能够显示在屏幕上。
