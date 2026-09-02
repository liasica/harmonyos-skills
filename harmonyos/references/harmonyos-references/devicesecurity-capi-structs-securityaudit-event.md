---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-structs-securityaudit-event
title: SecurityAudit_Event
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 结构体 > SecurityAudit_Event
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0745eb239a4b099105d2aaec7524ca11a83a8239d675d1a6463d293057f3a96a
---

## 概述

定义审计事件信息。

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAudit](devicesecurity-capi-securityaudit.md)

**所在头文件：** [security\_audit.h](devicesecurity-capi-security-audit-8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int64\_t [eventId](devicesecurity-capi-structs-securityaudit-event.md#eventid) | 审计事件ID。 |
| const char \* [metadata](devicesecurity-capi-structs-securityaudit-event.md#metadata) | 集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。 |
| const char \* [content](devicesecurity-capi-structs-securityaudit-event.md#content) | 事件内容。 |

## 结构体成员变量说明

### content

```cpp
const char* SecurityAudit_Event::content
```

**描述**

事件内容。

### eventId

```cpp
int64_t SecurityAudit_Event::eventId
```

**描述**

审计事件ID。

### metadata

```cpp
const char* SecurityAudit_Event::metadata
```

**描述**

集成了事件版本号、事件接收时间、设备ID和用户ID的json字符串。
