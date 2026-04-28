---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-tracerouteoption
title: NetConn_TraceRouteOption
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_TraceRouteOption
category: harmonyos-references
scraped_at: 2026-04-28T08:08:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6dd3932b351b7a406abe9e44872713e7e4df7e0a81158992ab45ba97e45415a1
---

```
1. typedef struct NetConn_TraceRouteOption {...} NetConn_TraceRouteOption
```

## 概述

PhonePC/2in1TabletTVWearable

定义网络跟踪路由选项。

**起始版本：** 20

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t maxJumpNumber | 探测结果最大跳数，需要和TraceRouteInfo设置一致，最大可设置30跳，默认为30跳。 |
| NetConn\_PacketsType packetsType | 探测包协议类型，默认为NETCONN\_PACKETS\_ICMP。 |
