---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-preparations
title: 接入流程
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 接入流程
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1aec3335fb3d4d0f0c4fd957f5da169cab587fefc182328c32deb7c610e1b1d1
---

1. **启用数字商品服务**

   请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行后续开发活动。在启动开发之前，需先[启用数字商品服务](store-iap-config-agc.md) ，打开相关服务API开关和配置服务参数，才能对数字商品相关的API进行调用。
2. **配置数字商品**

   开发者需要提前录入商品信息（包括商品ID、商品类型、不同国家的商品价格、商品名称等），在客户端调用购买接口时，只需传入已配置的商品ID和商品类型。当前支持[通过AppGallery Connect配置商品信息](store-iap-product-agc.md)和[通过Server API配置数字商品](store-iap-product-server.md) 。
3. **应用内分发数字商品**

   当前支持在开发者的应用内展示和[分发数字商品](store-iap-distribute-query.md)，在完成数字商品配置和接入数字商品购买能力后，当用户在开发者的应用内发起购买时，应用需要调用相关接口来拉起订单页面，展示商品名称、商品价格等信息，用户可在确认交易订单后完成商品购买。
4. **测试数字商品服务**

   当前支持开发者使用沙盒测试，在接入数字商品服务的调测过程中无需真实付款即可完成数字商品的购买等相关测试。在进行测试前，需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html#/)中的“用户与访问”中添加测试账号，这些测试账号都是真实的华为账号。开发者接入IAP沙盒测试时，需要在测试设备上登录已配置的测试账号。具体请参考“[测试数字商品服务](store-iap-sandbox.md)”章节。
