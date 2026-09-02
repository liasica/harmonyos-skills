---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-leadingmarginspandrawinfo
title: OH_ArkUI_LeadingMarginSpanDrawInfo
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_LeadingMarginSpanDrawInfo
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a645a71450ffdecc2d7c49dfdb365b494c220c2ee91925f4877bb35c526e299f
---

```c
typedef struct OH_ArkUI_LeadingMarginSpanDrawInfo OH_ArkUI_LeadingMarginSpanDrawInfo
```

## 概述

定义段首缩进的自定义绘制信息，包含当前行的绘制上下文信息（如绘制区域、偏移量等），开发者可在回调函数中基于该信息实现自定义的段首缩进绘制逻辑，适用于需要在段落首行添加自定义图标、装饰元素或实现特殊缩进样式等场景，使段落排版更加灵活丰富。例如，在阅读应用中为段落首行绘制书签图标，或在文档编辑器中为特定段落绘制自定义缩进标记。

调用[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Create](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_create)接口创建对应的段首缩进的自定义绘制信息对象。

调用[OH\_ArkUI\_LeadingMarginSpanDrawInfo\_Destroy](capi-styled-string-h.md#oh_arkui_leadingmarginspandrawinfo_destroy)接口销毁该对象。

该对象用于在[OH\_ArkUI\_ParagraphStyle\_RegisterOnDrawLeadingMarginCallback](capi-styled-string-h.md#oh_arkui_paragraphstyle_registerondrawleadingmargincallback)注册的回调函数中，提供当前行的绘制上下文和自定义绘制信息对象。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
