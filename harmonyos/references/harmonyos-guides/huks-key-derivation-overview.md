---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/huks-key-derivation-overview
title: 密钥派生介绍及算法规格
breadcrumb: 指南 > 系统 > 安全 > Universal Keystore Kit（密钥管理服务） > 本地密钥管理 > 密钥使用 > 密钥派生 > 密钥派生介绍及算法规格
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ed36badac3b92b8cf2f1c3acf636ae19add44064e135600cc665272fe47a115c
---

在密码学中，密钥派生函数（Key derivation function，KDF）使用伪随机函数从诸如主密码或密码的秘密值中派生出一个或多个密钥。

说明

* 在HUKS中只能通过HUKS托管的密钥进行密钥派生。
* 轻量级智能穿戴不支持密钥派生功能。
* 使用现有密钥别名作为派生结果密钥别名会把现有密钥覆盖。

从API 23开始支持[群组密钥](huks-group-key-overview.md)特性。

## 支持的算法

以下为密钥派生支持的规格说明。

派生密钥是业务基于三段式得到密钥会话结果，业务可决定派生密钥是否由HUKS管理（即密钥不出[TEE](huks-concepts.md#可信执行环境tee)）亦或是业务独立管理。

说明

PBKDF2/HKDF仅支持HUKS托管密钥的派生，不支持直接基于非HUKS托管的密钥进行派生，如：用户的口令，密钥托管参考[密钥导入](huks-key-import-overview.md)。

| 算法/摘要 | 派生密钥的算法/长度 | 派生结果密钥可用算法/长度 | API级别 |
| --- | --- | --- | --- |
| HKDF/SHA256 | AES/192/256 | AES/128/192/256  HMAC/8-1024  SM4/128 | 8+ |
| HKDF/SHA384 | AES/256 | AES/128/192/256  HMAC/8-1024  SM4/128 | 8+ |
| HKDF/SHA512 | AES/256 | AES/128/192/256  HMAC/8-1024  SM4/128 | 8+ |
| PBKDF2/SHA256 | AES/192/256 | AES/128/192/256  HMAC/8-1024  SM4/128 | 8+ |
| PBKDF2/SHA384 | AES/256 | AES/128/192/256  HMAC/8-1024  SM4/128 | 8+ |
| PBKDF2/SHA512 | AES/256 | AES/128/192/256  HMAC/8-1024  SM4/128 | 8+ |
| 算法/摘要 | 派生密钥的算法/长度 | 派生结果密钥可用算法/长度 | API级别 |
| -------- | -------- | -------- | -------- |
| HMAC/SHA256 | AES/192/256 | AES/256  HMAC/256 | 12+ |
| HMAC/SHA384 | AES/256 | HMAC/384 | 12+ |
| HMAC/SHA512 | AES/256 | HMAC/512 | 12+ |
| HKDF/SHA256 | X25519/256 | X25519/256 | 12+ |
| HKDF/SHA384 | X25519/256 | X25519/256 | 12+ |
| HKDF/SHA512 | X25519/256 | X25519/256 | 12+ |
