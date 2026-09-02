---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-context-h
title: context.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > context.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:44cfe0eca4f3225a634ae6d05364a27a5fcdae5bbd272915dce166fbc7937bd9
---

## 概述

提供上下文数据结构[AbilityRuntime\_Context](capi-abilityruntime-abilityruntime-context.md)和相关接口用于获取当前上下文的应用文件路径、数据加密等级和进程名等信息。

**引用文件：** <AbilityKit/ability\_runtime/context.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 24

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [AbilityRuntime\_Context](capi-abilityruntime-abilityruntime-context.md) | - | 定义AbilityRuntime\_Context结构体类型。 |
| [AbilityRuntime\_Context\*](capi-abilityruntime-abilityruntime-context8h.md) | AbilityRuntime\_ContextHandle | 定义AbilityRuntime\_Context对象指针。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetCacheDir(AbilityRuntime\_ContextHandle context, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getcachedir) | 获取上下文的缓存目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetTempDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_gettempdir) | 获取上下文的临时文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetFilesDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getfilesdir) | 获取上下文的通用文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetDatabaseDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getdatabasedir) | 获取上下文的数据库文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetPreferencesDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getpreferencesdir) | 获取上下文的首选项文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetBundleCodeDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getbundlecodedir) | 获取上下文的安装文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetDistributedFilesDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getdistributedfilesdir) | 获取上下文的分布式文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetResourceDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getresourcedir) | 获取上下文的资源目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetCloudFileDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getcloudfiledir) | 获取上下文的云文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetAreaMode(AbilityRuntime\_ContextHandle context, AbilityRuntime\_AreaMode\* areaMode)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getareamode) | 获取上下文的数据加密等级。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_SetAreaMode(AbilityRuntime\_ContextHandle context, AbilityRuntime\_AreaMode areaMode)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_setareamode) | 设置上下文的数据加密等级。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetLogFileDir(AbilityRuntime\_ContextHandle context, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getlogfiledir) | 获取上下文的日志文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_Context\_GetProcessName(AbilityRuntime\_ContextHandle context, char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-abilityruntime-context-h.md#oh_abilityruntime_context_getprocessname) | 获取上下文所在的进程名称。 |

## 函数说明

### OH\_AbilityRuntime\_Context\_GetCacheDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetCacheDir(
    AbilityRuntime_ContextHandle context, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的缓存目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取缓存目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的缓存目录。 |
| int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetCacheDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t cacheDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetCacheDir(context, buffer, 1024, &cacheDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetTempDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetTempDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的临时文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取临时文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的临时文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetTempDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t tempDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetTempDir(context, buffer, 1024, &tempDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetFilesDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetFilesDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的通用文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取通用文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的通用文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetFilesDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t filesDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetFilesDir(context, buffer, 1024, &filesDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetDatabaseDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetDatabaseDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的数据库文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取数据库文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的数据库文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetDatabaseDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t databaseDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetDatabaseDir(context, buffer, 1024, &databaseDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetPreferencesDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetPreferencesDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的首选项文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取首选项文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的首选项文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetPreferencesDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t preferencesDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetPreferencesDir(context, buffer, 1024, &preferencesDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetBundleCodeDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetBundleCodeDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的安装文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取安装文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的安装文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetBundleCodeDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t bundleCodeDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetBundleCodeDir(context, buffer, 1024, &bundleCodeDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetDistributedFilesDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetDistributedFilesDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的分布式文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取分布式文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的分布式文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetDistributedFilesDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t distributedFilesDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetDistributedFilesDir(context, buffer, 1024, &distributedFilesDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetResourceDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetResourceDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的资源目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取资源目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的资源目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetResourceDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t resourceDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetResourceDir(context, buffer, 1024, &resourceDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetCloudFileDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetCloudFileDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的云文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取云文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的云文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetCloudFileDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t cloudFileDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetCloudFileDir(context, buffer, 1024, &cloudFileDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetAreaMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetAreaMode(
    AbilityRuntime_ContextHandle context, AbilityRuntime_AreaMode* areaMode)
```

**描述**

获取上下文的数据加密等级。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取数据加密等级的上下文。 |
| [AbilityRuntime\_AreaMode](capi-context-constant-h.md#abilityruntime_areamode)\* areaMode | 指向接收数据加密等级的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参areaMode为空。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetAreaMode(AbilityRuntime_ContextHandle context)
{
    AbilityRuntime_AreaMode areaMode;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetAreaMode(context, &areaMode);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_SetAreaMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_SetAreaMode(
    AbilityRuntime_ContextHandle context, AbilityRuntime_AreaMode areaMode)
```

**描述**

设置上下文的数据加密等级。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要设置数据加密等级的上下文。 |
| [AbilityRuntime\_AreaMode](capi-context-constant-h.md#abilityruntime_areamode) areaMode | 数据加密等级。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参context为空。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testSetAreaMode(AbilityRuntime_ContextHandle context)
{
    AbilityRuntime_AreaMode areaMode = ABILITY_RUNTIME_AREA_MODE_EL1;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_SetAreaMode(context, areaMode);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetLogFileDir()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetLogFileDir(
    AbilityRuntime_ContextHandle context, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文的日志文件目录。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取日志文件目录的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收上下文的日志文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetLogFileDir(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t logFileDirSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetLogFileDir(context, buffer, 1024, &logFileDirSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```

### OH\_AbilityRuntime\_Context\_GetProcessName()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_Context_GetProcessName(
    AbilityRuntime_ContextHandle context, char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取上下文所在的进程名称。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md) context | 要获取进程名称的上下文。 |
| char\* buffer | 指向缓冲区的指针，用于接收进程名称。 |
| int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或writeLength为空或context为空，或缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 上下文不存在。 |

**示例代码：**

```c
#include <AbilityKit/ability_runtime/context.h>

// 接收一个context 对象
void testGetProcessName(AbilityRuntime_ContextHandle context)
{
    char buffer[1024] = {0};
    int32_t processNameSize = 0;
    AbilityRuntime_ErrorCode errorCode = ABILITY_RUNTIME_ERROR_CODE_NO_ERROR;
    errorCode = OH_AbilityRuntime_Context_GetProcessName(context, buffer, 1024, &processNameSize);
    if (errorCode != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
        // 记录错误日志以及其他业务处理
    }
    // 正常业务处理
}
```
