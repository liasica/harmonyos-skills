---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-digital-cny-pay-preparations
title: （可选）数字人民币接入准备
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 开发准备 > （可选）数字人民币接入准备
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:29+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a7ae9e6818a5aee44ae4d1b9ef7e0297628b09b80e3019c67859164e5392b273
---

如不接入数字人民币支付能力或已完成运营机构或受理服务机构商户入网并获取了商户号和APPID，可跳过该步骤。

数字人民币支付仅支持通过运营机构或受理服务机构申请的商户接入，在开发前需要先完成商户入网（可拨打数字人民币客服热线956196根据指引完成商户入网）。

商户入网后，数字人民币的运营机构会分配对应的商户号和APPID，商户号和APPID是[开放API接口](../harmonyos-references/payment-ecnypaymentservice.md)请求的必要入参。

## 应用配置

在构建的开发者应用/元服务“entry/src/main/module.json5”文件中添加钱包schemes配置信息，配置内容示例如下：

```
1. {
2. "module": {
3. "querySchemes": [
4. "wallet"
5. ]
6. }
7. }
```
