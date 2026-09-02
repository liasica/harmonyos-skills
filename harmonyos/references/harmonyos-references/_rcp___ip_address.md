---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address
title: Rcp_IpAddress
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_IpAddress
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1cc8e70a2264fdfce75ea743637282b06aeae3e182b0f52627a7d98da17971e9
---

## 概述

指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](_rcp___static_dns_rule_item.md)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char [ipAddress](_rcp___ip_address.md#ipaddress) [[RCP\_IP\_MAX\_LEN](remote-communication-overview.md#rcp_ip_max_len)] | IP地址。 |
| struct [Rcp\_IpAddress](_rcp___ip_address.md) \* [next](_rcp___ip_address.md#next) | 链式存储。指向下一个[Rcp\_IpAddress](_rcp___ip_address.md)。 |

## 结构体成员变量说明

### ipAddress

```cpp
char Rcp_IpAddress::ipAddress[RCP_IP_MAX_LEN]
```

**描述**

ip地址。

### next

```cpp
struct Rcp_IpAddress* Rcp_IpAddress::next
```

**描述**

链式存储。指向下一个[Rcp\_IpAddress](_rcp___ip_address.md)。
