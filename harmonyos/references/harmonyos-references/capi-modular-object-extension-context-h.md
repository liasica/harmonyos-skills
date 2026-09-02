---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-modular-object-extension-context-h
title: modular_object_extension_context.h
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 头文件 > modular_object_extension_context.h
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:26430b8645418eb79d0b419a9a14c90912a87aedfe5113cc0389640f8174400b
---

## 概述

声明ModularObjectExtensionAbility的上下文接口，包括启动UIAbility、销毁ModularObjectExtensionAbility自身、创建和销毁IPC对象等功能。

**引用文件：** <AbilityKit/ability\_runtime/modular\_object\_extension\_context.h>

**库：** libability\_runtime.so

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_AbilityRuntime\_ModularObjectExtensionContext\*](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) | OH\_AbilityRuntime\_ModObjExtensionContextHandle | 表示ModularObjectExtensionAbility上下文的句柄。 |

### 函数

| 名称 | 描述 |
| --- | --- |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ModObjExtensionContext\_GetBaseContext(OH\_AbilityRuntime\_ModObjExtensionContextHandle modObjExtensionContext, AbilityRuntime\_ContextHandle\* baseContext)](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_getbasecontext) | 从ModularObjectExtensionAbility上下文中获取基础上下文。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ModObjExtensionContext\_StartSelfUIAbility(OH\_AbilityRuntime\_ModObjExtensionContextHandle context, const AbilityBase\_Want \*want)](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_startselfuiability) | 启动当前应用的UIAbility。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ModObjExtensionContext\_StartSelfUIAbilityWithStartOptions(OH\_AbilityRuntime\_ModObjExtensionContextHandle context, const AbilityBase\_Want \*want, const AbilityRuntime\_StartOptions \*options)](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_startselfuiabilitywithstartoptions) | 通过StartOptions启动当前应用的UIAbility。 |
| [AbilityRuntime\_ErrorCode OH\_AbilityRuntime\_ModObjExtensionContext\_TerminateSelf(OH\_AbilityRuntime\_ModObjExtensionContextHandle context)](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_terminateself) | 销毁ModularObjectExtensionAbility自身。 |
| [OHIPCRemoteStub\* OH\_AbilityRuntime\_ModObjExtensionContext\_CreateIPCRemoteStub(OH\_AbilityRuntime\_ModObjExtensionContextHandle context, const char \*descriptor, OH\_OnRemoteRequestCallback requestCallback, OH\_OnRemoteDestroyCallback destroyCallback, void \*userData)](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_createipcremotestub) | 创建一个OHIPCRemoteStub对象，回调函数将在ExtensionAbility指定的线程上运行。requestCallback和destroyCallback将在由ExtensionAbility的[OH\_AbilityRuntime\_ThreadMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_threadmode)决定的线程上按顺序执行。调用[OH\_AbilityRuntime\_ModObjExtensionContext\_DestroyIPCRemoteStub](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_destroyipcremotestub)后，不会再有新的requestCallback回调，且正在执行的requestCallback完成后才会回调destroyCallback。调用方需调用[OH\_AbilityRuntime\_ModObjExtensionContext\_DestroyIPCRemoteStub](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_destroyipcremotestub)销毁返回的对象，避免内存泄漏。 |
| [void OH\_AbilityRuntime\_ModObjExtensionContext\_DestroyIPCRemoteStub(OH\_AbilityRuntime\_ModObjExtensionContextHandle context, OHIPCRemoteStub \*stub)](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_destroyipcremotestub) | 销毁OHIPCRemoteStub对象。 |

## 函数说明

