---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-application-context-h
title: application_context.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > application_context.h
category: harmonyos-references
scraped_at: 2026-04-28T07:58:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4f2fd471ec6b810d73ce8d49b77ad381e8f3872a96a4d0c8d04af7c2a3746a8c
---

## 概述

PhonePC/2in1TabletTVWearable

提供应用级别上下文相关的接口。

**引用文件：** <AbilityKit/ability\_runtime/application\_context.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 13

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetCacheDir(char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetcachedir) | 获取本应用的应用级的缓存目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetAreaMode(AbilityRuntime\_AreaMode\* areaMode)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetareamode) | 获取本应用的应用级的文件数据加密等级。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetBundleName(char\* buffer, int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetbundlename) | 获取应用包名。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetTempDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgettempdir) | 获取本应用的应用级的临时文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetFilesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetfilesdir) | 获取本应用的应用级的通用文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetDatabaseDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetdatabasedir) | 获取本应用的应用级的数据库文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetPreferencesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetpreferencesdir) | 获取本应用的应用级的首选项文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetBundleCodeDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetbundlecodedir) | 获取本应用的应用级的安装文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetDistributedFilesDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetdistributedfilesdir) | 获取本应用的应用级的分布式文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetCloudFileDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetcloudfiledir) | 获取本应用的应用级的云文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLogFileDir(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetlogfiledir) | 获取本应用的应用级的日志文件目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetResourceDir(const char\* moduleName, char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetresourcedir) | 获取应用级别的资源目录。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbility(AbilityBase\_Want \*want)](capi-application-context-h.md#oh_abilityruntime_startselfuiability) | 启动当前应用的UIAbility。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbilityWithStartOptions(AbilityBase\_Want \*want,AbilityRuntime\_StartOptions \*options)](capi-application-context-h.md#oh_abilityruntime_startselfuiabilitywithstartoptions) | 通过StartOptions启动当前应用的UIAbility。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetVersionCode(int64\_t\* versionCode)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetversioncode) | 获取应用版本号。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_StartSelfUIAbilityWithPidResult(AbilityBase\_Want \*want, AbilityRuntime\_StartOptions \*options, int32\_t \*targetPid)](capi-application-context-h.md#oh_abilityruntime_startselfuiabilitywithpidresult) | 通过StartOptions启动当前应用的UIAbility，并获取目标UIAbility的进程号。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLaunchParameter(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetlaunchparameter) | 获取本应用首次启动UIAbility的WantParams参数。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ApplicationContextGetLatestParameter(char\* buffer, const int32\_t bufferSize, int32\_t\* writeLength)](capi-application-context-h.md#oh_abilityruntime_applicationcontextgetlatestparameter) | 获取本应用最近一次启动UIAbility的WantParams参数。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_AbilityRuntime\_ApplicationContextGetCacheDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetCacheDir(char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的缓存目录。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收本应用的应用级的缓存目录。 |
| int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetAreaMode()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetAreaMode(AbilityRuntime_AreaMode* areaMode)
```

**描述**

获取本应用的应用级的文件数据加密等级。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityRuntime\_AreaMode](capi-context-constant-h.md#abilityruntime_areamode)\* areaMode | 指向接收数据加密等级的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - areaMode为null。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetBundleName()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetBundleName(char* buffer, int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取应用包名。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收应用包名。 |
| int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetTempDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetTempDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的临时文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收临时文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetFilesDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetFilesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的通用文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收通用文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetDatabaseDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetDatabaseDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的数据库文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收数据库文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetPreferencesDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetPreferencesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的首选项文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收首选项文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetBundleCodeDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetBundleCodeDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的安装文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收安装文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetDistributedFilesDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetDistributedFilesDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的分布式文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收分布式文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetCloudFileDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetCloudFileDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的云文件目录。

**起始版本：** 16

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收云文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetLogFileDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLogFileDir(char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的日志文件目录。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收日志文件目录。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_ApplicationContextGetResourceDir()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetResourceDir(const char* moduleName, char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用的应用级的资源目录。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* moduleName | 模块名。 |
| char\* buffer | 指向缓冲区的指针，用于接收资源目录。 |
| int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入到缓冲区的字符串长度，单位为字节。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

### OH\_AbilityRuntime\_StartSelfUIAbility()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbility(AbilityBase_Want *want)
```

**描述**

启动当前应用的UIAbility。

**需要权限：** ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**起始版本：** 15

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动当前应用UIAbility时需要的Want信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED - 调用方权限校验失败。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 调用方入参校验失败。  ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED - 设备类型不支持。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY - 指定的Ability名称不存在。  ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE - 接口调用Ability类型错误。  ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED - 众测应用到期。  ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE - Wukong模式，不允许启动/停止Ability。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED - 应用被管控。  ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED - 应用被EDM管控。  ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP - 限制API 11以上版本三方应用跳转。  ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL - 内部错误。  ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY - 非顶层应用。  ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED - 应用多实例已达到上限（从API17开始）。  ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED - 不允许设置APP\_INSTANCE\_KEY（从API17开始）。  详细内容参考AbilityRuntime\_ErrorCode。 |

**示例代码：**

```
1. #include <AbilityKit/ability_base/want.h>
2. #include <AbilityKit/ability_runtime/application_context.h>

4. void startSelfUIAbilityTest()
5. {
6. AbilityBase_Element element;
7. element.abilityName = const_cast<char*>("EntryAbility");
8. element.bundleName = const_cast<char*>("com.example.myapplication");
9. element.moduleName = const_cast<char*>("entry");
10. AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);

12. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_StartSelfUIAbility(want);
13. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
14. // 记录错误日志以及其他业务处理
15. return;
16. }
17. // 销毁want，防止内存泄漏
18. OH_AbilityBase_DestroyWant(want);
19. }
```

### OH\_AbilityRuntime\_StartSelfUIAbilityWithStartOptions()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbilityWithStartOptions(AbilityBase_Want *want,AbilityRuntime_StartOptions *options)
```

**描述**

通过StartOptions启动当前应用的UIAbility。

**需要权限：** ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**起始版本：** 17

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动当前应用UIAbility时需要的Want信息。 |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*options | 启动当前应用UIAbility时需要的StartOptions信息。如果该参数中[startVisibility](capi-context-constant-h.md#abilityruntime_startvisibility)属性的值不为空，必须确保当前应用已添加到状态栏，否则会返回[ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode)错误码。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED - 调用方权限校验失败。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 调用方入参校验失败。  ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED - 设备类型不支持。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY - 指定的Ability名称不存在。  ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE - 接口调用Ability类型错误。  ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED - 众测应用到期。  ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE - Wukong模式，不允许启动/停止Ability。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED - 应用被管控。  ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED - 应用被EDM管控。  ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP - 限制API 11以上版本三方应用跳转。  ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL - 内部错误。  ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY - 非顶层应用。  ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED - 不允许设置窗口启动可见性。  ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED - 不支持应用分身和多实例。  ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY - 无效多实例。  ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED - 应用多实例已达到上限。  ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED - 不支持应用多实例。  ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED - 不允许设置APP\_INSTANCE\_KEY。  详细内容参考AbilityRuntime\_ErrorCode。 |

**示例代码：**

```
1. #include <AbilityKit/ability_base/want.h>
2. #include <AbilityKit/ability_runtime/application_context.h>

4. void demo()
5. {
6. AbilityBase_Element element;
7. element.abilityName = const_cast<char*>("EntryAbility");
8. element.bundleName = const_cast<char*>("com.example.myapplication");
9. element.moduleName = const_cast<char*>("entry");
10. AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);
11. if (want == nullptr) {
12. // 记录错误日志以及其他业务处理
13. return;
14. }

16. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
17. if (options == nullptr) {
18. // 记录错误日志以及其他业务处理

20. // 销毁want，防止内存泄漏
21. OH_AbilityBase_DestroyWant(want);
22. return;
23. }
24. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_StartSelfUIAbilityWithStartOptions(want, options);
25. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
26. // 记录错误日志以及其他业务处理
27. }
28. // 销毁want，防止内存泄漏
29. OH_AbilityBase_DestroyWant(want);

