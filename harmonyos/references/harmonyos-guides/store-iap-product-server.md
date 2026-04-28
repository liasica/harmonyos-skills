---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-product-server
title: 通过Server API配置数字商品
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 配置数字商品 > 通过Server API配置数字商品
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4013e6e511eb0822ccb044c2778b9feb5b173b655fdd14e7db464ef37958c77c
---

您也可以通过[PMS](../AppGallery-connect-References/agcapi-pmsapi-0000001162548121.md)（Product Management System）接口，对应用内数字商品的销售完成商品创建、查询、更新、管理促销活动等操作，并实现全球本地化定价。

基本的开发流程如下：

* [获取AppGallery Connect服务端授权](../AppGallery-connect-Guides/agcapi-getstarted-0000001111845114.md)：通过API客户端方式或者OAuth客户端方式获取服务端授权。
* [创建商品](../AppGallery-connect-Guides/agcapi-pms-add_product-0000001115868326.md)：包括商品的单个和批量方式的创建，您还可以参考《HarmonyOS NEXT 应用服务》中[管理数字商品](../app/digital-products-manage-0000001959074881.md)的相关内容基于AppGallery Connect网站进行商品管理的相关操作。
* [查询与更新商品](../AppGallery-connect-Guides/agcapi-pms-manage_product-0000001162468125.md)：商品创建后可以查询和更新商品信息。
* [管理商品状态](../AppGallery-connect-Guides/agcapi-pms-manage_productstatus-0000001162548101.md)：激活与去激活商品。激活后商品生效，将开放商品的购买。去激活后商品失效，将禁用商品的购买，如有进行中的优惠活动将立即结束。针对订阅类商品客户端用户原已生效的订阅仍然有效，建议开发者维持订阅服务到已生效订阅有效期截止。
* [管理商品促销信息](../AppGallery-connect-Guides/agcapi-pms-manage_product_prom-0000001116028236.md)：针对订阅类和非订阅类商品可以创建、更新和查询商品促销信息，定义促销的时间段，适用国家/地区，以及促销价格。
