---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/devicesecurity-capi-securityaudit
title: SecurityAudit
breadcrumb: API参考 > 系统 > 安全 > Device Security Kit（设备安全服务） > C API > 模块 > SecurityAudit
category: harmonyos-references
scraped_at: 2026-09-02T15:01:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f245bc9221b0c863e728747096aaff10bcdd0874e165998f445af7cdf3fe0754
---

## 概述

提供安全审计的API。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

## 汇总

### 文件

| 名称 | 描述 |
| --- | --- |
| [security\_audit.h](devicesecurity-capi-security-audit-8h.md) | 文件中定义了与安全审计相关的函数。 |

### 结构体

| 名称 | 描述 |
| --- | --- |
| struct [SecurityAudit\_Event](devicesecurity-capi-structs-securityaudit-event.md) | 定义审计事件信息。 |
| struct [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) | 提供过滤条件。 |
| struct [SecurityAudit\_AuthClientConfiguration](devicesecurity-capi-structs-securityaudit-authclientconfiguration.md) | 阻断事件客户端配置项。 |

### 类型定义

| 名称 | 描述 |
| --- | --- |
| typedef void(\* [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler)) (const [SecurityAudit\_Event](devicesecurity-capi-structs-securityaudit-event.md) \*events, uint64\_t count) | 定义事件处理函数。 |
| typedef struct SecurityAudit\_AuthClient\_Impl [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) | 定义阻断事件客户端。 |
| typedef struct SecurityAudit\_AuthClientConfiguration\_Impl [SecurityAudit\_AuthClientConfiguration](devicesecurity-capi-securityaudit.md#securityaudit_authclientconfiguration) | 定义阻断事件客户端配置对象。 |
| typedef struct SecurityAudit\_Client\_Impl [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) | 定义通知事件客户端。 |

### 枚举

| 名称 | 描述 |
| --- | --- |
| [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) {  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PASTEBOARD = 0x27000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE = 0x1C000007,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED = 0x1C001100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT = 0x10000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_WINDOW = 0x07000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_VOLUME = 0x0F000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINTER = 0x2E000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS = 0x1C000008,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_TRAFFIC = 0x1C00000E,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_CONN = 0x1C00000F,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_CAMERA = 0x2D000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP = 0x10000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_EDM = 0x11000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_CERT = 0x12003000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_CREATE = 0x1C00000B,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ = 0x1C000012,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_VARIANT = 0x1C00000C,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_INTERCEPT = 0x1C00000A,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PERMISSION = 0x0B000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DNS = 0x03000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_INSTALL\_INTERCEPTED = 0x18000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UNINSTALL\_INTERCEPTED = 0x18000101,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UPDATE\_INTERCEPTED = 0x18000102,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_RECOVER\_INTERCEPTED = 0x18000103,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_START\_INTERCEPTED = 0x18000104,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_USB\_ACCESS\_INTERCEPTED = 0x30000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_SMB\_FILE\_SEND = 0x0F000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SHARE= 0x0F000002,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DATA\_DRAG= 0x0F000003,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_PRE\_OPEN = 0x1C000014,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_HDC\_DEBUG = 0x27000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_HDC\_DEBUG\_INTERCEPTED = 0x27000101,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_USER\_SPACE\_DATA\_TRANSFER = 0x2F000000,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_USER\_SPACE\_DATA\_TRANSFER\_POLICY = 0x2F000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_SERIAL\_PORT\_ACCESS = 0x30000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_BLUETOOTH\_INTERCEPTED = 0x03000200,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DISC\_BURNING = 0x0F000004,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_MEDIA\_FILE\_ACCESS = 0x0F000005,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT\_MANAGEMENT = 0x10000103,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DEVICE\_POWER\_ON = 0x16000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DEVICE\_POWER\_OFF = 0x16000002,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_AUDIO\_INTERFACE\_ACCESS = 0x1A000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_VIDEO\_INTERFACE\_ACCESS = 0x1A000002,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_SERIAL\_PORT\_INTERCEPTED = 0x30000101,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_INTERCEPTED = 0x03000002,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_WIFI\_INTERCEPTED = 0x03000100,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINT\_INTERCEPTED = 0x2E000001,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_CS\_VERIFY\_NULL = 0x12001081,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_CS\_VERIFY\_ABNORMAL = 0x12001082,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FS\_MOUNT\_ABNORMAL = 0x1C001102,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DRIVER\_CS\_ABNORMAL = 0x1C001200,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DRIVER\_MMAP\_ABNORMAL = 0x1C001201,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_KERNEL\_MEMORY\_ABNORMAL = 0x1C001300,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS\_DEBUG\_ABNORMAL = 0x1C001401,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS\_CRASH\_ABNORMAL = 0x1C001402,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS\_PRIVILEGE\_ESCALATION = 0x1C001403,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_DLP\_FILE\_ACCESS = 0x0F000006,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_CREATE = 0x1C001104,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_OPEN = 0x1C001105,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_CLOSE = 0x1C001106,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_DELETE = 0x1C001107,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_RENAME = 0x1C001108,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_COPY = 0x1C001109,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SETOWNER = 0x1C00110A,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SETMODE = 0x1C00110B,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SETEXTATTR = 0x1C00110C,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_DELETEEXTATTR = 0x1C00110D,  SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_WRITE = 0x1C00110E  } | 定义通知事件的事件ID。 |
| [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) {  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE = 0x1C801100,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_OPEN = 0x1C801101,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_RENAME = 0x1C801102,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETE = 0x1C801103,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_SETEXTATTR = 0x1C801104,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETEEXTATTR = 0x1C801105,  SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_READ\_END = 0x1C801106,  SECURITY\_AUDIT\_AUTH\_EVENT\_PROCESS\_EXEC = 0x1C801400  } | 定义阻断类事件的事件ID。 |
| [SecurityAudit\_FilterType](devicesecurity-capi-securityaudit.md#securityaudit_filtertype) {  EVENT\_TYPE\_EQUAL = 0x00000100,  EVENT\_SUBTYPE\_EQUAL = 0x00000200,  FILE\_PATH\_EQUAL = 0x00010000,  FILE\_PATH\_PREFIX = 0x00010001,  FILE\_PATH\_SUFFIX = 0x00010002, FILE\_PATH\_REGULAR = 0x00010003,  PROCESS\_UID\_EQUAL = 0x00020000,  PROCESS\_PID\_EQUAL = 0x00020100,  PROCESS\_NAME\_EQUAL = 0x00020200,  PROCESS\_NAME\_PREFIX = 0x00020201,  PROCESS\_NAME\_SUFFIX = 0x00020202  } | 定义过滤器类型。 |
| [SecurityAudit\_AuthResult](devicesecurity-capi-securityaudit.md#securityaudit_authresult) { SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW = 0, SECURITY\_AUDIT\_AUTH\_RESULT\_DENY = 1 } | 定义阻断结果的类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| int32\_t [HMS\_SecurityAudit\_NewClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_newclient) ([SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*\*client, [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler) handler) | 创建一个新的通知事件客户端。 |
| int32\_t [HMS\_SecurityAudit\_DeleteClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_deleteclient) ([SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client) | 删除通知客户端。 |
| int32\_t [HMS\_SecurityAudit\_Subscribe](devicesecurity-capi-securityaudit.md#hms_securityaudit_subscribe) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, const [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) \*events, uint64\_t count) | 订阅通知事件。 |
| int32\_t [HMS\_SecurityAudit\_Unsubscribe](devicesecurity-capi-securityaudit.md#hms_securityaudit_unsubscribe) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, const [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) \*events, uint64\_t count) | 取消订阅通知事件。 |
| int32\_t [HMS\_SecurityAudit\_AddFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_addfilter) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 为通知事件添加过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_RemoveFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_removefilter) (const [SecurityAudit\_Client](devicesecurity-capi-securityaudit.md#securityaudit_client) \*client, [SecurityAudit\_Notify\_Event](devicesecurity-capi-securityaudit.md#securityaudit_notify_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 删除通知事件的过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_NewAuthClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclient) ([SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*\*client, [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler) handler) | 创建一个新的阻断类事件客户端（超时默认放行）。 |
| int32\_t [HMS\_SecurityAudit\_NewAuthClientWithConfiguration](devicesecurity-capi-securityaudit.md#hms_securityaudit_newauthclientwithconfiguration) ([SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*\*outOwnedClient, [SecurityAudit\_Handler](devicesecurity-capi-securityaudit.md#securityaudit_handler) handler, const [SecurityAudit\_AuthClientConfiguration](devicesecurity-capi-structs-securityaudit-authclientconfiguration.md) \*configuration) | 创建一个新的阻断类事件客户端（可配置超时默认阻断策略）。 |
| int32\_t [HMS\_SecurityAudit\_CreateAuthClientConfiguration](devicesecurity-capi-securityaudit.md#hms_securityaudit_createauthclientconfiguration) ([SecurityAudit\_AuthClientConfiguration](devicesecurity-capi-structs-securityaudit-authclientconfiguration.md) \*\*outOwnedConfiguration) | 创建阻断类事件客户端配置对象。 |
| int32\_t [HMS\_SecurityAudit\_DestroyAuthClientConfiguration](devicesecurity-capi-securityaudit.md#hms_securityaudit_destroyauthclientconfiguration) ([SecurityAudit\_AuthClientConfiguration](devicesecurity-capi-structs-securityaudit-authclientconfiguration.md) \*configuration) | 销毁阻断类事件客户端配置对象。 |
| int32\_t [HMS\_SecurityAudit\_AuthClientConfiguration\_SetTimeoutAuthResult](devicesecurity-capi-securityaudit.md#hms_securityaudit_authclientconfiguration_settimeoutauthresult) ([SecurityAudit\_AuthClientConfiguration](devicesecurity-capi-structs-securityaudit-authclientconfiguration.md) \*configuration, [SecurityAudit\_AuthResult](devicesecurity-capi-securityaudit.md#securityaudit_authresult) authResult) | 设置超时默认授权结果。 |
| int32\_t [HMS\_SecurityAudit\_DeleteAuthClient](devicesecurity-capi-securityaudit.md#hms_securityaudit_deleteauthclient) ([SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client) | 删除阻断类事件客户端。 |
| int32\_t [HMS\_SecurityAudit\_SubscribeAuthEvent](devicesecurity-capi-securityaudit.md#hms_securityaudit_subscribeauthevent) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, const [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) \*events, uint64\_t count) | 订阅阻断类事件。 |
| int32\_t [HMS\_SecurityAudit\_UnsubscribeAuthEvent](devicesecurity-capi-securityaudit.md#hms_securityaudit_unsubscribeauthevent) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, const [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) \*events, uint64\_t count) | 取消订阅阻断类事件。 |
| int32\_t [HMS\_SecurityAudit\_AddAuthEventFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_addautheventfilter) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 为阻断类事件添加过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_RemoveAuthEventFilter](devicesecurity-capi-securityaudit.md#hms_securityaudit_removeautheventfilter) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, [SecurityAudit\_Auth\_Event](devicesecurity-capi-securityaudit.md#securityaudit_auth_event) event, const [SecurityAudit\_Filter](devicesecurity-capi-structs-securityaudit-filter.md) \*filter) | 删除阻断类事件的过滤条件。 |
| int32\_t [HMS\_SecurityAudit\_Auth](devicesecurity-capi-securityaudit.md#hms_securityaudit_auth) (const [SecurityAudit\_AuthClient](devicesecurity-capi-securityaudit.md#securityaudit_authclient) \*client, const [SecurityAudit\_Event](devicesecurity-capi-structs-securityaudit-event.md) \*event, [SecurityAudit\_AuthResult](devicesecurity-capi-securityaudit.md#securityaudit_authresult) authResult) | 设置审计事件的阻断结果。 |
| int32\_t [HMS\_SecurityAudit\_QueryAllProcesses](devicesecurity-capi-securityaudit.md#hms_securityaudit_queryallprocesses)(char\*\* result) | 获取所有的应用进程信息。 |
| int32\_t [HMS\_SecurityAudit\_QueryProcesses](devicesecurity-capi-securityaudit.md#hms_securityaudit_queryprocesses)(uint64\_t\* pids, uint64\_t count, char\*\* result) | 获取输入的pid的应用进程信息。 |
| int32\_t [HMS\_SecurityAudit\_AcquireCodeSign](devicesecurity-capi-securityaudit.md#hms_securityaudit_acquirecodesign)(char\* path, char\*\* outOwnedResult) | 获取输入的文件路径的代码签名信息。 |
| int32\_t [HMS\_SecurityAudit\_AcquireAllClientsInfo](devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallclientsinfo) (char\*\* outOwnedResult) | 获取全量通知类客户端信息。 |
| int32\_t [HMS\_SecurityAudit\_AcquireAllAuthClientsInfo](devicesecurity-capi-securityaudit.md#hms_securityaudit_acquireallauthclientsinfo) (char\*\* outOwnedResult) | 获取全量阻断类客户端信息。 |

## 类型定义说明

### SecurityAudit\_AuthClient

```cpp
typedef struct SecurityAudit_AuthClient_Impl SecurityAudit_AuthClient
```

**描述**

定义阻断事件客户端。

**起始版本：** 6.0.0(20)

### SecurityAudit\_Client

```cpp
typedef struct SecurityAudit_Client_Impl SecurityAudit_Client
```

**描述**

定义通知事件客户端。

**起始版本：** 6.0.0(20)

### SecurityAudit\_Handler

```cpp
typedef void(* SecurityAudit_Handler) (const SecurityAudit_Event *events, uint64_t count)
```

**描述**

定义事件处理函数。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| events | 指向审计事件信息的指针。 |
| count | 数组中的事件数。 |

### SecurityAudit\_AuthClientConfiguration

```cpp
typedef struct SecurityAudit_AuthClientConfiguration_Impl SecurityAudit_AuthClientConfiguration
```

**描述**

定义阻断事件客户端配置对象。

**起始版本：** 26.0.0

## 枚举类型说明

### SecurityAudit\_Auth\_Event

```cpp
enum SecurityAudit_Auth_Event
```

**描述**

定义阻断事件的事件ID。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_CREATE | 文件创建阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_OPEN | 文件打开阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_RENAME | 文件重命名阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETE | 文件删除阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_SETEXTATTR | 文件设置扩展属性的阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_DELETEEXTATTR | 文件删除扩展属性的阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_FILE\_READ\_END | 文件读结束阻断事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_AUTH\_EVENT\_PROCESS\_EXEC | 进程执行阻断事件。  **起始版本：** 26.0.0 |

### SecurityAudit\_AuthResult

```cpp
enum SecurityAudit_AuthResult
```

**描述**

定义阻断结果的类型。

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| SECURITY\_AUDIT\_AUTH\_RESULT\_ALLOW | 允许的阻断事件。 |
| SECURITY\_AUDIT\_AUTH\_RESULT\_DENY | 拒绝的阻断事件。 |

### SecurityAudit\_FilterType

```cpp
enum SecurityAudit_FilterType
```

**描述**

定义过滤器类型。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| EVENT\_TYPE\_EQUAL | 事件类型的过滤器类型。 |
| EVENT\_SUBTYPE\_EQUAL | 事件子类型的过滤器类型。 |
| FILE\_PATH\_EQUAL | 文件路径类型的过滤器类型。 |
| FILE\_PATH\_PREFIX | 文件路径前缀类型的过滤器类型。 |
| FILE\_PATH\_SUFFIX | 文件路径后缀类型的过滤器类型。 |
| FILE\_PATH\_REGULAR | 文件路径正则表达式的过滤类型。  **起始版本：** 26.0.0  **模型约束：** 此接口仅可在Stage模型下使用。 |
| PROCESS\_UID\_EQUAL | 过滤进程的 UID 类型。 |
| PROCESS\_PID\_EQUAL | 过滤进程 ID 类型。 |
| PROCESS\_NAME\_EQUAL | 筛选进程名称类型。 |
| PROCESS\_NAME\_PREFIX | 进程名称前缀的过滤类型。 |
| PROCESS\_NAME\_SUFFIX | 进程名称后缀的过滤类型。 |

### SecurityAudit\_Notify\_Event

```cpp
enum SecurityAudit_Notify_Event
```

**描述**

定义通知事件的事件ID。

**系统能力：** SystemCapability.Security.SecurityAudit

**起始版本：** 6.0.0(20)

| 枚举值 | 描述 |
| --- | --- |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PASTEBOARD | 剪贴板复制和粘贴事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE | 文件事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_INTERCEPTED | 文件访问规则违规事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT | 账户登录和注销事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_WINDOW | 窗口截图、屏幕录制、屏幕投影事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_VOLUME | 可移动存储设备的插入和移除事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINTER | 打印机事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS | 进程创建或退出事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_TRAFFIC | 网络流量事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_CONN | 网络连接事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_CAMERA | 相机事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP | 应用程序事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_EDM | 企业设备管理事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_CERT | 证书操作事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_CREATE | KIA文件创建事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_READ | KIA文件读取事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_VARIANT | KIA文件变体事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_INTERCEPT | KIA文件拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PERMISSION | 应用程序权限更改事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DNS | DNS审计事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_INSTALL\_INTERCEPTED | 应用程序安装拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UNINSTALL\_INTERCEPTED | 应用程序卸载拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_UPDATE\_INTERCEPTED | 应用程序更新拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_RECOVER\_INTERCEPTED | 应用程序恢复拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_APP\_START\_INTERCEPTED | 应用程序开始拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_USB\_ACCESS\_INTERCEPTED | USB访问拦截事件。 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_SMB\_FILE\_SEND | SMB(Samba)外发事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_KIA\_PRE\_OPEN | KIA文件秒开事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_HDC\_DEBUG | HDC(HarmonyOS Device Connector)调测文件事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_HDC\_DEBUG\_INTERCEPTED | HDC(HarmonyOS Device Connector)调测拦截事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_USER\_SPACE\_DATA\_TRANSFER | 多用户空间数据互传事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_USER\_SPACE\_DATA\_TRANSFER\_POLICY | 多用户空间互换审核策略事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_SERIAL\_PORT\_ACCESS | 串口访问审计事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_NETWORK\_INTERCEPTED | 网络拦截事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_WIFI\_INTERCEPTED | WI-FI拦截事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PRINT\_INTERCEPTED | 打印拦截事件  起始版本：6.1.0(23) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS\_PRIVILEGE\_ESCALATION | 进程提权事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS\_DEBUG\_ABNORMAL | 进程异常调试事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FS\_MOUNT\_ABNORMAL | 系统目录异常挂载事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_PROCESS\_CRASH\_ABNORMAL | 进程异常崩溃事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_CS\_VERIFY\_NULL | 应用代码未签名事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_CS\_VERIFY\_ABNORMAL | 应用代码验签异常事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DRIVER\_CS\_ABNORMAL | 驱动代码验签异常事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DRIVER\_MMAP\_ABNORMAL | 驱动非法映射内核内存事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_KERNEL\_MEMORY\_ABNORMAL | 内核内存异常使用事件  起始版本：6.1.1(24) |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SHARE | 文件分享事件  起始版本：26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DATA\_DRAG | 数据拖拽事件  起始版本：26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DLP\_FILE\_ACCESS | DLP文件访问  起始版本：26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_CREATE | 文件创建事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_OPEN | 文件打开事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_CLOSE | 文件关闭事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_DELETE | 文件删除事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_RENAME | 文件重命名事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_COPY | 文件复制事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SETOWNER | 文件修改所有者事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SETMODE | 文件修改mode事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_SETEXTATTR | 文件设置扩展属性事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_DELETEEXTATTR | 文件删除扩展属性事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_FILE\_WRITE | 文件写事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_BLUETOOTH\_INTERCEPTED | 蓝牙拦截事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DISC\_BURNING | 光盘刻录事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_MEDIA\_FILE\_ACCESS | 媒体文件访问事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_ACCOUNT\_MANAGEMENT | 账户管理事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DEVICE\_POWER\_ON | 设备开机事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_DEVICE\_POWER\_OFF | 设备关机事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_AUDIO\_INTERFACE\_ACCESS | 音频接口访问事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_VIDEO\_INTERFACE\_ACCESS | 视频接口访问事件。  **起始版本：** 26.0.0 |
| SECURITY\_AUDIT\_NOTIFY\_EVENT\_SERIAL\_PORT\_INTERCEPTED | 串口拦截事件。  **起始版本：** 26.0.0 |

## 函数说明

### HMS\_SecurityAudit\_AddAuthEventFilter()

```cpp
int32_t HMS_SecurityAudit_AddAuthEventFilter (const SecurityAudit_AuthClient * client, SecurityAudit_Auth_Event event, const SecurityAudit_Filter * filter )
```

**描述**

为阻断类事件添加过滤条件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 用户已创建的阻断类事件客户端。 |
| event | 需要添加过滤条件的阻断类事件。 |
| filter | 阻断类事件的过滤器描述。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果过滤器数量超过上限，则返回1012000004。 如果事件不支持过滤条件，则返回1012000005。

### HMS\_SecurityAudit\_AddFilter()

```cpp
int32_t HMS_SecurityAudit_AddFilter (const SecurityAudit_Client * client, SecurityAudit_Notify_Event event, const SecurityAudit_Filter * filter )
```

**描述**

为通知事件添加过滤条件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 用户已创建的通知类事件客户端。 |
| event | 通知要添加过滤条件的事件。 |
| filter | 通知事件的过滤器描述。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果过滤器数量超过上限，则返回1012000004。 如果事件不支持过滤条件，则返回1012000005。

### HMS\_SecurityAudit\_Auth()

```cpp
int32_t HMS_SecurityAudit_Auth (const SecurityAudit_AuthClient * client, const SecurityAudit_Event * event, SecurityAudit_AuthResult authResult )
```

**描述**

设置审计事件的阻断结果

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 用户已创建的阻断类事件客户端。 |
| event | 审计阻断类事件信息。 |
| authResult | 阻断结果。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_DeleteAuthClient()

```cpp
int32_t HMS_SecurityAudit_DeleteAuthClient (SecurityAudit_AuthClient * client)
```

**描述**

删除阻断类事件客户端。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 要删除的阻断类事件客户端实例。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_DeleteClient()

```cpp
int32_t HMS_SecurityAudit_DeleteClient (SecurityAudit_Client * client)
```

**描述**

删除通知客户端。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 要删除的客户端实例。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_NewAuthClient()

```cpp
int32_t HMS_SecurityAudit_NewAuthClient (SecurityAudit_AuthClient ** client, SecurityAudit_Handler handler )
```

**描述**

创建一个新的阻断类客户端。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 指向新阻断类事件客户端实例的指针，一个进程最大只允许创建2个client实例，当前设备最多只允许创建16个client实例。一个客户端实例最大只允许设置256条正过滤的过滤value和256条反过滤的过滤value。 |
| handler | 处理发送到此客户端的所有消息的处理器。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果客户端数量超过总上限，返回1012000002。 如果客户端数量超过当前进程的上限，则返回1012000003。

### HMS\_SecurityAudit\_NewClient()

```cpp
int32_t HMS_SecurityAudit_NewClient (SecurityAudit_Client ** client, SecurityAudit_Handler handler )
```

**描述**

创建一个新的通知事件客户端。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 指向新客户端实例的指针。 |
| handler | 处理发送到此客户端的所有消息的处理器。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果客户端数量超过总上限，返回1012000002。 如果客户端数量超过当前进程的上限，则返回1012000003。

### HMS\_SecurityAudit\_RemoveAuthEventFilter()

```cpp
int32_t HMS_SecurityAudit_RemoveAuthEventFilter (const SecurityAudit_AuthClient * client, SecurityAudit_Auth_Event event, const SecurityAudit_Filter * filter )
```

**描述**

删除阻断类事件的过滤条件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 客户已创建的阻断类事件客户端。 |
| event | 要删除过滤条件的阻断类事件。 |
| filter | 阻断类事件的过滤器描述。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果事件不支持过滤条件，则返回1012000005。

### HMS\_SecurityAudit\_RemoveFilter()

```cpp
int32_t HMS_SecurityAudit_RemoveFilter (const SecurityAudit_Client * client, SecurityAudit_Notify_Event event, const SecurityAudit_Filter * filter )
```

**描述**

删除通知事件的过滤条件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 客户已创建的通知类事件客户端。 |
| event | 通知要删除过滤条件的事件。 |
| filter | 通知事件的过滤器描述。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果事件不支持过滤条件，则返回1012000005。

### HMS\_SecurityAudit\_Subscribe()

```cpp
int32_t HMS_SecurityAudit_Subscribe (const SecurityAudit_Client * client, const SecurityAudit_Notify_Event * events, uint64_t count )
```

**描述**

订阅通知事件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 订阅通知事件的客户端。 |
| events | 要订阅的通知事件数组。 |
| count | 数组中的通知事件数。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_SubscribeAuthEvent()

```cpp
int32_t HMS_SecurityAudit_SubscribeAuthEvent (const SecurityAudit_AuthClient * client, const SecurityAudit_Auth_Event * events, uint64_t count )
```

**描述**

订阅阻断类事件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 客户已创建的阻断类事件客户端。 |
| events | 要订阅的阻断类事件数组。 |
| count | 数组中的阻断类事件数。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_Unsubscribe()

```cpp
int32_t HMS_SecurityAudit_Unsubscribe (const SecurityAudit_Client * client, const SecurityAudit_Notify_Event * events, uint64_t count )
```

**描述**

取消订阅通知事件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 取消订阅通知事件的客户端。 |
| events | 要取消订阅的通知事件数组。 |
| count | 数组中的通知事件数。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_UnsubscribeAuthEvent()

```cpp
int32_t HMS_SecurityAudit_UnsubscribeAuthEvent (const SecurityAudit_AuthClient * client, const SecurityAudit_Auth_Event * events, uint64_t count )
```

**描述**

取消订阅阻断类事件。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| client | 客户已创建的阻断类事件客户端。 |
| events | 要取消订阅的阻断类事件数组。 |
| count | 数组中的阻断类事件数。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001

### HMS\_SecurityAudit\_QueryAllProcesses()

```cpp
int32_t HMS_SecurityAudit_QueryAllProcesses(char** result)
```

**描述**

查询获取所有的应用进程信息。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| result | 查询获取到的应用进程信息。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_QueryProcesses()

```cpp
int32_t HMS_SecurityAudit_QueryProcesses(uint64_t* pids, uint64_t count, char** result)
```

**描述**

查询获取输入的pid的应用进程信息。

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 描述 |
| --- | --- |
| pids | 应用要查询的pid数组名。 |
| count | 应用要查询的pid数组元素个数。 |
| result | 查询获取到的应用进程信息。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。如果要查询的pid数组元素个数超过限制，则返回1012000006。

### HMS\_SecurityAudit\_AcquireCodeSign()

```cpp
int32_t HMS_SecurityAudit_AcquireCodeSign(char* path, char** outOwnedResult)
```

**描述**

获取输入的文件路径的代码签名信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**起始版本：** 6.1.1(24)

**参数：**

| 名称 | 描述 |
| --- | --- |
| path | 待查询的应用文件路径。 |
| outOwnedResult | 代码签名内容，内容为json格式字符串。例如：{"1": {}}。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。如果文件未找到或者应用无打开文件权限，则返回1012000008。

### HMS\_SecurityAudit\_AcquireAllClientsInfo()

```cpp
int32_t HMS_SecurityAudit_AcquireAllClientsInfo(char** outOwnedResult)
```

**描述**

查询获取全量通知类客户端信息。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| outOwnedResult | 查询获取到的全量通知类客户端信息。 |

**Permission：**

ohos.permission.QUERY\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_CreateAuthClientConfiguration()

```cpp
int32_t HMS_SecurityAudit_CreateAuthClientConfiguration(SecurityAudit_AuthClientConfiguration** outOwnedConfiguration)
```

**描述**

创建阻断类事件客户端配置对象。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| outOwnedConfiguration | 指向创建的阻断类事件客户端配置对象的指针。 |

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果发生内部错误，则返回1012000001。

**使用说明：**

创建的配置对象需要调用HMS\_SecurityAudit\_DestroyAuthClientConfiguration释放。

### HMS\_SecurityAudit\_DestroyAuthClientConfiguration()

```cpp
int32_t HMS_SecurityAudit_DestroyAuthClientConfiguration(SecurityAudit_AuthClientConfiguration* configuration)
```

**描述**

销毁阻断类事件客户端配置对象。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| configuration | 要销毁的阻断类事件客户端配置对象。 |

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。

### HMS\_SecurityAudit\_AuthClientConfiguration\_SetTimeoutAuthResult()

```cpp
int32_t HMS_SecurityAudit_AuthClientConfiguration_SetTimeoutAuthResult(SecurityAudit_AuthClientConfiguration* configuration, SecurityAudit_AuthResult authResult)
```

**描述**

设置超时默认阻断结果。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| configuration | 阻断类事件客户端配置对象。 |
| authResult | 超时后的默认授权结果。 |

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果发生内部错误，则返回1012000001。

### HMS\_SecurityAudit\_NewAuthClientWithConfiguration()

```cpp
int32_t HMS_SecurityAudit_NewAuthClientWithConfiguration(SecurityAudit_AuthClient** outOwnedClient, SecurityAudit_Handler handler, const SecurityAudit_AuthClientConfiguration* configuration)
```

**描述**

创建一个新的阻断类客户端（可配置超时默认阻断策略）。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| outOwnedClient | 指向新阻断类事件客户端实例的指针。 |
| handler | 处理发送到此客户端的所有消息的处理器。 |
| configuration | 授权客户端配置对象，用于配置超时默认阻断策略。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。 如果客户端数量超过总上限，返回1012000002。 如果客户端数量超过当前进程的上限，则返回1012000003。 如果配置无效，则返回1012000004。

### HMS\_SecurityAudit\_AcquireAllAuthClientsInfo()

```cpp
int32_t HMS_SecurityAudit_AcquireAllAuthClientsInfo(char** outOwnedResult)
```

**描述**

查询获取全量阻断类客户端信息。

**起始版本：** 26.0.0

**参数：**

| 名称 | 描述 |
| --- | --- |
| outOwnedResult | 查询获取到的全量阻断类客户端信息。 |

**Permission：**

ohos.permission.kernel.AUTH\_AUDIT\_EVENT

**返回：**

函数执行结果。 返回值说明： 如果操作成功，则返回0。 如果权限验证失败，则返回201。 如果发生内部错误，则返回1012000001。
