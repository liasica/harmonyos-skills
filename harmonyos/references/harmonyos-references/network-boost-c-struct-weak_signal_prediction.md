---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/network-boost-c-struct-weak_signal_prediction
title: NetworkBoost_WeakSignalPrediction
breadcrumb: API参考 > 系统 > 网络 > Network Boost Kit（网络加速服务） > C API > 结构体 > NetworkBoost_WeakSignalPrediction
category: harmonyos-references
scraped_at: 2026-09-02T15:01:57+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:33077c2998f7dffa3c8dfea52ce45e8f9be277a95dd0361b8847b17b89647347
---

## 概述

弱信号预测相关信息。

**起始版本：** 5.1.0(18)

**相关模块：** [NetworkBoost](network-boost-c-overview.md)

**所在头文件：** [network\_boost\_quality.h](network-boost-c-files-quality.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool [isLastPredictionValid](network-boost-c-struct-weak_signal_prediction.md#islastpredictionvalid) | 最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。 |
| uint32\_t [startTime](network-boost-c-struct-weak_signal_prediction.md#starttime) | 预计多长时间进入弱信号，单位为s，取值范围为0和任意正数。 |
| uint32\_t [duration](network-boost-c-struct-weak_signal_prediction.md#duration) | 预计在弱信号区域停留时长，单位为s，取任意正数。取值0，此次预测结果无效。 |

## 结构体成员变量说明

### duration

```c
uint32_t NetworkBoost_WeakSignalPrediction::duration
```

**描述**

预计在弱信号区域停留时长（单位：s），取任意正数。取值0，此次预测结果无效。

### isLastPredictionValid

```c
bool NetworkBoost_WeakSignalPrediction::isLastPredictionValid
```

**描述**

最近一次的弱信号预测是否有效，true表示最近一次的弱信号预测依旧有效，false表示最近一次的弱信号预测失效，此时startTime和duration参数忽略。

### startTime

```c
uint32_t NetworkBoost_WeakSignalPrediction::startTime
```

**描述**

预计多长时间进入弱信号（单位：s），取值范围为0和任意正数。
