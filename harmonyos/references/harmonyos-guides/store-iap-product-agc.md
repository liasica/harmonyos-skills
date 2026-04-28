---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-product-agc
title: 通过AppGallery Connect配置数字商品
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 配置数字商品 > 通过AppGallery Connect配置数字商品
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5a9ab05391f082389683245e12bad706dd9d399959dcc463f3a5c5730e549d1b
---

您可以通过华为数字商品管理系统将您的数字商品信息托管在华为侧，方便您的商品价格国际化管理，助力您的应用进行全球化推广。开发者需要在AppGallery Connect中提前录入商品信息（包括商品ID、商品类型、不同国家的商品价格、商品名称等），在客户端调用购买接口时，只需传入此处配置的商品ID和商品类型，系统会根据用户当前的账号服务地展示对应国家/地区的商品信息（包括商品价格、商品名称等），而无需开发者自行管理商品价格。

* 如果新增非订阅类数字商品，请参见[消耗型/非消耗型/非续期订阅商品](../app/non-subscription-0000001959074885.md)。
* 如果新增订阅类数字商品，请参见[自动续期订阅商品](../app/non-subscription-0000001958955109.md)。
* 如果为数字商品设置促销，请参见[设置促销价格](../app/set-0000001931995712.md)。

注意

在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)完成商品配置后，AppGallery Connect不会跟随汇率实时刷新商品价格，开发者需要定期[手动刷新价格](../app/single-0000001931995708.md)，在商品的价格编辑页面点击刷新并保存，即可根据当时的汇率刷新商品价格。
