---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-3
title: 如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:450a5a51d72983d0d872cf6345f272702943b44f9d8bb9925dab9a6cc3a79d87
---

需要先调用[reset()](../harmonyos-references/arkts-apis-media-avplayer.md#reset9)打断前一个音频，然后切换音频源。因为reset()是异步的，所以调用reset()的语句需加上await关键字。
