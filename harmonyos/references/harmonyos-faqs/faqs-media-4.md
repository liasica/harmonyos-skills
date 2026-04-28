---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-4
title: 使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:40+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:82c47fc0adeb98ed5caa6968832c787eb64db8f90aa42a7f020206c5ff91178e
---

在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法[avPlayer.play()](../harmonyos-references/arkts-apis-media-avplayer.md#play9)，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法[avPlayer.pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9)即可。
