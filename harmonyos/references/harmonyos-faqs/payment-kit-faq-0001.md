---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/payment-kit-faq-0001
title: 收银台支付报错排查
breadcrumb: FAQ > 应用服务开发 > 华为支付服务（Payment Kit） > 常见问题 > 收银台支付报错排查
category: harmonyos-faqs
scraped_at: 2026-10-23T07:14:28+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:42e527bbc11d565007560566fb78da6b3cce351fc86ff6df995a2da74353a8fb
---

**Q：拉起华为收银台进行支付，支付失败，提示：服务暂不可用，请稍后重试，如何解决？**

**A**：可以从如下几个方面进行排查：

1. 账号账户是否被冻结，如被冻结需要按照此路径：“钱包”App-“我的”-“华为支付”-“账户与安全”-“证件影像”，上传身份证解冻。
2. 检查[orderStr](../harmonyos-references/payment-model.md#orderstr)入参格式、字段值（如merc\_no、app\_id、auth\_id等）是否正确，auth\_id是否归属于merc\_no（即公私钥对以及商户是否匹配）。
3. 应用是否在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)注册，本地使用的调试签名证书是否是从HarmonyOS 开发者中心上面下载的。
4. 订单信息[orderStr](../harmonyos-references/payment-model.md#orderstr)传入的app\_id是否与[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console/#/home/)上面创建应用的APPID一致（如orderStr不传app\_id字段时可正常拉起收银台，则需仔细检查传递时的app\_id是否正确）。
