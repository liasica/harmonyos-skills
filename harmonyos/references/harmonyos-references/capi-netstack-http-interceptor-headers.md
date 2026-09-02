---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor-headers
title: OH_Http_Interceptor_Headers
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor_Headers
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95692e02858d880515cb214b79d44e8d513daa53cc1a1001897b467637bcc06f
---

```c
typedef struct OH_Http_Interceptor_Headers {
    char *data;
    struct OH_Http_Interceptor_Headers *next;
} OH_Http_Interceptor_Headers;
```

## 概述

定义拦截器的请求/响应头信息。

**起始版本：** 24

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](capi-net-http-interceptor-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char \*data | 拦截器请求/响应头信息。 |
| struct OH\_Http\_Interceptor\_Headers \*next | 指向下一个头信息的指针。 |
