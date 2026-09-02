---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netspecifier
title: NetConn_NetSpecifier
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_NetSpecifier
category: harmonyos-references
scraped_at: 2026-09-02T15:01:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c5f3283a9ecc6122483311ab5a355a8fd7011c9e953dbe72ebce26f5ebd4ebde
---

```c
typedef struct NetConn_NetSpecifier {...} NetConn_NetSpecifier
```

## 概述

网络的特征集。

**起始版本：** 12

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [NetConn\_NetCapabilities](capi-netconnection-netconn-netcapabilities.md) caps | 网络能力集。 |
| char \*bearerPrivateIdentifier | 网络标识符。 |
