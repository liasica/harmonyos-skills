---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-spanstyle
title: OH_ArkUI_SpanStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_SpanStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0ef192434465ed0c70532fe2addb2fdfa3b1d477efaa275a1416bee650206a28
---

```c
typedef struct OH_ArkUI_SpanStyle OH_ArkUI_SpanStyle
```

## 概述

定义属性字符串样式对象，用于对属性字符串中指定范围的文本设置样式效果，支持多种样式类型的灵活组合与精确范围指定，适用于需要对同一属性字符串中不同片段分别应用不同样式以实现富文本效果的场景，例如聊天应用中不同消息片段使用不同颜色和字体大小、新闻阅读应用中对标题和正文分别设置不同样式、笔记应用中高亮标注关键内容等。

调用[OH\_ArkUI\_SpanStyle\_Create](capi-styled-string-h.md#oh_arkui_spanstyle_create)接口创建属性字符串样式对象。

调用[OH\_ArkUI\_SpanStyle\_Destroy](capi-styled-string-h.md#oh_arkui_spanstyle_destroy)接口销毁属性字符串样式对象。

对象创建后，需调用[OH\_ArkUI\_SpanStyle\_SetStart](capi-styled-string-h.md#oh_arkui_spanstyle_setstart)和[OH\_ArkUI\_SpanStyle\_SetLength](capi-styled-string-h.md#oh_arkui_spanstyle_setlength)指定样式作用的范围。

调用OH\_ArkUI\_SpanStyle\_SetXXXStyle系列接口设置生效的具体样式，范围指定与样式设置需配合使用才能使样式在指定范围内生效。

例如调用[OH\_ArkUI\_SpanStyle\_SetTextStyle](capi-styled-string-h.md#oh_arkui_spanstyle_settextstyle)设置字体样式效果。配置完成的SpanStyle需添加到属性字符串中方可生效。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
