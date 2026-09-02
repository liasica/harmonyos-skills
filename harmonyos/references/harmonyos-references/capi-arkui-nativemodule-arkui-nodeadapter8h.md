---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-nodeadapter8h
title: ArkUI_NodeAdapter*
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_NodeAdapter*
category: harmonyos-references
scraped_at: 2026-09-02T14:51:51+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8fa94eb7913d46aa165ded066e7c1cafa8c2827bc7a87a87c98af157be51c028
---

```c
typedef struct ArkUI_NodeAdapter* ArkUI_NodeAdapterHandle
```

## 概述

定义组件适配器对象，用于滚动类组件的元素懒加载，适用于需要按需加载大量滚动内容的场景，可避免一次性创建全部元素，降低内存占用并提升滑动性能。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_node.h](capi-native-node-h.md)
