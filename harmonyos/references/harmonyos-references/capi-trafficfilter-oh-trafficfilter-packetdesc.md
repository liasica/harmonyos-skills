---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-packetdesc
title: OH_TrafficFilter_PacketDesc
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PacketDesc
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2ee14b999803868c0d9f9a177c438cd890b0c05f0eceeaec3fa5a86b46a1474e
---

```c
typedef struct OH_TrafficFilter_PacketDesc {...} OH_TrafficFilter_PacketDesc
```

## 概述

报文描述符。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t packetId | 报文ID（报文到达netfilter（Network Filter，网络过滤器）时由内核分配）。 |
| uint8\_t protocol | 协议类型。 |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) srcIp | 源IP地址（支持IPv4和IPv6）。 |
| uint16\_t srcPort | 源端口。 |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) dstIp | 目的IP地址（支持IPv4和IPv6）。 |
| uint16\_t dstPort | 目的端口。 |
| uint32\_t packetLen | 报文长度。 |
| uint8\_t\* data | 报文数据指针（用户可修改，内存由系统管理，**仅在回调期间有效，回调返回后不可再访问该指针**）。 |
| void\* userData | 用户数据（在回调中使用）。 |
