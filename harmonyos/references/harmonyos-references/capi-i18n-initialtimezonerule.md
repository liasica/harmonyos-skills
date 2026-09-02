---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-initialtimezonerule
title: InitialTimeZoneRule
breadcrumb: API参考 > 应用框架 > Localization Kit（本地化开发服务） > C API > 结构体 > InitialTimeZoneRule
category: harmonyos-references
scraped_at: 2026-09-02T15:01:38+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:faafcd590902fa268fd8a8d8ba07f22b78e1c95ed495ced06976d519565b6f14
---

```c
typedef struct InitialTimeZoneRule {...} InitialTimeZoneRule
```

## 概述

起始时区规则。

**起始版本：** 22

**相关模块：** [i18n](capi-i18n.md)

**所在头文件：** [timezone.h](capi-timezone-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t rawOffset | 时区的原始偏移量，单位为毫秒（ms）。 |
| int32\_t dstSavings | 夏令时的偏移量，单位为毫秒（ms）。 |
