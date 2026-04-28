---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration
title: Rcp_Configuration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_Configuration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edf6fa86394720e6a29675c987bdee4c00cd024659aa0056a11cfdf31525956f
---

## 概述

PhonePC/2in1TabletTVWearable

请求配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_TransferConfiguration](_rcp___transfer_configuration.md)[transferConfiguration](_rcp___configuration.md#transferconfiguration) | 传输配置。 |
| [Rcp\_TracingConfiguration](_rcp___tracing_configuration.md)[tracingConfiguration](_rcp___configuration.md#tracingconfiguration) | 请求追踪配置。 |
| [Rcp\_ProxyConfiguration](_rcp___proxy_configuration.md)[proxyConfiguration](_rcp___configuration.md#proxyconfiguration) | 代理配置。 |
| [Rcp\_DnsConfiguration](_rcp___dns_configuration.md)[dnsConfiguration](_rcp___configuration.md#dnsconfiguration) | DNS配置。 |
| [Rcp\_SecurityConfiguration](_rcp___security_configuration.md)[securityConfiguration](_rcp___configuration.md#securityconfiguration) | 安全配置。 |
| void \* [configurationPrivate](_rcp___configuration.md#configurationprivate) | 可扩展字段。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### configurationPrivate

PhonePC/2in1TabletTVWearable

```
1. void* Rcp_Configuration::configurationPrivate
```

**描述**

可扩展字段。

### dnsConfiguration

PhonePC/2in1TabletTVWearable

```
1. Rcp_DnsConfiguration Rcp_Configuration::dnsConfiguration
```

**描述**

DNS配置。

### proxyConfiguration

PhonePC/2in1TabletTVWearable

```
1. Rcp_ProxyConfiguration Rcp_Configuration::proxyConfiguration
```

**描述**

代理配置。

### securityConfiguration

PhonePC/2in1TabletTVWearable

```
1. Rcp_SecurityConfiguration Rcp_Configuration::securityConfiguration
```

**描述**

安全配置。

### tracingConfiguration

PhonePC/2in1TabletTVWearable

```
1. Rcp_TracingConfiguration Rcp_Configuration::tracingConfiguration
```

**描述**

请求追踪配置。

### transferConfiguration

PhonePC/2in1TabletTVWearable

```
1. Rcp_TransferConfiguration Rcp_Configuration::transferConfiguration
```

**描述**

传输配置。
