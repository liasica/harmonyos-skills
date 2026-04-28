---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-24
title: 线程间JS对象通过序列化方式进行数据通信，是否存在性能问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 线程间JS对象通过序列化方式进行数据通信，是否存在性能问题
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:44fea429a183b38868c0d3cd4b47e213c2a85c30d761d9e3009d4fcb938e0748
---

线程间对象的数据通信依赖于序列化和反序列化，耗时与数据量成正比。为了提高效率，建议控制传输的数据量，或者使用ArrayBuffer或SharedArrayBuffer进行数据转移或共享。
