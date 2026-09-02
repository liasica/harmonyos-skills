---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-141
title: 如何定义一个未知类型的对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何定义一个未知类型的对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0d8214636eb37fbe107c78410a56e75ca0ef8d7296fa53af0d37f8d7a2baf2a2
---

可使用Record类型，有几个属性就对应几个类型参数，参考代码如下：

```ts
const asd: Record<string, number | string> = {
  'name': 'xc',
  'age': 29
}
```
