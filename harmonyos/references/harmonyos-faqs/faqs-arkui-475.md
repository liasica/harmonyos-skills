---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-475
title: 如何实现Tabs高度自适应内容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现Tabs高度自适应内容
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f1b7fdd8cdb068551f8032a56009ebcb41eb5d39af53ad9d8bd5c60846f2c429
---

可以给Tabs设置height('auto')。参考示例如下：

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Tabs() {
7. TabContent() {
8. Row() {
9. Text('hello')
10. }
11. .width('100%')
12. }
13. }
14. .height('auto')
15. .barBackgroundColor(Color.Orange)
16. .barHeight(0)
17. }
18. .height('100%')
19. .width('100%')
20. }
21. }
```

[TabsHeightAdaptive.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TabsHeightAdaptive.ets#L21-L42)
