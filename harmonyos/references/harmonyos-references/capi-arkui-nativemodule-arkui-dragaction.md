---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-dragaction
title: ArkUI_DragAction
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_DragAction
category: harmonyos-references
scraped_at: 2026-09-02T14:51:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:181e2224ae29959697c5550d1f63be05eeca7dc90c531f6f772db69eb766b00f
---

```c
typedef struct ArkUI_DragAction ArkUI_DragAction
```

## 概述

拖拽行为句柄，用于主动发起拖拽操作，即由开发者主动调用接口启动拖拽，区别于被动响应拖拽事件。开发者可结合主动拖拽流程了解ArkUI\_DragAction的创建、配置和执行机制，相关说明请参见[绑定拖拽事件](../harmonyos-guides/ndk-drag-event.md)。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [drag\_and\_drop.h](capi-drag-and-drop-h.md)
