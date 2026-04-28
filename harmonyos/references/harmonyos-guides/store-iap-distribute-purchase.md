---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-distribute-purchase
title: 购买数字商品
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 应用内分发数字商品 > 购买数字商品
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:483df9332f5c255cab2f8ff7c9107507c2239db9d70bbd126e2a7dcf3c4d2b90
---

## 场景介绍

在应用内数字商品的购买场景中，用户会以一次性付款的方式购买消耗型商品或非消耗型商品。

订阅是指用户在购买自动续期订阅商品后，可以在一段时间访问应用的增值功能或内容，并且会在订阅周期结束后自动续期购买下一期服务的能力。如果期间用户取消订阅，则订阅在当期结束后将不再自动续期。

接入数字商品服务购买能力前，您需在华为[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站[配置数字商品](store-iap-product.md)，录入商品ID和商品价格等信息。用户在开发者应用内发起购买时，使用数字商品服务的应用需要调用IAP Kit的[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口来拉起收银台，收银台会展示商品名称、商品价格等信息，用户可在收银台完成商品购买。

## 业务流程及开发步骤

### 消耗型/非消耗型商品

详细开发流程请参考[消耗型/非消耗型商品接入购买](iap-integrate-purchase.md)。

### 自动续期订阅商品

详细开发流程请参考[接入自动续期订阅](iap-integrate-subscription.md)。

### 非续期订阅商品

详细开发流程请参考[非续期订阅商品购买](iap-integrate-nonrenewable.md)。
