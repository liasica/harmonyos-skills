---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-launch-third-party-payment-sdk
title: 基于接口拉起方式
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 通用收银台接入 > 拉起三方支付收银台 > 基于接口拉起方式
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:549cb49dc268756fa3c672ced023e0b3d8bfd5474d3af46ee49ff1861caa6611
---

**说明** 

* 当前基于接口拉起方式拉起三方支付收银台支持的支付方式参见[PayMethod](../harmonyos-references/payment-third-payment-service.md#paymethod)。
* 基于接口拉起三方支付收银台起始版本为：6.0.0(20)。
* 拉起支付宝支付需要[配置服务器域名](../atomic-guides/agc-help-harmonyos-server-domain.md#section1745215342321)：https://mobilegw.alipay.com。

1. 商户客户端根据Payment Kit接口返回的支付信息[PayResult](../harmonyos-references/payment-paymentservice.md#payresult)(混合支付场景）/[PickerResult](../harmonyos-references/payment-paymentservice.md#pickerresult)（纯外部支付场景），按照三方支付平台接入要求构建三方支付信息[payInfo](../harmonyos-references/payment-model.md#payinfo)调用[ThirdPayClient.pay](../harmonyos-references/payment-third-payment-service.md#pay)接口拉起三方支付收银台。

   拉起三方支付收银台示例代码如下：

   ```typescript
   import { BusinessError } from '@kit.BasicServicesKit';
   import { thirdPaymentService } from '@kit.PaymentKit';
   import { common } from '@kit.AbilityKit';

   export let thirdPayClient: thirdPaymentService.ThirdPayClient | undefined = undefined;

   @Entry
   @Component
   struct Index {
     context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
     thirdPaymentServicePayPromise() {
       thirdPayClient = new thirdPaymentService.ThirdPayClient(this.context, thirdPaymentService.PayMethod.WECHAT_PAY, 'appid_123456');
       // 请使用开发者自己的三方支付信息（payInfo）
       const payInfo = '{"xxx1":"***", "xxx2":"***", "token":"***"}';
       thirdPayClient.pay(payInfo).then(() => {
         // 支付成功
         console.info('succeeded in paying.');
       }).catch((error: BusinessError) => {
         // 支付失败
         console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
       });
     }

     build() {
       Column() {
         Button('thirdPaymentServicePayPromise')
           .type(ButtonType.Capsule)
           .width('50%')
           .margin(20)
           .onClick(() => {
             this.thirdPaymentServicePayPromise();
           })
       }
       .width('100%')
       .height('100%')
     }
   }
   ```
2. 拉起三方支付收银台可同步通过调用[ThirdPayClient.handlePayCallback](../harmonyos-references/payment-third-payment-service.md#handlepaycallback)接口（用户支付完成后，会将支付操作结果回调给商户客户端），获取三方支付处理结果，完成支付操作处理。参考示例代码如下：

   ```typescript
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { UIAbility, Want } from '@kit.AbilityKit';
   // 需要从thirdPayClient对象定义的代码文件中导入三方支付客户端对象，以下为示例，具体以应用定义路径为准。
   import { thirdPayClient } from '../pages/thirdPaymentServicetest';

   // 如果已有Ability实现类，可直接添加onNewWant生命周期方法处理即可。
   export default class EntryAbility extends UIAbility {
     onNewWant(want: Want): void {
       // 需要和拉起支付收银台的三方支付客户端对象为同一个
       if (thirdPayClient) {
         hilog.info(0x0000, 'testTag', '%{public}s','clientForThirdPayment handlePayCallback');
         let handlePayCallback = thirdPayClient.handlePayCallback(want);
         hilog.info(0x0000, 'testTag', 'clientForThirdPayment handlePayCallback result: %{public}s', handlePayCallback);
       }
     }
   }
   ```
3. 商户客户端收到三方支付回调通知或主动查询订单支付结果成功后，按照三方支付平台要求完成订单支付后的下一步业务处理，如对返回的支付结果信息验签等。
