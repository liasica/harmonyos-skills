---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-interceptor
title: OH_Http_Interceptor
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_Http_Interceptor
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5f996855c913565b463cf33071ba1e6cd5984e8dfbe63005e1b3ea9e69978cbb
---

```c
typedef struct OH_Http_Interceptor {
    int32_t groupId;
    OH_Interceptor_Stage stage;
    OH_Interceptor_Type type;
    OH_Http_InterceptorHandler handler;
    int32_t enabled;
} OH_Http_Interceptor;
```

## 概述

定义HTTP全局拦截器的配置信息。

**起始版本：** 24

**相关模块：** [netstack](capi-netstack.md)

**所在头文件：** [http\_interceptor\_type.h](capi-net-http-interceptor-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| int32\_t groupId | 拦截器组ID。 |
| OH\_Interceptor\_Stage stage | 拦截器的执行阶段，详情请参考[OH\_Interceptor\_Stage](capi-net-http-interceptor-type-h.md#oh_interceptor_stage) 枚举定义。 |
| OH\_Interceptor\_Type type | 拦截器的类型，详情请参考[OH\_Interceptor\_Type](capi-net-http-interceptor-type-h.md#oh_interceptor_type) 枚举定义。 |
| OH\_Http\_InterceptorHandler handler | 拦截器处理函数，详情请参考[OH\_Http\_InterceptorHandler](capi-net-http-interceptor-type-h.md#oh_http_interceptorhandler) 函数指针定义。 |
| int32\_t enabled | 拦截器的启用状态。0代表未启用，非0代表启用。 |
