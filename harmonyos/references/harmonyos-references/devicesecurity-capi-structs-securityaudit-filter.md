---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-filter
title: SecurityAudit_Filter
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 结构体 > SecurityAudit_Filter
category: harmonyos-references
scraped_at: 2026-04-28T08:07:19+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d9b45c14546322d88f7929ddb09b1c779e9c33309fe47fa935a5d04099afc70d
---

## 概述

PC/2in1

提供过滤条件。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAudit](devicesecurity-capi-securityaudit.md)

**所在头文件：** [security\_audit.h](devicesecurity-capi-security-audit-8h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| bool [isInclude](devicesecurity-capi-structs-securityaudit-filter.md#isinclude) | TRUE: 符合条件的事件被返回给客户端。 FALSE: 符合条件的事件不被返回给客户端。 |
| [SecurityAudit\_FilterType](devicesecurity-capi-securityaudit.md#securityaudit_filtertype) [type](devicesecurity-capi-structs-securityaudit-filter.md#type) | 过滤器类型。 |
| const char \*\* [value](devicesecurity-capi-structs-securityaudit-filter.md#value) | 事件的过滤器的值。 |
| uint64\_t [valueCount](devicesecurity-capi-structs-securityaudit-filter.md#valuecount) | 过滤器值的数量。 |

## 结构体成员变量说明

PC/2in1

### isInclude

PC/2in1

```
1. bool SecurityAudit_Filter::isInclude
```

**描述**

TRUE: 符合条件的事件被返回给客户端。 FALSE: 符合条件的事件不被返回给客户端。

### type

PC/2in1

```
1. SecurityAudit_FilterType SecurityAudit_Filter::type
```

**描述**

过滤器类型。

### value

PC/2in1

```
1. const char** SecurityAudit_Filter::value
```

**描述**

事件的过滤器的值。

### valueCount

PC/2in1

```
1. uint64_t SecurityAudit_Filter::valueCount
```

**描述**

过滤器值的数量。
