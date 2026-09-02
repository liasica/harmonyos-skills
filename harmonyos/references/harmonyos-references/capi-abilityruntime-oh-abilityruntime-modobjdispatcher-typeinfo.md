---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modobjdispatcher-typeinfo
title: OH_AbilityRuntime_ModObjDispatcher_TypeInfo
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModObjDispatcher_TypeInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:91e47102d5608c9d8ca85864a68a4bb203eb0c2e8ecbe7dd862e93b93c625ad0
---

```c
typedef struct OH_AbilityRuntime_ModObjDispatcher_TypeInfo {...} OH_AbilityRuntime_ModObjDispatcher_TypeInfo
```

## 概述

定义参数或返回值的类型信息。

使用带标签的联合体u描述类型信息，通过vt字段决定联合体中哪个成员有效。

* 对于映射（MAP）类型，使用u.mapType.keyType描述键类型，u.mapType.pValueType描述值类型；
* 对于数组（ARRAY）类型，使用u.arrayType.pElementType描述元素类型，u.arrayType.size描述数组的固定大小；
* 对于向量（VECTOR）或集合（SET）类型，使用u.pElementType描述元素类型；
* 对于结构体（STRUCT）、远端通信对象（IPC\_REMOTE\_PROXY、IPC\_REMOTE\_STUB）、枚举（ENUM）类型，使用u.idlType描述[IDL类型名称](../harmonyos-guides/modular-object-extension-ability-taihe.md#ohidl文件编写规范)。

使用完毕后需调用[OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfoClear](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_typeinfoclear)释放内部持有的堆资源。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjDispatcher\_ValueType](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_valuetype) vt | 类型标签，决定联合体中哪个成员有效。  **起始版本：** 26.0.0 |
| union {  struct {  [OH\_AbilityRuntime\_ModObjDispatcher\_ValueType](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_valuetype) keyType;  [OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfo](capi-abilityruntime-oh-abilityruntime-modobjdispatcher-typeinfo.md)\* pValueType;  } mapType;  struct {  [OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfo](capi-abilityruntime-oh-abilityruntime-modobjdispatcher-typeinfo.md)\* pElementType;  uint32\_t size;  } arrayType;  [OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfo](capi-abilityruntime-oh-abilityruntime-modobjdispatcher-typeinfo.md)\* pElementType;  char\* idlType;  } u | 类型特定的元数据联合体。有效的成员由vt决定。  mapType：映射类型元数据，当vt为MAP时使用。  mapType.keyType：映射的键类型，仅支持基本类型（BOOL、有符号整数、无符号整数、浮点数、STRING、ENUM），不支持容器类型（ARRAY、VECTOR、SET、MAP）和复杂类型（STRUCT、IPC\_REMOTE\_PROXY、IPC\_REMOTE\_STUB）。  mapType.pValueType：值类型描述符的句柄，需调用[OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfoClear](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_typeinfoclear)释放。  arrayType：数组类型元数据，当vt为ARRAY时使用。  arrayType.pElementType：元素类型描述符的句柄，需调用[OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfoClear](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_typeinfoclear)释放。  arrayType.size：数组的固定大小。  pElementType：元素类型描述符的句柄，当vt为VECTOR或SET时使用，需调用[OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfoClear](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_typeinfoclear)释放。  idlType：[IDL类型名称](../harmonyos-guides/modular-object-extension-ability-taihe.md#ohidl文件编写规范)字符串，当vt为STRUCT、IPC\_REMOTE\_PROXY、IPC\_REMOTE\_STUB、ENUM时使用，需调用[OH\_AbilityRuntime\_ModObjDispatcher\_TypeInfoClear](capi-modular-object-dispatcher-h.md#oh_abilityruntime_modobjdispatcher_typeinfoclear)释放。  **起始版本：** 26.0.0 |
