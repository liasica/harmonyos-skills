---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-arkui-surfaceholder
title: OH_ArkUI_SurfaceHolder
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_SurfaceHolder
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3222ad5556a3aa64e07917fbab4d38534fa38b795c24ceda6cb163ed197fce1e
---

```c
typedef struct OH_ArkUI_SurfaceHolder OH_ArkUI_SurfaceHolder
```

## 概述

OH\_ArkUI\_SurfaceHolder用于封装和管理Native XComponent的Surface，提供对底层渲染表面的访问与操作能力。可通过[OH\_ArkUI\_SurfaceHolder\_Create](capi-native-interface-xcomponent-h.md#oh_arkui_surfaceholder_create)接口创建实例，适用于在Native侧需要进行自定义渲染或与图形/媒体组件对接的场景。

**起始版本：** 19

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)
