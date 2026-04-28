---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-dlp-permission-api-h
title: dlp_permission_api.h
breadcrumb: API参考 > 系统 > 安全 > Data Protection Kit（数据保护服务） > C API > 头文件 > dlp_permission_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:09+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:fc0500d09ae9c300d3a11e2593a44fda281642f182e3433e7bfbe9019085fe9b
---

## 概述

PhonePC/2in1TabletTV

声明用于跨设备的文件的权限管理、加密存储、授权访问等能力的接口。

**库：** libohdlp\_permission.so

**引用文件：** <DataProtectionKit/dlp\_permission\_api.h>

**系统能力：** SystemCapability.Security.DataLossPrevention

**起始版本：** 14

**相关模块：** [DlpPermissionApi](capi-dlppermissionapi.md)

## 汇总

PhonePC/2in1TabletTV

### 枚举

PhonePC/2in1TabletTV

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | DLP\_ErrCode | DLP错误码的枚举。 |
| [DLP\_FileAccess](capi-dlp-permission-api-h.md#dlp_fileaccess) | DLP\_FileAccess | DLP文件授权类型的枚举。 |

### 函数

PhonePC/2in1TabletTV

| 名称 | 描述 |
| --- | --- |
| [DLP\_ErrCode OH\_DLP\_GetDlpPermissionInfo(DLP\_FileAccess \*dlpFileAccess, uint32\_t \*flags)](capi-dlp-permission-api-h.md#oh_dlp_getdlppermissioninfo) | 查询当前DLP沙箱的权限信息。 |
| [DLP\_ErrCode OH\_DLP\_GetOriginalFileName(const char \*fileName, char \*\*originalFileName)](capi-dlp-permission-api-h.md#oh_dlp_getoriginalfilename) | 获取指定DLP文件名的原始文件名。 |
| [DLP\_ErrCode OH\_DLP\_IsInSandbox(bool \*isInSandbox)](capi-dlp-permission-api-h.md#oh_dlp_isinsandbox) | 查询当前应用是否运行在DLP沙箱环境。 |
| [DLP\_ErrCode OH\_DLP\_SetSandboxAppConfig(const char \*configInfo)](capi-dlp-permission-api-h.md#oh_dlp_setsandboxappconfig) | 设置沙箱应用配置信息。 |
| [DLP\_ErrCode OH\_DLP\_GetSandboxAppConfig(char \*\*configInfo)](capi-dlp-permission-api-h.md#oh_dlp_getsandboxappconfig) | 获取沙箱应用配置信息。 |
| [DLP\_ErrCode OH\_DLP\_CleanSandboxAppConfig()](capi-dlp-permission-api-h.md#oh_dlp_cleansandboxappconfig) | 清理沙箱应用配置信息。 |

## 枚举类型说明

PhonePC/2in1TabletTV

### DLP\_ErrCode

PhonePC/2in1TabletTV

```
1. enum DLP_ErrCode
```

**描述**

DLP错误码的枚举。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| ERR\_OH\_SUCCESS = 0 | 表示操作成功。 |
| ERR\_OH\_INVALID\_PARAMETER = 19100001 | 表示入参错误。 |
| ERR\_OH\_API\_ONLY\_FOR\_SANDBOX = 19100006 | 表示非DLP沙箱应用。 |
| ERR\_OH\_API\_NOT\_FOR\_SANDBOX = 19100007 | 表示DLP沙箱应用不允许调用此接口。 |
| ERR\_OH\_SYSTEM\_SERVICE\_EXCEPTION = 19100011 | 表示系统服务工作异常。 |
| ERR\_OH\_OUT\_OF\_MEMORY = 19100012 | 表示内存申请失败。 |
| ERR\_OH\_APPLICATION\_NOT\_AUTHORIZED = 19100018 | 表示应用未授权。 |

### DLP\_FileAccess

PhonePC/2in1TabletTV

```
1. enum DLP_FileAccess
```

**描述**

DLP文件授权类型的枚举。

**起始版本：** 14

| 枚举项 | 描述 |
| --- | --- |
| NO\_PERMISSION = 0 | 表示无文件权限。 |
| READ\_ONLY = 1 | 表示文件的只读权限。 |
| CONTENT\_EDIT = 2 | 表示文件的编辑权限。 |
| FULL\_CONTROL = 3 | 表示文件的完全控制权限。 |

## 函数说明

PhonePC/2in1TabletTV

### OH\_DLP\_GetDlpPermissionInfo()

PhonePC/2in1TabletTV

```
1. DLP_ErrCode OH_DLP_GetDlpPermissionInfo(DLP_FileAccess *dlpFileAccess, uint32_t *flags)
```

**描述**

查询当前DLP沙箱的权限信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [DLP\_FileAccess](capi-dlp-permission-api-h.md#dlp_fileaccess) \*dlpFileAccess | 表示DLP文件针对用户的授权类型，例如：只读。 |
| uint32\_t \*flags | 表示DLP文件的详细操作权限，操作权限的具体含义为：  0x00000000-表示无文件权限。  0x00000001-表示文件的查看权限。  0x00000002-表示文件的保存权限。  0x00000004-表示文件的另存为权限。  0x00000008-表示文件的编辑权限。  0x00000010-表示文件的截屏权限。  0x00000020-表示文件的共享屏幕权限。  0x00000040-表示文件的录屏权限。  0x00000080-表示文件的复制权限。  0x00000100-表示文件的打印权限。  0x00000200-表示文件的导出权限。  0x00000400-表示文件的修改文件权限。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | 0 - 操作成功。  19100001 - 入参错误。  19100006 - 非DLP沙箱应用。  19100011 - 系统服务工作异常。  19100012 - 内存申请失败。 |

### OH\_DLP\_GetOriginalFileName()

PhonePC/2in1TabletTV

```
1. DLP_ErrCode OH_DLP_GetOriginalFileName(const char *fileName, char **originalFileName)
```

**描述**

获取指定DLP文件名的原始文件名。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*fileName | 指定要查询的文件名。 |
| char \*\*originalFileName | DLP文件的原始文件名。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | 0 - 操作成功。  19100001 - 入参错误。  19100012 - 内存申请失败。 |

### OH\_DLP\_IsInSandbox()

PhonePC/2in1TabletTV

```
1. DLP_ErrCode OH_DLP_IsInSandbox(bool *isInSandbox)
```

**描述**

查询当前应用是否运行在DLP沙箱环境。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool \*isInSandbox | true表示当前应用运行在DLP沙箱环境，false表示当前应用不是运行在DLP沙箱环境。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | 0 - 操作成功。  19100011 - 系统服务工作异常。  19100012 - 内存申请失败。 |

### OH\_DLP\_SetSandboxAppConfig()

PhonePC/2in1TabletTV

```
1. DLP_ErrCode OH_DLP_SetSandboxAppConfig(const char *configInfo)
```

**描述**

设置沙箱应用配置信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*configInfo | 沙箱应用配置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | 0 - 操作成功。  19100001 - 入参错误。  19100007 - DLP沙箱应用不允许调用此接口。  19100011 - 系统服务工作异常。  19100018 - 应用未授权。 |

### OH\_DLP\_GetSandboxAppConfig()

PhonePC/2in1TabletTV

```
1. DLP_ErrCode OH_DLP_GetSandboxAppConfig(char **configInfo)
```

**描述**

获取沙箱应用配置信息。

**起始版本：** 14

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*\*configInfo | 沙箱应用配置信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | 0 - 操作成功。  19100011 - 系统服务工作异常。  19100012 - 内存申请失败。  19100018 - 应用未授权。 |

### OH\_DLP\_CleanSandboxAppConfig()

PhonePC/2in1TabletTV

```
1. DLP_ErrCode OH_DLP_CleanSandboxAppConfig()
```

**描述**

清理沙箱应用配置信息。

**起始版本：** 14

**返回：**

| 类型 | 说明 |
| --- | --- |
| [DLP\_ErrCode](capi-dlp-permission-api-h.md#dlp_errcode) | 0 - 操作成功。  19100007 - DLP沙箱应用不允许调用此接口。  19100011 - 系统服务工作异常。  19100018 - 应用未授权。 |
