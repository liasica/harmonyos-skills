---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-64
title: AudioSession音频会话未停用影响其他应用音频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioSession音频会话未停用影响其他应用音频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d8d5f56cb6385cbbb67eced0b9464cf2ec25bd49618d36fede8708bf1d931b1f
---

## 问题现象

AudioSession音频会话激活时，会影响其他应用音频播放，如何解决？

## 解决方案

AudioSession音频会话[isAudioSessionActivated](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#isaudiosessionactivated12)可查询音频会话是否已激活，音频会话激活状态与是否有音频正在播放没有关系。

当音频结束音频播放时，如果需要释放音频焦点，需要手动调用[deactivateAudioSession](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#deactivateaudiosession12)停用音频会话释放焦点，否则音频会话仍然会保持焦点1分钟，影响其他应用音频播放效果。
