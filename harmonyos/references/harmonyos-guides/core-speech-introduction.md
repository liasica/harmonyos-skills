---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-speech-introduction
title: Core Speech Kit简介
breadcrumb: 指南 > AI > Core Speech Kit（基础语音服务） > Core Speech Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a8fcb7365191fbef724a7ab077116f44196ab88cc5813df2a245f72259792ec8
---

Core Speech Kit（基础语音服务）集成了语音类基础AI能力，包括文本转语音（TextToSpeech）及语音识别（SpeechRecognizer）能力，便于用户与设备进行互动，实现将实时输入的语音与文本之间相互转换。

## 场景介绍

* 文本转语音：将一段不超过10000字符数的文本合成为语音并进行播报。实现效果可参考[朗读控件](speech-textreader-guide.md)。
* 语音识别：将一段音频信息（短语音模式不超过60s，长语音模式不超过8h）转换为文本，可以将pcm音频文件或者实时语音转换为文字。实现效果可参考[AI字幕控件](speech-aicaption-guide.md)。

## 约束与限制

### 支持的设备

Phone、Tablet、PC/2in1。

### 支持的国家/地区

仅适用于中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 能力限制

| AI能力 | 约束 |
| --- | --- |
| 文本转语音 | - 支持的语种类型：中文、英文。（简体中文、繁体中文、中文语境下的英文）  - 支持的音色类型：聆小珊女声音色、英语（美国）劳拉女声音色、凌飞哲男声音色。  - 文本长度：不超过10000字符数。 |
| 语音识别 | - 支持的语种类型：中文普通话。  - 支持的模型类型：离线。  - 语音时长：短语音模式不超过60s，长语音模式不超过8h。 |

## 模拟器支持情况

本Kit能力从6.0.0(20)版本开始支持模拟器。
