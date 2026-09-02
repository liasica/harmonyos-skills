---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessibilityprovider
title: ArkUI_AccessibilityProvider
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_AccessibilityProvider
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8925fb1b885c5bc97cfa2d0d33d811a66f520a993bda1dc3d02350a94cfce0c6
---

```c
typedef struct ArkUI_AccessibilityProvider ArkUI_AccessibilityProvider
```

## 概述

该结构体为无障碍第三方操作提供者，用于承载回调函数的实现。开发者可通过该结构体注册和管理无障碍操作相关的回调，实现自定义的无障碍交互逻辑，适用于需要扩展或定制ArkUI无障碍能力的场景。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](capi-arkui-accessibility.md)

**所在头文件：** [native\_interface\_accessibility.h](capi-native-interface-accessibility-h.md)
