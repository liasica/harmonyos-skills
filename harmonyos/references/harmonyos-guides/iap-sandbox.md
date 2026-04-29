---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-sandbox
title: 沙盒测试
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 沙盒测试
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:720235b7da9d7c4ac2c512659b23b48b2c752c41b78c3ac00b4d60e1bea99c3a
---

沙盒测试允许开发者在接入华为应用内支付调测过程中对订单进行虚拟支付。

推荐您在提交数字商品审核前、即商品处于草稿/待提交状态下，使用沙盒测试进行调测。您可以通过设置沙盒测试账户，来模拟真实环境下数字商品的交易过程，在测试期间发现问题可以及时进行修复，这样确保了在商品上架生效以后可以提供给用户稳定流畅的商品购买体验。

说明

沙盒订单并非真实订单，无法在[开发者中心]->[我的报表]->[支付报表]中查询。

## 配置沙盒测试

* 添加测试账号

  在进行测试前，需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中的“用户与访问”中添加测试账号，这些测试账号必须是真实的华为账号。开发者在接入IAP Kit沙盒测试时，需要在测试设备上登录已添加的测试账号。添加沙盒测试账号步骤如下：

  1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。
  2. 左侧导航栏选择“沙盒测试 > 测试账号”，点击“新增”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Uk-ghyWrQTCS-PdGSrWLQA/zh-cn_image_0000002589245237.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=E94B8D756FC96B128635457511A9F4E802C9FEE4247EBA1E0E49B884C40B2525)
  3. 填写测试账号信息后，点击“确认”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/8uA8XIxBTTSENpzNPm8Dlg/zh-cn_image_0000002558765432.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=CF1ED2D1ADE479B724CD77068535AB44E000BEFA0C064168B4D751DF73F54E79)

  说明

  此配置需要5~10min才能生效。
