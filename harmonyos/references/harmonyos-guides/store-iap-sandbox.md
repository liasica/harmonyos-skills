---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-sandbox
title: 测试数字商品服务
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 测试数字商品服务
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:18+08:00
doc_updated_at: 2026-09-23
content_hash: sha256:f879f466806d5e151494a81532f35fe28a1ade1742cb2219c94d2e3f0e599973
---

沙盒测试允许开发者在接入数字商品服务的调测过程中无需真实付款即可完成数字商品的购买等相关测试。

**说明** 

沙盒订单并非真实订单，无法在[开发者中心]->[我的报表]->[支付报表]中查询。

## 配置沙盒测试

* 设置测试账号

  在进行测试前，需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中的“用户与访问”中添加测试账号，这些测试账号都是真实的华为账号。开发者在HarmonyOS上接入IAP沙盒测试时，需要在测试设备上登录已配置的测试账号。添加沙盒测试账号步骤如下：

  1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。
  2. 左侧导航栏选择“沙盒测试 > 测试账号”，点击“新增”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/MzNiTKNSS0Kulq1MiG3kKA/zh-cn_image_0000002792877876.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=5476B2131968FDD2081474193438D47ADF66F2010E88B8E461F319839B4C9898)
  3. 填写测试账号信息后，点击“确认”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/OyRjs7r8SjmODI0VZPKj1w/zh-cn_image_0000002821837783.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=7B82544590701496A83001340F14C9E59876168CC4CF99D22467BFF607F6C6A5)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/t6_LhtajT5W2GHsnoTib2Q/zh-cn_image_0000002821757785.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=79EDE50C7CDFCE511A905F4D688D086B5E44D65B0ECF96BA108154B841A6F014)

## 测试自动续期订阅商品

自动续期订阅商品的购买流程和消耗型/非消耗型商品的购买流程类似，但订阅还有其他细节场景，比如续订成功或失败，续订周期时长。为了帮助开发者快速测试应用的订阅场景，沙盒环境下的订阅续订时间会比正常情况更快，引入“**时光机**”概念，沙盒环境中的订阅换算时间为10秒/天。比如订阅周期为1周，商品将在首次购买成功70秒后发生续期。

* 沙盒环境下的订阅流程与正式环境的订阅流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP扣费成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 自动续期处理不需要完成真实扣款，IAP会直接返回成功。
* 在沙盒测试环境下，订阅首期由用户发起后会自动续期五次（累计共六期），后续需用户手动操作以恢复订阅；若同时涉及[促销场景](iap-subscription-functions.md#提供优惠)，系统将优先完成优惠周期内的自动续期，再继续进行六次续期，此场景下总续期次数为优惠周期数与六次续期之和。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/jLvQ7cAYTeOKQbTFkvTFaw/zh-cn_image_0000002793037848.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA906B1AF2C068FAB7275E757641508D765A2D9C560AA9973C5E518007EADD55)

## 测试非续期订阅商品购买

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台，用户按照正常流程完成购买，但实际不会产生真实扣费。

* 沙盒环境下的购买流程与正式环境的购买流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP购买成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/PELtcEDZSEmWg-bggo8NvQ/zh-cn_image_0000002792877878.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=5E58302DC9EAEDCE46734913041EE5B4834D202C654ED42B0F02D00124BA68C7)

## 清除沙盒账号的购买历史记录

开发者可以清除沙盒账号的购买历史记录，以便继续使用同一个沙盒账号进行测试。清除购买历史记录后，该测试账号在沙盒环境中产生的所有商品购买记录（包括自动续期订阅和消耗型/非消耗型商品）都将被删除，删除后该账号即可在沙盒环境中重新购买自动续期订阅商品、消耗型/非消耗型商品。清除购买历史记录后无法撤销操作。此操作不会影响生产环境数据。

清除沙盒账号购买历史记录的操作步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/C92iW_DXTNm3rmWDlZx5AQ/zh-cn_image_0000002821837785.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=1773DAA5AC2CD422D8AA36286EA62E849F1838205A9590AB4215DECC86A13AE8)
2. 左侧导航栏选择“沙盒测试 > 测试账号”，勾选对应的测试账号，点击右上角的“清除购买历史记录”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/MHSLnmBeT-G5gr-tATPbvA/zh-cn_image_0000002821757787.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=E631C014608286B45CCE479D52000508D718E935EA60D9EAE5F5152ACD564C0E)
3. 在出现的提示弹窗中，点击“确认”按钮，随后该账号在沙盒环境中产生的购买历史记录将被清除，此操作无法被撤销。如果该沙盒账号的购买次数较多，则清除其购买历史记录可能需要更长时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/8jqSfQNiTCmuOe2L3-wNFQ/zh-cn_image_0000002793037850.png?HW-CC-KV=V1&HW-CC-Date=20261121T011218Z&HW-CC-Expire=31536000000&HW-CC-Sign=EE4D2B47068DFED8413EB93462B944E4ABC56D59B80AE03B6A228C9382585EF6)
