---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-crypto-architecture-kit-new-00001
title: AES128|GCM解密报错convertSymKey key failed
breadcrumb: FAQ > 系统开发 > 安全 > 加解密算法（Crypto Architecture） > AES128|GCM解密报错convertSymKey key failed
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:1e43d7b42ab71c3a25c90fec61932503fb08d854989f6e7a6f2828bf367e7570
---

## 问题现象

在进行AES128|GCM解密时，设置32位长度的密钥会报错“Error: convertSymKey key failed!”，而将密钥长度设置为16位时可以正常解密。

## 背景知识

[AES（Advanced Encryption Standard）](../harmonyos-guides/crypto-sym-key-generation-conversion-spec.md#aes)支持三种长度的密钥：128位、192位、256位。在加解密框架中，调用[createSymKeyGenerator](../harmonyos-references/js-apis-cryptoframework.md#cryptoframeworkcreatesymkeygenerator)创建密钥生成器后，通过[convertKey](../harmonyos-references/js-apis-cryptoframework.md#convertkey)或[convertKeySync](../harmonyos-references/js-apis-cryptoframework.md#convertkeysync12)转换密钥时，框架会严格校验传入的密钥数据长度是否与算法规格匹配。

## 问题定位

1. 检查加解密使用的算法规格，确认为AES128|GCM。
2. 检查传入的密钥数据长度，当前设置为32字节。
3. 根据AES128算法规格，其要求的密钥长度应为16字节（128位），传入32字节（256位）会导致长度不匹配。

## 分析结论

使用AES128|GCM算法时，对应的密钥生成器为AES128，要求密钥数据必须为16字节。当传入32字节（256位）的密钥时，框架检测到长度不匹配，直接报错“Error: convertSymKey key failed!”。

## 修改建议

修正密钥长度以匹配算法规格

将AES128|GCM解密逻辑中的密钥长度从32字节修改为16字节，即可正常执行解密操作。
