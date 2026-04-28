---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-datetimerule
title: DateTimeRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > DateTimeRule
category: harmonyos-references
scraped_at: 2026-04-28T08:06:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cd9160db18381180f6e774b5b88f0ce5a02aa64213bb8ec029e112c060ad801b
---

```
1. typedef struct DateTimeRule {...} DateTimeRule
```

## 概述

PhonePC/2in1TabletTVWearable

时间日期规则。

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

**所在头文件：** [timezone.h](capi-timezone-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| int32\_t month | 月份。 |
| int32\_t dayOfMonth | 当月的第几天。 |
| int32\_t dayOfWeek | 当周的第几天。 |
| int32\_t weekInMonth | 当月的第几周。 |
| int32\_t millisInDay | 从当天凌晨0点开始到当前时间的毫秒值。 |
| [DateRuleType](capi-timezone-h.md#dateruletype) dateRuleType | 日期规则类型。 |
| [TimeRuleType](capi-timezone-h.md#timeruletype) timeRuleType | 时间规则类型。 |
