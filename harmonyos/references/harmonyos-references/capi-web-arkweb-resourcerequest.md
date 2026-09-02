---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcerequest
title: ArkWeb_ResourceRequest_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ResourceRequest_
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:6679279ee33d60f1db6f5d785a0ef675603a0f539ad5d9c6814f2e2e51623c70
---

```c
typedef struct ArkWeb_ResourceRequest_ ArkWeb_ResourceRequest
```

## 概述

ArkWeb\_ResourceRequest是被拦截的Scheme请求的详细信息结构体，包含请求的URL、HTTP方法、请求头等元数据。该结构体在ArkWeb\_SchemeHandler的onRequestStart回调中作为参数传入，适用于自定义协议处理、资源拦截等场景，帮助开发者实现跨域请求控制、本地资源映射等功能，从而增强安全性和性能。开发者通过它获取被拦截请求的完整信息，据此决定是否拦截以及如何构建自定义响应。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**系统能力：** SystemCapability.Web.Webview.Core

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
