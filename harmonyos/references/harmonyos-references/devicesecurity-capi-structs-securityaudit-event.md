---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-event
title: SecurityAudit_Event
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 结构体 > SecurityAudit_Event
category: harmonyos-references
scraped_at: 2026-04-28T08:07:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:3978b271a8bbf0b75db813d58764d816c44352120433baab64be276b7832f1bd
---

## 概述

PC/2in1

定义审计事件信息。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAudit](devicesecurity-capi-securityaudit.md)

**所在头文件：** [security\_audit.h](devicesecurity-capi-security-audit-8h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| int64\_t [eventId](devicesecurity-capi-structs-securityaudit-event.md#eventid) | 审计事件ID。 |
| const char \* [metadata](devicesecurity-capi-structs-securityaudit-event.md#metadata) | 集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。 |
| const char \* [content](devicesecurity-capi-structs-securityaudit-event.md#content) | 事件内容。 |

## 结构体成员变量说明

PC/2in1

### content

PC/2in1

```
1. const char* SecurityAudit_Event::content
```

**描述**

事件内容。

### eventId

PC/2in1

```
1. int64_t SecurityAudit_Event::eventId
```

**描述**

审计事件ID。

### metadata

PC/2in1

```
1. const char* SecurityAudit_Event::metadata
```

**描述**

集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。
