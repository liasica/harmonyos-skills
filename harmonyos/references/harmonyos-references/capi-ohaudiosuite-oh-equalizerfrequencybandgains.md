---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohaudiosuite-oh-equalizerfrequencybandgains
title: OH_EqualizerFrequencyBandGains
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > C API > 结构体 > OH_EqualizerFrequencyBandGains
category: harmonyos-references
scraped_at: 2026-04-28T08:11:56+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:37ceb3b9ca9dc78487d60f55e1e8915407168f15e9ac215ed59c1b15963ff074
---

```
1. typedef struct {...} OH_EqualizerFrequencyBandGains
```

## 概述

PhonePC/2in1Tablet

定义音频编创均衡器效果节点配置参数。

**起始版本：** 22

**相关模块：** [OHAudioSuite](capi-ohaudiosuite.md)

**所在头文件：** [native\_audio\_suite\_base.h](capi-native-audio-suite-base-h.md)

## 汇总

PhonePC/2in1Tablet

### 成员变量

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| int32\_t gains[EQUALIZER\_BAND\_NUM] | 均衡器频带增益配置，EQUALIZER\_BAND\_NUM为10，输入范围为[-10, 10]，单位为dB（分贝）。  频带：31Hz、62Hz、125Hz、250Hz、500Hz、1kHz、2kHz、4kHz、8kHz、16kHz。  **起始版本：** 22 |
