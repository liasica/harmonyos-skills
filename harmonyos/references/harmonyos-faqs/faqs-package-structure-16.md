---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-package-structure-16
title: 是否允许HAR的循环依赖
breadcrumb: FAQ > 应用框架开发 > 程序包结构 > 是否允许HAR的循环依赖
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:29+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a41b6aef5a036a6f0e4889e0b2ebf41735acb0862902f6de99cb953dced21ba4
---

不允许循环依赖。可以把公共部分放到一个共享包中，或者使用[HAR模块间动态import依赖解耦](../harmonyos-guides/arkts-dynamic-import.md#har模块间动态import依赖解耦)。
