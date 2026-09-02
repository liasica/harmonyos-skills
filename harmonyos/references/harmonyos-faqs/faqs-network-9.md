---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-9
title: http请求的官方示例代码中的extraData是什么类型
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求的官方示例代码中的extraData是什么类型
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:36+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:db5002c1aa46273266e827c1afabd21a2f13091c8c7554c3aaa5c8445806356c
---

1. 文档中对extraData的定义是“extraData?: string | Object | ArrayBuffer”，也就是extraData支持string、Object和ArrayBuffer三种类型。
2. 有如下三种方法可供选择。

   ```text
   1）extraData:"data to send";
   2）extraData:{ data: "data to send", };
   3）extraData:{ data: new ArrayBuffer(1)};
   ```

**参考链接**

[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)
