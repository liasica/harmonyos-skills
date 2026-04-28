---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item
title: Rcp_StaticDnsRuleItem
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_StaticDnsRuleItem
category: harmonyos-references
scraped_at: 2026-04-28T08:09:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:17f1687a2934197023c758d950091c82360f0b5347f51b50077f32a22abdb649
---

## 概述

PhonePC/2in1TabletTVWearable

描述单个静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| char [host](_rcp___static_dns_rule_item.md#host) [[RCP\_HOST\_MAX\_LEN](remote-communication-overview.md#rcp_host_max_len)] | 主机名。 |
| uint16\_t [port](_rcp___static_dns_rule_item.md#port) | 端口号。范围： [0, 65535]。 |
| [Rcp\_IpAddress](_rcp___ip_address.md) \* [ipAddresses](_rcp___static_dns_rule_item.md#ipaddresses) | 表示[Rcp\_StaticDnsRuleItem.host](_rcp___static_dns_rule_item.md#host)对应的IP地址。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### host

PhonePC/2in1TabletTVWearable

```
1. char Rcp_StaticDnsRuleItem::host[RCP_HOST_MAX_LEN]
```

**描述**

主机名。

### ipAddresses

PhonePC/2in1TabletTVWearable

```
1. Rcp_IpAddress* Rcp_StaticDnsRuleItem::ipAddresses
```

**描述**

表示[Rcp\_StaticDnsRuleItem.host](_rcp___static_dns_rule_item.md#host)对应的IP地址。

### port

PhonePC/2in1TabletTVWearable

```
1. uint16_t Rcp_StaticDnsRuleItem::port
```

**描述**

端口号。范围： [0, 65535]。
