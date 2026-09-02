---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-126
title: HarmonyOS下VPN的DNS解析顺序及域名拦截失效的处理方案
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HarmonyOS下VPN的DNS解析顺序及域名拦截失效的处理方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:262e5c099736b9227b99f4792c35e2ec5615aacfab5d330956c07dc525479204
---

## 问题现象

在HarmonyOS应用开发中，配置并启动VPN后，不同应用或网络组件对VPN指定DNS的解析行为可能存在差异。以下是两类典型的DNS解析场景：

问题一：启动[VPN](../harmonyos-references/js-apis-net-vpnextension.md#vpnextensionstartvpnextensionability)，通过[dnsAddresses](../harmonyos-references/js-apis-net-vpnextension.md#vpnconfig)配置VPN使用的DNS（Address1）服务器，若设备配置DOH（Address2），且APP使用rcp设置DNS（Address3）发起HTTP请求时，DNS会按什么顺序发起解析，是否会导致VPN的DNS解析异常？

问题二：在VPN应用中通过接管DNS协议通讯改写A记录（如将特定域名指向127.0.0.1）来实现域名封禁，但华为浏览器未使用VPN配置的DNS，导致可以正常访问被封禁的域名，应如何处理？

## 背景知识

* DNS（Domain Name System）：域名系统，是互联网的一项服务，它作为将域名转换为IP地址的系统，是网络基础设施的重要组成部分。
* [DOH（DNS over HTTPS）](../harmonyos-references/remote-communication-rcp.md#dnsoverhttpsconfiguration)：配置HTTPS上的DNS（DOH）设置，以加密的HTTPS协议进行DNS解析请求，避免原始DNS协议中用户的DNS解析请求被窃听或者修改的问题，来达到保护用户隐私的目的。

## 解决方案

针对上述不同场景下的DNS解析异常或拦截失效问题，提供以下解决方案：

问题一：VPN连接期间DNS解析顺序及rcp自定义DNS的影响。

在VPN连接期间，VPN旨在创建一个封闭的网络环境，所有尝试访问网络的请求默认将使用VPN提供的DNS服务器进行解析。当应用使用rcp给单个请求配置了[DOH（DNS over HTTPS）](../harmonyos-references/remote-communication-rcp.md#dnsoverhttpsconfiguration)，该单个请求会按照其特定配置解析，这属于应用自身的定制化行为，通常不会影响到系统整体VPN的DNS解析状态。

问题二：华为浏览器绕过VPN DNS导致域名封禁失效的处理方案。

华为浏览器在网络请求路径上存在特殊处理，会使用内置的HTTPDNS或代理域名进行解析，从而绕过VPN模块配置的DNS拦截规则。为了在VPN应用中实现对华为浏览器特定域名的有效封禁，建议在VPN应用的拦截或DNS改写规则中，显式禁用或拦截华为浏览器专用的以下域名：

HTTPDNS域名：httpdns-browser.platform.dbankcloud.cn

Proxy域名：gpa-proxy-drcn.platform.dbankcloud.cn

通过配置拦截上述域名，可以阻断浏览器自有的DNS解析通道，使其回退到VPN的DNS配置中，从而规避封禁失效的问题。

## 常见FAQ

Q：为什么在设置自定义DNS后，HTTP请求还是会走本地DNS缓存？

A：HTTP请求存在连接复用，而连接复用基于域名匹配，如果已经有指向相同域名的连接可以复用，那么请求会直接复用已有的连接，导致自定义规则不生效。

Q：HTTP已有连接复用，如何使自定义DNS立即生效？

A：本地DNS缓存默认超时时间为10分钟，对于HTTP1.1协议，可以通过发起一个超时时间为1ms的请求，当请求超时后会结束复用的TCP流，再次发起的请求将使用自定义DNS规则。

Q：如何清理本地DNS缓存？

A：当前本地DNS缓存由系统自动清理，触发时机为断网（包括切换网卡）或TTL超时，超时时间为10分钟。

Q：[dnsAddresses](../harmonyos-references/js-apis-net-vpnextension.md#vpnconfig)是否支持传入ip:port格式？

A：DNS服务器默认为53端口，支持传入ip:53，但传入ip:[其他端口]无法正常使用。
