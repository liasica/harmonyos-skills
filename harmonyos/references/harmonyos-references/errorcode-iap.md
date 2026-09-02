---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-iap
title: ArkTS API错误码
breadcrumb: API参考 > 应用服务 > IAP Kit（应用内支付服务） > ArkTS API > ArkTS API错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:be20cf5c24b94beb809aeb6bf8a1a7149c715d3c34c16d2d5bf4d7447dad0d60
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码](errorcode-universal.md)。

若问题仍无法解决，请选择[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。

## 1001860000 用户取消当前操作

**错误信息**

The operation was canceled by the user.

**错误描述**

用户取消当前操作。

**可能原因**

用户取消了当前操作流程。

**处理步骤**

向用户提示，操作取消。

## 1001860001 内部错误

**错误信息**

System internal error.

**错误描述**

系统内部错误。

**可能原因**

1. 当前DevEco Studio版本低于DevEco Studio 6.0.1 Release，或HarmonyOS SDK版本低于HarmonyOS 6.0.1 Release SDK。
2. JWT签名无效或已过期。
3. 使用了优惠签名，但nonce字段重复使用。
4. IAP Kit开关未打开。

**处理步骤**

1. 请确认DevEco Studio已升级到DevEco Studio 6.0.1 Release及以上版本，且HarmonyOS SDK已升级到HarmonyOS 6.0.1 Release SDK及以上版本。
2. 请参见[生成优惠签名购买参数](iap-server-subscribe-offer-sign.md)，检查JWT签名的有效性，确认JWT在有效时间内。
3. 如果使用了优惠签名，请确认nonce字段的唯一性，请勿重复使用。请参见[OfferInfo](iap-server-data-model.md#offerinfo)。
4. 请参见[开启和激活应用内购买服务](../harmonyos-guides/iap-enable-in-app-purchases.md)确认IAP Kit开关已开启，并已激活。
5. 其他情况请进行重试操作或通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。

## 1001860002 应用未被授权访问接口

**错误信息**

The application is not authorized.

**错误描述**

应用未被授权访问接口。

**可能原因**

1. 应用程序签名/身份信息配置有误。
2. 应用的支付服务开关未打开。

**处理步骤**

1. 请参考[配置应用身份信息](../harmonyos-guides/iap-config-app-identity-info.md)、[添加公钥指纹](../harmonyos-guides/application-dev-overview.md#条件必选添加公钥指纹)章节进行检查。
2. 请参考[配置签名信息](../harmonyos-guides/application-dev-overview.md#配置签名信息)检查是否使用了自动签名方式，请使用手动签名方式。
3. 需要使用华为应用内支付功能的应用必须[开启和激活应用内购买服务](../harmonyos-guides/iap-enable-in-app-purchases.md)。

## 1001860003 无效的商品信息

根据实际错误原因的不同，系统会上报不同的错误信息，具体如下。

### Product status is not online.

**错误信息**

Invalid product information. Failure reason: Product status is not online.

**错误描述**

当产品状态为不在线时，系统会产生此错误码。

**可能原因**

创建的商品状态异常（草稿、待提交、驳回）。

**处理步骤**

请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“APP与元服务 > 在应用列表中点击该商品的应用 > 运营 > 商品管理 > 商品列表”，查看对应商品是否存在且正确、商品信息已经提交审核并审核通过。如未审核通过，可使用沙盒账号来进行[沙盒测试](../harmonyos-guides/iap-sandbox.md)。

### The product type or product id does not match.

**错误信息**

Invalid product information. Failure reason: The product type or product id does not match.

**错误描述**

当产品类型或产品ID不匹配时，系统会产生此错误码。

**可能原因**

传入的商品ID、商品类型有误，或者商品价格未配置。

**处理步骤**

请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“APP与元服务 > 在应用列表中点击该商品的应用 > 运营 > 商品管理 > 商品列表”，请确认对应商品ID和商品类型是否正确，并确认商品价格已配置。

### The In-App Purchases Service is not activated.

**错误信息**

The application is not authorized. Failure reason: The In-App Purchases Service is not activated.

**错误描述**

当未激活应用内支付服务时，系统会产生此错误码。

**可能原因**

IAP Kit开关未开启。

**处理步骤**

请参见[开启和激活应用内购买服务](../harmonyos-guides/iap-enable-in-app-purchases.md)确认IAP Kit开关已开启，并已激活。

## 1001860004 接口访问过频

**错误信息**

Too frequent API calls.

**错误描述**

接口访问过频。

**可能原因**

接口访问间隔过短。

**处理步骤**

请控制接口调用频度。接口当前访问间隔时间默认为5s，后续IAP Kit可能会根据需要降低或提高速率限制。

## 1001860005 网络连接异常

**错误信息**

Network connection error.

**错误描述**

网络连接异常。

**可能原因**

请检查网络。

**处理步骤**

应用向用户给出提示，请用户检查网络。

## 1001860007 商品所属的应用未在指定国家/地区上架

**错误信息**

The app to which the product belongs is not released in a specified location.

**错误描述**

商品所属的应用未在指定国家/地区上架。

**可能原因**

商品所属的应用未在指定国家/地区上架。

**处理步骤**

请登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)网站，选择“我的应用 > 分发 > 版本信息 > 准备提交”，查看商品配置的国家/地区。

## 1001860050 未登录华为账号

**错误信息**

The HUAWEI ID is not signed in.

**错误描述**

未登录华为账号。

**可能原因**

未登录华为账号。

**处理步骤**

引导用户登录华为账号。

## 1001860051 由于已经拥有该商品，购买失败

**错误信息**

Failed to purchase a product because the user already owns the product.

**错误描述**

由于已经拥有该商品，购买失败。

**可能原因**

该商品已经购买。

**处理步骤**

可通过[queryPurchases](iap-iap.md#iapquerypurchases)接口确认用户是否购买了该商品。

* 若商品为消耗型商品或非续期订阅商品，检查商品是否发货，确认发货成功之后调用[finishPurchase](iap-iap.md#iapfinishpurchase)接口完成购买，下次可正常购买。
* 若商品为非消耗型商品或自动续期订阅商品，已经购买则不能再次购买。

## 1001860052 由于未支付该商品，发货失败

**错误信息**

The purchase cannot be finished because the user has not paid for it.

**错误描述**

由于未支付该商品，发货失败。

**可能原因**

1. 用户未购买该商品。
2. 参数传递错误。

**处理步骤**

1. 可通过[queryPurchases](iap-iap.md#iapquerypurchases)接口确认用户是否购买了该商品。
2. 请排查报错接口的传参是否存在问题。

## 1001860053 此次购买已经完成发货，无需重复发货

**错误信息**

The purchase has been finished and cannot be finished again.

**错误描述**

此次购买已经完成发货，无需重复发货。

**可能原因**

此次购买已经完成发货，无需重复发货。

**处理步骤**

可通过[queryPurchases](iap-iap.md#iapquerypurchases)接口查询是否有该商品的确认发货记录。

## 1001860054 用户账号所在服务地不在IAP Kit支持结算的国家/地区中

**错误信息**

The country or region of the signed-in HUAWEI ID does not support IAP.

**错误描述**

用户账号所在服务地不在IAP Kit支持结算的国家/地区中。

**可能原因**

用户账号所在服务地不在IAP Kit支持结算的国家/地区中。

**处理步骤**

用户账号服务地为非中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）地区。建议应用隐藏相关IAP功能入口。

## 1001860056 用户交易被拒绝

**错误信息**

The user is not allowed to make purchase.

**错误描述**

用户交易被拒绝。

**可能原因**

交易行为触发IAP Kit风控。

**处理步骤**

建议稍后重试或更换支付方式。

## 1001860057 当前应用不是debug签名的应用

**错误信息**

The app provision type is not debug.

**错误描述**

当前应用不是debug签名的应用。

**可能原因**

当前应用不是debug签名的应用。

**处理步骤**

可构建debug签名的应用：

1. 手动签名：您需要在AGC中[申请调试证书](../app/agc-help-debug-cert-0000002283256797.md)、[注册调试设备](../app/agc-help-add-device-0000002283189937.md)、[申请调试Profile](../app/agc-help-debug-profile-0000002248181278.md)后，再[手动配置签名信息](../harmonyos-guides/ide-signing-manual.md)。
2. 在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中[配置公钥指纹](../app/agc-help-cert-fingerprint-0000002278002933.md)。

## 1001860058 登录的华为账号不是配置的测试账号

**错误信息**

The HUAWEI ID is not test account.

**错误描述**

登录的华为账号不是配置的测试账号。

**可能原因**

未在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中的“用户与访问”中将登录的账号配置为测试账号。

**处理步骤**

需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)中的“用户与访问”中添加测试账号，具体请参见[沙盒测试中添加测试账号流程](../harmonyos-guides/iap-sandbox.md#配置沙盒测试)。

## 1001860059 无效的优惠信息

**错误信息**

Invalid promotional offer id.

**错误描述**

无效的优惠信息。

**可能原因**

[配置商品信息](../harmonyos-guides/iap-config-product.md)时没有为该商品配置自定义人群促销。

**处理步骤**

可通过[queryProducts](iap-iap.md#iapqueryproducts-1)接口确认该商品是否配置了优惠活动，具体请参见[设置促销价格](../app/set-0000001931995712.md)。

## 1001860060 无效的签名信息

**错误信息**

Invalid purchase signature.

**错误描述**

无效的签名信息。

**可能原因**

签名密钥及签名参数不合法，或签名失败。

**处理步骤**

可参考[生成优惠签名购买参数](iap-server-subscribe-offer-sign.md)进行签名过程处理。

## 1001860061 商品已退款或退款中

**错误信息**

The purchase has been refunded or in refund.

**错误描述**

商品已退款或退款中。

**可能原因**

商品已退款或正在退款中。

**处理步骤**

引导用户进订单详情中查看退款状态。

## 1001860062 不允许退款

**错误信息**

Refund is not allowed.

**错误描述**

该笔订单不允许退款。

**可能原因**

该笔订单不支持退款。目前应用内集成的退款入口系统组件仅针对非游戏场景开放，暂不支持游戏场景。

**处理步骤**

在游戏场景不展示退款入口。

## 1001860064 登录的华为账号上找不到该笔订单

**错误信息**

The purchase order is not found for the signed-in HUAWEI ID.

**错误描述**

在登录的华为账号上找不到该笔订单。

**可能原因**

用户登录的华为账号与订单账号不一致，或该笔订单不存在。

**处理步骤**

建议检查手机登录的华为账号与订单所在的应用账号是否一致，或检查传入订单号是否有误。

## 1001860065 不支持该操作

**错误信息**

The operation is not supported.

**错误描述**

不支持该操作。

**可能原因**

1. 本应用未在用户账户所在[国家或地区](../harmonyos-guides/iap-appendix-coverage.md)提供服务。
2. 该订单完成时间未满48小时或已超过36个月。
3. 该订单异常。
4. 该订单已线下开票。
5. 该订单已全额退款。
6. 该订单实付金额为0元。
7. 该订单使用纯花币支付。
8. 该设备不支持此类操作。

**处理步骤**

请按照上述可能原因检查订单是否存在问题。
