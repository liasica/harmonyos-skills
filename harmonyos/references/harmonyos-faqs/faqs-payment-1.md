---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-payment-1
title: 华为支付拉起收银台，取消支付后点击重新支付不会跳转到开通页面
breadcrumb: FAQ > 应用服务开发 > 鸿蒙支付服务（Payment Kit） > 华为支付拉起收银台，取消支付后点击重新支付不会跳转到开通页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:48+08:00
doc_updated_at: 2026-07-30
content_hash: sha256:f6e7aa0275b88bb45c2fda202a9a2e264f3005cbddf61e9ba6aef43b75d4c7bb
---

## 问题现象

开通页面点击立即购买，弹出支付方式，选择华为支付，拉起收银台，取消支付后页面显示重新支付，点击重新支付不会跳转到开通页面。

## 背景知识

* 拉起通用收银台：商户客户端构建[PaymentInfo](../harmonyos-references/payment-paymentservice.md#paymentinfo)参数调用[cashierPicker](../harmonyos-references/payment-paymentservice.md#cashierpicker)接口拉起Payment Kit通用收银台，用户选择支付方式并确认支付后，Payment Kit客户端将支付信息[PickerResult](../harmonyos-references/payment-paymentservice.md#pickerresult)返回给商户客户端 。
* 用户在拉起通用收银台后，如果用户在支付、签约等过程中取消退出，[cashierPicker](../harmonyos-references/payment-paymentservice.md#cashierpicker)接口会报[1001930000](../harmonyos-references/errorcode-payment.md#section1001930000-用户取消操作)错误码。

## 问题定位

根据问题现象尝试复现问题：

1. 拉起华为支付收银台，搜索'RequestPayment'、'paymentAggrUIExtensionAbility'关键词，日志如下：

   ```txt
   [nodict][payment_extension_ability.cpp] StartUIExtensionAbility# StartUIExtensionAbility sessionId 1139957771
   [nodict][payment_extension_ability.cpp] StartUIExtensionAbility# end StartUIExtensionAbility
   [nodict][payment_extension_ability.cpp] ExecuteRequestPayment# end ExecuteRequestPayment
   [nodict][payment_extension_ability.cpp] RequestPayment# end RequestPayment
   RSSurfaceNode::Unmarshalling, Node: 81312320848677, Name: com.huawei.hms.paymentAggrUIExtensionAbility
   RSNode::AddChild, Id: 69432441307937, SurfaceNode:[Id: 81312320848677, name: com.huawei.hms.paymentAggrUIExtensionAbility]
   ```
2. 取消支付，搜索错误码1001930000，日志如下：

   ```screen
   [nodict][payment_error.cpp] CreateBusinessError# CreateBusinessError errCode: 1001930000 errMsg: The operation was canceled by the user.
   [nodict][payment_error.cpp] CreateBusinessError# CreateBusinessError exit
   error: 支付失败: The operation was canceled by the user.code = 1001930000
   [] Background(500): Background ExtensionSession, id: 1139957772, state: 3
   error: 给JS回调 ： doHWPayxxx('{"reqId":"doHWPayxxx","serviceId":"doHWPay","resp":{"code":1001930000,"message":"The operation was canceled by the user."}}')
   ```
3. 搜索'onOverrideUrlLoading'关键词，取消支付会自动跳转重新支付页面，用浏览器打开日志中url页面显示和手机端一致：

   ```screen
   [nodict][nweb_handler_delegate.cc:1807] NWebHandlerDelegate::ShouldOverrideUrlLoading
   onOverrideUrlLoading url:https://www.example.com/xxx-h5/pay/xxx-pay-result.html?orderNo=xxxx
   ```
4. 点击重新支付，跳转的页面显示“未查询到缴费订单”，用浏览器打开日志中url页面显示和手机端一致：

   ```screen
   onOverrideUrlLoading url:https://www.example.com/xxx-h5/pay/xxx-order.html?key=000000008107405,,&derivation=index
   ```
5. 根据页面内容以及日志中的url链接分析，重新支付页面跳转的是“未查询到缴费订单”页面，而不是开通付费项目的页面或者未支付订单页面。

## 分析结论

用户取消华为支付时，应用没有跳转到开通付费项目的页面或者未支付订单页面，而是访问与业务无关的url，跳转到“未查询到缴费订单”页面。

## 修改建议

需要优化取消华为支付时的页面跳转逻辑，建议使用try-catch捕捉错误码1001930000，使得应用根据业务逻辑正确处理用户取消支付后的页面跳转操作。

```screen
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  requestCashierPicker() {
    const paymentInfo: paymentService.PaymentInfo = {
      tradeSummary: '***',
      amount: 100,
      currency: 'CNY',
      extraInfo: '{"***":"***"}'
    };
    paymentService.cashierPicker(this.context, paymentInfo)
      .then((pickerResult: paymentService.PickerResult) => {
        // succeeded in paying
        console.info('succeeded in paying, picker result: ', pickerResult);
      })
      .catch((error: BusinessError) => {
        // failed to pay
        console.error(`failed to pay, error.code: ${error.code}, error.message: ${error.message}`);
        if (error.code === 1001930000) {
          // 应用侧需要根据业务逻辑，正确处理用户取消支付后的页面跳转操作，避免显示不相关的页面
        }
      });
  }

  build() {
    Column() {
      Button('requestCashierPicker')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestCashierPicker();
        });
    }
    .width('100%')
    .height('100%');
  }
}
```