### OH\_AbilityRuntime\_ModObjExtensionContext\_GetBaseContext()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ModObjExtensionContext_GetBaseContext(OH_AbilityRuntime_ModObjExtensionContextHandle modObjExtensionContext, AbilityRuntime_ContextHandle* baseContext)
```

**描述**

从ModularObjectExtensionAbility上下文中获取基础上下文。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionContextHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) modObjExtensionContext | 指向ModularObjectExtensionAbility上下文的指针。 |
| AbilityRuntime\_ContextHandle\* baseContext | 指向[AbilityRuntime\_ContextHandle](capi-abilityruntime-abilityruntime-context8h.md)的指针，用于接收结果。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 参数校验失败。 |

### OH\_AbilityRuntime\_ModObjExtensionContext\_StartSelfUIAbility()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ModObjExtensionContext_StartSelfUIAbility(OH_AbilityRuntime_ModObjExtensionContextHandle context, const AbilityBase_Want *want)
```

**描述**

启动当前应用的UIAbility。

**需要权限：** ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionContextHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) context | 指向ModularObjectExtensionAbility上下文的指针。 |
| const [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动当前应用UIAbility时需要的Want信息。详细内容参考[AbilityBase\_Want](capi-abilitybase-want.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方无正确权限。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 传入参数无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 设备不支持启动当前应用的UIAbility。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 目标Ability不存在。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE](capi-ability-runtime-common-h.md#abilityruntime_errorcode) Ability类型不正确。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 众测应用已过期。  [ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 无法在Wukong模式下启动Ability。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用被管控。  [ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用被EDM管控。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方尝试启动不同应用。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 内部错误。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方进程不在前台。  [ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不支持应用分身和多实例。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用实例Key无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用实例数量已达上限。  [ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不支持应用多实例。  [ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不允许设置APP\_INSTANCE\_KEY。 |

### OH\_AbilityRuntime\_ModObjExtensionContext\_StartSelfUIAbilityWithStartOptions()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ModObjExtensionContext_StartSelfUIAbilityWithStartOptions(OH_AbilityRuntime_ModObjExtensionContextHandle context, const AbilityBase_Want *want, const AbilityRuntime_StartOptions *options)
```

**描述**

通过StartOptions启动当前应用的UIAbility。

**需要权限：** ohos.permission.NDK\_START\_SELF\_UI\_ABILITY

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionContextHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) context | 指向ModularObjectExtensionAbility上下文的指针。 |
| const [AbilityBase\_Want](capi-abilitybase-want.md) \*want | 启动当前应用UIAbility时需要的Want信息。详细内容参考[AbilityBase\_Want](capi-abilitybase-want.md)。 |
| const [AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md) \*options | 启动当前应用UIAbility时需要的StartOptions信息。详细内容参考[AbilityRuntime\_StartOptions](capi-abilityruntime-startoptions.md)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PERMISSION\_DENIED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方无正确权限。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 传入参数无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 设备不支持启动当前应用的UIAbility。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_SUCH\_ABILITY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 目标Ability不存在。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INCORRECT\_ABILITY\_TYPE](capi-ability-runtime-common-h.md#abilityruntime_errorcode) Ability类型不正确。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROWDTEST\_EXPIRED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 众测应用已过期。  [ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 无法在Wukong模式下启动Ability。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CONTROLLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用被管控。  [ABILITY\_RUNTIME\_ERROR\_CODE\_EDM\_CONTROLLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用被EDM管控。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CROSS\_APP](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方尝试启动不同应用。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 内部错误。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NOT\_TOP\_ABILITY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 调用方进程不在前台。  [ABILITY\_RUNTIME\_ERROR\_VISIBILITY\_SETTING\_DISABLED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 可见性设置已禁用。  [ABILITY\_RUNTIME\_ERROR\_CODE\_MULTI\_APP\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不支持应用分身和多实例。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INVALID\_APP\_INSTANCE\_KEY](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用实例Key无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_UPPER\_LIMIT\_REACHED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 应用实例数量已达上限。  [ABILITY\_RUNTIME\_ERROR\_MULTI\_INSTANCE\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不支持应用多实例。  [ABILITY\_RUNTIME\_ERROR\_CODE\_APP\_INSTANCE\_KEY\_NOT\_SUPPORTED](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 不允许设置APP\_INSTANCE\_KEY。 |

### OH\_AbilityRuntime\_ModObjExtensionContext\_TerminateSelf()

```c
AbilityRuntime_ErrorCode OH_AbilityRuntime_ModObjExtensionContext_TerminateSelf(OH_AbilityRuntime_ModObjExtensionContextHandle context)
```

**描述**

销毁ModularObjectExtensionAbility自身。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionContextHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) context | 指向ModularObjectExtensionAbility上下文的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [AbilityRuntime\_ErrorCode](capi-ability-runtime-common-h.md#abilityruntime_errorcode) | 返回特定的错误码。  [ABILITY\_RUNTIME\_ERROR\_CODE\_NO\_ERROR](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 接口调用成功。  [ABILITY\_RUNTIME\_ERROR\_CODE\_PARAM\_INVALID](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 传入参数无效。  [ABILITY\_RUNTIME\_ERROR\_CODE\_WUKONG\_MODE](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 无法在Wukong模式下销毁Ability。  [ABILITY\_RUNTIME\_ERROR\_CODE\_CONTEXT\_NOT\_EXIST](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 上下文不存在。  [ABILITY\_RUNTIME\_ERROR\_CODE\_INTERNAL](capi-ability-runtime-common-h.md#abilityruntime_errorcode) 内部错误。 |

### OH\_AbilityRuntime\_ModObjExtensionContext\_CreateIPCRemoteStub()

```c
OHIPCRemoteStub* OH_AbilityRuntime_ModObjExtensionContext_CreateIPCRemoteStub(OH_AbilityRuntime_ModObjExtensionContextHandle context, const char *descriptor, OH_OnRemoteRequestCallback requestCallback, OH_OnRemoteDestroyCallback destroyCallback, void *userData)
```

**描述**

创建一个OHIPCRemoteStub对象，回调函数将在ExtensionAbility指定的线程上运行。requestCallback和destroyCallback将在由ExtensionAbility的[OH\_AbilityRuntime\_ThreadMode](capi-modular-object-extension-manager-h.md#oh_abilityruntime_threadmode)决定的线程上按顺序执行。调用[OH\_AbilityRuntime\_ModObjExtensionContext\_DestroyIPCRemoteStub](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_destroyipcremotestub)后，不会再有新的requestCallback回调，且正在执行的requestCallback完成后才会回调destroyCallback。调用方需调用[OH\_AbilityRuntime\_ModObjExtensionContext\_DestroyIPCRemoteStub](capi-modular-object-extension-context-h.md#oh_abilityruntime_modobjextensioncontext_destroyipcremotestub)销毁返回的对象，避免内存泄漏。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionContextHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) context | 指向ModularObjectExtensionAbility上下文的指针。 |
| const char \*descriptor | 指向待创建的OHIPCRemoteStub对象描述符的指针，不能为NULL。创建过程中会内部拷贝该字符串，调用方可在本函数返回后释放该描述符。 |
| OH\_OnRemoteRequestCallback requestCallback | 处理数据请求的回调函数，不能为NULL。 |
| OH\_OnRemoteDestroyCallback destroyCallback | 对象销毁时调用的回调函数，可以为NULL。 |
| void \*userData | 指向用户数据的指针，可以为NULL，须在对象销毁前保持有效。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| OHIPCRemoteStub\* | 操作成功时返回创建的OHIPCRemoteStub对象指针；否则返回NULL。 |

### OH\_AbilityRuntime\_ModObjExtensionContext\_DestroyIPCRemoteStub()

```c
void OH_AbilityRuntime_ModObjExtensionContext_DestroyIPCRemoteStub(OH_AbilityRuntime_ModObjExtensionContextHandle context, OHIPCRemoteStub *stub)
```

**描述**

销毁OHIPCRemoteStub对象。

**起始版本：** 26.0.0

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjExtensionContextHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioncontext8h.md) context | 指向ModularObjectExtensionAbility上下文的指针。 |
| OHIPCRemoteStub \*stub | 指向待销毁的OHIPCRemoteStub对象的指针。 |
