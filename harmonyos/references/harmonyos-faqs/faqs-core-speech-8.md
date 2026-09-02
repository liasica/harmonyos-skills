---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-8
title: 文本转语音textToSpeech中onData未触发如何解决
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 文本转语音textToSpeech中onData未触发如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:0701211c292aabbbe8f2c8d5e086b6ff1e25f3cfb8e505618e84ca38c449978c
---

## 问题现象

在文本转语音的textToSpeech监听中，onData回调未触发，相关的日志也未打印，如何解决？

## 解决方案

参考文本转语音[SpeakParams](../harmonyos-references/hms-ai-texttospeech.md#speakparams)合成播报音频流的extraParams参数，关于合成类型<'playType', number>的介绍如下：

* 0：仅合成不播报，返回音频流。
* 1：合成与播报不返回音频流。

不传参时默认为1。

若希望获取onData回调，需要设置'playType'为0。
