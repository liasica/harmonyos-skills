---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-response
title: ArkWeb_Response_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_Response_
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:51d99dd70e9256f7e05650596da15a91774e2da6f4782dd4c1ab73929f0c7a58
---

```c
typedef struct ArkWeb_Response_ ArkWeb_Response
```

## 概述

ArkWeb\_Response是用于构建自定义HTTP响应的结构体，定义了响应状态码、响应头、响应体等核心字段。该结构体配合ArkWeb\_ResourceHandler使用，在Scheme请求拦截场景中为被拦截的请求提供完整的HTTP响应数据，实现自定义的资源返回能力。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**系统能力：** SystemCapability.Web.Webview.Core

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
