---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-94
title: 实现应用中的网络请求不被中间者拦截的方案
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 实现应用中的网络请求不被中间者拦截的方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:cd70029d4df371bca24b703b28b4ca4e91b46e489eeee8e80a2fe1a61c87bf28
---

## 问题现象

在应用开发中，网络请求存在被中间者截获、监听或篡改的风险，尤其是在传输用户敏感信息（如身份标识、令牌、交易数据）时，这类攻击可能导致数据泄露、身份冒用或业务逻辑被破坏。

如何设计机制或采取安全策略，防止应用中的网络请求在传输过程中被非法方拦截或篡改，从而保障数据通信的安全性？

## 背景知识

* [定制安全传输行为](../harmonyos-guides/remote-communication-customsecurityconfig.md)：一种加密通信机制，用于在客户端和服务器之间建立可信的连接。通过交换证书和公钥来验证双方的身份，并确保数据的完整性和隐私。
* [WebSocket连接](../harmonyos-references/js-apis-websocket.md)：API11之后，WebSocketRequestOptions配置里有caPath选项，设置了此参数，系统将使用用户指定路径的CA证书。clientCert选项还支持传输客户端证书。

## 解决方案

防止网络请求被中间者拦截可以从两个方面考虑，一方面是应用层面，另一方面是网络通信层面。

* 在应用层面可以考虑：
  + 启用双向认证：客户端不仅验证服务端证书，也提供自身证书TLS防止伪冒。
  + 代码混淆和加壳：配置HarmonyOS具有的代码混淆选项。
  + 请求签名机制：对每次请求参数进行HMAC或RSA签名，防篡改。
  + 时间戳+随机数：请求带上时间戳和随机数，防止重放攻击。
  + 在WebSocket配置证书。
* 在网络通信层面考虑：
  + 使用HTTPS协议进行网络通信，确保数据传输过程中的加密和完整性。可以防止中间者通过截取网络流量来获取或篡改数据。
  + 确保服务器端的SSL/TLS证书是有效的，并由受信任的证书颁发机构颁发。
  + 关闭中间缓存，请求设置Cache-Control:no-store避免敏感信息被缓存。
  + 自定义DNS服务器防止DNS劫持。
  + 建立加密通道如内网专线和VPN，避免在公共网络暴露。
  + 在request中设置请求的DNS规则。
