---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-connectioninfo
title: OH_TrafficFilter_ConnectionInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_ConnectionInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f7fa5f1e2c5ad65c93a88fd1d152a36624a8c18aae770e1b76b6646166a7c24e
---

```c
typedef struct OH_TrafficFilter_ConnectionInfo {...} OH_TrafficFilter_ConnectionInfo
```

## 概述

连接信息结构体。描述一条网络连接的五元组信息（源IP、目的IP、源端口、目的端口、协议类型），用于查询发起该连接的进程信息。

初始化规则：调用[OH\_TrafficFilter\_QueryProcess](capi-net-trafficfilter-h.md#oh_trafficfilter_queryprocess)之前，调用者必须将该结构体清零（例如使用memset），然后将[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)设置为调用者分配的结构体实际大小，通常为sizeof(OH\_TrafficFilter\_ConnectionInfo)。

二进制兼容规则（ABI，即应用程序二进制接口，保证新旧版本编译的代码能互相识别结构体布局）：系统通过[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)来确定哪些字段可以被安全读取。如果[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)小于当前接口所需的最小大小，接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[size](capi-trafficfilter-oh-trafficfilter-connectioninfo.md#成员变量)大于系统已知的大小，多余的字段将被忽略。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t size | 调用者分配的结构体实际大小。  **起始版本：** 26.0.0 |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) srcIp | 源IP地址，支持IPv4和IPv6。  **起始版本：** 26.0.0 |
| uint16\_t srcPort | 源端口。0表示任意源端口。  **起始版本：** 26.0.0 |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) dstIp | 目的IP地址，支持IPv4和IPv6，需要与源IP地址的地址族相同。  **起始版本：** 26.0.0 |
| uint16\_t dstPort | 目的端口。0表示任意目的端口。  **起始版本：** 26.0.0 |
| uint8\_t protocol | 协议类型。支持的取值：- OH\_TRAFFICFILTER\_PROTO\_TCP (6)- OH\_TRAFFICFILTER\_PROTO\_UDP (17)  **起始版本：** 26.0.0 |
