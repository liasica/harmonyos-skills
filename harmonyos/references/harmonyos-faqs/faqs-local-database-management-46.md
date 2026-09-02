---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46
title: "@ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值"
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:848aa1cededf785177ff0ae8c24cf9db1f83002cd6fcabde74f6f6a29fc9ae0b
---

appId是应用的唯一标识，由包名、下划线和证书公钥的Base64编码组成。可以调用[bundleManager.getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取自身的BundleInfo应用包信息，应用包信息中包含signatureInfo签名信息，签名信息中包含appId信息。示例代码可参见：[如何获取应用信息中的appId](../harmonyos-guides/common-problem-of-application.md#如何获取应用信息中的appid)。
