---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-signature-service-27
title: 编译HAP时签名过期问题如何解决
breadcrumb: FAQ > DevEco Studio > 签名服务 > 编译HAP时签名过期问题如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:05e1c188ad3b3a4febddba2b29942f28ee3bdc243017b11ae4d4323932bd8a2a
---

## 问题现象

本地调试时，DevEco编译HAP有如下报错：

```txt
TERROR - The certificate has expired! NotAfter: Sat Dec 07 15:30:13 CST 2024.
ERROR - hap-sign-tool: error: The certificate has expired! NotAfter: Sat Dec 07 15:30:13 CST 2024.
Try the following:
The certificate format is incorrect, please check your appCertFile parameter.
Detail: Please check the message from tools.hvigor ERROR: BUILD FAILED in 4 s 597 ms.
```

## 背景知识

针对开发调试场景，DevEco Studio为开发者提供了[自动签名](../harmonyos-guides/ide-signing.md#section18815157237)方案，帮助开发者高效进行调试。也可以选择[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)方式生成调试签名。

自动签名仅适用于部分调试场景，方便开发者进行调试。当需要进行跨设备调试、跨应用交互调试、断网情况下调试、涉及[申请ACL权限](../app/agc-help-apply-acl-0000002394212138.md#section156171230179)、或者多用户共同开发且需要共享密钥时，必须使用手动签名。

发布场景必须使用release签名。

## 解决方案

根据报错信息判断问题原因是签名过期，需要重新签名，具体步骤如下：

1. 在File-Project Structure-Signing Configs下查看证书存储路径(Certpath file(\*.cer))。
2. 进入证书存储路径，将过期的证书删除，废除过期的证书和Profile，用原有的csr和p12重新申请证书和Profile。
3. 本地调试时，在适用自动签名的场景，可以在Signing Configs页面勾选Automatically generate signature完成[自动签名](../harmonyos-guides/ide-signing.md#section18815157237)，其余需要手动签名的场景，需要去官网生成新的证书并更换证书。

## 常见FAQ

Q：打包报错提示“hap-sign-tool:error:invalid CEN header (bad signature)”。

A：出现此报错，可能是用户unsigned的包有问题，尝试clean project后重新打包。

Q：签名时，提示"Failed to query agreement signing records"。

A：出现该问题的原因一般是签名过程中，DevEco Studio与查询协议链接通道异常导致。请尝试通过如下两种方式解决。

* 方式一：该问题可能是由于DevEco Studio的HTTP代理问题引起的，请参考[配置代理](../harmonyos-guides/ide-environment-config.md)。
* 方式二：进行开发者实名认证，具体指导可以参考[实名认证指导](../start/itrna-0000001076878172.md)。
