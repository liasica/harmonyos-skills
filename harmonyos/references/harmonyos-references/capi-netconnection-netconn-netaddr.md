---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr
title: NetConn_NetAddr
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetAddr
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d8f21bac180e93efd928619ea165637522c1dd66e21cc76c48376b91faef0955
---

```c
typedef struct NetConn_NetAddr {...} NetConn_NetAddr
```

## 概述

网络地址。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t family | 网络地址族。 |
| uint8\_t prefixlen | 前缀长度。 |
| uint8\_t port | 端口号。 |
| char address[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 地址。 |
