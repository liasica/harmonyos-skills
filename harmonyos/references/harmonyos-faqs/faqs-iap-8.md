---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-iap-8
title: 如何对JWS格式的数据解码和验签以及JWS支持的证书类型
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 如何对JWS格式的数据解码和验签以及JWS支持的证书类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:223baf4f43f285ea5486d13485c276761a099b5e34401f50d40879aa5707bc4b
---

## 问题现象

问题一：IAP服务器API返回结果以及服务端关键事件通知返回的是JSON Web Signature （JWS）格式的数据，针对该数据开发者如何进行解码和验签？

问题二：JWS数据支持的证书类型有哪些？

## 解决方案

* 问题一：IAP服务器返回的JWS的数据由Header、Payload和Signature三部分数据组成，需要分别进行Base64编码，然后才能进行传输，Header解码后的alg和typ参数是固定为ES256和JWT，对于x5c证书链需固定顺序为叶子证书、中间证书、根证书，后续按照如下步骤进行解码验签：
  1. 使用Huawei CBG Root CA G2证书对证书链进行验证。
  2. 校验叶子证书的OID：1.3.6.1.4.1.2011.2.415.1.1（固定值）。
  3. 证书校验通过则从叶子证书获取到PublicKey。
  4. 使用Header指定的算法和获取到的PublicKey进行JWT验签，服务端验签参考文档：[JWS解码和验签示例](../harmonyos-references/iap-verifying-signature.md#jws解码和验签示例)。

* 问题二：通过TLS1.2和TLS1.3加密套件生成的证书目前JWS数据都是支持的。其中TLS1.3版本对应的加密套件是TLS\_AES\_128\_GCM\_SHA256、TLS\_AES\_256\_GCM\_SHA384和TLS\_CHACHA20\_POLY1305\_SHA256，TLS1.2版本对应的加密套件是TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384，TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256，TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384和TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256。
