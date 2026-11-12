---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-packetdecision
title: OH_TrafficFilter_PacketDecision
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PacketDecision
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:350db3bec34872253f93d06478ba65135a4c1be2698fd507c1a5b7cb097bc6ab
---

```c
typedef enum OH_TrafficFilter_PacketDecision {...} OH_TrafficFilter_PacketDecision
```

## 概述

报文处理决策类型。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 枚举项

| 名称 | 说明 |
| --- | --- |
| OH\_TRAFFICFILTER\_DECISION\_ACCEPT = 0 | 接受报文。 |
| OH\_TRAFFICFILTER\_DECISION\_DROP | 丢弃报文。 |
