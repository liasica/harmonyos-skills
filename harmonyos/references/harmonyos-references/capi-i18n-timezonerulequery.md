---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery
title: TimeZoneRuleQuery
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > TimeZoneRuleQuery
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fad344cbcb4886b98b591b51f82bb5f31ad945868732c929f9d7dfdbaf2c7622
---

```c
typedef struct TimeZoneRuleQuery {...} TimeZoneRuleQuery
```

## 概述

用于传入查询的信息，并接收查询的结果。

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

**所在头文件：** [timezone.h](capi-timezone-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| double base | 查询的基准时间，单位为毫秒（ms），采用Unix时间戳格式。 |
| int32\_t prevRawOffset | 上一次的时区原始偏移量，单位为毫秒（ms）。 |
| int32\_t prevDSTSavings | 上一次的夏令时偏移量，单位为毫秒（ms）。 |
| bool inclusive | 查询结果是否包含基准时间。true：查询结果包含基准时间；false：查询结果不包含基准时间。 |
| double result | 查询结果，单位为毫秒（ms），采用Unix时间戳格式。 |
