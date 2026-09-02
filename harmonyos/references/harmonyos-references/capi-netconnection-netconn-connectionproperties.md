---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-connectionproperties
title: NetConn_ConnectionProperties
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_ConnectionProperties
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:634f085c3befca1943d7b48565fcfed76c86c4b59e18ced6531f2f650596dbab
---

```c
typedef struct NetConn_ConnectionProperties {...} NetConn_ConnectionProperties
```

## 概述

网络连接信息。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char ifaceName[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络接口的名称。 |
| char domain[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络连接的域名信息。 |
| char tcpBufferSizes[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | TCP缓冲区大小。 |
| uint16\_t mtu | MTU。 |
| [NetConn\_NetAddr](capi-netconnection-netconn-netaddr.md) netAddrList[[NETCONN\_MAX\_ADDR\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 地址列表。 |
| int32\_t netAddrListSize | 地址列表的实际size。 |
| [NetConn\_NetAddr](capi-netconnection-netconn-netaddr.md) dnsList[[NETCONN\_MAX\_ADDR\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | DNS列表。 |
| int32\_t dnsListSize | DNS列表的实际size。 |
| [NetConn\_Route](capi-netconnection-netconn-route.md) routeList[[NETCONN\_MAX\_ROUTE\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 路由列表。 |
| int32\_t routeListSize | 路由列表的实际大小。 |
| [NetConn\_HttpProxy](capi-netconnection-netconn-httpproxy.md) httpProxy | HTTP代理信息。 |
