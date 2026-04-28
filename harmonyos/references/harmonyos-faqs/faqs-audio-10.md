---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-10
title: 三方应用如何选择音频流类型
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 三方应用如何选择音频流类型
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:37+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:280d5286e8642898f5524bfb69bf309dd2763c2cc93d7f5f9e76c0081ab8eb14
---

对于播放流，其类型由StreamUsage决定；对于录制流，其类型由SourceType决定。

（1）音频流类型在音量控制、音频焦点管理、输入/输出设备选择等方面有决定性影响。

（2）应用需要根据自身的业务场景和实际需求，为音频选择合适的流类型。

WebView策略：目前不支持主动设置流类型，由WebView根据是否有音频输入自动设置为Music或VoiceCommunication类型（有播放流、无录制流，则默认为Music类型；播放流、录制流都有，则默认为VoiceCommunication类型）。

**参考链接**

[使用合适的音频流类型](../harmonyos-guides/using-right-streamusage-and-sourcetype.md)
