---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-9
title: 静音播放音频时，如何做到不抢音频焦点
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 静音播放音频时，如何做到不抢音频焦点
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b3404031cca533cbe3b63a944ecb946ce1ea34ba82a63685dd979f2dd3c88710
---

若应用以静音状态开始播放音频或视频，并且希望静音阶段不影响其他音频，后续解除静音时，再以正常策略申请音频焦点，可以调用静音并发播放模式的相关接口。

* 若使用[AVPlayer开发音频播放功能(ArkTS)](../harmonyos-guides/using-avplayer-for-playback.md)，可以调用[setMediaMuted](../harmonyos-references/arkts-apis-media-avplayer.md#setmediamuted12)函数。
* 若使用[AudioRenderer开发音频播放功能](../harmonyos-guides/using-audiorenderer-for-playback.md)，可调用[setSilentModeAndMixWithOthers](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setsilentmodeandmixwithothers12)函数。
* 若使用WebView开发音频播放功能，播放前将流音量设为0，系统默认优先与其他音频流并发，解除静音时申请音频焦点。
