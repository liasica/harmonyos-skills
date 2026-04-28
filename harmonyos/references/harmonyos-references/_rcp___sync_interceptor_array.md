---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___sync_interceptor_array
title: Rcp_SyncInterceptorArray
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_SyncInterceptorArray
category: harmonyos-references
scraped_at: 2026-04-28T08:09:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:21687c03f8a98294da7461ff7630d62a3cd6974252f26ea064606903ecdd007a
---

## 概述

PhonePC/2in1TabletTVWearable

同步拦截器数组。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md) \* [interceptors](_rcp___sync_interceptor_array.md#interceptors) | 同步拦截器数组。 [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)[]。 |
| int [size](_rcp___sync_interceptor_array.md#size) | 数组大小。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### interceptors

PhonePC/2in1TabletTVWearable

```
1. Rcp_SyncInterceptor* Rcp_SyncInterceptorArray::interceptors
```

**描述**

同步拦截器数组。 [Rcp\_SyncInterceptor](_rcp___sync_interceptor.md)[]。

### size

PhonePC/2in1TabletTVWearable

```
1. int Rcp_SyncInterceptorArray::size
```

**描述**

数组大小。
