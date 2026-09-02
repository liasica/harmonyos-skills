---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-54
title: 证书生效，但开发工具提示证书过期
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 证书生效，但开发工具提示证书过期
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:51fdf295847d7aa3090751ea01ba10d15f04bd398f5c55d5dd8a4d9aafb699cd
---

## 问题现象

重新生成安装包的时候，证书上是生效的，为什么开发工具会提示证书过期？

## 解决方案

在HarmonyOS开发中，若重新生成安装包时提示“证书过期”但证书显示生效，可能涉及以下原因：

1. 证书与Profile未同步更新：证书（.cer）更新后，对应的Profile文件（.p7b）未重新生成或绑定，导致签名校验失败。
2. 密钥库文件不一致：新证书未通过同一CSR文件生成，导致密钥库文件（.p12）与原有证书不匹配。具体可以参考：[生成密钥和证书请求文件](../harmonyos-guides/ide-publish-app.md#section1079214271414)。
3. [调试证书](../app/agc-help-debug-cert-0000002283256797.md)与[发布证书](../app/agc-help-release-cert-0000002283336729.md)混淆：调试证书有效期为180天（实名开发者）或14天（未实名），发布证书有效期为3年。若误用调试证书，可能因实际有效期不符触发错误。
4. 开发工具缓存问题：旧证书或Profile信息可能被开发工具缓存，导致新文件未生效。

具体流程可参考[应用发布流程](../harmonyos-guides/ide-publish-app.md#section199431631899)。
