---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/core-speech-kit-faq-0001
title: 文本转语音男声音色无效
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 常见问题 > 文本转语音男声音色无效
category: harmonyos-faqs
scraped_at: 2026-10-28T07:49:07+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c7fd246676bcb82315e42a2c1648ab9e2aafa97d2984148c5bc5b1619da208e5
---

**Q：文本转语音功能中男声音色调用失败，日志如下：**

```txt
[{"language":"zh_CN","person":21,"style":"interaction-broadcast","status":"GA","gender":"Male","description":"中文 凌飞哲男声"}]
```

**A**：原因分析："status":"GA"表示该音色未下载，导致文本转语音功能无法使用。

可参考：[VoiceInfo](../harmonyos-references/hms-ai-texttospeech.md#voiceinfo)的status参数：

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | string | 否 | 是 | 音色模型状态  'GA'：音色可下载。  'INSTALLED'：音色已下载。  'EOM'：音色不可用。  起始版本：5.1.1(19) |

其中'GA'表示音色可下载；

需下载该音色资源，参考：[textToSpeech.downloadVoice](../harmonyos-references/hms-ai-texttospeech.md#section376811290229)。
