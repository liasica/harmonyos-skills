---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule
title: TimeArrayTimeZoneRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > TimeArrayTimeZoneRule
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2b5d0381ef2fc394a24fed195e0f1ad0e4a30e5a6925ff508a9044b14239b523
---

```c
typedef struct TimeArrayTimeZoneRule {...} TimeArrayTimeZoneRule
```

## 概述

起始时间戳数组定义的时区规则。

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

**所在头文件：** [timezone.h](capi-timezone-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char\* name | 时区规则的名称。 |
| int32\_t rawOffset | 时区的原始偏移量，单位为毫秒（ms）。 |
| int32\_t dstSavings | 夏令时的偏移量，单位为毫秒（ms）。 |
| double\* startTimes | 规则生效的起始时间戳数组，起始时间戳单位为毫秒（ms）。 |
| int32\_t numStartTimes | 规则生效的起始时间戳数组的大小。 |
| [TimeRuleType](capi-timezone-h.md#timeruletype) timeRuleType | 时间规则类型。 |
