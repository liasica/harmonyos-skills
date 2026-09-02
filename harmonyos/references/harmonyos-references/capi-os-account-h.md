---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-h
title: os_account.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > os_account.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0cd6ceb05567f3f2094a60dbd90c31f5b85dbcfa91387990f9bf63d71936f4b0
---

## 概述

声明访问和管理系统账号信息的API。

**库：** libos\_account\_ndk.so

**引用文件：** <BasicServicesKit/os\_account.h>

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**相关模块：** [OsAccount](capi-osaccount.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [OsAccount\_ErrCode OH\_OsAccount\_GetName(char \*buffer, size\_t buffer\_size)](capi-os-account-h.md#oh_osaccount_getname) | 获取调用方进程所属的系统账号的名称。 |
| [OsAccount\_ErrCode OH\_OsAccount\_GetNameByLocalId(int32\_t localId, char \*name, size\_t name\_size)](capi-os-account-h.md#oh_osaccount_getnamebylocalid) | 根据本地ID获取目标系统账号的名称。 |

## 函数说明

### OH\_OsAccount\_GetName()

```c
OsAccount_ErrCode OH_OsAccount_GetName(char *buffer, size_t buffer_size)
```

**描述**

获取调用方进程所属的系统账号的名称。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*buffer | 名称字符数组，其应具有能够存放名称和结束字符（'\0'）的空间，且最大长度为LOGIN\_NAME\_MAX。 |
| size\_t buffer\_size | 名称字符数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OsAccount\_ErrCode](capi-os-account-common-h.md#osaccount_errcode) | OS\_ACCOUNT\_ERR\_OK：操作成功。  OS\_ACCOUNT\_ERR\_INTERNAL\_ERROR：内部错误。  OS\_ACCOUNT\_ERR\_INVALID\_PARAMETER：表示buffer为空指针或名称长度（包括结束字符'\0'）大于buffer\_size。 |

### OH\_OsAccount\_GetNameByLocalId()

```c
OsAccount_ErrCode OH_OsAccount_GetNameByLocalId(int32_t localId, char *name, size_t name_size)
```

**描述**

根据本地ID获取目标系统账号的名称。

**需要权限：** ohos.permission.GET\_LOCAL\_ACCOUNT\_IDENTIFIERS

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int32\_t localId | 目标系统账号的本地ID。 |
| char \*name | 名称字符数组，其应具有能够存放名称和结束字符（'\0'）的空间，最大长度为LOGIN\_NAME\_MAX。 |
| size\_t name\_size | 名称字符数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OsAccount\_ErrCode](capi-os-account-common-h.md#osaccount_errcode) | OS\_ACCOUNT\_ERR\_OK：操作成功。  OS\_ACCOUNT\_ERR\_PERMISSION\_DENIED：权限被拒绝。  OS\_ACCOUNT\_ERR\_INTERNAL\_ERROR：内部错误。  OS\_ACCOUNT\_ERR\_INVALID\_PARAMETER：name为空指针或名称长度（包括结束字符'\0'）大于name\_size。  OS\_ACCOUNT\_ERR\_ACCOUNT\_NOT\_FOUND：未找到账号。  OS\_ACCOUNT\_ERR\_RESTRICTED\_ACCOUNT：账号受限。 |
