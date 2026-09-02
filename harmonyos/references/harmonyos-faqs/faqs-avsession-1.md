---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-1
title: 如何响应播控中心的播放模式切换
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 如何响应播控中心的播放模式切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c01b0c178ea85e915194cf2a72e55b6842c0e6e2c0f353433f6c27235be6411f
---

应用创建AVSession后，需监听系统切换播放模式的接口，以处理播控中心的控制命令。目前支持四种播放模式：顺序播放、随机播放、单曲循环和列表循环。收到回调时，应用将获取当前的播放模式，并可自行决定下一个播放模式，然后将新的播放模式设置给AVSession。

## 参考链接

[实现循环模式功能](../harmonyos-guides/avsession-access-scene.md#实现循环模式功能)
