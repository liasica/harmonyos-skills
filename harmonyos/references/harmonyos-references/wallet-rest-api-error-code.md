---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wallet-rest-api-error-code
title: REST API错误码
breadcrumb: API参考 > 应用服务 > Wallet Kit（钱包服务） > REST API > REST API错误码
category: harmonyos-references
scraped_at: 2026-09-02T14:53:32+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bf5c9310ab9da124f2b98dacfb0b70bcea8ec559653bc73304c130bfd1ec4bc7
---

| 错误码 | 描述 | 处理建议 |
| --- | --- | --- |
| 200 | 成功 | N/A |
| 400 | 参数错误 | 请参考返回信息，检查请求参数是否正确，并且需要确认商户服务器JDK版本高于1.8.211。如果检查正确，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 401 | 鉴权失败 | 请重新获取Authorization参数并填写在请求头中。 |
| 404 | 路径错误 | 请检查URL拼写是否正确。 |
| 405 | 权限错误 | 请检查是否在AGC网站上开启了钱包服务能力，请参见创建Wallet Kit服务。并检查申请的服务号（passTypeIdentifier）对应的卡券类型是否与调用的接口相对应。如果检查正确，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
| 429 | 服务不可用 | 请求接口次数超过调用量限额，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。 |
