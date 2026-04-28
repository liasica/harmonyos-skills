---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-1
title: 如何响应播控中心的播放模式切换
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 如何响应播控中心的播放模式切换
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:17c3a7943e6329b0039a975ca372cf78a12286e999976c18e87807c13df2a225
---

应用创建AVSession后，需监听系统切换播放模式的接口，以处理播控中心的控制命令。目前支持四种播放模式：顺序播放、随机播放、单曲循环和列表循环。收到回调时，应用将获取当前的播放模式，并可自行决定下一个播放模式，然后将新的播放模式设置给AVSession。

**参考链接**

[循环模式](../harmonyos-guides/avsession-access-scene.md#循环模式)
