---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-482
title: Text组件设置opacity后，文字颜色在整体透明度基础上叠加了一个透明，应该如何处理
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Text组件设置opacity后，文字颜色在整体透明度基础上叠加了一个透明，应该如何处理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1526c3d849ca7f5750e9718795aad0dae679c5e7c208d45dad83663de006b448
---

通过给组件设置renderGroup(true)或者blendMode(BlendMode.SRC\_OVER, BlendApplyType.OFFSCREEN)来实现。

可以参考如下示例：

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Row() {
6. Column() {
7. Text('你好')
8. .width(200)
9. .height(100)
10. .fontColor(Color.White)
11. .backgroundColor(Color.Blue)
12. .fontSize(20)
13. .textAlign(TextAlign.Center)
14. .opacity(0.3)
15. .margin(20)

17. Text('你好')
18. .width(200)
19. .height(100)
20. .fontColor(Color.White)
21. .backgroundColor(Color.Blue)
22. .fontSize(20)
23. .textAlign(TextAlign.Center)
24. .opacity(0.3)
25. .renderGroup(true)
26. }
27. .width('100%')
28. }
29. .height('100%')
30. }
31. }
```

[TextSetOpacity.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TextSetOpacity.ets#L21-L52)
