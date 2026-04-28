---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteinfo
title: NetConn_TraceRouteInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_TraceRouteInfo
category: harmonyos-references
scraped_at: 2026-04-28T08:08:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:da1d835acecfb050dbe6b1d148d02377d3d9fbd8037982b8bd779064798ec0af
---

```
1. typedef struct NetConn_TraceRouteInfo {...} NetConn_TraceRouteInfo
```

## 概述

PhonePC/2in1TabletTVWearable

定义跟踪路由信息。

**起始版本：** 20

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t jumpNo | 跳数。 |
| char address[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 主机名或地址。 |
| uint32\_t rtt[[NETCONN\_MAX\_RTT\_NUM]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 往返时间（单位：毫秒)，包含最大、最小、平均、标准差。 |
