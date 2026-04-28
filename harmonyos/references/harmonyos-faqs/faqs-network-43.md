---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-43
title: 能否通过httpResponse的result拿到一个加密内容的数据
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > 能否通过httpResponse的result拿到一个加密内容的数据
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:23f8355edf6d4d5c29e7c9f49fbaa5938c7aace0ac2c64537fd51a3f0aa2b363
---

使用HTTP请求传递加密数据，可以在result中获取到结果。

HTTP请求根据响应头中content-type类型返回对应的响应格式内容，若HttpRequestOptions无expectDataType字段，按如下规则返回：

* application/json：返回JSON格式的字符串。
* application/octet-stream：ArrayBuffer。
* image：ArrayBuffer。
* 其他：string。

若HttpRequestOption有expectDataType字段，开发者需传入与服务器返回类型相同的数据类型。

**参考链接**

[request](../harmonyos-references/js-apis-http.md#request)
