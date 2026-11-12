---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-tcpflagsmatch
title: OH_TrafficFilter_TCPFlagsMatch
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_TCPFlagsMatch
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:0ec39044e17307a151312c06b170d4c5faa4a06f8ecc30e2bdeeed166035039a
---

```c
typedef struct OH_TrafficFilter_TCPFlagsMatch {...} OH_TrafficFilter_TCPFlagsMatch
```

## 概述

TCP标志位匹配条件。仅对TCP协议有效。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool enable | 是否启用TCP标志位匹配，true表示启用TCP标志位匹配，false表示不启用TCP标志位匹配。 |
| uint8\_t flagMask | 标志位掩码（指定检查的标志位）。 |
| uint8\_t flagComp | 标志位比较值（标志位比对值）。 |
