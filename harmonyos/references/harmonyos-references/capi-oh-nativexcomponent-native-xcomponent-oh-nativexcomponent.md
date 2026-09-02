---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent-oh-nativexcomponent
title: OH_NativeXComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_NativeXComponent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:afb653f86b282376d0495757b1b78862048d671488a2ea114dbf64afb9ccaf15
---

```c
typedef struct OH_NativeXComponent OH_NativeXComponent
```

## 概述

OH\_NativeXComponent是ArkUI提供的XComponent在Native侧的实例封装。用于在ArkUI页面中嵌入自绘制渲染内容（如EGL/OpenGL ES/Vulkan渲染表面），并支持Native层与ArkUI层之间的触摸事件、尺寸变化等事件交互。适用于游戏、地图、视频渲染等需要在应用内集成高性能自绘制内容的场景。

**起始版本：** 8

**相关模块：** [OH\_NativeXComponent Native XComponent](capi-oh-nativexcomponent-native-xcomponent.md)

**所在头文件：** [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md)
