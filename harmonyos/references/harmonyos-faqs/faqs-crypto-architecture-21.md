---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-21
title: Huks生成2048位RSA密钥，加密数据，报错401错误
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > Huks生成2048位RSA密钥，加密数据，报错401错误
category: harmonyos-faqs
scraped_at: 2026-09-02T15:21:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c3ead19efa1e42684d655b1db540ff9cacd2d8be356472c533fd81e1b321c5ff
---

生成RSA密钥长度与生成密钥时传入参数有关，例如生成2048位RSA密钥参数可以传'RSA2048|PRIMES\_2'或者'RSA2048|PRIMES\_3'。

**参考链接**

[RSA](../harmonyos-guides/crypto-asym-encrypt-decrypt-spec.md#rsa)
