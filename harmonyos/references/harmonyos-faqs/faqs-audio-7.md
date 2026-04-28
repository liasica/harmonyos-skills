---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-7
title: AudioRenderer是否有跳转到某一帧的接口
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioRenderer是否有跳转到某一帧的接口
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:074023451dd58c5841aa7fd3239264f15a0ac3128418684bf737200072f82416
---

AudioRenderer底层不支持跳转到某一帧。AudioRenderer接口由客户端主动发送数据，完成后即开始播放。而AvPlayer支持跳转到某一帧，因为它有数据源，例如文件。可使用avPlayer.seek()方法跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用。

```
1. let seekTime: number = 1000
2. avPlayer.seek(seekTime,media.SeekMode.SEEK_PREV_SYNC)
```

[AvSeek.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/AudioKit/entry/src/main/ets/pages/AvSeek.ets#L13-L14)

**参考链接**

[seek](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)
