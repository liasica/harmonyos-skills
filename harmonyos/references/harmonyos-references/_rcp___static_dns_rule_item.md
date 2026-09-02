---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item
title: Rcp_StaticDnsRuleItem
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_StaticDnsRuleItem
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:eef05f65077394b74643eafe9b14188d98b868d9691bbba7b9975f960222e950
---

## 概述

描述单个静态DNS规则。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| char [host](_rcp___static_dns_rule_item.md#host) [[RCP\_HOST\_MAX\_LEN](remote-communication-overview.md#rcp_host_max_len)] | 主机名。 |
| uint16\_t [port](_rcp___static_dns_rule_item.md#port) | 端口号。范围： [0, 65535]。 |
| [Rcp\_IpAddress](_rcp___ip_address.md) \* [ipAddresses](_rcp___static_dns_rule_item.md#ipaddresses) | 表示[Rcp\_StaticDnsRuleItem.host](_rcp___static_dns_rule_item.md#host)对应的IP地址。 |

## 结构体成员变量说明

### host

```cpp
char Rcp_StaticDnsRuleItem::host[RCP_HOST_MAX_LEN]
```

**描述**

主机名。

### ipAddresses

```cpp
Rcp_IpAddress* Rcp_StaticDnsRuleItem::ipAddresses
```

**描述**

表示[Rcp\_StaticDnsRuleItem.host](_rcp___static_dns_rule_item.md#host)对应的IP地址。

### port

```cpp
uint16_t Rcp_StaticDnsRuleItem::port
```

**描述**

端口号。范围： [0, 65535]。
