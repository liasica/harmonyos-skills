---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-array8h
title: OH_AbilityRuntime_ModularObjectDispatcher_Array*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModularObjectDispatcher_Array*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6e54f782e3c7a98dc949ed5da0a7cc19ca31ff020e05fc27a9ea8d2f4a8019ee
---

```c
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_Array* OH_AbilityRuntime_ModObjDispatcher_ArrayHandle
```

## 概述

数组句柄。

该句柄指向一个固定大小的有序元素集合，所有元素类型相同，支持按索引设置获取元素和查询数组大小。

可通过[OH\_AbilityRuntime\_ModObjDispatcher\_ArrayCreate](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_arraycreate)创建，使用完毕后需通过[OH\_AbilityRuntime\_ModObjDispatcher\_ArrayRelease](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_arrayrelease)释放。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)
