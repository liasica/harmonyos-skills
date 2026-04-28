---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/crypto-key-generation-conversion-overview
title: 密钥生成与转换介绍
breadcrumb: 指南 > 系统 > 安全 > Crypto Architecture Kit（加解密算法框架服务） > 密钥生成和转换 > 密钥生成与转换介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:42:14+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:edb3035f4ab73cf9d92b576c6b00d574af2f789732951f76ae576b0d4ac375da
---

在以下场景中，经常需要使用密钥生成操作：

1. 随机生成算法库密钥对象。该对象可用于后续的加解密等操作。
2. 根据指定数据生成算法库密钥对象（即从外部源或存储系统中获取的二进制数据转换为算法库的密钥对象）。该对象可用于后续的加解密等操作。
3. 根据密钥参数生成指定的算法库密钥对象。该对象可用于后续的加解密等操作。
4. 获取算法库密钥对象的二进制数据，用于存储或传输。
5. 对于非对称密钥，获取密钥对象的参数属性，用于存储或传输。

其中，密钥对象Key包括对称密钥SymKey和非对称密钥（公钥PubKey和私钥PriKey），其中公钥和私钥组成密钥对KeyPair。
