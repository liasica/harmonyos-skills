---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netcapabilities
title: NetConn_NetCapabilities
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetCapabilities
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0051eab37af20a820b9cff1d54544cb4c953de0c086ced03e73a773292d24dbb
---

```c
typedef struct NetConn_NetCapabilities {...} NetConn_NetCapabilities
```

## 概述

网络能力集。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t linkUpBandwidthKbps | 上行带宽。 |
| uint32\_t linkDownBandwidthKbps | 下行带宽。 |
| [NetConn\_NetCap](capi-net-connection-type-h.md#netconn_netcap) netCaps[[NETCONN\_MAX\_CAP\_SIZE](capi-net-connection-type-h.md#宏定义)] | 网络能力列表。 |
| int32\_t netCapsSize | 网络能力列表的实际size。 |
| [NetConn\_NetBearerType](capi-net-connection-type-h.md#netconn_netbearertype) bearerTypes[[NETCONN\_MAX\_BEARER\_TYPE\_SIZE](capi-net-connection-type-h.md#宏定义)] | 承载类型列表。 |
| int32\_t bearerTypesSize | 承载类型列表的实际size。 |
