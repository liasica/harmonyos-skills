---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-errorinfo
title: ArkWeb_ErrorInfo_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ErrorInfo_
category: harmonyos-references
scraped_at: 2026-11-12T09:55:02+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:348f3e884445e73b04a5f3378e2075e16adf92fb411f42c177280fa1db278fd9
---

```c
typedef struct ArkWeb_ErrorInfo_ ArkWeb_ErrorInfo
```

## 概述

ArkWeb\_ErrorInfo是响应错误详情结构体，用于在自定义Scheme请求拦截场景中设置响应的错误信息。开发者可以通过该结构体设置错误码、自定义错误码以及是否在未收到响应时自动生成响应。该结构体通常与ArkWeb\_ResourceHandler配合使用，在请求失败时通过OH\_ArkWebResourceHandler\_DidFailWithErrorInfo传递错误信息。

**起始版本：** 26.0.1

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
