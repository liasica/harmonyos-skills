---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-struct8h
title: OH_AbilityRuntime_ModularObjectDispatcher_Struct*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModularObjectDispatcher_Struct*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b82ac21cc45bb3a55bae60d6d5d1eb6e70ce6408e36deea8d3df9f48de335358
---

```c
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_Struct* OH_AbilityRuntime_ModObjDispatcher_StructHandle
```

## 概述

结构体句柄。

该句柄指向一个具名字段的结构体实例，字段类型通过类型库元数据定义。

可通过[OH\_AbilityRuntime\_ModObjDispatcher\_StructCreate](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_structcreate)创建，使用完毕后需通过[OH\_AbilityRuntime\_ModObjDispatcher\_StructRelease](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_structrelease)释放。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)