* 构建debug签名的应用

  接入的应用必须是debug签名的应用。构建debug签名应用步骤如下：

  1.手动签名：您需要在AGC中[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[注册调试设备](../app/agc-help-add-device-0000002283189937.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)后，再[手动签名](ide-signing.md#section297715173233)。

  2.在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

## 沙盒测试能力未生效自检

如果配置的沙盒账号未生效，可参见[配置沙盒测试](iap-sandbox.md#配置沙盒测试)检查当前是否满足沙盒测试的两个条件：

* 是否已在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)添加测试账号。
* 应用是否是debug签名。

此外也可在应用中使用[isSandboxActivated](../harmonyos-references/iap-iap.md#iapissandboxactivated)接口来检查当前沙盒环境不可用的原因。

## 测试消耗型/非消耗型商品购买

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台，用户按照正常流程完成购买，但实际不会产生真实扣费。

* 沙盒环境下的购买流程与正式环境的购买流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP购买成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 沙盒环境下购买非消耗型商品，在确认发货之后可以再次测试购买。确认发货后该笔订单将无法通过[queryPurchases](../harmonyos-references/iap-iap.md#iapquerypurchases)接口查询返回。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示语，支付结果页也有沙盒环境的提示语，如下图所示。

说明

如果未显示截图的提示页面，表示本次交易未进入沙盒测试环境，继续测试会实际扣费，请参照[沙盒测试能力未生效自检](iap-sandbox.md#沙盒测试能力未生效自检)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/lVT5nBxtRUyjouwP7O-n8g/zh-cn_image_0000002558605776.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=533D89F17A020F6AC538CF1DCC534D995143B4FCF0E2EA97EB0CAAF5A92B66AE) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/vMXmS2CbSGWq47EP-YoEVw/zh-cn_image_0000002589325303.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=6458BFB0185FE01C5A14A7BC40B0930F0299A2F0A1C8B896BAEC674C55C0414F)

## 测试自动续期订阅商品

自动续期订阅商品的购买流程和消耗型/非消耗型商品的购买流程类似，但订阅还有其他细节场景，比如续订成功或失败，续订周期时长。为了帮助开发者快速测试应用的订阅场景，沙盒环境下的订阅续订时间会比正常情况更快，引入“时光机”概念，沙盒环境中的订阅换算时间为10秒/天。比如订阅周期为1周，商品将在首次购买成功70秒后发生续期。

* 沙盒环境下的订阅流程与正式环境的订阅流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP扣费成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 自动续期处理不需要完成真实扣款，IAP会直接返回成功。
* 在沙盒测试环境下，用户发起订阅首期会自动续期五次（累计共六期），后续需用户手动操作以恢复订阅。若同时涉及[促销场景](iap-subscription-functions.md#提供优惠)，系统将优先完成优惠周期内的自动续期，再继续进行六次续期，此场景下总续期次数为优惠周期数与六次续期之和。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示语，支付结果页也有沙盒环境的提示语，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/FGNvlPhfSmKW1H9OdkMvbg/zh-cn_image_0000002589245239.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=1302E7FA8591AF527D29D9611CC36E1868D4D624EB89EA6862BB2EBA44FAD3AF) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/lsM2VRQiTomT4RlVrWDgQQ/zh-cn_image_0000002558765434.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=E0C82C9D7E9AAFE9D3FE32FB2608253DBAEE93F14BD7E4C66798AC28B4379B24)

## 测试非续期订阅商品购买

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台，用户按照正常流程完成购买，但实际不会产生真实扣费。

* 沙盒环境下的购买流程与正式环境的购买流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP购买成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/7HC8F2RVTA66jnhx49qNOw/zh-cn_image_0000002558605778.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=188BFEA0DE1EA1C6D486DA3A554FC6D93D923B904B8422508E0A379055DC08DB) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/IoD_SUhLTCe8uNi1fdwL8g/zh-cn_image_0000002589325305.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=468D4DFAB1FD159D8CE44F6436E307C6F5D7502B84741305CA4AEC75D94C3974)

## 测试退款请求

开发者可以使用沙盒账号，针对在沙盒环境下购买商品产生的订单交易提交退款申请。该退款申请默认跳过退款审核和款项原路退回流程（沙盒环境下不真实扣费），IAP服务器会在沙盒环境中默认自动同意退款申请，同时给开发者服务器发送退款成功事件通知，以便开发者在收到退款事件通知后，测试应用内权益回收等场景。

具体操作步骤如下：

1. 在应用沙盒测试环境使用沙盒账号购买商品后，在测试设备上“手机设置 > 华为账号 > 付款与账单 > 购买记录”中会自动生成沙盒订单。
2. 点击待测试退款请求的沙盒订单，跳转至详情页面，点击“对订单有疑问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/-JsmmYQDQNOZ9rttPOFdNA/zh-cn_image_0000002589245241.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=0786BE82C8F11D191AF923C1C9F8FEF463CFF66835266D95FC596B6A6FD19BA7)
3. 在“对订单有疑问”页面，点击“申请退款”，选择任意的退款原因和填写任意必填资料后，提交退款申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/492akVDEQJ6wRXw0F7ohbg/zh-cn_image_0000002558765436.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=2B25DC0D16BA0F13DD734627F43C372566145B19CBB0D74C4EFFD1479E990DCF)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/ZplkNhSSQomLqlEsShwP_Q/zh-cn_image_0000002558605780.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=15918F011138D6ADF6037D706B4131306A3BD5800D4630F69F00AC6FC48FB9A9)
4. 退款申请提交后，IAP服务器默认跳过退款审核和款项原路退回流程，自动同意该笔退款申请，同时给开发者服务器发送退款成功事件通知（NotificationSubtype：REFUND\_TRANSACTION）。如果开发者配置了沙盒环境服务器地址，则该笔通知发送至沙盒环境服务器，详情请参考“[事件通知配置](../app/parameters-0000001931995692.md)”。
5. 开发者收到退款成功事件通知后，在测试环境中模拟应用内对该沙盒账号进行权益回收等操作，以实现测试目的。

## 清除沙盒账号的购买历史记录

开发者可以清除沙盒账号的购买历史记录，以便继续使用同一个沙盒账号进行测试。清除购买历史记录后，该测试账号在沙盒环境中产生的所有商品购买记录（包括自动续期订阅和消耗型/非消耗型商品）都将被删除，删除后该账号即可在沙盒环境中重新购买自动续期订阅商品、消耗型/非消耗型商品。清除购买历史记录后无法撤销操作。此操作不会影响生产环境数据。

清除沙盒账号购买历史记录的操作步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/Bmc6b4ppRUOqpo0rUL-auw/zh-cn_image_0000002589325307.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=3F05CF2FADF6506671BA7D2B83875A6F887D7A9C735CF864B487D592181802EB)
2. 左侧导航栏选择“沙盒测试 > 测试账号”，勾选对应的测试账号，点击右上角的“清除购买历史记录”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/J3-k_v3LQoW_ROsStNyeMA/zh-cn_image_0000002589245243.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=DECB47798CBBD4397B555301DEDED8B4E093B58C20FE16D33FBE81C84D62BE09)
3. 在出现的提示弹窗中，点击“确认”按钮，随后该账号在沙盒环境中产生的购买历史记录将被清除，此操作无法被撤销。如果该沙盒账号的购买次数较多，则清除其购买历史记录可能需要更长时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/4A-FKnRMTZKpXDPZS5Je2g/zh-cn_image_0000002558765438.png?HW-CC-KV=V1&HW-CC-Date=20260429T053840Z&HW-CC-Expire=86400&HW-CC-Sign=3FDB0A2CB0A5540BF4A695FB80E449F70D5CBBC9270186E7C1ED8D073B3025E4)

