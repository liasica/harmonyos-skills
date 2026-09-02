---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-7
title: 文本转语音男声音色无效
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 文本转语音男声音色无效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:d195575410cb26ef8c072a22eb388c8c253e9fbfad5cfb90a8535863850e9af5
---

## 问题现象

文本转语音功能中男声音色调用失败，日志如下：

```txt
[{"language":"zh_CN","person":21,"style":"interaction-broadcast","status":"GA","gender":"Male","description":"中文 凌飞哲男声"}]
```

## 解决方案

原因分析："status":"GA"表示该音色未下载，导致文本转语音功能无法使用。

可参考：[VoiceInfo](../harmonyos-references/hms-ai-texttospeech.md#voiceinfo)的status参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | string | 否 | 是 | 音色模型状态  'GA'：音色可下载。  'INSTALLED'：音色已下载。  'EOM'：音色不可用。  起始版本：5.1.1(19) |

其中'GA'表示音色可下载。

需下载该音色资源，参考：[textToSpeech.downloadVoice](../harmonyos-references/hms-ai-texttospeech.md#texttospeechdownloadvoice)。
