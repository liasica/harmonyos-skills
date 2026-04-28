---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-24
title: 创建KVManager时bundleName必须是本应用的包名吗
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 创建KVManager时bundleName必须是本应用的包名吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c889bb150ac257195eefcd56ba461defb2a5a6b75e98928d35363a9cf86593bc
---

虽然bundleName可以使用非本应用包名，但由于closeKVStore/deleteKVStore等操作需要验证appId与bundleName的一致性，为避免混淆建议使用应用包名。
