---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-payment-promotions
title: 利用支付优惠提升商品转化
breadcrumb: 指南 > 应用服务 > IAP Kit（应用内支付服务） > 利用支付优惠提升商品转化
category: harmonyos-guides
scraped_at: 2026-11-12T09:52:27+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:667fa1e435f9a623b3c6ff5e14b53e430db5cde3a7602e32b3f145fa71f50970
---

## 概述

在传统的购买流程中，用户在下单前往往难以直观感知具体的优惠力度，这可能会影响决策。自API版本26.0.1起，我们新增了IAP Kit支付优惠查询功能。通过让用户在购买前即可预览实际享受的优惠，不仅能增强购买意愿，还能有效提升下单转化率。

## 开发准备

请先参考[应用开发准备](application-dev-overview.md)完成基本准备工作，再继续以下开放能力准备项。

## 开发步骤

**代码示例**

```typescript
import { iap } from '@kit.IAPKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import Logger from '../common/Logger';
// ...
  queryPaymentPromotion() {
    const context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // productId需要替换成开发者在AppGallery Connect网站配置商品信息时设置的“商品ID”
    const parameter: iap.QueryPaymentPromotionParam[] = [{
      productId: 'testProduct01',
      microMarkedPrice: 1,
      currency: 'CNY',
    }];
    iap.queryPaymentPromotions(context, parameter).then((data: Array<iap.PaymentPromotion>) => {
      // 请求成功
      Logger.info(TAG, `Succeeded in querying paymentPromotions. data length: ${data?.length}`);
      // ...
    }).catch((err: BusinessError) => {
      // 请求失败
      Logger.error(TAG, `Failed to query paymentPromotions. Code is ${err.code}, message is ${err.message}`);
      // ...
    });
  }
```
