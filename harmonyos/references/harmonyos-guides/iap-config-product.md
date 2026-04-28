---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-config-product
title: 配置商品信息
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 开发准备 > 配置商品信息
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:108eb2c7baacbf0203dd1f8fdbfe4918b6cb660686c992473967a6633b001492
---

在接入商品购买前，开发者需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中录入商品信息（包括商品ID、商品类型、不同国家/地区的商品价格、商品名称等）。在客户端调用购买接口时，只需传入此处配置的商品ID和商品类型，IAP Kit会根据用户当前的账号服务地自动展示对应国家/地区的商品信息（包括商品价格、商品名称等），无需开发者处理因账号所在服务地变动带来的商品价格适配问题。

## 配置消耗型/非消耗型/非续期订阅商品

* 如新增商品，请参见[消耗型/非消耗型/非续期订阅商品](../app/non-subscription-0000001959074885.md)。
* 如为消耗型/非消耗型/非续期订阅商品设置优惠促销（自定义人群促销），具体操作请参见[设置促销价格](../app/promotion-non-subscription-0000001931836332.md#section1429175616582)。
* 如需修改商品配置（商品名称、商品价格等），具体操作请参见[修改单个商品-非自动续期订阅商品](../app/revise-non-subscription-0000001931836328.md)。

## 配置自动续期订阅商品

* 如新增商品，请先[新增订阅组](../app/non-subscription-0000001958955109.md#section37862471018)，然后在创建[自动续期订阅商品](../app/non-subscription-0000001958955109.md)时指定商品所在的订阅组。
* 如为自动续期订阅商品设置促销，包含[推介促销](iap-subscription-functions.md#提供优惠)（新用户促销）、[优惠促销](iap-subscription-functions.md#提供优惠)（自定义人群促销）和[挽留促销](iap-subscription-functions.md#提供优惠)（退订挽留促销，**即将开放**），具体操作请参见[设置促销价格](../app/promotion-renewal-0000001959074897.md#section128611895910)。
* 如需修改商品配置（商品名称、商品价格等），具体操作请参见[修改单个商品-自动续期订阅商品](../app/revise-renewal-0000001959074893.md)。

说明

在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)完成商品配置后，[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)不会跟随汇率实时刷新商品价格，需要开发者定期手动刷新价格，具体请参见[修改单个商品](../app/single-0000001931995708.md)。
