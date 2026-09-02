---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-manager-h
title: modular_object_extension_manager.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > modular_object_extension_manager.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bc6009876471797fb268e0dc14cccc1f03bb500bef48c1bab6e4d7df76a85aa7
---

## 概述

声明用于管理ModularObjectExtensionAbility的接口，包括查询ModularObjectExtensionAbility信息、连接与断开连接等能力。开发者可以通过本模块提供的接口查询当前应用内所有已注册的ModularObjectExtensionAbility的信息（包括启动模式、进程模式、线程模式、组件名称及禁用状态等），并根据需要建立或断开与ModularObjectExtensionAbility的通信连接。

**引用文件：** <AbilityKit/ability\_runtime/modular\_object\_extension\_manager.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AbilityRuntime\_ModularObjectExtensionInfo\*](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) | OH\_AbilityRuntime\_ModObjExtensionInfoHandle | 表示单个ModularObjectExtensionAbility的信息句柄。该句柄指向一个ModularObjectExtensionAbility的完整信息，包含启动模式、进程模式、线程模式、组件名称（[AbilityBase\_Element](capi-abilitybase-element.md)）以及禁用状态等属性。 |
| [OH\_AbilityRuntime\_AllModularObjectExtensionInfos\*](capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h.md) | OH\_AbilityRuntime\_AllModObjExtensionInfosHandle | 表示当前应用内所有ModularObjectExtensionAbility信息的集合句柄。该句柄指向一个包含多个[OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md)的集合，可通过[OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos)获取集合中元素的数量，并通过[OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex)按索引遍历获取单个ModularObjectExtensionAbility信息。使用完毕后需通过[OH\_AbilityRuntime\_ReleaseAllExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_releaseallextensioninfos)释放该集合。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AbilityRuntime\_LaunchMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_launchmode) | OH\_AbilityRuntime\_LaunchMode | 定义ModularObjectExtensionAbility的启动模式。 |
| [OH\_AbilityRuntime\_ProcessMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_processmode) | OH\_AbilityRuntime\_ProcessMode | 定义ModularObjectExtensionAbility的进程模式。 |
| [OH\_AbilityRuntime\_ThreadMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_threadmode) | OH\_AbilityRuntime\_ThreadMode | 定义ModularObjectExtensionAbility的线程模式。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetModularObjectExtensionInfoLaunchMode(OH\_AbilityRuntime\_ModObjExtensionInfoHandle extensionInfo, OH\_AbilityRuntime\_LaunchMode \*launchMode)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodularobjectextensioninfolaunchmode) | 从指定的ModularObjectExtensionAbility信息中获取启动模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetModularObjectExtensionInfoProcessMode(OH\_AbilityRuntime\_ModObjExtensionInfoHandle extensionInfo, OH\_AbilityRuntime\_ProcessMode \*processMode)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodularobjectextensioninfoprocessmode) | 从指定的ModularObjectExtensionAbility信息中获取进程模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetModularObjectExtensionInfoThreadMode(OH\_AbilityRuntime\_ModObjExtensionInfoHandle extensionInfo, OH\_AbilityRuntime\_ThreadMode \*threadMode)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodularobjectextensioninfothreadmode) | 从指定的ModularObjectExtensionAbility信息中获取线程模式。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetModularObjectExtensionInfoElementName(OH\_AbilityRuntime\_ModObjExtensionInfoHandle extensionInfo, AbilityBase\_Element \*element)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodularobjectextensioninfoelementname) | 从指定的ModularObjectExtensionAbility信息中获取组件名称（[AbilityBase\_Element](capi-abilitybase-element.md)）。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetModularObjectExtensionInfoDisableState(OH\_AbilityRuntime\_ModObjExtensionInfoHandle extensionInfo, bool \*isDisabled)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodularobjectextensioninfodisablestate) | 从指定的ModularObjectExtensionAbility信息中获取禁用状态。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_AcquireSelfModularObjectExtensionInfos(OH\_AbilityRuntime\_AllModObjExtensionInfosHandle \*outOwnedAllExtensionInfos)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_acquireselfmodularobjectextensioninfos) | 获取当前应用所有已注册的ModularObjectExtensionAbility信息。该接口返回一个包含当前应用所有已注册的ModularObjectExtensionAbility信息集合句柄。开发者可通过[OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos)和[OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex)遍历集合中的各个ModularObjectExtensionAbility信息，进而获取每个ModularObjectExtensionAbility的启动模式、进程模式、线程模式等属性。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ReleaseAllExtensionInfos(OH\_AbilityRuntime\_AllModObjExtensionInfosHandle \*allExtensionInfos)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_releaseallextensioninfos) | 释放由[OH\_AbilityRuntime\_AcquireSelfModularObjectExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_acquireselfmodularobjectextensioninfos)获取的ModularObjectExtensionAbility信息集合。当不再需要使用ModularObjectExtensionAbility信息集合时，必须调用此接口释放相关资源，避免内存泄漏。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos(OH\_AbilityRuntime\_AllModObjExtensionInfosHandle allExtensionInfos, size\_t \*count)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos) | 获取ModularObjectExtensionAbility信息集合中包含的ModularObjectExtensionAbility信息数量。返回的数量可用于确定遍历集合时的索引上限，配合[OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex)逐个访问集合中的ModularObjectExtensionAbility信息。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex(OH\_AbilityRuntime\_AllModObjExtensionInfosHandle allExtensionInfos, size\_t index, OH\_AbilityRuntime\_ModObjExtensionInfoHandle \*extensionInfo)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex) | 根据索引从ModularObjectExtensionAbility信息集合中获取指定的ModularObjectExtensionAbility信息。索引的有效范围为[0, count)，其中count可通过[OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos)获取。获取到的ModularObjectExtensionAbility信息句柄可用于查询该ModularObjectExtensionAbility的启动模式、进程模式、线程模式等属性。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ConnectModularObjectExtensionAbility(AbilityBase\_Want \*want, OH\_AbilityRuntime\_ConnectOptions \*connectOptions, int64\_t \*connectionId)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_connectmodularobjectextensionability) | 连接ModularObjectExtensionAbility。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_DisconnectModularObjectExtensionAbility(int64\_t connectionId)](capi-modular-object-extension-manager-h.md#oh_abilityruntime_disconnectmodularobjectextensionability) | 断开与ModularObjectExtensionAbility的连接。 |

## 枚举类型说明

### OH\_AbilityRuntime\_LaunchMode

```c
enum OH_AbilityRuntime_LaunchMode
```

**描述**

定义ModularObjectExtensionAbility的启动模式。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ABILITY\_RUNTIME\_LAUNCH\_MODE\_IN\_PROCESS = 0 | 表示ModularObjectExtensionAbility将在调用方（客户端）进程中启动。在此模式下，ModularObjectExtensionAbility与调用方共享同一个进程，适用于对进程隔离无要求的场景。 |
| OH\_ABILITY\_RUNTIME\_LAUNCH\_MODE\_CROSS\_PROCESS = 1 | 表示ModularObjectExtensionAbility允许跨进程启动。在此模式下，ModularObjectExtensionAbility运行在独立的进程中，与调用方进程隔离，适用于需要进程级隔离以提高稳定性和安全性的场景。 |

### OH\_AbilityRuntime\_ProcessMode

```c
enum OH_AbilityRuntime_ProcessMode
```

**描述**

定义ModularObjectExtensionAbility的进程模式。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ABILITY\_RUNTIME\_PROCESS\_MODE\_BUNDLE = 0 | 表示同一应用下的所有ModularObjectExtensionAbility实例共享一个进程。所有实例运行在同一进程中，减少系统资源消耗。 |
| OH\_ABILITY\_RUNTIME\_PROCESS\_MODE\_TYPE = 1 | 表示Ability名称相同的ModularObjectExtensionAbility实例共享一个进程。具有相同Ability名称的ModularObjectExtensionAbility实例被分配到同一进程中，不同Ability名称的实例运行在不同进程中。 |
| OH\_ABILITY\_RUNTIME\_PROCESS\_MODE\_INSTANCE = 2 | 表示每个ModularObjectExtensionAbility实例独占一个进程。每个ModularObjectExtensionAbility实例拥有独立的进程空间，实现最大程度的进程隔离，适用于对稳定性和安全性要求极高的场景。 |

### OH\_AbilityRuntime\_ThreadMode

```c
enum OH_AbilityRuntime_ThreadMode
```

**描述**

定义ModularObjectExtensionAbility的线程模式。

**起始版本：** 26.0.0

| 枚举项 | 描述 |
| --- | --- |
| OH\_ABILITY\_RUNTIME\_THREAD\_MODE\_BUNDLE = 0 | 表示同一应用下的所有ModularObjectExtensionAbility实例共享一个线程。所有实例在同一线程中依次执行，资源开销最小，但需注意避免单实例阻塞影响其他实例。 |
| OH\_ABILITY\_RUNTIME\_THREAD\_MODE\_TYPE = 1 | 表示Ability名称相同的ModularObjectExtensionAbility实例共享一个线程。具有相同Ability名称的ModularObjectExtensionAbility实例共享线程，不同Ability名称的实例使用不同线程，在资源消耗与并发性能之间取得平衡。 |
| OH\_ABILITY\_RUNTIME\_THREAD\_MODE\_INSTANCE = 2 | 表示每个ModularObjectExtensionAbility实例独占一个线程。每个ModularObjectExtensionAbility实例拥有独立的线程，互不干扰，适用于需要高并发或对响应时间有严格要求的场景。 |

## 函数说明

### OH\_AbilityRuntime\_GetModularObjectExtensionInfoLaunchMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetModularObjectExtensionInfoLaunchMode(OH_AbilityRuntime_ModObjExtensionInfoHandle extensionInfo, OH_AbilityRuntime_LaunchMode *launchMode)
```

**描述**

从指定的ModularObjectExtensionAbility信息中获取启动模式。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) extensionInfo | 目标ModularObjectExtensionAbility的信息句柄。 |
| [OH\_AbilityRuntime\_LaunchMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_launchmode) \*launchMode | 指向[OH\_AbilityRuntime\_LaunchMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_launchmode)的指针，用于接收启动模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) extensionInfo或launchMode为空。 |

### OH\_AbilityRuntime\_GetModularObjectExtensionInfoProcessMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetModularObjectExtensionInfoProcessMode(OH_AbilityRuntime_ModObjExtensionInfoHandle extensionInfo, OH_AbilityRuntime_ProcessMode *processMode)
```

**描述**

从指定的ModularObjectExtensionAbility信息中获取进程模式。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) extensionInfo | 目标ModularObjectExtensionAbility的信息句柄。 |
| [OH\_AbilityRuntime\_ProcessMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_processmode) \*processMode | 指向[OH\_AbilityRuntime\_ProcessMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_processmode)的指针，用于接收进程模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) extensionInfo或processMode为空。 |

