---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-portmulti
title: OH_TrafficFilter_PortMulti
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PortMulti
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8b2fcf2d9c4cad4744d75bd9550ef9a952e4fab140ffd9e035aed8f76b6589ad
---

```c
typedef struct OH_TrafficFilter_PortMulti {...} OH_TrafficFilter_PortMulti
```

## 概述

多端口匹配的端口匹配值。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t portCount | 数组中的端口数量。  **起始版本：** 26.0.0 |
| uint16\_t ports[OH\_TRAFFICFILTER\_MAX\_MULTI\_PORT\_COUNT] | 端口数组。  **起始版本：** 26.0.0 |
