---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-network-64
title: http请求传输大于5M文件报错2300023
breadcrumb: FAQ > 系统开发 > 网络 > 网络（Network） > http请求传输大于5M文件报错2300023
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:14+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c237b8763d60caf595a5743e7e9e64b78cd8e814b1ca1d6dcdf47a68ca5add28
---

http请求默认规格最大可传输5M数据文件（自API Version 23开始，该默认规格扩充至50MB），当http请求数据超过5M时，可在[HttpRequestOptions](../harmonyos-references/js-apis-http.md#httprequestoptions)的maxLimit中进行设置，将最大接收数据扩大到100M。如果超过100M大小，或者不确定数据大小但有可能超过100M时，建议使用[requestInStream](../harmonyos-references/js-apis-http.md#requestinstream10)接口发起流式请求。参考文档：[发起http流式传输请求](../harmonyos-guides/http-request.md#发起http流式传输请求)。
