---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/devicesecurity-trustedauth-enablebio
title: 开通生物特征认证能力
breadcrumb: 指南 > 系统 > 安全 > Device Security Kit（设备安全服务） > 数字盾服务 > 生物特征绑定、认证与解绑 > 开通生物特征认证能力
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a1a18103f41978371c68d20b28d83c58e0a498cad3bea7aaff96c1e0f83764f6
---

## 场景介绍

在完成数字盾密码设置后，用户可以在数字盾密码认证成功后，将系统已录入的人脸或指纹信息与账户绑定，即开通生物特征认证能力。此后，用户即可通过已绑定的生物特征（人脸或指纹）快速完成转账交易的身份验证。

## 约束与限制

本功能目前仅在手机设备支持。人脸认证功能仅支持具备**3D人脸识别能力**的设备，目前仅支持绑定一个指纹/人脸用于支付认证，且需应用服务器端同步接入配合端云协同认证。通过用户认证服务提供的接口[查询支持的认证能力](obtain-supported-authentication-capabilities.md)，可确认设备是否支持3D人脸。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/UUicxttkTl2SxkoCgfi4sQ/zh-cn_image_0000002558764894.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053133Z&HW-CC-Expire=86400&HW-CC-Sign=0DD05E7193902BC8232C12F974AE47ACA31C0CF12D466259D138FC93964FD1E8)

## 接口说明

接口及使用方法请参见[API参考](../harmonyos-references/devicesecurity-trusted-auth-api.md)。

| 接口名 | 描述 |
| --- | --- |
| [trustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthentication)(challenge: Uint8Array, authID: bigint, label: TUILable): Promise<[AuthToken](../harmonyos-references/devicesecurity-trusted-auth-api.md#authtoken)> | 数字盾密码认证 |
| [getBiometricAuthToken](../harmonyos-references/devicesecurity-trusted-auth-api.md#getbiometricauthtoken)(operType: [OperateType](../harmonyos-references/devicesecurity-trusted-auth-api.md#operatetype), tuiAuthToken: Uint8Array, bioAuthToken: Uint8Array): Promise<AuthToken> | 获取生物特征绑定完成后生成的authToken信息 |

## 开通生物特征认证能力界面介绍

如图表示开通人脸认证时对应的UI界面示例，当密码认证通过后，则会拉起系统人脸认证界面进行人脸信息绑定。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/sl5NoNnbTKuGsWREZYThOA/zh-cn_image_0000002558605238.png?HW-CC-KV=V1&HW-CC-Date=20260429T053133Z&HW-CC-Expire=86400&HW-CC-Sign=24F89D923CACD994D78492919CD1CCC84EA63C75E15CF930AA3172F69B6B519B)

## 开发步骤

1. 导入huks 、userAuth 、trustedAuthentication和相关依赖模块。

   ```
   1. import { resourceManager } from '@kit.LocalizationKit'
   2. import { huks } from '@kit.UniversalKeystoreKit';
   3. import { userAuth } from '@kit.UserAuthenticationKit';
   4. import { BusinessError } from '@kit.BasicServicesKit';
   5. import { trustedAuthentication } from '@kit.DeviceSecurityKit';
   6. import { cryptoFramework } from '@kit.CryptoArchitectureKit';
   7. import { hilog } from '@kit.PerformanceAnalysisKit';
   8. import { common } from '@kit.AbilityKit';
   ```
2. 通过用户认证服务提供的接口[查询设备是否已录入相关凭证](../harmonyos-references/js-apis-useriam-userauth.md#userauthgetenrolledstate12)。
3. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md)，初始化签名会话。
4. 调用数字盾密码认证接口[trustedAuthentication](../harmonyos-references/devicesecurity-trusted-auth-api.md#trustedauthentication)发起生物特征认证前的密码认证申请。

   ```
   1. async function PwdVerify(challenge: Uint8Array, context: common.UIAbilityContext):Promise<trustedAuthentication.AuthToken> {
   2. try {
   3. const authID: bigint = 11842183505170721246n;//实际填充为从服务器获取到的账号对应的authID值
   4. const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
   5. const fileData : Uint8Array = await resourceMgr.getRawFileContent('test_logo_rgba.png'); //实际使用时请替换为应用要在TUI界面展示的logo图片名称
   6. const buffer = fileData.buffer;
   7. const label:trustedAuthentication.TUILable = {
   8. image: buffer as ArrayBuffer,
   9. title: "数字盾密码认证",
   10. }
   11. const result = await trustedAuthentication.trustedAuthentication(challenge, authID, label);
   12. return result;
   13. } catch (err) {
   14. hilog.error(0x0000, 'testTag', `Failed to trustedAuthentication, code:${err.code}, message:${err.message}`);
   15. throw new Error('Password verify failed:' + (err as BusinessError).message);
   16. }
   17. }
   18. const rand = cryptoFramework.createRandom();
   19. const len: number = 32;
   20. const challenge: Uint8Array = rand?.generateRandomSync(len)?.data;//实际使用时请替换为通过UniversalKeystoreKit初始化会话获取的challenge
   21. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   22. const authToken: trustedAuthentication.AuthToken = await PwdVerify(challenge, context);
   ```
5. 通过用户认证服务提供的接口，拉起生物特征认证控件并[发起认证](start-authentication.md)。
6. 当订阅的生物认证结果获取到后，将数字盾密码认证结果和生物特征认证结果统一整合，发起生物特征绑定请求。

   ```
   1. let tuiAuthToken = new Uint8Array(1024);//实际使用时请替换为步骤6密码认证获取的authToken
   2. let bioAuthToken = new Uint8Array(1024);//实际使用时请替换为步骤7生物特征认证获取的authToken
   3. let operType = trustedAuthentication.OperateType.OPERATE_TYPE_BIOMETRIC_AUTH;
   4. trustedAuthentication.getBiometricAuthToken(operType, tuiAuthToken, bioAuthToken).then((newBioAuthToken) => {
   5. let authToken = newBioAuthToken.authToken as Uint8Array;
   6. });
   ```
7. 参考密钥管理服务提供的[签名/验签指导](huks-signing-signature-verification-arkts.md), 对返回生物特征绑定对应的authToken数据进行签名，并结束会话。
8. 应用可将签名获取的生物特征进行验签校验，并将生物特征credential信息与账号信息在服务器端绑定。
