---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-28
title: Worker和TaskPool的线程数量是否有限制
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > Worker和TaskPool的线程数量是否有限制
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:22+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:5f2d4df274ae0576d0bd7e99d5275bb9c1e4f18e1a8dc3d48ddb4cd04752d611
---

TaskPool会动态调整线程数量，不支持手动设置。只需将任务添加到线程池，确保高优先级任务及时执行。

Worker的线程个数最多为64个。如果超出此限制，创建将失败。

使用时，TaskPool和Worker相互独立，互不影响。因此，Worker数量达到上限时，不会影响TaskPool。Worker实例的数量上限为64个。TaskPool线程池的数量会根据硬件条件和任务负载动态调整。

**参考链接**

[TaskPool和Worker的对比 (TaskPool和Worker)](../harmonyos-guides/taskpool-vs-worker.md)
