---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-arkui-gestureevent
title: ArkUI_GestureEvent
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > ArkUI_GestureEvent
category: harmonyos-references
scraped_at: 2026-09-02T14:51:50+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ad2eb12303bee646adf1880504f23768437c5690870d027addff7c6b914578a
---

```c
typedef struct ArkUI_GestureEvent ArkUI_GestureEvent
```

## 概述

提供手势事件数据类型对象定义，用于在手势事件处理过程中承载和传递手势事件相关数据，支持获取手势事件类型、坐标、时间戳等关键信息；适用于需要处理触摸手势交互的场景，如点击、长按、拖动、缩放等手势识别与响应；开发者可通过相关手势事件接口获取事件信息。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [native\_gesture.h](capi-native-gesture-h.md)
