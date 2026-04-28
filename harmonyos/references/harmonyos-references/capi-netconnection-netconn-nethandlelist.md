---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist
title: NetConn_NetHandleList
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetHandleList
category: harmonyos-references
scraped_at: 2026-04-28T08:08:36+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:2fd1034f398f666971167873eaf9a2e2dda38128a19c3f9b15620b944172cba8
---

```
1. typedef struct NetConn_NetHandleList {...} NetConn_NetHandleList
```

## 概述

PhonePC/2in1TabletTVWearable

网络列表。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) netHandles[[NETCONN\_MAX\_NET\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | netHandle列表。 |
| int32\_t netHandleListSize | netHandleList的实际大小。 |
