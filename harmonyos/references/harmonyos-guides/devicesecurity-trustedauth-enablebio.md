---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-enablebio
title: 开通生物特征认证能力
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 生物特征绑定、认证与解绑 > 开通生物特征认证能力
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:41f858b3419022c2ff185f0ecfcb95ba67ed092c7e58f6b4b6c4008636517a25
---

## 场景介绍

1. 本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。
2. 人脸认证功能需设备具备**3D人脸识别能力**，可通过调用[查询支持的认证能力](obtain-supported-authentication-capabilities.md)确认设备是否支持3D人脸识别。当前仅支持绑定一个指纹或人脸用于支付认证。
3. 本功能需企业开发者应用服务器端完成接口接入，以配合端云协同认证流程。

## 约束与限制

本功能在6.1.1(24)之前版本仅在手机设备支持。对于6.1.1(24)及之后版本，本功能在手机设备、部分PC/2in1、部分Tablet设备支持。人脸认证功能仅支持具备**3D人脸识别能力**的设备，目前仅支持绑定一个指纹/人脸用于支付认证，且需企业开发者应用服务器端同步接入配合端云协同认证。通过用户认证服务提供的接口[查询支持的认证能力](obtain-supported-authentication-capabilities.md)，可确认设备是否支持3D人脸。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/rtHl2LxdRlGGA-ZMTPBY_w/zh-cn_image_0000002742123449.jpg)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-trusted-auth-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [trustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationtrustedauthentication)(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<[AuthToken](../harmonyos-references/devicesecurity-trusted-auth-api.md#authtoken)> | 数字盾密码认证 |
| [getBiometricAuthToken](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationgetbiometricauthtoken)(operType: [OperateType](../harmonyos-references/devicesecurity-trusted-auth-api.md#operatetype), tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken> | 获取生物特征绑定完成后生成的authToken信息。 |

## 开通生物特征认证能力界面介绍

如图表示开通人脸认证时对应的UI界面示例，当密码认证通过后，则会拉起系统人脸认证界面进行人脸信息绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/xSnMD6eDSciSH27xtZcohA/zh-cn_image_0000002712244536.png)

## 开发步骤

1. 导入huks 、userAuth 、trustedAuthentication和相关依赖模块。

   ```typescript
   import { resourceManager } from '@kit.LocalizationKit'
   import { huks } from '@kit.UniversalKeystoreKit';
   import { userAuth } from '@kit.UserAuthenticationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   import { common } from '@kit.AbilityKit';
   ```
2. 通过用户认证服务提供的接口[查询设备是否已录入相关凭证](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)。
3. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，初始化签名会话。
4. 调用数字盾密码认证接口[trustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationtrustedauthentication)发起生物特征认证前的密码认证申请。

   ```typescript
   async PwdVerify(challenge: Uint8Array, assetName: string): Promise<trustedAuthentication.AuthToken> {
     try {
       let resArray: Uint8Array = await AssetUtils.QueryDataFromAssetStore(assetName);
       let credentialID: bigint = CryptoUtils.uint8ArrayToBigInt(resArray);
       const context = AppStorage.get('context') as Context;
       const buffer: ArrayBuffer = await CryptoUtils.ImportImage();
       const label: trustedAuthentication.TUILable = {
         image: buffer,
         title: context.resourceManager.getStringSync($r('app.string.ShieldPwVerification').id)
       }
       const result = await trustedAuthentication.trustedAuthentication(challenge, credentialID, label);
       hilog.info(DOMAIN, 'testTag', 'DigitalShield password verification success：', result.authToken.length,
         result.authToken);
       return result;
     } catch (error) {
       hilog.error(DOMAIN, 'testTag', 'DigitalShield password verification failed：', error);
       throw new Error('DigitalShield password verification failed：' + (error as BusinessError).message);
     }
   }
   ```
5. 通过用户认证服务提供的接口，拉起生物特征认证控件并[发起认证](start-authentication.md)。
6. 当订阅的生物认证结果获取到后，将数字盾密码认证结果和生物特征认证结果统一整合，发起生物特征绑定请求。

   ```typescript
   try {
     let session = await TrustedAuth.SignInit();
     hilog.info(DOMAIN, 'testTag', 'Finish Signature Initialization');
     const tuiAuthToken: Uint8Array =
       await TrustedAuth.GetTUIAuthTokenBeforeBioVerify('placeholder', session, TUI_BIND_FACE, 'pin_label1'); // 步骤6密码认证获取的authToken
     let bioAuthToken: Uint8Array =
       await TrustedAuth.UserAuthBeforeSign(session, TUI_BIND_FACE); // 步骤7生物特征认证获取的authToken
     let operType = trustedAuthentication.OperateType.OPERATE_TYPE_BIOMETRIC_AUTH;
     let resignAuthToken =
       await trustedAuthentication.getBiometricAuthToken(operType, tuiAuthToken, bioAuthToken);
     let inputdata = 'placeholder';
     await TrustedAuth.bindFaceID(session.handle, resignAuthToken.authToken, inputdata)
     // ...
   } catch (error) {
     hilog.error(DOMAIN, 'testTag', 'Bind Face Fail:', error);
     // ...
   }
   ```
7. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md), 对返回生物特征绑定对应的authToken数据进行签名，并结束会话。
8. 企业开发者应用可将签名获取的生物特征进行验签校验，并将生物特征credential信息与账号信息在服务器端绑定。
