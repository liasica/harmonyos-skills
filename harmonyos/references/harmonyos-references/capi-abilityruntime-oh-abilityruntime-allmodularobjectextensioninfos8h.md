---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-allmodularobjectextensioninfos8h
title: OH_AbilityRuntime_AllModularObjectExtensionInfos*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_AllModularObjectExtensionInfos*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5dadac6d00979baba7e0c72343eb3393dbebda005a718d33eeb2203f97476ec3
---

```c
typedef struct OH_AbilityRuntime_AllModularObjectExtensionInfos* OH_AbilityRuntime_AllModObjExtensionInfosHandle
```

## 概述

表示当前应用内所有ModularObjectExtensionAbility信息的集合句柄。可通过[OH\_AbilityRuntime\_AcquireSelfModularObjectExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_acquireselfmodularobjectextensioninfos)获取该句柄。该句柄指向一个包含多个[OH\_AbilityRuntime\_ModObjExtensionInfoHandle](capi-abilityruntime-oh-abilityruntime-modularobjectextensioninfo8h.md) 的集合，可通过[OH\_AbilityRuntime\_GetCountFromAllModObjExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getcountfromallmodobjextensioninfos) 获取集合中元素的数量，并通过[OH\_AbilityRuntime\_GetModObjExtensionInfoByIndex](capi-modular-object-extension-manager-h.md#oh_abilityruntime_getmodobjextensioninfobyindex) 按索引获取单个ModularObjectExtensionAbility信息。使用完毕后需通过[OH\_AbilityRuntime\_ReleaseAllExtensionInfos](capi-modular-object-extension-manager-h.md#oh_abilityruntime_releaseallextensioninfos) 释放该集合。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_extension\_manager.h](capi-modular-object-extension-manager-h.md)
