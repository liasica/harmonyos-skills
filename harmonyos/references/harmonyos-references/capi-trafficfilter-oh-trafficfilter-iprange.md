---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-iprange
title: OH_TrafficFilter_IPRange
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_IPRange
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:cf7fadf42db22a75cbac6b854dc4ff0094130deba3b7c2fc5168b27c8eca93f9
---

```c
typedef struct OH_TrafficFilter_IPRange {...} OH_TrafficFilter_IPRange
```

## 概述

范围匹配的IP匹配值。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) start | 范围的起始IP地址。  **起始版本：** 26.0.0 |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) end | 范围的结束IP地址。  **起始版本：** 26.0.0 |