### OH\_AbilityRuntime\_GetModularObjectExtensionInfoThreadMode()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetModularObjectExtensionInfoThreadMode(OH_AbilityRuntime_ModObjExtensionInfoHandle extensionInfo, OH_AbilityRuntime_ThreadMode *threadMode)
```

**描述**

从指定的ModularObjectExtensionAbility信息中获取线程模式。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) extensionInfo | 目标ModularObjectExtensionAbility的信息句柄。 |
| [OH\_AbilityRuntime\_ThreadMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_threadmode) \*threadMode | 指向[OH\_AbilityRuntime\_ThreadMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_threadmode)的指针，用于接收线程模式。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) extensionInfo或threadMode为空。 |

### OH\_AbilityRuntime\_GetModularObjectExtensionInfoElementName()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetModularObjectExtensionInfoElementName(OH_AbilityRuntime_ModObjExtensionInfoHandle extensionInfo, AbilityBase_Element *element)
```

**描述**

从指定的ModularObjectExtensionAbility信息中获取组件名称（[AbilityBase\_Element](capi-abilitybase-element.md)）。element中的bundleName、moduleName、abilityName为非拥有型指针，指向extensionInfo内部数据，请勿单独释放，仅在extensionInfo有效期间可用。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) extensionInfo | 目标ModularObjectExtensionAbility的信息句柄。 |
| [AbilityBase\_Element](capi-abilitybase-element.md) \*element | 指向[AbilityBase\_Element](capi-abilitybase-element.md)的指针，用于接收组件名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) extensionInfo或element为空。 |

