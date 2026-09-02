---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-parallelgestureevent
title: ArkUI_ParallelGestureEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ParallelGestureEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8eecbc8bde1e47698af48acf2eaa50c620e15c0e21e6e0eb60a9732fd626951
---

```c
typedef struct ArkUI_ParallelGestureEvent ArkUI_ParallelGestureEvent
```

## 概述

定义并行手势事件。该结构体作为[setGestureParallelTo](capi-arkui-nativemodule-arkui-nativegestureapi-3.md#setgestureparallelto)回调函数的参数传递，用于在触发触摸测试时，将开发者自定义手势与响应链上其他组件的手势设置为并行关系的场景。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](capi-native-gesture-h.md)
