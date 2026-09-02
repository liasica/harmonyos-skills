---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-context8h
title: ArkUI_Context*
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_Context*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0402b918ec070cba85c9c061cb4feb57de5a5d05393aad64f56c40950ec91cd0
---

```c
typedef struct ArkUI_Context* ArkUI_ContextHandle
```

## 概述

ArkUI 在 Native 侧的上下文实例对象指针，用于表示组件所在页面的 UIContext。开发者可通过[OH\_ArkUI\_GetContextByNode](capi-native-node-h.md#oh_arkui_getcontextbynode)或[OH\_ArkUI\_GetContextFromNapiValue](capi-native-node-napi-h.md#oh_arkui_getcontextfromnapivalue)获取该指针，并将其作为 UI 任务调度、动画、焦点控制等接口的上下文入参。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_type.h](capi-native-type-h.md)
