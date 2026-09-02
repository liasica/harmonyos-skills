---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-os-account-common-h
title: os_account_common.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > os_account_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c2af5dad3b4f4648a9260c8648243b1dd6a6b4b1520df88d6790d0b3243139c8
---

## 概述

提供OsAccount接口的公共类型定义。

**库：** libos\_account\_ndk.so

**引用文件：** <BasicServicesKit/os\_account\_common.h>

**系统能力：** SystemCapability.Account.OsAccount

**起始版本：** 12

**相关模块：** [OsAccount](capi-osaccount.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OsAccount\_ErrCode](capi-os-account-common-h.md#osaccount_errcode) | OsAccount\_ErrCode | 枚举错误码。 |

## 枚举类型说明

### OsAccount\_ErrCode

```c
enum OsAccount_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| OS\_ACCOUNT\_ERR\_OK = 0 | 操作成功。 |
| OS\_ACCOUNT\_ERR\_PERMISSION\_DENIED = 201 | 没有权限。  **起始版本：** 26.0.0 |
| OS\_ACCOUNT\_ERR\_INTERNAL\_ERROR = 12300001 | 内部错误。 |
| OS\_ACCOUNT\_ERR\_INVALID\_PARAMETER = 12300002 | 无效的参数。 |
| OS\_ACCOUNT\_ERR\_ACCOUNT\_NOT\_FOUND = 12300003 | 账号不存在。  **起始版本：** 26.0.0 |
| OS\_ACCOUNT\_ERR\_RESTRICTED\_ACCOUNT = 12300008 | 受限账号。  **起始版本：** 26.0.0 |
