---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules
title: TimeZoneRules
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > TimeZoneRules
category: harmonyos-references
scraped_at: 2026-04-28T08:06:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1dc2a1305b36017e8da47f3e5c8afe485e340ea41380d47aa2e0ab1043a689e7
---

```
1. typedef struct TimeZoneRules {...} TimeZoneRules
```

## 概述

PhonePC/2in1TabletTVWearable

完整的时区规则。

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

**所在头文件：** [timezone.h](capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [InitialTimeZoneRule](capi-i18n-initialtimezonerule.md) initial | 起始时区规则。 |
| [TimeArrayTimeZoneRule\*](capi-i18n-timearraytimezonerule.md) timeArrayRules | 起始时间戳数组定义的时区规则数组。 |
| [AnnualTimeZoneRule\*](capi-i18n-annualtimezonerule.md) annualRules | 每年生效的时区规则数组。 |
| size\_t numTimeArrayRules | 起始时间戳数组定义的时区规则数组的大小。 |
| size\_t numAnnualRules | 每年生效的时区规则数组的大小。 |
