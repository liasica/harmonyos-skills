---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-verifybybio
title: 生物特征认证交易
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 生物特征绑定、认证与解绑 > 生物特征认证交易
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:22+08:00
doc_updated_at: 2026-08-03
content_hash: sha256:c14651ac7951b20c4d4868cf48382c70b4894759a5bbf3d6c0d1a197b85f2132
---

## 场景介绍

在完成对应生物特征认证能力开通后，用户即可通过已绑定的生物特征（人脸或指纹）完成认证交易。

## 约束与限制

1. 本功能在6.1.1(24)之前版本仅支持Phone；6.1.1(24)及之后版本，新增支持具备TUI能力的PC/2in1、具备TUI能力的Tablet。可通过接口[checkConfirmUITextFormat](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationcheckconfirmuitextformat)查询设备是否具备TUI能力。不支持的设备在调用数字盾服务相关业务接口时，返回错误码1019100016。
2. 当前仅支持绑定一个指纹或人脸用于支付认证。
3. 本功能需企业开发者应用服务器端完成接口接入，以配合端云协同认证流程。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/wF-TFso0T_KB94T5Ddy-HA/zh-cn_image_0000002742003489.jpg)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/errorcode-devicesecurity-trusted-auth.md)。

| 接口名 | 描述 |
| --- | --- |
| [procContentAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationproccontentauthentication)(challenge: Uint8Array, authID: bigint, authMsg: AuthReqParams, label: TUILable): Promise<AuthToken> | 交易信息处理接口。 |
| [getBiometricAuthToken](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationgetbiometricauthtoken)(operType: OperateType, tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken> | 获取生物特征交易认证的authToken信息。 |

## 生物特征认证交易界面介绍

如图表示使用人脸进行交易认证对应的UI界面示例，当用户确认交易信息内容后，则会拉起系统人脸认证界面完成对应生物特征认证交易。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/cvf7Py8BRoaD75zrLBWgog/zh-cn_image_0000002712404502.png)

## 开发步骤

1. 导入huks 、userAuth 、trustedAuthentication 和相关依赖模块。

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
2. 首先开发者需要在服务器查询对应账户是否已开通对应生物特征认证能力，在确认开通后方可发起生物特征认证交易。
3. 发起生物特征认证交易前，需从服务器获取当前账号在[设置数字盾密码](devicesecurity-trustedauth-setpwd.md)时获取的authID。
4. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，初始化签名会话。
5. 调用数字盾交易信息处理接口[procContentAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthenticationproccontentauthentication)发起生物特征认证前的交易信息确认申请。

   ```typescript
   async FaceAuthContent(indata: string, challenge: Uint8Array,
     assetName: string): Promise<trustedAuthentication.AuthToken> {
     try {
       let enrolledState = userAuth.getEnrolledState(userAuth.UserAuthType.FACE); // 获取系统人脸录入状态
       hilog.info(0x0000, 'testTag',
         `get current enrolled state success enrolledState = ${JSON.stringify(enrolledState)}`);
       let resArray: Uint8Array = await AssetUtils.QueryDataFromAssetStore(assetName);
       let credentialID: bigint = CryptoUtils.uint8ArrayToBigInt(resArray); // 实际填充为从服务器获取到的账号对应的credentialID值
       const context = AppStorage.get('context') as Context;
       const buffer: ArrayBuffer = await CryptoUtils.ImportImage(); // 获取应用要在TUI界面展示的logo图片
       const reqParams: trustedAuthentication.AuthReqParams = {
         reqType: trustedAuthentication.AuthType.AUTH_TYPE_FACE,
         authContent: indata.split('\n') // 实际使用时填充为交易信息，每一行交易信息为其中的一个字符串成员
       }
       const label: trustedAuthentication.TUILable = {
         image: buffer,
         title: context.resourceManager.getStringSync($r('app.string.FaceVerification').id)
       }
       const result = await trustedAuthentication.procContentAuthentication(challenge, credentialID, reqParams, label);
       hilog.info(0x0000, 'testTag', 'Face Verification Success：', result.authToken);
       return result;
     } catch (error) {
       hilog.error(0x0000, 'testTag', 'Face Verification Fail：', error);
       throw new Error('Face Verification Fail：' + (error as BusinessError).message);
     }
   }
   ```
6. 通过用户认证服务提供的接口，拉起生物特征认证控件并[发起认证](start-authentication.md)。
7. 当订阅的生物认证结果获取到后，将数字盾交易信息确认结果和生物特征认证结果统一整合，发起生物特征认证交易请求。

   ```typescript
    try {
      let session = await TrustedAuth.SignInit();
      hilog.info(DOMAIN, 'testTag', 'Signature Initialization success');
      let indata: string =
        this.resourceManager.getStringSync($r('app.string.Recipient').id) + ':' + this.receiver + '\n' +
        this.resourceManager.getStringSync($r('app.string.AccountNumber').id) + ':' + this.receiveAccount + '\n' +
        this.resourceManager.getStringSync($r('app.string.TradingAmount').id) + ':' + this.tradingAmount; // 签名内容与步骤5通过TUI展示的交易信息一致
      const tuiAuthToken: Uint8Array =
        await TrustedAuth.GetTUIAuthTokenBeforeBioVerify(indata, session, TUI_CONTENT_FACE_VERIFY, 'pin_label1'); // 步骤5获取的交易信息确认authToken
      let bioAuthToken: Uint8Array =
        await TrustedAuth.UserAuthBeforeSign(session, TUI_CONTENT_FACE_VERIFY); // 步骤6获取的生物特征认证authToken
      let operType = trustedAuthentication.OperateType.OPERATE_TYPE_CONTENT_AUTH;
      let resignAuthToken =
        await trustedAuthentication.getBiometricAuthToken(operType, tuiAuthToken, bioAuthToken);
      await TrustedAuth.HuksSignAndVerify(indata, session, resignAuthToken.authToken) // 调用HUKS签名，实际使用时验签请通过服务器导出的证书完成。
      // ...
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', 'Face Verification Fail:', error);
      // ...
    }
   ```
8. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md), 对返回的authToken数据和交易信息明文进行签名，并结束签名会话。
9. 企业开发者应用在交易信息验签通过后，可在应用对应服务器比对已绑定的生物特征凭证（credential）与当前交易认证采集的生物特征标识符（credential ID），确保账号绑定的生物特征信息与交易请求认证使用的生物特征信息的一致性。
