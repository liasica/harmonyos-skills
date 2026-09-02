---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipaddress
title: OH_TrafficFilter_IPAddress
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_IPAddress
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:15eeaa9d5027f31f83ae70c746beac5694614f4de5a3150768069c3d06498846
---

```c
typedef struct OH_TrafficFilter_IPAddress {...} OH_TrafficFilter_IPAddress
```

## 概述

二进制形式的IP地址，支持IPv4和IPv6。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_IPFamily](capi-net-trafficfilter-type-h.md#oh_trafficfilter_ipfamily) family | 地址族。若指定为OH\_TRAFFICFILTER\_IP\_FAMILY\_UNSPEC，默认使用IPv4。  **起始版本：** 26.0.0 |
| uint8\_t addr[OH\_TRAFFICFILTER\_IP\_ADDRLEN] | IP地址字节。字节必须以网络字节序存储。对于IPv4，[addr](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)[0]到[addr](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)[3]存储IPv4地址，[addr](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)[4]到[addr](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)[15]必须设置为0。对于IPv6，[addr](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)[0]到[addr](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)[15]存储IPv6地址。如果字节与[family](capi-trafficfilter-oh-trafficfilter-ipaddress.md#成员变量)要求的地址布局不匹配，使用该结构的接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。  **起始版本：** 26.0.0 |
