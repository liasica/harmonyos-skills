---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-macmatch
title: OH_TrafficFilter_MACMatch
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_MACMatch
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:96bd5bf41a8204bd9816b3d465004a26943a30583395c307003c5d76eaa6c68c
---

```c
typedef struct OH_TrafficFilter_MACMatch {...} OH_TrafficFilter_MACMatch
```

## 概述

MAC地址匹配条件。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool enable | 是否启用MAC地址匹配，true表示启用MAC地址匹配，false表示不启用MAC地址匹配。 |
| bool invert | 是否反转匹配结果。true表示反转匹配结果，false表示不反转匹配结果。 |
| char srcMac[OH\_TRAFFICFILTER\_MAC\_ADDRSTRLEN] | 源MAC地址（XX:XX:XX:XX:XX:XX格式）。 |
