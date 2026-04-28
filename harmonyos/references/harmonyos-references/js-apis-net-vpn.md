---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-vpn
title: @ohos.net.vpn (VPN管理)
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.vpn (VPN管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:08:28+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:b2b33ae6ccbbe5ee21027c23239b951dee8802a5ed614cfee8e6512f11238cef
---

本模块是操作系统提供的内置VPN功能，允许用户通过系统的网络设置进行VPN连接，通常提供的功能较少，而且有比较严格的限制。

说明

本模块首批接口从 API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { vpn } from '@kit.NetworkKit';
```

## LinkAddress

PhonePC/2in1TabletTVWearable

type LinkAddress = connection.LinkAddress

获取网络链接信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.LinkAddress](js-apis-net-connection.md#linkaddress) | 网络链路信息。 |

## RouteInfo

PhonePC/2in1TabletTVWearable

type RouteInfo = connection.RouteInfo

获取网络路由信息。

**系统能力**：SystemCapability.Communication.NetManager.Core

| 类型 | 说明 |
| --- | --- |
| [connection.RouteInfo](js-apis-net-connection.md#routeinfo) | 网络路由信息。 |

## AbilityContext

PhonePC/2in1TabletTVWearable

type AbilityContext = \_AbilityContext

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 类型 | 说明 |
| --- | --- |
| [\_AbilityContext](js-apis-inner-application-uiabilitycontext.md) | 需要保存状态的UIAbility所对应的context，继承自[Context](js-apis-inner-application-context.md)，提供UIAbility的相关配置信息以及操作UIAbility和ServiceExtensionAbility的方法。 |
