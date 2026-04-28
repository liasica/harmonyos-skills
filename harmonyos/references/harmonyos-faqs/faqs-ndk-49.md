---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-49
title: 使用Node-API实现ArkTS与C/C++语言交互
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 使用Node-API实现ArkTS与C/C++语言交互
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:38+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:4421112fdf7c5a184e591323c96dabf0675f994880dbfa62daa172fdaf1b0ea0
---

在ArkTS侧不能向C++层注册对象或函数，开发者需要在C++层自行处理。Env可以长期持有，但在使用Env时，必须在创建该Env的ArkTS线程中进行。

**参考链接**

[Native与ArkTS对象绑定](../harmonyos-guides/use-napi-process.md)
