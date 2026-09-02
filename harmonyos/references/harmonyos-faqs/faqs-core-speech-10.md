---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-10
title: textToSpeech文本转语音播报音量无法调节
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > textToSpeech文本转语音播报音量无法调节
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:dffd720746ce382cfd7e050073cd66c1e8d470f5a6aed050186a757f2000003e
---

## 问题现象

textToSpeech文字转语音播报音量无法调节。

## 解决方案

原因分析：textToSpeech语音播报接口，默认播放通道是小艺语音助手。小艺音量只有在播报过程中才可通过音量上下键调节，在简短的播报场景，当用户发现音量过大或过小去调节音量时，播报已经结束，此时无法通过音量上下键调节小艺音量。这种场景下给用户的错觉是textToSpeech语音播报的音量无法调节。

解决方案：

1. 去设置里调整小艺音量：设置->声音和振动->小艺。
2. 在语音播报过程中，通过音量上下键调节。
3. 开发者使用textToSpeech接口时，主动把播放通道设置为媒体（没有音频播放的情况下音量上下键调整的是媒体音量）。设置方法：[SpeakParams->extraParams->soundChannel](../harmonyos-references/hms-ai-texttospeech.md#speakparams)。
