---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule
title: AnnualTimeZoneRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > AnnualTimeZoneRule
category: harmonyos-references
scraped_at: 2026-04-28T08:06:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:dfa33339634f58fe69537214a99108ce9e0fc4f516f451d313a3944ab97a7ad5
---

```
1. typedef struct AnnualTimeZoneRule {...} AnnualTimeZoneRule
```

## 概述

PhonePC/2in1TabletTVWearable

每年生效的时区规则。

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

**所在头文件：** [timezone.h](capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char\* name | 时区规则的名称。 |
| int32\_t startYear | 时区规则生效的起始年份。 |
| int32\_t endYear | 时区规则生效的终止年份。 |
| int32\_t rawOffset | 时区的原始偏移量。 |
| int32\_t dstSavings | 夏令时的偏移量。 |
| [DateTimeRule](capi-i18n-datetimerule.md) dateTimeRule | 时间日期规则。 |
