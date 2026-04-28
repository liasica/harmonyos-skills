---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response
title: Http_Response
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > Http_Response
category: harmonyos-references
scraped_at: 2026-04-28T08:08:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:a7e1af43e77a0803db039794a4552951c5097c6a1ec643ce007b1f3045b8c2c3
---

```
1. typedef struct Http_Response {...} Http_Response
```

## 概述

PhonePC/2in1TabletTVWearable

定义HTTP响应的结构体。

**起始版本：** 20

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [net\_http\_type.h](capi-net-http-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Http\_Buffer](capi-netstack-http-buffer.md) body | HTTP请求响应的数据，参考[Http\_Buffer](capi-netstack-http-buffer.md)。 |
| [Http\_ResponseCode](capi-net-http-type-h.md#http_responsecode) responseCode | HTTP请求响应码，参考[Http\_ResponseCode](capi-net-http-type-h.md#http_responsecode)。 |
| [Http\_Headers](capi-netstack-http-headers.md) \*headers | HTTP响应的头，指向Http\_Headers的指针，参考[Http\_Headers](capi-netstack-http-headers.md)。 |
| char \*cookies | HTTP响应Cookies。 |
| [Http\_PerformanceTiming](capi-netstack-http-performancetiming.md) \*performanceTiming | HTTP响应时间信息，指向Http\_PerformanceTiming的指针，参考[Http\_PerformanceTiming](capi-netstack-http-performancetiming.md)。 |

### 成员函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [void (\*destroyResponse)(struct Http\_Response \*\*response)](capi-netstack-http-response.md#destroyresponse) | 销毁HTTP响应的回调函数 |

## 成员函数说明

PhonePC/2in1TabletTVWearable

### destroyResponse()

PhonePC/2in1TabletTVWearable

```
1. void (*destroyResponse)(struct Http_Response **response)
```

**描述**

销毁HTTP响应的回调函数

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| struct [Http\_Response](capi-netstack-http-response.md) \*\*response | 要销毁的HTTP响应，指向Http\_Response的指针，参考[Http\_Response](capi-netstack-http-response.md)。 |
