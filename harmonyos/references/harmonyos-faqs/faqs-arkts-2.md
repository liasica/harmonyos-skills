---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-2
title: 有哪些创建线程的方式
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 有哪些创建线程的方式
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a54c0ca552f1524f571224818df52123b0d1062fd3c49b253a026455d8b7257b
---

* 在ArkTS中，使用Worker创建线程。Worker线程与主线程相互独立，但不能直接操作UI，最多创建64个Worker线程。
* 在ArkTS中使用任务池创建线程任务。
* 通过NAPI机制，在C代码中使用标准的线程API创建线程。
