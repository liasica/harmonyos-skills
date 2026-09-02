---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-backgroundcolorstyle
title: OH_ArkUI_BackgroundColorStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_BackgroundColorStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:acee42e6f486cb550c91bba1129813757d45626e9f87c8d85dd61a739e4721a3
---

```c
typedef struct OH_ArkUI_BackgroundColorStyle OH_ArkUI_BackgroundColorStyle
```

## 概述

定义背景颜色样式，支持自定义背景颜色和圆角半径，适用于为属性字符串设置背景高亮效果，例如搜索结果高亮、重点文本标记、标签式文本展示等场景，可提升文本的视觉层次和可辨识度。

调用[OH\_ArkUI\_BackgroundColorStyle\_Create](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_create)接口创建背景颜色样式对象。

对象创建后，调用[OH\_ArkUI\_BackgroundColorStyle\_SetColor](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setcolor)和[OH\_ArkUI\_BackgroundColorStyle\_SetRadius](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_setradius)接口设置背景颜色和圆角半径。

调用[OH\_ArkUI\_BackgroundColorStyle\_GetColor](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_getcolor)和[OH\_ArkUI\_BackgroundColorStyle\_GetRadius](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_getradius)接口获取背景颜色和圆角半径。

使用完毕后，调用[OH\_ArkUI\_BackgroundColorStyle\_Destroy](capi-styled-string-h.md#oh_arkui_backgroundcolorstyle_destroy)接口销毁背景颜色样式对象。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
