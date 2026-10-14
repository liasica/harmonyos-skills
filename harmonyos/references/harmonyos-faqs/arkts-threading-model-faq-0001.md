---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-threading-model-faq-0001
title: ArkTS线程创建方式常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 常见问题 > ArkTS线程创建方式常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:41+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:08f22d7f1cf21177f73fbd1633f1554c4dd9a7263faa962ae85e6b83569ac27d
---

**Q：有哪些创建线程的方式？**

**A**：ArkTS中创建线程的方式有以下几种：

* 在ArkTS中，使用Worker创建线程。Worker线程与主线程相互独立，但不能直接操作UI，最多创建64个Worker线程。
* 在ArkTS中使用任务池创建线程任务。
* 通过NAPI机制，在C代码中使用标准的线程API创建线程。
