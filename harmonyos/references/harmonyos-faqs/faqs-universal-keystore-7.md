---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-7
title: 如何获取HarmonyOS签名证书的公钥信息
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > 如何获取HarmonyOS签名证书的公钥信息
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:35+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:619986f7fd2bf59aa15e041f09103a2f416e56f7aaa1facb9bd644796c2fe76e
---

获取HarmonyOS签名可以参考指南手动签名章节，公钥用于给数据加密，用公钥加密的数据只能使用私钥解密，可以通过以下命令获取公钥信息（需要提前安装安全套接字层密码库[Openssl](https://www.openssl.org/)）：

```powershell
openssl x509 -in xxx.cer -pubkey -noout
```

**参考链接**

[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)
