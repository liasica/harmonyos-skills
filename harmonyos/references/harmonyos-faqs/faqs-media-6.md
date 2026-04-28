---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-6
title: 在使用Video组件时，为Video添加本地视频播放源后，立刻播放，为什么会播放失败
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 在使用Video组件时，为Video添加本地视频播放源后，立刻播放，为什么会播放失败
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:49136db68d244682c348e1fec6a26505e7d435d81fc4929292a418f18fe5da2f
---

从Video组件加载资源到播放，必须经过加载过程，这需要一定时间。建议将开始播放的逻辑写入Video组件的onPrepared回调函数中，确保资源准备完毕后自动播放。
