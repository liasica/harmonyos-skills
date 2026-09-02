---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-base-common-h
title: ability_base_common.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > ability_base_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b4caeb9326b1fa607af07d9922b02eb8b27a2e020418f8e23400bb5c775d4d44
---

## 概述

声明AbilityBase定义的相关错误码。

**引用文件**：<AbilityKit/ability\_base/ability\_base\_common.h>

**库：** libability\_base\_want.so

**系统能力：** SystemCapability.Ability.AbilityBase

**起始版本：** 15

**相关模块：** [AbilityBase](capi-abilitybase.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityBase\_ErrorCode](capi-ability-base-common-h.md#abilitybase_errorcode) | AbilityBase\_ErrorCode | AbilityBase相关错误码枚举。 |

## 枚举类型说明

### AbilityBase\_ErrorCode

```c
enum AbilityBase_ErrorCode
```

**描述**

AbilityBase相关错误码枚举。

**起始版本：** 15

| 枚举项 | 描述 |
| --- | --- |
| ABILITY\_BASE\_ERROR\_CODE\_NO\_ERROR = 0 | 操作成功。 |
| ABILITY\_BASE\_ERROR\_CODE\_PARAM\_INVALID = 401 | 非法入参。 |
