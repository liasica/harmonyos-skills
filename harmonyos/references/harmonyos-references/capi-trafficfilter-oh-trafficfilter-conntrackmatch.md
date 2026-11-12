---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-conntrackmatch
title: OH_TrafficFilter_ConntrackMatch
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_ConntrackMatch
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:fdb6f3d23d4189305d8530c276ceb366a472dc6c765b8f60e0529906b2db3831
---

```c
typedef struct OH_TrafficFilter_ConntrackMatch {...} OH_TrafficFilter_ConntrackMatch
```

## 概述

连接跟踪（Connection Tracking）匹配条件。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool enable | 是否启用连接跟踪匹配，true表示启用连接跟踪匹配，false表示不启用连接跟踪匹配。 |
| uint8\_t stateMask | 连接状态。 |
