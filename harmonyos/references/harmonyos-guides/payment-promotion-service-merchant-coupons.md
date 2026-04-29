---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-promotion-service-merchant-coupons
title: 商家券场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 运营工具 > 商家券场景
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:587223b0569a818e359d4872fae18252f9d312b58eca673b28c177eba078f986
---

## 场景介绍

商家券是华为支付为商户提供的电子优惠券解决方案，通过该产品实现商家优惠券创建、投放、领取、核销及券查询等管理操作，商家券优惠规则和玩法由商家自定义，商家可将自有营销体系的优惠券同步到华为服务分发平台流量（日日有礼、搜索、品牌专区、支付成功页等）和商家自有流量进行发放和运营。

有开发意愿的商户或者服务商可使用API接口完成商家券创建、发放、领取、核销、券查询等全链路操作。

支持商户模型：直连商户、平台类商户、服务商。

用户在华为钱包卡包可见的商家券样式（参考下图，商家自定义）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/YrfUkq-mQ_2z8s9JSF3rYQ/zh-cn_image_0000002589245405.png?HW-CC-KV=V1&HW-CC-Date=20260429T053934Z&HW-CC-Expire=86400&HW-CC-Sign=CDBE43C8CF4BC4D55CA2CBC3A2E10272E294A09A92E05ACACF545FFA582E0B70)

## 接入前置条件

1. 商家有营销系统以及具备开发能力且存在应用/元服务。
2. 商家在华为支付完成[商户入网](payment-merc-regist-apply.md)。

## 业务模式

### 支持的券类型

可支持满减券、折扣券和换购券三种优惠类型的商家券。

| 类型 | 说明 |
| --- | --- |
| 满减券 | 满X元减X元（例如：满10元减5元券），商户可在券的使用说明字段里向用户说明，券的适用商品情况（例如：全场商品适用，特价商品除外或XX品牌商品适用）。 |
| 折扣券 | 满X元享受X折（例如：满10元享5折），商户可在券的使用说明字段里向用户说明，券的适用商品情况（例如：全场商品适用，特价商品除外或XX品牌商品适用），包装出全场折扣券或者指定单品折扣券。 |
| 换购券 | 满X元换商品（例如：原价10元打车券，特价5元），商户可以用换购券包装出免费兑换券或减至券。在券的使用说明字段里向用户说明，券的适用商品情况（例如：XX品牌商品适用，不适用于XX商品）。 |

### 支持的券码类型

商家券Code码可支持随机Code和商户自定义Code两类。其中，商户自定义Code支持导入Code模式和发放时指定Code模式。

| **模式** | 说明 |
| --- | --- |
| 随机Code | 商家无需提前预上传券Code，在调用商家券发放接口时由华为支付随机生成券Code分配给商家券。 |
| 导入Code | 商家需预先向华为支付上传券Code，当券在发放时，华为支付自动从已导入的Code中随机取值（不能指定），派发给用户。该模式更多适用在华为支付平台流量场景（例如：华为支付精选权益页）中投放的商家券。 |
| 指定Code | 商家无需提前预上传券Code，在调用商家券发放接口中填入需给用户派发的Code信息。该模式更多适用在商家自有流量场景（例如：应用/元服务）中投放商家券。 |

### 支持的发放渠道

当前商家券支持的发放渠道有商家自有流量场景、平台流量场景。

| **场景** | 说明 |
| --- | --- |
| 商家自有流量 | 支持在应用/元服务中派发商家券。 |
| 平台流量 | 支持在日日有礼、搜索、品牌专区、支付成功页等场地中派发商家券。  **说明：** 对于品牌专区支持平台流量，需要开发者进行[配置](../service/intents-kit315-0000002505659156.md)。 |

### 支持的核销方式

线上应用/元服务核销。用户领取商家券后可通过卡包点击去使用，跳转至商家应用/元服务。商家查询到用户已领取的所有商家券信息，再根据商家优惠规则进行使用判断，用户使用商家券并支付完成后，商家调用核销接口将用户钱包卡包里的商家券状态标为已核销。

### 券插入钱包卡包、临期消息通知

