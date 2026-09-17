---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-ipmulti
title: OH_TrafficFilter_IPMulti
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_IPMulti
category: harmonyos-references
scraped_at: 2026-09-18T06:49:58+08:00
doc_updated_at: 2026-09-17
content_hash: sha256:21a0ae6a52248dff38faef60a0e74e3ccacda68c8d4cdf230f03cb1373d2ede9
---

```c
typedef struct OH_TrafficFilter_IPMulti {...} OH_TrafficFilter_IPMulti
```

## 概述

多IP匹配的IP匹配值。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t ipCount | 数组中的IP地址数量。 |
| [OH\_TrafficFilter\_IPAddress](capi-trafficfilter-oh-trafficfilter-ipaddress.md) ips[OH\_TRAFFICFILTER\_MAX\_MULTI\_IP\_COUNT] | IP地址数组。 |