### OH\_AbilityRuntime\_GetModularObjectExtensionInfoDisableState()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetModularObjectExtensionInfoDisableState(OH_AbilityRuntime_ModObjExtensionInfoHandle extensionInfo, bool *isDisabled)
```

**描述**

从指定的ModularObjectExtensionAbility信息中获取禁用状态。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) extensionInfo | 目标ModularObjectExtensionAbility的信息句柄。 |
| bool \*isDisabled | 指向布尔值的指针，用于接收禁用状态。true表示已禁用，不允许其他应用连接；false表示未禁用，允许其他应用连接。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) extensionInfo或isDisabled为空。 |

### OH\_AbilityRuntime\_AcquireSelfModularObjectExtensionInfos()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_AcquireSelfModularObjectExtensionInfos(OH_AbilityRuntime_AllModObjExtensionInfosHandle *outOwnedAllExtensionInfos)
```

**描述**

获取当前应用所有已注册的ModularObjectExtensionAbility信息，返回ModularObjectExtensionAbility信息集合句柄。通过[OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos)获取集合元素数量，使用[OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex)按索引遍历各个ModularObjectExtensionAbility信息，获取启动模式、进程模式、线程模式等属性。使用完毕后需调用[OH\_AbilityRuntime\_ReleaseAllExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_releaseallextensioninfos)释放以避免内存泄漏。

