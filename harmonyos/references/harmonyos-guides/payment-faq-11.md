---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-faq-11
title: 收银台报错“服务暂不可用，请稍后重试”？
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit常见问题 > 收银台报错“服务暂不可用，请稍后重试”？
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2bf9bb823c337ec9ed44218fb46496f3bd95d8dea0516ba29fb83642fd109de8
---

1. 检查网络是否正常。
2. 检查[orderStr](../harmonyos-references/payment-model.md#orderstr)入参格式、字段值（如merc\_no、app\_id、auth\_id等）是否正确，auth\_id是否归属于merc\_no(即公私钥对以及商户是否匹配）。
3. 应用是否在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上面注册了，本地使用的调试签名证书是否是从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上面下载的。
4. 订单信息[orderStr](../harmonyos-references/payment-model.md#orderstr)传入的app\_id 是否与[AppGallery Connect上面创建应用的APPID](../app/agc-help-appinfo-0000001100014694.md)一致（如orderStr不传app\_id字段时可正常拉起收银台，则需仔细检查传递时的app\_id是否正确）。
5. 使用“hdc hilog > 日志路径”抓取运行日志，参考[错误码](../harmonyos-references/payment-error-code.md)及日志来分析具体的报错异常。
