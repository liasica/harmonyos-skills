---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy
title: Rcp_WebProxy
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_WebProxy
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:fc1b8bf80249e2636648620fcfc2438e68ed5e29f658d8523d04537d120b9d7c
---

## 概述

自定义代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char \* [url](_rcp___web_proxy.md#url) | 代理服务器的URL。如果您没有明确设置端口，则端口将为1080。 |
| [Rcp\_ProxyTunnelMode](remote-communication-overview.md#rcp_proxytunnelmode) [createTunnel](_rcp___web_proxy.md#createtunnel) | 用于控制何时创建代理隧道。 |
| [Rcp\_Exclusions](_rcp___exclusions.md) [exclusions](_rcp___web_proxy.md#exclusions) | 如果[Rcp\_Request.url](_rcp___request.md#url)匹配[Rcp\_Exclusions](_rcp___exclusions.md)规则，则[Rcp\_Request](_rcp___request.md)将不使用代理。 |
| [Rcp\_SecurityConfiguration](_rcp___security_configuration.md) [securityConfiguration](_rcp___web_proxy.md#securityconfiguration) | 代理中的[Rcp\_SecurityConfiguration](_rcp___security_configuration.md)。 |

## 结构体成员变量说明

### createTunnel

```cpp
Rcp_ProxyTunnelMode Rcp_WebProxy::createTunnel
```

**描述**

用于控制何时创建代理隧道。

### exclusions

```cpp
Rcp_Exclusions Rcp_WebProxy::exclusions
```

**描述**

如果[Rcp\_Request.url](_rcp___request.md#url)匹配[Rcp\_Exclusions](_rcp___exclusions.md)规则，则[Rcp\_Request](_rcp___request.md)将不使用代理。

### securityConfiguration

```cpp
Rcp_SecurityConfiguration Rcp_WebProxy::securityConfiguration
```

**描述**

代理中的[Rcp\_SecurityConfiguration](_rcp___security_configuration.md)。

### url

```cpp
const char* Rcp_WebProxy::url
```

**描述**

代理服务器的URL。如果您没有明确设置端口，则端口将为1080。
