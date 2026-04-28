---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-75
title: http模块是否支持忽略证书认证
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http模块是否支持忽略证书认证
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b087ca5250816af1297f5798fd653a8f192e9f75260222072c85c9dfc7e7152e
---

在API18及以上版本中，http模块支持忽略SSL证书认证过程。可通过设置参数HttpRequestOptions中的remoteValidation为skip，以跳过验证服务端证书。

**参考链接**

[RemoteValidation](../harmonyos-references/js-apis-http.md#remotevalidation18)
