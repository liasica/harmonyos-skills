---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-83
title: HarmonyOS应用如何做到防抓包
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > HarmonyOS应用如何做到防抓包
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:28c984f4292d41f7e895f133f13d7e960ea3f01dc60b87dab4e71c7f40bd9151
---

## 问题现象

为了数据传输安全，其他平台端都做了对应的防抓包措施，可以避免用户通过抓包工具窃取一些相关信息，HarmonyOS应用应该如何做到防抓包呢？

## 背景知识

应用与服务器之间通过网络传输数据，确保数据在传输过程中的安全，保护传输数据的机密性和完整性，防止敏感数据被窃取和篡改是很重要的。

当应用访问云侧服务器时，第三方可以通过网络代理工具（如Fiddler、Charles，也称抓包工具）对网络传输数据进行中间人攻击（如查看、篡改请求和响应消息），可能会导致应用或云侧服务器产生安全风险。因此，开发者需要实施必要的反抓包策略，以保护应用和用户的数据安全。

## 解决方案

HarmonyOS应用的防抓包策略是HTTPS协议+证书校验+取消代理。

1. HTTP升级成HTTPS：确保所有的网络请求都通过HTTPS协议进行，HTTPS是HTTP和SSL/TLS安全协议的结合，它提供了加密、数字证书认证、数据完整性三方面的保护。抓包工具即使拦截到数据包，也只能看到密文，无法直接解析。
2. 证书校验：常规HTTPS是单向认证（服务端向客户端证明身份），抓包工具通过伪造根证书让客户端信任，从而解密HTTPS数据。双向认证让客户端也向服务端证明身份，只有携带合法客户端证书的请求，服务端才会处理。详细步骤：

* 服务端生成CA根证书，并基于根证书生成客户端证书（公钥+私钥，如p12/pem格式）。
* HarmonyOS应用客户端将客户端证书内置到应用中，参考[配置信任应用管理的CA证书](../harmonyos-guides/network-connection-security-configuration.md#配置信任应用管理的ca证书)；同时配置[不信任用户安装的CA证书](../harmonyos-guides/network-connection-security-configuration.md#配置不信任用户安装的ca证书)。
* 服务端配置TLS双向认证，要求客户端握手时必须携带合法客户端证书，否则直接断开连接；
* 证书定期更新，避免证书泄露，若泄露立即吊销并更换。

3. 取消代理：检测客户端是否开启了HTTP/HTTPS代理，抓包工具几乎都需要通过代理拦截请求，对于有HTTPS请求和RCP请求可通过取消代理实现。

* Network Kit：[使用HTTP访问网络](../harmonyos-guides/http-request.md)通过配置usingProxy:false实现，示例代码可参考[发起HTTP数据请求](../harmonyos-guides/http-request.md#发起http数据请求).
* Remote Communication Kit：[定制代理](../harmonyos-guides/remote-communication-customproxyconfig.md)通过配置proxy:'no-proxy'实现，示例代码可参考[使用样例](../harmonyos-guides/remote-communication-customproxyconfig.md#no-proxy)。

## 常见FAQ

Q：SSL证书即将过期的情况下，使用axios发起网络请求如何防抓包？

A：防抓包需要SSL证书，所以需要及时更新SSL证书，避免证书到期导致无法抓包。

Q：如何禁止使用网络代理工具（如Fiddler、Charles）对应用进行抓包，从而获取HTTPS协议的网络请求返回的明文信息？

A：配置不信任用户安装的CA证书，创建src/main/resources/base/profile/network\_config.json配置文件并进行配置，如下设置（参考文档：[配置不信任用户安装的CA证书](../harmonyos-guides/network-connection-security-configuration.md#配置不信任用户安装的ca证书)）：{"trust-current-user-ca": false}
