---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-hmac-overview
title: HMAC介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > HMAC > HMAC介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cefb14a15ee23540ad13070f5737118e96aa339d170b9d8bb9ff94d9cdbd05a4
---

MAC（Message Authentication Code）提供了一种在不可靠介质上检验传输或存储信息完整性的方法，HMAC是密钥相关的哈希运算消息认证码（Hash-based Message Authentication Code），是一种基于Hash函数和密钥进行消息认证的方法。HMAC可以与任何加密哈希函数（例如SHA256、SM3等）结合使用，HUKS支持了HMAC结合主流的摘要算法进行使用。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 支持的算法

以下为HMAC支持的规格说明。

| 摘要算法 | 支持的密钥长度 | API级别 |
| --- | --- | --- |
| SHA256 | 192 - 1024 | 8+ |
| SHA384、SHA512 | 256 - 1024 | 8+ |
| SM3 | 80 - 1024 | 8+ |
