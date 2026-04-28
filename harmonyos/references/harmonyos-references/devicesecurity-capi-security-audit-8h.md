---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-security-audit-8h
title: security_audit.h
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 头文件 > security_audit.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d4eb0d3a08004f2ba5265cd9e1acbbc8eb31fbdff11ee1f862def7172d2ec620
---

## 概述

PC/2in1

文件中定义了与安全审计相关的函数。

**引用文件：** <DeviceSecurityKit/security\_audit.h>

**库：** libsecurityaudit\_ndk.z.so

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

**相关模块：** [SecurityAudit](devicesecurity-capi-securityaudit.md)

## 汇总

PC/2in1

### 结构体

PC/2in1

| 名称 | 描述 |
| --- | --- |
| struct [SecurityAudit\_Event](devicesecurity-capi-structs-securityaudit-event.md) | 定义审计事件信息。 |
| struct [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) | 提供过滤条件。 |

### 类型定义

PC/2in1

| 名称 | 描述 |
| --- | --- |
| typedef void(\* [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler)) (const [SecurityAudit\_Event](devicesecurity-capi-structs-securityaudit-event.md) \*events, uint64\_t count) | 定义事件处理函数。 |
| typedef struct SecurityAudit\_AuthClient\_Impl [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) | 定义阻断事件客户端。 |
| typedef struct SecurityAudit\_Client\_Impl [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) | 定义通知事件客户端。 |

### 枚举

PC/2in1

| 名称 | 描述 |
| --- | --- |
| [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) {  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PASTEBOARD = 0x27000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE = 0x1C000007, SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED = 0x1C001100, SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT = 0x10000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_WINDOW = 0x07000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_VOLUME = 0x0F000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINTER = 0x2E000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS = 0x1C000008,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_TRAFFIC = 0x1C00000E, SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_CONN = 0x1C00000F, SECURITY\_AUDIT\_NOTIFY\_EVENT\_CAMERA = 0x2D000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP = 0x10000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_EDM = 0x11000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_CERT = 0x12003000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_CREATE = 0x1C00000B, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ = 0x1C000012,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_VARIANT = 0x1C00000C, SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_INTERCEPT = 0x1C00000A, SECURITY\_AUDIT\_NOTIFY\_EVENT\_PERMISSION = 0x0B000000, SECURITY\_AUDIT\_NOTIFY\_EVENT\_DNS = 0x03000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_INSTALL\_INTERCEPTED = 0x18000100, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UNINSTALL\_INTERCEPTED = 0x18000101, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UPDATE\_INTERCEPTED = 0x18000102, SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_RECOVER\_INTERCEPTED = 0x18000103,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_START\_INTERCEPTED = 0x18000104, SECURITY\_AUDIT\_NOTIFY\_EVENT\_USB\_ACCESS\_INTERCEPTED = 0x30000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_SMB\_FILE\_SEND = 0x0F000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_PRE\_OPEN = 0x1C000014,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_HDC\_DEBUG = 0x27000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_HDC\_DEBUG\_INTERCEPTED = 0x27000101,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_USER\_SPACE\_DATA\_TRANSFER = 0x2F000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_USER\_SPACE\_DATA\_TRANSFER\_POLICY = 0x2F000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_SERIAL\_PORT\_ACCESS = 0x30000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_INTERCEPTED = 0x03000002,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_WIFI\_INTERCEPTED = 0x03000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINT\_INTERCEPTED = 0x2E000001  } | 定义通知事件的事件ID。 |
| [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) {  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE = 0x1C801100, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_OPEN = 0x1C801101, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_RENAME = 0x1C801102, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETE = 0x1C801103,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_SETEXTATTR = 0x1C801104, SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETEEXTATTR = 0x1C801105  } | 定义阻断事件的事件ID。 |
| [SecurityAudit\_FilterType](devicesecurity-capi-securityaudit.md#securityaudit_filtertype) {  EVENT\_TYPE\_EQUAL = 0x00000100, EVENT\_SUBTYPE\_EQUAL = 0x00000200, FILE\_PATH\_EQUAL = 0x00010000, FILE\_PATH\_PREFIX = 0x00010001,  FILE\_PATH\_SUFFIX = 0x00010002, PROCESS\_UID\_EQUAL = 0x00020000, PROCESS\_PID\_EQUAL = 0x00020100, PROCESS\_NAME\_EQUAL = 0x00020200,  PROCESS\_NAME\_PREFIX = 0x00020201, PROCESS\_NAME\_SUFFIX = 0x00020202  } | 定义过滤器类型。 |
| [SecurityAudit\_AuthResult](devicesecurity-capi-securityaudit.md#securityaudit_authresult) { SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW = 0, SECURITY\_AUDIT\_AUTH\_RESULT\_DENY = 1 } | 定义阻断结果的类型。 |

### 函数

PC/2in1

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_SecurityAudit\_NewClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_newclient) ([SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*\*client, [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler) handler) | 创建一个新的通知事件客户端。 |
| int32\_t [HMS\_SecurityAudit\_DeleteClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_deleteclient) ([SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client) | 删除通知客户端。 |
| int32\_t [HMS\_SecurityAudit\_Subscribe](devicesecurity-capi-securityaudit.md#hms_securityaudit_subscribe) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, const [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) \*events, uint64\_t count) | 订阅通知事件。 |
| int32\_t [HMS\_SecurityAudit\_Unsubscribe](devicesecurity-capi-securityaudit.md#hms_securityaudit_unsubscribe) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, const [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) \*events, uint64\_t count) | 取消订阅通知事件。 |
| int32\_t [HMS\_SecurityAudit\_AddFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_addfilter) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 为通知事件添加过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_RemoveFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_removefilter) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 删除通知事件的过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_NewAuthClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclient) ([SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*\*client, [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler) handler) | 创建一个新的阻断类事件客户端。 |
| int32\_t [HMS\_SecurityAudit\_DeleteAuthClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_deleteauthclient) ([SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client) | 删除阻断类事件客户端。 |
| int32\_t [HMS\_SecurityAudit\_SubscribeAuthEvent](devicesecurity-capi-securityaudit.md#hms_securityaudit_subscribeauthevent) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, const [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) \*events, uint64\_t count) | 订阅阻断类事件。 |
| int32\_t [HMS\_SecurityAudit\_UnsubscribeAuthEvent](devicesecurity-capi-securityaudit.md#hms_securityaudit_unsubscribeauthevent) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, const [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) \*events, uint64\_t count) | 取消订阅阻断类事件。 |
| int32\_t [HMS\_SecurityAudit\_AddAuthEventFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_addautheventfilter) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 为阻断类事件添加过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_RemoveAuthEventFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_removeautheventfilter) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 删除阻断类事件的过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_Auth](devicesecurity-capi-securityaudit.md#hms_securityaudit_auth) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, const [SecurityAudit\_Event](devicesecurity-capi-structs-securityaudit-event.md) \*event, [SecurityAudit\_AuthResult](devicesecurity-capi-securityaudit.md#securityaudit_authresult) authResult) | 设置审计事件的阻断结果。 |
| int32\_t [HMS\_SecurityAudit\_QueryAllProcesses](devicesecurity-capi-securityaudit.md#hms_securityaudit_queryallprocesses) (char\*\* result) | 获取所有的应用进程信息。 |
| int32\_t [HMS\_SecurityAudit\_QueryProcesses](devicesecurity-capi-securityaudit.md#hms_securityaudit_queryprocesses) (uint64\_t\* pids, uint64\_t count, char\*\* result) | 获取输入的pid的应用进程信息。 |
