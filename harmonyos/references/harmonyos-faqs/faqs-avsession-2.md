---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-2
title: 应用如何更新进度条
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 应用如何更新进度条
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2083d3eb72d4fdd27b982021c6cdba791c29f7cd03420fb9118ff3155e6f3334
---

如果应用希望在播控中心支持进度显示和控制，需要将资源的时长信息设置给AVSession，并注册seek的回调接口以响应系统的进度控制。应用可以在倍速或播放状态发生变化时更新进度条，以节约系统资源。

## 参考链接

[实现进度条控制功能](../harmonyos-guides/avsession-access-scene.md#实现进度条控制功能)
