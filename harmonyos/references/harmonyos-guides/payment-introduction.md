---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-introduction
title: Payment Kit简介
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > Payment Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:50:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:422aafe5325498ab1a10c38aeedb62063254da83176128a9ca6133c132079a66
---

Payment Kit（鸿蒙支付服务）提供了方便、安全和快捷的支付方式，开发者在开发的商户应用/元服务中接入支付服务便捷且快速。

商户应用/元服务接入Payment Kit后，可在商户的应用/元服务内通过拉起华为支付收银台来完成订单的支付并展示支付结果以及完成用户对**实体商品或服务**（例如酒店服务、出行服务、充值缴费服务等）的购买。

Payment Kit还提供了用户身份验证服务，包括实名信息验证、实名信息授权和人脸核身实人验证以及数字人民币支付能力，商户通过接入数字人民币支付能力，可在商户的应用/元服务调用开放API接口，拉起数字人民币收银台来完成订单支付。

除此之外，Payment Kit也提供了营销服务。通过集成营销服务组件，用户可以在组件内领取平台券，在支付时可选择使用平台券。

## 场景介绍

* 商城购物

  用户在商户的应用/元服务选购完不同的商品后，可以直接在商户的应用/元服务里完成下单和支付。

  接入场景：[商户基础支付场景](payment-payment-process.md)、[平台类商户合单支付场景](payment-partner-combined.md)、[通用收银台支付相关场景](payment-common-pay-introduction.md)。
* 免密代扣

  用户在商户APP应用/元服务选购完商品或主动点击商户提供的签约选项后，商户的应用/元服务可拉起华为支付签约收银台，用户完成签约后，后续再次购买商品时，商户可以直接发起代扣，减少用户拉起收银台、输入支付密码等相关操作。

  接入场景：[支付并签约场景](payment-pay-and-sign.md)、[签约代扣场景](payment-withhold-process.md)。
* 数字人民币支付

  用户在商户APP应用/元服务进行话费充值，选好充值金额后发起支付，商户的应用/元服务通过拉起数字人民币收银台完成订单支付以及话费充值的操作。

  接入场景：[数字人民币支付场景](payment-digital-cny-pay.md)。
* 用户身份验证服务

  政务、金融、医疗等类型应用/元服务在用户进行登录、预约等操作时需要核对用户信息，或核对用户是否本人。

  接入场景：[实名信息验证/授权场景](payment-real-name-verification.md)、[人脸核身实人验证场景](payment-real-name-face-verification.md)。
* 营销服务

  针对平台券，营销服务提供领券和选券组件。当元服务集成此组件后，用户可以在组件内查看可参加的平台券活动，在下单时可以选择已经领取的可用平台券。

  接入场景：[领券场景](payment-promotion-claim-coupon.md)、[选券场景](payment-promotion-select-coupon.md)。

## 基本概念

**数字人民币**：数字人民币是中国人民银行提供的通用账户型法定数字货币，由指定合格的运营机构参与运营，具有账户和价值模式。以广义账户体系为基础，与传统银行账户体系融合互通，支持可控匿名，具有法偿性。

**通用收银台**： 为鸿蒙生态下的应用和元服务提供收款能力的收银台。

**用户身份验证服务**：是鸿蒙支付服务针对元服务和应用开发提供的开放能力。实名信息验证/授权场景，是基于用户授权同意，验证输入的姓名及证件号是否与鸿蒙支付服务预留的信息一致或快速获取用户在鸿蒙支付服务预留且认证过的姓名及证件号。人脸核身实人验证场景，是基于用户授权同意，通过人脸识别比对等，验证用户所提供的信息是否准确且为本人操作。

## 商户模型与支付能力

如接入数字人民币支付场景，需在运营机构或受理服务机构完成商户入网（[参见这里](payment-digital-cny-pay-preparations.md)）。

Payment Kit当前提供三种接入商户模型：**商户**（下文统称为直连商户）、**平台类商户**、**服务商**。开发者需要根据实际业务模式选择适用的合作身份。商户模型详细内容请参见[接入模式](../pay-docs/hwzf-hezuoshenfen-0000001725918617.md)。

| 商户模型 | 说明 |
| --- | --- |
| **直连商户** | 直接与华为支付对接，使用鸿蒙支付服务的经营主体。 |
| **平台类商户** | 为商户交易场景提供支付、结算解决方案，主要面向对商品交易或服务进行线上撮合和管理的平台。  **子商户**：平台上入驻华为支付开展交易的商家，与平台类商户关联。 |
| **服务商** | 为商户提供开户申请、支付接入、技术开发等综合解决方案机构。  **特约商户**：服务商推荐在华为支付入网的商户，与服务商关联。 |

Payment Kit支持的支付能力如下：

