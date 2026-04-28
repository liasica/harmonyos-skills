---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-43
title: 在ArkTS的主线程中使用await会阻塞主线程吗
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 在ArkTS的主线程中使用await会阻塞主线程吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:25+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:51e0f82de403ada8d6fa57d58b2a45100fae4dd3b878c16b2e8bf8cdb1a8bc38
---

await会挂起当前异步任务，等待条件满足后唤醒执行，主线程可处理其他任务。