31. // 销毁options，防止内存泄漏
32. OH_AbilityRuntime_DestroyStartOptions(&options);
33. }
```

### OH\_AbilityRuntime\_ApplicationContextGetVersionCode()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetVersionCode(int64_t* versionCode)
```

**描述**

获取应用版本号。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t\* [versionCode](js-apis-bundlemanager-bundleinfo.md#bundleinfo-1) | 指向应用包版本号的指针，对应bundleInfo中的versionCode字段。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参versionCode为空。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。  ABILITY\_RUNTIME\_ERROR\_CODE\_GET\_APPLICATION\_INFO\_FAILED - 获取应用信息失败。 |

### OH\_AbilityRuntime\_StartSelfUIAbilityWithPidResult()

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_StartSelfUIAbilityWithPidResult(AbilityBase_Want *want, AbilityRuntime_StartOptions *options, int32_t *targetPid)
```

**描述**

通过StartOptions启动当前应用的UIAbility，并获取目标UIAbility的进程号。

接口不能在应用主线程调用，但可以在应用创建的[子进程](capi-childprocess.md)的主线程中调用。

如果在应用的主线程中调用，会返回ABILITY\_RUNTIME\_ERROR\_CODE\_MAIN\_THREAD\_NOT\_SUPPORTED错误码。

**需要权限：** ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**起始版本：** 21

**设备行为差异**：该接口仅在2in1和Tablet设备中可正常调用，在其他设备中返回ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动当前应用UIAbility时需要的Want信息。 |
| [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*options | 启动当前应用UIAbility时需要的StartOptions信息。如果该参数中[startVisibility](capi-context-constant-h.md#abilityruntime_startvisibility)属性的值不为空，必须确保当前应用已添加到状态栏，否则会返回[ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode)错误码。 |
| int32\_t \*targetPid | 目标UIAbility所在的进程号，作为出参使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED - 调用方权限校验失败。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 调用方入参校验失败。  ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED - 设备类型不支持。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY - 指定的Ability名称不存在。  ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE - 接口调用Ability类型错误。  ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED - 众测应用到期。  ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE - Wukong模式，不允许启动/停止Ability。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED - 应用被管控。  ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED - 应用被EDM管控。  ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP - 限制API 11以上版本三方应用跳转。  ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL - 内部错误。  ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY - 非顶层应用。  ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED - 不允许设置窗口启动可见性。  ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED - 不支持应用分身和多实例。  ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY - 无效多实例。  ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED - 应用多实例已达到上限。  ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED - 不支持应用多实例。  ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED - 不允许设置APP\_INSTANCE\_KEY。  ABILITY\_RUNTIME\_ERROR\_CODE\_START\_TIMEOUT - 启动UIAbility超时。  ABILITY\_RUNTIME\_ERROR\_CODE\_MAIN\_THREAD\_NOT\_SUPPORTED - 接口不允许在应用主线程被调用。 |

**示例代码：**

```
1. #include <AbilityKit/ability_base/want.h>
2. #include <AbilityKit/ability_runtime/application_context.h>

4. void demo()
5. {
6. AbilityBase_Element element;
7. element.abilityName = const_cast<char*>("EntryAbility");
8. element.bundleName = const_cast<char*>("com.example.myapplication");
9. element.moduleName = const_cast<char*>("entry");
10. AbilityBase_Want* want = OH_AbilityBase_CreateWant(element);
11. if (want == nullptr) {
12. // 记录错误日志以及其他业务处理
13. return;
14. }

16. AbilityRuntime_StartOptions* options = OH_AbilityRuntime_CreateStartOptions();
17. if (options == nullptr) {
18. // 记录错误日志以及其他业务处理

20. // 销毁want，防止内存泄漏
21. OH_AbilityBase_DestroyWant(want);
22. return;
23. }
24. int32_t pid = -1;
25. AbilityRuntime_ErrorCode err = OH_AbilityRuntime_StartSelfUIAbilityWithPidResult(want, options, &pid);
26. if (err != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
27. // 记录错误日志以及其他业务处理
28. }
29. // 销毁want，防止内存泄漏
30. OH_AbilityBase_DestroyWant(want);

32. // 销毁options，防止内存泄漏
33. OH_AbilityRuntime_DestroyStartOptions(&options);
34. }
```

### OH\_AbilityRuntime\_ApplicationContextGetLaunchParameter

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLaunchParameter(
2. char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用首次启动UIAbility时的WantParams参数，WantParams可参考[Want中的parameters参数](js-apis-inner-ability-want.md)。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收WantParams参数。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入缓冲区的字符串长度（单位：字节）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

**示例：**

```
1. #include "napi/native_api.h"
2. #include "AbilityKit/ability_runtime/application_context.h"

4. static napi_value GetLaunchParameter(napi_env env, napi_callback_info info)
5. {
6. const int32_t bufferSize = 2048; // 根据实际需要调整缓冲区大小
7. char buffer[bufferSize] = {0};
8. int32_t writeLength = 0;
9. int32_t ret = OH_AbilityRuntime_ApplicationContextGetLaunchParameter(buffer, bufferSize, &writeLength);

11. if (ret != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
12. // 失败处理
13. }
14. // 创建 JS 字符串返回WantParams
15. napi_value result;
16. napi_create_string_utf8(env, buffer, writeLength, &result);
17. return result;
18. }
```

### OH\_AbilityRuntime\_ApplicationContextGetLatestParameter

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextGetLatestParameter(
2. char* buffer, const int32_t bufferSize, int32_t* writeLength)
```

**描述**

获取本应用最近一次启动UIAbility时的WantParams参数，WantParams可参考[Want中的parameters参数](js-apis-inner-ability-want.md)。

**起始版本：** 21

**参数：**

| 参数项 | 描述 |
| --- | --- |
| char\* buffer | 指向缓冲区的指针，用于接收WantParams参数。 |
| const int32\_t bufferSize | 缓冲区大小，单位为字节。 |
| int32\_t\* writeLength | 在返回[ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode)时，表示实际写入缓冲区的字符串长度（单位：字节）。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 查询成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参buffer或者writeLength为空，或者缓冲区大小小于需要写入的大小。  ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST - 应用上下文不存在，如在应用创建的[子进程](capi-childprocess.md)中应用级别上下文不存在。 |

**示例：**

```
1. #include "napi/native_api.h"
2. #include "AbilityKit/ability_runtime/application_context.h"

4. static napi_value GetLatestParameter(napi_env env, napi_callback_info info)
5. {
6. const int32_t bufferSize = 2048; // 根据实际需要调整缓冲区大小
7. char buffer[bufferSize] = {0};
8. int32_t writeLength = 0;
9. int32_t ret = OH_AbilityRuntime_ApplicationContextGetLatestParameter(buffer, bufferSize, &writeLength);

11. if (ret != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
12. // 失败处理
13. }
14. // 创建 JS 字符串返回WantParams
15. napi_value result;
16. napi_create_string_utf8(env, buffer, writeLength, &result);
17. return result;
18. }
```

### OH\_AbilityRuntime\_ApplicationContextNotifyPageChanged

PhonePC/2in1TabletTVWearable

```
1. AbilityRuntime_ErrorCode OH_AbilityRuntime_ApplicationContextNotifyPageChanged(
2. const char* targetPageName, int32_t targetPageNameLength, int32_t windowId)
```

**描述**

该接口仅支持三方框架调用。三方框架每次切换页面时，将目标页面信息（包含目标页面路径、目标页面路径长度、目标页面对应的窗口ID）通知给系统。系统可按产品策略调整/恢复页面。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* targetPageName | 目标页面路径。 |
| int32\_t targetPageNameLength | 目标页面路径长度。 |
| int32\_t windowId | 目标页面对应的[窗口ID](arkts-apis-window-i.md#windowinfo18)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回执行结果。  ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 操作成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 入参targetPageName为空或者windowId无效。  ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL - 内部错误。 |

**示例：**

```
1. #include "napi/native_api.h"
2. #include "AbilityKit/ability_runtime/application_context.h"

4. static bool NotifyPageChanged(napi_env env, napi_callback_info info)
5. {
6. const char* testPageName = "https://home.taobao.com/homepage";
7. int32_t testPageNameLen = 32;
8. int32_t testWindowId = 12; // 示例数值仅供参考，实际开发需使用有效的窗口ID。
9. int32_t ret = OH_AbilityRuntime_ApplicationContextNotifyPageChanged(testPageName, testPageNameLen, testWindowId);

11. if (ret != ABILITY_RUNTIME_ERROR_CODE_NO_ERROR) {
12. // 失败处理
13. return false;
14. }
15. return true;
16. }
```
