---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/net-mgmt-overview
title: Network Kit简介
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > Network Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:50+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:52bb8387bdbc791f6d05a6d57d3e78561ec7cccbc4abe8a766912387c30cf31d
---

Network Kit（网络服务）主要提供以下功能：

* [HTTP数据请求](http-request.md)：通过HTTP发起一个数据请求。
* [WebSocket连接](websocket-connection.md)：使用WebSocket建立服务器与客户端的双向连接。
* [Socket连接](socket-connection.md)：通过Socket进行数据传输。
* [网络连接管理](net-connection-manager.md)：网络连接管理提供管理网络一些基础能力，包括WiFi/蜂窝/Ethernet等多网络连接优先级管理、网络质量评估、订阅默认/指定网络连接状态变化、查询网络连接信息、DNS解析等功能。
* [MDNS管理](net-mdns.md)：MDNS即多播DNS（Multicast DNS），提供局域网内的本地服务添加、删除、发现、解析等能力。

## 模拟器支持情况

Network Kit支持模拟器，但与真机存在差异，具体差异如下。

* 通用差异：详情请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器不支持VPN功能。

## 约束与限制

使用网络管理模块的相关功能时，需要请求相应的权限。

在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。然后参考[访问控制-声明权限](declare-permissions.md)声明对应权限。

| 权限名 | 说明 |
| --- | --- |
| ohos.permission.GET\_NETWORK\_INFO | 获取网络连接信息。 |
| ohos.permission.INTERNET | 允许程序打开网络套接字，进行网络连接。 |
