---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers
title: Rcp_DnsServers
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DnsServers
category: harmonyos-references
scraped_at: 2026-04-28T08:09:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:87353579f9ac2b9228a2d42e5a1d6b328f0462f1848ae3ad1f4c9db16b0beb1a
---

## 概述

PhonePC/2in1TabletTVWearable

DNS服务器。[Rcp\_DnsConfiguration.dnsRules](_rcp___dns_configuration.md#dnsrules)中的类型之一。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_IpAndPort](_rcp___ip_and_port.md)[ipAndPort](_rcp___dns_servers.md#ipandport) | IP和端口。 |
| struct [Rcp\_DnsServers](_rcp___dns_servers.md) \* [next](_rcp___dns_servers.md#next) | 链式存储。指向下一个[Rcp\_DnsServers](_rcp___dns_servers.md)的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### ipAndPort

PhonePC/2in1TabletTVWearable

```
1. Rcp_IpAndPort Rcp_DnsServers::ipAndPort
```

**描述**

IP和端口。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_DnsServers* Rcp_DnsServers::next
```

**描述**

链式存储。指向下一个[Rcp\_DnsServers](_rcp___dns_servers.md)的指针。
