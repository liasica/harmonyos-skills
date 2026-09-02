---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-soter
title: SOTER免密认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > 免密认证 > SOTER免密认证
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:d160d2fa62b06cc0d1294e6b338557ecaa5b16a984966043bbc37293b2475aa5
---

SOTER旨在提供一套生物认证平台和标准，使得业务可以采用设备上的传感器（如人脸传感器/指纹传感器）进行安全、高效的免密登录、免密支付等操作，当前已广泛应用于微信小程序/公众号、指纹支付等业务场景。

## 场景介绍

用户可以利用生物特征来代替传统的密码验证，实现免密认证。

* 开通：提供移动端开通SOTER生物特征（指纹/3D人脸）免密认证的能力。
* 认证：提供移动端采用生物特征（指纹/3D人脸）进行SOTER免密认证的能力。
* 注销：提供移动端注销SOTER生物特征（指纹/3D人脸）免密认证的能力。

## 约束与限制

* 开发者应用需要部署SOTER服务器。
* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```typescript
  import { soter } from '@kit.OnlineAuthenticationKit';
  import { userAuth } from '@kit.UserAuthenticationKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  // ...
  function getAvailableStatus() {
    try {
      // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
      userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
      console.info('current auth trust level is supported');
    } catch (error) {
      const err: BusinessError = error as BusinessError;
      console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
    }
  }
  ```
* 移动端设备使用此服务时需要处于联网状态。
* SOTER服务会将匿名化的指纹ID和面容ID等个人信息返回至应用，以提供绑定具体生物特征的免密认证能力。应用将个人信息上云前，需要向用户明示并且取得同意，详细请参考[个人数据处理说明](onlineauthentication-personal-data-processing-description.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/u8XTeY4oQ6S0Skom3KGmcQ/zh-cn_image_0000002706674378.png)

**生成应用密钥流程说明：**

1. 应用客户端调用[generateAppSecureKey](../harmonyos-references/onlineauthentication-soter-api.md#sotergenerateappsecurekey)接口生成应用密钥。
2. 应用客户端将应用密钥上传至应用服务端，应用服务端校验后返回校验结果。

**生成认证密钥流程说明：**

1. 应用客户端调用[generateAuthKey](../harmonyos-references/onlineauthentication-soter-api.md#sotergenerateauthkey)接口生成认证密钥。
2. 应用客户端将认证密钥上传至应用服务端，应用服务端校验后返回校验结果。

**认证流程说明：**

1. 应用客户端向应用服务端请求数据。
2. 应用客户端调用[generateChallengeSync](../harmonyos-references/onlineauthentication-soter-api.md#sotergeneratechallengesync)接口生成challenge。
3. 应用客户端请求身份认证，完成生物特征认证。
4. 应用客户端调用[signWithAuthKeySync](../harmonyos-references/onlineauthentication-soter-api.md#sotersignwithauthkeysync)接口进行SOTER认证，获取签名结果。
5. 应用客户端将签名结果上传至应用服务端，应用服务端校验后返回校验结果。

**关闭免密支付流程说明：**

应用客户端调用[deleteAuthKey](../harmonyos-references/onlineauthentication-soter-api.md#soterdeleteauthkey)接口删除认证密钥。

## 接口说明

以下是开通、认证、注销的所需要的接口，具体API说明详见[接口文档](../harmonyos-references/onlineauthentication-soter-api.md#sotergenerateappsecurekey)。

| 接口名 | 描述 |
| --- | --- |
| [generateAppSecureKey](../harmonyos-references/onlineauthentication-soter-api.md#sotergenerateappsecurekey)(keyType: [KeyType](../harmonyos-references/onlineauthentication-soter-api.md#keytype)): Promise<Uint8Array> | 生成App应用密钥，使用Promise异步回调。 |
| [generateAuthKey](../harmonyos-references/onlineauthentication-soter-api.md#sotergenerateauthkey)(keyAlias: string, keyType: [KeyType](../harmonyos-references/onlineauthentication-soter-api.md#keytype)): Promise<[SignedResult](../harmonyos-references/onlineauthentication-soter-api.md#signedresult)> | 生成authKey，使用Promise异步回调。 |
| [generateChallengeSync](../harmonyos-references/onlineauthentication-soter-api.md#sotergeneratechallengesync)(keyAlias: string): Uint8Array | 生成Challenge，同步返回结果。 |
| [signWithAuthKeySync](../harmonyos-references/onlineauthentication-soter-api.md#sotersignwithauthkeysync)(keyAlias: string, authToken: Uint8Array, info: string): [SignedResult](../harmonyos-references/onlineauthentication-soter-api.md#signedresult) | SOTER免密认证，同步返回签名的报文。 |
| [deleteAuthKey](../harmonyos-references/onlineauthentication-soter-api.md#soterdeleteauthkey)(keyAlias: string): Promise<void> | 删除AuthKey，使用Promise异步回调 |

## 开发步骤

1. 导入SOTER模块。

   ```typescript
   import { soter } from '@kit.OnlineAuthenticationKit';
   import { userAuth } from '@kit.UserAuthenticationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 生成应用密钥和认证密钥用于后续的开通、认证流程。

   ```typescript
   let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 加密类型，只支持ECC_P256
   let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名

   // 生成应用密钥
   try {
     let appSecureKey: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
     // ...
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to generate app secure key. Code is ${err.code}, message is ${err.message}`);
     // ...
   }
   // 生成authKey
   try {
     let authKey: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to generate auth key. Code is ${err.code}, message is ${err.message}`);
   }
   ```
3. 使用认证密钥签名，实现SOTER免密认证。

   ```typescript
   let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 加密类型，只支持ECC_P256
   let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名
   let info: string = 'Message to be signed.'; // info需要开发者的三方应用服务器下发，SOTER服务完成签名后需要重新上传给三方应用服务器

   // 获取此次免密支付的challenge
   let soterChallenge: Uint8Array = new Uint8Array([0]);
   try {
     soterChallenge = soter.generateChallengeSync(keyAlias);
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to generate challenge. Code is ${err.code}, message is ${err.message}`);
   }
   let authParam: userAuth.AuthParam = {
     challenge: soterChallenge,
     authType: [userAuth.UserAuthType.FINGERPRINT],
     authTrustLevel: userAuth.AuthTrustLevel.ATL4
   };
   // 使用preAuthResult请求身份认证
   try {
     let userAuthInstance = userAuth.getUserAuthInstance(authParam, {title: ' '});
     // 未获取到authToken则会返回错误码1。
     userAuthInstance.on('result', {
       onResult(result) {
         let authToken = result.token;
         try {
           // 生物特征认证成功后，调用soter认证
           console.info('soter auth start');
           // 使用soter.signWithAuthKeySync接口为待认证数据签名。开发者根据业务需求选择同步/异步接口。
           let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info);
           console.info('Succeeded in doing authSyn authResult');
           // 开发者处理authResult
           // ...
         } catch (err) {
           console.error(`Failed to signWithAuthKeySync. Code: ${err.code}, message: ${err.message}`);
           // ...
         }
       }
     });
     userAuthInstance.start();
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to user auth. Code is ${err.code}, message is ${err.message}`);
   }
   ```
4. 关闭免密认证时，删除认证密钥。

   ```typescript
   let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名
   try {
     soter.deleteAuthKey(keyAlias);
     // ...
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to delete auth key. Code is ${err.code}, message is ${err.message}`);
     // ...
   }
   ```
