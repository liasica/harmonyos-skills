---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers
title: Rcp_DnsServers
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DnsServers
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:5e7002d0d1e16c4c23c7e337d107056d9fd347c97d4b8a21e4c59b10678d8495
---

## 概述

DNS服务器。[Rcp\_DnsConfiguration.dnsRules](_rcp___dns_configuration.md#dnsrules)中的类型之一。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_IpAndPort](_rcp___ip_and_port.md) [ipAndPort](_rcp___dns_servers.md#ipandport) | IP和端口。 |
| struct [Rcp\_DnsServers](_rcp___dns_servers.md) \* [next](_rcp___dns_servers.md#next) | 链式存储。指向下一个[Rcp\_DnsServers](_rcp___dns_servers.md)的指针。 |

## 结构体成员变量说明

### ipAndPort

```cpp
Rcp_IpAndPort Rcp_DnsServers::ipAndPort
```

**描述**

IP和端口。

### next

```cpp
struct Rcp_DnsServers* Rcp_DnsServers::next
```

**描述**

链式存储。指向下一个[Rcp\_DnsServers](_rcp___dns_servers.md)的指针。
