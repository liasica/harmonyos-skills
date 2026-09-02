---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteinfo
title: NetConn_TraceRouteInfo
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_TraceRouteInfo
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9ebf4c91debf3bf3de5373880b8c4080f9bd67dabeccd3c4ce05c8715cea1483
---

```c
typedef struct NetConn_TraceRouteInfo {...} NetConn_TraceRouteInfo
```

## 概述

定义跟踪路由信息。

**起始版本：** 20

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t jumpNo | 跳数。 |
| char address[[NETCONN\_MAX\_STR\_LEN](capi-net-connection-type-h.md#宏定义)] | 主机名或地址。 |
| uint32\_t rtt[[NETCONN\_MAX\_RTT\_NUM](capi-net-connection-type-h.md#宏定义)] | 往返时间（单位：毫秒），包含最大、最小、平均、标准差。 |
