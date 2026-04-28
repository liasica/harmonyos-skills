---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor_array
title: Rcp_InterceptorArray
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_InterceptorArray
category: harmonyos-references
scraped_at: 2026-04-28T08:09:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0425611fb4dcdf50ee4d301f93eddd34d1b21f57470bbbbad4e16cd53d48cc7e
---

## 概述

PhonePC/2in1TabletTVWearable

异步拦截器数组。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Interceptor](_rcp___interceptor.md) \* [interceptors](_rcp___interceptor_array.md#interceptors) | 异步拦截器数组。 [Rcp\_Interceptor](_rcp___interceptor.md)[]。 |
| int [size](_rcp___interceptor_array.md#size) | 数组大小。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### interceptors

PhonePC/2in1TabletTVWearable

```
1. Rcp_Interceptor* Rcp_InterceptorArray::interceptors
```

**描述**

异步拦截器数组。 [Rcp\_Interceptor](_rcp___interceptor.md)[]。

### size

PhonePC/2in1TabletTVWearable

```
1. int Rcp_InterceptorArray::size
```

**描述**

数组大小。
