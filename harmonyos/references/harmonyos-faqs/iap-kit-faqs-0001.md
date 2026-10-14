---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/iap-kit-faqs-0001
title: JWS数据解码与验签常见问题
breadcrumb: FAQ > 应用服务开发 > 应用内支付服务（IAP Kit） > 常见问题 > JWS数据解码与验签常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:15:56+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:2366ca4fed24e43c346a4905b8470f491cf3a69f37a6067a4478127af7f80c94
---

**Q：IAP服务器API返回结果以及服务端关键事件通知返回的是JSON Web Signature（JWS）格式的数据，针对该数据开发者如何进行解码和验签？**

**A**：IAP服务器返回的JWS的数据由Header、Payload和Signature三部分数据组成，需要分别进行Base64编码，然后才能进行传输，Header解码后的alg和typ参数是固定为ES256和JWT，对于x5c证书链需固定顺序为叶子证书、中间证书、根证书，后续按照如下步骤进行解码验签：

1. 使用Huawei CBG Root CA G2证书对证书链进行验证；
2. 校验叶子证书的OID：1.3.6.1.4.1.2011.2.415.1.1（固定值）；
3. 证书校验通过则从叶子证书获取到PublicKey；
4. 使用Header指定的算法和获取到的PublicKey进行JWT验签，服务端验签参考文档：[JWS解码和验签示例](../harmonyos-references/iap-verifying-signature.md#jws解码和验签示例)。

**Q：JWS数据支持的证书类型有哪些？**

**A**：通过TLS1.2和TLS1.3加密套件生成的证书目前JWS数据都是支持的。其中TLS1.3版本对应的加密套件是TLS\_AES\_128\_GCM\_SHA256、TLS\_AES\_256\_GCM\_SHA384和TLS\_CHACHA20\_POLY1305\_SHA256，TLS1.2版本对应的加密套件是TLS\_ECDHE\_RSA\_WITH\_AES\_256\_GCM\_SHA384，TLS\_ECDHE\_RSA\_WITH\_AES\_128\_GCM\_SHA256，TLS\_ECDHE\_ECDSA\_WITH\_AES\_256\_GCM\_SHA384和TLS\_ECDHE\_ECDSA\_WITH\_AES\_128\_GCM\_SHA256。