| 支付能力 | 支持的商户 | 接入场景 | 描述 |
| --- | --- | --- | --- |
| **基础支付** | 直连商户、平台类商户、服务商 | [商户基础支付场景](payment-payment-process.md)  [通用收银台支付相关场景](payment-common-pay-introduction.md) | 用户选购商品后，商户通过接入基础支付完成用户订单的创建与支付。 |
| **合单支付** | 平台类商户 | [平台类商户合单支付场景](payment-partner-combined.md) | 通过合单支付，商户可将不同商户的一个或多个订单合并到同一个订单完成支付。 |
| **支付并签约** | 直连商户、服务商 | [支付并签约场景](payment-pay-and-sign.md) | 用户支付完成后可与商户签订协议，完成后续相关业务自动扣款。 |
| **签约代扣** | 直连商户、服务商 | [签约代扣场景](payment-withhold-process.md) | 商户可主动发起与用户签订相关协议，完成相关业务自动扣款（如水电费预缴，自动充值代扣等），简化用户操作流程。 |
| **数字人民币支付** | 运营机构或受理服务机构入网的商户 | [数字人民币支付场景](payment-digital-cny-pay.md) | 在运营机构或受理服务机构入网的商户可通过接入数字人民币来完成如用户话费充值缴费等相关支付操作。 |

支付能力之间的差异：

* 基础支付与合单支付主要差异在于基础支付一次支付仅支持支付单个订单，合单支付一次支付可以支持平台类商户多个不同子商户的订单。
* 基础支付及合单支付不涉及签约、支付并签约及签约代扣涉及用户及商户协议签订场景。
* 支付并签约与签约代扣差异在于签约时是否需要完成支付操作。
* 数字人民币支付开发准备与其它支付能力有所差异，完成[数字人民币接入准备](payment-digital-cny-pay-preparations.md)即可根据接入场景接入开发。

华为支付接入顺序如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/PbLttOjqSBiy5HneBSe7kg/zh-cn_image_0000002552799420.png?HW-CC-KV=V1&HW-CC-Date=20260427T235003Z&HW-CC-Expire=86400&HW-CC-Sign=372F0BA04EA5436D49B2DF5F1A09941C0DB5648F47C18135EF0A006A87BEF7D9)

[数字人民币支付](payment-digital-cny-pay.md)接入顺序如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/FM4sctXSQW2QhO9c-oMh3g/zh-cn_image_0000002583439115.png?HW-CC-KV=V1&HW-CC-Date=20260427T235003Z&HW-CC-Expire=86400&HW-CC-Sign=354979EE6C3AFDA23AE6AB4FE4D99E93122C7A195BC45068A853505771C9467B)

通用收银台[混合支付场景](payment-common-pay-mix.md)接入顺序如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/p6rcj6ESR5mWQhvCxx3ayw/zh-cn_image_0000002552959070.png?HW-CC-KV=V1&HW-CC-Date=20260427T235003Z&HW-CC-Expire=86400&HW-CC-Sign=2AFD3FD5A6B4A353D32DBD9E3C0F6E9E6F81C0B2D6F3490334C89FFF9A81A33C)

通用收银台[纯外部支付场景](payment-common-pay-external.md)接入顺序如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/vqogyvEFSW2SSbwr2q53PA/zh-cn_image_0000002583479071.png?HW-CC-KV=V1&HW-CC-Date=20260427T235003Z&HW-CC-Expire=86400&HW-CC-Sign=A568CD825C40EBE34C33830964FA36B76A7014008EAA6E0EE5AFB2BECB53A7BA)

用户身份验证服务、人脸核身实人验证接入顺序如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/l09gjk6hRMKkLyYdrdfr_A/zh-cn_image_0000002552799422.png?HW-CC-KV=V1&HW-CC-Date=20260427T235003Z&HW-CC-Expire=86400&HW-CC-Sign=5E50969095C16982831601A22C9230BAAF081446FC1AE1E5579ECEE42E7A2E3D)

## 约束与限制

Payment Kit的能力只支持实物商品和服务（酒店服务、出行服务、充值缴费服务）的支付，暂不支持如电子虚拟人物形象，游戏中的关卡、货币及道具等虚拟商品的支付。

虚拟商品的支付可接入[IAP应用内支付服务](iap-introduction.md)。

### 支持的设备

| 能力/服务 | 支持设备 |
| --- | --- |
| 基础支付 | Phone、Tablet、PC/2in1 |
| 平台类商户合单支付 | Phone、Tablet、PC/2in1 |
| 免密支付 | Phone、Tablet、PC/2in1 |
| 数字人民币支付 | Phone、Tablet、PC/2in1 |
| 通用收银台 | Phone、Tablet、PC/2in1 |
| 引导用户绑卡 | Phone、Tablet、PC/2in1 |
| 用户身份验证服务 | Phone、Tablet |
| 营销组件 | Phone、Tablet、PC/2in1 |

### 支持的国家/地区

当前Payment Kit的能力仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

## 模拟器支持情况

本Kit暂不支持模拟器。
