---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-real-name-face-verification
title: 人脸核身实人验证场景
breadcrumb: 指南 > 应用服务 > Payment Kit（鸿蒙支付服务） > 用户身份验证服务 > 人脸核身实人验证场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:59+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:35a7e94ad11fcbdfd3b470d3022e43ac968582d18bbe7c5590f9a17e8cd1918f
---

## 场景介绍

从5.1.1(19)版本开始，新增支持人脸核身实人验证场景。

开发者需要验证当前应用/元服务操作的用户的信息且验证是否为用户本人操作时，可接入人脸核身实人验证能力。

支持商户模型：不涉及

人脸核身实人验证页面展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/yIbqRQr5SvasS1QM2Y7i2w/zh-cn_image_0000002706835118.png)

## 约束与限制

人脸核身实人验证能力支持Phone、Tablet设备，从6.1.1(24)版本开始，新增支持PC/2in1设备。

为确保人脸识别的准确性，必须在全屏模式下调用人脸核身实人验证功能。

## 接入流程

华为支付人脸核身实人验证接入流程如下：

| 步骤 | 说明 |
| --- | --- |
| 开发准备 | 请先完成开发准备后再进行下面的开发接入。  - [端侧应用配置](payment-config-app-identity-info.md)  - [用户身份验证服务接入准备](payment-real-name-preparations.md) |
| 接入人脸核身实人验证 | 根据人脸核身实人验证场景[开发步骤](payment-real-name-face-verification.md#开发步骤)完成接入。 |

## 业务流程

开发者通过接入人脸核身实人验证能力，可以简便快捷的实现用户信息验证及本人操作的验证。具体接入流程如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/CK__f1CpSUWdFydA4cNWUQ/zh-cn_image_0000002736314225.png)

1. 开发者客户端收集用户实名信息加密后请求开发者服务端发起人脸核身实人预验证。
2. 开发者服务端请求Payment Kit服务端[人脸核身实人预验证](../harmonyos-references/payment-api-common-face-verifactaion-preverify.md)接口获取预验证ID（preVerifyId）。
3. Payment Kit服务端解密并获取请求传入的用户实名信息进行验证处理。
4. Payment Kit服务端验证用户实名信息通过后，返回预验证ID给开发者服务端。
5. 开发者服务端返回预验证信息给开发者客户端。
6. 开发者客户端使用预验证ID调用[startFaceVerification](../harmonyos-references/payment-realnameservice.md#startfaceverification)接口拉起人脸核身实人验证页面。
7. Payment Kit客户端展示验证信息。
8. 用户同意并完成人脸验证，Payment Kit客户端请求Payment Kit服务端处理验证。
9. Payment Kit服务端完成人脸验证处理并返回验证结果给Payment Kit客户端。
10. Payment Kit客户端将验证结果展示给用户。
11. Payment Kit客户端同步返回身份信息验证ID给开发者客户端。
12. 开发者客户端使用身份信息验证Id请求开发者服务端查询身份信息验证结果。
13. 开发者服务端请求Payment Kit服务端[人脸核身实人验证](../harmonyos-references/payment-api-common-face-verifactaion-result.md)接口查询验证结果。
14. Payment Kit服务端返回人脸核身实人验证结果给开发者服务端。
15. 开发者服务端将人脸核身实人验证结果返回给开发者客户端，开发者客户端根据验证结果进行下一步业务处理。

## 接口说明

拉起用户人脸核身实人验证页面的接口。具体API说明详见[接口文档](../harmonyos-references/payment-realnameservice.md#startfaceverification)。

| 接口名 | 描述 |
| --- | --- |
| startFaceVerification(context: common.UIAbilityContext | common.UIExtensionContext, preVerifyId: string): Promise<string>; | 拉起用户人脸核身实人验证（人脸验证）页面。 |

## 开发步骤

### 发起人脸核身预验证（服务器开发）

调用[人脸核身实人预验证](../harmonyos-references/payment-api-common-face-verifactaion-preverify.md)接口获取预验证ID后返回给端侧拉起人脸核身实人验证页面。服务器开发步骤可参考[实名信息验证/授权场景](payment-real-name-verification.md#实名信息验证)服务器开发实现。

### 拉起人脸核身实人验证（端侧开发）

开发者客户端使用后端服务返回的预验证ID作为参数调用[startFaceVerification](../harmonyos-references/payment-realnameservice.md#startfaceverification)接口拉起用户人脸核身实人验证页面。当接口通过.then()方法返回时，则表示当前接口请求成功，通过.catch()方法返回表示接口请求失败。当此次请求有异常时，可通过**error.code**获取错误码，错误码相关信息请参见[错误码](../harmonyos-references/errorcode-payment.md)。示例代码如下：

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { realNameService } from '@kit.PaymentKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
  requestStartFaceVerificationPromise() {
    // 请使用开发者真实的预验证ID（preVerifyId）
    let preVerifyId = '后端服务获取有效的预验证ID';
    realNameService.startFaceVerification(this.context, preVerifyId)
      .then((verifyResultId: string ) => {
        // 人脸验证成功
        console.info(`succeeded in face verifying, verifyResultId: ${verifyResultId}`);
      })
      .catch((error: BusinessError) => {
        // 人脸验证失败
        console.error(`failed to face verification, error.code: ${error.code}, error.message: ${error.message}`);
      });
  }

  build() {
    Column() {
      Button('requestStartFaceVerificationPromise')
        .type(ButtonType.Capsule)
        .width('50%')
        .margin(20)
        .onClick(() => {
          this.requestStartFaceVerificationPromise();
        })
      }
    .width('100%')
    .height('100%')
  }
}
```

### 查询人脸核身实人验证结果（服务器开发）

调用[人脸核身实人验证](../harmonyos-references/payment-api-common-face-verifactaion-result.md)接口查询验证结果。
