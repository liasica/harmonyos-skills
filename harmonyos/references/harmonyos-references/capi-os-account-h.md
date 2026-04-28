---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-h
title: os_account.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > os_account.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:49+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a748448bf6f65006a5219aa567bf7967746b7500c92bbf9040ebba2c1d524d11
---

## 概述

PhonePC/2in1TabletTVWearable

声明访问和管理系统帐号信息的API。

**库：** libos\_account\_ndk.so

**引用文件：** <BasicServicesKit/os\_account.h>

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**相关模块：** [OsAccount](capi-osaccount.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [OsAccount\_ErrCode OH\_OsAccount\_GetName(char \*buffer, size\_t buffer\_size)](capi-os-account-h.md#oh_osaccount_getname) | 获取调用方进程所属的系统帐号的名称。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_OsAccount\_GetName()

PhonePC/2in1TabletTVWearable

```
1. OsAccount_ErrCode OH_OsAccount_GetName(char *buffer, size_t buffer_size)
```

**描述**

获取调用方进程所属的系统帐号的名称。

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char \*buffer | 名称字符数组，其应具有能够存放名称（最大长度为LOGIN\_NAME\_MAX）和结束字符（'\0'）的空间。 |
| size\_t buffer\_size | 名称字符数组的大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OsAccount\_ErrCode](capi-os-account-common-h.md#osaccount_errcode) | OS\_ACCOUNT\_ERR\_OK：表示成功。  OS\_ACCOUNT\_ERR\_INTERNAL\_ERROR：表示内部错误。  OS\_ACCOUNT\_ERR\_INVALID\_PARAMETER：表示buffer为NULL指针，或名称（不包括结束字符'\0'）的长度大于等于buffer\_size。 |
