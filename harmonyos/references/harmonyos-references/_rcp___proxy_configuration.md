---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration
title: Rcp_ProxyConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ProxyConfiguration
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:23607b0e0407548b75c245766b8896088e31bf13f2ded640d7a0646314b34ef5
---

## 概述

代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype) [proxyType](_rcp___proxy_configuration.md#proxytype) | 区分请求使用的代理类型。 |
| [Rcp\_WebProxy](_rcp___web_proxy.md) [customProxy](_rcp___proxy_configuration.md#customproxy) | 自定义代理配置，参见[Rcp\_WebProxy](_rcp___web_proxy.md)。 |

## 结构体成员变量说明

### customProxy

```cpp
Rcp_WebProxy Rcp_ProxyConfiguration::customProxy
```

**描述**

自定义代理配置，参见[Rcp\_WebProxy](_rcp___web_proxy.md)。

### proxyType

```cpp
Rcp_ProxyType Rcp_ProxyConfiguration::proxyType
```

**描述**

区分请求使用的代理类型。
