---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-config-agc
title: 开通相关服务和配置参数
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 启用数字商品服务 > 开通相关服务和配置参数
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:38dc3e5a01bb11ab621321712151e29bf16c586fc7d398887491d894468e3531
---

请先参考“[应用开发准备](application-dev-overview.md)”完成基本准备工作及指纹配置，再继续进行以下开发活动。

说明

[配置签名信息](application-dev-overview.md#section42841246144813)时，请使用手动签名方式。

接入数字商品服务，需要[添加公钥指纹](application-dev-overview.md#section1726913517284)。

## 开通商户服务

开发者需开通商户服务才能使用华为数字商品服务，具体请登录[华为开发者联盟官网](https://developer.huawei.com/consumer/cn/)，点击“管理中心”>“开发者中心”>“商户服务”进入商户服务页面。

商户服务里配置的银行卡账号、币种，用于开发者接收华为分成收益。需要提供如下信息，具体可详见[商户服务](../start/merchant-service-0000001053025967.md)：

* 收款银行信息（开户行国家、开户银行、开户行支行、开户行账号、开户名等）
* 税务信息（税务地点、税务注册地址、税票类型）
* 联系人（市场、财务、法务、业务合作）

当销售数字商品后，可以选择“管理中心 > 我的账户”，选择“收益”，进入自助结算页面，查看商品产生的收益结算单并申请结算，详情见[自助结算指南](../start/checkoutguide-0000001053128363.md)。

## 打开应用内购买服务 (HarmonyOS NEXT)

需要使用数字商品服务的应用必须打开应用内购买服务 (HarmonyOS NEXT) API开关。打开服务开关是应用级别的，即每个需要使用数字商品服务的应用都需要先执行此步骤，具体操作请参见[打开应用内购买服务(HarmonyOS NEXT) API开关](../app/switch-0000001958955097.md)。

## 配置服务参数

开启应用内购买服务(HarmonyOS NEXT) 开关后，开发者需进一步激活应用内购买服务 (HarmonyOS NEXT)，具体请参见[激活服务和配置事件通知](../app/parameters-0000001931995692.md)。

说明

* 用户购买商品后，服务器会在订单/订阅场景的某些关键事件发生时通知您配置的事件通知地址，具体可参见[服务端关键事件通知](../harmonyos-references/iap-key-event-notifications.md)。
* 调试阶段必须[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[注册设备](../app/agc-help-add-device-0000002283189937.md)、开启和激活“应用内购买服务”后需要重新[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)，并完成[手动签名](ide-signing.md#section297715173233)。
* 发布阶段必须[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)、开启和激活“应用内购买服务”后需要重新[申请发布Profile](../app/agc-help-release-profile-0000002248341090.md)，并完成[手动签名](ide-signing.md#section297715173233)。

## 服务端密钥管理

数字商品服务器要求对每个服务端API请求进行JSON Web Token（JWT）授权。开发者可以使用从[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)下载的API密钥对Token签名生成JWT，授权发起的服务端API请求。

开发者可参见[创建密钥](../app/key-0000001959074877.md)、[下载密钥](../app/download-0000001958955101.md)、[撤销密钥](../app/cancel-0000001931995696.md)管理服务端密钥。
