---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-6
title: 音频处理哪些场景内置3A算法及AEC、ANC、AGC是否支持独立开关
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 音频处理哪些场景内置3A算法及AEC、ANC、AGC是否支持独立开关
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9c50f06ad7dc6a0a3c74fa693a63b48bbaa6f6a7703bc794688a87a465775dff
---

3A算法：指声学回声消除（Acoustic Echo Cancellation, AEC）、背景噪声抑制（Active Noise Control, ANC）和自动增益控制（Automatic Gain Control, AGC）三种音频处理算法。

配置为STREAM\_USAGE\_VOICE\_COMMUNICATION的音频流在运行时会自动启用3A算法。普通录音场景不会启用3A，仅在VoIP通话时才会启用。在播放音频流时，需要配置相应的StreamUsage类型。

**参考链接**

[AudioCapturer](../harmonyos-references/arkts-apis-audio-audiocapturer.md)
