---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hicollie-hicollie-settimerparam
title: HiCollie_SetTimerParam
breadcrumb: API参考 > 系统 > 调测调优 > Performance Analysis Kit（性能分析服务） > C API > 结构体 > HiCollie_SetTimerParam
category: harmonyos-references
scraped_at: 2026-09-02T15:02:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:57a7f1c9ee4054c6e8509b7af5e113f402a9500a86472bfc4dca0a87be2f0a47
---

```c
typedef struct HiCollie_SetTimerParam {...} HiCollie_SetTimerParam
```

## 概述

定义OH\_HiCollie\_SetTimer函数的输入参数，用于设置定时器监控任务的名称、任务超时时间阈值、超时回调函数及执行动作标志。

使用场景：适用于需要监控任务执行时间的场景，帮助开发者监控和处理任务超时问题。

**起始版本：** 18

**相关模块：** [HiCollie](capi-hicollie.md)

**所在头文件：** [hicollie.h](capi-hicollie-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \*name | timer任务名称。任务名称不可为空。 |
| unsigned int timeout | 任务超时时间阈值，单位：s，取值为大于0的正整数。当任务执行时间超过该阈值时，将触发超时处理机制。建议根据实际业务场景设置。 |
| [OH\_HiCollie\_Callback](capi-hicollie-h.md#oh_hicollie_callback) func | 超时发生时执行的回调函数。 |
| void \*arg | 回调函数的参数。 |
| [HiCollie\_Flag](capi-hicollie-h.md#hicollie_flag) flag | 超时发生时执行的动作，参考[HiCollie\_Flag](capi-hicollie-h.md#hicollie_flag)。 |
