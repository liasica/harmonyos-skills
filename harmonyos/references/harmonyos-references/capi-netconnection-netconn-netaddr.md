---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr
title: NetConn_NetAddr
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetAddr
category: harmonyos-references
scraped_at: 2026-04-28T08:08:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:38c564d961e946919409c239a68c0d88cfa2a7d9024efc77e9701f64a193fa9d
---

```
1. typedef struct NetConn_NetAddr {...} NetConn_NetAddr
```

## 概述

PhonePC/2in1TabletTVWearable

网络地址。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint8\_t family | 网络地址族。 |
| uint8\_t prefixlen | 前缀长度。 |
| uint8\_t port | 端口号。 |
| char address[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 地址。 |