**起始版本：** 26.0.0

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_AllModObjExtensionInfosHandle](capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h.md) \*outOwnedAllExtensionInfos | 指向[OH\_AbilityRuntime\_AllModObjExtensionInfosHandle](capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h.md)的指针，用于接收ModularObjectExtensionAbility信息集合。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) outOwnedAllExtensionInfos为空。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 设备不支持该操作。 |

### OH\_AbilityRuntime\_ReleaseAllExtensionInfos()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ReleaseAllExtensionInfos(OH_AbilityRuntime_AllModObjExtensionInfosHandle *allExtensionInfos)
```

**描述**

释放由[OH\_AbilityRuntime\_AcquireSelfModularObjectExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_acquireselfmodularobjectextensioninfos)获取的ModularObjectExtensionAbility信息集合。当不再需要使用ModularObjectExtensionAbility信息集合时，必须调用此接口释放相关资源，避免内存泄漏。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_AllModObjExtensionInfosHandle](capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h.md) \*allExtensionInfos | 指向需要释放的ModularObjectExtensionAbility信息集合句柄的指针。释放后该指针将被置空。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) allExtensionInfos为空。 |

**参考：**

[OH\_AbilityRuntime\_AcquireSelfModularObjectExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_acquireselfmodularobjectextensioninfos)

### OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetCountFromAllModObjExtensionInfos(OH_AbilityRuntime_AllModObjExtensionInfosHandle allExtensionInfos, size_t *count)
```

**描述**

获取ModularObjectExtensionAbility信息集合中包含的ModularObjectExtensionAbility信息数量。返回的数量可用于确定遍历集合时的索引上限，配合[OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex)逐个访问集合中的ModularObjectExtensionAbility信息。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_AllModObjExtensionInfosHandle](capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h.md) allExtensionInfos | ModularObjectExtensionAbility信息集合句柄。 |
| size\_t \*count | 指向size\_t的指针，用于接收ModularObjectExtensionAbility信息的数量。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) allExtensionInfos或count为空。 |

### OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_GetModObjExtensionInfoByIndex(OH_AbilityRuntime_AllModObjExtensionInfosHandle allExtensionInfos, size_t index, OH_AbilityRuntime_ModObjExtensionInfoHandle *extensionInfo)
```

**描述**

根据索引从ModularObjectExtensionAbility信息集合中获取指定的ModularObjectExtensionAbility信息。索引的有效范围为[0, count)，其中count可通过[OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos)获取。获取到的ModularObjectExtensionAbility信息句柄可用于查询该ModularObjectExtensionAbility的启动模式、进程模式、线程模式等属性。返回的extensionInfo为非拥有型句柄，指向allExtensionInfos集合内部存储，请勿单独释放，仅在allExtensionInfos有效期间可用。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_AllModObjExtensionInfosHandle](capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h.md) allExtensionInfos | ModularObjectExtensionAbility信息集合句柄。 |
| size\_t index | 目标ModularObjectExtensionAbility信息在集合中的索引，必须小于集合包含的ModularObjectExtensionAbility信息数量。 |
| [OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) \*extensionInfo | 指向[OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md)的指针，用于接收指定索引处的ModularObjectExtensionAbility信息句柄。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) allExtensionInfos或extensionInfo为空，  或index大于等于集合中ModularObjectExtensionAbility信息数量。 |

### OH\_AbilityRuntime\_ConnectModularObjectExtensionAbility()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ConnectModularObjectExtensionAbility(AbilityBase_Want *want, OH_AbilityRuntime_ConnectOptions *connectOptions, int64_t *connectionId)
```

**描述**

连接ModularObjectExtensionAbility。

**起始版本：** 26.0.0

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED错误码。

**参数：**

| 参数项 | 描述 |
| --- | --- |
| AbilityBase\_Want \*want | 连接ModularObjectExtensionAbility需要的Want信息。详细内容参考[AbilityBase\_Want](capi-abilitybase-want.md)。 |
| OH\_AbilityRuntime\_ConnectOptions \*connectOptions | 连接选项。详细内容参考[OH\_AbilityRuntime\_ConnectOptions](capi-abilityruntime-oh-abilityruntime-connectoptions.md)。 |
| int64\_t \*connectionId | 指向int64\_t的指针，用于接收连接ID。可以在后续调用[OH\_AbilityRuntime\_DisconnectModularObjectExtensionAbility](capi-modular-object-extension-manager-h.md#oh_abilityruntime_disconnectmodularobjectextensionability)时使用。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 传入参数无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 设备不支持连接ModularObjectExtensionAbility。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 目标Ability不存在。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE](capi-ability-runtime-common-h.md#abilityruntime_errorcode) Ability类型不正确。  [ABILITY\_RUNTIME\_ERROR\_CODE\_VISIBILITY\_VERIFICATION\_FAILED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 无法启动不可见组件。  [ABILITY\_RUNTIME\_ERROR\_CODE\_STATIC\_CFG\_PERMISSION](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 指定进程无相应权限。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_USER\_OPERATION](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不允许跨用户操作。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 众测应用已过期。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 内部错误。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方进程不在前台。  [ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 同名Ability的实例数超过20个。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_RUNNING\_ABILITIES\_WITH\_UI](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 目标应用无正在运行的UIAbility或UIExtensionAbility。  [ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_RATE\_LIMIT](capi-ability-runtime-common-h.md#abilityruntime_errorcode) API调用频率过高，超过每秒20次。  [ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_CONNECTION\_NUMBER\_LIMIT](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 同一进程最多连接5个同名的Ability。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP\_IN\_PROCESS](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 在[OH\_ABILITY\_RUNTIME\_LAUNCH\_MODE\_IN\_PROCESS](capi-modular-object-extension-manager-h.md#oh_abilityruntime_launchmode)模式下，调用方与目标Ability不在同一应用。 |

### OH\_AbilityRuntime\_DisconnectModularObjectExtensionAbility()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_DisconnectModularObjectExtensionAbility(int64_t connectionId)
```

**描述**

断开与ModularObjectExtensionAbility的连接。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| int64\_t connectionId | 表示连接ID。由[OH\_AbilityRuntime\_ConnectModularObjectExtensionAbility](capi-modular-object-extension-manager-h.md#oh_abilityruntime_connectmodularobjectextensionability)返回。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 传入参数无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 内部错误。 |
