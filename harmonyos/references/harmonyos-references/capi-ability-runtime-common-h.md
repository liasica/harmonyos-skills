---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ability-runtime-common-h
title: ability_runtime_common.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > ability_runtime_common.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d638887876b32c9dcc3759d89252567dd853bc8e59ba6c20a06908c525c2c2e8
---

## 概述

声明AbilityRuntime模块的错误码。

**引用文件：** <AbilityKit/ability\_runtime/ability\_runtime\_common.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 13

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | AbilityRuntime\_ErrorCode | AbilityRuntime模块的错误码的枚举。 |

## 枚举类型说明

### AbilityRuntime\_ErrorCode

```c
enum AbilityRuntime_ErrorCode
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
| ABILITY\_RUNTIME\_ERROR\_CODE\_VISIBILITY\_VERIFICATION\_FAILED = 16000004 | 无法启动不可见组件。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_STATIC\_CFG\_PERMISSION = 16000005 | 指定进程无相应权限。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_USER\_OPERATION = 16000006 | 不允许跨用户操作。  **起始版本：** 26.0.0 |
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
| ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_RUNNING\_ABILITIES\_WITH\_UI = 16000170 | 目标应用无正在运行的带界面的Ability。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_RATE\_LIMIT = 16000171 | API调用频率过高，超出限流阈值。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_CONNECTION\_NUMBER\_LIMIT = 16000172 | 连接数超过上限。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_PROPERTY\_NOT\_FOUND = 16000173 | 未找到请求的接口、方法、枚举、结构体成员和容器（数组、向量、集合和映射）的元素成员。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_TYPE\_MISMATCH = 16000174 | 运行时值类型与期望的元数据类型不匹配。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_SEND\_REQUEST\_FAILED = 16000175 | 向远端服务发送IPC请求失败。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP\_IN\_PROCESS = 16000176 | 在[OH\_ABILITY\_RUNTIME\_LAUNCH\_MODE\_IN\_PROCESS](capi-modular-object-extension-manager-h.md#oh_abilityruntime_launchmode)模式下，调用方与目标Ability不在同一应用。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_ABILITY\_WRAPPER\_INVALID = 16000177 | NativeAbility数据信息无效或不完整。  **起始版本：** 26.0.0 |
| ABILITY\_RUNTIME\_ERROR\_CODE\_METADATA\_INVALID = 16000178 | 类型库元数据无效。  **起始版本：** 26.0.0 |
