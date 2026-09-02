---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-baselineoffsetstyle
title: OH_ArkUI_BaselineOffsetStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_BaselineOffsetStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0471d03fdcbbf5043b1bc465aff9db486230c2aa80702b9a592a5c40660474c4
---

```c
typedef struct OH_ArkUI_BaselineOffsetStyle OH_ArkUI_BaselineOffsetStyle
```

## 概述

定义基线偏移量样式，用于在属性字符串中设置文本的基线偏移量，使文本在垂直方向上相对于基线进行上移或下移，从而实现上下标等特殊排版效果。基线偏移量样式需通过创建样式对象、设置偏移值后应用到属性字符串中生效。

调用[OH\_ArkUI\_BaselineOffsetStyle\_Create](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_create)接口创建基线偏移量样式对象。

对象创建后，调用[OH\_ArkUI\_BaselineOffsetStyle\_SetBaselineOffset](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_setbaselineoffset)接口设置基线偏移量值。

调用[OH\_ArkUI\_BaselineOffsetStyle\_GetBaselineOffset](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_getbaselineoffset)接口获取基线偏移量值。

使用完毕后，调用[OH\_ArkUI\_BaselineOffsetStyle\_Destroy](capi-styled-string-h.md#oh_arkui_baselineoffsetstyle_destroy)接口销毁基线偏移量样式对象。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