用户领取商家券后，券会自动插入钱包卡包。券过期前，用户会收到商家券即将过期通知。

## 接入流程

| 步骤 | 说明 |
| --- | --- |
| [商户入网](payment-merc-regist-apply.md) | 在准备开发前，开发者需要在华为支付商户平台入网。商户入网成功后，需要为[商户号绑定AppID](payment-binding-appid-to-merc.md)。 |
| [准备证书](payment-certificates-config.md) | 商户成功登录商户平台后，须在证书管理中上传商户证书，上传完商户证书后商户方可进行交易，证书必须与商户号相匹配且是有效的。 |
| 商家券接入 | 根据[开发步骤](payment-promotion-service-merchant-coupons.md#开发步骤)完成商家券接入。 |

## 业务流程

### 华为平台随机Code发放场景

如果系统对商家券Code无特殊要求，则使用随机Code模式（HWPAY\_MODE），华为在代发商家券时，随机生成券码给用户发券，发券成功后会回调通知本次发券所使用的券码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/ECWO_t3JT6K8dt3MFcQC4Q/zh-cn_image_0000002558765598.png?HW-CC-KV=V1&HW-CC-Date=20260429T053934Z&HW-CC-Expire=86400&HW-CC-Sign=6ED04EA43638BD1D3C589C1FE7BC3B4450860C10C7DCF62FE39C81E9DD0779E1)

**券批次管理**

1. 商户服务端调Payment Kit服务端[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口创建批次。
2. 批次创建成功后，Payment Kit服务端返回批次号信息。
3. 如果商户服务端没有记录批次信息，需要调用[查询商家券批次详情](../harmonyos-references/common-promotion-service-merc-coup-coupbatch-query.md)接口获取批次库存信息，用于构造修改批次预算接口请求体。
4. Payment Kit服务端给商户返回批次详情信息。
5. 商户服务端调Payment Kit服务端[修改商家券批次预算](../harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge.md)接口修改批次预算。
6. Payment Kit服务端返回批次预算修改结果。

**券管理**

在商户没有券系统记录用户券列表的情况下，交互流程如下：

1. 用户在华为平台（负一屏）领券。
2. 华为平台（负一屏）调Payment Kit服务端接口给用户发券。
3. Payment Kit服务端通过批次上设置的回调地址给商户服务端发送[发券事件回调通知](../harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute.md)。
4. 用户在华为平台（负一屏）点击“去使用”。
5. 用户点击“去使用”后，引导用户跳转到商户服务端使用券。
6. 商户服务端调Payment Kit服务端[查询用户优惠券列表](../harmonyos-references/api-common-promotion-service-merc-coup-ucoup-query.md)查询用户优惠券列表。
7. Payment Kit服务端返回优惠券列表。
8. 用户在商户服务端选择优惠券并下单后，商户服务端调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。
9. Payment Kit服务端券核销成功后，把核销结果返回给商户服务端。
10. 用户在商户服务端上进行退单。
11. 商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券。
12. Payment Kit服务端退券处理完后，把退券结果返回给商户服务端。

在商户服务端记录用户券列表的情况下，交互流程如下：

1. 用户在华为平台（负一屏）领券。
2. 华为平台（负一屏）调Payment Kit服务端接口给用户发券。
3. Payment Kit服务端通过批次上设置的回调地址给商户服务端发送[发券事件回调通知](../harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute.md)。
4. 商户服务端将发出去的券码与自有系统券码做映射。
5. 用户在华为平台（负一屏）点击“去使用”。
6. 用户点击“去使用”后，引导用户跳转到商户服务端使用券。
7. 商户服务端在下单成功后，调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。
8. Payment Kit服务端券状态刷新后，把核销结果返回给商户服务端。
9. 用户在商户服务端上进行退单。
10. 商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券。
11. Payment Kit服务端退券处理完后，把退券结果返回给商户服务端。

### 华为平台导入Code发放场景

如果华为商家券系统中对商家券Code有特殊要求，希望华为平台（负一屏）代发券时使用自有券码，则在创建券批次时选用MERCHANT\_UPLOAD模式，并把自有券码通过[上传券预存Code](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-upload.md)接口同步到华为商家券系统。华为商家券系统在代发商家券时，随机选取已上传的券码给用户发券，发券成功后会回调通知本次发放所使用的券码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/34sdYBOHRvmWoUGOCvDFww/zh-cn_image_0000002558605942.png?HW-CC-KV=V1&HW-CC-Date=20260429T053934Z&HW-CC-Expire=86400&HW-CC-Sign=99301ECF9FD31AFEBFECE44A083FA3081F36E7265C2D4F10F7BA91369D8AEBF2)

