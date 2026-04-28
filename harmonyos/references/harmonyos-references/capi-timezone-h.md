---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h
title: timezone.h
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 头文件 > timezone.h
category: harmonyos-references
scraped_at: 2026-04-28T08:06:33+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6415725dbcfa0e81b9de357bd17130f919accc0587d169a6bc5d77b0bed034b2
---

## 概述

PhonePC/2in1TabletTVWearable

提供获取时区信息的能力。

**引用文件：** <i18n/timezone.h>

**库：** libohi18n.so

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DateTimeRule](capi-i18n-datetimerule.md) | DateTimeRule | 时间日期规则。 |
| [InitialTimeZoneRule](capi-i18n-initialtimezonerule.md) | InitialTimeZoneRule | 起始时区规则。 |
| [TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md) | TimeArrayTimeZoneRule | 起始时间戳数组定义的时区规则。 |
| [AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md) | AnnualTimeZoneRule | 每年生效的时区规则。 |
| [TimeZoneRules](capi-i18n-timezonerules.md) | TimeZoneRules | 完整的时区规则。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md) | TimeZoneRuleQuery | 用于传入查询的信息，并接收查询的结果。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DateRuleType](capi-timezone-h.md#dateruletype) | DateRuleType | 日期规则类型的枚举。 |
| [TimeRuleType](capi-timezone-h.md#timeruletype) | TimeRuleType | 时间规则类型的枚举。 |

### 宏定义

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| MAX\_YEAR\_IN\_ANNUAL\_TIMEZONE\_RULE 0x7fffffff | 每年生效时区规则的年份最大值。  **起始版本：** 22 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [I18n\_ErrorCode OH\_i18n\_GetTimeZoneRules(const char\* timeZoneID, TimeZoneRules\* rules)](capi-timezone-h.md#oh_i18n_gettimezonerules) | 通过时区ID，获取完整的时区规则。 |
| [I18n\_ErrorCode OH\_i18n\_GetFirstStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getfirststartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则的首次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetFirstStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getfirststartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则的首次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetFinalStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getfinalstartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则的最后一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetFinalStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getfinalstartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则的最后一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetNextStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getnextstartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetNextStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getnextstartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetPrevStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getprevstartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetPrevStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getprevstartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetStartTimeAt(TimeArrayTimeZoneRule\* rule, int32\_t index, double\* result)](capi-timezone-h.md#oh_i18n_getstarttimeat) | 根据TimeArrayTimeZoneRule，获取时区规则指定索引的起始时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetStartInYear(AnnualTimeZoneRule\* rule, int32\_t year, TimeZoneRuleQuery\* query)](capi-timezone-h.md#oh_i18n_getstartinyear) | 根据AnnualTimeZoneRule，获取时区规则在指定年份的生效时间。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### DateRuleType

PhonePC/2in1TabletTVWearable

```
1. enum DateRuleType
```

**描述**

日期规则类型的枚举。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| DOM = 0 | 当月的第几天，以2025年为例，十月十六日为：十月的第十六天。 |
| DOW = 1 | 当月的第几个星期几，以2025年为例，十月十六日为：十月的第三个星期四。 |
| DOW\_GEQ\_DOM = 2 | 当月第几天之后的第一个星期几，以2025年为例，十月十六日为：十月第十三天/十四天/十五天之后的第一个星期四。 |
| DOW\_LEQ\_DOM = 3 | 当月第几天之前的最后一个星期几，以2025年为例，十月十六日为：十月第二十天之前的最后一个星期四。 |

### TimeRuleType

PhonePC/2in1TabletTVWearable

```
1. enum TimeRuleType
```

**描述**

时间规则类型的枚举。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

| 枚举项 | 描述 |
| --- | --- |
| WALL\_TIME = 0 | 本地时钟时间（不考虑时区偏移）。 |
| STANDARD\_TIME = 1 | 本地标准时间（不考虑夏令时偏移）。 |
| UTC\_TIME = 2 | 世界标准时间（UTC时间）。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_i18n\_GetTimeZoneRules()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetTimeZoneRules(const char* timeZoneID, TimeZoneRules* rules)
```

**描述**

通过时区ID，获取完整的时区规则。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* timeZoneID | 时区ID，例如“Asia/Shanghai”。 |
| [TimeZoneRules](capi-i18n-timezonerules.md)\* rules | 与时区ID对应的完整时区规则[TimeZoneRules](capi-i18n-timezonerules.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetFirstStartFromTimeArrayTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetFirstStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则的首次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetFirstStartFromAnnualTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetFirstStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则的首次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetFinalStartFromTimeArrayTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetFinalStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则的最后一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetFinalStartFromAnnualTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetFinalStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则的最后一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetNextStartFromTimeArrayTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetNextStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetNextStartFromAnnualTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetNextStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetPrevStartFromTimeArrayTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetPrevStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetPrevStartFromAnnualTimeZoneRule()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetPrevStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetStartTimeAt()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetStartTimeAt(TimeArrayTimeZoneRule* rule, int32_t index, double* result)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则指定索引的起始时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](capi-i18n-timearraytimezonerule.md)。 |
| int32\_t index | 起始时间的索引。 |
| double\* result | 规则生效的起始时间。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |

### OH\_i18n\_GetStartInYear()

PhonePC/2in1TabletTVWearable

```
1. I18n_ErrorCode OH_i18n_GetStartInYear(AnnualTimeZoneRule* rule, int32_t year, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则在指定年份的生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](capi-i18n-annualtimezonerule.md)。 |
| int32\_t year | 查询的年份。 |
| [TimeZoneRuleQuery](capi-i18n-timezonerulequery.md)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [I18n\_ErrorCode](capi-errorcode-h.md#i18n_errorcode) | 0 - 成功。  8900001 - 传入参数无效。  8900050 - 预期之外的错误，例如内存错误。 |
