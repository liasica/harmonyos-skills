---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcehandler
title: ArkWeb_ResourceHandler_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ResourceHandler_
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:9b414adbaa51af6ed8aa6449ea1979a7f9b500ac559be1d7a53e9b91442b4bb3
---

```c
typedef struct ArkWeb_ResourceHandler_ ArkWeb_ResourceHandler
```

## 概述

ArkWeb\_ResourceHandler是用于处理被拦截的Scheme请求的资源处理器结构体。在ArkWeb\_SchemeHandler拦截到指定scheme的请求后，通过该结构体可以向Web组件返回自定义的响应数据，包括响应状态码、响应头、响应体等。该结构体在onRequestStart回调中作为参数传入，开发者通过它实现对被拦截请求的完全自定义响应。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**系统能力：** SystemCapability.Web.Webview.Core

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
