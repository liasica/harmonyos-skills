---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-8
title: 播放短促提示音（如点赞、收藏、新消息等场景的提示音或音效），应该如何处理
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 播放短促提示音（如点赞、收藏、新消息等场景的提示音或音效），应该如何处理
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9bae59b4896496dc516a5f8f07c5d2c9c25798ccdbd96b17a3c016372beb0d79
---

* 推荐优先使用[SoundPool](../harmonyos-references/js-apis-inner-multimedia-soundpool.md)，若应用使用SoundPool开发音频播放功能，且StreamUsage指定为Music、Movie、AudioBook等类型，播放短音，则其申请焦点时默认为并发模式，不会影响其他音频。
* 若应用不希望使用SoundPool，并且当前使用的流类型会打断其他音频播放，推荐使用[AudioSession](../harmonyos-guides/audio-playback-concurrency.md)相关接口，指定为MIX\_WITH\_OTHERS策略。
