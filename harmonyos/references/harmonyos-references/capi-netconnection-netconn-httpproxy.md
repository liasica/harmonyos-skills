---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-httpproxy
title: NetConn_HttpProxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_HttpProxy
category: harmonyos-references
scraped_at: 2026-09-02T15:01:55+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:04ed5a47fa827538022ed770b60e69c3574937ddb47f1109bdbc02d94758b120
---

```c
typedef struct NetConn_HttpProxy {...} NetConn_HttpProxy
```

## 概述

代理配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char host[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 主机名。 |
| char exclusionList[[NETCONN\_MAX\_EXCLUSION\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义)[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 代理服务器的排除列表。 |
| int32\_t exclusionListSize | 排除列表的实际大小。 |
| uint16\_t port | 端口号。 |
