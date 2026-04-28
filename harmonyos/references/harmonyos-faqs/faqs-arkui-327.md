---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-327
title: 如何处理ForEach第三个参数键值生成耗时久导致的卡顿问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何处理ForEach第三个参数键值生成耗时久导致的卡顿问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d0abec160454bf64c44ddb8d7649f2463e77f75212d9729bbad5ce23de18af47
---

针对ForEach耗时影响性能，需要注意[键值生成规则](../harmonyos-guides/arkts-rendering-control-foreach.md#键值生成规则)即KeyGenerator函数。

使用ForEach渲染时，第三个参数KeyGenerator函数如果缺省，ArkUI框架会使用默认的键值生成函数，即(item: any, index: number) => index + '\_' + JSON.stringify(item)。在处理复杂对象集合和复杂交互时，这会影响渲染性能。为确保键值的唯一性，建议使用对象数据中的唯一id作为键值，避免在KeyGenerator函数中使用数据项索引index。
