---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor_array
title: Rcp_SyncInterceptorArray
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_SyncInterceptorArray
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:534e5e3c6f69ec9bbcdf4325c6e07beb8390bab97e880674c87e4d598a01d8cd
---

## 概述

同步拦截器数组。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md) \* [interceptors](_rcp___sync_interceptor_array.md#interceptors) | 同步拦截器数组。 [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)[]。 |
| int [size](_rcp___sync_interceptor_array.md#size) | 数组大小。 |

## 结构体成员变量说明

### interceptors

```cpp
Rcp_SyncInterceptor* Rcp_SyncInterceptorArray::interceptors
```

**描述**

同步拦截器数组。 [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)[]。

### size

```cpp
int Rcp_SyncInterceptorArray::size
```

**描述**

数组大小。
