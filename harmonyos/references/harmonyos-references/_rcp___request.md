---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request
title: Rcp_Request
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Request
category: harmonyos-references
scraped_at: 2026-04-28T08:09:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d0c9d8783e2ac2fe666d77dd852248d4e186d7adaa652dc9766b41e7391bf834
---

## 概述

PhonePC/2in1TabletTVWearable

网络请求。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char [id](_rcp___request.md#id) [[RCP\_MAX\_REQUEST\_ID\_LEN](remote-communication-overview.md#rcp_max_request_id_len)] | 每个请求的唯一ID。由系统生成。 |
| char \* [url](_rcp___request.md#url) | 请求URL。 |
| const char \* [method](_rcp___request.md#method) | 请求方法。默认值为GET。 |
| [Rcp\_Headers](remote-communication-overview.md#rcp_headers) \* [headers](_rcp___request.md#headers) | 请求标头。 |
| [Rcp\_RequestContent](_rcp___request_content.md) \* [content](_rcp___request.md#content) | 请求体。 |
| [Rcp\_Configuration](_rcp___configuration.md) \* [configuration](_rcp___request.md#configuration) | 请求配置。请参见[Rcp\_Configuration](_rcp___configuration.md)。 |
| [Rcp\_TransferRange](_rcp___transfer_range.md) \* [transferRange](_rcp___request.md#transferrange) | HTTP传输范围。该设置将转换为HTTP Range标头。 |
| [Rcp\_RequestCookies](remote-communication-overview.md#rcp_requestcookies) \* [cookies](_rcp___request.md#cookies) | 请求Cookie。该设置将转换为HTTP Cookie标头。 |
| void \* [requestPrivate](_rcp___request.md#requestprivate) | 可扩展字段。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### configuration

PhonePC/2in1TabletTVWearable

```
1. Rcp_Configuration* Rcp_Request::configuration
```

**描述**

请求配置。请参见[Rcp\_Configuration](_rcp___configuration.md)。

### content

PhonePC/2in1TabletTVWearable

```
1. Rcp_RequestContent* Rcp_Request::content
```

**描述**

请求体。

### cookies

PhonePC/2in1TabletTVWearable

```
1. Rcp_RequestCookies* Rcp_Request::cookies
```

**描述**

请求Cookie。该设置将转换为HTTP Cookie标头。

### headers

PhonePC/2in1TabletTVWearable

```
1. Rcp_Headers* Rcp_Request::headers
```

**描述**

请求标头。

### id

PhonePC/2in1TabletTVWearable

```
1. char Rcp_Request::id[RCP_MAX_REQUEST_ID_LEN]
```

**描述**

每个请求的唯一ID。由系统生成。

### method

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_Request::method
```

**描述**

请求方法。默认值为GET。

### requestPrivate

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_Request::requestPrivate
```

**描述**

可扩展字段。

### transferRange

PhonePC/2in1TabletTVWearable

```
1. Rcp_TransferRange* Rcp_Request::transferRange
```

**描述**

HTTP传输范围。该设置将转换为HTTP Range标头。

### url

PhonePC/2in1TabletTVWearable

```
1. char* Rcp_Request::url
```

**描述**

请求URL。
