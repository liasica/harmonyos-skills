---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-14
title: Webview焦点如何适配
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > Webview焦点如何适配
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:38+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d23ff7c098cb4b8c2c1720f2057dd09a754669dab636352c6002af39896fe83a
---

1. 应用可通过HTML标准接口监听当前流媒体播放状态，响应停流操作并刷新UX界面。
2. 应用可配置mediaOptions属性实现自动恢复播放。若应用自身实现播放按钮UI，需监听视频播放状态来刷新UI按钮界面。resumeInterval的默认值为0，表示不续播，可配置范围为0~60，0表示不续播，60表示被打断60秒以内能恢复播放。audioExclusive的默认值为true，表示独占播放。一个应用内，配置为false时，可并发播放。

**参考链接**

[mediaOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#mediaoptions10)
