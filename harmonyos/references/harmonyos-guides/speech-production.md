---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/speech-production
title: Speech Kit简介
breadcrumb: 指南 > AI > Speech Kit（场景化语音服务） > Speech Kit简介
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:15+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:ca4e3156cdd3551c8d2175a3d156792160da0c8a46f4df1e6977c66731e4343f
---

Speech Kit（场景化语音服务）集成了语音类AI能力，包括朗读控件（TextReader）和AI字幕控件（AICaptionComponent）能力，便于用户与设备进行互动，为用户实现朗读文章。

## 场景介绍

* 朗读控件应用广泛，例如在用户不方便或者无法查看屏幕文字时，为用户朗读新闻，提供资讯。
* AI字幕控件应用广泛，例如在用户不熟悉音频源语言或者静音时，为用户提供字幕服务。

## 约束与限制

### 支持的设备

Phone、Tablet、PC/2in1。

### 支持的国家/地区

仅适用于中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

### 能力限制

| AI能力 | 约束 |
| --- | --- |
| 朗读控件 | 支持的语种类型：中文。 |
| AI字幕控件 | 支持的语种类型：中英文。  支持的音频流：  - 音频类型：当前仅支持 "pcm"编码。  - 音频采样率：当前仅支持16000采样率。  - 音频声道：当前仅支持1个通道。  - 音频采样位深：当前仅支持16位。  部分机型暂不支持，调用失败返回对应错误码[初始化失败](../harmonyos-references/errorcode-speech.md#section1010600011-初始化失败)。 |

## 模拟器支持情况

本Kit暂不支持模拟器。
