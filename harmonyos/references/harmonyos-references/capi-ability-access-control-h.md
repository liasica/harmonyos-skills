---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-access-control-h
title: ability_access_control.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > ability_access_control.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:57+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ab3032ced17406f497207231fd3e26e28c7aaed2ca152737db5022cfef51abd2
---

## 概述

PhonePC/2in1TabletTVWearable

声明管理进程访问控制的接口。

**库：** ability\_access\_control.so

**引用文件：** <accesstoken/ability\_access\_control.h>

**系统能力：** SystemCapability.Security.AccessToken

**起始版本：** 12

**相关模块：** [AbilityAccessControl](capi-abilityaccesscontrol.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [bool OH\_AT\_CheckSelfPermission(const char \*permission)](capi-ability-access-control-h.md#oh_at_checkselfpermission) | 校验应用是否被授予指定的权限。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AT\_CheckSelfPermission()

PhonePC/2in1TabletTVWearable

```
1. bool OH_AT_CheckSelfPermission(const char *permission)
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