**券批次管理**

1. 商户服务端调Payment Kit服务端[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口创建批次。
2. 批次创建成功后，Payment Kit服务端返回批次号信息。
3. 商户服务端调Payment Kit服务端[上传券预存Code](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-upload.md)接口上传Code。
4. Payment Kit服务端返回预存Code结果。
5. 如果商户服务端没有记录批次信息，需要调用[查询商家券批次详情](../harmonyos-references/common-promotion-service-merc-coup-coupbatch-query.md)接口获取批次库存信息，用于构造修改批次预算接口请求体。
6. Payment Kit服务端给商户返回批次详情信息。
7. 商户服务端调Payment Kit服务端[修改商家券批次预算](../harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge.md)接口修改批次预算。
8. Payment Kit服务端返回批次预算修改结果。

**券管理**

1. 用户在华为平台（负一屏）领券。
2. 华为平台（负一屏）调Payment Kit服务端接口给用户发券。
3. Payment Kit服务端通过[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口设置的回调地址给商户服务端发送[发券事件回调通知](../harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute.md)。
4. 用户在华为平台（负一屏）点击“去使用”。
5. 用户点击“去使用”后，引导用户跳转到商户服务端使用券。
6. 商户服务端在下单成功后，调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。
7. Payment Kit服务端券状态刷新后，把核销结果返回给商户服务端。
8. 用户在商户服务端上进行退单。
9. 商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券。
10. Payment Kit服务端退券处理完后，把退券结果返回给商户服务端。

### 商户平台指定Code发放场景

如果系统对商家券Code有特殊要求，仅希望在华为平台（负一屏）中展示用户在自有应用中领取到的券，则使用商户平台发券和指定券Code（MERCHANT\_API）模式，在调用“发放优惠券”接口时，把券码同步到华为商家券系统。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/D91byVXWRDqiafPeZNv8Pg/zh-cn_image_0000002589325469.png?HW-CC-KV=V1&HW-CC-Date=20260429T053934Z&HW-CC-Expire=86400&HW-CC-Sign=E5DF4440C136DB1EE31C3E08AF114A9FD84AA0E054763BA0B27FE0664E645E80)

**券批次管理**

1. 商户服务端调Payment Kit服务端[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口创建批次。
2. 批次创建成功后，Payment Kit服务端返回批次号信息。
3. 如果商户服务端没有记录批次信息，需要调用[查询商家券批次详情](../harmonyos-references/common-promotion-service-merc-coup-coupbatch-query.md)接口获取批次库存信息，用于构造修改批次预算接口请求体。
4. Payment Kit服务端给商户返回批次详情信息。
5. 商户服务端调Payment Kit服务端[修改商家券批次预算](../harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge.md)接口修改批次预算。
6. Payment Kit服务端返回批次预算修改结果。

**券管理**

1. 用户在商户服务端商户平台领券。
2. 商户服务端调Payment Kit服务端[发放优惠券](../harmonyos-references/ommon-promotion-service-merc-coup-ucoup-distribute.md)接口给用户发券。
3. Payment Kit服务端处理完后响应商户平台发券结果。
4. 用户在华为平台（负一屏）点击“去使用”。
5. 用户点击“去使用”后，引导用户跳转到商户服务端使用券。
6. 商户服务端在下单成功后，调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。
7. Payment Kit服务端券状态刷新后，把核销结果返回给商户服务端。
8. 用户在商户服务端上进行退单。
9. 商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券。
10. Payment Kit服务端退券处理完后，把退券结果返回给商户服务端。

## 开发步骤

说明

* 以下开发步骤仅涉及服务端开发，业务接口请求示例代码可参考[业务接口请求](payment-server-connect.md#业务接口请求)。
* [发券事件回调通知](../harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute.md)回调地址是开发者调用[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口时通过notifyConfig字段设置的回调地址，接收到回调通知后商户服务端可先对返回的支付信息进行[SM2验签](../harmonyos-references/payment-rest-overview.md#验签规则)处理。

### 华为平台随机Code发放场景

**券批次管理（服务端开发）**

开发者调用[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口创建券批次。成功后调用[修改商家券批次预算](../harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge.md)接口修改批次预算。

**券管理（服务端开发）**

1. 华为平台（负一屏）调Payment Kit服务端接口给用户发券后（使用随机Code模式，随机生成券码给用户发券），会给商户服务端发送发券事件回调，回调详细信息请参见[发券事件回调通知](../harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute.md)（商户服务端将发出去的券码与自有系统券码做映射）。
2. 商户服务端调Payment Kit服务端[查询用户优惠券列表](../harmonyos-references/api-common-promotion-service-merc-coup-ucoup-query.md)查询用户优惠券列表，用户在商户服务端选择优惠券并下单后，调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。如果用户在商户服务端上进行退单，商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券，把退券结果返回给商户服务端。

### 华为平台导入Code发放场景

**券批次管理（服务端开发）**

开发者调用[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口创建券批次。创建券批次成功后调用[上传券预存Code](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-upload.md)接口上传Code，券code上传成功后调用[修改商家券批次预算](../harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge.md)接口修改批次预算。

**券管理（服务端开发）**

1. 华为平台（负一屏）给用户发券后会给商户服务端发送发券事件回调，回调详细信息请参见[发券事件回调通知](../harmonyos-references/motion-service-merc-coup-ucoup-callback-distribute.md)。
2. 商户服务端在下单成功后，调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。用户如果在商户服务端上进行退单，商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券，把退券结果返回给商户服务端。

### 商户平台指定Code发放场景

**券批次管理（服务端开发）**

开发者调用[创建商家券批次](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-create.md)接口创建券批次，成功后调用[修改商家券批次预算](../harmonyos-references/mmon-promotion-service-merc-coup-coupbatch-upbudge.md)接口修改批次预算。

**券管理（服务端开发）**

1. 商户服务端调Payment Kit服务端[发放优惠券](../harmonyos-references/ommon-promotion-service-merc-coup-ucoup-distribute.md)接口给用户发券（使用指定Code模式，在调用接口时把券码同步到华为商家券系统），Payment Kit服务端处理完后响应商户平台发券结果。
2. 商户服务端在下单成功后，调用[核销优惠券](../harmonyos-references/t-api-common-promotion-service-merc-coup-ucoup-use.md)接口核销券，把券状态同步给Payment Kit服务端。用户如果在商户服务端上进行退单，商户服务端退单过程中调用华为支付[申请退券](../harmonyos-references/pi-common-promotion-service-merc-coup-ucoup-refund.md)接口退券，把退券结果返回给商户服务端。

## 测试和上线

1. 开发者收集好测试人员华为账号对应的手机号。
2. [联系华为运营人员](payment-service-support.md)添加允许清单手机号进行测试并提供测试结果录屏，录屏内容包括商家券领取、展示以及核销完整流程。
3. 华为运营人员审核测试录屏，无问题后配置全网上线。

## 延伸和拓展

当开发者完成上述能力之后，可以调用以下API接口完成其他相关操作。

[修改商家券批次基本信息](../harmonyos-references/ommon-promotion-service-merc-coup-coupbatch-update.md)、[使券失效](../harmonyos-references/ommon-promotion-service-merc-coup-ucoup-deactivate.md)、[查询用户单张优惠券详情](../harmonyos-references/common-promotion-service-merc-coup-ucoup-query-one.md)、[设置回调通知地址](../harmonyos-references/ion-service-merc-coup-coupbatch-callbackurl-update.md)、[查询回调通知地址](../harmonyos-references/ion-service-merc-coup-coupbatch-callbackurl-select.md)
