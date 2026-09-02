---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-response
title: OH_Http_Interceptor_Response
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor_Response
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b8c0f220932d93c3489dd2063f37cccdde5ac0bd3de410551212a403539c8323
---

```c
typedef struct OH_Http_Interceptor_Response {
    Http_Buffer body;
    Http_ResponseCode responseCode;
    OH_Http_Interceptor_Headers *headers;
    Http_PerformanceTiming performanceTiming;
} OH_Http_Interceptor_Response;
```

## 概述

定义拦截器的HTTP响应数据包结构。

**起始版本：** 24

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](capi-net-http-interceptor-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| Http\_Buffer body | 响应体内容，详情请参考[Http\_Buffer](capi-netstack-http-buffer.md)定义。 |
| Http\_ResponseCode responseCode | 响应状态码，详情请参考[Http\_ResponseCode](capi-net-http-type-h.md#http_responsecode) 枚举定义。 |
| OH\_Http\_Interceptor\_Headers \*headers | HTTP响应头信息，详情请参考[OH\_Http\_Interceptor\_Headers](capi-netstack-http-interceptor-headers.md)定义。 |
| Http\_PerformanceTiming performanceTiming | 响应性能信息，详情请参考[Http\_PerformanceTiming](capi-netstack-http-performancetiming.md)定义。 |
