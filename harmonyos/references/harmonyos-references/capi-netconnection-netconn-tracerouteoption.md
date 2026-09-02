---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteoption
title: NetConn_TraceRouteOption
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_TraceRouteOption
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fb734657f1952c280c59a1ef5ed4aa14fea29d2ee5b7fa8ab7e4b00d3f984687
---

```c
typedef struct NetConn_TraceRouteOption {...} NetConn_TraceRouteOption
```

## 概述

定义网络跟踪路由选项。

**起始版本：** 20

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t maxJumpNumber | 探测结果最大跳数，需要和TraceRouteInfo设置一致，最大可设置30跳，默认为30跳。 |
| NetConn\_PacketsType packetsType | 探测包协议类型，默认为NETCONN\_PACKETS\_ICMP。 |
