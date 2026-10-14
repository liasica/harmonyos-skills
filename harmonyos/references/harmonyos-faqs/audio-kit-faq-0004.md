---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/audio-kit-faq-0004
title: AudioRenderer播放控制与跳转帧接口常见问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 常见问题 > AudioRenderer播放控制与跳转帧接口常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:38+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:4cd482c1c9ef90646a8cb54066fb7a661b8225b09b9b0778a02c44b0627365dd
---

**Q：AudioRenderer是否有跳转到某一帧的接口？**

**A**：AudioRenderer底层不支持跳转到某一帧。AudioRenderer接口由客户端主动发送数据，完成后即开始播放。而AvPlayer支持跳转到某一帧，因为它有数据源，例如文件。可使用avPlayer.seek()方法跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用。从API Version 26开始，直播场景也支持[seek](../doccenter-references/api/arkts-apis-media-avplayer.md#seek9)。

```ts
let seekTime: number = 1000
avPlayer.seek(seekTime,media.SeekMode.SEEK_PREV_SYNC)
```
