---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-30
title: JS线程通过napi创建的C++线程的处理结果，如何返回JS线程
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > JS线程通过napi创建的C++线程的处理结果，如何返回JS线程
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:22+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a28f07f74bd02fee4144caad3d169d71f0cb2d785443c25a50e27c44068dabae
---

使用napi\_create\_threadsafe\_function在JS线程创建可被任意线程调用的函数，在C++线程调用napi\_call\_threadsafe\_function将结果回调给主线程。

**参考链接**

[使用Node-API接口进行线程安全开发](../harmonyos-guides/use-napi-thread-safety.md)
