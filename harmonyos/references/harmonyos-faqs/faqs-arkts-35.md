---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-35
title: 子线程和主线程的优先级及任务执行策略是什么
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > 子线程和主线程的优先级及任务执行策略是什么
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:23+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:68237cb25155801eb31d93556c322918021e79be0d78d252d0b8d3e5f7280bfc
---

主线程作为UI线程，拥有最高优先级。在高负载情况下，响应更及时；在低负载情况下，效率与其他线程差异不大。

子线程的调度可以受优先级设置和任务优先级的影响。
