---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-parallelinnergestureevent
title: ArkUI_ParallelInnerGestureEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_ParallelInnerGestureEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:6cc8f31639dfa2d37af55b16eb1eae767a1cef4c98d86df67b4618709c9cec55
---

```c
typedef struct ArkUI_ParallelInnerGestureEvent ArkUI_ParallelInnerGestureEvent
```

## 概述

定义并行内部手势事件。该结构体作为[setInnerGestureParallelTo](capi-arkui-nativemodule-arkui-nativegestureapi-1.md#setinnergestureparallelto)的回调函数的参数传递，用于将系统内置手势（如Scroll、List等容器组件的内置滑动手势）与响应链上其他组件设置为并行关系的场景。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](capi-native-gesture-h.md)
