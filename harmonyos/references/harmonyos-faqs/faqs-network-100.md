---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-100
title: HarmonyOS系统对标其他平台的网络方案
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HarmonyOS系统对标其他平台的网络方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0924f5662a1f6ce90b3664463f84ce9b34352c1f60344d0f5922d6fb57425477
---

## 问题现象

其他平台提供了一系列与网络相关的类和接口，用于处理网络连接、URI操作、WIFI管理等功能，HarmonyOS系统上的对标方案是什么？

## 解决方案

* 网络连接管理：提供类和方法来检查网络状态、连接类型等。

  HarmonyOS对标方案：
  1. [网络连接管理](../harmonyos-guides/net-connection-manager.md)提供管理网络的一些基础能力，包括WiFi/蜂窝/Ethernet等多网络连接优先级管理、网络质量评估、订阅默认/指定网络连接状态变化、查询网络连接信息、域名系统解析等功能。
  2. [以太网连接管理](../harmonyos-references/js-apis-net-ethernet.md)提供以太网连接管理能力，包括有线网络能力、获取有线网络的IP地址等信息。
* URI操作：提供工具类解析和操作URI。

  HarmonyOS对标方案：

  [URI](../harmonyos-references/js-apis-uri.md#uri)字符串解析模块遵循RFC3986规范标准，该标准定义了如何编码和解析用于定位网络资源的标识符，对于非标准场景不支持解析。
* WIFI管理：提供类和方法管理WIFI连接。

  HarmonyOS对标方案：

  [wifiManager](../harmonyos-references/js-apis-wifimanager.md)主要提供WLAN基础功能（Wi-Fi接入、Wi-Fi加密、Wi-Fi漫游等）、P2P（peer-to-peer）服务的基础功能和WLAN消息通知的相应服务，让应用可以通过WLAN和其他设备互联互通。
* 网络请求：使用Network和URLConnection进行网络请求。

  HarmonyOS对标方案：
  1. [HTTP数据请求](../harmonyos-guides/http-request.md)：应用通过HTTP发起一个数据请求，支持常见的GET、POST、OPTIONS、HEAD、PUT、DELETE、TRACE、CONNECT方法。
  2. [WebSocket连接](../harmonyos-guides/websocket-connection.md)：使用WebSocket建立服务器与客户端的双向连接，需要先通过createWebSocket()方法创建WebSocket对象，然后通过connect()方法连接到服务器。
  3. [Socket 连接](../harmonyos-guides/socket-connection.md)：主要是通过套接字进行数据传输，支持TCP/UDP/Multicast/TLS协议。
  4. [MDNS管理](../harmonyos-guides/net-mdns.md)：即多播DNS（Multicast DNS），提供局域网内的本地服务添加、移除、发现、解析等能力。
