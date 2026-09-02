---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist
title: NetConn_NetHandleList
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetHandleList
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d9d523b2e0e66b0a54f8fca5fa5759019554e5d7851d28fbde2dc7f220243b4d
---

```c
typedef struct NetConn_NetHandleList {...} NetConn_NetHandleList
```

## 概述

网络列表。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetConn\_NetHandle](capi-netconnection-netconn-nethandle.md) netHandles[[NETCONN\_MAX\_NET\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | netHandle列表。 |
| int32\_t netHandleListSize | netHandleList的实际大小。 |
