---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-textstyle
title: OH_ArkUI_TextStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_TextStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0faf2191a1da2a1e212bb416ecb8bc75545dafcbf9cc9eac75a154fc52fd5568
---

```c
typedef struct OH_ArkUI_TextStyle OH_ArkUI_TextStyle
```

## 概述

定义文本字体样式，用于设置文本的字体颜色、大小、样式等属性，适用于需要自定义文本显示效果的场景。

调用[OH\_ArkUI\_TextStyle\_Create](capi-styled-string-h.md#oh_arkui_textstyle_create)接口创建文本字体样式对象。

调用[OH\_ArkUI\_TextStyle\_Destroy](capi-styled-string-h.md#oh_arkui_textstyle_destroy)接口销毁文本字体样式对象。销毁后不应再调用OH\_ArkUI\_TextStyle\_SetXXX系列接口。

对象创建成功后，调用OH\_ArkUI\_TextStyle\_SetXXX系列接口设置具体样式；若创建失败则不可调用SetXXX系列接口。例如，调用[OH\_ArkUI\_TextStyle\_SetFontColor](capi-styled-string-h.md#oh_arkui_textstyle_setfontcolor)设置字体颜色。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