## 测试商品购买失败场景

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台。如果当前应用的“中断此测试账号的购买流程”配置项已配置，则用户将会在订单确认购买后被拦截。开发者可以测试该场景下应用的错误处理流程。具体模拟购买失败操作步骤如下：

1. 开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置“[中断此测试账号的购买流程](../app/agc-help-testaccount-0000001146438651.md#section9546175114555)”。

   说明

   当开发者在AppGallery Connect中更改了“中断此测试账号的购买流程”配置，需要等待3~5分钟后可尝试进行商品购买以触发数据刷新。
2. 用户选择购买消耗型/非消耗型/非续期订阅型/自动续期订阅型商品，按照正常流程进行拉起收银台下单。
3. 当用户确认购买后将会收到“服务暂不可用，请稍后重试”的错误提示，而开发者应用将会收到“[1001860056 用户交易被拒绝](../harmonyos-references/iap-error-code.md#section1001860056-用户交易被拒绝)”的错误。

   说明

   若购买结果与预期不一致，可尝试等待1分钟后继续购买。

## 测试自动续期订阅型商品续期失败场景

在满足沙盒测试条件下，当沙盒用户已购买自动续期订阅型商品，则开发者可以在App Gallery Connect中配置“中断此测试账号的购买流程”，模拟沙盒用户续期失败的场景。当沙盒用户持续地续期失败后订阅将会过期，IAP服务器将会向开发者服务器发送用户订阅过期的通知，开发者在收到订阅过期事件通知后，可测试应用内权益回收等场景。

具体操作步骤如下：

1. 沙盒用户按照正常流程购买自动续期订阅型商品。
2. 开发者在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置“[中断此测试账号的购买流程](../app/agc-help-testaccount-0000001146438651.md#section9546175114555)”。

   说明

   当开发者在AppGallery Connect中更改了“中断此测试账号的购买流程”配置，需要等待3~5分钟后可尝试进行商品购买以触发数据刷新。
3. 在测试设备上“系统设置-->华为账号->付款与账单->订阅->订阅详情”，预期会出现用户订阅续期异常的提示。
