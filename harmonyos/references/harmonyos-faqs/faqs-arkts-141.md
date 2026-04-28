---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-141
title: 如何定义一个具有任意键的对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何定义一个具有任意键的对象
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:18+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:c2a71889e0e30512587beca8248d601162adba556e07870866065ba3aebe9410
---

可使用Record类型，有几个属性就对应几个类型参数，参考代码如下：

```
1. const asd: Record<string, number | string> = {
2. 'name': 'xc',
3. 'age': 29
4. }
```

[UnknowType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/UnknowType.ets#L21-L24)
