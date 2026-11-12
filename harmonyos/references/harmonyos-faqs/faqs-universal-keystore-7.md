---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-universal-keystore-7
title: 如何获取HarmonyOS签名证书的公钥信息
breadcrumb: FAQ > 系统开发 > 安全 > 密钥管理（Universal Keystore） > 如何获取HarmonyOS签名证书的公钥信息
category: harmonyos-faqs
scraped_at: 2026-11-12T09:59:30+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:2bd41352f9fa22fb45fa7c7fad2716a6a91e8db6748b3a155e31264bc1dd9870
---

获取HarmonyOS签名可以参考指南手动签名章节，公钥用于给数据加密，用公钥加密的数据只能使用私钥解密，可以通过以下命令获取公钥信息（需要提前安装安全套接字层密码库[Openssl](https://www.openssl.org/)）：

```powershell
openssl x509 -in xxx.cer -pubkey -noout
```

**参考链接**

[手动签名](../doccenter-deveco-studio/ide-signing-manual.md)
