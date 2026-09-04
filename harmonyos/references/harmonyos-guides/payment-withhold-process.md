---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-withhold-process
title: 签约代扣场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 免密支付接入 > 签约代扣场景
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:15+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:4ab880bceecf610db9ea22987f0e944872847ff689df782cc8472cc489d72803
---

## 场景介绍

从4.1.0(11)版本开始，新增支持签约代扣场景。

用户在商户APP应用/元服务开通会员一段时间后，想要每个月自动续费而不用自己每个月都重新开通，商户可提供自动续费选项，用户主动选择开启，商户通过请求预签约接口发起签约，待签约生效后，商家可以按照协议中的时间，会员到期后直接发起免密代扣请求完成扣款续费，无需用户每个月都进行开通会员操作。

支持商户模型：直连商户、平台类商户、服务商

华为支付签约页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YD4_auiFRrWHWpAUqDtK_Q/zh-cn_image_0000002742124263.png)

## 业务流程

开发者通过接入Payment Kit 签约代扣能力，在获取用户签约授权的前提下，可以向用户的华为支付账户发起支付扣款，无需用户输入支付密码就可以优先使用签约的支付方式完成扣款。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/wrNwZWPTQwaW43FD3KTFTg/zh-cn_image_0000002712245356.png)

1. 商户客户端请求商户服务端创建签约订单。
2. 商户服务端按照商户模型调用Payment Kit服务端[直连商户预签约](../harmonyos-references/payment-withhold-presign.md)或[服务商预签约](../harmonyos-references/payment-partner-withhold-presign.md)接口。
3. Payment Kit服务端返回预签约号（preSignNo）给商户服务端。
4. 商户服务端构建[contractStr](../harmonyos-references/payment-model.md#contractstr)参数返回给商户客户端。
5. 商户客户端通过contractStr调用[requestContract](../harmonyos-references/payment-paymentservice.md#requestcontract)接口拉起Payment Kit签约收银台。
6. Payment Kit客户端通过签约收银台展示签约相关信息。
7. 用户在Payment Kit客户端签约收银台完成签约操作。
8. Payment Kit服务端处理签约。
9. Payment Kit服务端受理签约成功后返回签约结果信息给Payment Kit客户端。
10. Payment Kit客户端展示签约结果页。
11. 用户关闭签约结果页后Payment Kit客户端会返回商户客户端。
12. 签约完成后Payment Kit服务器会调用商户服务端调用预签约接口时传递的回调接口返回签约结果信息给商户服务器。
13. 商户服务器收到签约结果回调响应后，使用[SM2验签方式](../harmonyos-references/payment-rest-overview.md#验签规则)对签约结果进行验签。
14. 签约完成后，商户服务器后续可以调用Payment Kit服务端[直连商户申请免密代扣](../harmonyos-references/payment-withhold-apply.md)/[服务商申请免密代扣](../harmonyos-references/payment-partner-withhold-apply.md)接口来完成扣款服务。
15. 商户服务器调用Payment Kit服务端申请免密代扣接口后，Payment Kit服务端同步返回代扣申请结果。
16. Payment Kit服务端处理代扣扣款成功后，会调用商户服务器请求代扣接口时传递回调接口返回扣款结果信息给商户服务器。
17. 商户服务器收到扣款结果回调响应后，使用[SM2验签方式](../harmonyos-references/payment-rest-overview.md#验签规则)对扣款结果进行验签。

## 接口说明

接口返回值有两种返回形式：Promise和AsyncCallback。Promise和AsyncCallback只是返回方式不一样，功能相同。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md)。

| 接口名 | 描述 |
| --- | --- |
| requestContract(context: common.UIAbilityContext, contractStr: string): Promise<void>; | 拉起Payment Kit签约收银台。 |
| requestContract(context: common.UIAbilityContext, contractStr: string, callback: AsyncCallback<void>): void; | 拉起Payment Kit签约收银台。 |

## 开发步骤

### 预签约（服务器开发）

1. 开发者按照商户模型调用预[直连商户预签约](../harmonyos-references/payment-withhold-presign.md)或[服务商预签约](../harmonyos-references/payment-partner-withhold-presign.md)接口获取preSignNo构建签约信息参数[contractStr](../harmonyos-references/payment-model.md#contractstr)。

   为保证支付订单的安全性和可靠性需要对请求body和请求头PayMercAuth对象内的入参排序拼接进行签名。可参考[签名规则](../harmonyos-references/payment-rest-overview.md#签名规则)。

   以下为开放API接口请求及[contractStr](../harmonyos-references/payment-model.md#contractstr)构建[示例代码](https://gitcode.com/HarmonyOS_Samples/paymentkit-sample-code-serverdemo-java)片段：

   ```java
   import com.huawei.petalpay.paymentservice.apiservice.client.model.BaseGwRspWithSign;
   import com.huawei.petalpay.paymentservice.apiservice.client.model.PreSignRequestV2;
   import com.huawei.petalpay.paymentservice.apiservice.client.model.PreSignResponse;
   import com.huawei.petalpay.paymentservice.core.client.DefaultPetalPayClient;
   import com.huawei.petalpay.paymentservice.core.client.PetalPayClient;
   import com.huawei.petalpay.paymentservice.example.common.CommonResponse;
   import com.huawei.petalpay.paymentservice.example.common.MercConfigUtil;

   public class MercApiController {
       private static PetalPayClient payClient = new DefaultPetalPayClient(MercConfigUtil.getMercConfig());
       /**
        * 预签约接口调用
        */
       public CommonResponse contractPreSignAppV2() {
           // 组装对象
           PreSignRequestV2 preSignReq = getPreSignRequestV2();
           PreSignResponse response = null;
           try {
               response = payClient.execute("POST", "/api/v2/contract/presign/app", PreSignResponse.class, preSignReq);
           } catch (Exception e) {
               // 异常处理
               log.error("request error ", e);
               return CommonResponse.buildErrorRsp(e.getMessage());
           }
           if (!validResponse(response)) {
               // 异常处理
               log.error("response is invalid ", response);
               return CommonResponse.buildFailRsp(response);
           }
           return CommonResponse.buildSuccessRsp(payClient.buildContractStr(response.getPreSignNo()));
       }
       public static boolean validResponse(BaseGwRspWithSign rsp) {
           return rsp != null && "000000".equals(rsp.getResultCode());
       }
       /**
        * 预签约接口请求参数组装，商户请根据业务自行实现
        */
       private PreSignRequestV2 getPreSignRequestV2() {
           return PreSignRequestV2.builder().appId(MercConfigUtil.APP_ID) // appId，需要配置为与商户绑定的正确的appId
               .mercContractCode("pay-example-" + System.currentTimeMillis()) // 签约协议号，每次请求都要变，请将pay-example-修改为商户自己的订单前缀
               .mercNo(MercConfigUtil.MERC_NO) // 商户号
               .planId("100") // 协议模板ID，该模板ID是商户在向华为支付提交代扣权限申请时由华为支付生成。请填写正确的协议模板ID。
               .callbackUrl("https://www.xxxxxx.com/hw/sign/callback") // 回调通知地址，通知URL必须为直接可访问的URL，要求为https地址。最大长度为512。请替换为格式正确的结果通知回调地址。
               .build();
       }
   }
   ```

### 拉起华为支付签约收银台（端侧开发）

商户客户端使用[contractStr](../harmonyos-references/payment-model.md#contractstr)作为参数调用[requestContract](../harmonyos-references/payment-paymentservice.md#requestcontract)接口拉起Payment Kit签约收银台。

当接口通过.then()方法返回时，则表示当前订单支付成功，通过.catch()方法返回表示订单支付失败。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/errorcode-payment.md)。示例代码如下：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestContractPromise() {
    // 请使用开发者真实的入参信息（contractStr）
    const contractStr = '{"appId":"***","preSignNo":"***"}';
    paymentService.requestContract(this.context, contractStr)
      .then(() => {
        // 签约成功
        console.info('succeeded in signing');
      })
      .catch((error: BusinessError) => {
        // 签约失败
        console.error(`failed to sign, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestContractPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestContractPromise();
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

**说明** 

* 如果用户未提前登录，系统会自动拉起华为账号登录页面让用户登录。若用户取消登录或登录失败，则签约流程将中断。
* 签约成功，不建议以客户端返回作为用户的签约结果，需以服务器接收到的结果通知或者查询API返回为准。

### 签约结果回调通知（服务器开发）

支付成功后华为支付服务器会调用开发者提供的回调接口，将签约信息返回给开发者服务器，回调详细信息按商户模式请参见[签约结果回调通知](../harmonyos-references/payment-withhold-sign-notify.md)。

**说明** 

回调接口是开发者调用预签约时的入参字段callbackUrl或签约模板配置的回调地址。

为保证信息合法性，商户服务器需要对返回的签约信息进行[SM2验签](../harmonyos-references/payment-rest-overview.md#验签规则)，验签注意事项：

1. 需直接使用通知的完整内容进行验签。
2. 验签前需要对返回数据进行排序拼接，sign字段是签名值，排序拼接后的待验签内容需要排除sign字段。
3. 验签公钥使用[华为支付证书](payment-certificates-config.md#华为支付证书)。

## 延伸和拓展

当开发者完成上述能力之后还可以调用以下API接口完成订单相关操作。

### 直连商户

[申请免密代扣](../harmonyos-references/payment-withhold-apply.md)、[查询签约订单](../harmonyos-references/payment-withhold-query-contractcode.md)、[查询代扣订单](../harmonyos-references/payment-withhold-query-merc-order.md)、[申请解约](../harmonyos-references/payment-withhold-unsign.md)、[申请退款](../harmonyos-references/payment-withhold-refunds.md)、[查询退款订单](../harmonyos-references/payment-withhold-query-merc-refund-order.md)、[查询对账单](../harmonyos-references/payment-query-trade-bill.md)、[查询结算账单](../harmonyos-references/payment-query-settle-bill.md)。

### 服务商

[申请免密代扣](../harmonyos-references/payment-partner-withhold-apply.md)、[查询签约订单](../harmonyos-references/payment-partner-withhold-query-contractcode.md)、[查询代扣订单](../harmonyos-references/payment-partner-withhold-query-merc-order.md)、[申请解约](../harmonyos-references/payment-partner-withhold-unsign.md)、[申请退款](../harmonyos-references/payment-partner-withhold-refunds.md)、[查询退款订单](../harmonyos-references/payment-partner-withhold-query-merc-refund-order.md)、[查询对账单](../harmonyos-references/payment-partner-agent-query-trade-bill.md)、[查询结算账单](../harmonyos-references/payment-partner-agent-query-settle-bill.md)。
