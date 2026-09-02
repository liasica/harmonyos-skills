---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-letterspacingstyle
title: OH_ArkUI_LetterSpacingStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LetterSpacingStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:730c364a94298e595d04302ccddcd57ff3e5f103be9998284e50a26fea9b62a1
---

```c
typedef struct OH_ArkUI_LetterSpacingStyle OH_ArkUI_LetterSpacingStyle
```

## 概述

定义字符间距样式，用于对文本设置字符间距以优化排版效果。适用于文本排列过密导致阅读困难等需要调整字符间距的场景，可提升文本可读性和排版美观度。

调用[OH\_ArkUI\_LetterSpacingStyle\_Create](capi-styled-string-h.md#oh_arkui_letterspacingstyle_create)接口创建对应的字符间距样式对象。

创建对象成功后，调用[OH\_ArkUI\_LetterSpacingStyle\_SetLetterSpacing](capi-styled-string-h.md#oh_arkui_letterspacingstyle_setletterspacing)接口设置具体的字符间距值，取值原则详见该接口说明。

调用[OH\_ArkUI\_LetterSpacingStyle\_GetLetterSpacing](capi-styled-string-h.md#oh_arkui_letterspacingstyle_getletterspacing)接口获取字符间距值。

对象不再使用时，调用[OH\_ArkUI\_LetterSpacingStyle\_Destroy](capi-styled-string-h.md#oh_arkui_letterspacingstyle_destroy)接口销毁字符间距样式对象。若创建失败，则不得调用上述接口。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
