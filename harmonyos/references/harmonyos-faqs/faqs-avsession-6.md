---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-6
title: 如何做到连续投播
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 如何做到连续投播
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8efeb244d9dc1dbcf2a998272eeb9327182e2f9e6e4a4493cf38829f0e375819
---

在切换剧集（同一电视剧的不同集或预告、花絮等）的场景中，为了提升用户体验，不应终止投播。应用应获取下一集的播放URL，继续自动投播下一集。当应用收到上一资源结束的回调，或检测到播放进度距离结束还有5秒时，应准备下一个资源，以确保连续投播。
