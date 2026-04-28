---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-h
title: net_http.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_http.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:34+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1fee0719477870f04b617706d87d0b712b6eb149520744edf89e716737976e0c
---

## 概述

PhonePC/2in1TabletTVWearable

定义HTTP请求模块的接口。

**引用文件：** <network/netstack/net\_http.h>

**库：** libnet\_http.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Http\_Headers \*OH\_Http\_CreateHeaders(void)](capi-net-http-h.md#oh_http_createheaders) | 创建HTTP请求或者响应的头。 |
| [void OH\_Http\_DestroyHeaders(Http\_Headers \*\*headers)](capi-net-http-h.md#oh_http_destroyheaders) | 销毁HTTP请求或者响应的头。 |
| [uint32\_t OH\_Http\_SetHeaderValue(struct Http\_Headers \*headers, const char \*name, const char \*value)](capi-net-http-h.md#oh_http_setheadervalue) | 设置HTTP请求或者响应的头的键值对。 |
| [Http\_HeaderValue \*OH\_Http\_GetHeaderValue(Http\_Headers \*headers, const char \*name)](capi-net-http-h.md#oh_http_getheadervalue) | 通过键获取请求或响应头的值。 |
| [Http\_HeaderEntry \*OH\_Http\_GetHeaderEntries(Http\_Headers \*headers)](capi-net-http-h.md#oh_http_getheaderentries) | 获取请求或响应头的所有键值对。 |
| [void OH\_Http\_DestroyHeaderEntries(Http\_HeaderEntry \*\*headerEntry)](capi-net-http-h.md#oh_http_destroyheaderentries) | 销毁OH\_Http\_GetHeaderEntries中获取的所有键值对。 |
| [Http\_Request \*OH\_Http\_CreateRequest(const char \*url)](capi-net-http-h.md#oh_http_createrequest) | 创建HTTP请求。 |
| [int OH\_Http\_Request(Http\_Request \*request, Http\_ResponseCallback callback, Http\_EventsHandler handler)](capi-net-http-h.md#oh_http_request) | 发起HTTP请求。 |
| [void OH\_Http\_Destroy(struct Http\_Request \*\*request)](capi-net-http-h.md#oh_http_destroy) | 销毁HTTP请求。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_Http\_CreateHeaders()

PhonePC/2in1TabletTVWearable

```
1. Http_Headers *OH_Http_CreateHeaders(void)
```

**描述**

创建HTTP请求或者响应的头。

说明

建议在本次HTTP请求结束后，及时调用[OH\_Http\_DestroyHeaders](capi-net-http-h.md#oh_http_destroyheaders)销毁HTTP请求或者响应的头，执行资源清理等操作。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Http\_Headers](capi-netstack-http-headers.md) \* | Http\_Headers 返回HTTP请求或者响应的头，指向Http\_Headers。 |

### OH\_Http\_DestroyHeaders()

PhonePC/2in1TabletTVWearable

```
1. void OH_Http_DestroyHeaders(Http_Headers **headers)
```

**描述**

销毁HTTP请求或者响应的头。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Http\_Headers](capi-netstack-http-headers.md) \*\*headers | 要被销毁的HTTP请求或响应的头，是通过OH\_Http\_CreateHeaders生成的数据。 |

### OH\_Http\_SetHeaderValue()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_Http_SetHeaderValue(struct Http_Headers *headers, const char *name, const char *value)
```

**描述**

设置HTTP请求或者响应的头的键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct Http\_Headers](capi-netstack-http-headers.md) \*headers | 指向要设置的Http\_Headers的指针。 |
| const char \*name | 键值。 |
| const char \*value | 键值对应的值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | uint32\_t 0 - 成功。 401 - 参数错误。 2300027 - 内存不足。 |

### OH\_Http\_GetHeaderValue()

PhonePC/2in1TabletTVWearable

```
1. Http_HeaderValue *OH_Http_GetHeaderValue(Http_Headers *headers, const char *name)
```

**描述**

通过键获取请求或响应头的值。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Http\_Headers](capi-netstack-http-headers.md) \*headers | 指向要获取值的Http\_Headers的指针。 |
| const char \*name | 键值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Http\_HeaderValue](capi-netstack-http-headervalue.md) \* | Http\_HeaderValue 指向获取的Http\_HeaderValue的指针。 |

### OH\_Http\_GetHeaderEntries()

PhonePC/2in1TabletTVWearable

```
1. Http_HeaderEntry *OH_Http_GetHeaderEntries(Http_Headers *headers)
```

**描述**

获取请求或响应头的所有键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Http\_Headers](capi-netstack-http-headers.md) \*headers | 指向要获取值的Http\_Headers的指针。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Http\_HeaderEntry](capi-netstack-http-headerentry.md) \* | Http\_HeaderEntry 指向获取的Http\_HeaderEntry的指针。 |

### OH\_Http\_DestroyHeaderEntries()

PhonePC/2in1TabletTVWearable

```
1. void OH_Http_DestroyHeaderEntries(Http_HeaderEntry **headerEntry)
```

**描述**

销毁OH\_Http\_GetHeaderEntries中获取的所有键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Http\_HeaderEntry](capi-netstack-http-headerentry.md) \*\*headerEntry | 指向要销毁的Http\_HeaderEntry的指针，是通过OH\_Http\_GetHeaderEntries获取的数据。 |

### OH\_Http\_CreateRequest()

PhonePC/2in1TabletTVWearable

```
1. Http_Request *OH_Http_CreateRequest(const char *url)
```

**描述**

创建HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*url | 请求URL。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Http\_Request](capi-netstack-http-request.md) \* | 返回创建的请求，指向Http\_Request的指针。 |

### OH\_Http\_Request()

PhonePC/2in1TabletTVWearable

```
1. int OH_Http_Request(Http_Request *request, Http_ResponseCallback callback, Http_EventsHandler handler)
```

**描述**

发起HTTP请求。

说明

建议在本次HTTP请求收到响应并处理完毕后，及时调用[OH\_Http\_Destroy](capi-net-http-h.md#oh_http_destroy)中断HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Http\_Request](capi-netstack-http-request.md) \*request | 发送的请求，指向Http\_Request的指针。 |
| [Http\_ResponseCallback](capi-net-http-type-h.md#http_responsecallback) callback | 请求的响应，指向Http\_ResponseCallback。 |
| [Http\_EventsHandler](capi-netstack-http-eventshandler.md) handler | 监听不同HTTP事件的回调函数，指向Http\_EventsHandler。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 请求发起成功返回0，非0表示请求发起失败，错误码的具体描述，可以参考Http\_ErrCode。  在Http\_ResponseCallback中也会携带errCode信息，表示请求发起成功，但是因为一些原因，和服务器的交互异常，具体异常原因，同步参考Http\_ErrCode。 |

### OH\_Http\_Destroy()

PhonePC/2in1TabletTVWearable

```
1. void OH_Http_Destroy(struct Http_Request **request)
```

**描述**

中断HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [struct Http\_Request](capi-netstack-http-request.md) \*\*request | 要中断的请求，指向Http\_Request的指针，参考[Http\_Request](capi-netstack-http-request.md)。 |
