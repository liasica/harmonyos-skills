---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_and_port
title: Rcp_IpAndPort
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_IpAndPort
category: harmonyos-references
scraped_at: 2026-04-28T08:09:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4b3857cfa06fb1ddd8e27e92cf561d6bf5d6948594df3d2c21b556cfa8e05e56
---

## 概述

PhonePC/2in1TabletTVWearable

该接口用在[Rcp\_DnsServers](_rcp___dns_servers.md)中，表示一个DNS服务器的地址和端口。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char [ip](_rcp___ip_and_port.md#ip) [[RCP\_IP\_MAX\_LEN](remote-communication-overview.md#rcp_ip_max_len)] | IPv4或IPv6地址。 |
| uint16\_t [port](_rcp___ip_and_port.md#port) | 表示端口。取值范围：[0, 65535]。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### ip

PhonePC/2in1TabletTVWearable

```
1. char Rcp_IpAndPort::ip[RCP_IP_MAX_LEN]
```

**描述**

IPv4或IPv6地址。

### port

PhonePC/2in1TabletTVWearable

```
1. uint16_t Rcp_IpAndPort::port
```

**描述**

表示端口。取值范围：[0, 65535]。
