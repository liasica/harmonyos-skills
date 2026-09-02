---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-abilityruntime-oh-abilityruntime-modobjdispatcher-inputparams
title: OH_AbilityRuntime_ModObjDispatcher_InputParams
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > C API > 结构体 > OH_AbilityRuntime_ModObjDispatcher_InputParams
category: harmonyos-references
scraped_at: 2026-09-02T15:00:37+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:557ca61deaca51438a34e1965242a4e36da4d19df00c4ea0ffdb45526306d3d8
---

```c
typedef struct {...} OH_AbilityRuntime_ModObjDispatcher_InputParams
```

## 概述

定义方法调用的参数结构。rgvarg指向参数变体数组，数组长度由cArgs指定。参数顺序应与方法定义中的参数顺序一致。

**起始版本：** 26.0.0

**相关模块：** [AbilityRuntime](capi-abilityruntime.md)

**所在头文件：** [modular\_object\_dispatcher.h](capi-modular-object-dispatcher-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_AbilityRuntime\_ModObjDispatcher\_Variant\*](capi-abilityruntime-oh-abilityruntime-modobjdispatcher-variant.md) rgvarg | 参数变体数组。  **起始版本：** 26.0.0 |
| uint32\_t cArgs | 参数数量。  **起始版本：** 26.0.0 |
