---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-59
title: TaskPool后台I/O任务池，应用能否自行做管控？是否有方法开放管理机制
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > TaskPool后台I/O任务池，应用能否自行做管控？是否有方法开放管理机制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:25+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:24beaaf6d64dc2b5c59cf17a805ecc3f20ca6e37b1ee908a0791d363b272be81
---

1. TaskPool后台线程的数量由负载和硬件决定，无法直接管控。仅支持通过串行队列和任务组机制进行任务控制。

2. I/O任务池由底层进行调度，无法自行管控。
