---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-66
title: HarmonyOS NEXT生态市场单独发布HAR包为什么需要工程签名
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > HarmonyOS NEXT生态市场单独发布HAR包为什么需要工程签名
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5409bd2403b9835529fccfaaa6552c40b4d01f4632984a4d4b7feafbd2a10207
---

## 问题现象

伙伴开发HarmonyOS NEXT组件在生态市场上架失败，"审核意见：1、包体规范：签名验证未通过，请补充！"。

伙伴按照文档[对HAR进行签名](../harmonyos-guides/ide-hvigor-build-har.md#section116791730173713)更改签名，发现第二条配置工程签名信息，配置流程请参考[准备签名文件](../harmonyos-guides/ide-publish-app.md#section793484619307)。需要了解单独发布HAR包为何需要工程签名？

## 解决方案

伙伴可以申请一个单独的证书，工程签名的目的是确保这个组件是这个开发者的，否则，被其他开发者滥用，容易引发版权纠纷等问题。
