---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration
title: Rcp_ProxyConfiguration
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_ProxyConfiguration
category: harmonyos-references
scraped_at: 2026-04-28T08:09:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1640715d76eee49f8f5e4637f3572cce7568de00f4103a1541df7d8bc05f9afa
---

## 概述

PhonePC/2in1TabletTVWearable

代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [Rcp\_ProxyType](remote-communication-overview.md#rcp_proxytype)[proxyType](_rcp___proxy_configuration.md#proxytype) | 区分请求使用的代理类型。 |
| [Rcp\_WebProxy](_rcp___web_proxy.md)[customProxy](_rcp___proxy_configuration.md#customproxy) | 自定义代理配置，参见[Rcp\_WebProxy](_rcp___web_proxy.md)。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### customProxy

PhonePC/2in1TabletTVWearable

```
1. Rcp_WebProxy Rcp_ProxyConfiguration::customProxy
```

**描述**

自定义代理配置，参见[Rcp\_WebProxy](_rcp___web_proxy.md)。

### proxyType

PhonePC/2in1TabletTVWearable

```
1. Rcp_ProxyType Rcp_ProxyConfiguration::proxyType
```

**描述**

区分请求使用的代理类型。
