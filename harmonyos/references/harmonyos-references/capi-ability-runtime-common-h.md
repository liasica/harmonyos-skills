---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h
title: ability_runtime_common.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > ability_runtime_common.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:58+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9fd93ac5980e1cf163b006b0c8599a6c6b96162c2b684dab350c185458849e52
---

## 概述

PhonePC/2in1TabletTVWearable

声明AbilityRuntime模块的错误码。

**引用文件：** <AbilityKit/ability\_runtime/ability\_runtime\_common.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 13

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | AbilityRuntime\_ErrorCode | AbilityRuntime模块的错误码的枚举。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### AbilityRuntime\_ErrorCode

PhonePC/2in1TabletTVWearable

```
1. enum AbilityRuntime_ErrorCode
```

**描述**

AbilityRuntime模块的错误码的枚举。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR = 0 | 操作成功。 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED = 201 | 权限校验失败。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID = 401 | 无效参数。 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED = 801 | 设备类型不支持。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY = 16000001 | 指定的Ability名称不存在。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE = 16000002 | 接口调用Ability类型错误。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED = 16000008 | 众测应用到期。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE = 16000009 | Wukong模式，不允许启动/停止Ability。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST = 16000011 | 上下文不存在。 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED = 16000012 | 应用被管控。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED = 16000013 | 应用被EDM管控。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP = 16000018 | 限制API 11以上版本三方应用跳转。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL = 16000050 | 内部错误。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY = 16000053 | 非顶层应用。  **起始版本：** 15 |
| ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED = 16000067 | 不允许设置窗口启动可见性。  **起始版本：** 17 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED = 16000072 | 不支持应用分身和多实例。  **起始版本：** 17 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY = 16000076 | 无效多实例。  **起始版本：** 17 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED = 16000077 | 应用多实例已达到上限。  **起始版本：** 17 |
| ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED = 16000078 | 不支持应用多实例。  **起始版本：** 17 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED = 16000079 | 不允许设置APP\_INSTANCE\_KEY。  **起始版本：** 17 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_GET\_APPLICATION\_INFO\_FAILED = 16000081 | 获取应用信息失败。  **起始版本：** 21 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_START\_TIMEOUT = 16000133 | 启动UIAbility超时。  **起始版本：** 21 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_MAIN\_THREAD\_NOT\_SUPPORTED = 16000134 | 接口不允许在应用主线程调用。  **起始版本：** 21 |
