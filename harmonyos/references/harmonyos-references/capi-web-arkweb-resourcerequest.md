---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web-arkweb-resourcerequest
title: ArkWeb_ResourceRequest_
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 结构体 > ArkWeb_ResourceRequest_
category: harmonyos-references
scraped_at: 2026-04-28T08:05:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c1efeaf99099a8665197e01c9a74ee950df0e13eba275bdfed203c57d580afef
---

```
1. typedef struct ArkWeb_ResourceRequest_ ArkWeb_ResourceRequest
```

## 概述

PhonePC/2in1TabletTVWearable

对应内核的一个请求，可以通过OH\_ArkWebResourceRequest\_系列接口获取请求的URL、method、post data以及其他信息。如通过[OH\_ArkWebResourceRequest\_GetUrl](capi-arkweb-scheme-handler-h.md#oh_arkwebresourcerequest_geturl)获取请求的URL。

**起始版本：** 12

**相关模块：** [Web](capi-web.md)

**所在头文件：** [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md)
