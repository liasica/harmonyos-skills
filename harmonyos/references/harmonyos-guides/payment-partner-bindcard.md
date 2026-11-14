---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-partner-bindcard
title: 引导用户绑卡场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 引导用户绑卡场景
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:27+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:10f26b8853ce597eaedfebac2c713cc8e681cb48637e32490d6d50aeda6ba2dd
---

## 场景介绍

从5.0.5(17)版本开始，新增支持引导用户绑卡场景。

支持拉起绑卡页面，结合商户营销活动，有效引导用户完成绑卡操作。例如商户针对银行卡开展某营销活动，需要引导用户拉起绑卡页面完成银行卡绑定。

支持商户模型：直连商户、平台类商户、服务商

引导用户绑卡页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/Ih0JhgvoQ4-gdJcfgn-teQ/zh-cn_image_0000002817507667.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=37013EE8B15198607CD4277BACF42EE2860B20BAA449FC6294FA01FF6984E1E8)

## 提供绑卡跳转应用信息

开发者需与华为支付业务侧沟通（合作咨询可[点击此处](payment-service-support.md)）后提供以下应用信息：

| 应用信息 | 是否必选 | 说明 |
| --- | --- | --- |
| AppID | 是 | 应用的AppID（在[HarmonyOS 开发者中心](https://developer.huawei.com/consumer/cn/hdc-console)平台，点击“应用管理 > 基础信息”，在基本信息页面获取“APP ID”的值）。 |

## 业务流程

开发者接入引导用户绑卡，具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/EDQ9tsKhQqyZJt_HbVn6wA/zh-cn_image_0000002788308236.png?HW-CC-KV=V1&HW-CC-Date=20261114T004826Z&HW-CC-Expire=31536000000&HW-CC-Sign=AE6D21E648BD08A4DC8907CC76E9FE00BC4E7D553BB503D5B813B5DBDA4AA005)

**场景1：用户取消绑卡**

1. 商户客户端调用[requestBindCard](../harmonyos-references/payment-paymentservice.md#requestbindcard)接口拉起用户绑卡页面。
2. Payment Kit客户端展示绑卡页面，商户客户端可根据用户不同处理场景完成后续流程。
3. 用户返回或取消绑卡。
4. Payment Kit客户端返回商户客户端并将绑卡结果一并返回，商户客户端根据绑卡结果完成后续业务处理。

**场景2：用户完成绑卡**

1. 商户客户端调用[requestBindCard](../harmonyos-references/payment-paymentservice.md#requestbindcard)接口拉起用户绑卡页面。
2. Payment Kit客户端展示绑卡页面，商户客户端可根据用户不同处理场景完成后续流程。
3. 用户通过绑卡页面完成绑卡操作，Payment Kit客户端会请求Payment Kit服务端处理绑卡。
4. Payment Kit服务端处理绑卡。
5. Payment Kit服务端将绑卡结果返回给Payment Kit客户端。
6. Payment Kit客户端展示绑卡结果页面。
7. 用户关闭绑卡页后，Payment Kit客户端返回商户客户端并将绑卡结果一并返回。
8. 商户客户端根据绑卡结果完成后续业务处理。

## 接口说明

拉起用户绑卡页面接口。具体API说明详见[接口文档](../harmonyos-references/payment-paymentservice.md#requestbindcard)。

| 接口名 | 描述 |
| --- | --- |
| requestBindCard(context: common.UIAbilityContext | common.UIExtensionContext): Promise<BindCardResult> | 拉起用户绑卡页面。 |

## 开发步骤

### 拉起绑卡页面（端侧开发）

商户客户端调用[requestBindCard](../harmonyos-references/payment-paymentservice.md#requestbindcard)接口拉起用户绑卡页面。

当接口通过.then()方法返回结果，则表示接口请求成功，通过.catch()方法返回异常表示请求失败。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/errorcode-payment.md)。

示例代码如下：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { paymentService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestBindCardPromise() {
    paymentService.requestBindCard(this.context)
      .then((bindCardResult: paymentService.BindCardResult) => {
        // 绑卡成功
          console.info(`succeeded in binding card. result: ${bindCardResult}`);
      })
      .catch((error: BusinessError) => {
        // 绑卡失败
        console.error(`failed to binding card, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestBindCardPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestBindCardPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```
