---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-core-speech-9
title: 语音识别结果没有纠正如何解决
breadcrumb: FAQ > AI功能开发 > 机器学习 > 基础语音（Core Speech） > 语音识别结果没有纠正如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:55:00+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:2fd5de7468eeccc68f9470e4fbd5d8d9ef2527548f433829f460f9432a70df8e
---

## 问题现象

使用[语音识别](../harmonyos-guides/speechrecognizer-guide.md)能力，识别古诗词语音转文字后，概率出现在结果不准确时没有纠正的情况，如何解决？需要声音最低多少分贝？

## 解决方案

1. [语音识别](../harmonyos-guides/speechrecognizer-guide.md)为端侧能力，只预置了少量纠正能力，当发音不准时会出现未纠正现象。应用可根据热词进行优化，但热词有数量限制，总数最大为200，可参考创建引擎实例参数[CreateEngineParams](../harmonyos-references/hms-ai-speechrecognizer.md#createengineparams)配置系统热词，或参考启动语音识别参数[StartParams](../harmonyos-references/hms-ai-speechrecognizer.md#startparams)配置会话热词。
2. 声音分贝没有明确的限制，高噪声场景对识别效果会有影响。
