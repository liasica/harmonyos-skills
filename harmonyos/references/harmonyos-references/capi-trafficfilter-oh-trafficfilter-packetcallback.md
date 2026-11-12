---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-packetcallback
title: OH_TrafficFilter_PacketCallback
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PacketCallback
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0aacdffe4e0b16bfaeece96ad55de2fd7dc2cd7669cbc350e2b2817b9cfb4b7b
---

```c
typedef OH_TrafficFilter_PacketDecision (*OH_TrafficFilter_PacketCallback)(
    const OH_TrafficFilter_PacketDesc* packet,
    void* userData
)
```

## 概述

报文回调函数类型。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 参数

| 名称 | 描述 |
| --- | --- |
| [const OH\_TrafficFilter\_PacketDesc](capi-trafficfilter-oh-trafficfilter-packetdesc.md)\* packet | 报文描述符。 |
| void\* userData | 用户数据。 |

### 返回

| 类型 | 说明 |
| --- | --- |
| [OH\_TrafficFilter\_PacketDecision](capi-trafficfilter-oh-trafficfilter-packetdecision.md) | 报文处理决策（接受或丢弃）。 |
