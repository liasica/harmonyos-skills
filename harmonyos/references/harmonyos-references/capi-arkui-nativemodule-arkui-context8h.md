---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context8h
title: ArkUI_Context*
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_Context*
category: harmonyos-references
scraped_at: 2026-09-25T07:10:45+08:00
doc_updated_at: 2026-09-24
content_hash: sha256:2fe6aa148f1ff5f169a0fdcb92f621b66ff950c9a8c50e6a448ea1d5599fcd5c
---

```c
typedef struct ArkUI_Context* ArkUI_ContextHandle
```

## 概述

ArkUI在Native侧的上下文实例对象指针，用于表示组件所在页面的UIContext。开发者可通过[OH\_ArkUI\_GetContextByNode](capi-native-node-h.md#oh_arkui_getcontextbynode)或[OH\_ArkUI\_GetContextFromNapiValue](capi-native-node-napi-h.md#oh_arkui_getcontextfromnapivalue)获取该指针，并将其作为UI任务调度、动画、焦点控制等接口的上下文入参。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [common\_type.h](capi-common-type-h.md)
