---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-vector8h
title: OH_AbilityRuntime_ModularObjectDispatcher_Vector*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModularObjectDispatcher_Vector*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:511eb956da9cebe9c31453ac52ee35a8de955aa79b6b17bdf9e33bdaede6b631
---

```c
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_Vector* OH_AbilityRuntime_ModObjDispatcher_VectorHandle
```

## 概述

向量句柄。

该句柄指向一个动态大小的有序元素集合，所有元素类型相同，支持添加元素、按索引获取元素、查询向量大小和清空操作。

可通过[OH\_AbilityRuntime\_ModObjDispatcher\_VectorCreate](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_vectorcreate)创建，使用完毕后需通过[OH\_AbilityRuntime\_ModObjDispatcher\_VectorRelease](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_vectorrelease)释放。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)
