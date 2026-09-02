---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-arkui-xcomponentsurfaceconfig
title: ArkUI_XComponentSurfaceConfig
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_XComponentSurfaceConfig
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ce2715af8f01f6211186ad44cda7b2f8fbc54d1c6511cf4729c2cd98f2148a13
---

```c
typedef struct ArkUI_XComponentSurfaceConfig ArkUI_XComponentSurfaceConfig
```

## 概述

定义该Surface配置，用于设置XComponent组件持有的Surface在渲染时是否被视为不透明。适用于对XComponent渲染性能有要求的场景，将Surface设置为不透明可以减少渲染合成开销，提升渲染性能。需要注意的是，仅当Surface实际渲染的内容全部为不透明时才应设置为不透明，否则可能导致渲染异常。

**起始版本：** 22

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)
