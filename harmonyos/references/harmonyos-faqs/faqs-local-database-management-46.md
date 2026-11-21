---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-46
title: "@ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值"
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > @ohos.data.distributedKVStore接口中的deleteKVStore，第一个参数appId需要传递什么值
category: harmonyos-faqs
scraped_at: 2026-11-21T09:18:37+08:00
doc_updated_at: 2026-11-20
content_hash: sha256:a26365d637207368c72419c8dd63dc141cbc8645c67a014e241f06c036d82002
---

在 @ohos.data.distributedKVStore 接口中的[deleteKVStore](../doccenter-references/api/js-apis-distributedkvstore.md#deletekvstore)方法中，第一个参数 appId 需要传递的是应用的BundleName。

[BundleName](../doccenter-getting-started/app-configuration-file.md#配置文件标签)为应用的Bundle名称，用于标识应用的唯一性，在工程 AppScope/app.json5 配置文件的 bundleName 标签中声明。
