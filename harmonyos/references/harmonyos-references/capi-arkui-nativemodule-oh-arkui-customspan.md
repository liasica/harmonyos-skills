---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-customspan
title: OH_ArkUI_CustomSpan
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_CustomSpan
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4e34ee7a34b1a8809bfd872ff8138e870a846c3300273d726f6e7d5e7d0c9921
---

```c
typedef struct OH_ArkUI_CustomSpan OH_ArkUI_CustomSpan
```

## 概述

定义自定义绘制Span，用于在属性字符串中实现自定义测量和绘制能力。自定义绘制Span通过测量回调确定其占位大小，通过绘制回调在对应区域内绘制自定义内容，从而将自定义图形元素嵌入到富文本中。

调用[OH\_ArkUI\_CustomSpan\_Create](capi-styled-string-h.md#oh_arkui_customspan_create)接口创建自定义绘制Span对象。

对象创建后，调用[OH\_ArkUI\_CustomSpan\_RegisterOnMeasureCallback](capi-styled-string-h.md#oh_arkui_customspan_registeronmeasurecallback)接口注册测量回调函数。

调用[OH\_ArkUI\_CustomSpan\_RegisterOnDrawCallback](capi-styled-string-h.md#oh_arkui_customspan_registerondrawcallback)接口注册绘制回调函数。

调用[OH\_ArkUI\_CustomSpan\_Destroy](capi-styled-string-h.md#oh_arkui_customspan_destroy)接口销毁自定义绘制Span对象。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
