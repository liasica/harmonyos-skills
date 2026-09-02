---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-eventshandler
title: Http_EventsHandler
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_EventsHandler
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c60b2a6ca3067f07ccfbfb96aa50799674d1ca0e9acb699ac1fda0e922f1feaa
---

```c
typedef struct Http_EventsHandler {...} Http_EventsHandler
```

## 概述

监听不同HTTP事件的回调函数。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Http\_OnDataReceiveCallback](capi-net-http-type-h.md#http_ondatareceivecallback) onDataReceive | 收到响应体时的回调函数，参考[Http\_OnDataReceiveCallback](capi-net-http-type-h.md#http_ondatareceivecallback)。 |
| [Http\_OnProgressCallback](capi-net-http-type-h.md#http_onprogresscallback) onUploadProgress | 上传时调用的回调函数，参考[Http\_OnProgressCallback](capi-net-http-type-h.md#http_onprogresscallback)。 |
| [Http\_OnProgressCallback](capi-net-http-type-h.md#http_onprogresscallback) onDownloadProgress | 下载时调用的回调函数，参考[Http\_OnProgressCallback](capi-net-http-type-h.md#http_onprogresscallback)。 |
| [Http\_OnHeaderReceiveCallback](capi-net-http-type-h.md#http_onheaderreceivecallback) onHeadersReceive | 收到header时的回调函数，参考[Http\_OnHeaderReceiveCallback](capi-net-http-type-h.md#http_onheaderreceivecallback)。 |
| [Http\_OnVoidCallback](capi-net-http-type-h.md#http_onvoidcallback) onDataEnd | 传输结束时的回调函数，参考[Http\_OnVoidCallback](capi-net-http-type-h.md#http_onvoidcallback)。 |
| [Http\_OnVoidCallback](capi-net-http-type-h.md#http_onvoidcallback) onCanceled | 请求被取消时的回调函数，参考[Http\_OnVoidCallback](capi-net-http-type-h.md#http_onvoidcallback)。 |
