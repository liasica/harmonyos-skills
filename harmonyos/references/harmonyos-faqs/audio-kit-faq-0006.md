---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/audio-kit-faq-0006
title: ArkWeb网页音频播放中断与续播适配
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 常见问题 > ArkWeb网页音频播放中断与续播适配
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:14+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:d0b38708aa0b8f8a484d91003d6730815238aa85a71a9f87ca5788a075b23611
---

**Q：Webview焦点如何适配？**

**A**：Webview焦点适配方案如下：

1. 应用可通过HTML标准接口监听当前流媒体播放状态，响应停流操作并刷新UX界面。
2. 应用可配置mediaOptions属性实现自动恢复播放。若应用自身实现播放按钮UI，需监听视频播放状态来刷新UI按钮界面。resumeInterval的默认值为0，表示不续播，可配置范围为0~60，0表示不续播，60表示被打断60秒以内能恢复播放。audioExclusive的默认值为true，表示独占播放。一个应用内，配置为false时，可并发播放。

参考链接：[mediaOptions](../harmonyos-references/arkts-basic-components-web-attributes.md#mediaoptions10)。
