---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response
title: Rcp_Response
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Response
category: harmonyos-references
scraped_at: 2026-04-28T08:09:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1dfcf84790299b900114f4cd22b8134ce83537c7b485c38b03b469238f2a39eb
---

## 概述

PhonePC/2in1TabletTVWearable

网络请求的响应。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const [Rcp\_Request](_rcp___request.md) \* [request](_rcp___response.md#request) | 表示生成响应的请求。 |
| char \* [effectiveUrl](_rcp___response.md#effectiveurl) | 上次使用的有效URL。 |
| [Rcp\_StatusCode](remote-communication-overview.md#rcp_statuscode)[statusCode](_rcp___response.md#statuscode) | 响应状态码。 |
| [Rcp\_Headers](remote-communication-overview.md#rcp_headers) \* [headers](_rcp___response.md#headers) | 响应标头。 |
| [Rcp\_Buffer](_rcp___buffer.md)[body](_rcp___response.md#body) | 响应消息体。 |
| [Rcp\_DebugInfo](_rcp___debug_info.md) \* [debugInfo](_rcp___response.md#debuginfo) | 请求/响应处理调试信息。 |
| [Rcp\_TimeInfo](_rcp___time_info.md) \* [timeInfo](_rcp___response.md#timeinfo) | 响应时间信息。 |
| [Rcp\_ResponseCookies](_rcp___response_cookies.md) \* [cookies](_rcp___response.md#cookies) | 响应Cookies。 |
| const [Rcp\_ResponseCallbackObject](_rcp___response_callback_object.md) \* [responseCallback](_rcp___response.md#responsecallback) | 使用的响应回调。 |
| void(\* [destroyResponse](_rcp___response.md#destroyresponse) )(struct [Rcp\_Response](_rcp___response.md) \*response) | 用于销毁响应的方法。 |
| void \* [responsePrivate](_rcp___response.md#responseprivate) | 可扩展字段。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### body

PhonePC/2in1TabletTVWearable

```
1. Rcp_Buffer Rcp_Response::body
```

**描述**

响应消息体。

### cookies

PhonePC/2in1TabletTVWearable

```
1. Rcp_ResponseCookies* Rcp_Response::cookies
```

**描述**

响应Cookies。

### debugInfo

PhonePC/2in1TabletTVWearable

```
1. Rcp_DebugInfo* Rcp_Response::debugInfo
```

**描述**

请求/响应处理调试信息。

收集的事件取决于[Rcp\_TracingConfiguration](_rcp___tracing_configuration.md)配置信息。

### destroyResponse

PhonePC/2in1TabletTVWearable

```
1. void(* Rcp_Response::destroyResponse) (struct Rcp_Response *response)
```

**描述**

用于销毁响应的方法。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| --- | --- |
| response | 指示要销毁的响应。它是一个指向[Rcp\_Response](_rcp___response.md)的指针。 |

### effectiveUrl

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_Response::effectiveUrl
```

**描述**

上次使用的有效URL。

如果重定向，或设置了[Rcp\_SessionConfiguration.baseUrl](_rcp___session_configuration.md#baseurl)，则有效URL可能不等于[Rcp\_Request.url](_rcp___request.md#url)。

### headers

PhonePC/2in1TabletTVWearable

```
1. Rcp_Headers* Rcp_Response::headers
```

**描述**

响应标头。

### request

PhonePC/2in1TabletTVWearable

```
1. const Rcp_Request* Rcp_Response::request
```

**描述**

表示生成响应的请求。

### responseCallback

PhonePC/2in1TabletTVWearable

```
1. const Rcp_ResponseCallbackObject* Rcp_Response::responseCallback
```

**描述**

使用的响应回调。

### responsePrivate

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_Response::responsePrivate
```

**描述**

可扩展字段。

### statusCode

PhonePC/2in1TabletTVWearable

```
1. Rcp_StatusCode Rcp_Response::statusCode
```

**描述**

响应状态码。

### timeInfo

PhonePC/2in1TabletTVWearable

```
1. Rcp_TimeInfo* Rcp_Response::timeInfo
```

**描述**

响应时间信息。

是否收集该信息取决于[Rcp\_TracingConfiguration.collectTimeInfo](_rcp___tracing_configuration.md#collecttimeinfo)文件中的配置信息。
