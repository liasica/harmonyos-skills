---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-iap-distribute-query
title: 展示数字商品
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > 数字商品服务 > 应用内分发数字商品 > 展示数字商品
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7913daf7c06d289f930e89e1f0cf7ef1ec165105714e203e7d140e2b3fb7e43f
---

数字商品服务为接入消耗型/非消耗型、非续期订阅商品、自动续期订阅商品购买能力的应用提供向用户展示可供购买的商品信息列表的能力。

## 前提条件

当前登录的华为账号所在服务地支持数字商品服务。

## 开发步骤

1. 判断当前登录的华为账号所在的服务地是否支持数字商品服务应用内支付。

   在使用应用内支付之前，应用需要向IAP Kit发送[queryEnvironmentStatus](../harmonyos-references/iap-iap.md#iapqueryenvironmentstatus)请求，以此判断用户当前登录的华为账号所在服务地是否在IAP Kit支持结算的国家/地区中。

   说明

   当前IAP Kit支持结算的国家/地区仅包括中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。

   ```
   1. import { iap } from '@kit.IAPKit';
   2. import { common } from '@kit.AbilityKit';
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. import { UIContext } from '@kit.ArkUI'

   6. class QueryEnvironmentStatus {
   7. queryEnvironmentStatus() {
   8. const context: common.UIAbilityContext = UIContext.prototype.getHostContext() as common.UIAbilityContext;
   9. iap.queryEnvironmentStatus(context).then(() => {
   10. // 请求成功
   11. console.info('Succeeded in querying environment status.');
   12. }).catch((err: BusinessError) => {
   13. // 请求失败
   14. console.error(`Failed to query environment status. Code is ${err.code}, message is ${err.message}`);
   15. });
   16. }
   17. }
   ```
2. 查询商品信息。

   通过[queryProducts](../harmonyos-references/iap-iap.md#iapqueryproducts)来获取在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上配置的商品信息。发起请求时，需在请求参数[QueryProductsParameter](../harmonyos-references/iap-iap.md#queryproductsparameter)中携带相关的商品ID，并根据实际配置指定其productType，订阅型商品指定其productType为[iap.ProductType.AUTORENEWABLE](../harmonyos-references/iap-iap.md#producttype)。

   当接口请求成功时，IAP Kit将返回商品信息[Product](../harmonyos-references/iap-iap.md#product)的列表。 应用可以使用[Product](../harmonyos-references/iap-iap.md#product)包含的商品价格、名称和描述等信息，向用户展示可供购买的商品列表。

   说明

   [queryProducts](../harmonyos-references/iap-iap.md#iapqueryproducts)每次只能查询一种类型的商品，单次查询请勿超过200条。

   ```
   1. import { iap } from '@kit.IAPKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. import { common } from '@kit.AbilityKit';
   4. import { UIContext } from '@kit.ArkUI'
   5. class Queryproducts {
   6. queryProducts() {
   7. const queryProductParam: iap.QueryProductsParameter = {
   8. // iap.ProductType.CONSUMABLE：消耗型商品;
   9. // iap.ProductType.NONCONSUMABLE：非消耗型商品;
   10. // productType: iap.ProductType.AUTORENEWABLE;订阅型商品
   11. productType: iap.ProductType.CONSUMABLE,
   12. // 查询的商品必须是开发者在AppGallery Connect网站配置的商品
   13. productIds: ['ohos_consume_001']
   14. };
   15. const context: common.UIAbilityContext = UIContext.prototype.getHostContext() as common.UIAbilityContext;
   16. iap.queryProducts(context, queryProductParam).then((result) => {
   17. // 请求成功
   18. console.info('Succeeded in querying products.');
   19. // 展示商品信息
   20. // ...
   21. }).catch((err: BusinessError) => {
   22. // 请求失败
   23. console.error(`Failed to query products. Code is ${err.code}, message is ${err.message}`);
   24. });
   25. }
   26. }
   ```
