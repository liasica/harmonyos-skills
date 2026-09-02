---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modularobjectdispatcher8h
title: OH_AbilityRuntime_ModularObjectDispatcher*
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModularObjectDispatcher*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:07+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bb3548fd8728a73a1fdd5c32d1cc57e7b20438d1fd9cd2067b77bcc6c1486c69
---

```c
typedef struct OH_AbilityRuntime_ModularObjectDispatcher* OH_AbilityRuntime_ModObjDispatcherHandle
```

## 概述

ModularObject分发器的句柄。

该句柄指向一个ModularObject分发器实例，可通过[OH\_AbilityRuntime\_ModObjDispatcher\_CreateMainServiceInstance](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_createmainserviceinstance)或[OH\_AbilityRuntime\_ModObjDispatcher\_CreateSubInstance](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_createsubinstance)创建，使用完毕后需通过[OH\_AbilityRuntime\_ModObjDispatcher\_Release](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_release)释放。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)
