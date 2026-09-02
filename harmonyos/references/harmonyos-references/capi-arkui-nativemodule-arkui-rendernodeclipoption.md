---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-rendernodeclipoption
title: ArkUI_RenderNodeClipOption
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_RenderNodeClipOption
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3893c960781452aa2cb176d5500649091253b984d9a8936b4a05b42d7a657624
---

```c
typedef struct ArkUI_RenderNodeClipOption ArkUI_RenderNodeClipOption
```

## 概述

定义渲染节点裁剪配置项，用于通过矩形、圆角矩形、圆形、椭圆形或自定义绘制路径描述渲染节点的裁剪区域，并作为[OH\_ArkUI\_RenderNodeUtils\_SetClip](capi-native-render-h.md#oh_arkui_rendernodeutils_setclip)的入参为渲染节点应用裁剪。

**起始版本：** 20

**相关模块：** [ArkUI\_RenderNodeUtils](capi-arkui-rendernodeutils.md)

**所在头文件：** [native\_render.h](capi-native-render-h.md)
