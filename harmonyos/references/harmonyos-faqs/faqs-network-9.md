---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-9
title: http请求的官方示例代码中的extraData是什么类型
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求的官方示例代码中的extraData是什么类型
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:05+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:b89f247114e6925f983db0e56d8b116ef176702d8a706e8ba4675f45b2422c38
---

1. 文档中对extraData的定义是“extraData?: string | Object | ArrayBuffer”，也就是extraData支持string、Object和ArrayBuffer三种类型。
2. 有如下三种方法可供选择。

   ```
   1. 1）extraData:"data to send";
   2. 2）extraData:{ data: "data to send", };
   3. 3）extraData:{ data: new ArrayBuffer(1)};
   ```

   [ExtraData.txt](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/NetworkKit/entry/src/main/ets/pages/ExtraData.txt#L8-L10)

**参考链接**

[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)
