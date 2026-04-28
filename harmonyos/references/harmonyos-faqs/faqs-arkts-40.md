---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-40
title: TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > TaskPool在任务执行过程中如何跟主线程进行通信？如何操作同一块内存变量
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:bf85248bdaa92cb1fbd1322398d9ab4524d4e104dea5d3d9be41c8ff98569be1
---

TaskPool的任务通过sendData接口触发主线程的onReceiveData回调，目前不支持主线程向子线程通信。

多个线程可以通过SharedArrayBuffer操作同一块内存。
