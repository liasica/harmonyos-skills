---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-linespacingstyle
title: OH_ArkUI_LineSpacingStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LineSpacingStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e5aa13b45ba38f2139629c16e4889caf32d970fdee224159f4e94e82869a6f71
---

```c
typedef struct OH_ArkUI_LineSpacingStyle OH_ArkUI_LineSpacingStyle
```

## 概述

定义行间距样式，用于设置文本行之间的间距，可提升文本可读性和视觉效果。适用于电子书阅读器、新闻资讯类应用、长文档编辑等需要精细控制多行文本排版行间距的场景。

调用[OH\_ArkUI\_LineSpacingStyle\_Create](capi-styled-string-h.md#oh_arkui_linespacingstyle_create)接口创建行间距样式对象，行间距默认值为0，行间距是否只在行间生效默认为false。

调用[OH\_ArkUI\_LineSpacingStyle\_Destroy](capi-styled-string-h.md#oh_arkui_linespacingstyle_destroy)接口销毁行间距样式对象。

对象创建成功后，调用[OH\_ArkUI\_LineSpacingStyle\_SetLineSpacing](capi-styled-string-h.md#oh_arkui_linespacingstyle_setlinespacing)接口设置行间距值（取值范围及约束详见该接口说明）。

调用[OH\_ArkUI\_LineSpacingStyle\_SetOnlyBetweenLines](capi-styled-string-h.md#oh_arkui_linespacingstyle_setonlybetweenlines)接口设置行间距是否只在行间生效（取值规则详见该接口说明）。

**起始版本：** 26.0.0

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
