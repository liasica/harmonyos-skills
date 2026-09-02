---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-trafficfilter
title: TrafficFilter
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 模块 > TrafficFilter
category: harmonyos-references
scraped_at: 2026-09-02T14:52:21+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3e4b5f4c4fba69219c9ff789b96f5be57afdc03324f49464c6ba1c508520e08d
---

## 概述

实现网络流量过滤与重定向功能。流量过滤是指在系统内核网络协议栈中拦截网络数据包（报文），根据预设规则决定报文的放行或丢弃，适用于防火墙、家长控制、应用流量管控等场景。

流量重定向是指将匹配规则的TCP流量转发到指定的代理服务器，适用于企业网络审计、内容过滤代理、VPN透明代理等场景。

使用时，先创建控制器或重定向器实例，再添加过滤或重定向规则，即可对网络流量进行管控。使用完毕后需调用对应的销毁接口释放资源。

**起始版本：** 26.0.0

## 文件汇总

| 名称 | 描述 |
| --- | --- |
| [net\_trafficfilter.h](capi-net-trafficfilter-h.md) | 声明网络流量过滤与重定向功能的C接口。该头文件提供创建和销毁报文控制器、注册报文回调、添加和清除过滤规则，以及创建和销毁流量重定向器、添加和清除重定向规则的接口。  适用于需要在系统层面对网络数据包进行拦截、过滤和重定向的应用场景。 |
| [net\_trafficfilter\_type.h](capi-net-trafficfilter-type-h.md) | 声明网络流量过滤与重定向功能所需的通用类型和错误码。该头文件定义了流量过滤与重定向功能中使用的IP地址、端口、接口等匹配条件结构体，报文过滤规则、重定向规则等配置结构体，以及操作返回的错误码。  适用于调用[OH\_TrafficFilter\_CreateRedirector](capi-net-trafficfilter-h.md#oh_trafficfilter_createredirector)等接口时构造参数和解析返回值。 |
