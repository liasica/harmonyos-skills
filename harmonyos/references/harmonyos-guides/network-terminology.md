---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/network-terminology
title: Network Kit术语
breadcrumb: 指南 > 系统 > 网络 > Network Kit（网络服务） > Network Kit术语
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:34+08:00
doc_updated_at: 2026-06-13
content_hash: sha256:6fd9d008a3c15b36d62eaa80b52a579a21e5256bc2c052e31d2f140d964e102d
---

## D

### DNS

Domain Name System，域名系统。其核心功能是将人类易记的域名转换为机器可识别的IP地址，实现网络资源的定位与访问‌。

### Default Network；默认网络

默认网络是系统默认使用的网络。由系统决定，与应用是否指定网络无关，系统会根据网络可用性、能力、优先级和其他策略，在Wi‑Fi、蜂窝数据、以太网、蓝牙连接中选定默认网络。

* 应用若未绑定到特定网络，其请求通常通过默认网络发送。
* 默认网络可能因网络切换、信号变化或系统策略而发生变化。
* 默认网络不一定是唯一可用网络，而是系统当前首选的网络。

## E

### Extensible Authentication Protocol (EAP)；可扩展认证协议

一种用于网络认证的认证框架，支持多种认证方法。在802.1X网络中，EAP提供了一个灵活的认证机制，可以在以太网、Wi-Fi等网络中使用，允许开发者自定义EAP认证流程。

## H

### HTTP

Hypertext Transfer Protocol，超文本传输协议。是一种用于分布式、协作式和超媒体信息系统的应用层协议。

### HTTPS

Hypertext Transfer Protocol Secure，是一种基于HTTP的安全通信协议，通过SSL/TLS加密技术实现数据传输的保密性、完整性和身份认证‌。

### Interceptor；拦截器

用于在HTTP请求和响应过程中进行拦截和修改的组件，支持创建拦截器链，按需定制一组拦截器对网络请求/响应进行修改。

## M

### MDNS

Multicast DNS，即多播DNS，用于在局域网中自动发现和配置设备。

### Multi-part Form；多部分表单

用于发送HTTP多部分表单数据的对象，支持指定表单中key的发送顺序，适用于文件上传等场景。

## N

### Network Handle (NetHandle)；网络句柄

网络句柄是系统用于标识特定网络连接实例的标识符。应用可通过该句柄查询网络能力、链路属性、路由状态等信息，或将流量绑定到指定网络。

* 用于唯一标识一个已建立或可用的网络实例。
* 可用于网络查询、网络绑定和策略控制。
* 当无网络可用时，网络句柄的netId为0。

### Network Bearer Type (NetBearType)；网络承载类型

网络承载类型用于表示底层接入网络的类别，如蜂窝网络、Wi‑Fi、以太网、蓝牙或VPN等，用于区分不同类型的网络接入方式。

### Network Probing；网络探测

网络探测是系统用于评估网络可用性、连通性或互联网可访问性的检测机制。

## S

### SSL

Secure Socket Layer，安全套接字层，是一种网络安全协议，为客户端（如浏览器）与服务器之间的通信提供加密和身份验证，确保传输数据的保密性、完整性和可靠性‌。

### System VPN；系统VPN

系统VPN是系统提供的VPN连接与管理能力，用户可通过系统设置、企业配置或系统接口建立和管理VPN连接。系统VPN通常与系统网络栈深度集成，可统一管理连接状态、路由、认证和策略。

## T

### TCP

Transmission Control Protocol，是一种面向连接的、可靠的、基于字节流的传输层通信协议‌。

### TLS

Transport Layer Security，安全传输层，TLS是建立在传输层TCP协议之上的协议，服务于应用层，它的前身是SSL，实现了将应用层的报文进行加密后再交由TCP进行传输的功能。

### Third-party VPN；三方VPN

第三方VPN是由非操作系统提供方开发的VPN应用或服务，通常通过系统提供的VPN能力创建虚拟网络接口并处理网络流量。其具体协议、功能和安全能力取决于应用实现。

## U

### UDP

User Datagram Protocol，是传输层的一种无连接、不可靠的通信协议，主要用于实时性要求高的数据传输‌。

## V

### VPN

Virtual Private Network，虚拟专用网络。主要功能是在公用网络上建立专用网络，进行加密通信。‌
