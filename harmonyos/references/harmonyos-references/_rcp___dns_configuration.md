---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration
title: Rcp_DnsConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_DnsConfiguration
category: harmonyos-references
scraped_at: 2026-09-02T15:01:58+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:291f39771eb00617f9842e4d4804b5c8c6e17911a5018b6e7faf8cc380667e8d
---

## 概述

DNS解析配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_DnsRule](_rcp___dns_rule.md) \* [dnsRules](_rcp___dns_configuration.md#dnsrules) | DNS规则配置。 |
| [Rcp\_DnsOverHttps](_rcp___dns_over_https.md) [dnsOverHttps](_rcp___dns_configuration.md#dnsoverhttps) | DOH配置。 |

## 结构体成员变量说明

### dnsOverHttps

```cpp
Rcp_DnsOverHttps Rcp_DnsConfiguration::dnsOverHttps
```

**描述**

DOH配置。

### dnsRules

```cpp
Rcp_DnsRule* Rcp_DnsConfiguration::dnsRules
```

**描述**

DNS规则配置。

[Rcp\_DnsServers](_rcp___dns_servers.md): 表示优先使用指定的DNS服务器解析主机名。

[Rcp\_StaticDnsRule](_rcp___static_dns_rule.md): 表示如果主机名匹配，则优先使用指定的地址。

[Rcp\_DynamicDnsRuleFunction](remote-communication-overview.md#rcp_dynamicdnsrulefunction): 表示优先使用函数中返回的地址。
