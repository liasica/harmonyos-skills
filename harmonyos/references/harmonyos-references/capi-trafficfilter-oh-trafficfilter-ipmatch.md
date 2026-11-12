---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipmatch
title: OH_TrafficFilter_IPMatch
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_IPMatch
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:78f8edf040bb0e707b7f3e855e841d3d8f5ea1a4681b662ce9160f736aef4b40
---

```c
typedef struct OH_TrafficFilter_IPMatch {...} OH_TrafficFilter_IPMatch
```

## 概述

IP匹配条件。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_IPMatchType](capi-net-trafficfilter-type-h.md#oh_trafficfilter_ipmatchtype) type | 匹配类型。 |
| bool invert | 是否反转匹配结果。 |
| union value | 匹配规则。 （[OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) single、[OH\_TrafficFilter\_IPCidr](capi-trafficfilter-oh-trafficfilter-ipcidr.md) cidr、[OH\_TrafficFilter\_IPRange](capi-trafficfilter-oh-trafficfilter-iprange.md) range、[OH\_TrafficFilter\_IPMulti](capi-trafficfilter-oh-trafficfilter-ipmulti.md) multi） |
