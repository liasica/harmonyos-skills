---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-launch-third-party-payment-url
title: 基于URL跳转方式
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 通用收银台接入 > 拉起三方支付收银台 > 基于URL跳转方式
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:30+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:4d258adde946ac89086a71621fd59d4ea887f0994329f9a6ec2f87582e8917dd
---

1. 商户客户端根据Payment Kit接口返回的支付信息[PayResult](../harmonyos-references/payment-paymentservice.md#payresult)(混合支付场景）/[PickerResult](../harmonyos-references/payment-paymentservice.md#pickerresult)（纯外部支付场景），按照三方支付平台接入要求创建订单获取拉起三方支付收银台链接并构建**订单支付跳转信息**[orderStr](../harmonyos-references/payment-model.md#orderstr)请求[requestPayment](../harmonyos-references/payment-paymentservice.md#requestpayment)接口跳转或拉起三方支付收银台。

   跳转三方支付收银台示例代码如下：

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { paymentService } from '@kit.PaymentKit';
   import { common } from '@kit.AbilityKit';

   @Entry
   @Component
   struct Index {
    context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    requestPaymentPromise() {
      // 请使用开发者自己的订单信息（orderStr），跳转三方支付方式。
      const orderStr = '{"nextAction":"L","linkUrl":"","scheme":"","clientToken":"***"}';
      paymentService.requestPayment(this.context, orderStr, 'AP')
        .then(() => {
          console.info('requestPayment success');
        })
        .catch((error: BusinessError) => {
          // 支付失败
          console.error(`requestPayment failed, error.code: ${error.code}, error.message: ${error.message}`);
        });
    }

    build() {
      Column() {
        Button('requestPaymentPromise')
          .type(ButtonType.Capsule)
          .width('50%')
          .margin(20)
          .onClick(() => {
            this.requestPaymentPromise();
          })
        }
      .width('100%')
      .height('100%')
    }
   }
   ```
2. 开发者按照三方支付平台要求完成订单支付后的下一步业务处理，如对返回的支付结果信息验签等。
