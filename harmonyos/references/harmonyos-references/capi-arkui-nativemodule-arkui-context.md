---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context
title: ArkUI_Context
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_Context
category: harmonyos-references
scraped_at: 2026-09-02T14:51:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:2b624a81f6d5bedf870a7eff995c1612e42df75dcd26793c58b746939ad225dc
---

```c
typedef struct ArkUI_Context ArkUI_Context
```

## 概述

ArkUI native UI 的上下文实例对象，用于表示组件所在页面的 UIContext。其指针类型为 [ArkUI\_ContextHandle](capi-arkui-nativemodule-arkui-context8h.md)，开发者可通过 [OH\_ArkUI\_GetContextByNode](capi-native-node-h.md#oh_arkui_getcontextbynode) 获取对应上下文，并将其作为拖拽操作、动画、UI 任务调度等接口的上下文入参。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)
