---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule-oh-arkui-urlstyle
title: OH_ArkUI_UrlStyle
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > C API > 结构体 > OH_ArkUI_UrlStyle
category: harmonyos-references
scraped_at: 2026-09-02T14:51:52+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d5af80e051f7973899b718cf4a18005a04a5557b0815ca27bcf8c764cab90e9e
---

```c
typedef struct OH_ArkUI_UrlStyle OH_ArkUI_UrlStyle
```

## 概述

定义链接样式，用于为属性字符串中的文本设置可点击的URL链接效果，适用于需要在文本内容中嵌入可交互链接的场景，可提升文本的交互性和用户体验。

调用[OH\_ArkUI\_UrlStyle\_Create](capi-styled-string-h.md#oh_arkui_urlstyle_create)接口创建链接样式对象。

调用[OH\_ArkUI\_UrlStyle\_Destroy](capi-styled-string-h.md#oh_arkui_urlstyle_destroy)接口销毁链接样式对象。

创建链接样式对象后，调用[OH\_ArkUI\_UrlStyle\_SetUrl](capi-styled-string-h.md#oh_arkui_urlstyle_seturl)接口设置链接地址。

**起始版本：** 24

**相关模块：** [ArkUI\_NativeModule](capi-arkui-nativemodule.md)

**所在头文件：** [styled\_string.h](capi-styled-string-h.md)
