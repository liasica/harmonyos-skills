---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-faq
title: 常见问题
breadcrumb: 指南 > 优化应用性能 > 附录 > 常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:37f844fc06c6cb7754b7d17e290f45155c28098d8a1d516fbed476c3074d7b7a
---

## Native Leaks泳道录制捕获的泄露数据减少或丢失

**问题现象**

应用生命周期中，使用Allocation模板在当前会话录制ArkTS Snapshot泳道后，未重启应用在后续会话直接录制Native Leaks泳道，可能会导致捕获的泄露数据减少或丢失问题。

**解决措施**

录制ArkTS Snapshot泳道后，需重启应用，再录制Native Leaks泳道。
