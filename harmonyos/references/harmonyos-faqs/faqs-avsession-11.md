---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-avsession-11
title: 投播后支持哪些控制功能
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音视频播控（AVSession） > 投播后支持哪些控制功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:44+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b070a386bbd2387591fa9569ce48817f6dadb2476e16134f2ffda8a3d4ee1c2a
---

投播成功后，目前在本端支持的功能有：播放、暂停、下一首/曲、上一首/曲、快进、快退、进度控制、音量控制。

对端大屏设备支持的功能有：播放、暂停、下一首/曲、上一首/曲、快进、快退、进度控制。

目前不支持清晰度切换、音轨切换、倍速、弹幕等功能。

支持的接口：[sendControlCommand](../harmonyos-references/arkts-apis-avsession-avsessioncontroller.md#sendcontrolcommand10)(command: AVCastControlCommand, callback: AsyncCallback<void>): void。
