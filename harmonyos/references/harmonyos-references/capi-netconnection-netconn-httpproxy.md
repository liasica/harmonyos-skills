---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-httpproxy
title: NetConn_HttpProxy
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 结构体 > NetConn_HttpProxy
category: harmonyos-references
scraped_at: 2026-04-28T08:08:35+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:728f7dabb0cd47bbdd15f2d5f9516a5b62a2a1b7c3a96cbeab859bb13cbdbe53
---

```
1. typedef struct NetConn_HttpProxy {...} NetConn_HttpProxy
```

## 概述

PhonePC/2in1TabletTVWearable

代理配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](capi-netconnection.md)

**所在头文件：** [net\_connection\_type.h](capi-net-connection-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char host[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 主机名。 |
| char exclusionList[[NETCONN\_MAX\_EXCLUSION\_SIZE]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义)[[NETCONN\_MAX\_STR\_LEN]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 代理服务器的排除列表。 |
| int32\_t exclusionListSize | 排除列表的实际大小。 |
| uint16\_t port | 端口号。 |
