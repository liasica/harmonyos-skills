---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-13
title: Hash.hash是否支持同步接口
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > Hash.hash是否支持同步接口
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:23+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c16b2260a5765fcb5b7fc90da540328c7e16a805da8977b178996b8cf0ddb4a7
---

**解决措施**

[@ohos.file.hash](../harmonyos-references/js-apis-file-hash.md)提供文件哈希处理能力。

其中的[Hash.hash](../harmonyos-references/js-apis-file-hash.md#hashhash)方法为异步方法，目前不支持同步方法。若需实现同步逻辑，可将该方法的调用放在回调函数中。
