---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativexcomponent-native-xcomponent
title: OH_NativeXComponent Native XComponent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 模块 > OH_NativeXComponent Native XComponent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:43+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9fb3fce7da5ad9cd86b5cafa8a07c9f73bb3122782dd3f295228a265f0ad849e
---

## 概述

OH\_NativeXComponent提供ArkUI XComponent持有的Surface和触摸事件能力。支持将EGL/OpenGLES渲染输出、媒体数据等自绘内容上屏显示，并实现Native层与ArkUI之间的触摸等事件交互。适用于游戏/图形渲染、视频播放、相机预览等需要在Native侧进行高性能绘制并与ArkUI联动交互的场景，具体使用请参考[Native XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)。

**起始版本：** 8

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [native\_interface\_xcomponent.h](capi-native-interface-xcomponent-h.md) | 声明用于访问Native XComponent的API。 |
| [native\_xcomponent\_key\_event.h](capi-native-xcomponent-key-event-h.md) | 声明用于访问Native XComponent键盘事件的枚举类型。 |
