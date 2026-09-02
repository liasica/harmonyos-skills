---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textshadowstyle
title: OH_ArkUI_TextShadowStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextShadowStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3f3ab9f0fc7f7582f30398b2b8cb19b0584cc27b1b9aeb89e6bacc99ebbe7ccf
---

```c
typedef struct OH_ArkUI_TextShadowStyle OH_ArkUI_TextShadowStyle
```

## 概述

定义文本阴影样式，文本阴影样式包含阴影偏移、模糊半径、颜色等属性，用于为文本添加阴影效果，如标题文字突出显示、深色背景下的文字增强等。

调用[OH\_ArkUI\_TextShadowStyle\_Create](capi-styled-string-h.md#oh_arkui_textshadowstyle_create)接口创建文本阴影样式对象。

调用[OH\_ArkUI\_TextShadowStyle\_Destroy](capi-styled-string-h.md#oh_arkui_textshadowstyle_destroy)接口销毁文本阴影样式对象。

创建文本阴影样式对象后，调用[OH\_ArkUI\_TextShadowStyle\_SetTextShadow](capi-styled-string-h.md#oh_arkui_textshadowstyle_settextshadow)接口设置文本阴影的具体样式。

调用[OH\_ArkUI\_TextShadowStyle\_GetTextShadow](capi-styled-string-h.md#oh_arkui_textshadowstyle_gettextshadow)接口获取已设置的文本阴影样式。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
