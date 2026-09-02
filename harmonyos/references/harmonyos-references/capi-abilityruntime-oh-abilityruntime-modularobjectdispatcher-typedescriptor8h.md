---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-typedescriptor8h
title: OH_AbilityRuntime_ModularObjectDispatcher_TypeDescriptor*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModularObjectDispatcher_TypeDescriptor*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:76609c8421af5aad3d4a49b3d8051bfd9c9758aa22c0e0c5bd672549de23f7e7
---

```c
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_TypeDescriptor* OH_AbilityRuntime_ModObjDispatcher_TypeDescriptorHandle
```

## 概述

定义ModularObject分发器的类型描述符句柄。

该句柄指向类型库元数据的访问接口，可用于查询远端服务定义的接口、方法、枚举和结构体等信息。

可通过[OH\_AbilityRuntime\_ModObjDispatcher\_GetTypeDescriptor](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_gettypedescriptor)获取。使用完毕后需通过[OH\_AbilityRuntime\_TypeDescriptor\_Release](capi-modular-object-dispatcher-h.md#oh_abilityruntime_typedescriptor_release)释放。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)
