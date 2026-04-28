---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-15
title: 设备切换后没有暂停
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 设备切换后没有暂停
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3f8fc08ab99e44a0781bc9e6b8ea89d9015288205cd9ccd22d091f590c9a0d71
---

* 开发者可以了解音频流输出设备变更信息，并完成相应适配，确保应用在设备发生变更时的用户体验。开发者可使用AudioRenderer的[outputDeviceChangeWithInfo](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onoutputdevicechangewithinfo11)，用于监听音频流输出设备变化及原因。当系统出现音频输出设备的上下线、用户强选、设备抢占或设备选择策略变更等情况，导致音频流输出设备变更时，系统将通过该接口通知应用当前音频流设备变更信息，包含当前音频流输出设备信息和设备变更原因。
* Webview策略：若应用实现播放按钮UI，需监听video播放状态以刷新UI按钮界面。

**参考链接**

[响应输出设备变更时合理暂停](../harmonyos-guides/audio-output-device-change.md)
