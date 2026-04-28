---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-37
title: ArkTS是否支持类似Java的共享内存模型进行多线程开发
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > ArkTS是否支持类似Java的共享内存模型进行多线程开发
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:22e73dc5a8acc0c00ae8a60682598d445e62b36d783069687385c063c0ac9624
---

无法通过加锁的方式实现多个线程同时对同一个内存对象进行操作。

ArkTS采用Actor并发模型，线程间内存隔离，目前仅支持SharedArrayBuffer和Native层对象的共享。

**参考链接**

[多线程并发概述](../harmonyos-guides/multi-thread-concurrency-overview.md)
