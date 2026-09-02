---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-access-control-h
title: ability_access_control.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > ability_access_control.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:69b73db6e4a39ccd724e0f05590071107150f1caf35596a7f8f6cda2e8caa8bd
---

## 概述

声明管理进程访问控制的接口。

**库：** ability\_access\_control.so

**引用文件：** <accesstoken/ability\_access\_control.h>

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**相关模块：** [AbilityAccessControl](capi-abilityaccesscontrol.md)

## 汇总

### 函数

| 名称 | 描述 |
| --- | --- |
| [bool OH\_AT\_CheckSelfPermission(const char \*permission)](capi-ability-access-control-h.md#oh_at_checkselfpermission) | 校验应用是否被授予指定的权限。 |

## 函数说明

### OH\_AT\_CheckSelfPermission()

```c
bool OH_AT_CheckSelfPermission(const char *permission)
```

**描述**

校验应用是否被授予指定的权限。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*permission | 需要校验的权限名称，合法的权限名取值可在应用权限列表中查询。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | true：应用已经被授予该权限。  false：应用未被授予该权限。 |
