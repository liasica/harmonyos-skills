---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-ifaa
title: IFAA免密认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > 免密认证 > IFAA免密认证
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:24+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:39f81510cc6b61ee432e59e84ccf903faf1c36fd88397a0d6fbb4cca03a986ad
---

## 场景介绍

* 开通：提供移动端开通生物特征（指纹/3D人脸）IFAA免密认证的能力。使用用户已有的生物特征类型进行开通，会开通移动端对应生物特征类型的IFAA免密认证能力。
* 认证：提供移动端认证生物特征（指纹/3D人脸）IFAA免密认证的能力。使用用户已开通的生物特征进行认证，认证成功；使用未开通的生物特征进行认证，认证失败。
* 注销：提供移动端注销生物特征（指纹/3D人脸）IFAA免密认证的能力。使用用户已开通的生物特征类型进行注销，会注销移动端对应生物特征类型的IFAA免密认证能力。

## 约束与限制

* 应用已接入IIFAA联盟，可以从IIFAA中心服务器获取签名数据。
* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```typescript
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
* IFAA服务会将匿名化的指纹ID和面容ID等个人信息返回至应用，以提供绑定具体生物特征的免密认证能力。应用将个人信息上云前，需要向用户明示并且取得同意，详细请参考[个人数据处理说明](onlineauthentication-personal-data-processing-description.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/hna1rZtHSW6UHlcMLO2qnw/zh-cn_image_0000002742003503.png)

**注册流程说明：**

1. 应用客户端调用[getAnonymousIdSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaagetanonymousidsync)接口通过用户标识获取设备标识ID。
2. 应用客户端向应用服务端获取开通数据。
3. 应用客户端调用[register](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaregister)接口注册，获取注册报文。
4. 应用客户端将注册报文上报至应用服务端，应用服务端验证后返回结果。

**认证流程说明：**

1. 应用客户端调用[getAnonymousIdSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaagetanonymousidsync)接口通过用户标识获取设备标识ID。
2. 应用客户端向应用服务端获取认证数据。
3. 应用客户端调用[preAuthSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaapreauthsync)接口获取免密支付challenge。
4. 应用客户端请求身份认证，完成生物特征认证。
5. 应用客户端调用[auth](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaauth)接口进行IFAA认证，获取认证报文。
6. 应用客户端将认证报文上报至应用服务端，应用服务端验证后返回结果。

**关闭流程说明：**

1. 应用客户端调用[getAnonymousIdSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaagetanonymousidsync)接口通过用户标识获取设备标识ID。
2. 应用客户端向应用服务端获取注销数据。
3. 应用客户端调用[deregisterSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaderegistersync)接口注销IFAA。

## 接口说明

以下是开通、认证、注销的所需要的接口，具体API说明详见[接口文档](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaregister)。

| 接口名 | 描述 |
| --- | --- |
| [register](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaregister)(registerData: Uint8Array): Promise<Uint8Array> | 开通IFAA免密认证，使用Promise异步回调。 |
| [auth](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaauth)(authToken: Uint8Array, authData: Uint8Array): Promise<Uint8Array> | IFAA免密认证，使用Promise异步回调。 |
| [deregisterSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaderegistersync)(deregisterData: Uint8Array): void | 注销IFAA免密认证，同步返回结果。 |
| [getAnonymousIdSync](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaagetanonymousidsync)(userToken: Uint8Array): Uint8Array | 获取IFAA免密认证的匿名化ID，同步返回结果。 |

## 开发步骤

1. 导入相关模块。

   ```typescript
   import { ifaa } from '@kit.OnlineAuthenticationKit';
   import { userAuth } from '@kit.UserAuthenticationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 开通IFAA免密认证能力。

   ```typescript
   try {
     // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
     let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(userTokenFp);
     console.info('Succeeded in getting anonymous id, result:', getAnonIdResult);
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
   }
   try {
     // 开发者需使用getAnonymousIdSync从服务端获取签名后的开通数据
     // 开发者将开通数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvRegisterFp，再使用ifaa.register接口。
     let registerPromise: Promise<Uint8Array> = ifaa.register(tlvRegisterFp);
     registerPromise.then(registerResult => {
       console.info('Succeeded in doing register, result:', registerResult);
       // 开通成功，开发者获取ifaa.register结果并处理。
       // ...
     }).catch((err: BusinessError) =>{
       console.error(`Failed to call register. Code: ${err.code}, message: ${err.message}`);
       // 开通失败，开发者获取ifaa.register错误并处理。
     });
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to register. Code is ${err.code}, message is ${err.message}`);
   }
   ```
3. 使用IFAA免密认证能力。

   ```typescript
   // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
   let getAnonIdResult: Uint8Array;
   try {
     getAnonIdResult = ifaa.getAnonymousIdSync(userTokenFp);
     console.info('Succeeded in getting anonymous id, result:', getAnonIdResult);
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
   }

   // 开发者需使用getAnonymousIdSync从服务端获取签名后的认证数据
   // 获取此次免密支付的challenge
   let ifaaChallenge: Uint8Array = new Uint8Array([0]);
   try {
     ifaaChallenge = ifaa.preAuthSync();
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to pre auth. Code is ${err.code}, message is ${err.message}`);
   }
   let authParam: userAuth.AuthParam = {
     challenge: ifaaChallenge,
     authType: [userAuth.UserAuthType.FINGERPRINT],
     authTrustLevel: userAuth.AuthTrustLevel.ATL4
   };

   try {
     let userAuthInstance = userAuth.getUserAuthInstance(authParam, {title: ' '});
     userAuthInstance.on('result', {
       onResult(result) {
         let authToken = result.token;
         try {
           // 生物特征认证成功后，调用IFAA认证
           console.info('IFAA auth start');
           // 开发者将认证数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvAuthFp，再使用ifaa.authSync接口。
           // 开发者根据业务需求选择同步/异步接口
           let authResult: Uint8Array = ifaa.authSync(authToken, tlvAuthFp);
           console.info('Succeeded in auth, result:', authResult);
           // 开发者处理authResult
           // ...
         } catch (error) {
           const err: BusinessError = error as BusinessError;
           console.error(`Failed to call auth. Code is ${err.code}, message is ${err.message}`);
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
4. 注销IFAA免密认证能力。

   ```typescript
   // 开发者根据IIFAA协议构造TLV入参，转换为Uint8Array，得到userTokenFp，再使用ifaa.getAnonymousIdSync接口。
   try {
     let getAnonIdResult: Uint8Array = ifaa.getAnonymousIdSync(userTokenFp);
     console.info('Succeeded in getting anonymous id, result:', getAnonIdResult);
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to get anonymous id. Code is ${err.code}, message is ${err.message}`);
   }

   // 开发者需使用getAnonymousId的结果从服务端获取签名后的注销数据
   // 开发者将注销数据（IIFAA协议的TLV格式）转换为Uint8Array，得到tlvDeregisterRp，再使用ifaa.deregisterSync接口。
   try {
     ifaa.deregisterSync(tlvDeregisterRp);
     // ...
   } catch (error) {
     const err = error as BusinessError;
     console.error(`Failed to deregister. Code is ${err.code}, message is ${err.message}`);
     // ...
   }
   ```
