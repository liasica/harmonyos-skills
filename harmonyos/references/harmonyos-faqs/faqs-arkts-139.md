---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-139
title: 对象中函数的this如何指向外层
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 对象中函数的this如何指向外层
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:18+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1233cc32c07989a6305c8d10b1e919ab1ce02e0ea4049e36c081431bf15fbd3e
---

通过箭头函数实现。参考代码如下：

```
1. interface T {
2. start: () => number
3. }
4. @Component
5. struct PointingOuterLayer {
6. @State num: number = 1
7. obj: T = {
8. start: () => {
9. return this.num
10. }
11. }
```

[PointingOuterLayer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/PointingOuterLayer.ets#L21-L31)
