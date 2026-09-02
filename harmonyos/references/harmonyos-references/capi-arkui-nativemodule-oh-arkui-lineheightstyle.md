---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-lineheightstyle
title: OH_ArkUI_LineHeightStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LineHeightStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3574abb0e568473e575ac762ccdd044660d2b8fe861524490656ba0b07ca0c0c
---

```c
typedef struct OH_ArkUI_LineHeightStyle OH_ArkUI_LineHeightStyle
```

## 概述

定义行高样式。

可以通过[OH\_ArkUI\_LineHeightStyle\_Create](capi-styled-string-h.md#oh_arkui_lineheightstyle_create)接口创建对应的行高样式对象。

可以通过[OH\_ArkUI\_LineHeightStyle\_Destroy](capi-styled-string-h.md#oh_arkui_lineheightstyle_destroy)接口销毁行高样式对象。

对象创建后可以通过[OH\_ArkUI\_LineHeightStyle\_SetLineHeight](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheight)接口设置具体的固定行高值。

从API版本26.0.0开始，对象创建后可以通过[OH\_ArkUI\_LineHeightStyle\_SetLineHeightMultiple](capi-styled-string-h.md#oh_arkui_lineheightstyle_setlineheightmultiple)接口设置具体的行高的倍数值。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
