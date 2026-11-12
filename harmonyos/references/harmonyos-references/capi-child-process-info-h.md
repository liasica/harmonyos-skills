---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-child-process-info-h
title: child_process_info.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > child_process_info.h
category: harmonyos-references
scraped_at: 2026-11-12T09:53:36+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8549be31c91eddbeb8c6ab954ca41625eb6e209c0c9c8e6516fbb9977902758d
---

## 概述

定义子进程信息类型和访问器函数，用于从应用内子进程信息集合中按索引获取单个子进程信息句柄，并支持获取子进程的PID、父进程PID、进程名，以及释放子进程信息集合。

**引用文件：** <AbilityKit/ability\_runtime/child\_process\_info.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 26.0.1

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AbilityRuntime\_ChildProcessInfo](capi-nativechildprocess-info.md) | OH\_AbilityRuntime\_ChildProcessInfoHandle | 指向子进程信息的句柄。 |
| [OH\_AbilityRuntime\_ChildProcessInfos](capi-nativechildprocess-infos.md) | OH\_AbilityRuntime\_ChildProcessInfosHandle | 指向子进程信息集合的句柄。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetChildProcessInfoByIndex(OH\_AbilityRuntime\_ChildProcessInfosHandle infos, uint32\_t index, OH\_AbilityRuntime\_ChildProcessInfoHandle \*info)](capi-child-process-info-h.md#oh_abilityruntime_getchildprocessinfobyindex) | 按索引从子进程信息集合中获取特定子进程信息句柄。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ChildProcessInfo\_GetPid(OH\_AbilityRuntime\_ChildProcessInfoHandle info, int32\_t \*pid)](capi-child-process-info-h.md#oh_abilityruntime_childprocessinfo_getpid) | 获取子进程的PID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ChildProcessInfo\_GetParentPid(OH\_AbilityRuntime\_ChildProcessInfoHandle info, int32\_t \*parentPid)](capi-child-process-info-h.md#oh_abilityruntime_childprocessinfo_getparentpid) | 获取子进程的父进程PID。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ChildProcessInfo\_GetProcessName(OH\_AbilityRuntime\_ChildProcessInfoHandle info, char \*processName, uint32\_t processNameSize, uint32\_t \*requiredSize)](capi-child-process-info-h.md#oh_abilityruntime_childprocessinfo_getprocessname) | 获取子进程的进程名。 |
| [void OH\_AbilityRuntime\_ReleaseChildProcessInfos(OH\_AbilityRuntime\_ChildProcessInfosHandle \*infos)](capi-child-process-info-h.md#oh_abilityruntime_releasechildprocessinfos) | 释放子进程信息集合。 |

## 函数说明

### OH\_AbilityRuntime\_GetChildProcessInfoByIndex()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetChildProcessInfoByIndex(OH_AbilityRuntime_ChildProcessInfosHandle infos, uint32_t index, OH_AbilityRuntime_ChildProcessInfoHandle *info)
```

**描述**

按索引从子进程信息集合中获取特定子进程信息句柄。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ChildProcessInfosHandle](capi-nativechildprocess-infos.md) infos | 应用内所有子进程的信息集合。 |
| uint32\_t index | 要获取的子进程信息的索引，必须严格小于子进程总数。 |
| [OH\_AbilityRuntime\_ChildProcessInfoHandle](capi-nativechildprocess-info.md) \*info | 输出对应索引处的单个子进程信息句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 传入的参数无效。 |

### OH\_AbilityRuntime\_ChildProcessInfo\_GetPid()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ChildProcessInfo_GetPid(OH_AbilityRuntime_ChildProcessInfoHandle info, int32_t *pid)
```

**描述**

获取子进程的PID。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ChildProcessInfoHandle](capi-nativechildprocess-info.md) info | 子进程信息句柄，不能为空。 |
| int32\_t \*pid | 指向子进程PID的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 表示接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 传入的参数无效。 |

### OH\_AbilityRuntime\_ChildProcessInfo\_GetParentPid()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ChildProcessInfo_GetParentPid(OH_AbilityRuntime_ChildProcessInfoHandle info, int32_t *parentPid)
```

**描述**

获取子进程的父进程PID。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ChildProcessInfoHandle](capi-nativechildprocess-info.md) info | 子进程信息句柄，不能为空。 |
| int32\_t \*parentPid | 指向父进程PID的指针，不能为空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - 传入的参数无效。 |

### OH\_AbilityRuntime\_ChildProcessInfo\_GetProcessName()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ChildProcessInfo_GetProcessName(OH_AbilityRuntime_ChildProcessInfoHandle info, char *processName, uint32_t processNameSize, uint32_t *requiredSize)
```

**描述**

获取子进程的进程名。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ChildProcessInfoHandle](capi-nativechildprocess-info.md) info | 子进程信息句柄，不能为空指针。 |
| char \*processName | 用于接收进程名的缓冲区。 |
| uint32\_t processNameSize | 缓冲区大小（字节），包含结尾的空字符。 |
| uint32\_t \*requiredSize | 实际所需大小（字节），包含结尾的空字符。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR - 接口调用成功。  ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID - processName、info或requiredSize为空指针，或者processNameSize为0。  ABILITY\_RUNTIME\_ERROR\_CODE\_BUFFER\_TOO\_SMALL - 缓冲区过小。 |

### OH\_AbilityRuntime\_ReleaseChildProcessInfos()

```c
void OH_AbilityRuntime_ReleaseChildProcessInfos(OH_AbilityRuntime_ChildProcessInfosHandle *infos)
```

**描述**

释放子进程信息集合。

**起始版本：** 26.0.1

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ChildProcessInfosHandle](capi-nativechildprocess-infos.md) \*infos | 待释放的子进程信息集合，不能为空。释放后句柄将被置为NULL。 |
