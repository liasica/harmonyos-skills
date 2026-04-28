---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-32
title: 系统多线程模型是什么样的
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 系统多线程模型是什么样的
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:23+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:b5df658ae9d98473fd167756d3ab0e9984ad6bcf92929e3b69f53dfe2eeaf72d
---

ArkTS 提供 TaskPool API 支持多线程开发，长耗时任务可使用 Worker。Worker 的数量限制为 64 个。

建议在Native侧使用FFRT线程池，而 pthread 线程的数量则不受限制。
