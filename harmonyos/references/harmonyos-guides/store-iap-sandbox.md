---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-sandbox
title: 测试数字商品服务
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 测试数字商品服务
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:12+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:d8cba6163517b491c698e2bee8531c3e8e86725ec53dc9967f0d4c4cf7ae3bcb
---

沙盒测试允许开发者在接入数字商品服务的调测过程中无需真实付款即可完成数字商品的购买等相关测试。

**说明** 

沙盒订单并非真实订单，无法在[开发者中心]->[我的报表]->[支付报表]中查询。

## 配置沙盒测试

* 设置测试账号

  在进行测试前，需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中的“用户与访问”中添加测试账号，这些测试账号都是真实的华为账号。开发者在HarmonyOS上接入IAP沙盒测试时，需要在测试设备上登录已配置的测试账号。添加沙盒测试账号步骤如下：

  1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。
  2. 左侧导航栏选择“沙盒测试 > 测试账号”，点击“新增”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/7xMu30AURqSQZkRpA9z7iQ/zh-cn_image_0000002788307894.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=B19B0C1C6AD34AFB4DFCA9F27B98072BA862A32C9212620C6DD18D55A5D89320)
  3. 填写测试账号信息后，点击“确认”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/2iMdeLzGSWaT9ZNRMs5Seg/zh-cn_image_0000002817427257.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CCA60408FAF38EF43C1B6994A34982A2A1F2192FB4CF93F51BAA9B2F6481850)

  **说明** 

  沙盒测试账号必须填写已注册、真实的华为账号。添加完成之后需要5~10min才能生效。使用时请检查当前的账号是否支持沙盒测试。
* 构建debug签名的应用

  接入的应用必须是debug签名的应用。构建debug签名应用步骤如下：

  1. 手动签名：开发者需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[注册调试设备](../app/agc-help-add-device-0000002283189937.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)后，再[手动签名](ide-signing-manual.md)。
  2. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

## 沙盒测试能力未生效自检

如果配置的沙盒账号未生效，可参见[配置沙盒测试](store-iap-sandbox.md#配置沙盒测试)检查当前是否满足沙盒测试的两个条件：

* 是否已在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)添加测试账号。
* 应用是否是debug签名。

此外也可在应用中使用[isSandboxActivated](../harmonyos-references/iap-iap.md#iapissandboxactivated)接口来检查当前沙盒环境不可用的原因。

## 测试消耗/非消耗型商品购买

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台，跳过实际支付环节，直接购买成功。

* 沙盒环境下的购买流程与正式环境的购买流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* 购买成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 沙盒环境下购买非消耗型商品，购买之后可以确认发货以完成购买，之后可以再次购买，以方便测试。

  **说明** 

  正式环境下，非消耗型商品仅允许用户购买一次，不能重复购买。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

**说明** 

如果未显示截图的提示页面，表示本次交易未进入沙盒测试环境，继续测试会实际扣费，请检查当前是否满足沙盒测试的两个条件。开发者也可在应用中使用[isSandboxActivated](../harmonyos-references/iap-iap.md#iapissandboxactivated)接口来检查当前沙盒环境不可用的原因。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/VBIqoiG_S6W2seIuL863Mw/zh-cn_image_0000002788467838.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=0B4933B8BE1C83BA9019660515CFF838ABB0F4F3FB6BFA4C98960C42B2E0E4F2)

## 测试自动续期订阅商品

自动续期订阅商品的购买流程和消耗型/非消耗型商品的购买流程类似，但订阅还有其他细节场景，比如续订成功或失败，续订周期时长。为了帮助开发者快速测试应用的订阅场景，沙盒环境下的订阅续订时间会比正常情况更快，引入“**时光机**”概念，沙盒环境中的订阅换算时间为10秒/天。比如订阅周期为1周，商品将在首次购买成功70秒后发生续期。

* 沙盒环境下的订阅流程与正式环境的订阅流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP扣费成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 自动续期处理不需要完成真实扣款，IAP会直接返回成功。
* 在沙盒测试环境下，订阅首期由用户发起后会自动续期五次（累计共六期），后续需用户手动操作以恢复订阅；若同时涉及[促销场景](iap-subscription-functions.md#提供优惠)，系统将优先完成优惠周期内的自动续期，再继续进行六次续期，此场景下总续期次数为优惠周期数与六次续期之和。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ZD81DjFrQnW1rblfmGdeGA/zh-cn_image_0000002817507327.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=A68C9F6685181E988F3B0B1D349C697DA9588AA7CFBCD978F6E3A40A1747F694)

## 测试非续期订阅商品购买

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台，用户按照正常流程完成购买，但实际不会产生真实扣费。

* 沙盒环境下的购买流程与正式环境的购买流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP购买成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/EogXFPU8ST66Wk-l-Zv8tA/zh-cn_image_0000002788307896.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=EBA797BFB203462126640767ED21DD4377FCAEA0EC2C1D02200ED9DB6B010A67)

## 清除沙盒账号的购买历史记录

开发者可以清除沙盒账号的购买历史记录，以便继续使用同一个沙盒账号进行测试。清除购买历史记录后，该测试账号在沙盒环境中产生的所有商品购买记录（包括自动续期订阅和消耗型/非消耗型商品）都将被删除，删除后该账号即可在沙盒环境中重新购买自动续期订阅商品、消耗型/非消耗型商品。清除购买历史记录后无法撤销操作。此操作不会影响生产环境数据。

清除沙盒账号购买历史记录的操作步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ie62rDPXTCOEXHs9Rk6mhQ/zh-cn_image_0000002817427259.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=A87457DEF92D88C0E07F73BA52481EA67F6F6C25728D833EE6712E70287F6028)
2. 左侧导航栏选择“沙盒测试 > 测试账号”，勾选对应的测试账号，点击右上角的“清除购买历史记录”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/CKCRbjVPQXmlWGOZXvuOjw/zh-cn_image_0000002788467840.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=BB312E02A20003943A93731F338127D7D020548D4CA164447031BD6940701041)
3. 在出现的提示弹窗中，点击“确认”按钮，随后该账号在沙盒环境中产生的购买历史记录将被清除，此操作无法被撤销。如果该沙盒账号的购买次数较多，则清除其购买历史记录可能需要更长时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/5J7n6R5wTvGZmX73VVcZXg/zh-cn_image_0000002817507329.png?HW-CC-KV=V1&HW-CC-Date=20261114T004629Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4BD3E91E1FE4C245AE4BE7499FECBD6E8CDDFE29D227AF20C6F2FEBF6764391)
