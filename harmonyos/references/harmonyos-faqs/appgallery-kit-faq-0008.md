---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-faq-0008
title: 应用内支付商品类型与ID配置常见问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 常见问题 > 应用内支付商品类型与ID配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-23T07:14:34+08:00
doc_updated_at: 2026-10-22
content_hash: sha256:43b4d0344d7d15f7abf71cd75790b7a1c6066262e52c6e9d12780ddebfbac7ab
---

**Q：由于想更换商品类型从消耗型商品更改为非续期订阅商品，发现新建商品后不能复用之前的商品ID，在后台能否直接更改商品类型？**

**A**：应用后台不支持更换商品类型，同时商品ID和商品类型创建成功后是不能修改的，只能[重新创建应用内商品](../doccenter-distribution/create-digital-products-0000001958955105.md)。但是消耗型商品和非续期订阅商品IAP交互流程是一样的，非必要可以不进行更改商品类型。

**Q：HarmonyOS 开发者中心上商品管理的审核信息中，应用内截图指的是什么？**

**A**：商品在应用内部页面的截图。

**Q：数字商品未上架怎么测试？**

**A**：通过沙盒环境[测试数字商品服务](../harmonyos-guides/store-iap-sandbox.md)。

**Q：HarmonyOS 开发者中心上商品管理的审核信息中应用内截图是否是每一个计费点都需要使用不同的截图？**

**A**：不需要，同一个模块下的计费点可以使用同一个截图，如：同一商品列表页下的商品可以统一使用商品列表页面，只要能看到商品位置即可。

**Q：体验卡或月卡等不需要自动续期的有效期商品应该创建为什么类型的商品？**

**A**：应创建为非续期订阅商品。非续期订阅商品的定义为：用户购买后在一段时间内允许访问增值功能或内容，周期结束后禁止访问，除非再次购买。

**Q：非续期订阅商品在HarmonyOS 开发者中心商品配置中无法设置使用时长，如何管理有效期？**

**A**：非续期订阅商品的使用时长和有效期由开发者根据自身业务逻辑管理，HarmonyOS 开发者中心商品配置中不提供使用时长的设置项。

**Q：如何查询用户购买的商品信息？**

**A**：调用[iap.queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)接口查询已购商品的订单信息，开发者根据返回的商品信息自行管理使用时长和有效期。

**Q：消耗型商品和非续期订阅商品的区别是什么？**

**A**：消耗型商品使用一次后即消耗掉，随使用减少，如游戏货币、游戏道具等；非续期订阅商品是用户购买后在一段时间内允许访问增值功能或内容，如视频一个月会员。具体区别可以参考[IAP简介](../harmonyos-guides/iap-introduction.md)。
