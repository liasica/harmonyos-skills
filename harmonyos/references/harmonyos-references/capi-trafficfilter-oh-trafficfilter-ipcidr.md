---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipcidr
title: OH_TrafficFilter_IPCidr
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_IPCidr
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:184693a2141705714b1631969feb9baf46ff00d065fec9f4464cbc2265fb7ba9
---

```c
typedef struct OH_TrafficFilter_IPCidr {...} OH_TrafficFilter_IPCidr
```

## 概述

CIDR（Classless Inter-Domain Routing，无类别域间路由）匹配的IP匹配值。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) base | CIDR（无类别域间路由）块的基IP地址。  **起始版本：** 26.0.0 |
| uint8\_t prefixLen | CIDR前缀长度，表示网络掩码中前导1的位数（如24表示子网掩码255.255.255.0）。  **起始版本：** 26.0.0 |
