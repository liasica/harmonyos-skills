---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-sandbox
title: 沙盒测试
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 沙盒测试
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8dffebf77eb5d75d08039a282790c081e9be0921aa27e8d7855e538bb909ed5f
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

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/Kew767u6TaeRUxqaPurlSw/zh-cn_image_0000002583438977.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=647DA04CC2B4D4E19590AB3F1687FFDD1606F315F01ED1D89BCF7E9D3C97E486)
  3. 填写测试账号信息后，点击“确认”。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/rH-xER7CQWOqPR-K41kS4A/zh-cn_image_0000002552958932.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=548E6B15641BC782CA7DC170F0124C6D256EEEA3B00748480FB10A7DCFDA218E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/Rj2ULv45TnC7xuxC_mT_4Q/zh-cn_image_0000002583478933.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=9BB3B510A93AE1B8916F19A442F22D7510F5FCF52D1F0689BF5F5334834E58FA) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/efiDjXyVTIeb8kK4drVg3A/zh-cn_image_0000002552799284.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=6837EC3E29849162638A2225A4E7E5C3CCD2688AB87282C7E10AA030411E8983)

## 测试自动续期订阅商品

自动续期订阅商品的购买流程和消耗型/非消耗型商品的购买流程类似，但订阅还有其他细节场景，比如续订成功或失败，续订周期时长。为了帮助开发者快速测试应用的订阅场景，沙盒环境下的订阅续订时间会比正常情况更快，引入“时光机”概念，沙盒环境中的订阅换算时间为10秒/天。比如订阅周期为1周，商品将在首次购买成功70秒后发生续期。

* 沙盒环境下的订阅流程与正式环境的订阅流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP扣费成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 自动续期处理不需要完成真实扣款，IAP会直接返回成功。
* 在沙盒测试环境下，用户发起订阅首期会自动续期五次（累计共六期），后续需用户手动操作以恢复订阅。若同时涉及[促销场景](iap-subscription-functions.md#提供优惠)，系统将优先完成优惠周期内的自动续期，再继续进行六次续期，此场景下总续期次数为优惠周期数与六次续期之和。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示语，支付结果页也有沙盒环境的提示语，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/OlBIrRe8TweIAsmHiCTZQQ/zh-cn_image_0000002583438979.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=8530ECAE4B9831AE4D839051036A510DF9538B5C99A06BA4B5F60F8CB2B59AF1) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/yx0nGuwHTaOZXp3_ZUvwyg/zh-cn_image_0000002552958934.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=D6A4E5213859F694B0B4B6BBC096A26C60009ED4881519B6D928358833E40FE1)

## 测试非续期订阅商品购买

在满足沙盒测试条件下，开发者调用[createPurchase](../harmonyos-references/iap-iap.md#iapcreatepurchase)接口拉起收银台，用户按照正常流程完成购买，但实际不会产生真实扣费。

* 沙盒环境下的购买流程与正式环境的购买流程一致，仍需要完成绑定付款方式，但该过程不会真实扣费。
* IAP购买成功后的收据信息[PurchaseOrderPayload](../harmonyos-references/iap-data-model.md#purchaseorderpayload)中，会携带值为"SANDBOX"的environment字段，标识此次购买为沙盒测试的记录。
* 沙盒测试拉起收银台时，会在收银台展示沙盒测试提示，结果页也有沙盒环境的标志，如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/bUgtZg_7R3aDeDhVfp5zag/zh-cn_image_0000002583478935.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=D8EB558C326BCF54FA132C2FD79F933300564B50AAAD597D30DDF16EDB1F4F8D) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/iQY6ZkMPQSGZ6bl2AH0z_A/zh-cn_image_0000002552799286.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=85734DBFB22078D075FABE257149A52E214083F181235C7276E7DD7D649091AB)

## 测试退款请求

开发者可以使用沙盒账号，针对在沙盒环境下购买商品产生的订单交易提交退款申请。该退款申请默认跳过退款审核和款项原路退回流程（沙盒环境下不真实扣费），IAP服务器会在沙盒环境中默认自动同意退款申请，同时给开发者服务器发送退款成功事件通知，以便开发者在收到退款事件通知后，测试应用内权益回收等场景。

具体操作步骤如下：

1. 在应用沙盒测试环境使用沙盒账号购买商品后，在测试设备上“手机设置 > 华为账号 > 付款与账单 > 购买记录”中会自动生成沙盒订单。
2. 点击待测试退款请求的沙盒订单，跳转至详情页面，点击“对订单有疑问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/gzwwjI64RGOP-53_Yyj8Zg/zh-cn_image_0000002583438981.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=EDF24B8248656FE8B3AA678DD3C0A4FFE77E0336873B4984F89AB08AE53272E8)
3. 在“对订单有疑问”页面，点击“申请退款”，选择任意的退款原因和填写任意必填资料后，提交退款申请。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/KlwDWk9kTJyJyjVQIV2LrA/zh-cn_image_0000002552958936.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=58E6617466A5A7454A745D48D97021EB560785E96646FAD73E210A51860D84BD)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/4HJdMSd6T8-eTWhBF-CI1A/zh-cn_image_0000002583478937.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=95A51F28733DD2EBFCD3EB65B8862F4A368D1752198F08E9D859AC818F9AEECD)
4. 退款申请提交后，IAP服务器默认跳过退款审核和款项原路退回流程，自动同意该笔退款申请，同时给开发者服务器发送退款成功事件通知（NotificationSubtype：REFUND\_TRANSACTION）。如果开发者配置了沙盒环境服务器地址，则该笔通知发送至沙盒环境服务器，详情请参考“[事件通知配置](../app/parameters-0000001931995692.md)”。
5. 开发者收到退款成功事件通知后，在测试环境中模拟应用内对该沙盒账号进行权益回收等操作，以实现测试目的。

## 清除沙盒账号的购买历史记录

开发者可以清除沙盒账号的购买历史记录，以便继续使用同一个沙盒账号进行测试。清除购买历史记录后，该测试账号在沙盒环境中产生的所有商品购买记录（包括自动续期订阅和消耗型/非消耗型商品）都将被删除，删除后该账号即可在沙盒环境中重新购买自动续期订阅商品、消耗型/非消耗型商品。清除购买历史记录后无法撤销操作。此操作不会影响生产环境数据。

清除沙盒账号购买历史记录的操作步骤如下：

1. 登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“用户与访问”。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/Inc8gO9HRaeoc-70mDWb7g/zh-cn_image_0000002552799288.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=6899A296E80C72A198655DFFBCCD9D7F839D1B2D0AD6E9AC63409D6061B67970)
2. 左侧导航栏选择“沙盒测试 > 测试账号”，勾选对应的测试账号，点击右上角的“清除购买历史记录”按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/P4_WMVJLR8yk1RqYPp9SRA/zh-cn_image_0000002583438983.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=7809187EDE11487851C03CE8EE5030AA1C59448F69F6BA7E42C6B3AA2998AF45)
3. 在出现的提示弹窗中，点击“确认”按钮，随后该账号在沙盒环境中产生的购买历史记录将被清除，此操作无法被撤销。如果该沙盒账号的购买次数较多，则清除其购买历史记录可能需要更长时间。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/j51PMhUYQxmwXdr2rA2ZCg/zh-cn_image_0000002552958938.png?HW-CC-KV=V1&HW-CC-Date=20260427T234927Z&HW-CC-Expire=86400&HW-CC-Sign=8E4475331B76AAE6C14B0082B0C77C1931E8F3176DF6F6F0762D38B2874DF6A5)

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
