---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-interceptor-type-h
title: http_interceptor_type.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > http_interceptor_type.h
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca665b43eb2b58d13837d85b1f42bf9ed10887806b97dcaa67e6e17546fdc059
---

## 概述

为HTTP全局拦截器模块提供C接口的数据结构定义，包含拦截器的请求/响应头信息、HTTP请求/响应数据包结构、拦截器配置信息以及相关的枚举类型和函数指针。

**引用文件：** <network/netstack/http\_interceptor\_type.h>

**库：** libhttp\_interceptor.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 24

**相关模块：** [netstack](capi-netstack.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Http\_Interceptor\_Headers](capi-netstack-http-interceptor-headers.md) | OH\_Http\_Interceptor\_Headers | 定义拦截器的请求/响应头信息。 |
| [OH\_Http\_Interceptor\_Request](capi-netstack-http-interceptor-request.md) | OH\_Http\_Interceptor\_Request | 定义拦截器的HTTP请求数据包结构。 |
| [OH\_Http\_Interceptor\_Response](capi-netstack-http-interceptor-response.md) | OH\_Http\_Interceptor\_Response | 定义拦截器的HTTP响应数据包结构。 |
| [OH\_Http\_Interceptor](capi-netstack-http-interceptor.md) | OH\_Http\_Interceptor | 定义HTTP全局拦截器的配置信息。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [OH\_Interceptor\_Stage](capi-net-http-interceptor-type-h.md#oh_interceptor_stage) | OH\_Interceptor\_Stage | 定义拦截器的执行阶段。 |
| [OH\_Interceptor\_Type](capi-net-http-interceptor-type-h.md#oh_interceptor_type) | OH\_Interceptor\_Type | 定义拦截器的类型。 |
| [OH\_Interceptor\_Result](capi-net-http-interceptor-type-h.md#oh_interceptor_result) | OH\_Interceptor\_Result | 定义拦截器的处理结果。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef OH\_Interceptor\_Result (\*OH\_Http\_InterceptorHandler)(OH\_Http\_Interceptor\_Request \*request, OH\_Http\_Interceptor\_Response \*response, int32\_t \*isModified)](capi-net-http-interceptor-type-h.md#oh_http_interceptorhandler) | OH\_Http\_InterceptorHandler | 指向HTTP拦截器处理函数的指针。 |

## 枚举类型说明

### OH\_Interceptor\_Stage

```c
enum OH_Interceptor_Stage
```

**描述**

定义拦截器的执行阶段。

**起始版本：** 24

**参数：**

| 枚举项 | 描述 |
| --- | --- |
| OH\_STAGE\_REQUEST | 拦截器处理请求。 |
| OH\_STAGE\_RESPONSE | 拦截器处理响应。 |

### OH\_Interceptor\_Type

```c
enum OH_Interceptor_Type
```

**描述**

定义拦截器的类型。

**参数：**

| 枚举项 | 描述 |
| --- | --- |
| OH\_TYPE\_READ\_ONLY | 只读拦截器。**起始版本：** 24。 |
| OH\_TYPE\_MODIFY\_NETWORK\_KIT | 可修改拦截器。仅针对Network Kit HTTP请求生效。**起始版本：** 26.0.0。 |

### OH\_Interceptor\_Result

```c
enum OH_Interceptor_Result
```

**描述**

定义拦截器的处理结果。

**起始版本：** 24

**参数：**

| 枚举项 | 描述 |
| --- | --- |
| OH\_CONTINUE | 继续处理。 |
| OH\_ABORT | 拦截处理。 |

## 函数说明

### OH\_Http\_InterceptorHandler()

```c
typedef OH_Interceptor_Result (*OH_Http_InterceptorHandler)(
    OH_Http_Interceptor_Request *request,
    OH_Http_Interceptor_Response *response,
    int32_t *isModified)
```

**描述**

定义HTTP拦截器处理函数。

**起始版本：** 24

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_Http\_Interceptor\_Request](capi-netstack-http-interceptor-request.md) \*request | HTTP请求数据包指针（仅在请求阶段有效）。 |
| [OH\_Http\_Interceptor\_Response](capi-netstack-http-interceptor-response.md) \*response | HTTP响应数据包指针（仅在响应阶段有效）。 |
| int32\_t \*isModified | 标识拦截器是否修改了数据包。对OH\_TYPE\_READ\_ONLY类型拦截器无效，可配置为nullptr。  - 0表示未对数据执行修改操作。  - 非0表示已对数据执行修改操作。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [OH\_Interceptor\_Result](capi-net-http-interceptor-type-h.md#oh_interceptor_result) | 拦截器处理结果。  - OH\_CONTINUE：继续处理  - OH\_ABORT：拦截处理 |
