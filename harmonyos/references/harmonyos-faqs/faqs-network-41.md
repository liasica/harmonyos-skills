---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-41
title: httpRequest.request请求https接口ssl证书验证失败
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > httpRequest.request请求https接口ssl证书验证失败
category: harmonyos-faqs
scraped_at: 2026-04-29T14:19:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:91a95bfd3cb827aa92751ff31e914a79e136419b3dc6af147e4c960d0c863622
---

**问题现象**

https接口httpRequest.request请求报错：“SSL peer certificate or SSH remote key was not OK”。

1. httpRequest.request怎样进行证书验证。
2. httpRequest.request能否忽略证书认证访问https接口。

**解决措施**

HTTPS证书用于保护网站安全。HTTPS证书校验是在建立连接时验证证书，确保连接安全。

HTTPS校验主要包括以下几个步骤：

1. 客户端向服务器发送HTTPS请求。
2. 服务器返回SSL证书。
3. 客户端对证书进行校验。
4. 如果验证通过，客户端和服务器将建立安全的HTTPS连接。

本题中的报错出现在第三步，即客户端对证书校验报错。

客户端对证书的校验，验证SSL证书的四个方面：

1. 检查SSL证书是否是由浏览器中“受信任的根证书颁发机构”颁发。
2. 检查SSL证书中的证书吊销列表，检查证书是否被证书颁发机构吊销。
3. 检查此SSL证书是否过期。
4. 检查部署此SSL证书校验的网站域名和证书域名是否一致。

如果客户端未对证书进行校验，可能会导致中间人攻击。中间人攻击包括SSL劫持和SSL剥离。

SSL劫持原理：第三方攻击者会先接入请求方和接收方之间，通过伪造的证书与请求方交换数据，再以请求方的身份与接收方进行数据交互。SSL劫持通常发生在用户安装了未经权威CA认证的证书时，因此需要进行证书校验。

**图1** SSL劫持  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/zFQcX8_9SHW0rRFXGeiRgQ/zh-cn_image_0000002194158516.png?HW-CC-KV=V1&HW-CC-Date=20260429T061915Z&HW-CC-Expire=86400&HW-CC-Sign=4F6AC718976F7AF2F4710A8AD278FACD4303CC9CE1C05E513605904454009152 "点击放大")

SSL剥离通常发生在HTTP请求中，现代网站多强制使用HTTPS。

问题1：开发者应对服务端的证书进行上述四个方面的检查，确认无误。如果服务端证书是自定义的CA，即SSL证书不是由浏览器中“受信任的根证书颁发机构”颁发，可以通过httpRequest.request接口的HttpRequestOptions参数中的caPath设置自定义CA的路径。设置此参数后，系统将使用指定路径的CA证书，开发者需确保该路径下CA证书的可访问性。否则，系统将使用预设的CA证书，预设CA证书位置为：/etc/ssl/certs/cacert.pem。

**参考链接**

[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)
