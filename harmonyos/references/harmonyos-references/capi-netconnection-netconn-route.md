---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-route
title: NetConn_Route
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_Route
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:f1123a977604d2cf79e8f0cd5e7b6aa8bd80f1c4eea7fc0db8310797fb0cf256
---

```c
typedef struct NetConn_Route {...} NetConn_Route
```

## 概述

路由配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char iface[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络接口 |
| [NetConn\_NetAddr](capi-netconnection-netconn-netaddr.md) destination | 目标地址 |
| [NetConn\_NetAddr](capi-netconnection-netconn-netaddr.md) gateway | 网关地址 |
| int32\_t hasGateway | 是否存在网关 |
| int32\_t isDefaultRoute | 是否是默认路由 |
