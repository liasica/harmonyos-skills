---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-97
title: ArkTS是否支持匿名内部类
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS是否支持匿名内部类
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4d3ff9c4fae0a306553ff2673f038c19deb3bf4fcac630cf4c38276b0dcab86e
---

ArkTS不支持匿名类，建议使用嵌套类实现。

因为使用匿名类创建的对象类型未知，这与ArkTS[不支持structural typing](../harmonyos-guides/typescript-to-arkts-migration-guide.md#不支持structural-typing)和对象字面量的类型冲突。限制主要是考虑运行时的性能开销，需要显式声明类。

**参考链接**

[不支持使用类表达式](../harmonyos-guides/typescript-to-arkts-migration-guide.md#不支持使用类表达式)
