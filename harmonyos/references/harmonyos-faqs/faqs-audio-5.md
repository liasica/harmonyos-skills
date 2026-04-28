---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-5
title: 如何实现录音监听
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何实现录音监听
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:8634b68fc13daef152add5b3d00bd3a90a9a0c6b30938c28f2e1baada29482fd
---

系统音频监听功能在AudioStreamManager内，录音监听可以通过on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void订阅接口实现。详细可参考链接：[on('audioCapturerChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#onaudiocapturerchange9)。
