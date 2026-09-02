---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-httpbodystream
title: ArkWeb_HttpBodyStream_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_HttpBodyStream_
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:f56770ed9a248ac012ec388423d827a1c2e9af5bd096f2f4f62cdc9a39bcc5cb
---

```c
typedef struct ArkWeb_HttpBodyStream_ ArkWeb_HttpBodyStream
```

## 概述

ArkWeb\_HttpBodyStream是HTTP请求体流结构体，用于在自定义Scheme请求拦截场景中获取HTTP请求的body数据。当拦截到的POST等包含请求体的HTTP请求时，可通过该结构体读取请求体的原始字节流数据。该结构体通常与ArkWeb\_ResourceRequest配合使用，在ArkWeb\_SchemeHandler的回调中获取完整的请求信息。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**系统能力：** SystemCapability.Web.Webview.Core

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
