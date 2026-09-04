---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-portmatch
title: OH_TrafficFilter_PortMatch
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PortMatch
category: harmonyos-references
scraped_at: 2026-09-05T06:19:03+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:1db226a3b128dea5a009c220fbd163a85743f2e0dc36e3c87f4744530ef7c480
---

```c
typedef struct OH_TrafficFilter_PortMatch {...} OH_TrafficFilter_PortMatch
```

## 概述

端口匹配条件。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_PortMatchType](capi-net-trafficfilter-type-h.md#oh_trafficfilter_portmatchtype) type | 匹配类型。  **起始版本：** 26.0.0 |
| bool invert | 是否反转匹配结果。true表示反转匹配结果，false表示不反转匹配结果。  **起始版本：** 26.0.0 |
| union | 匹配规则。  **起始版本：** 26.0.0 |
