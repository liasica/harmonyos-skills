---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor
title: Rcp_SyncInterceptor
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_SyncInterceptor
category: harmonyos-references
scraped_at: 2026-04-28T08:09:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46ab4e84d107efa556be2104d1c81b1edd0b8c41909004d6a159e0dbdfb07f24
---

## 概述

PhonePC/2in1TabletTVWearable

同步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Response](_rcp___response.md) \*(\* [intercept](_rcp___sync_interceptor.md#intercept) )([Rcp\_Request](_rcp___request.md) \*request, const [Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler) \*next, uint32\_t \*errCode) | 指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### intercept

PhonePC/2in1TabletTVWearable

```
1. Rcp_Response*(* Rcp_SyncInterceptor::intercept) (Rcp_Request *request, const Rcp_SyncRequestHandler *next, uint32_t *errCode)
```

**描述**

指向同步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 指向[Rcp\_Request](_rcp___request.md)的指针。 |
| next | 指向下一个同步处理器的指针[Rcp\_SyncRequestHandler](remote-communication-overview.md#rcp_syncrequesthandler)。 |
| errCode | 表示拦截器的返回值。 |

**返回：**

Rcp\_Response\* 返回的响应。
