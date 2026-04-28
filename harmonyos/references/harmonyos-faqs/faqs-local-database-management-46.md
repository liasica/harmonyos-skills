---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46
title: @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:60e34b7be253323ddccc930744dcac915a360b0b0af248cb5a1cd395c93fda72
---

appId是调用方应用的包名。通过调用[bundleManager.getBundleInfoForSelf()](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)获取BundleInfo，然后通过BundleInfo对象的signatureInfo属性获取appId。
