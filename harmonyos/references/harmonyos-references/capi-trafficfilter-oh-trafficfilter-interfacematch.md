---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-interfacematch
title: OH_TrafficFilter_InterfaceMatch
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_InterfaceMatch
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fc2fa271f90387fb5a7571a6018bd8d0b0fec458d5418e2d17a4840e98a589e2
---

```c
typedef struct OH_TrafficFilter_InterfaceMatch {...} OH_TrafficFilter_InterfaceMatch
```

## 概述

接口匹配条件。

**起始版本：** 26.0.0

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool enabled | 是否启用接口匹配，true表示启用接口匹配，false表示不启用接口匹配。  **起始版本：** 26.0.0 |
| bool invert | 是否反转匹配结果，true表示反转匹配结果，false表示不反转匹配结果。  **起始版本：** 26.0.0 |
| bool isPrefix | 接口名称是否按前缀匹配，true表示按前缀匹配，false表示不按前缀匹配。  **起始版本：** 26.0.0 |
| char ifName[OH\_TRAFFICFILTER\_IFNAMSIZ] | 接口名称。字符串必须使用UTF-8编码且以NULL结尾。该缓冲区容量为[OH\_TRAFFICFILTER\_IFNAMSIZ](capi-net-trafficfilter-type-h.md#宏定义)字节，包含结尾的NULL字符。因此接口名称最大长度为[OH\_TRAFFICFILTER\_IFNAMSIZ](capi-net-trafficfilter-type-h.md#宏定义) - 1字节，不包含结尾的NULL字符。如果[enabled](capi-trafficfilter-oh-trafficfilter-interfacematch.md#成员变量)为true，该字符串不能为空。如果该字符串在[OH\_TRAFFICFILTER\_IFNAMSIZ](capi-net-trafficfilter-type-h.md#宏定义)字节内未以NULL结尾，或其长度超过[OH\_TRAFFICFILTER\_IFNAMSIZ](capi-net-trafficfilter-type-h.md#宏定义) - 1字节，使用该结构的接口将返回[OH\_TRAFFICFILTER\_ERROR\_INVALID\_PARAM](capi-net-trafficfilter-type-h.md#oh_trafficfilter_errcode)。如果[enabled](capi-trafficfilter-oh-trafficfilter-interfacematch.md#成员变量)为false，该字段将被忽略。建议在禁用接口匹配时将该缓冲区全部置零。  **起始版本：** 26.0.0 |
