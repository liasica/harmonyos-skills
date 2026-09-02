---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-ability-wrapper-h
title: native_ability_wrapper.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > native_ability_wrapper.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:36+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:60b188daeb1ee3c562f8428bf116fa684052a362f8e47ea1e42bc26a55ddf9b8
---

## 概述

提供NativeAbility数据信息相关接口，用于获取Ability实例ID、Ability名称和napi\_env等信息。

**引用文件：** <AbilityKit/ability\_runtime/native\_ability\_wrapper.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_NativeAbilityWrapper](capi-abilityruntime-nativeabilitywrapper.md) | AbilityRuntime\_NativeAbilityWrapper | NativeAbility数据信息结构体类型。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetAbilityInstanceId(const AbilityRuntime\_NativeAbilityWrapper\* nativeAbilityWrapper, char\* buffer, const int32\_t bufferSize)](capi-native-ability-wrapper-h.md#oh_abilityruntime_getabilityinstanceid) | 从NativeAbility数据信息中获取Ability实例ID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetAbilityName(const AbilityRuntime\_NativeAbilityWrapper \*nativeAbilityWrapper, char \*buffer, const int32\_t bufferSize, int32\_t \*writeLength)](capi-native-ability-wrapper-h.md#oh_abilityruntime_getabilityname) | 从NativeAbility数据信息中获取Ability名称。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetEnv(const AbilityRuntime\_NativeAbilityWrapper\* nativeAbilityWrapper, napi\_env\* env)](capi-native-ability-wrapper-h.md#oh_abilityruntime_getenv) | 从NativeAbility数据信息中获取napi\_env。 |

## 函数说明

### OH\_AbilityRuntime\_GetAbilityInstanceId()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetAbilityInstanceId(
    const AbilityRuntime_NativeAbilityWrapper* nativeAbilityWrapper,
    char* buffer,
    const int32_t bufferSize)
```

**描述**

从NativeAbility数据信息中获取Ability实例ID。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_NativeAbilityWrapper](capi-abilityruntime-nativeabilitywrapper.md)\* nativeAbilityWrapper | NativeAbility数据信息指针。 |
| char\* buffer | 接收实例ID字符串的缓冲区指针。实例ID为UUID格式，长度为37字节。 |
| int32\_t bufferSize | 缓冲区长度，必须至少为37字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回错误码。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示操作成功。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示nativeAbilityWrapper或buffer为空指针，或bufferSize小于37。 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/native_ability_wrapper.h>
#include <AbilityKit/ability_runtime/ability_runtime_common.h>

void GetAbilityInstanceId(const AbilityRuntime_NativeAbilityWrapper* wrapper)
{
    if (wrapper == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }
    // buffer中存储了UUID格式的Ability实例ID
    char buffer[37] = {0};
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetAbilityInstanceId(wrapper, buffer, 37);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
        return;
    }
}
```

### OH\_AbilityRuntime\_GetAbilityName()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetAbilityName(
    const AbilityRuntime_NativeAbilityWrapper *nativeAbilityWrapper,
    char *buffer,
    const int32_t bufferSize,
    int32_t *writeLength)
```

**描述**

从NativeAbility数据信息中获取Ability名称。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_NativeAbilityWrapper](capi-abilityruntime-nativeabilitywrapper.md)\* nativeAbilityWrapper | NativeAbility数据信息指针。 |
| char\* buffer | 接收Ability名称字符串的缓冲区指针。传入nullptr可查询Ability名称长度。 |
| int32\_t bufferSize | 缓冲区长度（字节）。确保缓冲区至少有额外一个字节用于'\0'。 |
| int32\_t\* writeLength | 输出Ability名称字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回错误码。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示操作成功。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示nativeAbilityWrapper或writeLength为空指针，或缓冲区太小无法存储Ability名称。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_ABILITY\_WRAPPER\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示NativeAbility数据信息无效或不完整。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示内部错误。 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/native_ability_wrapper.h>
#include <AbilityKit/ability_runtime/ability_runtime_common.h>

void GetAbilityName(const AbilityRuntime_NativeAbilityWrapper* wrapper)
{
    if (wrapper == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    const int32_t bufferSize = 256; // 根据实际需要调整缓冲区大小
    char buffer[bufferSize] = {0};
    int32_t writeLength = 0;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetAbilityName(wrapper, buffer, bufferSize, &writeLength);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
        return;
    }
}
```

### OH\_AbilityRuntime\_GetEnv()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetEnv(
    const AbilityRuntime_NativeAbilityWrapper* nativeAbilityWrapper,
    napi_env* env)
```

**描述**

从NativeAbility数据信息中获取napi\_env。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_NativeAbilityWrapper](capi-abilityruntime-nativeabilitywrapper.md)\* nativeAbilityWrapper | NativeAbility数据信息指针。 |
| napi\_env\* env | 接收napi\_env值的指针。napi\_env在进程终止前一直有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回错误码。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示操作成功。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示nativeAbilityWrapper或env为空指针。  返回[ABILITY\_RUNTIME\_ERROR\_CODE\_ABILITY\_WRAPPER\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode)表示NativeAbility数据信息无效或不完整。 |

**示例代码：**

```cpp
#include <AbilityKit/ability_runtime/native_ability_wrapper.h>
#include <AbilityKit/ability_runtime/ability_runtime_common.h>
#include <napi/native_api.h>

void GetEnv(const AbilityRuntime_NativeAbilityWrapper* wrapper)
{
    if (wrapper == nullptr) {
        // 记录错误日志以及其他业务处理
        return;
    }

    napi_env env = nullptr;
    AbilityRuntime_ErrorCode err = OH_AbilityRuntime_GetEnv(wrapper, &env);
    if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
        return;
    }
}
```
