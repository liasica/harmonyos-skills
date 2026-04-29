---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-soter
title: SOTER免密身份认证
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > SOTER免密身份认证
category: harmonyos-guides
scraped_at: 2026-04-29T13:31:51+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:92e77b4db098ebaeb0c5601914e2d70920f514cead32b1ac1d40e2896a51bb0b
---

## 场景介绍

用户可以利用生物特征来代替传统的密码验证，实现免密身份认证。

* 开通：提供移动端开通SOTER生物特征（指纹/3D人脸）免密身份认证的能力。
* 认证：提供移动端采用生物特征（指纹/3D人脸）进行SOTER免密身份认证的能力。
* 注销：提供移动端注销SOTER生物特征（指纹/3D人脸）免密身份认证的能力。

## 基本概念

SOTER旨在提供一套生物认证平台和标准，使得业务可以采用设备上的传感器（如人脸传感器/指纹传感器）进行安全、高效的免密登录、免密支付等操作，当前已广泛应用于微信小程序/公众号、指纹支付等业务场景。

## 相关权限

* 获取网络权限：ohos.permission.INTERNET。
* 获取振动权限：ohos.permission.VIBRATE。
* 获取生物识别权限：ohos.permission.ACCESS\_BIOMETRIC。

## 约束与限制

* 开发者应用需要部署SOTER服务器。
* 移动端设备需要支持生物特征（指纹/3D人脸），查询当前移动端设备是否支持ATL4级别的认证可信等级。

  ```
  1. import { BusinessError } from '@kit.BasicServicesKit';
  2. import { userAuth } from '@kit.UserAuthenticationKit';

  4. try {
  5. // 示例，查询设备人脸识别是否支持ATL4级别的认证可信等级
  6. userAuth.getAvailableStatus(userAuth.UserAuthType.FACE, userAuth.AuthTrustLevel.ATL4);
  7. console.info('current auth trust level is supported');
  8. } catch (error) {
  9. const err: BusinessError = error as BusinessError;
  10. console.error(`current auth trust level is not supported. Code is ${err?.code}, message is ${err?.message}`);
  11. }
  ```
* 移动端设备使用此服务时需要处于联网状态。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/-cPr2MfzRdKkzMrArjBE3Q/zh-cn_image_0000002558605250.png?HW-CC-KV=V1&HW-CC-Date=20260429T053150Z&HW-CC-Expire=86400&HW-CC-Sign=DA8A29FE12CF32A306509AF8E878D8E24D9AA3B9EB23A505534020228404AB99)

## 接口说明

**表1** 开通、认证、注销的所需要的接口

| 接口名 | 描述 |
| --- | --- |
| [generateAppSecureKey](../harmonyos-references/onlineauthentication-soter-api.md#generateappsecurekey)(keyType: [KeyType](../harmonyos-references/onlineauthentication-soter-api.md#keytype)): Promise<Uint8Array> | 生成应用密钥。 |
| [generateAuthKey](../harmonyos-references/onlineauthentication-soter-api.md#generateauthkey)(keyAlias: string, keyType: [KeyType](../harmonyos-references/onlineauthentication-soter-api.md#keytype)): Promise<[SignedResult](../harmonyos-references/onlineauthentication-soter-api.md#signedresult)> | 生成认证密钥。 |
| [generateChallengeSync](../harmonyos-references/onlineauthentication-soter-api.md#generatechallengesync)(keyAlias: string): Uint8Array | 生成Challenge。 |
| [signWithAuthKeySync](../harmonyos-references/onlineauthentication-soter-api.md#signwithauthkeysync)(keyAlias: string, authToken: Uint8Array, info: string): [SignedResult](../harmonyos-references/onlineauthentication-soter-api.md#signedresult) | 使用认证密钥对业务数据签名。 |
| [deleteAuthKey](../harmonyos-references/onlineauthentication-soter-api.md#deleteauthkey)(keyAlias: string): Promise<void> | 删除认证密钥。 |

## 开发步骤

1. 导入SOTER模块。

   ```
   1. import { soter } from '@kit.OnlineAuthenticationKit';
   2. import { userAuth } from '@kit.UserAuthenticationKit';
   ```
2. 生成应用密钥和认证密钥用于后续的开通、认证流程。

   ```
   1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 加密类型，只支持ECC_P256
   2. let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名

   4. // 生成应用密钥
   5. let appSecureKey: Promise<Uint8Array> = soter.generateAppSecureKey(keyType);
   6. // 生成AuthKey
   7. let authKey: Promise<soter.SignedResult> = soter.generateAuthKey(keyAlias, keyType);
   ```
3. 使用认证密钥签名，实现SOTER免密认证。

   ```
   1. let keyType: soter.KeyType = soter.KeyType.ECC_P256; // 加密类型，只支持ECC_P256
   2. let keyAlias: string = 'keyAlias'; // 开发者自定义密钥别名
   3. let info: string = 'Message to be signed.'; // info需要开发者的三方应用服务器下发，SOTER服务完成签名后需要重新上传给三方应用服务器

   5. // 获取此次免密支付的challenge
   6. let soterChallenge: Uint8Array = soter.generateChallengeSync(keyAlias);
   7. let authParam: userAuth.AuthParam = {
   8. challenge: soterChallenge,
   9. authType: [userAuth.UserAuthType.FINGERPRINT],
   10. authTrustLevel: userAuth.AuthTrustLevel.ATL4,
   11. };
   12. // 使用preAuthResult请求身份认证
   13. let userAuthInstance = userAuth.getUserAuthInstance(authParam,  {title: ' '});
   14. // 未获取到authToken则会返回错误码1。
   15. userAuthInstance.on('result', {
   16. async onResult (result) {
   17. let authToken = result.token;
   18. try {
   19. // 生物特征认证成功后，调用soter认证
   20. console.info('soter auth start');
   21. // 使用soter.signWithAuthKeySync接口为待认证数据签名。开发者根据业务需求选择同步/异步接口。
   22. let authResult: soter.SignedResult = soter.signWithAuthKeySync(keyAlias, authToken, info);
   23. console.info('Succeeded in doing authSyn authResult');
   24. // 开发者处理authResult
   25. } catch (err) {
   26. console.error(`Failed to signWithAuthKeySync. Code: ${err.code}, message: ${err.message}`);
   27. }
   28. }
   29. });
   30. userAuthInstance.start();
   ```
4. 关闭免密认证时，删除认证密钥。

   ```
   1. // 删除AuthKey
   2. soter.deleteAuthKey(keyAlias);
   ```
