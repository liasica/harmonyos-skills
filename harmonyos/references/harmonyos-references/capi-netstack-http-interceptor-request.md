---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-request
title: OH_Http_Interceptor_Request
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor_Request
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:58f10196b5c26beaaa669e50ad38864b39da14d1bd44b7d34326f5fbcff9f082
---

```c
typedef struct OH_Http_Interceptor_Request {
    Http_Buffer url;
    Http_Buffer method;
    OH_Http_Interceptor_Headers *headers;
    Http_Buffer body;
} OH_Http_Interceptor_Request;
```

## 概述

定义拦截器的HTTP请求数据包结构。

**起始版本：** 24

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](capi-net-http-interceptor-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| Http\_Buffer url | 请求URL，详情请参考[Http\_Buffer](capi-netstack-http-buffer.md)定义。 |
| Http\_Buffer method | 请求方法，详情请参考[Http\_Buffer](capi-netstack-http-buffer.md)定义。 |
| OH\_Http\_Interceptor\_Headers \*headers | HTTP请求头信息，详情请参考[OH\_Http\_Interceptor\_Headers](capi-netstack-http-interceptor-headers.md)定义。 |
| Http\_Buffer body | 请求体内容，详情请参考[Http\_Buffer](capi-netstack-http-buffer.md)定义。 |
