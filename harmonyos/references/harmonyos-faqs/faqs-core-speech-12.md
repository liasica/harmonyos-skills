---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-12
title: 语音识别自动停止或初始化失败问题解决方案
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 语音识别自动停止或初始化失败问题解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:c9708d08a88d111181f01d9cea7b3ce18a347d3932a4353f39d0ff358125345d
---

## 问题现象

使用speechRecognizer.startListening接口语音实时转文字，说话时稍有停顿就自动停止，如何解决？

## 背景知识

[语音识别](../harmonyos-guides/speechrecognizer-guide.md)支持将一段中文音频信息（中文、中文语境下的英文；短语音模式不超过60s，长语音模式不超过8h）转换为文本，音频信息可以为PCM音频文件或者实时语音。

## 问题定位

在[speechRecognizer.startListening](../harmonyos-references/hms-ai-speechrecognizer.md#startlistening)接口的传参[StartParams](../harmonyos-references/hms-ai-speechrecognizer.md#startparams)中的extraParams可以设置Voice Activity Detection(VAD)后端点设置，具体规格如下：

* <'vadBegin', number>，Voice Activity Detection(VAD)后端点设置。
  + 参数范围是[500,10000]。
  + 可选，不传参时默认为800ms。

后端点设置越短，停顿后结束识别的时长也会越短，默认的800ms小于1s，所以会让用户在感官上认为稍有停顿识别就自动停止。

## 分析结论

开发者使用了默认后端点设置的800ms，小于1s，导致了用户在感官上认为稍有停顿语音识别就结束了。

## 修改建议

建议开发者可以显式地设置vadBegin参数大于1s，让用户可以有更多的时间进行停顿而不终止语音识别。
