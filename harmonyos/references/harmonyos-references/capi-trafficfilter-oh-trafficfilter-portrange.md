---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-portrange
title: OH_TrafficFilter_PortRange
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PortRange
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:95b6e392183c85f7f69609ed95f3a016037434003c924412e7aef5bf4a2ae02e
---

```c
typedef struct OH_TrafficFilter_PortRange {...} OH_TrafficFilter_PortRange
```

## 概述

范围匹配的端口匹配值。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint16\_t startPort | 范围的起始端口。  **起始版本：** 26.0.0 |
| uint16\_t endPort | 范围的结束端口。  **起始版本：** 26.0.0 |
