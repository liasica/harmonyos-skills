---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-texteditorchangeevent
title: OH_ArkUI_TextEditorChangeEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextEditorChangeEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bc72fed66e764c252b1cce482530941bb4ffc4b47fd279280244d21ea528119c
---

```c
typedef struct OH_ArkUI_TextEditorChangeEvent OH_ArkUI_TextEditorChangeEvent
```

## 概述

定义TextEditor组件文本内容变化事件的结构体，用于在文本内容变化时通知用户，支持获取变化前后的内容等信息，适用于需要在文本内容变化前进行拦截或校验的场景，例如输入拦截、内容过滤、变更确认等。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)
