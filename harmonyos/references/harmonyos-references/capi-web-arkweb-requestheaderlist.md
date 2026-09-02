---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-requestheaderlist
title: ArkWeb_RequestHeaderList_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_RequestHeaderList_
category: harmonyos-references
scraped_at: 2026-09-02T14:51:56+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:05aab9e9547a23d164f4652cf761bb3c039667914e3d7527cae257549d25b906
---

```c
typedef struct ArkWeb_RequestHeaderList_ ArkWeb_RequestHeaderList
```

## 概述

ArkWeb\_RequestHeaderList是HTTP请求头列表结构体，用于在ArkWeb NDK中表示和管理HTTP请求头的键值对集合。该结构体包含请求头数组（headers）和数组长度（headerCount），headers为ArkWeb\_RequestHeader指针数组，headerCount表示数组元素个数。该结构体配合ArkWeb\_ResourceRequest等结构体使用，提供对Web组件网络请求头的读取和设置能力。使用场景：在自定义协议处理器中处理HTTP请求头、在网络请求拦截器中修改请求头、在API鉴权场景中添加认证头、在缓存控制和内容协商等场景中配置请求头。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**系统能力：** SystemCapability.Web.Webview.Core

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
