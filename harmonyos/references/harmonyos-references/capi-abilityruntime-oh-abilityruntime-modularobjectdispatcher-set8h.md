---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher-set8h
title: OH_AbilityRuntime_ModularObjectDispatcher_Set*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModularObjectDispatcher_Set*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e7e14c047867e783851d640fc8945e8fa1ac659afdb0565f0d70deac6ab917b4
---

```c
typedef struct OH_AbilityRuntime_ModularObjectDispatcher_Set* OH_AbilityRuntime_ModObjDispatcher_SetHandle
```

## 概述

集合句柄。

该句柄指向一个不重复元素的无序集合，所有元素类型相同，支持添加元素、删除元素、查询指定元素是否存在、按索引获取元素、查询集合大小和清空操作。

可通过[OH\_AbilityRuntime\_ModObjDispatcher\_SetCreate](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_setcreate)创建，使用完毕后需通过[OH\_AbilityRuntime\_ModObjDispatcher\_SetRelease](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_setrelease)释放。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)
