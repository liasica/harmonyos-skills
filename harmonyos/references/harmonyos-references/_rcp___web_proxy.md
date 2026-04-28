---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy
title: Rcp_WebProxy
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_WebProxy
category: harmonyos-references
scraped_at: 2026-04-28T08:09:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fd7bc545bc107ee1b66bb89a19b01a06e6470b6a7903ba49d87de1286c30dc60
---

## 概述

PhonePC/2in1TabletTVWearable

自定义代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* [url](_rcp___web_proxy.md#url) | 代理服务器的URL。如果您没有明确设置端口，则端口将为1080。 |
| [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode)[createTunnel](_rcp___web_proxy.md#createtunnel) | 用于控制何时创建代理隧道。 |
| [Rcp\_Exclusions](_rcp___exclusions.md)[exclusions](_rcp___web_proxy.md#exclusions) | 如果[Rcp\_Request.url](_rcp___request.md#url)匹配[Rcp\_Exclusions](_rcp___exclusions.md)规则，则[Rcp\_Request](_rcp___request.md)将不使用代理。 |
| [Rcp\_SecurityConfiguration](_rcp___security_configuration.md)[securityConfiguration](_rcp___web_proxy.md#securityconfiguration) | 代理中的[Rcp\_SecurityConfiguration](_rcp___security_configuration.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### createTunnel

PhonePC/2in1TabletTVWearable

```
1. Rcp_ProxyTunnelMode Rcp_WebProxy::createTunnel
```

**描述**

用于控制何时创建代理隧道。

### exclusions

PhonePC/2in1TabletTVWearable

```
1. Rcp_Exclusions Rcp_WebProxy::exclusions
```

**描述**

如果[Rcp\_Request.url](_rcp___request.md#url)匹配[Rcp\_Exclusions](_rcp___exclusions.md)规则，则[Rcp\_Request](_rcp___request.md)将不使用代理。

### securityConfiguration

PhonePC/2in1TabletTVWearable

```
1. Rcp_SecurityConfiguration Rcp_WebProxy::securityConfiguration
```

**描述**

代理中的[Rcp\_SecurityConfiguration](_rcp___security_configuration.md)。

### url

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_WebProxy::url
```

**描述**

代理服务器的URL。如果您没有明确设置端口，则端口将为1080。
