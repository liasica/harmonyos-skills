---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter-oh-trafficfilter-packetcopymode
title: OH_TrafficFilter_PacketCopyMode
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > OH_TrafficFilter_PacketCopyMode
category: harmonyos-references
scraped_at: 2026-11-12T09:55:43+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8eba73bb1c1f7069ea8eee1ef80f7de954fde9620842af11ccb3ee007de6a72e
---

```c
typedef enum OH_TrafficFilter_PacketCopyMode {...} OH_TrafficFilter_PacketCopyMode
```

## 概述

报文复制模式枚举。

**起始版本：** 26.0.1

**相关模块：** [TrafficFilter](capi-trafficfilter.md)

**所在头文件：** [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md)

## 汇总

### 枚举项

| 名称 | 说明 |
| --- | --- |
| OH\_TRAFFICFILTER\_COPY\_MODE\_META = 0 | 仅复制元数据（不复制报文数据）。 |
| OH\_TRAFFICFILTER\_COPY\_MODE\_HEADER = 1 | 仅复制报文头部（由packetCopyLen指定）。 |
| OH\_TRAFFICFILTER\_COPY\_MODE\_FULL = 2 | 复制整个报文。 |
| OH\_TRAFFICFILTER\_COPY\_MODE\_MAXLEN = 3 | 复制指定最大长度的报文。 |
