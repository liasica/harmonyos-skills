---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor
title: Rcp_Interceptor
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Interceptor
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fec1c0098e967bbc8bf79399ac9d5c3876829e561fb2bd90624911625412beb1
---

## 概述

异步拦截器。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t(\* [intercept](_rcp___interceptor.md#intercept) )([Rcp\_Request](_rcp___request.md) \*request, const [Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler) \*next, const [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md) \*responseCallback) | 指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。 |

## 结构体成员变量说明

### intercept

```cpp
uint32_t(* Rcp_Interceptor::intercept) (Rcp_Request *request, const Rcp_RequestHandler *next, const Rcp_ResponseCallbackObject *responseCallback)
```

**描述**

指向异步拦截器函数的指针。用户若需要使用拦截器，需实现该函数。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| request | 指向[Rcp\_Request](_rcp___request.md)的指针。 |
| next | 指向下一个异步处理器的指针[Rcp\_RequestHandler](remote-communication-overview.md#rcp_requesthandler)。 |
| responseCallback | 指向[Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md)的指针。 |

**返回：**

uint32\_t 返回表示拦截器的返回值。
