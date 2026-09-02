---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___interceptor_array
title: Rcp_InterceptorArray
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_InterceptorArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:544a32df3a542b5f028a38ec95eeebf92cc703040c68df04c1b717e7c7b52feb
---

## 概述

异步拦截器数组。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_Interceptor](_rcp___interceptor.md) \* [interceptors](_rcp___interceptor_array.md#interceptors) | 异步拦截器数组。 [Rcp\_Interceptor](_rcp___interceptor.md)[]。 |
| int [size](_rcp___interceptor_array.md#size) | 数组大小。 |

## 结构体成员变量说明

### interceptors

```cpp
Rcp_Interceptor* Rcp_InterceptorArray::interceptors
```

**描述**

异步拦截器数组。 [Rcp\_Interceptor](_rcp___interceptor.md)[]。

### size

```cpp
int Rcp_InterceptorArray::size
```

**描述**

数组大小。
