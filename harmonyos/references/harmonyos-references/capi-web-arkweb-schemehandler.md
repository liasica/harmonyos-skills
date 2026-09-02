---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-schemehandler
title: ArkWeb_SchemeHandler_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_SchemeHandler_
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:0af730c78a2172890154c3fa70a4273bef5aa9fb8c96a67414cf973ed1e6b231
---

```c
typedef struct ArkWeb_SchemeHandler_ ArkWeb_SchemeHandler
```

## 概述

ArkWeb\_SchemeHandler是用于注册自定义Scheme（协议）拦截器的结构体，定义了onRequestStart请求开始回调和onRequestStop请求停止回调两个函数指针。通过该结构体，开发者可以拦截Web组件中指定scheme的网络请求，适用于资源本地化、数据模拟、请求过滤、协议扩展等场景：在onRequestStart中判断是否拦截并返回自定义数据，在onRequestStop中执行资源清理，onRequestStart和onRequestStop会按请求生命周期顺序依次调用。该结构体配合ArkWeb\_ResourceHandler和ArkWeb\_Response实现完整的请求拦截与自定义响应流程，调用顺序为：ArkWeb\_SchemeHandler拦截请求 → ArkWeb\_ResourceHandler处理资源 → ArkWeb\_Response返回响应。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**系统能力：** SystemCapability.Web.Webview.Core

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
