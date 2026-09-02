---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-arkui-surfacecallback
title: OH_ArkUI_SurfaceCallback
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_SurfaceCallback
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9106f68758eb13479e89ed5c7b73ffc0811a10038afeb3867ebf928e9361110d
---

```c
typedef struct OH_ArkUI_SurfaceCallback OH_ArkUI_SurfaceCallback
```

## 概述

定义Surface生命周期回调结构体。当XComponent的Surface创建、销毁或尺寸发生变化时，会触发对应的回调。开发者可在回调中获取Surface指针并执行自定义渲染（如OpenGL ES渲染、Vulkan渲染或视频解码渲染等场景）。

**起始版本：** 19

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)
