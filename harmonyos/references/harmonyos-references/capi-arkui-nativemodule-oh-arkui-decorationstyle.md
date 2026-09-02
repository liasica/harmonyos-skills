---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-decorationstyle
title: OH_ArkUI_DecorationStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_DecorationStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:92ed336c98e2e05fabe92a1f556c99c5b5469e6f8ddf7de88329603bdd9347a5
---

```c
typedef struct OH_ArkUI_DecorationStyle OH_ArkUI_DecorationStyle
```

## 概述

定义文本装饰线样式，支持对文本添加下划线、删除线等装饰线效果，适用于需要自定义文本装饰线外观的场景，可帮助开发者灵活控制文本装饰线的类型、颜色与样式。

调用[OH\_ArkUI\_DecorationStyle\_Create](capi-styled-string-h.md#oh_arkui_decorationstyle_create)接口创建文本装饰线样式对象。

对象创建后，调用OH\_ArkUI\_DecorationStyle\_SetXXX系列接口设置具体样式。例如，调用[OH\_ArkUI\_DecorationStyle\_SetTextDecorationType](capi-styled-string-h.md#oh_arkui_decorationstyle_settextdecorationtype)接口设置装饰线类型。

使用完毕后，调用[OH\_ArkUI\_DecorationStyle\_Destroy](capi-styled-string-h.md#oh_arkui_decorationstyle_destroy)接口销毁文本装饰线样式对象。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
